#!/usr/bin/env python3
"""Pre-send checks for Round 50's exact certificate and prompt receipt."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "work/round-50-prompt.md"
SENT = ROOT / "artifacts/web-gpt56sol-pro/round-50-prompt-sent.md"
SOURCE = ROOT / "work/enumerate_round50_three_ratio.cpp"
BINARY = ROOT / "work/enumerate_round50_three_ratio"
PROMPT_SHA = "9897a614ae814a6bbba1cb208d521d59a5cfa93b97fcfb38b5e68a262e3991e4"

EXPECTED = {
    4_888: 602_407_424,
    4_889: 592_149_880,
    6_000: 704_730_480,
    8_000: 825_312_104,
    10_000: 921_780_944,
    11_000: 950_898_280,
    11_500: 961_659_096,
    12_000: 968_681_800,
    12_100: 970_254_336,
    12_150: 970_863_016,
    12_287: 971_038_848,
}


def receipt(path: Path) -> tuple[str, int, int]:
    data = path.read_bytes()
    return sha256(data).hexdigest(), len(data), data.count(b"\n")


def main() -> None:
    assert PROMPT.read_bytes() == SENT.read_bytes()
    assert receipt(PROMPT) == (PROMPT_SHA, 7_337, 313)
    assert b"\r" not in PROMPT.read_bytes()

    subprocess.run(
        [
            "c++",
            "-std=c++20",
            "-O3",
            "-pthread",
            str(SOURCE),
            "-o",
            str(BINARY),
        ],
        check=True,
    )
    result = subprocess.run(
        [str(BINARY), *(str(value) for value in EXPECTED)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    for eta, expected in EXPECTED.items():
        marker = f"eta={eta} exact={expected} "
        assert marker in result, marker

    assert "classes=81122193" in result
    assert "support=(34937728,42597744,46377508,49367732,50598780," in result
    assert "classes=(4740930,5743060,6239508,6639662,6801900," in result
    assert 970_330_473 - (602_407_424 - 1) == 367_923_050
    assert 6_167 - (-6_119) == 12_286

    print("round50 pre-send verification: PASS")
    print(f"prompt receipt: {receipt(PROMPT)}")
    print(f"verified anchors: {EXPECTED}")


if __name__ == "__main__":
    main()
