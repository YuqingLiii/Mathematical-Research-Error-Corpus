# 072 — 旧节点把只有在可行集非空时才有意义的 minimum-dimension/minimum-rank 结论写成无条件子句。空集上通常意义的 minimum 不存在；旧审查目标没有明示扩展值约定。

**Research problem:** P12 — Group-orbit Bell matrices

## Original statement

> the minimum real vector dimension among such strategies is the minimum rank of a feasible H.

**Context:** 此句由2026-09-07同期独立审查 F4 逐字保留，审查绑定的是旧 GROTHORB.equality-characterization.claim，SHA256 b0247e9891b03886886050461c971ee8f44b8535257deeeaacea7c5da1d2184e。该旧节点对任意非零 A 量化，却遗漏可行集非空限定；原 GOC-T3 正文有 Whenever it does，后来 SC2 与节点事件明确补回。这里不是首次写入事件的恢复，也不把已经修正的当前节点当成旧原文。

**Original locator:** See reconciliation source window 1

## Why it is an error

旧节点把只有在可行集非空时才有意义的 minimum-dimension/minimum-rank 结论写成无条件子句。空集上通常意义的 minimum 不存在；旧审查目标没有明示扩展值约定。

## Witness / evidence

取 A=diag(2,1)。其最大奇异值为2且重数r=1，可取 U=V=(1,0)^T。任意标量权重h的 VhV^T 对角为(h,0)，不能等于(1,1)，故平衡谱面体为空，不存在达到谱上界的策略，也不存在该集合上的最小秩。反例只击中未限定的 minimum 子句；等式刻画以及可行集非空条件下的秩公式仍正确。

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 将只在可行集非空时有意义的最小秩表述推广到任意非零 A；diag(2,1) 使该平衡可行集为空，没有通常意义下的 minimum。

minimum 的非空适用前提未保留，归 IV；不声称所有数学知识缺失或术语混淆。

## Adjudication notes

旧节点把只有在可行集非空时才有意义的 minimum-dimension/minimum-rank 结论写成无条件子句。空集上通常意义的 minimum 不存在；旧审查目标没有明示扩展值约定。

取 A=diag(2,1)。其最大奇异值为2且重数r=1，可取 U=V=(1,0)^T。任意标量权重h的 VhV^T 对角为(h,0)，不能等于(1,1)，故平衡谱面体为空，不存在达到谱上界的策略，也不存在该集合上的最小秩。反例只击中未限定的 minimum 子句；等式刻画以及可行集非空条件下的秩公式仍正确。

Scope: argument_invalid

保留为原节点 minimum-dimension 子句遗漏非空前提，非等式刻画定理错误。原正文 GOC-T3 已写 Whenever it does，但旧节点对任意非零 A 写出 minimum rank；不可行的 diag(2,1) 使通常意义下 minimum 未定义。不可用现在已修好的节点或另一个 rank-threshold 定义中的 infinity 约定反向补入旧节点。F4 给出旧 exact claim 哈希与逐字旧子句，SC2 与节点事件确认修改；这已足够绑定历史错误，不必重新找到最初写入消息。

旧恢复的目标是 hash-bound 旧节点而非正确的下层正文。上一轮新增要求逐字首次写入/全新推理轨迹，不是判定局部节点声明缺陷所必需。恢复旧范围缺口裁定；不宣称目标谱面体理论整体错误。

用同期哈希绑定审查的逐字旧节点引文补齐 original_excerpt；明确来源形式为 contemporaneous_review_quotation，不声称找到旧节点首次写入，也不因缺少首次写入重新降级。

## Original materials

- [original/M01-spectral-classification-review-20260907.md](original/M01-spectral-classification-review-20260907.md)
- [original/M02-proof_dag_schema.py](original/M02-proof_dag_schema.py)
- [original/M03-balanced-rank-theorem-draft-20260829.md](original/M03-balanced-rank-theorem-draft-20260829.md)
- [original/M04-complete-extremizer-classification-20260829.md](original/M04-complete-extremizer-classification-20260829.md)
- [original/M05-GROTHORB.spectral-upper.yaml](original/M05-GROTHORB.spectral-upper.yaml)
- [original/M06-GROTHORB.balanced-criterion.yaml](original/M06-GROTHORB.balanced-criterion.yaml)
- [original/M07-GROTHORB.invariant-projector.yaml](original/M07-GROTHORB.invariant-projector.yaml)
- [original/M08-GROTHORB.equality-characterization.yaml](original/M08-GROTHORB.equality-characterization.yaml)
- [original/M09-GROTHORB.transitive-optimum.yaml](original/M09-GROTHORB.transitive-optimum.yaml)
- [original/M10-GROTHORB.extremizer-classification.yaml](original/M10-GROTHORB.extremizer-classification.yaml)
- [original/M11-GROTHORB.counterexample.yaml](original/M11-GROTHORB.counterexample.yaml)
- [original/M12-GROTHORB.noninvariant-extremizer.yaml](original/M12-GROTHORB.noninvariant-extremizer.yaml)
- [original/context/A01-spectral-classification-scope-repair-20260907.md](original/context/A01-spectral-classification-scope-repair-20260907.md)
- [original/context/R01-spectral-classification-review-20260907.md.context.md](original/context/R01-spectral-classification-review-20260907.md.context.md)
- [original/context/R02-complete-extremizer-classification-20260829.md.context.md](original/context/R02-complete-extremizer-classification-20260829.md.context.md)
- [original/context/R03-spectral-classification-scope-repair-20260907.md.context.md](original/context/R03-spectral-classification-scope-repair-20260907.md.context.md)
- [original/context/R04-GROTHORB.equality-characterization.yaml.context.md](original/context/R04-GROTHORB.equality-characterization.yaml.context.md)

[Back to all 65 errors](../../README.md)
