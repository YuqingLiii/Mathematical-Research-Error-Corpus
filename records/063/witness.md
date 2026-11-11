# 063 — A stale support vector is used in the exploratory weighted calculation.

**Research problem:** P01 — Channel additivity violations

## Original statement

>     constexpr std::array<std::uint64_t, N> SUPPORT = {
>         53624480, 67257904, 74298900, 80378416, 82204926, 85479258, 83844372,
>         85479258, 82204926, 80378416, 74298900, 67257904, 53624480,
>     };
> 
> [...]
> 
>         weighted_surviving += static_cast<u128>(SUPPORT[deleted]) *
>                               static_cast<u128>(
>                                   matched > BUDGET[deleted] ? matched - BUDGET[deleted] : 0
>                               );

**Context:** The exploratory program computes weighted_surviving using the active SUPPORT array for a later finite-slope instance whose exact support total is K=970337664. The selected constants come from a prior instance.

**Original locator:** explore_round82_global.cpp, lines 340–343, 458–461

## Why it is an error

A stale support vector is used in the exploratory weighted calculation.

## Witness / evidence

The thirteen printed SUPPORT entries sum to 970332140. The independently enumerated target vector reported in the round-82 thirteen-row census is (53624480,67257904,74299396,80379126,82205586,85479878,83844924,85479878,82205586,80379126,74299396,67257904,53624480), whose sum is 970337664. The difference is 5524. Because weighted_surviving multiplies each row by SUPPORT[deleted], these are not interchangeable constants. The archived final proof did not depend on this exploratory diagnostic. The original thirteen-row execution log is now bundled in reconciliation_sources. This release recomputes its sum and compares the active constants with those recorded rows; it does not claim a new full determinant enumeration.

## Scope

computation_false

## Classification

- V: 其他错误. 后续实例程序仍载入上一实例的 SUPPORT 数据，实际数组与对应归档计数不一致。此处按数据更新/转录失配处理，不假定正确运算过程本身失败。

研究场景适配：V 包括程序材料的数据更新失配，不等于原论文较窄的最终答案抄写子类；不据此推断生成者的数学推理正确。

其他类别用于程序材料的数据更新失配

## Adjudication notes

A stale support vector is used in the exploratory weighted calculation.

The thirteen printed SUPPORT entries sum to 970332140. The independently enumerated target vector reported in the round-82 thirteen-row census is (53624480,67257904,74299396,80379126,82205586,85479878,83844924,85479878,82205586,80379126,74299396,67257904,53624480), whose sum is 970337664. The difference is 5524. Because weighted_surviving multiplies each row by SUPPORT[deleted], these are not interchangeable constants. The archived final proof did not depend on this exploratory diagnostic. The original thirteen-row execution log is now bundled in reconciliation_sources. This release recomputes its sum and compares the active constants with those recorded rows; it does not claim a new full determinant enumeration.

Scope: computation_false

恢复数值错误确认：原执行日志逐行给出的实际 support 与活跃 C++ 常量不同，合计相差5524；旧程序中常量确用于 weighted_surviving。它不影响已分开验证的最终证书。

打包脚本因“本轮未重跑determinant census”自动降级了已有确认。这是打包回归，不是缺失错误证据。现补入原执行日志，不冒称重新运行整个枚举。

## Original materials

- [original/M01-explore_round82_global.cpp](original/M01-explore_round82_global.cpp)
- [original/M02-round-82-response.md](original/M02-round-82-response.md)
- [original/M03-concentrated_audit_5_rounds_82_105.md](original/M03-concentrated_audit_5_rounds_82_105.md)
- [original/M04-round-104-prompt.md](original/M04-round-104-prompt.md)
- [original/context/A01-round82-exploratory-global.log](original/context/A01-round82-exploratory-global.log)
- [original/context/A02-round-82-local-audit.md](original/context/A02-round-82-local-audit.md)
- [original/context/R01-M01-explore_round82_global.cpp.context.md](original/context/R01-M01-explore_round82_global.cpp.context.md)
- [original/context/R02-round82-exploratory-global.log.context.md](original/context/R02-round82-exploratory-global.log.context.md)

[Back to all 65 errors](../../README.md)
