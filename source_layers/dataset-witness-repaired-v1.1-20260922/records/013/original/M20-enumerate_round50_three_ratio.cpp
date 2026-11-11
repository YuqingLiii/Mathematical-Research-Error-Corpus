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
constexpr int PCODES = 1 << 8;
constexpr int DSHIFT = 12;
constexpr int DEST_BITS = 320000;
constexpr int DEST_WORDS = DEST_BITS / 64;
constexpr int OFFSET = DEST_BITS / 2;
constexpr std::int64_t TARGET = 970330473;

using SmallBits = std::array<std::uint64_t, BWORDS>;
using DifferenceBits = std::array<SmallBits, 25>;
using PatternTable = std::vector<DifferenceBits>;

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

int pattern_weight(std::uint16_t code) {
    int first = code & 15;
    int second = (code >> 4) & 15;
    if (first == 0 || second == 0) {
        throw std::runtime_error("two-edge pattern has a zero nibble");
    }
    return first == second ? 4 : 8;
}

struct DeletedResult {
    int deleted = 0;
    std::vector<std::int64_t> support;
    std::vector<std::int64_t> classes;
};

DeletedResult compute_deleted(int deleted, const std::vector<int>& etas) {
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
                            int partial = 3 * u + v + 20 * (a - b) + 490 * (c - d);
                            if (partial < BMIN || partial > BMAX) {
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
                                    int bit = partial - BMIN;
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

    DeletedResult result;
    result.deleted = deleted;
    result.support.resize(etas.size());
    result.classes.resize(etas.size());
    for (std::size_t eta_index = 0; eta_index < etas.size(); ++eta_index) {
        int eta = etas[eta_index];
        for (int code = 1; code < PCODES; ++code) {
            if (!active[code]) continue;
            std::array<std::uint64_t, DEST_WORDS> joined{};
            for (int difference = -12; difference <= 12; ++difference) {
                if (difference == 0) continue;
                const auto& source = table[code][difference + DSHIFT];
                int start = OFFSET + eta * difference + BMIN;
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
            result.classes[eta_index] += distinct;
            result.support[eta_index] += distinct * pattern_weight(code);
        }
    }
    return result;
}

}  // namespace

int main(int argc, char** argv) {
    std::vector<int> etas;
    bool full_scan = false;
    for (int index = 1; index < argc; ++index) {
        if (std::string_view(argv[index]) == "--all") {
            full_scan = true;
            continue;
        }
        int eta = std::abs(std::atoi(argv[index]));
        if (eta < 1 || eta > 12287) {
            throw std::runtime_error("eta must lie between 1 and 12287");
        }
        etas.push_back(eta);
    }
    if (full_scan) {
        if (!etas.empty()) {
            throw std::runtime_error("--all cannot be combined with explicit eta values");
        }
        etas.reserve(12286);
        for (int eta = 1; eta <= 12286; ++eta) etas.push_back(eta);
    }
    if (etas.empty()) etas = {4888};

    for (int mask = 0; mask <= FULL; ++mask) {
        if (std::popcount(static_cast<unsigned>(mask)) <= 4 &&
            std::popcount(static_cast<unsigned>(mask)) % 2 == 0) {
            matching_patterns(mask);
        }
    }

    std::vector<std::future<DeletedResult>> futures;
    for (int deleted = 0; deleted < N; ++deleted) {
        futures.push_back(std::async(std::launch::async, compute_deleted, deleted, etas));
    }

    std::vector<std::vector<std::int64_t>> rows(
        etas.size(), std::vector<std::int64_t>(N));
    std::vector<std::vector<std::int64_t>> class_rows(
        etas.size(), std::vector<std::int64_t>(N));
    std::vector<std::int64_t> class_totals(etas.size());
    for (int deleted = 0; deleted < N; ++deleted) {
        DeletedResult result = futures[deleted].get();
        for (std::size_t index = 0; index < etas.size(); ++index) {
            rows[index][deleted] = result.support[index];
            class_rows[index][deleted] = result.classes[index];
            class_totals[index] += result.classes[index];
        }
    }

    for (std::size_t index = 0; index < etas.size(); ++index) {
        std::int64_t total = 0;
        for (std::int64_t value : rows[index]) total += value;
        std::cout << "eta=" << etas[index]
                  << " exact=" << total
                  << " sharp_margin=" << TARGET - (total - 1)
                  << " classes=" << class_totals[index] << std::endl;
        std::cout << "  support=(";
        for (int deleted = 0; deleted < N; ++deleted) {
            if (deleted != 0) std::cout << ",";
            std::cout << rows[index][deleted];
        }
        std::cout << ")" << std::endl;
        std::cout << "  classes=(";
        for (int deleted = 0; deleted < N; ++deleted) {
            if (deleted != 0) std::cout << ",";
            std::cout << class_rows[index][deleted];
        }
        std::cout << ")" << std::endl;
    }
    return 0;
}
