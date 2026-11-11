"""P4 -- fast decisive check: cross(i,Pi) on the tight family C = A (x) P2."""
import itertools
import json
import math

import numpy as np

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
    return float(np.real(Q(ptrace(MP @ C @ MP, d, k, {i}),
                           ptrace(MQ @ C @ MQ, d, k, {i}), d, k - 1)))


def rand_proj(d, r=2):
    M = rng.normal(size=(d, r)) + 1j * rng.normal(size=(d, r))
    Qm, _ = np.linalg.qr(M)
    return Qm @ Qm.conj().T


OUT = {}
k = 3
print("cross(i,Pi) on the tight family  C = |Phi><Phi|_{12} (x) P2_{3}   (k=3)")
print("=" * 76)
for d in (3, 4, 5, 6):
    Phi = np.zeros(d * d, dtype=complex)
    for j in range(d):
        Phi[j * d + j] = 1.0 / math.sqrt(d)
    C = np.kron(np.outer(Phi, Phi.conj()),
                np.diag([1.0, 1.0] + [0.0] * (d - 2)).astype(complex))
    P2 = np.diag([1.0, 1.0] + [0.0] * (d - 2)).astype(complex)
    nat = [cross_val(C, d, k, 2, P2), cross_val(C, d, k, 0, P2), cross_val(C, d, k, 1, P2)]
    w = 0.0
    for i in range(3):
        for _ in range(40):
            w = max(w, abs(cross_val(C, d, k, i, rand_proj(d))))
    print(f" d={d}: cross at Pi=P2 on (copy3, copy1, copy2) = "
          f"{['%+.2e' % v for v in nat]};  max|cross| over 120 RANDOM Pi = {w:.3e}")
    OUT[f"d{d}"] = dict(natural=nat, random_max_abs=w)

print()
print("control -- random rank-2 C: cross for 120 random Pi per copy")
for d in (3, 4):
    n = d ** k
    v = [rng.normal(size=n) + 1j * rng.normal(size=n) for _ in range(4)]
    C = np.outer(v[0], v[1].conj()) + np.outer(v[2], v[3].conj())
    N = float(np.vdot(C, C).real)
    per = []
    for i in range(3):
        vals = [cross_val(C, d, k, i, rand_proj(d)) / N for _ in range(120)]
        per.append((min(vals), max(vals)))
    print(f" d={d}: (min,max) cross/||C||^2 per copy = "
          f"{[('%+.3e' % a, '%+.3e' % b) for a, b in per]}")
    OUT[f"control_d{d}"] = per

json.dump(OUT, open("artifacts/logs_nptbe_p2_20260729/P4/p4_cross_fast.json", "w"),
          indent=1, default=float)
print("\nwrote artifacts/logs_nptbe_p2_20260729/P4/p4_cross_fast.json")
