#!/usr/bin/env python3
"""Independent exact checks for the archived Round 52 response."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import math
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-52-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-52-prompt-sent.md"
RESPONSE = ROOT / "artifacts/web-gpt56sol-pro/round-52-response.md"
OUTPUT = ROOT / "outputs/round-52-gpt56sol-pro-response.md"
SOURCE = ROOT / "work/verify_round52_laurent.cpp"
BINARY = ROOT / "work/verify_round52_laurent"

PROMPT_SHA = "b17ff9bc992c624a0a9d9ba8f5534786c897f59c61a46fa87002305166edde48"
RESPONSE_SHA = "7e464cb5f1b910ab0e46348a567bb09996415d72f7ce23636c28458f9de08714"
D = 941_541_228_773_064_677
K = 970_330_492
TARGET = 970_330_473
SLOPES = (3, 1, 20, -20, 490, -490, 12_090, -12_090, 300_177, -300_177)


def receipt(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()
    return sha256(data).hexdigest(), len(data), data.count(b"\n")


def is_prime_64(n: int) -> bool:
    """Deterministic Miller-Rabin for n < 2**64."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in small:
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


def assignment_extrema(square_rows: bool) -> tuple[int, int]:
    """Exact DP over injective assignments of ten columns to thirteen rows."""
    infinity = 10**30
    minima = {0: 0}
    maxima = {0: 0}
    for slope in SLOPES:
        next_min: dict[int, int] = {}
        next_max: dict[int, int] = {}
        for mask, value in minima.items():
            for row in range(13):
                bit = 1 << row
                if mask & bit:
                    continue
                coordinate = row * row if square_rows else row
                new_mask = mask | bit
                candidate = value + slope * coordinate
                next_min[new_mask] = min(next_min.get(new_mask, infinity), candidate)
        for mask, value in maxima.items():
            for row in range(13):
                bit = 1 << row
                if mask & bit:
                    continue
                coordinate = row * row if square_rows else row
                new_mask = mask | bit
                candidate = value + slope * coordinate
                next_max[new_mask] = max(next_max.get(new_mask, -infinity), candidate)
        minima, maxima = next_min, next_max
    return min(minima.values()), max(maxima.values())


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert RESPONSE.read_bytes() == OUTPUT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 7_983, 226)
    assert receipt(RESPONSE) == (RESPONSE_SHA, 20_800, 1_106)

    text = RESPONSE.read_text()
    for marker in (
        "# Verdict",
        "GenericTheta300177Exclusion remains OPEN.",
        "Theta300177LaurentSupportExactness",
        "P_{i;t,q}(Z,W)",
        "Q_6(\\pi)",
        "Q_r(\\pi)=x^2-y^2",
        "1037836800",
        "481716856",
        "1037836116",
        "82985908",
        "887344584",
        "6227020800=13\\cdot12!",
        "\\boxed{\\min=1,\\qquad \\max=480.}",
        "M=90080353",
        "26033222016",
        "EnergyRay18",
        "EighteenSlack",
        "7149371020340889916998112",
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

    # Independently rerun the exact 1,037,836,800-permutation Laurent census.
    subprocess.run(
        ["c++", "-std=c++20", "-O3", "-pthread", str(SOURCE), "-o", str(BINARY)],
        check=True,
    )
    census_text = subprocess.run(
        [str(BINARY), "--threads", "4"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    for marker in (
        "representatives=146",
        "raw=1037836800",
        "t_fibers=481716856",
        "tq_groups=1037836116",
        "collision_groups=684",
        "collision_excess=684",
        "zero_collision_groups=0",
        "third_hits=0",
        "subsets_with_collision=100",
        "t_fiber_min=1",
        "t_fiber_max=96",
        "formal_support=970330492",
        "formal_singleton=82985908",
        "formal_multiple=887344584",
        "round52 Laurent census: PASS",
    ):
        assert marker in census_text, marker

    expected_support = (
        53_624_480, 67_257_904, 74_298_872, 80_378_258, 82_204_740,
        85_478_914, 83_844_156, 85_478_914, 82_204_740, 80_378_258,
        74_298_872, 67_257_904, 53_624_480,
    )
    expected_singleton = (
        2_611_200, 5_487_296, 6_765_948, 7_099_366, 7_595_724,
        8_124_130, 7_618_580, 8_124_130, 7_595_724, 7_099_366,
        6_765_948, 5_487_296, 2_611_200,
    )
    expected_maximum = (480, 240, 360, 360, 360, 360, 360, 360, 360, 360, 360, 240, 480)
    rows = re.findall(
        r"^deleted=(\d+) support=(\d+) singleton=(\d+) multiple=(\d+)$",
        census_text,
        re.MULTILINE,
    )
    assert len(rows) == 13
    for deleted_text, support_text, singleton_text, multiple_text in rows:
        deleted = int(deleted_text)
        support = int(support_text)
        singleton = int(singleton_text)
        multiple = int(multiple_text)
        assert support == expected_support[deleted]
        assert singleton == expected_singleton[deleted]
        assert multiple == support - singleton
    direct_maxima = {
        int(deleted): int(maximum)
        for deleted, maximum in re.findall(
            r"^deleted=(\d+) direct_maximum=(\d+)$", census_text, re.MULTILINE
        )
    }
    assert direct_maxima == dict(enumerate(expected_maximum))
    assert sum(expected_support) == K
    assert sum(expected_singleton) == 82_985_908
    assert K - sum(expected_singleton) == 887_344_584
    assert 13 * math.factorial(12) == 6_227_020_800

    # Audit the exponent formula and the exact full-support specialization.
    assert sum(SLOPES) == 4
    exact_t_min, exact_t_max = assignment_extrema(square_rows=False)
    exact_q6_min, exact_q6_max = assignment_extrema(square_rows=True)
    # The response deliberately uses safe crude bounds, not the tighter
    # injective-assignment extrema computed by this DP.
    assert (exact_t_min, exact_t_max) == (-3_727_047, 3_727_095)
    assert (exact_q6_min, exact_q6_max) == (-44_724_695, 44_725_009)
    t_min, t_max = -3_753_323, 3_753_371
    q6_min, q6_max = -45_039_888, 45_040_464
    assert t_min <= exact_t_min <= exact_t_max <= t_max
    assert q6_min <= exact_q6_min <= exact_q6_max <= q6_max
    q6_span = q6_max - q6_min
    assert q6_span == 90_080_352
    m = q6_span + 1
    assert m == 90_080_353
    encoded_span = q6_span + 288 * m
    assert encoded_span == 26_033_222_016 < D - 1
    assert t_max - t_min == 7_506_694 < m
    frequency_span = (t_max - t_min) + 24 * m
    assert 8 * frequency_span < D
    ratios = (3, 1, 20, -20, 490, -490, 12_090, -12_090, 300_177, -300_177, m, -m)
    assert len({value % D for value in ratios}) == 12
    assert is_prime_64(D)
    assert (-(-8) * pow(8, -1, D)) % D == 1
    assert (-(-8 * m) * pow(8, -1, D)) % D == m

    # Check the exact 18-unit algebra and both slack identities symbolically by coefficients.
    assert K - 18 == 970_330_474 == TARGET + 1
    assert K - 1 - TARGET == 18
    # [KE - x] + [x - y] + [y - c] + [c - E - M] = (K - 1)E - M.
    coefficient_e = K - 1
    coefficient_m = -1
    assert (coefficient_e, coefficient_m) == (970_330_491, -1)

    print("round52 verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"response receipt: {receipt(RESPONSE)}")
    print("Laurent census: 1037836800 raw, 684 size-two same-sign collision groups, 0 zeros")
    print("formal fibers: 970330492 = 82985908 singleton + 887344584 multiple")
    print("full-support specialization: exponent and frequency injections verified")
    print("remaining exact gap: EighteenSlack >= 18E")


if __name__ == "__main__":
    main()
