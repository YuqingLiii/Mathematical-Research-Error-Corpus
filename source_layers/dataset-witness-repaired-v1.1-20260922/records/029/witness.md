# Record 029 — Circuit-distance stabilization

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> **Why this is a gap and not a result:** Definition 3.5 is introduced in *this* document. If a
> reviewer prefers a different canonical split — for instance one defined by a family of *code-state*
> inputs rather than logical-basis inputs, which is a genuinely different family because
> `|0⟩^{⊗n}` is not a code state and makes the round-0 X-check outcomes random — then `𝒟_X` changes
> and, in principle, so could `d_R`. Three things reduce the risk and should be recorded with the
> sub-claim: (a) whatever `𝒟` is chosen, if it contains the Definition-2.7 set and is contained in
> `V`, then Proposition 3.7's argument goes through verbatim, because `F^X` annihilates *all* of
> `V_X` and all of `𝒟_Z`; (b) the split is forced on the Z-side by 3.6's dimension count; (c) it is
> confirmed numerically on 18 instances including a dependent generating set (11.2). **What is not
> established is that Definition 3.5 is the split the frozen 公共定义 intends.** This is precisely the
> hole the window theorem labelled W-G3 and its review answered with S3′; §3 answers it more sharply,
> but the answer rests on a definition a reviewer must ratify.

Context: The draft proposes robustness under replacing its canonical detector space D by any intermediate space D' containing the short detector list and contained in the larger deterministic-parity space V. The latter also contains logical observable directions.

Locator: Proof draft dated 23 August 2026, section 12, proposed mitigation (a), lines 1426–1437.

## 2. Witness / adjudication

Containment in V permits adding a parity with a logical-observable component. A fault that is logical and undetected by the original detectors can then be detected by the new parity, so the claimed unchanged proof does not apply.

Let λ be a logical observable and P_X the round-zero redundant-X-check parity of Steane with an added dependent X-check row. Set D'=span(D_b)+span(D_a)+span(P_X+λ). This contains the original short detector set and lies in V. A projected logical witness flips P_X by 0 and λ by 1, hence flips P_X+λ and is detected by D'. The archived exact example changes distance from 2 to 3 at R=2 and from 2 to 4 at R=3. The safe hypothesis is D'⊆D, not merely D'⊆V. The failure of the inference follows already from the displayed logical component; the canonical-space theorem is unaffected.

Scope: argument_invalid

D′⊆V允许加入含logical observable的parity，不等价于D′⊆D。原文明确称较大范围下原论证verbatim适用；该投影实际会被新增parity检测。

维持已确认错误；旧review与amendment均将V改为D，本次无新反证推翻该结论。

## 3. Evidence and verification

逐式核对P_X+lambda作用；沿用已精确重跑的Steane距离2→3/4审计，不将本轮未重跑写成缺材料。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_sat_transfer_proof_20260823.md](original/M01-circdist_sat_transfer_proof_20260823.md) — inherited_sanitized_source
- [M02-circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md) — inherited_sanitized_source
- [M03-circdist_sat_transfer_amendment1_20260823.md](original/M03-circdist_sat_transfer_amendment1_20260823.md) — inherited_sanitized_source
- [M04-agent-a650547b7eb957124.jsonl.readable.md](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — inherited_sanitized_source
- [M04-agent-a650547b7eb957124.jsonl.visible.json](original/M04-agent-a650547b7eb957124.jsonl.visible.json) — inherited_sanitized_source
- [M05-SAT_RESCOPE_20260822.md](original/M05-SAT_RESCOPE_20260822.md) — inherited_sanitized_source
- [M06-CIRCDIST_PROBLEMS.md](original/M06-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M07-circdist_sat_window_theorem_20260822.md](original/M07-circdist_sat_window_theorem_20260822.md) — inherited_sanitized_source
- [M08-circdist_sat_recon_20260820.md](original/M08-circdist_sat_recon_20260820.md) — inherited_sanitized_source
- [M09-circdist_sat_window_amendment1_20260822.md](original/M09-circdist_sat_window_amendment1_20260822.md) — inherited_sanitized_source
- [M10-circdist_sat_window_review_20260822.md](original/M10-circdist_sat_window_review_20260822.md) — inherited_sanitized_source
- [M11-circdist_lift_nonint_proof_20260820.md](original/M11-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M12-CIRCDIST.sat.transfer.yaml](original/M12-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M13-CIRCDIST.sat.transfer.yaml](original/M13-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M14-CIRCDIST_PROBLEMS.md](original/M14-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M15-SAT_RESCOPE_20260822.md](original/M15-SAT_RESCOPE_20260822.md) — inherited_sanitized_source
- [M16-circdist_sat_transfer_review_20260823.md](original/M16-circdist_sat_transfer_review_20260823.md) — inherited_sanitized_source
- [M17-circdist_sat_transfer_rereview_20260823.md](original/M17-circdist_sat_transfer_rereview_20260823.md) — inherited_sanitized_source
- [M18-circdist_transfer_bridgefold_20260823.md](original/M18-circdist_transfer_bridgefold_20260823.md) — inherited_sanitized_source
- [M19-circdist_sat_window_theorem_20260822.md](original/M19-circdist_sat_window_theorem_20260822.md) — inherited_sanitized_source
- [M20-circdist_sat_window_amendment1_20260822.md](original/M20-circdist_sat_window_amendment1_20260822.md) — inherited_sanitized_source
- [M21-circdist_sat_window_review_20260822.md](original/M21-circdist_sat_window_review_20260822.md) — inherited_sanitized_source
- [M22-circdist_amendments4_review_20260822.md](original/M22-circdist_amendments4_review_20260822.md) — inherited_sanitized_source
- [M23-circdist_readjudication_20260823.md](original/M23-circdist_readjudication_20260823.md) — inherited_sanitized_source
- [M24-circdist_sat_window_selfcontained_exact_proof_20260826.md](original/M24-circdist_sat_window_selfcontained_exact_proof_20260826.md) — inherited_sanitized_source
- [M25-circdist_sat_window_selfcontained_exact_review_20260826.md](original/M25-circdist_sat_window_selfcontained_exact_review_20260826.md) — inherited_sanitized_source
- [M26-circdist_sat_v3_exact_text_review_20260826.md](original/M26-circdist_sat_v3_exact_text_review_20260826.md) — inherited_sanitized_source
- [M27-circdist_sat_instances_window_edge_exact_review_20260826.md](original/M27-circdist_sat_instances_window_edge_exact_review_20260826.md) — inherited_sanitized_source
- [M28-circdist_sat_window_downstream_scope_rebind_review_20260826.md](original/M28-circdist_sat_window_downstream_scope_rebind_review_20260826.md) — inherited_sanitized_source
- [M29-circdist_sat_root_assembly_20260823.md](original/M29-circdist_sat_root_assembly_20260823.md) — inherited_sanitized_source
- [M30-circdist_sat_root_review_20260823.md](original/M30-circdist_sat_root_review_20260823.md) — inherited_sanitized_source
- [M31-circdist_sat_root_proved_adjudication_20260823.md](original/M31-circdist_sat_root_proved_adjudication_20260823.md) — inherited_sanitized_source
- [M32-CIRCDIST.sat.transfer.yaml](original/M32-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M33-proof_dag_check.py](original/M33-proof_dag_check.py) — inherited_sanitized_source
- [M34-SCHEDULER.yaml](original/M34-SCHEDULER.yaml) — inherited_sanitized_source
- [M35-circdist_sat_recon_20260820.md](original/M35-circdist_sat_recon_20260820.md) — inherited_sanitized_source
- [M36-evidence_closure_check.py](original/M36-evidence_closure_check.py) — inherited_sanitized_source
- [M37-check_circdist_migration.py](original/M37-check_circdist_migration.py) — inherited_sanitized_source
- [M38-check_event_append_only.py](original/M38-check_event_append_only.py) — inherited_sanitized_source
- [M39-circdist_sat_transfer_review_20260823.md](original/M39-circdist_sat_transfer_review_20260823.md) — inherited_sanitized_source
- [M40-circdist_sat_transfer_proof_20260823.md](original/M40-circdist_sat_transfer_proof_20260823.md) — inherited_sanitized_source
- [R01-M01-circdist_sat_transfer_proof_20260823.md.context.md](reconciliation_sources/R01-M01-circdist_sat_transfer_proof_20260823.md.context.md) — reconciliation_source_window
- [R02-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md](reconciliation_sources/R02-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
