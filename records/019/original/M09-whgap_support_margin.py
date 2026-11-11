"""Conditioning-aware boundary check for the independent WHGAP review.

For 0 < x < 1, omega_x has constant support span{Phi, Alt^2(C^3)} of
dimension four.  If eta >= 0 and Tr_B2 eta = omega_x, positivity forces eta
to be supported on supp(omega_x) tensor B2 (dimension 12).  Optimizing the
minimum eigenvalue on that forced support gives a nondegenerate feasibility
margin while retaining the full swap-conjugation constraint, including both
B1/B2 swap sectors.
"""

from __future__ import annotations

import csv
import json
import math
import time
from pathlib import Path

import cvxpy as cp
import numpy as np


D = 3


def idx(a: int, b1: int, b2: int) -> int:
    return 9 * a + 3 * b1 + b2


def omega(x: float) -> np.ndarray:
    phi = np.zeros(9)
    for i in range(D):
        phi[3 * i + i] = 1 / math.sqrt(3)
    f = np.zeros((9, 9))
    for a in range(D):
        for b in range(D):
            f[3 * b + a, 3 * a + b] = 1
    return (1 - x) * np.outer(phi, phi) + (x / 6) * (np.eye(9) - f)


def support_isometry() -> np.ndarray:
    columns = []
    phi = np.zeros(9)
    for i in range(D):
        phi[3 * i + i] = 1 / math.sqrt(3)
    columns.append(phi)
    for i in range(D):
        for j in range(i + 1, D):
            v = np.zeros(9)
            v[3 * i + j] = 1 / math.sqrt(2)
            v[3 * j + i] = -1 / math.sqrt(2)
            columns.append(v)
    q = np.column_stack(columns)
    assert np.allclose(q.T @ q, np.eye(4), atol=1e-15)
    return np.kron(q, np.eye(D))


def swap() -> np.ndarray:
    result = np.zeros((27, 27))
    for a in range(D):
        for b1 in range(D):
            for b2 in range(D):
                result[idx(a, b2, b1), idx(a, b1, b2)] = 1
    return result


class Program:
    def __init__(self) -> None:
        self.u = support_isometry()
        self.r = cp.Variable((12, 12), symmetric=True)
        self.t = cp.Variable()
        self.target = cp.Parameter((9, 9), symmetric=True)
        self.eta = self.u @ self.r @ self.u.T
        s = swap()
        constraints = [self.r - self.t * np.eye(12) >> 0, s @ self.eta @ s.T == self.eta]
        for a in range(D):
            for b1 in range(D):
                for ap in range(D):
                    for bp1 in range(D):
                        constraints.append(
                            sum(
                                self.eta[idx(a, b1, b2), idx(ap, bp1, b2)]
                                for b2 in range(D)
                            )
                            == self.target[3 * a + b1, 3 * ap + bp1]
                        )
        self.problem = cp.Problem(cp.Maximize(self.t), constraints)

    def solve(self, x: float) -> dict:
        self.target.value = omega(x)
        started = time.perf_counter()
        value = self.problem.solve(
            solver=cp.SCS,
            eps_abs=1e-11,
            eps_rel=1e-11,
            max_iters=1_000_000,
            warm_start=False,
            verbose=False,
        )
        return {
            "x": x,
            "t_support": None if value is None else float(value),
            "status": self.problem.status,
            "solve_seconds": time.perf_counter() - started,
            "num_iters": self.problem.solver_stats.num_iters,
        }


def main() -> None:
    program = Program()
    boundary = 4 / 7
    points = [
        0.5,
        0.52,
        0.55,
        0.57,
        boundary - 1e-4,
        boundary,
        boundary + 1e-4,
        0.60,
        0.75,
        0.99,
    ]
    cache = {}

    def run(x: float) -> dict:
        key = f"{x:.17g}"
        if key not in cache:
            cache[key] = program.solve(x)
            print(json.dumps(cache[key], sort_keys=True), flush=True)
        return cache[key]

    for x in points:
        run(x)
    lo = 0.5
    hi = boundary
    iterations = []
    while hi - lo > 1e-8:
        mid = (lo + hi) / 2
        row = run(mid)
        iterations.append(row)
        if row["status"] != cp.OPTIMAL:
            raise SystemExit(f"unclean status at x={mid}: {row['status']}")
        if row["t_support"] >= -1e-9:
            hi = mid
        else:
            lo = mid
    result = {
        "anchoring": (
            "Independent support construction; proposer output was read only after "
            "the earlier independent full and swap-sector t* runs were fixed."
        ),
        "support_argument": (
            "PSD eta with marginal omega has support contained in "
            "supp(omega) tensor B2; supp(omega)=span{Phi, Alt^2(B)} for 0<x<1."
        ),
        "formulation": (
            "12x12 support variable, full 27x27 swap-conjugation equality, "
            "same-basis B2 partial trace"
        ),
        "points": [cache[f"{x:.17g}"] for x in points],
        "bracket": {
            "low": lo,
            "high": hi,
            "width": hi - lo,
            "midpoint": (lo + hi) / 2,
            "distance_midpoint_to_4_7": abs((lo + hi) / 2 - boundary),
            "meaning": (
                "operational tolerance bracket: low has t_support < -1e-9; "
                "high has t_support >= -1e-9"
            ),
            "infeasible_threshold_used_for_gate_points": -1e-8,
            "feasible_threshold": -1e-9,
        },
        "iterations": iterations,
    }
    out_dir = Path("artifacts/logs_whgap_review_20260728")
    (out_dir / "whgap_support_margin_tolerance.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    with (out_dir / "whgap_support_margin_tolerance.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["x", "t_support", "status", "solve_seconds", "num_iters"],
        )
        writer.writeheader()
        for row in list(cache.values()):
            writer.writerow(row)
    print("BRACKET", json.dumps(result["bracket"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
