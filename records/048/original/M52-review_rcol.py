#!/usr/bin/env python3
"""Independent semantic/numerical review of the first tame c=2 R_col gate."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import time
from fractions import Fraction
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
ART = HERE.parent
SOURCE = ART / "logs_se_trace_t5_tame_c2_rcol_20260721"
INVENTORY = ART / "logs_se_trace_t5_tame_c2_gate_20260721"
ROUT = ART / "logs_se_trace_t5_tame_c2_rout_20260721"
ROUT_REVIEW = ART / "logs_se_trace_t5_tame_c2_rout_review_20260721"

LONG = (29, 3, 2, 1)
KAPPA = (14, 2, 1)
NU = (15, 2, 1)
THETA = (3, 2, 1)
ALPHA = BETA = (2, 1)
ACTIVE = ((14, 2, 1), (13, 3, 1), (13, 2, 2), (13, 2, 1, 1),
          (12, 3, 2), (12, 3, 1, 1), (12, 2, 2, 1), (11, 3, 2, 1))
BRANCHES = ("long", "tail_1", "tail_2", "tail_3")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def verify_manifest(directory: Path) -> dict:
    rows = []
    ok = True
    for line in (directory / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        expected, name = line.split(None, 1)
        path = directory / name.strip()
        actual = sha256(path)
        match = actual == expected
        ok &= match
        rows.append({"file": name.strip(), "expected": expected, "actual": actual, "match": match})
    return {"ok": ok, "rows": rows}


def rowwords(outer: tuple[int, ...], inner: tuple[int, ...] = ()) -> list[tuple[int, ...]]:
    """Enumerate standard tableaux by legal Young-lattice row additions."""
    inner = tuple(inner) + (0,) * (len(outer) - len(inner))
    answer: list[tuple[int, ...]] = []
    word: list[int] = []

    def visit(shape: tuple[int, ...]) -> None:
        if shape == outer:
            answer.append(tuple(word))
            return
        for r in range(len(outer)):
            if shape[r] == outer[r] or (r and shape[r] == shape[r - 1]):
                continue
            nxt = list(shape)
            nxt[r] += 1
            word.append(r)
            visit(tuple(nxt))
            word.pop()

    visit(inner)
    return answer


def contents(word: tuple[int, ...], inner: tuple[int, ...] = ()) -> list[int]:
    rank = max(len(inner), max(word, default=-1) + 1)
    widths = list(inner) + [0] * (rank - len(inner))
    out = []
    for r in word:
        out.append(widths[r] - r)
        widths[r] += 1
    return out


def own_plan(words: list[tuple[int, ...]], inner: tuple[int, ...] = ()):
    index = {word: i for i, word in enumerate(words)}
    n = len(words[0])
    diagonal = np.empty((n - 1, len(words)))
    target = np.full((n - 1, len(words)), -1, dtype=np.int32)
    off = np.zeros((n - 1, len(words)))
    for col, word in enumerate(words):
        cc = contents(word, inner)
        for i in range(n - 1):
            distance = cc[i + 1] - cc[i]
            diagonal[i, col] = 1.0 / distance
            if abs(distance) != 1:
                swapped = list(word)
                swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
                target[i, col] = index[tuple(swapped)]
                off[i, col] = math.sqrt(1.0 - 1.0 / distance**2)
    return diagonal, target, off


def apply(plan, i: int, vector: np.ndarray) -> np.ndarray:
    diagonal, target, off = plan
    d, t, o = diagonal[i], target[i], off[i]
    if vector.ndim == 1:
        out = d * vector
        live = t >= 0
        out[live] += o[live] * vector[t[live]]
    else:
        out = d[:, None] * vector
        live = t >= 0
        out[live] += o[live, None] * vector[t[live]]
    return out


def axis_apply(plan, i: int, vector: np.ndarray, axis: int) -> np.ndarray:
    diagonal, target, off = plan
    d, t, o = diagonal[i], target[i], off[i]
    x = np.moveaxis(vector, axis, 0)
    shape = (len(d),) + (1,) * (x.ndim - 1)
    out = d.reshape(shape) * x
    live = t >= 0
    out[live] += o[live].reshape((-1,) + (1,) * (x.ndim - 1)) * x[t[live]]
    return np.moveaxis(out, 0, axis)


def permutation_word(images: list[int]) -> list[int]:
    """Independent bubble decomposition with images[source]=target."""
    current = list(range(len(images)))
    word = []
    for destination, desired in enumerate(images):
        location = current.index(desired)
        while location > destination:
            current[location - 1], current[location] = current[location], current[location - 1]
            word.append(location - 1)
            location -= 1
    assert current == images
    return word


def permuted_list(size: int, word: list[int]) -> list[int]:
    values = list(range(size))
    for i in word:
        values[i], values[i + 1] = values[i + 1], values[i]
    return values


def extension(size: int, sources: tuple[int, ...], targets: tuple[int, ...]) -> list[int]:
    images = [-1] * size
    for source, target in zip(sources, targets):
        images[source] = target
    unused = iter(x for x in range(size) if x not in targets)
    for i in range(size):
        if images[i] < 0:
            images[i] = next(unused)
    return images


def permute_vector(vector: np.ndarray, images: list[int], plan) -> np.ndarray:
    out = vector
    for i in reversed(permutation_word(images)):
        out = apply(plan, i, out)
    return out


def pieri_embedding(shape: tuple[int, ...], small: tuple[int, ...], full_plan=None):
    small_words = rowwords(small)
    suffix_words = rowwords(shape, small)
    suffix_plan = own_plan(suffix_words, small)
    # Solve the common +1 line by ordinary symmetric eigendecomposition.
    penalty = np.zeros((len(suffix_words), len(suffix_words)))
    for i in range(len(suffix_words[0]) - 1):
        eye = np.eye(len(suffix_words))
        generator = apply(suffix_plan, i, eye)
        residual = generator - eye
        penalty += residual.T @ residual
    _, vectors = np.linalg.eigh((penalty + penalty.T) / 2)
    seed = vectors[:, 0]
    if seed[np.flatnonzero(abs(seed) > 1e-13)[0]] < 0:
        seed = -seed
    full_words = rowwords(shape)
    index = {word: i for i, word in enumerate(full_words)}
    embedding = np.zeros((len(full_words), len(small_words)))
    for j, small_word in enumerate(small_words):
        for suffix, value in zip(suffix_words, seed):
            embedding[index[small_word + suffix], j] = value
    return full_words, embedding


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    a = [row[:] for row in matrix]
    value = Fraction(1)
    for i in range(len(a)):
        pivot = next(j for j in range(i, len(a)) if a[j][i])
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            value = -value
        q = a[i][i]
        value *= q
        for j in range(i + 1, len(a)):
            factor = a[j][i] / q
            for k in range(i + 1, len(a)):
                a[j][k] -= factor * a[i][k]
    return value


def skew_dimension(outer: tuple[int, ...], inner: tuple[int, ...] = ()) -> int:
    n = sum(outer) - sum(inner)
    inner = tuple(inner) + (0,) * (len(outer) - len(inner))
    matrix = []
    for i in range(len(outer)):
        row = []
        for j in range(len(outer)):
            k = outer[i] - inner[j] - i + j
            row.append(Fraction(1, math.factorial(k)) if k >= 0 else Fraction(0))
        matrix.append(row)
    return int(math.factorial(n) * determinant(matrix))


def horizontal_endpoints() -> list[tuple[int, ...]]:
    answer = []
    for a in range(20, -1, -1):
        for b in range(min(a, 3), -1, -1):
            for c in range(min(b, 2), -1, -1):
                d = 20 - a - b - c
                shape = (a, b, c, d)
                if d < 0 or d > c or any(shape[i] > LONG[i] for i in range(4)):
                    continue
                if any(shape[i] < (ALPHA[i] if i < 2 else 0) for i in range(4)):
                    continue
                removed_columns = [column for r, width in enumerate(LONG)
                                   for column in range(shape[r], width)]
                if len(removed_columns) == len(set(removed_columns)):
                    answer.append(tuple(x for x in shape if x))
    return answer


class DiagonalS17:
    def __init__(self, kappa_plan, nu_plan):
        self.kappa_plan = kappa_plan
        self.nu_plan = nu_plan

    def generator(self, i: int, vector: np.ndarray) -> np.ndarray:
        out = axis_apply(self.kappa_plan, i, vector, 0)
        return axis_apply(self.nu_plan, i + 1, out, 2)

    def jm(self, k: int, vector: np.ndarray) -> np.ndarray:
        if k == 1:
            return np.zeros_like(vector)
        sx = self.generator(k - 2, vector)
        return self.generator(k - 2, self.jm(k - 1, sx)) + sx

    def central(self, vector: np.ndarray) -> np.ndarray:
        out = np.zeros_like(vector)
        for k in range(2, 18):
            out += self.jm(k, vector)
        return out


def central_content(shape: tuple[int, ...]) -> int:
    return sum(column - row for row, width in enumerate(shape) for column in range(width))


def frac(text: str) -> Fraction:
    return Fraction(text)


def main() -> None:
    source_manifest = verify_manifest(SOURCE)
    inventory_manifest = verify_manifest(INVENTORY)
    rout_manifest = verify_manifest(ROUT)
    rout_review_manifest = verify_manifest(ROUT_REVIEW)
    assert source_manifest["ok"] and inventory_manifest["ok"]
    assert rout_manifest["ok"] and rout_review_manifest["ok"]
    assert "**CONFIRMED.**" in (ROUT_REVIEW / "REPORT.md").read_text(encoding="utf-8")

    inv = np.load(INVENTORY / "tame_c2_reduced_inventory.npz", allow_pickle=False)
    packet = np.load(SOURCE / "tame_c2_rcol.npz", allow_pickle=False)
    source_json = json.loads((SOURCE / "tame_c2_rcol.json").read_text(encoding="utf-8"))

    # Re-enumerate both representation bases; do not use archived generator plans.
    nu_words = rowwords(NU)
    skew_words = rowwords(LONG, KAPPA)
    stored_nu = [tuple(map(int, word)) for word in inv["nu_rowwords"]]
    stored_skew = [tuple(map(int, word)) for word in inv["query_skew_rowwords"]]
    assert nu_words == stored_nu and skew_words == stored_skew
    nu_plan = own_plan(nu_words)
    skew_plan = own_plan(skew_words, KAPPA)
    kappa_words = rowwords(KAPPA)
    kappa_plan = own_plan(kappa_words)
    plan_comparison = {}
    for name, own in (("nu", nu_plan), ("skew", skew_plan)):
        plan_comparison[name] = {
            "diagonal_max_abs": float(np.max(abs(own[0] - inv[f"{name}_generator_diagonal"]))),
            "target_identical": bool(np.array_equal(own[1], inv[f"{name}_generator_target"])),
            "offdiagonal_max_abs": float(np.max(abs(own[2] - inv[f"{name}_generator_offdiagonal"]))),
        }
        assert plan_comparison[name]["diagonal_max_abs"] == 0
        assert plan_comparison[name]["target_identical"]
        assert plan_comparison[name]["offdiagonal_max_abs"] == 0

    # Independently audit query seed JM type using the fresh skew plan.
    seeds = packet["query_seeds"]
    reference = min(range(len(nu_words)), key=lambda i: nu_words[i])
    reference_content = contents(nu_words[reference])

    def skew_jm(k: int, vector: np.ndarray) -> np.ndarray:
        if k == 1:
            return np.zeros_like(vector)
        sx = apply(skew_plan, k - 2, vector)
        return apply(skew_plan, k - 2, skew_jm(k - 1, sx)) + sx

    seed_gram_residual = float(np.linalg.norm(seeds.T @ seeds - np.eye(2), ord=np.inf))
    seed_jm_residuals = [float(np.linalg.norm(skew_jm(k, seeds) - reference_content[k - 1] * seeds))
                         for k in range(2, 19)]

    # Exhaustive permutation-level audit of the corrected unmatched-nu convention.
    base_images = extension(18, (0, 1, 2), (4, 5, 6))
    assert base_images == [4, 5, 6, 0, 1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
    color_rows = []
    for I in itertools.combinations(range(6), 3):
        J = tuple(x for x in range(6) if x not in I)
        images = list(I) + list(J)
        word = permutation_word(images)
        inverse = [images.index(x) for x in range(6)]
        assert permuted_list(6, word) == images
        assert permuted_list(6, list(reversed(word))) == inverse
        k_images = images + list(range(6, 17))
        n_images = [0] + [images[x] + 1 for x in range(6)] + list(range(7, 18))
        assert n_images[0] == 0
        assert all(n_images[x + 1] == k_images[x] + 1 for x in range(6))
        color_rows.append({"I": list(I), "images": images, "word_length": len(word),
                           "nu_spectator_fixed": n_images[0] == 0,
                           "matched_shift_consistent": True})

    # A representation-level check: after base placement beta lives on nu labels 4,5,6.
    _, nu_embedding = pieri_embedding(NU, BETA)
    nu_base = np.column_stack([permute_vector(nu_embedding[:, j], base_images, nu_plan)
                               for j in range(nu_embedding.shape[1])])
    beta_words = rowwords(BETA)
    beta_plan = own_plan(beta_words)
    beta_intertwining = []
    for small_i, nu_i in enumerate((4, 5)):
        right_action = apply(beta_plan, small_i, np.eye(2))
        beta_intertwining.append(float(np.linalg.norm(apply(nu_plan, nu_i, nu_base)
                                                        - nu_base @ right_action)))

    # Independent Aitken dimensions and exact 42-swap block permutation.
    endpoints = horizontal_endpoints()
    endpoint_dimensions = {str(tau): skew_dimension(tau, ALPHA) for tau in endpoints}
    raw_dimension = skew_dimension(LONG, ALPHA)
    shuffle = list(range(13, -1, -1)) + list(range(14, 0, -1)) + list(range(15, 1, -1))
    shuffle_image = permuted_list(17, shuffle)
    assert raw_dimension == 3212127
    assert len(endpoints) == 8 and sum(endpoint_dimensions.values()) == 141168
    assert len(shuffle) == 42 and shuffle_image == [14, 15, 16] + list(range(14))

    R = packet["R_color_to_carrier"]
    exact_r2 = Fraction(3640, 4437)
    R_gram = R.T @ R
    R_residual = float(np.linalg.norm(R_gram - float(exact_r2) * np.eye(2), ord=np.inf))
    R_offdiag = float(max(abs(R[0, 1]), abs(R[1, 0])))

    z = packet["z"]
    diagonal = DiagonalS17(kappa_plan, nu_plan)
    theta_content = contents(min(rowwords(THETA)))
    theta_jm_residuals = [float(np.linalg.norm(diagonal.jm(k, z) - theta_content[k - 1] * z))
                          for k in range(2, 7)]
    s11_residuals = [float(np.linalg.norm(diagonal.generator(i, z) - z)) for i in range(6, 16)]

    # Fresh 8-step Lanczos from stored z, with independently generated actions.
    norm2 = float(np.vdot(z, z).real)
    basis = [z / math.sqrt(norm2)]
    alpha = []
    beta = []
    seconds = []
    closure = None
    for degree in range(8):
        started = time.perf_counter()
        work = diagonal.central(basis[-1])
        seconds.append(time.perf_counter() - started)
        a = float(np.vdot(basis[-1], work).real)
        alpha.append(a)
        work -= a * basis[-1]
        if degree:
            work -= beta[-1] * basis[-2]
        for _ in range(2):
            for old in basis:
                work -= float(np.vdot(old, work).real) * old
        b = float(np.linalg.norm(work))
        print(f"central Lanczos step {degree + 1}/8: alpha={a:.15g}, residual={b:.6g}", flush=True)
        if degree == 7:
            closure = b
            break
        beta.append(b)
        basis.append(work / b)
    tri = np.diag(alpha)
    for i, b in enumerate(beta):
        tri[i, i + 1] = tri[i + 1, i] = b
    eigenvalues, eigenvectors = np.linalg.eigh(tri)
    weights = norm2 * eigenvectors[0] ** 2
    expected_spectrum = sorted(central_content(mu) for mu in ACTIVE)
    rounded_spectrum = [round(x) for x in eigenvalues]
    assert rounded_spectrum == expected_spectrum
    by_spectrum = dict(zip(rounded_spectrum, weights))
    active_spectrum = [central_content(mu) for mu in ACTIVE]
    q_numeric = [float(by_spectrum[x]) for x in active_spectrum]
    q_recovered = [Fraction(x).limit_denominator(50_000_000) for x in q_numeric]

    # Compare only after independent reconstruction; stored numerator/denominator were not inputs.
    q_archived = [Fraction(int(n), int(d)) for n, d in
                  zip(packet["q_mu_numerator"], packet["q_mu_denominator"])]
    assert q_recovered == q_archived
    q_errors = [abs(q_numeric[i] - float(q_recovered[i])) for i in range(8)]
    sum_q = sum(q_recovered, Fraction(0))
    norm2_exact = Fraction(254780, 31059)
    assert sum_q == norm2_exact

    f_mu = [int(x) for x in inv["f_mu"]]
    inventory_active = [tuple(x for x in map(int, row) if x) for row in inv["active_mu"]]
    assert inventory_active == list(ACTIVE)
    normalization = [Fraction(math.comb(17, 6) * 16, f) for f in f_mu]
    t2 = [normalization[i] * q_recovered[i] for i in range(8)]
    r_mu = [x / 20 for x in t2]

    rout = json.loads((ROUT / "tame_c2_rout.json").read_text(encoding="utf-8"))
    d2 = {branch: [Fraction(0) for _ in ACTIVE] for branch in BRANCHES}
    for row in rout["rows"]:
        branch = row["branch"]
        mu = tuple(row["mu"])
        d2[branch][ACTIVE.index(mu)] = frac(row["d_squared"])
    branch_actual = {branch: sum(Fraction(f_mu[i]) * d2[branch][i] * r_mu[i]
                                 for i in range(8)) for branch in BRANCHES}
    actual_ta = branch_actual["long"]
    actual_tb = sum((branch_actual[b] for b in BRANCHES[1:]), Fraction(0))
    cap_a = Fraction(51396202, 35)
    cap_b = Fraction(51396202, 1015)

    checks = {
        "source_manifest": source_manifest["ok"],
        "inventory_manifest": inventory_manifest["ok"],
        "confirmed_rout_review_manifest": rout_review_manifest["ok"],
        "fresh_basis_and_plans": all(x["target_identical"] and x["diagonal_max_abs"] == 0
                                     and x["offdiagonal_max_abs"] == 0 for x in plan_comparison.values()),
        "query_seed_type": seed_gram_residual < 1e-12 and max(seed_jm_residuals) < 2e-12,
        "nu_unmatched_bug_absent": all(row["nu_spectator_fixed"] and row["matched_shift_consistent"]
                                       for row in color_rows) and max(beta_intertwining) < 1e-12,
        "reduced_block_shuffle": raw_dimension == 3212127 and sum(endpoint_dimensions.values()) == 141168,
        "R_gram": R_residual < 3e-12,
        "theta_JM": max(theta_jm_residuals) < 1e-12,
        "S11_invariance": max(s11_residuals) < 1e-12,
        "central_support_exactly_8": rounded_spectrum == expected_spectrum and closure < 1e-7,
        "q_recovered_not_loaded": q_recovered == q_archived and max(q_errors) < 3e-12,
        "q_sum": sum_q == norm2_exact and abs(norm2 - float(norm2_exact)) < 3e-12,
        "T_a_pass": actual_ta <= cap_a,
        "T_b_pass": actual_tb <= cap_b,
    }
    assert all(checks.values())

    result = {
        "verdict": "CONFIRMED",
        "scope": "first tame c=2 actual gate only",
        "integrity": {"source": source_manifest, "inventory": inventory_manifest,
                      "rout_source": rout_manifest, "confirmed_rout_review": rout_review_manifest},
        "inventory_semantic_audit": {
            "nu_basis_size": len(nu_words), "query_skew_basis_size": len(skew_words),
            "plan_comparison": plan_comparison,
            "query_seed_gram_residual_inf": seed_gram_residual,
            "query_seed_JM_residuals": seed_jm_residuals,
        },
        "colored_transport": {
            "nu_base_images": base_images,
            "nu_unmatched_label": 0,
            "coloring_count": len(color_rows),
            "all_spectator_fixed": all(row["nu_spectator_fixed"] for row in color_rows),
            "all_matched_shifts_consistent": all(row["matched_shift_consistent"] for row in color_rows),
            "carrier_word": "inverse/reversed adjacent word",
            "theta_pullback_word": "forward adjacent word",
            "beta_on_nu_labels_4_5_6_intertwining_residuals": beta_intertwining,
            "colorings": color_rows,
        },
        "block_shuffle": {
            "raw_Aitken_dimension": raw_dimension,
            "endpoint_count": len(endpoints),
            "endpoint_dimensions": endpoint_dimensions,
            "reduced_dimension_total": sum(endpoint_dimensions.values()),
            "shuffle_word_length": len(shuffle),
            "shuffle_image": shuffle_image,
            "R": R.tolist(), "R_gram": R_gram.tolist(),
            "R_squared_exact": str(exact_r2),
            "R_gram_residual_inf": R_residual, "R_offdiagonal_max_abs": R_offdiag,
        },
        "fold_invariance": {
            "z_shape": list(z.shape), "z_norm_squared_numeric": norm2,
            "theta_reference_contents_k2_to_k6": theta_content[1:6],
            "theta_JM_residuals": theta_jm_residuals,
            "S11_generator_residuals": s11_residuals,
        },
        "independent_central_lanczos": {
            "steps": len(alpha), "alpha": alpha, "beta": beta, "closure_residual": closure,
            "seconds": seconds, "ritz_eigenvalues": eigenvalues.tolist(),
            "rounded_spectrum": rounded_spectrum, "expected_spectrum_from_contents": expected_spectrum,
            "q_numeric_active_order": q_numeric,
            "q_recovered_active_order": [str(x) for x in q_recovered],
            "q_abs_errors": q_errors, "sum_q": str(sum_q),
            "stored_q_used_as_input": False,
        },
        "normalization_and_actual_gate": {
            "f_mu": f_mu,
            "normalization_C17_6_times_16_over_fmu": [str(x) for x in normalization],
            "t_norm_squared": [str(x) for x in t2],
            "r_mu_equals_t2_over_20": [str(x) for x in r_mu],
            "R_out_source": "independently CONFIRMED Rout review packet",
            "d2_positive_count": sum(x > 0 for row in d2.values() for x in row),
            "d2_zero_count": sum(x == 0 for row in d2.values() for x in row),
            "branch_values": {k: str(v) for k, v in branch_actual.items()},
            "T_a": str(actual_ta), "T_a_float": float(actual_ta),
            "T_a_cap": str(cap_a), "T_a_pass": actual_ta <= cap_a,
            "T_b": str(actual_tb), "T_b_float": float(actual_tb),
            "T_b_cap": str(cap_b), "T_b_pass": actual_tb <= cap_b,
        },
        "checks": checks,
        "forbidden_scope_modified": False,
    }
    (HERE / "rcol_review.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": result["verdict"], "checks": checks,
                      "spectrum": rounded_spectrum,
                      "q": [str(x) for x in q_recovered],
                      "T_a": str(actual_ta), "T_b": str(actual_tb)}, indent=2))


if __name__ == "__main__":
    main()
