# Record 031 — Circuit-distance stabilization

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> min-plus matrix powers are eventually periodic

Context: A registered external-theorem assumption summarizes a min-plus matrix theorem as unqualified eventual periodicity. It is an auxiliary asymptotic assertion, not the finite-round transfer identity.

Locator: Archived external-theorem assumption registered 23 August 2026, assumption statement, lines 21–23.

## 2. Witness / adjudication

Min-plus powers generally have linear drift. Eventual periodicity of the unshifted sequence requires normalization and additional hypotheses; it does not hold for every min-plus matrix.

For the one-by-one min-plus matrix A=[1], min-plus multiplication adds its only entry. By induction A^{⊙R}=[R] for every positive integer R. For any period p>0, A^{⊙(R+p)}=[R+p]≠[R]=A^{⊙R}, at every R. This exactly refutes the unqualified statement. It does not refute the finite-round transfer formula or the more careful zero-cycle normalized argument for the specific transfer matrices.

Scope: statement_false

安装为external-theorem的无条件“min-plus matrix powers are eventually periodic”删掉漂移/归一化和定理适用条件。A=[1]的R次min-plus幂为[R]，精确反驳原泛称。

维持旧裁定，错误对象仅为安装的外部定理摘要；不得扩大成有限R的transfer公式错误。

## 3. Evidence and verification

1×1矩阵归纳直接证明；上轮精确check已通过，本轮核原节点条件未把泛称限定于零漂移矩阵。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-CIRCDIST.sat.transfer.yaml](original/M01-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M02-circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md) — inherited_sanitized_source
- [M03-CIRCDIST.sat.transfer.yaml](original/M03-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
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
- [M13-CIRCDIST_PROBLEMS.md](original/M13-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M14-SAT_RESCOPE_20260822.md](original/M14-SAT_RESCOPE_20260822.md) — inherited_sanitized_source
- [M15-circdist_sat_transfer_proof_20260823.md](original/M15-circdist_sat_transfer_proof_20260823.md) — inherited_sanitized_source
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
- [R01-M01-CIRCDIST.sat.transfer.yaml.context.md](reconciliation_sources/R01-M01-CIRCDIST.sat.transfer.yaml.context.md) — reconciliation_source_window
- [R02-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md](reconciliation_sources/R02-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
