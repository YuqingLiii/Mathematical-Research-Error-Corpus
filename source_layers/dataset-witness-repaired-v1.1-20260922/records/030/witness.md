# Record 030 — Circuit-distance stabilization

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> > **Remark 6.5 (what each boundary buys, quantitatively).** Drop the round-0 detector (noisy or
> > unknown initialisation). Then (W) becomes `u(S_r) = H_Z σ_r + κ` for an unconstrained constant
> > `κ ∈ F₂^ℬ`, and the correct object is no longer a single `(u,A,v)` but the family
> > `A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ)` with `d_R = min_κ ( u ⊙ A_κ^{⊙R} ⊙ v )` — equivalently a
> > state space `Σ × F₂^ℬ` in which `κ` is carried as a constant component. Drop the terminal detector
> > instead and `v` loses its first clause, becoming `v[σ] = 0` iff `σ ≠ [0]`, which is a *different*
> > and generally smaller quantity. **Both boundaries are load-bearing, in different places**, and
> > this is the precise form of the round-0/terminal asymmetry.

Context: The model studies a counterfactual boundary convention in which the initial detector is removed. It correctly introduces a free recursion constant κ into the transition matrix but leaves the terminal vector v unchanged.

Locator: Proof draft dated 23 August 2026, Remark 6.5, lines 603–610.

## 2. Witness / adjudication

Removing the initial detector changes the terminal consistency condition as well as the transition matrix. Keeping the old kernel test in v excludes allowed terminal states with nonzero κ.

The detector recursion becomes u(S_r)=H_Zσ_r+κ. The terminal detector is D_{b,R}=(H_Zσ_R)_b+[(H_Zσ_{R−1})+u(S_{R−1})]_b=(H_Zσ_R)_b+κ_b. Therefore vanishing terminal detectors require H_Zσ_R=κ, not H_Zσ_R=0. Since σ_R need not lie in ker H_Z, 'σ_R≠[0]' is no longer the correct logical test; the observable condition is λ(σ_R)=1. The correct v_κ is zero only where both H_Zσ_R=κ and the target logical flip occur. The archived tests matched in 0/16 cases with fixed v and 16/16 after this correction.

Scope: computation_false

删左边界后递推常数κ进入末端detector，末态必须满足H_Zσ_R=κ。原式只改Aκ却继续用v(σ)=1[H_Zσ=0且非零逻辑]，直接算错边界公式。

维持旧错误确认；这是计算/公式错误，不必因为对象随模型变化就自动标overclaim。

## 3. Evidence and verification

本轮按detector递推手算末态条件；0/16与修正16/16是旧审计结果，未冒称本轮全量重跑。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_sat_transfer_proof_20260823.md](original/M01-circdist_sat_transfer_proof_20260823.md) — inherited_sanitized_source
- [M02-circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md) — inherited_sanitized_source
- [M03-circdist_sat_transfer_amendment1_20260823.md](original/M03-circdist_sat_transfer_amendment1_20260823.md) — inherited_sanitized_source
- [M04-agent-a650547b7eb957124.jsonl.readable.md](original/M04-agent-a650547b7eb957124.jsonl.readable.md) — inherited_sanitized_source
- [M04-agent-a650547b7eb957124.jsonl.visible.json](original/M04-agent-a650547b7eb957124.jsonl.visible.json) — inherited_sanitized_source
- [M05-SAT_RESCOPE_20260822.md](original/M05-SAT_RESCOPE_20260822.md) — inherited_sanitized_source
- [M06-CIRCDIST_PROBLEMS.md](original/M06-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M07-circdist_sat_window_theorem_20260822.md](original/M07-circdist_sat_window_theorem_20260822.md) — inherited_sanitized_source
- [M08-circdist_sat_recon_20260820.md](original/M08-circdist_sat_recon_20260820.md) — inherited_sanitized_source
- [M09-circdist_sat_window_amendment1_20260822.md](original/M09-circdist_sat_window_amendment1_20260822.md) — inherited_sanitized_source
- [M10-circdist_sat_window_review_20260822.md](original/M10-circdist_sat_window_review_20260822.md) — inherited_sanitized_source
- [M11-circdist_lift_nonint_proof_20260820.md](original/M11-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M12-CIRCDIST.sat.transfer.yaml](original/M12-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M13-CIRCDIST.sat.transfer.yaml](original/M13-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M14-CIRCDIST_PROBLEMS.md](original/M14-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M15-SAT_RESCOPE_20260822.md](original/M15-SAT_RESCOPE_20260822.md) — inherited_sanitized_source
- [M16-circdist_sat_transfer_review_20260823.md](original/M16-circdist_sat_transfer_review_20260823.md) — inherited_sanitized_source
- [M17-circdist_sat_transfer_rereview_20260823.md](original/M17-circdist_sat_transfer_rereview_20260823.md) — inherited_sanitized_source
- [M18-circdist_transfer_bridgefold_20260823.md](original/M18-circdist_transfer_bridgefold_20260823.md) — inherited_sanitized_source
- [M19-circdist_sat_window_theorem_20260822.md](original/M19-circdist_sat_window_theorem_20260822.md) — inherited_sanitized_source
- [M20-circdist_sat_window_amendment1_20260822.md](original/M20-circdist_sat_window_amendment1_20260822.md) — inherited_sanitized_source
- [M21-circdist_sat_window_review_20260822.md](original/M21-circdist_sat_window_review_20260822.md) — inherited_sanitized_source
- [M22-circdist_amendments4_review_20260822.md](original/M22-circdist_amendments4_review_20260822.md) — inherited_sanitized_source
- [M23-circdist_readjudication_20260823.md](original/M23-circdist_readjudication_20260823.md) — inherited_sanitized_source
- [M24-circdist_sat_window_selfcontained_exact_proof_20260826.md](original/M24-circdist_sat_window_selfcontained_exact_proof_20260826.md) — inherited_sanitized_source
- [M25-circdist_sat_window_selfcontained_exact_review_20260826.md](original/M25-circdist_sat_window_selfcontained_exact_review_20260826.md) — inherited_sanitized_source
- [M26-circdist_sat_v3_exact_text_review_20260826.md](original/M26-circdist_sat_v3_exact_text_review_20260826.md) — inherited_sanitized_source
- [M27-circdist_sat_instances_window_edge_exact_review_20260826.md](original/M27-circdist_sat_instances_window_edge_exact_review_20260826.md) — inherited_sanitized_source
- [M28-circdist_sat_window_downstream_scope_rebind_review_20260826.md](original/M28-circdist_sat_window_downstream_scope_rebind_review_20260826.md) — inherited_sanitized_source
- [M29-circdist_sat_root_assembly_20260823.md](original/M29-circdist_sat_root_assembly_20260823.md) — inherited_sanitized_source
- [M30-circdist_sat_root_review_20260823.md](original/M30-circdist_sat_root_review_20260823.md) — inherited_sanitized_source
- [M31-circdist_sat_root_proved_adjudication_20260823.md](original/M31-circdist_sat_root_proved_adjudication_20260823.md) — inherited_sanitized_source
- [M32-CIRCDIST.sat.transfer.yaml](original/M32-CIRCDIST.sat.transfer.yaml) — inherited_sanitized_source
- [M33-proof_dag_check.py](original/M33-proof_dag_check.py) — inherited_sanitized_source
- [M34-SCHEDULER.yaml](original/M34-SCHEDULER.yaml) — inherited_sanitized_source
- [M35-circdist_sat_recon_20260820.md](original/M35-circdist_sat_recon_20260820.md) — inherited_sanitized_source
- [M36-evidence_closure_check.py](original/M36-evidence_closure_check.py) — inherited_sanitized_source
- [M37-check_circdist_migration.py](original/M37-check_circdist_migration.py) — inherited_sanitized_source
- [M38-check_event_append_only.py](original/M38-check_event_append_only.py) — inherited_sanitized_source
- [M39-circdist_sat_transfer_review_20260823.md](original/M39-circdist_sat_transfer_review_20260823.md) — inherited_sanitized_source
- [M40-circdist_sat_transfer_proof_20260823.md](original/M40-circdist_sat_transfer_proof_20260823.md) — inherited_sanitized_source
- [R01-M01-circdist_sat_transfer_proof_20260823.md.context.md](reconciliation_sources/R01-M01-circdist_sat_transfer_proof_20260823.md.context.md) — reconciliation_source_window
- [R02-M03-circdist_sat_transfer_amendment1_20260823.md.context.md](reconciliation_sources/R02-M03-circdist_sat_transfer_amendment1_20260823.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
