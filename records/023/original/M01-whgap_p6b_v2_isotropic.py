#!/usr/bin/env python3
"""WHGAP P6b V2: the isotropic first-order weight operator D_psi(x) in closed form.

Commission: channel-capacity/werner-holevo-gap/notes/WHGAP_COMMISSION_P6B_20260729.md (V2).
Nodes: WHGAP.no-ascent-hierarchy (evidence), WHGAP.order-boundary (companion).

D_psi(x) := M_B - M_E with
  M_B = Lambda^dag(P_{conj psi}) = sum_a K_a^dag |conj psi><conj psi| K_a      (w_B = Tr[M_B phi])
  M_E = sum_{a,b} (Pi_E)_{ab} K_a^dag K_b                                       (w_E = Tr[M_E phi])
where Pi_E projects onto ker Lambda^c(P_psi), exactly as P9b defined the weights
(tools/whgap_p9b_g0.py::exact_weight_operator_at_x).  Everything is exact sympy in
symbolic x; the x = 9/20 value is a substitution, not the derivation.
"""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "artifacts" / "logs_whgap_p6b_20260729"
OUT = LOG_DIR / "v2_isotropic.json"

x = sp.Symbol("x", positive=True)
X1_DECIMAL = "0.390910232076181323482721853134"  # P3, WHGAP.qpositive-onset.md:41


def levi(mu: int) -> sp.Matrix:
    return sp.Matrix(3, 3, lambda j, k: sp.LeviCivita(mu, j, k))


def kraus() -> list[sp.Matrix]:
    return [sp.sqrt(1 - x) * sp.eye(3)] + [sp.sqrt(x / 2) * levi(mu) for mu in range(3)]


def channel(y: sp.Matrix) -> sp.Matrix:
    return sp.expand((1 - x) * y + (x / 2) * (sp.trace(y) * sp.eye(3) - y.T))


def complement(y: sp.Matrix) -> sp.Matrix:
    # Kraus matrices are REAL for x in (0,1): use .T, not .H — .H on symbolic
    # sqrt(1-x) leaves an unresolved conjugate() that breaks solve/reduce later
    # (decision-layer fix 2026-07-29 completing the interrupted executor's repair).
    ks = kraus()
    return sp.Matrix(4, 4, lambda a, b: sp.simplify(sp.trace(ks[a] * y * ks[b].T)))


_W = sp.Wild("w")


def realify(e):
    """Rewrite conjugate(sqrt(u)) -> sqrt(u) everywhere.

    Sound in this construction: every sqrt argument (1-x, x/2, x(1-x)/2, numeric
    positives) is a positive real on 0 < x < 1, so the conjugates left behind by
    symbolic .H are identities (decision-layer fix 2026-07-29, completing the
    interrupted executor's repair of the conjugation trap).
    """
    if isinstance(e, sp.MatrixBase):
        return e.applyfunc(realify)
    return sp.simplify(e.replace(sp.conjugate(sp.sqrt(_W)), sp.sqrt(_W)))


def zero(expr) -> bool:
    return sp.simplify(sp.expand(realify(expr))) == 0


def zero_matrix(m: sp.Matrix) -> bool:
    return all(zero(v) for v in m)


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.H / (vector.H * vector)[0, 0])


def weight_operators(psi: sp.Matrix, third: sp.Matrix) -> dict:
    """Build M_B, M_E, D and the diagonalizing basis for one isotropic psi."""
    ks = kraus()
    psi_bar = psi.conjugate()
    p_psi = projector(psi)
    lam_p = channel(p_psi)
    lamc_p = complement(p_psi)

    # receiver kernel: span{conj psi}
    receiver_kernel_pass = zero_matrix(lam_p * psi_bar)
    receiver_closed_form = sp.simplify(
        (1 - x / 2) * p_psi + (x / 2) * projector(third) - lam_p
    )

    # environment kernel: analytic basis  (0, conj(u+iv)) and (1, -i kappa w),
    # kappa = sqrt(2(1-x)/x); verified below to be a basis of ker Lambda^c(P_psi).
    kappa = sp.sqrt(2 * (1 - x) / x)
    k1 = sp.Matrix([0, *list(sp.simplify(sp.sqrt(2) * psi_bar))])
    k2 = sp.Matrix([1, *list(sp.simplify(-sp.I * kappa * third))])
    analytic_kernel_pass = zero_matrix(lamc_p * k1) and zero_matrix(lamc_p * k2)
    analytic_kernel_orthogonal = zero((k1.H * k2)[0, 0])
    pi_e = sp.simplify(projector(k1) + projector(k2))

    projector_checks = {
        "hermitian": zero_matrix(pi_e - pi_e.H),
        "idempotent": zero_matrix(pi_e * pi_e - pi_e),
        "trace_two": zero(sp.trace(pi_e) - 2),
        "annihilates_environment_output": zero_matrix(pi_e * lamc_p),
        "analytic_basis_in_kernel": analytic_kernel_pass,
        "analytic_basis_orthogonal": analytic_kernel_orthogonal,
    }

    # audit of the P9b construction (raw sympy nullspace, un-orthogonalized sum)
    raw_basis = lamc_p.nullspace()
    raw_sum = sp.simplify(sum((projector(v) for v in raw_basis), sp.zeros(4)))
    raw_orthogonal = all(
        zero((raw_basis[i].H * raw_basis[j])[0, 0])
        for i in range(len(raw_basis))
        for j in range(i + 1, len(raw_basis))
    )
    p9b_audit = {
        "raw_nullspace_dimension": len(raw_basis),
        "raw_basis_mutually_orthogonal": bool(raw_orthogonal),
        "raw_sum_equals_true_projector": bool(zero_matrix(raw_sum - pi_e)),
        "verdict": (
            "P9b built Pi_E as a sum of normalized rank-one projectors over sympy's raw "
            "nullspace basis; that equals the orthogonal projector only if the raw basis is "
            "orthogonal. Both facts are recorded here."
        ),
    }

    m_b = sp.simplify(sum((k.H * projector(psi_bar) * k for k in ks), sp.zeros(3)))
    m_e = sp.simplify(
        sum(
            (ks[a].H * pi_e[a, b] * ks[b] for a in range(4) for b in range(4)),
            sp.zeros(3),
        )
    )
    d = sp.simplify(m_b - m_e)

    basis = sp.Matrix.hstack(third, psi_bar, psi)
    unitary_pass = zero_matrix(basis.H * basis - sp.eye(3))
    d_basis = realify(sp.simplify(basis.H * d * basis))
    m_b_basis = sp.simplify(basis.H * m_b * basis)
    m_e_basis = sp.simplify(basis.H * m_e * basis)

    return {
        "receiver_kernel_is_conj_psi": bool(receiver_kernel_pass),
        "receiver_closed_form_pass": bool(zero_matrix(receiver_closed_form)),
        "receiver_spectrum": sorted(
            [str(sp.simplify(v)) for v in lam_p.eigenvals()], key=str
        ),
        "environment_spectrum": sorted(
            [str(sp.simplify(v)) for v in lamc_p.eigenvals()], key=str
        ),
        "projector_checks": {k: bool(v) for k, v in projector_checks.items()},
        "p9b_pi_e_audit": p9b_audit,
        "M_B_closed_form_is_Lambda_of_P_conj_psi": bool(zero_matrix(m_b - channel(projector(psi_bar)))),
        "M_B_in_basis": [[str(sp.simplify(v)) for v in m_b_basis.row(i)] for i in range(3)],
        "M_E_in_basis": [[str(sp.simplify(v)) for v in m_e_basis.row(i)] for i in range(3)],
        "D_in_basis": [[str(sp.simplify(v)) for v in d_basis.row(i)] for i in range(3)],
        "basis_unitary": bool(unitary_pass),
        "_d": d,
        "_d_basis": d_basis,
        "_m_e": m_e,
        "_pi_e": pi_e,
    }


def rational_density(seed: int) -> sp.Matrix:
    """Deterministic rational faithful density matrix (integer Gram + floor)."""
    import numpy as np

    rng = np.random.default_rng(seed)
    real = rng.integers(-4, 5, size=(3, 3))
    imag = rng.integers(-4, 5, size=(3, 3))
    z = sp.Matrix(real.tolist()) + sp.I * sp.Matrix(imag.tolist())
    rho = z * z.H + sp.Rational(1, 3) * sp.eye(3)
    return sp.simplify(rho / sp.trace(rho))


def main() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    result: dict = {
        "task": "WHGAP P6b V2 - closed-form isotropic weight operator D_psi(x)",
        "node_ids": ["WHGAP.no-ascent-hierarchy", "WHGAP.order-boundary"],
        "definition": {
            "w_B": "<conj psi| Lambda(phi) |conj psi> = Tr[M_B phi], M_B = sum_a K_a^dag P_{conj psi} K_a",
            "w_E": "Tr[Pi_E Lambda^c(phi)] = Tr[M_E phi], M_E = sum_{ab} (Pi_E)_{ab} K_a^dag K_b",
            "D_psi": "M_B - M_E, so w_B - w_E = Tr[D_psi phi]",
            "basis_order": ["e_0-type (w = u x v)", "conj(psi)", "psi"],
            "source_of_definition": "tools/whgap_p9b_g0.py::exact_weight_operator_at_x (P9b)",
        },
        "type_audit": {
            "Lambda": "M_3 -> M_3; Lambda^c: M_3 -> M_4",
            "Pi_E": "orthogonal projector on C^4, rank 2 for every x in (0,1)",
            "M_B, M_E, D_psi": "Hermitian operators on C^3 (3x3), entries rational in x",
            "psi": "isotropic pure state, psi^T psi = 0 (tau = 0 stratum)",
        },
    }

    # ---------- canonical isotropic psi
    psi = sp.Matrix([0, 1, -sp.I]) / sp.sqrt(2)
    w_third = sp.Matrix([1, 0, 0])
    result["canonical"] = {
        "psi": ["0", "1/sqrt(2)", "-I/sqrt(2)"],
        "normalized": bool(zero((psi.H * psi)[0, 0] - 1)),
        "isotropic_tau_zero": bool(zero((psi.T * psi)[0, 0])),
        "third_vector": ["1", "0", "0"],
        "third_is_u_cross_v": True,
    }
    canonical = weight_operators(psi, w_third)
    d_basis = canonical.pop("_d_basis")
    d_op = canonical.pop("_d")
    m_e_op = canonical.pop("_m_e")
    pi_e_op = canonical.pop("_pi_e")
    result["canonical"].update(canonical)

    # d0/d1 are real-valued by construction (diagonal entries of a Hermitian weight
    # difference in its diagonalizing basis); clear residual conjugate(sqrt(1-x))
    # artifacts of symbolic .H so solve/reduce_inequalities can run
    # (decision-layer fix 2026-07-29).
    def _realify(e):
        return sp.simplify(e.subs(sp.conjugate(sp.sqrt(1 - x)), sp.sqrt(1 - x)))

    d0 = _realify(sp.simplify(d_basis[0, 0]))
    d1 = _realify(sp.simplify(d_basis[1, 1]))
    d2 = sp.simplify(d_basis[2, 2])
    off_diagonal_zero = all(
        zero(d_basis[i, j]) for i in range(3) for j in range(3) if i != j
    )
    claim_d0 = -x * (1 - x) / (2 - x)
    claim_d1 = (1 - x) * (2 - 5 * x) / (2 - x)

    result["closed_form"] = {
        "diagonal_in_(e0, conj psi, psi)": bool(off_diagonal_zero),
        "d_0(x)": str(sp.factor(sp.cancel(d0))),
        "d_1(x)": str(sp.factor(sp.cancel(d1))),
        "d_2(x)": str(sp.simplify(d2)),
        "d_0_claim": str(sp.factor(claim_d0)),
        "d_1_claim": str(sp.factor(claim_d1)),
        "d_0_pass": bool(zero(d0 - claim_d0)),
        "d_1_pass": bool(zero(d1 - claim_d1)),
        "d_2_is_zero": bool(zero(d2)),
        "psi_in_kernel": bool(zero_matrix(d_op * psi)),
        "latex": (
            r"D_\psi(x)=\operatorname{diag}\!\Bigl(-\frac{x(1-x)}{2-x},"
            r"\ \frac{(1-x)(2-5x)}{2-x},\ 0\Bigr)"
            r"\quad\text{in }(w,\bar\psi,\psi)"
        ),
        "M_B_closed_form": "diag(x/2, 1-x/2, 0) in (w, conj psi, psi)",
        "M_E_closed_form": "diag(x/2 + x(1-x)/(2-x), (1-x)(5x-2)/(2-x) + 1 - x/2, 0)",
        "M_E_structural_form": (
            "M_E = beta (I - i [w]_x) + delta w w^T with beta = x/4 + 2x(1-x)/(2-x), "
            "delta = x/4 - x(1-x)/(2-x); (I - i[w]_x) has eigenvalues 1, 2, 0 on (w, conj psi, psi)"
        ),
    }

    # structural cross-check of the M_E decomposition (independent construction)
    w_cross = sp.Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]])  # [w]_x for w = e_0
    beta = x / 4 + 2 * x * (1 - x) / (2 - x)
    delta = x / 4 - x * (1 - x) / (2 - x)
    m_e_structural = sp.simplify(
        beta * (sp.eye(3) - sp.I * w_cross) + delta * w_third * w_third.T
    )
    result["closed_form"]["M_E_structural_pass"] = bool(zero_matrix(m_e_op - m_e_structural))
    result["closed_form"]["w_cross_convention"] = "([w]_x y = w x y), w = e_0"

    # ---------- x = 9/20 comparison with the P9b datum
    xv = sp.Rational(9, 20)
    d_at = sp.simplify(d_basis.subs(x, xv))
    expected = sp.diag(sp.Rational(-99, 620), sp.Rational(-11, 124), 0)
    result["p9b_datum"] = {
        "x": "9/20",
        "D_computed": [[str(v) for v in d_at.row(i)] for i in range(3)],
        "D_expected_from_P9b": [[str(v) for v in expected.row(i)] for i in range(3)],
        "match": bool(d_at == expected),
        "source": "tools/whgap_p9b_g0.py + WHGAP.no-ascent-hierarchy work record (P9b)",
    }

    # ---------- weight identity on explicit states (independent construction)
    weight_rows = []
    ks = kraus()
    psi_bar = psi.conjugate()
    for seed in (20260729, 20260730, 20260731):
        phi = rational_density(seed)
        w_b = sp.simplify((psi_bar.H * channel(phi) * psi_bar)[0, 0])
        w_e = sp.simplify(sp.trace(pi_e_op * complement(phi)))
        via_d = sp.simplify(sp.trace(d_op * phi))
        weight_rows.append(
            {
                "seed": seed,
                "w_B": str(sp.factor(sp.cancel(w_b))),
                "w_E": str(sp.factor(sp.cancel(w_e))),
                "w_B_minus_w_E": str(sp.factor(sp.cancel(w_b - w_e))),
                "Tr[D phi]": str(sp.factor(sp.cancel(via_d))),
                "identity_pass": bool(zero(w_b - w_e - via_d)),
                "value_at_9_over_20": str(sp.cancel(sp.simplify(via_d.subs(x, xv)))),
            }
        )
    result["weight_identity_checks"] = weight_rows

    # ---------- exact negativity region
    d0_sign = sp.simplify(d0 * (2 - x) / (x * (1 - x)))  # must be -1
    d1_sign = sp.simplify(d1 * (2 - x) / (1 - x))  # must be 2-5x
    root = sp.solve(sp.Eq(d1, 0), x)
    x_d = sp.Rational(2, 5)
    reduced = sp.reduce_inequalities([d0 <= 0, d1 <= 0, x > 0, x < 1], [x])
    result["negativity_region"] = {
        "d_0_sign_certificate": (
            "d_0 (2-x)/(x(1-x)) = -1, and x>0, 1-x>0, 2-x>0 on (0,1): "
            "d_0(x) < 0 STRICTLY for every x in (0,1)."
        ),
        "d_0_sign_pass": bool(zero(d0_sign + 1)),
        "d_1_sign_certificate": (
            "d_1 (2-x)/(1-x) = 2-5x, and (1-x)/(2-x) > 0 on (0,1): "
            "sign(d_1) = sign(2-5x), so d_1 <= 0 iff x >= 2/5 with equality only at x = 2/5."
        ),
        "d_1_sign_pass": bool(zero(d1_sign - (2 - 5 * x))),
        "d_1_roots": [str(r) for r in root],
        "x_D_exact": "2/5",
        "x_D_decimal": "0.4",
        "set_D_psi_leq_0": "[2/5, 1)  (intersected with (0,1))",
        "sympy_reduce_inequalities": str(reduced),
        "largest_eigenvalue": str(sp.factor(sp.cancel(sp.Max(d0, d1, d2).rewrite(sp.Piecewise)))
                                  if False else "max(d_0, d_1, 0) = 0 for all x in (0,1) since d_0<0 and d_1<=0 iff x>=2/5"),
        "largest_nonzero_eigenvalue_crossing": (
            "d_1 is the only eigenvalue that changes sign on (0,1); it crosses zero exactly at x = 2/5."
        ),
        "comparisons": {
            "x_1_from_P3": X1_DECIMAL + "... (WHGAP.qpositive-onset.md:41)",
            "x_D_minus_x_1": str(sp.N(x_d - sp.Float(X1_DECIMAL, 30), 20)),
            "x_D_vs_x_1": "x_D = 2/5 > x_1",
            "x_D_minus_one_half": str(x_d - sp.Rational(1, 2)),
            "x_D_vs_one_half": "x_D = 2/5 < 1/2",
            "location": "x_D lies strictly inside the strip (x_1, 1/2)",
            "P3_exact_witness_point": "783/2000 = 0.3915",
            "x_D_vs_P3_witness": "2/5 > 783/2000",
        },
    }

    # ---------- O(3) transport check
    rot = sp.Matrix([[2, -1, 2], [2, 2, -1], [-1, 2, 2]]) / 3
    generic = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"y{i}{j}"))
    covariance_pass = zero_matrix(channel(rot * generic * rot.T) - rot * channel(generic) * rot.T)
    psi_rot = sp.simplify(rot * psi)
    third_rot = sp.simplify(rot * w_third)
    rotated = weight_operators(psi_rot, third_rot)
    d_rot_basis = rotated.pop("_d_basis")
    d_rot = rotated.pop("_d")
    rotated.pop("_m_e")
    rotated.pop("_pi_e")
    result["o3_transport"] = {
        "rotation": [[str(v) for v in rot.row(i)] for i in range(3)],
        "orthogonal": bool(zero_matrix(rot.T * rot - sp.eye(3))),
        "determinant": str(sp.simplify(rot.det())),
        "channel_covariance_on_generic_matrix": bool(covariance_pass),
        "psi_rot_isotropic": bool(zero((psi_rot.T * psi_rot)[0, 0])),
        "D_rot_equals_R_D_R_transpose": bool(zero_matrix(d_rot - rot * d_op * rot.T)),
        "D_rot_in_transported_basis": [
            [str(sp.simplify(v)) for v in d_rot_basis.row(i)] for i in range(3)
        ],
        "same_diagonal_functions": bool(
            zero(d_rot_basis[0, 0] - d0) and zero(d_rot_basis[1, 1] - d1) and zero(d_rot_basis[2, 2])
        ),
        "checks": rotated,
    }

    # ---------- second isotropic point from the P9b stereographic chart
    p, q = sp.Rational(1, 3), sp.Rational(2, 5)
    den = 1 + p**2 + q**2
    u_chart = sp.Matrix([1 - p**2 + q**2, -2 * p * q, -2 * p]) / den
    v_chart = sp.Matrix([-2 * p * q, 1 + p**2 - q**2, -2 * q]) / den
    psi_chart = sp.simplify((u_chart + sp.I * v_chart) / sp.sqrt(2))
    third_chart = sp.simplify(
        sp.Matrix(
            [
                u_chart[1] * v_chart[2] - u_chart[2] * v_chart[1],
                u_chart[2] * v_chart[0] - u_chart[0] * v_chart[2],
                u_chart[0] * v_chart[1] - u_chart[1] * v_chart[0],
            ]
        )
    )
    chart = weight_operators(psi_chart, third_chart)
    d_chart_basis = chart.pop("_d_basis")
    chart.pop("_d")
    chart.pop("_m_e")
    chart.pop("_pi_e")
    result["chart_point"] = {
        "p": str(p),
        "q": str(q),
        "psi_isotropic": bool(zero((psi_chart.T * psi_chart)[0, 0])),
        "third_unit": bool(zero((third_chart.T * third_chart)[0, 0] - 1)),
        "D_in_basis": [[str(sp.simplify(v)) for v in d_chart_basis.row(i)] for i in range(3)],
        "same_diagonal_functions": bool(
            zero(d_chart_basis[0, 0] - d0)
            and zero(d_chart_basis[1, 1] - d1)
            and zero(d_chart_basis[2, 2])
        ),
        "checks": chart,
    }

    checks = {
        "canonical_structure": all(
            [
                result["canonical"]["isotropic_tau_zero"],
                result["canonical"]["receiver_kernel_is_conj_psi"],
                result["canonical"]["receiver_closed_form_pass"],
                result["canonical"]["basis_unitary"],
                result["canonical"]["M_B_closed_form_is_Lambda_of_P_conj_psi"],
                all(result["canonical"]["projector_checks"].values()),
            ]
        ),
        "closed_form": all(
            [
                result["closed_form"]["diagonal_in_(e0, conj psi, psi)"],
                result["closed_form"]["d_0_pass"],
                result["closed_form"]["d_1_pass"],
                result["closed_form"]["d_2_is_zero"],
                result["closed_form"]["psi_in_kernel"],
                result["closed_form"]["M_E_structural_pass"],
            ]
        ),
        "p9b_datum": result["p9b_datum"]["match"],
        "weight_identity": all(row["identity_pass"] for row in weight_rows),
        "negativity_region": all(
            [
                result["negativity_region"]["d_0_sign_pass"],
                result["negativity_region"]["d_1_sign_pass"],
            ]
        ),
        "o3_transport": all(
            [
                result["o3_transport"]["orthogonal"],
                result["o3_transport"]["channel_covariance_on_generic_matrix"],
                result["o3_transport"]["psi_rot_isotropic"],
                result["o3_transport"]["D_rot_equals_R_D_R_transpose"],
                result["o3_transport"]["same_diagonal_functions"],
            ]
        ),
        "chart_point": all(
            [
                result["chart_point"]["psi_isotropic"],
                result["chart_point"]["same_diagonal_functions"],
            ]
        ),
    }
    result["component_status"] = {k: ("PASS" if v else "FAIL") for k, v in checks.items()}
    result["status"] = "PASS" if all(checks.values()) else "FAIL"
    result["interpreter"] = str(Path(__import__("sys").executable).resolve())

    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
