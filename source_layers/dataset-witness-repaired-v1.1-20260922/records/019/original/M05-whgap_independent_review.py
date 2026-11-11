"""Independent WHGAP calibration and symmetric-extension review.

This file was written before reading the proposer's scripts, result tables, or
logs.  Tensor ordering used throughout is lexicographic:
  AB:       (a,b) -> 3*a+b
  AB1B2:    (a,b1,b2) -> 9*a+3*b1+b2.

The SDP is not the full 27-by-27 formulation from the commission.  It
parameterizes the commutant of the B1/B2 swap as independent real symmetric
blocks on A tensor Sym^2(B) (dimension 18) and A tensor Alt^2(B)
(dimension 9).  Real variables are without loss for the real Choi marginal:
averaging a complex feasible point with its entrywise conjugate preserves all
constraints and positive semidefiniteness.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import time
from pathlib import Path

import cvxpy as cp
import numpy as np
import sympy as sp


D = 3
BOUNDARY_CLAIM = 4.0 / 7.0


def e(i: int, j: int, n: int = D) -> sp.Matrix:
    out = sp.zeros(n)
    out[i, j] = 1
    return out


def sp_trace(m: sp.Matrix) -> sp.Expr:
    return sum(m[i, i] for i in range(m.rows))


def lambda_sp(x: sp.Expr, y: sp.Matrix) -> sp.Matrix:
    return (1 - x) * y + (x / 2) * (sp_trace(y) * sp.eye(D) - y.T)


def levi_kraus_half() -> list[sp.Matrix]:
    mats: list[sp.Matrix] = []
    for mu in range(D):
        mats.append(
            sp.Matrix(D, D, lambda j, k: sp.LeviCivita(mu, j, k))
        )
    return [sp.eye(D) / sp.sqrt(2)] + [a / 2 for a in mats]


def complement_sp(y: sp.Matrix, kraus: list[sp.Matrix]) -> sp.Matrix:
    return sp.Matrix(
        len(kraus),
        len(kraus),
        lambda a, b: sp_trace(kraus[a] * y * kraus[b].conjugate().T),
    )


def vec_row_sp(m: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([m[i, j] for i in range(m.rows) for j in range(m.cols)])


def j_map(y: sp.Matrix) -> sp.Matrix:
    a = sp.Matrix(
        [
            y[1, 2] - y[2, 1],
            y[2, 0] - y[0, 2],
            y[0, 1] - y[1, 0],
        ]
    )
    out = sp.zeros(4)
    out[0, 0] = sp_trace(y)
    for k in range(D):
        out[0, k + 1] = sp.sqrt(2) * a[k]
        out[k + 1, 0] = -sp.sqrt(2) * a[k]
    lower = 2 * sp_trace(y) * sp.eye(D) - y - 2 * y.T
    out[1:4, 1:4] = lower
    return out / 3


def choi_sp(x: sp.Expr) -> sp.Matrix:
    out = sp.zeros(D * D)
    for i in range(D):
        for j in range(D):
            out += sp.kronecker_product(e(i, j), lambda_sp(x, e(i, j))) / D
    return sp.simplify(out)


def partial_transpose_a_sp(m: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(D * D)
    for a in range(D):
        for b in range(D):
            for ap in range(D):
                for bp in range(D):
                    out[D * a + b, D * ap + bp] = m[D * ap + b, D * a + bp]
    return out


def swap_ab_sp() -> sp.Matrix:
    out = sp.zeros(D * D)
    for a in range(D):
        for b in range(D):
            out[D * b + a, D * a + b] = 1
    return out


def swap_b1_b2_sp() -> sp.Matrix:
    out = sp.zeros(D**3)
    for a in range(D):
        for b1 in range(D):
            for b2 in range(D):
                src = D * D * a + D * b1 + b2
                dst = D * D * a + D * b2 + b1
                out[dst, src] = 1
    return out


def exact_psd_congruence(m: sp.Matrix) -> tuple[bool, list[sp.Expr], sp.Matrix]:
    """Exact symmetric elimination certificate over Q(sqrt(3)).

    A PSD matrix with a zero diagonal entry has a zero corresponding row.
    Therefore repeated positive diagonal pivots, followed by an exact zero
    residual, are an exact congruence proof of positive semidefiniteness.
    """
    residual = sp.MutableDenseMatrix(m)
    remaining = list(range(m.rows))
    pivots: list[sp.Expr] = []
    while remaining:
        pivot_index = None
        for candidate in remaining:
            diag = sp.radsimp(sp.factor(residual[candidate, candidate]))
            if diag != 0:
                pivot_index = candidate
                break
        if pivot_index is None:
            tail = residual.extract(remaining, remaining).applyfunc(sp.simplify)
            return tail == sp.zeros(len(remaining)), pivots, tail
        pivot = sp.radsimp(sp.factor(residual[pivot_index, pivot_index]))
        if sp.ask(sp.Q.positive(pivot)) is not True:
            return False, pivots + [pivot], residual.extract(remaining, remaining)
        pivots.append(pivot)
        others = [i for i in remaining if i != pivot_index]
        for row_position, i in enumerate(others):
            for j in others[row_position:]:
                value = residual[i, j] - (
                    residual[i, pivot_index] * residual[pivot_index, j] / pivot
                )
                value = sp.radsimp(sp.factor(value))
                residual[i, j] = value
                residual[j, i] = value
        for i in others:
            residual[i, pivot_index] = 0
            residual[pivot_index, i] = 0
        remaining = others
    return True, pivots, sp.zeros(0)


def exact_calibration() -> dict:
    half = sp.Rational(1, 2)
    basis = [e(i, j) for i in range(D) for j in range(D)]
    a_mats = levi_kraus_half()[1:]
    # Undo the x=1/2 Kraus scale to recover A_mu.
    a_mats = [2 * a for a in a_mats]

    c1_action = all(
        sp.simplify(
            sum((a * y * a.conjugate().T for a in a_mats), sp.zeros(D))
            - (sp_trace(y) * sp.eye(D) - y.T)
        )
        == sp.zeros(D)
        for y in basis
    )
    c1_cptp = (
        sp.simplify(
            sum((a.conjugate().T * a for a in a_mats), sp.zeros(D))
            - 2 * sp.eye(D)
        )
        == sp.zeros(D)
    )
    print("EXACT_STAGE C1", flush=True)

    kraus = levi_kraus_half()
    c2_unital = lambda_sp(half, sp.eye(D)) == sp.eye(D)
    comp_i = sp.simplify(complement_sp(sp.eye(D), kraus))
    c2_comp = comp_i == sp.diag(
        sp.Rational(3, 2),
        sp.Rational(1, 2),
        sp.Rational(1, 2),
        sp.Rational(1, 2),
    )
    print("EXACT_STAGE C2", flush=True)

    omega = choi_sp(half)
    omega_pt = partial_transpose_a_sp(omega)
    c3_eigs = {str(k): int(v) for k, v in omega_pt.eigenvals().items()}
    c3_expected = {
        sp.Rational(1, 4): 5,
        sp.Integer(0): 1,
        -sp.Rational(1, 12): 3,
    }
    c3 = omega_pt.eigenvals() == c3_expected
    print("EXACT_STAGE C3", flush=True)

    j_super = sp.zeros(16, 9)
    for col, y in enumerate(basis):
        j_super[:, col] = vec_row_sp(j_map(y))
    c4_lift = True
    for y in basis:
        lhs = j_super.conjugate().T * vec_row_sp(complement_sp(y, kraus))
        rhs = vec_row_sp(lambda_sp(half, y))
        if sp.simplify(lhs - rhs) != sp.zeros(9, 1):
            c4_lift = False
            break
    j_e00 = sp.simplify(j_map(e(0, 0)))
    c4_nonpsd = j_e00 == sp.diag(
        sp.Rational(1, 3),
        -sp.Rational(1, 3),
        sp.Rational(2, 3),
        sp.Rational(2, 3),
    )
    print("EXACT_STAGE C4", flush=True)

    g_mats: list[sp.Matrix] = []
    for mu in range(D):
        g = sp.zeros(9, 3)
        for i in range(D):
            for j in range(D):
                for k in range(D):
                    g[D * j + k, i] = (
                        sp.KroneckerDelta(j, i) * sp.KroneckerDelta(k, mu)
                        + sp.Rational(1, 2)
                        * sp.KroneckerDelta(j, mu)
                        * sp.KroneckerDelta(k, i)
                        - sp.Rational(1, 2)
                        * sp.KroneckerDelta(mu, i)
                        * sp.KroneckerDelta(j, k)
                    )
        g_mats.append(g)

    c5_defect = True
    for tau in basis:
        l_lam = sp.kronecker_product(lambda_sp(half, tau), sp.eye(D))
        l_comp = sp.kronecker_product(complement_sp(tau, kraus), sp.eye(4))
        delta = sp.simplify(l_lam - j_super.conjugate().T * l_comp * j_super)
        rhs = sp.Rational(2, 9) * sum(
            (g * tau * g.conjugate().T for g in g_mats), sp.zeros(9)
        )
        if sp.simplify(delta - rhs) != sp.zeros(9):
            c5_defect = False
            break
    gram = sp.Matrix(
        D,
        D,
        lambda mu, nu: sp_trace(g_mats[mu].conjugate().T * g_mats[nu]),
    )
    c5_gram = gram == 4 * sp.eye(D)
    print("EXACT_STAGE C5", flush=True)

    phi_vec = sp.zeros(9, 1)
    for i in range(D):
        phi_vec[D * i + i] = 1 / sp.sqrt(D)
    phi = phi_vec * phi_vec.conjugate().T
    f = swap_ab_sp()
    pminus = (sp.eye(9) - f) / 2
    pst = (sp.eye(9) + f) / 2 - phi
    w0 = (2 * sp.sqrt(3) - 4) / 5
    w1 = (2 * sp.sqrt(3) - 3) / 5
    witness = sp.simplify(w0 * phi + w1 * pminus + pst)
    witness_value = sp.simplify(sp_trace(witness * omega))
    c6_value = witness_value == (4 * sp.sqrt(3) - 7) / 10

    s12 = swap_b1_b2_sp()
    h_first = sp.kronecker_product(witness, sp.eye(D))
    h = sp.simplify((h_first + s12 * h_first * s12.T) / 2)
    c6_psd, h_pivots, h_zero_residual = exact_psd_congruence(h)
    print("EXACT_STAGE C6", flush=True)

    # General Choi and partial-transpose multiplicities, derived independently.
    xs = sp.symbols("x", real=True)
    omega_general = choi_sp(xs)
    omega_expected = (
        (1 - xs) * phi + (xs / 6) * (sp.eye(9) - f)
    )
    choi_formula = sp.simplify(omega_general - omega_expected) == sp.zeros(9)
    pt_general = partial_transpose_a_sp(omega_general)
    pt_spectral_projectors = sp.simplify(
        pt_general
        - (
            ((1 - 2 * xs) / 3) * phi
            + ((2 - xs) / 6) * pst
            + ((3 * xs - 2) / 6) * pminus
        )
    ) == sp.zeros(9)

    checks = {
        "C1_channel_action": c1_action,
        "C1_kraus_cptp": c1_cptp,
        "C2_unital": c2_unital,
        "C2_complement_identity": c2_comp,
        "C3_partial_transpose_spectrum": c3,
        "C4_lift_identity_full_basis": c4_lift,
        "C4_J_E00_nonpsd": c4_nonpsd,
        "C5_defect_full_basis": c5_defect,
        "C5_G_gram": c5_gram,
        "C6_witness_value": c6_value,
        "C6_exact_H_psd": c6_psd,
        "general_choi_projector_formula": choi_formula,
        "general_pt_projector_formula": pt_spectral_projectors,
    }
    return {
        "all_pass": all(checks.values()),
        "checks": checks,
        "lambda_c_identity": [[str(v) for v in comp_i.row(i)] for i in range(4)],
        "omega_pt_eigenvalues": c3_eigs,
        "J_E00": [[str(v) for v in j_e00.row(i)] for i in range(4)],
        "G_gram": [[str(v) for v in gram.row(i)] for i in range(3)],
        "witness_value": str(witness_value),
        "H_exact_congruence_positive_pivots": [str(v) for v in h_pivots],
        "H_exact_congruence_rank": len(h_pivots),
        "H_exact_zero_residual": h_zero_residual == sp.zeros(h_zero_residual.rows),
        "general_choi_spectrum": {
            "1-x": 1,
            "x/3": 3,
            "0": 5,
        },
        "general_partial_transpose_spectrum": {
            "(1-2*x)/3": 1,
            "(2-x)/6": 5,
            "(3*x-2)/6": 3,
        },
    }


def omega_np(x: float) -> np.ndarray:
    out = np.zeros((9, 9), dtype=float)
    for i in range(D):
        for j in range(D):
            y = np.zeros((D, D), dtype=float)
            y[i, j] = 1.0
            lam = (1.0 - x) * y + (x / 2.0) * (
                np.trace(y) * np.eye(D) - y.T
            )
            out[
                D * i : D * (i + 1),
                D * j : D * (j + 1),
            ] = lam / D
    return out


def swap_sector_isometries() -> tuple[np.ndarray, np.ndarray]:
    plus_b = []
    minus_b = []
    for i in range(D):
        v = np.zeros(9)
        v[D * i + i] = 1.0
        plus_b.append(v)
    for i in range(D):
        for j in range(i + 1, D):
            vp = np.zeros(9)
            vm = np.zeros(9)
            vp[D * i + j] = 1.0 / math.sqrt(2.0)
            vp[D * j + i] = 1.0 / math.sqrt(2.0)
            vm[D * i + j] = 1.0 / math.sqrt(2.0)
            vm[D * j + i] = -1.0 / math.sqrt(2.0)
            plus_b.append(vp)
            minus_b.append(vm)
    ub_plus = np.column_stack(plus_b)
    ub_minus = np.column_stack(minus_b)
    return np.kron(np.eye(D), ub_plus), np.kron(np.eye(D), ub_minus)


class SymmetricExtensionProgram:
    def __init__(self) -> None:
        self.up, self.um = swap_sector_isometries()
        self.rp = cp.Variable((18, 18), symmetric=True, name="rho_plus")
        self.rm = cp.Variable((9, 9), symmetric=True, name="rho_minus")
        self.t = cp.Variable(name="min_block_eigenvalue")
        self.target = cp.Parameter((9, 9), symmetric=True, name="omega")
        eta = self.up @ self.rp @ self.up.T + self.um @ self.rm @ self.um.T
        constraints = [
            self.rp - self.t * np.eye(18) >> 0,
            self.rm - self.t * np.eye(9) >> 0,
        ]
        for a in range(D):
            for b1 in range(D):
                row = D * a + b1
                for ap in range(D):
                    for bp1 in range(D):
                        col = D * ap + bp1
                        marginal_entry = 0
                        for b2 in range(D):
                            i = D * D * a + D * b1 + b2
                            j = D * D * ap + D * bp1 + b2
                            marginal_entry += eta[i, j]
                        constraints.append(marginal_entry == self.target[row, col])
        self.problem = cp.Problem(cp.Maximize(self.t), constraints)

    def solve(self, x: float) -> dict:
        self.target.value = omega_np(x)
        attempts = []
        settings_ladder = [
            (1e-8, 250_000),
            (1e-10, 750_000),
            (1e-11, 1_500_000),
        ]
        for eps, max_iters in settings_ladder:
            start = time.perf_counter()
            value = self.problem.solve(
                solver=cp.SCS,
                eps_abs=eps,
                eps_rel=eps,
                max_iters=max_iters,
                acceleration_lookback=10,
                warm_start=False,
                verbose=False,
            )
            elapsed = time.perf_counter() - start
            attempt = {
                "eps": eps,
                "max_iters": max_iters,
                "status": self.problem.status,
                "objective": None if value is None else float(value),
                "t": None if self.t.value is None else float(self.t.value),
                "solve_seconds": elapsed,
                "num_iters": getattr(self.problem.solver_stats, "num_iters", None),
            }
            attempts.append(attempt)
            if self.problem.status == cp.OPTIMAL:
                break
        final = attempts[-1]
        tval = final["t"]
        if final["status"] != cp.OPTIMAL or tval is None:
            classification = "unresolved"
        elif tval >= -1e-9:
            classification = "feasible_at_1e-9"
        elif tval < -1e-6:
            classification = "infeasible_at_1e-6"
        else:
            classification = "tolerance_gap"
        return {
            "x": float(x),
            "status": final["status"],
            "t": tval,
            "classification": classification,
            "attempts": attempts,
        }


def numerical_review() -> dict:
    program = SymmetricExtensionProgram()
    # Both mandated endpoints plus four interior points on each side of 4/7.
    points = [
        0.5,
        0.52,
        0.55,
        0.57,
        BOUNDARY_CLAIM - 1e-4,
        BOUNDARY_CLAIM,
        BOUNDARY_CLAIM + 1e-4,
        0.60,
        0.75,
        1.0,
    ]
    rows = []
    cache: dict[str, dict] = {}

    def solve_cached(x: float) -> dict:
        key = f"{x:.17g}"
        if key not in cache:
            cache[key] = program.solve(x)
        return cache[key]

    for point in points:
        result = solve_cached(point)
        rows.append(result)
        print(
            "POINT",
            f"x={point:.12f}",
            f"t={result['t']:.12e}" if result["t"] is not None else "t=None",
            f"status={result['status']}",
            f"class={result['classification']}",
            flush=True,
        )

    low = 0.5
    high = BOUNDARY_CLAIM
    low_result = solve_cached(low)
    high_result = solve_cached(high)
    bisection = []
    bracket_valid = (
        low_result["t"] is not None
        and high_result["t"] is not None
        and low_result["t"] < 0
        and high_result["t"] >= 0
    )
    if bracket_valid:
        while high - low > 1e-8:
            mid = (low + high) / 2
            result = solve_cached(mid)
            bisection.append(result)
            if result["status"] != cp.OPTIMAL or result["t"] is None:
                bracket_valid = False
                break
            if result["t"] >= 0:
                high = mid
            else:
                low = mid
    boundary = {
        "method": "raw-SCS-objective-sign; not an exact feasibility bracket",
        "valid_solver_sign_bracket": bracket_valid,
        "low": low,
        "high": high,
        "width": high - low,
        "midpoint": (low + high) / 2,
        "distance_midpoint_to_4_7": abs((low + high) / 2 - BOUNDARY_CLAIM),
        "iterations": bisection,
    }
    print(
        "BOUNDARY",
        json.dumps({k: v for k, v in boundary.items() if k != "iterations"}),
        flush=True,
    )
    return {
        "solver": "CVXPY 1.6.0 / SCS; independent swap-sector block formulation",
        "classification_semantics": {
            "feasible_at_1e-9": "clean OPTIMAL and t >= -1e-9",
            "infeasible_at_1e-6": "clean OPTIMAL and t < -1e-6",
            "tolerance_gap": "clean OPTIMAL and -1e-6 <= t < -1e-9",
            "unresolved": "non-OPTIMAL clean status or absent objective",
        },
        "point_results": rows,
        "boundary": boundary,
        "cvxpy_installed_solvers": cp.installed_solvers(),
    }


def write_csv(path: Path, numerical: dict) -> None:
    rows = numerical["point_results"] + numerical["boundary"]["iterations"]
    seen = set()
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "category",
                "x",
                "t",
                "status",
                "classification",
                "eps",
                "max_iters",
                "solve_seconds",
                "num_iters",
            ],
        )
        writer.writeheader()
        point_ids = {f"{r['x']:.17g}" for r in numerical["point_results"]}
        for row in rows:
            key = f"{row['x']:.17g}"
            if key in seen:
                continue
            seen.add(key)
            attempt = row["attempts"][-1]
            writer.writerow(
                {
                    "category": "gate_point" if key in point_ids else "bisection",
                    "x": f"{row['x']:.17g}",
                    "t": "" if row["t"] is None else f"{row['t']:.17g}",
                    "status": row["status"],
                    "classification": row["classification"],
                    "eps": attempt["eps"],
                    "max_iters": attempt["max_iters"],
                    "solve_seconds": f"{attempt['solve_seconds']:.9f}",
                    "num_iters": attempt["num_iters"],
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    started = time.perf_counter()
    exact = exact_calibration()
    print("EXACT_CALIBRATION", json.dumps(exact, sort_keys=True), flush=True)
    if not exact["all_pass"]:
        raise SystemExit("Independent exact calibration failed; SDP not run.")
    numerical = numerical_review()
    result = {
        "provenance": {
            "independent": True,
            "anchoring_statement": (
                "Written and executed before opening proposer scripts, artifact tables, or logs."
            ),
            "python": "C:[USER_HOME]/cpython3119/python.exe",
            "tensor_order": {
                "AB": "(a,b) -> 3*a+b",
                "AB1B2": "(a,b1,b2) -> 9*a+3*b1+b2",
            },
        },
        "exact": exact,
        "numerical": numerical,
        "elapsed_seconds": time.perf_counter() - started,
    }
    result_path = args.output_dir / "whgap_independent_results.json"
    result_path.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    write_csv(args.output_dir / "whgap_independent_scan.csv", numerical)
    print(f"WROTE {result_path}", flush=True)
    print(f"ELAPSED_SECONDS {result['elapsed_seconds']:.6f}", flush=True)


if __name__ == "__main__":
    main()
