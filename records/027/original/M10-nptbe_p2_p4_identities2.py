"""P4 review -- reviewer's own in-session check of every displayed identity.

Coded from the frozen definitions only (see P4_INDEPENDENT_DERIVATION_PRE_READ.md
for the hand derivations, written before any W2/W3 derivation was read).

  A   q_k(C) = sum_{p,q} G_pq,  G_pq = <x_p (x) y_q, K (x_q (x) y_p)>, K = ox(I-F_i/2)
  A'  the partial-TRANSPOSE reading of T_S collapses to 2^{-k}||C||^2 (type flag)
  B   block recursion   q_k(C) = sum_{a,b} q_{k-1}(C_ab) - (1/2) q_{k-1}(tr_i C)
  C   pinch identity    q_k(C) - q_k(E_i C) = sum_{a != b} q_{k-1}(C_ab)
  D   budget identity, {Pi,Pi'} 2-block reading
  D'  budget identity, rank-1-pinching reading of the H_i term (expected WRONG)
  E   cross-lemma equivalence
  F   A-factorization  q_k(C) = <C, ox_i (1 - (d/2) P_i) C>
  G   K = 2^{-k} sum_S 2^{|S|} Pi_S
  H   K_a F = a^k K_{1/a}
  I   complementation  <T_S(uv*),T_S(st*)> = <T_{S^c}(tv*),T_{S^c}(su*)>
"""
import itertools
import json

import numpy as np

rng = np.random.default_rng(880729)


def ptrace(C, d, k, S):
    T = C.reshape([d] * k + [d] * k)
    lab = list(range(2 * k))
    for i in S:
        lab[k + i] = lab[i]
    out = [i for i in range(k) if i not in S] + [k + i for i in range(k) if i not in S]
    T = np.einsum(T, lab, out)
    m = d ** (k - len(S))
    return T.reshape(m, m)


def ptranspose(C, d, k, S):
    T = C.reshape([d] * k + [d] * k)
    perm = list(range(2 * k))
    for i in S:
        perm[i], perm[k + i] = perm[k + i], perm[i]
    return T.transpose(perm).reshape(d ** k, d ** k)


def Q(A, B, d, k):
    """polarised form Q_k(A,B) = sum_S (-1/2)^{|S|} <tr_S A, tr_S B>_HS."""
    tot = 0.0 + 0j
    for r in range(k + 1):
        for S in itertools.combinations(range(k), r):
            tot += ((-0.5) ** r) * np.vdot(ptrace(A, d, k, set(S)), ptrace(B, d, k, set(S)))
    return tot


def qk(C, d, k):
    return float(Q(C, C, d, k).real)


def qk_transpose_reading(C, d, k):
    tot = 0.0
    for r in range(k + 1):
        for S in itertools.combinations(range(k), r):
            T = ptranspose(C, d, k, set(S))
            tot += ((-0.5) ** r) * float(np.vdot(T, T).real)
    return tot


def swap_i(v, d, k, i):
    A = v.reshape([d] * k + [d] * k)
    p = list(range(2 * k))
    p[i], p[k + i] = p[k + i], p[i]
    return A.transpose(p).reshape(-1)


def applyK(v, d, k, a=-0.5):
    out = np.zeros_like(v)
    for r in range(k + 1):
        for S in itertools.combinations(range(k), r):
            w = v.copy()
            for i in S:
                w = swap_i(w, d, k, i)
            out = out + (a ** r) * w
    return out


def blocks(C, d, k, i, basis=None):
    """C_ab = <a|_i C |b>_i as operators on (C^d)^{ox(k-1)}."""
    if basis is None:
        basis = np.eye(d, dtype=complex)
    T = C.reshape([d] * k + [d] * k)
    T = np.moveaxis(T, [i, k + i], [0, 1])
    out = {}
    m = d ** (k - 1)
    for a in range(d):
        for b in range(d):
            blk = np.einsum("i,j,ij...->...", basis[:, a].conj(), basis[:, b], T)
            out[(a, b)] = blk.reshape(m, m)
    return out


def corner(C, d, k, i, P):
    """apply projector P on copy i from both sides (or P,Pp)."""
    op = np.eye(1, dtype=complex)
    mats = [np.eye(d, dtype=complex)] * k
    mats[i] = P
    M = mats[0]
    for j in range(1, k):
        M = np.kron(M, mats[j])
    return M


res = {}
worst = {kk: 0.0 for kk in "A A' B C D D' E F G H I".split()}
cases = [(2, 2), (3, 2), (2, 3), (3, 3), (4, 3), (2, 4), (3, 4)]
for d, k in cases:
    n = d ** k
    for trial in range(3):
        for real in (False, True):
            def rv():
                v = rng.normal(size=n)
                return v.astype(complex) if real else v + 1j * rng.normal(size=n)
            xs = [rv(), rv()]
            ys = [rv(), rv()]
            C = np.outer(xs[0], ys[0].conj()) + np.outer(xs[1], ys[1].conj())
            nrm = float(np.vdot(C, C).real)
            q = qk(C, d, k)
            # A
            G = np.zeros((2, 2), dtype=complex)
            for p in range(2):
                for qq in range(2):
                    G[p, qq] = np.vdot(np.kron(xs[p], ys[qq]),
                                       applyK(np.kron(xs[qq], ys[p]), d, k))
            worst["A"] = max(worst["A"], abs(q - np.sum(G).real) / nrm)
            # A'
            worst["A'"] = max(worst["A'"],
                              abs(qk_transpose_reading(C, d, k) - (0.5 ** k) * nrm) / nrm)
            # B, C
            i = trial % k
            blk = blocks(C, d, k, i)
            rhs = sum(qk(blk[(a, b)], d, k - 1) for a in range(d) for b in range(d)) \
                - 0.5 * qk(ptrace(C, d, k, {i}), d, k - 1)
            worst["B"] = max(worst["B"], abs(q - rhs) / nrm)
            Ei = np.zeros_like(C)
            for a in range(d):
                Pa = np.zeros((d, d), dtype=complex)
                Pa[a, a] = 1.0
                M = corner(C, d, k, i, Pa)
                Ei = Ei + M @ C @ M
            off = sum(qk(blk[(a, b)], d, k - 1) for a in range(d) for b in range(d) if a != b)
            worst["C"] = max(worst["C"], abs((q - qk(Ei, d, k)) - off) / nrm)
            # D, D'
            P = np.zeros((d, d), dtype=complex)
            P[0, 0] = 1.0
            if d > 1:
                P[1, 1] = 1.0
            Pp = np.eye(d, dtype=complex) - P
            MP = corner(C, d, k, i, P)
            MQ = corner(C, d, k, i, Pp)
            C11 = MP @ C @ MP
            C22 = MQ @ C @ MQ
            C12 = MP @ C @ MQ
            C21 = MQ @ C @ MP
            cross = float(np.real(Q(ptrace(C11, d, k, {i}), ptrace(C22, d, k, {i}), d, k - 1)))
            rhsD = qk(C11, d, k) + qk(C22, d, k) + qk(C12, d, k) + qk(C21, d, k) - cross
            worst["D"] = max(worst["D"], abs(q - rhsD) / nrm)
            rhsDp = qk(C11, d, k) + qk(C22, d, k) + off - cross
            worst["D'"] = max(worst["D'"], abs(q - rhsDp) / nrm)
            # E
            Z = ptrace(C11, d, k, {i})
            TiC = ptrace(C, d, k, {i})
            lhs = qk(Z, d, k - 1) + qk(TiC - Z, d, k - 1) - qk(TiC, d, k - 1)
            # q(Z) + q(TiC-Z) - q(TiC) == -2 Re Q_{k-1}(Z, TiC-Z), and TiC - Z = tr_i C22
            # so Q_{k-1}(Z, TiC-Z) = Q_{k-1}(tr_i C11, tr_i C22) = cross.
            worst["E"] = max(worst["E"], abs(lhs + 2 * cross) / nrm)
            # F  A-factorization
            X = C.copy()
            for j in range(k):
                Tj = ptrace(X, d, k, {j})
                # reinsert identity on copy j
                Tt = Tj.reshape([d] * (k - 1) + [d] * (k - 1))
                Tt = np.tensordot(Tt, np.eye(d, dtype=complex), axes=0)
                nr = k - 1
                rows = list(range(nr))
                cols = list(range(nr, 2 * nr))
                a_, b_ = 2 * nr, 2 * nr + 1
                Tt = Tt.transpose(rows[:j] + [a_] + rows[j:] + cols[:j] + [b_] + cols[j:])
                Pj = Tt.reshape(n, n) / d
                X = X - (d / 2.0) * Pj
            worst["F"] = max(worst["F"], abs(float(np.vdot(C, X).real) - q) / nrm)
            # H
            a = 0.31 - 0.17j
            v = rng.normal(size=n * n) + 1j * rng.normal(size=n * n)
            fv = v.copy()
            for j in range(k):
                fv = swap_i(fv, d, k, j)
            L = applyK(fv, d, k, a)
            R = (a ** k) * applyK(v, d, k, 1.0 / a)
            worst["H"] = max(worst["H"], np.max(np.abs(L - R)) / np.max(np.abs(R)))
            # I
            u, vv, s, t = rv(), rv(), rv(), rv()
            for r in range(k + 1):
                for S in itertools.combinations(range(k), r):
                    Ss = set(S)
                    Sc = set(range(k)) - Ss
                    L1 = np.vdot(ptrace(np.outer(u, vv.conj()), d, k, Ss),
                                 ptrace(np.outer(s, t.conj()), d, k, Ss))
                    R1 = np.vdot(ptrace(np.outer(t, vv.conj()), d, k, Sc),
                                 ptrace(np.outer(s, u.conj()), d, k, Sc))
                    sc = max(1.0, abs(L1))
                    worst["I"] = max(worst["I"], abs(L1 - R1) / sc)

# G: K = 2^{-k} sum_S 2^{|S|} Pi_S  (exact matrix comparison, small cases)
gworst = 0.0
for d, k in [(2, 1), (2, 2), (3, 2), (2, 3)]:
    n = d ** k
    dim = n * n
    K = np.zeros((dim, dim), dtype=complex)
    Alt = np.zeros((dim, dim), dtype=complex)
    for j in range(dim):
        e = np.zeros(dim, dtype=complex)
        e[j] = 1.0
        K[:, j] = applyK(e, d, k)
        acc = np.zeros(dim, dtype=complex)
        for r in range(k + 1):
            for S in itertools.combinations(range(k), r):
                w = e.copy()
                for i in S:
                    w = 0.5 * (w - swap_i(w, d, k, i))
                acc = acc + (2.0 ** r) * w
        Alt[:, j] = acc * (2.0 ** (-k))
    gworst = max(gworst, float(np.max(np.abs(K - Alt))))
    ev = np.linalg.eigvalsh((K + K.conj().T) / 2)
    res[f"K_spectrum_d{d}_k{k}"] = [float(ev.min()), float(ev.max())]
worst["G"] = gworst

print("reviewer's own identity checks -- max relative error over")
print(f"  (d,k) in {cases}, 3 trials, real AND complex")
for kk in ["A", "A'", "B", "C", "D", "D'", "E", "F", "G", "H", "I"]:
    note = ""
    if kk == "A'":
        note = "   <- partial-TRANSPOSE reading collapses to 2^-k||C||^2 (type flag)"
    if kk == "D'":
        note = "   <- rank-1-pinching reading of H_i: WRONG, as pre-flagged"
    print(f"  {kk:3s} {worst[kk]:.3e}{note}")
res["worst"] = {k: float(v) for k, v in worst.items()}
json.dump(res, open("artifacts/logs_nptbe_p2_20260729/P4/p4_identities2.json", "w"), indent=1)
print("\nK spectra (min,max):")
for k, v in res.items():
    if k.startswith("K_spectrum"):
        print(" ", k, [round(x, 12) for x in v])
