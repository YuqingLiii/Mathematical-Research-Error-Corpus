"""R7 reviewer script (independent): claims 2, 3, 5, 6 of the P13-B package.

Own exact construction of the 2-copy weight operator D_Psi and of the exact
negative-semidefiniteness / lambda_max certificates.

INDEPENDENT PATH (rule 7c).  Nothing is taken from tools/whgap_p13b_*.py (not read before
this file was written).  My own derivation, from the frozen definitions only:

  * Lambda^{(2)}(rho) = sum_m W_m rho W_m^dag, W_m = K_a (x) K_b = c_m Bhat_m,
    Bhat_m = Ahat_a (x) Ahat_b integer, c_m^2 = c_a^2 c_b^2 rational in x.
  * Lambda self-adjoint in Hilbert-Schmidt  ==>  M_B := (Lambda^{(2)})^dag(Pi_B)
    = sum_m c_m^2 Bhat_m^T Pi_B Bhat_m.  (Cross-checked against a DIRECT index-action
    implementation of Y -> (1-x)Y + (x/2)(Tr Y . 1 - Y^T) on each tensor factor, which
    never mentions the Kraus set.)
  * (Lambda^c)^dag(Z) = sum_{ab} Z_{ab} K_a^T K_b   (own derivation:
    <Z, Lambda^c(Y)> = Tr[(sum_{ab} conj(Z_ab) K_b^T K_a) Y]), so
    M_E = sum_{mn} (Pi_E)_{mn} W_m^T W_n = sum_{mn} R_{mn} Bhat_m^T Bhat_n with
    R := Delta Pi_E Delta.
  * RADICAL-FREE Pi_E BY THE RANGE ROUTE (this differs from the executor's kernel-basis
    route): Ghat_{mn} := Tr[Bhat_m P_Psi Bhat_n^T] is x-free and G_E = Delta Ghat Delta,
    so range(G_E) = Delta range(Ghat).  With S a rational column basis of range(Ghat),
    the projector onto range(G_E) is Q = Delta S (S^dag D2 S)^{-1} S^dag Delta, hence
      R = Delta (1 - Q) Delta = D2 - D2 S (S^dag D2 S)^{-1} S^dag D2,
    which is rational in x with no square root anywhere.  (The executor used
    R = Nhat (Nhat^dag D2inv Nhat)^{-1} Nhat^dag with Nhat a basis of ker Ghat; the two
    are compared numerically inside this script as an extra gate.)
  * D_Psi = M_B - M_E.  Exact certificate: D Hermitian with real spectrum, and
      D <= 0  <==>  every coefficient of det(lam*1 - D) is >= 0
    (write lam_i = -mu_i >= 0: det = prod(lam + mu_i) has nonnegative coefficients;
    conversely nonnegative coefficients + monic => no positive real root).

Interpreter: C:[USER_HOME]/cpython3119/python.exe
"""
import itertools
import json
import sys
import time

import sympy as sp

lam = sp.Symbol("lam")


def eps3(i, j, k):
    return sp.Integer((i - j) * (j - k) * (k - i)) // 2 if len({i, j, k}) == 3 else sp.Integer(0)


A = [sp.Matrix(3, 3, lambda j, k: eps3(i, j, k)) for i in range(3)]
Ahat = [sp.eye(3)] + A
u0 = sp.Matrix([1, sp.I, 0])
u0b = sp.Matrix([1, -sp.I, 0])
e3 = sp.Matrix([0, 0, 1])

IDX = [(a, b) for a in range(4) for b in range(4)]
Bhat = [sp.Matrix(sp.kronecker_product(Ahat[a], Ahat[b])) for (a, b) in IDX]


def csq_of(a, xv):
    return (1 - xv) if a == 0 else xv / sp.Integer(2)


def vec(Mx):
    """Psi_{3j+k} = M_{jk}"""
    return sp.Matrix([Mx[j, k] for j in range(3) for k in range(3)])


def lam1_direct(Z, xv):
    """Lambda_x on tensor factor 1 of a 9x9 sympy matrix, from the CHANNEL FORMULA."""
    R = sp.zeros(9, 9)
    for j, k, jp, kp in itertools.product(range(3), repeat=4):
        val = (1 - xv) * Z[3 * j + k, 3 * jp + kp]
        pt = sum(Z[3 * p + k, 3 * p + kp] for p in range(3))
        val += xv / 2 * ((1 if j == jp else 0) * pt - Z[3 * jp + k, 3 * j + kp])
        R[3 * j + k, 3 * jp + kp] = val
    return R


def lam2_direct(Z, xv):
    R = sp.zeros(9, 9)
    for j, k, jp, kp in itertools.product(range(3), repeat=4):
        val = (1 - xv) * Z[3 * j + k, 3 * jp + kp]
        pt = sum(Z[3 * j + p, 3 * jp + p] for p in range(3))
        val += xv / 2 * ((1 if k == kp else 0) * pt - Z[3 * j + kp, 3 * jp + k])
        R[3 * j + k, 3 * jp + kp] = val
    return R


def proj_from_basis(N, simp=sp.simplify):
    """orthogonal projector onto col span of N (columns independent)."""
    Nd = N.conjugate().T
    return simp(N * (Nd * N).inv() * Nd)


def weight_operator(Mx, xv, crosschecks=True, simp=None):
    """exact D_Psi, plus diagnostics."""
    info = {}
    if simp is None:
        simp = sp.expand if xv.is_number else sp.simplify
    Psi = vec(Mx)
    nrm2 = simp((Psi.conjugate().T * Psi)[0, 0])
    P = simp(Psi * Psi.conjugate().T / nrm2)

    # ---- B side
    GB = sp.zeros(9, 9)
    for m, (a, b) in enumerate(IDX):
        GB += csq_of(a, xv) * csq_of(b, xv) * Bhat[m] * P * Bhat[m].T
    GB = simp(GB)
    NB = GB.nullspace()                                # own route: nullspace of G_B itself
    mB = len(NB)
    r = 9 - mB
    info["r"] = r
    info["m_B"] = mB

    # x-free cross-check of the kernel (claim 2): ker G_B = (span{Ahat_a M Ahat_b^T})^perp
    U = sp.Matrix.hstack(*[vec(Ahat[a] * Mx * Ahat[b].T) for (a, b) in IDX])
    info["rank_U"] = U.rank()
    NB2 = U.conjugate().T.nullspace()
    info["kernel_dims_agree"] = (len(NB2) == mB)

    if mB:
        NBm = sp.Matrix.hstack(*NB)
        PiB = proj_from_basis(NBm, simp)
        if info["kernel_dims_agree"]:
            PiB2 = proj_from_basis(sp.Matrix.hstack(*NB2), simp)
            info["PiB_two_routes_equal"] = bool(simp(PiB - PiB2) == sp.zeros(9, 9))
        MB = sp.zeros(9, 9)
        for m, (a, b) in enumerate(IDX):
            MB += csq_of(a, xv) * csq_of(b, xv) * Bhat[m].T * PiB * Bhat[m]
        MB = simp(MB)
        if crosschecks:
            MBd = simp(lam2_direct(lam1_direct(PiB, xv), xv))
            info["MB_selfadjoint_route_equals_direct_formula"] = bool(simp(MB - MBd) == sp.zeros(9, 9))
    else:
        PiB = sp.zeros(9, 9)
        MB = sp.zeros(9, 9)
        info["PiB_two_routes_equal"] = True
        info["MB_selfadjoint_route_equals_direct_formula"] = True

    # ---- E side, radical-free RANGE route
    Ghat = sp.Matrix(16, 16, lambda m, n: simp((Bhat[m] * P * Bhat[n].T).trace()))
    D2 = sp.diag(*[csq_of(a, xv) * csq_of(b, xv) for (a, b) in IDX])
    info["rank_Ghat"] = Ghat.rank()
    cols = Ghat.columnspace()
    S = sp.Matrix.hstack(*cols)
    R = simp(D2 - D2 * S * (S.conjugate().T * D2 * S).inv() * S.conjugate().T * D2)
    info["m_E"] = 16 - len(cols)
    ME = sp.zeros(9, 9)
    for m in range(16):
        for n in range(16):
            if R[m, n] != 0:
                ME += R[m, n] * Bhat[m].T * Bhat[n]
    ME = simp(ME)

    D = simp(MB - ME)
    info["D_hermitian"] = bool(simp(D - D.conjugate().T) == sp.zeros(9, 9))
    info["ME_psd_trace"] = str(simp(ME.trace()))
    info["Tr_D_P"] = str(simp((D * P).trace()))
    info["D_Psi_is_zero_vector"] = bool(simp(D * Psi) == sp.zeros(9, 1))
    return D, info


def nsd_certificate(D):
    """exact charpoly-coefficient certificate; returns (is_nsd, coeffs, lam_max_exact_or_None).

    Denominators are cleared first: with L a positive integer clearing every entry of D,
    N := L*D is a Gaussian-INTEGER Hermitian matrix, spec(N) = L*spec(D), so N <= 0 <=> D <= 0
    and lam_max(D) = lam_max(N)/L.  This keeps the degree-9 Berkowitz determinant in integer
    arithmetic (sympy 'simplify' on large rationals was the bottleneck).
    """
    dens = []
    for i in range(9):
        for j in range(9):
            dens += [int(sp.denom(sp.re(D[i, j]))), int(sp.denom(sp.im(D[i, j])))]
    L = sp.ilcm(*dens)
    N = sp.Matrix(9, 9, lambda i, j: sp.expand(L * D[i, j]))
    # charpoly via Newton's identities from p_k = Tr(N^k)  (integer arithmetic only; the
    # symbolic-lam Berkowitz determinant is far slower on 14-digit Gaussian integers).
    p, Nk = [], sp.eye(9)
    for k in range(1, 10):
        Nk = sp.expand(Nk * N)
        p.append(sp.expand(Nk.trace()))
    e = [sp.Integer(1)]
    for k in range(1, 10):
        acc = 0
        for i in range(1, k + 1):
            acc += (-1) ** (i - 1) * e[k - i] * p[i - 1]
        e.append(sp.expand(acc / k))
    coeffs = [(-1) ** k * e[k] for k in range(10)]      # det(lam*1 - N) = sum_k (-1)^k e_k lam^{9-k}
    real_ok = all(sp.im(c) == 0 for c in coeffs)
    reco = [sp.re(c) for c in coeffs]
    is_nsd = all(c >= 0 for c in reco)
    lam_max = None
    if not is_nsd:
        lam_max = max(sp.real_roots(sp.Poly(reco, lam))) / L
    return is_nsd, [str(c) for c in reco], lam_max, real_ok


FAMILIES = {
    "iso_prod_a  M=u0 u0^T": u0 * u0.T,
    "iso_conjiso_d  M=u0 u0bar^T": u0 * u0b.T,
    "typeE  M=diag(1,1,0)": sp.diag(1, 1, 0),
    "typeE_e2  M=E12+E21": sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    "P3g_r8  M=u0(1,0,2)^T+(0,1,1)u0^T": u0 * sp.Matrix([[1, 0, 2]]) + sp.Matrix([0, 1, 1]) * u0.T,
    "P3s  M=u0 e3^T + e3 u0^T": u0 * e3.T + e3 * u0.T,
    "P3c_r6  M=(u0+e3)u0^T": (u0 + e3) * u0.T,
    "maxent  M=I": sp.eye(3),
    "diag1i0  M=diag(1,i,0)": sp.diag(1, sp.I, 0),
}

JOBS = [
    ("iso_prod_a  M=u0 u0^T", sp.Rational(9, 20)),
    ("typeE  M=diag(1,1,0)", sp.Rational(21, 50)),
    ("P3g_r8  M=u0(1,0,2)^T+(0,1,1)u0^T", sp.Rational(12, 25)),
    ("typeE  M=diag(1,1,0)", sp.Rational(2, 5)),
    ("P3g_r8  M=u0(1,0,2)^T+(0,1,1)u0^T", sp.Rational(2, 5)),
    ("P3s  M=u0 e3^T + e3 u0^T", sp.Rational(9, 20)),
    ("iso_prod_a  M=u0 u0^T", sp.Rational(7, 20)),
    ("typeE  M=diag(1,1,0)", sp.Rational(7, 20)),
    ("typeE_e2  M=E12+E21", sp.Rational(7, 20)),
    ("P3c_r6  M=(u0+e3)u0^T", sp.Rational(7, 20)),
    ("maxent  M=I", sp.Rational(9, 20)),
    ("diag1i0  M=diag(1,i,0)", sp.Rational(9, 20)),
    ("iso_prod_a  M=u0 u0^T", sp.Rational(11, 20)),
]

if __name__ == "__main__":
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    results = []
    for name, xv in JOBS:
        if only and not any(o in name for o in only):
            continue
        t0 = time.time()
        D, info = weight_operator(FAMILIES[name], xv)
        is_nsd, coeffs, lmax, real_ok = nsd_certificate(D)
        rec = {"family": name, "x": str(xv), **info,
               "charpoly_coeffs_real": real_ok,
               "NSD_exact_certificate": is_nsd,
               "lambda_max_exact": (str(lmax) if lmax is not None else "0"),
               "lambda_max_float": (float(lmax) if lmax is not None else 0.0),
               "secs": round(time.time() - t0, 1)}
        results.append(rec)
        print(json.dumps(rec, indent=1, default=str), flush=True)
    with open("artifacts/logs_whgap_p13b_20260730/r7_exact.json", "w", newline="\n") as fh:
        json.dump(results, fh, indent=1, default=str)
