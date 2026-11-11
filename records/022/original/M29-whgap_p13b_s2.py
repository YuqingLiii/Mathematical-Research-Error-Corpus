"""WHGAP P13-B, S2: the degeneracy-variety derivation, fully symbolic.

S2.1  Closed form of the kernel-candidate quadratic form (the n=2 analogue of (1-x)tau^2):
        F(M) := <conj(Psi)| (Lambda x Lambda)(P_Psi) |conj(Psi)>
              = (1-x)^2 |Tr(M M^T)|^2 + x^2 ||adj M||_F^2
      via the three holomorphic identities
        Tr(M^T A_i M)   = 0            (M^T A_i M is antisymmetric)
        Tr(M^T M A_i)   = 0            (M^T M is symmetric)
        Tr(M^T A_i M A_j) = -2 (adj M)_{ji}
      Consequence: conj(Psi) lies in ker Lambda^(2)(P_Psi) iff Tr(MM^T) = 0 AND adj M = 0,
      i.e. iff Psi is a PRODUCT state u tensor v with an isotropic factor.  So no entangled
      Psi has conj(Psi) in the B-side kernel: the entangled part of the degeneracy variety
      must be found by rank analysis, not by this direction.

S2.2  Sufficient degenerate families (exact, proved symbolically): with
        P3 := { M = v a^T + y u^T : u^T u = v^T v = 0 },
      B := u v^T annihilates every aMb (a,b in L = span{1,A_1,A_2,A_3}), hence
      dim span{ K_a M K_b^T } <= 8, i.e. m_B >= 1, for every M in P3.
      (Verified as a polynomial identity in the isotropic chart u = (1-z^2, i(1+z^2), 2z).)
      P3 contains: iso x iso products, iso-factor products, the type-E entangled points
      diag(1,1,0) ~ u0 conj(u0)^T + conj(u0) u0^T, and generic rank-2 entangled points.

S2.3  x-independence: ker Lambda^(2)(P_Psi) = (span{Ahat_a M Ahat_b^T})^perp carries no x,
      so r(M) and m_B are constant on x in (0,1).

S2.4  Symbolic-in-x weight operator for the structured entangled families, with the exact
      charpoly-coefficient (D <= 0) test as a function of x.
"""
import json
import sys
import time

import sympy as sp

sys.path.insert(0, __file__.rsplit('\\', 1)[0].replace('\\', '/'))
from whgap_p13b_exact import AH, BH, weight_operator_exact, berkowitz_charpoly, dag, vec

x = sp.Symbol('x', positive=True)
OUT = {}


def adjugate(M):
    return sp.Matrix(3, 3, lambda i, j: sp.expand(
        (-1) ** (i + j) * M.minor_submatrix(j, i).det()))


def s2_1():
    m = sp.symbols('m0:9')
    n = sp.symbols('n0:9')          # independent stand-ins for conj(m)
    M = sp.Matrix(3, 3, m)
    N = sp.Matrix(3, 3, n)
    A = AH[1:]
    checks = {}
    checks['Tr(M^T A_i M) = 0'] = all(sp.expand((M.T * A[i] * M).trace()) == 0 for i in range(3))
    checks['Tr(M^T M A_i) = 0'] = all(sp.expand((M.T * M * A[i]).trace()) == 0 for i in range(3))
    adjM = adjugate(M)
    checks['Tr(M^T A_i M A_j) = -2 adj(M)_{ji}'] = all(
        sp.expand((M.T * A[i] * M * A[j]).trace() + 2 * adjM[j, i]) == 0
        for i in range(3) for j in range(3))
    # full closed form, symbolic in m, n (= conj m) and x
    csq = [1 - x, x / 2, x / 2, x / 2]
    lhs = 0
    for a in range(4):
        for b in range(4):
            Ka2 = csq[a] * csq[b]                     # |c_a c_b|^2
            lhs += Ka2 * sp.expand((M.T * AH[a] * M * AH[b].T).trace()) * \
                sp.expand((N.T * AH[a] * N * AH[b].T).trace())
    adjN = adjugate(N)
    rhs = (1 - x) ** 2 * sp.expand((M * M.T).trace()) * sp.expand((N * N.T).trace()) + \
        x ** 2 * sum(adjM[i, j] * adjN[i, j] for i in range(3) for j in range(3))
    checks['F(M) closed form (symbolic in m, conj m, x)'] = sp.expand(lhs - rhs) == 0
    for k, v in checks.items():
        print(('PASS ' if v else 'FAIL ') + k)
    OUT['s2_1'] = {k: bool(v) for k, v in checks.items()}
    return all(checks.values())


def s2_2():
    z1, z2, c1, c2 = sp.symbols('z1 z2 c1 c2')
    a = sp.Matrix(sp.symbols('a1 a2 a3'))
    y = sp.Matrix(sp.symbols('y1 y2 y3'))
    u = c1 * sp.Matrix([1 - z1 ** 2, sp.I * (1 + z1 ** 2), 2 * z1])
    v = c2 * sp.Matrix([1 - z2 ** 2, sp.I * (1 + z2 ** 2), 2 * z2])
    checks = {}
    checks['chart is isotropic: u^T u = 0'] = sp.expand((u.T * u)[0, 0]) == 0
    checks['chart is isotropic: v^T v = 0'] = sp.expand((v.T * v)[0, 0]) == 0
    M = v * a.T + y * u.T
    B = u * v.T
    res = []
    for i in range(4):
        for j in range(4):
            res.append(sp.expand((B * AH[i] * M * AH[j].T).trace()))
    checks['B = u v^T annihilates all 16 a M b  (=> m_B >= 1 on P3)'] = all(r == 0 for r in res)
    # type-E membership: diag(1,1,0) = u0 conj(u0)^T + conj(u0) u0^T
    u0 = sp.Matrix([1, sp.I, 0]) / sp.sqrt(2)
    u0b = sp.Matrix([1, -sp.I, 0]) / sp.sqrt(2)
    checks['diag(1,1,0) = u0 u0bar^T + u0bar u0^T (type-E is in P3)'] = \
        sp.simplify(u0 * u0b.T + u0b * u0.T - sp.diag(1, 1, 0)) == sp.zeros(3, 3)
    for k, v_ in checks.items():
        print(('PASS ' if v_ else 'FAIL ') + k)
    OUT['s2_2'] = {k: bool(v_) for k, v_ in checks.items()}
    return all(checks.values())


def s2_4():
    """symbolic-in-x weight operator + exact D <= 0 threshold, for the key families"""
    s2 = sp.sqrt(2)
    I = sp.I
    u0 = sp.Matrix([1, I, 0]) / s2
    fam = [('a  iso product u0 u0^T', u0 * u0.T),
           ('e1 type-E diag(1,1,0)/sqrt2', sp.diag(1, 1, 0) / s2)]
    rows = []
    for name, M in fam:
        t0 = time.time()
        res = weight_operator_exact(M, x)
        D = res['D']
        co, lam = berkowitz_charpoly(D)
        co = [sp.factor(sp.cancel(c)) for c in co]
        # the sign-critical coefficients: locate the roots in (0,1) of each
        crit = []
        for k, c in enumerate(co):
            if c == 0:
                crit.append((k, '0', []))
                continue
            rts = [sp.nsimplify(r) for r in sp.solve(sp.numer(sp.together(c)), x)]
            rr = []
            for r in rts:
                try:
                    fv = float(sp.re(sp.N(r)))
                    if abs(sp.im(sp.N(r))) < 1e-12 and 0 < fv < 1:
                        rr.append((sp.sstr(r), fv))
                except Exception:
                    pass
            crit.append((k, sp.sstr(c), rr))
        rows.append(dict(family=name, r=res['r'], mB=res['mB'], mE=res['mE'],
                         charpoly=[str(c) for c in co],
                         roots_in_01=[(k, cc, rr) for k, cc, rr in crit],
                         seconds=round(time.time() - t0, 1)))
        print('=== %s  (r=%d, mB=%d, mE=%d, %.1fs)' % (name, res['r'], res['mB'], res['mE'],
                                                       time.time() - t0))
        for k, cc, rr in crit:
            print('   coeff[%d] = %s   roots in (0,1): %s' % (k, cc, rr))
    OUT['s2_4'] = rows


def main():
    ok1 = s2_1()
    ok2 = s2_2()
    s2_4()
    OUT['all_identity_gates_pass'] = bool(ok1 and ok2)
    with open('artifacts/logs_whgap_p13b_20260730/s2_symbolic.json', 'w', newline='\n') as f:
        json.dump(OUT, f, indent=1)


if __name__ == '__main__':
    main()
