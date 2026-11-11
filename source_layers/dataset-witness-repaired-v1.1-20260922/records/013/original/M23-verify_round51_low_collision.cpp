#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <future>
#include <iostream>
#include <limits>
#include <memory>
#include <stdexcept>
#include <string>
#include <vector>

namespace {

constexpr int N = 13;
constexpr int FULL = (1 << N) - 1;
constexpr int BMIN = -6119;
constexpr int BMAX = 6167;
constexpr int BWIDTH = BMAX - BMIN + 1;
constexpr int BWORDS = (BWIDTH + 63) / 64;
constexpr int ETA = 12090;
constexpr int TMIN = BMIN - 12 * ETA;
constexpr int TMAX = BMAX + 12 * ETA;
constexpr int TWIDTH = TMAX - TMIN + 1;
constexpr int TWORDS = (TWIDTH + 63) / 64;
constexpr int PCODES = 1 << 8;
constexpr int DSHIFT = 12;
constexpr int THETA_MAX = 150151;

using SmallBits = std::array<std::uint64_t, BWORDS>;
using DifferenceBits = std::array<SmallBits, 25>;
using PatternTable = std::vector<DifferenceBits>;
using TBits = std::array<std::uint64_t, TWORDS>;
using SignedSets = std::array<std::array<TBits, 25>, 25>;

std::array<std::vector<std::uint16_t>, 1 << N> match_cache;
std::array<bool, 1 << N> match_ready{};

std::uint16_t add_difference(std::uint16_t code, int difference) {
    std::array<int, 2> values{};
    int size = 0;
    for (int shift = 0; shift < 8; shift += 4) {
        int value = (code >> shift) & 15;
        if (value != 0) values[size++] = value;
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
    if (match_ready[mask]) return match_cache[mask];
    match_ready[mask] = true;
    auto& result = match_cache[mask];
    if (mask == 0) {
        result.push_back(0);
        return result;
    }
    int first = std::countr_zero(static_cast<unsigned>(mask));
    int rest = mask & ~(1 << first);
    for (int partner = first + 1; partner < N; ++partner) {
        if ((rest & (1 << partner)) == 0) continue;
        int smaller = rest & ~(1 << partner);
        for (std::uint16_t code : matching_patterns(smaller)) {
            result.push_back(add_difference(code, partner - first));
        }
    }
    std::sort(result.begin(), result.end());
    result.erase(std::unique(result.begin(), result.end()), result.end());
    return result;
}

template <typename Destination, typename Source>
void or_shifted(Destination& destination, const Source& source, int source_words, int start) {
    int word_offset = start / 64;
    int shift = start % 64;
    for (int word = 0; word < source_words; ++word) {
        std::uint64_t value = source[word];
        if (value == 0) continue;
        destination[word_offset + word] |= value << shift;
        if (shift != 0 && word_offset + word + 1 < static_cast<int>(destination.size())) {
            destination[word_offset + word + 1] |= value >> (64 - shift);
        }
    }
}

std::int64_t shifted_intersection(const TBits& left, const TBits& right, int shift_bits) {
    int word_shift = shift_bits / 64;
    int bit_shift = shift_bits % 64;
    std::int64_t total = 0;
    for (int output_word = word_shift; output_word < TWORDS; ++output_word) {
        int source_word = output_word - word_shift;
        std::uint64_t shifted = right[source_word] << bit_shift;
        if (bit_shift != 0 && source_word > 0) {
            shifted |= right[source_word - 1] >> (64 - bit_shift);
        }
        total += std::popcount(left[output_word] & shifted);
    }
    return total;
}

struct DeletedResult {
    std::vector<std::int64_t> h0;
    std::vector<std::int64_t> h1;
};

DeletedResult compute_deleted(int deleted, int theta_limit) {
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
                    for (int c = 0; c < N; ++c) {
                        if (c == deleted || c == u || c == v || c == a || c == b) continue;
                        for (int d = 0; d < N; ++d) {
                            if (d == deleted || d == u || d == v || d == a || d == b || d == c) continue;
                            int base = 3 * u + v + 20 * (a - b) + 490 * (c - d);
                            for (int e = 0; e < N; ++e) {
                                if (e == deleted || e == u || e == v || e == a || e == b || e == c || e == d) continue;
                                for (int f = 0; f < N; ++f) {
                                    if (f == deleted || f == u || f == v || f == a || f == b || f == c || f == d || f == e) continue;
                                    int remaining = FULL;
                                    remaining &= ~(1 << deleted);
                                    remaining &= ~(1 << u);
                                    remaining &= ~(1 << v);
                                    remaining &= ~(1 << a);
                                    remaining &= ~(1 << b);
                                    remaining &= ~(1 << c);
                                    remaining &= ~(1 << d);
                                    remaining &= ~(1 << e);
                                    remaining &= ~(1 << f);
                                    int difference = e - f;
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
        }
    }

    std::vector<TBits> folded(PCODES);
    for (int code = 1; code < PCODES; ++code) {
        if (!active[code]) continue;
        for (int difference = -12; difference <= 12; ++difference) {
            if (difference == 0) continue;
            int start = BMIN + ETA * difference - TMIN;
            or_shifted(folded[code], table[code][difference + DSHIFT], BWORDS, start);
        }
    }

    auto sets = std::make_unique<SignedSets>();
    for (int code = 1; code < PCODES; ++code) {
        if (!active[code]) continue;
        int first = code & 15;
        int second = (code >> 4) & 15;
        auto add_assignment = [&](int theta_magnitude, int residual_magnitude) {
            for (int theta_sign : {-1, 1}) {
                for (int residual_sign : {-1, 1}) {
                    auto& destination = (*sets)[DSHIFT + residual_sign * residual_magnitude]
                                                     [DSHIFT + theta_sign * theta_magnitude];
                    for (int word = 0; word < TWORDS; ++word) {
                        destination[word] |= folded[code][word];
                    }
                }
            }
        };
        add_assignment(first, second);
        if (first != second) add_assignment(second, first);
    }

    const std::array<std::pair<int, int>, 12> matching0 = {{
        {-12, -11}, {-10, -9}, {-8, -7}, {-6, -5}, {-4, -3}, {-2, -1},
        {1, 2}, {3, 4}, {5, 6}, {7, 8}, {9, 10}, {11, 12},
    }};
    const std::array<std::pair<int, int>, 10> matching1 = {{
        {-11, -10}, {-9, -8}, {-7, -6}, {-5, -4}, {-3, -2},
        {2, 3}, {4, 5}, {6, 7}, {8, 9}, {10, 11},
    }};

    DeletedResult result;
    result.h0.resize(THETA_MAX + 1);
    result.h1.resize(THETA_MAX + 1);
    for (int theta = 1; theta <= theta_limit; ++theta) {
        std::int64_t h0 = 0;
        std::int64_t h1 = 0;
        for (int q = -12; q <= 12; ++q) {
            if (q == 0) continue;
            for (auto [d, next] : matching0) {
                h0 += shifted_intersection(
                    (*sets)[DSHIFT + q][DSHIFT + d],
                    (*sets)[DSHIFT + q][DSHIFT + next], theta);
            }
            for (auto [d, next] : matching1) {
                h1 += shifted_intersection(
                    (*sets)[DSHIFT + q][DSHIFT + d],
                    (*sets)[DSHIFT + q][DSHIFT + next], theta);
            }
        }
        result.h0[theta] = h0;
        result.h1[theta] = h1;
    }
    return result;
}

std::string decimal(unsigned __int128 value) {
    if (value == 0) return "0";
    std::string result;
    while (value != 0) {
        result.push_back(static_cast<char>('0' + value % 10));
        value /= 10;
    }
    std::reverse(result.begin(), result.end());
    return result;
}

}  // namespace

int main(int argc, char** argv) {
    int theta_limit = THETA_MAX;
    if (argc == 2) {
        theta_limit = std::stoi(argv[1]);
        if (theta_limit < 1 || theta_limit > THETA_MAX) {
            throw std::runtime_error("theta limit outside certified range");
        }
    } else if (argc != 1) {
        throw std::runtime_error("usage: verifier [theta_limit]");
    }
    for (int mask = 0; mask <= FULL; ++mask) {
        if (std::popcount(static_cast<unsigned>(mask)) <= 4 &&
            std::popcount(static_cast<unsigned>(mask)) % 2 == 0) {
            matching_patterns(mask);
        }
    }

    std::vector<std::future<DeletedResult>> futures;
    for (int deleted = 0; deleted < N; ++deleted) {
        futures.push_back(std::async(std::launch::async, compute_deleted, deleted, theta_limit));
    }

    std::vector<std::int64_t> h0(THETA_MAX + 1);
    std::vector<std::int64_t> h1(THETA_MAX + 1);
    for (auto& future : futures) {
        DeletedResult part = future.get();
        for (int theta = 1; theta <= theta_limit; ++theta) {
            h0[theta] += part.h0[theta];
            h1[theta] += part.h1[theta];
        }
    }

    std::int64_t minimum = std::numeric_limits<std::int64_t>::max();
    int minimizer = 0;
    unsigned __int128 sum0 = 0;
    unsigned __int128 sum1 = 0;
    unsigned __int128 weighted0 = 0;
    unsigned __int128 weighted1 = 0;
    unsigned __int128 square0 = 0;
    unsigned __int128 square1 = 0;
    for (int theta = 1; theta <= theta_limit; ++theta) {
        std::int64_t value = std::max(h0[theta], h1[theta]);
        if (value < minimum) {
            minimum = value;
            minimizer = theta;
        }
        unsigned __int128 t = static_cast<unsigned>(theta);
        sum0 += h0[theta];
        sum1 += h1[theta];
        weighted0 += t * h0[theta];
        weighted1 += t * h1[theta];
        square0 += t * t * h0[theta];
        square1 += t * t * h1[theta];
    }

    std::cout << "minimum_max=" << minimum << " minimizer=" << minimizer
              << " h0=" << h0[minimizer] << " h1=" << h1[minimizer] << "\n";
    std::cout << "sum_h0=" << decimal(sum0) << " sum_h1=" << decimal(sum1) << "\n";
    std::cout << "sum_theta_h0=" << decimal(weighted0)
              << " sum_theta_h1=" << decimal(weighted1) << "\n";
    std::cout << "sum_theta2_h0=" << decimal(square0)
              << " sum_theta2_h1=" << decimal(square1) << "\n";
    return 0;
}
