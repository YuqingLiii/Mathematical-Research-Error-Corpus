# Record 034 — Circuit versus effective distance

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> > In graph-like detector error models with fixed boundaries, a proven necessary-and-sufficient
> > structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when
> > d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma
> > of the length of the shortest closed spacetime lift of gamma", with zero time-direction
> > voltage/monodromy as the equal-weight liftability condition; the criterion recovers the
> > non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit
> > interleaved example with d_circ > d_eff.

Context: An assembly imported a proved-under-assumptions equality criterion from a child theorem into an unrestricted root statement. The original child theorem explicitly assumes a memory experiment with R≥d rounds.

Locator: Root assembly dated 22 August 2026, root statement, lines 121–127; imported criterion in section 2.1.

## 2. Witness / adjudication

The premise R≥d is lost in the root statement and its carried-forward caveats. An implication established under that hypothesis does not by itself establish the same implication for every round count.

The assembly restates the imported result as: for every legal, measurement-consistent schedule M and R≥d, d_circ(C_R(M))=d_eff(M) iff a minimum effective logical γ has repair(γ)=0. Its root claim instead says the structural criterion characterizes d_circ=d_eff without an R quantifier or restriction. None of the assembly's listed caveats restores R≥d. This is a direct premise-versus-conclusion scope mismatch. The independent audit found no counterexample at R=1 on its d=2 test instance, so the witness invalidates the unrestricted inference, not the theorem for small R.

Scope: argument_invalid

保留为组装中的R≥d前提遗漏。原assembly明确把C1–C4解释为整个模型类上的universal，同时§2.1引用的定理要求R≥d；§6宣布携带所有限制但遗漏这一条。后续节点增加C-M7正是修复。不能用修复后的caveat否认旧组装错误。

旧审计F2与后修YAML的C-M7完整接上。上一轮把§2.1出现R条件当成全篇自然继承，忽略assembly自己独立列出的根量词及caveat清单，是误降级。

## 3. Evidence and verification

原根、显式量词解释、子定理和修复边界逐项对账；不需要数值小R反例才能确认论证未携带假设。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_lift_root_assembly_20260822.md](original/M01-circdist_lift_root_assembly_20260822.md) — inherited_sanitized_source
- [M02-circdist_lift_root_review_20260822.md](original/M02-circdist_lift_root_review_20260822.md) — inherited_sanitized_source
- [M03-circdist_lift_iff_proof_20260820.md](original/M03-circdist_lift_iff_proof_20260820.md) — inherited_sanitized_source
- [M04-agent-a54f4eb22e936ab7c.jsonl.readable.md](original/M04-agent-a54f4eb22e936ab7c.jsonl.readable.md) — inherited_sanitized_source
- [M04-agent-a54f4eb22e936ab7c.jsonl.visible.json](original/M04-agent-a54f4eb22e936ab7c.jsonl.visible.json) — inherited_sanitized_source
- [M05-CIRCDIST.lift.yaml](original/M05-CIRCDIST.lift.yaml) — inherited_sanitized_source
- [M06-CIRCDIST.lift.iff.yaml](original/M06-CIRCDIST.lift.iff.yaml) — inherited_sanitized_source
- [M07-CIRCDIST.lift.nonint.yaml](original/M07-CIRCDIST.lift.nonint.yaml) — inherited_sanitized_source
- [M08-CIRCDIST.lift.gap-example.yaml](original/M08-CIRCDIST.lift.gap-example.yaml) — inherited_sanitized_source
- [M09-circdist_lift_iff_proof_20260820.md](original/M09-circdist_lift_iff_proof_20260820.md) — inherited_sanitized_source
- [M10-circdist_lift_iff_amendment1_20260820.md](original/M10-circdist_lift_iff_amendment1_20260820.md) — inherited_sanitized_source
- [M11-circdist_lift_iff_amendment2_20260820.md](original/M11-circdist_lift_iff_amendment2_20260820.md) — inherited_sanitized_source
- [M12-circdist_lift_nonint_proof_20260820.md](original/M12-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M13-circdist_lift_proofs_review_20260820.md](original/M13-circdist_lift_proofs_review_20260820.md) — inherited_sanitized_source
- [M14-circdist_amendments_review_20260820.md](original/M14-circdist_amendments_review_20260820.md) — inherited_sanitized_source
- [M15-circdist_amendments2_review_20260820.md](original/M15-circdist_amendments2_review_20260820.md) — inherited_sanitized_source
- [M16-circdist_numerical_review_20260820.md](original/M16-circdist_numerical_review_20260820.md) — inherited_sanitized_source
- [M17-circdist_lift_d3gate_20260820.md](original/M17-circdist_lift_d3gate_20260820.md) — inherited_sanitized_source
- [M18-CIRCDIST_PROBLEMS.md](original/M18-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M19-circdist_lift_root_assembly_20260822.md](original/M19-circdist_lift_root_assembly_20260822.md) — inherited_sanitized_source
- [M20-proof_dag_v6.py](original/M20-proof_dag_v6.py) — inherited_sanitized_source
- [M21-ksum_L2_phase27_shared_no_rule7_review_20260721.md](original/M21-ksum_L2_phase27_shared_no_rule7_review_20260721.md) — inherited_sanitized_source
- [M22-circdist_lift_litverify2_20260820.md](original/M22-circdist_lift_litverify2_20260820.md) — inherited_sanitized_source
- [R01-M01-circdist_lift_root_assembly_20260822.md.context.md](reconciliation_sources/R01-M01-circdist_lift_root_assembly_20260822.md.context.md) — reconciliation_source_window
- [R02-M01-circdist_lift_root_assembly_20260822.md.context.md](reconciliation_sources/R02-M01-circdist_lift_root_assembly_20260822.md.context.md) — reconciliation_source_window
- [R03-M01-circdist_lift_root_assembly_20260822.md.context.md](reconciliation_sources/R03-M01-circdist_lift_root_assembly_20260822.md.context.md) — reconciliation_source_window
- [R04-M02-circdist_lift_root_review_20260822.md.context.md](reconciliation_sources/R04-M02-circdist_lift_root_review_20260822.md.context.md) — reconciliation_source_window
- [R05-M05-CIRCDIST.lift.yaml.context.md](reconciliation_sources/R05-M05-CIRCDIST.lift.yaml.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
