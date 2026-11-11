#!/usr/bin/env python3
"""Exact/certified gates for the T5 physical long cap.

This script never forms or uses an eigenvalue-only von Neumann surrogate.
It checks closed physical formulas on three solvable faces and audits the
certified 59-row actual-pairing sweep.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SWEEP_DIR = ROOT / "artifacts" / "logs_se_trace_t5_counterexample_sweep_20260721"
SWEEP_JSON = SWEEP_DIR / "se_trace_t5_counterexample_sweep.json"


def qtext(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def parse_q(s: str) -> Fraction:
    return Fraction(s)


def hook_dim(part: tuple[int, ...]) -> int:
    part = tuple(x for x in part if x)
    size = sum(part)
    numerator = math.factorial(size)
    denominator = 1
    for i, row in enumerate(part):
        for col in range(row):
            below = sum(1 for lower in part[i + 1 :] if lower > col)
            denominator *= row - col + below
    assert numerator % denominator == 0
    return numerator // denominator


def partitions(n: int, cap: int | None = None):
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for first in range(cap, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_manifest(directory: Path) -> list[dict]:
    rows = []
    for line in (directory / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, name = line.split(None, 1)
        path = directory / name.strip()
        actual = sha256(path)
        assert actual == expected, (path, expected, actual)
        rows.append({"path": str(path.relative_to(ROOT)), "sha256": actual})
    return rows


def unbarred_ratio(n: int, j: int, theta: tuple[int, ...]) -> Fraction:
    """Exact pure-unbarred ratio, as a Pieri constituent/dimension ratio."""
    kappa = (n - 1 - j,) + theta
    return Fraction(hook_dim(kappa), math.comb(n - 1, j) * hook_dim(theta))


def barred_column_ratio(n: int, j: int) -> Fraction:
    return Fraction(2 * n - 2 * j - 1, 2 * n - 1)


def j1_ratio(n: int, a: int) -> Fraction:
    if a == 1:
        return Fraction(n - 2, n - 1)
    if a == 0:
        return Fraction(2 * n - 3, 2 * n - 1)
    raise ValueError(a)


def exhaustive_symbolic_gates() -> dict:
    # Hook/Pieri identity on the complete pure-unbarred face.  For hook
    # theta it simplifies to 1-j/(n-theta_1); for general theta the exact
    # dimension ratio is the correct closed form.
    hook_rows = 0
    for j in range(1, 13):
        for theta in partitions(j):
            ftheta = hook_dim(theta)
            for n in range(3 * j, 8 * j + 8):
                if n - 1 - j < theta[0]:
                    continue
                kappa = (n - 1 - j,) + theta
                lhs = Fraction(hook_dim(kappa), math.comb(n - 1, j) * ftheta)
                rhs = unbarred_ratio(n, j, theta)
                assert lhs == rhs and 0 <= rhs < 1
                if len(theta) == 1 or all(x == 1 for x in theta[1:]):
                    assert rhs == Fraction(n - theta[0] - j, n - theta[0])
                hook_rows += 1

    # In the pure-barred column face, the normalized hook/exterior-power
    # singular masses are 1 (multiplicity C(n-2,j)) and 1/(2n-1)
    # (multiplicity C(n-2,j-1)).
    wedge_rows = 0
    for j in range(1, 13):
        for n in range(3 * j, 8 * j + 8):
            lhs = Fraction(
                math.comb(n - 2, j), math.comb(n - 1, j)
            ) + Fraction(
                math.comb(n - 2, j - 1),
                (2 * n - 1) * math.comb(n - 1, j),
            )
            rhs = barred_column_ratio(n, j)
            assert lhs == rhs and 0 <= rhs < 1

            # Independent orbital/Pluecker evaluation: only equal and
            # one-replacement subset pairs have nonzero Gram entries.
            q = 2 * n
            m = math.comb(n - 1, j)
            diag_out = Fraction(q * (q - j - 1), (q - j) * (q - 1))
            adj_out = Fraction(-q, (q - j) * (q - 1))
            diag_in = Fraction(q * (n - j), n * (q - j))
            adj_in = Fraction(-q, n * (q - j))
            actual = m * (
                diag_out * diag_in
                + j * (n - 1 - j) * adj_out * adj_in
            )
            B = Fraction(q, q - j)
            assert actual == B * B * m * rhs
            wedge_rows += 1

    return {
        "pure_unbarred_hook_identity_rows": hook_rows,
        "pure_barred_column_wedge_identity_rows": wedge_rows,
    }


def j1_ar_certificate(n: int, a: int) -> dict:
    q = 2 * n
    B = Fraction(q, q - 1)
    if a == 1:
        # Only mu=(n-2,1) is active.
        blocks = [{
            "mu": [n - 2, 1], "f_mu": n - 2,
            "a_0mu": qtext(B), "r_mu": qtext(B),
            "f_a_r": qtext(Fraction(n - 2) * B * B),
        }]
    else:
        # Restricting the B-standard carrier to the matched S_(n-1)
        # gives a standard block and one unmatched-point contrast line.
        a_std, r_std = B, B
        a_triv = B * B / 2
        r_triv = B / n
        blocks = [
            {"mu": [n - 2, 1], "f_mu": n - 2,
             "a_0mu": qtext(a_std), "r_mu": qtext(r_std),
             "f_a_r": qtext(Fraction(n - 2) * a_std * r_std)},
            {"mu": [n - 1], "f_mu": 1,
             "a_0mu": qtext(a_triv), "r_mu": qtext(r_triv),
             "f_a_r": qtext(a_triv * r_triv)},
        ]
    total = sum((parse_q(x["f_a_r"]) for x in blocks), Fraction())
    cap = B * B * (n - 1)
    assert total / cap == j1_ratio(n, a)
    return {"n": n, "a": a, "b": 1 - a, "B": qtext(B),
            "blocks": blocks, "actual": qtext(total), "cap": qtext(cap),
            "ratio": qtext(total / cap)}


def sweep_gates() -> dict:
    data = json.loads(SWEEP_JSON.read_text(encoding="utf-8"))
    assert data["load_bearing_semantics"] == "actual direction-sensitive physical pairings only"
    assert len(data["results"]) == 59
    j1_rows = []
    face_rows = []
    all_pass = 0
    for row in data["results"]:
        ta = row["targets"]["T-a"]
        cap = parse_q(ta["cap_exact"])
        lo, hi = map(float, ta["certified_interval"])
        assert hi < float(cap) and ta["verdict"] == "PASS"
        all_pass += 1
        sec = row["sector"]
        n, j, a, b = sec["n"], sec["j"], sec["a"], sec["b"]
        theta = tuple(sec["theta"])
        predicted = None
        family = None
        if j == 1:
            predicted = j1_ratio(n, a)
            family = "j=1 exact"
        elif b == 0:
            predicted = unbarred_ratio(n, j, theta)
            family = "pure unbarred arbitrary theta"
        elif a == 0 and theta == (1,) * j:
            predicted = barred_column_ratio(n, j)
            family = "pure barred column"
        if predicted is not None:
            exact_actual = cap * predicted
            assert lo <= float(exact_actual) <= hi, (row["sector_id"], exact_actual, lo, hi)
            rec = {
                "sector_id": row["sector_id"], "family": family,
                "predicted_actual": qtext(exact_actual),
                "predicted_ratio": qtext(predicted),
                "certified_interval": [lo, hi],
            }
            face_rows.append(rec)
            if j == 1:
                j1_rows.append(rec)
    assert len(j1_rows) == 16
    return {
        "all_59_actual_Ta_certified_pass": all_pass,
        "closed_face_rows_in_sweep": len(face_rows),
        "j1_rows": j1_rows,
        "closed_face_rows": face_rows,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", type=Path, required=True)
    ap.add_argument("--log", type=Path, required=True)
    args = ap.parse_args()

    manifests = {
        "counterexample_sweep": verify_manifest(SWEEP_DIR),
        "common_line_review": verify_manifest(
            ROOT / "artifacts" / "logs_se_trace_t5_common_line_review_20260721"
        ),
        "direction_law": verify_manifest(
            ROOT / "artifacts" / "logs_se_trace_t5_direction_law_20260721"
        ),
    }
    symbolic = exhaustive_symbolic_gates()
    sweep = sweep_gates()
    j1_ar = [j1_ar_certificate(n, a) for n in range(3, 21) for a in (0, 1)]

    payload = {
        "node": "SE.denom.Phi.legal.trace.t5",
        "verdict": "STILL BLOCKED",
        "surrogate_policy": "actual direction-sensitive pairings only; eigenvalue-only VN excluded",
        "proved": {
            "j1_b0_ratio": "(n-2)/(n-1)",
            "j1_b1_ratio": "(2n-3)/(2n-1)",
            "pure_unbarred_ratio": "f^(n-1-j,theta)/(C(n-1,j) f^theta); for hook theta this is (n-theta_1-j)/(n-theta_1)",
            "pure_barred_column_ratio": "(2n-2j-1)/(2n-1)",
        },
        "symbolic_gates": symbolic,
        "j1_a_r_certificates": j1_ar,
        "sweep_gates": sweep,
        "source_manifests": manifests,
        "minimal_residual": (
            "For every remaining admissible mixed/non-column sector, prove "
            "Delta=B_theta(q)^2*T-M*sum_r k_r*Phi_r >= 0, where Phi_r is "
            "the exact physical four-overlap orbital kernel; arbitrary LR multiplicity c is retained."
        ),
    }
    args.json.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    lines = [
        "SE TRACE T5 LONG CAP EXACT/CERTIFIED GATES 2026-07-21",
        "SURROGATE_POLICY actual_direction_sensitive_only; eigenvalue_only_VN=EXCLUDED",
        f"MANIFESTS verified_files={sum(map(len, manifests.values()))} PASS",
        f"SYMBOLIC pure_unbarred_rows={symbolic['pure_unbarred_hook_identity_rows']} PASS",
        f"SYMBOLIC pure_barred_column_rows={symbolic['pure_barred_column_wedge_identity_rows']} PASS",
        f"J1 exact_a_r_rows={len(j1_ar)} PASS",
        f"SWEEP actual_Ta={sweep['all_59_actual_Ta_certified_pass']}/59 PASS",
        f"SWEEP closed_face_interval_matches={sweep['closed_face_rows_in_sweep']} PASS",
        "VERDICT STILL BLOCKED residual=mixed_or_noncolumn_orbital_defect_all_parameters_all_c",
    ]
    args.log.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
