# 030 — Removing the initial detector changes the terminal consistency condition as well as the transition matrix. Keeping the old kernel test in v excludes allowed terminal states with nonzero κ.

**Research problem:** P05 — Circuit-distance stabilization

## Original statement

> > **Remark 6.5 (what each boundary buys, quantitatively).** Drop the round-0 detector (noisy or
> > unknown initialisation). Then (W) becomes `u(S_r) = H_Z σ_r + κ` for an unconstrained constant
> > `κ ∈ F₂^ℬ`, and the correct object is no longer a single `(u,A,v)` but the family
> > `A_κ[σ,σ'] := w_M(σ'−σ, H_Z σ + κ)` with `d_R = min_κ ( u ⊙ A_κ^{⊙R} ⊙ v )` — equivalently a
> > state space `Σ × F₂^ℬ` in which `κ` is carried as a constant component. Drop the terminal detector
> > instead and `v` loses its first clause, becoming `v[σ] = 0` iff `σ ≠ [0]`, which is a *different*
> > and generally smaller quantity. **Both boundaries are load-bearing, in different places**, and
> > this is the precise form of the round-0/terminal asymmetry.

**Context:** The model studies a counterfactual boundary convention in which the initial detector is removed. It correctly introduces a free recursion constant κ into the transition matrix but leaves the terminal vector v unchanged.

**Original locator:** Proof draft dated 23 August 2026, Remark 6.5, lines 603–610.

## Why it is an error

Removing the initial detector changes the terminal consistency condition as well as the transition matrix. Keeping the old kernel test in v excludes allowed terminal states with nonzero κ.

## Witness / evidence

The detector recursion becomes u(S_r)=H_Zσ_r+κ. The terminal detector is D_{b,R}=(H_Zσ_R)_b+[(H_Zσ_{R−1})+u(S_{R−1})]_b=(H_Zσ_R)_b+κ_b. Therefore vanishing terminal detectors require H_Zσ_R=κ, not H_Zσ_R=0. Since σ_R need not lie in ker H_Z, 'σ_R≠[0]' is no longer the correct logical test; the observable condition is λ(σ_R)=1. The correct v_κ is zero only where both H_Zσ_R=κ and the target logical flip occur. The archived tests matched in 0/16 cases with fixed v and 16/16 after this correction.

## Scope

computation_false

## Classification

- IV: 逻辑推理错误. 改变初始边界后仍把旧终端 v 接到新 A_kappa 上，未保留公式各部件对应关系。正确终端约束依赖 kappa，还须检验目标逻辑翻转。

不是识别不到边界已经变化，而是在更新后的公式中错误沿用旧终端对应关系，归 IV。

## Adjudication notes

Removing the initial detector changes the terminal consistency condition as well as the transition matrix. Keeping the old kernel test in v excludes allowed terminal states with nonzero κ.

The detector recursion becomes u(S_r)=H_Zσ_r+κ. The terminal detector is D_{b,R}=(H_Zσ_R)_b+[(H_Zσ_{R−1})+u(S_{R−1})]_b=(H_Zσ_R)_b+κ_b. Therefore vanishing terminal detectors require H_Zσ_R=κ, not H_Zσ_R=0. Since σ_R need not lie in ker H_Z, 'σ_R≠[0]' is no longer the correct logical test; the observable condition is λ(σ_R)=1. The correct v_κ is zero only where both H_Zσ_R=κ and the target logical flip occur. The archived tests matched in 0/16 cases with fixed v and 16/16 after this correction.

Scope: computation_false

删左边界后递推常数κ进入末端detector，末态必须满足H_Zσ_R=κ。原式只改Aκ却继续用v(σ)=1[H_Zσ=0且非零逻辑]，直接算错边界公式。

维持旧错误确认；这是计算/公式错误，不必因为对象随模型变化就自动标overclaim。

## Original materials

- [original/M01-circdist_sat_transfer_proof_20260823.md](original/M01-circdist_sat_transfer_proof_20260823.md)
- [original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md](original/M02-circdist_sat_transfer_endtoend_exact_review_20260826.md)
- [original/M03-circdist_sat_transfer_amendment1_20260823.md](original/M03-circdist_sat_transfer_amendment1_20260823.md)
- [original/M05-SAT_RESCOPE_20260822.md](original/M05-SAT_RESCOPE_20260822.md)
- [original/M06-CIRCDIST_PROBLEMS.md](original/M06-CIRCDIST_PROBLEMS.md)
- [original/M07-circdist_sat_window_theorem_20260822.md](original/M07-circdist_sat_window_theorem_20260822.md)
- [original/M08-circdist_sat_recon_20260820.md](original/M08-circdist_sat_recon_20260820.md)
- [original/M09-circdist_sat_window_amendment1_20260822.md](original/M09-circdist_sat_window_amendment1_20260822.md)
- [original/M10-circdist_sat_window_review_20260822.md](original/M10-circdist_sat_window_review_20260822.md)
- [original/M11-circdist_lift_nonint_proof_20260820.md](original/M11-circdist_lift_nonint_proof_20260820.md)
- [original/M12-CIRCDIST.sat.transfer.yaml](original/M12-CIRCDIST.sat.transfer.yaml)
- [original/M13-CIRCDIST.sat.transfer.yaml](original/M13-CIRCDIST.sat.transfer.yaml)
- [original/M14-CIRCDIST_PROBLEMS.md](original/M14-CIRCDIST_PROBLEMS.md)
- [original/M15-SAT_RESCOPE_20260822.md](original/M15-SAT_RESCOPE_20260822.md)
- [original/M16-circdist_sat_transfer_review_20260823.md](original/M16-circdist_sat_transfer_review_20260823.md)
- [original/M17-circdist_sat_transfer_rereview_20260823.md](original/M17-circdist_sat_transfer_rereview_20260823.md)
- [original/M18-circdist_transfer_bridgefold_20260823.md](original/M18-circdist_transfer_bridgefold_20260823.md)
- [original/M19-circdist_sat_window_theorem_20260822.md](original/M19-circdist_sat_window_theorem_20260822.md)
- [original/M20-circdist_sat_window_amendment1_20260822.md](original/M20-circdist_sat_window_amendment1_20260822.md)
- [original/M21-circdist_sat_window_review_20260822.md](original/M21-circdist_sat_window_review_20260822.md)
- [original/M22-circdist_amendments4_review_20260822.md](original/M22-circdist_amendments4_review_20260822.md)
- [original/M23-circdist_readjudication_20260823.md](original/M23-circdist_readjudication_20260823.md)
- [original/M24-circdist_sat_window_selfcontained_exact_proof_20260826.md](original/M24-circdist_sat_window_selfcontained_exact_proof_20260826.md)
- [original/M25-circdist_sat_window_selfcontained_exact_review_20260826.md](original/M25-circdist_sat_window_selfcontained_exact_review_20260826.md)
- [original/M26-circdist_sat_v3_exact_text_review_20260826.md](original/M26-circdist_sat_v3_exact_text_review_20260826.md)
- [original/M27-circdist_sat_instances_window_edge_exact_review_20260826.md](original/M27-circdist_sat_instances_window_edge_exact_review_20260826.md)
- [original/M28-circdist_sat_window_downstream_scope_rebind_review_20260826.md](original/M28-circdist_sat_window_downstream_scope_rebind_review_20260826.md)
- [original/M29-circdist_sat_root_assembly_20260823.md](original/M29-circdist_sat_root_assembly_20260823.md)
- [original/M30-circdist_sat_root_review_20260823.md](original/M30-circdist_sat_root_review_20260823.md)
- [original/M31-circdist_sat_root_proved_adjudication_20260823.md](original/M31-circdist_sat_root_proved_adjudication_20260823.md)
- [original/M32-CIRCDIST.sat.transfer.yaml](original/M32-CIRCDIST.sat.transfer.yaml)
- [original/M33-proof_dag_check.py](original/M33-proof_dag_check.py)
- [original/M34-SCHEDULER.yaml](original/M34-SCHEDULER.yaml)
- [original/M35-circdist_sat_recon_20260820.md](original/M35-circdist_sat_recon_20260820.md)
- [original/M36-evidence_closure_check.py](original/M36-evidence_closure_check.py)
- [original/M37-check_circdist_migration.py](original/M37-check_circdist_migration.py)
- [original/M38-check_event_append_only.py](original/M38-check_event_append_only.py)
- [original/M39-circdist_sat_transfer_review_20260823.md](original/M39-circdist_sat_transfer_review_20260823.md)
- [original/M40-circdist_sat_transfer_proof_20260823.md](original/M40-circdist_sat_transfer_proof_20260823.md)
- [original/context/R01-M01-circdist_sat_transfer_proof_20260823.md.context.md](original/context/R01-M01-circdist_sat_transfer_proof_20260823.md.context.md)
- [original/context/R02-M03-circdist_sat_transfer_amendment1_20260823.md.context.md](original/context/R02-M03-circdist_sat_transfer_amendment1_20260823.md.context.md)

[Back to all 65 errors](../../README.md)
