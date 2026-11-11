# Phase-2 synthesis — NPTBE.k3 (2026-07-30)

Workflow wf_7f31fc9b-fe0 (5 Opus agents; P1a double-executed across the interrupted run = free
independent replication). Artifacts: artifacts/logs_nptbe_p2_20260729/{P1a,P1b,P2,P3,P4}/.
All claims pending-review unless marked as decision-layer-verified.

## Structural verdicts

1. **M1/M2 are NOT lemmas — they are the endpoint conjecture itself.** P1a and P1b independently
   proved M1 <=> M2 <=> (E_{k,d}): c^dag G c = q_k(c1|x1><y1| + c2|x2><y2|) sweeps all rank-<=2
   matrices; Gamma^{T2} = B^dag K^{T2} B similarly. The phase-1 "three lines to the theorem"
   framing was CIRCULAR; M1's screening evidence = endpoint screening evidence. Salvage: the
   endpoint conjecture <=> Phi_{1/2}^{tensor k} is 2-positive (Phi_t(A) = tr(A)I - tA, co-CP at
   t = 1/2) — the standard tensor-stable-positivity formulation.
2. **Decision-layer E_S route REFUTED** (P1a, P1b, P4 independently): every non-empty E^S is
   indefinite (exact witnesses, 0.0 residual); the k=1 Pluecker lemma is FALSE; and a rigorous
   class-level no-go: ANY positive decomposition K = sum c_j A_j has a piece failing PSD at rank 3
   (G itself has eigenvalue -1/2 at the rank-3 witness) — positive-decomposition proofs are closed
   as a CLASS.
3. **CROSS LEMMA REFUTED** (P2; decision-layer verified 2026-07-30 with own code: Fourier family
   |Omega_s> = (1/d)sum|i,j,i+j+s>, C = |O0><O0|+|O1><O1|, rank 2, G3 = 3/2-3/d > 0; cross term
   >= r(d-r)[d-2-2cos(2pi/d)]/d^3 > 0 for ALL Pi, ranks, copies, d >= 3; measured minima match:
   4/27 at d=3 [mine: 0.148372 over 300 random Pi vs bound 0.148148]). P3's contrary "cross
   survives" is explained: its search missed the family (see methodological catch below); P3 did
   correctly identify W3's +1e-11 as an exact zero at 2-dim-support C (trivial-split equality).
   Formal REFUTED awaits rule-6 review (phase-3 Q4).
4. **The split induction is REPAIRABLE (P2): lemma L_H** — for every rank-<=2 C, SOME orthogonal
   two-block split has defect(Pi) := G3(PiCPi) + G3(Pi'CPi') - G3(C) <= 0 ("G3 superadditive
   under some splitting"; via the budget identity defect = cross - H_i(R), so L_H <=> exists Pi:
   cross <= H_i(R), strictly weaker than cross <= 0). L_H holds with wide margins on every tested
   class INCLUDING the cross-lemma counterexamples; saturated exactly at tight C. NEW NODE:
   NPTBE.k3.R1.superadd.

## Unconditional new mathematics (pending-review)

- **Product-class theorem (P1a):** for product vectors, G = Hadamard product of k=1 exchange
  matrices; Schur + k=1 Cauchy-Schwarz PROVE the endpoint on the entire product class, every k,
  every d, every alpha >= -1/2. Splitting corollary: vectors product across any cut reduce to
  smaller k — the hard core is exactly vectors entangled across EVERY cut.
- **k=1 M1 closed (P3):** symbolic eigenvalues {1, alpha^2 sin^4 t/(1+alpha)^2}; holds iff
  alpha >= -1/2. Tensor-lift lemma: any k=1 violation lifts to every k.
- **Endpoint necessity exact (P1a):** product witness gives exchange spectrum
  (1+a)^{k-1}{1, 1+2a}: for a < -1/2 a rank-2 PRODUCT violation exists at every k.
- **Weight-enumerator form (P1b):** q_k(W) = sum_S (1-d/2)^{|S|}||W_S||^2 for general d
  (contains W1's d=4 odd-weight-mass form as a special case).
- **|KF| = K (P1b):** one-line crossed Cauchy-Schwarz, losing exactly 2^k at tight points —
  structural reason no K-metric argument reaches the diagonal bound.

## P4 review of phase 1: MAJOR (core sound, five defects)

Reproduced: all 11 identities (<= 6.6e-16), K-decomposition exact, Farkas certificates valid in
Fraction arithmetic, batch-2 baseline to 15 digits, W5 recerts upgraded to EXACT rational
(positive, no precision caveat). Defects to apply: (A) "d-independent tight polygon / maximizers
land on same d=4 vertices" is FALSE at d >= 5 (W5's own logs + exact product-family explanation)
— d-scope all tight-set claims to d <= 4 pending re-derivation; (B) E_S reduction refuted (above);
(C) W3's "min_Pi cross" numbers mislabelled (inner minimization provably fails on the tight
family) — consistent with P2's refutation; (D) W4's "batch-2 OVERTURNED" is a mis-adjudication:
batch-2's reviewed scope is EXTENDED, not contradicted, and W4's "FEASIBLE" is UNSUPPORTED
(archived Gram blocks non-PSD at -7.7e-11; solver legs disagree by 5 orders) — downgrade to
"undecided on the corrected slice".

## Methodological catch (campaign-wide, P1a + P3)

Random Gaussian screening is nearly BLIND here (high-dim near-orthogonality kills trace
contractions): at alpha = -0.51 where the claim is false, 300 random samples saw nothing while a
two-line product witness violates immediately; P3's first control run missed known violations
until recalibrated. All "survived N random samples" evidence must be down-weighted; structured/
covariant families (Fourier, group orbits, product witnesses) are the real filters.

## Phase-3 plan

Q1/Q2: two independent provers for L_H (direct; and averaging-over-splits). Q3: adversarial on
L_H with structured families (Fourier/covariant, NOT Gaussian). Q4: rule-7 review of the phase-2
derivation layer (equivalences, product theorem, cross refutation, L_H identities) + adjudication
of P2-vs-P3.
