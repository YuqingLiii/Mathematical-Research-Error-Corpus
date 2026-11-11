# Record 045 — Quantum k-sum with small alphabets

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> **定理 A**(奇 q≥5,任意 t,任意 N):Q(2-Sum) = Ω(√N·q^{1/6}),范围到 q ≤ 2N−1;

Context: The construction uses two equally sized lists. Odd total N is handled by reserving one unused coordinate.

Locator: Assistant final-report summary, July17; main-session JSONL lines447–468.

## 2. Witness / adjudication

The range imported from the two-list donor must use the active half-length floor(N/2), not N/2 for odd N.

Writing n=floor(N/2) and K=(q-1)/2, the invoked donor permits K<=2n-1. This yields q<=4floor(N/2)-1. For even N this equals2N-1; for odd N it equals2N-3. At N=5,q=9, the stated2N-1 condition passes, but K=4 exceeds2n-1=3. The recorded reduction does not cover that endpoint; this is not a proof that the asymptotic bound itself is false.

Scope: argument_invalid

保留偶数 N 推导的端点直接沿用到冻结一个坐标的奇数 N 的范围缺口。错误是这套 reduction 的覆盖范围，不能夸成最终渐近下界被证伪。

KSUM-009 的同提交两份工件和后来修复已经恢复；继续沿用，未重跑不是缺资料。

## 3. Evidence and verification

冻结版本原文与 donor 代入式逐项对读，精确整数代数。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-<session-id-redacted>.jsonl.readable.md](original/M01-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M01-<session-id-redacted>.jsonl.visible.json](original/M01-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M02-949240a-ksum_small_alphabet.tex](original/M02-949240a-ksum_small_alphabet.tex) — inherited_sanitized_source
- [M03-8e0f1063-KSUM_FINAL_REPORT.md](original/M03-8e0f1063-KSUM_FINAL_REPORT.md) — inherited_sanitized_source
- [M04-DATA6_ksum_ledger.md](original/M04-DATA6_ksum_ledger.md) — inherited_sanitized_source
- [R01-8e0f1063-KSUM_FINAL_REPORT.md.context.md](reconciliation_sources/R01-8e0f1063-KSUM_FINAL_REPORT.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
