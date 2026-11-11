# 015 — The largest integer strictly less than x is ceil(x)-1, not ceil(x).

**Research problem:** P01 — Channel additivity violations

## Original statement

> Since \(D_i\le\Delta_{\rm flat}<HE\), equations (1.6) and (2.4) give
> 
> $$
> m_i<
> \frac{H\,127^2K^2}
> {126^2(K-H)S_i}.
> $$
> 
> The exact strict-integer ceilings are
> 
> $$
> \boxed{
> \begin{aligned}
> (m_i)=(&60996,48631,44023,40693,39789,38265,39011,\\
>        &38265,39789,40693,44023,48631,60996).
> \end{aligned}}
> \tag{2.6}
> $$

**Context:** For each row, the source derives the strict real bound m_i<x_i, where x_i=H*127^2*K^2/[126^2*(K-H)*S_i]. It then labels a vector of ceilings as exact strict-integer values.

**Original locator:** round-59-response.md, lines 222–239

## Why it is an error

The largest integer strictly less than x is ceil(x)-1, not ceil(x).

## Witness / evidence

For integer m, m<x is equivalent to m<=ceil(x)-1. If x=2 exactly, the maximum admissible integer is 1, not 2; if x=2.3, it is 2, not 3. Consequently the printed thirteen ceilings must each be reduced by one to be sharp strict-integer maxima. Their use as conservative, larger deletion budgets may still be safe; the error is the exactness claim.

## Scope

computation_false

## Classification

- III: 计算与代数错误. 将严格实数上界转成最大整数时差一：m<x 的精确最大整数是 ceil(x)-1；原十三个 ceiling 不是所称的精确最大值。

## Adjudication notes

The largest integer strictly less than x is ceil(x)-1, not ceil(x).

For integer m, m<x is equivalent to m<=ceil(x)-1. If x=2 exactly, the maximum admissible integer is 1, not 2; if x=2.3, it is 2, not 3. Consequently the printed thirteen ceilings must each be reduced by one to be sharp strict-integer maxima. Their use as conservative, larger deletion budgets may still be safe; the error is the exactness claim.

Scope: computation_false

严格小于 x 的最大整数是 ceil(x)-1，不是 ceil(x)。本轮确认一般取整规则和端点；未重新计算所有历史表格行。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-round-59-response.md](original/M01-round-59-response.md)
- [original/M02-concentrated_audit_4_rounds_59_81.md](original/M02-concentrated_audit_4_rounds_59_81.md)
- [original/M03-round58_response.md](original/M03-round58_response.md)
- [original/M04-round59_size3_reproducer.cpp](original/M04-round59_size3_reproducer.cpp)
- [original/M05-round59_size2_keycounts.cpp](original/M05-round59_size2_keycounts.cpp)
- [original/M06-round59_size2_merge_audit.cpp](original/M06-round59_size2_merge_audit.cpp)
- [original/M07-round59_verify_global.py](original/M07-round59_verify_global.py)
- [original/M08-round59_lowfiber_summary.csv](original/M08-round59_lowfiber_summary.csv)
- [original/M09-round59_size3_summary.csv](original/M09-round59_size3_summary.csv)
- [original/M10-round59_global_size2_summary.csv](original/M10-round59_global_size2_summary.csv)
- [original/M11-round59_global_size2_detail.txt](original/M11-round59_global_size2_detail.txt)
- [original/M12-round59_size2_checks.txt](original/M12-round59_size2_checks.txt)
- [original/M13-round59_stream_sha256.txt](original/M13-round59_stream_sha256.txt)
- [original/M14-round59_exact_inequality_checks.txt](original/M14-round59_exact_inequality_checks.txt)
- [original/M15-round59_digest.txt](original/M15-round59_digest.txt)

[Back to all 65 errors](../../README.md)
