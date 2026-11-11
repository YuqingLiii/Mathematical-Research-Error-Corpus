#!/usr/bin/env python3
"""Independent exact checks for the archived Round 46 response."""

from __future__ import annotations

from functools import lru_cache
from fractions import Fraction
from hashlib import sha256
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-46-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-46-prompt-sent.md"
RESPONSE = ROOT / "artifacts/web-gpt56sol-pro/round-46-response.md"
OUTPUT = ROOT / "outputs/round-46-gpt56sol-pro-response.md"

PROMPT_SHA = "22938c4b1c2df39b8481950a6053ad98aecc3616a073d1e63d208d8562845535"
RESPONSE_SHA = "69323698f9d0d1718592da03148310ea53fc805766e91c3f9e732a189f60b4f8"

D = 941_541_228_773_064_677
M = 970_330_474

EXPECTED_ONE_DEFECT = (
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
)
EXPECTED_ONE_DEFECT_CLASSES = (
    66_610,
    73_310,
    77_582,
    79_560,
    81_354,
    81_104,
    79_498,
    81_104,
    81_354,
    79_560,
    77_582,
    73_310,
    66_610,
)
EXPECTED_ALIGNED = (
    35_294_528,
    43_703_904,
    49_357_728,
    52_344_128,
    55_092_096,
    56_225_568,
    57_751_808,
    56_225_568,
    55_092_096,
    52_344_128,
    49_357_728,
    43_703_904,
    35_294_528,
)


def receipt(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()
    return sha256(data).hexdigest(), len(data), data.count(b"\n")


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


def pattern_weight(pattern: tuple[int, ...]) -> int:
    denominator = 1
    for difference in set(pattern):
        denominator *= factorial(pattern.count(difference))
    return (2**5) * factorial(5) // denominator


def one_defect_tables() -> tuple[tuple[int, ...], tuple[int, ...]]:
    counts: list[int] = []
    class_counts: list[int] = []
    for deleted in range(13):
        retained = tuple(v for v in range(13) if v != deleted)
        total = 0
        classes = 0
        for u in retained:
            for v in retained:
                if u == v:
                    continue
                remainder = tuple(x for x in retained if x not in (u, v))
                patterns = matching_patterns(remainder)
                classes += len(patterns)
                total += sum(pattern_weight(pattern) for pattern in patterns)
        counts.append(total)
        class_counts.append(classes)
    return tuple(counts), tuple(class_counts)


def aligned_tables() -> tuple[tuple[int, ...], tuple[int, ...]]:
    counts: list[int] = []
    class_counts: list[int] = []
    for deleted in range(13):
        retained = tuple(v for v in range(13) if v != deleted)
        total = 0
        classes = 0
        for u in retained:
            union: set[tuple[int, ...]] = set()
            for v in retained:
                if u == v:
                    continue
                remainder = tuple(x for x in retained if x not in (u, v))
                union.update(matching_patterns(remainder))
            classes += len(union)
            total += sum(pattern_weight(pattern) for pattern in union)
        counts.append(total)
        class_counts.append(classes)
    return tuple(counts), tuple(class_counts)


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert RESPONSE.read_bytes() == OUTPUT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 6550, 224)
    assert receipt(RESPONSE) == (RESPONSE_SHA, 22808, 1224)

    text = RESPONSE.read_text()
    for marker in (
        "# Verdict",
        "K_{\\rm supp}=2021966592",
        "AlignedOneDefectTwelveSlopeExclusion",
        "45\\cdot49^6-1",
        "622857924044",
        "641787712",
        "25\\cdot49^5-1",
        "7061881224",
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
    ):
        assert marker in text, marker

    one_defect, one_defect_classes = one_defect_tables()
    aligned, aligned_classes = aligned_tables()
    assert one_defect == EXPECTED_ONE_DEFECT
    assert one_defect_classes == EXPECTED_ONE_DEFECT_CLASSES
    assert sum(one_defect) == 2_021_966_592
    assert sum(one_defect_classes) == 998_538
    assert tuple(value // 32 for value in one_defect) == (
        3_906_586,
        4_502_800,
        4_884_952,
        5_130_666,
        5_277_668,
        5_299_474,
        5_182_164,
        5_299_474,
        5_277_668,
        5_130_666,
        4_884_952,
        4_502_800,
        3_906_586,
    )
    assert sum(value // 32 for value in one_defect) == 63_186_456

    assert aligned == EXPECTED_ALIGNED
    assert aligned_classes == (
        19_992,
        23_275,
        25_967,
        26_957,
        28_329,
        28_666,
        29_696,
        28_666,
        28_329,
        26_957,
        25_967,
        23_275,
        19_992,
    )
    assert sum(aligned_classes) == 336_068
    assert tuple(value // 32 for value in aligned) == (
        1_102_954,
        1_365_747,
        1_542_429,
        1_635_754,
        1_721_628,
        1_757_049,
        1_804_744,
        1_757_049,
        1_721_628,
        1_635_754,
        1_542_429,
        1_365_747,
        1_102_954,
    )
    assert sum(value // 32 for value in aligned) == 20_055_866
    assert sum(aligned) == 641_787_712

    full_forbidden = 45 * 49**6 - 1
    full_candidates = full_forbidden + 1
    aligned_forbidden = 25 * 49**5 - 1
    aligned_candidates = aligned_forbidden + 1
    assert full_forbidden == 622_857_924_044
    assert aligned_forbidden == 7_061_881_224
    assert full_candidates < D
    assert aligned_candidates < D
    assert 792 * full_candidates < 7 * D
    assert 792 * aligned_candidates < 7 * D
    assert 7 * D - 792 * full_candidates == 6_590_295_297_935_609_099
    assert 7 * D - 792 * aligned_candidates == 6_590_783_008_401_522_539

    target_over_support = Fraction(17 * M, 18 * sum(one_defect))
    assert target_over_support == Fraction(8_247_809_029, 18_197_699_328)
    assert Fraction(17 * M, 18) < sum(one_defect)
    assert 17 * M - 18 * sum(aligned) == 4_943_439_242 > 0

    print("round46 verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"response receipt: {receipt(RESPONSE)}")
    print(f"one-defect counts: {one_defect}")
    print(f"one-defect checksum: {sum(one_defect)}")
    print(f"aligned counts: {aligned}")
    print(f"aligned checksum: {sum(aligned)}")
    print(f"aligned contradiction margin: {17 * M - 18 * sum(aligned)}")


if __name__ == "__main__":
    main()
