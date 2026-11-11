# Record 033 — Circuit versus effective distance

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> 2. `d_circ` is computable from the one-round data `{(E(f), s(f), u(f), λ(f)) : f ∈ 𝔽}` alone, by a
>    search over fault multisets of size `≤ d` distributed over `≤ d` consecutive rounds. No
>    multi-round circuit is constructed at any point.

**Recorded location:** Proof draft dated 20 August 2026, conjectured Corollary 5.10(2), lines 859–861; sector convention in Definition 1.5.

**Context (annotation, not a source quotation):** All statements in the relevant part of the proof concern one memory sector. The variable d is the static whole-code distance min(d_X,d_Z), but the algorithmic search truncates both fault weight and round span at d.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The whole-code ceiling applies to the minimum over memory sectors, not separately to each sector. A sector whose logical distance exceeds d can have no witness within the stated weight budget.

### Argument or calculation

Use n=6, X-check supports {0,1},{2,3},{4,5}, and Z-check supports {0,1,2,3},{2,3,4,5}. The code has k=1, d_X=3, d_Z=2, and d=2. A non-interleaved list schedule with ideal boundaries has effective and Z-memory circuit distance 3; the archived direct multi-round check reports 3 for R=1,2,3,4. Consequently searching only fault multisets of size ≤d=2 returns no Z-memory logical witness; using the sector bound d_X=3 returns the correct value. The claimed global proof target is not thereby refuted; the per-sector truncation constant is wrong.

Scope: argument_invalid.


### Archived review excerpt

> ### 4.3 **DEFECT — the stated bound is the wrong constant, and it is false per sector**
> 
> 5.10(2) fixes the search size **and** the window at the **code distance `d`**. That constant comes
> from the trailing chain of 5.9, "round-span(`F`) `≤ |F| = d_circ ≤ d`", and from 5.10(1)/(1′),
> "`d_R` … constant for all `R ≥ d`" — which Amendment 1 §3 restates explicitly **"per sector"**, and
> whose ceiling Amendment 2 §3 sources to the 公共定义: *"The 公共定义 gives `d_R(M) <= d` for every
> `R`"*.
> 
> The 公共定义's inequality is `d_eff(M) <= d_circ(C(M)) <= d`, written for the **circuit** `C(M)`.
> Definition 1.5 of the proof document defines `d_circ(C)` as the **min over the two memory sectors**.
> But all of §5 is per-sector ("All statements below are for the Z-memory"). Per sector the only
> available bound is `d_circ^{Z-mem} ≤ d_X`, and `d = min(d_X, d_Z)`. **For a CSS code with
> `d_Z < d_X` the transposition fails.**
> 
> I built such an instance and measured it (§4.5): `n = 6`, X-checks `{0,1},{2,3},{4,5}`, Z-checks
> `{0,1,2,3},{2,3,4,5}`, `k = 1`; `d_X = 3`, `d_Z = 2`, so `d = 2`. Non-interleaved list-scheduled
> single-ancilla CSS circuit (hence legal and (MC)-automatic), ideal boundaries. **This instance is
> `graph-like` in the Z-memory sector (Def 1.12 verified on all 91 elementary faults, 0 violations),
> so it lies inside the repaired claim's own scope.** Measured, by direct multi-round simulation:
> 
> ```
>   d_eff = 3 ;  d_circ(Z-memory) = 3  at R = 1,2,3,4     while  d = 2
>   5.10(2) as stated, W = d = 2      ->  returns NOTHING     <-- defect
>   5.10(2) with W = d_X = 3          ->  returns 3           <-- correct
> ```

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理已用全局码距 d 为固定 memory sector 的 d_circ 构造上界，正文沿用；非对称 CSS 的扇区码距不允许这样替换。

- [2026-08-20T15:54:10.293Z — claude_visible_thinking](original/M04-agent-afd9b18b206ce896f.jsonl.readable.md) — source line 18; recorded role: generation.

## Original materials

- [M01: circdist_lift_iff_proof_20260820.md](original/M01-circdist_lift_iff_proof_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): lines 859–861; #L127-130 (Def1.5), L859-861 (5.10(2))
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md`

- [M02: circdist_lift_claimrepair2_review_20260823.md](original/M02-circdist_lift_claimrepair2_review_20260823.md "research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–477.
  - Relevant location(s): §4.3; lines 194–218; #4.3,4.5; #4.3
  - Source: `research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md`

- [M03: circdist_lift_iff_amendment2_20260820.md](original/M03-circdist_lift_iff_amendment2_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_amendment2_20260820.md")
  - Coverage: Full bundled file; source lines 1–240.
  - Relevant location(s): #L167-171
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_amendment2_20260820.md`

- [M04: agent-afd9b18b206ce896f.jsonl](original/M04-agent-afd9b18b206ce896f.jsonl.readable.md "claude-session-archive/agent-afd9b18b206ce896f.jsonl") · [event data](original/M04-agent-afd9b18b206ce896f.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 12–24, 50–62.
  - Relevant location(s): lines 18; lines 56
  - Source: `claude-session-archive/agent-afd9b18b206ce896f.jsonl`

- [M05: CIRCDIST_PROBLEMS.md](original/M05-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md; Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_amendment2_20260820.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M06: circdist_lift_litverify2_20260820.md](original/M06-circdist_lift_litverify2_20260820.md "artifacts/circdist_lift_litverify2_20260820.md")
  - Coverage: Full bundled file; source lines 1–55.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_litverify2_20260820.md`

- [M07: circdist_lift_nonint_proof_20260820.md](original/M07-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M08: circdist_lift_d3gate_20260820.md](original/M08-circdist_lift_d3gate_20260820.md "artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md; Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `artifacts/circdist_lift_d3gate_20260820.md`

- [M09: circdist_iff_scope_adjudication_20260823.md](original/M09-circdist_iff_scope_adjudication_20260823.md "research-graph/artifacts/circdist_iff_scope_adjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–449.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `research-graph/artifacts/circdist_iff_scope_adjudication_20260823.md`

- [M10: circdist_claimrepair_review_20260823.md](original/M10-circdist_claimrepair_review_20260823.md "research-graph/artifacts/circdist_claimrepair_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–219.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `research-graph/artifacts/circdist_claimrepair_review_20260823.md`

- [M11: circdist_amendments4_review_20260822.md](original/M11-circdist_amendments4_review_20260822.md "artifacts/circdist_amendments4_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–545.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `artifacts/circdist_amendments4_review_20260822.md`

- [M12: CIRCDIST.lift.iff.yaml](original/M12-CIRCDIST.lift.iff.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml")
  - Coverage: Full bundled file; source lines 1–188.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml`

- [M13: CIRCDIST.lift.yaml](original/M13-CIRCDIST.lift.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml")
  - Coverage: Full bundled file; source lines 1–198.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml`

- [M14: CIRCDIST.lift.nonint.yaml](original/M14-CIRCDIST.lift.nonint.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml")
  - Coverage: Full bundled file; source lines 1–94.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml`

- [M15: circdist_lift_iff_proof_20260820.md](original/M15-circdist_lift_iff_proof_20260820.md "artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_amendment2_20260820.md
  - Source: `artifacts/circdist_lift_iff_proof_20260820.md`

- [M16: circdist_lift_iff_amendment1_20260820.md](original/M16-circdist_lift_iff_amendment1_20260820.md "artifacts/circdist_lift_iff_amendment1_20260820.md")
  - Coverage: Full bundled file; source lines 1–619.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_amendment2_20260820.md
  - Source: `artifacts/circdist_lift_iff_amendment1_20260820.md`

- [M17: circdist_lift_iff_amendment2_20260820.md](original/M17-circdist_lift_iff_amendment2_20260820.md "artifacts/circdist_lift_iff_amendment2_20260820.md")
  - Coverage: Full bundled file; source lines 1–240.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `artifacts/circdist_lift_iff_amendment2_20260820.md`

- [M18: circdist_lift_proofs_review_20260820.md](original/M18-circdist_lift_proofs_review_20260820.md "artifacts/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `artifacts/circdist_lift_proofs_review_20260820.md`

- [M19: circdist_amendments2_review_20260820.md](original/M19-circdist_amendments2_review_20260820.md "artifacts/circdist_amendments2_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–362.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `artifacts/circdist_amendments2_review_20260820.md`

- [M20: circdist_lift_root_review_20260822.md](original/M20-circdist_lift_root_review_20260822.md "artifacts/circdist_lift_root_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–498.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `artifacts/circdist_lift_root_review_20260822.md`

- [M21: DAG_PROTOCOL.md](original/M21-DAG_PROTOCOL.md "research/DAG_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–316.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md
  - Source: `research/DAG_PROTOCOL.md`

- [M22: circdist_amendments_review_20260820.md](original/M22-circdist_amendments_review_20260820.md "artifacts/circdist_amendments_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–571.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_amendment2_20260820.md
  - Source: `artifacts/circdist_amendments_review_20260820.md`
