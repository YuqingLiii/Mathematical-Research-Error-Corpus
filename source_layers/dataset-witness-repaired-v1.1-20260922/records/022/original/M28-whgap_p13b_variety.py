"""WHGAP P13-B, S2: the 2-copy degeneracy variety.

  r(M) := rank Lambda^(2)(P_Psi) = dim span{ K_a M K_b^T } = dim span{ a M b : a,b in L },
  L := span{1, A_1, A_2, A_3}   (4-dim; K_a are nonzero multiples of these for x in (0,1)),
so r(M) and hence m_B = 9 - r(M) are INDEPENDENT of x on (0,1).

Part 1 numerically hunts the variety {r(M) <= 8} by minimising the 9th eigenvalue of
Lambda^(2)(P_Psi) and classifies the minimisers by O(3)xO(3) invariants.
Part 2 tests the two analytic strata (isotropic-factor products; the "diag(1,1,0) type").
Part 3 tests invariance of r under complex-orthogonal equivalence M -> O_1 M O_2.
"""
import json
import sys

import numpy as np
from scipy.optimize import minimize

sys.path.insert(0, __file__.rsplit('\\', 1)[0].replace('\\', '/'))
from whgap_p13b_core import channel2, vec, normalize, span_matrix, lam_max, weight_operator_fast

X0 = 9 / 20


def pack(M):
    return np.concatenate([np.real(M).ravel(), np.imag(M).ravel()])


def unpack(p):
    M = (p[:9] + 1j * p[9:]).reshape(3, 3)
    return normalize(M)


def lam9(M, x=X0):
    Psi = vec(M)
    G = channel2(x, np.outer(Psi, Psi.conj()))
    w = np.sort(np.real(np.linalg.eigvalsh(G)))
    return w[0] / max(w[-1], 1e-300)


def rank_of(M, x=X0):
    sv = np.linalg.svd(span_matrix(x, M), compute_uv=False)
    return int(np.sum(sv > 1e-9 * sv[0])), sv


def invariants(M):
    sv = np.linalg.svd(M, compute_uv=False)
    adj = np.array([[np.linalg.det(np.delete(np.delete(M, j, 0), i, 1)) * (-1) ** (i + j)
                     for j in range(3)] for i in range(3)])
    return dict(trMMT=complex(np.trace(M @ M.T)), det=complex(np.linalg.det(M)),
                sv=sv.tolist(), adjnorm=float(np.linalg.norm(adj)),
                MMT_idem=float(np.linalg.norm((M @ M.T) @ (M @ M.T) - np.trace(M @ M.T) / 2 * (M @ M.T))))


def cplx_so3(rng, scale=1.0):
    """random complex special-orthogonal 3x3 via exp of complex antisymmetric"""
    w = (rng.normal(size=3) + 1j * rng.normal(size=3)) * scale
    Aw = np.array([[0, w[2], -w[1]], [-w[2], 0, w[0]], [w[1], -w[0], 0]])
    from scipy.linalg import expm
    return expm(Aw)


def hunt(nrestart=120, seed=5):
    rng = np.random.default_rng(seed)
    found = []
    for i in range(nrestart):
        p0 = rng.normal(size=18)
        res = minimize(lambda p: lam9(unpack(p)), p0, method='L-BFGS-B',
                       options=dict(maxiter=4000, ftol=1e-18, gtol=1e-14))
        M = unpack(res.x)
        r, sv = rank_of(M)
        if res.fun < 1e-12:
            inv = invariants(M)
            found.append(dict(i=i, f=float(res.fun), r=r, rankM=int(np.sum(np.array(inv['sv']) > 1e-7)),
                              **{k: (str(v) if isinstance(v, complex) else v) for k, v in inv.items()}))
    return found


def main():
    out = {}
    rng = np.random.default_rng(7)

    # ---- Part 3: invariance of r under complex-orthogonal equivalence
    inv_tests = []
    base = [np.diag([1, 1, 0]) / np.sqrt(2), np.diag([1, 1j, 0]) / np.sqrt(2),
            np.eye(3) / np.sqrt(3), np.outer([1, 1j, 0], [1, 0, 0]) / np.sqrt(2)]
    for B in base:
        r0, _ = rank_of(normalize(B))
        rs = []
        for _ in range(6):
            O1, O2 = cplx_so3(rng, 0.7), cplx_so3(rng, 0.7)
            r, _ = rank_of(normalize(O1 @ B @ O2))
            rs.append(r)
        inv_tests.append(dict(r0=r0, transformed=rs, ok=all(r == r0 for r in rs)))
    out['cplx_orth_invariance'] = inv_tests
    print('complex-orthogonal invariance of r:', json.dumps(inv_tests))

    # ---- Part 1: hunt
    found = hunt()
    out['hunt'] = found
    rs = sorted(set(f['r'] for f in found))
    print('\nhunt: %d/120 restarts reached lam9 < 1e-12 ; ranks r found = %s' % (len(found), rs))
    for r in rs:
        sub = [f for f in found if f['r'] == r]
        print('  r = %d : %d hits ; example |Tr MM^T| = %s, rank M = %s, |adj M| = %.3e'
              % (r, len(sub), abs(complex(sub[0]['trMMT'])), sub[0]['rankM'], sub[0]['adjnorm']))
    out['rank_histogram'] = {str(r): sum(1 for f in found if f['r'] == r) for r in rs}

    # ---- Part 2: the two analytic strata + lam_max in the strip
    strata = []
    for tag, M in [('prod: y u^T, u isotropic', np.outer([1, 2j, 0.5], [1, 1j, 0])),
                   ('prod: u y^T, u isotropic', np.outer([1, 1j, 0], [1, 2j, 0.5])),
                   ('typeE: a diag(1,-1,0) + c(E12+E21)',
                    np.array([[0.3, 0.7 + 0.2j, 0], [0.7 + 0.2j, -0.3, 0], [0, 0, 0]])),
                   ('typeE: O1 diag(1,1,0) O2 (complex orth)',
                    cplx_so3(rng, 0.6) @ np.diag([1, 1, 0]) @ cplx_so3(rng, 0.6))]:
        M = normalize(M)
        r, _ = rank_of(M)
        row = dict(tag=tag, r=r, lam=dict())
        for x in (0.4, 0.45, 0.49, 0.55):
            res = weight_operator_fast(x, M)
            row['lam']['%.2f' % x] = dict(lam_max=lam_max(res['D']), mB=res['mB'], mE=res['mE'],
                                          okB=bool(res['okB']), okE=bool(res['okE']))
        strata.append(row)
        print('%-42s r=%d  %s' % (tag, r, json.dumps(row['lam'])))
    out['strata'] = strata

    with open('artifacts/logs_whgap_p13b_20260730/variety.json', 'w', newline='\n') as f:
        json.dump(out, f, indent=1, default=str)


if __name__ == '__main__':
    main()
