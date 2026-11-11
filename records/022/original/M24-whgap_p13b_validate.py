"""WHGAP P13-B: post-hoc validation of every sweep incumbent whose lam_max exceeds 1e-6.

Two independent filters are applied to the stored best-M of each such row:
  (1) the rank discipline INCLUDING the conditioning criterion (ii) of
      whgap_p13b_core.kernel_projector (added mid-run, artifact section 8.1);
  (2) the DEFINITIONAL slope gate: does the raw coherent information Ic_2(rho_eps),
      computed from channel/complement entropies with no reference to D_Psi, really have
      the predicted eps log(1/eps) slope?  (validate_slope)

A candidate that fails either filter is a scanner artifact and is reported as such; a
candidate that passes both is a genuine first-order witness at that x (which, in the strip,
would be gate G+).
"""
import glob
import json
import os
import sys

for _v in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ.setdefault(_v, '1')

import numpy as np

sys.path.insert(0, __file__.rsplit('\\', 1)[0].replace('\\', '/'))
from whgap_p13b_core import weight_operator_rf, lam_max, validate_slope, normalize

OUT = []


def check(row):
    M = np.array([[complex(z) for z in r] for r in row['Mbest']])
    x = row['x']
    res = weight_operator_rf(x, M)
    D = res['D']
    lm = lam_max(D)
    w, V = np.linalg.eigh((D + D.conj().T) / 2)
    phi = np.outer(V[:, -1], V[:, -1].conj())
    ok_slope, pred, ratios = validate_slope(x, M, phi, D)
    rec = dict(chart=row['chart'], x=x, reported=row['best'], recomputed=lm,
               rank_discipline_ok=bool(res['okB'] and res['okE']),
               cond_ratio_B=res['diagB']['cond_ratio'], cond_ratio_E=res['diagE']['cond_ratio'],
               mB=res['mB'], mE=res['mE'], slope_gate_ok=ok_slope,
               predicted_slope=pred, measured_ratios=ratios,
               verdict=('GENUINE' if (res['okB'] and res['okE'] and ok_slope) else 'ARTIFACT'))
    OUT.append(rec)
    print('%-3s x=%.3f reported %+.3e | rank-ok %-5s condB %.2e | slope-gate %-5s pred %+.5f '
          'measured %s -> %s'
          % (rec['chart'], x, rec['reported'], rec['rank_discipline_ok'], rec['cond_ratio_B'],
             rec['slope_gate_ok'], pred, ['%+.5f' % v for v in ratios], rec['verdict']),
          flush=True)


def main():
    files = sorted(glob.glob('artifacts/logs_whgap_p13b_20260730/sweep_*.json'))
    for f in files:
        d = json.load(open(f))
        for row in d['rows']:
            if row['best'] > 1e-6 and row['Mbest'] is not None:
                check(row)
    with open('artifacts/logs_whgap_p13b_20260730/validation.json', 'w', newline='\n') as fh:
        json.dump(OUT, fh, indent=1)
    art = [r for r in OUT if r['verdict'] == 'ARTIFACT']
    strip_genuine = [r for r in OUT if r['verdict'] == 'GENUINE' and r['x'] >= 0.4]
    print('\n%d candidates checked, %d ARTIFACT, %d GENUINE; genuine IN THE STRIP: %d'
          % (len(OUT), len(art), len(OUT) - len(art), len(strip_genuine)))


if __name__ == '__main__':
    main()
