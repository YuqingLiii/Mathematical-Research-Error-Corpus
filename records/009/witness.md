# 009 — The displayed polynomial has been evaluated incorrectly.

**Research problem:** P01 — Channel additivity violations

## Original statement

> At \(|T|=777716\), this is the first undecided finite determinant/kernel system. The dictionary has at most
> 
> $$
> r_1^2+r_1+1
> =
> 970353651
> $$
> 
> columns, but the coefficient vector has the special nonlinear form (8.2). Merely proving \(G_T\) singular would be necessary, not sufficient: its kernel must contain a vector with that exact conjugate-quadratic structure.

**Context:** The displayed dictionary-count expression uses r1=777716. This is a local arithmetic display, not the main theorem’s proof.

**Original locator:** round-28-response.md, lines 725–733

## Why it is an error

The displayed polynomial has been evaluated incorrectly.

## Witness / evidence

Exact integer arithmetic gives 777716^2+777716+1=604842954373, whereas 970353651=31151*31150+1. The printed number belongs to a different expression.

## Scope

computation_false

## Classification

- III: 计算与代数错误. 给定 r1=777716，显示的 r1^2+r1+1 应为 604842954373，而非打印值。未见同一次正确结果被抄坏的必要证据，不擅自标成 V。

## Adjudication notes

The displayed polynomial has been evaluated incorrectly.

Exact integer arithmetic gives 777716^2+777716+1=604842954373, whereas 970353651=31151*31150+1. The printed number belongs to a different expression.

Scope: computation_false

777716²+777716+1=604842954373，与原文求值不符；这是局部精确算术错误。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-round-28-response.md](original/M01-round-28-response.md)
- [original/M02-concentrated_audit_2_rounds_24_42.md](original/M02-concentrated_audit_2_rounds_24_42.md)
- [original/M03-MASTER_AUDIT_PROTOCOL.md](original/M03-MASTER_AUDIT_PROTOCOL.md)
- [original/M04-round-23-local-audit.md](original/M04-round-23-local-audit.md)

[Back to all 65 errors](../../README.md)
