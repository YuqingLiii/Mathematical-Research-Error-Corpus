"""WHGAP P13-B: calibration + machinery gates (run FIRST, before any strip claim).

Gates
  C0  Kraus set reproduces Lambda_x entrywise; sum K^dag K = 1 ; Lambda self-adjoint (HS).
  C1  2-copy pure-input isospectrality: nonzero spectra of Lambda^(2)(P_Psi) and
      Lambda^{c(2)}(P_Psi) agree  =>  Ic_2(P_Psi) = 0 and rank_B = rank_E.
  C2  slow (matrix-unit) and fast (operator-sum) constructions of D_Psi agree; D Hermitian;
      Tr[D P_Psi] = 0.
  C3  first-order slope gate: (Ic_2(rho_eps)) / (eps log(1/eps)) -> Tr[D phi] as eps -> 0
      (independent check of the whole weight-operator machinery).
  G-cal1  at x = 7/20 the embedded n=1 witness is found: lam_max(D_Psi) >= d_1(7/20)
      for family (a) Psi = psi_0 tensor psi_0, and the psibar-slot product direction
      attains exactly d_1.
  G-cal2  at x = 11/20 nothing positive above 1e-9 over all structured families and a
      random sweep (Q = 0 is PROVED there; a positive means the scanner is defective).

Interpreter: C:[USER_HOME]/cpython3119/python.exe
"""

import json
import sys
import numpy as np

sys.path.insert(0, __file__.rsplit('\\', 1)[0].replace('\\', '/'))
from whgap_p13b_core import (A_LIST, kraus, channel2, complement2, vec, weight_operator,
                             weight_operator_fast, lam_max, Ic2, span_matrix, normalize)

RESULTS = []


def gate(name, ok, detail):
    RESULTS.append(dict(gate=name, pass_=bool(ok), detail=detail))
    print(('PASS ' if ok else 'FAIL ') + name + ' :: ' + detail)
    return ok


def lam1(x, Y):
    """single-copy channel"""
    K = kraus(x)
    return sum(k @ Y @ k.conj().T for k in K)


def d1(x):
    return (1 - x) * (2 - 5 * x) / (2 - x)


PSI0 = np.array([1, 1j, 0]) / np.sqrt(2)     # isotropic:  psi^T psi = 0
E3 = np.array([0, 0, 1.0])


# ----------------------------------------------------------------------- C0
def gate_C0():
    ok = True
    for x in (0.35, 0.45, 0.55):
        K = kraus(x)
        for _ in range(3):
            Y = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)
            lhs = sum(k @ Y @ k.conj().T for k in K)
            rhs = (1 - x) * Y + (x / 2) * (np.trace(Y) * np.eye(3) - Y.T)
            ok &= np.allclose(lhs, rhs, atol=1e-13)
        ok &= np.allclose(sum(k.conj().T @ k for k in K), np.eye(3), atol=1e-13)
        # self-adjointness of Lambda in HS inner product
        for _ in range(3):
            Y = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)
            Z = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)
            a = np.trace(Z.conj().T @ lam1(x, Y))
            b = np.trace(lam1(x, Z).conj().T @ Y)
            ok &= abs(a - b) < 1e-12
    return gate('C0', ok, 'Kraus <-> Lambda_x entrywise, TP, and HS self-adjointness at 3 x values')


# ----------------------------------------------------------------------- C1
def gate_C1(Ms, xs):
    ok = True
    worst = 0.0
    for x in xs:
        for tag, M in Ms:
            Psi = vec(normalize(M))
            P = np.outer(Psi, Psi.conj())
            wb = np.sort(np.real(np.linalg.eigvalsh(channel2(x, P))))[::-1]
            we = np.sort(np.real(np.linalg.eigvalsh(complement2(x, P))))[::-1]
            n = 9
            dd = np.max(np.abs(wb[:n] - we[:n]))
            worst = max(worst, dd)
            ok &= dd < 1e-11
    return gate('C1', ok, 'pure-input isospectrality of the two 2-copy outputs, max dev %.2e' % worst)


# ----------------------------------------------------------------------- C2
def gate_C2(Ms, xs):
    ok = True
    worst = 0.0
    worst0 = 0.0
    for x in xs:
        for tag, M in Ms:
            Mn = normalize(M)
            slow = weight_operator(x, Mn)
            fast = weight_operator_fast(x, Mn)
            dd = np.max(np.abs(slow['D'] - fast['D']))
            herm = np.max(np.abs(slow['D'] - slow['D'].conj().T))
            Psi = vec(Mn)
            t0 = abs(np.real(Psi.conj() @ slow['D'] @ Psi))
            worst = max(worst, dd, herm)
            worst0 = max(worst0, t0)
            ok &= dd < 1e-11 and herm < 1e-11 and t0 < 1e-11
            ok &= slow['mB'] == fast['mB'] and slow['mE'] == fast['mE']
            ok &= slow['rankB'] == slow['rankE']
    return gate('C2', ok, 'slow==fast, D Hermitian, Tr[D P_Psi]=0 ; worst %.2e / %.2e' % (worst, worst0))


# ----------------------------------------------------------------------- C3
def gate_C3(cases):
    """cases: list of (tag, x, M, phi). Check the eps log(1/eps) slope."""
    ok = True
    rows = []
    for tag, x, M, phi in cases:
        Mn = normalize(M)
        res = weight_operator_fast(x, Mn)
        pred = float(np.real(np.trace(res['D'] @ phi)))
        vals = []
        for eps in (1e-6, 1e-8, 1e-10, 1e-12):
            v = Ic2(x, Mn, phi, eps)
            vals.append(v / (eps * np.log(1 / eps)))
        # Richardson-free check: the sequence must approach pred (remainder is O(1/log(1/eps)))
        err = abs(vals[-1] - pred)
        trend = abs(vals[-1] - pred) < abs(vals[0] - pred) + 1e-14
        rows.append(dict(tag=tag, x=x, pred=pred, ratios=vals, err=err, trend=bool(trend)))
        ok &= (err < 0.05 * max(1.0, abs(pred))) and trend
    return gate('C3', ok, 'slope gate: ' + json.dumps(rows)), rows


# ------------------------------------------------------------------ G-cal1
def gate_cal1():
    x = 7 / 20
    M = np.outer(PSI0, PSI0)              # family (a): Psi = psi_0 tensor psi_0
    res = weight_operator_fast(x, normalize(M))
    lm = lam_max(res['D'])
    target = d1(x)
    # the embedded n=1 witness direction: phi = P_{psibar} tensor P_{psi}
    psib = PSI0.conj()
    phi = np.kron(np.outer(psib, psib.conj()), np.outer(PSI0, PSI0.conj()))
    val = float(np.real(np.trace(res['D'] @ phi)))
    ok = (lm >= target - 1e-10) and abs(val - target) < 1e-10
    return gate('G-cal1', ok,
                'x=7/20: lam_max=%.12f, d_1=%.12f, psibar-slot direction=%.12f, mB=%d, mE=%d'
                % (lm, target, val, res['mB'], res['mE']))


# ------------------------------------------------------------------ G-cal2
def gate_cal2(Ms, nrand=60, seed=11):
    x = 11 / 20
    rng = np.random.default_rng(seed)
    worst = -np.inf
    worst_tag = None
    for tag, M in Ms:
        res = weight_operator_fast(x, normalize(M))
        lm = lam_max(res['D'])
        if lm > worst:
            worst, worst_tag = lm, tag
    for i in range(nrand):
        M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
        res = weight_operator_fast(x, normalize(M))
        lm = lam_max(res['D'])
        if lm > worst:
            worst, worst_tag = lm, 'random-%d' % i
    ok = worst <= 1e-9
    return gate('G-cal2', ok, 'x=11/20: max lam_max over families+%d random = %.3e (at %s)'
                % (nrand, worst, worst_tag))


def structured_families():
    psi = PSI0
    psib = PSI0.conj()
    u_iso = np.array([1, 1j, 0]) / np.sqrt(2)
    Ms = [
        ('a: psi0 x psi0', np.outer(psi, psi)),
        ('d: psi0 x conj(psi0)', np.outer(psi, psib)),
        ('b: maximally entangled 1/sqrt3', np.eye(3) / np.sqrt(3)),
        ('b: O/sqrt3 (rotation)', np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]) / np.sqrt(3)),
        ('c: diag(1,i,0)/sqrt2  [Tr(MM^T)=0]', np.diag([1, 1j, 0]) / np.sqrt(2)),
        ('c: u v^T both isotropic', np.outer(u_iso, np.array([1, -1j, 0]) / np.sqrt(2))),
        ('e: diag(1,1,0)/sqrt2  [rank2, equal squares]', np.diag([1, 1, 0]) / np.sqrt(2)),
        ('e: diag(1,-1,0)/sqrt2', np.diag([1, -1, 0]) / np.sqrt(2)),
        ('f: e1 x e1 (non-isotropic product)', np.outer([1, 0, 0], [1, 0, 0])),
        ('g: (e1e1+e2e2+i e3e3)/sqrt3', np.diag([1, 1, 1j]) / np.sqrt(3)),
    ]
    return [(t, np.asarray(M, dtype=complex)) for t, M in Ms]


def main():
    np.random.seed(3)
    Ms = structured_families()
    xs = (7 / 20, 9 / 20, 11 / 20)
    print('--- ranks of the 16x9 Kraus-span matrix (x-independence probe) ---')
    ranktab = []
    for tag, M in Ms:
        rr = []
        for x in (0.2, 7 / 20, 9 / 20, 11 / 20, 0.8):
            S = span_matrix(x, normalize(M))
            sv = np.linalg.svd(S, compute_uv=False)
            rr.append(int(np.sum(sv > 1e-10 * sv[0])))
        ranktab.append(dict(tag=tag, ranks=rr))
        print('%-42s r = %s' % (tag, rr))
    gate('C4', all(len(set(r['ranks'])) == 1 for r in ranktab),
         'rank r(M) is x-independent on all structured families: ' + json.dumps(ranktab))

    gate_C0()
    gate_C1(Ms, xs)
    gate_C2(Ms[:6], (9 / 20, 11 / 20))
    cases = []
    psib = PSI0.conj()
    cases.append(('a@7/20 psibar-slot', 7 / 20, np.outer(PSI0, PSI0),
                  np.kron(np.outer(psib, psib.conj()), np.outer(PSI0, PSI0.conj()))))
    cases.append(('a@9/20 psibar-slot', 9 / 20, np.outer(PSI0, PSI0),
                  np.kron(np.outer(psib, psib.conj()), np.outer(PSI0, PSI0.conj()))))
    rr = np.zeros((9, 9), dtype=complex)
    rr[0, 0] = 0.5
    rr[4, 4] = 0.5
    cases.append(('e@9/20 diag phi', 9 / 20, np.diag([1, 1, 0]) / np.sqrt(2), rr))
    _, rows = gate_C3(cases)
    gate_cal1()
    gate_cal2(Ms)

    out = dict(results=RESULTS, ranktable=ranktab, slope_rows=rows)
    with open('artifacts/logs_whgap_p13b_20260730/gates.json', 'w', newline='\n') as f:
        json.dump(out, f, indent=1)
    npass = sum(1 for r in RESULTS if r['pass_'])
    print('\n%d/%d gates PASS' % (npass, len(RESULTS)))


if __name__ == '__main__':
    main()
