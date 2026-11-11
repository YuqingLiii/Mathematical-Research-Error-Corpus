#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <thread>
#include <utility>
#include <vector>

namespace {

constexpr int N = 13;
constexpr int CHOOSE = 10;
constexpr std::array<int, CHOOSE> SLOPES = {
    3, 1, 20, -20, 490, -490, 12090, -12090, 300179, -300179,
};
constexpr int TMIN = -3753347;
constexpr int TMAX = 3753395;
constexpr int TWIDTH = TMAX - TMIN + 1;
constexpr int MAX_FIBER = 480;

struct Term {
    std::int32_t q6 = 0;
    std::int16_t qr = 0;
    bool negative = false;
};

struct PairSlot {
    std::array<Term, 2> term{};
    std::uint8_t filled = 0;
};

struct Record {
    std::int32_t t = 0;
    std::int32_t d6 = 0;
    std::int16_t dr = 0;
    std::int8_t q = 0;
    std::int8_t sigma = 0;
};

struct QResult {
    int deleted = 0;
    int q = 0;
    std::array<std::uint64_t, MAX_FIBER + 1> histogram{};
    int maximum = 0;
    std::uint64_t plus2 = 0;
    std::uint64_t zero = 0;
    std::vector<Record> records;
};

using u128 = unsigned __int128;
using i128 = __int128;

void require(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

std::string to_string_u128(u128 value) {
    if (value == 0) return "0";
    std::string result;
    while (value != 0) {
        result.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    }
    std::reverse(result.begin(), result.end());
    return result;
}

std::string to_string_i128(i128 value) {
    if (value < 0) return "-" + to_string_u128(static_cast<u128>(-value));
    return to_string_u128(static_cast<u128>(value));
}

std::array<int, CHOOSE> complement_rows(int deleted, int x, int y) {
    std::array<int, CHOOSE> rows{};
    int cursor = 0;
    for (int row = 0; row < N; ++row) {
        if (row != deleted && row != x && row != y) rows[cursor++] = row;
    }
    require(cursor == CHOOSE, "bad ten-row complement");
    return rows;
}

bool placement_negative(const std::array<int, CHOOSE>& rows, int x, int y) {
    int inversions = x > y ? 1 : 0;
    for (int row : rows) {
        inversions += row > x ? 1 : 0;
        inversions += row > y ? 1 : 0;
    }
    return (inversions & 1) != 0;
}

void enumerate_counts(
    const std::array<int, CHOOSE>& rows,
    int depth,
    unsigned remaining,
    int t,
    std::vector<std::uint16_t>& counts
) {
    if (depth == CHOOSE - 1) {
        const int position = std::countr_zero(remaining);
        const int value = t + SLOPES[depth] * rows[position];
        std::uint16_t& count = counts[value - TMIN];
        require(count != std::numeric_limits<std::uint16_t>::max(), "fiber overflow");
        ++count;
        return;
    }

    unsigned choices = remaining;
    while (choices != 0) {
        const int position = std::countr_zero(choices);
        const unsigned bit = 1U << position;
        choices &= ~bit;
        enumerate_counts(
            rows,
            depth + 1,
            remaining & ~bit,
            t + SLOPES[depth] * rows[position],
            counts
        );
    }
}

void enumerate_terms(
    const std::array<int, CHOOSE>& rows,
    int depth,
    unsigned remaining,
    int t,
    int q6,
    bool negative,
    bool placement_sign,
    std::int16_t qr,
    const std::vector<std::int32_t>& slot_for_t,
    std::vector<PairSlot>& slots
) {
    if (depth == CHOOSE - 1) {
        const int position = std::countr_zero(remaining);
        const int row = rows[position];
        const int final_t = t + SLOPES[depth] * row;
        const std::int32_t slot_index = slot_for_t[final_t - TMIN];
        if (slot_index >= 0) {
            PairSlot& slot = slots[static_cast<std::size_t>(slot_index)];
            require(slot.filled < 2, "more than two terms in size-two slot");
            slot.term[slot.filled++] = Term{
                q6 + SLOPES[depth] * row * row,
                qr,
                static_cast<bool>(negative ^ placement_sign),
            };
        }
        return;
    }

    unsigned choices = remaining;
    while (choices != 0) {
        const int position = std::countr_zero(choices);
        const unsigned bit = 1U << position;
        choices &= ~bit;
        const int row = rows[position];
        const int rank = std::popcount(remaining & (bit - 1));
        enumerate_terms(
            rows,
            depth + 1,
            remaining & ~bit,
            t + SLOPES[depth] * row,
            q6 + SLOPES[depth] * row * row,
            negative ^ ((rank & 1) != 0),
            placement_sign,
            qr,
            slot_for_t,
            slots
        );
    }
}

QResult compute_q(int deleted, int q) {
    QResult result;
    result.deleted = deleted;
    result.q = q;

    std::vector<std::uint16_t> counts(TWIDTH, 0);
    for (int x = 0; x < N; ++x) {
        const int y = x - q;
        if (y < 0 || y >= N || x == deleted || y == deleted) continue;
        const auto rows = complement_rows(deleted, x, y);
        enumerate_counts(rows, 0, (1U << CHOOSE) - 1, 0, counts);
    }

    std::vector<std::int32_t> slot_for_t(TWIDTH, -1);
    std::size_t size_two_count = 0;
    for (int index = 0; index < TWIDTH; ++index) {
        const int count = counts[index];
        if (count == 0) continue;
        require(count <= MAX_FIBER, "fiber exceeds certified maximum");
        ++result.histogram[count];
        result.maximum = std::max(result.maximum, count);
        if (count == 2) slot_for_t[index] = static_cast<std::int32_t>(size_two_count++);
    }

    std::vector<PairSlot> slots(size_two_count);
    for (int x = 0; x < N; ++x) {
        const int y = x - q;
        if (y < 0 || y >= N || x == deleted || y == deleted) continue;
        const auto rows = complement_rows(deleted, x, y);
        enumerate_terms(
            rows,
            0,
            (1U << CHOOSE) - 1,
            0,
            0,
            false,
            placement_negative(rows, x, y),
            static_cast<std::int16_t>(x * x - y * y),
            slot_for_t,
            slots
        );
    }

    result.records.reserve(size_two_count);
    for (int index = 0; index < TWIDTH; ++index) {
        const std::int32_t slot_index = slot_for_t[index];
        if (slot_index < 0) continue;
        PairSlot& slot = slots[static_cast<std::size_t>(slot_index)];
        require(slot.filled == 2, "size-two slot did not receive exactly two terms");
        Term first = slot.term[0];
        Term second = slot.term[1];
        if (std::pair(first.q6, first.qr) > std::pair(second.q6, second.qr)) {
            std::swap(first, second);
        }
        const int d6 = second.q6 - first.q6;
        const int dr = second.qr - first.qr;
        const int sigma = first.negative == second.negative ? 1 : -1;
        if (d6 == 0 && dr == 0) {
            if (sigma == 1) ++result.plus2;
            else ++result.zero;
            continue;
        }
        require(d6 >= 0, "noncanonical Q6 difference");
        result.records.push_back(Record{
            index + TMIN,
            d6,
            static_cast<std::int16_t>(dr),
            static_cast<std::int8_t>(q),
            static_cast<std::int8_t>(sigma),
        });
    }
    require(result.records.size() + result.plus2 + result.zero == size_two_count,
            "size-two classification mismatch");
    return result;
}

std::uint64_t difference_key(const Record& record) {
    require(record.dr >= -32768 && record.dr <= 32767, "difference out of int16 range");
    const std::uint64_t dr = static_cast<std::uint16_t>(
        static_cast<int>(record.dr) + 32768
    );
    return (static_cast<std::uint64_t>(record.d6) << 16) | dr;
}

struct Totals {
    std::uint64_t records = 0;
    i128 sum_t = 0;
    u128 sum_d6 = 0;
    i128 sum_dr = 0;
    i128 sum_sigma = 0;
    u128 sum_t2 = 0;
    u128 sum_d62 = 0;
    u128 sum_dr2 = 0;
    std::uint64_t plus = 0;
    std::uint64_t minus = 0;
};

void add_record(Totals& totals, const Record& record) {
    ++totals.records;
    totals.sum_t += record.t;
    totals.sum_d6 += static_cast<std::uint64_t>(record.d6);
    totals.sum_dr += record.dr;
    totals.sum_sigma += record.sigma;
    totals.sum_t2 += static_cast<u128>(static_cast<std::int64_t>(record.t) * record.t);
    totals.sum_d62 += static_cast<u128>(static_cast<std::uint64_t>(record.d6) * record.d6);
    totals.sum_dr2 += static_cast<u128>(static_cast<std::int64_t>(record.dr) * record.dr);
    if (record.sigma == 1) ++totals.plus;
    else if (record.sigma == -1) ++totals.minus;
    else throw std::runtime_error("bad sigma");
}

}  // namespace

int main(int argc, char** argv) {
    int requested_threads = std::max(1U, std::thread::hardware_concurrency() / 2);
    if (argc == 3 && std::string(argv[1]) == "--threads") {
        requested_threads = std::max(1, std::atoi(argv[2]));
    } else if (argc != 1) {
        throw std::runtime_error("usage: verify_round54_lowfiber [--threads N]");
    }

    constexpr std::array<std::uint64_t, N> EXPECTED_ONE = {
        2611200, 5487296, 6766012, 7099514, 7595714, 8124302, 7618408,
        8124302, 7595714, 7099514, 6766012, 5487296, 2611200,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_TWO = {
        8170368, 13221080, 15472264, 17577832, 19216316, 20091844, 18913468,
        20091844, 19216316, 17577832, 15472264, 13221080, 8170368,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_THREE = {
        2127360, 3505232, 4554384, 4984594, 5436030, 5747358, 6162308,
        5747358, 5436030, 4984594, 4554384, 3505232, 2127360,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_FOUR = {
        8437248, 11517728, 12835624, 14926928, 15308304, 16651026, 15684232,
        16651026, 15308304, 14926928, 12835624, 11517728, 8437248,
    };
    constexpr std::array<int, N> EXPECTED_MAXIMUM = {
        480, 240, 360, 360, 360, 360, 360,
        360, 360, 360, 360, 240, 480,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_DISTINCT_SIGNED = {
        357170, 922377, 1366982, 1772341, 2141504, 1975040, 1075004,
        1975040, 2141504, 1772341, 1366982, 922377, 357170,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_MATCHED = {
        9020, 39298, 56382, 58032, 37358, 68998, 65744,
        68998, 37358, 58032, 56382, 39298, 9020,
    };
    constexpr std::array<std::uint64_t, N> SUPPORT = {
        53624480, 67257904, 74299020, 80378492, 82204810, 85479020, 83844096,
        85479020, 82204810, 80378492, 74299020, 67257904, 53624480,
    };
    constexpr std::array<std::uint64_t, N> BUDGET = {
        39258, 31300, 28334, 26192, 25610, 24628, 25108,
        24628, 25610, 26192, 28334, 31300, 39258,
    };

    Totals global;
    std::array<std::uint64_t, MAX_FIBER + 1> global_histogram{};
    std::uint64_t global_plus2 = 0;
    std::uint64_t global_zero = 0;
    std::uint64_t matched_sum = 0;
    u128 weighted_surviving = 0;
    int d6_min = std::numeric_limits<int>::max();
    int d6_max = std::numeric_limits<int>::min();
    int dr_min = std::numeric_limits<int>::max();
    int dr_max = std::numeric_limits<int>::min();

    std::vector<int> q_values;
    for (int q = -12; q <= 12; ++q) if (q != 0) q_values.push_back(q);

    for (int deleted = 0; deleted < N; ++deleted) {
        std::vector<QResult> results(q_values.size());
        std::atomic<std::size_t> next{0};
        const int thread_count = std::min<int>(requested_threads, q_values.size());
        std::vector<std::thread> threads;
        for (int worker = 0; worker < thread_count; ++worker) {
            threads.emplace_back([&] {
                for (;;) {
                    const std::size_t index = next.fetch_add(1);
                    if (index >= q_values.size()) break;
                    results[index] = compute_q(deleted, q_values[index]);
                }
            });
        }
        for (auto& thread : threads) thread.join();

        std::array<std::uint64_t, MAX_FIBER + 1> row_histogram{};
        std::uint64_t row_plus2 = 0;
        std::uint64_t row_zero = 0;
        std::uint64_t row_records = 0;
        int row_maximum = 0;
        std::vector<std::uint64_t> signed_keys;

        for (std::size_t q_index = 0; q_index < results.size(); ++q_index) {
            const QResult& result = results[q_index];
            require(result.deleted == deleted && result.q == q_values[q_index],
                    "task result ordering mismatch");
            for (int size = 1; size <= MAX_FIBER; ++size) {
                row_histogram[size] += result.histogram[size];
                global_histogram[size] += result.histogram[size];
            }
            row_maximum = std::max(row_maximum, result.maximum);
            row_plus2 += result.plus2;
            row_zero += result.zero;
            row_records += result.records.size();
            signed_keys.reserve(signed_keys.size() + result.records.size());

            int last_t = std::numeric_limits<int>::min();
            for (const Record& record : result.records) {
                require(record.q == result.q, "record q mismatch");
                require(record.t > last_t, "records are not strictly t-sorted");
                last_t = record.t;
                add_record(global, record);
                d6_min = std::min(d6_min, record.d6);
                d6_max = std::max(d6_max, record.d6);
                dr_min = std::min(dr_min, static_cast<int>(record.dr));
                dr_max = std::max(dr_max, static_cast<int>(record.dr));
                signed_keys.push_back((difference_key(record) << 1) | (record.sigma < 0));
            }
        }

        require(row_histogram[1] == EXPECTED_ONE[deleted], "size-one count mismatch");
        require(row_histogram[2] == EXPECTED_TWO[deleted], "size-two count mismatch");
        require(row_histogram[3] == EXPECTED_THREE[deleted], "size-three count mismatch");
        require(row_histogram[4] == EXPECTED_FOUR[deleted], "size-four count mismatch");
        require(row_maximum == EXPECTED_MAXIMUM[deleted], "maximum fiber mismatch");
        require(row_records == EXPECTED_TWO[deleted], "genuine-binomial count mismatch");
        require(row_plus2 == 0, "a size-two fiber collected to a +/-2 monomial");
        require(row_zero == 0, "a size-two fiber collected to zero");

        std::sort(signed_keys.begin(), signed_keys.end());
        std::uint64_t distinct_base = 0;
        std::uint64_t distinct_signed = 0;
        std::uint64_t matched = 0;
        std::size_t cursor = 0;
        while (cursor < signed_keys.size()) {
            ++distinct_base;
            const std::uint64_t base = signed_keys[cursor] >> 1;
            std::uint64_t plus = 0;
            std::uint64_t minus = 0;
            while (cursor < signed_keys.size() && (signed_keys[cursor] >> 1) == base) {
                const bool negative_sigma = (signed_keys[cursor] & 1) != 0;
                std::uint64_t count = 0;
                const std::uint64_t exact = signed_keys[cursor];
                while (cursor < signed_keys.size() && signed_keys[cursor] == exact) {
                    ++cursor;
                    ++count;
                }
                ++distinct_signed;
                if (negative_sigma) minus = count;
                else plus = count;
            }
            matched += std::min(plus, minus);
        }
        require(distinct_base == EXPECTED_DISTINCT_SIGNED[deleted],
                "distinct exponent-difference count mismatch");
        require(matched == EXPECTED_MATCHED[deleted], "opposite-sign match count mismatch");
        matched_sum += matched;
        weighted_surviving += static_cast<u128>(SUPPORT[deleted]) *
                              static_cast<u128>(
                                  matched > BUDGET[deleted] ? matched - BUDGET[deleted] : 0
                              );
        global_plus2 += row_plus2;
        global_zero += row_zero;

        std::cout << "deleted=" << deleted
                  << " size1=" << row_histogram[1]
                  << " size2=" << row_histogram[2]
                  << " size3=" << row_histogram[3]
                  << " size4=" << row_histogram[4]
                  << " maximum=" << row_maximum
                  << " distinct_base=" << distinct_base
                  << " distinct_signed=" << distinct_signed
                  << " matched=" << matched
                  << " surviving="
                  << (matched > BUDGET[deleted] ? matched - BUDGET[deleted] : 0)
                  << "\n";
    }

    int occupied_sizes = 0;
    for (int size = 1; size <= MAX_FIBER; ++size) {
        if (global_histogram[size] != 0) ++occupied_sizes;
    }

    require(global_histogram[1] == 82'986'484ULL, "global size-one count mismatch");
    require(global_histogram[2] == 206'412'876ULL, "global size-two count mismatch");
    require(global_histogram[3] == 58'872'224ULL, "global size-three count mismatch");
    require(global_histogram[4] == 175'037'948ULL, "global size-four count mismatch");
    require(occupied_sizes == 91, "occupied-size count mismatch");
    require(global_plus2 == 0 && global_zero == 0, "global size-two collection mismatch");
    require(global.records == 206'412'876ULL, "record checksum mismatch");
    require(global.plus == 171'603'784ULL, "plus-sign checksum mismatch");
    require(global.minus == 34'809'092ULL, "minus-sign checksum mismatch");
    require(global.sum_t == static_cast<i128>(4'953'909'024LL), "sum(t) mismatch");
    require(global.sum_d6 == static_cast<u128>(751'418'613'554'112ULL), "sum(d6) mismatch");
    require(global.sum_dr == static_cast<i128>(3'333'280), "sum(dr) mismatch");
    require(global.sum_sigma == static_cast<i128>(136'794'692), "sum(sigma) mismatch");
    require(to_string_u128(global.sum_t2) == "879344995479279201900", "sum(t^2) mismatch");
    require(to_string_u128(global.sum_d62) == "7182382339465020225280", "sum(d6^2) mismatch");
    require(to_string_u128(global.sum_dr2) == "79579910944", "sum(dr^2) mismatch");
    require(matched_sum == 603'920ULL, "global match count mismatch");
    require(to_string_u128(weighted_surviving) == "23286218764480",
            "weighted surviving-pair checksum mismatch");
    require(d6_min == 0 && d6_max == 22'475'252, "d6 extrema mismatch");
    require(dr_min == -72 && dr_max == 72, "dr extrema mismatch");

    constexpr std::uint64_t K = 970'331'548ULL;
    constexpr std::uint64_t H = 1'074ULL;
    const u128 comparison = static_cast<u128>(64) * weighted_surviving
                          - static_cast<u128>(486) * H * K;
    require(to_string_u128(comparison) == "983839864806448",
            "final rational comparison mismatch");

    std::cout << "occupied_sizes=" << occupied_sizes << "\n";
    std::cout << "records=" << global.records << "\n";
    std::cout << "plus=" << global.plus << " minus=" << global.minus << "\n";
    std::cout << "matched=" << matched_sum << "\n";
    std::cout << "d6_range=" << d6_min << "," << d6_max << "\n";
    std::cout << "dr_range=" << dr_min << "," << dr_max << "\n";
    std::cout << "sum_t=" << to_string_i128(global.sum_t) << "\n";
    std::cout << "sum_d6=" << to_string_u128(global.sum_d6) << "\n";
    std::cout << "sum_dr=" << to_string_i128(global.sum_dr) << "\n";
    std::cout << "sum_sigma=" << to_string_i128(global.sum_sigma) << "\n";
    std::cout << "sum_t2=" << to_string_u128(global.sum_t2) << "\n";
    std::cout << "sum_d62=" << to_string_u128(global.sum_d62) << "\n";
    std::cout << "sum_dr2=" << to_string_u128(global.sum_dr2) << "\n";
    std::cout << "weighted_surviving=" << to_string_u128(weighted_surviving) << "\n";
    std::cout << "comparison=" << to_string_u128(comparison) << "\n";
    std::cout << "round55 low-fiber census: PASS\n";
}
