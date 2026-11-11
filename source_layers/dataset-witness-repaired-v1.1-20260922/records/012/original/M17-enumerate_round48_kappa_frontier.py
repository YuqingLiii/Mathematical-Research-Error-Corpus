#!/usr/bin/env python3
"""Exact formal-support counts for m_j = kappa m_6 in the ratio-two class.

The distinguished centered pair is kept oriented.  Its difference is folded
into t = 3u + v + kappa(a-b); the remaining four centered pairs are counted
as labelled, oriented difference coordinates.
"""

from __future__ import annotations

from functools import lru_cache
from math import factorial


TARGET = 970_330_473


@lru_cache(maxsize=None)
def matching_patterns(vertices: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    if not vertices:
        return frozenset({()})
    first = vertices[0]
    out: set[tuple[int, ...]] = set()
    for position in range(1, len(vertices)):
        partner = vertices[position]
        rest = vertices[1:position] + vertices[position + 1 :]
        for pattern in matching_patterns(rest):
            out.add(tuple(sorted(pattern + (abs(first - partner),))))
    return frozenset(out)


def four_pair_weight(pattern: tuple[int, ...]) -> int:
    denominator = 1
    for difference in set(pattern):
        denominator *= factorial(pattern.count(difference))
    return (2**4) * factorial(4) // denominator


def exact_support(kappa: int) -> tuple[int, ...]:
    per_deleted: list[int] = []
    for deleted in range(13):
        retained = tuple(row for row in range(13) if row != deleted)
        groups: dict[int, set[tuple[int, ...]]] = {}
        for u in retained:
            for v in retained:
                if u == v:
                    continue
                after_defect = tuple(row for row in retained if row not in (u, v))
                for a in after_defect:
                    for b in after_defect:
                        if a == b:
                            continue
                        t = 3 * u + v + kappa * (a - b)
                        remaining = tuple(
                            row for row in after_defect if row not in (a, b)
                        )
                        groups.setdefault(t, set()).update(
                            matching_patterns(remaining)
                        )
        per_deleted.append(
            sum(
                sum(four_pair_weight(pattern) for pattern in patterns)
                for patterns in groups.values()
            )
        )
    return tuple(per_deleted)


def main() -> None:
    for kappa in range(2, 49):
        counts = exact_support(kappa)
        total = sum(counts)
        range_bound = 13 * (47 + 24 * abs(kappa)) * 24**4
        print(
            f"kappa={kappa:2d} exact={total:10d} "
            f"margin={TARGET-total:10d} range={range_bound:10d}"
        )
        print(f"  counts={counts}")


if __name__ == "__main__":
    main()
