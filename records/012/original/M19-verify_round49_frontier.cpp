#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <future>
#include <iostream>
#include <numeric>
#include <set>
#include <stdexcept>
#include <tuple>
#include <vector>

namespace {

constexpr int N = 13;
constexpr int FULL = (1 << N) - 1;
constexpr int BMIN = -239;
constexpr int BMAX = 287;
constexpr int BWIDTH = BMAX - BMIN + 1;
constexpr int BWORDS = (BWIDTH + 63) / 64;
constexpr int PCODES = 1 << 12;
constexpr int DSHIFT = 12;
constexpr int MAX_LAMBDA = 526;
constexpr int DEST_BITS = 14080;
constexpr int DEST_WORDS = DEST_BITS / 64;
constexpr int OFFSET = 7000;
constexpr std::int64_t TARGET = 970330473;
constexpr std::int64_t SATURATED = 974917184;

using SmallBits = std::array<std::uint64_t, BWORDS>;
using DifferenceBits = std::array<SmallBits, 25>;
using PatternTable = std::vector<DifferenceBits>;

std::array<std::vector<std::uint16_t>, 1 << N> match_cache;
std::array<bool, 1 << N> match_ready{};

std::uint16_t add_difference(std::uint16_t code, int difference) {
    std::array<int, 3> values{};
    int size = 0;
    for (int shift = 0; shift < 12; shift += 4) {
        int value = (code >> shift) & 15;
        if (value != 0) {
            values[size++] = value;
        }
    }
    values[size++] = difference;
    std::sort(values.begin(), values.begin() + size);
    std::uint16_t result = 0;
    for (int index = 0; index < size; ++index) {
        result |= static_cast<std::uint16_t>(values[index] << (4 * index));
    }
    return result;
}

const std::vector<std::uint16_t>& matching_patterns(int mask) {
    if (match_ready[mask]) {
        return match_cache[mask];
    }
    match_ready[mask] = true;
    auto& result = match_cache[mask];
    if (mask == 0) {
        result.push_back(0);
        return result;
    }
    int first = std::countr_zero(static_cast<unsigned>(mask));
    int rest = mask & ~(1 << first);
    for (int partner = first + 1; partner < N; ++partner) {
        if ((rest & (1 << partner)) == 0) {
            continue;
        }
        int smaller = rest & ~(1 << partner);
        for (std::uint16_t code : matching_patterns(smaller)) {
            result.push_back(add_difference(code, partner - first));
        }
    }
    std::sort(result.begin(), result.end());
    result.erase(std::unique(result.begin(), result.end()), result.end());
    return result;
}

int pattern_weight(std::uint16_t code) {
    std::array<int, 3> values{};
    for (int index = 0; index < 3; ++index) {
        values[index] = (code >> (4 * index)) & 15;
        if (values[index] == 0) {
            throw std::runtime_error("three-edge pattern has a zero nibble");
        }
    }
    int denominator = 1;
    if (values[0] == values[1] && values[1] == values[2]) {
        denominator = 6;
    } else if (values[0] == values[1] || values[1] == values[2]) {
        denominator = 2;
    }
    return 48 / denominator;
}

struct DeletedResult {
    std::array<std::int64_t, MAX_LAMBDA + 1> support{};
    std::array<std::int64_t, MAX_LAMBDA + 1> classes{};
};

DeletedResult compute_deleted(int deleted) {
    PatternTable table(PCODES);
    std::array<bool, PCODES> active{};

    for (int u = 0; u < N; ++u) {
        if (u == deleted) continue;
        for (int v = 0; v < N; ++v) {
            if (v == deleted || v == u) continue;
            for (int a = 0; a < N; ++a) {
                if (a == deleted || a == u || a == v) continue;
                for (int b = 0; b < N; ++b) {
                    if (b == deleted || b == u || b == v || b == a) continue;
                    int base = 3 * u + v + 20 * (a - b);
                    if (base < BMIN || base > BMAX) {
                        throw std::runtime_error("base outside certified range");
                    }
                    for (int c = 0; c < N; ++c) {
                        if (c == deleted || c == u || c == v || c == a || c == b) continue;
                        for (int d = 0; d < N; ++d) {
                            if (d == deleted || d == u || d == v || d == a || d == b || d == c) continue;
                            int difference = c - d;
                            int remaining = FULL;
                            remaining &= ~(1 << deleted);
                            remaining &= ~(1 << u);
                            remaining &= ~(1 << v);
                            remaining &= ~(1 << a);
                            remaining &= ~(1 << b);
                            remaining &= ~(1 << c);
                            remaining &= ~(1 << d);
                            int bit = base - BMIN;
                            for (std::uint16_t code : matching_patterns(remaining)) {
                                table[code][difference + DSHIFT][bit / 64] |=
                                    std::uint64_t{1} << (bit % 64);
                                active[code] = true;
                            }
                        }
                    }
                }
            }
        }
    }

    DeletedResult result;
    for (int lambda = 1; lambda <= MAX_LAMBDA; ++lambda) {
        for (int code = 1; code < PCODES; ++code) {
            if (!active[code]) continue;
            std::array<std::uint64_t, DEST_WORDS> joined{};
            for (int difference = -12; difference <= 12; ++difference) {
                if (difference == 0) continue;
                const auto& source = table[code][difference + DSHIFT];
                int start = OFFSET + lambda * difference + BMIN;
                if (start < 0 || start + BWIDTH >= DEST_BITS) {
                    throw std::runtime_error("destination bit range too small");
                }
                int word_offset = start / 64;
                int shift = start % 64;
                for (int word = 0; word < BWORDS; ++word) {
                    std::uint64_t value = source[word];
                    if (value == 0) continue;
                    joined[word_offset + word] |= value << shift;
                    if (shift != 0) {
                        joined[word_offset + word + 1] |= value >> (64 - shift);
                    }
                }
            }
            std::int64_t distinct = 0;
            for (std::uint64_t word : joined) {
                distinct += std::popcount(word);
            }
            result.classes[lambda] += distinct;
            result.support[lambda] += distinct * pattern_weight(code);
        }
    }
    return result;
}

}  // namespace

int main() {
    for (int mask = 0; mask <= FULL; ++mask) {
        if (std::popcount(static_cast<unsigned>(mask)) <= 6 &&
            std::popcount(static_cast<unsigned>(mask)) % 2 == 0) {
            matching_patterns(mask);
        }
    }

    std::vector<std::future<DeletedResult>> futures;
    for (int deleted = 0; deleted < N; ++deleted) {
        futures.push_back(std::async(std::launch::async, compute_deleted, deleted));
    }

    std::array<std::int64_t, MAX_LAMBDA + 1> totals{};
    std::array<std::int64_t, MAX_LAMBDA + 1> class_totals{};
    std::array<std::int64_t, N> rows_204{};
    std::array<std::int64_t, N> rows_490{};
    for (int deleted = 0; deleted < N; ++deleted) {
        DeletedResult row = futures[deleted].get();
        rows_204[deleted] = row.support[204];
        rows_490[deleted] = row.support[490];
        for (int lambda = 1; lambda <= MAX_LAMBDA; ++lambda) {
            totals[lambda] += row.support[lambda];
            class_totals[lambda] += row.classes[lambda];
        }
    }

    std::int64_t checksum0 = 0;
    std::int64_t checksum1 = 0;
    std::int64_t checksum2 = 0;
    std::vector<int> passing;
    int last_nonstabilized = 0;
    int closest_passing = 0;
    std::int64_t closest_margin = TARGET + 1;
    for (int lambda = 1; lambda <= MAX_LAMBDA; ++lambda) {
        checksum0 += totals[lambda];
        checksum1 += static_cast<std::int64_t>(lambda) * totals[lambda];
        checksum2 += static_cast<std::int64_t>(lambda) * lambda * totals[lambda];
        if (totals[lambda] <= TARGET + 1) {
            passing.push_back(lambda);
            std::int64_t margin = TARGET + 1 - totals[lambda];
            if (margin < closest_margin) {
                closest_margin = margin;
                closest_passing = lambda;
            }
        }
        if (totals[lambda] != SATURATED) {
            last_nonstabilized = lambda;
        }
    }

    const std::array<std::int64_t, N> expected_204 = {
        34204072, 42236704, 46007576, 48676144, 49799584, 50919000,
        50283048, 50919000, 49799584, 48676144, 46007576, 42236704,
        34204072
    };
    const std::array<std::int64_t, N> expected_490 = {
        53624480, 67280008, 74352832, 80448368, 82285472, 85566112,
        83924304, 85566112, 82285472, 80448368, 74352832, 67280008,
        53624480
    };
    if (rows_204 != expected_204 || rows_490 != expected_490) {
        throw std::runtime_error("row table mismatch");
    }
    if (class_totals[204] != 15389243) {
        throw std::runtime_error("lambda 204 class checksum mismatch");
    }
    if (checksum0 != 336812082968LL ||
        checksum1 != 110335357319864LL ||
        checksum2 != 41937553140659688LL) {
        throw std::runtime_error("frontier checksum mismatch");
    }

    std::vector<int> expected_passing;
    for (int lambda = 1; lambda <= 489; ++lambda) {
        expected_passing.push_back(lambda);
    }
    expected_passing.push_back(491);
    expected_passing.push_back(493);
    expected_passing.push_back(495);
    if (passing != expected_passing) {
        throw std::runtime_error("passing set mismatch");
    }
    if (last_nonstabilized != 517) {
        throw std::runtime_error("stabilization frontier mismatch");
    }
    if (closest_passing != 488 || closest_margin != 318058) {
        throw std::runtime_error("closest passing value mismatch");
    }

    const std::array<std::int64_t, 9> expected_frontier = {
        970012416, 968283648, 971038848, 968935984, 971993648,
        969521392, 972940864, 970008416, 973635440
    };
    for (int offset = 0; offset < 9; ++offset) {
        if (totals[488 + offset] != expected_frontier[offset]) {
            throw std::runtime_error("frontier value mismatch");
        }
    }
    for (int lambda = 518; lambda <= MAX_LAMBDA; ++lambda) {
        if (totals[lambda] != SATURATED) {
            throw std::runtime_error("post-518 stabilization mismatch");
        }
    }

    std::cout << "round49 frontier verification: PASS" << std::endl;
    std::cout << "checksums: " << checksum0 << " " << checksum1 << " " << checksum2 << std::endl;
    std::cout << "lambda=204 total/classes: " << totals[204] << " " << class_totals[204] << std::endl;
    std::cout << "lambda=490 total/sharp gap: " << totals[490] << " "
              << totals[490] - 1 - TARGET << std::endl;
    std::cout << "last nonstabilized lambda: " << last_nonstabilized << std::endl;
    std::cout << "closest passing lambda/margin: " << closest_passing << " "
              << closest_margin << std::endl;
    return 0;
}
