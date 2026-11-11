# Record 045 — Quantum k-sum with small alphabets

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> **定理 A**(奇 q≥5,任意 t,任意 N):Q(2-Sum) = Ω(√N·q^{1/6}),范围到 q ≤ 2N−1;

**Recorded location:** Assistant final-report summary, July17; main-session JSONL lines447–468.

**Context (annotation, not a source quotation):** The construction uses two equally sized lists. Odd total N is handled by reserving one unused coordinate.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The range imported from the two-list donor must use the active half-length floor(N/2), not N/2 for odd N.

### Argument or calculation

Writing n=floor(N/2) and K=(q-1)/2, the invoked donor permits K<=2n-1. This yields q<=4floor(N/2)-1. For even N this equals2N-1; for odd N it equals2N-3. At N=5,q=9, the stated2N-1 condition passes, but K=4 exceeds2n-1=3. The recorded reduction does not cover that endpoint; this is not a proof that the asymptotic bound itself is false.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理分开考虑偶数 N 和需检查的奇数 padding；尚未定位到同一生成块明确写出 forall N 的错误上端点。也不足以证明最终只是漏抄奇偶限制。

- [2026-07-17T03:42:57.561Z — claude_visible_thinking](original/M01-<session-id-redacted>.jsonl.readable.md) — source line 421; recorded role: generation.
- [2026-07-17T04:05:23.800Z — claude_visible_thinking](original/M01-<session-id-redacted>.jsonl.readable.md) — source line 446; recorded role: generation.

## Original materials

- [M01: <session-id-redacted>.jsonl](original/M01-<session-id-redacted>.jsonl.readable.md "tracking/ai-proof-records-20260912/reasoning-summary-sources/claude/<session-id-redacted>.jsonl") · [event data](original/M01-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 15–27, 415–433, 440–463.
  - Relevant location(s): JSONL lines 421–427（偶数 N 推导）、447–468（扩展与最终报告）、596（纠正）；git 8e0f1063 KSUM_FINAL_REPORT.md line 21；git 949240a paper/ksum_small_alphabet.tex; JSONL lines 421–427（偶数 N 推导）、447–468（扩展与最终报告）、596（纠正）；git 8e0f1063 KSUM_FINAL_REPORT.md line 21；git 949240a ; lines 421; lines 446
  - Source: `tracking/ai-proof-records-20260912/reasoning-summary-sources/claude/<session-id-redacted>.jsonl`

- [M02: 949240a-ksum_small_alphabet.tex](original/M02-949240a-ksum_small_alphabet.tex "paper/evidence_to_overclaim_iclr2027/release_work/recovered_artifacts/949240a-ksum_small_alphabet.tex")
  - Coverage: Full bundled file; source lines 1–316.
  - Source: `paper/evidence_to_overclaim_iclr2027/release_work/recovered_artifacts/949240a-ksum_small_alphabet.tex`

- [M03: 8e0f1063-KSUM_FINAL_REPORT.md](original/M03-8e0f1063-KSUM_FINAL_REPORT.md "paper/evidence_to_overclaim_iclr2027/release_work/recovered_artifacts/8e0f1063-KSUM_FINAL_REPORT.md")
  - Coverage: Full bundled file; source lines 1–73.
  - Source: `paper/evidence_to_overclaim_iclr2027/release_work/recovered_artifacts/8e0f1063-KSUM_FINAL_REPORT.md`

- [M04: DATA6_ksum_ledger.md](original/M04-DATA6_ksum_ledger.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md`
