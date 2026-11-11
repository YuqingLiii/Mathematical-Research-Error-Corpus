#!/usr/bin/env python3
"""Independent exact checks for the archived Round 51 response."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-51-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-51-prompt-sent.md"
RESPONSE = ROOT / "artifacts/web-gpt56sol-pro/round-51-response.md"
OUTPUT = ROOT / "outputs/round-51-gpt56sol-pro-response.md"
SOURCE = ROOT / "work/enumerate_round51_four_ratio.cpp"
BINARY = ROOT / "work/enumerate_round51_four_ratio"
CRITICAL_SCAN = ROOT / "work/round51-critical-full-scan.txt"
LOW_COLLISION = ROOT / "work/round51-low-collision-summary.txt"

PROMPT_SHA = "e13dfdedf8f04f9871f50c47a077b46c7be0bffeedf3ad69cee948889db30614"
RESPONSE_SHA = "e51c333bd1aa1bf8b36887af8b6bc387bc020601c81eab1d9404b6f75f8a9b79"
TARGET = 970_330_473
PASS_LIMIT = TARGET + 1
SATURATED = 970_343_224
EXCEPTIONS = {
    300_178, 300_180, 300_182, 300_184, 300_186, 300_188,
    300_190, 300_192, 300_195, 300_197, 300_199, 300_201,
    300_203, 300_205, 300_220,
}

EXPECTED_SELECTED = {
    116_982: 653_612_792,
    116_983: 637_805_190,
    150_000: 739_935_564,
    200_000: 855_376_712,
    250_000: 933_982_600,
    300_000: 970_296_048,
    300_176: 970_322_512,
    300_177: 970_330_492,
    300_178: 970_321_472,
    300_220: 970_330_348,
    300_302: 970_343_224,
    300_303: 970_343_224,
    302_447: 970_343_224,
}


def receipt(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()
    return sha256(data).hexdigest(), len(data), data.count(b"\n")


def assignment(values: tuple[int, ...], deleted: int = 4) -> tuple[int, int, int]:
    assert len(values) == 12
    assert len(set(values)) == 12
    assert set(values) == set(range(13)) - {deleted}
    u, v, ap, am, bp, bm, cp, cm, x, y, g, h = values
    t0 = 3 * u + v + 20 * (ap - am) + 490 * (bp - bm) + 12_090 * (cp - cm)
    return t0, x - y, g - h


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert RESPONSE.read_bytes() == OUTPUT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 8_172, 266)
    assert receipt(RESPONSE) == (RESPONSE_SHA, 19_953, 1_225)

    text = RESPONSE.read_text()
    for marker in (
        "# Verdict",
        "ExtendedEta12090FourthRatioExclusion",
        "Theta300177FifthRatioExclusion",
        "300178,300180,300182,300184,300186,300188",
        "300203,300205,300220",
        "K^{(4)}_{300177}=970330492",
        "K^{(4)}_{300220}=970330348",
        "last even collision value}=300284",
        "last odd collision value}=300301",
        "|\\theta|\\ge300302",
        "131974409852556",
        "30190751891579666896",
        "7149371020340881916998112",
        "31687862306776",
        "27020159369932",
        "2058618643449205948",
        "1754604114323772216",
        "189488938022181601177204",
        "161400866866551803426992",
        "2797343",
        "970330179",
        "970330491",
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

    subprocess.run(
        [
            "c++", "-std=c++20", "-O3", "-pthread",
            str(SOURCE), "-o", str(BINARY),
        ],
        check=True,
    )
    selected_text = subprocess.run(
        [str(BINARY), *(str(theta) for theta in EXPECTED_SELECTED)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    selected_pattern = re.compile(
        r"^theta=(\d+) exact=(\d+) sharp_margin=(-?\d+)\n"
        r"  support=\(([^)]*)\)$",
        re.MULTILINE,
    )
    selected = {}
    for match in selected_pattern.finditer(selected_text):
        theta, exact, margin = map(int, match.group(1, 2, 3))
        support = tuple(map(int, match.group(4).split(",")))
        assert len(support) == 13
        assert sum(support) == exact
        assert margin == TARGET - (exact - 1)
        selected[theta] = exact, margin, support
    assert set(selected) == set(EXPECTED_SELECTED)
    for theta, expected in EXPECTED_SELECTED.items():
        assert selected[theta][0] == expected

    assert selected[116_983][2] == (
        38_501_902, 45_642_450, 49_073_650, 51_909_066, 52_849_566,
        54_110_020, 53_631_882, 54_110_020, 52_849_566, 51_909_066,
        49_073_650, 45_642_450, 38_501_902,
    )
    assert selected[300_177][2] == (
        53_624_480, 67_257_904, 74_298_872, 80_378_258, 82_204_740,
        85_478_914, 83_844_156, 85_478_914, 82_204_740, 80_378_258,
        74_298_872, 67_257_904, 53_624_480,
    )
    assert selected[300_177][1] == -18
    assert selected[300_220][1] == 126

    critical_rows = {}
    for match in re.finditer(
        r"^theta=(\d+) exact=(\d+) sharp_margin=(-?\d+)$",
        CRITICAL_SCAN.read_text(),
        re.MULTILINE,
    ):
        theta, exact, margin = map(int, match.groups())
        assert margin == TARGET - (exact - 1)
        critical_rows[theta] = exact
    assert list(critical_rows) == list(range(150_152, 300_302))
    assert sum(critical_rows.values()) == 131_974_409_852_556
    assert sum(t * k for t, k in critical_rows.items()) == 30_190_751_891_579_666_896
    assert (
        sum(t * t * k for t, k in critical_rows.items())
        == 7_149_371_020_340_889_916_998_112
    )

    critical_passing = {t for t, k in critical_rows.items() if k <= PASS_LIMIT}
    expected_critical = set(range(150_152, 300_177)) | EXCEPTIONS
    assert critical_passing == expected_critical
    assert len(critical_passing) == 150_040
    assert len(critical_rows) - len(critical_passing) == 110

    raw_passing = set(range(1, 150_152)) | critical_passing
    expected_raw = set(range(1, 300_177)) | EXCEPTIONS
    assert raw_passing == expected_raw
    assert len(raw_passing) == 300_191
    assert sum(raw_passing) == 45_057_468_476
    assert sum(t * t for t in raw_passing) == 9_017_246_088_045_214
    assert min(t for t in critical_rows if t not in critical_passing) == 300_177
    assert min((PASS_LIMIT - critical_rows[t], t) for t in critical_passing) == (126, 300_220)
    assert max(t for t in critical_passing) == 300_220

    last_even = max(t for t, k in critical_rows.items() if t % 2 == 0 and k != SATURATED)
    last_odd = max(t for t, k in critical_rows.items() if t % 2 == 1 and k != SATURATED)
    assert (last_even, last_odd) == (300_284, 300_301)
    assert selected[300_302][0] == selected[300_303][0] == SATURATED

    low = LOW_COLLISION.read_text()
    for marker in (
        "minimum_max=118074632 minimizer=149647 h0=118074632 h1=99754732",
        "sum_h0=31687862306776 sum_h1=27020159369932",
        "sum_theta_h0=2058618643449205948 sum_theta_h1=1754604114323772216",
        "sum_theta2_h0=189488938022181601177204 sum_theta2_h1=161400866866551803426992",
    ):
        assert marker in low, marker

    # Exact rearrangement extrema and explicit last-collision witnesses.
    maximum = -12_090 * 0 - 490 * 1 - 20 * 2 + 1 * 8 + 3 * 9 + 20 * 10 + 490 * 11 + 12_090 * 12
    minimum = 12_090 * 0 + 490 * 1 + 20 * 2 + 3 * 3 + 1 * 4 - 20 * 10 - 490 * 11 - 12_090 * 12
    assert (minimum, maximum, maximum - minimum) == (-150_127, 150_175, 300_302)

    even_left = (10, 8, 9, 2, 11, 1, 12, 0, 3, 6, 5, 7)
    common_right = (3, 5, 2, 10, 1, 11, 0, 12, 6, 9, 7, 8)
    odd_left = (9, 8, 10, 2, 11, 1, 12, 0, 3, 6, 5, 7)
    assert assignment(even_left) == (150_158, -3, -2)
    assert assignment(common_right) == (-150_126, -3, -1)
    assert assignment(odd_left) == (150_175, -3, -2)
    assert 150_158 - 2 * 300_284 == -150_126 - 300_284 == -450_410
    assert 150_175 - 2 * 300_301 == -150_126 - 300_301 == -450_427

    # Fifth-ratio rectangular certificate at the exact first four-ratio failure.
    a_min = minimum - 12 * 300_177
    a_max = maximum + 12 * 300_177
    width = a_max - a_min + 1
    assert (a_min, a_max, width) == (-3_752_251, 3_752_299, 7_504_551)
    bound_end = 13 * (width + 24 * 2_797_343)
    bound_next = 13 * (width + 24 * 2_797_344)
    assert bound_end == 970_330_179
    assert TARGET - (bound_end - 1) == 295
    assert bound_next == 970_330_491
    assert bound_next - 1 - TARGET == 17

    theorem_set = (set(range(2, 300_177)) - {3, 20, 490, 12_090}) | EXCEPTIONS
    assert not theorem_set & {1, 3, 20, 490, 12_090}
    fifth_set = set(range(2, 2_797_344)) - {3, 20, 490, 12_090, 300_177}
    assert fifth_set

    print("round51 verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"response receipt: {receipt(RESPONSE)}")
    print("critical checksums: 131974409852556 30190751891579666896 7149371020340889916998112")
    print("raw passing: {1..300176} U 15 exact exceptions")
    print("last nonsaturated even/odd: 300284 300301")
    print("fifth-ratio rectangular endpoint: 2797343")


if __name__ == "__main__":
    main()
