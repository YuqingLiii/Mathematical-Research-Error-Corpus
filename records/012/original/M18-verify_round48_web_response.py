#!/usr/bin/env python3
"""Independent exact checks for the archived Round 48 response."""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-48-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-48-prompt-sent.md"
RESPONSE = ROOT / "artifacts/web-gpt56sol-pro/round-48-response.md"
OUTPUT = ROOT / "outputs/round-48-gpt56sol-pro-response.md"

PROMPT_SHA = "8282eea33070ddc6bd2481463e48d0cc2a84fc4861919bd8a1c43ef29241bbf6"
RESPONSE_SHA = "323707605a98d430023d37c73896fe922918aca1aec548d650e6dffa1e8cd248"

D = 941_541_228_773_064_677
M = 970_330_474
TARGET = 970_330_473
EPSILON_DENOMINATOR = 1_805_000_000_000

EXPECTED_TOTALS = {
    2: 211_854_128,
    3: 131_116_640,
    4: 320_592_976,
    5: 198_640_736,
    6: 430_377_536,
    7: 259_963_008,
    8: 533_770_816,
    9: 321_004_256,
    10: 628_744_464,
    11: 378_251_200,
    12: 710_785_248,
    13: 436_843_008,
    14: 786_470_368,
    15: 489_505_216,
    16: 856_650_560,
    17: 542_150_896,
    18: 920_817_248,
    19: 592_977_696,
    20: 974_917_184,
    21: 638_619_280,
    22: 1_011_957_984,
    23: 682_635_568,
    24: 1_029_398_144,
    25: 722_708_256,
    26: 1_029_398_144,
    27: 759_829_184,
    28: 1_029_398_144,
    29: 797_774_496,
    30: 1_029_398_144,
    31: 834_552_160,
    32: 1_029_398_144,
    33: 868_878_016,
    34: 1_029_398_144,
    35: 902_867_136,
    36: 1_029_398_144,
    37: 934_352_608,
    38: 1_029_398_144,
    39: 962_192_928,
    40: 1_029_398_144,
    41: 985_516_384,
    42: 1_029_398_144,
    43: 1_005_823_968,
    44: 1_029_398_144,
    45: 1_019_492_064,
    46: 1_029_398_144,
}

EXPECTED_ROWS = {
    8: (
        29_048_528, 37_000_944, 41_137_344, 44_083_088, 45_513_792,
        46_791_216, 46_620_992, 46_791_216, 45_513_792, 44_083_088,
        41_137_344, 37_000_944, 29_048_528,
    ),
    20: (
        53_624_480, 67_432_560, 74_666_656, 80_830_800, 82_706_752,
        86_002_000, 84_390_688, 86_002_000, 82_706_752, 80_830_800,
        74_666_656, 67_432_560, 53_624_480,
    ),
    39: (
        52_969_664, 66_573_392, 73_631_872, 79_719_104, 81_669_040,
        85_007_360, 83_052_064, 85_007_360, 81_669_040, 79_719_104,
        73_631_872, 66_573_392, 52_969_664,
    ),
}


def receipt(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()
    return sha256(data).hexdigest(), len(data), data.count(b"\n")


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


def pattern_weight(pattern: tuple[int, ...]) -> int:
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
                        level = 3 * u + v + kappa * (a - b)
                        remaining = tuple(
                            row for row in after_defect if row not in (a, b)
                        )
                        groups.setdefault(level, set()).update(
                            matching_patterns(remaining)
                        )
        per_deleted.append(
            sum(
                sum(pattern_weight(pattern) for pattern in patterns)
                for patterns in groups.values()
            )
        )
    return tuple(per_deleted)


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert RESPONSE.read_bytes() == OUTPUT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 7_306, 254)
    assert receipt(RESPONSE) == (RESPONSE_SHA, 25_954, 1_419)

    text = RESPONSE.read_text()
    for marker in (
        "# Verdict",
        "ExtendedIntegerRatioTwoOneDefectExclusion",
        "974917183",
        "4586710",
        "K_{20,203}^{\\rm rect}",
        "970265088",
        "974578176",
        "Two-Ratio Exclusion",
        "1\\le|\\lambda|\\le203",
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

    computed: dict[int, int] = {}
    for kappa, expected in EXPECTED_TOTALS.items():
        rows = exact_support(kappa)
        computed[kappa] = sum(rows)
        assert computed[kappa] == expected, (kappa, computed[kappa], expected)
        if kappa in EXPECTED_ROWS:
            assert rows == EXPECTED_ROWS[kappa], (kappa, rows)

    unfurled = 1_029_398_144
    for kappa in range(24, 47, 2):
        assert computed[kappa] == unfurled
    assert exact_support(47) == exact_support(48)
    assert sum(exact_support(47)) == unfurled

    passing = {
        kappa for kappa, total in computed.items() if total - 1 <= TARGET
    }
    assert passing == {
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        18, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
    }
    # Kappa 3 is numerically passing but forbidden by distinctness; kappa 1
    # is likewise forbidden, so the theorem's admissible set removes 3.
    theorem_set = passing - {3}
    assert theorem_set == {
        2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
        19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
    }

    assert D == M * M + 1
    assert M * (EPSILON_DENOMINATOR - 1) > TARGET * EPSILON_DENOMINATOR
    assert EXPECTED_TOTALS[20] - 1 - TARGET == 4_586_710
    assert TARGET - (EXPECTED_TOTALS[39] - 1) == 8_137_546
    assert EXPECTED_TOTALS[41] - 1 - TARGET == 15_185_910

    rect_203 = 13 * (527 + 24 * 203) * 24**3
    rect_204 = 13 * (527 + 24 * 204) * 24**3
    assert rect_203 == 970_265_088
    assert TARGET - rect_203 == 65_385
    assert TARGET - (rect_203 - 1) == 65_386
    assert rect_204 == 974_578_176
    assert rect_204 - TARGET == 4_247_703
    assert rect_204 - 1 - TARGET == 4_247_702

    support_20 = EXPECTED_ROWS[20]
    assert max(support_20) == 86_002_000
    assert 4 * (max(support_20) - 1) < D
    assert D % 4 == 1
    # If n is a represented difference with |n|<D and 4|n, then n cannot be
    # congruent to 2 modulo D: the only candidates are 2 and 2-D, neither 0 mod 4.
    assert 2 % 4 != 0 and (2 - D) % 4 != 0

    print("round48 verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"response receipt: {receipt(RESPONSE)}")
    print(f"verified kappa totals: {len(computed)} entries through 46")
    print(f"kappa=20 sharp gap: {EXPECTED_TOTALS[20] - 1 - TARGET}")
    print(f"two-ratio rectangular endpoint: {rect_203}")


if __name__ == "__main__":
    main()
