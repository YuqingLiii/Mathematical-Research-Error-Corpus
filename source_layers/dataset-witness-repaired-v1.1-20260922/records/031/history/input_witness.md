# Record 031 — Circuit-distance stabilization

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> min-plus matrix powers are eventually periodic

**Recorded location:** Archived external-theorem assumption registered 23 August 2026, assumption statement, lines 21–23.

**Context (annotation, not a source quotation):** A registered external-theorem assumption summarizes a min-plus matrix theorem as unqualified eventual periodicity. It is an auxiliary asymptotic assertion, not the finite-round transfer identity.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Min-plus powers generally have linear drift. Eventual periodicity of the unshifted sequence requires normalization and additional hypotheses; it does not hold for every min-plus matrix.

### Argument or calculation

For the one-by-one min-plus matrix A=[1], min-plus multiplication adds its only entry. By induction A^{⊙R}=[R] for every positive integer R. For any period p>0, A^{⊙(R+p)}=[R+p]≠[R]=A^{⊙R}, at every R. This exactly refutes the unqualified statement. It does not refute the finite-round transfer formula or the more careful zero-cycle normalized argument for the specific transfer matrices.

Scope: statement_false.


### Archived review excerpt

> So the dossier’s more careful A1 application can be repaired into a correct argument. The **installed node assumption is still overbroad**: “min-plus matrix powers are eventually periodic” is false without normalization/rate and connectivity qualifications. The one-by-one min-plus matrix `[1]` has power `[R]`, not an eventually periodic unshifted sequence.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** proposer 讨论带零循环/非负权条件的 periodicity，错误安装版却是无条件；尚无同一安装事件的诊断性推理。

- [2026-08-23T07:55:57.401Z — claude_visible_thinking](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — source line 23; recorded role: generation.

## Original materials

- [M01: CIRCDIST.sat.transfer.yaml](original/M01-CIRCDIST.sat.transfer.yaml "research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–274.
  - Relevant location(s): lines 21–23; #assumptions.a1-bcoq-3112; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml`

- [M02: circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–1037.
  - Relevant location(s): §4 exact-claim audit；§§6.2,7.3–8.3,10–12 按条目; lines 480; #10.1,10.2; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md`

- [M03: CIRCDIST.sat.transfer.yaml](original/M03-CIRCDIST.sat.transfer.yaml "research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–152.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml`

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
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
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
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research/circdist/notes/SAT_RESCOPE_20260822.md`

- [M12: circdist_sat_root_proved_adjudication_20260823.md](original/M12-circdist_sat_root_proved_adjudication_20260823.md "research-graph/artifacts/circdist_sat_root_proved_adjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–426.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/artifacts/circdist_sat_root_proved_adjudication_20260823.md`

- [M13: CIRCDIST_PROBLEMS.md](original/M13-CIRCDIST_PROBLEMS.md "research-graph/circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/definitions/CIRCDIST_PROBLEMS.md`

- [M14: SAT_RESCOPE_20260822.md](original/M14-SAT_RESCOPE_20260822.md "research-graph/circdist/artifacts/definitions/SAT_RESCOPE_20260822.md")
  - Coverage: Full bundled file; source lines 1–99.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/circdist/artifacts/definitions/SAT_RESCOPE_20260822.md`

- [M15: circdist_sat_transfer_proof_20260823.md](original/M15-circdist_sat_transfer_proof_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md")
  - Coverage: Full bundled file; source lines 1–1486.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md`

- [M16: circdist_sat_transfer_amendment1_20260823.md](original/M16-circdist_sat_transfer_amendment1_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md")
  - Coverage: Full bundled file; source lines 1–1025.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md`

- [M17: circdist_sat_transfer_review_20260823.md](original/M17-circdist_sat_transfer_review_20260823.md "research-graph/circdist/reviews/circdist_sat_transfer_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–453.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_review_20260823.md`

- [M18: circdist_sat_transfer_rereview_20260823.md](original/M18-circdist_sat_transfer_rereview_20260823.md "research-graph/circdist/reviews/circdist_sat_transfer_rereview_20260823.md")
  - Coverage: Full bundled file; source lines 1–425.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_rereview_20260823.md`

- [M19: circdist_transfer_bridgefold_20260823.md](original/M19-circdist_transfer_bridgefold_20260823.md "research-graph/circdist/reviews/circdist_transfer_bridgefold_20260823.md")
  - Coverage: Full bundled file; source lines 1–640.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
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
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
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
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml
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
