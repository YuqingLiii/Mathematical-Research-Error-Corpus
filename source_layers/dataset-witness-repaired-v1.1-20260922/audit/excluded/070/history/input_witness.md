# Record 070 — Circuit-distance stabilization

**Review status:** `interpretation_check_pending`.

The source claim invokes 'the stated ... unit-fault model' and Lemma 2.9; those surrounding definitions may already supply the full-group hypothesis. Resolve incorporation-by-reference before treating the isolated statement as an actual overclaim.

## Original statement and context

>   exactly. The d_R so computed is moreover invariant under the counting and detector-split
>   conventions the surrounding route composes across: by Lemma 2.9 it is the same whether a witness
>   is counted by its number of elementary faults, collisions permitted, or by its number of faulty
>   locations;

**Recorded location:** Archived theorem statement installed on 23 August 2026, counting-invariance clause, lines 10–13.

**Context (annotation, not a source quotation):** The installed claim states equality of collision-permitting elementary-fault counts and occupied-location counts. The dossier proves it by multiplying faults at a shared location inside the full local Pauli group, with unit cost for every nonidentity assignment.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The collision-merging proof needs the allowed alphabet to be closed under local multiplication and uses a compatible uniform cost. Unit weights alone do not provide group closure.

### Argument or calculation

At one CNOT location allow X_c and X_t but not X_cX_t. A multiset containing X_c and X_t has size two and realizes the combined effect X_cX_t. A legal configuration, which permits only one allowed assignment at that location, cannot realize that product there. Thus multiset and occupied-location optima need not agree for an incomplete alphabet. In the full Pauli-group unit-cost model, merging does prove equality; the witness concerns extending the statement beyond that model, not refuting the full-model lemma.

Scope: argument_invalid.


### Archived review excerpt

> ### 6.2 Elementary-fault count versus occupied locations
> 
> Let `m(e)` be the least cardinality of a multiset of unit elementary faults with total effect `e`, allowing multiple members at one location, and let `c(e)` be the least number of occupied locations in a configuration.
> 
> A configuration is itself such a multiset, so `m(e)<=c(e)`. Conversely, in any multiset, replace two elements at one location by their product in that location’s full Pauli group. The effect is unchanged. If the product is nonidentity the multiset shrinks by one; if identity it shrinks by two. Repeat until at most one element remains per location. This produces a configuration of weight at most the original multiset size, so `c(e)<=m(e)`. Therefore
> 
> ```text
> m(e)=c(e).
> ```
> 
> Disjoint copied round-location sets then give exact additivity across rounds. This proves Lemma 2.9 with both hidden hypotheses exposed: linear effect and group closure with uniform unit cost.
> 
> A non-group alphabet gives an immediate counterexample. At one CNOT location allow `X_c` and `X_t` but not `X_cX_t`. The collision-permitting multiset realizes the product effect with two elementary faults at that location, while a one-assignment configuration cannot realize it there. A nonuniform model similarly invalidates the weight-nonincreasing projection if `Y` is cheap but its pure X or Z component is expensive.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 完整 Pauli 故障及均匀代价假设下的合并论证，与安装版无条件等价不是同一命题；现有推理不足以定位去掉假设的节点。

- [2026-08-23T07:55:57.401Z — claude_visible_thinking](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — source line 23; recorded role: generation.
- [2026-08-23T08:03:29.160Z — claude_visible_thinking](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — source line 54; recorded role: generation.

## Original materials

- [M01: CIRCDIST.sat.transfer.yaml](original/M01-CIRCDIST.sat.transfer.yaml "research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–274.
  - Relevant location(s): lines 10–13; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml`

- [M02: circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–1037.
  - Relevant location(s): §4 exact-claim audit；§§6.2,7.3–8.3,10–12 按条目; lines 226–238; #6.2; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md`

- [M03: circdist_sat_transfer_proof_20260823.md](original/M03-circdist_sat_transfer_proof_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md")
  - Coverage: Full bundled file; source lines 1–1486.
  - Relevant location(s): #L210-223 (Lemma2.9), L476-480, L810; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md`

- [M04: agent-a650547b7eb957124.jsonl](original/M04-agent-a650547b7eb957124.jsonl.readable.md "claude-session-archive/agent-a650547b7eb957124.jsonl") · [event data](original/M04-agent-a650547b7eb957124.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 17–29, 48–60.
  - Relevant location(s): lines 23; lines 54
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
