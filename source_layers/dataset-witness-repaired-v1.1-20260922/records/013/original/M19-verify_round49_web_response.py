#!/usr/bin/env python3
"""Independent exact checks for the archived Round 49 response."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-49-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-49-prompt-sent.md"
RESPONSE = ROOT / "artifacts/web-gpt56sol-pro/round-49-response.md"
OUTPUT = ROOT / "outputs/round-49-gpt56sol-pro-response.md"
FRONTIER_SOURCE = ROOT / "work/verify_round49_frontier.cpp"
FRONTIER_BINARY = ROOT / "work/verify_round49_frontier"

PROMPT_SHA = "79ee719cdd4ebaa47d2abd7ecac2d0e401337b462f34f35e453e56782f1b70c2"
RESPONSE_SHA = "f2291d9ec6087fa5919b9d77e84489cd6a79263a0e27e3bf510192957d68a9ae"
TARGET = 970_330_473


def receipt(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()
    return sha256(data).hexdigest(), len(data), data.count(b"\n")


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert RESPONSE.read_bytes() == OUTPUT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 7_106, 263)
    assert receipt(RESPONSE) == (RESPONSE_SHA, 20_359, 1_158)

    text = RESPONSE.read_text()
    for marker in (
        "# Verdict",
        "ExtendedKappaTwentyTwoRatioExclusion",
        "Lambda490ThirdRatioExclusion",
        "336812082968",
        "110335357319864",
        "41937553140659688",
        "971038848",
        "708374",
        "970012416",
        "318058",
        "491,493,495",
        "974917184",
        "\\lambda\\ge502",
        "\\lambda\\ge519",
        "|\\lambda|\\ge518",
        "970257600",
        "72874",
        "970437312",
        "106838",
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
            str(FRONTIER_SOURCE), "-o", str(FRONTIER_BINARY),
        ],
        check=True,
    )
    frontier = subprocess.run(
        [str(FRONTIER_BINARY)], check=True, capture_output=True, text=True
    ).stdout
    assert "round49 frontier verification: PASS" in frontier
    assert "336812082968 110335357319864 41937553140659688" in frontier
    assert "last nonstabilized lambda: 517" in frontier

    # The rectangular three-ratio argument at the first two-ratio failure.
    coefficient_4887 = 13 * (12_287 + 24 * 4_887) * 24**2
    coefficient_4888 = 13 * (12_287 + 24 * 4_888) * 24**2
    assert coefficient_4887 == 970_257_600
    assert TARGET - (coefficient_4887 - 1) == 72_874
    assert coefficient_4888 == 970_437_312
    assert coefficient_4888 - 1 - TARGET == 106_838

    # Formal repetition values forced independently of the arbitrary pairs.
    inadmissible = {0, 1, 3, 20}
    theorem_set = (set(range(2, 490)) - {3, 20}) | {491, 493, 495}
    assert not theorem_set & inadmissible
    assert min(set(range(1, 527)) - ({1, 3, 20} | theorem_set)) == 490

    print("round49 verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"response receipt: {receipt(RESPONSE)}")
    print(frontier.strip())
    print(f"third-ratio rectangular endpoint: {coefficient_4887}")


if __name__ == "__main__":
    main()
