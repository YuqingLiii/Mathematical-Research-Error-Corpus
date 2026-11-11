# Record 017 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> For output dimension `d`, define
> 
> `f_d(eps) = eps log_2(d-1) + h_2(eps)`.
> 
> Only sufficiently small `eps` is needed below. Audenaert's Theorem 1 gives
> 
> `|S(rho)-S(sigma)| <= f_d((1/2)||rho-sigma||_1)`
> 
> for `d`-dimensional states.

**Recorded location:** Proof-artifact creation event, 2026-08-30T02:02:11.343Z, JSONL line 4003

**Context (annotation, not a source quotation):** The surrounding claim covers arbitrary finite output dimensions. This original write lacks the later separate treatment of one-dimensional outputs.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The written continuity modulus is undefined at output dimension d=1.

### Argument or calculation

Substituting d=1 produces log2(d-1)=log2(0), not a finite real number. A one-dimensional output state is uniquely [1] and its entropy is exactly zero, so that case must be handled separately with zero entropy variation; it is not covered by the displayed formula. This invalidates the stated all-dimensions argument, not its repaired conclusion.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 连续性推导的摘要是短标题，没有 d=1 边界分析。

- [2026-08-30T02:00:32.436Z — codex_reasoning_summary](original/M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.readable.md) — source line 3990; recorded role: generation.

## Original materials

- [M01: rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl](original/M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.readable.md "local-session-archive/2026/08/26/rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl") · [event data](original/M01-rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 3979–4012, 7353–7366, 22840–22853.
  - Relevant location(s): Proof-artifact creation event, 2026-08-30T02:02:11.343Z, JSONL line 4003; lines 3990
  - Source: `local-session-archive/2026/08/26/rollout-2026-08-26T20-38-22-<session-id-redacted>.jsonl`

- [M02: FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md](original/M02-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md "research-graph/holevo-counterexample-prevalence/reviews/FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md")
  - Coverage: Full bundled file; source lines 1–284.
  - Relevant location(s): HCP-FS-IR-02
  - Source: `research-graph/holevo-counterexample-prevalence/reviews/FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md`

- [M03: FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md](original/M03-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md "research-graph/holevo-counterexample-prevalence/artifacts/FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md")
  - Coverage: Full bundled file; source lines 1–112.
  - Relevant location(s): Referenced by research-graph/holevo-counterexample-prevalence/reviews/FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-counterexample-prevalence/artifacts/FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md`

- [M04: STABILITY_AND_MEASURE_PROOF_20260829.md](original/M04-STABILITY_AND_MEASURE_PROOF_20260829.md "research-graph/holevo-counterexample-prevalence/artifacts/STABILITY_AND_MEASURE_PROOF_20260829.md")
  - Coverage: Full bundled file; source lines 1–134.
  - Relevant location(s): Referenced by research-graph/holevo-counterexample-prevalence/reviews/FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-counterexample-prevalence/artifacts/STABILITY_AND_MEASURE_PROOF_20260829.md`

- [M05: ADDITIVE_OPEN_REGION_PROOF_20260829.md](original/M05-ADDITIVE_OPEN_REGION_PROOF_20260829.md "research-graph/holevo-counterexample-prevalence/artifacts/ADDITIVE_OPEN_REGION_PROOF_20260829.md")
  - Coverage: Full bundled file; source lines 1–53.
  - Relevant location(s): Referenced by research-graph/holevo-counterexample-prevalence/reviews/FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md
  - Source: `research-graph/holevo-counterexample-prevalence/artifacts/ADDITIVE_OPEN_REGION_PROOF_20260829.md`
