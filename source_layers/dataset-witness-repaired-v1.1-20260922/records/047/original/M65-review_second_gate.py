"""Independent reload/reconstruction audit for the n=19 second tame c=2 gate.

No proposer module is imported.  The archived JSON/NPZ data are checked from
representation-theoretic definitions, including a fresh action of the central
S_18 class sum on the stored fold vector.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction as F
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "artifacts/logs_se_trace_t5_second_tame_c2_gate_20260722"
FIRST_INV = ROOT / "artifacts/logs_se_trace_t5_tame_c2_gate_20260721/tame_c2_reduced_inventory.npz"
FIRST_WITNESS = ROOT / "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.npz"
FIRST_JSON = ROOT / "artifacts/logs_se_trace_t5_tame_c2_rcol_20260721/tame_c2_rcol.json"

N, Q, J = 19, 38, 6
THETA, ALPHA, BETA = (3, 2, 1), (2, 1), (2, 1)
LAMBDA, KAPPA, NU, LONG = (32, 3, 2, 1), (15, 2, 1), (16, 2, 1), (31, 3, 2, 1)
TAUS = (LONG, (32, 2, 2, 1), (32, 3, 1, 1), (32, 3, 2))
BRANCHES = ("long", "tail_1", "tail_2", "tail_3")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def hook_dimension(shape):
    hooks = 1
    for row, width in enumerate(shape):
        for col in range(width):
            hooks *= width - col + sum(other > col for other in shape[row + 1 :])
    return math.factorial(sum(shape)) // hooks


def content(shape):
    return sum(col - row for row, width in enumerate(shape) for col in range(width))


def partitions(total, ceiling=None):
    if total == 0:
        yield ()
        return
    ceiling = min(total, ceiling if ceiling is not None else total)
    for first in range(ceiling, 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def horizontal_strip(outer, inner):
    rank = max(len(outer), len(inner))
    outer = outer + (0,) * (rank - len(outer))
    inner = inner + (0,) * (rank - len(inner))
    if any(inner[i] > outer[i] for i in range(rank)):
        return False
    columns = [col for row in range(rank) for col in range(inner[row], outer[row])]
    return len(columns) == len(set(columns))


def skew_tableau_count(outer, inner=()):
    """Aitken determinant formula for the number of standard skew tableaux."""
    rank = len(outer)
    inner = inner + (0,) * (rank - len(inner))
    size = sum(outer) - sum(inner)
    matrix = []
    for i in range(rank):
        row = []
        for k in range(rank):
            value = outer[i] - inner[k] - i + k
            row.append(F(0) if value < 0 else F(1, math.factorial(value)))
        matrix.append(row)
    det = F(1)
    for col in range(rank):
        pivot = next(row for row in range(col, rank) if matrix[row][col])
        if pivot != col:
            matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
            det = -det
        value = matrix[col][col]
        det *= value
        matrix[col] = [x / value for x in matrix[col]]
        for row in range(col + 1, rank):
            factor = matrix[row][col]
            matrix[row] = [matrix[row][k] - factor * matrix[col][k] for k in range(rank)]
    answer = det * math.factorial(size)
    assert answer.denominator == 1
    return answer.numerator


def lr_coefficient(alpha, beta, theta):
    """Direct LR-word enumeration; sufficient here because the skew size is 3."""
    cells = [(r, c) for r, width in enumerate(theta) for c in range(width)
             if c >= (alpha[r] if r < len(alpha) else 0)]
    reading = sorted(cells, key=lambda rc: (rc[0], -rc[1]))
    remaining = list(beta)
    assignment = {}
    total = 0

    def visit(pos, prefix_counts):
        nonlocal total
        if pos == len(reading):
            total += 1
            return
        r, c = reading[pos]
        for value in range(1, len(beta) + 1):
            if remaining[value - 1] == 0:
                continue
            # Row weak increase: the already filled right neighbor is >= value.
            right = assignment.get((r, c + 1))
            if right is not None and value > right:
                continue
            # Column strict increase: the already filled upper neighbor is < value.
            above = assignment.get((r - 1, c))
            if above is not None and above >= value:
                continue
            counts = prefix_counts.copy()
            counts[value - 1] += 1
            if any(counts[i] < counts[i + 1] for i in range(len(counts) - 1)):
                continue
            remaining[value - 1] -= 1
            assignment[(r, c)] = value
            visit(pos + 1, counts)
            del assignment[(r, c)]
            remaining[value - 1] += 1

    visit(0, [0] * len(beta))
    return total


def standard_words(shape):
    word, out = [], []

    def visit(widths):
        if len(word) == sum(shape):
            out.append(tuple(word))
            return
        for row in range(len(shape)):
            if widths[row] == shape[row]:
                continue
            if row and widths[row] + 1 > widths[row - 1]:
                continue
            new = list(widths)
            new[row] += 1
            word.append(row)
            visit(tuple(new))
            word.pop()

    visit((0,) * len(shape))
    return out


def word_contents(word):
    widths = [0] * (max(word) + 1)
    out = []
    for row in word:
        out.append(widths[row] - row)
        widths[row] += 1
    return out


def seminormal_plan(words):
    index = {word: i for i, word in enumerate(words)}
    degree = len(words[0]) - 1
    diagonal = np.empty((degree, len(words)))
    target = np.full((degree, len(words)), -1, dtype=np.int32)
    off = np.zeros((degree, len(words)))
    for col, word in enumerate(words):
        contents = word_contents(word)
        for i in range(degree):
            distance = contents[i + 1] - contents[i]
            diagonal[i, col] = 1.0 / distance
            if abs(distance) != 1:
                swap = list(word)
                swap[i], swap[i + 1] = swap[i + 1], swap[i]
                target[i, col] = index[tuple(swap)]
                off[i, col] = math.sqrt(1 - 1 / distance**2)
    return diagonal, target, off


def validate_plan(diagonal, target, off):
    worst = 0.0
    for row in range(diagonal.shape[0]):
        live = target[row] >= 0
        idx = np.arange(diagonal.shape[1])[live]
        dst = target[row, live]
        checks = [
            np.max(np.abs(diagonal[row] ** 2 + off[row] ** 2 - 1)),
            np.max(np.abs(target[row, dst] - idx)) if len(idx) else 0,
            np.max(np.abs(diagonal[row, dst] + diagonal[row, idx])) if len(idx) else 0,
            np.max(np.abs(off[row, dst] - off[row, idx])) if len(idx) else 0,
        ]
        worst = max(worst, *(float(x) for x in checks))
    return worst


def axis_apply(vector, diagonal, target, off, axis):
    x = np.moveaxis(vector, axis, 0)
    shape = (len(diagonal),) + (1,) * (x.ndim - 1)
    out = diagonal.reshape(shape) * x
    live = target >= 0
    out[live] += off[live].reshape((-1,) + (1,) * (x.ndim - 1)) * x[target[live]]
    return np.moveaxis(out, 0, axis)


class IndependentCentral:
    def __init__(self, inventory):
        self.kappa = seminormal_plan(standard_words(KAPPA))
        self.nu = (
            inventory["nu_generator_diagonal"], inventory["nu_generator_target"],
            inventory["nu_generator_offdiagonal"],
        )

    def generator(self, i, vector):
        kd, kt, ko = self.kappa
        nd, nt, no = self.nu
        out = axis_apply(vector, kd[i], kt[i], ko[i], 0)
        return axis_apply(out, nd[i + 1], nt[i + 1], no[i + 1], 2)

    def jm(self, k, vector):
        if k == 1:
            return np.zeros_like(vector)
        sx = self.generator(k - 2, vector)
        return self.generator(k - 2, self.jm(k - 1, sx)) + sx

    def class_sum(self, vector):
        out = np.zeros_like(vector)
        for k in range(2, 19):
            out += self.jm(k, vector)
        return out


def fresh_spectrum_and_weights(inventory, z):
    central = IndependentCentral(inventory)
    norm = np.linalg.norm(z)
    basis = [z / norm]
    alpha, beta = [], []
    previous = None
    for degree in range(12):
        print(f"CENTRAL_ACTION {degree + 1}", flush=True)
        work = central.class_sum(basis[-1])
        a = float(np.vdot(basis[-1], work).real)
        alpha.append(a)
        work -= a * basis[-1]
        if previous is not None:
            work -= beta[-1] * previous
        for _ in range(2):
            for vector in basis:
                work -= float(np.vdot(vector, work).real) * vector
        b = float(np.linalg.norm(work))
        if b < 1e-7:
            break
        previous = basis[-1]
        beta.append(b)
        basis.append(work / b)
    tri = np.diag(alpha)
    for i in range(len(alpha) - 1):
        tri[i, i + 1] = tri[i + 1, i] = beta[i]
    eigenvalues, eigenvectors = np.linalg.eigh(tri)
    weights = norm**2 * eigenvectors[0] ** 2
    return eigenvalues, weights, alpha, beta


def check_manifest(directory):
    rows = []
    for line in (directory / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        expected, name = line.split("  ", 1)
        actual = sha(directory / name)
        rows.append({"file": name, "expected": expected, "actual": actual, "match": expected == actual})
    return {"ok": all(row["match"] for row in rows), "rows": rows}


def isolated_verifier():
    with tempfile.TemporaryDirectory(prefix="second-c2-independent-") as tmp:
        copied = Path(tmp) / SOURCE.name
        shutil.copytree(SOURCE, copied)
        proc = subprocess.run([sys.executable, str(copied / "verify_second_gate.py")],
                              cwd=copied, capture_output=True, text=True)
        return {"exit_code": proc.returncode, "stdout": proc.stdout.splitlines(),
                "stderr": proc.stderr.splitlines(), "pass": proc.returncode == 0}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    args = parser.parse_args()

    manifest = check_manifest(SOURCE)
    verifier = isolated_verifier()
    data = json.loads((SOURCE / "second_gate.json").read_text(encoding="utf-8"))
    inv = np.load(SOURCE / "second_gate_inventory.npz", allow_pickle=False)
    witness = np.load(SOURCE / "second_gate_witness.npz", allow_pickle=False)

    active = [p for p in partitions(N - 1) if len(p) <= 4
              and horizontal_strip(p, THETA) and horizontal_strip(LONG, p)]
    archived_active = [tuple(int(x) for x in row if x) for row in inv["active_mu"]]
    strict = N > 3 * J and Q == 2 * N
    lr = lr_coefficient(ALPHA, BETA, THETA)
    dimensions = {
        "nu_hook": hook_dimension(NU),
        "query_skew_aitken": skew_tableau_count(LONG, KAPPA),
        "fixed_fibre_skew_aitken": skew_tableau_count(LAMBDA, THETA),
    }
    inventory_checks = {
        "strict_tame": strict,
        "LR_multiplicity_independent": lr,
        "active_mu_independent": [list(x) for x in active],
        "active_mu_exact_match": active == archived_active,
        "dimensions": dimensions,
        "dimension_exact_match": dimensions == {
            "nu_hook": inv["nu_rowwords"].shape[0],
            "query_skew_aitken": inv["query_skew_rowwords"].shape[0],
            "fixed_fibre_skew_aitken": data["R_out"]["full_skew_dimension"],
        },
        "f_mu_exact_match": list(map(hook_dimension, active)) == inv["f_mu"].tolist(),
        "nu_words_unique": len({tuple(x) for x in inv["nu_rowwords"]}) == len(inv["nu_rowwords"]),
        "query_words_unique": len({tuple(x) for x in inv["query_skew_rowwords"]}) == len(inv["query_skew_rowwords"]),
    }
    plan_residuals = {
        "nu": validate_plan(inv["nu_generator_diagonal"], inv["nu_generator_target"], inv["nu_generator_offdiagonal"]),
        "query_skew": validate_plan(inv["skew_generator_diagonal"], inv["skew_generator_target"], inv["skew_generator_offdiagonal"]),
    }

    fmu = list(map(hook_dimension, active))
    d2 = [[F(int(witness["d2_numerator"][a, i]), int(witness["d2_denominator"][a, i]))
           for i in range(8)] for a in range(4)]
    json_rows = data["R_out"]["rows"]
    json_d2 = {(row["branch"], tuple(row["mu"])): F(row["d_squared"]) for row in json_rows}
    d2_match = all(d2[a][i] == json_d2[(BRANCHES[a], active[i])]
                   for a in range(4) for i in range(8))
    support_match = all((d2[a][i] != 0) == horizontal_strip(TAUS[a], active[i])
                        for a in range(4) for i in range(8))

    btheta = F(math.comb(Q, J) * hook_dimension(THETA), hook_dimension(LAMBDA))
    long_corner_content = 31
    removed_contents = (31, 1, -1, -3)
    deltas_plus_one = [1] + [long_corner_content - x + 1 for x in removed_contents[1:]]
    etas = [F(btheta * hook_dimension(TAUS[a]),
              math.comb(Q - 1, J) * deltas_plus_one[a]) for a in range(4)]
    aggregates = [sum(F(fmu[i]) * d2[a][i] for i in range(8)) for a in range(4)]
    expected_aggregates = [F(math.comb(N - 1, J)) * etas[a] for a in range(4)]
    rout_checks = {
        "d2_json_npz_exact_match": d2_match,
        "support_from_horizontal_strips_exact_match": support_match,
        "supported": sum(x != 0 for row in d2 for x in row),
        "forced_zero": sum(x == 0 for row in d2 for x in row),
        "B_theta": str(btheta),
        "delta_plus_one": deltas_plus_one,
        "eta": [str(x) for x in etas],
        "aggregates": [str(x) for x in aggregates],
        "aggregate_formula_exact_match": aggregates == expected_aggregates,
    }

    rmat = witness["R_color_to_carrier"]
    gram = rmat.T @ rmat
    r2 = F(2240, 2697)
    rcol_checks = {
        "R": rmat.tolist(), "gram": gram.tolist(), "target_squared": str(r2),
        "gram_residual_inf": float(np.linalg.norm(gram - float(r2) * np.eye(2), ord=np.inf)),
        "pass": np.linalg.norm(gram - float(r2) * np.eye(2), ord=np.inf) < 4e-12,
    }

    eigenvalues, numeric_weights, alpha, beta = fresh_spectrum_and_weights(inv, witness["z"])
    rounded = [round(x) for x in eigenvalues]
    expected_spectrum = sorted(content(mu) for mu in active)
    exact_q = [F(int(x), int(y)) for x, y in zip(witness["q_mu_numerator"], witness["q_mu_denominator"])]
    weight_by_eigen = dict(zip(rounded, numeric_weights))
    ordered_numeric_q = [weight_by_eigen[content(mu)] for mu in active]
    q_errors = [abs(ordered_numeric_q[i] - float(exact_q[i])) for i in range(8)]
    spectrum_checks = {
        "fresh_eigenvalues": eigenvalues.tolist(), "rounded": rounded,
        "expected_from_contents": expected_spectrum,
        "spectrum_exact_match": rounded == expected_spectrum,
        "fresh_q_by_active_mu": ordered_numeric_q,
        "exact_q": [str(x) for x in exact_q],
        "max_q_error": max(q_errors),
        "q_recovery_pass": max(q_errors) < 3e-12,
        "sum_q": str(sum(exact_q, F(0))),
        "z_norm_squared": float(np.vdot(witness["z"], witness["z"]).real),
        "lanczos_alpha": alpha, "lanczos_beta": beta,
    }

    color_dim = math.comb(J, 3) * hook_dimension(ALPHA) * hook_dimension(BETA)
    t_dimension = math.comb(N - 1, J) * color_dim
    cap_a = btheta**2 * t_dimension
    cap_b = cap_a / min(deltas_plus_one[1:])
    # The input-line norm uses f^theta; the larger color dimension enters T.
    t2 = [F(math.comb(N - 1, J) * hook_dimension(THETA), fmu[i]) * exact_q[i] for i in range(8)]
    rmu = [x / math.comb(J, 3) for x in t2]
    branch_values = [sum(F(fmu[i]) * d2[a][i] * rmu[i] for i in range(8)) for a in range(4)]
    ta, tb = branch_values[0], sum(branch_values[1:], F(0))
    gate_checks = {
        "color_dimension": color_dim, "T": t_dimension, "B_theta": str(btheta),
        "t_norm_squared": [str(x) for x in t2], "r_mu": [str(x) for x in rmu],
        "branch_values": [str(x) for x in branch_values],
        "T_a": str(ta), "T_b": str(tb), "T_a_cap": str(cap_a), "T_b_cap": str(cap_b),
        "archived_values_exact_match": ta == F(data["R_in_and_gate"]["T_a"])
        and tb == F(data["R_in_and_gate"]["T_b"])
        and cap_a == F(data["R_in_and_gate"]["T_a_cap"])
        and cap_b == F(data["R_in_and_gate"]["T_b_cap"]),
        "T_a_pass": ta < cap_a, "T_b_pass": tb < cap_b,
        "T_a_margin": str(cap_a - ta), "T_b_margin": str(cap_b - tb),
    }

    old_inv = np.load(FIRST_INV, allow_pickle=False)
    old_witness = np.load(FIRST_WITNESS, allow_pickle=False)
    old_json = json.loads(FIRST_JSON.read_text(encoding="utf-8"))
    reuse_checks = {
        "source_code_reused": True,
        "numeric_witness_reused": False,
        "new_inventory_shape": list(inv["nu_rowwords"].shape),
        "old_inventory_shape": list(old_inv["nu_rowwords"].shape),
        "new_z_shape": list(witness["z"].shape), "old_z_shape": list(old_witness["z"].shape),
        "new_z_payload_sha256": hashlib.sha256(witness["z"].tobytes()).hexdigest(),
        "old_z_payload_sha256": hashlib.sha256(old_witness["z"].tobytes()).hexdigest(),
        "new_q": [str(x) for x in exact_q],
        "old_q": [str(F(int(x), int(y))) for x, y in zip(old_witness["q_mu_numerator"], old_witness["q_mu_denominator"])],
        "new_R_squared": str(r2), "old_R_squared": old_json["R_squared_exact"],
        "static_dataflow": "new generator loads old Python constructors but only the newly written n=19 inventory NPZ; it does not load either n=18 numeric NPZ witness",
        "hardcoded_target_boundary": "Q19 rational targets are embedded in proposer code, but this review independently recovers them from the newly shaped z witness by fresh central-operator Lanczos",
    }
    reuse_checks["numeric_witness_reused"] = not (
        reuse_checks["new_inventory_shape"] != reuse_checks["old_inventory_shape"]
        and reuse_checks["new_z_shape"] != reuse_checks["old_z_shape"]
        and reuse_checks["new_z_payload_sha256"] != reuse_checks["old_z_payload_sha256"]
        and reuse_checks["new_q"] != reuse_checks["old_q"]
        and reuse_checks["new_R_squared"] != reuse_checks["old_R_squared"]
    )
    no_numeric_reuse = reuse_checks["numeric_witness_reused"] is False

    checks = {
        "manifest": manifest["ok"], "isolated_verifier": verifier["pass"],
        "strict_tame_and_lr2": strict and lr == 2,
        "inventory": all([inventory_checks["active_mu_exact_match"], inventory_checks["dimension_exact_match"],
                          inventory_checks["f_mu_exact_match"], inventory_checks["nu_words_unique"],
                          inventory_checks["query_words_unique"], max(plan_residuals.values()) < 1e-12]),
        "R_out": d2_match and support_match and aggregates == expected_aggregates,
        "R_col": rcol_checks["pass"],
        "spectrum_q": spectrum_checks["spectrum_exact_match"] and spectrum_checks["q_recovery_pass"],
        "exact_gates": gate_checks["archived_values_exact_match"] and gate_checks["T_a_pass"] and gate_checks["T_b_pass"],
        "no_n18_numeric_witness_reuse": no_numeric_reuse,
    }
    confirmed = all(checks.values())
    result = {
        "scope": "only n=19,q=38,j=6,theta=(3,2,1),alpha=beta=(2,1),c=2; no uniform inference",
        "manifest": manifest, "isolated_verifier": verifier,
        "inventory": inventory_checks, "generator_plan_residuals": plan_residuals,
        "R_out": rout_checks, "R_col": rcol_checks,
        "spectrum_and_q": spectrum_checks, "exact_gate": gate_checks,
        "reuse_boundary": reuse_checks, "checks": checks,
        "verdict": "CONFIRMED_SINGLE_GATE" if confirmed else "NOT_CONFIRMED",
        "uniform_c2_or_t5_promotion_licensed": False,
    }
    args.json.write_text(json.dumps(
        result, indent=2, sort_keys=True,
        default=lambda value: value.item() if isinstance(value, np.generic) else str(value),
    ) + "\n", encoding="utf-8")
    lines = [
        "SECOND TAME c=2 n=19 INDEPENDENT REVIEW",
        f"MANIFEST {'PASS' if checks['manifest'] else 'FAIL'}",
        f"ISOLATED_VERIFIER {'PASS' if checks['isolated_verifier'] else 'FAIL'}",
        f"STRICT_TAME_LR2 {'PASS' if checks['strict_tame_and_lr2'] else 'FAIL'}",
        f"INVENTORY {'PASS' if checks['inventory'] else 'FAIL'}",
        f"R_OUT {'PASS' if checks['R_out'] else 'FAIL'}",
        f"R_COL {'PASS' if checks['R_col'] else 'FAIL'}",
        f"SPECTRUM_Q {'PASS' if checks['spectrum_q'] else 'FAIL'} max_q_error={spectrum_checks['max_q_error']:.3e}",
        f"T_A {ta} < {cap_a} {'PASS' if gate_checks['T_a_pass'] else 'FAIL'}",
        f"T_B {tb} < {cap_b} {'PASS' if gate_checks['T_b_pass'] else 'FAIL'}",
        f"NO_N18_NUMERIC_REUSE {'PASS' if no_numeric_reuse else 'FAIL'}",
        f"VERDICT {result['verdict']}",
        "SCOPE SINGLE n=19 GATE ONLY; NO UNIFORM c>=2 OR T5 INFERENCE",
    ]
    args.log.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    if not confirmed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
