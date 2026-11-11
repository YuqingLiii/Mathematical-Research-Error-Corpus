#!/usr/bin/env python3
"""Independent exact checks for the archived Round 45 response."""

from __future__ import annotations

from functools import lru_cache
from fractions import Fraction
from hashlib import sha256
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-45-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-45-prompt-sent.md"
RESPONSE = ROOT / "artifacts/web-gpt56sol-pro/round-45-response.md"
OUTPUT = ROOT / "outputs/round-45-gpt56sol-pro-response.md"

PROMPT_SHA = "9fc9125732d779c0a3234c60202cdac42fb50c88370e0a538c937762aa77fa52"
RESPONSE_SHA = "35008be6ef363f499a4f5cd7b7f18b4d1c181c877da75bb8cdaa1c1bdcb569ff"

D = 941_541_228_773_064_677
M = 970_330_474
EXPECTED_PATTERN_COUNTS = (
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
)
EXPECTED_SUPPORT_COUNTS = (
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
)


def receipt(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()
    return sha256(data).hexdigest(), len(data), data.count(b"\n")


@lru_cache(maxsize=None)
def matching_patterns(vertices: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    """All sorted absolute-edge-difference multisets of perfect matchings."""
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


def labeled_oriented_count(patterns: frozenset[tuple[int, ...]]) -> int:
    total = 0
    for pattern in patterns:
        denominator = 1
        for difference in set(pattern):
            denominator *= factorial(pattern.count(difference))
        total += (2**6) * factorial(6) // denominator
    return total


def secular_error(x: int, support_counts: tuple[int, ...]) -> Fraction:
    return sum((Fraction(n, x + n) for n in support_counts), start=Fraction()) - 1


def is_prime_64(n: int) -> bool:
    """Deterministic Miller--Rabin for unsigned 64-bit integers."""
    if n < 2:
        return False
    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert RESPONSE.read_bytes() == OUTPUT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 7349, 279)
    assert receipt(RESPONSE) == (RESPONSE_SHA, 19600, 1166)

    response_text = RESPONSE.read_text()
    required_markers = (
        "# Verdict",
        "FullWienerSquareBound",
        "SixPairTwelveSlopeExclusion",
        "CentralAffineExtension",
        "49^6-1=13841287200",
        "508658597<\\Lambda_*<508658598",
        "552596672\\,E",
        "|T_1|>\\frac{17}{18}E",
        "PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.",
        "# VERIFIED",
        "# CORRECTED",
        "# DISPROVED",
        "# NECESSARY-ONLY",
        "# EQUIVALENT",
        "# NUMERICAL-ONLY",
        "# CONJECTURED",
        "# OPEN",
    )
    for marker in required_markers:
        assert marker in response_text, marker

    assert D == M * M + 1
    assert is_prime_64(D)

    pattern_counts: list[int] = []
    support_counts: list[int] = []
    all_rows = tuple(range(13))
    for deleted in all_rows:
        vertices = tuple(v for v in all_rows if v != deleted)
        patterns = matching_patterns(vertices)
        pattern_counts.append(len(patterns))
        support_counts.append(labeled_oriented_count(patterns))

    assert tuple(pattern_counts) == EXPECTED_PATTERN_COUNTS
    assert tuple(support_counts) == EXPECTED_SUPPORT_COUNTS
    assert sum(pattern_counts) == 33_886
    assert tuple(n // 64 for n in support_counts) == (
        422001,
        579650,
        664496,
        729608,
        773663,
        808748,
        677991,
        808748,
        773663,
        729608,
        664496,
        579650,
        422001,
    )
    assert sum(n // 64 for n in support_counts) == 8_634_323
    full_wiener_constant = sum(support_counts)
    assert full_wiener_constant == 552_596_672

    low_error = secular_error(508_658_597, tuple(support_counts))
    high_error = secular_error(508_658_598, tuple(support_counts))
    assert low_error > 0
    assert high_error < 0
    assert low_error.numerator == 5_024_366_318_856_287_115_322_208_015_053_637_047_659_649_757_302_771
    assert low_error.denominator == 15_453_290_821_421_479_918_856_452_677_979_994_900_066_166_369_888_400_970_070_733
    assert high_error.numerator == -2_231_703_814_696_354_740_166_836_012_191_559_964_345_062_079
    assert high_error.denominator == 1_503_004_495_185_634_616_689_732_921_258_782_154_774_534_153_638_099_615

    assert 2 * 508_658_598 - M == 46_986_722
    assert Fraction(46_986_722, M) > Fraction(48423, 1_000_000)
    assert Fraction(46_986_722, M) < Fraction(48424, 1_000_000)

    crude_forbidden = sum(n * (n - 1) for n in support_counts)
    assert crude_forbidden == 24_333_724_302_039_872
    coefficient_vectors = 49**6
    assert coefficient_vectors == 13_841_287_201
    assert coefficient_vectors - 1 == 13_841_287_200
    assert coefficient_vectors < D

    # With h <= 49^6 and pi < 22/7, the phase half-width is < 1/3.
    assert 792 * coefficient_vectors < 7 * D
    # Since cos(t) >= 1-t^2/2, t < 1/3 yields cos(t) > 17/18.
    assert Fraction(1) - Fraction(1, 2) * Fraction(1, 3) ** 2 == Fraction(17, 18)

    # The exact contradiction uses sqrt(D+1) > M.
    assert D + 1 > M * M
    assert 17 * M > 18 * full_wiener_constant

    print("round45 verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"response receipt: {receipt(RESPONSE)}")
    print(f"pattern counts: {tuple(pattern_counts)}")
    print(f"support counts: {tuple(support_counts)}")
    print(f"full Wiener constant: {full_wiener_constant}")
    print(f"Perron signs: low={low_error > 0}, high={high_error < 0}")
    print(f"forbidden coefficient vectors: {coefficient_vectors - 1}")
    print(f"contradiction margin: {17 * M - 18 * full_wiener_constant}")


if __name__ == "__main__":
    main()
