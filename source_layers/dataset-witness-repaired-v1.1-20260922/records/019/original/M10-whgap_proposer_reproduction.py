"""Re-run proposer programs while redirecting every write to review storage."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "artifacts" / "logs_whgap_review_20260728" / "proposer_reproduction"
OUT.mkdir(parents=True, exist_ok=True)


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main() -> int:
    artifact = OUT / "reproduction_artifact.md"
    artifact.write_text("# Redirected proposer reproduction\n", encoding="utf-8")

    p0 = load("whgap_p0_reproduced", ROOT / "tools" / "whgap_p0_calibration.py")
    p0.ARTIFACT = artifact
    print("REPRODUCTION P0 START", flush=True)
    code0 = p0.main()
    print(f"REPRODUCTION P0 EXIT {code0}", flush=True)
    if code0 != 0:
        return code0

    p1 = load(
        "whgap_p1_reproduced", ROOT / "tools" / "whgap_p1_antideg_boundary.py"
    )
    p1.LOG_DIR = OUT
    p1.SCAN_LOG = OUT / "reproduction_scan.csv"
    p1.SUMMARY_LOG = OUT / "reproduction_summary.json"
    p1.ARTIFACT = artifact
    print("REPRODUCTION P1 START", flush=True)
    code1 = p1.main()
    print(f"REPRODUCTION P1 EXIT {code1}", flush=True)
    return code1


if __name__ == "__main__":
    raise SystemExit(main())
