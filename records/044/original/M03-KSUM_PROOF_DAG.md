# k-Sum (small alphabet) — AND/OR proof-search DAG

**Most recent change — 2026-08-01 LEAN DOCS-SYNC BATCH: the seven honesty defects of the
independent DELTA-FIDELITY REVIEW discharged, plus one manuscript sentence. NO STATUS MOVED and the
graph is unchanged (no node added or removed, no edge re-typed); documentation and docstrings
only.** Review
[`artifacts/ksum_lean_delta_fidelity_review_20260801.md`](../../../artifacts/ksum_lean_delta_fidelity_review_20260801.md)
(build self-reproduced 0/3017; census 283 lines / 268 distinct names, all standard; new-statement
verdicts **F 21 / N 7 / W 1 / D 0**; census DF-9 CORRECTIONS C-1…C-4 applied by the lead; honesty
**FAIL on record-accuracy** — 7 defects). Repair report
[`artifacts/ksum_lean_docsync_20260801.md`](../../../artifacts/ksum_lean_docsync_20260801.md),
evidence [`artifacts/logs_ksum_lean_docsync_20260801/`](../../../artifacts/logs_ksum_lean_docsync_20260801/).
**(1) D-1, the largest:** seven Lean files (plus the `rel` displays on `KSUM.A1`/`KSUM.B1` and the
`LeanT1` labels in the views below) still asserted that `freeze`/`constQ` are **not in the
manuscript** — false since paper v5.2, which states them as facts **(iii)** and **(iv)**. The
standing conditionality of the whole audit now reads uniformly **"ABI21 + Tani24 + `sec:prelim`
facts (i)–(iv), all stated"**, with `freeze` rendered precisely as facts (i)+(iii) composed at the
last position. **(2) D-5, the one NON-conservative defect:** the `#print axioms` coverage
denominators on the project README and in `Trust.lean` were stale in the direction of claiming more
coverage than exists — corrected from disk to **283 directives → 283 printed lines, 268 distinct
names, of which 240 `theorem`/`lemma` out of 401 in the sources, i.e. ~161 unprinted helpers**
(the review's own repair figure "~133" mixed `theorem`/`lemma` with `def` and is superseded by the
split, which claims less). **(3) D-3:** `KSUM.LEAN.T3`'s caveat RE-GRADED — (51), `ρ_j ≤ 4/5`, the
tilted OUTER half and the (G2) satellite bridge are DERIVED/PROVED, so what remains there is
STRUCTURAL, not analytic; the Mermaid and outline entries below are synced to it in this same
change. **(4)** `Trust.lean` no longer says none of `EmbedData`'s fields is proved while still
stating that `prop:embed`'s **encoding identity** is unformalized (census C-1); `KSUM.B1` no longer
denies that its route proof is written, and records that §1 computes NUMERICAL·pending-review, one
rung above its displayed CONJECTURED (**left to the lead** — the displayed value is conservative);
the campaign ledger's CAMPAIGN-CLOSED obligations list is annotated for what batches 1–2 closed.
**(5) A NEW manuscript finding, on no previous repair list:** `thm:tilted-log-band`'s printed
justification of `C_h ≤ 25/19` does not deliver it — flat Weierstrass gives only `4/3`. The bound
is TRUE and the Lean already proves it by peeling the `d = 1` factor and bounding only the tail
(`∑_{d≥2}5^{−d} = 1/20`, `(4/5)(19/20) = 19/25`); that step is now printed. Statement, constants and
every later display unchanged. `lake build` **exit 0 / 3017 jobs / zero warnings**;
`latexmk` **exit 0, warnings delta 0**, 37 pages; validators 0/0/0.

**Previous change — 2026-08-01 LEAN GAP-CLOSURE BATCH 2 (items H-1 … H-7), THE HARD TAIL:
five of the seven commissioned items CLOSED, two reported RESISTED with exact residuals. NO STATUS
MOVED — the graph is unchanged (no node added or removed, no edge re-typed).**
Report [`artifacts/ksum_lean_gapclose2_20260731.md`](../../../artifacts/ksum_lean_gapclose2_20260731.md),
evidence [`artifacts/logs_ksum_lean_gapclose2_20260731/`](../../../artifacts/logs_ksum_lean_gapclose2_20260731/):
`lake build` **exit 0, 3017 jobs, zero warnings**, **283 `#print axioms` records (was 237), 0
outside Lean's three standard axioms**, hash drift 0, both validators exit 0. The substance:
**(1) `thm:tilted-log-band`'s OUTER half is DERIVED** (node `KSUM.B4b.L2.L2P3`) — the construction
(42) itself, the divided-difference annihilation, the ratio computation (44), and BOTH displayed
bounds `C_h ≤ 25/19` and `∑_j A_j ≤ 29/23`, so `⟨μ,F⟩ ≥ 437/581 > 3/4` now holds **with no
hypothesis**, where the module previously said in its own header that no theorem in it was the
LaTeX theorem. (The `25/19` needs the `d=1` factor peeled exactly; the flat Weierstrass estimate
gives only `4/3`.)
**(2) `thm:orientation-obstruction`'s analytic step PRODUCING display (51) is proved** (node
`KSUM.B4b.L2.ORIENT`) — endpoint phases (`I_s = -A_s`, `|A_s| = 1` even / `≥ 2^{-1/2}` odd), the
one-block Fourier modulus `2W_0·A^r` as an exact identity, the triangle inequality that survives
the `S_N` average, and `corr ≤ 1/8` (even `s`) / `≤ 1/2` (odd `s`) outright for all `r ≥ 2, m ≥ 2`.
Clause (b) is no longer only "(51) ⇒ ≤ 1/2".
**(3) `thm:block-obstruction` clause (iii)'s `ρ_j ≤ 4/5` is DERIVED from the tilted inner** (node
`KSUM.B4b.L2.T4`), through the manuscript's OWN three-weight step instantiated at the manuscript's
own normalized weights; what remains a hypothesis there is structural (which measure the block
carries), not numeric.
**(4) `lem:band-multiplication`'s convolution reduction is closed at the block splitting** (nodes
`KSUM.B4b.L2.BANDMULT`/`FILT`) — `A^{N₁+N₂} ≃ A^{N₁} × A^{N₂}`, occupancy additivity, and the
pushforward of the lifted product = the convolution.
**(5) `prop:embed` is CONSTRUCTED for ALL `k ≥ 3, n ≥ 1, R ≥ 2`** (node `KSUM.A2`), from the
manuscript's parameter display, with `c_P = k(k-1)2^{k-2}` depending only on `k` — closing the
fidelity review's per-instance-vs-uniform caveat on `Θ_k(R^{k-1})`.
**(6) `prop:joint-lp` now has exact primal AND dual certificates for all 24 LPs** (node
`KSUM.B4b.L2.JOINTLP`, new module `KsumAudit/JointLP.lean`), six of them kernel-checked — the
subset that decides rows 1 and 3 of display (39), including its sharpest separation `5/7 > 2/3 >
3/5`. **Value-vs-formula: the optima were RECOMPUTED independently and are IDENTICAL to the
manuscript in all 24 cases; display (39) is reproduced exactly. No mismatch.**
**A new FINDING, F-LP-1:** `sympy.solvers.simplex.lpmin`/`linprog` return INFEASIBLE points on
these Chebyshev duals (minimal reproducer in the report), so the duals are computed by a purpose-
written exact rational simplex, `tools/exact_simplex.py`. The manuscript is unaffected — the
ancillary script uses `lpmax` on the primal, and every primal witness re-verifies exactly.
**Resisted, each with an exact residual recorded on its node:** the pair-tensor `ℤ_q`
pair-orientation and labeled→occupancy pushforward (H-4(a), `KSUM.B4b.L2.M1`, verbatim from batch
1); `thm:block-obstruction` clause (i)'s `m`-fold multivariate Vandermonde plus the block-module
design call (H-3); the `S_N`-average operator of the convolution reduction; the inner pair tensor
as a measure on `ℤ_q^N`, which is what still keeps the LaTeX `thm:tilted-log-band` and the
`φ`-identification of `thm:orientation-obstruction` out of the kernel; and `prop:rosmanis`(1)
(H-7), which was gated on capacity and never reached. Every new or changed statement is on the
delta-fidelity queue at `KSUM.LEAN.statement-fidelity`; the executor reviewed none of its own work.

**Previous change — 2026-07-31 LEAN GAP-CLOSURE BATCH 1 (items L-1 … L-7): four of the seven
commissioned gaps CLOSED, three reported RESISTED with their residuals named. NO STATUS MOVED —
the graph is unchanged (no node added or removed, no edge re-typed).**
Report [`artifacts/ksum_lean_gapclose1_20260731.md`](../../../artifacts/ksum_lean_gapclose1_20260731.md),
evidence [`artifacts/logs_ksum_lean_gapclose1_20260731/`](../../../artifacts/logs_ksum_lean_gapclose1_20260731/):
`lake build` **exit 0, 3015 jobs, zero warnings**, **237 `#print axioms` records (was 193), 0
outside Lean's three standard axioms**, hash drift 0, both validators exit 0. The substance:
**(1) `lem:factorial-filtration` is PROVED, both directions** (new module
`KsumAudit/FactorialFiltration.lean`, node `KSUM.B4b.L2.FILT`) — the bridge the statement-fidelity
review named as *the root cause of tier T3's headline NARROWER*. The `(N)_m` normalization is
present and proved to be the right constant; the manuscript's idempotence/incompatibility
reductions are discharged by the monomial index set; and the same module adds the uniform orbit
lift with its occupancy pushforward and `ℓ¹` identities, which is the second half of the bridge and
was separately named as missing in `ObstructionsPairTensor` and `ObstructionsBandMult`.
**(2) `lem:band-multiplication` clauses (a) and (d) are PROVED** — (a) as the paper's own
integral-domain argument on generating polynomials in `MvPolynomial A ℚ`, which is what makes
clause (c)'s `ℓ¹` normalization legal.
**(3) `prop:transfer-facts` (G2) now stands at the manuscript's own "nontrivial `H`-satellite"
hypothesis**: the Maschke dictionary is proved, not granted.
**(4) `KSUM.B1` has a node module and its Claim is PROVED** (unconditional in the donor —
`abi`/`tani` unused), `import KSUM.B1` is in `KSUM/goal.lean`, and `KSUM.B2.DonorClaim` finally
carries its `k` argument, closing the review's §10 KSUM-layer caveat (2).
**A new FINDING is on `KSUM.B1`:** `KSUM.A1.Claim` (= `A1d`, a numeric floor) does **not** imply
`KSUM.B1.Claim` (a reduction), so the drawn edge `A1 → B1` is an edge between BRANCHES, not between
the two Claims; `composition_via_A1` is declared with its hypothesis explicitly not consumed, and
repairing the edge is a lead call.
**Resisted, each with an exact residual recorded on its node:** the pair-tensor-specific lift to
query polynomials on `Z_q^N` (the `Z_q` pair-orientation and the labeled→occupancy pushforward);
the convolution reduction (the `A^{N₁+N₂}` block splitting); `thm:block-obstruction` clause (i)
(an `m`-fold multivariate Vandermonde — the linearity half IS proved) and clause (iii) (blocked
upstream by `thm:tilted-log-band` being unformalized); and `prop:rosmanis`(1)'s orbit bijection and
count (`C(σ)`'s `(C₂≀S_m)×S_τ` structure is itself an unformalized T2 caveat, and Mathlib has no
`p_{≤m}` counting function). Every new or changed statement is on the delta-fidelity queue at
`KSUM.LEAN.statement-fidelity`; the executor reviewed none of its own work.

**Previous change — 2026-07-31 FIDELITY CLOSEOUT BATCH APPLIED: the review's eight honesty
defects are repaired, its three non-vacuity gaps are CLOSED WITH WITNESSES, its one WIDER is
closed, and hash drift is now a validator ERROR. NO STATUS MOVED — the graph is unchanged.**
Report [`artifacts/ksum_lean_closeout_20260731.md`](../../../artifacts/ksum_lean_closeout_20260731.md),
evidence [`artifacts/logs_ksum_lean_closeout_20260731/`](../../../artifacts/logs_ksum_lean_closeout_20260731/):
`lake build` **exit 0, 3011 jobs, zero warnings**, **193 declarations printed (was 176), 0 outside
Lean's three standard axioms**, both validators exit 0. The substance, in the order it matters:
**(1) The two live frozen-Claim hash breaks are gone and can never again hide behind "validators
exit 0"** — `KSUM.A2b` (`fe3f827d…` → `e1154f27…`, and the module's "FROZEN CLAIM (verbatim …)"
quotation is verbatim again) and `KSUM.B1` (`4d8818e1…` → `aa324409…`, plus its `lean.reason`,
which still denied that B1's Claim was a proposition six weeks after the §7.4 rewrite made it one);
and `tools/proof_dag_check.py` now emits §7.6 check-3a drift as an **ERROR**, verified by negative
control (corrupt a hash ⇒ exit 1) and by a clean repo-wide run (293 nodes) afterwards.
**(2) Three vacuity questions the review left open are now answered on disk.**
`KSUM.Support.demoEmbed` inhabits `EmbedData`, so the four `∀ D : EmbedData` Claims (`A2a`, `A2b`,
`A2`, `B2`) are no longer "machine-checked but not machine-checked to be about anything";
`KSUM.B4.sandwichModel` is an alphabet-aware model satisfying `B4a.Claim` **and** `B4bClaim`
simultaneously (`sandwich_nonvacuous`), the first evidence that `KSUM.B4.composition` composes
compatible hypotheses — `demoModel` provably cannot, its length-only `N^{2/3}` falling below
`c·N^{1/2}q^{1/4}` at `q ≈ N`; and five `core_reduction_at` witnesses at `r ≥ 1` (at the rightmost
window target, where the modulus hypothesis is tight) finally exercise the repair batch's *new*
content, the four older ones all being `r = 0`. Each closure is a CONSISTENCY witness in the sense
`demoModel` is one: **none of them is quantum query complexity, and the true-`Q` obligation of
§11 is untouched.** **(3) `KSUM.B4a.Claim` gained `thm:k2-upper`'s `q ≥ 2`** — the audit's single
WIDER — and `KSUM.B4.composition` still closes, since it uses that Claim only at `5 ≤ q ≤ N`.
**(4) Record honesty:** the Lean README no longer says `A1a`/`A1c` are merely stated (they are
proved) nor that `Obstructions*` is unadopted (adopted 2026-07-30, with an explicit
adoption-is-not-fidelity warning carrying the review's 6-labels/9-clauses NARROWER count); the two
work-package-`T2` modules are in the table; §7.8 mechanization tiers are now separated from the
campaign's `T1/T2/T3` work-package names; `Trust.lean`'s `lem:core` row can no longer be read as
"`lem:core` is FAITHFUL" (only the whole-core-sum sub-clause is; the subset-range clause stays
base-target-only); and the `#print axioms` coverage is stated as arithmetic (193 printed of 276
`theorem`/`lemma`s, helpers transitively covered) instead of the false "every top-level
declaration". The §7.9 scope clauses were left byte-for-byte — the review called them exemplary.
Node count 142; endpoints, root and every status unchanged.

**Previous change — 2026-07-31 GATE G-L3 CLOSED: the consolidated statement-fidelity review
landed and was applied; the Lean audit's four children are all CERTIFIED\*.** The reviewer executed
all six §7.10 duties itself (build reproduced exit 0 / 3011 jobs; census clean — 176 declarations
at exactly the three standard axioms, zero sorry/axiom/native_decide; 7c anchoring worksheets on
every ruled clause, executors' tables read LAST). Verdicts **F 42 / N 23 / W 1 / D 0 / infra 12**,
zero DIVERGENT; rollups T1/T2/T3/KSUM-layer all **PASS-WITH-CAVEATS** → tier nodes and the
fidelity node move **NUMERICAL/OPEN → CERTIFIED\*** (single review = starred tier, caveats in
frontmatter); `KSUM.LEAN` recomputes OPEN → **CONJECTURED**, capped by its restated composition
obligation (census table). Substance: the kernel CONFIRMS `thm:product-obstruction`, the block
correlation identity (49), transfer (G1)/(G3), band-mult (b)/(c), the whole T1 chain and the T2
cores; it does **NOT** confirm the orientation obstruction, the block degree/ρ clauses, or the
tilted-band witness — **T3's NARROWER count rose from 4 labels to 6 labels / 9 clauses** (three
findings T3 had self-marked FAITHFUL: block (i) product-rows-only, block (iii) ρ≤4/5 assumed, G2
satellite-via-Maschke; plus orientation (a) as a counting identity). One WIDER: `B4a.Claim` drops
the paper's `q ≥ 2` (benign, queued). Honesty verdict **FAIL on record-accuracy only** — 8
staleness/drift defects (README ×3, two LIVE frozen-Claim hash breaks A2b/B1 concealed by
warning-level checker output, B4 prose/Lean q-range divergence, Trust row precision, findings not
on audited nodes — the last repaired in this same change) — with an explicit finding of ZERO
scope-overstatement anywhere. Closeout batch dispatched: H-1..H-8 + m-1/m-2, three cheap
non-vacuity closures (demoEmbed; a B4-sandwich witness model; a `core_reduction_at` r≥1 witness),
B4a `q ≥ 2`, and promotion of hash-drift from checker warning to ERROR. A1's promotion was
independently confirmed substantively correct (procedural caveat recorded). Standing
conditionality restated: T1/A1c-interface/compositions are exactly as strong as
ABI21+Tani24+facts(i)/(ii)+F1/F2; T3 and the T2 cores are unconditional; whether the true `Q`
satisfies the interface is open and unprovable here. Node count 142; endpoints and root unchanged.

**Previous change — 2026-07-31 A1 PROMOTED TO PROVED (review license applied) + B1 →
CONJECTURED (mechanical recompute).** The composition-layer review's §3.1 license — "PROVED once
R-A1-1 and R-A1-3 land" — became unconditional when the repair batch implemented both repairs
machine-checked; the lead verified the new Claim texts against the reviewer's prescriptions
(every-window-target quantifier, coset membership `s = t + k·a`, explicit `/C` constant — all
present in the Lean statements) and wrote **A1: CONJECTURED → PROVED** citing review + repair
artifacts (rule 2: the reviewer licenses, the lead writes after verification). `KSUM.A1.holds` now
closes the A1 Claim relative to the declared interface (ABI/Tani, facts (i)/(ii), freeze) — the
k≥3 floor's reduction chain is composition-checked end to end. Mechanical §1 propagation:
**B1 OPEN → CONJECTURED** (one live route with A1 PROVED and the near-trivial route proof
unwritten); **goal unchanged, OPEN on exactly one live route (B2, donor-blocked)**. Node count 142.
Next gate in flight: the consolidated statement-fidelity review (G-L3) over T1+T2+T3+repairs+the
KSUM composition layer — the only thing that can lift the Lean tier nodes above NUMERICAL.

**Previous change — 2026-07-30 REVIEW-REPAIR BATCH: the two `A1` claim defects are FIXED, the
`A1` composition is RE-PROVED against the repaired children, `B4`'s vacuous Lean claim is scoped,
and the `goal → B4` edge is re-typed to `related`.** Four commissioned repairs, all landed, build
green (`lake build`, 3011 jobs, `BUILD_RESULT: exit=0`, **176 declarations printed, 0 outside
Lean's three standard axioms**, zero `sorry`/`axiom`/`native_decide`/warnings).
**(1) `KSUM.A1a` (R-A1-1 + R-A1-3):** the frozen Claim is widened to *"a frozen core of `k−2`
coordinates, PLUS the parked coordinate when `N−(k−2)` is odd, valid at EVERY window target"* — the
reviewer's exact prescription — and **proved in that widened form**, unconditionally, by the new
`KsumAudit.KFloor.core_reduction_at`. T2's NARROWER caveat (base target only) is closed. The
window hypothesis `(k²−2)K+2k−1 ≤ q` did **not** have to move: it is exactly the master inequality
at the rightmost window target `r=k−1`, tight there — which is also why `lem:transl-cover`(ii)
carries the same threshold. The base-target theorem survives as `core_reduction`/`holds_base`.
**(2) `KSUM.A1c` (R-A1-3):** the Claim is restated as the COSET-COVERING statement — *for every `t`
there is a window target `t′ ∈ t+kZ_q` with `Q(kSum_t) ≥ Q(kSum_{t′})/C`* — and **PROVED with
`C=2`** (`holds` ← `Q_window_cover_coset`), so `lean.state` moves `stated → proved` and
`lem:transl-cover` is now formalized end to end. The refuted all-pairs rendering is preserved,
unproved and consumed by nothing, as `ClaimAllPairs`, beside `not_reachable_k3_q21`.
**(3) `KSUM.A1`:** the composition was **re-proved, not patched** — the old proof consumed the
refuted all-pairs premise. It now runs in the manuscript's order (cover first, then freeze at the
covered window target). **Consequence: all three child Claims are theorems, so `KSUM.A1.holds`
closes `A1d`'s conclusion relative to the interface and the named non-vacuity gap F-R8 is CLOSED,
not narrowed.** Review §3.1's PROVED licence is now unconditional in its own terms — **the write
is the lead's, not the executor's (rule 2), so `A1` still reads CONJECTURED here.**
**(4) `KSUM.B4` (R-B4-1) + the `goal → B4` re-typing (review §5.4):** `B4bClaim`/`Claim` are
restricted to `q` odd with `5 ≤ q ≤ N` (the `thm:main-odd` regime), so the `q=2` unsatisfiability
witness is out of scope and the mechanized sandwich is no longer vacuous — the *prose* half of
R-B4-1 remains owed at the decision layer; and `goal`'s children become `[B1,B2,B3]`, `B4.parents`
becomes `[]`, the retired route entry is kept verbatim under a renamed key, the Mermaid edge is now
`G -.-> B4`, and `import KSUM.B4` is removed from `KSUM/goal.lean` (§7.6 check 6: the import graph
must agree with `children`). **No epistemic status changed anywhere** — `A1` CONJECTURED, `A1a`/
`A1c` PROVED, `B4` OPEN, root **OPEN** on one live route (B2). Claim hashes re-synced:
`A1a d9b25ae9→5a70591b`, `A1c 049957e5→ed56ed4d` (both superseded texts printed in the Lean
headers). Report: `artifacts/ksum_lean_repair_batch_20260730.md`; evidence:
`artifacts/logs_ksum_lean_repair_20260730/`.

**Previous change — 2026-07-30 LEAN TIER T2 LANDED, and it turned `KSUM.A1c`'s Lean Claim into a
CONFIRMED DEFECT:** the `k`-floor combinatorial cores and the Rosmanis barrier are machine-checked,
**unconditionally** (neither new module imports `QueryModel`). Two new modules —
`KsumAudit/T2KFloor.lean` (`lem:core`; `prop:core-even` + `lem:core-odd` as the single theorem
`core_reduction`, covering both parities through `m ∈ {k-2, k-1}`; the `lem:transl-cover` window
arithmetic (i)/(ii) and the Bezout coset-covering step) and `KsumAudit/RosmanisBarrier.lean`
(`prop:rosmanis` (1), (2)-witnesses, (3)). Build green: 3011 jobs, `BUILD_RESULT: exit=0`, **162
declarations printed and 0 outside Lean's three standard axioms**, zero `sorry`/`axiom`/
`native_decide`, zero warnings. **`KSUM.A1a.Claim` is now PROVED unconditionally** (`lean.state`
`stated -> proved`), so two of `KSUM.A1.composition`'s three leaf hypotheses are theorems and the
reorg pass's finding F-R8 narrows to one. **`KSUM.A1c.Claim` is NOT provable** — it renders
`lem:transl-cover` in an all-pairs-of-targets form while the manuscript's covering argument is
coset-local; three independent derivations now agree (prose composition pass, review finding R-A1-3,
this tier), and the in-range machine-checked obstruction is `KSUM.A1c.not_reachable_k3_q21` at
`k=3, q=21` (R-A1-3's own witness `k=3, q=3` lies OUTSIDE the Claim's range hypothesis
`q_0(3)=19 <= q` — reported, not silently reconciled). The Claim was neither proved nor reshaped
(repair is a lead decision); the faithful content was proved instead: `Q_kSum_translate_le`,
`Q_window_cover` (for every target there IS a window target within factor 2), `Q_le_of_coprime`.
`prop:rosmanis`(1)'s count `>= 2` is proved **orbit-proper** — the `S_N x C(sigma)` action is
defined, shown to preserve `D_0`, and the separating invariant is PROVED invariant — in both
manuscript branches; **the bijection with `(f, lambda)` and the formula `sum_f p_{<=m}(N-f)` are NOT
formalized**, and neither is part (2)'s representation sentence (only its two finite witnesses are).
Also NOT attempted: `prop:embed`, and `prop:core-even`/`lem:core-odd` at every window target rather
than at the base one. **New F-T1-pattern finding: `prop:rosmanis` has NO DAG node at all** — no node
file, no index row, only Lean-audit nodes naming it as scope — despite `sec:branch-ledger` citing it
as the structural reason a whole DAG leaf is dead; registering it is a rule-8a decision for the lead
and was NOT done here. `LeanT2` moves OPEN -> **NUMERICAL · pending-review: LeanFid**; no other
node's epistemic status changed; root stays **OPEN**; endpoints unchanged.
Report: `artifacts/ksum_lean_T2_rosmanis_kfloor_20260730.md`; evidence:
`artifacts/logs_ksum_lean_T2_20260730/`.

**Previous change — 2026-07-30 T3 ACCEPTANCE PASS + F-T1 REPAIR (lead):** T3 deliverables
independently spot-checked and accepted (build exit 0 re-read; 58/58 axiom-clean in
`print_axioms.txt`; SHA ledger re-verified 29/29 over the LF/RAW convention; no `QueryModel` import
in the tier; views in sync; both validators exit 0). The two nodeless labels exposed by F-T1 are now
REGISTERED — `B4bL2Filt` (`lem:factorial-filtration`, the occupancy-rows→query-degree bridge whose
absence made `thm:pair-tensor` NARROWER) and `B4bL2JointLP` (`prop:joint-lp`, script-delegated exact
optima with no printed dual certificates) — both CONJECTURED · pending-review, `related`-only edges,
with the recorded rule-8b breach and the M1 edge-typing question left to the composition-layer
review. ORIENT carries a dated partial-confirmation note (clause (a) machine-checked; clause (b)
only as "(51) ⇒ ≤1/2"; status unchanged under its archived review). Node count 138 → **140**.
In flight next: T2 (Rosmanis orbit count + k-floor cores) and the composition-layer prose review;
the consolidated statement-fidelity review runs after T2 lands. Root **OPEN**, endpoints unchanged.

**Previous change — 2026-07-30 LEAN TIER T3 LANDED: the obstruction group is machine-checked,
UNCONDITIONALLY, and the audit found four NARROWER statements — one of them on an obstruction.**
The lead-mandated terminal deliverable of the Lean audit is in. The eight `Obstructions*` modules
left UNADOPTED by an interrupted executor were **audited before being built on** (adopt-or-rewrite,
rendering every Lean statement back into English from the Lean alone before reading the LaTeX):
**ADOPT 44 / REPAIR 0 / REJECT 0**, plus **14 theorems added** to close gaps the audit found.
Build green (3009 jobs, exit 0), **58 declarations at exactly Lean's three standard axioms**, zero
`sorry`, zero `axiom`, zero warnings (all 16 fixed). **No `QueryModel` anywhere in this tier**, so
unlike T1/T2 every theorem here is UNCONDITIONAL — which is exactly why this tier was mandated.
**Fidelity: 6 FAITHFUL, 4 NARROWER, 0 WIDER, 1 AMBIGUOUS-IN-SOURCE.** The one NARROWER that bites
is `thm:orientation-obstruction` **clause (b)**: Lean *assumes* the paper's displayed bound (51)
and derives `corr <= 1/2`, so the Lean tier does not confirm that obstruction clause — clause (a)'s
exact `2^{-r(m-1)}` factor IS proved. The other three (`thm:pair-tensor`, `thm:tilted-log-band`,
`lem:band-multiplication` clauses (a)/(d)) are positive claims, where NARROWER means the audit
under-delivers rather than that the paper over-claims. **Two hypothesis substitutions in the draft
were found and PROVED AWAY** — the rule-7 failure mode caught by the kernel: `prop:transfer-facts`
(G3) had `tr A != 0` where the paper says "every NONZERO PSD `A`" (now proved: PSD with zero trace
is zero), and (G2) had `R_H v = 0` where the paper says "`v` lies in a nontrivial `H`-satellite"
(now proved: `R_H v = 0` iff `v` is in the augmentation submodule). New this run: general-`m` band
multiplication (the draft had only `m = 2,3` against a paper that quantifies over `m`), the mixture
VALUE `2^{1-r}` for `thm:product-obstruction` (only the ratio form was checked), the `q`-indexed
value budget (no draft theorem mentioned `q`), and the first non-vacuity witnesses for the T4
correlation identity and for (G2). **Two of the nine in-scope labels have NO DAG node at all** —
`lem:factorial-filtration` (the bridge from falling-factorial rows to QUERY polynomials, and the
reason `thm:pair-tensor` is NARROWER) and `prop:joint-lp` (whose exact LP optima need dual
certificates the manuscript does not print; it delegates to an ancillary Python script). Both are
named gaps, not silent omissions. Manuscript repair recommended: `thm:block-obstruction` never says
which "block label" `OR_m` reads — only its proof does. **No status changed anywhere else**: all
ten obstruction nodes stay PROVED, `LeanT3` moves OPEN -> **NUMERICAL · pending-review: LeanFid**
(a build is a run, §2/§7.1), `Lean` stays OPEN, root stays **OPEN**, endpoints unchanged.
Report: `artifacts/ksum_lean_T3_obstructions_20260730.md`; evidence:
`artifacts/logs_ksum_lean_T3_20260730/`.

**Previous change — 2026-07-30 §7 LEAN REORGANIZATION + COMPOSITION LAYER MECHANIZED
(lead directive; DAG_PROTOCOL.md §7 "Lean is the machine-readable form of the same DAG"):**
the lake project moved `research/ksum/lean/` → `research/ksum/proof-dag/lean/` (§7.2, a sibling of
`nodes/`; forwarding stub left behind, T1 sources byte-identical by raw-SHA cross-check), and a
**DAG-mirroring layer** was written on top of it: module name = node id, one module per
participating node, the node's Lean `composition` theorem IS its composition proof (§7.3/§7.4).
Seventeen modules — the twelve node modules `A1a A1b A1c A1d A1 A2a A2b A2 B4a B4 B2 goal` plus `Interface`, `Support/*`,
`Trust`, `SelfTest` — build green, **sorry-free and axiom-clean** (3009 jobs, exit 0; 106
declarations printed, and the only axioms appearing anywhere are Lean's three standard ones).
**Two composition proofs now carry machine-checked mathematics.** `KSUM.A1.composition`
(`A1a ∧ A1b ∧ A1c ⇒ A1d`) closes **relative to exactly the four premises `A1`'s composition block
already declared** — ABI21/Tani24, facts (i) and (ii), and the unstated coordinate-freezing
principle **F1** — with **no extra hypothesis**, in particular no `gcd(k,q)=1`. `KSUM.A2.composition`
(`A2a ∧ A2b ⇒ A2`) likewise, and it **DISCHARGES A2's standing `gcd(k,q)=1` obligation**:
`KSUM.A2.coprime_k_q` proves `gcd(k,(P+1)(M+1))=1` from `k∣P` and `2(M+1)=(2k+1)^{k-1}+1`, i.e.
the construction FORCES it (`lem:embed-allt`) — and `A2a`'s own 2026-07-19 review had already
verified it, so the hypothesis was never missing from the disk, only from `A2`'s `rel`.
`KSUM.B4.composition` makes the "same `(N,q)`, not one slice" requirement structural rather than
prose; `KSUM.B2.composition` mechanizes the donor transport and **names the gap** that its novelty
side condition (is the transported bound NEW?) is not rendered — the omission that killed L2e/L2f.
`KSUM.goal` is **intentionally claim-free**: the goal's frozen Claim is a target description, not a
proposition, and the modus-ponens "route schema" was declined as content-free. Two quantifier
findings, both checked against the manuscript rather than guessed: `A1c`'s "all t via gcd argument"
carries **no** coprimality hypothesis (coverage runs off the window length `≥ k ≥ gcd(k,q)`), and
`A1`'s composition needs the parked-coordinate case (`m ∈ {k-2, k-1}`) to reach every `N`.
`SelfTest.lean` `decide`s 33 definitional checks, each definition with a positive AND a negative
case. **No status changed anywhere** — a green build is a run (§2, §7.1) and is evidence for the
pending rule-6/rule-7 reviews of the `A1`/`A2` composition claims, not a review; `A1`/`A2` stay
CONJECTURED, root stays **OPEN**, endpoints unchanged. Sync fix in the same diff: the nested
outline's `LeanT1` status word, stale at `[OPEN]` since the T1 landing, now reads
`[NUMERICAL · pending-review]` like the node, index and Mermaid. Report:
`artifacts/ksum_lean_reorg_20260730.md`; evidence: `artifacts/logs_ksum_lean_reorg_20260730/`.

**Earlier same-day change — 2026-07-30 §1 COMPOSITION PASS (lead directive: an edge is an obligation,
not an implication; Lean merged into the DAG protocol as §7):** every internal node now carries a
frozen `composition:` block — AND composition claims on `A1`, `A2`, `B2`, `B4`, `KSUM.LEAN`; route
maps on `KSUM.goal`, `B1`, `B3`, `B4b`, `k3.donor`, `L32`. Statuses recomputed bottom-up under
`min(composition, children)` / `max min(child, route)`: **`A1` and `A2` PROVED → CONJECTURED** —
their children stay PROVED and the theorems live on the reviewed leaves (`A1d`, `lem:embed`); what
was never on disk is the parent composition proof, now written and awaiting review (review restores
PROVED). Substantive premise gaps surfaced by writing the compositions: A1's coordinate-freezing
principle (in no child, no printed fact — **independently = Lean-audit finding F1**), A2's
`gcd(k,q)=1` (living only in a work-log line). Route-level: `B1→GOAL` and `B3→GOAL` kills argued at
proposer tier (floor `2/3 < k/(k+1)`; G11), REFUTED pending rule-6 review; `B2→GOAL` conditional on
the one named donor hypothesis; `goal→B4` edge type QUESTIONED (k=2 vs k≥3, no route proof ever
attempted). Edge re-typings (structural, no status change): `A1e` caveat + `A1f` certification
record + `B4b.U1` obstruction outcome all `children→related`; `L32→L32a` flagged. Root **OPEN**,
unchanged — now for explicit reasons. T3 Lean executor interrupted by session limit (partial
modules on disk, unadopted); T1 landed earlier the same day (see below). Endpoints unchanged: no
new bound.

**Earlier same-day change — 2026-07-30 Lean audit OPENED (lead directive):** six nodes registered under
rule 8a/8b BEFORE any commission — `Lean` (AND parent), `LeanT1` (k=2 lower-bound main line),
`LeanT2` (Rosmanis orbit count + k-floor), `LeanT3` (obstruction group; **lead-mandated terminal
deliverable**), `LeanFid` (statement-fidelity completion gate), and `LeanAltQM` (the road not taken:
formalizing the query model itself, OPEN·PARKED with a revival condition). Environment gate **G-L1
PASSED**: Lean `v4.31.0` + Mathlib `v4.31.0` build green (1982 jobs) at `research/ksum/lean/`,
reusing a machine-local prebuilt package cache. Three standing scope clauses, written on the parent
node: the cited bounds (ABI, Tani, query-model facts (i)/(ii)) enter as **structure fields, not
proved content**, so a Lean-verified derivation is exactly as strong as those citations and no
stronger; **`lean-checked` is an evidence attribute, never a status**, and a green build with
`LeanFid` OPEN licenses nothing; the audit is **confirmatory and can only demote** — it produces no
new bound. Endpoints unchanged. Frontier unchanged.

**Earlier change — 2026-07-23 rule-7 review batch CLOSED (both CONFIRMING):** the G1 review
(PASS + two MINOR repairs: cosmetic exponent; sign-rep escape closed via Young's rule) licenses
**REFUTED · DEAD** on `hs-query-energy-law` — the 14th refuted node — scoped strictly to the
HS-energy-only route with the polar/range-reducing siblings expressly preserved. The β1 review
(no MAJOR/GAP; C2 extended to q=17 with an independent closed form; C4 re-verified with the
reviewer's own moment map; C1 re-grounded on exact moment-row-space/kernel invariance and
verified through q=11; C3 ruled a finite observation, capped at NUMERICAL) licenses
PROVED-scoped status for the C1/C2/C4 identities on `profile-lattice-core`, whose node status
remains OPEN (main multi-pair non-product construction untouched). Both reviews archived with
independent gate scripts and SHA ledgers. Frontier unchanged: the `>=3-active-pair`
non-product coefficient law. Endpoints unchanged: no new bound.

**Earlier same-day change — 2026-07-23 β batch CLOSED; both proof languages converge on one missing
object:** β0 verified all four ChatGPT-reported sources (1503.07261 / 1302.6191 / 1710.09079 /
2002.08389 all VERIFIED-MATCH) and extracted the collision-dual mechanism card (sum of two
components cancelling exactly on one shared bad orbit; 8 sigma-twist rework points). β1
(outcome class B): K2 = CONTAINS (the proved q=5 germ is an exactly-feasible LP point of the
new boundary-pairing ansatz); K1's kill condition did not fire, but the ansatz as written has
NO q-gain — the `<=2-active-pair` support is exactly q-independent, and activating `Theta(q)`
pairs by a product pays exactly M2's `2^(1-(q-1)/2)`; K4 passes. First positive q-trend on the
lower-bound side: the super-threshold full-orbit ceiling grows `0.533<0.587<0.618` for
q=5/7/9 at `N=8,D=5` (decelerating; G11 — no asymptotic claim). Batch verdict: the live
frontier in BOTH languages is the same zero-sample object — a multi-pair (`>=3` active pairs)
NON-PRODUCT coefficient law (L3's M7 in SDP language, the super-threshold region here in LP
language). Per the boundary-stop directive no further commissions auto-launched; consolidated
report delivered to the lead. `profile-lattice-core` stays OPEN with NUMERICAL evidence
pending review. Root unchanged (OPEN).

**Earlier same-day change — 2026-07-23 β batch launched (lead-approved):** with the first gate batch
negative on L3 (G1 OUT-OF-BUDGET, G2 NOT-ASSEMBLABLE/M7), L3 is suspended pending a coefficient
law and the β track opens: β0 = verify-before-cite of the collision-dual/mass-correction sources
plus a formula-level mechanism card; β1 = concrete occupancy-profile ansatz with exact `q=5`
shadow check against the preregistered kill criteria K1/K2 of
`B4bL2AltNonproductProfileLatticeCore`. Stop rule preregistered: K1 or K2 failure ⇒ full stop
and consolidated final report (boundary-stop directive). No status changes in this entry.

**Earlier same-day change — 2026-07-23 gate G1 executed; first Opus 4.8 batch CLOSED:** the HS-loss
quantification returns OUT-OF-BUDGET: `L >= sqrt(f^lambda* f^mu*) = Theta(q^alpha)` with
`alpha >= 3/4` (most favourable reading; `>= 2` for the pure energy route) against the retarget
budget `alpha < 1/12`; at `a=16,q=64` the loss is `q^0.667`–`q^2.99` vs tolerated `~1.41`.
Mechanism is structural (query localisation breaks position symmetry; position carriers
`f^lambda, f^mu >= n-1 = Theta(q^(3/2))` do not cancel; position-trivial adversaries capped at
`Theta(N^(1/3))`). Secondary: the literal masked-query HS identity is absent from disk (stub);
the two documented strict gaps only add loss. `hs-query-energy-law` moves to NUMERICAL —
pending-review with its kill criterion firing; REFUTED/DEAD awaits an independent rule-7 review.
Batch verdict recorded with G2's NOT-ASSEMBLABLE/M7 result; no further commissions launched
pending lead decision (boundary-stop directive). Artifact:
artifacts/ksum_L3_hs_loss_quantification_20260723.md.

**Earlier same-day change — 2026-07-23 gate G2 executed (first Opus 4.8 batch):** the payload value
test returns the pre-registered NOT-ASSEMBLABLE class: the reviewed `a=16,q=64` components do
not compose into the compressed-model candidate `Gamma`. Seven file-level missing pieces: four
private point-children tables; `Omega_tau` kernel unevaluated; native transfer `K_s`
unassembled; query polar/range norm interface unfixed (exact guard `1/4 != 1/2` reconfirms
compressed defect != true norm); outer numerator map undefined; `19456` slice not norm-complete;
no adversary coefficient law — the scalar choice collapses to the `N^(11/18)` baseline. All
finite verification gates on the present components PASS. NUMERICAL — pending-review; finite
diagnostic only (G11), not a refutation. Artifact:
artifacts/ksum_L3_payload_value_test_a16_20260723.md. G1 (HS-loss quantification) still
running; no new commissions pending batch evaluation (boundary-stop directive).

**Earlier same-day change — 2026-07-23 gate-plan registration (strategy layer, no mathematical
adjudication):** four nodes registered under rule 8 BEFORE any commission: `B4bRetarget`
(milestone relaxed to any `eta>1/6`; total bridge-loss budget `q^(1/12-delta)` at
`q=Theta(N^(2/3))`; CONJECTURED pending review), `B4bCompcap` (screening cap: disjoint-block
factorized constructions with currently proved block hardness top out at `q^(1/6)`;
CONJECTURED), `B4bL3AltCriticalInducedPacketPayloadValueTest` (gate G2: finite `a=16,q=64`
assembled compressed-model value vs matched composition baseline; OPEN), and
`B4bL2AltNonproductProfileLatticeCore` (occupancy-profile exact-cancellation dual, kill criteria
preregistered; OPEN). Lead directives of the same date: executor layer = Opus 4.8 subagents
(codex retired); commissions in small batches with stop-and-evaluate (boundary-stop). Root
unchanged.

**Earlier change — 2026-07-22 fast close of the active L3 gates:** fresh Rule-7 review gives the
equivariant-sufficiency PARTIAL theorem **MINOR / STRICTLY SCOPED PASS**, review SHA-256
`79259DD8A49B9CB05E22BF3CFB892E75F23540772B31F8E455DCA38AB7690E5F`. Full `Hom_(S_q)` closure
is banked for the fixed invariant candidate, but `19456` is not norm-complete and the two named
successors are Wigner-facing interface packages, not the only remaining tasks. The literal-query
package, its off-diagonal polar-block priority law, range-reducing conditional law, Hilbert--Schmidt
fallback, and the outer numerator package now each have canonical OPEN nodes. The active private-
child run and first `s=7` discriminator were interrupted before final outputs during fast wrap-up;
neither supplies a mathematical verdict, and both obligations remain OPEN.

**Earlier same-day change — 2026-07-22 uniform occurrence count and finite YES central-insufficiency
receive fresh Rule-7 scoped passes:** the exact legal-family formula is
`C_s=sum_(j=0)^(s-2)p(j)`, so the registered quadratic joint candidate first fails at `s=6`, where
`C_6=12` rather than eleven. This refutes the proposed exhaustive natural-module realization but,
by dimension alone, not an abstract `Q^3 direct-sum M_8(Q)` action with repeated simples. The
separate exact finite `s=6` algebra now receives fresh Rule-7 **PASS / STRICTLY SCOPED PASS** and is
`M_1(Q) direct-sum M_11(Q)`, review SHA-256
`A7EA6C9633942262181E8E255F406FD2C9C13376FF61162F8222BD0F0FFB1389`. This is not an all-`s`
law. The Rule-8-registered next discriminator computes the full `s=7` algebra before testing a
partition-indexed centralizer/connectivity proof. Uniform multiplicity review SHA-256:
`991FC187F7C0AA65D44B54CCC355679DFB84060B52BEA57A167CB0DEC022BF22`.

At `s=4,a=16,q=64`, the finite YES common-child physical assembly and central decision also receive
**MINOR / STRICTLY SCOPED PASS**. The reviewed fixed-mark component, ranks, covariance, five-child
inventory, and two-completion guard prove that the common child alone cannot determine the literal
central transfer. The four private children and an equivariant-sufficiency decision gate are now
active; no full transfer spectrum, taper, norm, numerator, or exponent is licensed. Review SHA-256:
`A2DA44F5BE33F73CB4C84F4AD8C586F8AC7407C6E57059D4E3C764816B965052`.

The common-child Schur-coset reducer now receives fresh Rule-7 **PASS / STRICTLY SCOPED PASS** on
the three-parent, position-carrier-suppressed `Hom_(S_64)` model. It verifies the forced
`A^1 B A^0` order, factors `3780/61,180/59,189/124`, and dimension `19456`; review SHA-256
`E062009CA2BBD47A2EE0DB8BA5D667D2793430E55CBC587A9F7388DB65A0B6D6`. The registered next gate
asks whether this explicitly invariant block-multiplier construction closes entirely on
`Hom_(S_q)`. Only if that gate fails is the full nontrivial-carrier/Wigner spectrum required for
this candidate. Private children and all feasibility/asymptotic obligations remain open.

**Earlier same-day change — 2026-07-22 second-target `s=5` occurrence reducer receives fresh Rule-7
MINOR / STRICTLY SCOPED PASS:** a hostile blind model independently reconstructs `C_5=7`, all six
ranks and commutators, common commutant dimension three, generated-algebra dimension twenty-seven,
and the exact rational decomposition
`M_1(Q) direct-sum M_1(Q) direct-sum M_5(Q)`. The sole minor corrects the radical-normalized
matrices to a real algebraic extension; the rational calculation already uses `A=G^(-1)H` and is
unchanged. Review:
`artifacts/ksum_L3_critical_induced_packet_second_target_s5_occurrence_rule7_review_20260722.md`,
SHA-256 `B53F416DAF1B698E2FF13638589A32F89B555D6E491CA44040D8D0E6B7EE1506`.
Together with reviewed `s=4`, this authorizes—but does not prove—the registered all-`s` candidate
`C_s=1+binom(s-1,2)`,
`A_s=Q^(s-3) direct-sum M_((s^2-5s+10)/2)(Q)`. Formula-level prove/kill work is now active.

**Earlier same-day change — 2026-07-22 finite YES alphabet gate receives fresh Rule-7 MINOR / SCOPED
PASS:** at `a=16,q=64,t=1,tau=(61,2)` and one fixed raw mark, a genuinely isolated checker banks
the complete `1|5|10` parent closure, all sixteen marked columns, the eight-projector `C^8`
resolution, unequal-cell normalization, and both rank-ten orientation images with their full
six-column unmatched complements. Review:
`artifacts/ksum_L3_critical_induced_packet_yes_alphabet_point_child_gate_a16_rule7_review_20260722.md`,
SHA-256 `BE1B4BD6BD7D2D39459FB94B23ECA1B47DDEA31BC26469FAAE5BCC5578DE6D23`.
This is one finite same-fixed-mark alphabet factor only: it proves no distinct-mark table,
occurrence/Pieri assembly, NO-to-YES central transfer, joint spectrum, feasible adversary,
attenuation, numerator, or exponent. The already Rule-8-registered next gate now tests whether
exact `S_q` covariance upgrades this fixed-mark input to the literal all-`z` rectangular transfer;
otherwise it must stop and specify the missing distinct-mark rows.

**Earlier same-day change — 2026-07-22 L3 occurrence and alphabet point-child factors receive fresh
Rule-7 reviews:** at finite `s=4`, the six occurrence matrices receive **PASS / STRICTLY SCOPED
PASS** and generate `M_1(Q) direct-sum M_3(Q)`. At finite
`a=16,q=64,t=0,tau=(61,2)`, with one fixed common raw mark, the NO same-mark alphabet factor
receives **MINOR / SCOPED PASS**: its six projectors form `C^6`, sum to the identity, and include
nonzero cross-parent blocks. Together with the reviewed corrected transported Pieri table, these
factors have now been assembled into the finite NO/fixed-same-mark physical pencil. Fresh Rule-7
**MINOR / SCOPED PASS** verifies effect-level active/full commutator ranks `8/32` and the surviving
`M_3` core. This proves no YES assembly, distinct-mark child, uniformity in `a,q`, feasible adversary,
attenuation, numerator, or asymptotic exponent. Reviews:
`artifacts/ksum_L3_critical_induced_packet_first_target_exact_wreath_occurrence_reducer_rule7_review_20260722.md`,
SHA-256 `1741AD66F658E28BEC4EE7E606052EBE5F575FA35069BFA4C285B0364861AC12`, and
`artifacts/ksum_L3_critical_induced_packet_alphabet_point_child_gate_a16_rule7_review_20260722.md`,
SHA-256 `4A8FEE28DFD4FC91EEB6E7B5F89BC8A0A3C26491895AC1AFE6889982E1560137`.
The corrected transported finite Pieri recoupling scalar table has fresh Rule-7
**MINOR / SCOPED PASS**; the typed identities require an explicit `rho_lambda(g)`.
Proposer artifact:
`artifacts/ksum_L3_critical_induced_packet_first_target_pieri_recoupling_scalars_a16_20260722.md`,
SHA-256 `07EF9D8E3BBC901B19E74D1F457C7E7BF0BD0607B14FF6B629A8EB60640012DC`.
Review:
`artifacts/ksum_L3_critical_induced_packet_first_target_pieri_recoupling_scalars_a16_rule7_review_20260722.md`,
SHA-256 `DB65748CCE7C8F7E6541A203B9BEAE072DB479B58CBC090100156E9101A273CF`.
Physical-assembly review:
`artifacts/ksum_L3_critical_induced_packet_first_target_no_physical_assembly_a16_rule7_review_20260722.md`,
SHA-256 `24D6803403119E4673606380C74A329C965DCDB912CAC84AF9ACAD9071257112`.

**Earlier same-day change — 2026-07-22 L3 direct-coset cross-side factorization receives fresh Rule-7
MINOR / SCOPED PASS:** the canonical complete selected projector is a product over every physical
coset, including the full YES complement. Aggregate left/right source effects commute for every
`z,w` in both answers; same-`z` commutation survives actual status, ordered-position,
compatible-heavy-path, and central common/private point-child refinements; and the native
rectangular transfers commute and are simultaneously unitarily diagonalizable. This makes the
exact native cross-side noncommuting-Sylvester leaf REFUTED/DEAD. Same-side effects, different-`z`
point children, orientation pullbacks, nonproduct full-type truncations, spectra, resolvents,
attenuation, and numerator remain open. Review:
`artifacts/ksum_L3_critical_induced_packet_direct_coset_cross_side_factorization_rule7_review_20260722.md`,
SHA-256 `C3A7DFD24286F6C74A111DD01981D284E9A17F08B10E007766AC22AF0DDDECEB`;
checker/log SHA-256 `A1AB28656C147EFEE01AF5074DFFCC51F4AB9D7A6920A0A7716067EAF207A0B1` /
`FD3A6F672841EA0F367F6DBEEFC268CF45D5F1C6D13BA4BFC3535F2290ABB873`.
Separately, fresh Rule-7 review now promotes the exact Phase-30 balanced positive-split support
to REFUTED/DEAD: its two-factor actual Chebyshev separator has weight `<D` and forces every
normalized low-row annihilator to have correlation `o(1)`. Other balanced supports and the
balanced/dense mixture remain outside scope. Fresh macroscopic-chain review returns PARTIAL: the
corrected interior/common-auxiliary adjacent two-row `Theta(m)` chain remains near-isometric and
its physical marked maps retain `1-o(1)`, but endpoint and scope defects forbid a broad ruling.
Fresh non-skeleton review is also PARTIAL: after correcting the positive-effect/literal-map typing,
the first exact sign/rectangle carrier has sandwiched equality coefficient only `O(1/a)` and both
queries retain `1-o(1)`; two printed type identities fail. Both broad L3 nodes remain OPEN. Rule 8
records the two precise outside-scope successors before work: a cyclic full
Young-rank balanced harmonic and a non-scaled many-corner plethystic/occurrence kernel. Fresh
full-Young review is PARTIAL: it independently confirms the exact `1-1/q` physical retention on
the complete trivial-alphabet sector, but corrects the proposer's illegal endpoint sequence to
`a=k^2,d=4k-1`. The non-scaled audit has also found an exact three-row constituent with growing
occurrence multiplicity. Its block-standard coefficient is exactly `sum_(j=0)^(r-2)p(j)`, but the
complete single-cell raw frame is identity on that occurrence index and the opposite query retains
`1-o(1)`. Fresh review of this block-standard result is PARTIAL: it confirms the actual `r>=4`
physical family and scoped no-go, but the formal `C_r=1` regime has no required opposite invariant,
the coefficient matrix is square rather than arbitrary rectangular, and several local definitions
need repair. Fresh review of the preceding trivial-alphabet three-row audit is PARTIAL: all coefficient,
legality, occurrence, and physical no-go values survive, but proposer (6.3) is ill-typed for
`c>1` and must use the composition `A F_z`, not `F_z tensor A`. A true two-box bicovariant alphabet
tensor occurs exactly once in each of `(q-2,2)` and `(q-2,1,1)`, but the completed proposer audit
finds every fixed-single-irrep raw effect at most `I/2`, forcing both queries to retain
`1/2-o(1)`. Fresh independent Rule-7 review passes this formula-level obstruction, so the exact
single-full-type node is REFUTED/DEAD. That audit generated a distinct mixed-full-type successor,
registered before calculation: the symmetric and alternating two-box blocks share a
point-stabilizer constituent even though their legal unmarked full-group blocks are orthogonal.
The completed mixed proposer audit finds that the physical cell projection reduces each usable
common weight to exactly `1/(2a)`; summed cross-full-type outputs vanish by Schur orthogonality, so
both queries still retain `1-o(1)`. Fresh independent Rule-7 review passes the complete typed
obstruction and promotes the exact `nu_+ direct-sum nu_-` two-box leaf to REFUTED/DEAD (review
`artifacts/ksum_L3_critical_three_row_mixed_two_box_full_type_recoupling_rule7_review_20260722.md`,
SHA-256 `0D6AA6C0AFE42716A9DBC4F0D85D0E2FC9722998432A7C1AA032B445E5F79506`). This ruling does not
cover the complete induced alphabet packet, another alphabet partition, more than two full types,
or another position parent. The complete-packet first gate now has a fresh Rule-7
**MINOR / SCOPED PASS** on the exact `p=0,u=1,q=4a` quotient: the full NO packet embeds
isometrically in YES, `J_L^*J_R` is the normalized `J(2a,a)` swap walk, and the literal marked
mass is `1/a+(a-1)/a=1`. This total does not make the orientation average uniformly near-isometric:
for `A=(J_L+J_R)/2`, `A^*A=(I+K)/2`; an external occurrence identity likewise requires an
explicit common occurrence isometry. The review refines every full-type multiplicity by
`c_(nu,j)=[s_nu]s_(2a-j,j)s_(a-1,1)^2` and corrects the baseline wording: the immediate
orbitals equal the old two-orbital formulas, while general scalar Johnson-degree laws are only
contained in the support-quotiented UIC architecture, not equal to arbitrary addressed UIC.
It also warns that the one-dimensional `a=2` heavy fiber does not make all full-type
multiplicities one. The broad packet node remains OPEN because neither query attenuation nor the
numerator is proved. Review SHA-256
`CF1E853AE7BEBC689963409A03D19BBA96684AF0C4BBAF4ED59155E2F64741F2`.
Rule 8 records the complete induced-alphabet-packet successor and, before fallback calculation,
Rule 8(b) also records three nonseparable induced-packet successors: a matrix-valued Young
holonomy law, a joint parent-content kernel, and a divergence-free plaquette-flow law. They are
queued behind the packet's scalar-orientation and literal marked-point gates. Before any new
coefficient calculation, the joint-parent route was split into an occurrence-pencil prerequisite,
a deprioritized scalar total-energy resolvent, and a conditional native cross-side Sylvester law.
The direct-coset review now settles the complete aggregate cross-side algebra: every left effect
commutes with every right effect, and the native rectangular transfers commute. The conditional
noncommuting-Sylvester leaf is therefore REFUTED/DEAD. The classification additionally banks two
separate finite factors: the `s=4` occurrence algebra `M_1(Q) direct-sum M_3(Q)`, and the
`a=16` NO/same-mark alphabet algebra `C^6` with nonzero cross-parent coupling. It remains OPEN
because those factors have not been assembled through the reviewed corrected Pieri transport into
a physical pencil at reviewed finite NO/fixed-same-mark scope: its noncommutative core survives,
with active/full commutator ranks `8/32`. YES, distinct-mark, uniform/asymptotic, and
feasibility/query claims are absent. The rectangular transfer-resolvent on `Hom(E_0,E_1)` remains OPEN even though its two
native transfers are simultaneously diagonalizable; no joint eigenvalues, deterministic taper,
attenuation, norm, or numerator are known. The scalar total-energy law remains OPEN/deprioritized
and must still pass its one-dimensional-collapse gate. The same strategy pass
Rule-8-registers a separate globally bounded symmetrized-polynomial
fallback. It explicitly relies on off-promise `[0,1]` boundedness, because the promised orbits
alone admit a degree-two cross-collision separator; it is OPEN and deprioritized behind the
growing-occurrence audit. Earlier fresh reviews promoted the exact weighted-activation dense slice and the exact
two-row/global-standard `L_d plus R_d` covariant direct sum to REFUTED/DEAD. Earlier same-day work
found that three registered non-sampling upper architectures give no
`o(N^(2/3))` attack on the exact critical shelf:
duplicate classification and direct statistics cost `O-tilde(N^(5/6))` in their best audited
realizations, while the optimized soft-filter walk reduces to ordinary Johnson at
`Theta(N^(2/3))`. This is scoped negative algorithmic evidence, not a lower bound. The exact
orbit-intertwiner system kills the local two-orbital span at `Theta(N^(1/3))`, recovers the
addressed `N^(11/18)` block, and isolates the missing `m^(1/6)` gain. The declared strict full-
low-degree projector architecture is defeated by exact degree-two through degree-nine promise-
kernel, role, transfer, and anti-concentration witnesses; its generic split/bottom estimates and
all provisional progress exponents are withdrawn. Fresh Rule 7(a)–(g) review passes after two
major corrections, so that exact full-low-degree certificate-support architecture is now
REFUTED/DEAD. The standalone square signed-cycle family is likewise REFUTED/DEAD after fresh
Rule 7(a)–(g) review of its universal constant marked/unmarked ceiling and legal `p=0` subsequence
giving `o(m^(1/6))`. Neither result touches the
separately Rule-8-registered nonseparable rectangular outer-UIC/address-cycle kernel, now the sole
prioritized lower construction. Its exact `C/uC` incidence normalization and query-mask compression now
pass, but the first transition-selected pointed-hook law retains a marked branch `(a-1)/a` and
stays at `N^(11/18)`. Exact Schur pairing caps every one/two-endpoint higher-Specht selector, and
the complete fixed two-block `P/Q` algebra has only the ordinary `sqrt(m)` ratio. The first formula
in each growing Rule-8 successor now also fails: true multiplicity-one repaired-full-matching
transport is input-wise unitary with marked block `I_r`, while a hidden-selector-star law is
forgotten by incidence and returns to the `P/Q` cut; disjoint grouping loses outer scale. Genuine
LR multiplicity `c=r+1` exists, but every fixed middle operator fails by marked-branch convexity.
Natural two-matching cycle words reduce to standalone Hecke kernels plus two capped endpoints.
Full position incidence is now exactly classified by a pair of jointly quotiented transportation
matrices and strictly exceeds the old address data, but raw/fixed-centered contingency minors and
exterior powers are fixed-middle and have a norm-retaining marked branch. Two explicit
`Theta(m^(1/3)) x Theta(m^(1/3))` parent grids fail because a unique heavy-unselected predecessor
retains `1-o(1)` norm. The shared-branch repair is also obstructed at target-controlled size:
first-row deletion is an injective almost-unit pivot throughout the singleton/Pieri cone, so no
exact Young harmonic exists there and every `o(m)` patch has down norm `1-o(1)`; a fresh Rule-7
review independently passes this scoped result after correcting three restricted-matrix typings. A genuine growing
same-parent transportation multiplicity does exist, but its first `nu=(q)` family is again
near-isometric for every coefficient matrix because equality pinching is scalar. Replacing it by
the global standard hook passes common multiplicity, but the first separately invariant type-cell
product family has equality pinching only `O(1/q)` and also retains `1-o(1)` query norm. The
registered noncoverage boundaries are a macroscopic `Omega(m)` parent patch and a non-skeleton
heavy-occurrence carrier. The single-cell covariant block-standard coupling has now been computed:
its multiplicity grows, but the opposite physical side retains `1-o(1)` norm. The minimal
two-cell `L_d/R_d` repair is also obstructed: its raw frame is sector block diagonal,
so at least one physical query retains `(1/2-o(1))||B||` for every matrix. Fresh Rule-7 review
passes after restoring literal polar-lifted maps, and this exact family is REFUTED/DEAD. The first
non-skeleton sign/rectangle family now closes its alphabet gate negatively at proposer tier:
correctly summing both global predecessor branches gives raw pinching `O(1/a)` and retained query
norm `1-o(1)`. The adjacent two-row macroscopic chain is also near-isometric and physically
retained. Both broader nodes remain OPEN pending independent review of these scoped outcomes.
Promise-ideal and reachability-sensitive strict fallbacks are registered but deprioritized. The
quotient-only version of the former has a proposer-tier dichotomy, and its exact query-module Hom
continuation is now also zero: the answer quotients have disjoint joint spectra, while degree-two
equality projectors already resolve the YES identity. Only a general nonintertwining masked
adversary remains, with no automatic quotient benefit. The
universal linear version of the latter is now REFUTED/DEAD after fresh Rule 7(a)–(g) review: the
span of all `T`-query state families equals the full restricted degree-`T` image. Nonlinear or
algorithm-dependent carriers remain untested in a separate successor. The endpoint, L3, and root
remain OPEN. Artifacts:
`artifacts/ksum_L3_critical_nonsampling_upper_attacks_20260721.md` and
`artifacts/ksum_L3_critical_orbit_intertwiner_attempt_20260721.md`, and
`artifacts/ksum_L3_critical_strict_injection_recording_attempt_20260721.md`,
`artifacts/ksum_L3_critical_strict_injection_rule7_review_20260721.md`, and
`artifacts/ksum_L3_critical_signed_cycle_weight_attempt_20260721.md`,
`artifacts/ksum_L3_critical_signed_cycle_rule7_review_20260722.md`, and
`artifacts/ksum_L3_critical_coupled_uic_address_cycle_attempt_20260721.md`,
`artifacts/ksum_L3_critical_coupled_higher_specht_attempt_20260722.md`,
`artifacts/ksum_L3_critical_coupled_multiblock_inner_attempt_20260722.md`, and
`artifacts/ksum_L3_critical_reachability_span_audit_20260722.md`, and
`artifacts/ksum_L3_critical_reachability_span_rule7_review_20260722.md`, and
`artifacts/ksum_L3_critical_promise_ideal_quotient_audit_20260722.md`, and
`artifacts/ksum_L2_balanced_positive_split_scalar_selector_obstruction_20260722.md`, and
`artifacts/ksum_L3_critical_macroscopic_two_row_parent_chain_audit_20260722.md`, and
`artifacts/ksum_L3_critical_macroscopic_two_row_parent_chain_rule7_review_20260722.md`, and
`artifacts/ksum_L3_critical_nonskeleton_highest_plethystic_pieri_audit_20260722.md`, and
`artifacts/ksum_L3_critical_nonskeleton_highest_plethystic_pieri_rule7_review_20260722.md`, and
`artifacts/ksum_L3_critical_full_young_rank_balanced_harmonic_feasibility_20260722.md`, and
`artifacts/ksum_L3_critical_full_young_rank_balanced_harmonic_rule7_review_20260722.md`, and
`artifacts/ksum_L3_critical_nonscaled_plethystic_many_corner_candidate_audit_20260722.md`, and
`artifacts/ksum_L3_critical_nonscaled_plethystic_many_corner_rule7_review_20260722.md`.

**Prior change — 2026-07-21 B4bL3 conditional lift audit:** the critical-core pSearch bridge
passes every theorem and embedding interface. Conditional on one uniform exact-orbit bound
`Adv+/-(HF_(B,kappa))=Omega(B^(2/3))`, BHK zero-support composition and exact integer choices give
the full `Omega(min{sqrt(N)q^(1/4),N^(2/3)})` curve, including fixed `q`, the crossover/cap,
side sentinels, leftover and odd padding, arbitrary targets, and cyclic range `O(q)`. The flattened
composition is exactly the critical shelf, with its block image a restriction of the full
permutation orbit. The antecedent remains wholly OPEN; the implication is not a lower bound by
itself. Artifact: `artifacts/ksum_L3_critical_core_psearch_lift_audit_20260721.md`.

**Prior change — 2026-07-21 B4bL3 critical adversary baseline:** the exact frozen critical
promise now has a theorem-backed addressed subfunction lower bound
`Adv+/-=Omega(a^(2/3)sqrt(d+1))=Omega(N^(11/18))`, with all integer remainders, partial-outer
composition, label interfaces, and query simulation closed. No `Omega(N^(2/3))` adversary or
`o(N^(2/3))` algorithm was found. The remaining `N^(1/18)` address-erasure gain is isolated as an
explicit matrix between the two legal orbits with numerator `Omega(N^(2/3))` and all query masks
bounded by one, or an equivalent strict random-injection recording-query progress theorem. Three
non-sampling upper attacks are registered before dedicated testing. Artifact:
`artifacts/ksum_L3_hidden_frequency_critical_adversary_attempt_20260721.md`.

**Prior change — 2026-07-21 B4bL3 multiscale upper envelope:** the complete
sample/delete/compress family is governed by the Laplace residual
`D(ell)=R+sum_j h_j M_j exp(-ell M_j/N)`. It does not universally beat the target. A legal
two-scale law with one macroscopic decoy, `Theta(q)` decoys of multiplicity `Theta(sqrt(q))`, and
singleton candidates leaves `Theta(q^(3/2))` critical-shelf mass and makes the optimized envelope
`Theta(sqrt(N)q^(1/4))` throughout `5<=q<=N^(2/3)`. This is not a lower bound; duplicate tests,
joint walks, and joint statistics remain unaudited. The shelf appears to coincide with the
pSearch-expanded critical core, so the conditional lift and direct multiscale views may reduce to
the same critical endpoint donor. Artifact:
`artifacts/ksum_L3_multiscale_frequency_upper_envelope_20260721.md`. An independent exact-spectrum
pass reaches the same scale: residual compression forces the lowest decoy multiplicity
`m>=sqrt(q)`, while quantum distinct-label enumeration forces `m<=sqrt(q)`. Its rounded law,
range, embedding, and endpoints pass, and deleting the reservoir leaves exactly
`B=Theta(q^(3/2))`. Artifact: `artifacts/ksum_L3_multiscale_frequency_candidate_20260721.md`.

**Prior change — 2026-07-21 B4bL3 critical-core scaling candidate:** a new Rule-8 node records
the conditional bridge from one critical donor to the whole quarter-power curve. If a range-`q`
critical promise on `B=Theta(q^(3/2))` positions has complexity
`Omega(B^(2/3))=Omega(q)`, coordinatewise `q`-valued
`pSearch_(Theta(N/B))` composition formally yields
`Omega(q sqrt(N/B))=Omega(sqrt(N)q^(1/4))`. This identity is registered before source/interface
verification and is not yet a theorem: outer-promise composition, constants, integer regimes,
range, padding, and the actual critical donor all remain OPEN. Canonical:
`research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.critical-core-psearch-lift.yaml`.

**Prior change — 2026-07-21 B4bL3 hidden-frequency pass:** the exact balanced rare/heavy
promise and its constant-query arbitrary-target cyclic 2-SUM embedding are now frozen. A hostile
upper-algorithm pass gives `O-tilde(q+sqrt(N)q^(1/6))`, strictly below
`sqrt(N)q^(1/4)` for every polynomial `q=N^kappa`, `0<kappa<2/3`; hence this single-scale
profile cannot close the uniform window. The critical `q=Theta(N^(2/3))` instance remains open:
all audited sample/frequency/Johnson attacks meet the `N^(2/3)` cap, but a local donor audit finds
no theorem-backed lower bound (ABI/Tani gives only `N^(11/18)`). Rule 8 therefore registers the
narrow critical endpoint and a new active multiscale-frequency-mask candidate before further work.
L3/B4b/B4/root remain OPEN; no completion-tier refutation is claimed. Artifacts:
`artifacts/ksum_L3_hidden_frequency_promise_20260721.md`,
`artifacts/ksum_L3_hidden_frequency_upper_attack_20260721.md`, and
`artifacts/ksum_L3_hidden_frequency_donor_audit_20260721.md`.

**Prior change — 2026-07-21 B4bL3 first pass:** three independent local-corpus passes close
the parameter-only escape. Tani already optimizes unequal-domain independent-pSearch parameters;
fixed relabels collapse to one complement code; and the ABI-composable certificate remains at
`O(sqrt(N)q^(1/6))`. A concrete shared-address correlated gadget passes exact claw and cyclic
2-SUM embedding but transposes to an OR of ordinary claws and again has a
`O(sqrt(N)q^(1/6))` algorithm. This does not refute L3: direct fixed relabeling losslessly transfers
the full small-range claw problem. L3 remains OPEN only for a genuinely global donor/composition
with no independent buckets or searchable latent coordinate; B4b/B4/root remain OPEN. Artifacts:
`artifacts/ksum_L3_asymmetric_claw_parameter_audit_20260721.md`,
`artifacts/ksum_L3_correlated_gadget_attempt_20260721.md`, and
`artifacts/ksum_L3_fixed_relabel_ceiling_20260721.md`.

**Prior change — 2026-07-21 B4bL2 phases 14–30:** the selective route has an exact weighted-
projection normal form. One-parameter, balanced, finite-palette, and separated rich-palette `q=N`
laws all admit sub-target Chebyshev separators. A critical dense mixture now raises known
separators to target order and leaves the genuine constant window
`0<c<(arcosh 3)/2` at `D=cN^(2/3)`. At `q=5`, the canonical Hahn law fails analytically at fixed
`D=3`, while smooth boundary/radial/Christoffel repairs fail finite target-scale gates.
At `c=1/2` in the large-endpoint window, full-orbit finite correlations are nonmonotone and the
two largest feasible gates fall below `2/3`; Phase 23 identifies the decisive row as the mixed
moment `sum_i s_i x_i` and types the full large-endpoint problem as a growing multisymmetric Gram
operator whose absolute-value/tail sign asymptotics remain open.
Canonical and single-entry label-aware moving circuits both fail on correlation and global
equioscillation. At `q=5`, an ordinary continuum support density is singular: correlation lies in
normal boundary layers and discrete corner jets where rounding is leading order. The resulting
stratified boundary-jet Remez system has now been analyzed: its fixed four sectors are incomplete,
direct corner-to-normal matching is exponentially ill-conditioned, and scalar `xi` loses actual
orbit rows. Phases 25--26 scope out canonical and overcomplete one-orientation ladders, naive
exactors, and canonical exposed-phase pairing; exact correction is typed by a canonical dual
defect. Phase 27 then finds an explicit smaller-constant shared-NO construction that passes every
`q=5` endpoint gate and a fresh Rule-7 MINOR/PASS independently verifies it, so that scoped node is
PROVED. At `q=N`, an
exact parity tail plus perfect low bridge passes raw gates but fails scalar cross moments.
Phases 28--30 show that separated bands, positive-scale ladders, `o(D)`-level ladders, and natural
same-total near-zero paired bridges are all subtarget-selectable. Coupling an exact parity tail to
the full mixed residual closes exact moments, tail, and normalization. A latent Boolean argument
proves `Z_D>0`, but a follow-up global Chebyshev polynomial in `C=sum_i x_i` combines with the
activation low-tail estimate to force this explicit bridge's correlation to `o(1)`. A fresh
independent Rule-7 review passes that scoped formula-level obstruction on sufficiently large
admissible odd `N`. The separate weighted-activation OR dual-composition node now has its own
freshly reviewed dense-slice obstruction: a weight-`<D` scalar separator forces correlation
`O(exp(-N^(1/6)/5))`. That exact node is REFUTED/DEAD; balanced positive splits are outside scope
and remain registered OPEN.
B4bL2 remains CONJECTURED;
B4b/B4/root remain OPEN.

**Prior change — 2026-07-20 B4bL2 phase-7 web feasibility pass:** the natural
center/Jucys–Murphy implementation fails proposer-tier separation/cross-`N` gates, while a direct
Bun–Thaler-style two-ray orbit construction gives exact common-bad-profile cancellation, constant
correlation, and only a logarithmic explicit band. A candidate Chebyshev argument caps the entire
two-ray support class at `O_tau(sqrt(N))`, uniformly in `q`, so it cannot meet the `N^(2/3)`
endpoint at `q=N`. New related nodes `B4bL2AltTworay` (CONJECTURED · pending-review) and
`B4bL2AltMultipair` (OPEN, no formula yet) record the outcome and surviving escape. B4bL2 remains
CONJECTURED; B4b/B4/root remain OPEN. Artifact:
`artifacts/ksum_L2_phase7_web_feasibility_20260720.md`.

**Prior change — 2026-07-20 B4bL2 component promotion / rule-8 remediation:** 18 reviewed,
scoped, blocked, conjectured, or not-pursued L2 components are now first-class canonical LEAF
nodes. They are conceptual children of B4bL2 but use only reciprocal `related` edges, so they are
non-propagating evidence/tool/obstruction/alternative records rather than AND/OR proof children.
This is a structural migration only: B4bL2 remains CONJECTURED, B4b/B4/root remain OPEN, and no
existing status changed. The node index, Mermaid cluster, and nested outline are synchronized.

**Prior change — 2026-07-20 B4b journal-version integration review completed (fresh
independent reviewer):** **PASS after minor statement/type repairs; no substantive or remaining
scope defect.** The integrated invariant algebra, exact finite LP table, M1 pair tensor, L2P3
tilted log-band witness, band-multiplication lemma, four formula-defined obstruction classes,
G1--G3 transfer facts, and conditional `F_SC^charge` certificate retain their reviewed scopes.
Aggregate L2P6-G remains discussion-only and explicitly CONJECTURED; finite optimizer data carry
no exponent inference. All nine ancillary copies match their reviewed source hashes; eight
standard-library scripts reran successfully, while the declared missing SymPy dependency prevented
the LP script from being rerun. The paper builds cleanly at 34 pages. Review:
`artifacts/ksum_merge_review.md`. B4bL2 stays CONJECTURED and B4b/B4/root stay OPEN.

**Prior change — 2026-07-19 B4bL2 phase-6 hostile rule-7 review:** multiplicity-gauge/
terminal-label insufficiency, direct nontrivial-vector Reynolds zero, and positive
diagonal/Reynolds band zero are **PROVED components**. Fresh exact code reproduces correlations
`49/95` and `5/7`; read-only certificate reconstruction verifies both held-out labels, requested
Adv± values, and 91–92% oracle diagnostics. MAJOR D14 keeps aggregate L2P6-G **CONJECTURED** because
the optimizer-faithful transfer class is not formula-defined and the two displayed maps are not
exhaustive. The literal label-coordinate/direct-vector/positive-diagonal mechanism is
**BLOCKED/reviewed**; signed canonical-multiplicity and cap-scale witnesses remain open. B4bL2 stays
CONJECTURED and B4b/B4/root stay OPEN. Review: `artifacts/ksum_L2p6_review.md`; fresh run:
`artifacts/logs_ksum_L2p6r_20260719/`. The executor and older phase-5 headings below remain history.

**Prior change — 2026-07-19 B4bL2 phase 6 non-composition transfer (executor; review now
completed):** exact `S_(N-1) x C(sigma)` labels identify the trivial spine, the tau-indexed
standard satellites, and the `tau=0` bipartition `((1),(1))` repetition-two sector. Both frozen
held-out label predictions pass; held-out-refit rank-one oracle diagnostics exceed 91%, but no
no-refit capture is defined because multiplicity coordinates have independent orthogonal gauge.
The proposer candidate says nontrivial vector satellites average to zero and positive
projector-diagonal transfers have constant moment one/band zero. Exact `(4,5,0)` and `(5,5,0)` gates
pass. Final component and aggregate statuses are governed by the completed review above. Report:
`artifacts/ksum_L2_phase6.md`; run: `artifacts/logs_ksum_L2p6_20260719/`.

Canonical per-node records and the Mermaid-to-ID/alias map:
[`../proof-dag/NODE_INDEX.md`](../proof-dag/NODE_INDEX.md). In particular, legacy `L2`, `L2a`, and
`L2b` resolve to `KSUM.k3.donor`, `KSUM.k3.donor.zhang-tani`, and
`KSUM.k3.donor.dream`. The node files were initialized as faithful mirrors of this append-only record.

**Most recent change — 2026-07-19 B4bL2 phase-5 hostile rule-7 review:** the general `S_N`-averaged factorial/Vandermonde band-multiplication lemma is a **PROVED component**. The exact NO orientation loss `2^{-r(m-1)}` and Fourier/l1 bound `corr<=1/2` are also **PROVED** for the hard class of identical phase-3 blocks with one common exact pair total on every pair and block and a product outer tensor. Fresh code reconstructs all four exact gates and adds complete `m=3` identities. MINOR D13 hardens the class label. That selected family is **BLOCKED/reviewed**; unequal totals, nonidentical blocks, non-product couplings, alternative inners/non-composition shapes, and the cap-scale witness remain open. B4bL2 stays CONJECTURED; B4b/B4/root stay OPEN. Review: `artifacts/ksum_L2p5_review.md`; fresh run: `artifacts/logs_ksum_L2p5r_20260719/`.

**Prior change — 2026-07-19 B4bL2 phase 5 averaged shared-value composition (executor; review now completed):** the exact occupancy convolution retains a formal multiplied band, but shared values reduce true-NO mass. The completed review above supplies the final scoped component rulings and hard family boundary. Report: `artifacts/ksum_L2_phase5.md`; run: `artifacts/logs_ksum_L2p5_20260719/`.

**Prior change — 2026-07-19 B4bL2 phase-4 hostile rule-7 review:** the logarithmic-inner bound `rho<=4/5`, fixed-allocation unaveraged sign-bit composition identity, and whole-pair budget are **PROVED components**. MAJOR D10 rejects carrying the product upper bound through a possibly norm-reducing symmetry average and renormalization. The preregistered mechanism remains **BLOCKED** because the PROVED budget `sum_j r_j<=(q-1)/2` independently prevents `m` from tracking `N` at fixed `q`. Fresh exact reconstruction verifies the printed `(10,5,0,2)` formulas and adds identity/pattern gates at `m=3`. B4bL2 remains CONJECTURED and B4b/B4/root remain OPEN. Review: `artifacts/ksum_L2p4_review.md`; fresh run: `artifacts/logs_ksum_L2p4r_20260719/`.

**Prior change — 2026-07-19 B4bL2 phase 4 band-amplification obstruction (executor; review now completed):** the proposer recorded a BLOCKED outcome for standard absolute-value OR composition and whole-pair allocation. The completed review above proves the fixed-allocation and budget components, but limits the correlation-product obstruction at the symmetry-normalization boundary. Report: `artifacts/ksum_L2_phase4.md`; run: `artifacts/logs_ksum_L2p4_20260719/`.

**Prior change — 2026-07-19 B4bL2 phase-3 hostile completion review:** the general L2P3 component is **PROVED** for every odd q>=3, N>=q, and target: unit l1, full invariance, pure high degree at least `2(1+floor(log_5((q-1)/2)))`, and correlation at least `437/581>3/4`. Fresh exact-rational code passes every target at (5,5) and (7,3), including raw degree-zero/one query rows. MINOR D9 corrects the M2 escape scope: genuine escape holds for q>=5 by the invariant zero K=2 layer; q=3 is the in-class M1 endpoint. B4bL2 remains **CONJECTURED** because polynomial-scale amplification and the untouched sqrt(N) side remain open; B4b/B4/root remain **OPEN**. Review: `artifacts/ksum_L2p3_review.md`; fresh run: `artifacts/logs_ksum_L2p3r_20260719/`.

**Prior change — 2026-07-19 B4bL2 phase 3 correlated outer kernel (executor; review now completed):** a signed divided-difference tilt on the number of interior pairs passed the preregistered PROGRESS gate with a logarithmic band and correlation greater than 3/4. The completed review above proves the component lemma and repairs the q=3 M2-escape wording. Report: `artifacts/ksum_L2_phase3.md`; run: `artifacts/logs_ksum_L2p3_20260719/`.

**Prior change — 2026-07-19 B4bL2 phase-2 hostile completion review:** M1 is **PROVED** for general odd q, N>=q, and every target: cancellation holds separately on every exact-total size slice, falling-factorial order matches query degree, l1 is one, and the lift is invariant. M2 is **PROVED** for the precisely defined fully locally zero-balanced sign-separated product/sign-aligned-positive-mixture class, with correlation exactly 2^(1-(q-1)/2). MINOR D8 tightens that family label; correlated outer signed kernels remain outside the obstruction. M3 passes preregistration, G11, status, and odd-q scope checks. B4bL2 remains **CONJECTURED** with the cap-scale correlated witness open; B4b, B4, and the root remain **OPEN**. Review: `artifacts/ksum_L2p2_review.md`; fresh exact outputs: `artifacts/logs_ksum_L2p2r_20260719/`.

**Prior change — 2026-07-19 B4bL2 phase 2 + delegated D7 sync:** the canonical obligation now implements the completed repair review's prescribed odd-q/all-target scope and labels even q optional, so B4bL2 was restored to **CONJECTURED · pending-review**. The first explicit exact-total pair tensor kills every query polynomial below degree q-1 with l1=1, but its correlation is exactly 2^(1-(q-1)/2), hence only 1/2 at q=5. This was a preregistered BLOCKED outcome for the independently zero-balanced sign-separated tensor construction, not the correlated route. Exact rational checks at (5,5) and (7,3) passed all claimed moments, norm, correlation, and centralizer invariance; G11 forbade exponent inference. Report: `artifacts/ksum_L2_phase2.md`; review conditioning the status sync: `artifacts/ksum_L2r_review.md`.

**Prior change — 2026-07-19 B4bL2 corrected-repair hostile review:** the strict (>2/3) predicate and all 24 exact finite LP bands independently pass; certified degrees are single-to-joint (0\to2), (0\to2), and (2\to3), with exact l1=1 and zero rational moment residuals. P2 remains shell-deficit-only evidence, and the capped degree formula passes both upper-bound sweeps. New MODERATE defect D7 remained at review time: the registered “exact” P4 statement silently strengthened the paper's odd-q gap to both even-q target cycle types, which C7 does not identify. The scope repair and resulting status sync are recorded above. Review: `artifacts/ksum_L2r_review.md`.

**Prior change — 2026-07-19 B4bL2 corrected-threshold repair (executor; review now completed):** strict correlation (>2/3) became the canonical direct-error-(1/3) test. Exact rational reruns gave certified degrees single-to-joint (0\to2), (0\to2), and (2\to3), so every finite joint gain survived and the all-points kill criterion did not fire. P2 remained shell-deficit-only evidence. The repair registered a capped P4 obligation; its scope defect is recorded in the completed review above. Addendum: `artifacts/ksum_L2_phase1_addendum.md`.

**Prior change — 2026-07-19 B4bL2 fresh hostile completion review:** all 24 finite rational LP optima and both shell deficits were independently verified. P2 is re-graded to the nonautomatic 25--27 percentage-point shell deficit because full-orbital capture is forced; the ±1 threshold 1/3 is sign approximate degree at error 1/3, not a direct Q_(1/3) >= d/2 certificate; and the uncapped P4 lemma is false at q=N because eta>1/6 exceeds the N^(2/3) walk cap. B4bL2 is **OPEN · review completed** pending a capped or restricted-range lemma; B4b, B4, and the root remain **OPEN**. Review: `artifacts/ksum_L2p1_review.md`.

**Prior change — 2026-07-19 B4bL2 phase 1 (executor; review now completed):** the frozen shell-deficit gate and exact finite LPs ran; the original report then registered the now-rejected uncapped P4 lemma. Report: `artifacts/ksum_L2_phase1.md`.

**Prior change — 2026-07-19 B4bL1 phase-1 family kill (executor; pending review):** the explicit three-class reciprocal-Hamming polar completion is PSD, commutant-invariant, and HLS-feasible, but even per-instance oracle-best balance fits capture only 38.90%--62.83% of the reviewed numerical optima and fall below 60% on five of six points. The commissioned P2 stop fired; no held-out prediction or solve and no P4 lemma followed. This kills the tested family, not the broad route: B4bL1 stays **OPEN · pending-review** under rule 6; B4b, B4, and the root remain **OPEN**. G11: fits are structure evidence only. Report: `artifacts/ksum_L1_phase1.md`.

**Prior change — 2026-07-19 Front-L structure reconnaissance (executor; pending review):** six high-accuracy MOSEK HLS-dual optimizers were extracted at the commissioned points with command/log/SHA provenance; the Zhang--BHK--ABI 1/6 chain was audited; and three candidate lower-bound routes were registered as OPEN OR-children B4bL1--B4bL3. G11 applies: structure only, no numerical exponent claim. B4b, B4, and the root all remain **OPEN**. Report: `artifacts/ksum_expL_structure.md`.

**Prior change — 2026-07-19 Front U fresh hostile completion review:**
**B4bU1 is CERTIFIED* only as a conditional charged-recurrence outcome.** The reviewer independently
re-derived the exponent map, invariant, nonuniform-depth Bellman monotonicity, residual MNRS balance,
pair-Grover cost, and dyadic multiplicity bound. A MAJOR family-boundary defect prevents PROVED: the
submitted family uses independent selector and compulsory child costs as accounting assumptions and
does not prove a composition lower bound for all algorithms informally called sample–compress. A
MODERATE plateau caveat limits rho>=2/3 to an all-q range-independent generic base; q-dependent and
residual-promise solvers remain escapes. B4b, B4, and the root remain OPEN. Review:
`artifacts/ksum_B4bU1_review.md`.

**Prior change — 2026-07-19 Front U exponent-balance audit (executor; pending review at write-time):**
New OR-route child **B4bU1** records a **CONJECTURED — pending-review** family obstruction.
For the precisely defined black-box sample–compress family F_SC, a level with child exponents
(a,c) has cost ell + sqrt(s) + s^a q^(a-1/2+c) ell^(-(a-1/2)); the binding equality gives
Phi(a,c)=(a/(a+1/2),(a-1/2+c)/(a+1/2)). Starting from the Johnson base (2/3,0),
c_D=1/4-(3/2)(a_D-1/2), so forcing the N exponent to 1/2 drives the q exponent to 1/4;
q^(1/6) would require a generic residual base exponent at most 3/5 or another exit from F_SC.
The audit found no gain from arity/depth schedules, alternative sample schedules, residual
Johnson/MNRS walks, counting variants, fixed-point handling, multiplicity stratification, coherent
amplification, or the on-disk nested-walk formula. This is not an all-algorithms lower bound and
does not close the global exponent window; B4b, B4, and the root remain **OPEN**. Canonical record:
`research/ksum/proof-dag/nodes/KSUM.B4b.U1.yaml`.

**Prior change — 2026-07-19 fresh hostile completing review:** **PASS; I1–I6 DISCHARGED,
0 substantive defects, 0 trivial manuscript defects.** The reviewer independently re-derived the
A1d cutoff/counterexample/plateau, the A2 all-target coprimality proof, and the B4a coherent-oracle
square-root-loss/hybrid argument, then rebuilt the 26-page paper and reran all requested validators.
All statuses and graph edges remain unchanged; the root remains **OPEN**. Review:
`artifacts/ksum_rev2_review.md`.

**Prior change — 2026-07-19 quantifier and proof-repair pass (independent review now completed;
statuses unchanged):** the A1d statement now records the proof's actual lower cutoff
q0(k)=2k²+2k−5, the range q0(k)≤q≤C_kN, and the separately supported plateau for
q≥c_kN. This corrects the former false “all q up to Θ_k(N)” wording; the F1-audited
fixed-K reduction already contained the threshold, so no status was changed. The manuscript also
replaces the composite-modulus counting argument for all-target embedding by the stronger proof
that the constructed modulus is coprime to k, and makes the coherent-oracle square-root error loss
explicit. These mathematics edits passed fresh independent review under rule 6; see
`artifacts/ksum_rev2_review.md`.

## How to read this

This file records the **search**, not just the current front. The central question is
**OPEN**: how far can the alphabet-size requirement in the Belovs–Špalek `Ω(N^{k/(k+1)})`
k-Sum lower bound be reduced, and what is `Q(N,k,q)` on the curve between `q=O(1)` (Grover
`√N`) and `q≥n^k` (BS, tight)? The `k=2` end is essentially settled in a separate report
(`KSUM_FINAL_REPORT.md`) — *settled at the threshold only*: the `k=2` **middle gap** (lower
`Ω(√N·q^{1/6})` vs the now-proved B4a upper `O_epsilon(N^{1/2+epsilon}q^{1/4})`
for `ω(1)≤q≤o(N)`) is still OPEN: the `q`-exponent gap `1/6<1/4` survives and
is mapped here in B4 (paper Open Problem `prob:k2-gap`). **This DAG is the `k≥3`
campaign plus the k=2 upper/direct-solver/incumbent branches.** Most branches below are OPEN, PARKED, or REFUTED. Nobody is rewarded for the tree
looking alive.

Decomposition semantics: an **OR-node** has alternative routes and an **AND-node** has jointly
required obligations. Statuses:
`PROVED` · `NUMERICAL` (finite-instance only) ·
`CONJECTURED` · `OPEN` · `REFUTED`. Every REFUTED/dead node carries a one-sentence failure
reason, a disk citation, and a **DEAD** (no repair) / **PARKED** (repairable/deprioritized)
tag. Every PROVED/NUMERICAL node carries its disk citation; where a Fable-only workflow
(strategist proposes, single Opus executor checks) certified it, the caveat
**"(proposer≈checker; independent hostile re-verification owed)"** is attached.

**Most recent change — W-line paper integration independently reviewed (2026-07-18, fresh reviewer; proof statuses unchanged):** **PASS with 0 substantive, 0 trivial, and 0 remaining defects.** The licensed R>=2 filler endpoint, quadratic-range color-coding statement, per-call amplification, Belovs decision/alphabet import, dominated constructed-family-only composition, n^(2/3)-versus-n^(k/(k+1)) open gap, and qualified priority claim all pass. No TeX fix was needed; a fresh pdflatex/bibtex/pdflatex/pdflatex build is clean at 25 pages with zero errors, warnings, or undefined references/citations. L2e, L2f, and L2eC remain PROVED; L2 remains OPEN/PARKED, B2 remains OPEN, and the root remains OPEN. Review: artifacts/ksum_paper_integration2_review.md; ground truth: artifacts/ksum_W_review.md, artifacts/ksum_composition_review.md, artifacts/ksum_W_walkopt_landscape.md.

**Prior change — C-A composition completion review (2026-07-18, fresh hostile reviewer):** L2eC is **PROVED** after completed rule-6 review. Exact quantifiers: fixed `k>=3`, `N=kn`, `2<=R<=n`, every target, and only the explicit moduli `q_k(R)=(P_k(R)+1)(M_k+1)`; the family reaches `Theta_k(N^{k-1})` but has natural density zero. The two-query oracle simulation and all `O_k(1)` conversions are absorbed correctly. The bound is at most `N^{2/3}`, never conflicts with the walk upper bound, and is dominated at every covered point by PROVED Theorem C. The intake's “new/nothing previously known” gloss is rejected as a MAJOR significance defect; the on-disk C-A already avoided it. L2 remains OPEN/PARKED, B2 remains OPEN, and the root remains OPEN. Review: `artifacts/ksum_composition_review.md`; run: `artifacts/logs_ksum_W_20260718/codex_comp_review_run.log`.

**Prior change — W-LB1/W-LB2 independent hostile completion review (2026-07-18, fresh reviewer):** L2e and L2f are **PROVED** after completed rule-6 review. The filler lift is exact for the formal problem domain `R>=2` (the omitted `R=1` endpoint was a MINOR defect); color coding is a worst-case bounded-error reduction after explicit `O_k(1)` amplification (a MINOR exposition repair). New CONJECTURED/pending-review dotted children L2eC/L2fC record the W3E-2 arithmetic: R-A gives `Ω_k(√N q^{1/(6(k−1))})` on the constructed moduli in `q∈[Θ_k(N),Θ_k(N^{k−1})]` but is dominated there by the existing `N^{2/3}` floor, while R-B's `R=Ω(n²)` hypothesis forces `q=Ω_k(N^{2(k−1)})`, so it yields no corollary in that zone. L2, B2, and the root remain OPEN. Review: `artifacts/ksum_W_review.md`; run: `artifacts/logs_ksum_W_20260718/codex_review_run.log`.

**Prior change — W walk-optimality reconnaissance (2026-07-18, executor; review now completed):** The prior “no k≥3 lower bound above √n at any range” claim was corrected by candidate nodes L2e/L2f; L2g records the lifted reversal obstruction. L2e/L2f have now passed independent review as described above; L2g remains CONJECTURED/pending-review. Original report: `artifacts/ksum_W_walkopt_landscape.md`.

**Prior change — paper-integration review complete (2026-07-18, fresh independent reviewer):** **PASS after one MINOR precision defect was corrected; 0 substantive and 0 remaining defects.** The exact theorem quantifiers, complete D1/D2 proof, surrounding claims, unchanged Section 4, and clean 23-page build all passed. Review: `artifacts/ksum_paper_integration_review.md`.

**Prior change — B4 upper bound integrated into the paper (2026-07-18, executor; theorem status unchanged):** The independently reviewed B4a result is now stated as Theorem `thm:k2-upper` with the exact review2 quantifiers, and its complete algorithm, correctness proof, deterministic query cap, two-case recurrence, and epsilon accounting are in Appendix `app:k2-upper`. The abstract, introduction, and k=2 open problem now give the proved `q^{1/6}`-versus-`q^{1/4}` window; the optional reviewed `(N,q)=(5,4)` adversary values record the predicted tau-dependence. B4a remains **PROVED**, B4b remains **OPEN**, hence B4 and the root remain **OPEN**. Paper cite: `research/ksum/paper/ksum_small_alphabet.tex`, labels `thm:k2-upper`, `app:k2-upper`, and `prob:k2-gap`; proof review: `artifacts/ksum_B4_review2.md`.

**Prior change — L33 independent hostile completion review (2026-07-18, fresh Codex reviewer; authored none of the target; no wanted verdict):** L33 remains **NUMERICAL**, now with **independent review completed**. The exact fixed-subspace/commutant reduction and its implementation passed; independent commutant-dimension checks matched on six instances; tightened reduced/unreduced anchors agree within 3.72e-8 and 2.62e-6; the historical mismatches are SCS noise; Stage-0's 56/28 were identified as S_N input-histogram counts, not equality-constraint orbits; and a non-anchor full-cone spot check agrees within 1.31e-6. Two MINOR robustness/provenance defects do not affect the reviewed values. The pending-review marker is removed. Root recomputed and stays **OPEN**. Review: artifacts/ksum_L33_review.md; provenance: artifacts/logs_ksum_L33_20260718/l33r_SHA256SUMS.txt.

**Prior change — B4 round-2 independent completion review (2026-07-18, fresh Codex reviewer; authored none of v1/v2/review1; no wanted verdict):** B4a is **PROVED**. D1 and D2 were independently re-derived with v2's capped estimate `h`, both MINORs and the full standalone recursion/error/query accounting passed, and no new defect was found. The k=2 middle gap is narrowed but remains OPEN: lower `Ω(√N q^{1/6})` versus upper `O_epsilon(N^{1/2+epsilon}q^{1/4})`, so `1/6<1/4` survives. B4 stays **OPEN** because its exponent-matching AND-child is OPEN; the root stays **OPEN**. Review: artifacts/ksum_B4_review2.md; provenance: artifacts/logs_ksum_B4_20260718/codex_review2_run.log.

**Prior change — B4 independent hostile review (2026-07-18, fresh Codex rule-6 reviewer):** B4a remained **CONJECTURED** after completed review. The ABI attribution and single-list/fixed-point repair passed, but the review found 2 MAJOR repairable proof gaps and 2 MINOR defects. Review and repair derivations: artifacts/ksum_B4_review.md; run provenance: artifacts/logs_ksum_B4_20260718/codex_review_run.log. B4 and the root remained **OPEN**.

**Prior change — B4 ABI-algorithm port candidate (2026-07-18, Codex executor; independent review was pending):** ABI's upper-bound proof was extracted from the on-disk source and ported to cyclic 2-Sum. The naive single-list compression has one exact false-positive mechanism — repeated virtual copies of one fixed-point index — repaired by O(sqrt(N)) fixed-point multiplicity detection and exclusion. The recurrence then gives the candidate O_epsilon(N^{1/2+epsilon}q^{1/4}) bound. New leaf B4a is **CONJECTURED — pending-review:**; B4 remains OPEN because review and the q^{1/6}-vs-q^{1/4} gap remain, so the root remains **OPEN**. Cite: artifacts/ksum_B4_upper_note.md:1-201.

**Prior change — L33 reduced Adv± solver (2026-07-18, executor; review was pending):**
L33 was built as a direct isotypic/Wedderburn reduction under S_N×C(σ) and moved
**OPEN → NUMERICAL**. Five requested new points returned values; (5,5,0) and
(6,4,0) hit the explicit 1,200-second cap. The historical Stage-0 SCS anchors
were not all reproduced within their stated 1e-4 tolerance; full residual audits
and MOSEK diagnostics are disclosed in artifacts/ksum_L33_reduced_solver_note.md.
**Independent review completed:** exactness/code audit passed; see artifacts/ksum_L33_review.md.
Root recomputed and stays **OPEN**. Script SHA-256
940de0ceb9472aa5fa47e33b7fd0bfb604fbb020e4245aec3c6ff2d1e0d76111;
logs + manifest: artifacts/logs_ksum_L33_20260718/.

**Most recent change — GAP verify pass (2026-07-18, fresh Codex completing reviewer):** L2d's
rule-6 review cycle is closed: the repaired value-search bound, donor cap, endpoint-qualified iff,
and blocked-sub-zone arithmetic were independently re-derived and the fixed checker rerun. See the
GAP verify ledger entry in §3 and `artifacts/ksum_gap_verification.md`.

**Prior change — GAP-audit pass (2026-07-18, codex gpt-5.6-sol):** see the GAP-audit ledger entry in §3 for the 5 MODERATE + 6 LOW repairs and primary-source dependency pins.

**Most recent change — R3 parity-lemma audit + paper integration (2026-07-18, fresh Opus 4.8
executor-verifier, did NOT author the lemma):** the last single-author caveat on B1's floor — the
odd-`N` parity repair `Lemma lem:core-odd` (the parked-coordinate argument authored in the F1 pass,
which the F1 auditor correctly refused to self-stamp for general `k`) — was **independently audited
and PASSED**. Own from-scratch brute force (oracle enumerates all `C(N,k)` subsets; shares no algebra
with the encoders): the reduction identity `kSum==Claw` at **input level for k=3..8** (incl. **k=7,8,
beyond the F1 k≤6 range**), the "no subset containing the parked coord `v` hits `t`" claim at input
level k=3..8, the proof's `W∈[1,q-1]` interval at **pattern level k=3..10**, full `Z_q` target coverage
via translation (k=3,4), and load-bearing negative controls (a mis-placed `v` and an out-of-window `t`
both leak; the `+1` in `v=t+(k-1)K+1` is **exactly tight**). The proof and the threshold identity
`|W_odd|=q−[(k²−2)K+2k−1]+k` were also re-derived by hand. Verdict **PROVED** (fresh checker ≠ author,
§2 ladder); the parity caveat under A1f is **DISCHARGED**. Cite: `tools/ksum_r3_parity.py`
(SHA `c62bd56c…`), `artifacts/logs_ksum_R3_20260718/parity_audit.log` (SHA `fb515cd2…`),
run-1 audit-trail `parity_audit_run1.log` (SHA `9567e9f2…`). **Paper integration:** `revision_k3.tex`'s
full §4 + Appendix A dropped into `research/ksum/paper/ksum_small_alphabet.tex` (label-compatible; the
old constant-freeze *sketch* §4 replaced by the positive-core proof + full Appendix-A proofs incl.
`lem:core-odd`); §6's donor Open Problem de-duplicated (superseded by `prob:donor`); the F0 walk-cap /
walk-optimality equivalence added to §6 with the Tani k-claw-walk citation (arXiv:0708.2584, pinned
via arXiv → `refs.bib` as `Tani09`); the MTZ `k≥4` crossover propagated (`refs.bib` `MTZ20`,
arXiv:2002.08389); the intro R3-ALIGN reconciled and the technique sentence updated to the core+parked
construction. Full pdflatex+bibtex cycle **clean: 0 errors, 0 undefined refs, 18 pp** (was 12).
`revision_k3.tex` left on disk untouched as the historical drop-in source. Root stays **OPEN** (floor
still `Ω_k(N^{2/3})` at `q=Θ(N)`; the k≥3 donor is still the whole open problem). No PROVED/REFUTED
flips beyond discharging the parity caveat.

**Most recent change — F1 independent hostile audit (2026-07-18, fresh Opus 4.8 auditor, did NOT
author W3E):** the owed independent audit of A1f (W3E-1/W3E-2) was COMMISSIONED, RAN TO COMPLETION,
and **PASSED**; root stays **OPEN** (the floor is still `Ω_k(N^{2/3})` at `q=Θ(N)`, below the tight
`N^{k/(k+1)}` — A1e). Own from-scratch code (oracle enumerates all `C(N,k)` subsets, shares no
algebra with the encoders), own hand re-derivations. **W3E-1 floor:** reduction identity, all-`t`
coverage (gcd argument), and thresholds verified over **47,496** inputs, `k=3,4,5,6` — incl. the
`k=5,6` odd/parity case. **W3E-2 embedding:** encoding identity, the reviewer's no-closing-coefficient
trap (confirmed REAL), and the tight margin verified over **58,033** inputs + pattern cert `k=3..6`;
`max|payload|=P` and `min tag-separation=P+1` attained **EXACTLY**. **Promotions (§2 ladder, fresh
checker ≠ author):** `A1,A1a–A1d,A1f` and `A2,A2a,A2b` lose the single-author caveat → **PROVED**
(reduction proved modulo the inherited on-disk ABI/Tani donor). **Findings (no REFUTE — claim intact):**
(1) W3E-1 AS AUTHORED has a genuine `k≥5` padding gap (extra `C₀`-constant pads self-hit,
`3C₀≡t₀` at k=3,q=24, demonstrated); the delivered **`research/ksum/paper/revision_k3.tex`** (full §4 +
Appendix A, compiles clean) closes it with a single parked-coordinate parity argument, verified
`k=3,4,5,6`. (2) The core window floor `(k−2)(kK+1)` is sufficient but not tight for `k≥4`. Cites:
`tools/ksum_f1_floor.py` (SHA `79a22f3f…`), `.../floor_audit.log` (SHA `bf0c4d17…`);
`tools/ksum_f1_embed.py` (SHA `ca5bdbbc…`), `.../embed_audit.log` (SHA `e92eee2c…`), all under
`artifacts/logs_ksum_F1_20260718/`. This supersedes A1f's prior "IN PROGRESS / interrupted" status.

**F0 donor-cap pass (2026-07-17, Opus 4.8 executor-verifier):** the missing-donor frontier F0 was
attacked from the obstruction side. A fresh targeted literature pass (new axis; NO-DONOR reconfirmed —
Tani-2410.02243 forward-cites still 0, MTZ-2002.08389's 14 forward-cites contain no small-range
k-partite claw detection LB; Iwama–Kawachi is a #intermediate-solutions upper bound, useless at small
range) surfaced the **cap** instead of a donor: Tani's k-claw quantum walk `O(n^{k/(k+1)})`
  (arXiv:0708.2584) is **range-independent**, so at `R=Θ(n)` it forces any donor `Ω(√n·R^c)` to obey
  `c ≤ (k−1)/(2(k+1))` — **exactly the "dream donor" exponent**. New node **L2d** (PROVED constraint,
  dotted under L2, root unchanged) records this; **L2b sharpened**: the dream donor is *maximal* and
  the dream **endpoint bound** is *equivalent at `R=Θ(n)`* to "the k-claw walk is optimal at range =
  domain" (KNOWN k=2, **OPEN k≥3**); the uniform-in-`R` converse is unproved. Also proved: the `k≥4`
  low-`q` sub-zone of the B2 value zone is unreachable even by a maximal donor. Deliverables:
`artifacts/ksum_F0_obstruction_note.md`, `tools/ksum_f0_captable.py` (+ log), evidence file — all
SHA-256'd in `artifacts/logs_ksum_F0_20260718/F0_sha256.txt`. No PROVED/REFUTED status changed; no A1*/A2*
node touched. Root stays **OPEN**.

**Most recent change (2026-07-17):** W3E-1 (the inherited floor) and W3E-2 (the k-collision
encoding) were built and self-verified; the W3 campaign was banked-and-stopped
(`KSUM_W3_CLOSEOUT.md:3`). Two recon corrections are applied here: the frozen-coordinate
reduction is **LIVE/PROVED-BY-REDUCTION**, not "refuted" — the gcd/odd-live obstructions kill
only the *naive* variants, and the reduction was repaired; and the k-collision **encoding is
PROVED**, with the sole OPEN item being the missing donor. One recon "NOT LOCATED" item is now
resolved: git shows the W3 work **is** committed (`ed542e1`, `949240a` atop `8e0f106`), so
`KSUM_W3_CLOSEOUT.md:25` "committed with logs and hashes" is accurate and the W3E header's
"HEAD 8e0f106 (no commits made by this work)" (`ksum_W3E_embedding_lemmas.md:3`) was true only
at write-time and is now stale.

**Third pass (2026-07-18, strategist, post-external-review):** an external hostile review of the
*paper* (`research/ksum/paper/`) returned **major revision**; its k=2/model/barrier mandates are now
**discharged in the working tree** (oracle two-query simulation replacing the false one-query
relabeling claim; claw range freed; threshold corollary made piecewise; orbit proposition rewritten
to the rigorously-provable form; ancillary code packaged) — see PROVER_PROMPT F2, now stale-marked.
The owed independent hostile audit of W3E-1/W3E-2 (A1f) **ran twice and was interrupted** (session
limit, then user stop) with interim confirmations recorded at A1f. Changes in this pass: (1) **L2a
crossover corrected** — "beats the floor only for k≥7" is the BKT-only figure; the survey's own MTZ
citation (`ksum_W3_donor_survey.md:31`, Ω̃(n^{3/4−1/(4k)}) for k≥4) moves the crossover to **k≥4**
(3/4−1/(4k)>2/3 ⟺ k≥4; the stale k≥7 figure sat in `KSUM_W3_CLOSEOUT.md:15,21` — now carrying an
appended Erratum — while the paper's §6 was grep-verified NOT to carry it; see PROVER_PROMPT F4); (2) added **B4** (upper-bound/algorithm branch, was
missing although the GOAL says "find Q(N,k,q)"); (3) added **C0** (proved pruning constraints — WHY
the donor detour is forced); (4) added **L33** (the designed-never-built Wedderburn-reduced solver
under B3); (5) **L32a** evidence extended to n=8 (certified/√n rising 0.775→0.799, drop-falsifier
never fired); (6) k=2 middle-gap pointer added to the header. No PROVED/REFUTED status changed;
L2a stays PARKED with a corrected parking rationale.

**Adversarial-verification pass (2026-07-17, second author):** every node re-checked against
disk. Corrections made this pass: (1) added leaf **L2c** — the Belovs-2026 non-polynomial route,
REFUTED (doesn't transfer: large-alphabet-only + non-range-symmetric), which was obstruction 3 of
the W3 map (`KSUM_W3_CLOSEOUT.md:16`) and was **missing** from the tree; (2) **B2 relabelled an
AND-node** (its own text says "provable only if BOTH A2 and L2") and rendered with an AND bracket,
matching its semantics; (3) removed a phantom `class … PROVED` mermaid line referencing an
undefined class (only `proved` is defined) that could break rendering; (4) added two residual
uncertainties (the `k≥5` padding gap and the `CONJECTURED` W3E-2 family constant). No status was
changed — every PROVED/REFUTED/OPEN label survived re-verification against the cited sources.

---

## 1. The DAG (mermaid)

```mermaid
flowchart TD
  G(["GOAL [OPEN]: reduce alphabet requirement in BS Ω(N^{k/(k+1)}) for fixed k≥3;<br/>find Q(N,k,q) between q=O(1) (Grover √N) and q≥n^k (BS tight)"])

  G --> B1(["OR-1: FROZEN-COORDINATE REDUCTION — Claim a proposition since 2026-07-30 (review §7.4)<br/>route proof MACHINE-CHECKED (composition_via_A1_inputs, C=4, donor-unconditional)<br/>[NUMERICAL · pending-review — statement on the delta-fidelity queue]"])
  G --> B2["OR-2 (AND: encoding A2 proved; needs a WALK-OPTIMAL donor L2):<br/>CONDITIONAL k-COLLISION EMBEDDING<br/>(partial W floors do not discharge consequence; branch OPEN)"]
  G --> B3(["OR-3: DIRECT / INCUMBENT SOLVERS (no reduction; compute Adv± directly)<br/>ALL ROUTES DEAD: G11 + k=2-vs-k≥3 — review-confirmed kills 2026-07-30<br/>[REFUTED · PARKED — revival: an analytic, uniform-in-n Adv± route stated for k≥3]"])
  G -.-> B4["OR-4 (AND internally): UPPER-BOUND / ALGORITHM SIDE — close the k=2 middle gap<br/>(B4a PROVED: upper q^1/4; lower q^1/6, so exponent matching remains) [OPEN]<br/>RELATED, NOT A ROUTE (re-typed 2026-07-30, review §5.4): k=2 ≠ k≥3, no route proof exists"]
  L31 -.-> Rosmanis["Rosmanis barrier (prop:rosmanis): D0 never a single S_N x C(sigma) orbit for q>=3, sigma != id<br/>LATE REGISTRATION via T2 F-T1 finding; count>=2 core kernel-proved orbit-proper (T2, unconditional)<br/>[NUMERICAL - pending node-granular review; bijection + count formula unformalized]"]
  B3 -.-> G11["G11 constraint: no finite exact computation licenses a uniform asymptotic exponent<br/>registered 2026-07-30 per review repair K-B3-1; carries the confirmed B3/goal route kills [CERTIFIED*]"]
  G -.-> C0["CONSTRAINTS (proved; prune ALL branches):<br/>(i) any small-q bound must use group structure — OA-uniform bounds are vacuous;<br/>(ii) k≥3 alphabet symmetry is only diag(Aff)⋊S_n ⇒ k-Sum itself is not multisymmetric<br/>⇒ the DONOR DETOUR of OR-2 is forced, not a choice"]
  B4 --> B4a["B4a: bounded-query ABI port to cyclic 2-Sum after fixed-point preprocessing<br/>O_epsilon(N^{1/2+epsilon}q^{1/4}) [PROVED · independent review2]<br/>2026-07-19 coherent-oracle repair independently reviewed; paper thm:k2-upper + app:k2-upper"]
  B4 --> B4b(["B4b (OR): close the remaining q^{1/6}-vs-q^{1/4} exponent window<br/>Front U conditional outcome + Front L candidate routes; global gap remains [OPEN]"])
  B4b -.-> B4bU1["B4bU1: charged-recurrence certificate F_SC^charge has limiting q exponent 1/4<br/>not an algorithm-family lower bound; q-dependent/promise-aware/shared-query escapes remain<br/>journal integration review completed [CERTIFIED* · CONDITIONAL OUTCOME]"]
  B4b -.-> B4bRetarget["B4bRetarget: milestone relaxed to any eta>1/6<br/>total bridge-loss budget q^(1/12-delta) at q=Theta(N^(2/3)) [CONJECTURED]"]
  B4b -.-> B4bCompcap["B4bCompcap: composition cap — disjoint-block factorized constructions with proved block hardness top out at q^(1/6)<br/>surplus requires cross-block shared-alphabet coupling [CONJECTURED]"]
  B4b --> B4bL1["B4bL1: symmetry-resolved direct adversary family<br/>three-class polar completion stopped at P2 (38.90%--62.83% capture); redesign pending review [OPEN]"]
  B4b --> B4bL2["B4bL2: multisymmetric joint-histogram dual polynomial<br/>phase-6 G1/G2/G3 PROVED; literal transfer BLOCKED/reviewed; aggregate candidate CONJECTURED<br/>journal integration review completed; cap-scale witness open [CONJECTURED]"]
  B4b --> B4bL3["B4bL3: correlated composition beyond disjoint pSearch<br/>single-scale hidden mask is subtarget below crossover; multiscale mask active [OPEN]"]

  %% B4bL2 related component map: non-propagating evidence/tool/obstruction/alternative links.
  subgraph B4bL2Related["B4bL2 related toolkit / obstruction map / open escapes — NON-PROPAGATING"]
    B4bL2M1["M1 pair-tensor annihilation<br/>odd q, N>=q, all t; degree <q-1; l1=1; invariant [PROVED]"]
    B4bL2L2P3["L2P3 tilted log-band witness<br/>degree 2(1+floor(log_5((q-1)/2))); corr >=437/581 [PROVED]"]
    B4bL2BandMult["BANDMULT S_N-averaged convolution<br/>annihilation bands add; Vandermonde; legal normalization [PROVED]"]
    B4bL2M2["M2 five-condition locally balanced sign-separated product obstruction<br/>corr exactly 2^(1-(q-1)/2), q>=5 [PROVED]"]
    B4bL2T4["T4 fixed-allocation unaveraged sign-bit composition<br/>rho<=4/5; product bound; D10 excludes norm-changing average [PROVED]"]
    B4bL2VBud["VBUD whole-pair/value-disjoint budget<br/>m*r0 <= (q-1)/2; no fixed-q N-tracking [PROVED]"]
    B4bL2Orient["ORIENT identical-block/common-total/product-outer class, N=mrs<br/>NO coherence 2^(-r(m-1)); corr <=1/2 [PROVED]"]
    B4bL2G1["G1 multiplicity gauge / terminal-label + GT/JM insufficiency [PROVED]"]
    B4bL2G2["G2 direct nontrivial-satellite-vector Reynolds zero [PROVED]"]
    B4bL2G3["G3 positive diagonal/Reynolds transfer has band zero [PROVED]"]
    B4bL2Filt["FILT falling-factorial query filtration (lem:factorial-filtration)<br/>bridge occupancy rows -> QUERY degree; LATE REGISTRATION via Lean-T3 F-T1<br/>[CERTIFIED* — covered by the archived M1 phase-2 review at its use; Lean gap remains]"]
    B4bL2JointLP["JOINTLP exact finite joint-histogram separation (prop:joint-lp)<br/>script-delegated optima, no printed dual certificates; LATE REGISTRATION F-T1 [CONJECTURED]"]
    B4bL2L2P6G["L2P6-G aggregate transfer obstruction<br/>D14: class undefined and maps nonexhaustive [CONJECTURED]"]
    B4bL2P2Ansatz["P2ANSATZ pure sign-separated tensor<br/>BLOCKED for ansatz at proposer tier; not REFUTED [OPEN / PARKED]"]
    B4bL2AltFewpair["ALT.fewpair few-pair mixture<br/>phase-3 stop rule fired before attempt [OPEN]"]
    B4bL2AltBkt["ALT.bkt active-pair BKT-style outer dual<br/>not attempted; on-disk theorem gap [OPEN]"]
    B4bL2AltNonidentical["ALT.nonidentical unequal-total / nonidentical blocks<br/>outside ORIENT; unexamined [OPEN]"]
    B4bL2AltNonproduct["ALT.nonproduct non-product signed block couplings<br/>unexamined [OPEN]"]
    B4bL2AltCanonbasis["ALT.canonbasis signed map in ambient canonical multiplicity basis<br/>natural center/JM implementation blocked at proposer tier; broader door [OPEN]"]
    B4bL2AltAltinner["ALT.altinner alternative inner kernels<br/>named obligation; unexamined [OPEN]"]
    B4bL2AltTworay["ALT.tworay common-bad-profile two-ray class<br/>explicit log band; O_tau(sqrt(N)) ceiling candidate [CONJECTURED]"]
    B4bL2AltMultipair["ALT.multipair one-defect multi-pair support<br/>C_t=O(N) support ceiling candidate [CONJECTURED]"]
    B4bL2AltMultipairHighCtBalanced["ALT.multipair.highCt-balanced<br/>single-scale M/g=O(N) ceiling candidate [CONJECTURED]"]
    B4bL2AltMultipairMultiscaleSplits["ALT.multipair.multiscale-splits<br/>fixed-scale selector / per-scale OR ceiling candidate [CONJECTURED]"]
    B4bL2AltMultipairVariablePairTotals["ALT.multipair.variable-pair-totals<br/>target-scale finite sweep survives; asymptotic kernel missing [OPEN]"]
    B4bL2AltMultipairGrowingRankMomentDesign["ALT.variable-pair-totals.growing-rank-moment-design<br/>faithful determinant/OA family ceiling candidate [CONJECTURED]"]
    B4bL2AltMultipairSelectiveOrbitTensorKernel["ALT.variable-pair-totals.selective-orbit-tensor-kernel<br/>exact projection normal form; explicit base measure missing [OPEN]"]
    B4bL2AltMultipairMovingRemezCubature["ALT.selective-orbit-tensor-kernel.moving-remez-cubature<br/>moving rank+1 cofactor/equioscillation ansatz [OPEN]"]
    B4bL2AltMultipairMultiscaleGapfreeBaseMeasure["ALT.selective-orbit-tensor-kernel.multiscale-gapfree-base-measure<br/>small-positive-to-high-Ct residual scales [OPEN]"]
    B4bL2AltMultipairLabelAwareFeketeBasisExchange["ALT.moving-remez-cubature.label-aware-fekete-basis-exchange<br/>joint boundary/interior basis selection [OPEN]"]
    B4bL2AltMultipairContinuationSeededBlockFekete["ALT.label-aware-fekete.continuation-seeded-block-fekete<br/>transported coordinated basis exchange [OPEN]"]
    B4bL2AltMultipairCriticalDensePaletteResidualWindow["ALT.multiscale-gapfree.critical-dense-palette-residual-window<br/>0&lt;c&lt;(arcosh 3)/2 full-orbit residual [OPEN]"]
    B4bL2AltMultipairContinuumRemezSupportFlow["ALT.continuation-block-fekete.continuum-limit-remez-support-flow<br/>analytic scaled support flow [OPEN]"]
    B4bL2AltMultipairStratifiedBoundaryJetRemez["ALT.continuum-flow.stratified-boundary-jet-remez<br/>bulk/layer/NO-face/corner system [OPEN]"]
    B4bL2AltMultipairMesoscopicSplitOpeningCascade["ALT.stratified-remez.mesoscopic-split-opening-cascade<br/>corner-to-normal scale ladder [OPEN]"]
    B4bL2AltIteratedMultiscaleBoundaryCompactification["ALT.stratified-remez.iterated-multiscale-compactification<br/>all scales plus stable exactor [OPEN]"]
    B4bL2AltMesoscopicMinorityOccupancyTransition["ALT.stratified-remez.mesoscopic-minority-transition<br/>fixed-m to m=Theta(D) hierarchy [OPEN]"]
    B4bL2AltTangentialPhasePairedTransport["ALT.mesoscopic-minority.tangential-phase-paired-transport<br/>birth edge plus uniform WKB right inverse [OPEN]"]
    B4bL2AltTwoOrientationSharedNoCascade["ALT.split-opening.two-orientation-shared-NO<br/>explicit q=5 endpoint construction [PROVED]"]
    B4bL2AltPhaseSubexposedCorrelationReservoir["ALT.phase-paired.subexposed-correlation-reservoir<br/>correlation off exposed WKB phases [OPEN]"]
    B4bL2AltCorrelationTailDecoupledTwoReservoir["ALT.subexposed.two-reservoir-decoupling<br/>boundary correlation plus neutral high tail [OPEN]"]
    B4bL2AltMultiscaleMomentBearingNeutralLadder["ALT.two-reservoir.multiscale-neutral-ladder<br/>local moment transport across Ct scales [OPEN]"]
    B4bL2AltNearZeroBridgeIndependentParityTail["ALT.multiscale-neutral.near-zero-bridge-plus-parity-tail<br/>explicit pi projection has corr o(1) [OPEN]"]
    B4bL2AltWeightedActivationOrDualComposition["ALT.weighted-activation-OR-dual<br/>dense scalar separator [REFUTED]"]
    B4bL2AltBalancedPositiveSplitWeightedDualComposition["ALT.balanced-positive-split dual<br/>exact support scalar-separated [REFUTED]"]
    B4bL2AltNonproductProfileLatticeCore["ALT.nonproduct.profile-lattice-core<br/>rule-7 reviewed: C1 q-independence + C2 M2-exact decay + C4 germ containment PROVED-scoped (C3 crossing stays NUMERICAL); live region &ge;3 active pairs non-product [OPEN · reviewed sub-results]"]
  end
  B4bL2 -.-> B4bL2M1
  B4bL2 -.-> B4bL2L2P3
  B4bL2 -.-> B4bL2BandMult
  B4bL2 -.-> B4bL2M2
  B4bL2 -.-> B4bL2T4
  B4bL2 -.-> B4bL2VBud
  B4bL2 -.-> B4bL2Orient
  B4bL2 -.-> B4bL2G1
  B4bL2 -.-> B4bL2G2
  B4bL2 -.-> B4bL2G3
  B4bL2 -.-> B4bL2L2P6G
  B4bL2 -.-> B4bL2P2Ansatz
  B4bL2 -.-> B4bL2AltFewpair
  B4bL2 -.-> B4bL2AltBkt
  B4bL2 -.-> B4bL2AltNonidentical
  B4bL2 -.-> B4bL2AltNonproduct
  B4bL2 -.-> B4bL2AltCanonbasis
  B4bL2 -.-> B4bL2AltAltinner
  B4bL2 -.-> B4bL2AltTworay
  B4bL2 -.-> B4bL2AltMultipair
  B4bL2 -.-> B4bL2AltMultipairHighCtBalanced
  B4bL2AltMultipair -.-> B4bL2AltMultipairHighCtBalanced
  B4bL2 -.-> B4bL2AltMultipairMultiscaleSplits
  B4bL2AltMultipairHighCtBalanced -.-> B4bL2AltMultipairMultiscaleSplits
  B4bL2 -.-> B4bL2AltMultipairVariablePairTotals
  B4bL2AltMultipairMultiscaleSplits -.-> B4bL2AltMultipairVariablePairTotals
  B4bL2 -.-> B4bL2AltMultipairGrowingRankMomentDesign
  B4bL2AltMultipairVariablePairTotals -.-> B4bL2AltMultipairGrowingRankMomentDesign
  B4bL2 -.-> B4bL2AltMultipairSelectiveOrbitTensorKernel
  B4bL2AltMultipairVariablePairTotals -.-> B4bL2AltMultipairSelectiveOrbitTensorKernel
  B4bL2AltMultipairGrowingRankMomentDesign -.-> B4bL2AltMultipairSelectiveOrbitTensorKernel
  B4bL2 -.-> B4bL2AltMultipairMovingRemezCubature
  B4bL2AltMultipairSelectiveOrbitTensorKernel -.-> B4bL2AltMultipairMovingRemezCubature
  B4bL2 -.-> B4bL2AltMultipairMultiscaleGapfreeBaseMeasure
  B4bL2AltMultipairSelectiveOrbitTensorKernel -.-> B4bL2AltMultipairMultiscaleGapfreeBaseMeasure
  B4bL2 -.-> B4bL2AltMultipairLabelAwareFeketeBasisExchange
  B4bL2AltMultipairMovingRemezCubature -.-> B4bL2AltMultipairLabelAwareFeketeBasisExchange
  B4bL2 -.-> B4bL2AltMultipairContinuationSeededBlockFekete
  B4bL2AltMultipairLabelAwareFeketeBasisExchange -.-> B4bL2AltMultipairContinuationSeededBlockFekete
  B4bL2 -.-> B4bL2AltMultipairCriticalDensePaletteResidualWindow
  B4bL2AltMultipairMultiscaleGapfreeBaseMeasure -.-> B4bL2AltMultipairCriticalDensePaletteResidualWindow
  B4bL2 -.-> B4bL2AltMultipairContinuumRemezSupportFlow
  B4bL2AltMultipairContinuationSeededBlockFekete -.-> B4bL2AltMultipairContinuumRemezSupportFlow
  B4bL2 -.-> B4bL2AltMultipairStratifiedBoundaryJetRemez
  B4bL2AltMultipairContinuumRemezSupportFlow -.-> B4bL2AltMultipairStratifiedBoundaryJetRemez
  B4bL2 -.-> B4bL2AltMultipairMesoscopicSplitOpeningCascade
  B4bL2AltMultipairStratifiedBoundaryJetRemez -.-> B4bL2AltMultipairMesoscopicSplitOpeningCascade
  B4bL2 -.-> B4bL2AltIteratedMultiscaleBoundaryCompactification
  B4bL2AltMultipairStratifiedBoundaryJetRemez -.-> B4bL2AltIteratedMultiscaleBoundaryCompactification
  B4bL2 -.-> B4bL2AltMesoscopicMinorityOccupancyTransition
  B4bL2AltMultipairStratifiedBoundaryJetRemez -.-> B4bL2AltMesoscopicMinorityOccupancyTransition
  B4bL2 -.-> B4bL2AltTangentialPhasePairedTransport
  B4bL2AltMesoscopicMinorityOccupancyTransition -.-> B4bL2AltTangentialPhasePairedTransport
  B4bL2 -.-> B4bL2AltTwoOrientationSharedNoCascade
  B4bL2AltMultipairMesoscopicSplitOpeningCascade -.-> B4bL2AltTwoOrientationSharedNoCascade
  B4bL2 -.-> B4bL2AltPhaseSubexposedCorrelationReservoir
  B4bL2AltTangentialPhasePairedTransport -.-> B4bL2AltPhaseSubexposedCorrelationReservoir
  B4bL2 -.-> B4bL2AltCorrelationTailDecoupledTwoReservoir
  B4bL2AltPhaseSubexposedCorrelationReservoir -.-> B4bL2AltCorrelationTailDecoupledTwoReservoir
  B4bL2 -.-> B4bL2AltMultiscaleMomentBearingNeutralLadder
  B4bL2AltCorrelationTailDecoupledTwoReservoir -.-> B4bL2AltMultiscaleMomentBearingNeutralLadder
  B4bL2 -.-> B4bL2AltNearZeroBridgeIndependentParityTail
  B4bL2AltMultiscaleMomentBearingNeutralLadder -.-> B4bL2AltNearZeroBridgeIndependentParityTail
  B4bL2AltNearZeroBridgeIndependentParityTail -.-> B4bL2AltWeightedActivationOrDualComposition
  B4bL2AltWeightedActivationOrDualComposition -.-> B4bL2AltBalancedPositiveSplitWeightedDualComposition
  B4bL2 -.-> B4bL2AltNonproductProfileLatticeCore
  B4bL2AltNonproduct -.-> B4bL2AltNonproductProfileLatticeCore
  B4bL2AltTwoOrientationSharedNoCascade -.-> B4bL2AltNonproductProfileLatticeCore

  %% B4bL3 related candidate map: non-propagating Rule-8 visibility nodes.
  subgraph B4bL3Related["B4bL3 correlated-composition candidates — NON-PROPAGATING"]
    B4bL3AltHiddenFrequencyMask["ALT.hidden-frequency-mask<br/>exact single-scale promise; subcritical upper kill, endpoint open [OPEN]"]
    B4bL3AltHiddenFrequencyMaskCriticalEndpoint["ALT.hidden-frequency-mask.critical-endpoint<br/>exact N^(11/18) baseline; N^(2/3) matrix open [OPEN]"]
    B4bL3AltCriticalDuplicateClassification["critical ALT.duplicate-classification<br/>scoped best N^(5/6) [OPEN]"]
    B4bL3AltCriticalFrequencyAwareJointWalk["critical ALT.frequency-aware-joint-walk<br/>soft-filter min Johnson N^(2/3) [OPEN]"]
    B4bL3AltCriticalJointStatisticEstimation["critical ALT.joint-statistic-estimation<br/>scoped best N^(5/6) [OPEN]"]
    B4bL3AltCriticalOrbitIntertwinerAdversary["critical ALT.orbit-intertwiner-adversary<br/>standalone ceiling; coupled open [OPEN]"]
    B4bL3AltCriticalSignedCycleWeightLaw["critical ALT.signed-cycle-weight-law<br/>standalone square constant ceiling [REFUTED]"]
    B4bL3AltCriticalCoupledUicAddressCycleKernel["critical ALT.coupled-uic-address-cycle<br/>input-wise/two-matching laws fail; three-layer open [OPEN]"]
    B4bL3AltCriticalCoupledGrowingSelectorSpechtBranchingKernel["coupled ALT.growing-selector-Specht<br/>fixed-middle and natural word laws fail [OPEN]"]
    B4bL3AltCriticalCoupledLrMultiplicitySpaceMixing["growing-selector ALT.LR-multiplicity<br/>c=r+1 exists; fixed mixer fails [OPEN]"]
    B4bL3AltCriticalCoupledNonfactorizableCycleWordSelector["growing-selector ALT.cycle-word<br/>natural two-matching algebra fails [OPEN]"]
    B4bL3AltCriticalCoupledFullPositionIncidenceThreeLayerWordKernel["cycle-word ALT.full-position-three-layer<br/>transportation orbits typed; fixed minors fail [OPEN]"]
    B4bL3AltCriticalNoncommutingParentMixingKernel["full-position ALT.noncommuting-parent-mixing<br/>two grids and small Pieri patches fail [OPEN]"]
    B4bL3AltCriticalSharedBranchYoungLatticePatchKernel["parent-mixing ALT.shared-branch Young patch<br/>o(m) Pieri obstruction reviewed [OPEN]"]
    B4bL3AltCriticalSameParentOccurrenceMultiplicityMixingKernel["parent-mixing ALT.same-parent multiplicity<br/>growing space exists; trivial alphabet fails [OPEN]"]
    B4bL3AltCriticalMacroscopicParentPatchKernel["parent-patch ALT.macroscopic support<br/>adjacent two-row chain fails; broader open [OPEN]"]
    B4bL3AltCriticalNonSkeletonHeavyOccurrenceCarrier["parent-patch ALT.non-skeleton occurrence<br/>sign/rectangle fails; broader open [OPEN]"]
    B4bL3AltCriticalFullYoungRankBalancedHarmonicKernel["macroscopic ALT.full Young-rank harmonic<br/>trivial alphabet reviewed no-go; broader open [OPEN]"]
    B4bL3AltCriticalNonScaledPlethysticManyCornerOccurrenceKernel["non-skeleton ALT.non-scaled plethysm<br/>three-row multiplicity; trivial frame fails [OPEN]"]
    B4bL3AltCriticalGloballyBoundedSymmetrizedPolynomialLowerBound["critical ALT.globally bounded polynomial<br/>off-promise interpolation untested [OPEN]"]
    B4bL3AltCriticalThreeRowBlockStandardCovariantOccurrenceKernel["non-scaled ALT.three-row block-standard<br/>single-cell no-go reviewed PARTIAL [OPEN]"]
    B4bL3AltCriticalThreeRowBicovariantTwoCellAlphabetKernel["three-row ALT.two-cell tensor alphabet<br/>single irrep retains one half [REFUTED]"]
    B4bL3AltCriticalThreeRowMixedTwoBoxFullTypeRecouplingKernel["three-row ALT.mixed two-box full types<br/>exact two-type mass 1/a [REFUTED · DEAD]"]
    B4bL3AltCriticalThreeRowInducedBicovariantAlphabetPacketKernel["three-row ALT.induced alphabet packet<br/>first gate reviewed; joint query law open [OPEN]"]
    B4bL3AltCriticalInducedPacketYoungHolonomyLaw["induced packet ALT.Young holonomy<br/>matrix connection untested [OPEN]"]
    B4bL3AltCriticalInducedPacketJointParentContentKernel["induced packet ALT.joint parent content<br/>finite factors banked; assembly open [OPEN]"]
    B4bL3AltCriticalInducedPacketOccurrencePencilClassification["induced packet GATE.occurrence pencils<br/>finite M1+M3/C6; Pieri assembly open [OPEN]"]
    B4bL3AltCriticalInducedPacketTotalEnergyResolventLaw["induced packet ALT.total-energy resolvent<br/>scalar-collapse risk [OPEN · DEPRIORITIZED]"]
    B4bL3AltCriticalInducedPacketNoncommutingSylvesterLaw["induced packet ALT.matrix Sylvester<br/>native cross-side premise false [REFUTED · DEAD]"]
    B4bL3AltCriticalInducedPacketRectangularTransferResolventLaw["induced packet ALT.rectangular transfer<br/>commuting pair; factor assembly open [OPEN]"]
    B4bL3AltCriticalLiteralMarkedQueryPolarNormInterface["rectangular GATE.literal query/polar norm<br/>three candidate laws registered [OPEN]"]
    B4bL3AltCriticalPolarOffdiagonalBlockLaw["literal-query ALT.off-diagonal polar blocks<br/>priority direct-norm law [OPEN]"]
    B4bL3AltCriticalPhysicalRangeReducingEqualityLaw["literal-query ALT.range-reducing equality<br/>packet-specific conditional repair [OPEN]"]
    B4bL3AltCriticalHsQueryEnergyLaw["literal-query ALT.HS energy<br/>Schur carrier floor L>=sqrt(f^lambda f^mu)=Omega(q^(3/4)) vs budget q^(1/12); sign-rep escape closed; scoped to HS-only route [REFUTED · DEAD · rule-7 confirmed]"]
    B4bL3AltCriticalInducedPacketOuterIncidenceNumeratorInterface["rectangular GATE.outer numerator<br/>typed incidence map absent [OPEN]"]
    B4bL3AltCriticalInducedPacketPlaquetteFlowLaw["induced packet ALT.plaquette flow<br/>divergence-free law untested [OPEN]"]
    B4bL3AltCriticalNontrivialAlphabetOccurrenceMixingKernel["same-parent ALT.nontrivial alphabet<br/>minimal type-cell product fails [OPEN]"]
    B4bL3AltCriticalCovariantBlockStandardOccurrenceMixingKernel["nontrivial-alphabet ALT.covariant Std_a<br/>single-cell opposite side retained [OPEN]"]
    B4bL3AltCriticalTwoCellCovariantCrossSectorMixingKernel["covariant ALT.two-cell cross-sector<br/>constant retained branch [REFUTED]"]
    B4bL3AltCriticalCoupledDelocalizedMultiblockOccurrenceKernel["coupled ALT.delocalized-multiblock<br/>selector-star/PQ fails; non-PQ overlap open [OPEN]"]
    B4bL3AltCriticalStrictInjectionRecordingQuery["critical ALT.strict-injection-recording-query<br/>full-low-degree projector [REFUTED]"]
    B4bL3AltCriticalPromiseIdealQuotientAdversary["critical ALT.promise-ideal-quotient<br/>exact module Hom zero; nonintertwining adversary open [OPEN]"]
    B4bL3AltCriticalReachabilitySensitiveRecordingFiltration["critical ALT.reachable-recording<br/>universal linear span full [REFUTED]"]
    B4bL3AltCriticalNonlinearAlgorithmDependentRecordingCarrier["reachable ALT.nonlinear-carrier<br/>algorithm-dependent invariant untested [OPEN]"]
    B4bL3AltCriticalCorePsearchLift["ALT.critical-core-psearch-lift<br/>all conditional interfaces pass; donor open [OPEN]"]
    B4bL3AltMultiscaleFrequencyMask["ALT.multiscale-frequency-mask<br/>critical shelf passes sampling + enumeration gates [OPEN]"]
    B4bL3AltBicliqueCoverGraphClaw["ALT.biclique-cover-graph-claw<br/>r=q^(3/2) relation donor; no noncircular LB [OPEN]"]
    B4bL3AltCriticalInducedPacketPayloadValueTest["induced packet GATE.payload value test<br/>NOT ASSEMBLABLE at a=16,q=64: 7 missing pieces incl. both interfaces and coefficient law; scalar collapses to N^(11/18) baseline [NUMERICAL · pending-review]"]
  end
  B4bL3 -.-> B4bL3AltHiddenFrequencyMask
  B4bL3 -.-> B4bL3AltHiddenFrequencyMaskCriticalEndpoint
  B4bL3AltHiddenFrequencyMaskCriticalEndpoint -.-> B4bL3AltCriticalDuplicateClassification
  B4bL3AltHiddenFrequencyMaskCriticalEndpoint -.-> B4bL3AltCriticalFrequencyAwareJointWalk
  B4bL3AltHiddenFrequencyMaskCriticalEndpoint -.-> B4bL3AltCriticalJointStatisticEstimation
  B4bL3AltHiddenFrequencyMaskCriticalEndpoint -.-> B4bL3AltCriticalOrbitIntertwinerAdversary
  B4bL3AltCriticalOrbitIntertwinerAdversary -.-> B4bL3AltCriticalSignedCycleWeightLaw
  B4bL3AltCriticalOrbitIntertwinerAdversary -.-> B4bL3AltCriticalCoupledUicAddressCycleKernel
  B4bL3AltCriticalCoupledUicAddressCycleKernel -.-> B4bL3AltCriticalCoupledGrowingSelectorSpechtBranchingKernel
  B4bL3AltCriticalCoupledGrowingSelectorSpechtBranchingKernel -.-> B4bL3AltCriticalCoupledLrMultiplicitySpaceMixing
  B4bL3AltCriticalCoupledGrowingSelectorSpechtBranchingKernel -.-> B4bL3AltCriticalCoupledNonfactorizableCycleWordSelector
  B4bL3AltCriticalCoupledNonfactorizableCycleWordSelector -.-> B4bL3AltCriticalCoupledFullPositionIncidenceThreeLayerWordKernel
  B4bL3AltCriticalCoupledFullPositionIncidenceThreeLayerWordKernel -.-> B4bL3AltCriticalNoncommutingParentMixingKernel
  B4bL3AltCriticalNoncommutingParentMixingKernel -.-> B4bL3AltCriticalSharedBranchYoungLatticePatchKernel
  B4bL3AltCriticalNoncommutingParentMixingKernel -.-> B4bL3AltCriticalSameParentOccurrenceMultiplicityMixingKernel
  B4bL3AltCriticalSharedBranchYoungLatticePatchKernel -.-> B4bL3AltCriticalMacroscopicParentPatchKernel
  B4bL3AltCriticalSharedBranchYoungLatticePatchKernel -.-> B4bL3AltCriticalNonSkeletonHeavyOccurrenceCarrier
  B4bL3AltCriticalMacroscopicParentPatchKernel -.-> B4bL3AltCriticalFullYoungRankBalancedHarmonicKernel
  B4bL3AltCriticalNonSkeletonHeavyOccurrenceCarrier -.-> B4bL3AltCriticalFullYoungRankBalancedHarmonicKernel
  B4bL3AltCriticalNonSkeletonHeavyOccurrenceCarrier -.-> B4bL3AltCriticalNonScaledPlethysticManyCornerOccurrenceKernel
  B4bL3AltCriticalFullYoungRankBalancedHarmonicKernel -.-> B4bL3AltCriticalNonScaledPlethysticManyCornerOccurrenceKernel
  B4bL3AltHiddenFrequencyMaskCriticalEndpoint -.-> B4bL3AltCriticalGloballyBoundedSymmetrizedPolynomialLowerBound
  B4bL3AltCriticalNonScaledPlethysticManyCornerOccurrenceKernel -.-> B4bL3AltCriticalThreeRowBlockStandardCovariantOccurrenceKernel
  B4bL3AltCriticalCovariantBlockStandardOccurrenceMixingKernel -.-> B4bL3AltCriticalThreeRowBlockStandardCovariantOccurrenceKernel
  B4bL3AltCriticalThreeRowBlockStandardCovariantOccurrenceKernel -.-> B4bL3AltCriticalThreeRowBicovariantTwoCellAlphabetKernel
  B4bL3AltCriticalTwoCellCovariantCrossSectorMixingKernel -.-> B4bL3AltCriticalThreeRowBicovariantTwoCellAlphabetKernel
  B4bL3AltCriticalThreeRowBicovariantTwoCellAlphabetKernel -.-> B4bL3AltCriticalThreeRowMixedTwoBoxFullTypeRecouplingKernel
  B4bL3AltCriticalThreeRowMixedTwoBoxFullTypeRecouplingKernel -.-> B4bL3AltCriticalThreeRowInducedBicovariantAlphabetPacketKernel
  B4bL3AltCriticalThreeRowInducedBicovariantAlphabetPacketKernel -.-> B4bL3AltCriticalInducedPacketYoungHolonomyLaw
  B4bL3AltCriticalThreeRowInducedBicovariantAlphabetPacketKernel -.-> B4bL3AltCriticalInducedPacketJointParentContentKernel
  B4bL3AltCriticalInducedPacketJointParentContentKernel -.-> B4bL3AltCriticalInducedPacketOccurrencePencilClassification
  B4bL3AltCriticalInducedPacketOccurrencePencilClassification -.-> B4bL3AltCriticalInducedPacketTotalEnergyResolventLaw
  B4bL3AltCriticalInducedPacketOccurrencePencilClassification -.-> B4bL3AltCriticalInducedPacketNoncommutingSylvesterLaw
  B4bL3AltCriticalInducedPacketOccurrencePencilClassification -.-> B4bL3AltCriticalInducedPacketRectangularTransferResolventLaw
  B4bL3AltCriticalInducedPacketRectangularTransferResolventLaw -.-> B4bL3AltCriticalLiteralMarkedQueryPolarNormInterface
  B4bL3AltCriticalInducedPacketRectangularTransferResolventLaw -.-> B4bL3AltCriticalInducedPacketOuterIncidenceNumeratorInterface
  B4bL3AltCriticalLiteralMarkedQueryPolarNormInterface -.-> B4bL3AltCriticalPolarOffdiagonalBlockLaw
  B4bL3AltCriticalLiteralMarkedQueryPolarNormInterface -.-> B4bL3AltCriticalPhysicalRangeReducingEqualityLaw
  B4bL3AltCriticalLiteralMarkedQueryPolarNormInterface -.-> B4bL3AltCriticalHsQueryEnergyLaw
  B4bL3AltCriticalThreeRowInducedBicovariantAlphabetPacketKernel -.-> B4bL3AltCriticalInducedPacketPlaquetteFlowLaw
  B4bL3AltCriticalThreeRowInducedBicovariantAlphabetPacketKernel -.-> B4bL3AltCriticalInducedPacketPayloadValueTest
  B4bL3AltCriticalInducedPacketOuterIncidenceNumeratorInterface -.-> B4bL3AltCriticalInducedPacketPayloadValueTest
  B4bL3AltCriticalSameParentOccurrenceMultiplicityMixingKernel -.-> B4bL3AltCriticalNontrivialAlphabetOccurrenceMixingKernel
  B4bL3AltCriticalNontrivialAlphabetOccurrenceMixingKernel -.-> B4bL3AltCriticalCovariantBlockStandardOccurrenceMixingKernel
  B4bL3AltCriticalCovariantBlockStandardOccurrenceMixingKernel -.-> B4bL3AltCriticalTwoCellCovariantCrossSectorMixingKernel
  B4bL3AltCriticalCoupledUicAddressCycleKernel -.-> B4bL3AltCriticalCoupledDelocalizedMultiblockOccurrenceKernel
  B4bL3AltHiddenFrequencyMaskCriticalEndpoint -.-> B4bL3AltCriticalStrictInjectionRecordingQuery
  B4bL3AltCriticalStrictInjectionRecordingQuery -.-> B4bL3AltCriticalPromiseIdealQuotientAdversary
  B4bL3AltCriticalStrictInjectionRecordingQuery -.-> B4bL3AltCriticalReachabilitySensitiveRecordingFiltration
  B4bL3AltCriticalReachabilitySensitiveRecordingFiltration -.-> B4bL3AltCriticalNonlinearAlgorithmDependentRecordingCarrier
  B4bL3 -.-> B4bL3AltCriticalCorePsearchLift
  B4bL3 -.-> B4bL3AltMultiscaleFrequencyMask
  B4bL3 -.-> B4bL3AltBicliqueCoverGraphClaw

  %% Branch 1
  B1 --> L11["naive UNIFORM shift of k−2 frozen coords<br/>[REFUTED · DEAD]"]
  B1 --> L12["odd-live-coordinate variant<br/>[REFUTED · DEAD]"]
  B1 --> A1["Lemma W3E-1 = Theorem C (AND) — the REPAIRED reduction<br/>[PROVED — composition CONFIRMED-WITH-REPAIRS by the 2026-07-30 review (§3.1); R-A1-1/R-A1-3<br/>discharged by the repair batch, machine-checked; KSUM.A1.holds closes the Claim rel interface]"]
  A1 --> A1a["freeze a core of k−2 coords: CONSTANT C₀=⌊q/(k−1)⌋ (as authored) OR positive CORE summing to the target<br/>(kills all d≥1 bad patterns), PLUS the parked coordinate v=t+(k−1)K+1 when N−(k−2) is odd;<br/>valid at EVERY window target t ∈ [t₀, t₀+k), t₀=(k−2)(kK+1) [PROVED — widened 2026-07-30 per R-A1-1/R-A1-3]"]
  A1 --> A1b["EVEN 2n-coord k=2 claw encoding on live part<br/>(no unpaired live coord) [PROVED]"]
  A1 --> A1c["target coverage, COSET-COVERING form: window family + translation identity<br/>k-Sum_t(x)=k-Sum_{t+ka}(x+a·1); every t has a window target t′ ∈ t+kZ_q with Q(kSum_t) ≥ Q(kSum_t′)/C,<br/>no parity and no coprimality cond. [PROVED — restated 2026-07-30 per R-A1-3; all-pairs form refuted]"]
  A1 --> A1d["RESULT: for fixed k≥3, q0(k)=2k²+2k−5≤q≤C_kN implies<br/>Q(k-Sum,Z_q,t,N)=Ω_k(√N·q^{1/6}); q≥c_kN gives Ω_k(N^{2/3})<br/>[PROVED-BY-REDUCTION; statement correction independently reviewed 2026-07-19; status unchanged]"]
  A1 -.-> A1e["CAVEAT floor≠target: at q=Θ(N) reads Ω_k(N^{2/3}) < N^{k/(k+1)}<br/>[PROVED outcome (review §4.2): corollary of PROVED A1d + arithmetic; re-typed related 2026-07-30;<br/>superseded as load-bearing by the K-B1-1 ceiling citation on the B1→GOAL kill]"]
  A1 -.-> A1f["certification: independent hostile audit (fresh Opus, own code) COMPLETED &amp; PASSED 2026-07-18;<br/>trap confirmed real, closing-coeff re-derivations passed, payload bound P and margin P+1 attained exactly;<br/>odd-N parity repair (lem:core-odd) INDEPENDENTLY RE-AUDITED by R3 (k=3..8 input incl. k=7,8; k=3..10 pattern; +1 margin tight) — last single-author caveat DISCHARGED;<br/>single-author star REMOVED. Donor (ABI/Tani) still on trust, as in k=2. [DONE · PROVED]"]

  %% Branch 2
  B2 --> A2["Lemma W3E-2 (AND): exact query-free reduction<br/>k-partite k-collision → k-Sum, q=Θ_k(R^{k−1})<br/>[PROVED — composition CONFIRMED-WITH-REPAIRS by the 2026-07-30 review (§3.2), repairs applied;<br/>gcd(k,q)=1 ruled a THEOREM of the construction (coprime_k_q), not a hypothesis]"]
  A2 --> A2a["complete payload/tag formulas u_j=ω^{j−1}, u_k=−(ω^{k−1}−1)/(ω−1),<br/>w_j=V·(2k+1)^{j−1}; modulus q=(P+1)(M+1) [PROVED]<br/>2026-07-19 gcd(k,q)=1 all-target repair independently reviewed"]
  A2 --> A2b["all wrong block-multisets excluded (balanced base-ω)<br/>+ 62,140 exhaustive checks [PROVED + NUMERICAL]"]
  B2 --> L2["k-Sum CONSEQUENCE: needs a WALK-OPTIMAL small-range k≥3 k-collision<br/>detection LB — no tight donor found; partial floors L2e/f do not suffice [OPEN · PARKED]"]
  L2 --> L2a["SUB-OR: manufacture donor via k-fold Zhang + Tani transfer<br/>→ plateau n^{3/4−1/(2k)} (BKT) resp. n^{3/4−1/(4k)} (MTZ theorem: fixed k≥2) — always < target;<br/>beats the OR-1 floor for k≥4 under MTZ (k≥7 under BKT alone) [PARKED]"]
  L2 --> L2b["SUB-OR: dream ENDPOINT bound c=(k−1)/(2(k+1)) at R=Θ(n) ⇔ k-claw walk OPTIMAL there<br/>(KNOWN k=2 via ABI; OPEN k≥3; uniform-in-R converse UNPROVED); sits EXACTLY on PROVED cap L2d<br/>→ target only at endpoint q=Θ(N^{k−1}), never at small q=Θ(N) [PARKED]"]
  L2 --> L2c["SUB-OR: transfer Belovs-2026 tight NON-polynomial k-distinctness<br/>framework directly — large-alphabet-only (q≥Ω(n²)), non-range-symmetric;<br/>neither Ambainis nor Tani transfer carries it [REFUTED · DEAD]"]
  L2 -.-> L2d["DONOR-CAP [PROVED · INDEPENDENTLY REVIEWED 2026-07-18 · prunes L2a–c]: value-search Õ(√Rn)<br/>+ Tani walk O(n^{k/(k+1)}) [PROVED-IN-LIT, range-independent] ⇒ c≤min{1/2,(k−1)/(2θ(k+1))};<br/>at R=Θ(n), dream ENDPOINT bound ⇔ walk optimality; uniform-in-R converse UNPROVED;<br/>k≥4 low-q sub-zone 1≤E&lt;(k−1)²/(k+1) BLOCKED; relative length k(k−3)/((k+1)(k−2)).<br/>Review: ksum_final_gap_audit.md → ksum_gap_fixes_applied.md → ksum_gap_verification.md + captable_verify.log"]
  L2 -.-> L2e["W-LB1 PARTIAL FLOOR (R≥2): hard 2-claw + fixed surjective filler lists<br/>⇒ Ω(√n·min{R,n}^{1/6}), hence Ω(n^{2/3}) for R≥n<br/>[PROVED · independent review; INTEGRATED INTO PAPER as prop:kclaw-fillers; does not discharge L2]"]
  L2e -.-> L2eC["W3E-2 COMPOSITION: for N=kn, 2≤R≤n, exact q=q_k(R), every t,<br/>Ω_k(√N·q^{1/(6(k−1))}); density-zero family, dominated throughout by W3E-1<br/>[PROVED · independent review; INTEGRATED INTO PAPER as dominated rem:kclaw-composition]"]
  L2 -.-> L2f["W-LB2 PARTIAL FLOOR: amplified random color coding k-distinctness → k-partite k-claw<br/>+ Belovs-2026 ⇒ Ω(n^{3/4−1/(4(2^k−1))}) at R=Ω(n²)<br/>[PROVED · independent review; INTEGRATED INTO PAPER as prop:kclaw-coloring; does not discharge L2]"]
  L2f -.-> L2fC["W3E-2 RANGE OBSTRUCTION: R=Ω(n²) forces q=Ω_k(N^{2(k−1)}), above N^{k−1};<br/>no composition corollary in requested zone, and BS is stronger there [CONJECTURED · pending-review OUTCOME]"]
  L2 -.-> L2g["W-BS-REV: lifted k-sum → k-claw relation works with domain blow-up N=Θ(m^{k−1})<br/>⇒ only Ω(N^{k/(k²−1)}) &lt; √N for k≥3<br/>[CONJECTURED · pending-review; obstruction outcome, not an OR proof route]"]

  %% Branch 3
  B3 --> L31["incumbent ksum_probe.py regular-rep 'reduction'<br/>inflates PSD block 6–29×, zero numbers ever [REFUTED · DEAD]"]
  B3 --> L32["fresh unreduced direct Adv± solver: k=2 values only<br/>(3,3)=2.4186 (4,3)=2.7127; k≥3 not reached [NUMERICAL/WORKS]"]
  L32 -.-> L32a["exponent numerically UNDECIDABLE at reachable n<br/>(pilot band 1.49–1.93; extension to n=8 at q=3: certified/√n rises 0.775→0.799,<br/>drop-falsifier never fired — still G11-non-discriminating) [OPEN]"]
  B3 --> L33["Wedderburn/isotypic-reduced Adv± solver under S_n×C(σ)<br/>BUILT for cyclic k=2: 5/7 requested new points returned; (5,5)/(6,4) capped at 1200 s<br/>exact reduction/code audit PASS; values verified numerically [NUMERICAL · REVIEW COMPLETE]"]

  %% Lean audit (2026-07-30 lead directive) — non-propagating to G; audits existing theorems,
  %% can only DEMOTE them. Produces no new bound.
  G -.-> Lean["Lean: machine-checked audit (Lean 4 + Mathlib v4.31.0), AND of four children<br/>2026-08-01: ALL-STARRED — composition (census DF-9-verified, C-1..C-4 applied) + T1/T2/T3/Fid all CERTIFIED*<br/>[CERTIFIED* — single-review caveat class; interface facts (i)-(iv) now ALL stated in paper v5.2]"]
  Lean --> LeanT1["LeanT1: k=2 lower-bound main line, 7/7 targets, explicit constants<br/>29/29 axiom-clean; findings F1-F7 — F1/F2 (freeze, constQ) were unstated when found and are<br/>STATED as facts (iii)/(iv) since paper v5.2<br/>[CERTIFIED* — fidelity PASS-WITH-CAVEATS 2026-07-31; conditional on ABI/Tani + facts (i)-(iv), all stated]"]
  Lean --> LeanT2["LeanT2: k-floor cores + Rosmanis barrier, UNCONDITIONAL (no QueryModel)<br/>A1a proved at every window target; A1c all-pairs form refuted, coset-covering proved;<br/>rosmanis(1) count>=2 orbit-proper [CERTIFIED* — fidelity PASS-WITH-CAVEATS 2026-07-31]"]
  Lean --> LeanT3["LeanT3: obstruction group, UNCONDITIONAL; ADOPT 44/0/0 + 14 added, axiom-clean<br/>kernel CONFIRMS product-obstruction + block identity (49) + G1/G2/G3 + band-mult (a)-(d) + FILT;<br/>caveat RE-GRADED 2026-08-01 — (51), rho&lt;=4/5 and the tilted OUTER half are now DERIVED;<br/>residuals are STRUCTURAL (pair tensor on Z_q^N, genPoly&lt;-&gt;phase, hident, block (i) Vandermonde, S_N average)<br/>[CERTIFIED* — NARROWER 6 labels/9 clauses]"]
  Lean --> LeanFid["LeanFid: consolidated statement-fidelity review COMPLETED 2026-07-31<br/>build self-reproduced 0/3011; census clean; 7c anchoring worksheets; honesty FAIL on record-accuracy<br/>(8 staleness defects incl. 2 live hash breaks -> closeout batch) [CERTIFIED*]"]
  Lean -.-> LeanAltQM["LeanAltQM: road not taken (rule 8b) — formalize the quantum query model,<br/>the adversary method, and reprove ABI/Zhang/BHK in Lean for an UNCONDITIONAL bound;<br/>multi-person-year, no Mathlib substrate. Revives if a quantum-query library appears [OPEN · PARKED]"]

  classDef proved fill:#d4f5d4,stroke:#2e7d32,color:#1b3d1b;
  classDef numerical fill:#fff3cd,stroke:#b8860b,color:#4a3b00;
  classDef conjectured fill:#ffe8b3,stroke:#c77800,color:#4a2b00;
  classDef certified fill:#fff0c2,stroke:#9a6700,color:#4a3200;
  classDef open fill:#e8eefc,stroke:#3a5bbf,color:#1a2b5c;
  classDef refuted fill:#f8d7da,stroke:#b02a37,color:#4a1116;
  classDef goal fill:#ececec,stroke:#555,color:#111;
  classDef constraint fill:#f0e6f7,stroke:#7b1fa2,color:#2a0e33;

  class G,B2 goal;
  class A1a,A1b,A1c,A1d,A1f,A2a,B4a proved;
  class A1,A1e,A2,A2b,L2d,L2e,L2eC,L2f proved;
  class B4bL2M1,B4bL2L2P3,B4bL2BandMult,B4bL2M2,B4bL2T4,B4bL2VBud,B4bL2Orient,B4bL2G1,B4bL2G2,B4bL2G3 proved;
  class B1,L32,L33,B4bL3AltCriticalInducedPacketPayloadValueTest,Rosmanis numerical;
  class L2,L2a,L2b,L32a,B4,B4b,B4bL1,B4bL3,B4bL3AltHiddenFrequencyMask,B4bL3AltHiddenFrequencyMaskCriticalEndpoint,B4bL3AltCriticalDuplicateClassification,B4bL3AltCriticalFrequencyAwareJointWalk,B4bL3AltCriticalJointStatisticEstimation,B4bL3AltCriticalOrbitIntertwinerAdversary,B4bL3AltCriticalCoupledUicAddressCycleKernel,B4bL3AltCriticalCoupledGrowingSelectorSpechtBranchingKernel,B4bL3AltCriticalCoupledLrMultiplicitySpaceMixing,B4bL3AltCriticalCoupledNonfactorizableCycleWordSelector,B4bL3AltCriticalCoupledFullPositionIncidenceThreeLayerWordKernel,B4bL3AltCriticalNoncommutingParentMixingKernel,B4bL3AltCriticalSharedBranchYoungLatticePatchKernel,B4bL3AltCriticalSameParentOccurrenceMultiplicityMixingKernel,B4bL3AltCriticalMacroscopicParentPatchKernel,B4bL3AltCriticalNonSkeletonHeavyOccurrenceCarrier,B4bL3AltCriticalFullYoungRankBalancedHarmonicKernel,B4bL3AltCriticalNonScaledPlethysticManyCornerOccurrenceKernel,B4bL3AltCriticalGloballyBoundedSymmetrizedPolynomialLowerBound,B4bL3AltCriticalThreeRowBlockStandardCovariantOccurrenceKernel,B4bL3AltCriticalThreeRowInducedBicovariantAlphabetPacketKernel,B4bL3AltCriticalInducedPacketYoungHolonomyLaw,B4bL3AltCriticalInducedPacketJointParentContentKernel,B4bL3AltCriticalInducedPacketOccurrencePencilClassification,B4bL3AltCriticalInducedPacketTotalEnergyResolventLaw,B4bL3AltCriticalInducedPacketRectangularTransferResolventLaw,B4bL3AltCriticalLiteralMarkedQueryPolarNormInterface,B4bL3AltCriticalPolarOffdiagonalBlockLaw,B4bL3AltCriticalPhysicalRangeReducingEqualityLaw,B4bL3AltCriticalInducedPacketOuterIncidenceNumeratorInterface,B4bL3AltCriticalInducedPacketPlaquetteFlowLaw,B4bL3AltCriticalNontrivialAlphabetOccurrenceMixingKernel,B4bL3AltCriticalCovariantBlockStandardOccurrenceMixingKernel,B4bL3AltCriticalCoupledDelocalizedMultiblockOccurrenceKernel,B4bL3AltCriticalPromiseIdealQuotientAdversary,B4bL3AltCriticalNonlinearAlgorithmDependentRecordingCarrier,B4bL3AltCriticalCorePsearchLift,B4bL3AltMultiscaleFrequencyMask,B4bL3AltBicliqueCoverGraphClaw open;
  class B4bL2P2Ansatz,B4bL2AltFewpair,B4bL2AltBkt,B4bL2AltNonidentical,B4bL2AltNonproduct,B4bL2AltCanonbasis,B4bL2AltAltinner,B4bL2AltMultipairVariablePairTotals,B4bL2AltMultipairSelectiveOrbitTensorKernel,B4bL2AltMultipairMovingRemezCubature,B4bL2AltMultipairMultiscaleGapfreeBaseMeasure,B4bL2AltMultipairLabelAwareFeketeBasisExchange,B4bL2AltMultipairContinuationSeededBlockFekete,B4bL2AltMultipairCriticalDensePaletteResidualWindow,B4bL2AltMultipairContinuumRemezSupportFlow,B4bL2AltNonproductProfileLatticeCore open;
  class LeanAltQM open;
  class LeanT2,LeanT3 numerical;
  class L2fC,L2g,B4bL2,B4bL2L2P6G,B4bL2AltTworay,B4bL2AltMultipair,B4bL2AltMultipairHighCtBalanced,B4bL2AltMultipairMultiscaleSplits,B4bL2AltMultipairGrowingRankMomentDesign,B4bRetarget,B4bCompcap,B4bL2JointLP conjectured;
  class B4bU1,G11,B4bL2Filt,Lean,LeanT1,LeanT2,LeanT3,LeanFid certified;
  class B3,L11,L12,L31,L2c,B4bL2AltWeightedActivationOrDualComposition,B4bL2AltBalancedPositiveSplitWeightedDualComposition,B4bL3AltCriticalSignedCycleWeightLaw,B4bL3AltCriticalStrictInjectionRecordingQuery,B4bL3AltCriticalReachabilitySensitiveRecordingFiltration,B4bL3AltCriticalTwoCellCovariantCrossSectorMixingKernel,B4bL3AltCriticalThreeRowBicovariantTwoCellAlphabetKernel,B4bL3AltCriticalThreeRowMixedTwoBoxFullTypeRecouplingKernel,B4bL3AltCriticalInducedPacketNoncommutingSylvesterLaw,B4bL3AltCriticalHsQueryEnergyLaw refuted;
  class C0 constraint;
```

---

## 2. Nested text outline (every node: decomposition · status · citation)

**KSUM.goal [OR-node · OPEN]** — reduce the alphabet-size requirement in the Belovs–Špalek
`Ω(N^{k/(k+1)})` k-Sum lower bound for fixed `k≥3`, and find `Q(N,k,q)` between `q=O(1)`
(Grover `√N`) and `q≥n^k` (BS tight). Provable by any one OR-branch reaching the tight target;
none does — Branch 1 banks a *floor*, Branch 2 is donor-blocked, Branch 3 computes but cannot
read an exponent. Disk: `KSUM_W3_CLOSEOUT.md:23-25`; `AUDIT.md:13-20`;
`ksum_W3_donor_survey.md:26` (target `n^{k/(k+1)}` at `q=Θ(N)`).

### OR-branch 1 — FROZEN-COORDINATE REDUCTION
Freeze `k−2` coordinates, embed the proved `k=2` claw→2-Sum encoding into the live coordinates.

**Branch status 2026-07-31: B1 CONJECTURED, A1 PROVED.** The 2026-07-30 composition-layer review
(§3.1) confirmed `A1`'s composition with two repairs (R-A1-1 every-window-target widening of A1a;
R-A1-3 coset-covering restatement of A1c — the all-pairs form was REFUTED); the repair batch
implemented both **in Lean, sorry-free** (`core_reduction_at`; `Q_window_cover`; `A1.composition`
re-proved; `KSUM.A1.holds` closes the Claim relative to the ABI/Tani + facts (i)/(ii) + freeze
interface), and the lead applied the review's PROVED license. `B1` rose OPEN → CONJECTURED by
mechanical §1 propagation (its Claim is now a proposition per review §7.4; the near-trivial route
proof `A1 ⇒ B1` is the one unwritten piece). **The route `B1 → KSUM.goal` stays REFUTED · DEAD**
(donor-intrinsic ceiling) — this branch banks the floor, not the goal.

- **Route [REFUTED · DEAD]** — naive target-coverage by **uniformly shifting** the `k−2` frozen
  coords. Failure: a uniform shift `δ` moves the target by `(k−2)δ`, so it cannot realize every
  target when `gcd(k−2,q)>1`. Cite: `AUDIT.md:15`. *Genuinely refuted for this method only —
  the repaired AND-node below routes around it (constant freeze, not a shift).*

- **Route [REFUTED · DEAD]** — odd-live-coordinate variant. Failure: with an odd number of live
  coords one coordinate stays unpaired and can join unintended `k`-subsets (leakage). Cite:
  `AUDIT.md:16`. *Refuted for this variant only — the repair uses an EVEN `2n`-coord live part.*

- **AND-node [CONJECTURED — §1 composition recompute 2026-07-30; was PROVED-BY-REDUCTION mod donor · INDEPENDENTLY AUDITED (F1)]** — the REPAIRED
  reduction = **Lemma W3E-1 / Theorem C**. Routes around both dead leaves above. Children A1a–A1d
  all remain PROVED (analytic proof + 40,668 W3E + 47,496 F1 exhaustive checks) and the theorem
  itself lives on the reviewed leaf A1d; what moved is the PARENT: under the revised DAG protocol
  §1 an AND edge is an obligation, the newly written composition proof `A1a∧A1b∧A1c ⇒ A1d` (on the
  canonical node) is unreviewed, and it surfaced a load-bearing premise in no child and no printed
  fact — the coordinate-freezing principle (= Lean audit finding F1, independently). Review of the
  composition restores PROVED. Edges re-typed same date: A1e (caveat) and A1f (certification
  record) moved children→related.
  Status is **PROVED-BY-REDUCTION modulo the on-disk ABI/Tani `k=2` donor**; the single-author
  caveat is **DISCHARGED** — a fresh Opus instance that did not author W3E re-derived the
  construction and re-verified it with its own from-scratch code (A1f). Cite:
  `KSUM_W3_CLOSEOUT.md:7-8`; `ksum_W3E_embedding_lemmas.md:5-9,15-41`; F1 audit
  `tools/ksum_f1_floor.py` (SHA `79a22f3f…`), `artifacts/logs_ksum_F1_20260718/floor_audit.log`
  (SHA `bf0c4d17…`); paper deliverable `research/ksum/paper/revision_k3.tex` **now INTEGRATED** into
  `research/ksum/paper/ksum_small_alphabet.tex` (§4 + Appendix A, 18 pp, clean pdflatex+bibtex; the
  parity lemma `lem:core-odd` inside it is R3-audited, A1f). `revision_k3.tex` kept as historical source.
  - **A1a [PROVED]** — freeze a core of `k−2` coords so no `d≥1` bad pattern hits, **plus the
    parked coordinate `v=t+(k−1)K+1` when `N−(k−2)` is odd**, **at EVERY window target**
    `t ∈ [t₀,t₀+k)`, `t₀=(k−2)(kK+1)` *(Claim widened 2026-07-30 per review R-A1-1/R-A1-3; the
    earlier text said only "freeze k−2 coords … summing to t" and was existential in the target)*.
    TWO verified variants:
    (i) **constant** `C₀=⌊q/(k−1)⌋` (W3E as authored) — `dist_q(d·C₀,0) ≥ C₀ ≥ kK+1 > mK`; and
    (ii) **positive core** `c_i=kK+1 (i<k−2), c_{k−2}=t−(k−3)(kK+1)` summing to `t`, every
    nonempty core subset sum in the safe band `[kK+1,t]` (revision_k3.tex). Both F1-verified.
    Machine-checked in the widened form, unconditionally: `KSUM.A1a.holds` ←
    `KsumAudit.KFloor.core_reduction_at`; the window hypothesis `q≥(k²−2)K+2k−1` is unchanged
    because it is exactly tight at the rightmost window target.
    Cite: `ksum_W3E_embedding_lemmas.md:26,17-21`; `revision_k3.tex` (Prop. `prop:core-even`,
    Lemma `lem:core-odd`); `artifacts/ksum_lean_repair_batch_20260730.md`.
  - **A1b [PROVED]** — use the **even `2n`-coordinate** `k=2` claw encoding for the live part,
    so no unpaired live coord exists (sidesteps the odd-leakage leaf). Cite:
    `ksum_W3E_embedding_lemmas.md:17-20`.
  - **A1c [PROVED]** — cover targets via a **window family** (shift one frozen coord, resp. slide
    the core sum `t` across a window) plus the **translation identity**
    `k-Sum_t(x)=k-Sum_{t+ka}(x+a·1)`. **Claim restated 2026-07-30 (review R-A1-3) in the
    COSET-COVERING form** — *for every `t` there is a window target `t′ ∈ t+kZ_q` with
    `Q(kSum_t) ≥ Q(kSum_{t′})/C`* — and PROVED with `C=2` (`KSUM.A1c.holds`). The earlier
    rendering ("every `t∈Z_q`" read as an ALL-PAIRS transfer between arbitrary targets) is what
    the translation identity does NOT give: it relates only targets inside one coset. That
    rendering is kept, unproved and unconsumed, as `KSUM.A1c.ClaimAllPairs`, next to the
    machine-checked in-range obstruction `not_reachable_k3_q21`. No parity condition. **F1 gcd argument
    verified**: coverage holds iff window length `≥ gcd(k,q)`; thresholds `q≥(k−1)(kK+2)` (even N)
    resp. `q≥(k²−2)K+2k−1` (odd N, parked coord) make window length `≥ k ≥ gcd`; full `Z_q` target
    sweeps pass with `gcd(k,q)` up to 6 (k=4,5,6), and below-threshold coverage is provably partial
    (load-bearing). Cite: `ksum_W3E_embedding_lemmas.md:30-32`; `floor_audit.log` Part C;
    `revision_k3.tex` (Lemma `lem:transl-cover`).
  - **A1d [PROVED-BY-REDUCTION mod donor; statement correction independently reviewed 2026-07-19,
    status unchanged]** —
    Put `q0(k)=2k²+2k−5`. For every fixed `k≥3` there are constants `C_k,c_k>0` such that,
    for all sufficiently large `N`, every target, and `q0(k)≤q≤C_kN`,
    `Q(k-Sum, Z_q, t, N) = Ω_k(√N·q^{1/6})`; for `q≥c_kN` the same reduction gives
    `Ω_k(N^{2/3})`. The bound is super-Grover when `q→∞` in the first range. The underlying
    F1-audited fixed-`K` proof already imposed `K≥2`; this statement correction passed fresh
    independent review (`artifacts/ksum_rev2_review.md`). Evidence: analytic complete-pattern proof
    + 40,668 W3E + **47,496 independent F1** exhaustive input checks, negative controls fire as
    required. Cite: `KSUM_W3_CLOSEOUT.md:7-8`; `ksum_W3E_embedding_lemmas.md:37-41,43-55`;
    F1 log `artifacts/logs_ksum_F1_20260718/floor_audit.log` (SHA `bf0c4d17…`),
    script `tools/ksum_f1_floor.py` (SHA `79a22f3f…`).
  - **A1e [PROVED · outcome (review §4.2) · re-typed related 2026-07-30]** — at `q=Θ(N)` this reads `Ω_k(N^{2/3})`, which for
    `k≥3` does NOT meet the conjectured `Θ(N^{k/(k+1)})` optimum. It is a floor, not the target.
    Under §1 a caveat is not an AND input; its real work is the route entry `B1→KSUM.goal` on
    `KSUM.goal` (kill argued at proposer tier, pending review). Cite: `ksum_W3E_embedding_lemmas.md:41`.
  - **A1f [certification · audit DONE & PASSED · PROVED]** — the reduction still rests on the
    on-disk ABI (`2103.16390`) / Tani (`2410.02243`) `k=2` claw donor taken **on trust** (inherited,
    not a defect — identical to the k=2 report). The owed independent hostile audit is now
    **COMPLETE**: a third-attempt fresh Opus instance (did NOT author W3E) re-derived both lemmas by
    hand and re-verified them with its own from-scratch code (oracle enumerates all C(N,k) subsets;
    shares no algebra with the encoders). **Results:** the reviewer's no-closing-coefficient trap is
    REAL (collision payloads `≡ 13,31,40,121 ≠ 0` at k=3,3,4,5) and the closing coefficient
    `u_k=−(ω^{k−1}−1)/(ω−1)` fixes it; the payload bound `P` **and** the tag-separation margin `P+1`
    are attained **exactly** (k=3..6), so `q=(P+1)(M+1)` is the tightest admissible modulus; all
    47,496 (floor) + 58,033 (embed) inputs PASS. Single-author star **removed**. **Findings (no
    REFUTE, claim intact):** (1) W3E-1 AS AUTHORED has a real k≥5 padding gap — padding with extra
    `C₀`-constants self-hits (`3C₀≡t₀` at k=3,q=24, demonstrated); revision_k3.tex closes it with a
    single parked-coordinate parity argument, verified k=3,4,5,6. (2) The core window floor
    `(k−2)(kK+1)` is sufficient but not tight for k≥4. **Scope of the PROVED stamp (proposer≠checker
    honesty):** the stamp covers the W3E-1 *claim* I independently audited — the reduction identity,
    all-`t` coverage, even-`N` (all k≥3), and odd-`N` for k=3,4. The **odd-`N` k≥5** closure (the
    parked-coordinate `Lemma lem:core-odd` in revision_k3.tex, authored in F1) was the last piece
    carrying a proposer=checker caveat; the **R3 pass INDEPENDENTLY RE-VERIFIED it and it is PROVED**
    (fresh Opus, did NOT author it: hand re-derivation of the proof and the `|W_odd|=q−[(k²−2)K+2k−1]+k`
    threshold identity + own from-scratch brute force — input-level `kSum==Claw` for k=3..8 incl.
    **k=7,8 beyond the F1 k≤6 range**, pattern-level `W∈[1,q−1]` for k=3..10, full `Z_q` coverage via
    translation, and negative controls proving the parked value and window load-bearing with the `+1`
    in `v=t+(k−1)K+1` exactly tight). Caveat **DISCHARGED**. This never weakened the asymptotic
    floor `Ω_k(√N·q^{1/6})`, which already held for every k≥3 via the fully-audited even-`N` case.
    Cite: `ksum_W3E_embedding_lemmas.md:158-159`;
    F1 `tools/ksum_f1_floor.py` (SHA `79a22f3f…`), `tools/ksum_f1_embed.py` (SHA `ca5bdbbc…`), logs
    `floor_audit.log` (SHA `bf0c4d17…`), `embed_audit.log` (SHA `e92eee2c…`);
    R3 parity re-audit `tools/ksum_r3_parity.py` (SHA `c62bd56c…`),
    `artifacts/logs_ksum_R3_20260718/parity_audit.log` (SHA `fb515cd2…`); integrated paper
    `research/ksum/paper/ksum_small_alphabet.tex` (§4 + Appendix A, 18 pp, clean compile).

### OR-branch 2 — CONDITIONAL k-COLLISION EMBEDDING  *(AND-node internally)*

**A2 restored to PROVED 2026-07-30** (composition CONFIRMED-WITH-REPAIRS by the independent
composition-layer review §3.2; R-A2-1 + the `gcd` §6.2 resolution applied; `gcd(k,q)=1` is a
THEOREM of the construction, machine-checked as `KSUM.A2.coprime_k_q`). B2 itself stays OPEN —
blocked solely on the walk-optimal donor ([[KSUM.k3.donor]]); its composition is CERTIFIED\*.
Embed `k`-partite `k`-collision into `k`-Sum, then transfer a collision lower bound = **Lemma
W3E-2**. This is an OR-alternative at the top level but an **AND-node internally**: provable only
if BOTH the encoding (A2) AND the donor consequence (L2) hold. The encoding is proved; the
consequence is blocked (no walk-optimal donor; the partial W floors are insufficient). Hence rendered as an AND bracket in the mermaid, not an OR
oval.

- **AND-node [CONJECTURED — §1 composition recompute 2026-07-30; was ENCODING PROVED · INDEPENDENTLY AUDITED (F1)]** — children A2a/A2b remain
  PROVED and the encoding lemma lives on in the manuscript (`lem:embed`); the newly written parent
  composition proof `A2a∧A2b ⇒ A2` (on the canonical node) is unreviewed and surfaced that the
  load-bearing `gcd(k,q)=1` hypothesis of the 2026-07-19 all-target repair lives only in a
  work-record line, in no Claim. Review restores PROVED. Original entry: exact, query-free reduction
  `k`-partite `k`-collision (range `R`) → `k`-Sum over `Z_q` with `q=Θ_k(R^{k−1})`; all `t`
  handled; `t≠0` existence proved with verified constructive witnesses. Single-author caveat
  **DISCHARGED** — a fresh Opus instance re-derived and re-verified the encoding with its own code
  (58,033 inputs + pattern cert k=3..6, all PASS). Cite: `KSUM_W3_CLOSEOUT.md:10`;
  `ksum_W3E_embedding_lemmas.md:8,58-98`; F1 `tools/ksum_f1_embed.py` (SHA `ca5bdbbc…`),
  `artifacts/logs_ksum_F1_20260718/embed_audit.log` (SHA `e92eee2c…`); `revision_k3.tex`
  (Prop. `prop:embed`).
  - **A2a [PROVED · 2026-07-19 all-target repair independently reviewed]** — complete formulas:
    `u_j=ω^{j−1}`, `u_k=−(ω^{k−1}−1)/(ω−1)`, tags
    `w_j=V·(2k+1)^{j−1}`, derived modulus `q_proof=(P+1)(M+1)`. **F1-confirmed** that this modulus
    is exactly tight: min tag-separation `= P+1` and max payload `= P` attained (k=3..6), so the
    good-pattern balanced-base-ω argument and the P+1 > P separation are both sharp. Cite:
    `ksum_W3E_embedding_lemmas.md:74-85`; `embed_audit.log` Parts C,E. The replacement proof that
    `gcd(k,(P+1)(M+1))=1`, and hence translation covers every target, passed the independent review
    `artifacts/ksum_rev2_review.md` (I2).
  - **A2b [PROVED]** — all wrong block-multiplicity patterns excluded by a balanced-base-`ω`
    argument; 62,140 W3E + **58,033 independent F1** exhaustive input-level checks PASS (`k=3,4,5`;
    pattern-level `k=3..6`); the no-closing-coefficient control breaks as required. Cite:
    `ksum_W3E_embedding_lemmas.md:85-98`; F1 `embed_audit.log` (SHA `e92eee2c…`).

- **Route [OPEN · PARKED]** — the `k`-Sum **consequence** still needs a walk-optimal
  small-range `k≥3` `k`-collision *detection* lower bound. Independently reviewed L2e gives
  `Ω(√n·min{R,n}^{1/6})` for `R≥2`, and reviewed L2f gives the stronger Belovs-derived
  exponent at `R=Ω(n²)`. Neither reaches `n^{k/(k+1)}`. Their W3E-2 children also do not
  advance this ancestor: independently reviewed L2eC is dominated by the existing `N^{2/3}`
  floor throughout the requested zone, and L2fC records that the Belovs range hypothesis maps
  beyond that zone. Therefore no tight donor was found and L2 remains OPEN/PARKED; B2 and the
  root remain OPEN. Cite: `artifacts/ksum_composition_review.md`;
  `artifacts/ksum_W_review.md`; original landscape and negative-search caveat:
  `artifacts/ksum_W_walkopt_landscape.md` Q1 and query log; prior baseline:
  `ksum_W3_donor_survey.md:93-95`.
  - **SUB-OR [PARKED · current-base capped]** — manufacture the donor via a `k`-fold Zhang
    W-LB2 supplies a simpler pending-review color-coding route from `k`-distinctness; the
    reduction + Tani's published `k`-symmetric transfer. Under-delivers: the realizable base is
    the `k`-distinctness dual-polynomial line — `n^{3/4−1/(2k)}` (BKT), improved to
    `n^{3/4−1/(4k)}` by **MTZ for every fixed `k≥2`** (`ksum_W3_donor_survey.md:31,97`) — always
    `< n^{k/(k+1)}` (`k=2` was a coincidence: ED approx-degree `= n^{2/3} =` target).
    **Crossover vs the Branch-1 free floor `N^{2/3}` at `q=Θ(N)` [CORRECTED 2026-07-18]:**
    `3/4−1/(4k) > 2/3 ⟺ k≥4`, so under the MTZ base the route beats the floor **for every
    `k≥4`**; MTZ's theorem holds for every fixed `k≥2`, but at `k=3` its exponent is exactly `2/3`
    (and at `k=2` it is below `2/3`). The previously
    recorded "only `k≥7`" is the BKT-only figure. The stale `k≥7` also appears in
    `KSUM_W3_CLOSEOUT.md:15,21` and the paper's §6 discussion — **propagation owed**
    (PROVER_PROMPT F4). Parking rationale, corrected: still sub-target for all `k`, still one
    genuinely new link of mathematics (the `k`-fold Zhang reduction), but for `k≥4` it now buys
    a strictly-better-than-floor bound — a stronger revival case than previously recorded.
    Propagation [UPDATED same day]: `KSUM_W3_CLOSEOUT.md` carries an appended Erratum; the paper's
    §6 grep-verified clean (audit-1 wording `n^{3/4−Θ(1/k)}` carries no crossover figure).
    Cite: `ksum_W3_donor_survey.md:31` (MTZ, TQC'20, arXiv:2002.08389, `k≥2`), `:97` (base
    line = BKT/MTZ), `:101` (exponent cap still below target).
  - **SUB-OR [PARKED · full research program]** — the "dream donor" `c≥(k−1)/(2(k+1))` (`k=3`:
    `c=1/4`, sitting on ABI's claw *upper*-bound envelope). Even if achieved, yields only a
    threshold shift `q: N³→N²` at `k=3`, never the tight `N^{k/(k+1)}` at `q=Θ(N)`. Cite:
    `KSUM_W3_CLOSEOUT.md:17`; `ksum_W3E_embedding_lemmas.md:127-138` (transfer arithmetic).
    **[SHARPENED 2026-07-17, F0; ENDPOINT-QUALIFIED 2026-07-18]** By the donor-cap L2d,
    `c=(k−1)/(2(k+1))` is *exactly* the algorithmic ceiling at `R=Θ(n)` — the dream **endpoint
    bound** is **maximal, not merely a goalpost**, and is **equivalent at that endpoint** to the
    statement "the k-claw Johnson walk is optimal at range = domain":
    `Q_k(n,Θ(n))=Θ(n^{k/(k+1)})`. KNOWN for `k=2` (ABI `Ω(√n·R^{1/6})` at `R=Θ(n)` = `Ω(n^{2/3})`,
    matches the walk); **OPEN for `k≥3`**. The converse to a single uniform donor family throughout
    smaller `R` is **UNPROVED**. So the endpoint bound is not a free target — it is a tight lower
    bound one `k` beyond where the ABI/Aaronson–Shi methods currently reach. Cite:
    `artifacts/ksum_F0_obstruction_note.md` §2 Cor. A.
  - **SUB-OR [REFUTED · DEAD]** — skip the polynomial method entirely and transfer **Belovs
    2026's tight non-polynomial `k`-distinctness framework** to small alphabet. Failure: that
    framework is **large-alphabet-only** (`q ≥ Ω(n²)`) and **not range-symmetric**, so neither
    Ambainis's nor Tani's transfer engine carries it — the one method that beats the degree cap
    does not transfer. This is obstruction 3 of the W3 map. Cite: `KSUM_W3_CLOSEOUT.md:16`;
    `ksum_W3_donor_survey.md:102` (risk 2: "explicitly large-alphabet and non-symmetric, so
    neither Ambainis nor Tani transfers it"), `:112` (Belovs 2026 tight lower = large alphabet).

  - **L2e [PROVED · independently reviewed · PARTIAL FLOOR, dotted edge]** — for the formal
    problem domain `R≥2`, restrict the first two lists to an ABI 2-claw over
    `s=min{R,n}` and fix every remaining list to a surjection onto `[s]`. Every base claw
    extends, while every k-claw necessarily contains a base-list equality; filler collisions
    create no spurious witness. Fixed fillers are query-free. Thus
    `Q_k(n,R)≥Q_2(n,s)=Ω(√n·s^{1/6})`, hence `Ω(n^{2/3})` for `R≥n`.
    The review found and repaired one MINOR endpoint omission: at `R=1` the function is
    constant YES. This does not discharge L2. **Integrated into the paper** as Proposition
    `prop:kclaw-fillers`. Cite: `artifacts/ksum_W_review.md` R-A;
    source theorem `artifacts/references/abi_2103.16390_src/claw.tex:289-295`.
    - **L2eC [PROVED · fresh independent rule-6 review completed · COMPOSITION OUTCOME, dotted edge]** —
      for fixed `k≥3`, `2≤R≤n`, `N=kn`, every target, and the exact constructed modulus
      `q_k(R)=(P_k(R)+1)(M_k+1)=Θ_k(R^{k−1})`,
      `Q(k-Sum_{Z_q,t,N})=Ω_k(√N·q^{1/(6(k−1))})`. The family has `n−1` points,
      counting function `Θ_k(X^{1/(k−1)})`, and natural density zero; no all-`q` or
      arbitrary-`N` interpolation is claimed. The bound is at most `N^{2/3}`, is consistent
      with the walk upper bound, and is dominated at every covered point by PROVED Theorem C.
      Thus the composition is correct but supplies no new lower-bound envelope. **Integrated into
      the paper** only as dominated Remark `rem:kclaw-composition`. Cite:
      completed review `artifacts/ksum_composition_review.md`; run
      `artifacts/logs_ksum_W_20260718/codex_comp_review_run.log`; source
      paper labels `prop:kclaw-fillers`, `rem:kclaw-composition`, and `lem:embed`.

  - **L2f [PROVED · independently reviewed · PARTIAL FLOOR, dotted edge]** — random color coding
    maps worst-case decision `k`-distinctness to `k`-partite `k`-claw. Dummies are distinct
    and outside the donor alphabet, hence every donor NO maps to NO for every coloring; a fixed
    k-fold value is colorful with probability `k!/k^k`. Amplifying each claw call before
    `O_k(1)` repetitions gives a worst-case bounded-error reduction with `O_k(1)` query
    overhead. Belovs 2026 therefore gives `Ω(n^{3/4−1/(4(2^k−1))})` for sufficiently large
    `R≥C_k n²`. One MINOR amplification omission was repaired. This neither discharges L2 nor
    repairs L2c, which concerns moving Belovs to small alphabet. **Integrated into the paper**
    as Proposition `prop:kclaw-coloring`. Cite:
    `artifacts/ksum_W_review.md` R-B; source `new-adversary_v6.tex:93-102,3078-3089`.
    - **L2fC [CONJECTURED · pending-review · RANGE-OBSTRUCTION OUTCOME, dotted edge]** — W3E-2 maps the required
      `R=Ω(n²)` only to `q=Ω_k(N^{2(k−1)})`, strictly above the requested
      `q≤Θ_k(N^{k−1})` zone. At `R=Θ(n²)` it would reproduce the donor exponent there,
      but BS already applies and is stronger. Thus R-B has no licensed in-zone composition
      corollary. Cite: `artifacts/ksum_W_review.md` C-B.

  - **L2g [CONJECTURED · pending-review · OBSTRUCTION OUTCOME, dotted edge]** — a lifted reversal
    of W3E-2 is structurally possible: each claw item carries `k−1` colored k-sum coordinates and
    infers the missing value. But `N=Θ(m^{k−1})`, so BS yields only
    `Ω(N^{k/(k²−1)})<√N` for `k≥3`. A domain-preserving factorization is obstructed because the
    sum tensor does not factor into equality of unary labels. Cite:
    `artifacts/ksum_W_walkopt_landscape.md` Can W3E-2 be reversed?.


  - **CONSTRAINT [PROVED · independent rule-6 review completed 2026-07-18 · prunes L2a–L2c from
    above] — the DONOR-CAP (endpoint iff qualified).**
    Attached to L2 by a dotted edge (a proved pruning fact, like C0 — not an OR-route, so L2's
    OR-max is unchanged and the root stays OPEN). The original synthesis has now completed the
    independent review chain required by rule 6: hostile audit `artifacts/ksum_final_gap_audit.md`
    (Target 2), prescribed repairs `artifacts/ksum_gap_fixes_applied.md`, and completing review
    `artifacts/ksum_gap_verification.md`, including the fresh exact-arithmetic run
    `artifacts/logs_ksum_GAP_20260718/captable_verify.log`. The external Tani walk input is
    **PROVED-IN-LIT** and was pinned to primary-source Corollary 11 by the hostile audit; the reviewed
    synthesis is as follows. The donor property `KColl_k(n,R)` has two upper
    bounds: **(walk)** Tani `Q_k=O(n^{k/(k+1)})`, **range-INDEPENDENT** (arXiv:0708.2584, TCS 2009);
    **(value-search)** `Q_k=Õ(√(Rn))=Õ(√n·R^{1/2})` (nested Grover + HMdW robust search, PROVED in
    the note §1a). A lower bound cannot exceed an upper bound, so any donor `Ω(√n·R^c)` at range
    `R=n^θ` obeys `c ≤ min{1/2, (k−1)/(2θ(k+1))}`; at `R=Θ(n)` this is **`c ≤ (k−1)/(2(k+1))`,
    exactly the dream exponent** (arithmetic machine-checked). Consequences: (i) **no donor can
    overshoot the dream value** — the dream donor is the ceiling (⇒ the L2b reframing); (ii) at the
    endpoint `R=Θ(n)`, the dream endpoint lower bound exists **iff** the walk is optimal there; this
    does **not** prove a uniform donor family for all smaller `R`; (iii) reaching the k-Sum target
    requires a donor *tight against* the algorithm at some
    `θ∈[(k−1)/(k+1),1]`, i.e. `q∈[Θ(N^{(k−1)²/(k+1)}),Θ(N^{k−1})]`; for `k≥4` the low-`q` sub-zone
    `[Θ(N),Θ(N^{(k−1)²/(k+1)}))` of the B2 value zone is **BLOCKED** (needs `c>1/2`, exceeding
    value-search). In `E=log_N q` coordinates this blocked interval has relative length
    `k(k−3)/((k+1)(k−2))` within `[1,k−1]` (`2/5` for `k=4`, `5/9` for `k=5`). **Honest caveat:**
    the `1/2` cap is loose — an ABI-style `k≥3` small-range
    algorithm (unbuilt; k=2 gives `R^{1/4}<R^{1/2}`) would *shrink* the reachable zone, so the
    apparent `k=3` small-`q` opening is an artifact and does not reopen L2b. Cite:
    `artifacts/ksum_F0_obstruction_note.md` (SHA-256 `7416bc70fa4a1f2f`); machine-check
    original machine-check `tools/ksum_f0_captable.py` (`130a06fde1f4eb5d`) →
    `artifacts/logs_ksum_F0_20260718/captable.log` (`8192dfb3cf7f5ecb`); repaired checker SHA-256
    `75c5cebf3f9931de70ea4a1169016bce9d6e096c4901fd30eaaf03d7543c4408` → fresh review run
    `artifacts/logs_ksum_GAP_20260718/captable_verify.log`; fresh literature pass
    `artifacts/references/ksum_F0_literature_evidence.txt`
    (`ad6d9ec16b785ee0`, NO-DONOR reconfirmed: Tani-2410.02243 fwd-cites=0, MTZ-2002.08389
    fwd-cites=14 none a small-range k-partite claw LB).

### OR-branch 3 — DIRECT / INCUMBENT SOLVERS
No reduction; compute `Adv±` directly.

**Branch status 2026-07-30: REFUTED · PARKED** — the independent composition-layer review
(§4.3–§4.4) confirmed the route kills: every registered route into B3, and B3's route into the
KSUM.goal, is dead ([[KSUM.G11]] — finite exact values license no uniform exponent — plus the reviewer's
independent ground that these are `k=2` solvers against a `k≥3` goal). The solvers below KEEP their
NUMERICAL value as evidence; the revival condition (on the node) is an analytic, uniform-in-`n`
`Adv±` route stated for `k≥3`.

- **Route [REFUTED · DEAD]** — the incumbent `ksum_probe.py` regular-representation "reduction."
  Failure: it **inflates** the PSD block `6–29×` above the unreduced problem, SCS is
  non-convergent, it hangs at its smallest grid point and **never produced a single `Adv±`
  number** — a phantom incumbent. Cite: `KSUM_STAGE0_VERDICT.md:14,39,86`;
  `KSUM_STAGE0_CHALLENGE.md:86-87`; probe at repo-root `ksum_probe.py`.

- **Route [NUMERICAL / WORKS — `k=2` ONLY]** — the fresh unreduced direct `Adv±` solver produced
  the first real 2-Sum values: `(n=3,q=3)=2.4186` (±~4e-4), `(4,3)=2.7127`, etc.  **No exact
  `k≥3` `Adv±` value exists anywhere on disk** — `k≥3` was never solved directly. Cite:
  `KSUM_STAGE0_VERDICT.md:14,71`; provenance `:120-121`.
  - **[OPEN]** — the exponent is **numerically undecidable** at reachable `n`: the
    pilot band lands `1.49–1.93` vs `√n` `2.00–2.45` vs `n^{k/(k+1)}` `2.52–3.83`, all inside a
    factor of 2; the hypotheses differ by `n^{1/6}` so a `2×` separation needs `n≈256` at `q=3`.
    **[EVIDENCE EXTENDED 2026-07-18]** the matrix-free extension pushed `q=3, t=1` to `n=7,8`:
    certified `= 2.10093, 2.26020`; `certified/√n` rises monotonically `0.775→0.799` over
    `n=5..8` — the registered drop-falsifier never fired, and the rise (+3.1% over `n=5→8`) is
    still far under the `+8.15%` an `n^{1/6}` law predicts: **non-discriminating in both
    directions**, per the permanent blocker. Cite: `KSUM_STAGE0_VERDICT.md:59-61`;
    `KSUM_SMALL_G_COMMISSION.md:1205-1208`; extension log
    `artifacts/logs_ksum_stage0_20260716/C7_extend.log:15,22`.

- **Route [NUMERICAL · INDEPENDENT REVIEW COMPLETED] — L33 isotypic/Wedderburn-reduced solver BUILT for cyclic 2-Sum.**
  The exact position-block projection reduces the HLS matrix to one input block; full
  S_N×C(σ) averaging puts it in the S_(N−1)×C(σ) commutant; a generic real group-algebra
  element plus Schur-polar copy alignment exposes the true multiplicity PSD blocks (not the dead
  incumbent's regular representation). Five requested new points returned: preferred high-accuracy
  values (5,4,0)=3.334239787, (5,4,1)=3.312520213, (6,3,0/1)=3.349771964,
  (7,3,0)=3.631736630; (5,5,0) and (6,4,0) hit the explicit 1,200-second cap.
  Independent review passed the exactness/code audit and found no value-changing defect. Tightened
  reduced/unreduced anchors agree within 3.72e-8 at (3,3,0) and 2.62e-6 at (4,3,0), adjudicating
  the historical deviations as SCS noise. Stage-0's 56/28 were S_N input-histogram counts; the
  correct full-G YES/NO equality-orbit counts are 306/81. A non-anchor (3,4,1) full-cone spot check
  agrees within 1.31e-6. Printed decimals remain numerical approximations; two MINOR
  robustness/provenance caveats are recorded in the review.
  Cite: artifacts/ksum_L33_reduced_solver_note.md;
  independent review artifacts/ksum_L33_review.md;
  original manifest artifacts/logs_ksum_L33_20260718/SHA256SUMS.txt;
  review manifest artifacts/logs_ksum_L33_20260718/l33r_SHA256SUMS.txt;
  script tools/ksum_l33_reduced_adv.py SHA-256
  940de0ceb9472aa5fa47e33b7fd0bfb604fbb020e4245aec3c6ff2d1e0d76111.

### OR-branch 4 — UPPER-BOUND / ALGORITHM SIDE  *(AND-node internally after B4 pass)*
The KSUM.goal asks for Q(N,k,q), which includes the upper side; every branch above searches lower
bounds only. At k=2, B4a now proves Q(2-Sum over Z_q,t,N)=O_epsilon(N^(1/2+epsilon)q^(1/4))
for every q>=2 and target t. The known lower side is Omega(sqrt(N)q^(1/6)); therefore the
q-exponent gap 1/6<1/4 remains. This branch is an **AND-node internally** for closing that
middle gap: B4a supplies the independently completed upper bound, while B4b is the remaining
exponent-matching obligation. Therefore B4 is min(PROVED,OPEN)=OPEN.

- **B4a [PROVED — fresh independent rule-6 reviews completed]** — The bounded-query ABI port gives
  Q(2-Sum over Z_q,t,N)=O_epsilon(N^(1/2+epsilon)q^(1/4)) for every q>=2 and every target t, with no parity assumption.
  Fixed-point multiplicity preprocessing removes the single-list compression false-positive mechanism.
  The actual-short-list Johnson fallback discharges D1; capped counting, the h<=4U gate, fixed virtual
  sizes, prefix truncation, and bounded nested calls discharge D2. The epsilon and fixed-point error
  MINORs are also closed. The round-2 reviewer independently re-derived both repairs, checked the full
  algorithm/recursion/error/query balance, and found no new defect. Cite:
  artifacts/ksum_B4_upper_note_v2.md; completion review: artifacts/ksum_B4_review2.md;
  provenance: artifacts/logs_ksum_B4_20260718/codex_review2_run.log. The 2026-07-19 Appendix-B
  coherent-oracle repair (square-root loss, `M_i` caps, and hybrid) independently passed
  `artifacts/ksum_rev2_review.md` (I3). Integrated into the paper as
  Theorem `thm:k2-upper` with full proof in Appendix `app:k2-upper`; paper cite:
  research/ksum/paper/ksum_small_alphabet.tex.

- **B4b OR-node [OPEN]** — Close the remaining middle-regime exponent window. B4a narrows the upper
  side to q^(1/4), but the proved lower side is only q^(1/6); 1/6<1/4, so the complexity is not
  determined. Front U now has one scoped obstruction outcome; it redirects search but does not close
  the global gap. Cite: paper Open Problem `prob:k2-gap` in
  research/ksum/paper/ksum_small_alphabet.tex; completed upper proof artifacts/ksum_B4_review2.md.
  - **B4bU1 [CERTIFIED* · CONDITIONAL OUTCOME]** — In the explicit charged model
    F_SC^charge, the one-level minimax map is (a,c) to
    (a/(a+1/2),(a-1/2+c)/(a+1/2)); from Johnson it preserves
    c=1/4-(3/2)(a-1/2), so an N exponent tending to 1/2 forces q exponent 1/4. Fresh review
    confirmed residual MNRS, pair-Grover, dyadic stratification, and nonuniform-depth optimization.
    Named caveats: no selector/child composition lower bound for a broader algorithm family, and the
    plateau constrains only all-q range-independent bases. This is not a global quantum lower bound.
    Canonical cite: research/ksum/proof-dag/nodes/KSUM.B4b.U1.yaml; review:
    artifacts/ksum_B4bU1_review.md.
  - **B4bRetarget tool [CONJECTURED · pending-review · related/non-propagating]** — Campaign
    milestone relaxed to any `eta>1/6`: beating `Omega(sqrt(N)q^(1/6))` at `q=Theta(N^(2/3))`
    tolerates a total bridge-loss factor up to `q^(1/12-delta)`; bounded-loss interfaces
    re-admitted and the literal-query triage re-runs under this budget. Budget arithmetic
    unreviewed. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.retarget.yaml.
  - **B4bCompcap obstruction [CONJECTURED · pending-review · related/non-propagating]** —
    Screening cap: disjoint-block factorized constructions instantiated with currently proved
    block hardness certify at most `sqrt(N)q^(1/6)`; surplus requires cross-block
    shared-alphabet coupling or self-referential small-range block hardness. Formal proof not
    yet commissioned. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.compcap.yaml.
  - **Lean AND/tool [CERTIFIED\* · ALL-STARRED 2026-08-01 (census DF-9-verified) · related/non-propagating to G]** — Machine-checked (Lean 4 + Mathlib
    v4.31.0) audit of the paper's theorems. Status computed as `min(children)`. Three standing
    scope clauses: (a) the cited bounds (`thm:abi`, `thm:tani`, query-model facts (i)/(ii)) enter as
    fields of an abstract `QueryModel` **structure** — deliberately not `axiom`, so `#print axioms`
    stays at Lean's three standard axioms and the citation manifest is machine-checked — hence a
    Lean-verified derivation is exactly as strong as those citations and not one notch stronger;
    (b) formalization **relocates** risk into "does the formal statement say what the paper says",
    which is why `LeanFid` is a separate node and a green build alone licenses nothing; (c) the
    audit is confirmatory and can only DEMOTE — it produces no new asymptotic bound, and the
    endpoints stay `Omega(N^(11/18)) <= Q <= O(N^(2/3))` at the critical alphabet. Gate G-L1
    (environment) PASSED 2026-07-30: `lake build` green, 1982 jobs, substrate probes for `ZMod`
    (both the within-half natural-number form and the cross-half integer form), pigeonhole, and
    `rpow` all compile. Canonical: research/ksum/proof-dag/nodes/KSUM.LEAN.yaml; development:
    research/ksum/proof-dag/lean/ (moved there 2026-07-30 under DAG_PROTOCOL.md §7.2, a sibling of
    nodes/; forwarding stub at research/ksum/lean/README.md). That directory also holds the
    DAG-mirroring layer KSUM/, whose module names ARE node ids (§7.3) and whose per-node
    `composition` theorems are the Lean form of the §1 composition proofs.
    - **LeanT1 tool [CERTIFIED\* · fidelity PASS-WITH-CAVEATS 2026-07-31 · conditional on ABI/Tani + `sec:prelim` facts (i)–(iv), all four STATED since paper v5.2 — F1/F2 (`freeze` = (i)+(iii), `constQ` = (iv)) were unstated when the audit found them and were added by manuscript repairs M-1/M-2 on 2026-07-31]** — `lem:encode` → `lem:shift` → `lem:oddN` → `thm:main-odd` →
      `thm:main-general` → `cor:threshold`, plus `thm:oabarrier`, in explicit-constant form (no
      `Omega`/`Theta` in the statements, which is strictly stronger and removes the two-parameter
      asymptotic ambiguity where `N` and `q` are coupled). Gate G-L2 is `lem:encode` sorry-free.
      `thm:k2-upper` is out of scope (an algorithm). Canonical:
      research/ksum/proof-dag/nodes/KSUM.LEAN.T1.k2-main-line.yaml.
    - **LeanT2 tool [CERTIFIED\* · fidelity PASS-WITH-CAVEATS 2026-07-31 · cores unconditional]** — Two new
      modules, neither importing `QueryModel`, so every theorem in them is UNCONDITIONAL.
      `KsumAudit/T2KFloor.lean`: `lem:core`; `prop:core-even` + `lem:core-odd` as one theorem
      `core_reduction` quantified over `m in {k-2, k-1}` (so both parities, parked coordinate
      included); `lem:transl-cover` windows (i)/(ii) and the Bezout coset-covering step, which
      machine-confirms F-R2 (no coprimality hypothesis — coverage runs off the window LENGTH).
      `KsumAudit/RosmanisBarrier.lean`: `prop:rosmanis`(1) count `>= 2` proved ORBIT-PROPER (the
      `S_N x C(sigma)` action is defined, preserves `D_0`, and the separating invariant is PROVED
      invariant) in both branches `m >= 2` and `m = 1`; (2)'s two finite witnesses; (3).
      **NOT formalized, declared not omitted:** the bijection with `(f, lambda)` and the count
      FORMULA `sum_f p_{<=m}(N-f)`; part (2)'s representation sentence; `C(sigma) = (C_2 wr S_m) x
      S_tau`; `prop:embed`; and `prop:core-even`/`lem:core-odd` at every window target (they are
      proved at the base window target `t_0 = (k-2)(kK+1)`, which suffices for `A1a.Claim` because
      that Claim is existential in `t_0`).
      Gates G-T2a/c/d/e PASS; **G-T2b FAIL-BY-CLAIM-DEFECT**: `KSUM.A1c.Claim` is the all-pairs
      target form, unprovable because `lem:transl-cover` is coset-local; the in-range obstruction
      `KSUM.A1c.not_reachable_k3_q21` (`k=3, q=21`) is machine-checked, and the faithful content is
      proved as `Q_kSum_translate_le` / `Q_window_cover` / `Q_le_of_coprime`.
      `KSUM.A1a.Claim` moves `stated -> proved`, unconditionally.
      **F-T1 pattern: `prop:rosmanis` has NO DAG node** — flagged for the lead, not created.
      Canonical: research/ksum/proof-dag/nodes/KSUM.LEAN.T2.rosmanis-kfloor.yaml.
    - **LeanT3 tool [CERTIFIED\* · fidelity PASS-WITH-CAVEATS 2026-07-31 · NARROWER 6 labels/9 clauses · unconditional]** — The obstruction group. Label↔node mapping RESOLVED FROM
      DISK (gate G-T3a): `thm:pair-tensor`→M1, `thm:tilted-log-band`→L2P3,
      `lem:band-multiplication`→BANDMULT, `thm:product-obstruction`→M2,
      `thm:block-obstruction`(48-49)→T4 and (50)→VBUD, `thm:orientation-obstruction`→ORIENT,
      `prop:transfer-facts`(G1/G2/G3)→G1/G2/G3; **`lem:factorial-filtration` and `prop:joint-lp`
      have NO node at all** and are the two labels left unformalized. This tier needs **no
      `QueryModel`** (verified by grep), so every theorem is UNCONDITIONAL — categorically stronger
      evidence than T1/T2. The interrupted first executor's eight modules were audited
      adopt/repair/reject **44/0/0**, with **14 theorems added**; build green (3009 jobs, exit 0),
      58 declarations at Lean's three standard axioms, zero sorry/axiom, zero warnings (16 fixed).
      Fidelity **as graded 2026-07-30**: **6 FAITHFUL, 4 NARROWER, 0 WIDER, 1
      AMBIGUOUS-IN-SOURCE**. The NARROWER that mattered was `thm:orientation-obstruction` clause
      (b) — the only one on an OBSTRUCTION: Lean assumed the paper's displayed bound (51) and
      derived `<=1/2` rather than proving (51). The other three (pair-tensor, tilted-log-band,
      band-multiplication clauses (a)/(d)) are positive claims where NARROWER means the audit
      under-delivers.
      **RE-GRADED 2026-08-01** (delta-fidelity review §3.B rows 8/9/14/29; node caveat rewritten by
      the docs-sync batch): the gap-closure batches PROVED the analytic step producing (51) — the
      derived exponent `1-r(m-1)-m` equals the paper's `r+1-m(r+1)` — DERIVED `rho_j <= 4/5` from
      the tilted inner via the manuscript's own three-weight step, made the tilted-band OUTER half
      hypothesis-free (including both displayed constants `C_h <= 25/19`, `sum_j A_j <= 29/23`),
      PROVED the (G2) satellite bridge with Maschke granted nowhere, and PROVED
      `lem:factorial-filtration` in both directions. What remains is STRUCTURAL, not analytic: the
      inner pair tensor as a measure on `Z_q^N` (so `thm:tilted-log-band` as a whole is still not a
      theorem of the module), the `genPoly`<->phase-function identification, `hident` in block
      clause (iii), block clause (i)'s `m`-fold multivariate Vandermonde, and the `S_N`-average
      operator. Two draft HYPOTHESIS SUBSTITUTIONS were
      found and proved away: (G3)'s `tr A != 0` vs the paper's "nonzero PSD", and (G2)'s `R_H v=0`
      vs "v lies in a nontrivial H-satellite". The `beta1` C3 identity was NOT formalized, per its
      NUMERICAL cap. No obstruction node's status changed. Report:
      artifacts/ksum_lean_T3_obstructions_20260730.md; evidence:
      artifacts/logs_ksum_lean_T3_20260730/. Canonical:
      research/ksum/proof-dag/nodes/KSUM.LEAN.T3.obstruction-theorems.yaml.
    - **LeanFid tool [CERTIFIED\* · review COMPLETED + archived 2026-07-31 · honesty FAIL on record-accuracy → closeout batch]** — Statement-fidelity
      review by a fresh instance that did not author the formalization: per-theorem verdict
      FAITHFUL / NARROWER / WIDER / DIVERGENT, with the Lean statement rendered back into English
      BEFORE the LaTeX is read (rule 7c anchoring ban). Named failure modes: vacuity (unsatisfiable
      hypotheses ⇒ true and useless; countered by an explicit witness instance per theorem),
      weakening, definitional smuggling, interface over-assumption (a `QueryModel` field stronger
      than what ABI/Tani actually give), and non-instantiability (the structure is never shown
      plausibly inhabitable — an obligation that stays open and must be declared, so the reader
      knows T1/T2 are conditional). Canonical:
      research/ksum/proof-dag/nodes/KSUM.LEAN.statement-fidelity.yaml.
    - **LeanAltQM tool [OPEN · PARKED · rule 8b road-not-taken]** — Build the bounded-error
      quantum query model, the negative-weight adversary method, and a Lean reproof of
      `thm:abi`/Zhang/BHK from first principles, for an unconditional machine-checked bound. Parked:
      no Mathlib substrate, a three-deep citation chain, multi-person-year effort, and it does not
      target where an error could actually hide (our chain and our obstruction theorems). Not
      REFUTED — correct mathematics, merely far outside budget (rule 3). Revives if a Mathlib-level
      quantum-query library appears, at which point it discharges the conditionality of `Lean`
      rather than replacing it. Canonical:
      research/ksum/proof-dag/nodes/KSUM.LEAN.ALT.full-query-model.yaml.
  - **B4bL1 [OPEN · P2 family kill recorded · pending-review]** — The explicit three-class
    reciprocal-Hamming polar completion (rank-one spine, tau=0 multiplicity-two satellites, pooled
    remainder) is PSD and HLS-feasible but captures only 38.90%--62.83% even with per-instance
    oracle-best balance weights. The P2 stop fired before held-outs/P4. Revive only with a finer
    joint-histogram cross kernel or exact cross-N sector labels. Canonical cite:
    research/ksum/proof-dag/nodes/KSUM.B4b.L1.yaml; report: artifacts/ksum_L1_phase1.md.
  - **B4bL2 [CONJECTURED · phase-3/4/5 reviewed components and phase-6 G1/G2/G3 PROVED; scoped composition and literal phase-6 transfer mechanisms BLOCKED/reviewed; aggregate L2P6-G candidate CONJECTURED]** — The canonical
    obligation implements the completed D7 review's odd-q/all-target scope and labels even q
    optional. Reviewed M1/M2 stand. Fresh phase-3 review proves unit l1, full invariance, correlation
    at least `437/581>3/4`, and pure high degree `2(1+floor(log_5((q-1)/2)))` for every odd q>=3 and
    N>=q. MINOR D9 restricts the genuine M2 escape to q>=5; q=3 is the in-class M1 endpoint. The band
    is logarithmic and has no sqrt(N) growth. Phase-4 review proves that fixed-allocation unaveraged
    absolute-value OR composition multiplies the inner conditional-correctness parameters (at most
    4/5 per logarithmic block), and that whole-pair soundness consumes disjoint sigma-pairs. MAJOR
    D10 leaves norm-changing symmetry averaging outside the product upper bound. The selected
    whole-pair mechanism remains BLOCKED by the value budget. Phase-5 review proves that the exact
    occupancy convolution multiplies the factorial band and that cross-block NO coherence costs
    `2^{-r(m-1)}`. A Fourier norm floor bounds correlation by `1/2` for identical phase-3 blocks
    with one common exact pair total on every pair and block and a product outer tensor. That family
    is BLOCKED/reviewed. Unequal totals, nonidentical blocks, non-product couplings, alternative
    inners/non-composition shapes, and the cap-scale obligation remain open; finite checks make no
    exponent claim (G11). Canonical cite:
    research/ksum/proof-dag/nodes/KSUM.B4b.L2.yaml; reviewed component: artifacts/ksum_L2p3_review.md;
    phase-4 report/review: artifacts/ksum_L2_phase4.md, artifacts/ksum_L2p4_review.md; phase-5
    report/review: artifacts/ksum_L2_phase5.md, artifacts/ksum_L2p5_review.md.
    - **B4bL2M1 tool [PROVED · related/non-propagating]** — Odd `q`, `N>=q`, all targets;
      exact `l1=1`, `S_N x C(sigma)` invariance, and annihilation below `q-1`. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.M1.yaml; report/review:
      artifacts/ksum_L2_phase2.md, artifacts/ksum_L2p2_review.md.
    - **B4bL2L2P3 tool [PROVED · related/non-propagating]** — Tilted witness with band
      `2(1+floor(log_5((q-1)/2)))` and correlation `>=437/581>3/4`; D9 gives genuine M2 escape
      only for `q>=5`. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.L2P3.yaml;
      report/review: artifacts/ksum_L2_phase3.md, artifacts/ksum_L2p3_review.md.
    - **B4bL2BandMult tool [PROVED · related/non-propagating]** — `S_N`-averaged block
      convolution adds annihilation bands by multivariate Vandermonde and is legally normalizable.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.BANDMULT.yaml; report/review:
      artifacts/ksum_L2_phase5.md, artifacts/ksum_L2p5_review.md.
    - **B4bL2M2 obstruction [PROVED · related/non-propagating]** — In the complete
      five-condition fully locally zero-balanced sign-separated product/sign-aligned-positive-
      mixture class, correlation is exactly `2^(1-(q-1)/2)` for odd `q>=5`. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.M2.yaml; report/review:
      artifacts/ksum_L2_phase2.md, artifacts/ksum_L2p2_review.md.
    - **B4bL2T4 obstruction [PROVED · related/non-propagating]** — `rho<=4/5` and the
      correlation-product identity hold only for fixed-allocation unaveraged sign-bit composition;
      D10 excludes norm-changing averaging. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.T4.yaml; report/review:
      artifacts/ksum_L2_phase4.md, artifacts/ksum_L2p4_review.md.
    - **B4bL2VBud obstruction [PROVED · related/non-propagating]** — Whole-pair/value-
      disjoint allocation forces `m*r0<=(q-1)/2`, so block count cannot track `N` at fixed `q`.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.VBUD.yaml; report/review:
      artifacts/ksum_L2_phase4.md, artifacts/ksum_L2p4_review.md.
    - **B4bL2Orient obstruction [PROVED · related/non-propagating]** — For the identical-
      block/common-exact-total/product-outer class with `N=mrs`, true-NO coherence costs exactly
      `2^{-r(m-1)}` and correlation is `<=1/2`. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ORIENT.yaml; report/review:
      artifacts/ksum_L2_phase5.md, artifacts/ksum_L2p5_review.md. Lean T3 note 2026-07-30: clause
      (a) machine-checked unconditionally; clause (b) only as "(51) ⇒ ≤1/2" — producing (51) stays
      prose-only under the archived review; status unchanged.
    - **B4bL2Filt tool [CERTIFIED* · scope caveat on node · related/non-propagating · LATE
      REGISTRATION]** — `lem:factorial-filtration`, the falling-factorial query filtration: the
      bridge converting occupancy-row "pure high degree" statements into QUERY-degree statements.
      Registered 2026-07-30 after Lean-T3 finding F-T1 exposed it as load-bearing and nodeless
      (recorded rule-8b breach); unformalized — this is why `thm:pair-tensor` is NARROWER. M1
      edge-typing left to the composition-layer review. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.FILT.yaml.
    - **B4bL2JointLP tool [CONJECTURED · pending-review · related/non-propagating · LATE
      REGISTRATION]** — `prop:joint-lp`, exact finite joint-histogram separation. The only
      §proof-search statement whose proof delegates wholesale to an ancillary script; exact optima
      lack printed dual certificates. Registered 2026-07-30 (F-T1). Adjudication owed: whether the
      2026-07-19 L2-phase-1 review's "24 finite rational LP optima" are these objects (rule 7d).
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.JOINTLP.yaml.
    - **B4bL2G1 obstruction [PROVED · related/non-propagating]** — Multiplicity gauge makes
      terminal H-irrep labels insufficient; a GT/Jucys–Murphy chain does not resolve the copy
      space. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.G1.yaml; report/review:
      artifacts/ksum_L2_phase6.md, artifacts/ksum_L2p6_review.md.
    - **B4bL2G2 obstruction [PROVED · related/non-propagating]** — Full Reynolds averaging
      kills a direct vector from every nontrivial H-satellite. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.G2.yaml; report/review:
      artifacts/ksum_L2_phase6.md, artifacts/ksum_L2p6_review.md.
    - **B4bL2G3 obstruction [PROVED · related/non-propagating]** — Every nonzero PSD
      `Reynolds(diag A)/tr A` transfer has constant moment one and band zero. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.G3.yaml; report/review:
      artifacts/ksum_L2_phase6.md, artifacts/ksum_L2p6_review.md.
    - **B4bL2L2P6G obstruction [CONJECTURED · related/non-propagating]** — Aggregate
      optimizer-faithful transfer obstruction; D14 leaves the class undefined and the displayed
      maps nonexhaustive. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.L2P6G.yaml;
      report/review: artifacts/ksum_L2_phase6.md, artifacts/ksum_L2p6_review.md.
    - **B4bL2P2Ansatz proof [OPEN · PARKED · related/non-propagating]** — Pure sign-separated
      tensor ansatz is BLOCKED at proposer tier by M2's correlation formula; it is not REFUTED.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.P2ANSATZ.yaml; report/review:
      artifacts/ksum_L2_phase2.md, artifacts/ksum_L2p2_review.md.
    - **B4bL2AltFewpair proof [OPEN · related/non-propagating]** — Few-pair mixture;
      phase-3 stop-rule fired at the tilted-product mechanism before this was attempted. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.fewpair.yaml; cite:
      artifacts/ksum_L2_phase3.md.
    - **B4bL2AltBkt proof [OPEN · related/non-propagating]** — BKT-style active-pair outer
      dual; not attempted, with an on-disk dual-composition theorem gap. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.bkt.yaml; cite:
      artifacts/ksum_L2_phase3.md.
    - **B4bL2AltNonidentical proof [OPEN · related/non-propagating]** — Nonidentical and/or
      unequal-total blocks lie outside ORIENT and remain unexamined. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.nonidentical.yaml; cite:
      artifacts/ksum_L2p5_review.md.
    - **B4bL2AltNonproduct proof [OPEN · related/non-propagating]** — Non-product signed block
      couplings remain unexamined outside the proved product-outer classes. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.nonproduct.yaml; cites:
      artifacts/ksum_L2p5_review.md, artifacts/ksum_L2p6_review.md.
      - **B4bL2AltNonproductProfileLatticeCore proof [OPEN · β1 identities rule-7 REVIEWED 2026-07-23: C1/C2/C4 PROVED-scoped, C3 NUMERICAL · related/non-propagating]** —
        Review (no MAJOR/GAP): C2 extended to q=17 with an independent closed form; C4
        re-verified with the reviewer's own moment map (residual exactly 0); C1 re-grounded on
        exact moment-row-space (kernel) invariance and relabeled ("two one-sided pairs, f=0"),
        verified through q=11; C3 ruled a finite observation (D_crit/sqrt(N) wobbles 0.75-1.0),
        not a cap theorem. Review: artifacts/ksum_beta1_obstruction_identities_rule7_review_20260723.md.
        Pre-review record:
        β0 verified all four literature inputs and extracted the sum-with-shared-bad-orbit
        cancellation card (8 sigma-twist rework points). β1 (outcome class B): K2 CONTAINS —
        the proved q=5 shared-NO germ is an exactly-feasible LP point (moment residual 0,
        corr > 2/3 to N=20003); K1 kill did not fire but the written ansatz has NO q-gain —
        <=2-active-pair support exactly q-independent, product activation pays exactly M2's
        2^(1-(q-1)/2), q=5 critical degree Theta(sqrt(N)); K4 passes (non-factorizing).
        First positive q-trend: super-threshold full-orbit ceiling 0.533<0.587<0.618 for
        q=5/7/9 (N=8,D=5), decelerating, G11-capped. Live frontier: >=3-active-pair
        non-product region where no coefficient law exists (same object as L3's M7). Cites:
        artifacts/ksum_beta0_litverify_mechanism_card_20260723.md,
        artifacts/ksum_beta1_profile_lattice_ansatz_q5_20260723.md. Canonical:
        research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.nonproduct.profile-lattice-core.yaml.
    - **B4bL2AltCanonbasis proof [OPEN · related/non-propagating]** — A genuinely signed map in
      an ambient canonical multiplicity/branching basis remains a D14-unexcluded door, but the
      natural center/JM implementation now fails proposer-tier `CB-1`/`CB-4` gates. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.canonbasis.yaml; cite:
      artifacts/ksum_L2p6_review.md, artifacts/ksum_L2_phase7_web_feasibility_20260720.md.
    - **B4bL2AltAltinner proof [OPEN · related/non-propagating]** — Alternative inner kernels
      were named in the obligations and remain unexamined. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.altinner.yaml; cite:
      artifacts/ksum_L2_phase4.md.
    - **B4bL2AltTworay obstruction [CONJECTURED · pending-review · related/non-propagating]**
      — Common-bad-profile two-ray cancellation gives an explicit constant-correlation logarithmic
      band; a proposer Chebyshev argument caps the whole support class at `O_tau(sqrt(N))`.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.tworay.yaml; cite:
      artifacts/ksum_L2_phase7_web_feasibility_20260720.md.
    - **B4bL2AltMultipair obstruction [CONJECTURED · pending-review · related/non-propagating]**
      — The one-defect multi-pair support has `C_t<=N-1`; a proposer Chebyshev argument gives an
      `O_tau(sqrt(N))` ceiling for arbitrary coefficients. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.yaml; cite:
      artifacts/ksum_L2_phase8_multipair_web_feasibility_20260720.md.
    - **B4bL2AltMultipairHighCtBalanced obstruction [CONJECTURED · pending-review · related/non-propagating]**
      — A single-dyadic-scale balanced split family reaches `C_t=Theta(N^(4/3))`, but
      `M_F/g_F=O(N)` yields a proposer `O_tau(sqrt(N))` support ceiling. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.highCt-balanced.yaml; cite:
      artifacts/ksum_L2_phase9_highCt_balanced_web_feasibility_20260721.md.
    - **B4bL2AltMultipairMultiscaleSplits obstruction [CONJECTURED · pending-review · related/non-propagating]** —
      Fixed low-complexity pair-total scales can be isolated by low-degree interpolation; the target
      reduces to an OR of per-scale thresholds and is `o(N^(2/3))` for geometric ladders. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.multiscale-splits.yaml; cite:
      artifacts/ksum_L2_phase10_multiscale_splits_web_feasibility_20260721.md.
    - **B4bL2AltMultipairVariablePairTotals proof [OPEN · related/non-propagating]** —
      Exact target-scale finite sweeps survive at `q=5`, while several bounded natural kernel
      classes fail scoped gates; the uniform asymptotic kernel remains missing. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.yaml; cite:
      artifacts/ksum_L2_phase14_target_scale_sweep_20260721.md.
    - **B4bL2AltMultipairGrowingRankMomentDesign obstruction [CONJECTURED · pending-review · related/non-propagating]** —
      A faithful determinant/OA family gives exact low-degree cancellation, but over-annihilates
      coordinate cylinders, loses constant correlation, and cannot meet the `q=5` band. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.growing-rank-moment-design.yaml; cite:
      artifacts/ksum_L2_phase15_growing_rank_moment_design_20260721.md.
    - **B4bL2AltMultipairSelectiveOrbitTensorKernel proof [OPEN · related/non-propagating]** —
      Weighted projection gives an exact selective annihilator normal form and explicit
      correlation/tail inequalities, but a formula-defined base measure remains equivalent to the
      original missing dual. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.yaml;
      cite: artifacts/ksum_L2_phase16_selective_orbit_tensor_kernel_20260721.md.
    - **B4bL2AltMultipairMovingRemezCubature proof [OPEN · related/non-propagating]** —
      Exact `q=5` optima use moving rank-plus-one supports; the registered analytic ansatz seeks a
      support formula, cofactor bounds, and global equioscillation certificate. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.yaml;
      cite: artifacts/ksum_L2_phase16_q5_selective_structure_20260721.md.
    - **B4bL2AltMultipairMultiscaleGapfreeBaseMeasure proof [OPEN · related/non-propagating]** —
      Registered escape seeking residual-relevant small positive `C_t` scales together with a
      constant `Theta(N^(4/3))` tail, so no low-degree scalar gap separates NO. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.multiscale-gapfree-base-measure.yaml;
      cite: artifacts/ksum_L2_phase18_qN_multidimensional_pi_20260721.md.
    - **B4bL2AltMultipairLabelAwareFeketeBasisExchange proof [OPEN · related/non-propagating]** —
      Registered escape replacing the failed lexicographic near-boundary basis by deterministic
      joint boundary/interior Fekete or basis-exchange selection. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.label-aware-fekete-basis-exchange.yaml;
      cite: artifacts/ksum_L2_phase19_moving_remez_cubature_20260721.md.
    - **B4bL2AltMultipairContinuationSeededBlockFekete proof [OPEN · related/non-propagating]** —
      Registered escape transporting supports between neighboring `(N,D)` points and using
      coordinated multi-column exchange rather than restarted single-entry local search. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.label-aware-fekete-basis-exchange.continuation-seeded-block-fekete.yaml;
      cite: artifacts/ksum_L2_phase20_label_aware_fekete_basis_exchange_20260721.md.
    - **B4bL2AltMultipairCriticalDensePaletteResidualWindow proof [OPEN · related/non-propagating]** —
      The Phase-21 critical mixture blocks all known little-`o` separators; direct full-orbit
      residual analysis remains open for `0<c<(arcosh 3)/2`. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.multiscale-gapfree-base-measure.critical-dense-palette-residual-window.yaml;
      cite: artifacts/ksum_L2_phase21_critical_dense_palette_20260721.md.
    - **B4bL2AltMultipairContinuumRemezSupportFlow proof [OPEN · related/non-propagating]** —
      Registered analytic escape deriving a scaled support flow and equioscillation equations
      before lattice rounding, instead of widening finite support search toward the LP. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.label-aware-fekete-basis-exchange.continuation-seeded-block-fekete.continuum-limit-remez-support-flow.yaml;
      cite: artifacts/ksum_L2_phase21_continuation_seeded_block_fekete_20260721.md.
    - **B4bL2AltMultipairStratifiedBoundaryJetRemez proof [OPEN · related/non-propagating]** —
      Registered after Phase 23 proved the ordinary continuum density singular. The candidate must
      couple bulk, `xi=D^2 C_t/N^2` normal layer, NO face, and discrete corner jets with exact
      kernels, matching, and degree-jump birth laws. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multipair.variable-pair-totals.selective-orbit-tensor-kernel.moving-remez-cubature.label-aware-fekete-basis-exchange.continuation-seeded-block-fekete.continuum-limit-remez-support-flow.stratified-boundary-jet-remez-system.yaml;
      cite: artifacts/ksum_L2_phase23_continuum_remez_support_flow_20260721.md.
    - **B4bL2AltMultipairMesoscopicSplitOpeningCascade proof [OPEN · related/non-propagating]** —
      Registered during Phase 24 before testing. It asks whether intermediate slot-total scales can
      transfer `C_t=O(1)` corner cancellation to the `C_t=Theta(N)` normal layer with bounded total
      variation. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.mesoscopic-split-opening-cascade.yaml.
    - **B4bL2AltIteratedMultiscaleBoundaryCompactification proof [OPEN · related/non-propagating]** —
      Registered during Phase 24 before testing. It seeks a regime-complete compactification of all
      intermediate `C_t` scales plus a uniformly stable exact moment corrector. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.iterated-multiscale-boundary-compactification.yaml;
      cite: artifacts/ksum_L2_phase24_stratified_feasibility_20260721.md.
    - **B4bL2AltMesoscopicMinorityOccupancyTransition proof [OPEN · related/non-propagating]** —
      Registered during Phase 24 before testing. It asks for exact transition kernels from fixed
      minority occupancy through `m=Theta(D)` to bulk, because scalar `xi` loses orbit information.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.mesoscopic-minority-occupancy-transition.yaml;
      cite: artifacts/ksum_L2_phase24_stratified_normal_kernel_20260721.md.
    - **B4bL2AltTangentialPhasePairedTransport proof [OPEN · related/non-propagating]** —
      Registered during Phase 25 before testing. It asks for a global pairing of exposed tangential
      WKB phases and a uniformly bounded right inverse through the exact `m=b+O(1)` birth edge.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.tangential-phase-paired-transport.yaml;
      cite: artifacts/ksum_L2_phase25_mesoscopic_minority_transition_20260721.md.
    - **B4bL2AltTwoOrientationSharedNoCascade proof [PROVED · Rule-7 reviewed · related/non-propagating]** —
      Complementary orientations share one NO orbit. The explicit smaller-constant `q=5`
      construction has exact annihilation, correlation above `2/3`, and tail `1/4`; fresh Rule-7
      MINOR/PASS independently verifies all displays and quantifiers.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.two-orientation-shared-no-cascade.yaml.
    - **B4bL2AltPhaseSubexposedCorrelationReservoir proof [OPEN · related/non-propagating]** —
      Registered during Phase 26 before testing. It moves signed correlation mass off all exposed
      positive-minority WKB phases to avoid the exponentially ill-conditioned birth inverse.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.phase-subexposed-correlation-reservoir.yaml;
      cite: artifacts/ksum_L2_phase26_tangential_phase_paired_transport_20260721.md.
    - **B4bL2AltCorrelationTailDecoupledTwoReservoir proof [OPEN · related/non-propagating]** —
      Registered during Phase 27 before testing. It separates the `O(N)` correlation bridge from a
      correlation-neutral `omega(N)` tail reservoir and leaves only cross moments to cancel.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.correlation-tail-decoupled-two-reservoir.yaml;
      cite: artifacts/ksum_L2_phase27_phase_subexposed_reservoir_20260721.md.
    - **B4bL2AltMultiscaleMomentBearingNeutralLadder proof [OPEN · related/non-propagating]** —
      Registered during Phase 28 before testing. It seeks local moment transport from an `O(N)`
      bridge to an `N^(4/3)` neutral tail, avoiding separated-scale extrapolation.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.multiscale-moment-bearing-neutral-ladder.yaml;
      cite: artifacts/ksum_L2_phase28_qN_two_reservoir_construction_20260721.md.
    - **B4bL2AltNearZeroBridgeIndependentParityTail proof [OPEN · related/non-propagating]** —
      The explicit bridge has exact low moments, parity tail, and now analytically proved
      `Z_D>0`, but a different legal global scalar selector uses the activation low tail and proves
      its normalized correlation is `o(1)`. This scoped-kills the displayed `pi_N` projection law,
      not every near-zero bridge.
      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.near-zero-bridge-independent-parity-tail.yaml;
      cite: artifacts/ksum_L2_phase30_activation_tail_chebyshev_selector_20260722.md.
      - **B4bL2AltWeightedActivationOrDualComposition proof [REFUTED · DEAD · related/non-propagating]** —
        Fresh Rule-7 review confirms the dense-composition obstruction for every coefficient law: its
        global target count lies in `[1,N-L]` on YES, so a legal subcutoff Chebyshev row forces
        correlation `o(1)`. Balanced positive-split supports are outside this dead node's scope.
        Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.weighted-activation-or-dual-composition.yaml.
        - **B4bL2AltBalancedPositiveSplitWeightedDualComposition [REFUTED · DEAD · related/non-propagating]** -
          On the exact Phase-30 nearly-equal support, constant-degree interpolation separates unit
          activation `A` from bulk target count `G`; two anchored Chebyshev factors form an actual
          weight-`<D` row that is one on NO and `o(1)` on every YES regime. Fresh Rule-7 review
          independently passes and kills this exact support. Other balanced supports and the
          balanced/dense mixture are outside scope. Canonical:
          research/ksum/proof-dag/nodes/KSUM.B4b.L2.ALT.balanced-positive-split-weighted-dual-composition.yaml.
  - **B4bL3 [OPEN · pending-review]** — Correlated-composition route beyond independent
    pSearch. Unequal-domain/bucket/depth tuning is exhausted at the `q^(1/6)` theorem template, and
    the first shared-address gadget is closed by a transposed OR-of-claws algorithm. Fixed relabels
    themselves remain a lossless transfer layer, so the route is still open for a genuinely global
    donor with no searchable latent coordinate. Canonical:
    research/ksum/proof-dag/nodes/KSUM.B4b.L3.yaml; cites:
    artifacts/ksum_L3_asymmetric_claw_parameter_audit_20260721.md,
    artifacts/ksum_L3_correlated_gadget_attempt_20260721.md,
    artifacts/ksum_L3_fixed_relabel_ceiling_20260721.md.
    - **B4bL3AltHiddenFrequencyMask proof [OPEN · related/non-propagating]** — The exact
      balanced single-scale promise and lossless embedding are frozen, but a proposer-tier
      `O-tilde(q+sqrt(N)q^(1/6))` algorithm makes it subtarget throughout every strictly
      subcritical polynomial range. The `q=Theta(N^(2/3))` endpoint remains unresolved; no
      completion-tier refutation is claimed. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.yaml; cites:
      artifacts/ksum_L3_hidden_frequency_promise_20260721.md,
      artifacts/ksum_L3_hidden_frequency_upper_attack_20260721.md, and
      artifacts/ksum_L3_hidden_frequency_donor_audit_20260721.md.
    - **B4bL3AltHiddenFrequencyMaskCriticalEndpoint proof [OPEN · related/non-propagating]** —
      Exact critical `q=Theta(N^(2/3))` hidden-palette problem. An addressed
      `UIC o pSearch` subfunction gives `Omega(N^(11/18))`; three non-sampling attack families find
      no subcap algorithm, and the missing `N^(1/18)` is now two explicit lower-route inequalities.
      Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.yaml;
      cites: artifacts/ksum_L3_hidden_frequency_critical_adversary_attempt_20260721.md,
      artifacts/ksum_L3_critical_nonsampling_upper_attacks_20260721.md, and
      artifacts/ksum_L3_critical_orbit_intertwiner_attempt_20260721.md.
      - **CriticalDuplicateClassification [OPEN · related/non-propagating]** — Coherent
        singleton/heavy duplicate classification audit; best scoped cost `O-tilde(N^(5/6))`, so no
        subcap attack was found. Canonical:
        research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.duplicate-classification.yaml.
      - **CriticalFrequencyAwareJointWalk [OPEN · related/non-propagating]** — Frequency-conditioned
        soft-filter walk; exact optimization chooses zero filtering and ordinary
        `Theta(N^(2/3))` Johnson. Canonical:
        research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.frequency-aware-joint-walk.yaml.
      - **CriticalJointStatisticEstimation [OPEN · related/non-propagating]** — Estimate the unit
        joint-histogram/support/collision change; best direct scoped cost
        `O-tilde(N^(5/6))`. Canonical:
        research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.joint-statistic-estimation.yaml.
      - **CriticalOrbitIntertwinerAdversary [OPEN · related/non-propagating]** — Formula-defined
        double-coset system is exact; local collision split gives `Theta(N^(1/3))`, addressed
        blocks give `N^(11/18)`, standalone square cycles have a constant ceiling, and the
        rectangular coupled kernel remains open. Canonical:
        research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.yaml.
        - **CriticalSignedCycleWeightLaw [REFUTED · DEAD · related/non-propagating]** — Rule-8-
          registered standalone square formula family on alternating hidden-address cycles; its
          exact universal constant ceiling on a legal infinite sequence passes fresh Rule 7(a)–(g)
          review. This status does not propagate to the rectangular coupled node. Canonical:
          research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.signed-cycle-weight-law.yaml.
        - **CriticalCoupledUicAddressCycleKernel [OPEN · related/non-propagating]** — Rectangular
          incidence normalization is exact; every one/two-endpoint selector, the fixed `P/Q`
          algebra, multiplicity-one repaired-full-matching transport, and the first hidden-selector-
          star law are capped at the addressed scale. Genuine LR multiplicity exists but fixed-
          middle mixing fails; natural two-matching words reduce to Hecke plus two endpoints. The
          pair-defined full-position three-layer successor remains open.
          Canonical:
          research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel.yaml.
          - **CriticalCoupledGrowingSelectorSpechtBranchingKernel [OPEN · related/non-propagating]**
            — The true repaired full matching contains a growing common Specht sector, but its
            multiplicity-one transport is unitary-equivalent to the base and marking gives `I_r`.
            Fixed-middle LR mixing and natural two-matching words also fail; the node remains OPEN
            only through the full-position three-layer successor. Canonical:
            research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel.ALT.growing-selector-specht-branching-kernel.yaml.
            - **CriticalCoupledLrMultiplicitySpaceMixing [OPEN · related/non-propagating]** — The
              exact family has genuine LR multiplicity `c=r+1`, but every fixed middle operator
              obeys a marked-branch convexity ceiling and gains nothing. Pair-dependent laws lie
              outside this scoped audit. Canonical:
              research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel.ALT.growing-selector-specht-branching-kernel.ALT.lr-multiplicity-space-mixing.yaml.
            - **CriticalCoupledNonfactorizableCycleWordSelector [OPEN · related/non-propagating]** —
              Every natural word in the repaired-singleton/heavy two-matching graph reduces to a
              standalone convolution/Hecke kernel plus at most two capped endpoints. Canonical:
              research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel.ALT.growing-selector-specht-branching-kernel.ALT.nonfactorizable-cycle-word-selector.yaml.
              - **CriticalCoupledFullPositionIncidenceThreeLayerWordKernel [OPEN · related/non-propagating]** —
                The exact new data are two joint transportation matrices and strictly exceed the
                old address maps, but arbitrary laws fill the whole Young-Hecke corner. Raw/fixed-
                centered contingency minors are fixed-middle and fail by marked-branch convexity.
                Only off-equality noncommuting parent mixing remains live. Canonical:
                research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.full-position-incidence-three-layer-word-kernel.yaml.
                - **CriticalNoncommutingParentMixingKernel [OPEN · related/non-propagating]** —
                  Two explicit `r x r` parent grids fail through unique near-unit heavy-
                  unselected predecessors. The target-sized shared-patch repair also fails in the
                  singleton/Pieri cone; same-parent and non-skeleton successors remain open.
                  Canonical:
                  research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.noncommuting-parent-mixing-kernel.yaml.
                  - **CriticalSharedBranchYoungLatticePatchKernel [OPEN · related/non-propagating]** —
                    Every finite support has a degree-at-most-two lower boundary; first-row deletion
                    is an injective almost-unit pivot throughout the singleton/Pieri cone. No exact
                    harmonic exists there and every `o(m)` patch retains `1-o(1)` down norm. Fresh
                    Rule-7 review passes this scalar subroute after local type corrections; the
                    broader construction node remains OPEN.
                    Canonical:
                    research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.shared-branch-young-lattice-patch-kernel.yaml.
                    - **CriticalMacroscopicParentPatchKernel [OPEN · related/non-propagating]** —
                      The first explicit `Theta(m)` adjacent two-row chain is near-isometric; its
                      exact cancelling vector is exponentially unbalanced and both physical maps
                      retain `1-o(1)` in the corrected common-auxiliary interior. Fresh Rule-7
                      review is PARTIAL because of endpoint, definition, scope, and frozen-SHA
                      defects; non-adjacent and non-two-row macroscopic supports remain open.
                      Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.macroscopic-parent-patch-kernel.yaml.
                      - **CriticalFullYoungRankBalancedHarmonicKernel [OPEN · related/non-propagating]** —
                        The scalar Young-down kernel is nonphysical because literal restriction
                        preserves orthogonal parent tags. Fresh Rule-7 review independently confirms
                        the stronger `1-1/q` left/right retention on the complete trivial-alphabet
                        sector, while correcting the proposer's illegal endpoint sequence to
                        `a=k^2,d=4k-1`; verdict PARTIAL and nontrivial alphabet/pair incidence remain
                        open. Canonical:
                        research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.full-young-rank-balanced-harmonic-kernel.yaml.
                    - **CriticalNonSkeletonHeavyOccurrenceCarrier [OPEN · related/non-propagating]** —
                      The exact odd-`d` sign/rectangle carrier exists, but after both global
                      predecessor branches are included its raw equality pinching is `O(1/a)` and
                      both physical queries retain `1-o(1)`. Fresh Rule-7 review is PARTIAL: the
                      corrected effect/polar/sandwich conclusion survives but two printed type
                      identities fail; other plethystic/occurrence carriers remain open. Canonical:
                      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.non-skeleton-heavy-occurrence-carrier.yaml.
                      - **CriticalNonScaledPlethysticManyCornerOccurrenceKernel [OPEN · related/non-propagating]** —
                        The exact three-row family `theta_r=(ad-r-1,r,1)` occurs in `h_a[h_d]`
                        with growing coefficient `p(r)+p(r-1)-p(r+1)`, but its all-top
                        trivial-alphabet carrier retains `1-o(1)` on both physical sides. The
                        shifted-staircase many-corner subcandidate retains a constant heavy branch.
                        Fresh review is PARTIAL: it independently confirms those scoped values but
                        repairs an ill-typed `c>1` tensor formula to the composition `A F_z`.
                        Block-standard covariance is a registered successor.
                        Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.non-scaled-plethystic-many-corner-occurrence-kernel.yaml.
                        - **CriticalThreeRowBlockStandardCovariantOccurrenceKernel [OPEN · related/non-propagating]** —
                          The exact coefficient is
                          `[s_(ad-r-1,r,1)]s_(a-1,1)[h_d]=sum_(j=0)^(r-2)p(j)`, so the common
                          covariant Hom-space grows rapidly on the legal endpoint. In the complete
                          single-cell realization, however, the opposite query acts as the identity
                          on this occurrence index and retains `1-o(1)` of every matrix. This is a
                          fresh Rule-7 PARTIAL scoped failure. The review confirms the real `r>=4`
                          critical family but finds the formal `C_r=1` physical regime infeasible
                          and narrows the matrix/type quantifiers. The registered bicovariant
                          two-box alphabet successor remains outside it.
                          Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-block-standard-covariant-occurrence-kernel.yaml.
                          - **CriticalThreeRowBicovariantTwoCellAlphabetKernel [REFUTED · DEAD · related/non-propagating]** —
                            A true `Std(H_L) tensor Std(H_R)` occurs once in either `(q-2,2)` or
                            `(q-2,1,1)` and gives `C_r^2` common NO/YES channels. It does not reduce
                            to the DEAD one-box direct sum. For each fixed global irrep, however,
                            every point effect is at most `I/2`. Fresh independent Rule-7 review
                            verifies all operator types, multiplicity regimes, and rectangular
                            coefficient laws, forcing `1/2-o(1)` query retention on both sides.
                            The mixed-full-type successor remains outside this scoped refutation.
                            Canonical:
                            research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-bicovariant-two-cell-alphabet-kernel.yaml.
                            - **CriticalThreeRowMixedTwoBoxFullTypeRecouplingKernel [REFUTED · DEAD · related/non-propagating]** —
                              Separate legal unmarked blocks do meet in the common point type, but
                              the physical cell projection leaves weight `1/(2a)` per carrier and
                              the summed cross-type outputs vanish. Fresh independent Rule-7 review
                              verifies the complete typed obstruction and gives `1-o(1)` retention
                              on both sides for arbitrary legal multipliers. This kills only the
                              exact `nu_+ direct-sum nu_-` two-box construction; the complete
                              induced packet remains OPEN. Review SHA-256
                              `0D6AA6C0AFE42716A9DBC4F0D85D0E2FC9722998432A7C1AA032B445E5F79506`.
                              Review artifact:
                              artifacts/ksum_L3_critical_three_row_mixed_two_box_full_type_recoupling_rule7_review_20260722.md.
                              Canonical:
                              research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-mixed-two-box-full-type-recoupling-kernel.yaml.
                              - **CriticalThreeRowInducedBicovariantAlphabetPacketKernel [OPEN · first gate fresh-reviewed · related/non-propagating]** —
                                The complete packet embeds physically and has full marked mass.
                                Fresh Rule-7 MINOR/SCOPED PASS verifies the all-multiplicity
                                isometry, Johnson cross-Gram, width/multiplicity bounds, and
                                `1/a+(a-1)/a` effects on `p=0,u=1,q=4a`. The total marked mass is
                                not a uniform orientation-average bound: `(J_L+J_R)/2` has Gram
                                `(I+K)/2`. Scalar Johnson-degree
                                laws lie in the support-quotiented UIC architecture, so the broad
                                query/numerator claim remains OPEN and the occurrence-pencil
                                classification is now the active prerequisite. Review SHA-256
                                `CF1E853AE7BEBC689963409A03D19BBA96684AF0C4BBAF4ED59155E2F64741F2`.
                                Canonical:
                                research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.three-row-induced-bicovariant-alphabet-packet-kernel.yaml.
                                - **CriticalInducedPacketYoungHolonomyLaw [OPEN · related/non-propagating]** —
                                  Matrix-valued transport on actual packet branching diamonds;
                                  registered before connection, holonomy, or query calculations and
                                  queued behind the scalar-orientation gate. Canonical:
                                  research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-young-holonomy-law.yaml.
                                  - **CriticalInducedPacketJointParentContentKernel [OPEN · related/non-propagating]** —
                                  A genuinely nonseparable law of both restriction parents,
                                  contents, and occurrence indices. The aggregate cross-side algebra
                                  is commuting. Separate finite factors are now reviewed at `s=4`
                                  and `a=16`; their finite NO/fixed-same-mark physical assembly now
                                  has a scoped pass and retains an `M_3` core. Uniform/YES transfer
                                  and every query calculation remain open. Canonical:
                                  research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-joint-parent-content-kernel.yaml.
                                    - **CriticalInducedPacketOccurrencePencilClassification [OPEN · related/non-propagating]** —
                                    The finite `s=4` occurrence factor receives PASS / STRICTLY
                                    SCOPED PASS and generates `M_1(Q) direct-sum M_3(Q)`. The finite
                                    `a=16` NO/same-mark alphabet factor receives MINOR / SCOPED PASS,
                                    forms `C^6`, and has nonzero cross-parent blocks. Earlier reviews
                                    also bank complete-source typing and the direct-coset product
                                    theorem, so aggregate cross-side effects and native transfers
                                    commute. The finite NO/fixed-same-mark physical assembly now
                                    has a scoped pass, while YES, distinct marks, uniformity, spectra,
                                    feasibility, attenuation, numerator, and asymptotics remain open.
                                    Canonical:
                                    research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-occurrence-pencil-classification.yaml.
                                    - **CriticalInducedPacketTotalEnergyResolventLaw [OPEN · deprioritized · related/non-propagating]** —
                                      Test `b_(j,h,k)=1/(epsilon+mu_j+ell_h+r_k)` only after the
                                      pencil gate. Despite possible tensor rank greater than one,
                                      it may collapse to forbidden one-dimensional total energy;
                                      no test has run. Canonical:
                                      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-total-energy-resolvent-law.yaml.
                                    - **CriticalInducedPacketNoncommutingSylvesterLaw [REFUTED · DEAD · related/non-propagating]** —
                                      The registered native cross-side premise is false: the complete
                                      aggregate left/right effects and native `E_L,E_R` commute and
                                      are simultaneously unitarily diagonalizable. Same-side,
                                      different-`z`, and pullback questions are outside this leaf.
                                      Canonical:
                                      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-noncommuting-sylvester-law.yaml.
                                    - **CriticalInducedPacketRectangularTransferResolventLaw [OPEN · related/non-propagating]** —
                                      Fresh scoped review banks `Hom_(S_q)` closure for the fixed
                                      invariant candidate and removes only its nontrivial alphabet-
                                      Wigner complement. The `19456` slice is not norm-complete;
                                      private children, active position branches, restricted spectrum,
                                      taper, physical query norm, and numerator remain open. The
                                      private-child run ended without a final output during fast close.
                                      Canonical:
                                      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-rectangular-transfer-resolvent-law.yaml.
                                      - **CriticalLiteralMarkedQueryPolarNormInterface [OPEN · related/non-propagating]** —
                                        Type the literal marked rows and polar ranges and control the
                                        actual masked operator norm; compression alone is insufficient.
                                        Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.literal-marked-query-polar-norm-interface.yaml.
                                        - **CriticalPolarOffdiagonalBlockLaw [OPEN · prioritized · related/non-propagating]** —
                                          Exact off-diagonal raw-value polar block reduction; no proof
                                          or finite gate started. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.polar-offdiagonal-block-law.yaml.
                                        - **CriticalPhysicalRangeReducingEqualityLaw [OPEN · deprioritized · related/non-propagating]** —
                                          Packet-specific exceptional condition that could equate literal
                                          and compressed norms despite the generic counterexample.
                                          Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.physical-range-reducing-equality-law.yaml.
                                        - **CriticalHsQueryEnergyLaw [REFUTED · DEAD · rule-7 review CONFIRMING 2026-07-23 · related/non-propagating]** —
                                          Kill confirmed and scoped to the HS-energy-only route (siblings
                                          expressly preserved); reviewer repaired the sign-rep gap via
                                          Young's rule and re-derived all hook dimensions two independent
                                          ways. Review: artifacts/ksum_L3_hs_loss_rule7_review_20260723.md.
                                          Original G1 finding:
                                          Loss quantified 2026-07-23: `L >= sqrt(f^lambda f^mu)`,
                                          dominant growth `q^alpha` with `alpha >= 3/4` (>= 2 for the
                                          pure energy route) vs budget `1/12`; mechanism is position-
                                          symmetry breaking by `Delta_i` (position carriers do not
                                          cancel; position-trivial adversaries capped separately). The
                                          literal masked-query HS identity is absent from disk; the two
                                          documented strict gaps only add loss. Kill criterion fires at
                                          proposer tier; REFUTED/DEAD awaits rule-7 review. Cite:
                                          artifacts/ksum_L3_hs_loss_quantification_20260723.md. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.hs-query-energy-law.yaml.
                                      - **CriticalInducedPacketOuterIncidenceNumeratorInterface [OPEN · related/non-propagating]** —
                                        Define the exact normalized physical numerator readout; equivariance
                                        alone does not determine it. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-outer-incidence-numerator-interface.yaml.
                                      - **CriticalInducedPacketPayloadValueTest [NUMERICAL · pending-review · gate G2 · related/non-propagating]** —
                                        Executed 2026-07-23: NOT ASSEMBLABLE at a=16,q=64 — seven
                                        file-level missing pieces (four private point-children tables,
                                        Omega_tau unevaluated, K_s unassembled, polar/range norm
                                        interface unfixed with exact 1/4-vs-1/2 guard, outer numerator
                                        undefined, 19456 slice not norm-complete, no coefficient law:
                                        scalar collapses to the N^(11/18) baseline). Finite diagnostic
                                        only (G11); not a refutation. Cite:
                                        artifacts/ksum_L3_payload_value_test_a16_20260723.md. Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-payload-value-test.yaml.
                                - **CriticalInducedPacketPlaquetteFlowLaw [OPEN · related/non-propagating]** —
                                  A matrix-valued divergence-free circulation on physical packet
                                  plaquettes; registered before graph, flow, or query calculations.
                                  Canonical:
                                  research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.induced-packet-plaquette-flow-law.yaml.
              - **CriticalGloballyBoundedSymmetrizedPolynomialLowerBound [OPEN · related/non-propagating]** —
                Seek an `Omega(N^(2/3))` globally bounded acceptance-polynomial degree lower bound
                through off-promise two-parameter interpolation. Promise-only approximate degree
                is inapplicable because cross-collision count is a degree-two exact separator.
                Registered before work and deprioritized behind the occurrence route. Canonical:
                research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.globally-bounded-symmetrized-polynomial-lower-bound.yaml.
                  - **CriticalSameParentOccurrenceMultiplicityMixingKernel [OPEN · related/non-propagating]** —
                    A genuine growing block-partition occurrence space exists in both answers, but
                    the first `nu=(q)` family is near-isometric under both physical queries for
                    every coefficient matrix. Canonical:
                    research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.same-parent-occurrence-multiplicity-mixing-kernel.yaml.
                    - **CriticalNontrivialAlphabetOccurrenceMixingKernel [OPEN · related/non-propagating]** —
                      The standard hook has growing common multiplicity, but its minimal separately
                      invariant Foulkes × type-cell product has pinching `O(1/q)` and both physical
                      queries retain `1-o(1)` for every coefficient matrix. Canonical:
                      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.nontrivial-alphabet-occurrence-mixing-kernel.yaml.
                      - **CriticalCovariantBlockStandardOccurrenceMixingKernel [OPEN · related/non-propagating]** —
                        Couple a heavy-cell alphabet `Std_a` diagonally to the position block-
                        permutation `Std_a` covariant space. Its exact multiplicity grows and the
                        common NO/YES embedding exists, but every one-cell sector has an opposite-
                        side query branch retained by `1-o(1)` for arbitrary internal matrices.
                        Canonical: research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.covariant-block-standard-occurrence-mixing-kernel.yaml.
                        - **CriticalTwoCellCovariantCrossSectorMixingKernel [REFUTED · DEAD · related/non-propagating]** —
                          Include both `L_d` and `R_d` covariant sectors and mix them crosswise so
                          neither physical side sees only a disjoint-cell retained branch. The full
                          frame is block diagonal, however, and a proposer-tier maximal-block bound
                          makes one query retain `1/2-o(1)` of every matrix; fresh Rule-7 review
                          passes after restoring the literal polar-lifted restriction maps. Canonical:
                          research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.two-cell-covariant-cross-sector-mixing-kernel.yaml.
          - **CriticalCoupledDelocalizedMultiblockOccurrenceKernel [OPEN · related/non-propagating]**
            — The first hidden-selector-star law at `r=Theta(m^(1/3))` collapses after incidence to
            the `P/Q` ceiling, and disjoint grouping loses outer scale. A genuinely post-incidence
            non-`P/Q`, outer-pair-dependent overlap remains open.
            Canonical:
            research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.orbit-intertwiner-adversary.ALT.coupled-uic-address-cycle-kernel.ALT.delocalized-multiblock-occurrence-kernel.yaml.
      - **CriticalStrictInjectionRecordingQuery [REFUTED/DEAD · related/non-propagating]** — Fresh
        Rule 7(a)–(g) PASS: degree-two through degree-nine witnesses refute the exact ambient
        low-degree certificate-support projector architecture. Parent endpoint, quotient route,
        and nonlinear reachability successor remain OPEN. Canonical:
        research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.strict-injection-recording-query.yaml.
        - **CriticalPromiseIdealQuotientAdversary [OPEN · related/non-propagating]** — Exact
          proposer-tier audits kill quotient-only inherited transfer and every exact query-module
          Hom: the disjoint answer spectra give a zero Hom space, and degree-two equality projectors
          already resolve the YES identity. Only a general nonintertwining masked adversary remains;
          fresh review is pending. Canonical:
          research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.promise-ideal-quotient-adversary.yaml.
        - **CriticalReachabilitySensitiveRecordingFiltration [REFUTED · DEAD · related/non-propagating]** —
          Fresh Rule 7(a)–(g) review confirms that every universal linear filtration containing all
          reachable states contains the full transferred low-degree image. Nonlinear or algorithm-
          dependent carriers remain OPEN only in the separate successor. Canonical:
          research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.reachability-sensitive-recording-filtration.yaml.
          - **CriticalNonlinearAlgorithmDependentRecordingCarrier [OPEN · related/non-propagating]**
            — Outside-scope successor seeking a precisely quantified nonlinear or per-algorithm
            invariant; registered before definition or testing and deprioritized. Canonical:
            research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.hidden-frequency-mask.critical-endpoint.ALT.reachability-sensitive-recording-filtration.ALT.nonlinear-algorithm-dependent-carrier.yaml.
    - **B4bL3AltCriticalCorePsearchLift proof [OPEN · related/non-propagating]** — Conditional
      bridge: a critical `B=Theta(q^(3/2))`, `Omega(B^(2/3))` donor followed by
      `pSearch_(Theta(N/B))` gives the entire capped quarter-power curve. Partial-promise,
      constants, integer, sentinel, range-`O(q)`, arbitrary-target, and padding interfaces pass;
      only the donor antecedent is open. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.critical-core-psearch-lift.yaml; cite:
      artifacts/ksum_L3_critical_core_psearch_lift_audit_20260721.md.
    - **B4bL3AltMultiscaleFrequencyMask proof [OPEN · related/non-propagating]** — Active
      global-window successor. The generic Laplace-residual sampling envelope is now explicit and
      has no universal subtarget kill: one macroscopic decoy plus a `q^(3/2)`-mass shelf at
      multiplicity `sqrt(q)` saturates the target. No lower bound or non-sampling algorithm audit
      exists. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.multiscale-frequency-mask.yaml; cite:
      artifacts/ksum_L3_multiscale_frequency_upper_envelope_20260721.md and
      artifacts/ksum_L3_multiscale_frequency_candidate_20260721.md.
    - **B4bL3AltBicliqueCoverGraphClaw proof [OPEN · related/non-propagating]** — Parameter
      identity using `r=q^(3/2)` and a size-`O(q)` bounded-incidence biclique cover; deprioritized
      because no noncircular `Omega(r^(2/3))` relation-claw donor is known. Canonical:
      research/ksum/proof-dag/nodes/KSUM.B4b.L3.ALT.biclique-cover-graph-claw.yaml.

**B4bL2 phase-6 outline supplement:** exact stabilizer-irrep labels and both frozen held-out label
predictions pass. Fresh hostile review proves the multiplicity-gauge, direct nontrivial-vector
Reynolds-zero, and positive diagonal/Reynolds band-zero facts as scoped components. MAJOR D14 leaves
the aggregate obstruction candidate CONJECTURED because the named transfer class is not exhaustive.
The literal three-branch mechanism is BLOCKED/reviewed. A Gelfand–Tsetlin basis of the irrep factor
does not fix the multiplicity factor; an ambient canonical branching/harmonic basis with a genuinely
signed map and the cap-scale witness remain open. Phase-6 report/review:
`artifacts/ksum_L2_phase6.md`, `artifacts/ksum_L2p6_review.md`.

**B4b journal-expansion outline supplement (integration review completed):** Sections
`sec:dual-toolkit` and `sec:dual-obstructions` of the manuscript now contain the reviewed
completion-tier components at their exact scopes, while the updated open problem retains the
cap-swept odd-`q` obligation and names the D14-unexcluded signed/canonical-multiplicity space.
The conditional U1 statement is presented only under the explicit `F_SC^charge` hypotheses.
Fresh rule-7 integration review passed after minor statement/type repairs, with no substantive or
remaining scope defect; see `artifacts/ksum_merge_review.md`. No DAG status or edge changed.

**Ancestor recomputation:** B4b remains **OPEN** because its global all-algorithms claim is not closed
by a conditional family outcome. Therefore B4 remains **OPEN** (AND-min of PROVED and OPEN), and the
KSUM.goal remains **OPEN**.

### CONSTRAINTS (proved facts that prune every branch)  *(added 2026-07-18; was implicit)*

- **Rosmanis obstruction [NUMERICAL · pending-review · registered 2026-07-30 (T2 F-T1
  finding, third nodeless load-bearing statement found by the Lean audit)]** — `prop:rosmanis`:
  the negative set of `twoSum` is never a single `S_N × C(σ)` orbit for `q ≥ 3, σ ≠ id`; the
  regular-representation identification of [Rosmanis14] does not transfer. T2 kernel-proved the
  count-`≥2` core ORBIT-PROPER plus part (2)'s witnesses and part (3), unconditionally; the
  `(f,λ)` bijection and count formula remain unformalized. Kills the L31 route class structurally.
  Canonical: research/ksum/proof-dag/nodes/KSUM.ROSMANIS.yaml.
- **G11 constraint [CERTIFIED\* · application-scoped · registered 2026-07-30]** — no finite
  exact computation licenses a uniform asymptotic exponent; finite exact values can REFUTE a
  conjectured exponent and supply evidence, never discharge an asymptotic obligation. Promoted from
  a prose term of art to a citable node by review repair K-B3-1 (rule 7g); carries the confirmed
  B3/goal route kills. Canonical: research/ksum/proof-dag/nodes/KSUM.G11.yaml.
- **Any small-`q` lower bound must use group structure beyond the orthogonal-array axioms:** for
  every `(k,q)` in the stated regimes some index-1 OA makes the problem constant, so `T_S`-uniform
  (Theorem-5-type) bounds are vacuous — `∀τ`-uniform bounds only; per-problem bounds unaffected.
  Cite: `ksum_stage2_aut_theorems.md:362,378-379,414` (Theorem 3, PROVED; coverage caveats `:437`).
- **`k≥3` `k`-Sum is not itself multisymmetric-transferable:** its alphabet-side symmetry collapses
  to `diag(Aff_{k,t}(G))⋊S_N` (tiny), unlike `k=2`'s huge centralizer `C(σ)` — so Ambainis/Tani
  range-reduction cannot be run **on `k`-Sum directly**, and OR-2's donor detour (a fully
  range-symmetric donor + an encoding) is **forced**, not a stylistic choice. Cite:
  `ksum_stage2_aut_theorems.md` §2 (Theorem 2, `k≥3` `Aut = diag(Aff)⋊S_N` mod NC-ext);
  `ksum_W3_donor_survey.md:73` (what IS Ambainis-symmetric and why `k`-Sum is not).

---

## 3. Ledger of applied recon corrections & residual uncertainties

- **C-A composition completing review (2026-07-18, fresh hostile reviewer):** L2eC is
  **PROVED** for fixed `k≥3`, exact input lengths `N=kn`, `2≤R≤n`, every target, and only
  the explicit density-zero modulus family `q_k(R)=(P_k(R)+1)(M_k+1)`. The two-query
  relabeling factor and all `k`-dependent conversions are absorbed in `Ω_k`; the all-target
  tag condition holds at the main modulus with no parity restriction. At `R=n` the bound is
  `Ω_k(N^{2/3})<O(N^{k/(k+1)})`, and throughout the family it is dominated by PROVED Theorem C.
  The intake's “new/nothing previously known” interpretation is a MAJOR significance defect,
  not a defect in the exact corollary. L2 remains OPEN/PARKED; B2 and the root remain OPEN.
  Cite: `artifacts/ksum_composition_review.md`; run:
  `artifacts/logs_ksum_W_20260718/codex_comp_review_run.log`.

- **W-LB1/W-LB2 completing review (2026-07-18, fresh hostile reviewer):** L2e and L2f promoted
  to **PROVED** after exact completeness/soundness, query simulation, range, theorem-statement,
  decision/search, and randomized bounded-error checks. Repairs: explicit `R≥2` on L2e
  (MINOR; `R=1` is constant YES) and explicit pre-amplification on L2f (MINOR). Newly authored
  composition children remain CONJECTURED/pending-review and record that L2e's W3E-2 bound is dominated by W3E-1 in the requested
  zone, while L2f's hypothesis maps beyond the zone. L2, B2, and root remain OPEN. Cite:
  `artifacts/ksum_W_review.md`; run `artifacts/logs_ksum_W_20260718/codex_review_run.log`.

**Corrections applied (disk overrides the intake brief):**
- **B4bL2 phase-6 completion review (2026-07-19, fresh hostile rule-7 reviewer):** G1/G2/G3 are
  PROVED only for terminal-label multiplicity coordinates, direct nontrivial-vector Reynolds
  extraction, and the positive diagonal/Reynolds map. Exact and held-out gates pass. MAJOR D14
  leaves aggregate L2P6-G CONJECTURED; MINOR D15/D16 correct the old-obstruction count and metric
  comparison. The literal mechanism is BLOCKED/reviewed, while signed ambient canonical-
  multiplicity constructions remain open. B4bL2 stays CONJECTURED and B4b/B4/root stay OPEN. Cite:
  artifacts/ksum_L2p6_review.md; run: artifacts/logs_ksum_L2p6r_20260719/.
- **B4bL2 phase 6 non-composition transfer (2026-07-19, executor; review now completed):** exact
  `S_(N-1) x C(sigma)` labels identify the trivial spine, tau-indexed satellites, and the tau=0
  repetition-two bipartition. Held-out labels pass, but the no-refit fit is blocked by independent
  multiplicity gauge. Direct nontrivial vector satellites average to zero; positive
  projector-diagonal transfers have constant moment one and band zero. Exact gates at `(4,5,0)`
  and `(5,5,0)` pass. The completed review above supplies the final component/aggregate split and
  leaves signed canonical-multiplicity witnesses open. B4bL2 stays CONJECTURED and B4b/B4/root
  stay OPEN. Cite: artifacts/ksum_L2_phase6.md; run:
  artifacts/logs_ksum_L2p6_20260719/.
- **B4bL2 phase-5 completion review (2026-07-19, fresh hostile rule-7 reviewer):** the general
  averaged factorial-band lemma is PROVED, as are the exact orientation loss and correlation-`<=1/2`
  obstruction for identical phase-3 product blocks with one common exact pair total. Fresh rational
  code reconstructs correlations `2/13`, `1/7`, `4/31`, and `1/16` and adds full `m=3` identity
  gates. MINOR D13 hardens the class boundary. This selected mechanism is BLOCKED/reviewed;
  unequal/nonidentical/non-product and alternative-shape D10 routes remain open. B4bL2 stays
  CONJECTURED and B4b/B4/root stay OPEN. Cite: artifacts/ksum_L2p5_review.md; run:
  artifacts/logs_ksum_L2p5r_20260719/.
- **B4bL2 phase 5 averaged shared-value composition (2026-07-19, executor; review now completed):**
  the exact hypergeometric average and four finite gates are retained as proposer evidence; the
  completed review above supplies the component statuses and hard family scope. Cite:
  artifacts/ksum_L2_phase5.md; run: artifacts/logs_ksum_L2p5_20260719/.
- **B4bL2 phase-4 completion review (2026-07-19, fresh hostile rule-7 reviewer):** the tight
  logarithmic-inner `rho<=4/5` bound, fixed-allocation unaveraged composition identity/degree
  lemma, and whole-pair budget are PROVED components. MAJOR D10 leaves the correlation product
  unproved after a norm-reducing symmetry average and renormalization. T2 nevertheless blocks the
  selected whole-pair mechanism at fixed q. Fresh formula-level code reconstructs `(10,5,0,2)` and
  adds m=3 gates. B4bL2 stays CONJECTURED and B4b/B4/root stay OPEN. Cite:
  artifacts/ksum_L2p4_review.md; run: artifacts/logs_ksum_L2p4r_20260719/.
- **B4bL2 phase 4 block-composition obstruction (2026-07-19, executor; review now completed):**
  whole sigma-pair allocation makes OR-of-blocks exact but forces `m r0<=(q-1)/2`; the proposer
  also derived the fixed-allocation product loss. The completed review above supplies the final
  scoped rulings and D10 boundary. Cite: artifacts/ksum_L2_phase4.md; run:
  artifacts/logs_ksum_L2p4_20260719/.
- **B4bL2 phase-3 completion review (2026-07-19, fresh hostile reviewer):** L2P3 is PROVED as a
  general odd-q logarithmic-band component with exact correlation at least 437/581>3/4. Fresh
  rational reconstruction passes every commissioned target and raw degree-zero/one row. MINOR D9
  corrects the M2 escape: the zero K=2 layer places the construction outside the complete class for
  q>=5, while q=3 is the allowed M1 product. The route stays CONJECTURED because the cap-scale and
  sqrt(N) obligations are open; B4b/B4/root stay OPEN. Cite: artifacts/ksum_L2p3_review.md; run:
  artifacts/logs_ksum_L2p3r_20260719/.
- **B4bL2 phase 3 correlated outer kernel (2026-07-19, executor; review now completed):** the first
  preregistered mechanism passes. A divided-difference outer functional supported on active-pair
  counts `0,1,5,25,...` yields a proposer proof of degree
  `2(1+floor(log_5((q-1)/2)))`, l1 one, invariance, and correlation greater than 3/4. Exact rational
  checks pass all targets at (5,5) and (7,3). Outcome is PROGRESS under the phase-3 bar; the completed
  review above proves the component and repairs its M2 endpoint wording. It remains non-cap-scale,
  so B4bL2 stays CONJECTURED and B4b/B4/root stay OPEN. Cite: artifacts/ksum_L2_phase3.md; run:
  artifacts/logs_ksum_L2p3_20260719/.
- **B4bL2 phase-2 completion review (2026-07-19, fresh hostile reviewer):** M1 and the precisely
  scoped M2 are PROVED structural claims; M3 passes. Fresh exact code checked every target at (5,5)
  and (7,3), plus every raw one-hot row below the claimed degree at t=0. MINOR D8 replaces the loose
  “pure tensor” label by the exact fully locally zero-balanced sign-separated product class. The
  route stays CONJECTURED because the correlated cap-scale witness is unbuilt; B4b/B4/root stay OPEN.
  Cite: artifacts/ksum_L2p2_review.md; run: artifacts/logs_ksum_L2p2r_20260719/.
- **B4bL2 D7 sync + phase 2 (2026-07-19, executor; new mathematics pending review):** the route-minimal
  odd-q obligation and optional even-q strengthening now satisfy the completed repair review's D7
  disposition, restoring B4bL2 to CONJECTURED. The coefficientwise pure tensor kills degrees below
  q-1 but has correlation 2^(1-(q-1)/2), blocking that subclass at q>=5. B4b/B4/root stay OPEN.
  Cite: artifacts/ksum_L2_phase2.md; run: artifacts/logs_ksum_L2p2_20260719/.
- **B4bL2 corrected-repair review (2026-07-19, fresh hostile reviewer):** D1 and D3 pass; the finite
  corrected LP table is proved, and the cap formula passes. D7 remains MODERATE: the addendum's exact
  P4 obligation includes both even-q cycle types even though the registered paper gap only needs odd q;
  C7 does not identify tau=0 with tau=2. B4bL2 is OPEN after completed review pending a scope repair;
  B4b, B4, and the root remain OPEN. Cite: artifacts/ksum_L2r_review.md.
- **B4bL2 corrected-threshold repair (2026-07-19, executor; review now completed):** strict correlation
  >2/3 replaces >1/3 for the direct Q_(1/3)>=d/2 interpretation. New exact-rational runs preserve
  joint certified-degree gains at all three commissioned points, and the corrected P4 obligation is
  capped at N^(2/3), with unrestricted range q<=N^(1/(6eta)). P2 remains shell-deficit-only evidence.
  B4bL2 was CONJECTURED pending review at write time; the completed review above returned it to OPEN.
  B4b, B4, and the root remain OPEN. Cite:
  artifacts/ksum_L2_phase1_addendum.md; run: artifacts/logs_ksum_L2r_20260719/.
- **B4 round-2 independent completion review (2026-07-18, fresh Codex reviewer):** B4a is **PROVED** under rule 6. D1/D2 were independently re-derived with the capped estimate h, the two MINOR repairs and full standalone proof passed, and no new defect was found. The k=2 middle gap is now lower Omega(sqrt(N)q^(1/6)) versus upper O_epsilon(N^(1/2+epsilon)q^(1/4)); 1/6<1/4 remains, so B4 and the root stay OPEN. Cite: artifacts/ksum_B4_review2.md; provenance: artifacts/logs_ksum_B4_20260718/codex_review2_run.log.

- **B4 v2 repair pass (2026-07-18, Codex executor):** B4a remains **CONJECTURED — pending-review:**; **v2 integrates review repairs; second review pending**. D1 now dispatches actual-short compressed calls to Johnson; D2 now caps every branch using capped counting, an estimate gate, fixed virtual sizes, and prefix truncation; both MINOR defects are fixed. Cite: `artifacts/ksum_B4_upper_note_v2.md`; first review: `artifacts/ksum_B4_review.md`; repair run: `artifacts/logs_ksum_B4_20260718/codex_repair_run.log`; numerical manifest: `artifacts/logs_ksum_B4_20260718/ksum_b4v2_sha256.txt`. B4 and the root remain OPEN.
- **B4 independent hostile review (2026-07-18, fresh Codex rule-6 reviewer):** completed against ABI's on-disk source and the candidate note. Attribution and the fixed-point/single-list compression repair pass. Findings: 2 MAJOR repairable proof gaps (recursive actual-length regime; worst-case cap on bad-sampling branches), 2 MINOR bookkeeping/error-wording defects, 0 FATAL. B4a remains **CONJECTURED** pending repair and fresh review; B4b and B4 remain OPEN; root remains **OPEN**. Cite: `artifacts/ksum_B4_review.md`; run: `artifacts/logs_ksum_B4_20260718/codex_review_run.log`.
- **B4 ABI-algorithm port candidate (2026-07-18; pending independent review):** extracted ABI's exact sample/compress recursion and identified the single-list obstruction: compression with replacement can duplicate one original fixed-point index and create a false pair. For cyclic groups, `tau<=2`; an `O(sqrt(N))` fixed-point multiplicity check followed by exclusion repairs soundness, after which ABI's recurrence gives the candidate `O_epsilon(N^{1/2+epsilon}q^{1/4})` upper bound. B4a is **CONJECTURED — pending-review:**, B4b remains OPEN, hence B4 and the root remain OPEN. Cite: `artifacts/ksum_B4_upper_note.md`.
- **GAP verify pass (2026-07-18, fresh Codex completing reviewer): L2d review cycle closed.** All 11
  GAP-audit repairs were checked in situ and independently re-derived where mathematical; the fixed
  checker was rerun (exit 0, exact PASS), and the paper rebuilt cleanly (four stages, 18 pp). L2d is
  now **PROVED** for value-search, the combined donor cap, the endpoint-qualified iff, and the corrected
  blocked-sub-zone arithmetic; Tani's walk input remains explicitly **PROVED-IN-LIT**. The
  uniform-in-`R` converse and a tighter `k≥3` small-range envelope remain respectively **UNPROVED** and
  **CONJECTURED**. Chain: `artifacts/ksum_final_gap_audit.md` →
  `artifacts/ksum_gap_fixes_applied.md` → `artifacts/ksum_gap_verification.md`; run:
  `artifacts/logs_ksum_GAP_20260718/captable_verify.log`. Ancestors recomputed: L2 and B2 remain OPEN;
  root remains **OPEN**.
- **GAP-audit pass (2026-07-18, codex gpt-5.6-sol):** independent audit of the three previously-unaudited pieces (revision-pass k=2 rewrites; F0 obstruction note; MTZ dependency) — 5 MODERATE + 6 LOW defects found and repaired (`artifacts/ksum_final_gap_audit.md`; repairs this entry); MTZ pinned from primary source (Thm 1.1, k≥2, range≥domain); Tani-walk Corollary 11 pinned from primary source — F0's ON-TRUST link closed. No HIGH defect; all main conclusions survive.
- The frozen-coordinate reduction is **NOT "REFUTED-in-part."** The gcd(`k−2,q`) and
  odd-live-leakage obstructions kill only the *naive uniform-shift* and *odd-live* variants
  (`AUDIT.md:15-16`); the reduction was **repaired** in Lemma W3E-1 (constant freeze `C₀`, even
  `2n`-coord claw encoding, window + translation coverage), yielding the banked floor Theorem C
  `Q=Ω_k(√N·q^{1/6})` (`KSUM_W3_CLOSEOUT.md:7-8`; `ksum_W3E_embedding_lemmas.md:17-41`). Correct
  status (at that pass): **LIVE / PROVED-BY-REDUCTION modulo the on-disk donor, single-author
  unaudited** — *the "single-author unaudited" clause is now SUPERSEDED; the independent audit
  completed and passed on 2026-07-18 (F1); see header and the resolved residual items below.*
- The `k`-collision embedding is **NOT "OPEN — incomplete formulas / modulus underived."** Lemma
  W3E-2 supplies complete formulas and a derived modulus, proves all wrong patterns excluded,
  passes 62,140 checks (`ksum_W3E_embedding_lemmas.md:74-98`). The **ENCODING is PROVED**; the
  only OPEN item is the missing `k≥3` donor (`ksum_W3_donor_survey.md:93-95`). The AUDIT.md:17
  wording is the stale gap-3 framing.

**Corrections applied (2026-07-18 pass, strategist; every cite re-read from disk this pass):**
- **L2a crossover k≥7 → k≥4-under-MTZ** (survey `:31` — MTZ Ω̃(n^{3/4−1/(4k)}), TQC'20, theorem for fixed `k≥2`;
  arithmetic `3/4−1/(4k)>2/3 ⟺ k≥4`). The `k≥7` figure was computed against the BKT base only.
  **Propagation [DONE same day]:** Erratum appended to `KSUM_W3_CLOSEOUT.md` (body preserved); the
  paper's §6 grep-verified NOT to carry the figure (audit-1 wording `n^{3/4−Θ(1/k)}`); the earlier
  claim here that the paper also carried it was a strategist overclaim, corrected in place.
- **A1f appended** with the interrupted-audit interim findings (trap confirmed real; independent
  re-derivations passed) — partial corroboration, caveat retained.
- **L32a evidence extended** to `n=8` (`C7_extend.log:15,22`).
- **Added B4, C0, L33** (upper-bound branch; proved pruning constraints; the designed-never-built
  reduced solver) — all previously missing structure, no status changes.
- **Header k=2 scope note** sharpened: threshold settled, middle gap OPEN and unmapped here.
- **PROVER_PROMPT synchronized**: F2 marked discharged (paper-side k=2 fixes done in working tree),
  F3 marked resolved (was already resolved in this file's ledger), F1 annotated in-progress, F4 added.
- *Verification note:* the disk cites added this pass were re-read directly by the strategist; the
  full line-number sweep of ALL pre-existing DAG citations by an independent instance is still queued
  (first codex job once the CLI session issue clears).

**Corrections/additions applied (2026-07-17, F0 executor-verifier pass):**
- **Added L2d (donor-cap, then single-author/awaiting independent review; now PROVED by the GAP verify
  pass above)** under L2 as a dotted constraint (root unchanged, still OPEN). The
  cap `c ≤ (k−1)/(2(k+1))` at `R=Θ(n)` comes from Tani's **range-independent** k-claw walk
  `O(n^{k/(k+1)})` (arXiv:0708.2584) + value-search `Õ(√Rn)`; it equals the dream exponent exactly
  (machine-checked, `tools/ksum_f0_captable.py` → `logs_ksum_F0_20260718/captable.log`). Full argument
  + honest caveats in `artifacts/ksum_F0_obstruction_note.md`.
- **L2b (dream donor) sharpened, not restatused:** stays PARKED, but the dream **endpoint bound** is
  identified as maximal and equivalent *at `R=Θ(n)`* to k-claw walk-optimality there (KNOWN k=2 /
  OPEN k≥3); the uniform-in-`R` converse is unproved. This does not contradict its "never tight at
  `q=Θ(N)`" note — it explains why (the loose-cap small-`q` opening is an artifact killed by any
  honest small-range algorithm).
- **Fresh literature pass (new axis)** reconfirms NO-DONOR (`artifacts/references/ksum_F0_literature_evidence.txt`);
  did **not** change L2's OPEN·PARKED status. Tani-2410.02243 fwd-cites = 0; MTZ-2002.08389 fwd-cites =
  14, none a small-range k-partite claw detection LB.

**Residual uncertainties (flagged, not resolved):**
- **F0 donor-cap is loose at small range (the honest limit of this pass):** the value-search `c≤1/2`
  arm is almost certainly not tight for `k≥3`; an ABI-style small-range k-claw algorithm (k=2 gives
  `R^{1/4}`) is **unbuilt**, so the true `c_0(k)` at `R=o(n)` — and the exact reachable B2 sub-zone —
  is undetermined. The proved upper cap at `R=Θ(n)` exactly equals the dream exponent; whether a
  matching lower bound attains it for `k≥3` remains OPEN.
- **The dream donor is capped but NOT settled:** L2d proves the donor cannot exceed `(k−1)/(2(k+1))`;
  it does **not** prove the k≥3 k-claw walk is optimal (which is the donor itself). That tight lower
  bound remains the single open problem for both B1 and B2.
- No exact/full `Adv±` value for any `k≥3` instance is located anywhere on disk; the working
  unreduced solver produced `2-Sum` values only.
- W3E-1's **padding of `N` to arbitrary size was proof-complete only for `k=3,4`** (≤2 pads,
  exhaustively verified); the general `(k,r)` window-avoidance was "stated but not exhaustively
  instantiated for `k ≥ 5`" — a routine-but-unwritten step (`ksum_W3E_embedding_lemmas.md:164`
  item 7). **[RESOLVED 2026-07-18 (F1)]** the F1 audit found that padding with extra `C₀`-constants
  genuinely CAN self-hit for `k≥3` (`3C₀≡t₀` at k=3,q=24), i.e. the "routine" step is not routine as
  framed. The delivered `revision_k3.tex` avoids padding entirely: it sizes the live block to `N`
  (`m=⌊(N−(k−2))/2⌋`) and uses **at most ONE parked coordinate** `v=t+(k−1)K+1` for odd `N−(k−2)`,
  with a fully-general parity proof (`Lemma lem:core-odd`) verified exhaustively for `k=3,4,5,6`
  (`floor_audit.log` Part B). Gap CLOSED. **[R3 2026-07-18]** `lem:core-odd` independently re-audited
  (fresh Opus, own from-scratch oracle): input-level `kSum==Claw` k=3..8 (incl. **k=7,8**, beyond the
  F1 k≤6 range), pattern-level `W∈[1,q−1]` k=3..10, full `Z_q` coverage, `+1` margin shown exactly
  tight; single-author caveat DISCHARGED (A1f). `tools/ksum_r3_parity.py` (SHA `c62bd56c…`),
  `artifacts/logs_ksum_R3_20260718/parity_audit.log` (SHA `fb515cd2…`).
- W3E-2's tight family constant is `CONJECTURED` (`≈2` at `k=3`, `≈4` at `k=4`); only the loose
  `q=(P+1)(M+1)` modulus is PROVED, and `k=6` is certified pattern-level only, no input-level run
  (`ksum_W3E_embedding_lemmas.md:112,162`). None of this affects encoding *correctness*, only the
  sharpness of the `q=Θ_k(R^{k−1})` constant.
- ~~No independent hostile (W2-style, second-author-with-own-code) audit of the `k≥3` W3E-1/W3E-2
  scripts is located~~ **[RESOLVED 2026-07-18 (F1)]** — a fresh Opus instance (did NOT author W3E)
  completed the independent hostile audit with its own from-scratch code: `tools/ksum_f1_floor.py`
  (SHA `79a22f3f…`, 47,496 inputs) + `tools/ksum_f1_embed.py` (SHA `ca5bdbbc…`, 58,033 inputs +
  pattern cert k=3..6), logs under `artifacts/logs_ksum_F1_20260718/`. Both lemmas PASS; single-author
  status discharged (A1f, A2). Remaining trust: only the external ABI/Tani donor, inherited from k=2.
- Git status **RESOLVED** here: the W3 work **is** committed (`ed542e1` "k-Sum W3 close-out",
  `949240a` atop `8e0f106`), so `KSUM_W3_CLOSEOUT.md:25` is accurate; the W3E header's "no
  commits made by this work" (`ksum_W3E_embedding_lemmas.md:3`) was true at write-time, now stale.
- `ksum_probe2.py` (repo root) is flagged "unaudited" (`KSUM_SMALL_G_COMMISSION.md:1293`); no
  audit result or `k≥3` number from it is on disk — status beyond "unaudited" is unrecorded.
