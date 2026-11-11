# 031 — Min-plus powers generally have linear drift. Eventual periodicity of the unshifted sequence requires normalization and additional hypotheses; it does not hold for every min-plus matrix.

**Research problem:** P05 — Circuit-distance stabilization

## Original statement

> min-plus matrix powers are eventually periodic

**Context:** A registered external-theorem assumption summarizes a min-plus matrix theorem as unqualified eventual periodicity. It is an auxiliary asymptotic assertion, not the finite-round transfer identity.

**Original locator:** Archived external-theorem assumption registered 23 August 2026, assumption statement, lines 21–23.

## Why it is an error

Min-plus powers generally have linear drift. Eventual periodicity of the unshifted sequence requires normalization and additional hypotheses; it does not hold for every min-plus matrix.

## Witness / evidence

For the one-by-one min-plus matrix A=[1], min-plus multiplication adds its only entry. By induction A^{⊙R}=[R] for every positive integer R. For any period p>0, A^{⊙(R+p)}=[R+p]≠[R]=A^{⊙R}, at every R. This exactly refutes the unqualified statement. It does not refute the finite-round transfer formula or the more careful zero-cycle normalized argument for the specific transfer matrices.

## Scope

statement_false

## Classification

- II: 数学知识错误. 外部定理被表述成不加限定的 min-plus 幂最终周期性，漏掉可能的线性漂移/归一化。A=[1] 的幂为 [R]，直接否定所述定理内容。

II/IV 边界：引用的外部定理本身被写成错误的无条件命题，归 II；与一个正确定理被用于错误实例相区分。 2026-09-23 核对：注册项自称引用外部定理、未在项目重推；早期有限条件推导不等于无条件安装声明的生成事件，保持 II。

## Adjudication notes

Min-plus powers generally have linear drift. Eventual periodicity of the unshifted sequence requires normalization and additional hypotheses; it does not hold for every min-plus matrix.

For the one-by-one min-plus matrix A=[1], min-plus multiplication adds its only entry. By induction A^{⊙R}=[R] for every positive integer R. For any period p>0, A^{⊙(R+p)}=[R+p]≠[R]=A^{⊙R}, at every R. This exactly refutes the unqualified statement. It does not refute the finite-round transfer formula or the more careful zero-cycle normalized argument for the specific transfer matrices.

Scope: statement_false

安装为external-theorem的无条件“min-plus matrix powers are eventually periodic”删掉漂移/归一化和定理适用条件。A=[1]的R次min-plus幂为[R]，精确反驳原泛称。

维持旧裁定，错误对象仅为安装的外部定理摘要；不得扩大成有限R的transfer公式错误。

## Original materials

- [original/M01-CIRCDIST.sat.transfer.yaml](original/M01-CIRCDIST.sat.transfer.yaml)
- [original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md)
- [original/M03-CIRCDIST.sat.transfer.yaml](original/M03-CIRCDIST.sat.transfer.yaml)
- [original/M05-circdist_sat_transfer_proof_20260823.md](original/M05-circdist_sat_transfer_proof_20260823.md)
- [original/M06-circdist_sat_transfer_rereview_20260823.md](original/M06-circdist_sat_transfer_rereview_20260823.md)
- [original/M07-circdist_transfer_bridgefold_20260823.md](original/M07-circdist_transfer_bridgefold_20260823.md)
- [original/M08-circdist_sat_recon_20260820.md](original/M08-circdist_sat_recon_20260820.md)
- [original/M09-circdist_sat_transfer_amendment1_20260823.md](original/M09-circdist_sat_transfer_amendment1_20260823.md)
- [original/M10-circdist_sat_transfer_review_20260823.md](original/M10-circdist_sat_transfer_review_20260823.md)
- [original/M11-SAT_RESCOPE_20260822.md](original/M11-SAT_RESCOPE_20260822.md)
- [original/M12-circdist_sat_root_proved_adjudication_20260823.md](original/M12-circdist_sat_root_proved_adjudication_20260823.md)
- [original/M13-CIRCDIST_PROBLEMS.md](original/M13-CIRCDIST_PROBLEMS.md)
- [original/M14-SAT_RESCOPE_20260822.md](original/M14-SAT_RESCOPE_20260822.md)
- [original/M15-circdist_sat_transfer_proof_20260823.md](original/M15-circdist_sat_transfer_proof_20260823.md)
- [original/M16-circdist_sat_transfer_amendment1_20260823.md](original/M16-circdist_sat_transfer_amendment1_20260823.md)
- [original/M17-circdist_sat_transfer_review_20260823.md](original/M17-circdist_sat_transfer_review_20260823.md)
- [original/M18-circdist_sat_transfer_rereview_20260823.md](original/M18-circdist_sat_transfer_rereview_20260823.md)
- [original/M19-circdist_transfer_bridgefold_20260823.md](original/M19-circdist_transfer_bridgefold_20260823.md)
- [original/M20-circdist_sat_window_theorem_20260822.md](original/M20-circdist_sat_window_theorem_20260822.md)
- [original/M21-circdist_sat_window_amendment1_20260822.md](original/M21-circdist_sat_window_amendment1_20260822.md)
- [original/M22-circdist_sat_window_review_20260822.md](original/M22-circdist_sat_window_review_20260822.md)
- [original/M23-circdist_amendments4_review_20260822.md](original/M23-circdist_amendments4_review_20260822.md)
- [original/M24-circdist_readjudication_20260823.md](original/M24-circdist_readjudication_20260823.md)
- [original/M25-circdist_sat_window_selfcontained_exact_proof_20260826.md](original/M25-circdist_sat_window_selfcontained_exact_proof_20260826.md)
- [original/M26-circdist_sat_window_selfcontained_exact_review_20260826.md](original/M26-circdist_sat_window_selfcontained_exact_review_20260826.md)
- [original/M27-circdist_sat_v3_exact_text_review_20260826.md](original/M27-circdist_sat_v3_exact_text_review_20260826.md)
- [original/M28-circdist_sat_instances_window_edge_exact_review_20260826.md](original/M28-circdist_sat_instances_window_edge_exact_review_20260826.md)
- [original/M29-circdist_sat_window_downstream_scope_rebind_review_20260826.md](original/M29-circdist_sat_window_downstream_scope_rebind_review_20260826.md)
- [original/M30-circdist_sat_root_assembly_20260823.md](original/M30-circdist_sat_root_assembly_20260823.md)
- [original/M31-circdist_sat_root_review_20260823.md](original/M31-circdist_sat_root_review_20260823.md)
- [original/M32-circdist_sat_root_proved_adjudication_20260823.md](original/M32-circdist_sat_root_proved_adjudication_20260823.md)
- [original/M33-proof_dag_check.py](original/M33-proof_dag_check.py)
- [original/M34-SCHEDULER.yaml](original/M34-SCHEDULER.yaml)
- [original/M35-circdist_sat_recon_20260820.md](original/M35-circdist_sat_recon_20260820.md)
- [original/M36-evidence_closure_check.py](original/M36-evidence_closure_check.py)
- [original/M37-check_circdist_migration.py](original/M37-check_circdist_migration.py)
- [original/M38-check_event_append_only.py](original/M38-check_event_append_only.py)
- [original/context/R01-M01-CIRCDIST.sat.transfer.yaml.context.md](original/context/R01-M01-CIRCDIST.sat.transfer.yaml.context.md)
- [original/context/R02-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md](original/context/R02-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md)

[Back to all 65 errors](../../README.md)
