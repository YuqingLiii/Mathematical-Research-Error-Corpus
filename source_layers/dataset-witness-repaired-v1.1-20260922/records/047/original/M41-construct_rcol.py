#!/usr/bin/env python3
"""Reduced four-block recoupling for the tame c=2 R_col_to_car gap."""

from __future__ import annotations

import itertools
import json
import math
import time
from collections import deque
from fractions import Fraction
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ART = HERE.parent
INV_PATH = ART / "logs_se_trace_t5_tame_c2_gate_20260721" / "tame_c2_reduced_inventory.npz"
LONG = (29, 3, 2, 1)
KAPPA = (14, 2, 1)
NU = (15, 2, 1)
THETA = (3, 2, 1)
ALPHA = BETA = (2, 1)
ACTIVE = ((14, 2, 1), (13, 3, 1), (13, 2, 2), (13, 2, 1, 1),
          (12, 3, 2), (12, 3, 1, 1), (12, 2, 2, 1), (11, 3, 2, 1))
F_MU = (1105, 5236, 3536, 5355, 20400, 24752, 20944, 116688)
Z1_ACTIVE = (88, 76, 74, 72, 63, 61, 59, 49)
Q_EXACT = (Fraction(41785, 41743296), Fraction(284075, 19380816),
           Fraction(28615, 2608956), Fraction(273545, 8613696),
           Fraction(39275, 269178), Fraction(10555, 31059),
           Fraction(150205, 346086), Fraction(4400, 609))
T_FACTORS = (Fraction(896, 5), Fraction(416, 11), Fraction(56),
             Fraction(1664, 45), Fraction(728, 75), Fraction(8),
             Fraction(104, 11), Fraction(56, 33))
D2 = {
    "long": (Fraction(17391, 78400), Fraction(17391, 44800), Fraction(52173, 125440),
             Fraction(17391, 39200), Fraction(3069, 4480), Fraction(1023, 1400),
             Fraction(3069, 3920), Fraction(341, 280)),
    "tail_1": (Fraction(459, 45472), Fraction(0), Fraction(1023, 90944),
               Fraction(3267, 227360), Fraction(0), Fraction(0), Fraction(341, 22736), Fraction(0)),
    "tail_2": (Fraction(51, 11600), Fraction(39, 2800), Fraction(0), Fraction(429, 81200),
               Fraction(0), Fraction(11, 700), Fraction(0), Fraction(0)),
    "tail_3": (Fraction(153, 64960), Fraction(9, 1792), Fraction(837, 103936),
               Fraction(0), Fraction(31, 1920), Fraction(0), Fraction(0), Fraction(0)),
}


def skew_rowwords(outer, inner=()):
    """Standard skew tableaux as row-addition words."""
    rank = len(outer)
    start = tuple(inner) + (0,) * (rank - len(inner))
    total = sum(outer) - sum(inner)
    word = []
    out = []

    def visit(shape):
        if len(word) == total:
            out.append(tuple(word))
            return
        for row in range(rank):
            if shape[row] >= outer[row]:
                continue
            if row and shape[row] + 1 > shape[row - 1]:
                continue
            new = list(shape)
            new[row] += 1
            word.append(row)
            visit(tuple(new))
            word.pop()
    visit(start)
    return out


def word_contents(word, inner=()):
    rank = max(len(inner), max(word, default=-1) + 1)
    widths = list(inner) + [0] * (rank - len(inner))
    values = []
    for row in word:
        column = widths[row]
        widths[row] += 1
        values.append(column - row)
    return values


def plan(rowwords, inner=()):
    index = {word: j for j, word in enumerate(rowwords)}
    n = len(rowwords[0])
    diagonal = np.empty((n - 1, len(rowwords)))
    target = np.full((n - 1, len(rowwords)), -1, dtype=np.int32)
    off = np.zeros((n - 1, len(rowwords)))
    for col, word in enumerate(rowwords):
        content = word_contents(word, inner)
        for i in range(n - 1):
            distance = content[i + 1] - content[i]
            diagonal[i, col] = 1.0 / distance
            if abs(distance) != 1:
                swapped = list(word)
                swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
                target[i, col] = index[tuple(swapped)]
                off[i, col] = math.sqrt(1.0 - 1.0 / distance**2)
    return diagonal, target, off


def apply(diagonal, target, off, vector):
    if vector.ndim == 1:
        out = diagonal * vector
        live = target >= 0
        out[live] += off[live] * vector[target[live]]
    else:
        out = diagonal[:, None] * vector
        live = target >= 0
        out[live] += off[live, None] * vector[target[live]]
    return out


def trivial_seed(rowwords, inner=()):
    """Unit trivial line, with exact squared coordinates."""
    if len(rowwords) == 1:
        return np.ones(1), [Fraction(1)]
    index = {word: j for j, word in enumerate(rowwords)}
    weights = [None] * len(rowwords)
    weights[0] = Fraction(1)
    queue = deque([0])
    while queue:
        col = queue.popleft()
        word = rowwords[col]
        content = word_contents(word, inner)
        for i in range(len(word) - 1):
            distance = content[i + 1] - content[i]
            if abs(distance) == 1:
                continue
            swapped = list(word)
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
            destination = index[tuple(swapped)]
            candidate = weights[col] * Fraction(distance - 1, distance + 1)
            if weights[destination] is None:
                weights[destination] = candidate
                queue.append(destination)
            elif weights[destination] != candidate:
                raise RuntimeError("inconsistent trivial seed")
    total = sum(weights, Fraction(0))
    normalized = [value / total for value in weights]
    return np.sqrt(np.asarray([float(value) for value in normalized])), normalized


def standard_shape_words(shape):
    return skew_rowwords(shape, ())


def stored_apply(inv, prefix, i, vector):
    d = inv[f"{prefix}_generator_diagonal"][i]
    t = inv[f"{prefix}_generator_target"][i]
    o = inv[f"{prefix}_generator_offdiagonal"][i]
    return apply(d, t, o, vector)


def jm_apply(inv, k, vector):
    if k == 1:
        return np.zeros_like(vector)
    sx = stored_apply(inv, "skew", k - 2, vector)
    return stored_apply(inv, "skew", k - 2, jm_apply(inv, k - 1, sx)) + sx


def chebyshev_weight_project(inv, k, content, vector):
    scale = k - 1
    raw = np.arange(-scale, scale + 1)
    coefficients = np.polynomial.chebyshev.chebfit(
        raw / scale, (raw == content).astype(float), len(raw) - 1)
    t0 = vector
    out = coefficients[0] * t0
    t1 = jm_apply(inv, k, vector) / scale
    out += coefficients[1] * t1
    for degree in range(2, len(coefficients)):
        t2 = 2 * jm_apply(inv, k, t1) / scale - t0
        out += coefficients[degree] * t2
        t0, t1 = t1, t2
    return out


def deterministic_basis(columns, dimension=2, tolerance=1e-8):
    projector = columns @ columns.T
    basis = []
    for coordinate in range(len(columns)):
        vector = projector[:, coordinate].copy()
        for old in basis:
            vector -= old * np.dot(old, vector)
        norm = np.linalg.norm(vector)
        if norm > tolerance:
            vector /= norm
            if vector[np.flatnonzero(abs(vector) > 1e-13)[0]] < 0:
                vector = -vector
            basis.append(vector)
            if len(basis) == dimension:
                break
    if len(basis) != dimension:
        raise RuntimeError("failed deterministic basis")
    return np.column_stack(basis)


def query_jm_seeds(inv):
    nu_words = [tuple(map(int, row)) for row in inv["nu_rowwords"]]
    reference = min(range(len(nu_words)), key=lambda i: nu_words[i])
    reference_content = word_contents(nu_words[reference])
    # The reference nu tableau has labels 1,...,15 in one row.  First build
    # the exact 34-dimensional S15-invariant subspace of the 4896-dimensional
    # skew module, then impose only X16=-1, X17=0, X18=-2 in that space.
    outer_words = [tuple(map(int, row)) for row in inv["query_skew_rowwords"]]
    grouped = {}
    for word in outer_words:
        widths = list(KAPPA) + [0] * (len(LONG) - len(KAPPA))
        for row in word[:15]:
            widths[row] += 1
        tau = tuple(x for x in widths if x)
        grouped.setdefault(tau, set()).add(word[15:])
    column_keys = [(tau, suffix) for tau in sorted(grouped, reverse=True)
                   for suffix in sorted(grouped[tau])]
    key_index = {key: i for i, key in enumerate(column_keys)}
    invariant = np.zeros((len(outer_words), len(column_keys)))
    prefix_coefficients = {}
    for tau in grouped:
        words = skew_rowwords(tau, KAPPA)
        seed, _ = trivial_seed(words, KAPPA)
        prefix_coefficients[tau] = dict(zip(words, seed))
    for row, word in enumerate(outer_words):
        widths = list(KAPPA) + [0] * (len(LONG) - len(KAPPA))
        for rr in word[:15]:
            widths[rr] += 1
        tau = tuple(x for x in widths if x)
        invariant[row, key_index[(tau, word[15:])]] = prefix_coefficients[tau][word[:15]]
    gram = invariant.T @ invariant
    if np.linalg.norm(gram - np.eye(len(column_keys)), ord=np.inf) > 2e-12:
        raise RuntimeError("S15 invariant basis is not orthonormal")
    penalty = np.zeros((len(column_keys), len(column_keys)))
    for k in range(16, 19):
        residual = invariant.T @ jm_apply(inv, k, invariant)
        residual -= reference_content[k - 1] * np.eye(len(column_keys))
        penalty += residual.T @ residual
    eigenvalues, eigenvectors = np.linalg.eigh((penalty + penalty.T) / 2)
    if np.sum(eigenvalues < 1e-12) != 2:
        raise RuntimeError(f"query reference nullity is not two: {eigenvalues[:6]}")
    seeds = deterministic_basis(invariant @ eigenvectors[:, :2])
    residuals = [float(np.linalg.norm(jm_apply(inv, k, seeds)
                                      - reference_content[k - 1] * seeds))
                 for k in range(2, 19)]
    return seeds, reference, reference_content, eigenvalues, residuals


def propagate_query_embedding(inv, seeds, reference):
    nu_words = [tuple(map(int, row)) for row in inv["nu_rowwords"]]
    nu_index = {word: i for i, word in enumerate(nu_words)}
    embedding = np.empty((len(nu_words), len(seeds), 2), dtype=np.float64)
    known = np.zeros(len(nu_words), dtype=bool)
    embedding[reference] = seeds
    known[reference] = True
    queue = deque([reference])
    while queue:
        source = queue.popleft()
        word = nu_words[source]
        content = word_contents(word)
        for i in range(17):
            distance = content[i + 1] - content[i]
            if abs(distance) == 1:
                continue
            swapped = list(word)
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
            destination = nu_index[tuple(swapped)]
            candidate = (stored_apply(inv, "skew", i, embedding[source])
                         - embedding[source] / distance) / math.sqrt(1 - 1 / distance**2)
            if known[destination]:
                if np.linalg.norm(candidate - embedding[destination]) > 2e-6:
                    raise RuntimeError("query propagation inconsistency")
            else:
                embedding[destination] = candidate
                known[destination] = True
                queue.append(destination)
    if not np.all(known):
        raise RuntimeError("query graph incomplete")
    return embedding


def internal_pieri_vectors(shape, small_shape):
    small_words = standard_shape_words(small_shape)
    suffix_words = skew_rowwords(shape, small_shape)
    seed, weights = trivial_seed(suffix_words, small_shape)
    full_words = standard_shape_words(shape)
    index = {word: i for i, word in enumerate(full_words)}
    vectors = []
    for small in small_words:
        vector = np.zeros(len(full_words))
        for suffix, value in zip(suffix_words, seed):
            vector[index[small + suffix]] = value
        vectors.append(vector)
    return full_words, np.column_stack(vectors), suffix_words, seed, weights


def small_color_embedding():
    skew = skew_rowwords(THETA, ALPHA)
    d, t, o = plan(skew, ALPHA)
    beta_words = standard_shape_words(BETA)
    reference = min(range(len(beta_words)), key=lambda i: beta_words[i])
    target_content = word_contents(beta_words[reference])
    jm = [np.zeros((len(skew), len(skew)))]
    for i in range(2):
        generator = np.diag(d[i])
        live = t[i] >= 0
        generator[np.arange(len(skew))[live], t[i, live]] = o[i, live]
        jm.append(generator @ jm[-1] @ generator + generator)
    penalty = sum((jm[k - 1] - target_content[k - 1] * np.eye(len(skew))) @
                  (jm[k - 1] - target_content[k - 1] * np.eye(len(skew)))
                  for k in range(2, 4))
    eigenvalues, eigenvectors = np.linalg.eigh((penalty + penalty.T) / 2)
    seeds = deterministic_basis(eigenvectors[:, :2])
    # Propagate each copy to both beta tableaux.
    beta_index = {word: i for i, word in enumerate(beta_words)}
    embedding = np.empty((len(beta_words), len(skew), 2))
    embedding[reference] = seeds
    known = {reference}
    queue = deque([reference])
    while queue:
        source = queue.popleft()
        content = word_contents(beta_words[source])
        for i in range(2):
            distance = content[i + 1] - content[i]
            if abs(distance) == 1:
                continue
            swapped = list(beta_words[source])
            swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
            destination = beta_index[tuple(swapped)]
            candidate = (apply(d[i], t[i], o[i], embedding[source])
                         - embedding[source] / distance) / math.sqrt(1 - 1 / distance**2)
            if destination not in known:
                embedding[destination] = candidate
                known.add(destination)
                queue.append(destination)
    return skew, beta_words, embedding, eigenvalues


def horizontal_endpoints():
    out = []
    for a in range(20, -1, -1):
        for b in range(min(a, 3), -1, -1):
            for c in range(min(b, 2), -1, -1):
                d = 20 - a - b - c
                shape = (a, b, c, d)
                if d < 0 or d > c or any(shape[i] > LONG[i] for i in range(4)):
                    continue
                if all(shape[i] >= (ALPHA[i] if i < len(ALPHA) else 0) for i in range(4)):
                    columns = []
                    for row, width in enumerate(LONG):
                        columns.extend(range(shape[row], width))
                    if len(columns) == len(set(columns)):
                        out.append(tuple(x for x in shape if x))
    return out


def compressed_recoupling(inv, query_embedding, color_embedding):
    k_words, k_vectors, k_suffix, k_seed, _ = internal_pieri_vectors(KAPPA, ALPHA)
    nu_words, nu_vectors, nu_suffix, nu_seed, _ = internal_pieri_vectors(NU, BETA)
    stored_nu = [tuple(map(int, row)) for row in inv["nu_rowwords"]]
    assert stored_nu == nu_words
    # Fold the propagated outer embedding with the beta+row15 internal vectors.
    g = np.empty((len(nu_vectors.T), len(inv["query_skew_rowwords"]), 2))
    for beta in range(nu_vectors.shape[1]):
        g[beta] = np.tensordot(nu_vectors[:, beta], query_embedding, axes=(0, 0))

    row_words = skew_rowwords(LONG, THETA)
    row_seed, _ = trivial_seed(row_words, THETA)
    outer_words = [tuple(map(int, row)) for row in inv["query_skew_rowwords"]]
    alpha_ref = 0
    beta_ref = 0
    # Kappa paths for one fixed alpha tableau.
    k_path_coeff = {word[len(standard_shape_words(ALPHA)[alpha_ref]):]: k_vectors[i, alpha_ref]
                    for i, word in enumerate(k_words) if k_vectors[i, alpha_ref] != 0}

    overlap = np.zeros((2, 2))
    dimensions = {}
    shuffle = ([i for i in range(13, -1, -1)]
               + [i for i in range(14, 0, -1)]
               + [i for i in range(15, 1, -1)])
    for tau in horizontal_endpoints():
        prefix_words = skew_rowwords(tau, ALPHA)
        prefix_index = {word: i for i, word in enumerate(prefix_words)}
        suffix_words = skew_rowwords(LONG, tau)
        suffix_seed, _ = trivial_seed(suffix_words, tau)
        suffix_coeff = dict(zip(suffix_words, suffix_seed))
        carrier = np.zeros((len(prefix_words), 2))
        for a_word, a_coeff in k_path_coeff.items():
            for b_index, b_word in enumerate(outer_words):
                prefix = a_word + b_word[:3]
                if prefix not in prefix_index:
                    continue
                suffix = b_word[3:]
                s_coeff = suffix_coeff.get(suffix)
                if s_coeff is not None:
                    carrier[prefix_index[prefix]] += a_coeff * s_coeff * g[beta_ref, b_index]
        physical = np.zeros((len(prefix_words), 2))
        for c_index, c_word in enumerate(skew_rowwords(THETA, ALPHA)):
            for r_index, r_word in enumerate(row_words):
                prefix = c_word + r_word[:14]
                if prefix not in prefix_index:
                    continue
                suffix = r_word[14:]
                s_coeff = suffix_coeff.get(suffix)
                if s_coeff is not None:
                    physical[prefix_index[prefix]] += (
                        color_embedding[beta_ref, c_index] * row_seed[r_index] * s_coeff)
        pd, pt, po = plan(prefix_words, ALPHA)
        moved = carrier
        for generator in shuffle:
            moved = apply(pd[generator], pt[generator], po[generator], moved)
        overlap += physical.T @ moved
        dimensions[str(tau)] = len(prefix_words)
    return overlap, dimensions


def permutation_word(images):
    current = list(range(len(images)))
    word = []
    for destination in range(len(images)):
        location = current.index(int(images[destination]))
        while location > destination:
            current[location - 1], current[location] = current[location], current[location - 1]
            word.append(location - 1)  # zero-based generator
            location -= 1
    return word


def extension(size, sources, targets):
    images = [-1] * size
    used = set()
    for source, target in zip(sources, targets):
        images[source] = target
        used.add(target)
    free_sources = [i for i, value in enumerate(images) if value < 0]
    free_targets = [i for i in range(size) if i not in used]
    for source, target in zip(free_sources, free_targets):
        images[source] = target
    return images


def permute_shape_vector(vector, images, plans):
    out = vector
    d, t, o = plans
    for generator in reversed(permutation_word(images)):
        out = apply(d[generator], t[generator], o[generator], out)
    return out


def build_fold_vector(inv, color_embedding, recoupling_squared):
    """Build z=(FL)^*delta as the literal coherent sum of 20 colorings."""
    k_words, k_vectors, _, _, _ = internal_pieri_vectors(KAPPA, ALPHA)
    nu_words, nu_vectors, _, _, _ = internal_pieri_vectors(NU, BETA)
    kd, kt, ko = plan(k_words)
    nd = inv["nu_generator_diagonal"]
    nt = inv["nu_generator_target"]
    no = inv["nu_generator_offdiagonal"]
    recoupling = math.sqrt(float(recoupling_squared))
    alpha_words = standard_shape_words(ALPHA)
    theta_words = standard_shape_words(THETA)
    theta_index = {word: i for i, word in enumerate(theta_words)}
    theta_skew = skew_rowwords(THETA, ALPHA)
    td, tt, to = plan(theta_words)
    delta_global = np.zeros(len(theta_words))
    delta_global[0] = 1.0
    # Full LR isometry in the theta GT basis.  The stored small embedding is
    # for one alpha tableau; Schur covariance repeats it for both alpha rows.
    color_full = np.zeros((len(theta_words), len(alpha_words), 2, 2))
    for alpha, alpha_word in enumerate(alpha_words):
        for skew_index, skew_word in enumerate(theta_skew):
            row = theta_index[alpha_word + skew_word]
            color_full[row, alpha] = color_embedding[:, skew_index, :]
    z = np.zeros((len(k_words), 2, len(nu_words)), dtype=np.float64)
    L = tuple(range(6))
    split_norms = []
    # Put the canonical beta block on matched positions 3,4,5.  Nu label 0
    # is unmatched, while matched position x is nu label x+1.
    nu_base_images = extension(18, (0, 1, 2), (4, 5, 6))
    nu_base = np.column_stack([
        permute_shape_vector(nu_vectors[:, beta], nu_base_images, (nd, nt, no))
        for beta in range(nu_vectors.shape[1])
    ])
    for I in itertools.combinations(L, 3):
        J = tuple(x for x in L if x not in I)
        color_images = list(I) + list(J)
        # One diagonal S6 coset representative on both carrier factors.
        k_images = color_images + list(range(6, 17))
        n_images = [0] + [color_images[x] + 1 for x in range(6)] + list(range(7, 18))
        k_split = np.column_stack([
            permute_shape_vector(k_vectors[:, alpha], k_images, (kd, kt, ko))
            for alpha in range(k_vectors.shape[1])
        ])
        n_vectors = np.column_stack([
            permute_shape_vector(nu_base[:, beta], n_images, (nd, nt, no))
            for beta in range(nu_vectors.shape[1])
        ])
        # tau_D maps the fixed labels (I on A, J on B) to their globally
        # ordered matched labels.  Pull the global theta basis vector back to
        # canonical block order alpha,beta before applying the LR adjoint.
        delta_block = delta_global
        for generator in permutation_word(color_images):
            delta_block = apply(td[generator], tt[generator], to[generator], delta_block)
        coefficients = recoupling * np.tensordot(delta_block, color_full, axes=(0, 0))
        # coefficients has axes alpha,beta,color-copy.
        block = np.zeros_like(z)
        for copy in range(2):
            block[:, copy, :] = k_split @ coefficients[:, :, copy] @ n_vectors.T
        split_norms.append(float(np.vdot(block, block).real))
        z += block
    return z, {
        "delta_theta_choice": "global lexicographic theta GT basis vector",
        "split_count": 20,
        "single_split_norm_squared_min": min(split_norms),
        "single_split_norm_squared_max": max(split_norms),
        "z_norm_squared": float(np.vdot(z, z).real),
        "color_isometry_gram_residual": float(np.linalg.norm(
            color_full.reshape(len(theta_words), -1).T @ color_full.reshape(len(theta_words), -1)
            - np.eye(8), ord=np.inf)),
    }


class CarrierCentral:
    def __init__(self, inv):
        k_words = standard_shape_words(KAPPA)
        self.kappa = plan(k_words)
        self.nu = (inv["nu_generator_diagonal"], inv["nu_generator_target"],
                   inv["nu_generator_offdiagonal"])

    @staticmethod
    def axis_apply(vector, diagonal, target, off, axis):
        x = np.moveaxis(vector, axis, 0)
        shape = (len(diagonal),) + (1,) * (x.ndim - 1)
        out = diagonal.reshape(shape) * x
        live = target >= 0
        out[live] += off[live].reshape((-1,) + (1,) * (x.ndim - 1)) * x[target[live]]
        return np.moveaxis(out, 0, axis)

    def generator(self, i, vector):
        kd, kt, ko = self.kappa
        nd, nt, no = self.nu
        out = self.axis_apply(vector, kd[i], kt[i], ko[i], 0)
        return self.axis_apply(out, nd[i + 1], nt[i + 1], no[i + 1], 2)

    def jm(self, k, vector):
        if k == 1:
            return np.zeros_like(vector)
        sx = self.generator(k - 2, vector)
        return self.generator(k - 2, self.jm(k - 1, sx)) + sx

    def z1(self, vector):
        out = np.zeros_like(vector)
        for k in range(2, 18):
            out += self.jm(k, vector)
        return out


def central_weights(inv, z):
    central = CarrierCentral(inv)
    norm = np.linalg.norm(z)
    basis = [z / norm]
    alpha = []
    beta = []
    timings = []
    previous = None
    for degree in range(12):
        start = time.perf_counter()
        work = central.z1(basis[-1])
        timings.append(time.perf_counter() - start)
        a = float(np.vdot(basis[-1], work).real)
        alpha.append(a)
        work -= a * basis[-1]
        if previous is not None:
            work -= beta[-1] * previous
        # Full double reorthogonalization keeps this short Krylov basis stable.
        for _ in range(2):
            for vector in basis:
                work -= float(np.vdot(vector, work).real) * vector
        b = float(np.linalg.norm(work))
        if b < 1e-7:
            break
        if degree == 11:
            beta.append(b)
            break
        previous = basis[-1]
        beta.append(b)
        basis.append(work / b)
    size = len(alpha)
    tridiagonal = np.diag(alpha)
    for i in range(size - 1):
        tridiagonal[i, i + 1] = tridiagonal[i + 1, i] = beta[i]
    eigenvalues, eigenvectors = np.linalg.eigh(tridiagonal)
    weights = norm**2 * eigenvectors[0] ** 2
    return (eigenvalues.tolist(), weights.tolist(), alpha, beta, timings,
            float(sum(weights) - norm**2))


def main():
    inv = np.load(INV_PATH, allow_pickle=False)
    seeds, reference, content, singular, jm_residuals = query_jm_seeds(inv)
    query_embedding = propagate_query_embedding(inv, seeds, reference)
    color_words, beta_words, color_embedding, color_eigenvalues = small_color_embedding()
    overlap, dimensions = compressed_recoupling(inv, query_embedding, color_embedding)
    exact_r2 = Fraction(3640, 4437)
    r2_residual = float(np.linalg.norm(overlap.T @ overlap - float(exact_r2) * np.eye(2), ord=np.inf))
    if r2_residual > 3e-12:
        raise RuntimeError(f"recoupling rational check failed: {r2_residual}")
    z, z_audit = build_fold_vector(inv, color_embedding, exact_r2)
    carrier_check = CarrierCentral(inv)
    theta_reference_content = word_contents(standard_shape_words(THETA)[0])
    z_audit["theta_JM_residuals"] = [float(np.linalg.norm(
        carrier_check.jm(k, z) - theta_reference_content[k - 1] * z)) for k in range(2, 7)]
    z_audit["S11_trivial_generator_residuals"] = [float(np.linalg.norm(
        carrier_check.generator(i, z) - z)) for i in range(6, 16)]
    del query_embedding
    z1_ritz, q_weights, lanczos_alpha, lanczos_beta, q_timings, q_sum_residual = central_weights(inv, z)
    rounded_ritz = [round(value) for value in z1_ritz]
    if rounded_ritz != sorted(Z1_ACTIVE):
        raise RuntimeError(f"unexpected carrier spectrum {z1_ritz}")
    q_numeric_by_eigen = dict(zip(rounded_ritz, q_weights))
    q_numeric = [q_numeric_by_eigen[eigen] for eigen in Z1_ACTIVE]
    q_reconstruction_residuals = [abs(value - float(exact))
                                  for value, exact in zip(q_numeric, Q_EXACT)]
    if max(q_reconstruction_residuals) > 3e-12:
        raise RuntimeError(f"q rational reconstruction failed: {q_reconstruction_residuals}")
    t_squared = [factor * q for factor, q in zip(T_FACTORS, Q_EXACT)]
    r_mu = [value / 20 for value in t_squared]
    branch_actual = {
        branch: sum(Fraction(F_MU[i]) * row[i] * r_mu[i] for i in range(8))
        for branch, row in D2.items()
    }
    actual_ta = branch_actual["long"]
    actual_tb = sum(branch_actual[name] for name in ("tail_1", "tail_2", "tail_3"))
    targets = [{
        "mu": list(ACTIVE[i]), "Z1": Z1_ACTIVE[i], "f_mu": F_MU[i],
        "q_mu": str(Q_EXACT[i]), "q_numeric": q_numeric[i],
        "q_reconstruction_abs": q_reconstruction_residuals[i],
        "t_norm_squared": str(t_squared[i]), "r_mu": str(r_mu[i]),
    } for i in range(8)]
    result = {
        "verdict": "COMPLETE",
        "query_seed_singular_values": singular.tolist(),
        "query_seed_jm_residuals": jm_residuals,
        "query_reference_index": reference,
        "compressed_dimensions": dimensions,
        "compressed_dimension_total": sum(dimensions.values()),
        "R_color_to_carrier": overlap.tolist(),
        "R_gram": (overlap.T @ overlap).tolist(),
        "R_determinant": float(np.linalg.det(overlap)),
        "R_squared_exact": str(exact_r2),
        "R_squared_rational_residual_inf": r2_residual,
        "color_penalty_eigenvalues": color_eigenvalues.tolist(),
        "fold_vector": z_audit,
        "targets": targets,
        "z1_ritz_eigenvalues": z1_ritz,
        "z1_lanczos_alpha": lanczos_alpha,
        "z1_lanczos_beta": lanczos_beta,
        "q_sum_minus_z_norm_squared": q_sum_residual,
        "z1_krylov_seconds": q_timings,
        "exact_checks": {
            "sum_q": str(sum(Q_EXACT)),
            "z_norm_squared_reconstruction": "254780/31059",
            "sum_q_equals_z_norm": sum(Q_EXACT) == Fraction(254780, 31059),
            "max_q_reconstruction_abs": max(q_reconstruction_residuals),
        },
        "actual_gates": {
            "branch_values": {key: str(value) for key, value in branch_actual.items()},
            "T_a": str(actual_ta), "T_a_float": float(actual_ta),
            "T_b": str(actual_tb), "T_b_float": float(actual_tb),
            "T_a_cap": "51396202/35",
            "T_b_cap": "51396202/1015",
            "T_a_pass": actual_ta <= Fraction(51396202, 35),
            "T_b_pass": actual_tb <= Fraction(51396202, 1015),
        },
    }
    (HERE / "tame_c2_rcol.json").write_text(json.dumps(result, indent=2) + "\n")
    np.savez_compressed(HERE / "tame_c2_rcol.npz", query_seeds=seeds,
                        R_color_to_carrier=overlap, z=z,
                        q_mu_numerator=np.asarray([q.numerator for q in Q_EXACT], dtype=np.int64),
                        q_mu_denominator=np.asarray([q.denominator for q in Q_EXACT], dtype=np.int64))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
