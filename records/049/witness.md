# 049 — The displayed integer product is incorrect.

**Research problem:** P11 — Finite-dimensional Grothendieck bounds

## Original statement

> \binom{600}{2}\,598=107281800

**Context:** The proof note counts index choices with an unordered pair of two distinct vertices and a third distinct vertex.

**Original locator:** Triangle/hypermetric no-go note, lines114–123.

## Why it is an error

The displayed integer product is incorrect.

## Witness / evidence

binom(600,2)=600*599/2=179700; multiplying by598 gives107460600, not107281800. The discrepancy is178800. This is a local arithmetic/count-reporting error; it does not by itself invalidate the checker loops or the associated nonnegativity result.

## Scope

computation_false

## Classification

- III: 计算与代数错误. 明确整数乘法显示错误：binom(600,2)*598=107460600。该局部算式不否定整个非负性检验。

## Adjudication notes

The displayed integer product is incorrect.

binom(600,2)=600*599/2=179700; multiplying by598 gives107460600, not107281800. The discrepancy is178800. This is a local arithmetic/count-reporting error; it does not by itself invalidate the checker loops or the associated nonnegativity result.

Scope: computation_false

binom(600,2)·598=107460600，与报告值相差 178800。错误不自动污染遍历循环或非负性定理。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-d4-triangle-hypermetric-no-go-20260830.md](original/M01-d4-triangle-hypermetric-no-go-20260830.md)
- [original/M02-GROTHD4.cut.triangle-no-go.yaml](original/M02-GROTHD4.cut.triangle-no-go.yaml)
- [original/M04-h4_triangle_hypermetric_no_go_checker.py](original/M04-h4_triangle_hypermetric_no_go_checker.py)

[Back to all 65 errors](../../README.md)
