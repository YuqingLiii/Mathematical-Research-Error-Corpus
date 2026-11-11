"""R7 reviewer script (independent): the remaining audits.

(A) VALUE-vs-FORMULA (rule 7f): the definitional slope gate, done with MY OWN entropies.
    Ic_2(rho_eps) = S(Lambda^(2)(rho_eps)) - S(Lambda^c(2)(rho_eps)) in nats, computed at
    60 decimal digits from the CHANNEL FORMULA (B side, no Kraus) and from the Kraus set
    (E side, unavoidable), for rho_eps = (1-eps) P_Psi + eps phi with phi the top
    eigenprojector of my exact D_Psi.  Confirms that lambda_max(D_Psi) really is the
    eps*log(1/eps) coefficient of the raw coherent information, independently of D_Psi.
(B) PER-USE NORMALISATION AUDIT of the "n=2 beats n=1 by 17%" claim.
(C) O(3)xO(3) orbit collapse of the 13 "structured families".
(D) x-independence of r (claim 2) at 6 rational x for 5 families.
(E) Independent audit of the refuted F2 false positive at x = 2/5 (the executor's own
    float incumbent, read from sweep_F2.json): singular values, kernel-threshold
    sensitivity, and MY OWN definitional slope measurement at that float point.
(F) A small independent float sweep on the F1 chart at the strip grid (corroboration).
"""
import json
import sys

import mpmath as mp
import numpy as np
import sympy as sp

from whgap_r7_exact import (Ahat, Bhat, FAMILIES, IDX, csq_of, nsd_certificate, u0, vec,
                            weight_operator)

mp.mp.dps = 60
OUT = {}

Anp = [np.array(Ahat[i], dtype=float) for i in range(4)]


# ------------------------------------------------------------------ numerics helpers
def kraus_np(xv):
    return [np.sqrt(1 - xv) * np.eye(3)] + [np.sqrt(xv / 2) * np.array(Ahat[i + 1], dtype=float)
                                            for i in range(3)]


def W_list_mp(xv):
    ca = [mp.sqrt(1 - xv)] + [mp.sqrt(xv / 2)] * 3
    Ws = []
    for (a, b) in IDX:
        Bh = mp.matrix(9, 9)
        Bnp = np.array(Bhat[IDX.index((a, b))], dtype=float)
        for i in range(9):
            for j in range(9):
                Bh[i, j] = mp.mpf(Bnp[i, j])
        Ws.append(ca[a] * ca[b] * Bh)
    return Ws


def lam1_direct_mp(Z, xv):
    R = mp.matrix(9, 9)
    for j in range(3):
        for k in range(3):
            for jp in range(3):
                for kp in range(3):
                    pt = sum(Z[3 * p + k, 3 * p + kp] for p in range(3))
                    R[3 * j + k, 3 * jp + kp] = ((1 - xv) * Z[3 * j + k, 3 * jp + kp]
                                                 + xv / 2 * ((1 if j == jp else 0) * pt
                                                             - Z[3 * jp + k, 3 * j + kp]))
    return R


def lam2_direct_mp(Z, xv):
    R = mp.matrix(9, 9)
    for j in range(3):
        for k in range(3):
            for jp in range(3):
                for kp in range(3):
                    pt = sum(Z[3 * j + p, 3 * jp + p] for p in range(3))
                    R[3 * j + k, 3 * jp + kp] = ((1 - xv) * Z[3 * j + k, 3 * jp + kp]
                                                 + xv / 2 * ((1 if k == kp else 0) * pt
                                                             - Z[3 * j + kp, 3 * jp + k]))
    return R


def entropy_mp(H):
    _, Q = mp.eighe(H)
    ev = mp.eighe(H)[0]
    s = mp.mpf(0)
    for lv in ev:
        lv = mp.re(lv)
        if lv > mp.mpf(10) ** (-mp.mp.dps + 8):
            s -= lv * mp.log(lv)
    return s


def Ic2_mp(rho, xv, Ws):
    outB = lam2_direct_mp(lam1_direct_mp(rho, xv), xv)          # channel formula, no Kraus
    outE = mp.matrix(16, 16)
    for m in range(16):
        for n in range(16):
            acc = mp.mpf(0)
            Wm, Wn = Ws[m], Ws[n]
            # Tr(W_m rho W_n^dag) ; W real
            T = Wm * rho * Wn.T
            for i in range(9):
                acc += T[i, i]
            outE[m, n] = acc
    return entropy_mp(outB) - entropy_mp(outE)


def mp_from_sympy(Mx, n):
    R = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            v = complex(Mx[i, j])
            R[i, j] = mp.mpc(v.real, v.imag)
    return R


def slope_table(Mexact, xv_rat, tag):
    xv = mp.mpf(sp.Rational(xv_rat).p) / sp.Rational(xv_rat).q
    D, info = weight_operator(Mexact, sp.Rational(xv_rat), crosschecks=False)
    isnsd, coeffs, lmax, _ = nsd_certificate(D)
    Dm = mp_from_sympy(D, 9)
    ev, Q = mp.eighe(Dm)
    top = max(range(9), key=lambda i: mp.re(ev[i]))
    phi_v = mp.matrix([Q[i, top] for i in range(9)])
    phi = mp.matrix(9, 9)
    for i in range(9):
        for j in range(9):
            phi[i, j] = phi_v[i] * mp.conj(phi_v[j])
    Psi = vec(Mexact)
    Pm = mp_from_sympy(sp.Matrix(sp.simplify(Psi * Psi.conjugate().T
                                             / (Psi.conjugate().T * Psi)[0, 0])), 9)
    Ws = W_list_mp(xv)
    rows = []
    for e in ("1e-8", "1e-12", "1e-16", "1e-20"):
        eps = mp.mpf(e)
        rho = (1 - eps) * Pm + eps * phi
        ic = Ic2_mp(rho, xv, Ws)
        rows.append({"eps": e, "Ic2": mp.nstr(ic, 12),
                     "ratio_Ic2_over_eps_log_1_over_eps": mp.nstr(ic / (eps * mp.log(1 / eps)), 12)})
    return {"tag": tag, "x": str(xv_rat), "r": info["r"], "m_B": info["m_B"],
            "lambda_max_exact": str(lmax) if lmax is not None else "0",
            "lambda_max_float": (float(lmax) if lmax is not None else 0.0),
            "top_eigenvalue_of_D_mp": mp.nstr(mp.re(ev[top]), 15), "slope_rows": rows}


# ------------------------------------------------------------------------- (A) + (B)
if "A" in sys.argv or not sys.argv[1:]:
    OUT["A_slope_gates"] = [
        slope_table(FAMILIES["iso_prod_a  M=u0 u0^T"], sp.Rational(7, 20), "iso-product, x=7/20"),
        slope_table(FAMILIES["typeE  M=diag(1,1,0)"], sp.Rational(7, 20), "type-E, x=7/20"),
    ]
    d1 = sp.Rational(13, 132)
    lE = sp.Rational(1102933, 9570000)
    OUT["B_per_use_audit"] = {
        "d1(7/20)_n1_coefficient": str(d1), "d1_float": float(d1),
        "typeE_n2_coefficient": str(lE), "typeE_float": float(lE),
        "ratio_unnormalised": float(lE / d1),
        "additive_baseline_2*d1": float(2 * d1),
        "n2_coefficient_PER_CHANNEL_USE_(lambda_max/2)": float(lE / 2),
        "n1_coefficient_per_channel_use": float(d1),
        "per_use_ratio_n2_over_n1": float(lE / (2 * d1)),
        "n2_is_stronger_per_use": bool(lE / 2 > d1),
    }

# ---------------------------------------------------------------------------- (C)
if "C" in sys.argv or not sys.argv[1:]:
    def rot(i, j, th):
        O = sp.eye(3)
        O[i, i] = sp.cos(th); O[j, j] = sp.cos(th)
        O[i, j] = -sp.sin(th); O[j, i] = sp.sin(th)
        return O

    Sg = sp.diag(1, -1, 1)
    R45 = rot(0, 1, sp.pi / 4)
    cyc = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    pairs = [
        ("(a) u0u0^T  ->  (d) u0 u0bar^T", u0 * u0.T, u0 * u0.conjugate().T, sp.eye(3), Sg),
        ("(a) u0u0^T  ->  (c) u v^T both iso (v = rot(u0))", u0 * u0.T,
         u0 * (rot(1, 2, sp.pi / 3) * u0).T, sp.eye(3), rot(1, 2, sp.pi / 3)),
        ("(e1) diag(1,1,0) -> (e3) diag(1,-1,0)", sp.diag(1, 1, 0), sp.diag(1, -1, 0),
         sp.eye(3), Sg),
        ("(e3) diag(1,-1,0) -> (e2) E12+E21", sp.diag(1, -1, 0),
         sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]), R45, R45),
        ("(b) I -> (b2) cyclic O", sp.eye(3), cyc, sp.eye(3), cyc.T),
    ]
    res = []
    for name, M1, M2, O1, O2 in pairs:
        img = sp.simplify(O1 * M1 * O2.T)
        ok_orth = (sp.simplify(O1.T * O1) == sp.eye(3)) and (sp.simplify(O2.T * O2) == sp.eye(3))
        # equality up to nonzero complex scalar
        ratio = None
        for i in range(3):
            for j in range(3):
                if sp.simplify(M2[i, j]) != 0:
                    ratio = sp.simplify(img[i, j] / M2[i, j]); break
            if ratio is not None:
                break
        same = bool(sp.simplify(img - ratio * M2) == sp.zeros(3, 3)) and ratio != 0
        res.append({"pair": name, "O1,O2 real orthogonal": bool(ok_orth),
                    "image == scalar * target": same, "scalar": str(ratio)})
    OUT["C_orbit_collapse"] = res
    # covariance of D under M -> O1 M O2^T (spectrum invariance), at one rational x
    xr = sp.Rational(9, 20)
    M1 = FAMILIES["typeE  M=diag(1,1,0)"]
    O1, O2 = rot(0, 2, sp.pi / 3), rot(1, 2, sp.pi / 4)
    D1, _ = weight_operator(M1, xr, crosschecks=False)
    D2_, _ = weight_operator(sp.simplify(O1 * M1 * O2.T), xr, crosschecks=False)
    Kron = sp.Matrix(sp.kronecker_product(O1, O2))
    OUT["C_covariance_identity_D_transforms"] = bool(
        sp.simplify(D2_ - Kron * D1 * Kron.T) == sp.zeros(9, 9))

# ---------------------------------------------------------------------------- (D)
if "D" in sys.argv or not sys.argv[1:]:
    rows = []
    for name in ("iso_prod_a  M=u0 u0^T", "P3c_r6  M=(u0+e3)u0^T", "typeE  M=diag(1,1,0)",
                 "P3g_r8  M=u0(1,0,2)^T+(0,1,1)u0^T", "maxent  M=I"):
        Mx = FAMILIES[name]
        U = sp.Matrix.hstack(*[vec(Ahat[a] * Mx * Ahat[b].T) for (a, b) in IDX])
        rU = U.rank()
        ranks = []
        for xr in (sp.Rational(1, 10), sp.Rational(7, 20), sp.Rational(2, 5),
                   sp.Rational(9, 20), sp.Rational(11, 20), sp.Rational(9, 10)):
            GB = sp.zeros(9, 9)
            Psi = vec(Mx)
            P = sp.simplify(Psi * Psi.conjugate().T / (Psi.conjugate().T * Psi)[0, 0])
            for m, (a, b) in enumerate(IDX):
                GB += csq_of(a, xr) * csq_of(b, xr) * Bhat[m] * P * Bhat[m].T
            Gh = sp.Matrix(16, 16, lambda m, n: sp.simplify((Bhat[m] * P * Bhat[n].T).trace()))
            ranks.append((str(xr), int(sp.simplify(GB).rank()), int(Gh.rank())))
        rows.append({"family": name, "rank_of_U (x-free)": int(rU),
                     "(x, rank G_B, rank Ghat)": ranks,
                     "x_independent": len({t[1] for t in ranks}) == 1 and all(t[1] == rU for t in ranks)})
    OUT["D_x_independence"] = rows

# ---------------------------------------------------------------------------- (E)
def float_weight_operator(Mv, xv, rel_floor=1e-6):
    """float D_Psi with an explicit relative kernel floor; returns (D, mB, mE, gapinfo)."""
    Psi = Mv.reshape(9)
    Psi = Psi / np.linalg.norm(Psi)
    P = np.outer(Psi, Psi.conj())
    Ks = kraus_np(xv)
    Ws = [np.kron(Ka, Kb) for Ka in Ks for Kb in Ks]
    GB = sum(W @ P @ W.conj().T for W in Ws)
    GE = np.array([[np.trace(Wm @ P @ Wn.conj().T) for Wn in Ws] for Wm in Ws])

    def kernel(H, n):
        ev, V = np.linalg.eigh(H)
        top = ev[-1]
        keep = ev > rel_floor * top
        idx = np.where(~keep)[0]
        gap = (ev[keep].min() / abs(ev[~keep]).max()) if (keep.any() and (~keep).any()) else np.inf
        return V[:, idx], gap

    NB, gB = kernel(GB, 9)
    NE, gE = kernel(GE, 16)
    PiB = NB @ NB.conj().T
    PiE = NE @ NE.conj().T
    MB = sum(W.conj().T @ PiB @ W for W in Ws)
    ME = sum(PiE[m, n] * Ws[m].conj().T @ Ws[n] for m in range(16) for n in range(16))
    D = MB - ME
    return D, NB.shape[1], NE.shape[1], gB, gE


if "E" in sys.argv or not sys.argv[1:]:
    js = json.load(open("artifacts/logs_whgap_p13b_20260730/sweep_F2.json"))
    row = [r for r in js["rows"] if abs(r["x"] - 0.4) < 1e-12][0]
    Mv = np.array([[complex(s) for s in rr] for rr in row["Mbest"]])
    sv = np.linalg.svd(Mv, compute_uv=False)
    rec = {"executor_reported_best": row["best"], "singular_values": [float(s) for s in sv],
           "sigma2_over_sigma1": float(sv[1] / sv[0]), "sigma3_over_sigma1": float(sv[2] / sv[0]),
           "threshold_sensitivity": []}
    for fl in (1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-9, 1e-11):
        D, mB, mE, gB, gE = float_weight_operator(Mv, 0.4, rel_floor=fl)
        rec["threshold_sensitivity"].append(
            {"rel_floor": fl, "m_B": int(mB), "m_E": int(mE),
             "lambda_max": float(np.linalg.eigvalsh(D)[-1]),
             "gapB": float(gB), "gapE": float(gE)})
    # my own definitional slope measurement at that float point (floor 1e-6, as executor used)
    D, mB, mE, gB, gE = float_weight_operator(Mv, 0.4, rel_floor=1e-6)
    ev, V = np.linalg.eigh(D)
    phi_v = V[:, -1]
    Psi = Mv.reshape(9); Psi = Psi / np.linalg.norm(Psi)
    Pm = mp.matrix(9, 9); Ph = mp.matrix(9, 9)
    for i in range(9):
        for j in range(9):
            Pm[i, j] = mp.mpc(complex(Psi[i] * np.conj(Psi[j])))
            Ph[i, j] = mp.mpc(complex(phi_v[i] * np.conj(phi_v[j])))
    Ws = W_list_mp(mp.mpf("0.4"))
    slopes = []
    for e in ("1e-6", "1e-8", "1e-10", "1e-14"):
        eps = mp.mpf(e)
        rho = (1 - eps) * Pm + eps * Ph
        ic = Ic2_mp(rho, mp.mpf("0.4"), Ws)
        slopes.append({"eps": e, "Ic2": mp.nstr(ic, 10),
                       "ratio": mp.nstr(ic / (eps * mp.log(1 / eps)), 10)})
    rec["my_definitional_slope_at_float_point"] = slopes
    rec["predicted_slope_from_float_D"] = float(ev[-1])
    OUT["E_false_positive_audit"] = rec

# ---------------------------------------------------------------------------- (F)
if "F" in sys.argv or not sys.argv[1:]:
    rng = np.random.default_rng(7302026)
    u0n = np.array([1, 1j, 0]) / np.sqrt(2)
    res = []
    for xv in (0.35, 0.39, 0.40, 0.42, 0.45, 0.49):
        best = -1.0
        for _ in range(400):
            a = rng.normal(size=3) + 1j * rng.normal(size=3)
            y = rng.normal(size=3) + 1j * rng.normal(size=3)
            Mv = np.outer(u0n, a) + np.outer(y, u0n)
            if np.linalg.norm(Mv) < 1e-9:
                continue
            Mv /= np.linalg.norm(Mv)
            D, mB, mE, gB, gE = float_weight_operator(Mv, xv, rel_floor=1e-6)
            if mB == 0:
                continue
            lm = float(np.linalg.eigvalsh(D)[-1])
            if lm > best:
                best = lm
        res.append({"x": xv, "best_lambda_max_random_400_F1_points": best})
    OUT["F_independent_F1_random_probe"] = res

print(json.dumps(OUT, indent=1, default=str))
tagname = "".join(sys.argv[1:]) or "all"
with open(f"artifacts/logs_whgap_p13b_20260730/r7_checks_{tagname}.json", "w", newline="\n") as fh:
    json.dump(OUT, fh, indent=1, default=str)
