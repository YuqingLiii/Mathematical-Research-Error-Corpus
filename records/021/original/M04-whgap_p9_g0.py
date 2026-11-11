#!/usr/bin/env python3
"""P9 E1 gate G0: exact pure spectra and high-precision epsilon expansion."""

from __future__ import annotations

import json
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "artifacts" / "logs_whgap_p9_20260729"
OUT = LOG_DIR / "g0_derivation_check.json"
X = sp.Rational(9, 20)


def sympy_kraus(x: sp.Expr) -> list[sp.Matrix]:
    antisymmetric = [
        sp.Matrix(3, 3, lambda j, k, mu=mu: sp.LeviCivita(mu, j, k))
        for mu in range(3)
    ]
    return [sp.sqrt(1 - x) * sp.eye(3)] + [
        sp.sqrt(x / 2) * matrix for matrix in antisymmetric
    ]


def sympy_outputs(psi: sp.Matrix, x: sp.Expr) -> tuple[sp.Matrix, sp.Matrix]:
    rho = psi * psi.H
    ks = sympy_kraus(x)
    receiver = sum((k * rho * k.H for k in ks), sp.zeros(3))
    environment = sp.Matrix(
        4,
        4,
        lambda a, b: sp.simplify(sp.trace(ks[a] * rho * ks[b].H)),
    )
    return sp.simplify(receiver), sp.simplify(environment)


def multiset(matrix: sp.Matrix) -> dict[str, int]:
    return {str(sp.simplify(value)): multiplicity for value, multiplicity in matrix.eigenvals().items()}


def np_kraus(x: float) -> np.ndarray:
    mats = [np.sqrt(1.0 - x) * np.eye(3, dtype=complex)]
    for mu in range(3):
        a = np.zeros((3, 3), dtype=complex)
        for j in range(3):
            for k in range(3):
                a[j, k] = float(sp.LeviCivita(mu, j, k))
        mats.append(np.sqrt(x / 2.0) * a)
    return np.stack(mats)


def outputs_np(rho: np.ndarray, ks: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    receiver = np.einsum("aij,jk,alk->il", ks, rho, ks.conj(), optimize=True)
    environment = np.einsum("aij,jk,bik->ab", ks, rho, ks.conj(), optimize=True)
    return receiver, environment


def mp_matrix(matrix: np.ndarray) -> mp.matrix:
    return mp.matrix(
        [[mp.mpc(complex(matrix[i, j])) for j in range(matrix.shape[1])] for i in range(matrix.shape[0])]
    )


def entropy_mp(matrix: np.ndarray) -> mp.mpf:
    eigenvalues, _ = mp.eighe(mp_matrix((matrix + matrix.conj().T) / 2.0))
    total = mp.mpf("0")
    for value in eigenvalues:
        real_value = mp.re(value)
        if real_value > mp.mpf("1e-60"):
            total -= real_value * mp.log(real_value)
    return total


def log_on_support(matrix: np.ndarray, tolerance: float = 1e-11) -> np.ndarray:
    values, vectors = np.linalg.eigh((matrix + matrix.conj().T) / 2.0)
    positive = values > tolerance
    return (vectors[:, positive] * np.log(values[positive])) @ vectors[:, positive].conj().T


def allowed_input_basis(psi: np.ndarray, ks: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    pure = np.outer(psi, psi.conj())
    _, environment = outputs_np(pure, ks)
    values, vectors = np.linalg.eigh((environment + environment.conj().T) / 2.0)
    kernel_vector = vectors[:, np.argmin(values)]
    annihilator = sum(kernel_vector[a].conjugate() * ks[a] for a in range(len(ks)))
    _, singular_values, vh = np.linalg.svd(annihilator)
    basis = vh.conj().T[:, singular_values < 1e-10]
    return basis, kernel_vector


def random_density_on_basis(rng: np.random.Generator, basis: np.ndarray) -> np.ndarray:
    z = rng.normal(size=(basis.shape[1], basis.shape[1])) + 1j * rng.normal(
        size=(basis.shape[1], basis.shape[1])
    )
    small = z @ z.conj().T
    small /= np.trace(small).real
    return basis @ small @ basis.conj().T


def coherent_information_nats(rho: np.ndarray, ks: np.ndarray) -> mp.mpf:
    receiver, environment = outputs_np(rho, ks)
    return entropy_mp(receiver) - entropy_mp(environment)


def epsilon_record(seed: int) -> dict:
    rng = np.random.default_rng(seed)
    ks = np_kraus(float(X))
    psi = rng.normal(size=3) + 1j * rng.normal(size=3)
    psi /= np.linalg.norm(psi)
    basis, kernel_vector = allowed_input_basis(psi, ks)
    pure = np.outer(psi, psi.conj())
    nontrivial_pair_exists = basis.shape[1] >= 2
    phi = (
        random_density_on_basis(rng, basis)
        if nontrivial_pair_exists
        else pure
    )
    receiver_psi, environment_psi = outputs_np(pure, ks)
    receiver_phi, environment_phi = outputs_np(phi, ks)
    log_receiver = log_on_support(receiver_psi)
    log_environment = log_on_support(environment_psi)
    c1 = float(
        -np.trace((receiver_phi - receiver_psi) @ log_receiver).real
        + np.trace((environment_phi - environment_psi) @ log_environment).real
    )

    if nontrivial_pair_exists:
        epsilons = [mp.mpf(10) ** (-k) for k in range(4, 10)]
        design = mp.matrix(
            [[eps, eps**2 * mp.log(eps), eps**2] for eps in epsilons]
        )
        observations = mp.matrix(
            [
                coherent_information_nats(
                    (1.0 - float(eps)) * pure + float(eps) * phi,
                    ks,
                )
                for eps in epsilons
            ]
        )
        fitted, _ = mp.qr_solve(design, observations)
        fitted_c1 = fitted[0]
        absolute_error = abs(fitted_c1 - c1)
    else:
        fitted_c1 = mp.nan
        absolute_error = mp.inf

    hitting_vector = rng.normal(size=3) + 1j * rng.normal(size=3)
    hitting_vector /= np.linalg.norm(hitting_vector)
    hitting_phi = np.outer(hitting_vector, hitting_vector.conj())
    kernel_weight = float(
        np.vdot(
            kernel_vector,
            outputs_np(hitting_phi, ks)[1] @ kernel_vector,
        ).real
    )
    hitting_ratios = []
    for eps in [mp.mpf("1e-5"), mp.mpf("1e-7"), mp.mpf("1e-9")]:
        value = coherent_information_nats(
            (1.0 - float(eps)) * pure + float(eps) * hitting_phi,
            ks,
        )
        hitting_ratios.append(
            {
                "epsilon": mp.nstr(eps, 5),
                "Ic_nats": mp.nstr(value, 30),
                "Ic_over_eps_log_1_over_eps": mp.nstr(
                    value / (eps * mp.log(1 / eps)), 30
                ),
            }
        )

    return {
        "seed": seed,
        "psi_real": psi.real.tolist(),
        "psi_imag": psi.imag.tolist(),
        "allowed_support_dimension": int(basis.shape[1]),
        "nontrivial_kernel_avoiding_pair_exists": nontrivial_pair_exists,
        "support_diagnostic": (
            "The sole allowed input ray is psi; the commissioned random distinct "
            "(psi,phi) kernel-avoiding fit cannot be formed."
            if not nontrivial_pair_exists
            else "A nontrivial allowed input support was found."
        ),
        "annihilation_residual": float(
            np.linalg.norm(
                sum(kernel_vector[a].conjugate() * ks[a] for a in range(len(ks)))
                @ basis
            )
        ),
        "claimed_c1_nats": f"{c1:.17g}",
        "fitted_c1_nats": (
            mp.nstr(fitted_c1, 30) if nontrivial_pair_exists else "not-applicable"
        ),
        "absolute_error": (
            mp.nstr(absolute_error, 20) if nontrivial_pair_exists else "not-applicable"
        ),
        "eight_digit_match": bool(
            nontrivial_pair_exists and absolute_error < mp.mpf("5e-9")
        ),
        "kernel_hitting_weight": kernel_weight,
        "kernel_hitting": hitting_ratios,
        "kernel_plunge_confirmed": bool(
            kernel_weight > 1e-8
            and all(mp.mpf(item["Ic_over_eps_log_1_over_eps"]) < 0 for item in hitting_ratios)
        ),
    }


def main() -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = 80

    real_psi = sp.Matrix([1, 0, 0])
    complex_psi = sp.Matrix([1, sp.I, 1]) / sp.sqrt(3)
    real_receiver, real_environment = sympy_outputs(real_psi, X)
    complex_receiver, complex_environment = sympy_outputs(complex_psi, X)

    claimed_receiver = {str(sp.Rational(11, 20)): 1, str(sp.Rational(9, 40)): 2}
    claimed_environment = {
        str(sp.Rational(11, 20)): 1,
        str(sp.Rational(9, 40)): 2,
        "0": 1,
    }
    real_receiver_spectrum = multiset(real_receiver)
    real_environment_spectrum = multiset(real_environment)
    complex_receiver_spectrum = multiset(complex_receiver)
    complex_environment_spectrum = multiset(complex_environment)

    r_squared = sp.Rational(1, 9)
    a = 1 - X
    b = X / 2
    discriminant = sp.simplify((1 - b) ** 2 - 4 * a * b * r_squared)
    generic_formula = [
        b,
        sp.simplify((1 - b - sp.sqrt(discriminant)) / 2),
        sp.simplify((1 - b + sp.sqrt(discriminant)) / 2),
    ]
    formula_check = sorted(
        [sp.N(value, 40) for value in generic_formula], key=lambda value: float(value)
    ) == sorted(
        [sp.N(value, 40) for value in complex_receiver.eigenvals().keys()],
        key=lambda value: float(value),
    )

    epsilon_records = [epsilon_record(20260729 + offset) for offset in range(4)]
    spectra_claim_pass = (
        real_receiver_spectrum == claimed_receiver
        and real_environment_spectrum == claimed_environment
        and complex_receiver_spectrum == claimed_receiver
        and complex_environment_spectrum == claimed_environment
    )
    epsilon_fit_pass = all(item["eight_digit_match"] for item in epsilon_records)
    kernel_plunge_pass = all(item["kernel_plunge_confirmed"] for item in epsilon_records)
    gate_pass = spectra_claim_pass and epsilon_fit_pass and kernel_plunge_pass

    result = {
        "task": "WHGAP P9 E1 D1 / gate G0",
        "x": "9/20",
        "status": "PASS" if gate_pass else "FAIL",
        "spectra_claim": {
            "status": "PASS" if spectra_claim_pass else "FAIL",
            "claimed_receiver": claimed_receiver,
            "claimed_environment": claimed_environment,
            "real_psi": {
                "psi": ["1", "0", "0"],
                "receiver_spectrum": real_receiver_spectrum,
                "environment_spectrum": real_environment_spectrum,
                "claim_holds": (
                    real_receiver_spectrum == claimed_receiver
                    and real_environment_spectrum == claimed_environment
                ),
            },
            "generic_complex_psi": {
                "psi": ["1/sqrt(3)", "i/sqrt(3)", "1/sqrt(3)"],
                "abs_psi_transpose_psi_squared": "1/9",
                "receiver_spectrum": complex_receiver_spectrum,
                "environment_spectrum": complex_environment_spectrum,
                "claim_holds": (
                    complex_receiver_spectrum == claimed_receiver
                    and complex_environment_spectrum == claimed_environment
                ),
            },
            "correct_receiver_formula": (
                "Let r^2=|psi^T psi|^2, a=1-x, b=x/2. "
                "The receiver eigenvalues are b and "
                "(1-b +/- sqrt((1-b)^2-4*a*b*r^2))/2; "
                "the environment has the same nonzero spectrum plus zero."
            ),
            "formula_check_at_complex_example": bool(formula_check),
            "commission_claim_scope": (
                "The displayed fixed spectrum is exact only when |psi^T psi|=1 "
                "(the real-up-to-phase orbit), not for a generic complex pure input."
            ),
        },
        "epsilon_expansion": {
            "status": "PASS" if epsilon_fit_pass else "FAIL",
            "precision_decimal_digits": 80,
            "fit_model": "c1*epsilon + c2*epsilon^2*log(epsilon) + c3*epsilon^2",
            "records": epsilon_records,
            "failure_reason": (
                "For every sampled generic pure psi, the support condition leaves a "
                "one-dimensional input support, hence phi=psi is the only state and "
                "there are no random distinct kernel-avoiding pairs to fit."
                if not epsilon_fit_pass
                else None
            ),
        },
        "kernel_hitting_plunge": {
            "status": "PASS" if kernel_plunge_pass else "FAIL",
            "criterion": "Ic/(epsilon*log(1/epsilon)) < 0 at 1e-5, 1e-7, 1e-9",
        },
        "gate_decision": (
            "STOP E1 before S1/S2 because the exact generic-complex pure-spectrum "
            "claim required by G0 is false."
            if not gate_pass
            else "Proceed to E1 S1/S2."
        ),
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not gate_pass:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
