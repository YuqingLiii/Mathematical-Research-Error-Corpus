# Record 070 — Circuit-distance stabilization

**Final admission:** excluded. **Overclaim:** not_applicable.

## 1. Original statement and context

> exactly. The d_R so computed is moreover invariant under the counting and detector-split
>   conventions the surrounding route composes across: by Lemma 2.9 it is the same whether a witness
>   is counted by its number of elementary faults, collisions permitted, or by its number of faulty
>   locations;

Context: The installed claim states equality of collision-permitting elementary-fault counts and occupied-location counts. The dossier proves it by multiplying faults at a shared location inside the full local Pauli group, with unit cost for every nonidentity assignment.

Locator: Archived theorem statement installed on 23 August 2026, counting-invariance clause, lines 10–13.

## 2. Witness / adjudication

This allegation is **not a positive mathematical-error record** in this release. The old witness is retained in history/input_witness.md for accountability, not endorsed here.

非群fault alphabet反例数学上正确，但原claim引用stated unit-fault model与Lemma2.9；同一安装YAML的caveats第47–54行明确完整Pauli GROUP及均匀单位代价，甚至明确讲非群时不成立。不能抽掉紧邻限定再指控无条件推广。

接回旧完整节点后发现原context本来已排除此反例域。之前只摘claim字符串形成的独立错误标注应纠正，不把已知正确lemma记作生成错误。

## 3. Evidence and verification

原节点条件、Lemma2.9全群合并论证与反例域逐项对照；全部材料早已在本地，不是缺恢复。

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
- [R02-M01-CIRCDIST.sat.transfer.yaml.context.md](reconciliation_sources/R02-M01-CIRCDIST.sat.transfer.yaml.context.md) — reconciliation_source_window
- [R03-M03-circdist_sat_transfer_proof_20260823.md.context.md](reconciliation_sources/R03-M03-circdist_sat_transfer_proof_20260823.md.context.md) — reconciliation_source_window
- [R04-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md](reconciliation_sources/R04-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).

## v1.1 witness repair review

用非群 fault alphabet 反驳完整 Pauli 群模型的结论。

同一安装节点紧邻 caveats 已写完整群与均匀单位代价，并明确非群不适用。

旧 witness 超出原始模型范围。
