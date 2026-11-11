# Record 026 — Quantum-capacity superactivation

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> 任何证明都不能只靠 Λ_ZW 的 cALN 性;幺正性(无旗性)是被逼出来的必要假设

**Recorded location:** Assistant message, 2026-07-29T22:52:39.324Z, JSONL line 1540

**Context (annotation, not a source quotation):** Translation: “No proof can rely only on Lambda_ZW being cALN; unitality (flaglessness) is a forced necessary hypothesis.” The source proposes unitality as the separator between its target and an erasure-channel counterexample. Here cALN refers to a receiver-versus-environment information-order property.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Excluding a counterexample forces some additional separating property, not specifically unitality or absence of a flag.

### Argument or calculation

The known activating pair shows only that the information-order assumption alone is insufficient. Formally, from a counterexample C satisfying A but not the desired conclusion, a successful strengthened theorem must restrict A enough to exclude C. It does not follow that every successful restriction equals the particular proposed predicate “unital.” No theorem in the argument makes unitality a necessary property of all zero-capacity pairs. The valid conclusion is that it is one candidate separator.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理认为 unitality/flaglessness 差异值得利用，不等于证明其为所有可能证明的必要条件；尚不能定位这一全称必要性何时形成。

- [2026-07-29T22:46:00.775Z — claude_visible_thinking](original/M01-<session-id-redacted>.jsonl.readable.md) — source line 1499; recorded role: generation.

## Original materials

- [M01: <session-id-redacted>.jsonl](original/M01-<session-id-redacted>.jsonl.readable.md "tracking/claude-proof-records/source-cache/macstudio-recovery/C--Users-wtaph-Documents-discovery-new-algorithms/<session-id-redacted>.jsonl") · [event data](original/M01-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1493–1505, 1534–1546, 1644–1656, 1662–1685.
  - Relevant location(s): Assistant message, 2026-07-29T22:52:39.324Z, JSONL line 1540; JSONL lines 1650,1668,1679; lines 1499
  - Source: `tracking/claude-proof-records/source-cache/macstudio-recovery/C--Users-wtaph-Documents-discovery-new-algorithms/<session-id-redacted>.jsonl`

- [M02: CLAUDE_CAMPAIGNS_20260821.json](original/M02-CLAUDE_CAMPAIGNS_20260821.json "tracking/ai-proof-records-20260912/recovered-marathon-20260821/CLAUDE_CAMPAIGNS_20260821.json")
  - Coverage: Full bundled file; source lines 1–465.
  - Relevant location(s): #campaigns/SUPERACT_AXC_DEDUPED/error_corrections/5
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/CLAUDE_CAMPAIGNS_20260821.json`
