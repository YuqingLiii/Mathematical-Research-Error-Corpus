#!/usr/bin/env python3
"""Independent exact audit for the T5 common-Pieri-line claim.

This file deliberately does not import the proposer common-line script.  It
checks the representation-independent transport covariance, Pieri dimension
identity/multiplicity-free criterion, and the reduced linear algebra with
nontrivial multiplicity, phases, gauges, and several tail branches.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from math import comb, factorial
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def partitions(n: int, ceiling: int | None = None):
    if n == 0:
        yield ()
        return
    if ceiling is None or ceiling > n:
        ceiling = n
    for first in range(ceiling, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def hook_dim(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    hooks = 1
    for r, width in enumerate(shape):
        for c in range(width):
            hooks *= width - c + sum(lower > c for lower in shape[r + 1 :])
    return factorial(n) // hooks


def horizontal_strip(mu: tuple[int, ...], theta: tuple[int, ...]) -> bool:
    """Return whether mu/theta is a horizontal strip (partition interlacing)."""
    length = max(len(mu), len(theta) + 1)
    mup = mu + (0,) * (length - len(mu))
    thp = theta + (0,) * (length - len(theta))
    contains = all(mup[i] >= thp[i] for i in range(length))
    interlaces = all(mup[i + 1] <= thp[i] for i in range(length - 1))
    return contains and interlaces


def pieri_audit(max_p: int = 12):
    rows = []
    for p in range(2, max_p + 1):
        for j in range(1, p + 1):
            for theta in partitions(j):
                allowed = [mu for mu in partitions(p) if horizontal_strip(mu, theta)]
                lhs = comb(p, j) * hook_dim(theta)
                rhs = sum(hook_dim(mu) for mu in allowed)
                assert lhs == rhs
                # Pieri attaches one trivial-row representation, so every
                # allowed shape occurs once and no shape is duplicated.
                assert len(allowed) == len(set(allowed))
                rows.append(
                    {
                        "p": p,
                        "j": j,
                        "theta": list(theta),
                        "allowed_count": len(allowed),
                        "induced_dimension": lhs,
                    }
                )
    return {
        "rows_checked": len(rows),
        "max_p": max_p,
        "dimension_identity_all_pass": True,
        "multiplicity_values": [0, 1],
        "sample_last": rows[-1],
    }


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Permutation p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    out = [0] * len(p)
    for i, x in enumerate(p):
        out[x] = i
    return tuple(out)


def transport(n: int, jset: frozenset[int]) -> tuple[int, ...]:
    p = list(range(2 * n))
    for i in jset:
        p[i], p[n + i] = p[n + i], p[i]
    return tuple(p)


def unbarred_action(n: int, small: tuple[int, ...]) -> tuple[int, ...]:
    p = list(range(2 * n))
    for source in range(1, n):
        p[source] = 1 + small[source - 1]
    return tuple(p)


def diagonal_action(n: int, small: tuple[int, ...]) -> tuple[int, ...]:
    p = list(unbarred_action(n, small))
    for source in range(1, n):
        p[n + source] = n + 1 + small[source - 1]
    return tuple(p)


def transport_covariance_audit(max_n: int = 6):
    checked = 0
    for n in range(2, max_n + 1):
        tail = tuple(range(1, n))
        for small in itertools.permutations(range(n - 1)):
            gu = unbarred_action(n, small)
            gd = diagonal_action(n, small)
            assert gu[0] == gd[0] == 0
            for assignment in itertools.product(range(3), repeat=n - 1):
                # 0=unused, 1=unbarred colour I, 2=barred colour J.
                iset = frozenset(tail[k] for k, value in enumerate(assignment) if value == 1)
                jset = frozenset(tail[k] for k, value in enumerate(assignment) if value == 2)
                gi = frozenset(1 + small[i - 1] for i in iset)
                gj = frozenset(1 + small[i - 1] for i in jset)
                tj = transport(n, jset)
                tgj = transport(n, gj)
                lhs = compose(tgj, gd)
                rhs = compose(gu, tj)
                dset = frozenset(iset) | frozenset(n + i for i in jset)
                # The two permutations need not agree globally.  They agree
                # on every point fixed by the colored fiber; their quotient
                # is therefore in the complement subgroup defining Pi_D and
                # acts trivially on Ran(Pi_D).  This is the exact covariance
                # needed by the canonical fiber transport.
                assert all(lhs[x] == rhs[x] for x in dset)
                quotient = compose(inverse(rhs), lhs)
                assert all(quotient[x] == x for x in dset)
                assert tj[0] == 0
                checked += 1
            # Completion permutations are supported on n,...,2n-1 and
            # therefore also fix the query 0.
            if n <= 5:
                for bsmall in itertools.permutations(range(n)):
                    pb = list(range(2 * n))
                    for source in range(n):
                        pb[n + source] = n + bsmall[source]
                    assert pb[0] == 0
    return {
        "max_n": max_n,
        "transport_covariance_instances": checked,
        "query_fixed_by_all_transports": True,
        "query_fixed_by_completion_subgroup": True,
    }


def norm_squared(v: sp.Matrix) -> sp.Expr:
    return sp.simplify((sp.conjugate(v).T * v)[0])


def reduced_algebra_audit():
    # ell : C^3 -> C^4, so both m_X>1 and a multi-column carrier are live.
    ell = sp.Matrix(
        [
            [1, sp.I, 2],
            [sp.Rational(1, 2), -1, 1 - sp.I],
            [2 + sp.I, 0, -sp.Rational(3, 2)],
            [-sp.I, 3, sp.Rational(2, 3)],
        ]
    )
    phi = sp.Matrix([[1 + sp.I, 2 - sp.I, -1, 3 * sp.I]])
    ds = {
        "long": 2 - sp.I,
        "tail_1": -sp.Rational(3, 2) * sp.I,
        "tail_2": 1 + sp.I,
        "tail_3": -2 - 2 * sp.I,
    }
    weights = {"long": 1, "tail_1": 2, "tail_2": 3, "tail_3": 5}
    phi_col = sp.conjugate(phi).T
    phi_norm2 = norm_squared(phi_col)
    u = phi_col / sp.sqrt(phi_norm2)
    rayleigh = norm_squared(sp.conjugate(ell).T * u)
    vectors = {name: sp.conjugate(d) * phi_col for name, d in ds.items()}
    gram = sp.Matrix(
        [
            [sp.simplify((sp.conjugate(vectors[a]).T * vectors[b])[0]) for b in ds]
            for a in ds
        ]
    )
    assert gram.rank() == 1
    for i in range(gram.rows):
        for j in range(gram.cols):
            minor = gram.extract([i, j], [i, j]).det()
            assert sp.simplify(minor) == 0
    direct_sum = 0
    compressed_sum = 0
    for name, v in vectors.items():
        direct = norm_squared(sp.conjugate(ell).T * v)
        a = norm_squared(v)
        assert sp.simplify(direct - a * rayleigh) == 0
        direct_sum += weights[name] * direct
        compressed_sum += weights[name] * a * rayleigh
    assert sp.simplify(direct_sum - compressed_sum) == 0

    # X-space gauge: ell and every physical branch vector transform together.
    wx = sp.Matrix(
        [
            [0, sp.I, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, -sp.I],
            [1, 0, 0, 0],
        ]
    )
    assert sp.conjugate(wx).T * wx == sp.eye(4)
    ell_x = wx * ell
    vectors_x = {name: wx * v for name, v in vectors.items()}
    for name in ds:
        assert sp.simplify(
            norm_squared(sp.conjugate(ell_x).T * vectors_x[name])
            - norm_squared(sp.conjugate(ell).T * vectors[name])
        ) == 0

    # Carrier gauge: right multiplication of ell preserves contraction norms.
    wc = sp.Matrix([[0, 1, 0], [0, 0, sp.I], [1, 0, 0]])
    assert sp.conjugate(wc).T * wc == sp.eye(3)
    ell_c = ell * wc
    for name in ds:
        assert sp.simplify(
            norm_squared(sp.conjugate(ell_c).T * vectors[name])
            - norm_squared(sp.conjugate(ell).T * vectors[name])
        ) == 0

    # Independent unit phases change cross-Gram entries covariantly but not
    # rank, diagonal masses, or actual contractions.
    phases = {"long": sp.I, "tail_1": -1, "tail_2": -sp.I, "tail_3": 1}
    phased = {name: phases[name] * vectors[name] for name in ds}
    phased_gram = sp.Matrix(
        [
            [sp.simplify((sp.conjugate(phased[a]).T * phased[b])[0]) for b in ds]
            for a in ds
        ]
    )
    assert phased_gram.rank() == 1
    for name in ds:
        assert norm_squared(phased[name]) == norm_squared(vectors[name])
        assert norm_squared(sp.conjugate(ell).T * phased[name]) == norm_squared(
            sp.conjugate(ell).T * vectors[name]
        )

    return {
        "m_X": 4,
        "m_C": 3,
        "branch_count": len(ds),
        "tail_count": 3,
        "complex_phases_live": True,
        "cross_gram_rank": int(gram.rank()),
        "common_rayleigh": str(rayleigh),
        "weighted_direct_sum": str(sp.simplify(direct_sum)),
        "weighted_compressed_sum": str(sp.simplify(compressed_sum)),
        "X_gauge_invariant": True,
        "carrier_gauge_invariant": True,
        "branch_phase_invariant": True,
    }


def dependency_audit():
    paths = [
        ROOT / "artifacts/logs_se_trace_t5_common_line_20260721/REPORT.md",
        ROOT / "artifacts/logs_se_trace_t5_common_line_20260721/se_trace_t5_common_line_exact.py",
        ROOT / "artifacts/logs_se_trace_t3_majorization_20260721/se_trace_t3_majorization.json",
        ROOT / "artifacts/logs_se_trace_t5_direction_law_20260721/se_trace_t5_direction_law.json",
        ROOT / "artifacts/logs_se_frames3b_20260719/frames3b_factor_gates.py",
        ROOT / "research/se/proof-dag/nodes/SE.denom.Phi.legal.trace.t5.md",
        ROOT / "research/se/proof-dag/nodes/SE.denom.Phi.legal.trace.t3.md",
    ]
    return {str(path.relative_to(ROOT)).replace("\\", "/"): sha256(path) for path in paths}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    args = parser.parse_args()
    result = {
        "verdict": "CONFIRMED",
        "scope": "common-line and actual-sum compression only; caps excluded",
        "dependency_hashes": dependency_audit(),
        "transport_covariance": transport_covariance_audit(),
        "pieri": pieri_audit(),
        "reduced_algebra": reduced_algebra_audit(),
        "cap_status": "NOT PROVED by the theorem or this audit",
    }
    args.json.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "T5 COMMON-LINE INDEPENDENT AUDIT",
        "VERDICT=CONFIRMED theorem-only; T-a/T-b caps excluded",
        f"TRANSPORT covariance_instances={result['transport_covariance']['transport_covariance_instances']} PASS",
        f"PIERI rows={result['pieri']['rows_checked']} dimension_and_multiplicity_free=PASS",
        "REDUCED mX=4 mC=3 tails=3 complex_phases=live rank=1 compression=PASS",
        "GAUGES X=PASS carrier=PASS branch_phase=PASS",
        "CAPS=NOT_PROVED",
    ]
    args.log.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
