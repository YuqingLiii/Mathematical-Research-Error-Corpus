# Record 032 — Circuit versus effective distance

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> **CONJECTURED 5.10 (saturation and one-round decidability).** Consequences of 5.9:
> 
> 1. `d_R(M) := d_circ(C_R(M))` is non-increasing in `R` and **constant for all `R ≥ d`**; i.e.
>    `R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model.

**Recorded location:** Proof draft dated 20 August 2026, conjectured Corollary 5.10(1), lines 855–858.

**Context (annotation, not a source quotation):** The historical saturation index was defined as the first round count after which circuit distance equals the static code distance d forever, with infinity if this never happens. It was not the index of convergence to an arbitrary lower limiting value. The quoted corollary was labelled CONJECTURED.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Eventual constancy of d_R does not imply eventual equality to d. The argument substitutes stabilization for the stronger saturation-to-code-distance definition.

### Argument or calculation

Take the Steane [[7,1,3]] code with X- and Z-check supports {3,4,5,6}, {1,2,5,6}, and {0,2,4,6}. Use increasing within-check orders, all X checks followed by all Z checks, and ideal temporal boundaries. In the X check ordered (0,2,4,6), an ancilla-X fault after the second CNOT produces residual X on {4,6}. Add one data-X fault on qubit 1 before the Z-check block. The net support {1,4,6} meets each listed Z check in zero or two positions, and is not an X stabilizer: every nonzero word in their X-check rowspace has weight four, whereas this support has weight three. Thus two faults produce an undetected logical X. Appending fault-free rounds preserves this witness, so d_R≤2 for every R; it can never equal the static distance d=3 eventually. Therefore R_sat=infinity, contradicting R_sat≤3. Only the saturation-to-d claim is refuted, not eventual constancy at a lower value. The original archived calculation also reports d_eff=2 and d_R=2 for R=1,2,3,4.

Scope: tentative_candidate_refuted.


### Archived review excerpt

>    R_sat(M) = min{ R_0 : d_R(M) = d  for all R ≥ R_0 },     = ∞ if no such R_0.
> ```
> 
> Saturation is at the **code distance `d`**, not at `lim_R d_R`. Contiguity gives the latter. When
> `d_∞(M) < d` — the generic hook-damaged case — `R_sat(M) = ∞`, not `≤ d`.
> 
> **Explicit counterexample, computed this session.** Steane `[[7,1,3]]`, natural within-check orders
> `X_i = Z_i = supp` in index order, non-interleaved (either block order), legal, `MC = ∅`:
> `d_eff = 2 < 3 = d`, and my exhaustive weight-`≤3` search gives `d_R = 2` for `R = 1,2,3,4`. Hence
> `R_sat = ∞`. The claim `R_sat ≤ d = 3` is false here. (Twelve further non-interleaved
> configurations in §4.4 with `d_eff < d` are additional witnesses.)
> 
> **The sibling document gets this right and the two contradict each other.** nonint Corollary 7.3:
> "`R_sat(M) = 1` if `d_eff(M) = d`, `R_sat(M) = ∞` if `d_eff(M) < d`." That is correct. The

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 较早推理明确说 R_sat 可能为无穷；后续论述把稳定到 d∞ 同达到目标码距 d 混为一谈，输出 R_sat≤d。属于例外未保留且概念混淆，不是纯抄写错误。

- [2026-08-20T15:43:37.650Z — claude_visible_thinking](original/M05-agent-afd9b18b206ce896f.jsonl.readable.md) — source line 17; recorded role: generation.
- [2026-08-20T15:54:10.293Z — claude_visible_thinking](original/M05-agent-afd9b18b206ce896f.jsonl.readable.md) — source line 18; recorded role: generation.

## Original materials

- [M01: circdist_lift_iff_proof_20260820.md](original/M01-circdist_lift_iff_proof_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): lines 855–858; #L855-863 (5.10(1)), L1167-1169 (sec8 item4)
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md`

- [M02: circdist_lift_proofs_review_20260820.md](original/M02-circdist_lift_proofs_review_20260820.md "research-graph/circdist/reviews/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): §3.3; lines 228–241; #3.3
  - Source: `research-graph/circdist/reviews/circdist_lift_proofs_review_20260820.md`

- [M03: circdist_lift_iff_amendment1_20260820.md](original/M03-circdist_lift_iff_amendment1_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_amendment1_20260820.md")
  - Coverage: Full bundled file; source lines 1–619.
  - Relevant location(s): #L206-277
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_amendment1_20260820.md`

- [M04: circdist_lift_nonint_proof_20260820.md](original/M04-circdist_lift_nonint_proof_20260820.md "research-graph/circdist/artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): #Cor7.3
  - Source: `research-graph/circdist/artifacts/circdist_lift_nonint_proof_20260820.md`

- [M05: agent-afd9b18b206ce896f.jsonl](original/M05-agent-afd9b18b206ce896f.jsonl.readable.md "claude-session-archive/agent-afd9b18b206ce896f.jsonl") · [event data](original/M05-agent-afd9b18b206ce896f.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 11–24, 50–62.
  - Relevant location(s): lines 17; lines 18; lines 56
  - Source: `claude-session-archive/agent-afd9b18b206ce896f.jsonl`

- [M06: CIRCDIST_PROBLEMS.md](original/M06-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md; Referenced by research-graph/circdist/reviews/circdist_lift_proofs_review_20260820.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_amendment1_20260820.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M07: circdist_lift_litverify2_20260820.md](original/M07-circdist_lift_litverify2_20260820.md "artifacts/circdist_lift_litverify2_20260820.md")
  - Coverage: Full bundled file; source lines 1–55.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_litverify2_20260820.md`

- [M08: circdist_lift_nonint_proof_20260820.md](original/M08-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_amendment1_20260820.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M09: circdist_lift_d3gate_20260820.md](original/M09-circdist_lift_d3gate_20260820.md "artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_d3gate_20260820.md`

- [M10: circdist_lift_iff_proof_20260820.md](original/M10-circdist_lift_iff_proof_20260820.md "artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_amendment1_20260820.md
  - Source: `artifacts/circdist_lift_iff_proof_20260820.md`

- [M11: circdist_lift_proofs_review_20260820.md](original/M11-circdist_lift_proofs_review_20260820.md "artifacts/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_amendment1_20260820.md
  - Source: `artifacts/circdist_lift_proofs_review_20260820.md`
