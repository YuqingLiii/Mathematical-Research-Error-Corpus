# Record 066 — Optimal circuit distance of the Gross code

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> UNSAT of the checked quotient plus sound base exclusions would prove every legal schedule has a weight<=10 direct mechanism; SAT supplies only a canonical candidate.

Context: A finite search quotient appended lexicographic symmetry-breaking clauses to an exclusion registry. The quotient was intended to cover the full legal schedule class. The registry had not been closed under the 72-element translation group.

Locator: Archived computational certificate dated 1 September 2026, iteration-185 quotient, finite_coverage_theorem.root_use.

## 2. Witness / adjudication

An orbit can be replaced by its lexicographically least member only if the base formula remains true under the group action. Soundness of individual exclusion clauses does not imply invariance of their installed subset.

Let B be the base formula with 330 selectors and 14,484 untranslated block cuts, and let L be its 71 nonidentity translation lex-leader constraints. The archived independent counter-scenario provides a legal base model S. Among all 72 translated schedules, only the identity translate satisfies B. The lexicographically least translate is at δ=(1,5), and it violates 75 installed block cuts. Therefore this orbit has a B-model but no model of B∧L. The required implication B(S)⇒B(δS) fails, so orbit-wise coverage and lifting an UNSAT result are unjustified. Both old formulas happened to be SAT; this witness invalidates the coverage theorem rather than claiming the quotient itself is UNSAT.

Scope: argument_invalid

旧iteration185的部分排除库未在平移作用下闭合，却声称加lex leader后有全局UNSAT提升。其缺少的不只是实验覆盖，而是B(S)⇒B(δS)这一必要桥梁；旧审计给出具体轨道反例，并有原作者撤回该coverage声明。

确认已有数学审计，不再以本轮未重跑为待核。需诚实保留复现粒度：审计第92行明确说其临时独立实现/输出在归档前删除，不能说该特定416062-literal assignment仍在；其源公式、算法、哈希、轨道计数和撤回链均在。

## 3. Evidence and verification

原installed certificate+旧独立精确审计+修正定理三方对账；接受历史核验，明确未重新求解百万子句模型。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false. The historical reviewer deleted temporary model assignments at the time; the archived audit and scoped retraction are preserved, not a surviving assignment fixture.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-independent_check.json](original/M01-independent_check.json) — inherited_sanitized_source
- [M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md](original/M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md) — inherited_sanitized_source
- [M03-GLOBAL_TRANSLATION_THEOREM.md](original/M03-GLOBAL_TRANSLATION_THEOREM.md) — inherited_sanitized_source
- [M04-CIRCDIST.gross.yaml](original/M04-CIRCDIST.gross.yaml) — inherited_sanitized_source
- [M05-rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl.readable.md](original/M05-rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M05-rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl.visible.json](original/M05-rollout-2026-09-01T00-22-48-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M06-scheduler.yaml](original/M06-scheduler.yaml) — inherited_sanitized_source
- [M07-circdist_gross_round80_whole_registry_exact_review_20260830.md](original/M07-circdist_gross_round80_whole_registry_exact_review_20260830.md) — inherited_sanitized_source
- [M08-circdist_gross_round78_cross_registry_exact_review_20260830.md](original/M08-circdist_gross_round78_cross_registry_exact_review_20260830.md) — inherited_sanitized_source
- [M09-circdist_gross_round76_online_generalizing_exact_review_20260829.md](original/M09-circdist_gross_round76_online_generalizing_exact_review_20260829.md) — inherited_sanitized_source
- [M10-circdist_gross_round74_online_generalizing_exact_review_20260829.md](original/M10-circdist_gross_round74_online_generalizing_exact_review_20260829.md) — inherited_sanitized_source
- [M11-circdist_gross_round72_generalization_exact_review_20260829.md](original/M11-circdist_gross_round72_generalization_exact_review_20260829.md) — inherited_sanitized_source
- [M12-circdist_gross_block_minimization_exact_review_20260829.md](original/M12-circdist_gross_block_minimization_exact_review_20260829.md) — inherited_sanitized_source
- [M13-circdist_dstar_hunt3_20260828.md](original/M13-circdist_dstar_hunt3_20260828.md) — inherited_sanitized_source
- [M14-circdist_gross_morphing_scope_ruling_20260826.md](original/M14-circdist_gross_morphing_scope_ruling_20260826.md) — inherited_sanitized_source
- [M15-CIRCDIST.gross.yaml](original/M15-CIRCDIST.gross.yaml) — inherited_sanitized_source
- [M16-legacy_DAG_PROTOCOL.md](original/M16-legacy_DAG_PROTOCOL.md) — inherited_sanitized_source
- [M17-circdist_gross_verdict_20260823.md](original/M17-circdist_gross_verdict_20260823.md) — inherited_sanitized_source
- [M18-SHA256SUMS.txt](original/M18-SHA256SUMS.txt) — inherited_sanitized_source
- [M19-circdist_gross_final_decision_20260823.md](original/M19-circdist_gross_final_decision_20260823.md) — inherited_sanitized_source
- [M20-SHA256SUMS.txt](original/M20-SHA256SUMS.txt) — inherited_sanitized_source
- [M21-circdist_gross_candidate_decision_20260822.md](original/M21-circdist_gross_candidate_decision_20260822.md) — inherited_sanitized_source
- [M22-SHA256SUMS.txt](original/M22-SHA256SUMS.txt) — inherited_sanitized_source
- [M23-circdist_gross_candidate_unsat_20260822.md](original/M23-circdist_gross_candidate_unsat_20260822.md) — inherited_sanitized_source
- [M24-circdist_gross_phicert_20260822.md](original/M24-circdist_gross_phicert_20260822.md) — inherited_sanitized_source
- [M25-circdist_sbbcert_review_20260820.md](original/M25-circdist_sbbcert_review_20260820.md) — inherited_sanitized_source
- [M26-CIRCDIST_PROBLEMS.md](original/M26-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M27-circdist_gross_sbbcert_20260820.md](original/M27-circdist_gross_sbbcert_20260820.md) — inherited_sanitized_source
- [M28-circdist_lift_iff_proof_20260820.md](original/M28-circdist_lift_iff_proof_20260820.md) — inherited_sanitized_source
- [M29-circdist_numerical_review_20260820.md](original/M29-circdist_numerical_review_20260820.md) — inherited_sanitized_source
- [M30-circdist_lift_d3gate_20260820.md](original/M30-circdist_lift_d3gate_20260820.md) — inherited_sanitized_source
- [M31-circdist_gross_g1_20260820.md](original/M31-circdist_gross_g1_20260820.md) — inherited_sanitized_source
- [M32-circdist_gross_toolfeas_20260820.md](original/M32-circdist_gross_toolfeas_20260820.md) — inherited_sanitized_source
- [M33-circdist_gross_recon_20260820.md](original/M33-circdist_gross_recon_20260820.md) — inherited_sanitized_source
- [M34-circdist_gross_verdict_review_20260823.md](original/M34-circdist_gross_verdict_review_20260823.md) — inherited_sanitized_source
- [M35-circdist_gross_links_review_20260823.md](original/M35-circdist_gross_links_review_20260823.md) — inherited_sanitized_source
- [M36-circdist_dstar_hunt1_20260823.md](original/M36-circdist_dstar_hunt1_20260823.md) — inherited_sanitized_source
- [M37-circdist_dstar_hunt2_20260823.md](original/M37-circdist_dstar_hunt2_20260823.md) — inherited_sanitized_source
- [M38-circdist_campaign4_closeout_20260823.md](original/M38-circdist_campaign4_closeout_20260823.md) — inherited_sanitized_source
- [M39-legacy_FILE_PROTOCOL.md](original/M39-legacy_FILE_PROTOCOL.md) — inherited_sanitized_source
- [M40-CAMPAIGN4_KICKOFF_20260822.md](original/M40-CAMPAIGN4_KICKOFF_20260822.md) — inherited_sanitized_source
- [M41-CAMPAIGN_CLOSEOUT_20260820.md](original/M41-CAMPAIGN_CLOSEOUT_20260820.md) — inherited_sanitized_source
- [M42-HANDOFF_20260820.md](original/M42-HANDOFF_20260820.md) — inherited_sanitized_source
- [M43-HANDOFF_20260823.md](original/M43-HANDOFF_20260823.md) — inherited_sanitized_source
- [M44-PATH_MAP.json](original/M44-PATH_MAP.json) — inherited_sanitized_source
- [M45-circdist_gross_efssc_exact_review_round87_20260830.md](original/M45-circdist_gross_efssc_exact_review_round87_20260830.md) — inherited_sanitized_source
- [M46-circdist_gross_proof_outer_exact_review_round89_20260830.md](original/M46-circdist_gross_proof_outer_exact_review_round89_20260830.md) — inherited_sanitized_source
- [M47-circdist_gross_proof_outer_exact_review_round91_20260830.md](original/M47-circdist_gross_proof_outer_exact_review_round91_20260830.md) — inherited_sanitized_source
- [M48-circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md](original/M48-circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md) — inherited_sanitized_source
- [M49-circdist_gross_proof_outer_round94_exact_review_round95_20260830.md](original/M49-circdist_gross_proof_outer_round94_exact_review_round95_20260830.md) — inherited_sanitized_source
- [M50-circdist_gross_proof_outer_round96_exact_review_round97_20260831.md](original/M50-circdist_gross_proof_outer_round96_exact_review_round97_20260831.md) — inherited_sanitized_source
- [M51-circdist_gross_proof_outer_round98_exact_review_round99_20260831.md](original/M51-circdist_gross_proof_outer_round98_exact_review_round99_20260831.md) — inherited_sanitized_source
- [M52-circdist_gross_proof_outer_round100_exact_review_round101_20260831.md](original/M52-circdist_gross_proof_outer_round100_exact_review_round101_20260831.md) — inherited_sanitized_source
- [M53-circdist_gross_links_review_20260823.md](original/M53-circdist_gross_links_review_20260823.md) — inherited_sanitized_source
- [M54-closure_plan.json](original/M54-closure_plan.json) — inherited_sanitized_source
- [M55-independent_closure_check.json](original/M55-independent_closure_check.json) — inherited_sanitized_source
- [M56-independent_check.json](original/M56-independent_check.json) — inherited_sanitized_source
- [M57-assignment_independent_check.json](original/M57-assignment_independent_check.json) — inherited_sanitized_source
- [M58-circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md](original/M58-circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md) — inherited_sanitized_source
- [M59-circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md](original/M59-circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md) — inherited_sanitized_source
- [M60-circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md](original/M60-circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md) — inherited_sanitized_source
- [M61-circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md](original/M61-circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md) — inherited_sanitized_source
- [M62-circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md](original/M62-circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md) — inherited_sanitized_source
- [M63-circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md](original/M63-circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md) — inherited_sanitized_source
- [M64-circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md](original/M64-circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md) — inherited_sanitized_source
- [M65-circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md](original/M65-circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md) — inherited_sanitized_source
- [M66-circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md](original/M66-circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md) — inherited_sanitized_source
- [M67-circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md](original/M67-circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md) — inherited_sanitized_source
- [M68-circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md](original/M68-circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md) — inherited_sanitized_source
- [M69-circdist_gross_iter198_order144_continuation_round126_exact_review_round127_20260906.md](original/M69-circdist_gross_iter198_order144_continuation_round126_exact_review_round127_20260906.md) — inherited_sanitized_source
- [R01-M01-independent_check.json.context.md](reconciliation_sources/R01-M01-independent_check.json.context.md) — reconciliation_source_window
- [R02-M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md.context.md](reconciliation_sources/R02-M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md.context.md) — reconciliation_source_window
- [R03-M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md.context.md](reconciliation_sources/R03-M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md.context.md) — reconciliation_source_window
- [R04-M03-GLOBAL_TRANSLATION_THEOREM.md.context.md](reconciliation_sources/R04-M03-GLOBAL_TRANSLATION_THEOREM.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
