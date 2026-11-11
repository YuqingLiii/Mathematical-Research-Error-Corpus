# Record 030 — Circuit-distance stabilization

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> > **Remark 6.5 (what each boundary buys, quantitatively).** Drop the round-0 detector (noisy or
> > unknown initialisation). Then (W) becomes `u(S_r) = H_Z σ_r + κ` for an unconstrained constant
> > `κ ∈ F₂^ℬ`, and the correct object is no longer a single `(u,A,v)` but the family
> > `A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ)` with `d_R = min_κ ( u ⊙ A_κ^{⊙R} ⊙ v )` — equivalently a
> > state space `Σ × F₂^ℬ` in which `κ` is carried as a constant component. Drop the terminal detector
> > instead and `v` loses its first clause, becoming `v[σ] = 0` iff `σ ≠ [0]`, which is a *different*
> > and generally smaller quantity. **Both boundaries are load-bearing, in different places**, and
> > this is the precise form of the round-0/terminal asymmetry.

**Recorded location:** Proof draft dated 23 August 2026, Remark 6.5, lines 603–610.

**Context (annotation, not a source quotation):** The model studies a counterfactual boundary convention in which the initial detector is removed. It correctly introduces a free recursion constant κ into the transition matrix but leaves the terminal vector v unchanged.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Removing the initial detector changes the terminal consistency condition as well as the transition matrix. Keeping the old kernel test in v excludes allowed terminal states with nonzero κ.

### Argument or calculation

The detector recursion becomes u(S_r)=H_Zσ_r+κ. The terminal detector is D_{b,R}=(H_Zσ_R)_b+[(H_Zσ_{R−1})+u(S_{R−1})]_b=(H_Zσ_R)_b+κ_b. Therefore vanishing terminal detectors require H_Zσ_R=κ, not H_Zσ_R=0. Since σ_R need not lie in ker H_Z, 'σ_R≠[0]' is no longer the correct logical test; the observable condition is λ(σ_R)=1. The correct v_κ is zero only where both H_Zσ_R=κ and the target logical flip occur. The archived tests matched in 0/16 cases with fixed v and 16/16 after this correction.

Scope: computation_false.


### Archived review excerpt

> The `A_κ` half is right and the `v` half is wrong. Re-run the document's own Lemma 6.2 computation
> with `D_{b,0}` deleted: the terminal detector reads
> 
> ```
>       D_{b,R} = (H_Z σ_R)_b + [ (H_Z σ_{R−1}) + u(S_{R−1}) ]_b = (H_Z σ_R)_b + κ_b ,
> ```
> 
> so the terminal condition is `H_Z σ_R = κ`, **not** `H_Z σ_R = 0`. And since `E_tot ∉ ker H_Z` in
> general once `κ ≠ 0`, Lemma 6.3's shortcut ("logical iff `σ_R ≠ [0]`", which is valid only on
> `ker H_Z`) is unavailable: the logical condition is `λ(σ_R) = 1`. Keeping `v` fixed forces `κ = 0`
> and collapses the family, so the printed formula does not merely lose precision — it computes the
> wrong number, in **16 of 16** instances tested (§6.2).

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理提到跟踪 κ 和初始边界，但没有充分明确固定 terminal v 正确或错误；仅凭正文公式错误不能判定是在推理还是书写时引入。

- [2026-08-23T07:55:57.401Z — claude_visible_thinking](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — source line 23; recorded role: generation.

## Original materials

- [M01: circdist_sat_transfer_proof_20260823.md](original/M01-circdist_sat_transfer_proof_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md")
  - Coverage: Full bundled file; source lines 1–1486.
  - Relevant location(s): lines 603–610; #L595-610 (sec6, Remark6.5); Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/artifacts/circdist_sat_transfer_proof_20260823.md`

- [M02: circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md "research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md")
  - Coverage: Full bundled file; source lines 1–1037.
  - Relevant location(s): §4 exact-claim audit；§§6.2,7.3–8.3,10–12 按条目; #9,12; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
  - Source: `research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md`

- [M03: circdist_sat_transfer_amendment1_20260823.md](original/M03-circdist_sat_transfer_amendment1_20260823.md "research-graph/circdist/artifacts/circdist_sat_transfer_amendment1_20260823.md")
  - Coverage: Full bundled file; source lines 1–1025.
  - Relevant location(s): lines 224–235; #3.1; Referenced by research-graph/circdist/reviews/circdist_sat_transfer_endtoend_exact_review_20260826.md
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
