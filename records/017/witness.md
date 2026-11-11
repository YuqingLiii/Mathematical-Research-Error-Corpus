# 017 — The written continuity modulus is undefined at output dimension d=1.

**Research problem:** P01 — Channel additivity violations

## Original statement

> For output dimension `d`, define
> 
> `f_d(eps) = eps log_2(d-1) + h_2(eps)`.
> 
> Only sufficiently small `eps` is needed below. Audenaert's Theorem 1 gives
> 
> `|S(rho)-S(sigma)| <= f_d((1/2)||rho-sigma||_1)`
> 
> for `d`-dimensional states.

**Context:** The surrounding claim covers arbitrary finite output dimensions. This original write lacks the later separate treatment of one-dimensional outputs.

**Original locator:** Proof-artifact creation event, 2026-08-30T02:02:11.343Z, JSONL line 4003

## Why it is an error

The written continuity modulus is undefined at output dimension d=1.

## Witness / evidence

Substituting d=1 produces log2(d-1)=log2(0), not a finite real number. A one-dimensional output state is uniquely [1] and its entropy is exactly zero, so that case must be handled separately with zero entropy variation; it is not covered by the displayed formula. This invalidates the stated all-dimensions argument, not its repaired conclusion.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 把含 log2(d-1) 的定理公式应用到任意有限输出维数，却未单列 d=1；这是适用域问题，不是对数函数的数值算错。

## Adjudication notes

The written continuity modulus is undefined at output dimension d=1.

Substituting d=1 produces log2(d-1)=log2(0), not a finite real number. A one-dimensional output state is uniquely [1] and its entropy is exactly zero, so that case must be handled separately with zero entropy variation; it is not covered by the displayed formula. This invalidates the stated all-dimensions argument, not its repaired conclusion.

Scope: argument_invalid

d=1 时 log2(d-1) 无定义，原通用连续性公式需要单独处理平凡输出维度。仅判此边界公式。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M02-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md](original/M02-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_INDEPENDENT_REVIEW_20260830.md)
- [original/M03-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md](original/M03-FULL_SUPPORT_FIXED_DIMENSION_PROBABILITY_DICHOTOMY_20260830.md)
- [original/M04-STABILITY_AND_MEASURE_PROOF_20260829.md](original/M04-STABILITY_AND_MEASURE_PROOF_20260829.md)
- [original/M05-ADDITIVE_OPEN_REGION_PROOF_20260829.md](original/M05-ADDITIVE_OPEN_REGION_PROOF_20260829.md)

[Back to all 65 errors](../../README.md)
