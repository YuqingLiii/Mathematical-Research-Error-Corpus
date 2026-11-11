# Phase-1 fleet synthesis — NPTBE.k3 new-regime campaign (2026-07-29)

Decision layer: Fable 5. Executors: 5 parallel Opus 4.8 agents (workflow wf_9b775620-c63; 0 errors;
per-agent artifacts + SHA256SUMS under artifacts/logs_nptbe_fleet_20260729/W{1..5}*/;
full structured returns in the workflow journal). All numerics pending-review unless stated.

## Headline

Two INDEPENDENT one-lemma-away proof routes emerged, plus a candidate lemma (M1) that would prove
the endpoint conjecture at EVERY k and d in three lines. No falsification anywhere (W5: d=5,6,8 at
k=3 and k=4 at d=3,4 all clean, with positive controls).

## W5 (R1.facet evidence): falsification sweep NEGATIVE, with controls

1080 rank-2 minimization restarts across (d,k) in {(5,3),(6,3),(8,3),(3,4),(4,4)}: global min
-1.66e-15, every argmin re-certified POSITIVE at 50 digits (mpmath). Facet-direction support value
h_d = 2.000000000 (9 digits) at d=5,6,8; 25-direction support grids at d=5,6 give worst_target =
1.000000000 and maximizers land on the SAME d=4 vertices. Positive controls: alpha=-0.51 gives
clear negatives (-2.18e-2 at d=6); rank-3 at alpha=-1/2 gives -0.500000000 instantly. k=4 does NOT
break. The endpoint conjecture is numerically solid across k and d.

## W1 (R1.zeroman): zero manifold characterized

Dominant component of {G3=0} on rank-2 (d=3,4, predictive test at d=5): the locus where ALL THREE
T_ij C equal a COMMON scalar multiple of one rank-2 orthogonal projector. Local dimension = 12d
(gauge-projected Hessian kernel; validated at d=2 ground truth + tangency retraction test;
predicted-then-measured 60 at d=5). x-image = the d-independent segment x1 = 2 + x3/2,
x2 = (3/2)x3, x3 in [0,2], from vertex (2,0,0) to the non-extreme tight point (3,3,2) — explaining
the reviewer's vertex correction. Invariant-level defining relations COMPLETE:
w_12 = w_13 = w_23 = mu*w_123 (mu = d/2-1), affine nullspace dim exactly 5. Self-corrections
recorded: an osr-based prediction was refuted at d=5 (clustering artifact); product-point Hessian
counts over-read (tangent cone issue) — flagged, unresolved. BONUS (verified d=2..6, 1.2e-15): at
d=4, A = R1R2R3 with R_i = 1 - 2P_i self-adjoint commuting UNITARIES, so the d=4 claim is exactly
"odd-weight mass <= 1/2 on rank-2": ||Pi_- C||^2 <= ||C||^2/2.

## W3 (R1.rep): compression route killed-and-transmuted; block recursion found

(a) The pre-registered compression existence test is structurally VACUOUS (min over local-dim-2
compressions is identically 0) — honest negative on the node's original mechanism. Pinch-to-2-dim
chains also killed (pinched objects leave the rank-2 cone, reach g3 = 1-d/2).
(b) EXACT PINCHING IDENTITY + PINCH LEMMA (derivation, conditional ONLY on the proved k=2 theorem):
for R = C - E_i(C), G3(C) - G3(E_iC) = H_i(R) = sum_{blocks ab} G2(R_ab) >= 0, because every block
of a rank-<=2 matrix has rank <= 2. Unconditional corollary: H_i(C) >= 0, i.e.
G3(C) >= -(1/2)G2(T_iC) (valid but insufficient alone: gives x1 <= 3 + x2/4).
(c) **BLOCK RECURSION (exact identity, basis-free, no d, verified 1e-16 at d=3,4,5):**
    G_k(C) = sum_{a,b} G_{k-1}(C_ab) - (1/2) G_{k-1}(T_i C)
so the k=3 facet claim is EQUIVALENT to: sum_{a,b} G2(C_ab) >= (1/2) G2(T_i C) for rank-<=2 C —
a k=2-form statement with no explicit d (explains the observed d-uniformity), and the natural
k -> k-1 induction skeleton for the WHOLE endpoint conjecture.
(d) SPLIT INDUCTION with ONE missing lemma (CROSS LEMMA): budget identity
G3(C) = G3(PiCPi) + G3(Pi'CPi') + H_i(C - E_iC) - Re G2(T_i(PiCPi), T_i(Pi'CPi')); induction over
local dimensions closes IF for every rank-<=2 C, some 2-dim projector Pi has the cross term <= 0
(equivalently G2(Z) + G2(T_iC - Z) >= G2(T_iC), Z = tr_i[(Pi tensor I)C]). Cross lemma numerics:
min over Pi strictly negative on 100/100 random C (so it is NOT implied by the target — evidence
non-vacuous); = 0 exactly at every tight exemplar; adversarial max of min_Pi cross ~ +1e-11.
Killed simplifications recorded (diagonal-only version FALSE at -1/2; crossed-Schwarz closure
impossible — explains the old crossed-Gram dead end structurally).

## W2 (R4): all four k=2 proofs anatomized; M1 candidate found

All four papers' mechanisms consume the SAME two facts, both k=2-only: (i) complementation
S <-> S^c preserves the coefficient layer only at k=2; (ii) full-swap parity makes the relevant
vectors complex-symmetric (Takagi) only at even k — BGH eq(61) fails at k=3 by a pure parity sign
(K_c^T = -K_c, verified ||K_c - K_c^T||/||K_c|| = 2.000000). The FGP/BGH "geometric heart" is the
SAME constant gamma_k(d); both need gamma_k <= 2^{1-k}, true at k=2 for all d, FALSE at k=3 for
every d >= 3. LP fact: the proved two-copy toolkit + all surviving invariant-level candidates
reaches only 2.833 (target 2) — NO proof in (x1,x2,x3)-invariants alone can work; a proof must see
finer data (dyad/exchange structure).
**M1 (headline surviving candidate; 8 of 14 survived screening on 2240 samples; M1 saturated
exactly on the whole tight set):** with K = tensor_{i=1}^k (I - F_i/2) >= 0 on H tensor H:
    |<y2 (x) x1, K (y1 (x) x2)>|  <=  sqrt(<x1 (x) y1, K(x1 (x) y1)> * <x2 (x) y2, K(x2 (x) y2)>)
for ALL vectors (no rank/balancing hypothesis). Chain: for C = |x1><y1| + |x2><y2|,
q_k(-1/2, C) = d1 + d2 + 2Re<y2 x1, K(y1 x2)> >= (sqrt d1 - sqrt d2)^2 >= 0 — the endpoint theorem
for EVERY k and d. Equivalent forms: exchange matrix G_pq = <x_p (x) y_q, K(x_q (x) y_p)> is PSD
at r=2 (identity q_k = sum_pq G_pq verified 1e-15); stronger M2: the crossed Gram is PPT in the
2x2 label system (min eig(Gamma^{T2}) > 0 on 800 samples, = 0 exactly at tight exemplars).

## W4 (R1.sos): batch-2 obstruction OVERTURNED; quartic route closed exactly

(1) Batch-2's degree-6 slice obstruction was an ARTIFACT of dropping the weight-+1 (2,1) Gram
block: on the corrected maximal rank-preserving slice the complete mixed-weight degree-6 SOS +
minor cone is numerically FEASIBLE (t* = -6.6e-11; baseline reproduces batch-2's -1.33819593246
to 15 digits). (2) Full d=3 degree-6 problem: exact block dims archived (torus-reduced max block
402,543 — HPC territory). (3) The quartic biquadratic SOS route is CLOSED NEGATIVELY with exact
rational Farkas certificates for d=3,4,5,6 (collapses to a 32-scalar LP; feasible only at d=2).

## Decision-layer note (unreviewed): a reduction path for M1

K_i = I - F_i/2 = (1/2)(I + 2 Pi_i^asym), so K = 2^{-k} sum_S 2^{|S|} Pi_S with Pi_S = products of
antisymmetrizers and ALL COEFFICIENTS POSITIVE. Hence M1 follows if for every S the elementary
exchange matrix E^S_pq = <x_p (x) y_q, Pi_S (x_q (x) y_p)> is PSD (r=2). S = empty: E = (X*X) o
(Y*Y)^T, PSD by Schur. k=1, S={1}: E_pq = (1/2)<w_pq, w_qp> with w_pq = x_p wedge y_q — a
Pluecker-type label-transposed Gram; 2x2 PSD reduces to |<x1^y2, x2^y1>|^2 <= ||x1^y1||^2 ||x2^y2||^2.
Screen E_S numerically first; if any E_S fails PSD, the positive-combination route needs weights.

## Phase-2 assignments (nodes registered before dispatch)

P1 prove/refute M1 (multi-angle, incl. E_S reduction + PPT form); P2 prove/refute the cross lemma;
P3 dedicated adversarial falsification of M1/M2/cross at k=4,5 and d up to 8; P4 rule-7 review of
phase-1 numerics + W3's derivation chain (pinch lemma, block recursion, budget identity).
