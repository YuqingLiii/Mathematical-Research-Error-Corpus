# Record 069 — Circuit-distance stabilization

**Final admission:** excluded. **Overclaim:** not_applicable.

## 1. Original statement and context

> For each fixed legal single-round single-ancilla CSS schedule M under the stated ideal temporal
>   boundaries and unit-fault model, there is an explicitly constructible finite min-plus transfer
>   system (u,A,v) such that d_R(M) = u^T min-plus A^R min-plus v for every R, with the two CSS
>   sectors, boundary conditions, unreachable states, and logical terminal condition represented
>   exactly.

Context: The installed transfer theorem quantifies over CSS schedules without explicitly requiring at least one encoded logical qubit. Its terminal vector is finite precisely for nonzero logical terminal classes.

Locator: Archived theorem statement installed on 23 August 2026, transfer claim, lines 6–10.

## 2. Witness / adjudication

This allegation is **not a positive mathematical-error record** in this release. The old witness is retained in history/input_witness.md for accountability, not endorsed here.

k=0时无非零逻辑终端的计算正确，但不会使有限min-plus表示等式错误：允许∞且min(empty)=∞时两边均∞。正文明确k≥1，且明确采用扩展值空集最小值约定；安装摘要未重写k域属于精度/自足性问题，现有witness未提供错误数学结论。

旧end-to-end审计原判是“fair summary beside dossier / not standalone enough for PROVED”，不是数学等式反例。后续把它录为独立数学错误不成立；此处纠正的是解释层，不是材料恢复状态。

## 3. Evidence and verification

手算n=2,ranks1+1,k=0及空终端支撑；对照正文范围和∞约定，不以缺新实验判定。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-CIRCDIST.sat.transfer.yaml](original/M01-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M02-circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md) — inherited_sanitized_source
- [M03-circdist_sat_transfer_proof_20260823.md](original/M03-circdist_sat_transfer_proof_20260823.md) — inherited_sanitized_source
- [M04-agent-a650547b7eb957124.jsonl.readable.md](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — inherited_sanitized_source
- [M04-agent-a650547b7eb957124.jsonl.visible.json](original/M04-agent-a650547b7eb957124.jsonl.visible.json) — inherited_sanitized_source
- [M05-circdist_sat_transfer_proof_20260823.md](original/M05-circdist_sat_transfer_proof_20260823.md) — inherited_sanitized_source
- [M06-circdist_sat_transfer_rereview_20260823.md](original/M06-circdist_sat_transfer_rereview_20260823.md) — inherited_sanitized_source
- [M07-circdist_transfer_bridgefold_20260823.md](original/M07-circdist_transfer_bridgefold_20260823.md) — inherited_sanitized_source
- [M08-circdist_sat_recon_20260820.md](original/M08-circdist_sat_recon_20260820.md) — inherited_sanitized_source
- [M09-circdist_sat_transfer_amendment1_20260823.md](original/M09-circdist_sat_transfer_amendment1_20260823.md) — inherited_sanitized_source
- [M10-circdist_sat_transfer_review_20260823.md](original/M10-circdist_sat_transfer_review_20260823.md) — inherited_sanitized_source
- [M11-SAT_RESCOPE_20260822.md](original/M11-SAT_RESCOPE_20260822.md) — inherited_sanitized_source
- [M12-circdist_sat_root_proved_adjudication_20260823.md](original/M12-circdist_sat_root_proved_adjudication_20260823.md) — inherited_sanitized_source
- [M13-CIRCDIST.sat.transfer.yaml](original/M13-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M14-CIRCDIST_PROBLEMS.md](original/M14-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M15-SAT_RESCOPE_20260822.md](original/M15-SAT_RESCOPE_20260822.md) — inherited_sanitized_source
- [M16-circdist_sat_transfer_amendment1_20260823.md](original/M16-circdist_sat_transfer_amendment1_20260823.md) — inherited_sanitized_source
- [M17-circdist_sat_transfer_review_20260823.md](original/M17-circdist_sat_transfer_review_20260823.md) — inherited_sanitized_source
- [M18-circdist_sat_transfer_rereview_20260823.md](original/M18-circdist_sat_transfer_rereview_20260823.md) — inherited_sanitized_source
- [M19-circdist_transfer_bridgefold_20260823.md](original/M19-circdist_transfer_bridgefold_20260823.md) — inherited_sanitized_source
- [M20-circdist_sat_window_theorem_20260822.md](original/M20-circdist_sat_window_theorem_20260822.md) — inherited_sanitized_source
- [M21-circdist_sat_window_amendment1_20260822.md](original/M21-circdist_sat_window_amendment1_20260822.md) — inherited_sanitized_source
- [M22-circdist_sat_window_review_20260822.md](original/M22-circdist_sat_window_review_20260822.md) — inherited_sanitized_source
- [M23-circdist_amendments4_review_20260822.md](original/M23-circdist_amendments4_review_20260822.md) — inherited_sanitized_source
- [M24-circdist_readjudication_20260823.md](original/M24-circdist_readjudication_20260823.md) — inherited_sanitized_source
- [M25-circdist_sat_window_selfcontained_exact_proof_20260826.md](original/M25-circdist_sat_window_selfcontained_exact_proof_20260826.md) — inherited_sanitized_source
- [M26-circdist_sat_window_selfcontained_exact_review_20260826.md](original/M26-circdist_sat_window_selfcontained_exact_review_20260826.md) — inherited_sanitized_source
- [M27-circdist_sat_v3_exact_text_review_20260826.md](original/M27-circdist_sat_v3_exact_text_review_20260826.md) — inherited_sanitized_source
- [M28-circdist_sat_instances_window_edge_exact_review_20260826.md](original/M28-circdist_sat_instances_window_edge_exact_review_20260826.md) — inherited_sanitized_source
- [M29-circdist_sat_window_downstream_scope_rebind_review_20260826.md](original/M29-circdist_sat_window_downstream_scope_rebind_review_20260826.md) — inherited_sanitized_source
- [M30-circdist_sat_root_assembly_20260823.md](original/M30-circdist_sat_root_assembly_20260823.md) — inherited_sanitized_source
- [M31-circdist_sat_root_review_20260823.md](original/M31-circdist_sat_root_review_20260823.md) — inherited_sanitized_source
- [M32-circdist_sat_root_proved_adjudication_20260823.md](original/M32-circdist_sat_root_proved_adjudication_20260823.md) — inherited_sanitized_source
- [M33-proof_dag_check.py](original/M33-proof_dag_check.py) — inherited_sanitized_source
- [M34-SCHEDULER.yaml](original/M34-SCHEDULER.yaml) — inherited_sanitized_source
- [M35-circdist_sat_recon_20260820.md](original/M35-circdist_sat_recon_20260820.md) — inherited_sanitized_source
- [M36-evidence_closure_check.py](original/M36-evidence_closure_check.py) — inherited_sanitized_source
- [M37-check_circdist_migration.py](original/M37-check_circdist_migration.py) — inherited_sanitized_source
- [M38-check_event_append_only.py](original/M38-check_event_append_only.py) — inherited_sanitized_source
- [M39-CIRCDIST_PROBLEMS.md](original/M39-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M40-circdist_sat_window_theorem_20260822.md](original/M40-circdist_sat_window_theorem_20260822.md) — inherited_sanitized_source
- [M41-circdist_sat_window_amendment1_20260822.md](original/M41-circdist_sat_window_amendment1_20260822.md) — inherited_sanitized_source
- [M42-circdist_sat_window_review_20260822.md](original/M42-circdist_sat_window_review_20260822.md) — inherited_sanitized_source
- [M43-circdist_lift_nonint_proof_20260820.md](original/M43-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M44-CIRCDIST.sat.transfer.yaml](original/M44-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [R01-M01-CIRCDIST.sat.transfer.yaml.context.md](reconciliation_sources/R01-M01-CIRCDIST.sat.transfer.yaml.context.md) — reconciliation_source_window
- [R02-M03-circdist_sat_transfer_proof_20260823.md.context.md](reconciliation_sources/R02-M03-circdist_sat_transfer_proof_20260823.md.context.md) — reconciliation_source_window
- [R03-M03-circdist_sat_transfer_proof_20260823.md.context.md](reconciliation_sources/R03-M03-circdist_sat_transfer_proof_20260823.md.context.md) — reconciliation_source_window
- [R04-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md](reconciliation_sources/R04-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md) — reconciliation_source_window
- [R05-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md](reconciliation_sources/R05-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).

## v1.1 witness repair review

用 k=0、没有逻辑终端反驳 min-plus 表示。

原文允许扩展值 ∞ 且正文明确 k≥1；即使扩展到 k=0，空集最小值下两边都是 ∞。

原例不是等式反例；摘要自足性不当作另一条数学错误。
