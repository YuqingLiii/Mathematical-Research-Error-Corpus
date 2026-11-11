# Record 069 — Circuit-distance stabilization

**Review status:** `interpretation_check_pending`.

This is a domain/definition omission in a summary theorem string. The min-plus representation itself can remain correct at k=0 under min(empty)=+infinity. Do not label it a false mathematical equality without deciding the intended convention and incorporated assumptions.

## Original statement and context

>   For each fixed legal single-round single-ancilla CSS schedule M under the stated ideal temporal
>   boundaries and unit-fault model, there is an explicitly constructible finite min-plus transfer
>   system (u,A,v) such that d_R(M) = u^T min-plus A^R min-plus v for every R, with the two CSS
>   sectors, boundary conditions, unreachable states, and logical terminal condition represented
>   exactly.

**Recorded location:** Archived theorem statement installed on 23 August 2026, transfer claim, lines 6–10.

**Context (annotation, not a source quotation):** The installed transfer theorem quantifies over CSS schedules without explicitly requiring at least one encoded logical qubit. Its terminal vector is finite precisely for nonzero logical terminal classes.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

At k=0 the set over which a logical-distance minimum is taken is empty. A finite logical witness is unavailable, so the theorem needs an explicit k≥1 restriction or an extended-real convention.

### Argument or calculation

Let n=2 and H_X=H_Z=(1,1). Both ranks are one, hence k=n−rank H_X−rank H_Z=0. The quotient ker(H_Z)/rowspace(H_X) has dimension zero; it contains no nonzero terminal logical class. The vector v has no finite entries. Declaring min(empty)=+infinity can extend the formula, but without such a convention the ordinary finite logical-distance assertion is not defined for this input.

Scope: argument_invalid.


### Archived review excerpt

> ### 4.2 `k=0` attack
> 
> For the stabilizer state with `n=2`, `H_X=H_Z=(11)`, `k=0`. Then
> 
> ```text
> dim(ker H_Z/S_X) = n-rank(H_X)-rank(H_Z) = 0.
> ```
> 
> There is no nonzero terminal class, so `v` is nowhere finite. One may choose a convention `min(empty)=+infinity`, but that is not the memory logical-distance proposition stated in the dossier. The theorem deliberately assumes `k>=1`; the exact claim must say so.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** proposer 推理有 k≥1 条件，但错误是后来安装版本遗漏条件；不能将不同版本、不同作者的推理与输出直接配对成抄写错误。

- [2026-08-23T07:55:57.401Z — claude_visible_thinking](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — source line 23; recorded role: generation.

## Original materials

- [M01: CIRCDIST.sat.transfer.yaml](original/M01-CIRCDIST.sat.transfer.yaml "research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–274.
  - Relevant location(s): lines 6–10; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml`

- [M02: circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–1037.
  - Relevant location(s): §4 exact-claim audit；§§6.2,7.3–8.3,10–12 按条目; lines 130–138; #3 (installed string, hash-bound),#4.2; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md`

- [M03: circdist_sat_transfer_proof_20260823.md](original/M03-circdist_sat_transfer_proof_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md")
  - Coverage: Full bundled file; source lines 1–1486.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
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
