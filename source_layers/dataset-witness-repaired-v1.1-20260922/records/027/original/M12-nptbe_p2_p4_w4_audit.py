"""P4 review -- independent audit of W4 (R1.sos): batch-2 baseline + exact Farkas.

(1) BASELINE.  Batch-2's reviewed-CLEAN dual certificate value is lambda_min of the
    weight-(0,0,0) Gram block restricted to the orthogonal complement of the
    determinant direction.  I recompute it from the ARCHIVED setup
    (w4_slice_setup.npz: G30_0, dvec, w30) with my own deflation + eigvalsh, not
    from W4's script.

(2) FARKAS.  Exact re-verification, in fractions.Fraction, of the four archived
    certificates y (d = 3,4,5,6) against the archived rational A/F coordinates:
        y >= 0,   <y, A_lambda> >= 0 for every generator,   <y, F> < 0
    which certifies F not in cone{A_lambda} + nonneg-orthant(B).
    Also re-checks the claimed closed-form family
        y = (1/(2(d/2-1)^3)) (e_TTTT + 3(d+1)^2 (d-1) e_JJJJ).

(3) The archived Gram blocks W and G21 of the "FEASIBLE" solution are re-tested
    for PSD-ness from w4_certificate.npz.
"""
import json
from fractions import Fraction

import numpy as np

W4 = "artifacts/logs_nptbe_fleet_20260729/W4/"
OUT = {}

print("=" * 78)
print("(1) batch-2 baseline lambda_min -- independent recomputation")
print("=" * 78)
z = np.load(W4 + "w4_slice_setup.npz", allow_pickle=True)
G = z["G30_0"]
dvec = z["dvec"]
w30 = z["w30"]
print(f"   G30_0 shape {G.shape}, hermiticity ||G-G^H|| = {np.linalg.norm(G - G.conj().T):.3e}")
Gh = (G + G.conj().T) / 2
ev_all = np.linalg.eigvalsh(Gh)
print(f"   lambda_min of the FULL 165x165 weight-0 Gram (no deflation) = {ev_all[0]:.16f}")

# restrict to the zero-weight sector, then deflate the determinant direction
mask0 = np.all(w30 == 0, axis=1)
print(f"   zero-weight sector dim = {int(mask0.sum())}")
G0 = Gh[np.ix_(mask0, mask0)]
d0 = dvec[mask0]
ev0 = np.linalg.eigvalsh(G0)
print(f"   lambda_min of the zero-weight block (undeflated) = {ev0[0]:.16f}")
if np.linalg.norm(d0) > 0:
    u = d0 / np.linalg.norm(d0)
    P = np.eye(G0.shape[0]) - np.outer(u, u.conj())
    # orthonormal basis of the complement
    Q, _ = np.linalg.qr(P)
    # drop the null direction: keep columns with significant projection
    keep = [i for i in range(Q.shape[1]) if np.linalg.norm(P @ Q[:, i]) > 1e-8]
    B = Q[:, keep]
    B, _ = np.linalg.qr(P @ B)
    Gd = B.conj().T @ G0 @ B
    Gd = (Gd + Gd.conj().T) / 2
    evd = np.linalg.eigvalsh(Gd)
    print(f"   lambda_min after deflating the det direction = {evd[0]:.16f}")
    OUT["baseline_deflated"] = float(evd[0])
OUT["baseline_zero_weight_block"] = float(ev0[0])
OUT["baseline_full"] = float(ev_all[0])
print(f"   W4 reports     -1.3381959324607335")
print(f"   batch-2 frozen -1.3381959324607333")

print()
print("=" * 78)
print("(2) EXACT Farkas re-verification (fractions.Fraction)")
print("=" * 78)
J = json.load(open(W4 + "w4_biquadratic_exact.json"))
farkas = {}
for key in ("d=3", "d=4", "d=5", "d=6"):
    e = J[key]
    d = e["d"]
    basis = list(e["F_coords"].keys())
    F = [Fraction(e["F_coords"][b]) for b in basis]
    y = [Fraction(s) for s in e["y"]]
    assert len(y) == len(basis), (len(y), len(basis))
    ymin = min(y)
    pairs = {}
    for lam, co in e["A_coords"].items():
        v = [Fraction(co[b]) for b in basis]
        pairs[lam] = sum(yi * vi for yi, vi in zip(y, v))
    minA = min(pairs.values())
    pF = sum(yi * fi for yi, fi in zip(y, F))
    ok = (ymin >= 0) and (minA >= 0) and (pF < 0)
    print(f" {key}:  min(y) = {ymin}   min_lambda <y,A_lambda> = {minA}   <y,F> = {pF}"
          f"   -> certificate {'VALID' if ok else 'INVALID'}")
    print(f"        y nonzero entries: "
          f"{{{', '.join(f'{basis[i]}: {y[i]}' for i in range(len(y)) if y[i] != 0)}}}")
    # closed-form family check
    mu = Fraction(d, 2) - 1
    pref = Fraction(1, 1) / (2 * mu ** 3)
    cf_T = pref
    cf_J = pref * 3 * (d + 1) ** 2 * (d - 1)
    iT = basis.index("BTTTT")
    iJ = basis.index("BJJJJ")
    # certificates are only defined up to positive scale; compare ratios
    ratio_ok = (y[iJ] * cf_T == y[iT] * cf_J)
    scale = y[iT] / cf_T if cf_T != 0 else None
    print(f"        closed form (1/(2(d/2-1)^3))(e_TTTT + 3(d+1)^2(d-1) e_JJJJ)"
          f" = ({cf_T}, {cf_J});  archived/(closed form) scale = {scale};"
          f" direction match: {ratio_ok}")
    farkas[key] = dict(min_y=str(ymin), min_pair_A=str(minA), pair_F=str(pF), valid=ok,
                       closed_form=(str(cf_T), str(cf_J)), scale=str(scale),
                       direction_match=bool(ratio_ok),
                       archived_flag=e["exact_certificate_valid"])
OUT["farkas"] = farkas

print()
print("=" * 78)
print("(3) archived 'feasible' Gram blocks -- PSD re-test")
print("=" * 78)
try:
    zc = np.load(W4 + "w4_certificate.npz", allow_pickle=True)
    print("   keys:", list(zc.keys()))
    worst = {}
    for k in zc.keys():
        a = zc[k]
        if a.ndim == 2 and a.shape[0] == a.shape[1] and a.shape[0] > 1:
            ah = (a + a.conj().T) / 2
            ev = np.linalg.eigvalsh(ah)
            worst[k] = float(ev[0])
    for k in sorted(worst, key=lambda x: worst[x])[:8]:
        print(f"   {k}: lambda_min = {worst[k]:.6e}")
    OUT["certificate_blocks_min_eig"] = worst
except Exception as ex:  # pragma: no cover
    print("   could not load:", ex)

v = json.load(open(W4 + "w4_verify.json"))
print(f"   w4_verify.json: min_eig_W = {v['min_eig_W']:.6e}, min_eig_G21 = {v['min_eig_G21']:.6e}")
print(f"   mp recheck W  : {v['mp_min_eig_W_worst_block']}")
print(f"   mp recheck G21: {v['mp_min_eig_G21_worst_block']}")
s1 = json.load(open(W4 + "w4_slice_sdp.json"))
s2 = json.load(open(W4 + "w4_slice_sdp2.json"))
print(f"   leg 1 (SCS primal): t* = {s1['primal_t']:.4e}, dual_status = {s1['dual_status']},"
       f" dual_value = {s1['dual_value']}, R_TRACE = {s1['R_TRACE']}")
print(f"   leg 2 (SCS dual)  : dual_status = {s2['dual_status']}, dual_value = {s2['dual_value']:.6e}")
OUT["sdp_legs"] = dict(primal_t=s1["primal_t"], dual_status_1=s1["dual_status"],
                       dual_value_2=s2["dual_value"], R_TRACE=s1["R_TRACE"])

json.dump(OUT, open("artifacts/logs_nptbe_p2_20260729/P4/p4_w4_audit.json", "w"),
          indent=1, default=str)
print("\nwrote artifacts/logs_nptbe_p2_20260729/P4/p4_w4_audit.json")
