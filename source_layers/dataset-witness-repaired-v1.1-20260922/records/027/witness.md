# Record 027 — Bound entanglement with negative partial transpose

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> - 2026-07-29 — decision-layer reduction note (unreviewed): K_i = (1/2)(I + 2 Pi_i^asym) gives
>   K = 2^{-k} sum_S 2^{|S|} Pi_S with POSITIVE coefficients, so M1 follows if each elementary
>   exchange matrix E^S_pq = <x_p (x) y_q, Pi_S(x_q (x) y_p)> is PSD; S = empty is Schur-PSD; k=1
>   S={1} reduces to the Pluecker-type inequality |<x1^y2, x2^y1>|^2 <= ||x1^y1||^2 ||x2^y2||^2.
>   Phase-2 task P1 screens E_S numerically FIRST, then attempts proofs.

Context: A tentative sufficient condition was proposed in an unfinished NPT-bound-entanglement investigation. Here Pi_i^asym=(I-F_i)/2, Pi_S is the product over selected copies, and E^S is the 2 by 2 exchange matrix displayed in the excerpt. The note is explicitly unreviewed and asks for screening before proofs. The positive-coefficient expansion and conditional implication are correct. The refuted mathematical object is the proposed per-subset PSD condition and its k=1 inequality, not the expansion, not the main undistillability theorem, and not a theorem-completion claim.

Locator: Research-node work record dated 2026-07-29, original lines 60-64; assistant report at 2026-07-29T23:07:43.892Z also calls this reduction pending verification.

## 2. Witness / adjudication

The proposed universal PSD strengthening is false even for one copy. A positive projector does not make this exchange matrix a Gram matrix with a common ordered vector list.

Take k=1, S={1}, d=2 (or embed into any d>=2), x1=y1=e1 and x2=y2=e2 with e1,e2 orthonormal. With Pi=(I-F)/2, E11=E22=0 and E12=E21=-1/2. Thus E=[[0,-1/2],[-1/2,0]], and (1,1) E (1,1)^T=-1<0; the eigenvalues are -1/2 and 1/2. In contrast K=I-F/2 gives G=[[1/2,-1/2],[-1/2,1/2]], which is PSD. This explicitly disproves the proposed per-subset condition without disproving the target matrix condition. The claimed wedge inequality also has right side zero (e_i wedge e_i=0) and nonzero left side. These are exact hand calculations, independently recorded in the archived verification.

Scope: tentative_candidate_refuted

原笔记的正系数分解与“若每个 E_S 为 PSD 则目标成立”均正确，并明确要求先筛查。E=[[0,-1/2],[-1/2,0]] 只推翻拟尝试的逐子集 PSD 条件。保留为失败候选，不记证明错误或 overclaim。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-NPTBE.k3.R1.m1.md](original/M01-NPTBE.k3.R1.m1.md) — inherited_sanitized_source
- [M02-<session-id-redacted>.jsonl.readable.md](original/M02-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M02-<session-id-redacted>.jsonl.visible.json](original/M02-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M03-P4_REVIEW.md](original/M03-P4_REVIEW.md) — inherited_sanitized_source
- [M04-p4_ES_reduction.py](original/M04-p4_ES_reduction.py) — inherited_sanitized_source
- [M05-p4_ES_reduction.log](original/M05-p4_ES_reduction.log) — inherited_sanitized_source
- [M06-p4_ES_reduction.json](original/M06-p4_ES_reduction.json) — inherited_sanitized_source
- [M07-CLAUDE_CAMPAIGNS_20260821.json](original/M07-CLAUDE_CAMPAIGNS_20260821.json) — inherited_sanitized_source
- [M08-nptbe_k3_p2_synthesis_20260730.md](original/M08-nptbe_k3_p2_synthesis_20260730.md) — inherited_sanitized_source
- [M09-nptbe_k3_fleet_phase1_synthesis_20260729.md](original/M09-nptbe_k3_fleet_phase1_synthesis_20260729.md) — inherited_sanitized_source
- [M10-nptbe_p2_p4_identities2.py](original/M10-nptbe_p2_p4_identities2.py) — inherited_sanitized_source
- [M11-nptbe_p2_p4_exact_recert.py](original/M11-nptbe_p2_p4_exact_recert.py) — inherited_sanitized_source
- [M12-nptbe_p2_p4_w4_audit.py](original/M12-nptbe_p2_p4_w4_audit.py) — inherited_sanitized_source
- [M13-nptbe_p2_p4_cross_fast.py](original/M13-nptbe_p2_p4_cross_fast.py) — inherited_sanitized_source
- [M14-grid_d5.log](original/M14-grid_d5.log) — inherited_sanitized_source
- [M15-grid_d6.log](original/M15-grid_d6.log) — inherited_sanitized_source
- [M16-ranklaw_d5.log](original/M16-ranklaw_d5.log) — inherited_sanitized_source
- [M17-mechanism_probe.log](original/M17-mechanism_probe.log) — inherited_sanitized_source
- [M18-d4k4.log](original/M18-d4k4.log) — inherited_sanitized_source
- [M19-nptbe_p2_p4_cross_at_tight.py](original/M19-nptbe_p2_p4_cross_at_tight.py) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
