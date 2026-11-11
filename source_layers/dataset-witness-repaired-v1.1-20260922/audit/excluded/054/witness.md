# Record 054 — Finite-dimensional Grothendieck bounds

**Final admission:** excluded. **Overclaim:** not_applicable.

## 1. Original statement and context

> E8 会话最终裁定 PROVED：官方归档、两份独立精确枚举、格同余、达界符号构造及谱值全部闭合，得到 K_G(8)≥165/109。

Context: The coordinator declared completion of an eight-dimensional Grothendieck-bound certificate. The recovered exact checker enumerates root-poset filters, but the connection to the Bell matrix and its two claimed optima was not present in the checked artifact.

Locator: Assistant message, 2026-08-27T01:44:33.150Z; reconstruction note, sections E8-R1–R5.

## 2. Witness / adjudication

This allegation is **not a positive mathematical-error record** in this release. The old witness is retained in history/input_witness.md for accountability, not endorsed here.

现有 witness 将 08-29 本地重建时缺少 Bell 矩阵和 9240/6104 推导，推定为 08-27 宣布完成时也没有这些推导。但完整原 rollout 的 01:29、01:31 和 01:44 网页捕获实际保存了 B=3G-13I、9240 的谱上界与单位根向量达界、任意符号配置到 upper filter 的归约、k=98/104 的格同余闭合，以及 6104 的 A1+A6 显式达界构造。网页还明确说存储的 SDP 数值只是归档一致性检查，不是其证明。故缺桥 witness 与当时完整材料冲突，不能据此确认协调器的数学完成声明错误。

已核对 P9_RECOVERY_20260917.md 44-55 与 historical_provenance_report.md 1939-1977 的 P→A/RECOVERED 历史裁定；它们的确恢复了协调器完成声明，但依赖后来的本地重建缺失推断当时缺桥。此次新增到审核视野的原浏览器工具输出直接否定这一推断，因此排除当前记录，非重新要求用户恢复机器，也非认证整个 E8 证明无误。

## 3. Evidence and verification

Directly read historical coordinator statements, recovery verdict, local reconstruction note, and earlier original webpage captures. This is claim-witness alignment reconciliation, not a new independent audit of all E8 congruence arguments or enumeration.

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-01a04050-2c65-7022-8844-6319c2da0799.md.excerpt.md](original/M01-01a04050-2c65-7022-8844-6319c2da0799.md.excerpt.md) — inherited_sanitized_source
- [M02-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.readable.md](original/M02-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M02-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.visible.json](original/M02-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M03-e8-reconstruction-20260829.md](original/M03-e8-reconstruction-20260829.md) — inherited_sanitized_source
- [R01-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md](reconciliation_sources/R01-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md) — reconciliation_source_window
- [R02-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md](reconciliation_sources/R02-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md) — reconciliation_source_window
- [R03-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md](reconciliation_sources/R03-rollout-2026-08-26T19-03-11-<session-id-redacted>.jsonl.context.md) — reconciliation_source_window
- [R04-e8-reconstruction-20260829.md.context.md](reconciliation_sources/R04-e8-reconstruction-20260829.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).

## v1.1 witness repair review

以后来的不完整重建推断原证明也缺失桥梁。

对回原网页，Bell 矩阵、9240 谱界、upper-filter 归约、6104 达界构造均在。不能继续用“未给这些步骤”作 witness。

当前缺桥指控不成立；不等于认证整个证明。
