#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WHGAP P13-A sanity script  (commission notes/WHGAP_COMMISSION_P13A_20260730.md, gate G5)
Node: WHGAP.onset-two-fifths.  Author: E-P13A executor (fresh instance), 2026-07-30.
Interpreter: C:[USER_HOME]/cpython3119/python.exe  (sympy 1.13.1, mpmath 1.3.0, numpy 1.26.4)

Frozen conventions (WHGAP_REVIEW_COMMISSION_R5_20260729.md section 1):
  Lambda_x(Y) = (1-x) Y + (x/2) (Tr(Y) 1 - Y^T)             on qutrits, x in (0,1)
  K_0 = t 1, K_i = sg A_i (i=1,2,3), (A_i)_{jk} = eps_{ijk}, t = sqrt(1-x), sg = sqrt(x/2)
  Lambda^c(Y)_{ab} = Tr(K_a Y K_b^dag)  (4x4 padded; Kraus real so dag = T)
  Ic(rho) = S(Lambda(rho)) - S(Lambda^c(rho))
  tau(psi) = |psi^T psi|

Gates
  G5i    symbolic: normal form, 2x2-block trace/det identity, closed 3-eigenvalue spectrum,
         full-rank criterion, complement charpoly / isospectrality, kernel vector k,
         K(k) = -sg [psi]_x, K(k)^dag K(k) = (x/2)(1 - P_psi), w_E closed form
  G5ii   numeric: Ic(rho_eps) vs -w_E eps log(1/eps) at (x,alpha) in
         {(9/20,pi/8),(9/20,pi/6),(1/5,pi/8)}, 3 random phi, eps in {1e-4,1e-6}(+ smaller)
  G5iii  tau -> 0 continuity crosscheck against the reviewed isotropic data (note section 7.3)
  G5iv   exceptional-set scan: numeric rank of K(k) on a 20x20 (x,alpha) grid

All logs -> artifacts/logs_whgap_p13a_20260730/
"""

import json
import os
import random
import sys
import time

import sympy as sp
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUTDIR = os.path.join(ROOT, "artifacts", "logs_whgap_p13a_20260730")
os.makedirs(OUTDIR, exist_ok=True)

LOG_LINES = []
RESULTS = {"gates": {}, "meta": {}}


def log(msg=""):
    print(msg)
    LOG_LINES.append(str(msg))


def gate(name, ok, detail=""):
    RESULTS["gates"][name] = {"pass": bool(ok), "detail": detail}
    log("  [%s] %-46s %s" % ("PASS" if ok else "FAIL", name, detail))
    return bool(ok)


# ---------------------------------------------------------------------------
# shared Levi-Civita data
# ---------------------------------------------------------------------------
def levi_civita_A():
    """A_i with (A_i)_{jk} = eps_{ijk}; A_i v = v x e_i  (i,j,k in 1..3)."""
    out = []
    for i in (1, 2, 3):
        M = sp.zeros(3, 3)
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                M[j - 1, k - 1] = sp.LeviCivita(i, j, k)
        out.append(M)
    return out


A_SYM = levi_civita_A()


def charpoly_expr(M, lam):
    """charpoly via det(lam 1 - M) with the Berkowitz algorithm.

    sympy's Matrix.charpoly() calls _sort_factors, which raises
    'cannot determine truth value of Relational' on these symbolic entries
    (standing failure mode 5, sorting-of-symbolics variant).
    """
    n = M.rows
    return sp.expand((lam * sp.eye(n) - M).det(method="berkowitz"))


# ===========================================================================
# G5(i) : symbolic gates
# ===========================================================================
def gate_symbolic():
    log("")
    log("=" * 78)
    log("G5(i)  SYMBOLIC GATES")
    log("=" * 78)
    allok = True

    x = sp.Symbol("x", positive=True)
    u = sp.Symbol("u", positive=True)          # u = tan(alpha), alpha in (0, pi/4) <=> u in (0,1)
    t = sp.Symbol("t", positive=True)          # t  stands for sqrt(1-x)   (real positive symbol)
    sg = sp.Symbol("sg", positive=True)        # sg stands for sqrt(x/2)   (real positive symbol)
    I = sp.I

    # --- normal-form state, built entrywise (no conjugate() ever called on a radical) ----
    nrm = 1 + u ** 2
    psi = sp.Matrix([1, I * u, 0]) / sp.sqrt(nrm)
    psib = sp.Matrix([1, -I * u, 0]) / sp.sqrt(nrm)          # entrywise conjugate, by construction
    P = sp.Matrix([[1, -I * u, 0], [I * u, u ** 2, 0], [0, 0, 0]]) / nrm
    tau = (1 - u ** 2) / nrm                                  # = psi^T psi  (real, >0 for u<1)

    ok = sp.simplify(sp.expand(P - psi * psib.T)) == sp.zeros(3, 3)
    allok &= gate("G5i.a1_P_equals_psi_psidag", ok, "P = |psi><psi| entrywise")
    ok = sp.simplify(sp.expand(P * P - P)) == sp.zeros(3, 3) and sp.simplify(sp.trace(P)) == 1
    allok &= gate("G5i.a2_P_projector", ok, "P^2 = P, Tr P = 1")
    ok = sp.simplify((psi.T * psi)[0, 0] - tau) == 0
    allok &= gate("G5i.a3_tau_normal_form", ok, "psi^T psi = (1-u^2)/(1+u^2) = cos(2 alpha)")
    # cos(2 alpha) with u = tan alpha
    al = sp.Symbol("al", positive=True)
    ok = sp.simplify(sp.cos(2 * al) - tau.subs(u, sp.tan(al))) == 0
    allok &= gate("G5i.a4_tau_is_cos2alpha", ok, "tau = cos(2 alpha), u = tan(alpha)")
    ok = sp.simplify((psi.T * psib)[0, 0] - 1) == 0
    allok &= gate("G5i.a5_normalization", ok, "psi^T psibar = ||psi||^2 = 1")
    # <psi|psibar> = sum conj(psi_j) psibar_j = conj(psi^T psi) = tau
    ok = sp.simplify((psib.T * psib)[0, 0] - tau) == 0
    allok &= gate("G5i.a6_overlap_equals_tau", ok, "<psi|psibar> = tau")

    # --- G1 : Lambda(P) block structure, trace, det, spectrum  (radical-free in x) -------
    Lam = lambda Y: (1 - x) * Y + (x / 2) * (sp.trace(Y) * sp.eye(3) - Y.T)
    LP = sp.simplify(Lam(P))

    ok = all(sp.simplify(LP[i, 2]) == 0 and sp.simplify(LP[2, i]) == 0 for i in (0, 1))
    allok &= gate("G5i.b1_block_structure", ok, "Lambda(P) block diag wrt span{e1,e2} + span{e3}")
    ok = sp.simplify(LP[2, 2] - x / 2) == 0
    allok &= gate("G5i.b2_complement_eigenvalue", ok, "Lambda(P)_{33} = x/2")

    MW = LP[0:2, 0:2]
    trW = sp.simplify(sp.trace(MW))
    detW = sp.simplify(sp.expand(MW.det()))
    tgt_det = sp.simplify(x * (1 - x) * tau ** 2 / 2)
    ok = sp.simplify(trW - (1 - x / 2)) == 0
    allok &= gate("G5i.b3_block_trace", ok, "Tr(2x2 block) = 1 - x/2  (value: %s)" % sp.simplify(trW))
    ok = sp.simplify(sp.together(detW - tgt_det)) == 0
    allok &= gate("G5i.b4_block_det", ok, "det(2x2 block) = x(1-x)tau^2/2")

    # closed spectrum
    T0 = 1 - x / 2
    D0 = x * (1 - x) * tau ** 2 / 2
    disc = sp.simplify(T0 ** 2 - 4 * D0)
    mu_p = (T0 + sp.sqrt(disc)) / 2
    mu_m = (T0 - sp.sqrt(disc)) / 2
    lam = sp.Symbol("lam")
    tgt_cp = sp.expand((lam - x / 2) * (lam ** 2 - T0 * lam + D0))
    ok = sp.simplify(charpoly_expr(LP, lam) - tgt_cp) == 0
    allok &= gate("G5i.b5_charpoly_factorization", ok,
                  "charpoly Lambda(P) = (lam - x/2)(lam^2 - (1-x/2)lam + x(1-x)tau^2/2)")
    for nm, mu in (("mu_plus", mu_p), ("mu_minus", mu_m)):
        ok = sp.simplify(sp.expand(mu ** 2 - T0 * mu + D0)) == 0
        allok &= gate("G5i.b6_%s_is_root" % nm, ok, "%s solves the quadratic" % nm)
    # discriminant nonnegativity: T0^2 - 4 D0 >= (1-3x/2)^2 since tau^2 <= 1
    ok = sp.simplify(sp.expand(disc.subs(u, 0) - (1 - sp.Rational(3, 2) * x) ** 2)) == 0
    allok &= gate("G5i.b7_disc_at_tau1", ok, "tau=1 (u=0): T^2-4D = (1-3x/2)^2")
    # x/2 lies between the roots: q(x/2) = (x/2)(1-x)(tau^2-1) <= 0
    qhalf = sp.simplify(sp.expand((x / 2) ** 2 - T0 * (x / 2) + D0))
    ok = sp.simplify(sp.together(qhalf - (x / 2) * (1 - x) * (tau ** 2 - 1))) == 0
    allok &= gate("G5i.b8_xhalf_between_roots", ok, "q(x/2) = (x/2)(1-x)(tau^2-1) <= 0 => mu_- <= x/2 <= mu_+")
    # full rank criterion
    ok = sp.simplify(sp.together(LP.det() - (x / 2) * tgt_det)) == 0
    allok &= gate("G5i.b9_det_Lambda_P", ok, "det Lambda(P) = (x/2) x(1-x) tau^2/2 -> full rank iff tau>0")
    # lower bound g >= x(1-x)tau^2/(2-x): mu_- = D/mu_+ and mu_+ <= T
    ok = sp.simplify(sp.expand(mu_p * mu_m - D0)) == 0
    allok &= gate("G5i.b10_root_product", ok, "mu_+ mu_- = D (used for g >= D/T = x(1-x)tau^2/(2-x))")

    # --- E side: RATIONAL CHART, no radicals anywhere ----------------------------------
    # Failure mode 1 discipline. Substituting t**2 -> 1-x on an expression containing the
    # ODD power t*sg makes sympy rewrite t as sqrt(1-x); conjugate(sqrt(1-x)) then survives
    # because sympy cannot decide 1-x > 0.  Instead use the rational point of the conic
    # t^2 + 2 sg^2 = 1:   t = (1-2v^2)/(1+2v^2), sg = 2v/(1+2v^2), v in (0, 1/sqrt2),
    # so x = 2 sg^2 = 8v^2/(1+2v^2)^2 sweeps (0,1) bijectively and EVERY expression below is
    # a rational function of (u, v) with rational coefficients: conjugation is entrywise-safe.
    v = sp.Symbol("v", positive=True)
    tv = (1 - 2 * v ** 2) / (1 + 2 * v ** 2)
    sgv = 2 * v / (1 + 2 * v ** 2)
    xv = sp.cancel(2 * sgv ** 2)
    ok = sp.simplify(tv ** 2 + 2 * sgv ** 2 - 1) == 0
    allok &= gate("G5i.c_chart_valid", ok,
                  "rational chart: t^2+2sg^2 = 1 with x = 8v^2/(1+2v^2)^2 = %s" % sp.factor(xv))
    T0v = sp.cancel(T0.subs(x, xv))
    D0v = sp.cancel(D0.subs(x, xv))

    K = [tv * sp.eye(3)] + [sgv * A for A in A_SYM]

    def Lamc(Y):
        M = sp.zeros(4, 4)
        for a in range(4):
            for b in range(4):
                M[a, b] = sp.cancel(sp.expand(sp.trace(K[a] * Y * K[b].T)))  # real Kraus: dag = T
        return M

    # channel reproduction gate (own check of the frozen Kraus data)
    Yg = sp.Matrix(3, 3, lambda i, j: sp.Symbol("y%d%d" % (i, j)))
    KrausSum = sum((K[a] * Yg * K[a].T for a in range(4)), sp.zeros(3, 3))
    Lamv = lambda Y: (1 - xv) * Y + (xv / 2) * (sp.trace(Y) * sp.eye(3) - Y.T)
    ok = sp.simplify(sp.expand(KrausSum - Lamv(Yg))) == sp.zeros(3, 3)
    allok &= gate("G5i.c0_kraus_reproduces_channel", ok, "sum K_a Y K_a^T = Lambda_x(Y), all 9 entries")
    idsum = sum((K[a].T * K[a] for a in range(4)), sp.zeros(3, 3))
    ok = sp.simplify(idsum - sp.eye(3)) == sp.zeros(3, 3)
    allok &= gate("G5i.c1_kraus_trace_preserving", ok, "sum K_a^T K_a = 1")

    LcP = Lamc(P)
    ok = len([e for e in LcP if e.has(sp.sqrt(2)) or e.atoms(sp.Pow) and
              any(p.exp.is_Rational and not p.exp.is_Integer for p in e.atoms(sp.Pow))]) == 0
    allok &= gate("G5i.c2_no_radical_present", ok, "every Lambda^c(P) entry is rational in (u,v)")
    ok = sp.simplify(sp.expand(LcP - LcP.conjugate().T)) == sp.zeros(4, 4)
    allok &= gate("G5i.c3_Lc_hermitian", ok, "Lambda^c(P) Hermitian")
    ok = sp.simplify(sp.trace(LcP) - 1) == 0
    allok &= gate("G5i.c4_Lc_trace_one", ok, "Tr Lambda^c(P) = 1")
    cp4 = charpoly_expr(LcP, lam)
    tgt4 = sp.expand(lam * (lam - xv / 2) * (lam ** 2 - T0v * lam + D0v))
    ok = sp.simplify(sp.together(cp4 - tgt4)) == 0
    allok &= gate("G5i.c5_complement_charpoly", ok,
                  "charpoly Lambda^c(P) = lam (lam-x/2)(lam^2-(1-x/2)lam+D) -> isospectral, ker dim 1")

    # kernel vector k = (0, psibar)
    k = sp.Matrix([0, psib[0], psib[1], psib[2]])
    ok = sp.simplify(sp.expand(LcP * k)) == sp.zeros(4, 1)
    allok &= gate("G5i.c6_k_in_kernel", ok, "Lambda^c(P) k = 0 with k = (0, psibar)")
    ok = sp.simplify((k.conjugate().T * k)[0, 0] - 1) == 0
    allok &= gate("G5i.c7_k_unit", ok, "||k|| = 1")

    # K(k) = sum_a conj(k_a) K_a ; conj of k = (0, psi) built entrywise
    kbar = sp.Matrix([0, psi[0], psi[1], psi[2]])
    Kk = sum((kbar[a] * K[a] for a in range(4)), sp.zeros(3, 3))
    cross = -sgv * sp.Matrix([[0, -psi[2], psi[1]], [psi[2], 0, -psi[0]], [-psi[1], psi[0], 0]])
    ok = sp.simplify(sp.expand(Kk - cross)) == sp.zeros(3, 3)
    allok &= gate("G5i.d1_Kk_is_minus_sg_cross", ok, "K(k) = -sg [psi]_x   (purely skew: k_0 = 0)")
    ok = sp.simplify(sp.expand(Kk * psi)) == sp.zeros(3, 1)
    allok &= gate("G5i.d2_Kk_psi_zero", ok, "K(k) psi = 0")
    KdK = sp.expand(Kk.conjugate().T * Kk)
    ok = sp.simplify(sp.expand(KdK - (xv / 2) * (sp.eye(3) - P))) == sp.zeros(3, 3)
    allok &= gate("G5i.d3_KdagK_closed_form", ok, "K(k)^dag K(k) = (x/2)(1 - P_psi)")
    cpK = charpoly_expr(KdK, lam)
    ok = sp.simplify(sp.together(cpK - sp.expand(lam * (lam - xv / 2) ** 2))) == 0
    allok &= gate("G5i.d4_KdagK_spectrum", ok,
                  "spec K^dag K = {0, x/2, x/2} -> rank K(k) = 2 for all tau, ker K(k) = span{psi}")
    # char roots of K(k) itself: 0, +- i sg sqrt(psi.psi) = 0, +- i sqrt(x tau/2)
    cpKk = charpoly_expr(Kk, lam)
    tgtKk = sp.expand(lam ** 3 + (xv / 2) * tau * lam)
    ok = sp.simplify(sp.together(cpKk - tgtKk)) == 0
    allok &= gate("G5i.d5_Kk_charpoly", ok,
                  "charpoly K(k) = lam^3 + (x tau/2) lam -> roots 0, +-i sqrt(x tau/2)")

    # w_E closed form on a general Hermitian phi
    ph = sp.zeros(3, 3)
    rs = [[sp.Symbol("r%d%d" % (i, j), real=True) for j in range(3)] for i in range(3)]
    ims = [[sp.Symbol("m%d%d" % (i, j), real=True) for j in range(3)] for i in range(3)]
    for i in range(3):
        ph[i, i] = rs[i][i]
        for j in range(i + 1, 3):
            ph[i, j] = rs[i][j] + I * ims[i][j]
            ph[j, i] = rs[i][j] - I * ims[i][j]
    Lcph = Lamc(ph)
    wE_def = sp.expand((k.conjugate().T * Lcph * k)[0, 0])
    wE_cls = sp.expand((xv / 2) * (1 - (psi.conjugate().T * ph * psi)[0, 0]))
    # Tr phi = 1 is NOT imposed here; the identity holds with Tr phi in place of 1
    wE_cls_gen = sp.expand((xv / 2) * (sp.trace(ph) - (psi.conjugate().T * ph * psi)[0, 0]))
    ok = sp.simplify(sp.together(wE_def - wE_cls_gen)) == 0
    allok &= gate("G5i.e1_wE_closed_form_general_phi", ok,
                  "<k|Lambda^c(phi)|k> = (x/2)(Tr phi - <psi|phi|psi>), general Hermitian phi")
    ok = sp.simplify(sp.together((wE_def - wE_cls).subs(rs[2][2], 1 - rs[0][0] - rs[1][1]))) == 0
    allok &= gate("G5i.e2_wE_on_states", ok, "on Tr phi = 1: w_E = (x/2)(1 - <psi|phi|psi>)")
    ok = sp.simplify(sp.together(wE_def - sp.trace(ph * KdK))) == 0
    allok &= gate("G5i.e3_wE_equals_Tr_phi_KdK", ok, "w_E = Tr[phi K(k)^dag K(k)]")

    RESULTS["meta"]["symbolic"] = {
        "tau_in_u": str(sp.simplify(tau)),
        "x_in_v": str(sp.factor(xv)),
        "det_2x2_block": str(sp.simplify(detW)),
        "mu_minus": str(sp.simplify(mu_m)),
        "mu_plus": str(sp.simplify(mu_p)),
        "wE_general": "(x/2)(Tr phi - <psi|phi|psi>)",
    }

    # --- general-psi (no normal form) versions of the load-bearing identities -----------
    log("")
    log("  -- general-psi gates (free complex psi, no normal form; rational chart) --")
    a1, a2, a3 = sp.symbols("a1 a2 a3", real=True)
    b1, b2, b3 = sp.symbols("b1 b2 b3", real=True)
    gpsi = sp.Matrix([a1 + I * b1, a2 + I * b2, a3 + I * b3])
    gpsib = sp.Matrix([a1 - I * b1, a2 - I * b2, a3 - I * b3])
    nsq = sp.expand((gpsib.T * gpsi)[0, 0])          # ||psi||^2
    gP = sp.expand(gpsi * gpsib.T)                   # unnormalized |psi><psi|
    gk = sp.Matrix([0, gpsib[0], gpsib[1], gpsib[2]])
    gkbar = sp.Matrix([0, gpsi[0], gpsi[1], gpsi[2]])
    gLcP = sp.zeros(4, 4)
    for a in range(4):
        for b in range(4):
            gLcP[a, b] = sp.expand(sp.trace(K[a] * gP * K[b].T))
    ok = sp.simplify(sp.expand(gLcP * gk)) == sp.zeros(4, 1)
    allok &= gate("G5i.f1_general_k_in_kernel", ok,
                  "Lambda^c(|psi><psi|) (0,psibar) = 0 for ARBITRARY complex psi")
    gKk = sum((gkbar[a] * K[a] for a in range(4)), sp.zeros(3, 3))
    gcross = -sgv * sp.Matrix([[0, -gpsi[2], gpsi[1]], [gpsi[2], 0, -gpsi[0]], [-gpsi[1], gpsi[0], 0]])
    ok = sp.simplify(sp.expand(gKk - gcross)) == sp.zeros(3, 3)
    allok &= gate("G5i.f2_general_Kk_skew", ok, "K(k) = -sg [psi]_x for arbitrary psi")
    gKdK = sp.expand(gKk.conjugate().T * gKk)
    ok = sp.simplify(sp.expand(gKdK - (xv / 2) * (nsq * sp.eye(3) - gP))) == sp.zeros(3, 3)
    allok &= gate("G5i.f3_general_KdagK", ok,
                  "K(k)^dag K(k) = (x/2)(||psi||^2 1 - |psi><psi|); = (x/2)(1-P) for unit psi")
    # general-psi trace/det of the Lambda(P) 2x2 block, via the M = a1+pP+qQ route
    gPn = sp.expand(gP / nsq)
    gQn = sp.expand(gPn.T)
    gM = sp.expand((x / 2) * sp.eye(3) + (1 - x) * gPn - (x / 2) * gQn)
    gtau2 = sp.expand(sp.trace(gPn * gQn))            # = |<psi|psibar>|^2 = tau^2
    gcp = charpoly_expr(gM, lam)
    gtgt = sp.expand((lam - x / 2) * (lam ** 2 - (1 - x / 2) * lam + x * (1 - x) * gtau2 / 2))
    ok = sp.simplify(sp.together(gcp - gtgt)) == 0
    allok &= gate("G5i.f7_general_charpoly", ok,
                  "for ARBITRARY unit psi: charpoly Lambda(P) = (lam-x/2)(lam^2-(1-x/2)lam+x(1-x)tau^2/2)")
    ok = sp.simplify(sp.together(gtau2 - sp.expand((gpsi.T * gpsi)[0, 0] * (gpsib.T * gpsib)[0, 0] / nsq ** 2))) == 0
    allok &= gate("G5i.f8_tau2_identity", ok, "Tr(P P^T) = |psi^T psi|^2/||psi||^4 = tau^2")
    # rank/kernel of [psi]_x for arbitrary complex psi:  S^2 = psi psi^T - (psi.psi) 1,  S^3 = -(psi.psi) S
    S = sp.Matrix([[0, -gpsi[2], gpsi[1]], [gpsi[2], 0, -gpsi[0]], [-gpsi[1], gpsi[0], 0]])
    bil = sp.expand((gpsi.T * gpsi)[0, 0])
    ok = sp.simplify(sp.expand(S * S - (gpsi * gpsi.T - bil * sp.eye(3)))) == sp.zeros(3, 3)
    allok &= gate("G5i.f4_cross_square", ok, "[psi]_x^2 = psi psi^T - (psi.psi) 1")
    ok = sp.simplify(sp.expand(S * S * S + bil * S)) == sp.zeros(3, 3)
    allok &= gate("G5i.f5_cross_cube", ok, "[psi]_x^3 = -(psi.psi) [psi]_x  (char roots 0, +-i sqrt(psi.psi))")
    ok = sp.simplify(sp.expand(S * gpsi)) == sp.zeros(3, 1)
    allok &= gate("G5i.f6_cross_kernel", ok, "[psi]_x psi = 0")
    # transport gate: O^T A_i O = det(O) sum_j O_{ij} A_j, at 4 test O (2 proper, 2 improper)
    tests = []
    Os = []
    th = sp.Rational(3, 5)
    c35, s35 = sp.Rational(3, 5), sp.Rational(4, 5)
    Os.append(sp.Matrix([[c35, -s35, 0], [s35, c35, 0], [0, 0, 1]]))
    Os.append(sp.Matrix([[1, 0, 0], [0, c35, -s35], [0, s35, c35]]))
    Os.append(sp.diag(1, 1, -1))
    Os.append(sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]]))
    for O in Os:
        dO = O.det()
        good = all(sp.simplify(O.T * A_SYM[i] * O - dO * sum((O[i, j] * A_SYM[j] for j in range(3)),
                                                            sp.zeros(3, 3))) == sp.zeros(3, 3)
                   for i in range(3))
        tests.append(bool(good and sp.simplify(O.T * O - sp.eye(3)) == sp.zeros(3, 3)))
    ok = all(tests)
    allok &= gate("G5i.g1_transport_identity", ok,
                  "O^T A_i O = det(O) sum_j O_ij A_j at 4 test O (det = %s)" %
                  [str(O.det()) for O in Os])

    return allok


# ===========================================================================
# numeric machinery (mpmath)
# ===========================================================================
def num_A():
    out = []
    for i in (1, 2, 3):
        M = mp.matrix(3, 3)
        for j in (1, 2, 3):
            for k in (1, 2, 3):
                M[j - 1, k - 1] = int(sp.LeviCivita(i, j, k))
        out.append(M)
    return out


A_NUM = num_A()


def kraus_num(x):
    t = mp.sqrt(1 - x)
    sg = mp.sqrt(x / 2)
    K = [t * mp.eye(3)]
    for A in A_NUM:
        K.append(sg * A)
    return K


def dagger(M):
    r, c = M.rows, M.cols
    out = mp.matrix(c, r)
    for i in range(r):
        for j in range(c):
            out[j, i] = mp.conj(M[i, j])
    return out


def lam_num(x, Y):
    tr = Y[0, 0] + Y[1, 1] + Y[2, 2]
    out = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            out[i, j] = (1 - x) * Y[i, j] + (x / 2) * ((tr if i == j else 0) - Y[j, i])
    return out


def lamc_num(x, Y):
    K = kraus_num(x)
    out = mp.matrix(4, 4)
    for a in range(4):
        Ma = K[a] * Y
        for b in range(4):
            M = Ma * dagger(K[b])
            out[a, b] = M[0, 0] + M[1, 1] + M[2, 2]
    return out


def herm_eigs(M):
    E, _ = mp.eighe(M)
    return [mp.re(e) for e in E]


def entropy(M):
    s = mp.mpf(0)
    for lamv in herm_eigs(M):
        if lamv > 0:
            s -= lamv * mp.log(lamv)
    return s


def Ic_num(x, rho):
    return entropy(lam_num(x, rho)) - entropy(lamc_num(x, rho))


def psi_num(alpha):
    v = mp.matrix(3, 1)
    v[0] = mp.cos(alpha)
    v[1] = mp.mpc(0, 1) * mp.sin(alpha)
    v[2] = 0
    return v


def proj(v):
    out = mp.matrix(3, 3)
    for i in range(3):
        for j in range(3):
            out[i, j] = v[i] * mp.conj(v[j])
    return out


def rand_state(rng, d=3):
    G = mp.matrix(d, d)
    for i in range(d):
        for j in range(d):
            G[i, j] = mp.mpc(rng.gauss(0, 1), rng.gauss(0, 1))
    R = G * dagger(G)
    tr = sum(R[i, i] for i in range(d))
    for i in range(d):
        for j in range(d):
            R[i, j] = R[i, j] / tr
    return R


def mu_minus(x, tau):
    T = 1 - x / 2
    D = x * (1 - x) * tau ** 2 / 2
    return (T - mp.sqrt(T ** 2 - 4 * D)) / 2


def C_const(g):
    """C(x,tau) of the note: 6/(e g) + (5/2)log(5/2) + 3(1+log(2/g)) + 3(1+log(4/(3g)))."""
    return (6 / (mp.e * g) + mp.mpf(5) / 2 * mp.log(mp.mpf(5) / 2)
            + 3 * (1 + mp.log(2 / g)) + 3 * (1 + mp.log(4 / (3 * g))))


# ===========================================================================
# G5(ii) : numeric spot-check of the G2 expansion
# ===========================================================================
def gate_expansion():
    log("")
    log("=" * 78)
    log("G5(ii)  NUMERIC SPOT-CHECK OF THE LEADING-COEFFICIENT EXPANSION")
    log("=" * 78)
    mp.mp.dps = 80
    allok = True
    rows = []
    points = [("9/20", mp.mpf(9) / 20, "pi/8", mp.pi / 8),
              ("9/20", mp.mpf(9) / 20, "pi/6", mp.pi / 6),
              ("1/5", mp.mpf(1) / 5, "pi/8", mp.pi / 8)]
    eps_list = [mp.mpf("1e-4"), mp.mpf("1e-6"), mp.mpf("1e-8"), mp.mpf("1e-12"), mp.mpf("1e-20")]
    rng = random.Random(20260730)

    slope_ok = True
    bound_ok = True
    kernel_ok = True
    wE_ok = True

    for xs, x, alps, alpha in points:
        psi = psi_num(alpha)
        P = proj(psi)
        tau = abs(mp.re((psi.T * psi)[0, 0] if False else sum(psi[i] * psi[i] for i in range(3))))
        g = mu_minus(x, tau)
        C = C_const(g)
        LcP = lamc_num(x, P)
        ev = sorted(herm_eigs(LcP))
        # kernel dimension check + independent k from the eigenvector
        E, Q = mp.eighe(LcP)
        idx = min(range(4), key=lambda i: abs(mp.re(E[i])))
        kvec = mp.matrix(4, 1)
        for i in range(4):
            kvec[i] = Q[i, idx]
        # analytic k = (0, conj(psi))
        kan = mp.matrix(4, 1)
        kan[0] = 0
        for i in range(3):
            kan[i + 1] = mp.conj(psi[i])
        # fix phase
        ph = None
        for i in range(4):
            if abs(kan[i]) > mp.mpf("0.1"):
                ph = kvec[i] / kan[i]
                break
        dev_k = max(abs(kvec[i] - ph * kan[i]) for i in range(4))
        gap = abs(ev[1]) / max(abs(ev[0]), mp.mpf("1e-300"))
        kernel_ok &= (abs(ev[0]) < mp.mpf("1e-60")) and (abs(ev[1]) > mp.mpf("1e-3")) and dev_k < mp.mpf("1e-50")
        log("  x=%-5s alpha=%-5s tau=%s  g=mu_-=%s  C=%s" %
            (xs, alps, mp.nstr(tau, 12), mp.nstr(g, 12), mp.nstr(C, 10)))
        log("      spec Lambda^c(P) = %s" % [mp.nstr(e, 10) for e in ev])
        log("      kernel dim 1 (lam_1/lam_0 = %s), |k_numeric - phase*(0,conj psi)| = %s" %
            (mp.nstr(gap, 6), mp.nstr(dev_k, 6)))

        for ip in range(3):
            phi = rand_state(rng, 3)
            wE_formula = (x / 2) * (1 - mp.re((dagger(psi) * (phi * psi))[0, 0]))
            Lcphi = lamc_num(x, phi)
            wE_def = mp.re((dagger(kvec) * (Lcphi * kvec))[0, 0])
            wE_ok &= abs(wE_formula - wE_def) < mp.mpf("1e-50")
            Fs = {}
            for eps in eps_list:
                rho = mp.matrix(3, 3)
                for i in range(3):
                    for j in range(3):
                        rho[i, j] = (1 - eps) * P[i, j] + eps * phi[i, j]
                ic = Ic_num(x, rho)
                pred = -wE_formula * eps * mp.log(1 / eps)
                resid = ic - pred
                Fs[eps] = ic / eps
                inrange = eps <= g / 4
                ok_b = (abs(resid) <= C * eps) if inrange else None
                if inrange and not ok_b:
                    bound_ok = False
                rows.append({"x": xs, "alpha": alps, "phi": ip, "eps": mp.nstr(eps, 3),
                             "Ic": mp.nstr(ic, 14), "pred": mp.nstr(pred, 14),
                             "resid_over_eps": mp.nstr(resid / eps, 10),
                             "w_E": mp.nstr(wE_formula, 14),
                             "eps_le_g_over_4": bool(inrange),
                             "abs_resid_le_C_eps": (None if not inrange else bool(ok_b)),
                             "Ic_sign": ("+" if ic > 0 else "-")})
            # two-point slope extraction at the two smallest eps
            e1, e2 = eps_list[-2], eps_list[-1]
            slope = (Fs[e1] - Fs[e2]) / (mp.log(1 / e1) - mp.log(1 / e2))
            relerr = abs(slope + wE_formula) / wE_formula
            slope_ok &= relerr < mp.mpf("1e-6")
            log("      phi#%d  w_E=%s (formula) =%s (from numeric k)  slope@1e-12/1e-20 = %s  rel.err vs -w_E = %s"
                % (ip, mp.nstr(wE_formula, 12), mp.nstr(wE_def, 12), mp.nstr(slope, 12), mp.nstr(relerr, 6)))

    allok &= gate("G5ii.a_kernel_dim_and_k", kernel_ok,
                  "dim ker Lambda^c(P_psi) = 1 and numeric kernel vector = (0, conj psi) up to phase")
    allok &= gate("G5ii.b_wE_two_routes", wE_ok,
                  "<k|Lambda^c(phi)|k> = (x/2)(1-<psi|phi|psi>) to <1e-50 (9 (point,phi) pairs)")
    allok &= gate("G5ii.c_slope_equals_minus_wE", slope_ok,
                  "two-point log-slope of Ic/eps -> -w_E, rel.err < 1e-6 (9 pairs)")
    allok &= gate("G5ii.d_rigorous_bound_where_applicable", bound_ok,
                  "|Ic + w_E eps log(1/eps)| <= C(x,tau) eps at every tested eps <= g/4")

    # certificate points at ultra-small eps, where the bound also forces the SIGN
    log("")
    log("  -- certificate points (eps below exp(-C/w_E): the bound forces Ic < 0) --")
    cert = []
    cert_ok = True
    for ip_, (xs, x0, alps, alpha0) in enumerate(points):
        # pass 1 at low precision: size the certificate eps and the needed working precision
        mp.mp.dps = 60
        x = mp.mpf(x0)
        alpha = mp.mpf(alpha0)
        psi = psi_num(alpha)
        tau = abs(sum(psi[i] * psi[i] for i in range(3)))
        g = mu_minus(x, tau)
        C = C_const(g)
        phi = rand_state(random.Random(11235 + ip_), 3)
        wE = (x / 2) * (1 - mp.re((dagger(psi) * (phi * psi))[0, 0]))
        eps0 = min(g / 4, mp.exp(mp.mpf("-1.2") * C / wE))
        need = int(mp.mpf("2.5") * (-mp.log10(eps0))) + 200
        # pass 2 at the required precision (phi is regenerated bit-identically from the seed)
        mp.mp.dps = need
        x = mp.mpf(9) / 20 if xs == "9/20" else mp.mpf(1) / 5
        alpha = mp.pi / 8 if alps == "pi/8" else mp.pi / 6
        psi = psi_num(alpha)
        P = proj(psi)
        tau = abs(sum(psi[i] * psi[i] for i in range(3)))
        g = mu_minus(x, tau)
        C = C_const(g)
        phi = rand_state(random.Random(11235 + ip_), 3)
        wE = (x / 2) * (1 - mp.re((dagger(psi) * (phi * psi))[0, 0]))
        eps = min(g / 4, mp.exp(mp.mpf("-1.2") * C / wE))
        rho = mp.matrix(3, 3)
        for i in range(3):
            for j in range(3):
                rho[i, j] = (1 - eps) * P[i, j] + eps * phi[i, j]
        ic = Ic_num(x, rho)
        pred = -wE * eps * mp.log(1 / eps)
        ok1 = ic < 0
        ok2 = abs(ic - pred) <= C * eps
        cert_ok &= bool(ok1 and ok2)
        cert.append({"x": xs, "alpha": alps, "dps": need, "eps": mp.nstr(eps, 8),
                     "w_E": mp.nstr(wE, 12), "C": mp.nstr(C, 8), "Ic": mp.nstr(ic, 14),
                     "pred": mp.nstr(pred, 14), "Ic_negative": bool(ok1), "bound_holds": bool(ok2)})
        log("      x=%-5s alpha=%-5s dps=%-5d eps=%s  Ic=%s  (-w_E eps log(1/eps))=%s  Ic<0:%s bound:%s"
            % (xs, alps, need, mp.nstr(eps, 8), mp.nstr(ic, 12), mp.nstr(pred, 12), ok1, ok2))
    allok &= gate("G5ii.e_certificate_points", cert_ok,
                  "at eps = min(g/4, exp(-1.2 C/w_E)) < exp(-C/w_E): Ic < 0 strictly AND the "
                  "remainder bound holds, at adaptive precision (3 points)")
    mp.mp.dps = 80
    RESULTS["meta"]["G5ii_table"] = rows
    RESULTS["meta"]["G5ii_certificates"] = cert
    return allok


# ===========================================================================
# G5(iii) : tau -> 0 continuity crosscheck against the reviewed isotropic data
# ===========================================================================
def gate_tau_zero():
    log("")
    log("=" * 78)
    log("G5(iii)  tau -> 0 CROSSCHECK vs THE REVIEWED ISOTROPIC DATA (N1' note section 7.3)")
    log("=" * 78)
    mp.mp.dps = 60
    allok = True
    rows = []
    ok_wE = True
    ok_mu = True
    ok_split = True
    for xs, x in (("9/20", mp.mpf(9) / 20), ("1/5", mp.mpf(1) / 5)):
        muA = 4 * x * (1 - x) / (2 - x)          # reviewed isotropic block-A slope
        wE_iso = muA + x / 2                     # reviewed isotropic w_E at phi = P_psibar
        log("  x=%s : reviewed isotropic mu_A = %s, w_E^iso(P_psibar) = %s, block-B slope x/2 = %s"
            % (xs, mp.nstr(muA, 12), mp.nstr(wE_iso, 12), mp.nstr(x / 2, 12)))
        for tau in [mp.mpf("1e-1"), mp.mpf("1e-2"), mp.mpf("1e-3"), mp.mpf("1e-5")]:
            alpha = mp.acos(tau) / 2
            psi = psi_num(alpha)
            psib = mp.matrix(3, 1)
            for i in range(3):
                psib[i] = mp.conj(psi[i])
            phi = proj(psib)                     # the isotropic witness state P_psibar
            # our tau>0 formula
            wE_ours = (x / 2) * (1 - mp.re((dagger(psi) * (phi * psi))[0, 0]))
            wE_pred = (x / 2) * (1 - tau ** 2)
            ok_wE &= abs(wE_ours - wE_pred) < mp.mpf("1e-40")
            # the vanishing regular eigenvalue and its tau^2 slope
            g = mu_minus(x, tau)
            LcP = lamc_num(x, proj(psi))
            ev = sorted(herm_eigs(LcP))
            g_num = ev[1]
            ok_mu &= abs(g - g_num) < mp.mpf("1e-40")
            ratio = g / tau ** 2
            ok_split &= abs(ratio - muA / 4) < mp.mpf("1e-3") * (muA / 4) + tau ** 2
            rows.append({"x": xs, "tau": mp.nstr(tau, 4),
                         "wE_tau_pos": mp.nstr(wE_ours, 14),
                         "wE_limit_x_over_2": mp.nstr(x / 2, 14),
                         "mu_minus": mp.nstr(g, 14),
                         "mu_minus_over_tau2": mp.nstr(ratio, 14),
                         "muA_over_4": mp.nstr(muA / 4, 14),
                         "eps_window_g_over_4": mp.nstr(g / 4, 8)})
            log("     tau=%-8s w_E(tau>0)=%s -> x/2=%s | mu_- =%s, mu_-/tau^2=%s vs mu_A/4=%s | window g/4=%s"
                % (mp.nstr(tau, 4), mp.nstr(wE_ours, 12), mp.nstr(x / 2, 12), mp.nstr(g, 10),
                   mp.nstr(ratio, 10), mp.nstr(muA / 4, 10), mp.nstr(g / 4, 6)))
    allok &= gate("G5iii.a_wE_limit", ok_wE,
                  "w_E(tau>0, phi=P_psibar) = (x/2)(1-tau^2) -> x/2 = the isotropic BLOCK-B slope")
    allok &= gate("G5iii.b_mu_minus_matches", ok_mu,
                  "closed-form mu_-(x,tau) reproduces the numeric 2nd-smallest Lambda^c(P) eigenvalue")
    allok &= gate("G5iii.c_muA_is_the_leaving_eigenvalue", ok_split,
                  "mu_-(x,tau)/tau^2 -> x(1-x)/(2-x) = mu_A/4: the missing isotropic slope mu_A "
                  "belongs to the eigenvalue that is NONZERO for tau>0")
    RESULTS["meta"]["G5iii_table"] = rows
    log("")
    log("  READING: the tau>0 result must NOT be continued to tau=0. At tau=0 the E-side kernel")
    log("  jumps from dim 1 to dim 2 and the B-side acquires a kernel; the extra isotropic slope")
    log("  mu_A = 4x(1-x)/(2-x) is carried by mu_-(x,tau) ~ x(1-x)tau^2/(2-x), which is a REGULAR")
    log("  (nonzero) eigenvalue for every tau>0. Correspondingly the validity window eps <= g/4")
    log("  collapses like tau^2, which is exactly why no contradiction with the isotropic ascent.")
    return allok


# ===========================================================================
# G5(iv) : exceptional-set scan
# ===========================================================================
def gate_exceptional_scan():
    log("")
    log("=" * 78)
    log("G5(iv)  EXCEPTIONAL-SET SCAN: numeric rank of K(k) on a 20 x 20 (x, alpha) grid")
    log("=" * 78)
    mp.mp.dps = 50
    allok = True
    N = 20
    xs = [mp.mpf(i) / (N + 1) for i in range(1, N + 1)]                    # x in (0,1)
    als = [mp.pi / 4 * mp.mpf(i) / (N + 1) for i in range(1, N + 1)]       # alpha in (0, pi/4) => tau>0
    worst_rank2 = None
    worst_sv0 = mp.mpf(0)
    min_sv12 = mp.mpf(10)
    worst_KdK = mp.mpf(0)
    worst_k = mp.mpf(0)
    min_kernel_gap = mp.mpf(10)
    rank_hist = {}
    for x in xs:
        for alpha in als:
            psi = psi_num(alpha)
            P = proj(psi)
            LcP = lamc_num(x, P)
            E, Q = mp.eighe(LcP)
            evs = sorted([mp.re(e) for e in E])
            # kernel of Lambda^c(P) must be 1-dimensional
            min_kernel_gap = min(min_kernel_gap, evs[1])
            idx = min(range(4), key=lambda i: abs(mp.re(E[i])))
            kvec = mp.matrix(4, 1)
            for i in range(4):
                kvec[i] = Q[i, idx]
            # analytic k
            kan = mp.matrix(4, 1)
            for i in range(3):
                kan[i + 1] = mp.conj(psi[i])
            ph = None
            for i in range(4):
                if abs(kan[i]) > mp.mpf("0.05"):
                    ph = kvec[i] / kan[i]
                    break
            worst_k = max(worst_k, max(abs(kvec[i] - ph * kan[i]) for i in range(4)))
            # K(k) from the numeric kernel vector
            K = kraus_num(x)
            Kk = mp.matrix(3, 3)
            for a in range(4):
                ca = mp.conj(kvec[a])
                for i in range(3):
                    for j in range(3):
                        Kk[i, j] += ca * K[a][i, j]
            KdK = dagger(Kk) * Kk
            sv2 = sorted([mp.re(e) for e in herm_eigs(KdK)])
            worst_sv0 = max(worst_sv0, abs(sv2[0]))
            min_sv12 = min(min_sv12, sv2[1])
            rank = sum(1 for v in sv2 if v > mp.mpf("1e-25"))
            rank_hist[rank] = rank_hist.get(rank, 0) + 1
            # closed form K^dag K = (x/2)(1-P)
            dev = mp.mpf(0)
            for i in range(3):
                for j in range(3):
                    tgt = (x / 2) * ((1 if i == j else 0) - P[i, j])
                    dev = max(dev, abs(KdK[i, j] - tgt))
            worst_KdK = max(worst_KdK, dev)
    log("  grid: x in {1/21,...,20/21}, alpha in {pi/4 * i/21, i=1..20}  (400 points, all tau>0)")
    log("  rank histogram of K(k):            %s" % rank_hist)
    log("  max |smallest eigenvalue of K^dag K|:      %s" % mp.nstr(worst_sv0, 8))
    log("  min  2nd-smallest eigenvalue of K^dag K:   %s" % mp.nstr(min_sv12, 8))
    log("  max deviation K^dag K vs (x/2)(1-P_psi):   %s" % mp.nstr(worst_KdK, 8))
    log("  max deviation numeric k vs (0, conj psi):  %s" % mp.nstr(worst_k, 8))
    log("  min 2nd-smallest eigenvalue of Lambda^c(P) (kernel-gap): %s" % mp.nstr(min_kernel_gap, 8))
    allok &= gate("G5iv.a_rank_two_everywhere", rank_hist == {2: 400},
                  "rank K(k) = 2 at all 400 grid points -> dim ker K(k) = 1 -> EXCEPTIONAL SET EMPTY")
    allok &= gate("G5iv.b_KdagK_closed_form", worst_KdK < mp.mpf("1e-30"),
                  "K^dag K = (x/2)(1 - P_psi) to %s" % mp.nstr(worst_KdK, 4))
    allok &= gate("G5iv.c_kernel_vector", worst_k < mp.mpf("1e-25"),
                  "numeric kernel vector = (0, conj psi) up to phase, dev %s" % mp.nstr(worst_k, 4))
    allok &= gate("G5iv.d_complement_kernel_dim_one", min_kernel_gap > mp.mpf("1e-6"),
                  "dim ker Lambda^c(P_psi) = 1 across the grid (min 2nd eigenvalue %s)"
                  % mp.nstr(min_kernel_gap, 4))
    RESULTS["meta"]["G5iv"] = {"rank_hist": {str(k): v for k, v in rank_hist.items()},
                              "max_sv0": mp.nstr(worst_sv0, 8),
                              "min_sv1": mp.nstr(min_sv12, 8),
                              "max_dev_KdK": mp.nstr(worst_KdK, 8),
                              "max_dev_k": mp.nstr(worst_k, 8),
                              "min_kernel_gap": mp.nstr(min_kernel_gap, 8)}
    return allok


# ===========================================================================
# G5(v) : NOT COMMISSIONED -- moderate-eps probe, recorded to fix the SCOPE of the
#         theorem (the theorem is a small-eps statement; at moderate eps a tau>0 base
#         point CAN give Ic > 0, and does so at x = 1/5 where Q > 0 is already proved)
# ===========================================================================
def gate_moderate_eps():
    log("")
    log("=" * 78)
    log("G5(v)  [ADD-ON, not commissioned]  moderate-eps probe from tau>0 pure base points")
    log("=" * 78)
    mp.mp.dps = 40
    rng = random.Random(777)
    out = []
    for xs, x in (("1/5", mp.mpf(1) / 5), ("9/20", mp.mpf(9) / 20), ("49/100", mp.mpf(49) / 100)):
        best = (mp.mpf("-1e9"), None, None)
        for ia in range(1, 9):
            alpha = mp.pi / 4 * mp.mpf(ia) / 8            # alpha in (0, pi/4], tau = cos 2 alpha >= 0
            psi = psi_num(alpha)
            P = proj(psi)
            phis = [proj(psi_num(mp.pi / 4 * mp.mpf(j) / 3)) for j in range(1, 4)]
            phis += [rand_state(rng, 3) for _ in range(4)]
            # include the "conjugate" witness phi = P_psibar
            pb = mp.matrix(3, 1)
            for i in range(3):
                pb[i] = mp.conj(psi[i])
            phis.append(proj(pb))
            for phi in phis:
                for ke in range(12):
                    eps = mp.mpf(10) ** (mp.mpf(-6) + mp.mpf(6) * ke / 11) * mp.mpf("0.9")
                    if eps > mp.mpf("0.9"):
                        continue
                    rho = mp.matrix(3, 3)
                    for i in range(3):
                        for j in range(3):
                            rho[i, j] = (1 - eps) * P[i, j] + eps * phi[i, j]
                    ic = Ic_num(x, rho)
                    if ic > best[0]:
                        best = (ic, alpha, eps)
        tau_b = abs(sum(psi_num(best[1])[i] * psi_num(best[1])[i] for i in range(3)))
        out.append({"x": xs, "max_Ic": mp.nstr(best[0], 10), "at_alpha_over_pi": mp.nstr(best[1] / mp.pi, 6),
                    "at_tau": mp.nstr(tau_b, 6), "at_eps": mp.nstr(best[2], 6)})
        log("  x=%-6s max Ic over the probe = %-16s at alpha/pi=%s (tau=%s), eps=%s"
            % (xs, mp.nstr(best[0], 10), mp.nstr(best[1] / mp.pi, 5), mp.nstr(tau_b, 5),
               mp.nstr(best[2], 5)))
    RESULTS["meta"]["G5v_moderate_eps"] = out
    log("  READING: at x = 1/5 (where Q > 0 is PROVED) a tau>0 base point gives Ic > 0 at")
    log("  MODERATE eps -- so the theorem of this note is strictly a small-eps (leading-order)")
    log("  statement and does NOT say tau != 0 base points are useless at finite mixing.")
    log("  This probe found nothing positive at 9/20 or 49/100, but it is a bounded search and")
    log("  licenses no claim; it only fixes the scope. (Compare P3's S1 scans, already on disk.)")
    return gate("G5v.probe_completed", True,
                "bounded moderate-eps probe finished (24 (x,alpha) x 8 phi x 12 eps); "
                "scope-fixing only, no claim")


# ===========================================================================
def main():
    t0 = time.time()
    log("WHGAP P13-A sanity script -- gates G5 (i)-(iv)")
    log("python: %s" % sys.version.replace("\n", " "))
    log("sympy %s, mpmath %s" % (sp.__version__, mp.__version__))
    RESULTS["meta"]["python"] = sys.version
    RESULTS["meta"]["sympy"] = sp.__version__
    RESULTS["meta"]["mpmath"] = mp.__version__

    ok = True
    ok &= gate_symbolic()
    ok &= gate_expansion()
    ok &= gate_tau_zero()
    ok &= gate_exceptional_scan()
    ok &= gate_moderate_eps()

    npass = sum(1 for v in RESULTS["gates"].values() if v["pass"])
    ntot = len(RESULTS["gates"])
    log("")
    log("=" * 78)
    log("SUMMARY: %d / %d gates PASS   (%s)" % (npass, ntot, "ALL PASS" if ok else "FAILURES PRESENT"))
    log("elapsed: %.1f s" % (time.time() - t0))
    RESULTS["meta"]["summary"] = {"pass": npass, "total": ntot, "all_pass": bool(ok)}

    with open(os.path.join(OUTDIR, "p13a_sanity.json"), "w", newline="\n") as f:
        json.dump(RESULTS, f, indent=1, sort_keys=True)
    with open(os.path.join(OUTDIR, "p13a_sanity.log"), "w", newline="\n") as f:
        f.write("\n".join(LOG_LINES) + "\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
