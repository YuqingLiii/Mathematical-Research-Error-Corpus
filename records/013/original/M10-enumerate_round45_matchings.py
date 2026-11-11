#!/usr/bin/env python3
"""Enumerate paired-slope difference patterns for the Round 45 support bound."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import factorial


def matching_patterns(rows: tuple[int, ...]) -> set[tuple[int, ...]]:
    patterns: set[tuple[int, ...]] = set()

    def visit(remaining: tuple[int, ...], differences: tuple[int, ...]) -> None:
        if not remaining:
            patterns.add(tuple(sorted(differences)))
            return
        first = remaining[0]
        for index in range(1, len(remaining)):
            second = remaining[index]
            visit(
                remaining[1:index] + remaining[index + 1 :],
                differences + (abs(first - second),),
            )

    visit(rows, ())
    return patterns


def oriented_labeled_count(patterns: set[tuple[int, ...]]) -> int:
    total = 0
    for pattern in patterns:
        permutations = factorial(6)
        for multiplicity in Counter(pattern).values():
            permutations //= factorial(multiplicity)
        total += (2**6) * permutations
    return total


def main() -> None:
    pattern_counts = []
    support_counts = []
    for omitted in range(13):
        rows = tuple(index for index in range(13) if index != omitted)
        patterns = matching_patterns(rows)
        pattern_counts.append(len(patterns))
        support_counts.append(oriented_labeled_count(patterns))

    assert pattern_counts == [
        1812,
        2396,
        2656,
        2841,
        2944,
        3054,
        2480,
        3054,
        2944,
        2841,
        2656,
        2396,
        1812,
    ]
    assert support_counts == [
        27_008_064,
        37_097_600,
        42_527_744,
        46_694_912,
        49_514_432,
        51_759_872,
        43_391_424,
        51_759_872,
        49_514_432,
        46_694_912,
        42_527_744,
        37_097_600,
        27_008_064,
    ]

    def secular(value: int) -> Fraction:
        return sum(Fraction(size, value + size) for size in support_counts) - 1

    assert secular(508_658_597) > 0
    assert secular(508_658_598) < 0
    assert 2 * 508_658_598 > 970_330_474
    gap_numerator = 2 * 508_658_598 - 970_330_474
    assert gap_numerator == 46_986_722

    forbidden_union_bound = sum(size * (size - 1) for size in support_counts)
    assert forbidden_union_bound == 24_333_724_302_039_872

    print("pattern counts:", pattern_counts)
    print("support counts:", support_counts)
    print("508658597 < lambda_* < 508658598")
    print("twice-upper-bound excess over 970330474:", gap_numerator)
    print("forbidden-shift union bound:", forbidden_union_bound)


if __name__ == "__main__":
    main()
