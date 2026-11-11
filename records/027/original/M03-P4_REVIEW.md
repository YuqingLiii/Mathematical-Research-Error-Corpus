# P4 — independent rule-7 review of the NPTBE.k3 phase-1 fleet (2026-07-29)

## Independence statement

I did not author, commission, design, or advise any part of W1–W5, the fleet synthesis, or the
decision-layer notes under review. I was given no desired outcome, no hypothesis to confirm, and
no indication of which findings the decision layer prefers to keep. I received the frozen
definitions, pointers to the material, and the rule-7 checklist, nothing else.

**Disclosure.** An earlier, interrupted pass under this same tag (P4) had written a draft report
and several scripts into this directory before being cut off mid-run (`p4_identities.log` was left
empty). I did **not** inherit its conclusions. I re-derived every identity from the definitions in
this session before opening it, re-ran every load-bearing verification with newly written code, and
I **corrected two of its statements** (items 15 and 28/O-2 below). Where my numbers differ from the
earlier draft's, mine are the ones reported and the difference is stated.

Every number below with a digit in it came from code I wrote
(`tools/nptbe_p2_p4_identities2.py`, `tools/nptbe_p2_p4_exact_recert.py`,
`tools/nptbe_p2_p4_w4_audit.py`, `tools/nptbe_p2_p4_cross_fast.py`). I imported no fleet code and
re-implemented every quantity from the definitions. Where I could not reproduce something within
budget I say so rather than deferring to the artifact.

**Overall verdict: MAJOR.**
The mathematics phase 2 actually stands on is sound: every displayed identity I tested is exact,
every 50-digit re-certification reproduces (I strengthened four of them to *exact* rational
arithmetic), and nothing anywhere falsifies the endpoint conjecture. MAJOR is triggered by five
defects, four of which propagate directly into phase 2:

1. a **false** claim about the tight set, contradicted by W5's own logged data, which invalidates
   the "vertex filter" used to screen proof candidates at d ≥ 5 (**Finding A**);
2. the decision-layer `E_S` reduction — which P1 is instructed to screen first — is **refuted**
   with an explicit two-vector counterexample (**Finding B**);
3. the cross lemma's inner minimisation over Π **provably fails** on the tight family, so W3's
   `min_Π cross` numbers (including the adversarial `+1e-11` maxima that P2/P3 are being told to
   re-certify) are not what they are labelled (**Finding C**);
4. a **mis-adjudicated** "overturning" of batch-2 plus an unsupported "FEASIBLE" (item 33/35);
5. an **over-scoped** impossibility claim, "no invariant-level proof can work" (item 16).

---

## 7c — ANCHORING BAN: my derivations, written before reading W2/W3

Recorded in `P4_INDEPENDENT_DERIVATION_PRE_READ.md`. In this session I re-derived, from the frozen
definitions and before opening any W2/W3 derivation, node file, or fleet script:

| identity | my derivation | agrees with fleet? |
|---|---|---|
| `q_k(C) = Σ_{p,q} G_pq` | sum `⟨x_p⊗y_q, F_S(x_q⊗y_p)⟩` over p,q; the p-sum gives `conj(C)`, the q-sum gives `C`, and regrouping the free indices produces `‖tr_S C‖²_F` | yes |
| BLOCK RECURSION `q_k(C) = Σ_{a,b} q_{k-1}(C_ab) − ½ q_{k-1}(tr_i C)` | split the S-sum by `i ∈ S`; use `(tr_S C)_ab = tr_S(C_ab)` for `i ∉ S` and `tr_{S∪i}C = tr_S(tr_i C)` for `i ∈ S` | yes |
| PINCH IDENTITY `q_k(C) − q_k(E_iC) = Σ_{a≠b} q_{k-1}(C_ab)` | block recursion twice; `tr_i E_iC = tr_i C` kills the second term | yes |
| BUDGET IDENTITY | corners are HS-orthogonal for `S ∌ i` and `tr_i(ΠCΠ′) = 0` for `S ∋ i`, so the only surviving cross term is `Q_k(ΠCΠ,Π′CΠ′) = −½ Q_{k-1}(tr_iΠCΠ, tr_iΠ′CΠ′)` | yes, **under the 2-block reading** (item 26) |
| cross-lemma equivalence | `tr_i C = tr_iC₁₁ + tr_iC₂₂`, then expand `q_2(tr_iC)` | yes |

**Two flags I wrote down before reading, both confirmed:**

* **(pre-flag 1, 7a)** `T_S` in `q_k(C) = Σ_S (−1/2)^{|S|}‖T_S C‖²_F` **cannot** be the partial
  transpose: partial transpose only permutes matrix entries, so `‖T_S C‖_F = ‖C‖_F` for every S and
  the sum would collapse to `2^{−k}‖C‖² ≥ 0` trivially for every C of every rank — and the identity
  with G would be false. It must be the partial **trace**. Confirmed numerically: the
  partial-transpose reading equals `2^{−k}‖C‖²` to **3.55e−16**.
* **(pre-flag 2)** In the budget identity the `H_i` term is the sum over the `{Π,Π′}` **cross
  corners**, not over all rank-1 off-diagonal blocks. Confirmed: the rank-1-pinching reading gives
  relative error **4.62e−01**; the 2-block reading gives **6.52e−16**.

**My in-session identity checks** (`p4_identities2.log`; (d,k) ∈ {(2,2),(3,2),(2,3),(3,3),(4,3),
(2,4),(3,4)}, 3 trials each, **real and complex**, max relative error):

```
A   q_k = sum_{p,q} G_pq                              7.176e-16
A'  partial-TRANSPOSE reading = 2^-k ||C||^2          3.552e-16   (type flag confirmed)
B   block recursion                                   4.713e-16
C   pinch identity                                    6.524e-16
D   budget identity ({Pi,Pi'} 2-block reading)        6.524e-16
D'  budget identity (rank-1-pinching reading of H_i)  4.622e-01   (WRONG reading, pre-flagged)
E   cross-lemma equivalence                           9.164e-17
F   A-factorization q_k = <C, ox_i(1-(d/2)P_i) C>     4.600e-16
G   K = 2^{-k} sum_S 2^{|S|} Pi_S                     0.000e+00   (exact, matrix-level)
H   K_a F = a^k K_{1/a}                               5.932e-16
I   complementation S <-> S^c                         5.888e-14
```

`K` spectra came out as `[2^{−k}, (3/2)^k]` exactly — `[0.5,1.5]`, `[0.25,2.25]`, `[0.125,3.375]` —
confirming `K ⪰ 0` and the factor eigenvalues 1/2 (symmetric) and 3/2 (antisymmetric).

**Notational coincidences flagged (7c):** `E_i` denotes two different pinchings in the same node
paragraph; `G_k` is used for both `q_k` and its polarisation `G2(A,B)`; W2's candidate list contains
**two distinct candidates both labelled `K11`** (`K11_parity_even`, `K11_parity_odd`); `T_i` is the
partial trace while `T_S` reads as a transpose-like symbol.

**Documentation inconsistency (7a).** `NPTBE.k3.R1.md` records the general-subset coefficient two
ways: the R3-gate quote says `(−2/d)^{|S|}`, the d-uniformity note says `α^{|S|} = (−1/2)^{|S|}`
independent of d. They coincide only at d = 4, which is where they were checked. The
`A = ⊗_i(1 − (d/2)P_i)` factorization (verified by me at 4.6e−16) forces the **d-independent**
`(−1/2)^{|S|}`, which is also the object the whole fleet uses. The `(−2/d)` phrasing should be
struck.

---

## FINDING A (headline) — the tight set is d-DEPENDENT

**Claim under review** (synthesis, W5): *"maximizers land on the SAME d=4 vertices"*; (R1.facet):
the tight set's x-image is a 2D polygon with conjectured vertices
`{(2,0,0), (3,2,0), (5/2,2,2), (4,5,2)}`, presented as d-independent and made a **mandatory vertex
filter** for proof-candidate screening.

**This is false for d ≥ 5, and W5's own logged data contains the refutation.** Verbatim:

```
W5/grid_d5.log:17: GRID d=5 l2=0.75 l3=-0.50 h=2.050000000 x=(2.400000,1.800000,2.000000) target=1.000000000 g3=-4.163e-16
W5/grid_d6.log:17: GRID d=6 l2=0.75 l3=-0.50 h=2.083333333 x=(2.333333,1.666667,2.000000) target=1.000000000
```

Both are exact zeros of g3 and both lie **outside** the hull of the four claimed vertices: at
x3 = 2 the hull requires x2 ≥ 2, and these have x2 = 1.8 and 1.667.

**Exact explanation (mine, derived and then verified).** `q_k` is multiplicative over a copy split:
if `C = A ⊗ B` with A on copies {1,2} and B on copy {3}, then `tr_S(A⊗B) = tr_{S∩12}A ⊗ tr_{S∩3}B`
and the Frobenius norms factor, so `q_3(A⊗B) = q_2(A)·q_1(B)`. Take **B = P₂, any rank-2 orthogonal
projector**: `q_1(P₂) = ‖P₂‖² − ½|tr P₂|² = 2 − 2 = 0`. Hence for **every** rank-1 A and **every** d,

> **C = A ⊗ P₂ is a rank-2 exact zero of q₃.**

Its invariants are, with `u = (‖tr₁A‖²+‖tr₂A‖²)/‖A‖²` and `t = |tr A|²/‖A‖²`,

  **x = (2 + u, t + 2u, 2t)**,  which satisfies `x1 − x2/2 + x3/4 = 2` identically, i.e. `q₃ = 0`.

Taking `A = |Φ⟩⟨Φ|` maximally entangled gives `u = 2/d`, `t = 1`:

  **x = (2 + 2/d, 1 + 4/d, 2)**, support value `h(0.75,−0.5) = 9/4 − 1/d`.

Verified (`p4_exact_recert.log`, PART B), rank(C) = 2 at every d:

| d | q₃ | x measured | x predicted | h | 9/4 − 1/d |
|---|---|---|---|---|---|
| 2 | 0.000e+00 | (3, 3, 2) | (3, 3, 2) | 1.7500000000 | 1.75 |
| 3 | 1.110e−16 | (2.666666667, 2.333333333, 2) | same | 1.9166666667 | 1.9166666667 |
| 4 | 0.000e+00 | (2.5, 2, 2) | same | 2.0000000000 | 2.0 |
| 5 | 0.000e+00 | **(2.4, 1.8, 2)** | same | **2.0500000000** | 2.05 |
| 6 | 0.000e+00 | **(2.333333333, 1.666666667, 2)** | same | **2.0833333333** | 2.0833333333 |
| 8 | 1.110e−16 | (2.25, 1.5, 2) | same | 2.1250000000 | 2.125 |

The d = 5 and d = 6 rows are **exactly** W5's logged grid maxima. 40 random rank-1 A at d = 3,5
give `max |q₃|/‖C‖² = 6.572e−16`, confirming the whole family, not just the entangled member.

**Why the campaign missed it:** `1 + 4/d ≥ 2 ⟺ d ≤ 4`. The family lies strictly inside the polygon
at d = 3, exactly **on** the claimed vertex (5/2,2,2) at d = 4, and pokes out only at d ≥ 5. The
polygon was fitted from d = 3,4 data. The family also explains the "non-extreme fifth tight point"
(3,3,2) (the u = t = 1 member) and the tight edge from (5/2,2,2) to (4,5,2) at d = 4 (t = 1,
u ∈ [1/2,2]).

**Independent corroboration of the same failure mode:** `W5/ranklaw_d5.log` shows the *rank law*,
also fitted at d = 3,4, breaking at d = 5 in the same way — rank-3 min `−0.525` vs law `−0.500`,
rank-4 `−1.050` vs `−1.000`, rank-5 `−1.575` vs `−1.500` (a uniform ×1.05), `all_match=False`. Two
independently fitted d ≤ 4 structures both fail at d = 5. **This disconfirmation appears in no
summary.**

**Consequences.** The mandatory 4-vertex filter is incomplete at d ≥ 5 and must be replaced by the
two-parameter family `{(2+u, t+2u, 2t)}`. Any "X is saturated exactly on the whole tight set"
verified only on the five stored d = 4 exemplars is unproven at d ≥ 5. **The target inequality is
not threatened**: every one of these points has `target = 1.000000000` exactly, never above.

---

## FINDING B — the decision-layer `E_S` reduction is REFUTED

The unreviewed decision-layer note (on `NPTBE.k3.R1.m1.md` and in the phase-2 dispatch) says: since
`K = 2^{−k} Σ_S 2^{|S|} Π_S` with all coefficients positive, M1 **follows if** every elementary
exchange matrix `E^S_pq = ⟨x_p⊗y_q, Π_S(x_q⊗y_p)⟩` is PSD at r = 2; and that the k=1, S={1} case
reduces to `|⟨x1∧y2, x2∧y1⟩|² ≤ ‖x1∧y1‖²‖x2∧y2‖²`.

* The **expansion is correct** — I verified `K = 2^{−k}Σ_S 2^{|S|}Π_S` at the matrix level,
  residual **exactly 0.0**.
* The **sufficient condition is false.** Take `x1 = y1 = e1`, `x2 = y2 = e2` (orthonormal, tensored
  with any common spectator). Then by hand and confirmed numerically
  (`p4_exact_recert.log`, PART C): `E^{S}` on the copy where e1,e2 differ is
  `[[0, −1/2], [−1/2, 0]]`, eigenvalues **±1/2** — not PSD — at k = 1, 2 **and** 3, while
  `G = [[½,−½],[−½,½]]` is PSD there (eigenvalues 0 and 1; at k=2,3 eigenvalues 0 and 2^{1−k}).
* The stated **Plücker inequality is false** at the same point: `x1∧y1 = e1∧e1 = 0` so RHS = 0,
  while `|⟨e1∧e2, e2∧e1⟩|² = 4 > 0`.

The positive-combination structure is real, but the per-S PSD strengthening is strictly too strong.
**P1 should not spend a batch on this route.**

---

## FINDING C (new; not in the earlier draft) — the cross lemma's inner minimisation over Π fails

The cross lemma quantifies over **every** copy i: there must exist a 2-dim Π on copy i with
`cross(i,Π) = Re Q_2(tr_i(ΠCΠ), tr_i(Π′CΠ′)) ≤ 0`. All the campaign's evidence for it consists of
random-start local searches for that Π. I evaluated `cross(i,Π)` on my tight family
`C = |Φ⟩⟨Φ|_{12} ⊗ P₂` (`p4_cross_percopy.log`, 60 random Π per copy):

| d | copy 1 (Φ) | copy 2 (Φ) | copy 3 (P₂), random Π | copy 3 at Π = P₂ |
|---|---|---|---|---|
| 3 | max\|cross\| 1.1e−16 | 8.3e−17 | min **+2.489e−01**, max +9.167e−01 | **+0.000e+00** |
| 4 | 1.1e−16 | 1.1e−16 | min **+5.370e−01**, max +9.998e−01 | **+0.000e+00** |
| 5 | 1.1e−16 | 1.1e−16 | min **+4.501e−01**, max +1.050e+00 | **+0.000e+00** |
| 6 | 1.1e−16 | 1.4e−16 | min **+4.444e−01**, max +1.083e+00 | **+0.000e+00** |

Structure (derived, then confirmed): on the two copies carrying `|Φ⟩`, `tr_i(ΠCΠ) = (Πᵀ/d) ⊗ P₂`
and the four terms of `Q_2` cancel identically, so `cross ≡ 0` for **every** Π. On the P₂ copy,
`Π = P₂` gives `ΠCΠ = C`, `Π′CΠ′ = 0`, hence `cross = 0` exactly — but this is an **isolated,
measure-zero optimum**, and every random Π gives a strictly positive value bounded away from zero.

**Three consequences, all decision-relevant:**

1. **The cross lemma holds at the tight family, with exactly zero margin and a unique witness.**
   Good news for P2 — but any proof must *construct* Π, since search will not find it.
2. **The earlier P4 draft's "min_Π cross per copy = −9.1e−17, −7.4e−17, +0.1204" at the d=3 tight
   exemplar is an inner-optimiser artifact, not a refutation** — the true minimum on that copy is
   exactly 0, attained at Π = P₂. I correct that entry here.
3. **W3's `min_Π cross` numbers are upper bounds on the true minimum, not the minimum.** Therefore
   the adversarial `max_C min_Π cross` values (`+1.41e−12` d=3, `+1.01e−11` d=4, `+4.61e−11` d=5)
   are **over**-estimates. That is the reassuring direction — they are consistent with a true
   maximum of exactly 0 — but it also means these numbers certify nothing, and
   **the argmax parameters are not archived** (`cross_l2b_only_results.json` stores only
   `{d, max_min_cross, secs}`), so they cannot be mpmath-re-certified from the archive at all. The
   search must be re-run with a structure-aware inner minimisation.

---

## Per-item PASS / FAIL / CAVEAT table

Legend: **F** = defect that changes a stated conclusion; **C** = caveat / scope repair; **P** = pass.
"value" = checks the printed number; "construction" = independent re-derivation (7f).

### W1 — zero manifold (NPTBE.k3.R1.zeroman)

| # | item | verdict | numbers / basis |
|---|---|---|---|
| 1 | dimension methodology (gauge-projected Hessian kernel) | **P** (construction) | d=2 ground-truth gate: exact Jacobian nullity 22 = Hessian count 22, cut-stable 1e−4…1e−12; gauge rank 10; gap ratios 6.4e13–1.9e14 |
| 2 | tangency retraction control | **P**, good design | kernel dirs ratio med 1.0000, cos 0.999997; non-kernel control ratio 0.0023, cos 0.0104 — a real ±control pair. But d=3, **1 point, 20 directions** only |
| 3 | "local dimension = 12d" | **P-scoped / C** | 36 (d=3), 48 (d=4 cluster), **60 at d=5 predicted-then-measured** — a genuine pre-registered prediction (7f). **C:** at d=5 the cut window is narrower than the d=2 gate: `cuts={1e−5:60, 1e−7:60, 1e−8:60, 1e−10:36, 1e−12:3}`. **C:** the exact-product zero at d=4 has `dim_Z_projective = 68 ≠ 48`, so ≥2 components of different local dimension exist |
| 4 | "**Dominant** component" | **F (7g)** | quantifier never resolved and false under natural readings: `structure_stdout` gives `frac<1e−10 = 0.28` at **both** d=4 and d=5 (0.60 at d=3), and the competing component has **larger** local dimension (68 > 48) |
| 5 | "defining relations COMPLETE, affine nullspace dim exactly 5" | **P-scoped** | proper train/holdout, n_hold = 20 (d=3) / 8 (d=4), max holdout residual 1.2e−15. "Complete" = for the fitted cluster, not for `{G3=0}` |
| 6 | x-image = d-independent segment `x1 = 2+x3/2, x2 = 1.5x3` | **C** | the consolidated JSON names the d=3 relation `x2_eq_4p5x3_over_d` (**d-dependent**); `structure_stdout` tests that form at d=4,5 and gets `frac = 0.00`, while the d=5 predictive run confirms the **d-independent** `x2 = 1.5x3`. At d=3 the two coincide. Two artifacts state incompatible formulas; only the d-independent one survives |
| 7 | `osr = 4(d−1)` | **P** (honest REFUTED) | d=5 osr values [4,5,6,7,8,9,10,12,15,16]; recorded as a clustering artifact |
| 8 | BONUS: d=4 ⇔ "odd-weight mass ≤ ½" | **P** (construction) | I re-derived `q_k = ⟨C, ⊗(1−(d/2)P_i)C⟩` (4.6e−16); at d=4, `R_i = 1−2P_i` are commuting self-adjoint unitaries, so `q₃ ≥ 0 ⟺ ‖Π₋C‖² ≤ ‖C‖²/2`. Also predicts λ_min(A) = −0.5 (d=3), −1 (d=4), matching CTRL-B |
| 9 | product-point Hessian over-read | **P** (self-flagged, unresolved) | acknowledged in the synthesis |

### W2 — k=2 mechanism transfer, M1 (NPTBE.k3.R4 / R1.m1)

| # | item | verdict | numbers / basis |
|---|---|---|---|
| 10 | identity `q_k = Σ G_pq` | **P** (construction) | mine **7.176e−16** over 7 (d,k) pairs, real+complex; theirs 5.7e−16…1.02e−15 |
| 11 | type of `T_S` | **C (7a)** | must be partial trace; displayed without definition (pre-flag 1) |
| 12 | complementation / dyad-swap / α-reversal / sector identities | **P** (value + construction) | theirs 3.2e−15, 1.2e−14, 5.1e−15, 5.5e−16; my own complementation check 5.9e−14 |
| 13 | BGH parity break at k=3 | **P** | `‖K_c−K_cᵀ‖/‖K_c‖` = 0.000000 (k=2) vs **2.000000** (k=3) at d=2,3; `⟨ψ,Tc⟩` = 0 at k=2, 0.084–0.600 at k=3 |
| 14 | `γ_k(d) ≤ 2^{1−k}`: "true at k=2 all d, FALSE at k=3 every d≥3" | **P-scoped + C** | logged: γ₂ = 0.500000000 (d=2,3,4) OK; γ₃ = 0.250 (d=2) OK, **1/3 (d=3) VIOLATED**, **0.375 (d=4) VIOLATED**; γ₄ = 0.125 (d=2) OK, **1/6 (d=3) VIOLATED**. Only d ≤ 4 tested. **Reviewer repair:** γ_k(d) is a sup of a scale-invariant ratio over a space embedding isometrically into the d′>d space, hence non-decreasing in d — so the k=3 violation does extend to all d ≥ 3. The "true at k=2 for all d" half is inherited from the published theorem, not measured |
| 15 | screening table "8 of 14 survived, 2240 samples" | **P** (arithmetic) + **C** | 14 candidates listed, 8 SURVIVES, `samples scanned: 2240` ✓. **C:** two distinct candidates both labelled **K11**. **C (correcting the earlier draft, which said four):** **six** of the eight SURVIVES verdicts rest on min margin `−0.000000` — K1, K2, K5, K13, K15, K16; only K8 (+0.133628) and K9 (+0.060401) have real margin |
| 16 | LP: "**NO** proof in (x1,x2,x3)-invariants alone can work" | **F (7g scope)** | the LP shows the *enumerated* cone reaches 2.833 > 2. It cannot show non-existence: the target *is* an inequality in (x1,x2,x3), so if true it is provable at invariant level from the achievable region's own supporting inequalities. Correct claim: "the enumerated invariant inequalities are insufficient" |
| 17 | M1 evidence attribution | **F (7f provenance)** | **"M1" does not occur anywhere in `screen.log`** (grep count 0). The "8 of 14 / 2240 samples" line describes the K1..K16 *invariant* list; the 2240-sample M1-adjacent quantity is `min (Γ11+Γ22)/(¼|B_{−2}|) = 1.000000000`, the **arithmetic-mean weakening M1′**, implied by M1 and strictly weaker. M1's real evidence is `m1.log` (random + local search: ratio → 1.000000, 0.999947 at k=3 d=4), `m1_stress` (k=4,5 **at d=2 only**), `exchange.log` |
| 18 | "M1 saturated exactly on the whole tight set" | **C** | `m1.log` states "balanced decomposition, d=4" — one decomposition, five d=4 exemplars, while M1 quantifies over all four vectors. Earlier draft extended this to 6 decompositions × new exemplars at d=3,4,5 (max ratio 1.0000000000000010, no violation); still unswept |
| 19 | rank-3 witness (G not PSD beyond r=2) | **P**, load-bearing | eig(G) = [−0.5, 1, 1], ΣG = −0.5 at k=2, while 250 random r=3 samples gave min eig **+0.0056** — direct evidence that random screening at fixed rank is unreliable here |
| 20 | second-order probe at the M1 equality manifold | **C** | (ratio−1)/ε² ∈ [−0.0106, −0.0028] over 960 probes — genuine local-max evidence, but the equality manifold is uncharacterised and sup = 1 is also attained on trivial rank-1 degenerations (x1=x2, y1=y2) |
| 21 | decision-layer `E_S` reduction | **F — REFUTED** | Finding B |
| 22 | superseded logs retained unmarked | **C** | `W2/mechanism_probe.log` carries the pre-fix normalisation, superseded by `probe_blockB_vertex_fine_data.log`, but is unmarked (unlike `probe_blockEFG_first_run_superseded.log`) |

### W3 — pinching, block recursion, cross lemma (NPTBE.k3.R1.blockrec / R1.rep)

| # | item | verdict | numbers / basis |
|---|---|---|---|
| 23 | BLOCK RECURSION exact, basis-free, no d | **P** (construction) | mine **4.713e−16** up to (4,3),(3,4), real+complex; theirs ≤ 9.99e−16 at d=3,4,5 in standard **and rotated** bases. Basis-freeness *proved* (sesquilinearity + unitary invariance of `Σ_{a,b}Q(C_ab,C_ab)`), not merely observed |
| 24 | PINCH IDENTITY / PINCH LEMMA | **P** (construction) | mine **6.524e−16**; theirs `|H_i − Σ_blocks|` ≤ 6.66e−16 over 15 cases; blocks of a rank-≤2 matrix are rank-≤2 ✓ |
| 25 | "**Unconditional** corollary `H_i(C) ≥ 0`" | **C** | it consumes the published k=2 theorem; "unconditional" means only "not conditional on the pinching step" |
| 26 | BUDGET IDENTITY | **P** under the 2-block reading; **C** on notation | mine **6.524e−16**; W3's `cross.log` uses the correct quantity. But the node writes `H_i(C − E_iC)` with `E_i` defined one clause earlier as the *rank-1* pinching; under that reading the identity is **wrong by 46%** (my D′ = 4.62e−01) |
| 27 | cross-lemma equivalence (the two stated forms) | **P** (construction) | mine **9.164e−17** |
| 28 | cross-lemma numerics | **F — mislabelled** (was **C** in the earlier draft) | see **Finding C**: the reported quantity is not `min_Π cross` but a local-search upper bound on it, which is demonstrably wrong by O(1) on the tight family. `0/300 positive` on random C and the adversarial `+1.4e−12 … +4.6e−11` inherit that defect; **the argmax parameters are not archived**, so no re-certification is possible from the archive |
| 29 | "min over Π strictly negative on 100/100 random C (so it is NOT implied by the target)" | **F (7g)** | non-sequitur: strict negativity on random inputs is evidence the lemma holds *with margin* there; it says nothing about implication. Presumably intended "the cross quantity is not identically zero" |
| 30 | "the cross lemma is the ONLY gap" | **C (7b)** | the induction over local dimensions bottoms out at all local dims ≤ 2, i.e. rank-≤2 C on `(C²)^{⊗3}`. The node names "G1 = rank-2 Cauchy–Schwarz, G2 = the 2026 theorem" but never this d=2,k=3 base case. W5-G4 gives min 0.264 over 200 random **any-rank** points at d=2,k=3 — evidence, not proof. **Two gaps, not one** |
| 31 | compression route vacuous / pinch-to-2 chains killed | **P** (honest negatives) | C3 adversarial `min_h ≥ −1.5e−17`; `partc5` min g3_pinched = −0.500, −1.000, −1.352 at d=3,4,5 |
| 32 | diagonal-only strengthening FALSE; crossed-Schwarz closure impossible | **P** | −0.333333 (d=3), −0.500 (d=4) |

### W4 — SOS / batch-2 adjudication (NPTBE.k3.R1.sos)

| # | item | verdict | numbers / basis |
|---|---|---|---|
| 33 | **"batch-2's obstruction OVERTURNED"** | **F — mis-adjudication** | Batch-2's reviewed-CLEAN finding was explicitly scoped: the archived slice direction is a valid dual certificate **only for the holomorphic-cubic Hermitian cone modulo the determinant**, and "the complete mixed-weight real degree-six cone … remain[s] undecided". W4 works on that larger, explicitly-undecided cone. **Nothing reviewed-CLEAN was contradicted.** W4's corrected slice *is* the right object for the larger question; it is not the object batch-2 certified. The right word is **"extended"**, not "overturned" |
| 34 | batch-2 baseline reproduction | **P** (construction) | my own recomputation from the archived `w4_slice_setup.npz` — restrict `G30_0` to the 21-dim zero-weight sector, deflate the `dvec` direction, symmetrise, `eigvalsh` — gives **−1.3381959324607331**, vs W4's −1.3381959324607335 and batch-2's frozen −1.3381959324607333. **Agreement to 15 significant digits.** (Undeflated zero-weight block: −1.5589391561407910.) The frozen number is confirmed |
| 35 | "complete mixed-weight degree-6 cone is numerically **FEASIBLE** (t* = −6.6e−11)" | **F/C (7e)** | I could **not** independently re-solve this SDP within budget, so I report what the archive shows: `t* = −6.61e−11` is the **SCS leg-1 primal** with `dual_status: "infeasible"`, `dual_value: Infinity`, trace bound `R = 1e4`; the **leg-2 dual** gives **−3.198e−06**, five orders larger; and I re-tested the archived solution blocks myself from `w4_certificate.npz`: **λ_min(W) = −7.714e−11**, **λ_min(G21) = −6.262e−12** — both negative, matching `w4_verify.json` and its mpmath recheck. A first-order solver optimum at −1e−10 with a 1e−6 dual gap and non-PSD archived Gram blocks is **not** a feasibility certificate. Defensible: "not obstructed at solver tolerance". Note the irony — the flaw W4 attributes to batch-2 (over-reading a scoped numerical object) recurs here |
| 36 | exact rational Farkas certificates, d = 3,4,5,6 | **P** (construction, exact) | I re-verified all four in `fractions.Fraction` from the archived rational coordinates, independent of the producing script: `min(y) = 0` ✓, `min_λ ⟨y,A_λ⟩ = 0` ✓, `⟨y,F⟩ = −1` ✓ — **all four VALID**. `y` = (4, 384), (½, 225/2), (4/27, 64), (1/16, 735/16) on (e_TTTT, e_JJJJ). Rational recognition validated by the archived 120-sample refits at 7.4e−16 / 9.6e−16 |
| 37 | closed-form Farkas family | **P at d=3..6**, **C** for all d | `y = (1/(2(d/2−1)³))(e_TTTT + 3(d+1)²(d−1) e_JJJJ)` reproduces all four archived `y` at scale **exactly 1** (not merely up to positive scale) — I checked the ratio in exact arithmetic. It is **matched at four values of d, not proved for all d**; that needs symbolic-in-d A and F coordinates. Consistent with feasibility only at d=2 (the prefactor blows up) |
| 38 | "the quartic biquadratic SOS route is CLOSED NEGATIVELY" | **C (scope)** | the Farkas argument rules out `cone{A_λ, B_μ}` (the `B` half being the nonnegative orthant, which is what `min(y) = 0` certifies). The identification of that 32-generator cone with "the equivariant quartic SOS cone" is **asserted in the script docstring and never verified**. The negative result is exactly as strong as that identification |
| 39 | size accounting (max torus block 402,543) | **P** (value) | matches `stage3_sizes.log` for the full d=3 v21 problem |
| 40 | artifact hygiene | **C** | the d=6 run wrote the same filename as d=3,4,5; the final `w4_biquadratic_exact.json` holds d=3,4,5,6 plus a duplicate `_d6` copy. Provenance recoverable, filename not run-unique |

### W5 — falsification sweep (NPTBE.k3.R1.facet evidence)

| # | item | verdict | numbers / basis |
|---|---|---|---|
| 41 | "1080 rank-2 restarts" | **P** (arithmetic) | archived `--min-restarts` args: 300 + 300 + 80 + 200 + 200 = **1080** ✓ (d4k4b's 200 supersedes the truncated d4k4 run at 150; `d4k4.log` retained without a SUPERSEDED marker — **C**) |
| 42 | "global min −1.66e−15" | **P** + **C** | per-run mins: −2.776e−16 (d5k3), −4.441e−16 (d6k3), −1.664e−15 (d8k3), −7.252e−17 (d3k4), −7.633e−17 (d4k4b). The quoted figure is the d=8 value ✓. **C:** the d=8 noise floor is ~1e−13 on dense re-evaluation, so −1.66e−15 understates it |
| 43 | "**every** argmin re-certified POSITIVE at 50 digits" | **F (7g)** | the code re-certifies the **single global argmin of each run** (5 total) plus an escalation branch that was empty — `n_below_-1e-8: 0` in all five MIN-SUMMARY lines. **Not 1080** |
| 44 | the 50-digit re-certifications themselves | **P** (construction) — **4 reproduced, ≥3 required, and STRENGTHENED** | I wrote an independent **dense, exact-rational** path (W5's is a factored mpmath inner-product path): every float64 is exactly `m·2^e`, so `2^k·q_k` and `‖C‖²` are exact integers and `g` is an exact rational. Results — **all four exactly POSITIVE, sign decided with no precision caveat at all**: d5k3 `2.405676970198795658642664787946845578769e−18`; d6k3 `2.975927320263179969583731293685763193519e−19`; d3k4 `2.678197524926072765373270666482950316859e−18`; d4k4 `6.738561147433606807556667638642406021791e−18`. **New caveat (7e), nobody flagged it:** these agree with W5's `g_mp50` only to **31–33 significant digits**, not 50 — `q_k` is a difference of O(1) terms with an ~18-digit cancellation, so `mp.dps = 50` buys ~32 correct digits. Harmless for a sign decision, but "50 digits" overstates the precision actually delivered |
| 45 | scope of the mp50 check (7f) | **C** | it re-evaluates at the *same float64 point*, so it certifies the printed value against cancellation, not that the true nearby local minimum is positive. W5 uses it correctly; the synthesis phrasing invites the stronger reading |
| 46 | `h_d = 2.000000000` at d=5,6,8 | **P** | d=5: 150/150 within 1e−9 of 2, `n_above_2 = 0`; d=6 same; d=8 separate run `d8k3h`, 30/30. Seed families cplx/real/prod0/emb4 all represented |
| 47 | 25-direction grids, `worst_target = 1.000000000` | **P** (value) | d=5 and d=6, `alert=False` |
| 48 | "maximizers land on the SAME d=4 vertices" | **F — false** | Finding A. Several other grid maximizers are not vertices at all: (2.845,2.690,2), (3.671,4.340,1.996), (2.294,0.588,0), (2.363,0.726,0), (2.437,0.875,0), (3.101,2.304,0.203), (3.235,2.706,0.471) |
| 49 | positive control A (α sweep) | **P**, well designed | α = −0.45/−0.49 strictly positive, −0.50 zero, −0.51/−0.55/−0.60 strictly negative, at d=5,6 (k=3) and d=3,4 (k=4). Correct sign structure on both sides of the endpoint |
| 50 | positive control B (rank sweep) | **P** + **F on the synthesis gloss** | rank ≥ 3 negative at d=3 (−0.5) and d=4 (−1.0) ✓. But "rank-3 at α = −1/2 gives −0.500000000" is d=3/4-specific: `ranklaw_d5.log` gives rank-3 min **−0.525**, `match=False`, `all_match=False` at d=5 (uniform ×1.05 across ranks 3,4,5). **This disconfirmation appears in no summary** — and it is the same d≤4-fit failure as Finding A |
| 51 | gates G1–G5 | **P** | E1-vs-E2 dense/factored cross-check 8.3e−16…2.8e−14 (real implementation independence, 7f); analytic-gradient FD check 5.8e−11…1.1e−10; embedding exactness 7.3e−16; archive-vs-fresh h₄ = 2.000000000 |
| 52 | "k=4 does NOT break" | **P-scoped** | (3,4) and (4,4) only, 200 restarts each, min −7.25e−17 / −7.63e−17, both exactly positive under my exact recert |

### Cross-cutting

| # | item | verdict | basis |
|---|---|---|---|
| 53 | SHA256SUMS integrity | **P** (all 5 packages, no content mismatch) + **C** (path bases) | I verified each after stripping CRLF. **From the repo root:** W1 20/20 OK, W2 28/28 OK, W4 33/33 OK, W3 0/38, W5 6/43. **From each package's own directory:** W3 38/38 OK, W5 37/43, W1/W2/W4 0. So W1/W2/W4 are repo-root-based, W3 is own-dir-based, and **W5 mixes the two** (37 own-dir + 6 `tools/` repo-root) — no single `sha256sum -c` invocation checks W5. Every file is intact; the defect is purely path-base and CRLF |
| 54 | provenance blocks | **P** | every W3/W4/W5 log carries script SHA-256, python/numpy/scipy versions, seed, argv, UTC. W2's logs carry seed + numpy but not the script SHA in the log body (it is in SHA256SUMS) |
| 55 | evidence tier discipline | **P** | W1's consolidated JSON self-labels "NUMERICAL (proposer-authored, pending independent review)"; both new nodes are CONJECTURED with pending-review markers. **No completion tier was written anywhere** |

---

## 7b — regime-complete gates: what is NOT tested

* **k**: the target is tested at k = 3 (d = 2–6, 8) and k = 4 (d = 3, 4 only). **k ≥ 5 untested for
  the target.** M1 alone was stressed at k = 4, 5 but **only at d = 2**.
* **d**: d = 7 and d ≥ 9 untested at every k. W1's structure work is d = 3, 4 with a d = 5
  predictive test; d ≥ 6 untested. W4's degree-6 work is a **d = 3 slice** only.
* **cross lemma**: k = 3 only, d = 3, 4, 5 only, copies of local dimension > 2 only — and see
  Finding C for what the reported quantity actually is.
* **rank**: r ≤ 2 is the target; r = 3, 4 appear only as controls at k = 2, 3 and d = 2, 3, 5.
  Rank-1 degenerations are not separately reported, yet they saturate M1 trivially.
* **real vs complex**: W5 covers both (`real`/`cplx` seed kinds); my identity checks cover both.
  W2's M1 and W3's cross-lemma searches are **complex-only** — a real-restricted counterexample
  would not be found.
* **M1 quantifier**: M1 ranges over all four vectors, i.e. over all rank-2 decompositions of a given
  C; W2 checked one "balanced" decomposition per exemplar.
* **split induction**: the d = 2, k = 3 base case is unproven (item 30).
* **W4**: the full d = 3 degree-6 problem (max torus block 402,543) is out of reach; only the
  9-variable slice is decided, and only at solver tolerance.

---

## What phase 2 may build on — SAFE

1. `q_k(C) = Σ_{p,q} G_pq` with **T_S = partial trace** — independently derived and verified 7.2e−16.
2. **BLOCK RECURSION**, **PINCH IDENTITY**, and the **BUDGET IDENTITY under the {Π,Π′} reading** —
   all three independently derived and verified ≤ 6.6e−16; the block recursion's basis-freeness and
   d-independence are *proved*, not merely observed.
3. The **cross-lemma equivalence** between the "cross term ≤ 0" and
   "`G2(Z)+G2(T_iC−Z) ≥ G2(T_iC)`" forms (9.2e−17).
4. `q_k(C) = ⟨C, ⊗_i(1 − (d/2)P_i) C⟩`, and the d=4 reformulation "odd-weight mass ≤ ½".
5. `K = 2^{−k} Σ_S 2^{|S|} Π_S` with positive coefficients (the **expansion** — exact, residual 0.0
   — **not** the `E_S` reduction), and `spec(K) ⊂ [2^{−k}, (3/2)^k]`.
6. The **four exact Farkas certificates** (d = 3,4,5,6) as statements about `cone{A_λ, B_μ}`, and
   the closed-form family, which matches all four at scale exactly 1.
7. **Batch-2's λ_min = −1.33819593246073…** and batch-2's reviewed scope (holomorphic-cubic
   Hermitian cone modulo the determinant) — both intact and independently reconfirmed.
8. W5's falsification-negative at the tested (d,k), and the five 50-digit re-certifications — four
   of which I upgraded to **exact rational** arithmetic (sign POSITIVE with no precision caveat).
9. `γ_3(3) = 1/3 > 1/4`, `γ_3(4) = 3/8`, `γ_4(3) = 1/6 > 1/8`, plus the monotonicity argument I
   supply extending the k=3 break to **all d ≥ 3**.
10. The rank-3 witness `eig(G) = [−0.5, 1, 1]` — a hard constraint on any M1 proof: whatever the
    argument is, it must fail at r = 3.
11. **NEW (this review):** the exact tight family `C = A ⊗ P₂` (A rank 1), `q₃ ≡ 0` for every d,
    with x-image `(2+u, t+2u, 2t)` and maximally-entangled member `(2+2/d, 1+4/d, 2)`,
    `h = 9/4 − 1/d`.
12. **NEW (this review):** on that family the cross lemma holds on **every** copy with exactly zero
    margin — identically zero on the two `|Φ⟩` copies, and zero at the unique witness `Π = P₂` on
    the third.

## What phase 2 must NOT build on — NOT SAFE

1. **"The tight set's x-image is a d-independent polygon with vertices {(2,0,0),(3,2,0),(5/2,2,2),
   (4,5,2)}"** and **"maximizers land on the same d=4 vertices"** — false at d ≥ 5. The *mandatory
   vertex filter* on R1.facet is incomplete at d ≥ 5 and must be replaced by the family in SAFE-11.
2. **The `E_S` reduction** and its Plücker corollary — refuted with an explicit counterexample.
   Do not commission a batch on it.
3. **W3's `min_Π cross` numbers**, including "strictly negative on 100/100 random C", "0/300
   positive", and the adversarial maxima `+1.4e−12 … +4.6e−11` — the inner minimisation is
   demonstrably unreliable (Finding C) and the argmaxima are not archived.
4. **"No proof in (x1,x2,x3)-invariants alone can work"** — over-scoped reading of an LP over an
   enumerated candidate list.
5. **"Batch-2's obstruction was overturned"** and **"the corrected cone is FEASIBLE"** — the first
   is a mis-adjudication (batch-2's scope was never contradicted), the second is a first-order
   solver result with negative archived Gram blocks (−7.7e−11, −6.3e−12) and a 1e−6 dual gap.
6. **"Every argmin re-certified at 50 digits"** (it was 5, and the delivered precision is ~32
   digits), **"M1 screened on 2240 samples"** (that was the invariant list; M1 does not appear in
   `screen.log`), **"dominant component"** (28% at d=4,5), **"the cross lemma is the only gap"**
   (two gaps), **"rank-3 gives −0.5"** (−0.525 at d=5) — none survives literal reading.
7. **The split induction's d=2, k=3 base case** — not established anywhere.
8. **The identification `cone{A_λ,B_μ}` = the equivariant quartic SOS cone** — asserted, unverified;
   carry it as a hypothesis in every restatement of the quartic closure.
9. Any **"saturated exactly on the whole tight set"** claim verified only at the five d=4 exemplars.

## Recommended immediate actions

* **A1.** Recompute the tight-exemplar set at each d in scope from the family `(2+u, t+2u, 2t)` and
  re-run every "saturated on the tight set" check (M1, M2, cross lemma, future candidates) against
  it. Highest-value single action.
* **A2.** Re-run W3's adversarial `max_C min_Π cross` with a structure-aware inner minimisation
  (seed Π from the spectral data of `tr_i C`, and always include the exact analytic candidates) and
  **archive the argmax parameters**. The current numbers cannot be re-certified at all.
* **A3.** Correct the false/over-scoped statements in the synthesis and on `NPTBE.k3.R1.facet`,
  `NPTBE.k3.R1.m1` (E_S note, M1 evidence attribution), `NPTBE.k3.R1.blockrec` ("only gap" → "two
  gaps"; `E_i` symbol collision), and `NPTBE.k3.R1.sos` ("overturned" → "extended"; "FEASIBLE" →
  "not obstructed at solver tolerance"). Strike the `(−2/d)^{|S|}` coefficient phrasing.
* **A4.** Pin the d=2, k=3 base case before the split induction is treated as one lemma away.
* **A5.** Mark `W2/mechanism_probe.log` and `W5/d4k4.log` SUPERSEDED; give W5's SHA256SUMS a single
  path base; note that all five files need CRLF stripping before `sha256sum -c`.
* **A6.** Investigate the d=5 rank-law ×1.05 deviation — it is the same "fitted at d ≤ 4, breaks at
  d = 5" pathology as Finding A and may have a similarly clean product-family explanation.

---

## Reviewer artifacts (this directory)

| file | content |
|---|---|
| `P4_INDEPENDENT_DERIVATION_PRE_READ.md` | the 7c pre-read derivations and the two pre-flags |
| `p4_identities2.{log,json}` | my in-session checks of identities A/A′/B/C/D/D′/E/F/G/H/I |
| `p4_exact_recert.{log,json}` | exact-rational re-certification of W5's four argmina; the tight family at d=2..8; the E_S counterexample |
| `p4_w4_audit.{log,json}` | batch-2 baseline recomputation; exact Fraction re-verification of all four Farkas certificates + closed form; PSD re-test of the archived "feasible" blocks |
| `p4_cross_fast.{log,json}`, `p4_cross_percopy.{log,json}` | Finding C — per-copy cross values on the tight family |
| earlier-pass files (`p4_selfcheck.*`, `p4_tightfamily.*`, `p4_grid.*`, `p4_m1_at_new_tight*`, `p4_ES_reduction.*`, `p4_recert.*`, `p4_farkas.json`) | retained; their load-bearing claims were re-verified independently in this session, with items 15 and 28 corrected |
| `tools/nptbe_p2_p4_identities2.py`, `tools/nptbe_p2_p4_exact_recert.py`, `tools/nptbe_p2_p4_w4_audit.py`, `tools/nptbe_p2_p4_cross_fast.py`, `tools/nptbe_p2_p4_cross_at_tight.py` | reviewer code (this session) |

**Known limitations of this review, stated plainly.** (i) I did **not** independently re-solve W4's
degree-6 SDP (item 35) — I verified its inputs, its baseline number, the non-PSD-ness of its
archived solution blocks, and the inconsistency of its two solver legs, but the feasibility question
itself remains open on my side. (ii) I did not re-run W3's adversarial search; I showed its inner
minimisation is unreliable and that its argmaxima are unarchived, which is why A2 is a re-run rather
than a re-certification. (iii) My exact-rational recertification certifies the sign of `g` at the
stored float64 points; like W5's, it says nothing about the true nearby local minimum.
