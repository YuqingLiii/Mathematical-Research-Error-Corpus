# Record 016 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> A Holevo pair gap g for finite-dimensional channels N and M can, after balancing their one-shot
>   Holevo quantities within one bit by a bounded classical side channel and taking T = N' direct-sum
>   M', be converted into chi(T tensor T) - 2 chi(T) at least g - log_2(9/4), with only constant
>   additive qubit overhead.

**Recorded location:** Proof-node creation event, 2026-08-30T01:21:04.780Z, JSONL line 3188

**Context (annotation, not a source quotation):** The proposed conversion balances the one-shot Holevo information of two channels by adding a classical side channel of size K, then forms a direct sum. The node was marked CONJECTURED; this record concerns the overly strong dimension-overhead clause, not a falsely certified final theorem.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The balancing side channel need not have constant dimension or constant additive qubit cost.

### Argument or calculation

If the Holevo quantities differ by Delta, balancing them within one bit requires |log2 K-Delta|<1, so log2 K>Delta-1. Taking channels with Holevo quantities log2 d and 0 makes the required overhead grow as log2 d. The final direct sum itself adds at most one qubit, but that does not erase the preceding balancing cost. The equal-Holevo special case avoids this cost.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** pair-to-self 的摘要只是主题标题，没有目标维数成本的推导。

- [2026-08-29T19:36:42.386Z — codex_reasoning_summary](original/M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.readable.md) — source line 2532; recorded role: generation.

## Original materials

- [M01: rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl](original/M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.readable.md "local-session-archive/2026/08/26/rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl") · [event data](original/M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 2523–2538, 3182–3197, 4018–4031, 5174–5187, 7186–7199, 22594–22607, 23096–23109.
  - Relevant location(s): Proof-node creation event, 2026-08-30T01:21:04.780Z, JSONL line 3188; lines 2532
  - Source: `local-session-archive/2026/08/26/rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl`

- [M02: ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md](original/M02-ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md "research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md")
  - Coverage: Full bundled file; source lines 1–327.
  - Relevant location(s): Finding AU-IR-05（claim hash sha256:ab44daaa…）；DAG HEXT.pair-to-self event general-overhead-claim-repaired; 189-229
  - Source: `research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md`

- [M03: PAIR_TO_SELF_REDUCTION_2026-08-29.md](original/M03-PAIR_TO_SELF_REDUCTION_2026-08-29.md "research-graph/holevo-extensive-violation/artifacts/PAIR_TO_SELF_REDUCTION_2026-08-29.md")
  - Coverage: Full bundled file; source lines 1–182.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-extensive-violation/artifacts/PAIR_TO_SELF_REDUCTION_2026-08-29.md`

- [M04: HEXT.finite-dimensional-unbounded-gap.yaml](original/M04-HEXT.finite-dimensional-unbounded-gap.yaml "research-graph/holevo-extensive-violation/proof-dag/nodes/HEXT.finite-dimensional-unbounded-gap.yaml")
  - Coverage: Full bundled file; source lines 1–131.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-extensive-violation/proof-dag/nodes/HEXT.finite-dimensional-unbounded-gap.yaml`

- [M05: HEXT.moe-to-holevo-transfer.yaml](original/M05-HEXT.moe-to-holevo-transfer.yaml "research-graph/holevo-extensive-violation/proof-dag/nodes/HEXT.moe-to-holevo-transfer.yaml")
  - Coverage: Full bundled file; source lines 1–80.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-extensive-violation/proof-dag/nodes/HEXT.moe-to-holevo-transfer.yaml`

- [M06: HEXT.pair-to-self.yaml](original/M06-HEXT.pair-to-self.yaml "research-graph/holevo-extensive-violation/proof-dag/nodes/HEXT.pair-to-self.yaml")
  - Coverage: Full bundled file; source lines 1–52.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-extensive-violation/proof-dag/nodes/HEXT.pair-to-self.yaml`

- [M07: HEXT.goal.yaml](original/M07-HEXT.goal.yaml "research-graph/holevo-extensive-violation/proof-dag/nodes/HEXT.goal.yaml")
  - Coverage: Full bundled file; source lines 1–667.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-extensive-violation/proof-dag/nodes/HEXT.goal.yaml`

- [M08: FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md](original/M08-FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md "research-graph/holevo-extensive-violation/artifacts/FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md")
  - Coverage: Full bundled file; source lines 1–343.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-extensive-violation/artifacts/FINITE_DIMENSIONAL_UNBOUNDED_GAP_PROOF_20260829.md`

- [M09: MOE_TO_HOLEVO_TRANSFER_PROOF_20260829.md](original/M09-MOE_TO_HOLEVO_TRANSFER_PROOF_20260829.md "research-graph/holevo-extensive-violation/artifacts/MOE_TO_HOLEVO_TRANSFER_PROOF_20260829.md")
  - Coverage: Full bundled file; source lines 1–52.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-extensive-violation/artifacts/MOE_TO_HOLEVO_TRANSFER_PROOF_20260829.md`

- [M10: proof_dag_check.py](original/M10-proof_dag_check.py "tools/proof_dag_check.py")
  - Coverage: Full bundled file; source lines 1–930.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `tools/proof_dag_check.py`

- [M11: check_holevo_three_question_scope.py](original/M11-check_holevo_three_question_scope.py "research-graph/tools/check_holevo_three_question_scope.py")
  - Coverage: Full bundled file; source lines 1–120.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/tools/check_holevo_three_question_scope.py`

- [M12: evidence_closure_check.py](original/M12-evidence_closure_check.py "research-graph/tools/evidence_closure_check.py")
  - Coverage: Full bundled file; source lines 1–75.
  - Relevant location(s): Referenced by research-graph/holevo-extensive-violation/reviews/ABSOLUTE_UNBOUNDED_CHAIN_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/tools/evidence_closure_check.py`
