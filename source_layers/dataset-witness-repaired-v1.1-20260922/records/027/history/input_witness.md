# Record 027 — Bound entanglement with negative partial transpose

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> - 2026-07-29 — decision-layer reduction note (unreviewed): K_i = (1/2)(I + 2 Pi_i^asym) gives
>   K = 2^{-k} sum_S 2^{|S|} Pi_S with POSITIVE coefficients, so M1 follows if each elementary
>   exchange matrix E^S_pq = <x_p (x) y_q, Pi_S(x_q (x) y_p)> is PSD; S = empty is Schur-PSD; k=1
>   S={1} reduces to the Pluecker-type inequality |<x1^y2, x2^y1>|^2 <= ||x1^y1||^2 ||x2^y2||^2.
>   Phase-2 task P1 screens E_S numerically FIRST, then attempts proofs.

**Recorded location:** Research-node work record dated 2026-07-29, original lines 60-64; assistant report at 2026-07-29T23:07:43.892Z also calls this reduction pending verification.

**Context (annotation, not a source quotation):** A tentative sufficient condition was proposed in an unfinished NPT-bound-entanglement investigation. Here Pi_i^asym=(I-F_i)/2, Pi_S is the product over selected copies, and E^S is the 2 by 2 exchange matrix displayed in the excerpt. The note is explicitly unreviewed and asks for screening before proofs. The positive-coefficient expansion and conditional implication are correct. The refuted mathematical object is the proposed per-subset PSD condition and its k=1 inequality, not the expansion, not the main undistillability theorem, and not a theorem-completion claim.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The proposed universal PSD strengthening is false even for one copy. A positive projector does not make this exchange matrix a Gram matrix with a common ordered vector list.

### Argument or calculation

Take k=1, S={1}, d=2 (or embed into any d>=2), x1=y1=e1 and x2=y2=e2 with e1,e2 orthonormal. With Pi=(I-F)/2, E11=E22=0 and E12=E21=-1/2. Thus E=[[0,-1/2],[-1/2,0]], and (1,1) E (1,1)^T=-1<0; the eigenvalues are -1/2 and 1/2. In contrast K=I-F/2 gives G=[[1/2,-1/2],[-1/2,1/2]], which is PSD. This explicitly disproves the proposed per-subset condition without disproving the target matrix condition. The claimed wedge inequality also has right side zero (e_i wedge e_i=0) and nonzero left side. These are exact hand calculations, independently recorded in the archived verification.

Scope: tentative_candidate_refuted.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理已选择逐子集 E_S 半正定辅助引理路线，而其中的辅助候选被反例否定。K 的正系数分解本身不是错误；原文明确说待验证，不能改写成已证明断言。

- [2026-07-29T23:01:00.100Z — claude_visible_thinking](original/M02-<session-id-redacted>.jsonl.readable.md) — source line 1040; recorded role: generation.

## Original materials

- [M01: NPTBE.k3.R1.m1.md](original/M01-NPTBE.k3.R1.m1.md "entanglement-distillation/npt-bound-entanglement/proof-dag/nodes/NPTBE.k3.R1.m1.md")
  - Coverage: Full bundled file; source lines 1–83.
  - Relevant location(s): lines 60-64; contextual original assistant JSONL line 1121; Referenced by entanglement-distillation/npt-bound-entanglement/proof-dag/nodes/NPTBE.k3.R1.m1.md
  - Source: `entanglement-distillation/npt-bound-entanglement/proof-dag/nodes/NPTBE.k3.R1.m1.md`

- [M02: <session-id-redacted>.jsonl](original/M02-<session-id-redacted>.jsonl.readable.md "tracking/claude-proof-records/source-cache/macstudio-recovery/C--Users-wtaph-Documents-discovery-new-algorithms/<session-id-redacted>.jsonl") · [event data](original/M02-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1034–1046, 1105–1127, 1267–1279.
  - Relevant location(s): JSONL lines 1040,1273; #L1040,L1111,L1121,L1273; lines 1040; lines 1121
  - Source: `tracking/claude-proof-records/source-cache/macstudio-recovery/C--Users-wtaph-Documents-discovery-new-algorithms/<session-id-redacted>.jsonl`

- [M03: P4_REVIEW.md](original/M03-P4_REVIEW.md "artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md")
  - Coverage: Full bundled file; source lines 1–426.
  - Relevant location(s): , Finding B; p4_ES_reduction.py and log
  - Source: `artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md`

- [M04: p4_ES_reduction.py](original/M04-p4_ES_reduction.py "artifacts/logs_nptbe_p2_20260729/P4/p4_ES_reduction.py")
  - Coverage: Full bundled file; source lines 1–101.
  - Source: `artifacts/logs_nptbe_p2_20260729/P4/p4_ES_reduction.py`

- [M05: p4_ES_reduction.log](original/M05-p4_ES_reduction.log "artifacts/logs_nptbe_p2_20260729/P4/p4_ES_reduction.log")
  - Coverage: Full bundled file; source lines 1–9.
  - Source: `artifacts/logs_nptbe_p2_20260729/P4/p4_ES_reduction.log`

- [M06: p4_ES_reduction.json](original/M06-p4_ES_reduction.json "artifacts/logs_nptbe_p2_20260729/P4/p4_ES_reduction.json")
  - Coverage: Full bundled file; source lines 1–145.
  - Source: `artifacts/logs_nptbe_p2_20260729/P4/p4_ES_reduction.json`

- [M07: CLAUDE_CAMPAIGNS_20260821.json](original/M07-CLAUDE_CAMPAIGNS_20260821.json "tracking/ai-proof-records-20260912/recovered-marathon-20260821/CLAUDE_CAMPAIGNS_20260821.json")
  - Coverage: Full bundled file; source lines 1–465.
  - Relevant location(s): #campaigns/NPTBE/error_corrections/3
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/CLAUDE_CAMPAIGNS_20260821.json`

- [M08: nptbe_k3_p2_synthesis_20260730.md](original/M08-nptbe_k3_p2_synthesis_20260730.md "artifacts/nptbe_k3_p2_synthesis_20260730.md")
  - Coverage: Full bundled file; source lines 1–76.
  - Relevant location(s): Referenced by entanglement-distillation/npt-bound-entanglement/proof-dag/nodes/NPTBE.k3.R1.m1.md
  - Source: `artifacts/nptbe_k3_p2_synthesis_20260730.md`

- [M09: nptbe_k3_fleet_phase1_synthesis_20260729.md](original/M09-nptbe_k3_fleet_phase1_synthesis_20260729.md "artifacts/nptbe_k3_fleet_phase1_synthesis_20260729.md")
  - Coverage: Full bundled file; source lines 1–101.
  - Relevant location(s): Referenced by entanglement-distillation/npt-bound-entanglement/proof-dag/nodes/NPTBE.k3.R1.m1.md
  - Source: `artifacts/nptbe_k3_fleet_phase1_synthesis_20260729.md`

- [M10: nptbe_p2_p4_identities2.py](original/M10-nptbe_p2_p4_identities2.py "tools/nptbe_p2_p4_identities2.py")
  - Coverage: Full bundled file; source lines 1–250.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `tools/nptbe_p2_p4_identities2.py`

- [M11: nptbe_p2_p4_exact_recert.py](original/M11-nptbe_p2_p4_exact_recert.py "tools/nptbe_p2_p4_exact_recert.py")
  - Coverage: Full bundled file; source lines 1–336.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `tools/nptbe_p2_p4_exact_recert.py`

- [M12: nptbe_p2_p4_w4_audit.py](original/M12-nptbe_p2_p4_w4_audit.py "tools/nptbe_p2_p4_w4_audit.py")
  - Coverage: Full bundled file; source lines 1–144.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `tools/nptbe_p2_p4_w4_audit.py`

- [M13: nptbe_p2_p4_cross_fast.py](original/M13-nptbe_p2_p4_cross_fast.py "tools/nptbe_p2_p4_cross_fast.py")
  - Coverage: Full bundled file; source lines 1–91.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `tools/nptbe_p2_p4_cross_fast.py`

- [M14: grid_d5.log](original/M14-grid_d5.log "artifacts/logs_nptbe_fleet_20260729/W5/grid_d5.log")
  - Coverage: Full bundled file; source lines 1–28.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `artifacts/logs_nptbe_fleet_20260729/W5/grid_d5.log`

- [M15: grid_d6.log](original/M15-grid_d6.log "artifacts/logs_nptbe_fleet_20260729/W5/grid_d6.log")
  - Coverage: Full bundled file; source lines 1–28.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `artifacts/logs_nptbe_fleet_20260729/W5/grid_d6.log`

- [M16: ranklaw_d5.log](original/M16-ranklaw_d5.log "artifacts/logs_nptbe_fleet_20260729/W5/ranklaw_d5.log")
  - Coverage: Full bundled file; source lines 1–8.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `artifacts/logs_nptbe_fleet_20260729/W5/ranklaw_d5.log`

- [M17: mechanism_probe.log](original/M17-mechanism_probe.log "artifacts/logs_nptbe_fleet_20260729/W2/mechanism_probe.log")
  - Coverage: Full bundled file; source lines 1–24.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `artifacts/logs_nptbe_fleet_20260729/W2/mechanism_probe.log`

- [M18: d4k4.log](original/M18-d4k4.log "artifacts/logs_nptbe_fleet_20260729/W5/d4k4.log")
  - Coverage: Full bundled file; source lines 1–9.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `artifacts/logs_nptbe_fleet_20260729/W5/d4k4.log`

- [M19: nptbe_p2_p4_cross_at_tight.py](original/M19-nptbe_p2_p4_cross_at_tight.py "tools/nptbe_p2_p4_cross_at_tight.py")
  - Coverage: Full bundled file; source lines 1–151.
  - Relevant location(s): Referenced by artifacts/logs_nptbe_p2_20260729/P4/P4_REVIEW.md
  - Source: `tools/nptbe_p2_p4_cross_at_tight.py`
