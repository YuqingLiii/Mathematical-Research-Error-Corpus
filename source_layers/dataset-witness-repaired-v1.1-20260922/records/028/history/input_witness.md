# Record 028 — Circuit-distance stabilization

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

>   For each fixed legal single-round single-ancilla CSS schedule M under the stated ideal temporal
>   boundaries and unit-fault model, there is an explicitly constructible finite min-plus transfer
>   system (u,A,v) such that d_R(M) = u^T min-plus A^R min-plus v for every R, with the two CSS
>   sectors, boundary conditions, unreachable states, and logical terminal condition represented
>   exactly.

**Recorded location:** Archived theorem statement installed on 23 August 2026, transfer claim, lines 6–10.

**Context (annotation, not a source quotation):** The installed claim uses a 'legal' schedule condition while the relevant legality notion guarantees only that no qubit participates in two gates simultaneously. Measurement consistency is separately required for the parity checks to be deterministic detectors.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Conflict freedom is a scheduling constraint, not a proof that the circuit measures the intended stabilizers. A non-measurement-consistent interleaving can produce random check records even with no physical faults.

### Argument or calculation

On four data qubits, take H_X=H_Z=(1,1,1,1). Prepare X ancilla a in |+> and Z ancilla b in |0>. Execute sequentially: q0→b, a→q0, a→q1, q1→b, a→q2, q2→b, a→q3, q3→b. The sequence is conflict-free, but exactly one common-support qubit has the Z CNOT before the X CNOT, an odd MC count. Back-propagating b's Z measurement creates Z on the fresh |+> ancilla a. That operator anticommutes with a's input stabilizer, so the check outcome is uniformly random and its proposed parity is not a deterministic detector. The transfer object needs MC as an additional hypothesis.

Scope: argument_invalid.


### Archived review excerpt

> ### 4.1 Concrete conflict-free but MC-failing attack
> 
> Take `H_X=H_Z=(1111)` on four data qubits. Schedule the eight CNOTs sequentially as
> 
> ```text
> q0->b, a->q0, a->q1, q1->b, a->q2, q2->b, a->q3, q3->b.
> ```
> 
> No qubit participates in two CNOTs in one time step, so the schedule is conflict-free. Exactly one common-support qubit has `t(q->b)<t(a->q)`, hence `c_ab=1`. Back-propagating the `Z` measurement of `anc(b)` produces a `Z` on the freshly `|+>`-prepared `anc(a)`; that anticommutes with its input stabilizer, so the check record is uniformly random. The Definition-2.7 parity is not a detector. This is not a marginal convention: the finite-state proof has no defined object to compute until MC is imposed.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** proposer 使用 MC 范围，安装版本变成一般 conflict-free；缺少对应安装节点的诊断性生成摘要。

- [2026-08-23T07:55:57.401Z — claude_visible_thinking](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — source line 23; recorded role: generation.

## Original materials

- [M01: CIRCDIST.sat.transfer.yaml](original/M01-CIRCDIST.sat.transfer.yaml "research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–274.
  - Relevant location(s): lines 6–10; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml`

- [M02: circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–1037.
  - Relevant location(s): §4 exact-claim audit；§§6.2,7.3–8.3,10–12 按条目; lines 120–128; #3,#4.1; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md`

- [M03: circdist_sat_transfer_proof_20260823.md](original/M03-circdist_sat_transfer_proof_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md")
  - Coverage: Full bundled file; source lines 1–1486.
  - Relevant location(s): #Def2.7; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md`

- [M04: agent-a650547b7eb957124.jsonl](original/M04-agent-a650547b7eb957124.jsonl.readable.md "claude-session-archive/agent-a650547b7eb957124.jsonl") · [event data](original/M04-agent-a650547b7eb957124.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 17–29.
  - Relevant location(s): lines 23
  - Source: `claude-session-archive/agent-a650547b7eb957124.jsonl`

- [M05: circdist_sat_transfer_proof_20260823.md](original/M05-circdist_sat_transfer_proof_20260823.md "artifacts/circdist_sat_transfer_proof_20260823.md")
  - Coverage: Full bundled file; source lines 1–1486.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `artifacts/circdist_sat_transfer_proof_20260823.md`

- [M06: circdist_sat_transfer_rereview_20260823.md](original/M06-circdist_sat_transfer_rereview_20260823.md "research-graph/artifacts/circdist_sat_transfer_rereview_20260823.md")
  - Coverage: Full bundled file; source lines 1–425.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/artifacts/circdist_sat_transfer_rereview_20260823.md`

- [M07: circdist_transfer_bridgefold_20260823.md](original/M07-circdist_transfer_bridgefold_20260823.md "research-graph/artifacts/circdist_transfer_bridgefold_20260823.md")
  - Coverage: Full bundled file; source lines 1–640.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/artifacts/circdist_transfer_bridgefold_20260823.md`

- [M08: circdist_sat_recon_20260820.md](original/M08-circdist_sat_recon_20260820.md "artifacts/circdist_sat_recon_20260820.md")
  - Coverage: Full bundled file; source lines 1–698.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml; Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_sat_recon_20260820.md`

- [M09: circdist_sat_transfer_amendment1_20260823.md](original/M09-circdist_sat_transfer_amendment1_20260823.md "research-graph/artifacts/circdist_sat_transfer_amendment1_20260823.md")
  - Coverage: Full bundled file; source lines 1–1025.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/artifacts/circdist_sat_transfer_amendment1_20260823.md`

- [M10: circdist_sat_transfer_review_20260823.md](original/M10-circdist_sat_transfer_review_20260823.md "artifacts/circdist_sat_transfer_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–453.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `artifacts/circdist_sat_transfer_review_20260823.md`

- [M11: SAT_RESCOPE_20260822.md](original/M11-SAT_RESCOPE_20260822.md "research/circdist/notes/SAT_RESCOPE_20260822.md")
  - Coverage: Full bundled file; source lines 1–99.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml; Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `research/circdist/notes/SAT_RESCOPE_20260822.md`

- [M12: circdist_sat_root_proved_adjudication_20260823.md](original/M12-circdist_sat_root_proved_adjudication_20260823.md "research-graph/artifacts/circdist_sat_root_proved_adjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–426.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/artifacts/circdist_sat_root_proved_adjudication_20260823.md`

- [M13: CIRCDIST.sat.transfer.yaml](original/M13-CIRCDIST.sat.transfer.yaml "research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–152.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml`

- [M14: CIRCDIST_PROBLEMS.md](original/M14-CIRCDIST_PROBLEMS.md "research-graph/circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md`

- [M15: SAT_RESCOPE_20260822.md](original/M15-SAT_RESCOPE_20260822.md "research-graph/circdist/artifacts/definitions/SAT_RESCOPE_20260822.md")
  - Coverage: Full bundled file; source lines 1–99.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/definitions/SAT_RESCOPE_20260822.md`

- [M16: circdist_sat_transfer_amendment1_20260823.md](original/M16-circdist_sat_transfer_amendment1_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md")
  - Coverage: Full bundled file; source lines 1–1025.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md`

- [M17: circdist_sat_transfer_review_20260823.md](original/M17-circdist_sat_transfer_review_20260823.md "research-graph/circdist/reviews/circdist_sat_transfer_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–453.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_review_20260823.md`

- [M18: circdist_sat_transfer_rereview_20260823.md](original/M18-circdist_sat_transfer_rereview_20260823.md "research-graph/circdist/reviews/circdist_sat_transfer_rereview_20260823.md")
  - Coverage: Full bundled file; source lines 1–425.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_rereview_20260823.md`

- [M19: circdist_transfer_bridgefold_20260823.md](original/M19-circdist_transfer_bridgefold_20260823.md "research-graph/circdist/reviews/circdist_transfer_bridgefold_20260823.md")
  - Coverage: Full bundled file; source lines 1–640.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_transfer_bridgefold_20260823.md`

- [M20: circdist_sat_window_theorem_20260822.md](original/M20-circdist_sat_window_theorem_20260822.md "research-graph/circdist/artifacts/circdist_sat_window_theorem_20260822.md")
  - Coverage: Full bundled file; source lines 1–933.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_window_theorem_20260822.md`

- [M21: circdist_sat_window_amendment1_20260822.md](original/M21-circdist_sat_window_amendment1_20260822.md "research-graph/circdist/artifacts/circdist_sat_window_amendment1_20260822.md")
  - Coverage: Full bundled file; source lines 1–458.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_window_amendment1_20260822.md`

- [M22: circdist_sat_window_review_20260822.md](original/M22-circdist_sat_window_review_20260822.md "research-graph/circdist/reviews/circdist_sat_window_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–343.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_window_review_20260822.md`

- [M23: circdist_amendments4_review_20260822.md](original/M23-circdist_amendments4_review_20260822.md "research-graph/circdist/reviews/circdist_amendments4_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–545.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_amendments4_review_20260822.md`

- [M24: circdist_readjudication_20260823.md](original/M24-circdist_readjudication_20260823.md "research-graph/circdist/reviews/circdist_readjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–617.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_readjudication_20260823.md`

- [M25: circdist_sat_window_selfcontained_exact_proof_20260826.md](original/M25-circdist_sat_window_selfcontained_exact_proof_20260826.md "research-graph/circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md")
  - Coverage: Full bundled file; source lines 1–1155.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md`

- [M26: circdist_sat_window_selfcontained_exact_review_20260826.md](original/M26-circdist_sat_window_selfcontained_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–1792.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md`

- [M27: circdist_sat_v3_exact_text_review_20260826.md](original/M27-circdist_sat_v3_exact_text_review_20260826.md "research-graph/circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–686.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md`

- [M28: circdist_sat_instances_window_edge_exact_review_20260826.md](original/M28-circdist_sat_instances_window_edge_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–692.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md`

- [M29: circdist_sat_window_downstream_scope_rebind_review_20260826.md](original/M29-circdist_sat_window_downstream_scope_rebind_review_20260826.md "research-graph/circdist/reviews/circdist_sat_window_downstream_scope_rebind_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–828.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_window_downstream_scope_rebind_review_20260826.md`

- [M30: circdist_sat_root_assembly_20260823.md](original/M30-circdist_sat_root_assembly_20260823.md "research-graph/circdist/artifacts/circdist_sat_root_assembly_20260823.md")
  - Coverage: Full bundled file; source lines 1–1098.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_root_assembly_20260823.md`

- [M31: circdist_sat_root_review_20260823.md](original/M31-circdist_sat_root_review_20260823.md "research-graph/circdist/reviews/circdist_sat_root_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–774.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_root_review_20260823.md`

- [M32: circdist_sat_root_proved_adjudication_20260823.md](original/M32-circdist_sat_root_proved_adjudication_20260823.md "research-graph/circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–426.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md`

- [M33: proof_dag_check.py](original/M33-proof_dag_check.py "tools/proof_dag_check.py")
  - Coverage: Full bundled file; source lines 1–930.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `tools/proof_dag_check.py`

- [M34: SCHEDULER.yaml](original/M34-SCHEDULER.yaml "research-graph/operations/circdist/SCHEDULER.yaml")
  - Coverage: Full bundled file; source lines 1–5252.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/operations/circdist/SCHEDULER.yaml`

- [M35: circdist_sat_recon_20260820.md](original/M35-circdist_sat_recon_20260820.md "research-graph/circdist/artifacts/circdist_sat_recon_20260820.md")
  - Coverage: Full bundled file; source lines 1–698.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_recon_20260820.md`

- [M36: evidence_closure_check.py](original/M36-evidence_closure_check.py "research-graph/tools/evidence_closure_check.py")
  - Coverage: Full bundled file; source lines 1–75.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/tools/evidence_closure_check.py`

- [M37: check_circdist_migration.py](original/M37-check_circdist_migration.py "research-graph/tools/check_circdist_migration.py")
  - Coverage: Full bundled file; source lines 1–127.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/tools/check_circdist_migration.py`

- [M38: check_event_append_only.py](original/M38-check_event_append_only.py "tools/check_event_append_only.py")
  - Coverage: Full bundled file; source lines 1–210.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `tools/check_event_append_only.py`

- [M39: CIRCDIST_PROBLEMS.md](original/M39-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M40: circdist_sat_window_theorem_20260822.md](original/M40-circdist_sat_window_theorem_20260822.md "artifacts/circdist_sat_window_theorem_20260822.md")
  - Coverage: Full bundled file; source lines 1–933.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_sat_window_theorem_20260822.md`

- [M41: circdist_sat_window_amendment1_20260822.md](original/M41-circdist_sat_window_amendment1_20260822.md "artifacts/circdist_sat_window_amendment1_20260822.md")
  - Coverage: Full bundled file; source lines 1–458.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_sat_window_amendment1_20260822.md`

- [M42: circdist_sat_window_review_20260822.md](original/M42-circdist_sat_window_review_20260822.md "artifacts/circdist_sat_window_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–343.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_sat_window_review_20260822.md`

- [M43: circdist_lift_nonint_proof_20260820.md](original/M43-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M44: CIRCDIST.sat.transfer.yaml](original/M44-CIRCDIST.sat.transfer.yaml "research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–112.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml`
