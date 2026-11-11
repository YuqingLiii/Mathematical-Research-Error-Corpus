# Record 075 — Quantum k-sum with small alphabets

**Review status:** `interpretation_check_pending`.

Historical witness supports rather than refutes the actual quoted assertion. A different false universal orbit-count sentence in the same proposition is a candidate replacement, not silently the same error.

## Original statement and context

> The regularity property fails in both directions: there are $y\in D_0$ and position permutations $\pi$ admitting no valid value permutation

**Recorded location:** Full-manuscript Write event, 2026-07-17T20:31:31.554Z; proposition on transferring the element-distinctness mechanism.

**Context (annotation, not a source quotation):** The old witness gives examples in which centralizer regularity fails, but the recovered proposition already claims that it fails. The proposed witness therefore supports this sentence instead of refuting it.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The published ledger's claim/witness alignment is inconsistent and must be adjudicated before this row is released as a positive error.

### Argument or calculation

For q=3, sigma fixes0 and swaps1,2, so no centralizer permutation can send0 to1; the swap of y=(0,1) is not induced by the centralizer. For q=4 with sigma=(0 1)(2 3), swapping the unused cycle (2 3) fixes y=(0,0), so the inducing value permutation is not unique. Both are examples of the regularity failure expressly asserted by the quoted original; they are not defeaters of that assertion.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理直接采用非恒等置换一律非单轨道的概括；正文延续这个漏掉退化情形的全称声明。

- [2026-07-17T20:28:27.854Z — claude_visible_thinking](original/M01-KSUM-main-b5fea9c2.jsonl.readable.md) — source line 567; recorded role: generation.

## Original materials

- [M01: KSUM-main-b5fea9c2.jsonl](original/M01-KSUM-main-b5fea9c2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl") · [event data](original/M01-KSUM-main-b5fea9c2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 561–576, 1485–1497.
  - Relevant location(s): JSONL line 569 (exact full-manuscript Write containing the focal claim); 569; 569 (2026-07-17T20:31:31.554Z); 1491; lines 567; lines 569
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl`

- [M02: DATA6_ksum_ledger.md](original/M02-DATA6_ksum_ledger.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md`
