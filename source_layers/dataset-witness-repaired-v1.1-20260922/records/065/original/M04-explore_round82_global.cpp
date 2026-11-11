#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <numeric>
#include <random>
#include <stdexcept>
#include <string>
#include <thread>
#include <utility>
#include <vector>

namespace {

constexpr int N = 13;
constexpr int CHOOSE = 10;
constexpr std::array<int, CHOOSE> SLOPES = {
    3, 1, 20, -20, 490, -490, 12090, -12090, 300219, -300219,
};
constexpr int TMIN = -3753400;
constexpr int TMAX = 3753450;
constexpr int TWIDTH = TMAX - TMIN + 1;
constexpr int MAX_FIBER = 480;
constexpr bool VERIFY_ROUND58_EXPECTATIONS = false;

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

struct KeyCounts {
    std::uint64_t base = 0;
    std::uint64_t plus = 0;
    std::uint64_t minus = 0;
};

struct MixedKeyProfile {
    std::uint64_t base = 0;
    std::array<std::uint64_t, N> plus{};
    std::array<std::uint64_t, N> minus{};
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
        throw std::runtime_error("usage: verify_round58_lowfiber [--threads N]");
    }

    constexpr std::array<std::uint64_t, N> EXPECTED_ONE = {
        2611200, 5487296, 6765992, 7099598, 7596018, 8124580, 7618740,
        8124580, 7596018, 7099598, 6765992, 5487296, 2611200,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_TWO = {
        8170368, 13221080, 15472420, 17578010, 19216372, 20092120, 18913704,
        20092120, 19216372, 17578010, 15472420, 13221080, 8170368,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_THREE = {
        2127360, 3505232, 4554436, 4984486, 5436016, 5747266, 6162284,
        5747266, 5436016, 4984486, 4554436, 3505232, 2127360,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_FOUR = {
        8437248, 11517728, 12835600, 14926940, 15308330, 16650972, 15684144,
        16650972, 15308330, 14926940, 12835600, 11517728, 8437248,
    };
    constexpr std::array<int, N> EXPECTED_MAXIMUM = {
        480, 240, 360, 360, 360, 360, 360,
        360, 360, 360, 360, 240, 480,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_MATCHED = {
        9084, 39388, 56644, 58044, 37500, 69164, 66180,
        69164, 37500, 58044, 56644, 39388, 9084,
    };
    constexpr std::array<std::uint64_t, N> SUPPORT = {
        53624480, 67257904, 74298900, 80378416, 82204926, 85479258, 83844372,
        85479258, 82204926, 80378416, 74298900, 67257904, 53624480,
    };
    constexpr std::array<std::uint64_t, N> BUDGET = {
        266366, 212372, 192246, 177704, 173756, 167100, 170358,
        167100, 173756, 177704, 192246, 212372, 266366,
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
    std::array<std::vector<KeyCounts>, N> row_key_counts;

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

        require(row_records == row_histogram[2], "genuine-binomial count mismatch");
        require(row_plus2 == 0, "a size-two fiber collected to a +/-2 monomial");
        require(row_zero == 0, "a size-two fiber collected to zero");
        if (VERIFY_ROUND58_EXPECTATIONS) {
            require(row_histogram[1] == EXPECTED_ONE[deleted], "size-one count mismatch");
            require(row_histogram[2] == EXPECTED_TWO[deleted], "size-two count mismatch");
            require(row_histogram[3] == EXPECTED_THREE[deleted], "size-three count mismatch");
            require(row_histogram[4] == EXPECTED_FOUR[deleted], "size-four count mismatch");
            require(row_maximum == EXPECTED_MAXIMUM[deleted], "maximum fiber-size mismatch");
        }

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
            row_key_counts[deleted].push_back(KeyCounts{base, plus, minus});
            matched += std::min(plus, minus);
        }
        if (VERIFY_ROUND58_EXPECTATIONS) {
            require(matched == EXPECTED_MATCHED[deleted], "opposite-sign match mismatch");
        }
        const std::uint64_t row_support = std::accumulate(
            row_histogram.begin(), row_histogram.end(), std::uint64_t{0}
        );
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
                  << " support=" << row_support
                  << " maximum=" << row_maximum
                  << " distinct_base=" << distinct_base
                  << " distinct_signed=" << distinct_signed
                  << " matched=" << matched
                  << " surviving="
                  << (matched > BUDGET[deleted] ? matched - BUDGET[deleted] : 0)
                  << "\n";
    }

    std::array<std::size_t, N> key_cursor{};
    std::uint64_t global_key_count = 0;
    std::uint64_t global_both_signs = 0;
    std::uint64_t global_matched = 0;
    std::uint64_t global_maximum_match = 0;
    u128 global_key_checksum = 0;
    u128 global_count_checksum = 0;
    std::array<std::uint64_t, N> example_plus{};
    std::array<std::uint64_t, N> example_minus{};
    std::array<std::uint64_t, N> minority_kill_by_row{};
    std::vector<MixedKeyProfile> mixed_profiles;
    const std::uint64_t example_base =
        (static_cast<std::uint64_t>(2401604) << 16) | static_cast<std::uint16_t>(32768);

    for (;;) {
        bool have_key = false;
        std::uint64_t base = 0;
        for (int row = 0; row < N; ++row) {
            if (key_cursor[row] == row_key_counts[row].size()) continue;
            const std::uint64_t candidate = row_key_counts[row][key_cursor[row]].base;
            if (!have_key || candidate < base) {
                have_key = true;
                base = candidate;
            }
        }
        if (!have_key) break;

        std::uint64_t plus = 0;
        std::uint64_t minus = 0;
        std::array<std::uint64_t, N> key_plus_by_row{};
        std::array<std::uint64_t, N> key_minus_by_row{};
        for (int row = 0; row < N; ++row) {
            if (key_cursor[row] == row_key_counts[row].size()) continue;
            const KeyCounts& counts = row_key_counts[row][key_cursor[row]];
            if (counts.base != base) continue;
            plus += counts.plus;
            minus += counts.minus;
            key_plus_by_row[row] = counts.plus;
            key_minus_by_row[row] = counts.minus;
            if (base == example_base) {
                example_plus[row] = counts.plus;
                example_minus[row] = counts.minus;
            }
            ++key_cursor[row];
        }

        ++global_key_count;
        const std::uint64_t matched = std::min(plus, minus);
        global_matched += matched;
        const bool kill_plus = plus <= minus;
        for (int row = 0; row < N; ++row) {
            minority_kill_by_row[row] +=
                kill_plus ? key_plus_by_row[row] : key_minus_by_row[row];
        }
        if (matched != 0) {
            ++global_both_signs;
            global_maximum_match = std::max(global_maximum_match, matched);
            mixed_profiles.push_back(MixedKeyProfile{
                base,
                key_plus_by_row,
                key_minus_by_row,
            });
        }
        global_key_checksum += static_cast<u128>(global_key_count) * base;
        global_count_checksum += static_cast<u128>(global_key_count) *
                                 (static_cast<u128>(3) * plus +
                                  static_cast<u128>(5) * minus);
    }

    if (VERIFY_ROUND58_EXPECTATIONS) {
        require(global_key_count == 7999142, "global difference-key count mismatch");
        require(global.plus == 171605268, "global plus-sign count mismatch");
        require(global.minus == 34809176, "global minus-sign count mismatch");
        require(global_both_signs == 177236, "global both-sign key count mismatch");
        require(global_matched == 1290408, "global cross-row match mismatch");
        require(global_maximum_match == 1152, "global maximum per-key match mismatch");
        require(example_plus == std::array<std::uint64_t, N>{
                    0, 0, 192, 96, 0, 288, 0, 288, 0, 96, 192, 0, 0},
                "example plus-row distribution mismatch");
        require(example_minus == std::array<std::uint64_t, N>{
                    0, 0, 0, 0, 480, 192, 0, 192, 480, 0, 0, 0, 0},
                "example minus-row distribution mismatch");
    }

    const std::uint64_t bad_budget =
        std::accumulate(BUDGET.begin(), BUDGET.end(), std::uint64_t{0});
    const std::uint64_t minority_kill_total =
        std::accumulate(
            minority_kill_by_row.begin(),
            minority_kill_by_row.end(),
            std::uint64_t{0}
        );
    require(minority_kill_total == global_matched,
            "minority-side deletion witness total mismatch");
    bool minority_witness_fits_budget = true;
    for (int row = 0; row < N; ++row) {
        minority_witness_fits_budget =
            minority_witness_fits_budget &&
            minority_kill_by_row[row] <= BUDGET[row];
    }

    std::vector<std::size_t> order(mixed_profiles.size());
    std::iota(order.begin(), order.end(), std::size_t{0});
    std::vector<std::uint8_t> best_choice(mixed_profiles.size(), 0);
    std::array<std::uint64_t, N> best_load{};
    std::uint64_t best_total_excess = std::numeric_limits<std::uint64_t>::max();
    std::uint64_t best_max_excess = std::numeric_limits<std::uint64_t>::max();
    bool balanced_witness_fits_budget = false;
    std::mt19937_64 generator(0x300219ULL);

    for (int trial = 0; trial < 128; ++trial) {
        if (trial != 0) std::shuffle(order.begin(), order.end(), generator);
        std::array<std::uint64_t, N> load{};
        std::vector<std::uint8_t> choice(mixed_profiles.size(), 0);
        for (std::size_t position : order) {
            const MixedKeyProfile& profile = mixed_profiles[position];
            long double plus_score = 0;
            long double minus_score = 0;
            bool plus_fits = true;
            bool minus_fits = true;
            for (int row = 0; row < N; ++row) {
                const long double budget = static_cast<long double>(BUDGET[row]);
                const long double plus_ratio =
                    static_cast<long double>(load[row] + profile.plus[row]) / budget;
                const long double minus_ratio =
                    static_cast<long double>(load[row] + profile.minus[row]) / budget;
                plus_score += plus_ratio * plus_ratio;
                minus_score += minus_ratio * minus_ratio;
                plus_fits = plus_fits &&
                            load[row] + profile.plus[row] <= BUDGET[row];
                minus_fits = minus_fits &&
                             load[row] + profile.minus[row] <= BUDGET[row];
            }
            bool kill_plus = false;
            if (plus_fits != minus_fits) {
                kill_plus = plus_fits;
            } else if (plus_score != minus_score) {
                kill_plus = plus_score < minus_score;
            } else {
                const std::uint64_t plus_total =
                    std::accumulate(profile.plus.begin(), profile.plus.end(),
                                    std::uint64_t{0});
                const std::uint64_t minus_total =
                    std::accumulate(profile.minus.begin(), profile.minus.end(),
                                    std::uint64_t{0});
                kill_plus = plus_total <= minus_total;
            }
            choice[position] = kill_plus ? 1 : 0;
            for (int row = 0; row < N; ++row) {
                load[row] +=
                    kill_plus ? profile.plus[row] : profile.minus[row];
            }
        }

        std::uint64_t total_excess = 0;
        std::uint64_t max_excess = 0;
        for (int row = 0; row < N; ++row) {
            const std::uint64_t excess =
                load[row] > BUDGET[row] ? load[row] - BUDGET[row] : 0;
            total_excess += excess;
            max_excess = std::max(max_excess, excess);
        }
        if (std::pair(total_excess, max_excess) <
            std::pair(best_total_excess, best_max_excess)) {
            best_total_excess = total_excess;
            best_max_excess = max_excess;
            best_load = load;
            best_choice = std::move(choice);
        }
        if (total_excess == 0) {
            balanced_witness_fits_budget = true;
            break;
        }
    }

    u128 balanced_choice_checksum = 0;
    std::uint64_t balanced_kill_total = 0;
    for (std::size_t index = 0; index < mixed_profiles.size(); ++index) {
        const MixedKeyProfile& profile = mixed_profiles[index];
        const bool kill_plus = best_choice[index] != 0;
        const std::uint64_t chosen_total = std::accumulate(
            kill_plus ? profile.plus.begin() : profile.minus.begin(),
            kill_plus ? profile.plus.end() : profile.minus.end(),
            std::uint64_t{0}
        );
        balanced_kill_total += chosen_total;
        balanced_choice_checksum +=
            static_cast<u128>(index + 1) *
            (static_cast<u128>(2) * profile.base + (kill_plus ? 0 : 1));
    }
    const std::uint64_t surviving_packets =
        global_matched > bad_budget ? global_matched - bad_budget : 0;
    const std::uint64_t surviving_anchors =
        global_histogram[1] - bad_budget;
    const i128 cleared_margin =
        static_cast<i128>(35) * surviving_anchors * surviving_packets -
        static_cast<i128>(7190) * 102 *
            (surviving_anchors + static_cast<std::uint64_t>(4) * surviving_packets);

    int best_symmetric_mask = 0;
    std::uint64_t best_subset_matched = 0;
    std::uint64_t best_subset_budget = 0;
    std::uint64_t best_subset_packets = 0;
    i128 best_subset_margin = std::numeric_limits<std::int64_t>::min();
    for (int mask = 1; mask < (1 << 7); ++mask) {
        std::uint64_t subset_budget = 0;
        for (int row = 0; row < N; ++row) {
            if ((mask & (1 << std::abs(row - 6))) != 0) {
                subset_budget += BUDGET[row];
            }
        }
        std::uint64_t subset_matched = 0;
        for (const MixedKeyProfile& profile : mixed_profiles) {
            std::uint64_t plus = 0;
            std::uint64_t minus = 0;
            for (int row = 0; row < N; ++row) {
                if ((mask & (1 << std::abs(row - 6))) == 0) continue;
                plus += profile.plus[row];
                minus += profile.minus[row];
            }
            subset_matched += std::min(plus, minus);
        }
        const std::uint64_t subset_packets =
            subset_matched > subset_budget ? subset_matched - subset_budget : 0;
        const i128 subset_margin =
            static_cast<i128>(35) * surviving_anchors * subset_packets -
            static_cast<i128>(7190) * 102 *
                (surviving_anchors + static_cast<std::uint64_t>(4) * subset_packets);
        if (subset_margin > best_subset_margin) {
            best_symmetric_mask = mask;
            best_subset_matched = subset_matched;
            best_subset_budget = subset_budget;
            best_subset_packets = subset_packets;
            best_subset_margin = subset_margin;
        }
    }
    std::uint64_t best_subset_both_signs = 0;
    std::uint64_t best_subset_maximum_match = 0;
    u128 best_subset_match_checksum = 0;
    for (std::size_t index = 0; index < mixed_profiles.size(); ++index) {
        const MixedKeyProfile& profile = mixed_profiles[index];
        std::uint64_t plus = 0;
        std::uint64_t minus = 0;
        for (int row = 0; row < N; ++row) {
            if ((best_symmetric_mask & (1 << std::abs(row - 6))) == 0) continue;
            plus += profile.plus[row];
            minus += profile.minus[row];
        }
        const std::uint64_t matched = std::min(plus, minus);
        if (matched != 0) {
            ++best_subset_both_signs;
            best_subset_maximum_match =
                std::max(best_subset_maximum_match, matched);
        }
        best_subset_match_checksum +=
            static_cast<u128>(index + 1) *
            (static_cast<u128>(2) * profile.base + 1) * matched;
    }

    if (VERIFY_ROUND58_EXPECTATIONS) {
        require(bad_budget == 1144944, "global bad-coordinate budget mismatch");
        require(surviving_packets == 145464, "surviving packet count mismatch");
        require(surviving_anchors == 81843164, "surviving anchor count mismatch");
        require(cleared_margin == static_cast<i128>(389325666745200ULL),
                "cleared comparison mismatch");
    }

    int occupied_sizes = 0;
    for (int size = 1; size <= MAX_FIBER; ++size) {
        if (global_histogram[size] != 0) ++occupied_sizes;
    }

    require(global_plus2 == 0 && global_zero == 0, "global size-two collection mismatch");
    if (VERIFY_ROUND58_EXPECTATIONS) {
        require(global.records == 206414444, "global size-two record mismatch");
        require(matched_sum == 605828, "global opposite-sign match mismatch");
        require(global.sum_t == static_cast<i128>(4953946656LL), "sum_t mismatch");
        require(global.sum_d6 == static_cast<u128>(751437057188672ULL), "sum_d6 mismatch");
        require(global.sum_dr == static_cast<i128>(3332976), "sum_dr mismatch");
        require(global.sum_sigma == static_cast<i128>(136796092), "sum_sigma mismatch");
        require(global.sum_t2 == static_cast<u128>(879381258751814153ULL) * 1000ULL + 744ULL,
                "sum_t2 mismatch");
        require(global.sum_d62 == static_cast<u128>(7182685321895457821ULL) * 1000ULL + 152ULL,
                "sum_d62 mismatch");
        require(global.sum_dr2 == static_cast<u128>(79580045136ULL), "sum_dr2 mismatch");
        require(weighted_surviving == static_cast<u128>(0),
                "weighted surviving mismatch");
    }
    const u128 comparison = weighted_surviving;

    std::cout << "occupied_sizes=" << occupied_sizes << "\n";
    std::cout << "records=" << global.records << "\n";
    std::cout << "plus=" << global.plus << " minus=" << global.minus << "\n";
    std::cout << "matched=" << matched_sum << "\n";
    std::cout << "global_keys=" << global_key_count << "\n";
    std::cout << "global_both_signs=" << global_both_signs << "\n";
    std::cout << "global_matched=" << global_matched << "\n";
    std::cout << "global_maximum_match=" << global_maximum_match << "\n";
    std::cout << "global_key_checksum=" << to_string_u128(global_key_checksum) << "\n";
    std::cout << "global_count_checksum=" << to_string_u128(global_count_checksum) << "\n";
    std::cout << "minority_kill_by_row=";
    for (int row = 0; row < N; ++row) {
        if (row != 0) std::cout << ",";
        std::cout << minority_kill_by_row[row];
    }
    std::cout << "\n";
    std::cout << "minority_kill_total=" << minority_kill_total << "\n";
    std::cout << "minority_witness_fits_budget="
              << (minority_witness_fits_budget ? "true" : "false") << "\n";
    std::cout << "balanced_kill_by_row=";
    for (int row = 0; row < N; ++row) {
        if (row != 0) std::cout << ",";
        std::cout << best_load[row];
    }
    std::cout << "\n";
    std::cout << "balanced_kill_total=" << balanced_kill_total << "\n";
    std::cout << "balanced_total_excess=" << best_total_excess << "\n";
    std::cout << "balanced_max_excess=" << best_max_excess << "\n";
    std::cout << "balanced_choice_checksum="
              << to_string_u128(balanced_choice_checksum) << "\n";
    std::cout << "balanced_witness_fits_budget="
              << (balanced_witness_fits_budget ? "true" : "false") << "\n";
    std::cout << "bad_budget=" << bad_budget << "\n";
    std::cout << "surviving_packets=" << surviving_packets << "\n";
    std::cout << "surviving_anchors=" << surviving_anchors << "\n";
    std::cout << "cleared_margin=" << to_string_i128(cleared_margin) << "\n";
    std::cout << "best_symmetric_mask=" << best_symmetric_mask << "\n";
    std::cout << "best_symmetric_rows=";
    {
        bool first = true;
        for (int row = 0; row < N; ++row) {
            if ((best_symmetric_mask & (1 << std::abs(row - 6))) == 0) continue;
            if (!first) std::cout << ",";
            first = false;
            std::cout << row;
        }
    }
    std::cout << "\n";
    std::cout << "best_subset_matched=" << best_subset_matched << "\n";
    std::cout << "best_subset_budget=" << best_subset_budget << "\n";
    std::cout << "best_subset_packets=" << best_subset_packets << "\n";
    std::cout << "best_subset_margin=" << to_string_i128(best_subset_margin) << "\n";
    std::cout << "best_subset_both_signs=" << best_subset_both_signs << "\n";
    std::cout << "best_subset_maximum_match="
              << best_subset_maximum_match << "\n";
    std::cout << "best_subset_match_checksum="
              << to_string_u128(best_subset_match_checksum) << "\n";
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
    std::cout << "round82 exploratory global cross-row census: COMPLETE\n";
}
