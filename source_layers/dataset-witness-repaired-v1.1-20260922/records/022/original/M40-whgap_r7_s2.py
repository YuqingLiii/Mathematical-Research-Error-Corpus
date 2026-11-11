"""R7 reviewer script (independent): claim 1 of the P13-B package -- the S2 identity

  F(M) := <conj Psi| (Lambda_x @ Lambda_x)(P_Psi) |conj Psi>
        = (1-x)^2 |Tr(M M^T)|^2 + x^2 ||adj M||_F^2 ,      ||M||_F = 1,

together with the constituent identity  Tr(M^T A_i M A_j) = -2 adj(M)_{ji}.

Independent path (rule 7c): the whole verification is built from the FROZEN definitions
only (channel formula + Kraus set of R5 commission section 1).  Three routes:

  R1  polynomial identity in 18 independent symbols (m_jk and n_jk standing for conj(m_jk))
      and symbolic x -- a FORMULA verification, not a value check;
  R2  the constituent adjugate identity, symbolic in the 9 entries of M;
  R3  a value check that closes the loop against the CHANNEL FORMULA rather than the Kraus
      set: (Lambda@Lambda) built by direct index action of Y -> (1-x)Y + (x/2)(Tr Y - Y^T)
      on each tensor factor, at c >= 3 random complex M and 3 rational x.

No file from tools/whgap_p13b_*.py was read before this script was written.
Interpreter: C:[USER_HOME]/cpython3119/python.exe
"""
import itertools
import json

import numpy as np
import sympy as sp

x = sp.Symbol("x", positive=True)

# ---------------------------------------------------------------- frozen objects
def eps3(i, j, k):
    return sp.Rational(int((i - j) * (j - k) * (k - i)) // 2) if len({i, j, k}) == 3 else 0


A = [sp.Matrix(3, 3, lambda j, k: eps3(i, j, k)) for i in range(3)]  # (A_i)_{jk} = eps_{ijk}
assert A[0] == sp.Matrix([[0, 0, 0], [0, 0, 1], [0, -1, 0]]), A[0]
Ahat = [sp.eye(3)] + A                      # integer parts of the Kraus operators
csq = [1 - x] + [x / sp.Integer(2)] * 3     # c_a^2

out = {"script": "tools/whgap_r7_s2.py"}

# ------------------------------------------------------- R2: the adjugate identity
Mg = sp.Matrix(3, 3, lambda j, k: sp.Symbol(f"m{j}{k}"))
adjM = Mg.adjugate()                        # sympy adjugate: M*adj(M) = det(M) I
assert sp.simplify(Mg * adjM - Mg.det() * sp.eye(3)) == sp.zeros(3, 3)
r2 = []
for i in range(3):
    for j in range(3):
        lhs = sp.expand((Mg.T * A[i] * Mg * A[j]).trace())
        rhs = sp.expand(-2 * adjM[j, i])
        r2.append(sp.simplify(lhs - rhs) == 0)
out["R2_adjugate_identity_all_9_ij"] = bool(all(r2))
# and the two vanishing traces used in the derivation
out["R2_tr_MT_Ai_M_is_zero"] = bool(all(sp.expand((Mg.T * A[i] * Mg).trace()) == 0 for i in range(3)))
out["R2_tr_MT_M_Ai_is_zero"] = bool(all(sp.expand((Mg.T * Mg * A[i]).trace()) == 0 for i in range(3)))

# ------------------------------- R1: F(M) as a polynomial identity in m, n(=conj m), x
Ng = sp.Matrix(3, 3, lambda j, k: sp.Symbol(f"n{j}{k}"))
adjN = Ng.adjugate()


def T(Mx, a, b):
    """holomorphic part of <conj Psi|(K_a @ K_b)|Psi> = Tr(M^T K_a M K_b^T), radicals stripped:
    returns (coefficient c_a^2 c_b^2 free) Tr(M^T Ahat_a M Ahat_b^T)."""
    return sp.expand((Mx.T * Ahat[a] * Mx * Ahat[b].T).trace())


F_lhs = 0
for a, b in itertools.product(range(4), repeat=2):
    F_lhs += sp.sqrt(csq[a] * csq[b]) ** 2 * T(Mg, a, b) * T(Ng, a, b)
F_lhs = sp.expand(F_lhs)

F_rhs = sp.expand(
    (1 - x) ** 2 * (Mg * Mg.T).trace() * (Ng * Ng.T).trace()
    + x ** 2 * sum(adjM[j, i] * adjN[j, i] for i in range(3) for j in range(3))
)
out["R1_symbolic_formula_identity"] = bool(sp.expand(F_lhs - F_rhs) == 0)
out["R1_n_symbols"] = 18
out["R1_x_symbolic"] = True

# also: the individual (a,b) block structure claimed in the note
blocks = {}
for a, b in itertools.product(range(4), repeat=2):
    blocks[f"{a}{b}"] = sp.expand(T(Mg, a, b))
out["R1_mixed_blocks_vanish"] = bool(
    all(blocks[f"{a}0"] == 0 and blocks[f"0{a}"] == 0 for a in (1, 2, 3))
)
out["R1_block00_is_Tr_MMT"] = bool(sp.expand(blocks["00"] - (Mg * Mg.T).trace()) == 0)

# ---------------------------------- R3: value check against the CHANNEL FORMULA (no Kraus)
def lam_factor1(Z, xv):
    """apply Lambda_x to tensor factor 1 of a 9x9 matrix Z (index layout (j,k),(j',k'))."""
    Zt = Z.reshape(3, 3, 3, 3)                    # [j,k,j',k']
    tr1 = np.einsum("pkpl->kl", Zt)               # partial trace over factor 1
    res = (1 - xv) * Zt \
        + (xv / 2) * (np.einsum("jl,kn->jkln", np.eye(3), tr1).transpose(0, 1, 2, 3)
                      - Zt.transpose(2, 1, 0, 3))
    return res.reshape(9, 9)


def lam_factor2(Z, xv):
    Zt = Z.reshape(3, 3, 3, 3)
    tr2 = np.einsum("jpkp->jk", Zt)
    res = (1 - xv) * Zt \
        + (xv / 2) * (np.einsum("kn,jl->jkln", np.eye(3), tr2)
                      - Zt.transpose(0, 3, 2, 1))
    return res.reshape(9, 9)


def lam2_formula(Z, xv):
    return lam_factor2(lam_factor1(Z, xv), xv)


def lam2_kraus(Z, xv):
    Ks = [np.sqrt(1 - xv) * np.eye(3)] + [np.sqrt(xv / 2) * np.array(A[i], dtype=float) for i in range(3)]
    acc = np.zeros((9, 9), dtype=complex)
    for Ka in Ks:
        for Kb in Ks:
            W = np.kron(Ka, Kb)
            acc += W @ Z @ W.conj().T
    return acc


rng = np.random.default_rng(20260730)


def _adj(Mv):
    """adjugate of a 3x3 numpy matrix, cofactor route (no inverse -> works at det=0)."""
    C = np.zeros((3, 3), dtype=complex)
    for i in range(3):
        for j in range(3):
            minor = np.delete(np.delete(Mv, i, axis=0), j, axis=1)
            C[i, j] = (-1) ** (i + j) * (minor[0, 0] * minor[1, 1] - minor[0, 1] * minor[1, 0])
    return C.T


r3 = []
for xv in (0.35, 0.4, 0.45, 0.49):
    for t in range(3):
        Mv = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        if t == 2:                                  # include a rank-2 (det = 0) sample
            Mv[:, 2] = Mv[:, 0] + 2 * Mv[:, 1]
        Mv /= np.linalg.norm(Mv)
        Psi = Mv.reshape(9)
        P = np.outer(Psi, Psi.conj())
        oB_f = lam2_formula(P, xv)
        oB_k = lam2_kraus(P, xv)
        cPsi = Psi.conj()
        F_num = float((cPsi.conj() @ oB_f @ cPsi).real)
        F_pred = float((1 - xv) ** 2 * abs(np.trace(Mv @ Mv.T)) ** 2
                       + xv ** 2 * np.linalg.norm(_adj(Mv)) ** 2)
        r3.append({"x": xv, "kraus_vs_formula_maxdev": float(np.max(np.abs(oB_f - oB_k))),
                   "F_from_channel_formula": F_num, "F_from_closed_form": F_pred,
                   "abs_err": abs(F_num - F_pred)})
out["R3_value_checks"] = r3
out["R3_max_abs_err"] = max(d["abs_err"] for d in r3)
out["R3_max_kraus_vs_formula"] = max(d["kraus_vs_formula_maxdev"] for d in r3)

# ------------------------------------- consequence (3.2): F = 0 iff rank<=1 with iso factor
u0 = sp.Matrix([1, sp.I, 0])
tests = {
    "iso x iso  u0 u0^T": u0 * u0.T,
    "iso x conj-iso": u0 * u0.conjugate().T,
    "one iso factor y u0^T": sp.Matrix([1, 2, 3]) * u0.T,
    "type-E diag(1,1,0)": sp.diag(1, 1, 0),
    "max entangled I": sp.eye(3),
    "diag(1,i,0) Tr(MM^T)=0": sp.diag(1, sp.I, 0),
}
cons = {}
for name, Mv in tests.items():
    Fv = sp.simplify((1 - x) ** 2 * sp.Abs((Mv * Mv.T).trace()) ** 2
                     + x ** 2 * sum(sp.Abs(Mv.adjugate()[j, i]) ** 2 for i in range(3) for j in range(3)))
    cons[name] = {"F": str(sp.simplify(Fv)),
                  "F_is_zero": bool(sp.simplify(Fv) == 0),
                  "TrMMT": str(sp.simplify((Mv * Mv.T).trace())),
                  "adj_is_zero": bool(sp.simplify(Mv.adjugate()) == sp.zeros(3, 3))}
out["consequence_3_2"] = cons

print(json.dumps(out, indent=1, default=str))
with open("artifacts/logs_whgap_p13b_20260730/r7_s2.json", "w", newline="\n") as fh:
    json.dump(out, fh, indent=1, default=str)
