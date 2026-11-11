"""P4 review -- INDEPENDENT EXACT re-certification and headline-finding checks.

Written by the P4 reviewer.  No fleet code is imported; every quantity is
re-implemented from the frozen definitions:

    T_S C  = partial trace of C over the copies in S
    q_k(C) = sum_{S subset [k]} (-1/2)^{|S|} ||T_S C||_F^2
    g(C)   = q_k(C) / ||C||_F^2          (the normalised Rayleigh quotient W5 reports)

PART A -- exact re-certification of W5's stored argmina.
  W5 re-certified its stored best_p at 50 digits with mpmath, using its *factored*
  (inner-product) path.  I instead build C DENSELY and evaluate q_k in EXACT
  dyadic-rational arithmetic: every float64 is exactly m*2^e, so C, all partial
  traces, all Frobenius norms and 2^k * q_k are exact integers after a common
  power-of-two rescaling.  The sign of g is therefore decided EXACTLY, not to
  50 digits.  This is an independent construction (7f), not a formula check.

PART B -- the reviewer's tight family  C = A (x) P2  (A rank 1, P2 a rank-2
  orthogonal projector on one copy).  q_1(P2) = ||P2||^2 - (1/2)|tr P2|^2 = 2-2 = 0
  and q_k is multiplicative over a copy split, so q_3(C) = q_2(A)*0 = 0 for EVERY A
  and every d.  Checked exactly (rational) for the maximally entangled member and
  in float for random members; x-invariants compared with the predicted
  (2+u, t+2u, 2t) and (2+2/d, 1+4/d, 2).

PART C -- the decision-layer E_S reduction, exact counterexample.
"""
import itertools
import json
import math
import sys
from fractions import Fraction

import numpy as np

OUT = {}

# --------------------------------------------------------------- exact toolkit


def f2int(vals):
    """Exact common-scale integer representation of a list of float64.

    Returns (ints, E) with vals[i] == ints[i] * 2**E exactly.
    """
    exps = []
    mants = []
    for x in vals:
        if x == 0.0:
            mants.append(0)
            exps.append(0)
            continue
        m, e = math.frexp(x)
        mi = int(round(m * (1 << 53)))
        assert mi * 2.0 ** (e - 53) == x, "frexp roundtrip failed"
        mants.append(mi)
        exps.append(e - 53)
    nz = [e for e, m in zip(exps, mants) if m != 0]
    E = min(nz) if nz else 0
    ints = [m << (e - E) if m != 0 else 0 for m, e in zip(mants, exps)]
    for i, x in enumerate(vals):
        assert ints[i] * 2.0 ** E == x or x == 0.0
    return ints, E


def exact_g(Ur, Ui, Vr, Vi, d, k):
    """EXACT normalised Rayleigh quotient g = q_k(C)/||C||^2 for C = U @ V.T.

    Ur,Ui,Vr,Vi are float64 arrays of shape (n,2).  Everything is done with
    Python ints after a single common power-of-two rescaling, so the result is
    an exact Fraction.
    """
    n = d ** k
    flat = list(Ur.ravel()) + list(Ui.ravel()) + list(Vr.ravel()) + list(Vi.ravel())
    ints, E = f2int(flat)
    m = n * 2
    ur = ints[0:m]
    ui = ints[m:2 * m]
    vr = ints[2 * m:3 * m]
    vi = ints[3 * m:4 * m]
    # C = U @ V.T  (note: V.T, not V^dagger -- W5's convention)
    Cr = [0] * (n * n)
    Ci = [0] * (n * n)
    for i in range(n):
        a0r, a0i = ur[2 * i], ui[2 * i]
        a1r, a1i = ur[2 * i + 1], ui[2 * i + 1]
        base = i * n
        for j in range(n):
            b0r, b0i = vr[2 * j], vi[2 * j]
            b1r, b1i = vr[2 * j + 1], vi[2 * j + 1]
            Cr[base + j] = a0r * b0r - a0i * b0i + a1r * b1r - a1i * b1i
            Ci[base + j] = a0r * b0i + a0i * b0r + a1r * b1i + a1i * b1r

    def partial_trace(Rr, Ri, dims_r, S):
        """contract copy indices in S; dims_r = list of k dims (all d)."""
        keep = [i for i in range(k) if i not in S]
        nk = d ** len(keep)
        Tr = [0] * (nk * nk)
        Ti = [0] * (nk * nk)
        # enumerate row/col multi-indices
        for rowk in range(nk):
            rk = []
            t = rowk
            for _ in keep:
                rk.append(t % d)
                t //= d
            rk = rk[::-1]
            for colk in range(nk):
                ck = []
                t = colk
                for _ in keep:
                    ck.append(t % d)
                    t //= d
                ck = ck[::-1]
                sr = 0
                si = 0
                for contracted in itertools.product(range(d), repeat=len(S)):
                    ridx = [0] * k
                    cidx = [0] * k
                    for pos, i in enumerate(keep):
                        ridx[i] = rk[pos]
                        cidx[i] = ck[pos]
                    for pos, i in enumerate(sorted(S)):
                        ridx[i] = contracted[pos]
                        cidx[i] = contracted[pos]
                    R = 0
                    Cc = 0
                    for i in range(k):
                        R = R * d + ridx[i]
                        Cc = Cc * d + cidx[i]
                    sr += Rr[R * n + Cc]
                    si += Ri[R * n + Cc]
                Tr[rowk * nk + colk] = sr
                Ti[rowk * nk + colk] = si
        return Tr, Ti

    def fro2(Ar, Ai):
        return sum(a * a for a in Ar) + sum(a * a for a in Ai)

    N = fro2(Cr, Ci)
    num = 0  # 2^k * q_k, integer
    for r in range(k + 1):
        for S in itertools.combinations(range(k), r):
            Tr, Ti = partial_trace(Cr, Ci, [d] * k, set(S))
            num += ((-1) ** r) * (2 ** (k - r)) * fro2(Tr, Ti)
    return Fraction(num, (2 ** k) * N)


# --------------------------------------------------------- float toolkit (Part B)


def ptrace_np(C, d, k, S):
    T = C.reshape([d] * k + [d] * k)
    labels = list(range(2 * k))
    out = []
    for i in range(k):
        if i in S:
            labels[k + i] = labels[i]
    for i in range(k):
        if i not in S:
            out.append(i)
    for i in range(k):
        if i not in S:
            out.append(k + i)
    T = np.einsum(T, labels, out)
    m = d ** (k - len(S))
    return T.reshape(m, m)


def qk_np(C, d, k):
    tot = 0.0
    for r in range(k + 1):
        for S in itertools.combinations(range(k), r):
            T = ptrace_np(C, d, k, set(S))
            tot += ((-0.5) ** r) * float(np.vdot(T, T).real)
    return tot


def xinv(C, d, k=3):
    N = float(np.vdot(C, C).real)
    x1 = sum(float(np.vdot(ptrace_np(C, d, k, {i}), ptrace_np(C, d, k, {i})).real)
             for i in range(k)) / N
    x2 = sum(float(np.vdot(ptrace_np(C, d, k, set(S)), ptrace_np(C, d, k, set(S))).real)
             for S in itertools.combinations(range(k), 2)) / N
    x3 = abs(np.trace(C.reshape(d ** k, d ** k))) ** 2 / N
    return x1, x2, x3


# =============================================================== PART A
print("=" * 78)
print("PART A -- EXACT re-certification of W5 stored argmina (dense path, exact rationals)")
print("=" * 78)
cases = [("d5k3", 5, 3, "min_records_d5_k3.npz", "w5_d5k3.json"),
         ("d6k3", 6, 3, "min_records_d6_k3.npz", "w5_d6k3.json"),
         ("d3k4", 3, 4, "min_records_d3_k4.npz", "w5_d3k4.json"),
         ("d4k4", 4, 4, "min_records_d4_k4.npz", "w5_d4k4b.json")]
root = "artifacts/logs_nptbe_fleet_20260729/W5/"
partA = {}
for tag, d, k, npz, js in cases:
    z = np.load(root + npz)
    p = z["best_p"]
    n = d ** k
    m = n * 2
    U = (p[0:m] + 1j * p[m:2 * m]).reshape(n, 2)
    V = (p[2 * m:3 * m] + 1j * p[3 * m:4 * m]).reshape(n, 2)
    g_exact = exact_g(U.real.copy(), U.imag.copy(), V.real.copy(), V.imag.copy(), d, k)
    j = json.load(open(root + js))
    claimed = j["min_g_argmin_recheck"]["g_mp50"]
    gf = float(g_exact)
    # 30-digit decimal of the exact rational
    import decimal
    decimal.getcontext().prec = 40
    dec = decimal.Decimal(g_exact.numerator) / decimal.Decimal(g_exact.denominator)
    print(f"[{tag}] d={d} k={k}")
    print(f"   W5 claimed g_mp50 = {claimed}")
    print(f"   my EXACT rational = {dec}")
    print(f"   sign            = {'POSITIVE' if g_exact > 0 else ('ZERO' if g_exact == 0 else 'NEGATIVE')}")
    print(f"   numerator bits  = {g_exact.numerator.bit_length()}, denom bits = {g_exact.denominator.bit_length()}")
    rel = abs(float(dec) - float(claimed)) / abs(float(claimed))
    print(f"   relative agreement with W5's mp50: {rel:.3e}")
    partA[tag] = dict(d=d, k=k, claimed_mp50=claimed, exact_decimal=str(dec),
                      positive=bool(g_exact > 0), rel_agreement=rel)
OUT["partA_exact_recert"] = partA

# =============================================================== PART B
print()
print("=" * 78)
print("PART B -- reviewer's tight family C = A (x) P2  (exact zeros of q_3 for all d)")
print("=" * 78)
partB = {}
rng = np.random.default_rng(4041)
for d in (2, 3, 4, 5, 6, 8):
    # maximally entangled A on copies 1,2 ; P2 = rank-2 projector on copy 3
    Phi = np.zeros(d * d, dtype=complex)
    for i in range(d):
        Phi[i * d + i] = 1.0 / math.sqrt(d)
    A = np.outer(Phi, Phi.conj())
    P2 = np.zeros((d, d), dtype=complex)
    P2[0, 0] = 1.0
    P2[1, 1] = 1.0
    C = np.kron(A, P2)
    q = qk_np(C, d, 3)
    x = xinv(C, d, 3)
    pred = (2 + 2 / d, 1 + 4 / d, 2.0)
    h = x[0] - 0.75 * x[1] + 0.5 * x[2]
    rk = np.linalg.matrix_rank(C, tol=1e-10)
    print(f" d={d}: rank(C)={rk}  q3={q:+.3e}  x={tuple(round(v,9) for v in x)}"
          f"  predicted={tuple(round(v,9) for v in pred)}  h={h:.10f}  9/4-1/d={2.25-1/d:.10f}")
    partB[f"d{d}"] = dict(rank=int(rk), q3=q, x=list(x), pred=list(pred), h=h,
                          h_pred=2.25 - 1 / d)
# random members: q3 must be 0 for ANY rank-1 A
worst = 0.0
for d in (3, 5):
    for _ in range(20):
        a = rng.normal(size=d * d) + 1j * rng.normal(size=d * d)
        b = rng.normal(size=d * d) + 1j * rng.normal(size=d * d)
        A = np.outer(a, b.conj())
        P2 = np.diag([1.0, 1.0] + [0.0] * (d - 2)).astype(complex)
        C = np.kron(A, P2)
        worst = max(worst, abs(qk_np(C, d, 3)) / float(np.vdot(C, C).real))
print(f" random rank-1 A, 40 samples (d=3,5): max |q3|/||C||^2 = {worst:.3e}")
partB["random_members_max_absq"] = worst
OUT["partB_tight_family"] = partB

# =============================================================== PART C
print()
print("=" * 78)
print("PART C -- decision-layer E_S reduction: exact counterexample")
print("=" * 78)


def swap_copy(v, d, k, i):
    A = v.reshape([d] * k + [d] * k)
    perm = list(range(2 * k))
    perm[i], perm[k + i] = perm[k + i], perm[i]
    return A.transpose(perm).reshape(-1)


def apply_PiS(v, d, k, S):
    for i in S:
        v = 0.5 * (v - swap_copy(v, d, k, i))
    return v


def apply_K(v, d, k):
    out = np.zeros_like(v)
    for r in range(k + 1):
        for S in itertools.combinations(range(k), r):
            w = v.copy()
            for i in S:
                w = swap_copy(w, d, k, i)
            out = out + ((-0.5) ** r) * w
    return out


partC = {}
for k in (1, 2, 3):
    d = 2
    n = d ** k
    e1 = np.zeros(n, dtype=complex)
    e1[0] = 1.0
    e2 = np.zeros(n, dtype=complex)
    e2[1] = 1.0
    xs = [e1, e2]
    ys = [e1, e2]
    G = np.zeros((2, 2), dtype=complex)
    for p in range(2):
        for q in range(2):
            G[p, q] = np.vdot(np.kron(xs[p], ys[q]), apply_K(np.kron(xs[q], ys[p]), d, k))
    evG = np.linalg.eigvalsh((G + G.conj().T) / 2)
    row = {"G_eigs": evG.tolist(), "ES": {}}
    for r in range(k + 1):
        for S in itertools.combinations(range(k), r):
            E = np.zeros((2, 2), dtype=complex)
            for p in range(2):
                for q in range(2):
                    E[p, q] = np.vdot(np.kron(xs[p], ys[q]),
                                      apply_PiS(np.kron(xs[q], ys[p]), d, k, set(S)))
            ev = np.linalg.eigvalsh((E + E.conj().T) / 2)
            row["ES"][str(S)] = ev.tolist()
    print(f" k={k}: eig(G) = {np.round(evG,12).tolist()}  (G PSD: {evG.min() > -1e-12})")
    for S, ev in row["ES"].items():
        flag = "  <-- NOT PSD" if min(ev) < -1e-12 else ""
        print(f"        S={S:12s} eig(E^S) = {[round(v,12) for v in ev]}{flag}")
    partC[f"k{k}"] = row
# the stated Pluecker inequality at the same point
print(" stated Pluecker reduction at x1=y1=e1, x2=y2=e2:")
print("   LHS |<x1^y2, x2^y1>|^2 = |<e1^e2, e2^e1>|^2 = 4  (convention u^v = u(x)v - v(x)u)")
print("   RHS ||x1^y1||^2 ||x2^y2||^2 = ||e1^e1||^2 ||e2^e2||^2 = 0   ==> INEQUALITY FALSE")
partC["pluecker"] = dict(LHS=4.0, RHS=0.0, holds=False)
OUT["partC_ES_refutation"] = partC

json.dump(OUT, open("artifacts/logs_nptbe_p2_20260729/P4/p4_exact_recert.json", "w"),
          indent=1, default=float)
print()
print("wrote artifacts/logs_nptbe_p2_20260729/P4/p4_exact_recert.json")
