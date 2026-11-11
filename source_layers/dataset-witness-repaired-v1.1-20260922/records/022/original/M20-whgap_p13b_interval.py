"""WHGAP P13-B: interval certificate on the WHOLE strip for the symbolic-in-x families.

Input: the symbolic charpoly coefficients c_k(x) of det(lam*1 - D_Psi(x)) produced by
tools/whgap_p13b_s2.py (stored in artifacts/logs_whgap_p13b_20260730/s2_symbolic.json).

For a Hermitian D, lam_max(D) <= 0 iff every coefficient of det(lam*1 - D) is >= 0.
Each c_k(x) is a rational function of x whose denominator is a power of (x-2) (no zero in
(0,1)).  So the sign of c_k on (2/5, 1) is constant unless the NUMERATOR has a real root
there.  The certificate therefore is:
   (i) exact real-root isolation of numer(c_k) (sympy real_roots, exact algebraic roots);
   (ii) no root lies in the open interval (2/5, 1);
   (iii) c_k(1/2) >= 0 exactly (one exact rational evaluation fixes the sign),
   (iv) plus c_k(2/5) >= 0 exactly (closes the left endpoint).
Then c_k(x) >= 0 for every x in [2/5, 1), hence D_Psi(x) <= 0 there: NO first-order
eps log(1/eps) ascent from this base point anywhere in the strip [2/5, 1/2) -- indeed on
all of [2/5, 1).
"""
import json
import sys

import sympy as sp

x = sp.Symbol('x')      # plain symbol: the stored strings carry no assumptions
TWO5 = sp.Rational(2, 5)


def certify(coeffs, lo=TWO5, hi=sp.Integer(1)):
    rows = []
    ok_all = True
    for k, cs in enumerate(coeffs):
        c = sp.sympify(cs, locals={'x': x})
        c = sp.cancel(sp.together(c))
        num, den = sp.fraction(c)
        num = sp.expand(num)
        if num == 0:
            rows.append(dict(k=k, zero=True, roots_in_open=[], sign_at_half='0',
                             sign_at_2_5='0', ok=True))
            continue
        den_roots = [r for r in sp.Poly(sp.expand(den), x).real_roots()] if den.has(x) else []
        bad_den = [str(r) for r in den_roots if lo <= r < hi]
        rr = sp.Poly(num, x).real_roots()
        inside = [str(r) for r in rr if lo < r < hi]
        s_half = sp.Rational(sp.cancel(c.subs(x, sp.Rational(1, 2))))
        s_lo = sp.Rational(sp.cancel(c.subs(x, lo)))
        ok = (not inside) and (not bad_den) and bool(s_half >= 0) and bool(s_lo >= 0)
        ok_all &= bool(ok)
        rows.append(dict(k=k, zero=False, roots_in_open=inside, denom_roots_in_range=bad_den,
                         sign_at_half=str(s_half), sign_at_2_5=str(s_lo), ok=bool(ok)))
    return ok_all, rows


def main():
    src = 'artifacts/logs_whgap_p13b_20260730/s2_symbolic.json'
    data = json.load(open(src))
    out = []
    for fam in data['s2_4']:
        ok, rows = certify(fam['charpoly'])
        print('=== %s : interval certificate on [2/5, 1) -> %s' % (fam['family'], 'PASS' if ok else 'FAIL'))
        for r in rows:
            print('   c_%d: roots in (2/5,1) = %s ; c(2/5) = %s ; c(1/2) = %s ; ok=%s'
                  % (r['k'], r['roots_in_open'], r['sign_at_2_5'][:40], r['sign_at_half'][:40], r['ok']))
        out.append(dict(family=fam['family'], r=fam['r'], mB=fam['mB'], mE=fam['mE'],
                        interval_certificate_pass=bool(ok), rows=rows))
    with open('artifacts/logs_whgap_p13b_20260730/interval_certificate.json', 'w', newline='\n') as f:
        json.dump(out, f, indent=1)


if __name__ == '__main__':
    main()
