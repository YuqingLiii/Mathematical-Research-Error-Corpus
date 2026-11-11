#!/usr/bin/env python3
"""Exact combinatorial support count for five centered pairs plus one defect pair."""

from __future__ import annotations

from functools import lru_cache
from math import factorial


@lru_cache(maxsize=None)
def matching_patterns(vertices: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    if not vertices:
        return frozenset({()})
    a = vertices[0]
    out: set[tuple[int, ...]] = set()
    for pos in range(1, len(vertices)):
        b = vertices[pos]
        rest = vertices[1:pos] + vertices[pos + 1 :]
        for pattern in matching_patterns(rest):
            out.add(tuple(sorted(pattern + (abs(a - b),))))
    return frozenset(out)


def five_pair_count(vertices: tuple[int, ...]) -> int:
    assert len(vertices) == 10
    total = 0
    for pattern in matching_patterns(tuple(sorted(vertices))):
        denominator = 1
        for difference in set(pattern):
            denominator *= factorial(pattern.count(difference))
        total += (2**5) * factorial(5) // denominator
    return total


def main() -> None:
    counts: list[int] = []
    for deleted in range(13):
        retained = tuple(v for v in range(13) if v != deleted)
        count = 0
        # The ordered endpoints carry the + and - columns of the defect pair.
        for u in retained:
            for v in retained:
                if u == v:
                    continue
                remainder = tuple(x for x in retained if x not in (u, v))
                count += five_pair_count(remainder)
        counts.append(count)

    expected = [
        125_010_752,
        144_089_600,
        156_318_464,
        164_181_312,
        168_885_376,
        169_583_168,
        165_829_248,
        169_583_168,
        168_885_376,
        164_181_312,
        156_318_464,
        144_089_600,
        125_010_752,
    ]
    assert counts == expected
    assert sum(counts) == 2_021_966_592
    assert counts == counts[::-1]
    print(f"one-defect support counts: {counts}")
    print(f"sum: {sum(counts)}")
    print(f"safe-spacing coefficient-vector bound: {45 * 49**6 - 1}")
    print("round46 candidate enumeration: PASS")


if __name__ == "__main__":
    main()

