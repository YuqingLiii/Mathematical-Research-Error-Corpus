#!/usr/bin/env python3
"""P9 E2: Choi hashing calibration and bounded filtered-hashing scans."""

from __future__ import annotations

import argparse
import json
import time
from itertools import combinations
from pathlib import Path

import mpmath as mp
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "artifacts" / "logs_whgap_p9_20260729"
STRIP_GRID = [0.42, 0.44, 0.46, 0.48, 0.49]
CALIBRATION_GRID = [0.385, 0.5, 0.55]
ALL_GRID = STRIP_GRID + CALIBRATION_GRID
RANDOM_LOW_RANK_PER_X = 120
TWO_COPY_RANDOM_PER_X = 30
NUMERICAL_FLOOR_BITS = 1e-10
STEP_CAP_SECONDS = 20 * 60
TWO_COPY_CAP_SECONDS = 20 * 60


def one_letter_kraus(x: float) -> np.ndarray:
    mats = [np.sqrt(1.0 - x) * np.eye(3, dtype=complex)]
    for mu in range(3):
        a = np.zeros((3, 3), dtype=complex)
        for j in range(3):
            for k in range(3):
                if len({mu, j, k}) == 3:
                    permutation = (mu, j, k)
                    inversions = sum(
                        permutation[p] > permutation[q]
                        for p in range(3)
                        for q in range(p + 1, 3)
                    )
                    a[j, k] = -1.0 if inversions % 2 else 1.0
        mats.append(np.sqrt(x / 2.0) * a)
    return np.stack(mats)


def normalized_choi(x: float) -> np.ndarray:
    phi = np.zeros(9, dtype=complex)
    phi[[0, 4, 8]] = 1 / np.sqrt(3)
    identity = np.eye(3, dtype=complex)
    choi = np.zeros((9, 9), dtype=complex)
    for k in one_letter_kraus(x):
        vector = np.kron(identity, k) @ phi
        choi += np.outer(vector, vector.conj())
    return (choi + choi.conj().T) / 2.0


def entropy_bits(matrix: np.ndarray) -> float:
    values = np.linalg.eigvalsh((matrix + matrix.conj().T) / 2.0).real
    values = np.clip(values, 0.0, None)
    positive = values[values > 1e-14]
    return float(-np.sum(positive * np.log2(positive)))


def partial_trace_a(rho: np.ndarray, dim_a: int, dim_b: int) -> np.ndarray:
    tensor = rho.reshape(dim_a, dim_b, dim_a, dim_b)
    return np.einsum("abac->bc", tensor, optimize=True)


def conditional_hash_bits(rho: np.ndarray, dim_a: int, dim_b: int) -> float:
    receiver = partial_trace_a(rho, dim_a, dim_b)
    return entropy_bits(receiver) - entropy_bits(rho)


def normalize_filter(matrix: np.ndarray) -> np.ndarray:
    norm = np.linalg.svd(matrix, compute_uv=False)[0]
    if norm < 1e-14:
        return np.zeros_like(matrix)
    return matrix / max(1.0, float(norm))


def filtered_rate(
    rho: np.ndarray, filter_a: np.ndarray, filter_b: np.ndarray
) -> tuple[float, float, float]:
    joint = np.kron(filter_a, filter_b)
    unnormalized = joint @ rho @ joint.conj().T
    success = float(np.trace(unnormalized).real)
    if success <= 1e-15:
        return success, float("-inf"), 0.0
    state = (unnormalized + unnormalized.conj().T) / (2.0 * success)
    hashing = conditional_hash_bits(state, filter_a.shape[0], filter_b.shape[0])
    return success, hashing, success * max(0.0, hashing)


def matrix_record(matrix: np.ndarray) -> dict:
    return {
        "real": matrix.real.tolist(),
        "imag": matrix.imag.tolist(),
        "rank": int(np.linalg.matrix_rank(matrix, tol=1e-10)),
        "operator_norm": float(np.linalg.svd(matrix, compute_uv=False)[0]),
    }


def evaluate_family(
    rho: np.ndarray,
    family: str,
    filters: list[tuple[str, np.ndarray, np.ndarray]],
) -> dict:
    best: dict | None = None
    positives = 0
    for label, filter_a, filter_b in filters:
        success, hashing, rate = filtered_rate(rho, filter_a, filter_b)
        positives += int(rate > NUMERICAL_FLOOR_BITS)
        if best is None or rate > best["rate_bits_per_input_pair"]:
            best = {
                "label": label,
                "success_probability": success,
                "hashing_bits_after_success": hashing,
                "rate_bits_per_input_pair": rate,
                "filter_a": matrix_record(filter_a),
                "filter_b": matrix_record(filter_b),
            }
    assert best is not None
    return {
        "family": family,
        "trials": len(filters),
        "positive_above_floor": positives,
        "best": best,
    }


def alice_postselection_only(
    filters: list[tuple[str, np.ndarray, np.ndarray]]
) -> list[tuple[str, np.ndarray, np.ndarray]]:
    """Make postselection direction-valid for A->B by leaving Bob trace preserving."""
    return [
        (f"{label}_Afilter_Bidentity", filter_a, np.eye(filter_b.shape[0]))
        for label, filter_a, filter_b in filters
    ]


def diagonal_filters(rng: np.random.Generator) -> list[tuple[str, np.ndarray, np.ndarray]]:
    records: list[tuple[str, np.ndarray, np.ndarray]] = [
        ("identity", np.eye(3), np.eye(3))
    ]
    for rank_a in (1, 2):
        for support_a in combinations(range(3), rank_a):
            for rank_b in (1, 2):
                for support_b in combinations(range(3), rank_b):
                    a = np.zeros(3)
                    b = np.zeros(3)
                    a[list(support_a)] = 1.0
                    b[list(support_b)] = 1.0
                    records.append(
                        (
                            f"projector_A{support_a}_B{support_b}",
                            np.diag(a),
                            np.diag(b),
                        )
                    )
    for index in range(80):
        ranks = rng.integers(1, 4, size=2)
        amplitudes_a = np.zeros(3)
        amplitudes_b = np.zeros(3)
        support_a = rng.choice(3, size=int(ranks[0]), replace=False)
        support_b = rng.choice(3, size=int(ranks[1]), replace=False)
        amplitudes_a[support_a] = np.exp(rng.uniform(-5.0, 0.0, size=len(support_a)))
        amplitudes_b[support_b] = np.exp(rng.uniform(-5.0, 0.0, size=len(support_b)))
        amplitudes_a /= amplitudes_a.max()
        amplitudes_b /= amplitudes_b.max()
        records.append(
            (
                f"random_diagonal_{index}",
                np.diag(amplitudes_a),
                np.diag(amplitudes_b),
            )
        )
    return records


def o3_projector_filters(
    rng: np.random.Generator,
) -> list[tuple[str, np.ndarray, np.ndarray]]:
    records = []
    for index in range(36):
        qa, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        qb, _ = np.linalg.qr(rng.normal(size=(3, 3)))
        rank_a = 1 + index % 2
        rank_b = 1 + (index // 2) % 2
        pa = qa[:, :rank_a] @ qa[:, :rank_a].T
        pb = qb[:, :rank_b] @ qb[:, :rank_b].T
        records.append((f"real_projectors_{index}", pa, pb))
    return records


def random_low_rank_matrix(
    rng: np.random.Generator, dimension: int, rank: int
) -> np.ndarray:
    left, _ = np.linalg.qr(
        rng.normal(size=(dimension, dimension))
        + 1j * rng.normal(size=(dimension, dimension))
    )
    right, _ = np.linalg.qr(
        rng.normal(size=(dimension, dimension))
        + 1j * rng.normal(size=(dimension, dimension))
    )
    singular = np.zeros(dimension)
    singular[:rank] = np.exp(rng.uniform(-4.0, 0.0, size=rank))
    singular[0] = 1.0
    return normalize_filter(left @ np.diag(singular) @ right.conj().T)


def random_low_rank_filters(
    rng: np.random.Generator, trials: int, dimension: int
) -> list[tuple[str, np.ndarray, np.ndarray]]:
    records = []
    for index in range(trials):
        rank_a = int(rng.integers(1, dimension + 1))
        rank_b = int(rng.integers(1, dimension + 1))
        records.append(
            (
                f"random_low_rank_{index}_r{rank_a}_{rank_b}",
                random_low_rank_matrix(rng, dimension, rank_a),
                random_low_rank_matrix(rng, dimension, rank_b),
            )
        )
    return records


def direct_hashing_calibration() -> dict:
    mp.mp.dps = 80

    def formula(x: mp.mpf) -> mp.mpf:
        return (
            mp.log(3)
            + (1 - x) * mp.log(1 - x)
            + x * mp.log(x / 3)
        ) / mp.log(2)

    root = mp.findroot(formula, (mp.mpf("0.39"), mp.mpf("0.392")))
    points = [
        mp.mpf("0.385"),
        mp.mpf("0.39"),
        root - mp.mpf("1e-20"),
        root + mp.mpf("1e-20"),
        mp.mpf("0.4"),
        mp.mpf("0.42"),
        mp.mpf("0.44"),
        mp.mpf("0.46"),
        mp.mpf("0.48"),
        mp.mpf("0.49"),
        mp.mpf("0.5"),
        mp.mpf("0.55"),
    ]
    records = []
    for x in points:
        numerical_choi = normalized_choi(float(x))
        numerical = conditional_hash_bits(numerical_choi, 3, 3)
        expected = formula(x)
        records.append(
            {
                "x": mp.nstr(x, 40),
                "formula_bits": mp.nstr(expected, 40),
                "choi_matrix_bits": numerical,
                "absolute_difference": mp.nstr(abs(expected - numerical), 20),
                "positive": bool(expected > 0),
            }
        )
    sign_rule = all(
        item["positive"] == (mp.mpf(item["x"]) < root) for item in records
    )
    matrix_agreement = all(
        mp.mpf(item["absolute_difference"]) < mp.mpf("2e-14") for item in records
    )
    protected_anchors = all(
        mp.mpf(item["formula_bits"]) <= 0
        for item in records
        if mp.mpf(item["x"]) >= mp.mpf("0.5")
    )
    return {
        "status": (
            "PASS" if sign_rule and matrix_agreement and protected_anchors else "FAIL"
        ),
        "x1": mp.nstr(root, 50),
        "formula_bits": (
            "log2(3)+(1-x)log2(1-x)+x*log2(x/3); "
            "equivalently log2(3)-H({1-x,x/3,x/3,x/3})"
        ),
        "choi_exact_spectrum": "{1-x,x/3,x/3,x/3,0x5}",
        "sign_positive_exactly_below_x1_on_test_set": sign_rule,
        "matrix_formula_agreement": matrix_agreement,
        "protected_anchor_signs": protected_anchors,
        "records": records,
    }


def selected_filters(
    filters: list[tuple[str, np.ndarray, np.ndarray]], allow_two_sided: bool
) -> list[tuple[str, np.ndarray, np.ndarray]]:
    return filters if allow_two_sided else alice_postselection_only(filters)


def one_copy_scan(global_start: float, allow_two_sided: bool) -> list[dict]:
    results = []
    for index, x in enumerate(ALL_GRID):
        if time.monotonic() - global_start > STEP_CAP_SECONDS:
            raise RuntimeError("20-minute single-step cap reached in one-copy S3")
        rng = np.random.default_rng(20260729 + 1009 * index)
        rho = normalized_choi(x)
        families = [
            evaluate_family(
                rho,
                (
                    "diagonal_rank_le_3_two_sided"
                    if allow_two_sided
                    else "diagonal_rank_le_3_A_to_B_valid"
                ),
                selected_filters(diagonal_filters(rng), allow_two_sided),
            ),
            evaluate_family(
                rho,
                (
                    "O3_adapted_real_projectors_two_sided"
                    if allow_two_sided
                    else "O3_adapted_real_projectors_A_to_B_valid"
                ),
                selected_filters(o3_projector_filters(rng), allow_two_sided),
            ),
            evaluate_family(
                rho,
                (
                    "random_complex_low_rank_two_sided"
                    if allow_two_sided
                    else "random_complex_low_rank_A_to_B_valid"
                ),
                selected_filters(
                    random_low_rank_filters(rng, RANDOM_LOW_RANK_PER_X, 3),
                    allow_two_sided,
                ),
            ),
        ]
        best = max(
            (family["best"] for family in families),
            key=lambda item: item["rate_bits_per_input_pair"],
        )
        results.append(
            {
                "x": x,
                "calibration_point": x in CALIBRATION_GRID,
                "families": families,
                "total_trials": sum(family["trials"] for family in families),
                "best": best,
                "positive_above_floor": (
                    best["rate_bits_per_input_pair"] > NUMERICAL_FLOOR_BITS
                ),
            }
        )
        print(
            f"S3 one-copy x={x:.3f} trials={results[-1]['total_trials']} "
            f"best_rate={best['rate_bits_per_input_pair']:.16g}",
            flush=True,
        )
    return results


def reordered_two_copy_choi(x: float) -> np.ndarray:
    one = normalized_choi(x)
    tensor = np.kron(one, one).reshape(3, 3, 3, 3, 3, 3, 3, 3)
    reordered = tensor.transpose(0, 2, 1, 3, 4, 6, 5, 7).reshape(81, 81)
    return (reordered + reordered.conj().T) / 2.0


def fixed_two_copy_filters() -> list[tuple[str, np.ndarray, np.ndarray]]:
    identity = np.eye(9)
    diagonal = np.zeros(9)
    diagonal[[0, 4, 8]] = 1.0
    correlated = np.diag(diagonal)
    antisymmetric_vectors = []
    for i, j in combinations(range(3), 2):
        vector = np.zeros(9)
        vector[3 * i + j] = 1 / np.sqrt(2)
        vector[3 * j + i] = -1 / np.sqrt(2)
        antisymmetric_vectors.append(vector)
    anti_basis = np.stack(antisymmetric_vectors, axis=1)
    antisymmetric = anti_basis @ anti_basis.T
    symmetric = identity - antisymmetric
    return [
        ("identity", identity, identity),
        ("maximally_correlated_projector", correlated, correlated),
        ("antisymmetric_projector", antisymmetric, antisymmetric),
        ("symmetric_projector", symmetric, symmetric),
        ("correlated_A_antisymmetric_B", correlated, antisymmetric),
        ("antisymmetric_A_correlated_B", antisymmetric, correlated),
    ]


def two_copy_scan(
    global_start: float, allow_two_sided: bool
) -> tuple[list[dict], float]:
    start = time.monotonic()
    results = []
    for index, x in enumerate(ALL_GRID):
        elapsed = time.monotonic() - start
        if elapsed > TWO_COPY_CAP_SECONDS or time.monotonic() - global_start > STEP_CAP_SECONDS:
            raise RuntimeError("two-copy S3 cap reached before completing the registered grid")
        rng = np.random.default_rng(20261729 + 2029 * index)
        rho = reordered_two_copy_choi(x)
        families = [
            evaluate_family(
                rho,
                (
                    "correlated_named_projectors_two_sided"
                    if allow_two_sided
                    else "correlated_named_projectors_A_to_B_valid"
                ),
                selected_filters(fixed_two_copy_filters(), allow_two_sided),
            ),
            evaluate_family(
                rho,
                (
                    "random_correlated_low_rank_two_sided"
                    if allow_two_sided
                    else "random_correlated_low_rank_A_to_B_valid"
                ),
                selected_filters(
                    random_low_rank_filters(rng, TWO_COPY_RANDOM_PER_X, 9),
                    allow_two_sided,
                ),
            ),
        ]
        best = max(
            (family["best"] for family in families),
            key=lambda item: item["rate_bits_per_input_pair"],
        )
        block_rate = best["rate_bits_per_input_pair"]
        results.append(
            {
                "x": x,
                "calibration_point": x in CALIBRATION_GRID,
                "families": families,
                "total_trials": sum(family["trials"] for family in families),
                "best_block_rate_bits_per_two_inputs": block_rate,
                "best_rate_bits_per_channel_use": block_rate / 2.0,
                "best": best,
                "positive_above_floor": block_rate / 2.0 > NUMERICAL_FLOOR_BITS,
            }
        )
        print(
            f"S3 two-copy x={x:.3f} trials={results[-1]['total_trials']} "
            f"best_per_use={block_rate / 2.0:.16g}",
            flush=True,
        )
    return results, time.monotonic() - start


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--allow-two-sided",
        action="store_true",
        help=(
            "Run the literal arbitrary F_A,F_B postselection calibration. "
            "This mode is expected to fail the protected anchors and is preserved "
            "only to diagnose the one-way direction issue."
        ),
    )
    args = parser.parse_args()
    allow_two_sided = bool(args.allow_two_sided)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    global_start = time.monotonic()
    calibration = direct_hashing_calibration()
    if calibration["status"] != "PASS":
        raise AssertionError("D2 hashing calibration failed")
    one_copy = one_copy_scan(global_start, allow_two_sided)
    two_copy, two_copy_elapsed = two_copy_scan(global_start, allow_two_sided)

    protected_failures = [
        {
            "layer": layer,
            "x": item["x"],
            "rate": (
                item["best"]["rate_bits_per_input_pair"]
                if layer == "one_copy"
                else item["best_rate_bits_per_channel_use"]
            ),
        }
        for layer, records in (("one_copy", one_copy), ("two_copy", two_copy))
        for item in records
        if item["x"] >= 0.5 and item["positive_above_floor"]
    ]
    strip_positives = [
        {
            "layer": layer,
            "x": item["x"],
            "rate": (
                item["best"]["rate_bits_per_input_pair"]
                if layer == "one_copy"
                else item["best_rate_bits_per_channel_use"]
            ),
        }
        for layer, records in (("one_copy", one_copy), ("two_copy", two_copy))
        for item in records
        if item["x"] in STRIP_GRID and item["positive_above_floor"]
    ]
    elapsed = time.monotonic() - global_start
    result = {
        "task": "WHGAP P9 E2 D2 + S3 filtered-hashing attack",
        "protocol_direction": (
            (
                "Literal arbitrary two-sided postselection calibration. This mode "
                "is not accepted as a one-way A->B protocol if it fails the proved "
                "x>=1/2 anchors."
            )
            if allow_two_sided
            else (
                "A->B one-way: stochastic postselection is applied on Alice only; "
                "Bob's filter is identity. The preliminary arbitrary two-sided-"
                "postselection pass is archived separately because it failed the "
                "proved x>=1/2 anchor and would require backward success communication."
            )
        ),
        "excluded_preliminary_pass": {
            "json": "artifacts/logs_whgap_p9_20260729/distillation_scan.json",
            "log": "artifacts/logs_whgap_p9_20260729/distillation_scan.log",
            "reason": (
                "Arbitrary two-sided postselection gave false positives at x=1/2 "
                "and 11/20; it is not interpreted as a one-way A->B protocol."
            ),
        },
        "status": "PASS" if not protected_failures else "FAIL",
        "D2_hashing_calibration": calibration,
        "S3_one_copy": {
            "random_low_rank_filters_per_x": RANDOM_LOW_RANK_PER_X,
            "results": one_copy,
        },
        "S3_two_copy": {
            "random_correlated_filters_per_x": TWO_COPY_RANDOM_PER_X,
            "hard_cap_seconds": TWO_COPY_CAP_SECONDS,
            "elapsed_seconds": two_copy_elapsed,
            "results": two_copy,
        },
        "numerical_floor_bits_per_channel_use": NUMERICAL_FLOOR_BITS,
        "protected_anchor_failures": protected_failures,
        "strip_positive_candidates": strip_positives,
        "G2_interpretation": (
            "MAJOR-positive numerical candidate; P3-grade rationalization and interval "
            "certification required before claiming a positive rate."
            if strip_positives
            else "bounded-null: no positive filtered-hashing rate above the numerical "
            "floor in the registered one- or two-copy families."
        ),
        "total_elapsed_seconds": elapsed,
        "single_step_cap_seconds": STEP_CAP_SECONDS,
        "single_step_cap_respected": elapsed <= STEP_CAP_SECONDS,
        "two_copy_cap_respected": two_copy_elapsed <= TWO_COPY_CAP_SECONDS,
    }
    out = LOG_DIR / (
        "distillation_scan.json"
        if allow_two_sided
        else "distillation_scan_direction_valid.json"
    )
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if protected_failures:
        raise SystemExit("protected x>=1/2 calibration attack produced a spurious positive")
    if elapsed > STEP_CAP_SECONDS:
        raise SystemExit("20-minute single-step cap exceeded")


if __name__ == "__main__":
    main()
