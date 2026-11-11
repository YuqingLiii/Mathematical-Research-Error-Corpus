#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <future>
#include <iostream>
#include <stdexcept>
#include <string_view>
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
constexpr std::int64_t TARGET = 970330473;

using SmallBits = std::array<std::uint64_t, BWORDS>;
using DifferenceBits = std::array<SmallBits, 25>;
using PatternTable = std::vector<DifferenceBits>;
using TBits = std::array<std::uint64_t, TWORDS>;

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

template <typename Source>
void or_shifted(
    std::vector<std::uint64_t>& destination,
    const Source& source,
    int source_words,
    int start
) {
    int word_offset = start / 64;
    int shift = start % 64;
    for (int word = 0; word < source_words; ++word) {
        std::uint64_t value = source[word];
        if (value == 0) continue;
        destination[word_offset + word] |= value << shift;
        if (shift != 0) {
            destination[word_offset + word + 1] |= value >> (64 - shift);
        }
    }
}

struct DeletedResult {
    int deleted = 0;
    std::vector<std::int64_t> support;
};

DeletedResult compute_deleted(int deleted, const std::vector<int>& thetas) {
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
                            if (base < BMIN || base > BMAX) {
                                throw std::runtime_error("base outside certified range");
                            }
                            for (int e = 0; e < N; ++e) {
                                if (e == deleted || e == u || e == v || e == a || e == b || e == c || e == d) continue;
                                for (int f = 0; f < N; ++f) {
                                    if (f == deleted || f == u || f == v || f == a || f == b || f == c || f == d || f == e) continue;
                                    int difference = e - f;
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
        std::vector<std::uint64_t> destination(TWORDS + 1);
        for (int difference = -12; difference <= 12; ++difference) {
            if (difference == 0) continue;
            int start = BMIN + ETA * difference - TMIN;
            or_shifted(destination, table[code][difference + DSHIFT], BWORDS, start);
        }
        std::copy_n(destination.begin(), TWORDS, folded[code].begin());
    }

    DeletedResult result;
    result.deleted = deleted;
    result.support.resize(thetas.size());
    for (std::size_t theta_index = 0; theta_index < thetas.size(); ++theta_index) {
        int theta = thetas[theta_index];
        int destination_bits = TWIDTH + 24 * theta;
        int destination_words = (destination_bits + 63) / 64 + 1;
        std::array<std::vector<std::uint64_t>, 25> joined;
        for (int signed_difference = -12; signed_difference <= 12; ++signed_difference) {
            if (signed_difference == 0) continue;
            joined[signed_difference + DSHIFT].resize(destination_words);
        }

        for (int code = 1; code < PCODES; ++code) {
            if (!active[code]) continue;
            int first = code & 15;
            int second = (code >> 4) & 15;
            if (first == 0 || second == 0) {
                throw std::runtime_error("two-edge pattern has a zero nibble");
            }
            auto add_theta_magnitude = [&](int theta_magnitude, int remaining_magnitude) {
                for (int remaining_sign : {-1, 1}) {
                    auto& destination = joined[DSHIFT + remaining_sign * remaining_magnitude];
                    or_shifted(destination, folded[code], TWORDS, theta * (12 - theta_magnitude));
                    or_shifted(destination, folded[code], TWORDS, theta * (12 + theta_magnitude));
                }
            };
            add_theta_magnitude(first, second);
            if (first != second) add_theta_magnitude(second, first);
        }

        std::int64_t total = 0;
        for (int signed_difference = -12; signed_difference <= 12; ++signed_difference) {
            if (signed_difference == 0) continue;
            for (std::uint64_t word : joined[signed_difference + DSHIFT]) {
                total += std::popcount(word);
            }
        }
        result.support[theta_index] = total;
    }
    return result;
}

}  // namespace

int main(int argc, char** argv) {
    std::vector<int> thetas;
    bool compact = false;
    bool have_range = false;
    int range_start = 0;
    int range_end = 0;
    for (int index = 1; index < argc; ++index) {
        std::string_view argument(argv[index]);
        if (argument == "--compact") {
            compact = true;
            continue;
        }
        if (argument == "--range") {
            if (index + 2 >= argc || have_range || !thetas.empty()) {
                throw std::runtime_error("--range requires exactly two bounds");
            }
            range_start = std::abs(std::atoi(argv[++index]));
            range_end = std::abs(std::atoi(argv[++index]));
            if (range_start < 1 || range_end < range_start || range_end > 302447) {
                throw std::runtime_error("invalid theta range");
            }
            have_range = true;
            continue;
        }
        int theta = std::abs(std::atoi(argv[index]));
        if (theta < 1 || theta > 302447) {
            throw std::runtime_error("theta must lie between 1 and 302447");
        }
        thetas.push_back(theta);
    }
    if (have_range) {
        thetas.reserve(range_end - range_start + 1);
        for (int theta = range_start; theta <= range_end; ++theta) {
            thetas.push_back(theta);
        }
    }
    if (thetas.empty()) thetas = {116983};

    for (int mask = 0; mask <= FULL; ++mask) {
        if (std::popcount(static_cast<unsigned>(mask)) <= 4 &&
            std::popcount(static_cast<unsigned>(mask)) % 2 == 0) {
            matching_patterns(mask);
        }
    }

    std::vector<std::future<DeletedResult>> futures;
    for (int deleted = 0; deleted < N; ++deleted) {
        futures.push_back(std::async(std::launch::async, compute_deleted, deleted, thetas));
    }

    std::vector<std::vector<std::int64_t>> rows(
        thetas.size(), std::vector<std::int64_t>(N));
    for (int deleted = 0; deleted < N; ++deleted) {
        DeletedResult result = futures[deleted].get();
        for (std::size_t index = 0; index < thetas.size(); ++index) {
            rows[index][deleted] = result.support[index];
        }
    }

    for (std::size_t index = 0; index < thetas.size(); ++index) {
        std::int64_t total = 0;
        for (std::int64_t value : rows[index]) total += value;
        std::cout << "theta=" << thetas[index]
                  << " exact=" << total
                  << " sharp_margin=" << TARGET - (total - 1) << std::endl;
        if (compact) continue;
        std::cout << "  support=(";
        for (int deleted = 0; deleted < N; ++deleted) {
            if (deleted != 0) std::cout << ",";
            std::cout << rows[index][deleted];
        }
        std::cout << ")" << std::endl;
    }
    return 0;
}
