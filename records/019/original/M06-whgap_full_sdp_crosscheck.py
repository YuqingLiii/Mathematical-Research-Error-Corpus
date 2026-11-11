"""Unreduced 27x27 cross-check for the independent WHGAP review.

Written and run before opening proposer scripts, tables, or logs.  Ordering is
(a,b1,b2) -> 9*a+3*b1+b2, and the marginal is formed by summing equal b2
indices in that same ordering.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import cvxpy as cp
import numpy as np


D = 3


def idx(a: int, b1: int, b2: int) -> int:
    return 9 * a + 3 * b1 + b2


def omega(x: float) -> np.ndarray:
    result = np.zeros((9, 9))
    for i in range(D):
        for j in range(D):
            unit = np.zeros((D, D))
            unit[i, j] = 1
            image = (1 - x) * unit + (x / 2) * (
                np.trace(unit) * np.eye(D) - unit.T
            )
            result[3 * i : 3 * i + 3, 3 * j : 3 * j + 3] = image / 3
    return result


def swap() -> np.ndarray:
    result = np.zeros((27, 27))
    for a in range(D):
        for b1 in range(D):
            for b2 in range(D):
                result[idx(a, b2, b1), idx(a, b1, b2)] = 1
    return result


def solve(x: float, solver: str) -> dict:
    eta = cp.Variable((27, 27), symmetric=True)
    t = cp.Variable()
    s = swap()
    constraints = [eta - t * np.eye(27) >> 0, s @ eta @ s.T == eta]
    target = omega(x)
    for a in range(D):
        for b1 in range(D):
            for ap in range(D):
                for bp1 in range(D):
                    constraints.append(
                        sum(
                            eta[idx(a, b1, b2), idx(ap, bp1, b2)]
                            for b2 in range(D)
                        )
                        == target[3 * a + b1, 3 * ap + bp1]
                    )
    problem = cp.Problem(cp.Maximize(t), constraints)
    started = time.perf_counter()
    if solver == "CLARABEL":
        value = problem.solve(
            solver=cp.CLARABEL,
            tol_gap_abs=1e-10,
            tol_gap_rel=1e-10,
            tol_feas=1e-10,
            max_iter=1000,
            verbose=False,
        )
    else:
        value = problem.solve(
            solver=cp.SCS,
            eps_abs=1e-10,
            eps_rel=1e-10,
            max_iters=750_000,
            warm_start=False,
            verbose=False,
        )
    return {
        "x": x,
        "solver": solver,
        "status": problem.status,
        "objective": None if value is None else float(value),
        "t": None if t.value is None else float(t.value),
        "solve_seconds": time.perf_counter() - started,
        "num_iters": problem.solver_stats.num_iters,
    }


def main() -> None:
    points = [0.5, 0.55, 0.57, 4 / 7, 0.6]
    results = []
    for point in points:
        for solver in ("CLARABEL", "SCS"):
            row = solve(point, solver)
            results.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    out = Path("artifacts/logs_whgap_review_20260728/whgap_full_sdp_crosscheck.json")
    out.write_text(
        json.dumps(
            {
                "anchoring_statement": (
                    "Run before opening proposer scripts, artifact tables, or logs."
                ),
                "formulation": "full real-symmetric 27x27 eta",
                "ordering": "(a,b1,b2) -> 9*a+3*b1+b2",
                "results": results,
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
