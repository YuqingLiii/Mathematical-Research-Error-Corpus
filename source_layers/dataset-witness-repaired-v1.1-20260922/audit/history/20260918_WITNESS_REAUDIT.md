# Historical report — not the governing release statistics

# 75-record mathematical error and witness re-audit

Date: 2026-09-18  
Input: `publication_curation_v03_grothendieck_additions/records_v03.jsonl`  
Policy: do not edit frozen v03; publish corrections as an additive adjudication layer.

## Bottom line

The frozen 75-record ledger should **not** be released unchanged.

| adjudication | count | meaning |
|---|---:|---|
| retain: direct mathematical defeater | 53 | a counterexample, exact calculation, type contradiction, or exact internal contradiction defeats the scoped claim |
| retain: proof/scope/status gap | 16 | the evidence defeats a claimed implication, proof completion, imported theorem, quantifier scope, or status promotion; it does not necessarily refute the theorem itself |
| retain after witness rewrite | 5 | the error is real, but the current witness sentence is temporally, logically, or scope-wise too strong |
| exclude as false positive | 1 | the alleged erroneous statement is not actually asserted by the source |
| **publication-ready after corrections** | **74** | 53 direct defeaters + 21 inference/proof/scope/status errors |

All 75 primary-source byte bindings pass: 74 exact-file hashes and one exact append-only prefix.
That verifies provenance, not mathematical truth by itself.

## The excluded record

### `GAP-004` — exclude

The dataset currently attributes this claim to the agent:

> The aggregate orthogonal identity implies a separate norm bound for every subset component.

The source does not say that.  It says that equation (44) is a generating function for the
aggregate nonempty sectors.  Twenty-six seconds later, in the same turn, the agent explicitly
adds that neither (44) nor the preceding lemma asserts a separate per-subset estimate.  The
database's alleged bad claim is therefore a disavowed interpretation, not an observed
mathematical assertion.  It may be retained as a **near-miss/negative control**, but not as one of
the positive error records.

## Five records whose witness must be rewritten

### `COLLISION-GOLD3-001`

The error is real: full Collision completion was declared without an established SE-to-Collision
inheritance bridge.  But the current witness incorrectly says the reused certificate “had already
been withdrawn.”  The completion claim preceded the formal upstream withdrawal.  The valid
witness is **unestablished inheritance at the time of completion**, not knowing reuse of a dead
certificate.

### `GAP-003`

The source supports an invalid jump from “necessary for this iterated-localization proof” to
“necessary for every extensive construction.”  Saying that a fixed conjugate-pair route remains
open does not furnish a counterexample to the universal conclusion.  Record it as an
**unsupported universal necessity inference**, not a disproved general theorem.

### `KSUM-004`

The vague witness “orbit behavior outside the claimed classification” should be replaced by
the source's concrete regularity witnesses.  At `(q,tau,n)=(3,1,2)`, the position swap of `(0,1)`
is not induced by the centralizer, so existence fails.  At `(4,0,2)`, flipping an unused 2-cycle
stabilizes `y=(0,0)`, so uniqueness fails.  These refute the blanket regularity/classification
claim, not every repaired orbit statement.

### `QEC-LIFT-004`

The recovered audit directly confirms omission of `R >= d` from the root claim.  The current
compound reference answer also mentions MC, but this pass did not find a separately bound
independent re-proof of that half.  Release the `R >= d` omission; split or separately source the
MC clause.

### `TAPER-GOLD4-001`

The witness establishes a target mismatch: the script controls `T_b/m` while the theorem claims
physical `T_b`.  It should not say that record 001 itself contains a physical `T_b`
counterexample.  The exact failing physical examples in the same episode concern `T_a` and are
already represented by `TAPER-GOLD4-003`.

## What “witness is valid” means here

The corpus contains two scientifically different witness classes:

1. **Direct defeater.**  The scoped mathematical sentence is false.  Examples include the
   `q=3,k=3,N>=7` KSUM pigeonhole family, the QEC Gross interleaving schedule, the NPTBE
   indefinite `E^S` matrices, the WHGAP per-use normalization, and arithmetic/checksum errors.
2. **Inference/proof/status witness.**  The claimed conclusion may still be true, but the recorded
   evidence does not establish it.  Examples include missing theorem imports, omitted hypotheses,
   a candidate called proved, or an unbound external lemma.

Both are legitimate natural research-process errors.  They must have different benchmark labels;
otherwise evaluation will mistakenly reward a critic for claiming a theorem is false when it has
only found a proof gap.

## Re-execution performed in this pass

- Recomputed all 75 primary-source hashes (including the one frozen prefix): all pass.
- Ran 26 compact exact checks in `replay_and_build.py`, including modular, pigeonhole,
  finite-field, Fourier-sign, variance-quantifier, strict-ceiling, large-integer, normalization,
  and Grothendieck arithmetic witnesses.
- Re-ran the v02 and v03 builders: both end in `FINAL PASS`; all 24 M3 records retain their source
  markers and replay/scope checks.
- Re-ran the independent NPTBE `p4_ES_reduction.py` with the scientific Python runtime.  It again
  produces `E^S=[[0,-1/2],[-1/2,0]]` with eigenvalues `(-1/2,1/2)` for the displayed cases and
  zero reassembly error.  The archived second independent pass gives the exact general value
  `lambda_min=-2^{-|S|}` for every nonempty `S` in its stated family.
- Re-read the exact QEC review witnesses rather than accepting their verdict labels.  In
  particular, the Gross MC/non-interleaving counterexample, the legal staggered six-layer
  schedule, the non-invariant-registry lex-quotient counter-scenario, the LIFT `R_sat` example,
  and the SAT boundary/detector counterexamples are explicit objects with scoped conclusions.

The 26 compact checks and the 24 M3 builder checks overlap; they must not be added as independent
sample counts.  They are reproducibility checks, not new data points.

## Publication recommendation

Freeze a v04 release with **74 positive records** and move `GAP-004` to a negative-control or
near-miss annex.  Preserve the five rewritten witnesses verbatim in the release.  In the paper,
report at least these two top-level classes separately:

- 53 direct counterexample/exact-contradiction records;
- 21 invalid-inference/proof-gap/scope/status records.

Do not describe all 74 as “false theorems,” and do not call all witnesses counterexamples.

## Files

- `WITNESS_REAUDIT.tsv`: one adjudication row per original record.
- `REPLAY_RESULTS.json`: source-byte checks and compact exact replay results.
- `replay_and_build.py`: deterministic builder for both files.

