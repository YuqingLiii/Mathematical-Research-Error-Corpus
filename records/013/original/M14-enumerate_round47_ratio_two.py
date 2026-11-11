#!/usr/bin/env python3
"""Exact support count for the proportional one-defect class delta = 2 m_6."""

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


def weight(pattern: tuple[int, ...]) -> int:
    denominator = 1
    for difference in set(pattern):
        denominator *= factorial(pattern.count(difference))
    return (2**5) * factorial(5) // denominator


def main() -> None:
    support_counts: list[int] = []
    class_counts: list[int] = []
    group_counts: list[int] = []

    for deleted in range(13):
        retained = tuple(v for v in range(13) if v != deleted)
        groups: dict[int, set[tuple[int, ...]]] = {}
        for u in retained:
            for v in retained:
                if u == v:
                    continue
                level = 3 * u + v
                remainder = tuple(x for x in retained if x not in (u, v))
                groups.setdefault(level, set()).update(matching_patterns(remainder))
        support_counts.append(
            sum(sum(weight(pattern) for pattern in patterns) for patterns in groups.values())
        )
        class_counts.append(sum(len(patterns) for patterns in groups.values()))
        group_counts.append(len(groups))

    expected = [
        54_947_328,
        70_576_192,
        78_683_008,
        85_863_712,
        87_736_832,
        91_611_264,
        90_561_472,
        91_611_264,
        87_736_832,
        85_863_712,
        78_683_008,
        70_576_192,
        54_947_328,
    ]
    assert support_counts == expected
    assert sum(support_counts) == 1_029_398_144
    assert class_counts == [
        30_731,
        37_829,
        40_942,
        44_147,
        44_338,
        46_282,
        45_572,
        46_282,
        44_338,
        44_147,
        40_942,
        37_829,
        30_731,
    ]
    assert sum(class_counts) == 534_110
    assert group_counts == [43, 46, 46, 47, 46, 47, 47, 47, 46, 47, 46, 46, 43]
    assert 93 * 49**5 - 1 == 26_270_198_156

    print(f"delta=2m6 support counts: {support_counts}")
    print(f"support checksum: {sum(support_counts)}")
    print(f"formal class counts: {class_counts}")
    print(f"group counts: {group_counts}")
    print(f"safe-spacing coefficient-vector bound: {93 * 49**5 - 1}")
    print("round47 candidate enumeration: PASS")


if __name__ == "__main__":
    main()

