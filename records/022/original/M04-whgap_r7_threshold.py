"""R7 reviewer script (independent): the type-E base point's OWN first-order threshold.

Reason this exists.  The interval certificate of claim 4 shows that, for the type-E entangled
base point, no charpoly coefficient of D_Psi(x) has a root in (2/5, 1).  The largest root in
(0,1) of any coefficient is therefore the exact x at which that base point's first-order
mechanism switches on.  For the isotropic-PRODUCT base point that root is exactly 2/5 (the
coefficients carry (5x-2) factors).  For the type-E ENTANGLED base point it is the unique root
in (0,1) of 19 x^4 - 21 x^3 - 14 x^2 + 28 x - 8, which is STRICTLY BELOW 2/5 -- so the type-E
point does NOT "die at the same 2/5": it dies earlier.  This script pins that number and
exhibits exact lambda_max values on both sides of it, together with d_1(x) for comparison.
"""
import json

import sympy as sp

from whgap_r7_exact import FAMILIES, nsd_certificate, weight_operator

x = sp.Symbol("x")
q = 19 * x ** 4 - 21 * x ** 3 - 14 * x ** 2 + 28 * x - 8
roots01 = [rr for rr in sp.real_roots(sp.Poly(q, x)) if 0 < rr < 1]
xstar = max(roots01)

out = {"typeE_threshold_minimal_polynomial": "19*x**4 - 21*x**3 - 14*x**2 + 28*x - 8",
       "typeE_threshold_roots_in_(0,1)": [str(sp.N(rr, 30)) for rr in roots01],
       "x_star_typeE": str(sp.N(xstar, 30)),
       "x_star_is_strictly_below_2/5": bool(xstar < sp.Rational(2, 5)),
       "2/5_minus_x_star": str(sp.N(sp.Rational(2, 5) - xstar, 12)),
       "table": []}

for xr in (sp.Rational(7, 20), sp.Rational(19, 50), sp.Rational(77, 200), sp.Rational(387, 1000),
           sp.Rational(39, 100), sp.Rational(2, 5)):
    row = {"x": str(xr), "x_float": float(xr),
           "d1(x)_n1": str(sp.N((1 - xr) * (2 - 5 * xr) / (2 - xr), 15))}
    for tag, key in (("typeE", "typeE  M=diag(1,1,0)"), ("iso_prod", "iso_prod_a  M=u0 u0^T")):
        D, info = weight_operator(FAMILIES[key], xr, crosschecks=False)
        ok, co, lm, ro = nsd_certificate(D)
        row[tag + "_lambda_max"] = ("0" if lm is None else str(lm))
        row[tag + "_lambda_max_float"] = (0.0 if lm is None else float(lm))
        row[tag + "_NSD"] = bool(ok)
    row["typeE_beats_n1_unnormalised"] = bool(row["typeE_lambda_max_float"]
                                              > float(sp.N((1 - xr) * (2 - 5 * xr) / (2 - xr))))
    row["typeE_beats_n1_PER_USE"] = bool(row["typeE_lambda_max_float"] / 2
                                        > float(sp.N((1 - xr) * (2 - 5 * xr) / (2 - xr))))
    out["table"].append(row)
    print(json.dumps(row, indent=1), flush=True)

with open("artifacts/logs_whgap_p13b_20260730/r7_threshold.json", "w", newline="\n") as fh:
    json.dump(out, fh, indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "table"}, indent=1))
