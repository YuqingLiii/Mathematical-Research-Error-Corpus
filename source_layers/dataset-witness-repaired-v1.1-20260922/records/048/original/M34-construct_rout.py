#!/usr/bin/env python3
"""Matrix-free physical Pieri-to-completion/query R_out recoupling.

All calculations take place in skew Specht modules.  The largest space is
S^{lambda/theta}, dimension 24360; no V_lambda ambient basis is constructed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import re
from fractions import Fraction
from pathlib import Path

os.environ["OMP_NUM_THREADS"] = "1"
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["MKL_DYNAMIC"] = "FALSE"

import numpy as np


THETA = (3, 2, 1)
LAMBDA = (30, 3, 2, 1)
ACTIVE_MU = (
    (14, 2, 1), (13, 3, 1), (13, 2, 2), (13, 2, 1, 1),
    (12, 3, 2), (12, 3, 1, 1), (12, 2, 2, 1), (11, 3, 2, 1),
)
BRANCHES = {
    "long": {"tau": (29, 3, 2, 1), "corner": (0, 29), "eta": Fraction(89001, 5600)},
    "tail_1": {"tau": (30, 2, 2, 1), "corner": (1, 2), "eta": Fraction(1, 28)},
    "tail_2": {"tau": (30, 3, 1, 1), "corner": (2, 1), "eta": Fraction(1, 25)},
    "tail_3": {"tau": (30, 3, 2), "corner": (3, 0), "eta": Fraction(1, 32)},
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_manifest(directory: Path) -> dict:
    rows = []
    for line in (directory / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if match is None:
            raise RuntimeError(f"malformed manifest row {line!r}")
        expected, name = match.groups()
        actual = sha256(directory / name)
        rows.append({"file": name, "expected": expected, "actual": actual,
                     "match": expected == actual})
    return {"all_match": all(row["match"] for row in rows), "files": rows}


def hook_dim(shape: tuple[int, ...]) -> int:
    hooks = 1
    for row, width in enumerate(shape):
        for column in range(width):
            hooks *= width - column + sum(lower > column for lower in shape[row + 1:])
    return math.factorial(sum(shape)) // hooks


def is_horizontal_strip(outer: tuple[int, ...], inner: tuple[int, ...]) -> bool:
    length = max(len(outer), len(inner)) + 1
    out = outer + (0,) * (length - len(outer))
    inn = inner + (0,) * (length - len(inner))
    return all(out[index] >= inn[index] >= out[index + 1] for index in range(length - 1))


def standard_skew_tableaux(outer: tuple[int, ...], inner: tuple[int, ...]):
    cells = {(row, column) for row, width in enumerate(outer)
             for column in range(width)
             if column >= (inner[row] if row < len(inner) else 0)}
    chosen: set[tuple[int, int]] = set()
    order: list[tuple[int, int]] = []
    output: list[tuple[tuple[int, int], ...]] = []

    def visit() -> None:
        if len(order) == len(cells):
            output.append(tuple(order))
            return
        available = []
        for cell in cells - chosen:
            row, column = cell
            if (row, column - 1) in cells and (row, column - 1) not in chosen:
                continue
            if (row - 1, column) in cells and (row - 1, column) not in chosen:
                continue
            available.append(cell)
        for cell in sorted(available):
            chosen.add(cell)
            order.append(cell)
            visit()
            order.pop()
            chosen.remove(cell)

    visit()
    return output


def seminormal_plans(tableaux):
    index = {tableau: position for position, tableau in enumerate(tableaux)}
    generator_count = len(tableaux[0]) - 1 if tableaux else 0
    size = len(tableaux)
    diagonal = np.empty((generator_count, size), dtype=np.float64)
    target = np.full((generator_count, size), -1, dtype=np.int32)
    off = np.zeros((generator_count, size), dtype=np.float64)
    for generator in range(generator_count):
        for column, tableau in enumerate(tableaux):
            left, right = tableau[generator], tableau[generator + 1]
            distance = (right[1] - right[0]) - (left[1] - left[0])
            diagonal[generator, column] = 1.0 / distance
            if abs(distance) != 1:
                swapped = list(tableau)
                swapped[generator], swapped[generator + 1] = swapped[generator + 1], swapped[generator]
                target[generator, column] = index[tuple(swapped)]
                off[generator, column] = math.sqrt(1.0 - 1.0 / (distance * distance))
    return diagonal, target, off


def apply_plan(diagonal, target, off, vector):
    result = diagonal * vector
    live = target >= 0
    result[target[live]] += off[live] * vector[live]
    return result


def trivial_seed(tableaux, tolerance=2e-12):
    """Exact squared coordinates of the unique trivial line, plus floats."""
    size = len(tableaux)
    diagonal, target, off = seminormal_plans(tableaux)

    def generator(index, vector):
        return apply_plan(diagonal[index], target[index], off[index], vector)

    weights: list[Fraction | None] = [None] * size
    weights[0] = Fraction(1)
    queue = [0]
    while queue:
        column = queue.pop(0)
        tableau = tableaux[column]
        for index in range(len(diagonal)):
            destination = int(target[index, column])
            if destination < 0:
                continue
            left, right = tableau[index], tableau[index + 1]
            distance = (right[1] - right[0]) - (left[1] - left[0])
            ratio = Fraction(distance - 1, distance + 1)
            candidate = weights[column] * ratio
            if weights[destination] is None:
                weights[destination] = candidate
                queue.append(destination)
            elif weights[destination] != candidate:
                raise RuntimeError("inconsistent exact trivial-line propagation")
    if any(weight is None for weight in weights):
        raise RuntimeError("trivial-line graph is disconnected")
    total = sum(weights, Fraction(0))
    normalized = [weight / total for weight in weights]
    seed = np.sqrt(np.asarray([float(weight) for weight in normalized]))

    def penalty(vector):
        result = np.zeros_like(vector)
        for index in range(len(diagonal)):
            result += vector - generator(index, vector)
        return result

    residuals = [float(np.linalg.norm(generator(index, seed) - seed))
                 for index in range(len(diagonal))]
    audit = {
        "dimension": size,
        "norm_squared": float(seed @ seed),
        "construction": "exact squared-coordinate propagation (d-1)/(d+1)",
        "generator_plus_one_worst_l2": max(residuals, default=0.0),
        "penalty_residual_l2": float(np.linalg.norm(penalty(seed))),
    }
    if audit["generator_plus_one_worst_l2"] > tolerance or audit["penalty_residual_l2"] > 1e-10:
        raise RuntimeError(f"trivial seed failed: {audit}")
    return seed, normalized, audit


def build(packet_dir: Path):
    packet_manifest = verify_manifest(packet_dir)
    packet_json = json.loads((packet_dir / "tame_c2_packet.json").read_text(encoding="utf-8"))
    packet_npz = np.load(packet_dir / "tame_c2_packet_subpacket.npz")
    f_mu = {mu: hook_dim(mu) for mu in ACTIVE_MU}

    # Unique S30-trivial fixed-fibre vector inside S^{lambda/theta}.
    full_tableaux = standard_skew_tableaux(LAMBDA, THETA)
    if len(full_tableaux) != 24360:
        raise RuntimeError(f"unexpected lambda/theta skew dimension {len(full_tableaux)}")
    full_index = {tableau: index for index, tableau in enumerate(full_tableaux)}
    fixed_fibre, fixed_weights, fixed_audit = trivial_seed(full_tableaux)

    rows = []
    chain_support_total = 0
    branch_overlap_sums = {name: Fraction(0) for name in BRANCHES}
    branch_d_weighted = {name: Fraction(0) for name in BRANCHES}
    forced_zeros = 0
    exact_chain_alignment = True

    for branch, info in BRANCHES.items():
        tau = info["tau"]
        corner = info["corner"]
        for mu in ACTIVE_MU:
            supported = is_horizontal_strip(tau, mu)
            if not supported:
                forced_zeros += 1
                rows.append({
                    "branch": branch, "mu": list(mu), "supported": False,
                    "overlap_squared": "0", "d_squared": "0", "a_mass": "0",
                    "reason": "Pieri coefficient c^{tau_gamma}_{mu,(18)}=0",
                })
                continue

            suffix = "_".join(str(value) for value in mu)
            p_tableaux = standard_skew_tableaux(mu, THETA)
            stored_p_seed = np.asarray(packet_npz[f"pieri_seed_{suffix}"], dtype=np.float64)
            p_seed, p_weights, p_audit = trivial_seed(p_tableaux)
            if np.linalg.norm(np.abs(stored_p_seed) - p_seed) > 2e-12:
                raise RuntimeError(f"persisted Pieri seed mismatch for {mu}")
            stored_rows = np.asarray(packet_npz[f"pieri_rowwords_{suffix}"], dtype=np.int8)
            rebuilt_rows = np.asarray([[row for row, _ in tableau] for tableau in p_tableaux], dtype=np.int8)
            if not np.array_equal(stored_rows, rebuilt_rows):
                raise RuntimeError(f"Pieri tableau order mismatch for {mu}")

            q_tableaux = standard_skew_tableaux(tau, mu)
            q_seed, q_weights, q_audit = trivial_seed(q_tableaux)
            overlap_squared = None
            support_weight = Fraction(0)
            support = 0
            for p_index, p_tableau in enumerate(p_tableaux):
                for q_index, q_tableau in enumerate(q_tableaux):
                    key = p_tableau + q_tableau + (corner,)
                    chain_weight = p_weights[p_index] * q_weights[q_index]
                    fixed_weight = fixed_weights[full_index[key]]
                    ratio = fixed_weight / chain_weight
                    if overlap_squared is None:
                        overlap_squared = ratio
                    elif overlap_squared != ratio:
                        exact_chain_alignment = False
                        raise RuntimeError(f"nonconstant exact chain ratio for {branch}, {mu}")
                    support_weight += fixed_weight
                    support += 1
            chain_support_total += support
            if overlap_squared is None or support_weight != overlap_squared:
                raise RuntimeError(f"exact support norm failed for {branch}, {mu}")
            overlap = math.sqrt(float(overlap_squared))
            overlap_squared_float = float(overlap_squared)
            d_squared = Fraction(math.comb(17, 6) * hook_dim(THETA), f_mu[mu]) * overlap_squared
            a_mass = 20 * d_squared
            branch_overlap_sums[branch] += overlap_squared
            branch_d_weighted[branch] += f_mu[mu] * d_squared
            rows.append({
                "branch": branch,
                "mu": list(mu),
                "supported": True,
                "pieri_left_dimension": len(p_tableaux),
                "pieri_right_dimension": len(q_tableaux),
                "chain_support": support,
                "left_seed_audit": p_audit,
                "right_seed_audit": q_audit,
                "overlap": overlap,
                "overlap_squared_numeric": overlap_squared_float,
                "overlap_squared": str(overlap_squared),
                "exact_coordinate_ratio_constant": True,
                "rational_reconstruction_abs": "0 (exact Fraction propagation)",
                "d_squared": str(d_squared),
                "d_squared_numeric": float(d_squared),
                "a_mass": str(a_mass),
                "a_mass_numeric": float(a_mass),
            })

    expected_d_sums = {
        row["branch"]: Fraction(row["d_squared_weighted_sum"])
        for row in packet_json["completed_subpacket"]["branch_aggregates"]
    }
    branch_checks = {}
    for branch, info in BRANCHES.items():
        overlap_expected = info["eta"] / hook_dim(THETA)
        overlap_actual = branch_overlap_sums[branch]
        d_expected = expected_d_sums[branch]
        branch_checks[branch] = {
            "overlap_squared_sum": str(overlap_actual),
            "expected_eta_over_f_theta": str(overlap_expected),
            "overlap_identity_abs": abs(float(overlap_actual - overlap_expected)),
            "sum_f_mu_d_squared": str(branch_d_weighted[branch]),
            "expected_sum_f_mu_d_squared": str(d_expected),
            "d_aggregate_identity": branch_d_weighted[branch] == d_expected,
            "numeric_reconstruction_abs": "0 (exact Fraction propagation)",
        }
        if overlap_actual != overlap_expected or branch_d_weighted[branch] != d_expected:
            raise RuntimeError(f"branch normalization failed for {branch}: {branch_checks[branch]}")

    total_overlap = sum(branch_overlap_sums.values(), Fraction(0))
    total_error = Fraction(0)
    if total_overlap != 1 or forced_zeros != 12 or chain_support_total != len(full_tableaux):
        raise RuntimeError((total_overlap, forced_zeros, chain_support_total))

    result = {
        "verdict": "COMPLETE",
        "target": "physical tame c=2 R_out and 8x4 |d_gamma,mu|^2 subpacket",
        "derivation": {
            "reduced_space": "S^{lambda/theta}",
            "reduced_dimension": len(full_tableaux),
            "fixed_fibre_vector": "unique unit S30-trivial vector w in S^{lambda/theta}",
            "chain_vectors": "unit S11 x S18-trivial vectors v_(gamma,mu) for theta->mu->tau_gamma->lambda",
            "overlap": "c_(gamma,mu)=<v_(gamma,mu),w>",
            "formula": "|d_(gamma,mu)|^2 = C(17,6) f^theta/f^mu * |c_(gamma,mu)|^2",
            "mass_formula": "a_(gamma,mu)=20|d_(gamma,mu)|^2",
            "why": "Frobenius reciprocity for the two multiplicity-one Pieri chains; induced-fibre Fourier normalization contributes C(17,6)f^theta/f^mu",
        },
        "fixed_fibre_audit": fixed_audit,
        "rows": rows,
        "checks": {
            "supported_entries": 20,
            "forced_zero_entries": forced_zeros,
            "orthogonal_chain_support_total": chain_support_total,
            "full_skew_dimension": len(full_tableaux),
            "total_overlap_squared": str(total_overlap),
            "total_overlap_numeric_reconstruction_abs": str(total_error),
            "branch_aggregate_checks": branch_checks,
            "exact_chain_alignment_all_rows": exact_chain_alignment,
            "max_rational_reconstruction_abs": "0 (not used)",
        },
        "source_packet_manifest": packet_manifest,
        "forbidden": {
            "ambient_V_lambda_built": False,
            "ambient_dense_matrix_built": False,
            "old_G6_used": False,
            "n7_values_used": False,
            "aggregate_constraints_used_to_fit_values": False,
            "aggregate_constraints_role": "post-computation exact checks only",
        },
        "storage": {
            "largest_vector_length": len(fixed_fibre),
            "largest_square_allocated": False,
        },
        "environment": {
            "python": platform.python_version(), "numpy": np.__version__,
            "platform": platform.platform(),
        },
    }
    row_lookup = {(row["branch"], tuple(row["mu"])): row for row in rows}
    def fraction_table(field):
        table = [[Fraction(row_lookup[(branch, mu)][field]) for mu in ACTIVE_MU]
                 for branch in BRANCHES]
        numerator = np.asarray([[value.numerator for value in line] for line in table], dtype=np.int64)
        denominator = np.asarray([[value.denominator for value in line] for line in table], dtype=np.int64)
        return numerator, denominator

    overlap_num, overlap_den = fraction_table("overlap_squared")
    d_num, d_den = fraction_table("d_squared")
    a_num, a_den = fraction_table("a_mass")
    arrays = {
        "fixed_fibre_S30_trivial": fixed_fibre,
        "active_mu": packet_npz["active_mu"],
        "f_mu": packet_npz["f_mu"],
        "branch_names_ascii": np.asarray([name.encode("ascii") for name in BRANCHES], dtype="S8"),
        "supported": np.asarray([[row_lookup[(branch, mu)]["supported"] for mu in ACTIVE_MU]
                                 for branch in BRANCHES], dtype=np.bool_),
        "overlap_squared_numerator": overlap_num,
        "overlap_squared_denominator": overlap_den,
        "d_squared_numerator": d_num,
        "d_squared_denominator": d_den,
        "a_mass_numerator": a_num,
        "a_mass_denominator": a_den,
    }
    return result, arrays


def render_log(result):
    lines = ["T5 TAME c=2 R_OUT", f"VERDICT {result['verdict']}",
             f"REDUCED_DIM={result['derivation']['reduced_dimension']}",
             f"FIXED_FIBRE_PLUS_RES={result['fixed_fibre_audit']['generator_plus_one_worst_l2']:.3e}"]
    for row in result["rows"]:
        lines.append(
            f"{row['branch']} mu={tuple(row['mu'])} support={row['supported']} "
            f"c2={row['overlap_squared']} d2={row['d_squared']} a={row['a_mass']}"
        )
    for branch, check in result["checks"]["branch_aggregate_checks"].items():
        lines.append(f"CHECK {branch} {check}")
    lines.append(f"CHECKS {result['checks']}")
    lines.append("AMBIENT=False OLD_G6=False N7=False FIT_FROM_AGGREGATES=False")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet-dir", type=Path, required=True)
    parser.add_argument("--npz", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    args = parser.parse_args()
    result, arrays = build(args.packet_dir)
    np.savez_compressed(args.npz, **arrays)
    result["storage"]["npz"] = {
        "path": str(args.npz), "bytes": args.npz.stat().st_size,
        "sha256": sha256(args.npz),
    }
    args.json.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    args.log.write_text(render_log(result), encoding="utf-8")
    print(render_log(result), end="")


if __name__ == "__main__":
    main()
