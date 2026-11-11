# Record 025 — Quantum-capacity superactivation

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> The two-way capacity K6 shows Q^↔(Λ_ZW) ≥ 0.0409, which proves Λ_ZW itself is not antidegradable. Since two-way capacity of a tensor product is at least the two-way capacity of either factor, this means Q^↔(T) ≥ 0.0409 as well, so T cannot be antidegradable either.

**Recorded location:** Visible reasoning block, 2026-07-30T05:38:38.545Z, JSONL line 1813

**Context (annotation, not a source quotation):** The agent tries to reject antidegradability of a candidate product channel T using a positive two-way-assisted quantum capacity. The superscript double arrow denotes assistance by two-way classical communication.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Positive two-way-assisted capacity does not exclude antidegradability.

### Argument or calculation

The d-dimensional 50% erasure channel is self-complementary and hence antidegradable. Send halves of maximally entangled pairs through it. The receiver identifies non-erased uses and communicates their positions back; half the uses retain maximally entangled pairs, giving a two-way-assisted rate at least (1/2) log2 d>0. Thus antidegradable does not imply Q_two_way=0, and the displayed inference is invalid.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** Q↔ 正容量推出非 antidegradable 的错误蕴含直接出现在推理块中。这里原始错误声明本身就在推理里；未找到另一个独立输出节点，不能声称形成了完整双端配对。

- [2026-07-30T05:38:38.545Z — claude_visible_thinking](original/M01-<session-id-redacted>.jsonl.readable.md) — source line 1813; recorded role: original_claim_in_reasoning.

## Original materials

- [M01: <session-id-redacted>.jsonl](original/M01-<session-id-redacted>.jsonl.readable.md "tracking/claude-proof-records/source-cache/macstudio-recovery/C--Users-wtaph-Documents-discovery-new-algorithms/<session-id-redacted>.jsonl") · [event data](original/M01-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1807–1819.
  - Relevant location(s): Visible reasoning block, 2026-07-30T05:38:38.545Z, JSONL line 1813; JSONL lines 1813,1924; lines 1813
  - Source: `tracking/claude-proof-records/source-cache/macstudio-recovery/C--Users-wtaph-Documents-discovery-new-algorithms/<session-id-redacted>.jsonl`

- [M02: CLAUDE_CAMPAIGNS_20260821.json](original/M02-CLAUDE_CAMPAIGNS_20260821.json "tracking/ai-proof-records-20260912/recovered-marathon-20260821/CLAUDE_CAMPAIGNS_20260821.json")
  - Coverage: Full bundled file; source lines 1–465.
  - Relevant location(s): #campaigns/SUPERACT_AXC_DEDUPED/error_corrections/7/part-a
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/CLAUDE_CAMPAIGNS_20260821.json`
