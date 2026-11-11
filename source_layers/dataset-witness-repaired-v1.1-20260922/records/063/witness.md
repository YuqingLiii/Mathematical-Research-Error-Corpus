# Record 063 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> constexpr std::array<std::uint64_t, N> SUPPORT = {
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

Context: The exploratory program computes weighted_surviving using the active SUPPORT array for a later finite-slope instance whose exact support total is K=970337664. The selected constants come from a prior instance.

Locator: explore_round82_global.cpp, lines 340–343, 458–461

## 2. Witness / adjudication

A stale support vector is used in the exploratory weighted calculation.

The thirteen printed SUPPORT entries sum to 970332140. The independently enumerated target vector reported in the round-82 thirteen-row census is (53624480,67257904,74299396,80379126,82205586,85479878,83844924,85479878,82205586,80379126,74299396,67257904,53624480), whose sum is 970337664. The difference is 5524. Because weighted_surviving multiplies each row by SUPPORT[deleted], these are not interchangeable constants. The archived final proof did not depend on this exploratory diagnostic. The original thirteen-row execution log is now bundled in reconciliation_sources. This release recomputes its sum and compares the active constants with those recorded rows; it does not claim a new full determinant enumeration.

Scope: computation_false

恢复数值错误确认：原执行日志逐行给出的实际 support 与活跃 C++ 常量不同，合计相差5524；旧程序中常量确用于 weighted_surviving。它不影响已分开验证的最终证书。

打包脚本因“本轮未重跑determinant census”自动降级了已有确认。这是打包回归，不是缺失错误证据。现补入原执行日志，不冒称重新运行整个枚举。

## 3. Evidence and verification

原始声明、已恢复历史裁定和对应 witness 对照；新增数学推导及计算层级单独标明。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-explore_round82_global.cpp](original/M01-explore_round82_global.cpp) — inherited_sanitized_source
- [M02-round-82-response.md](original/M02-round-82-response.md) — inherited_sanitized_source
- [M03-concentrated_audit_5_rounds_82_105.md](original/M03-concentrated_audit_5_rounds_82_105.md) — inherited_sanitized_source
- [M04-round-104-prompt.md](original/M04-round-104-prompt.md) — inherited_sanitized_source
- [R01-M01-explore_round82_global.cpp.context.md](reconciliation_sources/R01-M01-explore_round82_global.cpp.context.md) — reconciliation_source_window
- [R02-round82-exploratory-global.log.context.md](reconciliation_sources/R02-round82-exploratory-global.log.context.md) — reconciliation_source_window
- [A01-round82-exploratory-global.log](reconciliation_sources/A01-round82-exploratory-global.log) — supplementary_artifact
- [A02-round-82-local-audit.md](reconciliation_sources/A02-round-82-local-audit.md) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
