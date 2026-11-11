# 033 — The whole-code ceiling applies to the minimum over memory sectors, not separately to each sector. A sector whose logical distance exceeds d can have no witness within the stated weight budget.

**Research problem:** P06 — Circuit versus effective distance

## Original statement

> 2. `d_circ` is computable from the one-round data `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a
>    search over fault multisets of size `≤ d` distributed over `≤ d` consecutive rounds. No
>    multi-round circuit is constructed at any point.

**Context:** All statements in the relevant part of the proof concern one memory sector. The variable d is the static whole-code distance min(d_X,d_Z), but the algorithmic search truncates both fault weight and round span at d.

**Original locator:** Proof draft dated 20 August 2026, conjectured Corollary 5.10(2), lines 859–861; sector convention in Definition 1.5.

## Why it is an error

The whole-code ceiling applies to the minimum over memory sectors, not separately to each sector. A sector whose logical distance exceeds d can have no witness within the stated weight budget.

## Witness / evidence

Use n=6, X-check supports {0,1},{2,3},{4,5}, and Z-check supports {0,1,2,3},{2,3,4,5}. The code has k=1, d_X=3, d_Z=2, and d=2. A non-interleaved list schedule with ideal boundaries has effective and Z-memory circuit distance 3; the archived direct multi-round check reports 3 for R=1,2,3,4. Consequently searching only fault multisets of size ≤d=2 returns no Z-memory logical witness; using the sector bound d_X=3 returns the correct value. The claimed global proof target is not thereby refuted; the per-sector truncation constant is wrong.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 将全码距离 min(d_X,d_Z) 用作每个独立扇区的搜索上限。全局最小值不能为较大扇区提供这个截断保证。

## Adjudication notes

The whole-code ceiling applies to the minimum over memory sectors, not separately to each sector. A sector whose logical distance exceeds d can have no witness within the stated weight budget.

Use n=6, X-check supports {0,1},{2,3},{4,5}, and Z-check supports {0,1,2,3},{2,3,4,5}. The code has k=1, d_X=3, d_Z=2, and d=2. A non-interleaved list schedule with ideal boundaries has effective and Z-memory circuit distance 3; the archived direct multi-round check reports 3 for R=1,2,3,4. Consequently searching only fault multisets of size ≤d=2 returns no Z-memory logical witness; using the sector bound d_X=3 returns the correct value. The claimed global proof target is not thereby refuted; the per-sector truncation constant is wrong.

Scope: argument_invalid

整体min(d_X,d_Z)的d上界不能逐扇区使用；原§5全为Z-memory，却把搜索权重上限设为整体d。n=6不对称CSS例子该扇区距离3而整体d=2，搜索截断漏解。

维持旧对象/量词越界裁定；不因根问题未完成或未重跑所有日程降级。

## Original materials

- [original/M01-circdist_lift_iff_proof_20260820.md](original/M01-circdist_lift_iff_proof_20260820.md)
- [original/M02-circdist_lift_claimrepair2_review_20260823.md](original/M02-circdist_lift_claimrepair2_review_20260823.md)
- [original/M03-circdist_lift_iff_amendment2_20260820.md](original/M03-circdist_lift_iff_amendment2_20260820.md)
- [original/M05-CIRCDIST_PROBLEMS.md](original/M05-CIRCDIST_PROBLEMS.md)
- [original/M06-circdist_lift_litverify2_20260820.md](original/M06-circdist_lift_litverify2_20260820.md)
- [original/M07-circdist_lift_nonint_proof_20260820.md](original/M07-circdist_lift_nonint_proof_20260820.md)
- [original/M08-circdist_lift_d3gate_20260820.md](original/M08-circdist_lift_d3gate_20260820.md)
- [original/M09-circdist_iff_scope_adjudication_20260823.md](original/M09-circdist_iff_scope_adjudication_20260823.md)
- [original/M10-circdist_claimrepair_review_20260823.md](original/M10-circdist_claimrepair_review_20260823.md)
- [original/M11-circdist_amendments4_review_20260822.md](original/M11-circdist_amendments4_review_20260822.md)
- [original/M12-CIRCDIST.lift.iff.yaml](original/M12-CIRCDIST.lift.iff.yaml)
- [original/M13-CIRCDIST.lift.yaml](original/M13-CIRCDIST.lift.yaml)
- [original/M14-CIRCDIST.lift.nonint.yaml](original/M14-CIRCDIST.lift.nonint.yaml)
- [original/M15-circdist_lift_iff_proof_20260820.md](original/M15-circdist_lift_iff_proof_20260820.md)
- [original/M16-circdist_lift_iff_amendment1_20260820.md](original/M16-circdist_lift_iff_amendment1_20260820.md)
- [original/M17-circdist_lift_iff_amendment2_20260820.md](original/M17-circdist_lift_iff_amendment2_20260820.md)
- [original/M18-circdist_lift_proofs_review_20260820.md](original/M18-circdist_lift_proofs_review_20260820.md)
- [original/M19-circdist_amendments2_review_20260820.md](original/M19-circdist_amendments2_review_20260820.md)
- [original/M20-circdist_lift_root_review_20260822.md](original/M20-circdist_lift_root_review_20260822.md)
- [original/M21-DAG_PROTOCOL.md](original/M21-DAG_PROTOCOL.md)
- [original/M22-circdist_amendments_review_20260820.md](original/M22-circdist_amendments_review_20260820.md)
- [original/context/R01-M01-circdist_lift_iff_proof_20260820.md.context.md](original/context/R01-M01-circdist_lift_iff_proof_20260820.md.context.md)
- [original/context/R02-M02-circdist_lift_claimrepair2_review_20260823.md.context.md](original/context/R02-M02-circdist_lift_claimrepair2_review_20260823.md.context.md)

[Back to all 65 errors](../../README.md)
