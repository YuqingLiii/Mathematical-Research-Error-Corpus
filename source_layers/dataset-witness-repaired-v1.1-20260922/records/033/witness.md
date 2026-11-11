# Record 033 — Circuit versus effective distance

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> 2. `d_circ` is computable from the one-round data `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a
>    search over fault multisets of size `≤ d` distributed over `≤ d` consecutive rounds. No
>    multi-round circuit is constructed at any point.

Context: All statements in the relevant part of the proof concern one memory sector. The variable d is the static whole-code distance min(d_X,d_Z), but the algorithmic search truncates both fault weight and round span at d.

Locator: Proof draft dated 20 August 2026, conjectured Corollary 5.10(2), lines 859–861; sector convention in Definition 1.5.

## 2. Witness / adjudication

The whole-code ceiling applies to the minimum over memory sectors, not separately to each sector. A sector whose logical distance exceeds d can have no witness within the stated weight budget.

Use n=6, X-check supports {0,1},{2,3},{4,5}, and Z-check supports {0,1,2,3},{2,3,4,5}. The code has k=1, d_X=3, d_Z=2, and d=2. A non-interleaved list schedule with ideal boundaries has effective and Z-memory circuit distance 3; the archived direct multi-round check reports 3 for R=1,2,3,4. Consequently searching only fault multisets of size ≤d=2 returns no Z-memory logical witness; using the sector bound d_X=3 returns the correct value. The claimed global proof target is not thereby refuted; the per-sector truncation constant is wrong.

Scope: argument_invalid

整体min(d_X,d_Z)的d上界不能逐扇区使用；原§5全为Z-memory，却把搜索权重上限设为整体d。n=6不对称CSS例子该扇区距离3而整体d=2，搜索截断漏解。

维持旧对象/量词越界裁定；不因根问题未完成或未重跑所有日程降级。

## 3. Evidence and verification

核对给定校验支持与原scope；沿用已有独立多轮计算，未把缺本轮模拟等同原记录缺失。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_lift_iff_proof_20260820.md](original/M01-circdist_lift_iff_proof_20260820.md) — inherited_sanitized_source
- [M02-circdist_lift_claimrepair2_review_20260823.md](original/M02-circdist_lift_claimrepair2_review_20260823.md) — inherited_sanitized_source
- [M03-circdist_lift_iff_amendment2_20260820.md](original/M03-circdist_lift_iff_amendment2_20260820.md) — inherited_sanitized_source
- [M04-agent-afd9b18b206ce896f.jsonl.readable.md](original/M04-agent-afd9b18b206ce896f.jsonl.readable.md) — inherited_sanitized_source
- [M04-agent-afd9b18b206ce896f.jsonl.visible.json](original/M04-agent-afd9b18b206ce896f.jsonl.visible.json) — inherited_sanitized_source
- [M05-CIRCDIST_PROBLEMS.md](original/M05-CIRCDIST_PROBLEMS.md) — inherited_sanitized_source
- [M06-circdist_lift_litverify2_20260820.md](original/M06-circdist_lift_litverify2_20260820.md) — inherited_sanitized_source
- [M07-circdist_lift_nonint_proof_20260820.md](original/M07-circdist_lift_nonint_proof_20260820.md) — inherited_sanitized_source
- [M08-circdist_lift_d3gate_20260820.md](original/M08-circdist_lift_d3gate_20260820.md) — inherited_sanitized_source
- [M09-circdist_iff_scope_adjudication_20260823.md](original/M09-circdist_iff_scope_adjudication_20260823.md) — inherited_sanitized_source
- [M10-circdist_claimrepair_review_20260823.md](original/M10-circdist_claimrepair_review_20260823.md) — inherited_sanitized_source
- [M11-circdist_amendments4_review_20260822.md](original/M11-circdist_amendments4_review_20260822.md) — inherited_sanitized_source
- [M12-CIRCDIST.lift.iff.yaml](original/M12-CIRCDIST.lift.iff.yaml) — inherited_sanitized_source
- [M13-CIRCDIST.lift.yaml](original/M13-CIRCDIST.lift.yaml) — inherited_sanitized_source
- [M14-CIRCDIST.lift.nonint.yaml](original/M14-CIRCDIST.lift.nonint.yaml) — inherited_sanitized_source
- [M15-circdist_lift_iff_proof_20260820.md](original/M15-circdist_lift_iff_proof_20260820.md) — inherited_sanitized_source
- [M16-circdist_lift_iff_amendment1_20260820.md](original/M16-circdist_lift_iff_amendment1_20260820.md) — inherited_sanitized_source
- [M17-circdist_lift_iff_amendment2_20260820.md](original/M17-circdist_lift_iff_amendment2_20260820.md) — inherited_sanitized_source
- [M18-circdist_lift_proofs_review_20260820.md](original/M18-circdist_lift_proofs_review_20260820.md) — inherited_sanitized_source
- [M19-circdist_amendments2_review_20260820.md](original/M19-circdist_amendments2_review_20260820.md) — inherited_sanitized_source
- [M20-circdist_lift_root_review_20260822.md](original/M20-circdist_lift_root_review_20260822.md) — inherited_sanitized_source
- [M21-DAG_PROTOCOL.md](original/M21-DAG_PROTOCOL.md) — inherited_sanitized_source
- [M22-circdist_amendments_review_20260820.md](original/M22-circdist_amendments_review_20260820.md) — inherited_sanitized_source
- [R01-M01-circdist_lift_iff_proof_20260820.md.context.md](reconciliation_sources/R01-M01-circdist_lift_iff_proof_20260820.md.context.md) — reconciliation_source_window
- [R02-M02-circdist_lift_claimrepair2_review_20260823.md.context.md](reconciliation_sources/R02-M02-circdist_lift_claimrepair2_review_20260823.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
