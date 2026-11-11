#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <limits>
#include <mutex>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

namespace {

constexpr int N = 13;
constexpr int CHOOSE = 10;
constexpr int FULL = (1 << N) - 1;
constexpr std::array<int, CHOOSE> SLOPES = {
    3, 1, 20, -20, 490, -490, 12090, -12090, 300177, -300177,
};

// Exact global rearrangement bounds for the ten special columns.
constexpr int TMIN = -3753323;
constexpr int TMAX = 3753371;
constexpr int TWIDTH = TMAX - TMIN + 1;
constexpr int TWORDS = (TWIDTH + 63) / 64;
constexpr int QMIN = -45039888;
constexpr int QMAX = 45040464;
constexpr std::uint64_t QWIDTH = static_cast<std::uint64_t>(QMAX - QMIN + 1);

constexpr std::size_t HASH_CAPACITY = std::size_t{1} << 23;
constexpr std::uint64_t SIGN_FLAG = std::uint64_t{1} << 63;
constexpr std::uint64_t COLLISION_FLAG = std::uint64_t{1} << 62;
constexpr std::uint64_t RAW_MASK = COLLISION_FLAG - 1;

struct Metrics {
    std::uint64_t raw = 0;
    std::uint64_t t_fibers = 0;
    std::uint64_t tq_groups = 0;
    std::uint64_t collision_groups = 0;
    std::uint64_t collision_excess = 0;
    std::uint64_t zero_collision_groups = 0;
    std::uint64_t third_hits = 0;
    std::uint64_t subsets_with_collision = 0;
    int min_t_fiber = std::numeric_limits<int>::max();
    int max_t_fiber = 0;
};

struct SubsetBits {
    std::vector<std::uint64_t> support;
    std::vector<std::uint64_t> singleton;
};

std::array<SubsetBits, 1 << N> subset_bits;
std::mutex result_mutex;
Metrics global_metrics;

std::uint64_t mix64(std::uint64_t value) {
    value += 0x9e3779b97f4a7c15ULL;
    value = (value ^ (value >> 30)) * 0xbf58476d1ce4e5b9ULL;
    value = (value ^ (value >> 27)) * 0x94d049bb133111ebULL;
    return value ^ (value >> 31);
}

int reflect_mask(int mask) {
    int result = 0;
    for (int row = 0; row < N; ++row) {
        if (mask & (1 << row)) result |= 1 << (N - 1 - row);
    }
    return result;
}

void set_bit(std::vector<std::uint64_t>& bits, int t) {
    const int index = t - TMIN;
    if (index < 0 || index >= TWIDTH) throw std::runtime_error("t outside certified range");
    bits[index / 64] |= std::uint64_t{1} << (index % 64);
}

struct Worker {
    std::vector<std::uint64_t> table = std::vector<std::uint64_t>(HASH_CAPACITY);
    std::vector<std::uint8_t> t_counts = std::vector<std::uint8_t>(TWIDTH);
    Metrics metrics;

    std::uint64_t encode_key(int t, int q) const {
        if (t < TMIN || t > TMAX || q < QMIN || q > QMAX) {
            throw std::runtime_error("(t,Q) outside certified range");
        }
        const std::uint64_t key =
            static_cast<std::uint64_t>(t - TMIN) * QWIDTH
            + static_cast<std::uint64_t>(q - QMIN) + 1;
        if (key == 0 || key > RAW_MASK) throw std::runtime_error("bad encoded key");
        return key;
    }

    void insert(int t, int q, bool negative) {
        const std::uint64_t raw_key = encode_key(t, q);
        std::size_t slot = static_cast<std::size_t>(mix64(raw_key)) & (HASH_CAPACITY - 1);
        for (;;) {
            std::uint64_t& stored = table[slot];
            if (stored == 0) {
                stored = raw_key | (negative ? SIGN_FLAG : 0);
                ++metrics.tq_groups;
                break;
            }
            if ((stored & RAW_MASK) == raw_key) {
                ++metrics.collision_excess;
                if ((stored & COLLISION_FLAG) != 0) {
                    ++metrics.third_hits;
                } else {
                    stored |= COLLISION_FLAG;
                    ++metrics.collision_groups;
                    const bool first_negative = (stored & SIGN_FLAG) != 0;
                    if (first_negative != negative) ++metrics.zero_collision_groups;
                }
                break;
            }
            slot = (slot + 1) & (HASH_CAPACITY - 1);
        }

        std::uint8_t& count = t_counts[t - TMIN];
        if (count == std::numeric_limits<std::uint8_t>::max()) {
            throw std::runtime_error("t fiber overflow");
        }
        ++count;
        ++metrics.raw;
    }

    void enumerate(
        const std::array<int, CHOOSE>& rows,
        int depth,
        unsigned remaining,
        int t,
        int q,
        bool negative
    ) {
        if (depth == CHOOSE - 1) {
            const int position = std::countr_zero(remaining);
            const int row = rows[position];
            insert(
                t + SLOPES[depth] * row,
                q + SLOPES[depth] * row * row,
                negative
            );
            return;
        }
        unsigned choices = remaining;
        while (choices != 0) {
            const int position = std::countr_zero(choices);
            const unsigned bit = 1U << position;
            choices &= ~bit;
            const int row = rows[position];
            const int rank = std::popcount(remaining & (bit - 1));
            enumerate(
                rows,
                depth + 1,
                remaining & ~bit,
                t + SLOPES[depth] * row,
                q + SLOPES[depth] * row * row,
                negative ^ ((rank & 1) != 0)
            );
        }
    }

    void process(int mask) {
        std::fill(table.begin(), table.end(), 0);
        std::fill(t_counts.begin(), t_counts.end(), 0);
        metrics = {};
        metrics.min_t_fiber = std::numeric_limits<int>::max();

        std::array<int, CHOOSE> rows{};
        int cursor = 0;
        for (int row = 0; row < N; ++row) {
            if (mask & (1 << row)) rows[cursor++] = row;
        }
        if (cursor != CHOOSE) throw std::runtime_error("bad row mask");

        enumerate(rows, 0, (1U << CHOOSE) - 1, 0, 0, false);

        SubsetBits direct;
        direct.support.assign(TWORDS, 0);
        direct.singleton.assign(TWORDS, 0);
        for (int index = 0; index < TWIDTH; ++index) {
            const int count = t_counts[index];
            if (count == 0) continue;
            ++metrics.t_fibers;
            metrics.min_t_fiber = std::min(metrics.min_t_fiber, count);
            metrics.max_t_fiber = std::max(metrics.max_t_fiber, count);
            direct.support[index / 64] |= std::uint64_t{1} << (index % 64);
            if (count == 1) {
                direct.singleton[index / 64] |= std::uint64_t{1} << (index % 64);
            }
        }
        metrics.subsets_with_collision = metrics.collision_groups != 0;

        const int reflected_mask = reflect_mask(mask);
        SubsetBits reflected;
        if (reflected_mask != mask) {
            reflected.support.assign(TWORDS, 0);
            reflected.singleton.assign(TWORDS, 0);
            for (int index = 0; index < TWIDTH; ++index) {
                const int count = t_counts[index];
                if (count == 0) continue;
                const int t = index + TMIN;
                const int reflected_t = 48 - t;  // sum(SLOPES) = 4, row -> 12-row.
                set_bit(reflected.support, reflected_t);
                if (count == 1) set_bit(reflected.singleton, reflected_t);
            }
        }

        const std::uint64_t weight = reflected_mask == mask ? 1 : 2;
        std::lock_guard<std::mutex> lock(result_mutex);
        subset_bits[mask] = std::move(direct);
        if (reflected_mask != mask) subset_bits[reflected_mask] = std::move(reflected);
        global_metrics.raw += weight * metrics.raw;
        global_metrics.t_fibers += weight * metrics.t_fibers;
        global_metrics.tq_groups += weight * metrics.tq_groups;
        global_metrics.collision_groups += weight * metrics.collision_groups;
        global_metrics.collision_excess += weight * metrics.collision_excess;
        global_metrics.zero_collision_groups += weight * metrics.zero_collision_groups;
        global_metrics.third_hits += weight * metrics.third_hits;
        global_metrics.subsets_with_collision += weight * metrics.subsets_with_collision;
        global_metrics.min_t_fiber = std::min(global_metrics.min_t_fiber, metrics.min_t_fiber);
        global_metrics.max_t_fiber = std::max(global_metrics.max_t_fiber, metrics.max_t_fiber);
    }
};

std::uint64_t popcount_bits(const std::vector<std::uint64_t>& bits) {
    std::uint64_t total = 0;
    for (std::uint64_t word : bits) total += std::popcount(word);
    return total;
}

std::pair<std::uint64_t, std::uint64_t> aggregate_formal_fibers(int deleted) {
    std::uint64_t support_total = 0;
    std::uint64_t singleton_total = 0;
    const int remaining_mask = FULL & ~(1 << deleted);

    for (int q = -12; q <= 12; ++q) {
        if (q == 0) continue;
        std::vector<std::uint64_t> one(TWORDS, 0);
        std::vector<std::uint64_t> many(TWORDS, 0);
        for (int x = 0; x < N; ++x) {
            const int y = x - q;
            if (y < 0 || y >= N || x == deleted || y == deleted) continue;
            const int ten_mask = remaining_mask & ~(1 << x) & ~(1 << y);
            const SubsetBits& incoming = subset_bits[ten_mask];
            if (incoming.support.empty()) throw std::runtime_error("missing subset bitset");
            for (int word = 0; word < TWORDS; ++word) {
                const std::uint64_t old_support = one[word] | many[word];
                const std::uint64_t new_many =
                    many[word]
                    | (incoming.support[word] & ~incoming.singleton[word])
                    | (old_support & incoming.support[word]);
                const std::uint64_t new_one =
                    (one[word] | incoming.singleton[word]) & ~new_many;
                many[word] = new_many;
                one[word] = new_one;
            }
        }
        singleton_total += popcount_bits(one);
        for (int word = 0; word < TWORDS; ++word) one[word] |= many[word];
        support_total += popcount_bits(one);
    }
    return {support_total, singleton_total};
}

struct QFiberResult {
    int deleted = 0;
    int q = 0;
    std::uint64_t support = 0;
    std::uint64_t singleton = 0;
    int maximum = 0;
};

void enumerate_t_only(
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
        if (count == std::numeric_limits<std::uint16_t>::max()) {
            throw std::runtime_error("full formal fiber overflow");
        }
        ++count;
        return;
    }
    unsigned choices = remaining;
    while (choices != 0) {
        const int position = std::countr_zero(choices);
        const unsigned bit = 1U << position;
        choices &= ~bit;
        enumerate_t_only(
            rows,
            depth + 1,
            remaining & ~bit,
            t + SLOPES[depth] * rows[position],
            counts
        );
    }
}

QFiberResult compute_q_fibers(int deleted, int q) {
    QFiberResult result{deleted, q, 0, 0, 0};
    std::vector<std::uint16_t> counts(TWIDTH, 0);
    for (int x = 0; x < N; ++x) {
        const int y = x - q;
        if (y < 0 || y >= N || x == deleted || y == deleted) continue;
        std::array<int, CHOOSE> rows{};
        int cursor = 0;
        for (int row = 0; row < N; ++row) {
            if (row != deleted && row != x && row != y) rows[cursor++] = row;
        }
        if (cursor != CHOOSE) throw std::runtime_error("bad ten-row complement");
        enumerate_t_only(rows, 0, (1U << CHOOSE) - 1, 0, counts);
    }
    for (std::uint16_t count : counts) {
        if (count == 0) continue;
        ++result.support;
        if (count == 1) ++result.singleton;
        result.maximum = std::max(result.maximum, static_cast<int>(count));
    }
    return result;
}

void require(bool condition, const std::string& message) {
    if (!condition) throw std::runtime_error(message);
}

}  // namespace

int main(int argc, char** argv) {
    int requested_threads = std::max(1U, std::thread::hardware_concurrency() / 2);
    int limit = -1;
    for (int index = 1; index < argc; ++index) {
        const std::string argument = argv[index];
        if (argument == "--threads" && index + 1 < argc) {
            requested_threads = std::max(1, std::atoi(argv[++index]));
        } else if (argument == "--limit" && index + 1 < argc) {
            limit = std::max(1, std::atoi(argv[++index]));
        } else {
            throw std::runtime_error("usage: verify_round52_laurent [--threads N] [--limit N]");
        }
    }

    std::vector<int> representatives;
    for (int mask = 0; mask <= FULL; ++mask) {
        if (std::popcount(static_cast<unsigned>(mask)) != CHOOSE) continue;
        if (mask <= reflect_mask(mask)) representatives.push_back(mask);
    }
    require(representatives.size() == 146, "unexpected reflection representative count");
    if (limit > 0 && limit < static_cast<int>(representatives.size())) {
        representatives.resize(limit);
    }

    std::atomic<std::size_t> next{0};
    const int thread_count = std::min<int>(requested_threads, representatives.size());
    std::vector<std::thread> threads;
    for (int worker_index = 0; worker_index < thread_count; ++worker_index) {
        threads.emplace_back([&] {
            Worker worker;
            for (;;) {
                const std::size_t index = next.fetch_add(1);
                if (index >= representatives.size()) break;
                worker.process(representatives[index]);
            }
        });
    }
    for (auto& thread : threads) thread.join();

    std::cout << "representatives=" << representatives.size() << "\n";
    std::cout << "raw=" << global_metrics.raw << "\n";
    std::cout << "t_fibers=" << global_metrics.t_fibers << "\n";
    std::cout << "tq_groups=" << global_metrics.tq_groups << "\n";
    std::cout << "collision_groups=" << global_metrics.collision_groups << "\n";
    std::cout << "collision_excess=" << global_metrics.collision_excess << "\n";
    std::cout << "zero_collision_groups=" << global_metrics.zero_collision_groups << "\n";
    std::cout << "third_hits=" << global_metrics.third_hits << "\n";
    std::cout << "subsets_with_collision=" << global_metrics.subsets_with_collision << "\n";
    std::cout << "t_fiber_min=" << global_metrics.min_t_fiber << "\n";
    std::cout << "t_fiber_max=" << global_metrics.max_t_fiber << "\n";

    if (representatives.size() != 146) return 0;

    require(global_metrics.raw == 1'037'836'800ULL, "raw permutation count mismatch");
    require(global_metrics.t_fibers == 481'716'856ULL, "t-fiber count mismatch");
    require(global_metrics.tq_groups == 1'037'836'116ULL, "(t,Q) group count mismatch");
    require(global_metrics.collision_groups == 684, "collision-group count mismatch");
    require(global_metrics.collision_excess == 684, "collision-excess mismatch");
    require(global_metrics.zero_collision_groups == 0, "a signed collision cancelled");
    require(global_metrics.third_hits == 0, "a collision group has size at least three");
    require(global_metrics.subsets_with_collision == 100, "collision-subset count mismatch");
    require(global_metrics.min_t_fiber == 1 && global_metrics.max_t_fiber == 96,
            "t-fiber range mismatch");

    constexpr std::array<std::uint64_t, N> EXPECTED_SUPPORT = {
        53624480, 67257904, 74298872, 80378258, 82204740, 85478914, 83844156,
        85478914, 82204740, 80378258, 74298872, 67257904, 53624480,
    };
    constexpr std::array<std::uint64_t, N> EXPECTED_SINGLETON = {
        2611200, 5487296, 6765948, 7099366, 7595724, 8124130, 7618580,
        8124130, 7595724, 7099366, 6765948, 5487296, 2611200,
    };

    std::uint64_t support_checksum = 0;
    std::uint64_t singleton_checksum = 0;
    for (int deleted = 0; deleted < N; ++deleted) {
        const auto [support, singleton] = aggregate_formal_fibers(deleted);
        std::cout << "deleted=" << deleted
                  << " support=" << support
                  << " singleton=" << singleton
                  << " multiple=" << (support - singleton) << "\n";
        require(support == EXPECTED_SUPPORT[deleted], "per-cofactor support mismatch");
        require(singleton == EXPECTED_SINGLETON[deleted], "per-cofactor singleton mismatch");
        support_checksum += support;
        singleton_checksum += singleton;
    }
    require(support_checksum == 970'330'492ULL, "formal support checksum mismatch");
    require(singleton_checksum == 82'985'908ULL, "singleton checksum mismatch");
    require(support_checksum - singleton_checksum == 887'344'584ULL,
            "multiple-fiber checksum mismatch");

    constexpr std::array<int, N> EXPECTED_MAXIMUM = {
        480, 240, 360, 360, 360, 360, 360,
        360, 360, 360, 360, 240, 480,
    };
    std::vector<std::pair<int, int>> q_tasks;
    for (int deleted = 0; deleted < N; ++deleted) {
        for (int q = -12; q <= 12; ++q) {
            if (q != 0) q_tasks.emplace_back(deleted, q);
        }
    }
    std::atomic<std::size_t> next_q{0};
    std::vector<QFiberResult> q_results(q_tasks.size());
    threads.clear();
    for (int worker_index = 0; worker_index < thread_count; ++worker_index) {
        threads.emplace_back([&] {
            for (;;) {
                const std::size_t index = next_q.fetch_add(1);
                if (index >= q_tasks.size()) break;
                q_results[index] = compute_q_fibers(q_tasks[index].first, q_tasks[index].second);
            }
        });
    }
    for (auto& thread : threads) thread.join();

    for (int deleted = 0; deleted < N; ++deleted) {
        std::uint64_t support = 0;
        std::uint64_t singleton = 0;
        int maximum = 0;
        for (const QFiberResult& result : q_results) {
            if (result.deleted != deleted) continue;
            support += result.support;
            singleton += result.singleton;
            maximum = std::max(maximum, result.maximum);
        }
        require(support == EXPECTED_SUPPORT[deleted], "direct full-fiber support mismatch");
        require(singleton == EXPECTED_SINGLETON[deleted], "direct full-fiber singleton mismatch");
        require(maximum == EXPECTED_MAXIMUM[deleted], "direct full-fiber maximum mismatch");
        std::cout << "deleted=" << deleted << " direct_maximum=" << maximum << "\n";
    }

    std::cout << "formal_support=" << support_checksum << "\n";
    std::cout << "formal_singleton=" << singleton_checksum << "\n";
    std::cout << "formal_multiple=" << support_checksum - singleton_checksum << "\n";
    std::cout << "round52 Laurent census: PASS\n";
}
