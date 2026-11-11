#!/usr/bin/env python3
"""Independent exact checks for the archived Round 47 response."""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-47-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-47-prompt-sent.md"
RESPONSE = ROOT / "artifacts/web-gpt56sol-pro/round-47-response.md"
OUTPUT = ROOT / "outputs/round-47-gpt56sol-pro-response.md"

PROMPT_SHA = "a84dd92bbffcb69c9de4cbb161196cde9c81ee12cb76d4d7c996b1cd147fcbcf"
RESPONSE_SHA = "ff2e89d7f42dfc8ffb4674834eaa214092cb9a41710dc53e269b9f9f952d348d"

D = 941_541_228_773_064_677
M = 970_330_474
SAFE_TARGET = 970_330_473
EPSILON_DENOMINATOR = 1_805_000_000_000

EXPECTED_SUPPORT = (
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
)


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
    return (2**5) * factorial(5) // denominator


def ratio_two_tables() -> tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]]:
    support: list[int] = []
    classes: list[int] = []
    levels: list[int] = []
    for deleted in range(13):
        retained = tuple(row for row in range(13) if row != deleted)
        groups: dict[int, set[tuple[int, ...]]] = {}
        for u in retained:
            for v in retained:
                if u == v:
                    continue
                level = 3 * u + v
                remaining = tuple(row for row in retained if row not in (u, v))
                groups.setdefault(level, set()).update(matching_patterns(remaining))
        support.append(
            sum(
                sum(pattern_weight(pattern) for pattern in patterns)
                for patterns in groups.values()
            )
        )
        classes.append(sum(len(patterns) for patterns in groups.values()))
        levels.append(len(groups))
    return tuple(support), tuple(classes), tuple(levels)


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert RESPONSE.read_bytes() == OUTPUT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 6_190, 241)
    assert receipt(RESPONSE) == (RESPONSE_SHA, 23_688, 1_276)

    text = RESPONSE.read_text()
    for marker in (
        "# Verdict",
        "SmallIntegerRatioTwoOneDefectExclusion",
        "TwoCharacterBlockSupportOptimality",
        "1029398144",
        "59067671",
        "93\\cdot49^5-1",
        "26270198156",
        "970330473",
        "43016553",
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

    support, classes, levels = ratio_two_tables()
    assert support == EXPECTED_SUPPORT
    assert sum(support) == 1_029_398_144
    assert classes == (
        30_731, 37_829, 40_942, 44_147, 44_338, 46_282, 45_572,
        46_282, 44_338, 44_147, 40_942, 37_829, 30_731,
    )
    assert sum(classes) == 534_110
    assert levels == (43, 46, 46, 47, 46, 47, 47, 47, 46, 47, 46, 46, 43)
    assert tuple(value // 32 for value in support) == (
        1_717_104, 2_205_506, 2_458_844, 2_683_241, 2_741_776,
        2_862_852, 2_830_046, 2_862_852, 2_741_776, 2_683_241,
        2_458_844, 2_205_506, 1_717_104,
    )
    assert sum(value // 32 for value in support) == 32_168_692

    levels_full = {3 * u + v for u in range(13) for v in range(13) if u != v}
    assert levels_full == set(range(1, 48))
    safe_candidates = 93 * 49**5
    assert safe_candidates == 26_270_198_157
    assert safe_candidates - 1 == 26_270_198_156
    assert safe_candidates < D
    assert 7 * D - 264 * 950_000 * safe_candidates == 2_222_903_635_852_739

    assert D == M * M + 1
    assert M * (EPSILON_DENOMINATOR - 1) > SAFE_TARGET * EPSILON_DENOMINATOR
    assert sum(support) - M == 59_067_670
    assert sum(support) - SAFE_TARGET == 59_067_671

    expected_k = {
        2: 409_743_360,
        4: 616_771_584,
        5: 720_285_696,
        6: 823_799_808,
        7: 927_313_920,
    }
    for kappa, expected in expected_k.items():
        bound = 13 * (47 + 24 * kappa) * 24**4
        assert bound == expected
        assert bound < SAFE_TARGET
    assert SAFE_TARGET - expected_k[7] == 43_016_553
    assert 13 * (47 + 24 * 8) * 24**4 == 1_030_828_032 > SAFE_TARGET

    print("round47 verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"response receipt: {receipt(RESPONSE)}")
    print(f"support counts: {support}")
    print(f"support checksum: {sum(support)}")
    print(f"safe-spacing candidates: {safe_candidates}")
    print(f"closest stated subclass margin: {SAFE_TARGET - expected_k[7]}")


if __name__ == "__main__":
    main()
