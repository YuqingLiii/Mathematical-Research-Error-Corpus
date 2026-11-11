"""P6b-V2 replacement (decision-layer executor, 2026-07-29): exact isotropic weight
operator D_psi(x) — supersedes whgap_p6b_v2_isotropic.py, whose D/basis assembly was
shown wrong by independent numeric arbitration (its d1 = 1-x would violate proved Q=0
on [1/2,1); the P9b values are confirmed instead).

Construction (all exact sympy, real Kraus adjoint = .T):
  psi = (e1 + i e2)/sqrt2 (isotropic, tau = psi^T psi = 0), psi_bar, third = e3.
  M_B = Lambda^dagger(P_psibar)  (so Tr[M_B phi] = <psibar|Lambda(phi)|psibar> = w_B)
  Pi_E = orthogonal projector onto ker Lambda^c(P_psi)  (exact nullspace + Gram-Schmidt)
  M_E = sum_ab K_a^T (Pi_E)_ab K_b  (so Tr[M_E phi] = Tr[Pi_E Lambda^c(phi)] = w_E)
  D = M_B - M_E; claims: D diagonal in (third, psibar, psi) with
    d_0 = -x(1-x)/(2-x),  d_1 = (1-x)(2-5x)/(2-x),  d_2 = 0,
  hence max_phi (w_B - w_E) = max(d_0, d_1, 0) and the first-order isotropic ascent
  exists iff d_1 > 0 iff x < 2/5: candidate exact single-letter onset x_D = 2/5.
"""
import json
import sys
import time
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "artifacts" / "logs_whgap_p6b_20260729"
T0 = time.perf_counter()
x = sp.symbols("x", positive=True)


def levi(mu):
    return sp.Matrix(3, 3, lambda j, k: sp.LeviCivita(mu, j, k))


A = [levi(m) for m in range(3)]
K = [sp.sqrt(1 - x) * sp.eye(3)] + [sp.sqrt(x / 2) * A[m] for m in range(3)]


def lam(Y):
    return sp.expand((1 - x) * Y + (x / 2) * (sp.trace(Y) * sp.eye(3) - Y.T))


def lam_dag(Z):
    # HS adjoint of Lambda (self-adjoint family): Lambda^dagger = Lambda here
    # (Lambda is written with real coefficients and transpose; verify below).
    return lam(Z)


def lamc(Y):
    return sp.Matrix(4, 4, lambda a, b: sp.expand(sp.trace(K[a] * Y * K[b].T)))


def realify(e):
    """Strip conjugate(u) whenever u is I-free (hence a real function of x on (0,1)).

    Sound because x is a positive real parameter; such conjugates are artifacts of
    symbolic .H / Gram-Schmidt normalization (same trap family as the audit and the
    superseded V2 script; decision-layer fix 2026-07-29)."""
    if isinstance(e, sp.MatrixBase):
        return e.applyfunc(realify)
    return e.replace(
        lambda t: isinstance(t, sp.conjugate) and not t.args[0].has(sp.I),
        lambda t: t.args[0],
    )


def clean(e):
    return sp.simplify(sp.nsimplify(sp.expand(realify(e))))


psi = sp.Matrix([1, sp.I, 0]) / sp.sqrt(2)
psib = psi.conjugate()
third = sp.Matrix([0, 0, 1])
P = psi * psi.H
Pb = psib * psib.H

result = {"script": "tools/whgap_p6b_v2_fable.py"}

# --- sanity: Lambda self-adjointness on a symbolic matrix-unit basis
E = [[sp.Matrix(3, 3, lambda r, c: sp.Integer(r == i and c == j)) for j in range(3)] for i in range(3)]
sa = all(
    sp.simplify(sp.trace(E[a][b].H * lam(E[c][d])) - sp.trace(lam(E[a][b]).H * E[c][d])) == 0
    for a in range(3) for b in range(3) for c in range(3) for d in range(3)
)
result["lambda_self_adjoint"] = bool(sa)

# --- isotropic spectra
lamP = sp.simplify(lam(P))
lamcP = sp.Matrix(4, 4, lambda a, b: clean(lamc(P)[a, b]))
specB = [sp.simplify(v) for v in lamP.eigenvals(multiple=True)]
result["spec_Lambda_P"] = sorted(str(s) for s in specB)

# --- exact E-kernel and orthogonal projector
ker = lamcP.nullspace()
result["kernel_dim"] = len(ker)
# Gram-Schmidt (exact)
ons = []
for v in ker:
    w = v
    for u in ons:
        w = w - u * (u.H * w)[0, 0]
    w = sp.Matrix([clean(v) for v in w])
    n2 = clean((w.H * w)[0, 0])
    ons.append(w / sp.sqrt(n2))
PiE = sp.Matrix(4, 4, lambda i, j: clean((ons[0] * ons[0].H + ons[1] * ons[1].H)[i, j]))
result["PiE_checks"] = {
    "trace_two": bool(sp.simplify(sp.trace(PiE) - 2) == 0),
    "idempotent": bool(sp.simplify(PiE * PiE - PiE) == sp.zeros(4, 4)),
    "annihilates_output": bool(sp.simplify(PiE * lamcP) == sp.zeros(4, 4)),
}

# --- weight operators
M_B = sp.simplify(lam_dag(Pb))
M_E = sp.zeros(3, 3)
for a in range(4):
    for b in range(4):
        M_E += K[a].T * PiE[a, b] * K[b]
M_E = sp.Matrix(3, 3, lambda i, j: clean(M_E[i, j]))
D = sp.Matrix(3, 3, lambda i, j: clean(M_B[i, j] - M_E[i, j]))

basis = sp.Matrix.hstack(third, psib, psi)
Db = sp.Matrix(3, 3, lambda i, j: clean((basis.H * D * basis)[i, j]))
offdiag_zero = all(sp.simplify(Db[i, j]) == 0 for i in range(3) for j in range(3) if i != j)
d0, d1, d2 = (sp.simplify(Db[k, k]) for k in range(3))
claims = {
    "d0": -x * (1 - x) / (2 - x),
    "d1": (1 - x) * (2 - 5 * x) / (2 - x),
    "d2": sp.Integer(0),
}
result["D_diagonal_in_basis"] = bool(offdiag_zero)
result["d0"] = str(sp.factor(d0)); result["d0_claim_pass"] = bool(sp.simplify(d0 - claims["d0"]) == 0)
result["d1"] = str(sp.factor(d1)); result["d1_claim_pass"] = bool(sp.simplify(d1 - claims["d1"]) == 0)
result["d2"] = str(sp.factor(d2)); result["d2_claim_pass"] = bool(sp.simplify(d2 - claims["d2"]) == 0)

# --- P9b datum crosscheck at x = 9/20
xv = sp.Rational(9, 20)
result["p9b_datum_match"] = {
    "x": "9/20",
    "diag": [str(sp.simplify(d.subs(x, xv))) for d in (d0, d1, d2)],
    "expected": ["-99/620", "-11/124", "0"],
    "pass": bool(
        sp.simplify(d0.subs(x, xv) + sp.Rational(99, 620)) == 0
        and sp.simplify(d1.subs(x, xv) + sp.Rational(11, 124)) == 0
        and sp.simplify(d2.subs(x, xv)) == 0
    ),
}

# --- negativity region / onset candidate
result["region"] = {
    "d0_identity": str(sp.factor(sp.simplify(d0 * (2 - x) / (x * (1 - x))))) + " (claim: -1)",
    "d0_neg_all_x": bool(sp.simplify(d0 * (2 - x) / (x * (1 - x)) + 1) == 0),
    "d1_identity": str(sp.factor(sp.simplify(d1 * (2 - x) / (1 - x)))) + " (claim: 2-5x)",
    "d1_sign_rule": bool(sp.simplify(d1 * (2 - x) / (1 - x) - (2 - 5 * x)) == 0),
    "d1_root": "2/5",
    "onset_candidate": "max_phi (w_B - w_E) = max(d1, 0): first-order isotropic ascent iff x < 2/5",
}

gates = {
    "self_adjoint": result["lambda_self_adjoint"],
    "kernel": result["kernel_dim"] == 2 and all(result["PiE_checks"].values()),
    "diagonal": result["D_diagonal_in_basis"],
    "closed_forms": result["d0_claim_pass"] and result["d1_claim_pass"] and result["d2_claim_pass"],
    "p9b_datum": result["p9b_datum_match"]["pass"],
    "region": result["region"]["d0_neg_all_x"] and result["region"]["d1_sign_rule"],
}
result["gates"] = {k: ("PASS" if v else "FAIL") for k, v in gates.items()}
result["status"] = "PASS" if all(gates.values()) else "FAIL"
result["runtime_seconds"] = round(time.perf_counter() - T0, 3)
result["interpreter"] = sys.executable

LOG_DIR.mkdir(parents=True, exist_ok=True)
(LOG_DIR / "v2_fable_results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
sys.exit(0 if all(gates.values()) else 2)
