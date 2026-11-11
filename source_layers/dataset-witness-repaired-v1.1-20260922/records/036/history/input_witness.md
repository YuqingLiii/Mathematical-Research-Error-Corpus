# Record 036 — Optimal circuit distance of the Gross code

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> 1. **For the gross code, (MC) *is* [SBB26]'s non-interleaving condition.** Every overlapping
>    (X,Z) check pair shares exactly two qubits (§1), so `c_ab ∈ {0,1,2}`, and `c_ab` even means the
>    two shared CNOT pairs agree on their order, i.e. either all of `a`'s CNOTs on the overlap precede
>    all of `b`'s, or vice versa — S5 verbatim. **CONJECTURED** (the derivation is one line given §1;
>    the risk is only in whether S5's "either…or" is per-pair or global — S6 forces per-pair, since a
>    low-depth LRC cannot satisfy a global split).

**Recorded location:** Proof draft dated 20 August 2026, section 2.4(1), lines 246–251.

**Context (annotation, not a source quotation):** For overlapping X and Z checks, measurement consistency (MC) requires an even number of shared data qubits with Z-before-X local ordering. The draft identifies this pairwise parity condition with non-interleaving, which requires all operations of one check on their common support to precede all operations of the other. The proposed equivalence was labelled CONJECTURED.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Agreement of two pairwise precedence comparisons is strictly weaker than separating the two checks in time. The step after 'i.e.' changes the ordering predicate.

### Argument or calculation

Take common-support gate times A_1=1, B_1=2, A_2=3, B_2=4. Both comparisons B_i<A_i are false, so the MC count is zero (even), but neither max(A)<min(B) nor max(B)<min(A) holds. The archived Gross-specific witness uses time arrays LX(left)=[11,10,3], LX(right)=[7,5,8], LZ(left)=[6,8,5], LZ(right)=[2,1,10]. It has zero MC violations among 648 overlaps, while 288 pairs are interleaved. The elementary four-time example independently refutes the inference from pairwise order agreement to non-interleaving.

Scope: tentative_candidate_refuted.


### Archived review excerpt

> **The equivalence is false.** The target's derivation (§2.4(1)) reads: "`c_ab` even means the two
> shared CNOT pairs agree on their order, i.e. either all of `a`'s CNOTs on the overlap precede all
> of `b`'s, or vice versa — S5 verbatim." The step after "i.e." is a non-sequitur. With shared times
> `A₁,A₂` for `a` and `B₁,B₂` for `b`, "agree" is `(B₁<A₁) ⟺ (B₂<A₂)`; "all before all" is
> `max(A) < min(B)` or `max(B) < min(A)`. `A₁=1 < B₁=2 < A₂=3 < B₂=4` agrees but is interleaved.
> 
> This is not a hypothetical. Searching legal 12-layer translation-invariant gross schedules I found
> one in seconds:
> 
> ```
> LX(left)=[11,10,3]  LX(right)=[7,5,8]  LZ(left)=[6,8,5]  LZ(right)=[2,1,10]
> legal (all four 6-element unions distinct);  (MC) violations 0 / 648
> SBB non-interleaving violated on 4 of the 9 monomial classes  = 288 / 648 pairs
> ```
> 
> So **(MC) ⇏ non-interleaved**. The converse *does* hold (non-interleaved ⇒ each pair separated ⇒
> `c ∈ {0,2}`), which is the in-house Prop. 3.3 the target also cites.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理出现 MC 等价于 non-interleaved 的错误判断，同一块随后也产生怀疑；最终仍写入错误等价。不能只截怀疑句把整段说成正确。

- [2026-08-20T17:03:14.944Z — claude_visible_thinking](original/M05-agent-ace09be0f0bec8908.jsonl.readable.md) — source line 63; recorded role: generation.

## Original materials

- [M01: circdist_gross_sbbcert_20260820.md](original/M01-circdist_gross_sbbcert_20260820.md "artifacts/circdist_gross_sbbcert_20260820.md")
  - Coverage: Full bundled file; source lines 1–2910.
  - Relevant location(s): lines 246–251; #2.4(1),5(2),7(2); Referenced by research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md; Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.gross.mc-equiv.yaml
  - Source: `artifacts/circdist_gross_sbbcert_20260820.md`

- [M02: circdist_sbbcert_review_20260820.md](original/M02-circdist_sbbcert_review_20260820.md "research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–580.
  - Relevant location(s): §6，尤其 §2.4(1) 原句及 288 interleaved pairs; lines 378–394; #6; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.mc-equiv.yaml
  - Source: `research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md`

- [M03: CIRCDIST.gross.mc-equiv.yaml](original/M03-CIRCDIST.gross.mc-equiv.yaml "research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.mc-equiv.yaml")
  - Coverage: Full bundled file; source lines 1–40.
  - Relevant location(s): ; 
  - Source: `research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.mc-equiv.yaml`

- [M04: CIRCDIST.gross.mc-equiv.yaml](original/M04-CIRCDIST.gross.mc-equiv.yaml "research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.gross.mc-equiv.yaml")
  - Coverage: Full bundled file; source lines 1–54.
  - Relevant location(s): #events; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.mc-equiv.yaml
  - Source: `research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.gross.mc-equiv.yaml`

- [M05: agent-ace09be0f0bec8908.jsonl](original/M05-agent-ace09be0f0bec8908.jsonl.readable.md "claude-session-archive/agent-ace09be0f0bec8908.jsonl") · [event data](original/M05-agent-ace09be0f0bec8908.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 57–69, 217–229.
  - Relevant location(s): lines 63; lines 223
  - Source: `claude-session-archive/agent-ace09be0f0bec8908.jsonl`

- [M06: circdist_gross_g1_20260820.md](original/M06-circdist_gross_g1_20260820.md "artifacts/circdist_gross_g1_20260820.md")
  - Coverage: Full bundled file; source lines 1–2193.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_gross_g1_20260820.md`

- [M07: CIRCDIST_PROBLEMS.md](original/M07-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md; Referenced by research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M08: circdist_lift_d3gate_20260820.md](original/M08-circdist_lift_d3gate_20260820.md "artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_lift_d3gate_20260820.md`

- [M09: circdist_lift_nonint_proof_20260820.md](original/M09-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M10: circdist_lift_proofs_review_20260820.md](original/M10-circdist_lift_proofs_review_20260820.md "artifacts/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_lift_proofs_review_20260820.md`

- [M11: circdist_gross_toolfeas_20260820.md](original/M11-circdist_gross_toolfeas_20260820.md "artifacts/circdist_gross_toolfeas_20260820.md")
  - Coverage: Full bundled file; source lines 1–62.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_gross_toolfeas_20260820.md`

- [M12: circdist_gross_sbbcert_20260820.md](original/M12-circdist_gross_sbbcert_20260820.md "research-graph/circdist/artifacts/circdist_gross_sbbcert_20260820.md")
  - Coverage: Full bundled file; source lines 1–2910.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.gross.mc-equiv.yaml
  - Source: `research-graph/circdist/artifacts/circdist_gross_sbbcert_20260820.md`

- [M13: circdist_sbbcert_review_20260820.md](original/M13-circdist_sbbcert_review_20260820.md "artifacts/circdist_sbbcert_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–580.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.gross.mc-equiv.yaml
  - Source: `artifacts/circdist_sbbcert_review_20260820.md`
