"""R7 reviewer script (independent): claim 4 -- own symbolic-in-x charpoly + interval certificate.

Base point: the isotropic-product one, Psi = u0 (x) u0 with u0 = (1, i, 0) (r = 4).
Route (mine, see tools/whgap_r7_exact.py header): the B-side kernel and the E-side range
are BOTH x-free, so Pi_B and the range basis S are computed once over Q(i) and only D2
carries x.  Hence D_Psi(x) is rational in x with no branch/case analysis at all.

Certificate logic: D(x) is Hermitian with rational-function entries whose denominators must
have no zero in [2/5, 1).  Writing det(lam*1 - D(x)) = sum_k c_k(x) lam^k, the criterion
"all c_k >= 0  <=>  D <= 0" is applied pointwise in x; so it suffices that (i) no numerator
of any c_k has a root in the OPEN interval (2/5, 1), (ii) no denominator vanishes on
[2/5, 1), and (iii) every c_k is >= 0 at probe points inside and at the left end.  Each c_k
is then continuous and of constant sign on (2/5,1); with the x = 2/5 evaluation this gives
D(x) <= 0 for every x in [2/5, 1).
"""
import json

import sympy as sp

from whgap_r7_exact import IDX, Ahat, Bhat, csq_of, lam, proj_from_basis, u0, vec

x = sp.Symbol("x")
PROBES = [sp.Rational(2, 5), sp.Rational(9, 20), sp.Rational(1, 2), sp.Rational(3, 4),
          sp.Rational(99, 100)]

import sys
BASE = sys.argv[1] if len(sys.argv) > 1 else "isoprod"
M = u0 * u0.T if BASE == "isoprod" else sp.diag(1, 1, 0)   # "typeE" = diag(1,1,0)
Psi = vec(M)
P = sp.simplify(Psi * Psi.conjugate().T / (Psi.conjugate().T * Psi)[0, 0])

U = sp.Matrix.hstack(*[vec(Ahat[a] * M * Ahat[b].T) for (a, b) in IDX])
r = U.rank()
PiB = proj_from_basis(sp.Matrix.hstack(*U.conjugate().T.nullspace()))

MB = sp.zeros(9, 9)
for m, (a, b) in enumerate(IDX):
    MB += csq_of(a, x) * csq_of(b, x) * Bhat[m].T * PiB * Bhat[m]
MB = sp.simplify(MB)

Ghat = sp.Matrix(16, 16, lambda m, n: sp.simplify((Bhat[m] * P * Bhat[n].T).trace()))
S = sp.Matrix.hstack(*Ghat.columnspace())
D2 = sp.diag(*[csq_of(a, x) * csq_of(b, x) for (a, b) in IDX])
R = sp.simplify(D2 - D2 * S * (S.conjugate().T * D2 * S).inv() * S.conjugate().T * D2)
ME = sp.zeros(9, 9)
for m in range(16):
    for n in range(16):
        if R[m, n] != 0:
            ME += R[m, n] * Bhat[m].T * Bhat[n]
D = sp.simplify(MB - ME)

out = {"base_point": ("Psi = u0 (x) u0, u0=(1,i,0)" if BASE == "isoprod"
                      else "Psi = type-E, M = diag(1,1,0)"), "r": int(r), "m_B": 9 - int(r),
       "D_hermitian_symbolic": bool(sp.simplify(D - D.conjugate().T) == sp.zeros(9, 9)),
       "Tr_D_P_symbolic": str(sp.simplify((D * P).trace()))}

det = sp.expand(sp.simplify((lam * sp.eye(9) - D).det(method="berkowitz")))
coeffs = sp.Poly(det, lam).all_coeffs()          # lam^9 ... lam^0
rows, all_roots_01 = [], []
for k, c0 in enumerate(coeffs):
    c = sp.cancel(sp.simplify(c0))
    num, den = sp.fraction(c)
    numP = sp.Poly(sp.expand(num), x)
    denP = sp.Poly(sp.expand(den), x)
    nrts = list(sp.real_roots(numP)) if numP.degree() > 0 else []
    drts = list(sp.real_roots(denP)) if denP.degree() > 0 else []
    roots01 = [rr for rr in nrts if 0 < rr < 1]
    all_roots_01 += roots01
    vals = {str(pt): str(sp.simplify(c.subs(x, pt))) for pt in PROBES}
    nonneg = all(sp.simplify(c.subs(x, pt)) >= 0 for pt in PROBES)
    rows.append({
        "lam_power": 9 - k,
        "num_factored": str(sp.factor(numP.as_expr())),
        "den_factored": str(sp.factor(denP.as_expr())),
        "den_roots_in_[2/5,1)": [str(rr) for rr in drts if sp.Rational(2, 5) <= rr < 1],
        "num_roots_in_(2/5,1)": [str(rr) for rr in nrts if sp.Rational(2, 5) < rr < 1],
        "num_roots_in_(0,1)": [str(rr) for rr in roots01],
        "num_divisible_by_5x-2": bool(sp.rem(numP.as_expr(), 5 * x - 2, x) == 0) if numP.degree() > 0 else False,
        "values_at_probes": vals,
        "nonneg_at_all_probes": bool(nonneg),
    })
out["coefficients"] = rows
out["NO_num_root_in_open_(2/5,1)"] = all(not rr["num_roots_in_(2/5,1)"] for rr in rows)
out["NO_den_root_in_[2/5,1)"] = all(not rr["den_roots_in_[2/5,1)"] for rr in rows)
out["all_coeffs_nonneg_at_probes"] = all(rr["nonneg_at_all_probes"] for rr in rows)
out["max_num_root_in_(0,1)"] = str(max(all_roots_01)) if all_roots_01 else "none"
out["all_num_roots_in_(0,1)_are_le_2/5"] = bool(all(rr <= sp.Rational(2, 5) for rr in all_roots_01))
out["VERDICT_interval_cert_on_[2/5,1)"] = bool(
    out["NO_num_root_in_open_(2/5,1)"] and out["NO_den_root_in_[2/5,1)"]
    and out["all_coeffs_nonneg_at_probes"])
print(json.dumps(out, indent=1, default=str))
with open(f"artifacts/logs_whgap_p13b_20260730/r7_interval_{BASE}.json", "w", newline="\n") as fh:
    json.dump(out, fh, indent=1, default=str)
