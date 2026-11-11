# Record 024 — Quantum-capacity superactivation

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> 任何 Q=0 证明必须全局控制熵和,不能逐因子分解

**Recorded location:** Assistant message, 2026-07-29T22:52:39.324Z, JSONL line 1540

**Context (annotation, not a source quotation):** Translation: “Any Q=0 proof must control the entropy sum globally and cannot decompose factor by factor.” Failure of a bracketwise proof for the selected channel pair was generalized into a universal prohibition.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

A self-complementary channel gives a counterexample to the universal bracketwise no-go.

### Argument or calculation

For the 50% erasure channel A_(1/2), receiver and environment channels are unitarily equivalent. For A_(1/2) tensor A_(1/2), the corresponding receiver/environment conditional-entropy brackets match individually and each difference is zero. Their sum therefore proves coherent information zero by a legitimate per-bracket argument. Failure of a bracket bound for the originally selected pair cannot rule out this case.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 相关推理讨论当前冻结路线，错误输出扩大为任何 Q=0 证明；未找到推理中明确对所有可能证明量化的句子。

- [2026-07-29T22:44:26.624Z — claude_visible_thinking](original/M01-<session-id-redacted>.jsonl.readable.md) — source line 1481; recorded role: generation.

## Original materials

- [M01: <session-id-redacted>.jsonl](original/M01-<session-id-redacted>.jsonl.readable.md "tracking/claude-proof-records/source-cache/macstudio-recovery/C--Users-wtaph-Documents-discovery-new-algorithms/<session-id-redacted>.jsonl") · [event data](original/M01-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1475–1487, 1534–1546, 1644–1656, 1662–1674.
  - Relevant location(s): Assistant message, 2026-07-29T22:52:39.324Z, JSONL line 1540; JSONL lines 1481,1650,1668; lines 1481
  - Source: `tracking/claude-proof-records/source-cache/macstudio-recovery/C--Users-wtaph-Documents-discovery-new-algorithms/<session-id-redacted>.jsonl`

- [M02: CLAUDE_CAMPAIGNS_20260821.json](original/M02-CLAUDE_CAMPAIGNS_20260821.json "tracking/ai-proof-records-20260912/recovered-marathon-20260821/CLAUDE_CAMPAIGNS_20260821.json")
  - Coverage: Full bundled file; source lines 1–465.
  - Relevant location(s): #campaigns/SUPERACT_AXC_DEDUPED/error_corrections/6
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/CLAUDE_CAMPAIGNS_20260821.json`
