# 045 — The range imported from the two-list donor must use the active half-length floor(N/2), not N/2 for odd N.

**Research problem:** P09 — Quantum k-sum with small alphabets

## Original statement

> **定理 A**(奇 q≥5,任意 t,任意 N):Q(2-Sum) = Ω(√N·q^{1/6}),范围到 q ≤ 2N−1;

**Context:** The construction uses two equally sized lists. Odd total N is handled by reserving one unused coordinate.

**Original locator:** Assistant final-report summary, July17; main-session JSONL lines447–468.

## Why it is an error

The range imported from the two-list donor must use the active half-length floor(N/2), not N/2 for odd N.

## Witness / evidence

Writing n=floor(N/2) and K=(q-1)/2, the invoked donor permits K<=2n-1. This yields q<=4floor(N/2)-1. For even N this equals2N-1; for odd N it equals2N-3. At N=5,q=9, the stated2N-1 condition passes, but K=4 exceeds2n-1=3. The recorded reduction does not cover that endpoint; this is not a proof that the asymptotic bound itself is false.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 调用 donor 下界时未保留 K<=2 floor(N/2)-1；奇 N 时推导只覆盖 q<=2N-3，不能支持所报端点。

## Adjudication notes

The range imported from the two-list donor must use the active half-length floor(N/2), not N/2 for odd N.

Writing n=floor(N/2) and K=(q-1)/2, the invoked donor permits K<=2n-1. This yields q<=4floor(N/2)-1. For even N this equals2N-1; for odd N it equals2N-3. At N=5,q=9, the stated2N-1 condition passes, but K=4 exceeds2n-1=3. The recorded reduction does not cover that endpoint; this is not a proof that the asymptotic bound itself is false.

Scope: argument_invalid

保留偶数 N 推导的端点直接沿用到冻结一个坐标的奇数 N 的范围缺口。错误是这套 reduction 的覆盖范围，不能夸成最终渐近下界被证伪。

KSUM-009 的同提交两份工件和后来修复已经恢复；继续沿用，未重跑不是缺资料。

## Original materials

- [original/M03-8e0f1063-KSUM_FINAL_REPORT.md](original/M03-8e0f1063-KSUM_FINAL_REPORT.md)
- [original/M04-DATA6_ksum_ledger.md](original/M04-DATA6_ksum_ledger.md)
- [original/context/R01-8e0f1063-KSUM_FINAL_REPORT.md.context.md](original/context/R01-8e0f1063-KSUM_FINAL_REPORT.md.context.md)

[Back to all 65 errors](../../README.md)
