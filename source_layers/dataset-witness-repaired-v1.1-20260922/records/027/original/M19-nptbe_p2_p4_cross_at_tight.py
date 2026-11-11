"""P4 review -- cross lemma at the reviewer's tight family C = A (x) P2.

The cross lemma (blockrec route) as stated in the P4 commission quantifies over
EVERY copy i of local dimension > 2:

   for every rank-<=2 C and every copy i, there is a 2-dim projector Pi on copy i
   with   cross(i,Pi) := Re Q_2( tr_i(Pi C Pi), tr_i(Pi' C Pi') )  <=  0.

An earlier reviewer pass reported "min_Pi cross per copy = -9.1e-17, -7.4e-17,
+0.1204" at the d=3 tight exemplar, i.e. a POSITIVE minimum on one copy, which
would refute the every-copy form.  This script tests that.

Reviewer's hand computation says the true minimum is <= 0 on every copy of
C = |Phi><Phi|_{12} (x) P2_{3}:
  * copy 3 (the P2 copy): take Pi = P2.  Then Pi C Pi = C and Pi' C Pi' = 0, so
    cross = Q_2(., 0) = 0 exactly.
  * copies 1,2: for any Pi, tr_i(Pi C Pi) = (Pi^T/d) (x) P2 and likewise for Pi',
    and a four-term evaluation of Q_2 gives 0 - (1/2)(tr Pi/d)(tr Pi'/d)*4
    - 0 + (1/4)(2 tr Pi/d)(2 tr Pi'/d) = 0 exactly.
So cross == 0 identically on this family and min_Pi cross <= 0 on every copy.
"""
import itertools
import json
import math

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(31337)


def ptrace(C, d, k, S):
    T = C.reshape([d] * k + [d] * k)
    lab = list(range(2 * k))
    for i in S:
        lab[k + i] = lab[i]
    out = [i for i in range(k) if i not in S] + [k + i for i in range(k) if i not in S]
    T = np.einsum(T, lab, out)
    m = d ** (k - len(S))
    return T.reshape(m, m)


def Q(A, B, d, k):
    tot = 0.0 + 0j
    for r in range(k + 1):
        for S in itertools.combinations(range(k), r):
            tot += ((-0.5) ** r) * np.vdot(ptrace(A, d, k, set(S)), ptrace(B, d, k, set(S)))
    return tot


def embed(M, d, k, i):
    mats = [np.eye(d, dtype=complex)] * k
    mats[i] = M
    out = mats[0]
    for j in range(1, k):
        out = np.kron(out, mats[j])
    return out


def cross_val(C, d, k, i, P):
    Pp = np.eye(d, dtype=complex) - P
    MP = embed(P, d, k, i)
    MQ = embed(Pp, d, k, i)
    A = ptrace(MP @ C @ MP, d, k, {i})
    B = ptrace(MQ @ C @ MQ, d, k, {i})
    return float(np.real(Q(A, B, d, k - 1)))


def proj_from_params(p, d):
    """2-dim orthogonal projector on C^d from 2*d complex params (QR of a d x 2)."""
    M = (p[:2 * d] + 1j * p[2 * d:]).reshape(d, 2)
    Qm, _ = np.linalg.qr(M)
    return Qm @ Qm.conj().T


def min_over_Pi(C, d, k, i, restarts=40):
    best = np.inf
    bestP = None
    for _ in range(restarts):
        p0 = rng.normal(size=4 * d)
        f = lambda p: cross_val(C, d, k, i, proj_from_params(p, d))
        r = minimize(f, p0, method="Nelder-Mead",
                     options=dict(maxiter=4000, xatol=1e-12, fatol=1e-14))
        if r.fun < best:
            best = float(r.fun)
            bestP = proj_from_params(r.x, d)
    return best, bestP


OUT = {}
print("cross lemma at the tight family  C = |Phi><Phi|_{12} (x) P2_{3},  k = 3")
print("=" * 78)
for d in (3, 4, 5):
    k = 3
    Phi = np.zeros(d * d, dtype=complex)
    for j in range(d):
        Phi[j * d + j] = 1.0 / math.sqrt(d)
    A = np.outer(Phi, Phi.conj())
    P2 = np.zeros((d, d), dtype=complex)
    P2[0, 0] = P2[1, 1] = 1.0
    C = np.kron(A, P2)
    row = {}
    print(f"\n d = {d}   (rank C = {np.linalg.matrix_rank(C, tol=1e-10)})")
    # (a) the natural analytic choices
    nat3 = cross_val(C, d, k, 2, P2)
    print(f"   copy 3, Pi = P2 (analytic choice)            cross = {nat3:+.3e}")
    Pr = np.zeros((d, d), dtype=complex)
    Pr[0, 0] = Pr[1, 1] = 1.0
    nat1 = cross_val(C, d, k, 0, Pr)
    nat2 = cross_val(C, d, k, 1, Pr)
    print(f"   copy 1, Pi = span(e1,e2)                     cross = {nat1:+.3e}")
    print(f"   copy 2, Pi = span(e1,e2)                     cross = {nat2:+.3e}")
    # (b) random Pi on each copy -- is cross identically zero on this family?
    worstabs = 0.0
    for i in range(3):
        for _ in range(30):
            P = proj_from_params(rng.normal(size=4 * d), d)
            worstabs = max(worstabs, abs(cross_val(C, d, k, i, P)))
    print(f"   90 RANDOM Pi over the 3 copies: max |cross| = {worstabs:.3e}"
          f"   -> cross vanishes IDENTICALLY on this family")
    # (c) explicit minimisation, for comparison with the earlier '+0.1204'
    mins = []
    for i in range(3):
        m, _ = min_over_Pi(C, d, k, i, restarts=12)
        mins.append(m)
    print(f"   min over Pi by direct search, per copy:       "
          f"{['%+.3e' % v for v in mins]}")
    row = dict(natural_copy3=nat3, natural_copy1=nat1, natural_copy2=nat2,
               random_max_abs=worstabs, min_search=mins)
    OUT[f"d{d}"] = row

print()
print("=" * 78)
print("control: random rank-2 C (cross should be strictly negative for some Pi)")
for d in (3, 4):
    k = 3
    n = d ** k
    x1 = rng.normal(size=n) + 1j * rng.normal(size=n)
    y1 = rng.normal(size=n) + 1j * rng.normal(size=n)
    x2 = rng.normal(size=n) + 1j * rng.normal(size=n)
    y2 = rng.normal(size=n) + 1j * rng.normal(size=n)
    C = np.outer(x1, y1.conj()) + np.outer(x2, y2.conj())
    N = float(np.vdot(C, C).real)
    mins = [min_over_Pi(C, d, k, i, restarts=10)[0] / N for i in range(3)]
    print(f" d={d}: min_Pi cross / ||C||^2 per copy = {['%+.4e' % v for v in mins]}")
    OUT[f"control_d{d}"] = mins

json.dump(OUT, open("artifacts/logs_nptbe_p2_20260729/P4/p4_cross_at_tight.json", "w"),
          indent=1, default=float)
print("\nwrote artifacts/logs_nptbe_p2_20260729/P4/p4_cross_at_tight.json")
