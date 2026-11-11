# 066 — An orbit can be replaced by its lexicographically least member only if the base formula remains true under the group action. Soundness of individual exclusion clauses does not imply invariance of their installed subset.

**Research problem:** P07 — Optimal circuit distance of the Gross code

## Original statement

> UNSAT of the checked quotient plus sound base exclusions would prove every legal schedule has a weight<=10 direct mechanism; SAT supplies only a canonical candidate.

**Context:** A finite search quotient appended lexicographic symmetry-breaking clauses to an exclusion registry. The quotient was intended to cover the full legal schedule class. The registry had not been closed under the 72-element translation group.

**Original locator:** Archived computational certificate dated 1 September 2026, iteration-185 quotient, finite_coverage_theorem.root_use.

## Why it is an error

An orbit can be replaced by its lexicographically least member only if the base formula remains true under the group action. Soundness of individual exclusion clauses does not imply invariance of their installed subset.

## Witness / evidence

Let B be the base formula with 330 selectors and 14,484 untranslated block cuts, and let L be its 71 nonidentity translation lex-leader constraints. The archived independent counter-scenario provides a legal base model S. Among all 72 translated schedules, only the identity translate satisfies B. The lexicographically least translate is at δ=(1,5), and it violates 75 installed block cuts. Therefore this orbit has a B-model but no model of B∧L. The required implication B(S)⇒B(δS) fails, so orbit-wise coverage and lifting an UNSAT result are unjustified. Both old formulas happened to be SAT; this witness invalidates the coverage theorem rather than claiming the quotient itself is UNSAT.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 对不被平移群保持的 base 子句套用对称商覆盖推论，lex-leader 可删掉一个仍有合法 base model 的完整轨道。所需不变性前提不满足。

## Adjudication notes

An orbit can be replaced by its lexicographically least member only if the base formula remains true under the group action. Soundness of individual exclusion clauses does not imply invariance of their installed subset.

Let B be the base formula with 330 selectors and 14,484 untranslated block cuts, and let L be its 71 nonidentity translation lex-leader constraints. The archived independent counter-scenario provides a legal base model S. Among all 72 translated schedules, only the identity translate satisfies B. The lexicographically least translate is at δ=(1,5), and it violates 75 installed block cuts. Therefore this orbit has a B-model but no model of B∧L. The required implication B(S)⇒B(δS) fails, so orbit-wise coverage and lifting an UNSAT result are unjustified. Both old formulas happened to be SAT; this witness invalidates the coverage theorem rather than claiming the quotient itself is UNSAT.

Scope: argument_invalid

旧iteration185的部分排除库未在平移作用下闭合，却声称加lex leader后有全局UNSAT提升。其缺少的不只是实验覆盖，而是B(S)⇒B(δS)这一必要桥梁；旧审计给出具体轨道反例，并有原作者撤回该coverage声明。

确认已有数学审计，不再以本轮未重跑为待核。需诚实保留复现粒度：审计第92行明确说其临时独立实现/输出在归档前删除，不能说该特定416062-literal assignment仍在；其源公式、算法、哈希、轨道计数和撤回链均在。

## Original materials

- [original/M01-independent_check.json](original/M01-independent_check.json)
- [original/M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md](original/M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md)
- [original/M03-GLOBAL_TRANSLATION_THEOREM.md](original/M03-GLOBAL_TRANSLATION_THEOREM.md)
- [original/M04-CIRCDIST.gross.yaml](original/M04-CIRCDIST.gross.yaml)
- [original/M06-scheduler.yaml](original/M06-scheduler.yaml)
- [original/M07-circdist_gross_round80_whole_registry_exact_review_20260830.md](original/M07-circdist_gross_round80_whole_registry_exact_review_20260830.md)
- [original/M08-circdist_gross_round78_cross_registry_exact_review_20260830.md](original/M08-circdist_gross_round78_cross_registry_exact_review_20260830.md)
- [original/M09-circdist_gross_round76_online_generalizing_exact_review_20260829.md](original/M09-circdist_gross_round76_online_generalizing_exact_review_20260829.md)
- [original/M10-circdist_gross_round74_online_generalizing_exact_review_20260829.md](original/M10-circdist_gross_round74_online_generalizing_exact_review_20260829.md)
- [original/M11-circdist_gross_round72_generalization_exact_review_20260829.md](original/M11-circdist_gross_round72_generalization_exact_review_20260829.md)
- [original/M12-circdist_gross_block_minimization_exact_review_20260829.md](original/M12-circdist_gross_block_minimization_exact_review_20260829.md)
- [original/M13-circdist_dstar_hunt3_20260828.md](original/M13-circdist_dstar_hunt3_20260828.md)
- [original/M14-circdist_gross_morphing_scope_ruling_20260826.md](original/M14-circdist_gross_morphing_scope_ruling_20260826.md)
- [original/M15-CIRCDIST.gross.yaml](original/M15-CIRCDIST.gross.yaml)
- [original/M16-legacy_DAG_PROTOCOL.md](original/M16-legacy_DAG_PROTOCOL.md)
- [original/M17-circdist_gross_verdict_20260823.md](original/M17-circdist_gross_verdict_20260823.md)
- [original/M18-SHA256SUMS.txt](original/M18-SHA256SUMS.txt)
- [original/M19-circdist_gross_final_decision_20260823.md](original/M19-circdist_gross_final_decision_20260823.md)
- [original/M20-SHA256SUMS.txt](original/M20-SHA256SUMS.txt)
- [original/M21-circdist_gross_candidate_decision_20260822.md](original/M21-circdist_gross_candidate_decision_20260822.md)
- [original/M22-SHA256SUMS.txt](original/M22-SHA256SUMS.txt)
- [original/M23-circdist_gross_candidate_unsat_20260822.md](original/M23-circdist_gross_candidate_unsat_20260822.md)
- [original/M24-circdist_gross_phicert_20260822.md](original/M24-circdist_gross_phicert_20260822.md)
- [original/M25-circdist_sbbcert_review_20260820.md](original/M25-circdist_sbbcert_review_20260820.md)
- [original/M26-CIRCDIST_PROBLEMS.md](original/M26-CIRCDIST_PROBLEMS.md)
- [original/M27-circdist_gross_sbbcert_20260820.md](original/M27-circdist_gross_sbbcert_20260820.md)
- [original/M28-circdist_lift_iff_proof_20260820.md](original/M28-circdist_lift_iff_proof_20260820.md)
- [original/M29-circdist_numerical_review_20260820.md](original/M29-circdist_numerical_review_20260820.md)
- [original/M30-circdist_lift_d3gate_20260820.md](original/M30-circdist_lift_d3gate_20260820.md)
- [original/M31-circdist_gross_g1_20260820.md](original/M31-circdist_gross_g1_20260820.md)
- [original/M32-circdist_gross_toolfeas_20260820.md](original/M32-circdist_gross_toolfeas_20260820.md)
- [original/M33-circdist_gross_recon_20260820.md](original/M33-circdist_gross_recon_20260820.md)
- [original/M34-circdist_gross_verdict_review_20260823.md](original/M34-circdist_gross_verdict_review_20260823.md)
- [original/M35-circdist_gross_links_review_20260823.md](original/M35-circdist_gross_links_review_20260823.md)
- [original/M36-circdist_dstar_hunt1_20260823.md](original/M36-circdist_dstar_hunt1_20260823.md)
- [original/M37-circdist_dstar_hunt2_20260823.md](original/M37-circdist_dstar_hunt2_20260823.md)
- [original/M38-circdist_campaign4_closeout_20260823.md](original/M38-circdist_campaign4_closeout_20260823.md)
- [original/M39-legacy_FILE_PROTOCOL.md](original/M39-legacy_FILE_PROTOCOL.md)
- [original/M40-CAMPAIGN4_KICKOFF_20260822.md](original/M40-CAMPAIGN4_KICKOFF_20260822.md)
- [original/M41-CAMPAIGN_CLOSEOUT_20260820.md](original/M41-CAMPAIGN_CLOSEOUT_20260820.md)
- [original/M42-HANDOFF_20260820.md](original/M42-HANDOFF_20260820.md)
- [original/M43-HANDOFF_20260823.md](original/M43-HANDOFF_20260823.md)
- [original/M44-PATH_MAP.json](original/M44-PATH_MAP.json)
- [original/M45-circdist_gross_efssc_exact_review_round87_20260830.md](original/M45-circdist_gross_efssc_exact_review_round87_20260830.md)
- [original/M46-circdist_gross_proof_outer_exact_review_round89_20260830.md](original/M46-circdist_gross_proof_outer_exact_review_round89_20260830.md)
- [original/M47-circdist_gross_proof_outer_exact_review_round91_20260830.md](original/M47-circdist_gross_proof_outer_exact_review_round91_20260830.md)
- [original/M48-circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md](original/M48-circdist_gross_proof_outer_weight9_exact_review_round93_20260830.md)
- [original/M49-circdist_gross_proof_outer_round94_exact_review_round95_20260830.md](original/M49-circdist_gross_proof_outer_round94_exact_review_round95_20260830.md)
- [original/M50-circdist_gross_proof_outer_round96_exact_review_round97_20260831.md](original/M50-circdist_gross_proof_outer_round96_exact_review_round97_20260831.md)
- [original/M51-circdist_gross_proof_outer_round98_exact_review_round99_20260831.md](original/M51-circdist_gross_proof_outer_round98_exact_review_round99_20260831.md)
- [original/M52-circdist_gross_proof_outer_round100_exact_review_round101_20260831.md](original/M52-circdist_gross_proof_outer_round100_exact_review_round101_20260831.md)
- [original/M53-circdist_gross_links_review_20260823.md](original/M53-circdist_gross_links_review_20260823.md)
- [original/M54-closure_plan.json](original/M54-closure_plan.json)
- [original/M55-independent_closure_check.json](original/M55-independent_closure_check.json)
- [original/M56-independent_check.json](original/M56-independent_check.json)
- [original/M57-assignment_independent_check.json](original/M57-assignment_independent_check.json)
- [original/M58-circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md](original/M58-circdist_gross_iter187_invariant_continuation_round104_exact_review_round105_20260901.md)
- [original/M59-circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md](original/M59-circdist_gross_iter188_invariant_continuation_round106_exact_review_round107_20260901.md)
- [original/M60-circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md](original/M60-circdist_gross_iter189_invariant_continuation_round108_exact_review_round109_20260902.md)
- [original/M61-circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md](original/M61-circdist_gross_iter190_invariant_quotient_continuation_round110_exact_review_round111_20260902.md)
- [original/M62-circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md](original/M62-circdist_gross_iter191_invariant_quotient_continuation_round112_exact_review_round113_20260902.md)
- [original/M63-circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md](original/M63-circdist_gross_iter192_invariant_quotient_continuation_round114_exact_review_round115_20260902.md)
- [original/M64-circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md](original/M64-circdist_gross_iter193_invariant_quotient_continuation_round116_exact_review_round117_20260902.md)
- [original/M65-circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md](original/M65-circdist_gross_iter194_order144_continuation_round118_exact_review_round119_20260904.md)
- [original/M66-circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md](original/M66-circdist_gross_iter195_order144_continuation_round120_exact_review_round121_20260904.md)
- [original/M67-circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md](original/M67-circdist_gross_iter196_order144_continuation_round122_exact_review_round123_20260905.md)
- [original/M68-circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md](original/M68-circdist_gross_iter197_order144_continuation_round124_exact_review_round125_20260905.md)
- [original/M69-circdist_gross_iter198_order144_continuation_round126_exact_review_round127_20260906.md](original/M69-circdist_gross_iter198_order144_continuation_round126_exact_review_round127_20260906.md)
- [original/context/R01-M01-independent_check.json.context.md](original/context/R01-M01-independent_check.json.context.md)
- [original/context/R02-M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md.context.md](original/context/R02-M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md.context.md)
- [original/context/R03-M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md.context.md](original/context/R03-M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md.context.md)
- [original/context/R04-M03-GLOBAL_TRANSLATION_THEOREM.md.context.md](original/context/R04-M03-GLOBAL_TRANSLATION_THEOREM.md.context.md)

[Back to all 65 errors](../../README.md)
