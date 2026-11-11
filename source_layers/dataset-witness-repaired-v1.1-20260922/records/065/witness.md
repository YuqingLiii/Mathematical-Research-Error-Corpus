# Record 065 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> \[
> (H_{4,i})=(
> 8437248,11517728,12835576,14928318,15308304,16650864,15684084,
> 16650864,15308304,14928318,12835576,11517728,8437248).
> \tag{98.10}
> \]

Context: The transmitted input contains a thirteen-entry vector of raw-size-four determinant counts. Two entries were altered during prompt preparation; the receiving response recomputed the vector before use. This is an input-preparation error, not attributed to the receiving solver.

Locator: round-98-prompt-sent.md, lines 148–153

## 2. Witness / adjudication

Two copied input-vector values disagree with the independently regenerated determinant counts.

The transmitted vector contains 14928318 in zero-based rows 3 and 9. The regenerated raw-size-four vector is (8437248,11517728,12835576,14926862,15308304,16650864,15684084,16650864,15308304,14926862,12835576,11517728,8437248). The erroneous entries exceed the recomputed entries by 1456 each. The receiving response exposes and corrects this mismatch before using the data. The original thirteen-row execution log and the contemporaneous input audit are bundled in reconciliation_sources. Their source-bound mismatch is confirmed; a new full determinant enumeration was not performed in this release pass.

Scope: computation_false

恢复输入转录错误确认：发送稿两处14928318不等于已有精确日志及接收端独立复核的14926862；接收端在使用前已经纠正。

本条研究的是输入准备事件，不归因给接收模型；旧核验和实际日志已存在。不能因本次未重跑巨大枚举再说材料没齐。

## 3. Evidence and verification

原始声明、已恢复历史裁定和对应 witness 对照；新增数学推导及计算层级单独标明。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-98-prompt-sent.md](original/M01-round-98-prompt-sent.md) — inherited_sanitized_source
- [M02-round-98-response.md](original/M02-round-98-response.md) — inherited_sanitized_source
- [M03-concentrated_audit_5_rounds_82_105.md](original/M03-concentrated_audit_5_rounds_82_105.md) — inherited_sanitized_source
- [M04-explore_round82_global.cpp](original/M04-explore_round82_global.cpp) — inherited_sanitized_source
- [M05-round-104-prompt.md](original/M05-round-104-prompt.md) — inherited_sanitized_source
- [R01-M01-round-98-prompt-sent.md.context.md](reconciliation_sources/R01-M01-round-98-prompt-sent.md.context.md) — reconciliation_source_window
- [R02-round98-exploratory-global.log.context.md](reconciliation_sources/R02-round98-exploratory-global.log.context.md) — reconciliation_source_window
- [R03-round-98-local-audit.md.context.md](reconciliation_sources/R03-round-98-local-audit.md.context.md) — reconciliation_source_window
- [A01-round98-exploratory-global.log](reconciliation_sources/A01-round98-exploratory-global.log) — supplementary_artifact
- [A02-round-98-local-audit.md](reconciliation_sources/A02-round-98-local-audit.md) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
