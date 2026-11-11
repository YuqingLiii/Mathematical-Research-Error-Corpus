"""WHGAP P13-B, S1 + S2: EXACT (radical-free) 2-copy weight operator.

Radical-free rational chart (P13-A tooling addition).  Write K_a = c_a * Ahat_a with
Ahat_0 = 1, Ahat_i = A_i (integer matrices), c_0^2 = 1-x, c_i^2 = x/2.  For the two-copy
Kraus W_m = K_a tensor K_b = c_m * Bhat_m (c_m := c_a c_b, Bhat_m := Ahat_a tensor Ahat_b,
integer 9x9):

  G_B := (Lambda x Lambda)(P_Psi) = sum_m c_m^2 Bhat_m P Bhat_m^dag        [rational in x]
  ker G_B = ( span{ Ahat_a M Ahat_b^T } )^perp                             [x-FREE]
  G_E := (Lambda^c x Lambda^c)(P_Psi) = Delta Ghat Delta, Delta = diag(c_m),
         Ghat[m,n] = Tr[ Bhat_m P Bhat_n^T ]                               [x-FREE]
  Pi_E = Delta^{-1} Nh (Nh^dag D2inv Nh)^{-1} Nh^dag Delta^{-1},  D2inv = diag(1/c_m^2)
  M_B  = sum_m c_m^2 Bhat_m^T Pi_B Bhat_m                                  [rational in x]
  M_E  = sum_{m,n} R[m,n] Bhat_m^T Bhat_n,  R := Nh (Nh^dag D2inv Nh)^{-1} Nh^dag
         (since c_m c_n (Pi_E)[m,n] = R[m,n])                              [rational in x]
  D_Psi = M_B - M_E,  Tr[D_Psi phi] = w_B(phi) - w_E(phi).
No square root ever appears.  Berkowitz determinant is used, never Matrix.charpoly.

Negative-semidefiniteness test (exact): for Hermitian D, all eigenvalues <= 0  <=>  every
coefficient of det(lam*1 - D) is >= 0.  Since Tr[D P_Psi] = 0 always, lam_max >= 0, so
"all coefficients >= 0" is equivalent to lam_max = 0 EXACTLY (no first-order ascent).
"""
import json
import sys

from fractions import Fraction

import mpmath as mp
import sympy as sp

XS = sp.Symbol('x', positive=True)


def ahat():
    A = [sp.eye(3)]
    for i in range(3):
        Mi = sp.zeros(3, 3)
        for j in range(3):
            for k in range(3):
                p = (i, j, k)
                if len(set(p)) < 3:
                    continue
                sgn = 1
                q = list(p)
                for a in range(3):
                    for b in range(a + 1, 3):
                        if q[a] > q[b]:
                            sgn = -sgn
                Mi[j, k] = sgn
        A.append(Mi)
    return A


AH = ahat()
BH = [sp.Matrix(sp.kronecker_product(AH[a], AH[b])) for a in range(4) for b in range(4)]
BB = [[sp.Matrix(BH[m].T * BH[n]) for n in range(16)] for m in range(16)]   # integer, cached
BBt = [[sp.Matrix(BH[m] * BH[n].T) for n in range(16)] for m in range(16)]  # integer, cached


def csq2(xv):
    c = [1 - xv, xv / 2, xv / 2, xv / 2]
    return [sp.cancel(c[a] * c[b]) for a in range(4) for b in range(4)]


def vec(M):
    return sp.Matrix(9, 1, [M[j, k] for j in range(3) for k in range(3)])


def dag(M):
    return M.conjugate().T


def weight_operator_exact(M, xv):
    """M need NOT be normalised: the state is P = Psi Psi^dag / |Psi|^2 (radical-free when M
    has Gaussian-rational entries), while ker G_B / ker Ghat are scale-invariant and are
    computed from the raw M."""
    M = sp.Matrix(M)
    nrm = sp.expand(sum(M[i, j] * sp.conjugate(M[i, j]) for i in range(3) for j in range(3)))
    Psi = vec(M)
    P = sp.Matrix(sp.expand(Psi * dag(Psi) / nrm)).applyfunc(sp.cancel)
    c2 = csq2(xv)

    # ---- x-free objects
    rows = [list(vec(AH[a] * M * AH[b].T)) for a in range(4) for b in range(4)]
    Z = sp.Matrix(rows)                                     # 16 x 9
    r = Z.rank()
    nsB = Z.conjugate().nullspace()                         # ker G_B  (x-free)
    NB = sp.Matrix.hstack(*nsB) if nsB else sp.zeros(9, 0)
    mB = NB.shape[1]
    assert mB == 9 - r, (mB, r)
    Gh = sp.zeros(16, 16)
    for m in range(16):
        for n in range(16):
            Gh[m, n] = sp.expand((BB[n][m] * P).trace())    # Tr[Bhat_m P Bhat_n^T]
    nsE = Gh.nullspace()
    Nh = sp.Matrix.hstack(*nsE)
    mE = Nh.shape[1]
    assert mE == 16 - r, (mE, r)

    # ---- Pi_B, M_B
    if mB:
        PiB = NB * (dag(NB) * NB).inv() * dag(NB)
        PiB = sp.expand(PiB)
    else:
        PiB = sp.zeros(9, 9)
    MB = sp.zeros(9, 9)
    for m in range(16):
        if c2[m] == 0:
            continue
        MB += c2[m] * (BH[m].T * PiB * BH[m])
    MB = sp.Matrix(MB).applyfunc(sp.cancel)

    # ---- R, M_E  (radical-free)
    D2inv = sp.diag(*[sp.cancel(1 / c) for c in c2])
    Gm = sp.Matrix(dag(Nh) * D2inv * Nh).applyfunc(sp.cancel)
    R = sp.Matrix(Nh * Gm.inv() * dag(Nh)).applyfunc(sp.cancel)
    ME = sp.zeros(9, 9)
    for m in range(16):
        for n in range(16):
            if R[m, n] != 0:
                ME += R[m, n] * BB[m][n]
    ME = sp.Matrix(ME).applyfunc(sp.cancel)

    D = sp.Matrix(MB - ME).applyfunc(sp.cancel)
    return dict(D=D, MB=MB, ME=ME, r=r, mB=mB, mE=mE, Psi=Psi, PiB=PiB)


def _to_frac_complex(z):
    z = sp.expand(z)
    re, im = sp.Rational(sp.re(z)), sp.Rational(sp.im(z))
    return (Fraction(int(re.p), int(re.q)), Fraction(int(im.p), int(im.q)))


def _cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def _csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def _cdiv(a, b):
    d = b[0] * b[0] + b[1] * b[1]
    return ((a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d)


def hermitian_pos_def_exact(C):
    """Exact Hermitian positive-definiteness by fraction-arithmetic LDL^H.
    Returns (is_pd, pivots): pivots are the exact rational D-entries; all > 0 <=> C > 0,
    and the leading principal minors are the running products of the pivots."""
    n = C.shape[0]
    A = [[_to_frac_complex(C[i, j]) for j in range(n)] for i in range(n)]
    piv = []
    for k in range(n):
        p = A[k][k]
        if p[1] != 0:
            return 'NONREAL_PIVOT', ['non-real pivot at %d' % k]
        if p[0] < 0:
            piv.append(p[0])
            return 'INDEFINITE', [str(v) for v in piv]
        if p[0] == 0:
            piv.append(p[0])
            return 'ZERO_PIVOT', [str(v) for v in piv]
        piv.append(p[0])
        for i in range(k + 1, n):
            f = _cdiv(A[i][k], p)
            for j in range(k, n):
                A[i][j] = _csub(A[i][j], _cmul(f, A[k][j]))
    return 'PD', [str(v) for v in piv]


def berkowitz_charpoly(D):
    lam = sp.Symbol('lam')
    p = sp.expand((lam * sp.eye(D.shape[0]) - D).det(method='berkowitz'))
    return sp.Poly(p, lam).all_coeffs(), lam


def nsd_certificate(D, Psi):
    """EXACT certificate that D <= 0 with kernel direction Psi.
    (i) D Psi = 0 exactly; (ii) the compression of -D to an exact basis of Psi^perp is
    positive DEFINITE by Sylvester's criterion (all leading principal minors > 0, Berkowitz).
    Then spec(D) = {0} u (negatives), so lam_max(D) = 0 exactly and there is no
    first-order ascent from this base point at this x."""
    n = D.shape[0]
    DPsi = sp.Matrix(sp.expand(D * Psi)).applyfunc(sp.cancel)
    kills_psi = all(sp.expand(e) == 0 for e in DPsi)
    # exact basis of Psi^perp : project the standard basis, keep 8 independent columns
    nrm = sp.expand((dag(Psi) * Psi)[0, 0])
    cols = []
    for k in range(n):
        e = sp.zeros(n, 1)
        e[k] = 1
        w = sp.Matrix(sp.expand(e - Psi * ((dag(Psi) * e)[0, 0] / nrm))).applyfunc(sp.cancel)
        if not all(sp.simplify(z) == 0 for z in w):
            trial = cols + [w]
            if sp.Matrix.hstack(*trial).rank() == len(trial):
                cols.append(w)
        if len(cols) == n - 1:
            break
    B = sp.Matrix.hstack(*cols)
    C = sp.Matrix(sp.expand(-dag(B) * D * B)).applyfunc(sp.cancel)
    status, piv = hermitian_pos_def_exact(C)
    verdict = dict(kills_psi=bool(kills_psi), ldl_status=status,
                   compression_pos_def=(status == 'PD'), ldl_pivots=piv,
                   basis_rank=int(B.rank()))
    if status in ('ZERO_PIVOT', 'NONREAL_PIVOT'):
        # inconclusive without pivoting: fall back to the exact charpoly sign test
        co, _ = berkowitz_charpoly(D)
        verdict['charpoly_coeffs_nonneg'] = bool(all(sp.simplify(c) >= 0 for c in co))
        verdict['nsd'] = verdict['charpoly_coeffs_nonneg'] and kills_psi
    else:
        verdict['nsd'] = (status == 'PD') and kills_psi
    return verdict


def lam_max_mp(D, dps=60):
    mp.mp.dps = dps
    def cvt(v):
        v = sp.cancel(v)
        if v.is_Rational:
            return mp.mpf(int(v.p)) / mp.mpf(int(v.q))
        return mp.mpmathify(str(sp.N(v, dps + 5)))
    A = mp.matrix(D.shape[0], D.shape[1])
    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            z = sp.expand(D[i, j])
            A[i, j] = mp.mpc(cvt(sp.re(z)), cvt(sp.im(z)))
    E = mp.eighe(A, eigvals_only=True)
    return max(E), [mp.nstr(e, 25) for e in sorted(E, reverse=True)]


def d1(xv):
    return sp.cancel((1 - xv) * (2 - 5 * xv) / (2 - xv))


def families():
    I = sp.I
    u0 = sp.Matrix([1, I, 0])            # isotropic (unnormalised representatives are fine)
    u0b = sp.Matrix([1, -I, 0])
    e3 = sp.Matrix([0, 0, 1])
    out = [('a  iso product  psi0 x psi0', u0 * u0.T),
           ('d  psi0 x conj(psi0)', u0 * u0b.T),
           ('b  maximally entangled 1/sqrt3 * 1', sp.eye(3)),
           ('b2 O/sqrt3, O = cyclic permutation',
            sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])),
           ('c1 diag(1,i,0)/sqrt2   [Tr MM^T = 0, entangled]', sp.diag(1, I, 0)),
           ('e1 diag(1,1,0)/sqrt2  [type-E entangled, r=7]', sp.diag(1, 1, 0)),
           ('e2 (E12+E21)/sqrt2    [type-E rotated]',
            sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])),
           ('e3 diag(1,-1,0)/sqrt2', sp.diag(1, -1, 0)),
           ('P3g u0 a^T + y u0^T, a=(1,0,2), y=(0,1,1)',
            u0 * sp.Matrix([1, 0, 2]).T + sp.Matrix([0, 1, 1]) * u0.T),
           ('P3s u0 e3^T + e3 u0^T (symmetric)', u0 * e3.T + e3 * u0.T),
           ('P3i interpolation (1-s) u0u0^T + s (u0 u0b^T + u0b u0^T), s=1/3',
            2 * u0 * u0.T + (u0 * u0b.T + u0b * u0.T)),
           ('P3r generic rational P3, a=(2,-1,3), y=(1,2,0)',
            u0 * sp.Matrix([2, -1, 3]).T + sp.Matrix([1, 2, 0]) * u0.T),
           ('P3c a=(1,i,0)=u0 (=> rank1), y=(0,0,1)', u0 * u0.T + e3 * u0.T)]
    return out


def main():
    xvals = [sp.Rational(9, 20), sp.Rational(21, 50), sp.Rational(12, 25),
             sp.Rational(2, 5), sp.Rational(7, 20), sp.Rational(11, 20)]
    log = []
    for name, M in families():
        print('=== %s' % name)
        for xv in xvals:
            res = weight_operator_exact(M, xv)
            D = res['D']
            herm = all(sp.simplify(e) == 0 for e in (D - dag(D)))
            t0 = sp.simplify((dag(res['Psi']) * D * res['Psi'])[0, 0])
            cert = nsd_certificate(D, res['Psi'])
            nonneg = cert['nsd']
            lmax, spec = lam_max_mp(D)
            row = dict(family=name, x=str(xv), r=res['r'], mB=res['mB'], mE=res['mE'],
                       hermitian=bool(herm), trace_at_Psi=str(t0),
                       exact_nsd_certificate=cert,
                       charpoly_all_coeffs_nonneg=bool(nonneg),
                       lam_max_60dps=mp.nstr(lmax, 30), spectrum=spec,
                       d1=str(d1(xv)), d1_float=float(d1(xv)))
            log.append(row)
            print('   x=%-6s r=%d mB=%d mE=%d  Tr[D P]=%s  D<=0 %s  lam_max=%s  (d_1=%.9f)'
                  % (str(xv), res['r'], res['mB'], res['mE'], t0, nonneg,
                     mp.nstr(lmax, 12), float(d1(xv))))
        with open('artifacts/logs_whgap_p13b_20260730/exact_s1.json', 'w', newline='\n') as f:
            json.dump(log, f, indent=1)


if __name__ == '__main__':
    main()
