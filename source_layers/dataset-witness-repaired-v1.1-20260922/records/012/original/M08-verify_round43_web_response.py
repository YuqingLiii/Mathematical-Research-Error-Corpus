#!/usr/bin/env python3
"""Receipt, exact F_7, support, and finite-model checks for Round 43."""

from __future__ import annotations

from collections import Counter
import hashlib
from pathlib import Path

from verify_round43_translation import (
    holomorphic_coefficients,
    padded_basis_all_c,
    target_and_ordinary,
)


ROOT = Path(__file__).resolve().parents[1]
PROMPT = ROOT / "artifacts" / "web-gpt56sol-pro" / "round-43-prompt-sent.md"
PROMPT_SOURCE = ROOT / "work" / "round-43-prompt.md"
RESPONSE = ROOT / "artifacts" / "web-gpt56sol-pro" / "round-43-response.md"
OUTPUT = ROOT / "outputs" / "round-43-gpt56sol-pro-response.md"

PROMPT_SHA = "e135851fe5568a472a3b52e8fbdb69ad3ed98f180ac59d83f7a9239d69386431"
RESPONSE_SHA = "1c1fa4ecde375c54610839f341b20637898d2dbae3450574de46023633d59a94"


def receipt_and_scope_checks() -> None:
    prompt = PROMPT.read_bytes()
    response = RESPONSE.read_bytes()
    assert prompt == PROMPT_SOURCE.read_bytes()
    assert response == OUTPUT.read_bytes()
    assert hashlib.sha256(prompt).hexdigest() == PROMPT_SHA
    assert hashlib.sha256(response).hexdigest() == RESPONSE_SHA
    assert len(prompt) == 7_954 and len(prompt.decode("utf-8")) == 7_952
    assert prompt.count(b"\n") == 251
    assert len(response) == 23_410 and len(response.decode("utf-8")) == 23_396
    assert response.count(b"\n") == 1_312
    text = response.decode("utf-8")
    for heading in (
        "# VERIFIED",
        "# CORRECTED",
        "# DISPROVED",
        "# NECESSARY-ONLY",
        "# EQUIVALENT",
        "# NUMERICAL-ONLY",
        "# CONJECTURED",
        "# OPEN",
    ):
        assert text.count(heading) == 1, heading
    for needle in (
        "ProjectiveResidual",
        "PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.",
        "No thirteen-slope ansatz theorem.",
        "The sign of the exact frozen residual",
        "The complete transpose-symmetric constant-separator problem reduces",
        "two-slope parity-separation theorem for every \\(p\\ge11\\)",
        "1+6\\cos(\\pi/7)",
    ):
        assert needle in text, needle


# Elements of Z[zeta_7], represented in the group ring.  Two coefficient
# vectors are equal exactly when their difference is a multiple of
# 1+zeta+...+zeta^6.
Cyclo = tuple[int, int, int, int, int, int, int]


def cy(values=()) -> Cyclo:
    result = [0] * 7
    for exponent, coefficient in values:
        result[exponent % 7] += coefficient
    return tuple(result)  # type: ignore[return-value]


ZERO = cy()
ONE = cy(((0, 1),))


def cadd(left: Cyclo, right: Cyclo) -> Cyclo:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def cneg(value: Cyclo) -> Cyclo:
    return tuple(-a for a in value)  # type: ignore[return-value]


def csub(left: Cyclo, right: Cyclo) -> Cyclo:
    return cadd(left, cneg(right))


def cmul(left: Cyclo, right: Cyclo) -> Cyclo:
    result = [0] * 7
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[(i + j) % 7] += a * b
    return tuple(result)  # type: ignore[return-value]


def cscale(value: Cyclo, scalar: int) -> Cyclo:
    return tuple(scalar * a for a in value)  # type: ignore[return-value]


def cconj(value: Cyclo) -> Cyclo:
    result = [0] * 7
    for exponent, coefficient in enumerate(value):
        result[-exponent % 7] += coefficient
    return tuple(result)  # type: ignore[return-value]


def canonical(value: Cyclo) -> Cyclo:
    offset = value[-1]
    return tuple(a - offset for a in value)  # type: ignore[return-value]


def ceq(left: Cyclo, right: Cyclo) -> bool:
    return canonical(csub(left, right)) == ZERO


def cpow(value: Cyclo, exponent: int) -> Cyclo:
    result = ONE
    for _ in range(exponent):
        result = cmul(result, value)
    return result


def abs_square(value: Cyclo) -> Cyclo:
    return cmul(value, cconj(value))


def exact_f7_arrays():
    # q_0, q_1, q_2 exactly as equations (10.1)--(10.3) of the response.
    q_hats = (
        {2: cy(((3, 1),)), -2: cy(((-3, -1),))},
        {3: cy(((3, 1),)), -3: cy(((-3, -1),))},
        {2: cy(((1, 1),)), -2: cy(((-1, -1),))},
    )
    hats = [[{} for _ in range(2)] for _ in range(4)]
    for local in range(3):
        hats[local][0] = {frequency % 7: value for frequency, value in q_hats[local].items()}
        hats[local + 1][1] = {
            frequency % 7: cmul(value, cy(((frequency, 1),)))
            for frequency, value in q_hats[local].items()
        }

    convolution = {}
    for i in range(4):
        for j in range(4):
            for delta in range(7):
                matrix = [[ZERO, ZERO], [ZERO, ZERO]]
                for a in range(2):
                    for b in range(2):
                        total = ZERO
                        for ell, left in hats[i][a].items():
                            right = hats[j][b].get((delta - ell) % 7, ZERO)
                            total = cadd(total, cmul(left, right))
                        matrix[a][b] = total
                convolution[i, j, delta] = matrix

    target = [[ZERO, ZERO], [ZERO, ZERO]]
    for i in range(4):
        for a in range(2):
            for b in range(2):
                target[a][b] = cadd(
                    target[a][b],
                    cmul(cy(((i, 1),)), convolution[i, i, 6][a][b]),
                )
                target[a][b] = cadd(
                    target[a][b],
                    cmul(cy(((-i, 1),)), convolution[i, i, 1][a][b]),
                )

    inv2 = 4
    ordinary = {}
    for physical_x in range(7):
        for y in range(7):
            if y == 0 and physical_x in (1, 6):
                continue
            matrix = [[ZERO, ZERO], [ZERO, ZERO]]
            for i in range(4):
                for j in range(4):
                    if ((i - j) * inv2) % 7 != y:
                        continue
                    midpoint = ((i + j) * inv2) % 7
                    phase = cy(((midpoint * physical_x, 1),))
                    term = convolution[i, j, (-physical_x) % 7]
                    for a in range(2):
                        for b in range(2):
                            matrix[a][b] = cadd(matrix[a][b], cmul(phase, term[a][b]))
            ordinary[physical_x, y] = matrix
    return target, ordinary


def exact_f7_checks() -> None:
    target, ordinary = exact_f7_arrays()
    algebraic_x = cneg(cadd(cy(((3, 1),)), cy(((4, 1),))))
    assert ceq(csub(cpow(algebraic_x, 3), cpow(algebraic_x, 2)), csub(cscale(algebraic_x, 2), ONE))
    target_cross = cadd(target[0][1], target[1][0])
    assert ceq(target[0][0], cscale(ONE, 2))
    assert ceq(target_cross, cscale(algebraic_x, 4))

    mixed = []
    diagonal_only = []
    cross_only = []
    for matrix in ordinary.values():
        diagonal = matrix[0][0]
        cross = cadd(matrix[0][1], matrix[1][0])
        if not ceq(diagonal, ZERO) and not ceq(cross, ZERO):
            mixed.append((diagonal, cross))
        elif not ceq(diagonal, ZERO):
            diagonal_only.append(diagonal)
        elif not ceq(cross, ZERO):
            cross_only.append(cross)

    assert len(mixed) == 4
    assert all(ceq(diagonal, algebraic_x) and ceq(cross, ONE) for diagonal, cross in mixed)

    x2 = cpow(algebraic_x, 2)
    diagonal_magnitudes = (
        (csub(csub(x2, algebraic_x), ONE), 2),
        (ONE, 4),
        (csub(x2, cscale(ONE, 2)), 2),
        (cscale(ONE, 2), 4),
        (cscale(ONE, 6), 1),
    )
    cross_magnitudes = (
        (csub(csub(x2, algebraic_x), ONE), 4),
        (ONE, 4),
        (algebraic_x, 4),
        (cscale(ONE, 2), 2),
        (csub(x2, ONE), 4),
        (cscale(algebraic_x, 2), 2),
        (cscale(csub(x2, ONE), 2), 2),
    )

    def classify(values, candidates) -> Counter:
        counts = Counter()
        for value in values:
            matches = [index for index, (magnitude, _) in enumerate(candidates) if ceq(abs_square(value), cpow(magnitude, 2))]
            assert len(matches) == 1, matches
            counts[matches[0]] += 1
        return counts

    assert classify(diagonal_only, diagonal_magnitudes) == Counter(
        {index: multiplicity for index, (_, multiplicity) in enumerate(diagonal_magnitudes)}
    )
    assert classify(cross_only, cross_magnitudes) == Counter(
        {index: multiplicity for index, (_, multiplicity) in enumerate(cross_magnitudes)}
    )

    # Exact totals and ratio denominators, before the final elementary inequality.
    diagonal_only_total = cadd(csub(cscale(x2, 4), cscale(algebraic_x, 2)), cscale(ONE, 12))
    cross_only_total = csub(cadd(cscale(x2, 12), cscale(algebraic_x, 4)), cscale(ONE, 4))
    diagonal_total = cadd(diagonal_only_total, cscale(algebraic_x, 4))
    cross_total = cadd(cross_only_total, cscale(ONE, 4))
    assert ceq(diagonal_total, cadd(cadd(cscale(x2, 4), cscale(algebraic_x, 2)), cscale(ONE, 12)))
    assert ceq(cross_total, cadd(cscale(x2, 12), cscale(algebraic_x, 4)))


def two_slope_support_checks() -> None:
    local_support = ({-1, 1}, {-2, 2}, {-1, 1})
    diagonal_by_difference = {}
    cross_by_difference = {}
    for i in range(3):
        for j in range(3):
            product = {left + right for left in local_support[i] for right in local_support[j]}
            diagonal_by_difference.setdefault(i - j, set()).update(product)
            cross_by_difference.setdefault(i - (j + 1), set()).update(product)
            cross_by_difference.setdefault((i + 1) - j, set()).update(product)
    for difference in set(diagonal_by_difference) | set(cross_by_difference):
        diagonal = diagonal_by_difference.get(difference, set())
        cross = cross_by_difference.get(difference, set())
        assert diagonal.isdisjoint(cross)
        assert all(exponent % 2 == difference % 2 for exponent in diagonal)
        assert all(exponent % 2 != difference % 2 for exponent in cross)
        assert all(-4 <= exponent <= 4 for exponent in diagonal | cross)
        for left in diagonal:
            for right in cross:
                assert 0 < abs(left - right) < 11

    # Numerical checks on genuine cofactors catch normalization, midpoint,
    # exceptional-coordinate, and arbitrary-scale mistakes independently.
    for prime, m, h, r0 in (
        (11, 1, 1, 0),
        (11, 2, 3, 1),
        (13, 2, 3, 4),
        (17, 3, 2, 5),
        (19, 4, 3, 2),
    ):
        roots = [(r0 + i * h) % prime for i in range(4)]
        assert len(set(roots)) == 4
        basis = padded_basis_all_c(prime, roots, [m % prime, (-m) % prime])
        convolution = holomorphic_coefficients(prime, basis)
        for nu in range(prime):
            _, ordinary = target_and_ordinary(prime, roots, convolution, nu)
            for matrix in ordinary.values():
                diagonal = matrix[0][0]
                cross = matrix[0][1] + matrix[1][0]
                assert not (abs(diagonal) > 2e-7 and abs(cross) > 2e-7)


def main() -> None:
    receipt_and_scope_checks()
    exact_f7_checks()
    two_slope_support_checks()
    print(
        "PASS Round 43 receipt, exact F_7 target/census, parity separation, "
        "and genuine adjacent-cofactor checks"
    )


if __name__ == "__main__":
    main()
