"""R7 reviewer script (independent): claim 7 -- corroboration of the P3 degeneracy-variety
evidence, by my own unconstrained hunt.

Degeneracy of Psi (m_B >= 1) is equivalent (own derivation, claim 2) to
rank U(M) <= 8, U(M) = [ vec(Ahat_a M Ahat_b^T) ]_{a,b}  (9 x 16, x-FREE).
So I minimise sigma_9(U)/sigma_1(U) over all of C^{3x3} from random starts and, at each
converged point, read the annihilator B (the left null vector of U, i.e. the kernel of U^dag,
viewed as a 3x3 matrix) and test the P3 prediction: B is RANK ONE, B = u v^T with
u^T u = v^T v = 0.  (Theorem 3.3 of the package says P3 = {v a^T + y u^T : u,v isotropic};
its annihilator is u v^T, and the pairing is symmetric, so a degenerate M outside P3 would
show up as an annihilator that is not rank-one-with-isotropic-factors.)
"""
import json

import numpy as np
from scipy.optimize import minimize

EPS = np.array([[[int((i - j) * (j - k) * (k - i)) // 2 if len({i, j, k}) == 3 else 0
                  for k in range(3)] for j in range(3)] for i in range(3)], dtype=float)
Ahat = [np.eye(3)] + [EPS[i] for i in range(3)]


def U_of(M):
    return np.stack([(Ahat[a] @ M @ Ahat[b].T).reshape(9) for a in range(4) for b in range(4)], axis=1)


def obj(p):
    M = (p[:9] + 1j * p[9:]).reshape(3, 3)
    n = np.linalg.norm(M)
    if n < 1e-12:
        return 1.0
    s = np.linalg.svd(U_of(M / n), compute_uv=False)
    return float(s[8] / s[0])


rng = np.random.default_rng(30072026)
rows = []
for t in range(30):
    p0 = rng.normal(size=18)
    res = minimize(obj, p0, method="L-BFGS-B",
                   options={"maxiter": 4000, "ftol": 1e-18, "gtol": 1e-14})
    M = (res.x[:9] + 1j * res.x[9:]).reshape(3, 3)
    M /= np.linalg.norm(M)
    U = U_of(M)
    su = np.linalg.svd(U, compute_uv=False)
    # annihilator: left null vector of U  (kernel of U^dag)
    Ub, sb, Vb = np.linalg.svd(U)
    Bvec = Ub[:, 8]
    B = Bvec.reshape(3, 3)
    sB = np.linalg.svd(B, compute_uv=False)
    if sB[1] / sB[0] < 1e-6:                      # rank one: B = u v^T
        uu, ss, vv = np.linalg.svd(B)
        u = uu[:, 0]
        v = vv.conj()[0, :]
        isoU = abs(u @ u)
        isoV = abs(v @ v)
    else:
        isoU = isoV = None
    rows.append({"trial": t, "sigma9_over_sigma1_of_U": float(su[8] / su[0]),
                 "annihilator_rank1_ratio": float(sB[1] / sB[0]),
                 "|u^T u|": (float(isoU) if isoU is not None else None),
                 "|v^T v|": (float(isoV) if isoV is not None else None),
                 "in_P3": bool(sB[1] / sB[0] < 1e-6 and isoU is not None
                               and isoU < 1e-6 and isoV < 1e-6)})

conv = [r for r in rows if r["sigma9_over_sigma1_of_U"] < 1e-7]
out = {"n_trials": len(rows), "n_converged_to_degeneracy(sigma_ratio<1e-7)": len(conv),
       "n_converged_and_in_P3": sum(1 for r in conv if r["in_P3"]),
       "rows": rows}
print(json.dumps(out, indent=1))
with open("artifacts/logs_whgap_p13b_20260730/r7_variety.json", "w", newline="\n") as fh:
    json.dump(out, fh, indent=1)
