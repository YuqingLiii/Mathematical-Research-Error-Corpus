#!/usr/bin/env python3
"""Exact arithmetic checks for the Round 44 scale-free candidate."""

from __future__ import annotations

import itertools
import math
import random


D = 941_541_228_773_064_677
H = 365
SLOPES = tuple(range(-6, 0)) + tuple(range(1, 7))


def rearrangement_table() -> list[int]:
    values = []
    for omitted in range(13):
        rows = [index for index in range(13) if index != omitted]
        maximum = sum(row * slope for row, slope in zip(sorted(rows), sorted(SLOPES)))
        minimum = sum(
            row * slope for row, slope in zip(sorted(rows), sorted(SLOPES, reverse=True))
        )
        assert minimum == -maximum
        values.append(maximum)
    return values


def main() -> None:
    assert sum(SLOPES) == 0
    table = rearrangement_table()
    assert table == [161, 167, 172, 176, 179, 181, 182, 181, 179, 176, 172, 167, 161]
    support_bounds = [2 * value + 1 for value in table]
    assert support_bounds == [323, 335, 345, 353, 359, 363, 365, 363, 359, 353, 345, 335, 323]
    assert max(table) == 182
    assert max(support_bounds) == H

    # Multiplication by -H/4 is injective on the integer frequency range.
    inv4 = pow(4, -1, D)
    mapped = {(-H * integer * inv4) % D for integer in range(-182, 183)}
    assert len(mapped) == 365

    # A shift by two cannot connect two frequencies in any cofactor support.
    for difference in range(-364, 365):
        assert (H * difference + 8) % D != 0
        assert abs(H * difference + 8) < D

    # Ordered-pair and Cauchy constants in the scale-free bound.
    assert 365 * 12 == 4_380
    assert 2 * 4_380 == 8_760
    assert math.isqrt(D + 1) == 970_330_474
    assert 970_330_474**2 < D + 1
    assert 970_330_474 / 2 > 8_760
    assert 36 * H < D  # implies 12*pi*H/D < pi/3

    # Numerical stress check of sum_{i!=j} e_i e_j <= 12 sum_i e_i^2.
    generator = random.Random(44)
    for _ in range(100):
        energies = [generator.random() * 10 for _ in range(13)]
        ordered_cross = sum(
            energies[i] * energies[j]
            for i in range(13)
            for j in range(13)
            if i != j
        )
        square_sum = sum(value * value for value in energies)
        assert ordered_cross <= 12 * square_sum + 1e-10

    print(
        "PASS Round 44 rearrangement table, support injection, opposite-spike "
        "exclusion, scale-free constants, and contradiction arithmetic"
    )


if __name__ == "__main__":
    main()
