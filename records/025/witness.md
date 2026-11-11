# 025 — Positive two-way-assisted capacity does not exclude antidegradability.

**Research problem:** P03 — Quantum-capacity superactivation

## Original statement

> The two-way capacity K6 shows Q^↔(Λ_ZW) ≥ 0.0409, which proves Λ_ZW itself is not antidegradable. Since two-way capacity of a tensor product is at least the two-way capacity of either factor, this means Q^↔(T) ≥ 0.0409 as well, so T cannot be antidegradable either.

**Context:** The agent tries to reject antidegradability of a candidate product channel T using a positive two-way-assisted quantum capacity. The superscript double arrow denotes assistance by two-way classical communication.

**Original locator:** Visible reasoning block, 2026-07-30T05:38:38.545Z, JSONL line 1813

## Why it is an error

Positive two-way-assisted capacity does not exclude antidegradability.

## Witness / evidence

The d-dimensional 50% erasure channel is self-complementary and hence antidegradable. Send halves of maximally entangled pairs through it. The receiver identifies non-erased uses and communicates their positions back; half the uses retain maximally entangled pairs, giving a two-way-assisted rate at least (1/2) log2 d>0. Thus antidegradable does not imply Q_two_way=0, and the displayed inference is invalid.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 由正双向辅助容量推出非反可降解的蕴含不成立。50% 擦除信道同时反可降解且有正双向辅助容量。

II/IV 边界：容量概念有关，但原文明确可见的是由正容量推出非反可降解的错误蕴含，故只计 IV。

## Adjudication notes

Positive two-way-assisted capacity does not exclude antidegradability.

The d-dimensional 50% erasure channel is self-complementary and hence antidegradable. Send halves of maximally entangled pairs through it. The receiver identifies non-erased uses and communicates their positions back; half the uses retain maximally entangled pairs, giving a two-way-assisted rate at least (1/2) log2 d>0. Thus antidegradable does not imply Q_two_way=0, and the displayed inference is invalid.

Scope: argument_invalid

反可降解的 50% 擦除信道仍有正的双向辅助容量；有效的 Q↔>0 证据不能支持“不是反可降解”的结论。这里只判容量/辅助模型之间的错误桥接。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M02-CLAUDE_CAMPAIGNS_20260821.json](original/M02-CLAUDE_CAMPAIGNS_20260821.json)

[Back to all 65 errors](../../README.md)
