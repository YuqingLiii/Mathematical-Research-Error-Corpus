# 028 — Conflict freedom is a scheduling constraint, not a proof that the circuit measures the intended stabilizers. A non-measurement-consistent interleaving can produce random check records even with no physical faults.

**Research problem:** P05 — Circuit-distance stabilization

## Original statement

>   For each fixed legal single-round single-ancilla CSS schedule M under the stated ideal temporal
>   boundaries and unit-fault model, there is an explicitly constructible finite min-plus transfer
>   system (u,A,v) such that d_R(M) = u^T min-plus A^R min-plus v for every R, with the two CSS
>   sectors, boundary conditions, unreachable states, and logical terminal condition represented
>   exactly.

**Context:** The installed claim uses a 'legal' schedule condition while the relevant legality notion guarantees only that no qubit participates in two gates simultaneously. Measurement consistency is separately required for the parity checks to be deterministic detectors.

**Original locator:** Archived theorem statement installed on 23 August 2026, transfer claim, lines 6–10.

## Why it is an error

Conflict freedom is a scheduling constraint, not a proof that the circuit measures the intended stabilizers. A non-measurement-consistent interleaving can produce random check records even with no physical faults.

## Witness / evidence

On four data qubits, take H_X=H_Z=(1,1,1,1). Prepare X ancilla a in |+> and Z ancilla b in |0>. Execute sequentially: q0→b, a→q0, a→q1, q1→b, a→q2, q2→b, a→q3, q3→b. The sequence is conflict-free, but exactly one common-support qubit has the Z CNOT before the X CNOT, an odd MC count. Back-propagating b's Z measurement creates Z on the fresh |+> ancilla a. That operator anticommutes with a's input stabilizer, so the check outcome is uniformly random and its proposed parity is not a deterministic detector. The transfer object needs MC as an additional hypothesis.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 由无冲突调度条件推出精确 detector 转移表示时缺少 measurement consistency；合法调度仍可有随机检查结果，故所述充分条件不成立。

新提出的充分性定理漏条件，归 IV；没有据此推断原题文字被读错。

## Adjudication notes

Conflict freedom is a scheduling constraint, not a proof that the circuit measures the intended stabilizers. A non-measurement-consistent interleaving can produce random check records even with no physical faults.

On four data qubits, take H_X=H_Z=(1,1,1,1). Prepare X ancilla a in |+> and Z ancilla b in |0>. Execute sequentially: q0→b, a→q0, a→q1, q1→b, a→q2, q2→b, a→q3, q3→b. The sequence is conflict-free, but exactly one common-support qubit has the Z CNOT before the X CNOT, an odd MC count. Back-propagating b's Z measurement creates Z on the fresh |+> ancilla a. That operator anticommutes with a's input stabilizer, so the check outcome is uniformly random and its proposed parity is not a deterministic detector. The transfer object needs MC as an additional hypothesis.

Scope: argument_invalid

保留为安装节点的适用条件丢失，不指控正文证明错误。原claim独立量化所有legal日程，正文Definition 2.4把legal定义为无资源冲突；MC是额外条件。安装节点caveats补了Pauli群条件却没有MC。给定4比特日程满足该legal谓词但有随机测量记录，故不能无条件导入确定detector的transfer论证。

旧审计对账成立：它明确把此项定为exact-statement scope，而非缺证明。上一轮只看到正文T1含MC便重新待核，漏了本条原对象是独立安装claim。

## Original materials

- [original/M01-CIRCDIST.sat.transfer.yaml](original/M01-CIRCDIST.sat.transfer.yaml)
- [original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md)
- [original/M03-circdist_sat_transfer_proof_20260823.md](original/M03-circdist_sat_transfer_proof_20260823.md)
- [original/M05-circdist_sat_transfer_proof_20260823.md](original/M05-circdist_sat_transfer_proof_20260823.md)
- [original/M06-circdist_sat_transfer_rereview_20260823.md](original/M06-circdist_sat_transfer_rereview_20260823.md)
- [original/M07-circdist_transfer_bridgefold_20260823.md](original/M07-circdist_transfer_bridgefold_20260823.md)
- [original/M08-circdist_sat_recon_20260820.md](original/M08-circdist_sat_recon_20260820.md)
- [original/M09-circdist_sat_transfer_amendment1_20260823.md](original/M09-circdist_sat_transfer_amendment1_20260823.md)
- [original/M10-circdist_sat_transfer_review_20260823.md](original/M10-circdist_sat_transfer_review_20260823.md)
- [original/M11-SAT_RESCOPE_20260822.md](original/M11-SAT_RESCOPE_20260822.md)
- [original/M12-circdist_sat_root_proved_adjudication_20260823.md](original/M12-circdist_sat_root_proved_adjudication_20260823.md)
- [original/M13-CIRCDIST.sat.transfer.yaml](original/M13-CIRCDIST.sat.transfer.yaml)
- [original/M14-CIRCDIST_PROBLEMS.md](original/M14-CIRCDIST_PROBLEMS.md)
- [original/M15-SAT_RESCOPE_20260822.md](original/M15-SAT_RESCOPE_20260822.md)
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
- [original/M39-CIRCDIST_PROBLEMS.md](original/M39-CIRCDIST_PROBLEMS.md)
- [original/M40-circdist_sat_window_theorem_20260822.md](original/M40-circdist_sat_window_theorem_20260822.md)
- [original/M41-circdist_sat_window_amendment1_20260822.md](original/M41-circdist_sat_window_amendment1_20260822.md)
- [original/M42-circdist_sat_window_review_20260822.md](original/M42-circdist_sat_window_review_20260822.md)
- [original/M43-circdist_lift_nonint_proof_20260820.md](original/M43-circdist_lift_nonint_proof_20260820.md)
- [original/M44-CIRCDIST.sat.transfer.yaml](original/M44-CIRCDIST.sat.transfer.yaml)
- [original/context/R01-M01-CIRCDIST.sat.transfer.yaml.context.md](original/context/R01-M01-CIRCDIST.sat.transfer.yaml.context.md)
- [original/context/R02-M03-circdist_sat_transfer_proof_20260823.md.context.md](original/context/R02-M03-circdist_sat_transfer_proof_20260823.md.context.md)
- [original/context/R03-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md](original/context/R03-M02-circdist_sat_transfer_endtoend_exact_review_20260826.md.context.md)

[Back to all 65 errors](../../README.md)
