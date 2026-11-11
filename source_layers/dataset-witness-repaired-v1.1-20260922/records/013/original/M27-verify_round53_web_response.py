#!/usr/bin/env python3
"""Independent exact checks for the archived Round 53 response."""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import math
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-53-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-53-prompt-sent.md"
RESPONSE = ROOT / "artifacts/web-gpt56sol-pro/round-53-response.md"
OUTPUT = ROOT / "outputs/round-53-gpt56sol-pro-response.md"
ROUND52_BINARY = ROOT / "work/verify_round52_laurent"

PROMPT_SHA = "d1daefe3620945dd1a662cbe9f99bb808ec9efe8abe4dfe3cab113ca6396cec1"
RESPONSE_SHA = "d6bc54cc708e48701d83e0a44571e267a5b8a495a2ef4e21eccd07a8748c4e4c"

D = 941_541_228_773_064_677
K = 970_330_492
S = (
    53_624_480, 67_257_904, 74_298_872, 80_378_258, 82_204_740,
    85_478_914, 83_844_156, 85_478_914, 82_204_740, 80_378_258,
    74_298_872, 67_257_904, 53_624_480,
)
U = (
    2_611_200, 5_487_296, 6_765_948, 7_099_366, 7_595_724,
    8_124_130, 7_618_580, 8_124_130, 7_595_724, 7_099_366,
    6_765_948, 5_487_296, 2_611_200,
)
EXPECTED_LOSS = (326, 260, 235, 217, 212, 204, 208, 204, 212, 217, 235, 260, 326)
EXPECTED_ISOLATED = (
    2_610_548, 5_486_776, 6_765_478, 7_098_932, 7_595_300,
    8_123_722, 7_618_164, 8_123_722, 7_595_300, 7_098_932,
    6_765_478, 5_486_776, 2_610_548,
)


def receipt(path: Path) -> tuple[str, int, int, int]:
    data = path.read_bytes()
    text = data.decode()
    return sha256(data).hexdigest(), len(data), len(text), data.count(b"\n")


def largest_integer_strictly_below(value: Fraction) -> int:
    return (value.numerator - 1) // value.denominator


def rational_square_less(numerator: int, denominator: int, bound: Fraction) -> bool:
    """Check sqrt(numerator / denominator) < bound without floating point."""
    assert numerator >= 0 and denominator > 0 and bound >= 0
    return numerator * bound.denominator**2 < denominator * bound.numerator**2


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert RESPONSE.read_bytes() == OUTPUT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 9_164, 9_158, 265)
    assert receipt(RESPONSE) == (RESPONSE_SHA, 25_672, 25_652, 1_435)

    text = RESPONSE.read_text()
    for marker in (
        "# Verdict",
        "GenericTheta300177Exclusion remains OPEN.",
        "# 1. Exact physical domain",
        "C_{ii}(2)=0",
        "# 2. Exact near-equality rigidity",
        "5.8\\times10^{-4}",
        "82979676",
        "6232",
        "70/71<\\sqrt{E/K}<70/69",
        "# 4. Young-phase stability",
        "# 5. Physical-row grouping stability",
        "# 6. Direct cofactor-energy identities",
        "# 7. An exact array-level near-equality witness",
        "7815406983360860427850023498621204242",
        "# 8. Earliest exact missing lemma",
        "## Determinant Near-Equality Obstruction",
        "# 9. Finite exact next optimization",
        "# VERIFIED",
        "# CORRECTED",
        "# DISPROVED",
        "# NECESSARY-ONLY",
        "# EQUIVALENT",
        "# NUMERICAL-ONLY",
        "# CONJECTURED",
        "# OPEN",
        "PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.",
    ):
        assert marker in text, marker

    # Reuse the separately implemented exhaustive Laurent census to bind the
    # Round 53 support and singleton inputs to audited integer data.
    census = subprocess.run(
        [str(ROUND52_BINARY), "--threads", "4"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    rows = re.findall(
        r"^deleted=(\d+) support=(\d+) singleton=(\d+) multiple=(\d+)$",
        census,
        re.MULTILINE,
    )
    assert len(rows) == 13
    assert tuple(int(row[1]) for row in rows) == S
    assert tuple(int(row[2]) for row in rows) == U
    assert "formal_support=970330492" in census
    assert "formal_singleton=82985908" in census
    assert "formal_multiple=887344584" in census
    assert "round52 Laurent census: PASS" in census

    assert sum(S) == K
    assert sum(U) == 82_985_908
    assert S == tuple(reversed(S))
    assert U == tuple(reversed(U))

    # Perron-ray identities and the coordinatewise bound.
    # K ||e - ((w.e)/K)w||^2 = KE - (w.e)^2 because ||w||^2=K.
    assert K - 18 == 970_330_474
    min_support = min(S)
    relative_squared = Fraction(18 * K, (K - 18) * min_support)
    assert rational_square_less(
        relative_squared.numerator,
        relative_squared.denominator,
        Fraction(58, 100_000),
    )
    assert rational_square_less(
        relative_squared.numerator,
        relative_squared.denominator,
        Fraction(1, 1_000),
    )
    assert (K - 18) * min_support - 18 * 10**6 * K == 34_567_518_240_403_520

    # Exact per-row integer support-loss ceilings from strict inequality (3.3).
    computed_loss = tuple(
        largest_integer_strictly_below(
            Fraction(18 * 10**6 * K * K, 998_001 * (K - 18) * support)
        )
        for support in S
    )
    assert computed_loss == EXPECTED_LOSS
    computed_isolated = tuple(singletons - 2 * loss for singletons, loss in zip(U, computed_loss))
    assert computed_isolated == EXPECTED_ISOLATED
    assert sum(computed_loss) == 3_116
    assert 2 * sum(computed_loss) == 6_232
    assert sum(computed_isolated) == 82_979_676

    # Certify every displayed square-root decimal upper bound exactly.
    i = 0
    assert rational_square_less(
        18 * K,
        S[i] * computed_isolated[i],
        Fraction(11_169_886, 10**9),
    )
    assert rational_square_less(
        18 * K,
        S[i] ** 2,
        Fraction(2_464_524, 10**9),
    )
    assert rational_square_less(
        18,
        S[i],
        Fraction(579_369, 10**9),
    )
    # 1 - sqrt(1-18/K) < 9.276e-9, checked by squaring the
    # equivalent positive inequality sqrt(1-18/K) > 1-q.
    q = Fraction(9_276, 10**12)
    assert Fraction(K - 18, K) > (1 - q) ** 2
    error_sum = (
        Fraction(11_169_886, 10**9)
        + Fraction(2_464_524, 10**9)
        + Fraction(579_369, 10**9)
        + q
    )
    assert error_sum < Fraction(1, 70)

    # Check the normalized distance decimal in (2.6) without evaluating a root.
    distance_bound = Fraction(18_551, 10**12)
    assert Fraction(K - 18, K) > (1 - distance_bound / 2) ** 2

    # The explicit relaxation has the exact claimed sizes and target spike.
    support_max = max(S)
    assert 4 * (support_max - 1) == 341_915_652 < D
    radius = 4 * (support_max - 1) + 1
    assert radius == 341_915_653
    # e_i^2=S_i/K, E=1, L_i=S_i/sqrt(K), hence the first three
    # slacks are identically zero and total ungrouped mass is K.
    assert sum(Fraction(support, K) for support in S) == 1
    # Correlation lags are divisible by four, so lag two is absent.  There is
    # no modular wrap in the positive direction; in the negative direction
    # equality would require 4n=2-D, impossible because D=1 (mod 4).
    assert 4 * (support_max - 1) < D
    assert D % 4 == 1 and (2 - D) % 4 != 0
    certificate = 98 * D * D - 10**7 * (K - 1) * (264 * radius) ** 2
    assert certificate == 7_815_406_983_360_860_427_850_023_498_621_204_242
    group_upper = Fraction((K - 1) * (264 * radius) ** 2, 98 * D * D)
    assert 0 < group_upper < Fraction(1, 10**7)

    # The physical reparameterization is algebraically exact:
    # m6=-8a/h^2 and mr=-8b/h^2 give ell=2(at+bq)/h;
    # h[m6 dt+mr dq] != -8 becomes a dt+b dq != h.
    for a, b, h, t, q_value in ((7, 11, 13, 17, 19), (23, 29, 31, -37, 41)):
        m6 = Fraction(-8 * a, h * h)
        mr = Fraction(-8 * b, h * h)
        ell_original = Fraction(-h, 4) * (m6 * t + mr * q_value)
        ell_reduced = Fraction(2, h) * (a * t + b * q_value)
        assert ell_original == ell_reduced

    print("round53 verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"response receipt: {receipt(RESPONSE)}")
    print("support-loss ceilings:", computed_loss)
    print("isolated singleton lower bound:", sum(computed_isolated))
    print("array relaxation group-slack upper bound:", group_upper)
    print("earliest gap: determinant-specific near-equality obstruction")


if __name__ == "__main__":
    main()
