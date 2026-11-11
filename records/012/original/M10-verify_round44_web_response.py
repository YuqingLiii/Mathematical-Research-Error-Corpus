#!/usr/bin/env python3
"""Receipt and exact-arithmetic checks for the Round 44 response."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "artifacts" / "web-gpt56sol-pro" / "round-44-prompt-sent.md"
PROMPT_SOURCE = ROOT / "work" / "round-44-prompt.md"
RESPONSE = ROOT / "artifacts" / "web-gpt56sol-pro" / "round-44-response.md"
OUTPUT = ROOT / "outputs" / "round-44-gpt56sol-pro-response.md"

PROMPT_SHA = "55126a37ce15032c0ba4afc5f3a1f5259d9a0e6df38fc9d6bbac9fb441198779"
RESPONSE_SHA = "d3735763cbbe7b33f212a5b935f73de6ac475ed7a5d7574fd3aad833bce85490"
D = 941_541_228_773_064_677


def receipt_and_scope_checks() -> None:
    prompt = PROMPT.read_bytes()
    response = RESPONSE.read_bytes()
    assert prompt == PROMPT_SOURCE.read_bytes()
    assert response == OUTPUT.read_bytes()
    assert hashlib.sha256(prompt).hexdigest() == PROMPT_SHA
    assert hashlib.sha256(response).hexdigest() == RESPONSE_SHA
    assert len(prompt) == 7_266 and len(prompt.decode("utf-8")) == 7_264
    assert prompt.count(b"\n") == 294
    assert len(response) == 16_769 and len(response.decode("utf-8")) == 16_754
    assert response.count(b"\n") == 1_006
    text = response.decode("utf-8")
    for heading in (
        "# VERIFIED",
        "# CORRECTED",
        "# DISPROVED",
        "# NECESSARY-ONLY",
        "# EQUIVALENT",
        "# NUMERICAL-ONLY",
        "# CONJECTURED",
        "# OPEN",
    ):
        assert text.count(heading) == 1, heading
    for needle in (
        "ConsecutiveTwelveSlopeExclusion",
        "Affine-Consecutive Twelve-Slope Exclusion",
        "No general thirteen-slope theorem is proved.",
        "PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.",
        "Twelve-slope sets not affinely equivalent to the consecutive family.",
        "C_{ii}(2)=0",
        "\\mathcal O<4173E",
    ):
        assert needle in text, needle


def support_and_spectral_checks() -> None:
    slopes = tuple(range(-6, 0)) + tuple(range(1, 7))
    table = []
    for omitted in range(13):
        rows = [row for row in range(13) if row != omitted]
        maximum = sum(row * slope for row, slope in zip(sorted(rows), sorted(slopes)))
        minimum = sum(row * slope for row, slope in zip(sorted(rows), sorted(slopes, reverse=True)))
        assert minimum == -maximum
        assert maximum == 182 - abs(omitted - 6) * (abs(omitted - 6) + 1) // 2
        table.append(maximum)
    assert table == [161, 167, 172, 176, 179, 181, 182, 181, 179, 176, 172, 167, 161]
    supports = [2 * value + 1 for value in table]
    assert supports == [323, 335, 345, 353, 359, 363, 365, 363, 359, 353, 345, 335, 323]

    at_4172 = sum(Fraction(size, 4172 + size) for size in supports) - 1
    at_4173 = sum(Fraction(size, 4173 + size) for size in supports) - 1
    assert at_4172 == Fraction(
        236_238_967_578_020_997_584,
        1_544_137_792_611_644_278_039_225,
    )
    assert at_4172 > 0
    assert at_4173 < 0


def frequency_and_contradiction_checks() -> None:
    h = 365
    inv4 = pow(4, -1, D)
    assert len({(-h * k * inv4) % D for k in range(-182, 183)}) == 365
    for difference in range(-364, 365):
        integer = h * difference + 8
        assert abs(integer) < D
        assert integer != 0
        assert integer % D != 0
    assert 365 * 12 == 4_380
    assert 2 * 4_380 == 8_760
    assert 2 * 4_173 == 8_346
    assert 36 * h < D
    assert 970_330_474**2 < D + 1
    assert 970_330_474 // 2 == 485_165_237 > 8_760


def affine_extension_checks() -> None:
    base_slopes = tuple(range(-6, 0)) + tuple(range(1, 7))
    differences = tuple(range(-364, 0)) + tuple(range(1, 365))
    assert len(differences) == 728
    for scale in (1, 2, 7, 123_456_789, D - 1):
        forbidden = {
            (-8 * pow((scale * difference) % D, -1, D)) % D
            for difference in differences
        }
        candidates = range(1, 730)
        safe = [h for h in candidates if h not in forbidden]
        assert safe
        h = safe[0]
        assert 12 * h < D
        assert 36 * h < D
        for difference in differences:
            assert (scale * h * difference + 8) % D != 0

    # The additive slope shift is permutation-independent, while the centered
    # part retains precisely the same K-values.  A four-slope analogue checks
    # the algebra exhaustively.
    rows = [0, 1, 2, 4]
    centered = [-2, -1, 1, 2]
    mu, scale, r0, h = 9, 5, 3, 17
    values_by_permutation = []
    for permutation in itertools.permutations(centered):
        direct = sum(
            (mu + scale * slope) * (r0 + h * row)
            for row, slope in zip(rows, permutation)
        )
        k_value = sum(row * slope for row, slope in zip(rows, permutation))
        common = mu * (len(rows) * r0 + h * sum(rows))
        assert direct == common + scale * h * k_value
        values_by_permutation.append((direct - common) // (scale * h))
    assert set(values_by_permutation) == {
        sum(row * slope for row, slope in zip(rows, permutation))
        for permutation in itertools.permutations(centered)
    }


def main() -> None:
    receipt_and_scope_checks()
    support_and_spectral_checks()
    frequency_and_contradiction_checks()
    affine_extension_checks()
    print(
        "PASS Round 44 receipt, support table, spectral bracket, spike exclusion, "
        "contradiction constants, and affine-extension checks"
    )


if __name__ == "__main__":
    main()
