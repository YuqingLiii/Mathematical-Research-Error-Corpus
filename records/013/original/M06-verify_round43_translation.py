#!/usr/bin/env python3
"""Independent finite-field checks for the proposed Round 43 translation identities."""

from __future__ import annotations

import cmath
import itertools


def close(left: complex, right: complex, tol: float = 5e-6) -> None:
    scale = max(1.0, abs(left), abs(right))
    assert abs(left - right) <= tol * scale, (left, right, abs(left - right))


def determinant(matrix: list[list[complex]]) -> complex:
    n = len(matrix)
    total = 0j
    for permutation in itertools.permutations(range(n)):
        inversions = sum(
            permutation[a] > permutation[b]
            for a in range(n)
            for b in range(a + 1, n)
        )
        term: complex = -1 if inversions % 2 else 1
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def padded_basis_all_c(q: int, roots: list[int], slopes: list[int]):
    omega = cmath.exp(2j * cmath.pi / q)
    phase = [omega**exponent for exponent in range(q)]
    inv8 = pow(8, -1, q)
    n = len(roots)
    k = len(slopes)
    assert n == k + 2
    assert sum(slopes) % q == 0
    all_basis = []
    for c in range(q):
        matrix = [
            [phase[(-slope * (root + c) ** 2 * inv8) % q] for slope in slopes]
            for root in roots
        ]
        columns = []
        for support in (list(range(k + 1)), list(range(1, k + 2))):
            vector = [0j] * n
            submatrix = [matrix[index] for index in support]
            for local_index, global_index in enumerate(support):
                minor = [
                    row[:]
                    for row_index, row in enumerate(submatrix)
                    if row_index != local_index
                ]
                vector[global_index] = ((-1) ** local_index) * determinant(minor)
            columns.append(vector)
        all_basis.append(
            [[columns[column][row] for column in range(2)] for row in range(n)]
        )
    return all_basis


def holomorphic_coefficients(q: int, basis):
    omega = cmath.exp(2j * cmath.pi / q)
    n = len(basis[0])
    hats = [
        [
            [
                sum(
                    basis[c][i][component] * omega ** ((-ell * c) % q)
                    for c in range(q)
                )
                / q
                for component in range(2)
            ]
            for ell in range(q)
        ]
        for i in range(n)
    ]
    convolution = {}
    for i in range(n):
        for j in range(n):
            for delta in range(q):
                matrix = [[0j, 0j], [0j, 0j]]
                for ell in range(q):
                    left = hats[i][ell]
                    right = hats[j][(delta - ell) % q]
                    for a in range(2):
                        for b in range(2):
                            matrix[a][b] += left[a] * right[b]
                convolution[i, j, delta] = matrix
    return convolution


def target_and_ordinary(q: int, roots: list[int], convolution, nu: int):
    omega = cmath.exp(2j * cmath.pi / q)
    phase = [omega**exponent for exponent in range(q)]
    inv2 = pow(2, -1, q)
    n = len(roots)
    target = [[0j, 0j], [0j, 0j]]
    for i, root in enumerate(roots):
        plus = convolution[i, i, (nu - 1) % q]
        minus = convolution[i, i, (nu + 1) % q]
        for a in range(2):
            for b in range(2):
                target[a][b] += phase[root % q] * plus[a][b]
                target[a][b] += phase[(-root) % q] * minus[a][b]

    ordinary = {}
    for x in range(q):
        for y in range(q):
            matrix = [[0j, 0j], [0j, 0j]]
            for i in range(n):
                for j in range(n):
                    if ((roots[i] - roots[j]) * inv2) % q != y:
                        continue
                    midpoint = ((roots[i] + roots[j]) * inv2) % q
                    term = convolution[i, j, (nu - x) % q]
                    scalar = phase[(midpoint * x) % q]
                    for a in range(2):
                        for b in range(2):
                            matrix[a][b] += scalar * term[a][b]
            if not (y == 0 and x in (1, q - 1)):
                ordinary[x, y] = matrix
    return target, ordinary


def main() -> None:
    q = 17
    h = 2
    r0 = 3
    roots = [(r0 + i * h) % q for i in range(6)]
    slopes = [1, q - 1, 2, q - 2]
    basis = padded_basis_all_c(q, roots, slopes)

    # The second adjacent cofactor is the row-shifted first cofactor at c+h.
    for c in range(q):
        for i in range(1, 6):
            close(basis[c][i][1], basis[(c + h) % q][i - 1][0])

    convolution = holomorphic_coefficients(q, basis)
    omega = cmath.exp(2j * cmath.pi / q)
    for nu in range(q):
        target, ordinary = target_and_ordinary(q, roots, convolution, nu)
        translate_phase = omega ** ((nu * h) % q)
        close(target[1][1], translate_phase * target[0][0])
        for matrix in ordinary.values():
            close(matrix[1][1], translate_phase * matrix[0][0])

        for s0, s1 in ((2 + 3j, -1 + 0.5j), (1j, 2 - 4j), (1, 0)):
            factor = s0 + s1 * translate_phase
            direct_target = s0 * target[0][0] + s1 * target[1][1]
            close(direct_target, factor * target[0][0])
            direct_denominator = sum(
                abs(s0 * matrix[0][0] + s1 * matrix[1][1])
                for matrix in ordinary.values()
            )
            factored_denominator = abs(factor) * sum(
                abs(matrix[0][0]) for matrix in ordinary.values()
            )
            close(direct_denominator, factored_denominator)

        # The exact zero-factor diagonal separator annihilates target and ordinary arrays.
        s0 = 1 + 0j
        s1 = -1 / translate_phase
        close(s0 * target[0][0] + s1 * target[1][1], 0j)
        for matrix in ordinary.values():
            close(s0 * matrix[0][0] + s1 * matrix[1][1], 0j)

    print(
        "PASS Round 43 adjacent translation, diagonal target/ordinary phase, "
        "ratio factorization, and zero-factor checks"
    )


if __name__ == "__main__":
    main()
