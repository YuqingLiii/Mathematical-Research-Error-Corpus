---
id: "NPTBE.k3.R1.m1"
node_file: "entanglement-distillation/npt-bound-entanglement/proof-dag/nodes/NPTBE.k3.R1.m1.md"
aliases: ["M1n"]
kind: LEAF
role: proof
status: CONJECTURED
status_source: "fleet W2 2026-07-29 (survived 2240-sample screening, saturated on tight set; pending-review)"
disposition: null
parents: ["NPTBE.k3.R1"]
children: []
related: ["NPTBE.k3.R1.facet", "NPTBE.k3.R1.blockrec", "NPTBE.k3.R4"]
---

# NPTBE.k3.R1.m1 — the M1 exchange-matrix lemma (would prove the endpoint at EVERY k and d)

## Claim

With K = tensor_{i=1}^k (I - F_i/2) >= 0 on H tensor H, H = (C^d)^{tensor k}: for ALL vectors
x1, x2, y1, y2 in H (no rank/balancing/normalization hypothesis),
|<y2 (x) x1, K (y1 (x) x2)>| <= sqrt(<x1 (x) y1, K(x1 (x) y1)> <x2 (x) y2, K(x2 (x) y2)>) —
equivalently the 2x2 exchange matrix G_pq = <x_p (x) y_q, K (x_q (x) y_p)> is PSD. Via the
verified identity q_k(-1/2, C) = sum_pq G_pq for C = |x1><y1| + |x2><y2|, M1 implies
q_k >= (sqrt(G_11) - sqrt(G_22))^2 >= 0: the FULL endpoint conjecture at alpha = -1/2, every k,
every d. Stronger variant M2 (also screening-surviving): the crossed Gram
Gamma_{(pq),(rs)} = <x_p (x) y_q, K(x_r (x) y_s)> is PPT in the 2x2 label system. **[CONJECTURED]**

## Role in DAG

The sharpest object of the campaign: a three-line chain from one Cauchy-Schwarz-with-diagonal-norms
lemma to the whole endpoint theorem. It is exactly the repair of the crossed-norm closure that
batch 1-2 refuted (crossed version fails at tight vertices with ratio 0.33-0.54; diagonal version
is saturated at ratio exactly 1.000000000 there).

## Current status

CONJECTURED — but ROLE CORRECTED 2026-07-30 (phase-2, P1a + P1b independently, replicated
derivations): **M1 <=> M2 <=> the endpoint conjecture (E_{k,d}) itself** — c^dag G c sweeps
q_k over all rank-<=2 matrices, so this node is a REFORMULATION, not a lemma; the phase-1
"three lines to the theorem" chain was circular and the screening evidence coincides with
endpoint screening. Salvaged reformulation: (E) <=> Phi_{1/2}^{tensor k} is 2-positive
(tensor-stable-positivity form). Unconditional partial results now attached here (pending-review):
product-class theorem (endpoint holds for all product vectors, every k, d, alpha >= -1/2, via
Hadamard/Schur factorization G = o_i G^(i)); splitting corollary (hard core = vectors entangled
across every cut); k=1 closed symbolically + tensor-lift lemma; exact endpoint necessity
(product violation for every alpha < -1/2, every k). The decision-layer E_S reduction note is
REFUTED (every non-empty E^S indefinite; k=1 Pluecker lemma false; class-level no-go for ALL
positive decompositions — rank-3 witness). Evidence: artifacts/logs_nptbe_p2_20260729/P1a,P1b;
[phase-2 synthesis](../../../../artifacts/nptbe_k3_p2_synthesis_20260730.md);
[phase-1 synthesis](../../../../artifacts/nptbe_k3_fleet_phase1_synthesis_20260729.md).

## Dependencies

- Identity q_k = sum_pq G_pq (W2, verified 1e-15; pending-review).
- K >= 0 and K_a F = a^k K_{1/a} structure identities (W2, verified; pending-review).

## Work record

- 2026-07-29 — node registered (rule 8b) on reading fleet W2's return, before phase-2 dispatch.
- 2026-07-29 — decision-layer reduction note (unreviewed): K_i = (1/2)(I + 2 Pi_i^asym) gives
  K = 2^{-k} sum_S 2^{|S|} Pi_S with POSITIVE coefficients, so M1 follows if each elementary
  exchange matrix E^S_pq = <x_p (x) y_q, Pi_S(x_q (x) y_p)> is PSD; S = empty is Schur-PSD; k=1
  S={1} reduces to the Pluecker-type inequality |<x1^y2, x2^y1>|^2 <= ||x1^y1||^2 ||x2^y2||^2.
  Phase-2 task P1 screens E_S numerically FIRST, then attempts proofs.

## Evidence

- 2026-07-29 — W2 screening table + saturation data (pending-review): see Current status links.

## Adversarial reviews

None yet.

## Open obligations

Phase-2: P1 (prove: E_S route, PPT route, direct 2x2 determinant with structure identities),
P3 (dedicated adversarial refutation at k=4,5, d<=8, structured vector families), P4 (review).
A single certified counterexample kills this node and the M2 variant; report it as headline.

## Status history

- 2026-07-29 — created CONJECTURED (fleet W2; pending-review).
