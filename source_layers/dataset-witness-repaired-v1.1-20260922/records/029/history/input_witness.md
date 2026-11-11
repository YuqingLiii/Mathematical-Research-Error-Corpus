# Record 029 — Circuit-distance stabilization

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

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

**Recorded location:** Proof draft dated 23 August 2026, section 12, proposed mitigation (a), lines 1426–1437.

**Context (annotation, not a source quotation):** The draft proposes robustness under replacing its canonical detector space D by any intermediate space D' containing the short detector list and contained in the larger deterministic-parity space V. The latter also contains logical observable directions.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Containment in V permits adding a parity with a logical-observable component. A fault that is logical and undetected by the original detectors can then be detected by the new parity, so the claimed unchanged proof does not apply.

### Argument or calculation

Let λ be a logical observable and P_X the round-zero redundant-X-check parity of Steane with an added dependent X-check row. Set D'=span(D_b)+span(D_a)+span(P_X+λ). This contains the original short detector set and lies in V. A projected logical witness flips P_X by 0 and λ by 1, hence flips P_X+λ and is detected by D'. The archived exact example changes distance from 2 to 3 at R=2 and from 2 to 4 at R=3. The safe hypothesis is D'⊆D, not merely D'⊆V. The failure of the inference follows already from the displayed logical component; the canonical-space theorem is unaffected.

Scope: argument_invalid.


### Archived review excerpt

> On Steane with a redundant X row, let `P_X` be the round-zero dependent-row parity and let `lambda` be the logical observable. The old mitigation admitted
> 
> ```text
> D' = span(D_b) + span(D_a) + span(P_X+lambda),
> ```
> 
> because `D'` contains the short set and lies in `V`. Yet `P_X+lambda` detects the projected logical witness. The exact reproduced data are:
> 
> | R | record dimension | `dim V` | `dim D` | `rank span(D_b)` | `rank span(D_b,D_a)` | `d^{2.7}` | `d^{D'}` |
> |---:|---:|---:|---:|---:|---:|---:|---:|
> | 2 | 21 | 15 | 14 | 9 | 13 | 2 | 3 |
> | 3 | 28 | 22 | 21 | 12 | 20 | 2 | 4 |
> 
> At `R=3` this is the recorded quintuple `28/22/21/12/20`. Amendment 1 correctly replaces the false condition by
> 
> ```text
> span(D_b) subseteq D' subseteq D.
> ```
> 
> That containment is sufficient by the same projection proof. No version with only `D' subseteq V` survives.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 找到 type-split 推导与后续修复，但没有找到生成期明确支持原先任意 detector split 保距的推理。

- [2026-08-23T07:55:57.401Z — claude_visible_thinking](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — source line 23; recorded role: generation.

## Original materials

- [M01: circdist_sat_transfer_proof_20260823.md](original/M01-circdist_sat_transfer_proof_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md")
  - Coverage: Full bundled file; source lines 1–1486.
  - Relevant location(s): lines 1426–1437; #L409-419, L1426-1437 (T-G3 a); Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md`

- [M02: circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–1037.
  - Relevant location(s): §4 exact-claim audit；§§6.2,7.3–8.3,10–12 按条目; lines 330–349; #7.4; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md`

- [M03: circdist_sat_transfer_amendment1_20260823.md](original/M03-circdist_sat_transfer_amendment1_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md")
  - Coverage: Full bundled file; source lines 1–1025.
  - Relevant location(s): #2.2; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md`

- [M04: agent-a650547b7eb957124.jsonl](original/M04-agent-a650547b7eb957124.jsonl.readable.md "claude-session-archive/agent-a650547b7eb957124.jsonl") · [event data](original/M04-agent-a650547b7eb957124.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 17–29.
  - Relevant location(s): lines 23
  - Source: `claude-session-archive/agent-a650547b7eb957124.jsonl`

- [M05: SAT_RESCOPE_20260822.md](original/M05-SAT_RESCOPE_20260822.md "research/circdist/notes/SAT_RESCOPE_20260822.md")
  - Coverage: Full bundled file; source lines 1–99.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md; Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
  - Source: `research/circdist/notes/SAT_RESCOPE_20260822.md`

- [M06: CIRCDIST_PROBLEMS.md](original/M06-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md; Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M07: circdist_sat_window_theorem_20260822.md](original/M07-circdist_sat_window_theorem_20260822.md "artifacts/circdist_sat_window_theorem_20260822.md")
  - Coverage: Full bundled file; source lines 1–933.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_sat_window_theorem_20260822.md`

- [M08: circdist_sat_recon_20260820.md](original/M08-circdist_sat_recon_20260820.md "artifacts/circdist_sat_recon_20260820.md")
  - Coverage: Full bundled file; source lines 1–698.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_sat_recon_20260820.md`

- [M09: circdist_sat_window_amendment1_20260822.md](original/M09-circdist_sat_window_amendment1_20260822.md "artifacts/circdist_sat_window_amendment1_20260822.md")
  - Coverage: Full bundled file; source lines 1–458.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_sat_window_amendment1_20260822.md`

- [M10: circdist_sat_window_review_20260822.md](original/M10-circdist_sat_window_review_20260822.md "artifacts/circdist_sat_window_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–343.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_sat_window_review_20260822.md`

- [M11: circdist_lift_nonint_proof_20260820.md](original/M11-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M12: CIRCDIST.sat.transfer.yaml](original/M12-CIRCDIST.sat.transfer.yaml "research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–112.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md; Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.sat.transfer.yaml`

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

- [M16: circdist_sat_transfer_review_20260823.md](original/M16-circdist_sat_transfer_review_20260823.md "research-graph/circdist/reviews/circdist_sat_transfer_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–453.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_review_20260823.md`

- [M17: circdist_sat_transfer_rereview_20260823.md](original/M17-circdist_sat_transfer_rereview_20260823.md "research-graph/circdist/reviews/circdist_sat_transfer_rereview_20260823.md")
  - Coverage: Full bundled file; source lines 1–425.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_rereview_20260823.md`

- [M18: circdist_transfer_bridgefold_20260823.md](original/M18-circdist_transfer_bridgefold_20260823.md "research-graph/circdist/reviews/circdist_transfer_bridgefold_20260823.md")
  - Coverage: Full bundled file; source lines 1–640.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_transfer_bridgefold_20260823.md`

- [M19: circdist_sat_window_theorem_20260822.md](original/M19-circdist_sat_window_theorem_20260822.md "research-graph/circdist/artifacts/circdist_sat_window_theorem_20260822.md")
  - Coverage: Full bundled file; source lines 1–933.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_window_theorem_20260822.md`

- [M20: circdist_sat_window_amendment1_20260822.md](original/M20-circdist_sat_window_amendment1_20260822.md "research-graph/circdist/artifacts/circdist_sat_window_amendment1_20260822.md")
  - Coverage: Full bundled file; source lines 1–458.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_window_amendment1_20260822.md`

- [M21: circdist_sat_window_review_20260822.md](original/M21-circdist_sat_window_review_20260822.md "research-graph/circdist/reviews/circdist_sat_window_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–343.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_window_review_20260822.md`

- [M22: circdist_amendments4_review_20260822.md](original/M22-circdist_amendments4_review_20260822.md "research-graph/circdist/reviews/circdist_amendments4_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–545.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_amendments4_review_20260822.md`

- [M23: circdist_readjudication_20260823.md](original/M23-circdist_readjudication_20260823.md "research-graph/circdist/reviews/circdist_readjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–617.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_readjudication_20260823.md`

- [M24: circdist_sat_window_selfcontained_exact_proof_20260826.md](original/M24-circdist_sat_window_selfcontained_exact_proof_20260826.md "research-graph/circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md")
  - Coverage: Full bundled file; source lines 1–1155.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_window_selfcontained_exact_proof_20260826.md`

- [M25: circdist_sat_window_selfcontained_exact_review_20260826.md](original/M25-circdist_sat_window_selfcontained_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–1792.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_window_selfcontained_exact_review_20260826.md`

- [M26: circdist_sat_v3_exact_text_review_20260826.md](original/M26-circdist_sat_v3_exact_text_review_20260826.md "research-graph/circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–686.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_v3_exact_text_review_20260826.md`

- [M27: circdist_sat_instances_window_edge_exact_review_20260826.md](original/M27-circdist_sat_instances_window_edge_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–692.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_instances_window_edge_exact_review_20260826.md`

- [M28: circdist_sat_window_downstream_scope_rebind_review_20260826.md](original/M28-circdist_sat_window_downstream_scope_rebind_review_20260826.md "research-graph/circdist/reviews/circdist_sat_window_downstream_scope_rebind_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–828.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_window_downstream_scope_rebind_review_20260826.md`

- [M29: circdist_sat_root_assembly_20260823.md](original/M29-circdist_sat_root_assembly_20260823.md "research-graph/circdist/artifacts/circdist_sat_root_assembly_20260823.md")
  - Coverage: Full bundled file; source lines 1–1098.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_root_assembly_20260823.md`

- [M30: circdist_sat_root_review_20260823.md](original/M30-circdist_sat_root_review_20260823.md "research-graph/circdist/reviews/circdist_sat_root_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–774.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_root_review_20260823.md`

- [M31: circdist_sat_root_proved_adjudication_20260823.md](original/M31-circdist_sat_root_proved_adjudication_20260823.md "research-graph/circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–426.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_root_proved_adjudication_20260823.md`

- [M32: CIRCDIST.sat.transfer.yaml](original/M32-CIRCDIST.sat.transfer.yaml "research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml")
  - Coverage: Full bundled file; source lines 1–274.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.sat.transfer.yaml`

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

- [M39: circdist_sat_transfer_review_20260823.md](original/M39-circdist_sat_transfer_review_20260823.md "artifacts/circdist_sat_transfer_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–453.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
  - Source: `artifacts/circdist_sat_transfer_review_20260823.md`

- [M40: circdist_sat_transfer_proof_20260823.md](original/M40-circdist_sat_transfer_proof_20260823.md "artifacts/circdist_sat_transfer_proof_20260823.md")
  - Coverage: Full bundled file; source lines 1–1486.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md
  - Source: `artifacts/circdist_sat_transfer_proof_20260823.md`
