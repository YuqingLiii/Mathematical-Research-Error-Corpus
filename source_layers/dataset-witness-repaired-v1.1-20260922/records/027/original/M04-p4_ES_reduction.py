"""P4: test the decision-layer 'E_S reduction' note (unreviewed) that P1 is told to screen first:
   K = 2^-k sum_S 2^{|S|} Pi_S with POSITIVE coefficients, so M1 would follow if every
   elementary exchange matrix E^S_pq = <x_p ox y_q, Pi_S (x_q ox y_p)> were PSD at r=2.
Explicit candidate counterexample: x1 = y1 = e1, x2 = y2 = e2 (tensored with a common spectator)."""
import sys, itertools, json
import numpy as np
sys.path.insert(0, 'tools')
from nptbe_p2_p4_review import subsets

rng = np.random.default_rng(7)


def Pi_S_apply(W, k, S):
    """antisymmetriser on copies in S, acting on the tensor W[a_1..a_k, b_1..b_k] in H ox H"""
    Z = W.copy()
    for s in S:
        ax = list(range(2 * k)); ax[s], ax[k + s] = ax[k + s], ax[s]
        Z = 0.5 * (Z - np.transpose(Z, ax))
    return Z


def E_S(xs, ys, d, k, S):
    E = np.zeros((2, 2), complex)
    for p in range(2):
        for q in range(2):
            W = np.tensordot(xs[q].reshape((d,) * k), ys[p].reshape((d,) * k), 0)
            L = np.tensordot(xs[p].reshape((d,) * k), ys[q].reshape((d,) * k), 0)
            E[p, q] = np.vdot(L, Pi_S_apply(W, k, S))
    return E


def Gmat_from_ES(xs, ys, d, k):
    """K = 2^-k sum_S 2^{|S|} Pi_S  ->  G = 2^-k sum_S 2^{|S|} E^S ; cross-check vs direct G"""
    G = np.zeros((2, 2), complex)
    for S in subsets(k):
        G += 2.0 ** len(S) * E_S(xs, ys, d, k, S)
    return G / 2 ** k


def Gdirect(xs, ys, d, k):
    G = np.zeros((2, 2), complex)
    for p in range(2):
        for q in range(2):
            W = np.tensordot(xs[q].reshape((d,) * k), ys[p].reshape((d,) * k), 0)
            L = np.tensordot(xs[p].reshape((d,) * k), ys[q].reshape((d,) * k), 0)
            tot = 0j
            for S in subsets(k):
                ax = list(range(2 * k))
                for s in S:
                    ax[s], ax[k + s] = ax[k + s], ax[s]
                tot += (-0.5) ** len(S) * np.vdot(L, np.transpose(W, ax))
            G[p, q] = tot
    return G


out = []
# (i) explicit analytic counterexample, lifted to k = 1,2,3 with a product spectator
for k in [1, 2, 3]:
    d = 2
    e1 = np.zeros(d); e1[0] = 1
    e2 = np.zeros(d); e2[1] = 1
    c = np.ones(d) / np.sqrt(d)
    def lift(v):
        w = v
        for _ in range(k - 1):
            w = np.kron(w, c)
        return w.astype(complex)
    xs = [lift(e1), lift(e2)]; ys = [lift(e1), lift(e2)]
    S = (0,)
    E = E_S(xs, ys, d, k, S)
    ev = np.linalg.eigvalsh((E + E.conj().T) / 2)
    G = Gdirect(xs, ys, d, k)
    rec = {'case': 'x1=y1=e1, x2=y2=e2 (+ spectator)', 'k': k, 'd': d, 'S': list(S),
           'E_S': [[complex(E[i, j]).real for j in range(2)] for i in range(2)],
           'eig_E_S': [float(v) for v in ev], 'E_S_is_PSD': bool(ev[0] > -1e-12),
           'G_direct_eig': [float(v) for v in np.linalg.eigvalsh((G + G.conj().T) / 2)],
           'G_is_PSD': bool(np.linalg.eigvalsh((G + G.conj().T) / 2)[0] > -1e-12),
           'reassembly_err': float(np.linalg.norm(Gmat_from_ES(xs, ys, d, k) - G))}
    print(json.dumps(rec), flush=True)
    out.append(rec)

# (ii) random screen of every E^S at r=2
print('--- random screen: min eig of E^S over random vectors ---')
for (d, k) in [(2, 2), (3, 2), (2, 3), (3, 3)]:
    n = d ** k
    worst = {}
    for _ in range(150):
        xs = [rng.standard_normal(n) + 1j * rng.standard_normal(n) for _ in range(2)]
        ys = [rng.standard_normal(n) + 1j * rng.standard_normal(n) for _ in range(2)]
        nrm = max(np.linalg.norm(v) for v in xs + ys) ** 4
        for S in subsets(k):
            E = E_S(xs, ys, d, k, S)
            m = float(np.linalg.eigvalsh((E + E.conj().T) / 2)[0]) / nrm
            worst[str(S)] = min(worst.get(str(S), 1e9), m)
    rec = {'d': d, 'k': k, 'min_eig_E_S_normalised': worst,
           'n_S_with_negative_eig': int(sum(1 for v in worst.values() if v < -1e-9)),
           'n_S_total': 2 ** k}
    print(json.dumps(rec), flush=True)
    out.append(rec)
json.dump(out, open('artifacts/logs_nptbe_p2_20260729/P4/p4_ES_reduction.json', 'w'), indent=1)
