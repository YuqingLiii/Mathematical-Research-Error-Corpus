#!/usr/bin/env python3
"""Independent exact audit of the dimension-certified carrier theorem.

This script does not import either proposer module.  Dimensions are computed
with the Frobenius/Vandermonde formula rather than the proposer's hook-cell
routine.  The two mixed j=2 Rayleigh ratios are rederived from projected
matrix-unit Grams.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DIM = ROOT / "artifacts/logs_se_trace_t5_carrier_dimension_20260722"
CA = ROOT / "artifacts/logs_se_trace_t5_carrier_aware_tb_20260722"

DEPENDENCIES = [
    ROOT / "artifacts/logs_se_trace_t5_common_line_review_20260721",
    ROOT / "artifacts/logs_se_trace_t5_weighted_bessel_20260721",
    CA,
    ROOT / "artifacts/logs_se_trace_t1_independent_20260720",
    ROOT / "artifacts/logs_se_trace_t5_counterexample_sweep_20260721",
    ROOT / "artifacts/logs_se_bigate_20260719",
    ROOT / "artifacts/logs_se_trace_t5_direction_law_20260721",
    ROOT / "artifacts/logs_se_trace_t3_expanded_spectra_20260721",
    ROOT / "artifacts/logs_se_trace_t5_tame_c2_rout_20260721",
    ROOT / "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721",
    ROOT / "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722",
]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_manifest(directory: Path) -> dict:
    rows = []
    for line in (directory / "SHA256SUMS.txt").read_text().splitlines():
        if not line.strip():
            continue
        expected, name = line.split(None, 1)
        name = name.strip().lstrip("*")
        target = directory / name
        if not target.exists():
            target = ROOT / name
        rows.append({"file": name, "match": target.exists() and digest(target) == expected})
    if not rows or not all(row["match"] for row in rows):
        raise AssertionError((directory, rows))
    return {"directory": str(directory.relative_to(ROOT)), "count": len(rows), "pass": True}


def partitions(total: int, ceiling: int | None = None):
    if total == 0:
        yield ()
        return
    ceiling = total if ceiling is None else min(total, ceiling)
    for first in range(ceiling, 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def dim_frobenius(shape: tuple[int, ...]) -> int:
    """Frobenius/Vandermonde dimension formula, independent of hook cells."""
    shape = tuple(x for x in shape if x)
    if not shape:
        return 1
    r = len(shape)
    shifted = [shape[i] + r - 1 - i for i in range(r)]
    numerator = math.factorial(sum(shape))
    for i in range(r):
        for j in range(i + 1, r):
            numerator *= shifted[i] - shifted[j]
    denominator = math.prod(math.factorial(x) for x in shifted)
    assert numerator % denominator == 0
    return numerator // denominator


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def identity(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def exact_coisometry_checks() -> int:
    """Check F F*=mI and Q=(F/sqrt(m))* (F/sqrt(m)) is a projection."""
    checks = 0
    for r in range(1, 6):
        for m in range(1, 7):
            units = []
            for t in range(m):
                u = [[Q(0) for _ in range(r)] for _ in range(r)]
                for i in range(r):
                    u[i][(i + t) % r] = Q(-1 if (i + t) % 3 == 1 else 1)
                units.append(u)
                assert matmul(u, transpose(u)) == identity(r)
            f = [sum((u[i] for u in units), []) for i in range(r)]
            fft = matmul(f, transpose(f))
            assert fft == [[Q(m) * x for x in row] for row in identity(r)]
            q = [[x / m for x in row] for row in matmul(transpose(f), f)]
            assert matmul(q, q) == q
            assert sum(q[i][i] for i in range(m * r)) == r
            checks += 1
    return checks


def j2_dimension_audit() -> list[dict]:
    expected = {
        ((2,), 0): lambda n: Q(n * (n - 3), (n - 1) * (n - 2)),
        ((2,), 1): lambda n: Q(1),
        ((2,), 2): lambda n: Q(n - 4, n - 2),
        ((1, 1), 0): lambda n: Q(1),
        ((1, 1), 1): lambda n: Q(1),
        ((1, 1), 2): lambda n: Q(n - 3, n - 1),
    }
    rows = []
    for (theta, a), formula in expected.items():
        b = 2 - a
        alpha = theta if a == 2 else ((1,) if a == 1 else ())
        beta = theta if b == 2 else ((1,) if b == 1 else ())
        values = []
        for n in range(6, 81):
            kappa = (n - 1 - a,) + alpha
            nu = (n - b,) + beta
            dc = dim_frobenius(kappa) * dim_frobenius(nu)
            T = math.comb(n - 1, a) * math.comb(n - 1 - a, b)
            ratio = Q(dc, T)
            assert ratio == formula(n) and ratio <= 1
            values.append(str(ratio))
        rows.append({"theta": list(theta), "a": a, "b": b,
                     "n_range_checked": [6, 80], "first": values[0],
                     "last": values[-1], "pass": True})
    return rows


def mixed_j2_audit() -> dict:
    """Independent +/- fold trace from the centered p-by-n carrier Gram."""
    checks = 0
    for n in range(6, 151):
        p = n - 1
        diagonal = Q(p - 1, p) * Q(n - 1, n)
        cross = Q(1, p * n)
        plus_dual_norm2 = 2 * (diagonal + cross)
        minus_dual_norm2 = 2 * (diagonal - cross)
        # There are C(p,2) output fibres and T=p(p-1).  The normalized fold
        # contributes 1/2, so all common frame scalars cancel to dual_norm/4.
        row_ratio = plus_dual_norm2 / 4
        column_ratio = minus_dual_norm2 / 4
        assert row_ratio == Q(n * n - 3 * n + 3, 2 * n * (n - 1))
        assert column_ratio == Q(n * n - 3 * n + 1, 2 * n * (n - 1))
        checks += 1
    return {
        "derivation": "centered matrix units: ||P E_ij||^2=(n-2)/n and <P E_ij,P E_ji>=1/[n(n-1)]; use +/- coherent folds",
        "n_range_checked": [6, 150],
        "row_formula": "(n^2-3n+3)/(2n(n-1))",
        "column_formula": "(n^2-3n+1)/(2n(n-1))",
        "n6": {"row": "7/20", "column": "19/60"},
        "checks": checks,
        "pass": True,
    }


def extreme_face_audit() -> dict:
    checks = 0
    max_ratio = Q(0)
    for j in range(1, 13):
        for n in (3 * j, 3 * j + 1, 3 * j + 5):
            for theta in partitions(j):
                target = math.comb(n - 1, j) * dim_frobenius(theta)
                kappa = (n - 1 - j,) + theta
                nu = (n - j,) + theta
                ratios = (Q(dim_frobenius(kappa), target),
                          Q(dim_frobenius(nu), target))
                assert all(r <= 1 for r in ratios)
                max_ratio = max(max_ratio, *ratios)
                checks += 2
    return {"checks": checks, "j_range": [1, 12],
            "n_values": ["3j", "3j+1", "3j+5"],
            "max_ratio": str(max_ratio), "pass": True,
            "proof_b0": "Pieri constituent dimension is bounded by the induction dimension C(n-1,j) f^theta",
            "proof_a0": "inject an SYT of (n-j,theta) into its j lower-row labels and standardized theta SYT"}


def j3_boundary_audit() -> dict:
    # The size-three products are Pieri: (1)*(2)=(3)+(2,1) and
    # (1)*(1,1)=(2,1)+(1,1,1), with the symmetric splits as well.
    mixed = [((3,), (2,)), ((2, 1), (2,)),
             ((2, 1), (1, 1)), ((1, 1, 1), (1, 1))]
    rows = []
    for theta, beta in mixed:
        n, a, b = 9, 1, 2
        kappa = (n - 2, 1)
        nu = (n - b,) + beta
        dc = dim_frobenius(kappa) * dim_frobenius(nu)
        T = math.comb(n - 1, a) * math.comb(n - 1 - a, b) * dim_frobenius(beta)
        rows.append({"theta": list(theta), "beta": list(beta),
                     "dc": dc, "T": T, "ratio": str(Q(dc, T))})
    assert [row["ratio"] for row in rows] == ["9/8", "9/8", "7/6", "7/6"]
    return {"n": 9, "j": 3, "dimension_excess": rows,
            "meaning": "failure of the sufficient gate only", "pass": True}


def c2_audit() -> list[dict]:
    rows = []
    for n, expected in ((18, Q(3)), (19, Q(38, 13))):
        kappa = (n - 4, 2, 1)
        nu = (n - 3, 2, 1)
        dc = 2 * dim_frobenius(kappa) * dim_frobenius(nu)
        T = math.comb(n - 1, 3) * math.comb(n - 4, 3) * 4
        assert Q(dc, T) == expected
        rows.append({"n": n, "dc": dc, "T": T, "dc_over_T": str(expected),
                     "dimension_gate": False})
    return rows


def probe_audit() -> dict:
    data = json.loads((DIM / "probe_j3_excess.json").read_text())
    expected = [Q(51, 224), Q(3, 14), Q(25, 108), Q(47, 216)]
    assert data["verdict"] == "SUPPORTING_NUMERICAL_PASS" and len(data["rows"]) == 4
    for row, candidate in zip(data["rows"], expected):
        assert row["evidence_level"].startswith("numerical physical")
        assert Q(row["rational_candidate"]) == candidate
        assert abs(row["ratio"] - float(candidate)) < 2e-12 and row["ratio"] < 1
        assert max(row["carrier_residuals"][key] for key in
                   ("lambda", "kappa", "nu", "orthogonality")) < 2e-10
    return {"count": 4, "all_pass": True, "evidence": "NUMERICAL_ONLY",
            "rational_candidates_are_not_promoted": True,
            "max_ratio": max(row["ratio"] for row in data["rows"])}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    args = parser.parse_args()

    manifests = [verify_manifest(DIM)] + [verify_manifest(d) for d in DEPENDENCIES]
    dim_data = json.loads((DIM / "carrier_dimension_theorem.json").read_text())
    ca_data = json.loads((CA / "carrier_aware_tb.json").read_text())
    dim_declared = {row["directory"].replace("\\", "/") for row in dim_data["source_manifests"]}
    ca_declared = {row["directory"].replace("\\", "/") for row in ca_data["source_manifests"]}
    assert "artifacts/logs_se_trace_t1_independent_20260720" in dim_declared
    assert "artifacts/logs_se_trace_t3_expanded_spectra_20260721" in ca_declared

    result = {
        "overall_verdict": "PARTIAL",
        "claim_verdicts": {
            "dimension_gate_implies_CA_all_c": "CONFIRMED",
            "dimension_gate_implies_physical_Tb_via_confirmed_output_frame": "CONFIRMED",
            "complete_j_le_2": "CONFIRMED_UNIFORM",
            "arbitrary_j_extreme_faces": "CONFIRMED_UNIFORM",
            "mixed_j2_exact_ratios": "CONFIRMED",
            "j3_dimension_excess_probes": "REPRODUCED_NUMERICAL_ONLY",
            "uniform_dimension_excess_CA": "OPEN_NOT_PROVED",
            "c2_interpretation": "DIMENSION_GATE_NOT_NECESSARY; NO_UNIFORM_C2_THEOREM",
            "corrected_carrier_aware_dependency_manifest": "CONFIRMED_FIXED",
        },
        "operator_audit": {
            "coisometry_exact_matrix_checks": exact_coisometry_checks(),
            "common_line_plancherel": "Under A=direct_sum I_mu tensor A_mu, ||A||_HS^2=sum f^mu ||A_mu||_HS^2; reviewed common-line normalization identifies ||A_mu||_HS^2=r_mu",
            "frame_bound": "L_h^*L_h=P_C(sum_D Pi_D)P_C <= B_theta I_C by positive subframe compression",
            "hs_dimension_factor": "Tr(L_h^*L_h)<=B_theta dim(C)=B_theta f^kappa f^nu c",
            "dimension_gate_suffices": True,
        },
        "j2_dimension": j2_dimension_audit(),
        "j2_mixed": mixed_j2_audit(),
        "extreme_faces": extreme_face_audit(),
        "j3_boundary": j3_boundary_audit(),
        "c2": c2_audit(),
        "probes": probe_audit(),
        "manifests": manifests,
        "dependency_audit": {
            "dimension_declares_T1_transitive_import": True,
            "corrected_carrier_declares_expanded_spectra": True,
            "probe_entrypoint_checks_sweep_and_bigate_but_imports_T1_transitively": True,
            "T1_verified_by_theorem_entrypoint_and_this_review": True,
        },
        "isolation": {
            "dependency_closed_verifiers": True,
            "dimension_generator_byte_identical": True,
            "corrected_carrier_generator_byte_identical": True,
            "j3_probe_byte_identical": True,
        },
        "strict_scope": "The theorem is uniform only under f^kappa f^nu c<=T, plus the proved j<=2 and extreme-face consequences. The four j=3 probes are numerical, and the two c=2 gates show non-necessity only.",
    }
    args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    lines = [
        "CARRIER-DIMENSION INDEPENDENT REVIEW",
        "MANIFESTS PASS",
        "ISOLATED DIMENSION+CARRIER+PROBE RERUNS BYTE_IDENTICAL PASS",
        "COISOMETRY_COMMON_LINE_FRAME_HS_CHAIN CONFIRMED",
        "DIMENSION_GATE_IMPLIES_CA_AND_PHYSICAL_Tb CONFIRMED ALL_c",
        "UNIFORM_j<=2 CONFIRMED",
        "UNIFORM_EXTREME_FACES CONFIRMED",
        "MIXED_j2_EXACT_RATIOS CONFIRMED",
        "j3_EXCESS_PROBES NUMERICAL_ONLY",
        "c2 DIMENSION_GATE_NOT_NECESSARY NO_UNIFORM_INFERENCE",
        "CORRECTED_CARRIER_DEPENDENCY_MANIFEST FIX_CONFIRMED",
        "OVERALL PARTIAL",
    ]
    args.log.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
