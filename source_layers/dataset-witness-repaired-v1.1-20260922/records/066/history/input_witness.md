# Record 066 — Optimal circuit distance of the Gross code

**Review status:** `source_or_fixture_check_pending`.

The exact base-model assignment and all 72 translate evaluations are source-bound in the archive, but the selected text is not itself a standalone executable certificate. Before final release, bundle the small relevant schedule/registry witness or supply a self-contained reduced counterexample at the same claimed scope.

## Original statement and context

> UNSAT of the checked quotient plus sound base exclusions would prove every legal schedule has a weight<=10 direct mechanism; SAT supplies only a canonical candidate.

**Recorded location:** Archived computational certificate dated 1 September 2026, iteration-185 quotient, finite_coverage_theorem.root_use.

**Context (annotation, not a source quotation):** A finite search quotient appended lexicographic symmetry-breaking clauses to an exclusion registry. The quotient was intended to cover the full legal schedule class. The registry had not been closed under the 72-element translation group.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

An orbit can be replaced by its lexicographically least member only if the base formula remains true under the group action. Soundness of individual exclusion clauses does not imply invariance of their installed subset.

### Argument or calculation

Let B be the base formula with 330 selectors and 14,484 untranslated block cuts, and let L be its 71 nonidentity translation lex-leader constraints. The archived independent counter-scenario provides a legal base model S. Among all 72 translated schedules, only the identity translate satisfies B. The lexicographically least translate is at δ=(1,5), and it violates 75 installed block cuts. Therefore this orbit has a B-model but no model of B∧L. The required implication B(S)⇒B(δS) fails, so orbit-wise coverage and lifting an UNSAT result are unjustified. Both old formulas happened to be SAT; this witness invalidates the coverage theorem rather than claiming the quotient itself is UNSAT.

Scope: argument_invalid.


### Archived review excerpt

> Let `B_185` be the first outer base with 330 selectors and the untranslated 14,484 block registry. Its exact CNF has 416,062 variables, 1,417,374 clauses, and SHA-256 `ddd40740b42854b74de7d64e3899f017a58a56223b3fa560d15845a9f7cae6c9`. Let `L` be the conjunction of the 71 translation lex leaders.
> 
> I independently launched a fresh CaDiCaL solve of `B_185`, outside the proposer ledger. It returned `rc=10/SAT` in about 3.42 seconds with empty stderr. I parsed exactly 416,062 assignment literals, checked the exact variable domain, and satisfied all 1,417,374 clauses. The decoded legal raw schedule has SHA-256 `50e84c565d1ff4191a3fa48c22f0d4509ec072645540cb791e7acc3c33e8f148`; rank compression gives SHA-256 `1b68d1beb7c2205d7def84e5f1560340523d095be60ae348d27b58523f3df513`, 144 layers.
> 
> I then enumerated all 72 translated raw schedules and evaluated every original block and selector directly:
> 
> * exactly one translate survives `B_185`, the identity `(0,0)`;
> * the orbit’s lexicographically least raw vector occurs at `(1,5)`;
> * that least translate has raw schedule SHA-256 `01ced0f703ea1bf21c6c9a07d963f7514eaa85bbfd16ab4373a2635340c51087`;
> * it hits 75 installed block cuts and zero selectors; and
> * its first hit in registry order is `r69-Xerr-2-8-19`.
> 
> Therefore this base orbit contains no member satisfying both the original base and all lex leaders: its only base survivor is not least, and its least member is not a base model. The failed proof step is
> 
> \[
> B_{185}(S)\Longrightarrow B_{185}(\delta S),
> \]
> 
> which is false because the registry was not invariant. This is a concrete refutation of the orbit-canonicalization claim. It does not assert that `B_185 ∧ L` is UNSAT; the package’s different exploratory assignment proves it SAT. It establishes that the quotient has no licensed orbit-wise coverage or UNSAT lifting theorem.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 生成期摘要只有 quotient CNF/lex order 计划；后来识别不变性缺口的摘要不算生成期证据。

- [2026-09-01T04:36:22.530Z — codex_reasoning_summary](original/M05-rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl.readable.md) — source line 365; recorded role: generation.

## Original materials

- [M01: independent_check.json](original/M01-independent_check.json "research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/global/iter185_translation_quotient/independent_check.json")
  - Coverage: Full bundled file; source lines 1–44.
  - Relevant location(s): {"json_pointer": "/finite_coverage_theorem/root_use"}; #finite_coverage_theorem; Referenced by research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/GLOBAL_TRANSLATION_THEOREM.md
  - Source: `research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/global/iter185_translation_quotient/independent_check.json`

- [M02: circdist_gross_global_closure_round102_exact_review_round103_20260901.md](original/M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md "research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md")
  - Coverage: Full bundled file; source lines 1–1708.
  - Relevant location(s): §8，首段摘要; lines 351–369; #8; Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md`

- [M03: GLOBAL_TRANSLATION_THEOREM.md](original/M03-GLOBAL_TRANSLATION_THEOREM.md "research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/GLOBAL_TRANSLATION_THEOREM.md")
  - Coverage: Full bundled file; source lines 1–196.
  - Source: `research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/GLOBAL_TRANSLATION_THEOREM.md`

- [M04: CIRCDIST.gross.yaml](original/M04-CIRCDIST.gross.yaml "research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml")
  - Coverage: Full bundled file; source lines 1–1882.
  - Relevant location(s): gross-global-closure-round103-review; Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md
  - Source: `research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml`

- [M05: rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl](original/M05-rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl.readable.md "local-session-archive/2026/09/01/rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl") · [event data](original/M05-rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 352–371.
  - Relevant location(s): lines 365
  - Source: `local-session-archive/2026/09/01/rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl`

- [M06: scheduler.yaml](original/M06-scheduler.yaml "research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/bindings/scheduler.yaml")
  - Coverage: Full bundled file; source lines 1–3258.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md
  - Source: `research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/bindings/scheduler.yaml`

- [M07: circdist_gross_round80_whole_registry_exact_review_20260830.md](original/M07-circdist_gross_round80_whole_registry_exact_review_20260830.md "research-graph/circdist/reviews/circdist_gross_round80_whole_registry_exact_review_20260830.md")
  - Coverage: Full bundled file; source lines 1–317.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_round80_whole_registry_exact_review_20260830.md`

- [M08: circdist_gross_round78_cross_registry_exact_review_20260830.md](original/M08-circdist_gross_round78_cross_registry_exact_review_20260830.md "research-graph/circdist/reviews/circdist_gross_round78_cross_registry_exact_review_20260830.md")
  - Coverage: Full bundled file; source lines 1–412.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_round78_cross_registry_exact_review_20260830.md`

- [M09: circdist_gross_round76_online_generalizing_exact_review_20260829.md](original/M09-circdist_gross_round76_online_generalizing_exact_review_20260829.md "research-graph/circdist/reviews/circdist_gross_round76_online_generalizing_exact_review_20260829.md")
  - Coverage: Full bundled file; source lines 1–743.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_round76_online_generalizing_exact_review_20260829.md`

- [M10: circdist_gross_round74_online_generalizing_exact_review_20260829.md](original/M10-circdist_gross_round74_online_generalizing_exact_review_20260829.md "research-graph/circdist/reviews/circdist_gross_round74_online_generalizing_exact_review_20260829.md")
  - Coverage: Full bundled file; source lines 1–624.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_round74_online_generalizing_exact_review_20260829.md`

- [M11: circdist_gross_round72_generalization_exact_review_20260829.md](original/M11-circdist_gross_round72_generalization_exact_review_20260829.md "research-graph/circdist/reviews/circdist_gross_round72_generalization_exact_review_20260829.md")
  - Coverage: Full bundled file; source lines 1–549.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_round72_generalization_exact_review_20260829.md`

- [M12: circdist_gross_block_minimization_exact_review_20260829.md](original/M12-circdist_gross_block_minimization_exact_review_20260829.md "research-graph/circdist/reviews/circdist_gross_block_minimization_exact_review_20260829.md")
  - Coverage: Full bundled file; source lines 1–793.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_block_minimization_exact_review_20260829.md`

- [M13: circdist_dstar_hunt3_20260828.md](original/M13-circdist_dstar_hunt3_20260828.md "research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md")
  - Coverage: Full bundled file; source lines 1–678.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_dstar_hunt3_20260828.md`

- [M14: circdist_gross_morphing_scope_ruling_20260826.md](original/M14-circdist_gross_morphing_scope_ruling_20260826.md "research-graph/circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md")
  - Coverage: Full bundled file; source lines 1–490.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_morphing_scope_ruling_20260826.md`

- [M15: CIRCDIST.gross.yaml](original/M15-CIRCDIST.gross.yaml "research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.gross.yaml")
  - Coverage: Full bundled file; source lines 1–564.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.gross.yaml`

- [M16: legacy_DAG_PROTOCOL.md](original/M16-legacy_DAG_PROTOCOL.md "research-graph/circdist/artifacts/history/legacy_DAG_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–254.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/history/legacy_DAG_PROTOCOL.md`

- [M17: circdist_gross_verdict_20260823.md](original/M17-circdist_gross_verdict_20260823.md "research-graph/circdist/artifacts/circdist_gross_verdict_20260823.md")
  - Coverage: Full bundled file; source lines 1–1902.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_verdict_20260823.md`

- [M18: SHA256SUMS.txt](original/M18-SHA256SUMS.txt "research-graph/circdist/artifacts/logs_circdist_gross_verdict_20260823/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–63.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/logs_circdist_gross_verdict_20260823/SHA256SUMS.txt`

- [M19: circdist_gross_final_decision_20260823.md](original/M19-circdist_gross_final_decision_20260823.md "research-graph/circdist/artifacts/circdist_gross_final_decision_20260823.md")
  - Coverage: Full bundled file; source lines 1–1609.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_final_decision_20260823.md`

- [M20: SHA256SUMS.txt](original/M20-SHA256SUMS.txt "research-graph/circdist/artifacts/logs_circdist_gross_final_20260823/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–23.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/logs_circdist_gross_final_20260823/SHA256SUMS.txt`

- [M21: circdist_gross_candidate_decision_20260822.md](original/M21-circdist_gross_candidate_decision_20260822.md "research-graph/circdist/artifacts/circdist_gross_candidate_decision_20260822.md")
  - Coverage: Full bundled file; source lines 1–1100.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_candidate_decision_20260822.md`

- [M22: SHA256SUMS.txt](original/M22-SHA256SUMS.txt "research-graph/circdist/artifacts/logs_circdist_gross_drivers_20260823/SHA256SUMS.txt")
  - Coverage: Full bundled file; source lines 1–13.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/logs_circdist_gross_drivers_20260823/SHA256SUMS.txt`

- [M23: circdist_gross_candidate_unsat_20260822.md](original/M23-circdist_gross_candidate_unsat_20260822.md "research-graph/circdist/artifacts/circdist_gross_candidate_unsat_20260822.md")
  - Coverage: Full bundled file; source lines 1–2219.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_candidate_unsat_20260822.md`

- [M24: circdist_gross_phicert_20260822.md](original/M24-circdist_gross_phicert_20260822.md "research-graph/circdist/artifacts/circdist_gross_phicert_20260822.md")
  - Coverage: Full bundled file; source lines 1–2301.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_phicert_20260822.md`

- [M25: circdist_sbbcert_review_20260820.md](original/M25-circdist_sbbcert_review_20260820.md "research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–580.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md`

- [M26: CIRCDIST_PROBLEMS.md](original/M26-CIRCDIST_PROBLEMS.md "research-graph/circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md`

- [M27: circdist_gross_sbbcert_20260820.md](original/M27-circdist_gross_sbbcert_20260820.md "research-graph/circdist/artifacts/circdist_gross_sbbcert_20260820.md")
  - Coverage: Full bundled file; source lines 1–2910.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_sbbcert_20260820.md`

- [M28: circdist_lift_iff_proof_20260820.md](original/M28-circdist_lift_iff_proof_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md`

- [M29: circdist_numerical_review_20260820.md](original/M29-circdist_numerical_review_20260820.md "research-graph/circdist/reviews/circdist_numerical_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–2246.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_numerical_review_20260820.md`

- [M30: circdist_lift_d3gate_20260820.md](original/M30-circdist_lift_d3gate_20260820.md "research-graph/circdist/artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_d3gate_20260820.md`

- [M31: circdist_gross_g1_20260820.md](original/M31-circdist_gross_g1_20260820.md "research-graph/circdist/artifacts/circdist_gross_g1_20260820.md")
  - Coverage: Full bundled file; source lines 1–2193.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_g1_20260820.md`

- [M32: circdist_gross_toolfeas_20260820.md](original/M32-circdist_gross_toolfeas_20260820.md "research-graph/circdist/artifacts/circdist_gross_toolfeas_20260820.md")
  - Coverage: Full bundled file; source lines 1–62.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_toolfeas_20260820.md`

- [M33: circdist_gross_recon_20260820.md](original/M33-circdist_gross_recon_20260820.md "research-graph/circdist/artifacts/circdist_gross_recon_20260820.md")
  - Coverage: Full bundled file; source lines 1–755.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_recon_20260820.md`

- [M34: circdist_gross_verdict_review_20260823.md](original/M34-circdist_gross_verdict_review_20260823.md "research-graph/circdist/reviews/circdist_gross_verdict_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–1051.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_verdict_review_20260823.md`

- [M35: circdist_gross_links_review_20260823.md](original/M35-circdist_gross_links_review_20260823.md "research-graph/circdist/reviews/circdist_gross_links_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–522.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_links_review_20260823.md`

- [M36: circdist_dstar_hunt1_20260823.md](original/M36-circdist_dstar_hunt1_20260823.md "research-graph/circdist/artifacts/circdist_dstar_hunt1_20260823.md")
  - Coverage: Full bundled file; source lines 1–247.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_dstar_hunt1_20260823.md`

- [M37: circdist_dstar_hunt2_20260823.md](original/M37-circdist_dstar_hunt2_20260823.md "research-graph/circdist/artifacts/circdist_dstar_hunt2_20260823.md")
  - Coverage: Full bundled file; source lines 1–372.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_dstar_hunt2_20260823.md`

- [M38: circdist_campaign4_closeout_20260823.md](original/M38-circdist_campaign4_closeout_20260823.md "research-graph/circdist/artifacts/circdist_campaign4_closeout_20260823.md")
  - Coverage: Full bundled file; source lines 1–106.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/circdist_campaign4_closeout_20260823.md`

- [M39: legacy_FILE_PROTOCOL.md](original/M39-legacy_FILE_PROTOCOL.md "research-graph/circdist/artifacts/history/legacy_FILE_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–148.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/history/legacy_FILE_PROTOCOL.md`

- [M40: CAMPAIGN4_KICKOFF_20260822.md](original/M40-CAMPAIGN4_KICKOFF_20260822.md "research-graph/circdist/artifacts/history/notes/CAMPAIGN4_KICKOFF_20260822.md")
  - Coverage: Full bundled file; source lines 1–57.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/history/notes/CAMPAIGN4_KICKOFF_20260822.md`

- [M41: CAMPAIGN_CLOSEOUT_20260820.md](original/M41-CAMPAIGN_CLOSEOUT_20260820.md "research-graph/circdist/artifacts/history/notes/CAMPAIGN_CLOSEOUT_20260820.md")
  - Coverage: Full bundled file; source lines 1–95.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/history/notes/CAMPAIGN_CLOSEOUT_20260820.md`

- [M42: HANDOFF_20260820.md](original/M42-HANDOFF_20260820.md "research-graph/circdist/artifacts/history/notes/HANDOFF_20260820.md")
  - Coverage: Full bundled file; source lines 1–103.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/history/notes/HANDOFF_20260820.md`

- [M43: HANDOFF_20260823.md](original/M43-HANDOFF_20260823.md "research-graph/circdist/artifacts/history/notes/HANDOFF_20260823.md")
  - Coverage: Full bundled file; source lines 1–79.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/history/notes/HANDOFF_20260823.md`

- [M44: PATH_MAP.json](original/M44-PATH_MAP.json "research-graph/circdist/artifacts/history/PATH_MAP.json")
  - Coverage: Full bundled file; source lines 1–742.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/artifacts/history/PATH_MAP.json`

- [M45: circdist_gross_efssc_exact_review_round87_20260830.md](original/M45-circdist_gross_efssc_exact_review_round87_20260830.md "research-graph/circdist/reviews/circdist_gross_efssc_exact_review_round87_20260830.md")
  - Coverage: Full bundled file; source lines 1–861.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_efssc_exact_review_round87_20260830.md`

- [M46: circdist_gross_proof_outer_exact_review_round89_20260830.md](original/M46-circdist_gross_proof_outer_exact_review_round89_20260830.md "research-graph/circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md")
  - Coverage: Full bundled file; source lines 1–1370.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_proof_outer_exact_review_round89_20260830.md`

- [M47: circdist_gross_proof_outer_exact_review_round91_20260830.md](original/M47-circdist_gross_proof_outer_exact_review_round91_20260830.md "research-graph/circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md")
  - Coverage: Full bundled file; source lines 1–2278.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_proof_outer_exact_review_round91_20260830.md`

- [M48: circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md](original/M48-circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md "research-graph/circdist/reviews/circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md")
  - Coverage: Full bundled file; source lines 1–3167.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md`

- [M49: circdist_gross_proof_outer_round94_exact_review_round95_20260830.md](original/M49-circdist_gross_proof_outer_round94_exact_review_round95_20260830.md "research-graph/circdist/reviews/circdist_gross_proof_outer_round94_exact_review_round95_20260830.md")
  - Coverage: Full bundled file; source lines 1–1817.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_proof_outer_round94_exact_review_round95_20260830.md`

- [M50: circdist_gross_proof_outer_round96_exact_review_round97_20260831.md](original/M50-circdist_gross_proof_outer_round96_exact_review_round97_20260831.md "research-graph/circdist/reviews/circdist_gross_proof_outer_round96_exact_review_round97_20260831.md")
  - Coverage: Full bundled file; source lines 1–4832.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_proof_outer_round96_exact_review_round97_20260831.md`

- [M51: circdist_gross_proof_outer_round98_exact_review_round99_20260831.md](original/M51-circdist_gross_proof_outer_round98_exact_review_round99_20260831.md "research-graph/circdist/reviews/circdist_gross_proof_outer_round98_exact_review_round99_20260831.md")
  - Coverage: Full bundled file; source lines 1–5811.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_proof_outer_round98_exact_review_round99_20260831.md`

- [M52: circdist_gross_proof_outer_round100_exact_review_round101_20260831.md](original/M52-circdist_gross_proof_outer_round100_exact_review_round101_20260831.md "research-graph/circdist/reviews/circdist_gross_proof_outer_round100_exact_review_round101_20260831.md")
  - Coverage: Full bundled file; source lines 1–1685.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_proof_outer_round100_exact_review_round101_20260831.md`

- [M53: circdist_gross_links_review_20260823.md](original/M53-circdist_gross_links_review_20260823.md "research-graph/artifacts/circdist_gross_links_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–522.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_gross_global_closure_round102_exact_review_round103_20260901.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/artifacts/circdist_gross_links_review_20260823.md`

- [M54: closure_plan.json](original/M54-closure_plan.json "research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/frontier/iter186_full_invariant/closure_plan.json")
  - Coverage: Full bundled file; source lines 1–343.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/GLOBAL_TRANSLATION_THEOREM.md
  - Source: `research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/frontier/iter186_full_invariant/closure_plan.json`

- [M55: independent_closure_check.json](original/M55-independent_closure_check.json "research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/frontier/iter186_full_invariant/independent_closure_check.json")
  - Coverage: Full bundled file; source lines 1–54.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/GLOBAL_TRANSLATION_THEOREM.md
  - Source: `research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/frontier/iter186_full_invariant/independent_closure_check.json`

- [M56: independent_check.json](original/M56-independent_check.json "research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/frontier/iter186_full_invariant_quotient/independent_check.json")
  - Coverage: Full bundled file; source lines 1–44.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/GLOBAL_TRANSLATION_THEOREM.md
  - Source: `research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/frontier/iter186_full_invariant_quotient/independent_check.json`

- [M57: assignment_independent_check.json](original/M57-assignment_independent_check.json "research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/frontier/iter186_full_invariant_quotient/assignment_independent_check.json")
  - Coverage: Full bundled file; source lines 1–15.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/GLOBAL_TRANSLATION_THEOREM.md
  - Source: `research-graph/circdist/artifacts/circdist_gross_global_closure_round102_20260901/frontier/iter186_full_invariant_quotient/assignment_independent_check.json`

- [M58: circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md](original/M58-circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md "research-graph/circdist/reviews/circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md")
  - Coverage: Full bundled file; source lines 1–1634.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md`

- [M59: circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md](original/M59-circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md "research-graph/circdist/reviews/circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md")
  - Coverage: Full bundled file; source lines 1–1626.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md`

- [M60: circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md](original/M60-circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md "research-graph/circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md")
  - Coverage: Full bundled file; source lines 1–1520.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md`

- [M61: circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md](original/M61-circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md "research-graph/circdist/reviews/circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md")
  - Coverage: Full bundled file; source lines 1–1588.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md`

- [M62: circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md](original/M62-circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md "research-graph/circdist/reviews/circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md")
  - Coverage: Full bundled file; source lines 1–2602.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md`

- [M63: circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md](original/M63-circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md "research-graph/circdist/reviews/circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md")
  - Coverage: Full bundled file; source lines 1–1991.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md`

- [M64: circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md](original/M64-circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md "research-graph/circdist/reviews/circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md")
  - Coverage: Full bundled file; source lines 1–1971.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md`

- [M65: circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md](original/M65-circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md "research-graph/circdist/reviews/circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md")
  - Coverage: Full bundled file; source lines 1–1938.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md`

- [M66: circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md](original/M66-circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md "research-graph/circdist/reviews/circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md")
  - Coverage: Full bundled file; source lines 1–2079.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md`

- [M67: circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md](original/M67-circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md "research-graph/circdist/reviews/circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md")
  - Coverage: Full bundled file; source lines 1–2119.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md`

- [M68: circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md](original/M68-circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md "research-graph/circdist/reviews/circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md")
  - Coverage: Full bundled file; source lines 1–2259.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md`

- [M69: circdist_gross_iter198_order144_continuation_round126_exact_review_round127_20260906.md](original/M69-circdist_gross_iter198_order144_continuation_round126_exact_review_round127_20260906.md "research-graph/circdist/reviews/circdist_gross_iter198_order144_continuation_round126_exact_review_round127_20260906.md")
  - Coverage: Full bundled file; source lines 1–2284.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.yaml
  - Source: `research-graph/circdist/reviews/circdist_gross_iter198_order144_continuation_round126_exact_review_round127_20260906.md`
