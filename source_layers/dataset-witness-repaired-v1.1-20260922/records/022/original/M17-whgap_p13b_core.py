"""WHGAP P13-B core: 2-copy weight operator D_Psi for the noisy Werner-Holevo family.

Frozen conventions (R5 commission sec.1, inherited):
  Lambda_x(Y) = (1-x) Y + (x/2) (Tr(Y) 1 - Y^T)  on qutrits, x in (0,1)
  Kraus: K_0 = sqrt(1-x) 1 ; K_i = sqrt(x/2) A_i, (A_i)_{jk} = eps_{ijk}, i = 1,2,3
  Complement (padded, 4-dim): Lambda^c(Y)_{ab} = Tr(K_a Y K_b^dag) = Tr(K_a Y K_b^T)
  2-copy: Kraus K_a tensor K_b, (a,b) in {0..3}^2  ->  16-dim padded environment.

Index conventions used everywhere in this file:
  C^9 basis index  n = 3*j + k   with  vec(M)_{3j+k} = M_{jk}
      so (K_a tensor K_b) vec(M) = vec(K_a M K_b^T).
  C^16 environment index  m = 4*a + b.

Convention-safe construction of the weight operator: D_Psi is defined ONLY through
  Tr[D_Psi phi] = w_B(phi) - w_E(phi),
  w_B(phi) = Tr[Pi_B (Lambda tensor Lambda)(phi)],
  w_E(phi) = Tr[Pi_E (Lambda^c tensor Lambda^c)(phi)],
and is obtained by evaluating that linear functional on the 81 matrix units E_pq:
  V_pq := w_B(E_pq) - w_E(E_pq),  then  D_Psi = V^T.
No adjoint formula is ever hand-transposed.

Author: fresh executor instance (P13-B), 2026-07-30. Licenses no status by itself.
"""

import numpy as np


# ----------------------------------------------------------------- Kraus data

def levi_civita():
    A = [np.zeros((3, 3)) for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                # eps_{ijk} with 1-based labels i,j,k = index+1
                p = (i, j, k)
                if len(set(p)) < 3:
                    continue
                # sign of the permutation (0,1,2) -> p
                sgn = 1
                q = list(p)
                for a in range(3):
                    for b in range(a + 1, 3):
                        if q[a] > q[b]:
                            sgn = -sgn
                A[i][j, k] = sgn
    return A


A_LIST = levi_civita()


def kraus(x):
    """[K_0, K_1, K_2, K_3] as 3x3 float arrays."""
    t = np.sqrt(1.0 - x)
    s = np.sqrt(x / 2.0)
    return [t * np.eye(3)] + [s * A for A in A_LIST]


def kraus2(x):
    """The 16 two-copy Kraus operators K_a tensor K_b, indexed m = 4a+b."""
    K = kraus(x)
    return [np.kron(K[a], K[b]) for a in range(4) for b in range(4)]


def channel2(x, Y):
    """(Lambda tensor Lambda)(Y) for a 9x9 matrix Y."""
    out = np.zeros((9, 9), dtype=complex)
    for W in kraus2(x):
        out += W @ Y @ W.conj().T
    return out


def complement2(x, Y):
    """(Lambda^c tensor Lambda^c)(Y)_{(ab),(cd)} = Tr[(K_a x K_b) Y (K_c x K_d)^dag], 16x16."""
    W = kraus2(x)
    out = np.zeros((16, 16), dtype=complex)
    for m in range(16):
        for n in range(16):
            out[m, n] = np.trace(W[m] @ Y @ W[n].conj().T)
    return out


# ------------------------------------------------------------- state plumbing

def vec(M):
    """vec(M)_{3j+k} = M_{jk}."""
    return np.asarray(M, dtype=complex).reshape(9)


def unvec(v):
    return np.asarray(v, dtype=complex).reshape(3, 3)


def normalize(M):
    M = np.asarray(M, dtype=complex)
    return M / np.linalg.norm(M)


def span_matrix(x, M):
    """16x9 matrix whose rows are vec(K_a M K_b^T); its rank is r = rank Lambda^(2)(P_Psi)."""
    K = kraus(x)
    rows = []
    for a in range(4):
        for b in range(4):
            rows.append(vec(K[a] @ M @ K[b].T))
    return np.array(rows)


# ------------------------------------------------------- rank / kernel policy

def kernel_projector(H, gap_factor=1e6, cond_floor=1e-6):
    """Orthogonal projector onto ker H for Hermitian PSD H, with the pre-registered
    rank discipline.  Returns (Pi, m, ok, diag) where ok is False when the point is
    rank-ambiguous, i.e. when EITHER
      (i) the accepted zero cluster is not separated from the kept spectrum by
          >= gap_factor times the zero-cluster magnitude   [pre-registered criterion], OR
      (ii) the smallest kept eigenvalue is below cond_floor * ||H||   [conditioning
          criterion added 2026-07-30 mid-run, see the artifact section 8.1: with an exact
          zero cluster at machine-epsilon level, criterion (i) alone admits points sitting
          10^-8 away from a DEEPER stratum, where the float kernel projector -- and hence
          D_Psi -- is unreliable by O(10^-2).  Such a point produced a spurious
          lam_max = 0.02 at x = 2/5 that the definitional slope gate refuted.]
    """
    w, V = np.linalg.eigh(H)
    w = np.real(w)
    scale = max(np.max(np.abs(w)), 1e-300)
    tol = 1e-9 * scale                     # provisional zero threshold
    idx0 = [i for i in range(len(w)) if abs(w[i]) <= tol]
    idx1 = [i for i in range(len(w)) if abs(w[i]) > tol]
    m = len(idx0)
    zmag = max([abs(w[i]) for i in idx0], default=0.0)
    smin = min([abs(w[i]) for i in idx1], default=np.inf)
    # spectral-gap discipline: smallest kept eigenvalue must exceed gap_factor * zero cluster
    if m == 0:
        ok = True
    elif zmag == 0.0:
        ok = bool(np.isinf(smin) or smin > 0)
    else:
        ok = bool(smin > gap_factor * zmag)
    if m > 0 and not np.isinf(smin):
        ok = bool(ok and smin > cond_floor * scale)      # conditioning criterion (ii)
    Pi = np.zeros_like(H)
    for i in idx0:
        v = V[:, i:i + 1]
        Pi = Pi + v @ v.conj().T
    diag = dict(spectrum=w.tolist(), zero_mag=zmag, min_kept=(None if np.isinf(smin) else smin),
                scale=scale, m=m, cond_ratio=(None if np.isinf(smin) else smin / scale))
    return Pi, m, ok, diag


def weight_operator(x, M, gap_factor=1e6):
    """Exact-in-float D_Psi (3x3? no: 9x9) for the 2-copy pure input Psi = vec(M).

    Returns dict with D (9x9 Hermitian), ranks, kernel dims, gap diagnostics."""
    M = np.asarray(M, dtype=complex)
    Psi = vec(M)
    P = np.outer(Psi, Psi.conj())
    GB = channel2(x, P)
    GE = complement2(x, P)
    PiB, mB, okB, dB = kernel_projector(GB, gap_factor)
    PiE, mE, okE, dE = kernel_projector(GE, gap_factor)
    # V_pq = w_B(E_pq) - w_E(E_pq), evaluated with no hand-written adjoint anywhere
    V = np.zeros((9, 9), dtype=complex)
    for p in range(9):
        for q in range(9):
            E = np.zeros((9, 9), dtype=complex)
            E[p, q] = 1.0
            wB = np.trace(PiB @ channel2(x, E))
            wE = np.trace(PiE @ complement2(x, E))
            V[p, q] = wB - wE
    D = V.T
    return dict(D=D, mB=mB, mE=mE, okB=okB, okE=okE, diagB=dB, diagE=dE,
                rankB=9 - mB, rankE=16 - mE, GB=GB, GE=GE, PiB=PiB, PiE=PiE)


def weight_operator_fast(x, M, gap_factor=1e6):
    """Same D_Psi, vectorised: builds the two linear maps as 81x81 / 81x256 tensors once."""
    M = np.asarray(M, dtype=complex)
    Psi = vec(M)
    P = np.outer(Psi, Psi.conj())
    GB = channel2(x, P)
    GE = complement2(x, P)
    PiB, mB, okB, dB = kernel_projector(GB, gap_factor)
    PiE, mE, okE, dE = kernel_projector(GE, gap_factor)
    W = np.array(kraus2(x))                       # (16,9,9)
    # w_B(phi) = sum_m Tr[PiB W_m phi W_m^dag] = Tr[ (sum_m W_m^dag PiB W_m) phi ]
    MB = np.einsum('mij,ik,mkl->jl', W.conj(), PiB, W)
    # w_E(phi) = Tr[PiE Lambda^{c2}(phi)] = sum_{m,n} PiE[m,n] Tr[W_n phi W_m^dag]
    #          = Tr[ (sum_{m,n} PiE[m,n] W_m^dag W_n) phi ]
    ME = np.zeros((9, 9), dtype=complex)
    for m_ in range(16):
        for n_ in range(16):
            c = PiE[m_, n_]
            if c != 0:
                ME += c * (W[m_].conj().T @ W[n_])
    D = MB - ME
    return dict(D=D, mB=mB, mE=mE, okB=okB, okE=okE, diagB=dB, diagE=dE,
                rankB=9 - mB, rankE=16 - mE)


# ---------------------------------------------------- fast radical-free evaluator

BH_INT = None      # 16 integer 9x9 matrices Bhat_m = Ahat_a kron Ahat_b
BB_INT = None      # 256 integer 9x9 matrices Bhat_m^T Bhat_n


def _init_int():
    global BH_INT, BB_INT
    if BH_INT is not None:
        return
    AH = [np.eye(3)] + [A.copy() for A in A_LIST]
    BH_INT = np.array([np.kron(AH[a], AH[b]) for a in range(4) for b in range(4)])
    BB_INT = np.einsum('mji,njk->mnik', BH_INT, BH_INT)      # (Bhat_m^T Bhat_n)_{ik}


def csq2(x):
    """c_m^2 for m = 4a+b, c_0^2 = 1-x, c_i^2 = x/2."""
    c = np.array([1.0 - x, x / 2, x / 2, x / 2])
    return np.array([c[a] * c[b] for a in range(4) for b in range(4)])


def weight_operator_rf(x, M, gap_factor=1e6):
    """Radical-free fast evaluator: identical mathematics to weight_operator(), but all
    x-dependence carried by the scalars c_m^2 (B side) and c_m c_n (E side)."""
    _init_int()
    M = np.asarray(M, dtype=complex)
    Psi = vec(M)
    c2 = csq2(x)
    c1 = np.sqrt(c2)
    # B side
    ZB = np.einsum('mij,j->mi', BH_INT, Psi)                     # z_m = Bhat_m Psi  (16,9)
    GB = np.einsum('m,mi,mj->ij', c2, ZB, ZB.conj())             # sum_m c_m^2 z_m z_m^dag
    PiB, mB, okB, dB = kernel_projector(GB, gap_factor)
    # E side: G_E[m,n] = c_m c_n conj(z_m^dag z_n)   (Gram of the w_m = c_m z_m)
    Gr = np.einsum('m,mi,n,ni->mn', c1, ZB.conj(), c1, ZB)       # = w_m^dag w_n
    GE = Gr.T.copy()                                             # Lambda^{c2}(P)[m,n] = w_n^dag w_m
    PiE, mE, okE, dE = kernel_projector(GE, gap_factor)
    MB = np.einsum('m,mji,jk,mkl->il', c2, BH_INT, PiB, BH_INT)
    Y = np.outer(c1, c1) * PiE
    ME = np.einsum('mn,mnik->ik', Y, BB_INT)
    D = MB - ME
    return dict(D=D, mB=mB, mE=mE, okB=okB, okE=okE, diagB=dB, diagE=dE,
                rankB=9 - mB, rankE=16 - mE)


def lam_max(D):
    w = np.linalg.eigvalsh((D + D.conj().T) / 2)
    return float(np.max(np.real(w)))


# ------------------------------------------------------------ Ic for the gate

def entropy(w, tol=0.0):
    w = np.real(np.asarray(w))
    s = 0.0
    for v in w:
        if v > tol:
            s -= v * np.log(v)
    return s


def Ic2(x, M, phi, eps):
    """Coherent information of rho_eps = (1-eps) P_Psi + eps phi under Lambda^{tensor 2}."""
    Psi = vec(np.asarray(M, dtype=complex))
    P = np.outer(Psi, Psi.conj())
    rho = (1 - eps) * P + eps * np.asarray(phi, dtype=complex)
    SB = entropy(np.linalg.eigvalsh(channel2(x, rho)), tol=1e-300)
    SE = entropy(np.linalg.eigvalsh(complement2(x, rho)), tol=1e-300)
    return SB - SE


def validate_slope(x, M, phi, D, epss=(1e-6, 1e-8, 1e-10), rtol=0.25):
    """Definitional validation of a candidate: does the RAW coherent information really have
    the predicted eps log(1/eps) slope?  Returns (ok, predicted, measured_ratios).
    The remainder in Ic_2 = c*eps log(1/eps) + O(eps) decays only like 1/log(1/eps), so the
    test is a sign + magnitude test, not a precision test."""
    pred = float(np.real(np.trace(D @ phi)))
    vals = [Ic2(x, M, phi, e) / (e * np.log(1 / e)) for e in epss]
    if pred > 0:
        ok = all(v > 0 for v in vals) and abs(vals[-1] - pred) <= rtol * abs(pred) * 4
    else:
        ok = all(v <= 1e-12 for v in vals)
    return bool(ok), pred, vals
