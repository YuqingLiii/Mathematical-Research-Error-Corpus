"""WHGAP P13-B, S3: numeric sweep of lam_max(D_Psi) on the 2-copy degeneracy variety.

Charts swept (each is degenerate BY CONSTRUCTION, so the kernel projector is stable):
  F1  full P3 chart      M = u0 a^T + y u0^T ,  a,y in C^3        (12 real params)
        - u0 = (e1 + i e2)/sqrt2.  Every M with m_B >= 1 that the unconstrained hunt
          ever produced is O(3)xO(3)-equivalent to a point of this chart (see the
          artifact, S2): the annihilator is always B = u v^T with u,v isotropic, and
          real rotations move any isotropic pair to (u0,u0).
  F2  type-E chart       M = C1 diag(1,1,0) C2 , C_i complex special orthogonal (12)
  F3  product chart      M = y u0^T                                (6)
  F4  unconstrained control  M in C^{3x3}                          (18)  [expects 0]
Rank discipline (pre-registered): a kernel dimension is accepted only when the smallest
kept eigenvalue exceeds 1e6 times the accepted zero-cluster magnitude; otherwise the
point is recorded rank-ambiguous and EXCLUDED (append-only list in the output json).

Decision gates: G+ if any strip point gives lam_max > 1e-6 at a rank-unambiguous point.
Positive controls at x = 7/20 and 39/100 (below the conjectured onset 2/5) verify the
scanner can find witnesses when they exist.
"""
import json
import os
import sys
import time

for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
           'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ.setdefault(_v, '1')          # machine etiquette: single-threaded BLAS

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

sys.path.insert(0, __file__.rsplit('\\', 1)[0].replace('\\', '/'))
from whgap_p13b_core import (normalize, weight_operator_rf, lam_max, span_matrix, vec,
                             channel2)

weight_operator_fast = weight_operator_rf      # radical-free evaluator (3-way cross-checked)

U0 = np.array([1, 1j, 0]) / np.sqrt(2)
STRIP = [0.40, 0.41, 0.42, 0.43, 0.45, 0.47, 0.49]
CONTROL = [0.35, 0.39]


def cso3(w):
    Aw = np.array([[0, w[2], -w[1]], [-w[2], 0, w[0]], [w[1], -w[0], 0]])
    return expm(Aw)


def chart_F1(p):
    a = p[0:3] + 1j * p[3:6]
    y = p[6:9] + 1j * p[9:12]
    return normalize(np.outer(U0, a) + np.outer(y, U0))


def chart_F2(p):
    C1 = cso3(p[0:3] + 1j * p[3:6])
    C2 = cso3(p[6:9] + 1j * p[9:12])
    return normalize(C1 @ np.diag([1.0, 1.0, 0.0]) @ C2)


def chart_F3(p):
    y = p[0:3] + 1j * p[3:6]
    return normalize(np.outer(y, U0))


def chart_F4(p):
    return normalize((p[:9] + 1j * p[9:18]).reshape(3, 3))


CHARTS = dict(F1=(chart_F1, 12), F2=(chart_F2, 12), F3=(chart_F3, 6), F4=(chart_F4, 18))


def evaluate(x, M, gap_factor=1e6):
    res = weight_operator_fast(x, M, gap_factor)
    lm = lam_max(res['D'])
    return lm, res


def objective(p, x, chart):
    M = chart(p)
    try:
        lm, res = evaluate(x, M)
    except np.linalg.LinAlgError:
        return 0.0
    if not (res['okB'] and res['okE']):
        return 0.0            # rank-ambiguous: do not let the optimiser exploit it
    return -lm


def sweep(name, chart, npar, xs, nrestart=100, seed=17, nsample=1500, maxfev=400):
    """nrestart genuine local optimisations (Nelder-Mead), seeded by the best of a
    random pre-sample plus fresh random starts; every accepted point must pass the
    pre-registered rank discipline."""
    rng = np.random.default_rng(seed)
    rows = []
    for xv in xs:
        best = (-np.inf, None)
        amb = 0
        t0 = time.time()
        # random pre-sample (cheap) -> seeds
        pre = []
        for i in range(nsample):
            p = rng.normal(size=npar)
            pre.append((-objective(p, xv, chart), p))
        pre.sort(key=lambda z: -z[0])
        seeds = [z[1] for z in pre[:nrestart // 2]] + \
                [rng.normal(size=npar) for _ in range(nrestart - nrestart // 2)]
        for p0 in seeds:
            res = minimize(objective, p0, args=(xv, chart), method='Nelder-Mead',
                           options=dict(maxfev=maxfev, xatol=1e-10, fatol=1e-14))
            M = chart(res.x)
            lm, r = evaluate(xv, M)
            if not (r['okB'] and r['okE']):
                amb += 1
                continue
            if lm > best[0]:
                best = (lm, M.copy(), r['mB'], r['mE'])
        rows.append(dict(chart=name, x=xv, nrestart=nrestart, best=float(best[0]),
                         mB=(best[2] if best[1] is not None else None),
                         mE=(best[3] if best[1] is not None else None),
                         ambiguous_excluded=amb, seconds=round(time.time() - t0, 1),
                         Mbest=(None if best[1] is None else
                                [[str(z) for z in row] for row in best[1]])))
        print('%-3s x=%.3f  best lam_max = %+.3e  (mB=%s, ambiguous excluded %d, %.0fs)'
              % (name, xv, best[0], rows[-1]['mB'], amb, rows[-1]['seconds']), flush=True)
    return rows


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    nres = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    out = dict(strip=STRIP, control=CONTROL, rows=[])
    todo = ['F1', 'F2', 'F3', 'F4'] if which == 'all' else [which]
    for nm in todo:
        chart, npar = CHARTS[nm]
        nr = nres if nm != 'F4' else max(40, nres // 2)
        xs_strip = STRIP if nm != 'F4' else [0.40, 0.45, 0.49]
        print('--- chart %s (%d params): positive controls' % (nm, npar), flush=True)
        out['rows'] += sweep(nm, chart, npar, CONTROL, nrestart=nr, seed=101,
                             nsample=800, maxfev=250)
        print('--- chart %s: strip' % nm, flush=True)
        out['rows'] += sweep(nm, chart, npar, xs_strip, nrestart=nr, seed=202,
                             nsample=800, maxfev=250)
    tag = which if which != 'all' else 'all'
    with open('artifacts/logs_whgap_p13b_20260730/sweep_%s.json' % tag, 'w', newline='\n') as f:
        json.dump(out, f, indent=1)
    strip_best = max([r['best'] for r in out['rows'] if r['x'] >= 0.40], default=None)
    ctrl_best = max([r['best'] for r in out['rows'] if r['x'] < 0.40], default=None)
    print('\nBEST over strip points: %s ; best over controls (x<2/5): %s' % (strip_best, ctrl_best))


if __name__ == '__main__':
    main()
