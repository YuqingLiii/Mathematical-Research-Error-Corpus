# 065 — Two copied input-vector values disagree with the independently regenerated determinant counts.

**Research problem:** P01 — Channel additivity violations

## Original statement

> \[
> (H_{4,i})=(
> 8437248,11517728,12835576,14928318,15308304,16650864,15684084,
> 16650864,15308304,14928318,12835576,11517728,8437248).
> \tag{98.10}
> \]

**Context:** The transmitted input contains a thirteen-entry vector of raw-size-four determinant counts. Two entries were altered during prompt preparation; the receiving response recomputed the vector before use. This is an input-preparation error, not attributed to the receiving solver.

**Original locator:** round-98-prompt-sent.md, lines 148–153

## Why it is an error

Two copied input-vector values disagree with the independently regenerated determinant counts.

## Witness / evidence

The transmitted vector contains 14928318 in zero-based rows 3 and 9. The regenerated raw-size-four vector is (8437248,11517728,12835576,14926862,15308304,16650864,15684084,16650864,15308304,14926862,12835576,11517728,8437248). The erroneous entries exceed the recomputed entries by 1456 each. The receiving response exposes and corrects this mismatch before using the data. The original thirteen-row execution log and the contemporaneous input audit are bundled in reconciliation_sources. Their source-bound mismatch is confirmed; a new full determinant enumeration was not performed in this release pass.

## Scope

computation_false

## Classification

- V: 其他错误. 输入准备的文本替换把原计数 14926862 改成 14928318；同期审计记录了具体替换及接收方纠正。属于传递材料的数值损坏，不归因于接收方数学推理。

研究场景适配：V 的材料传递错误发生在下一轮输入，而不是最终答案；其具体文本替换由归档审计支持。

其他类别用于下一轮输入的抄录/替换错误

## Adjudication notes

Two copied input-vector values disagree with the independently regenerated determinant counts.

The transmitted vector contains 14928318 in zero-based rows 3 and 9. The regenerated raw-size-four vector is (8437248,11517728,12835576,14926862,15308304,16650864,15684084,16650864,15308304,14926862,12835576,11517728,8437248). The erroneous entries exceed the recomputed entries by 1456 each. The receiving response exposes and corrects this mismatch before using the data. The original thirteen-row execution log and the contemporaneous input audit are bundled in reconciliation_sources. Their source-bound mismatch is confirmed; a new full determinant enumeration was not performed in this release pass.

Scope: computation_false

恢复输入转录错误确认：发送稿两处14928318不等于已有精确日志及接收端独立复核的14926862；接收端在使用前已经纠正。

本条研究的是输入准备事件，不归因给接收模型；旧核验和实际日志已存在。不能因本次未重跑巨大枚举再说材料没齐。

## Original materials

- [original/M01-round-98-prompt-sent.md](original/M01-round-98-prompt-sent.md)
- [original/M02-round-98-response.md](original/M02-round-98-response.md)
- [original/M03-concentrated_audit_5_rounds_82_105.md](original/M03-concentrated_audit_5_rounds_82_105.md)
- [original/M04-explore_round82_global.cpp](original/M04-explore_round82_global.cpp)
- [original/M05-round-104-prompt.md](original/M05-round-104-prompt.md)
- [original/context/A01-round98-exploratory-global.log](original/context/A01-round98-exploratory-global.log)
- [original/context/A02-round-98-local-audit.md](original/context/A02-round-98-local-audit.md)
- [original/context/R01-M01-round-98-prompt-sent.md.context.md](original/context/R01-M01-round-98-prompt-sent.md.context.md)
- [original/context/R02-round98-exploratory-global.log.context.md](original/context/R02-round98-exploratory-global.log.context.md)
- [original/context/R03-round-98-local-audit.md.context.md](original/context/R03-round-98-local-audit.md.context.md)

[Back to all 65 errors](../../README.md)
