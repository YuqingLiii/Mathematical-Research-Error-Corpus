# Record 071 — Group-orbit Bell matrices

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> implication: Equality in the spectral upper bound confines every extremizer to paired top singular
>       spaces; group averaging and real Schur theory then reduce invariant Gram weights to R/C/H multiplicity
>       variables, while row norms become explicit balance constraints.
>     proof:
>       sketch: Combine equality conditions for the norm bound with the isotypic commutant decomposition.
>         The current draft only sketches the necessity direction.

Context: 这是 GROTHORB.extremizer-classification 节点保留的 commutant-classification 旧路线。父 claim 的目标是 all vector extremizers，而这条路线只把 invariant Gram weights 约化到 commutant。错误位于这项受限约化被注册为完成全部极值策略分类的路线，不在正确的 invariant averaging 子结论。节点同时保留该路线后来 REFUTED/retired 的记录和正确的替代 spectrahedral 路线；这里引用的是原退休路线，不是替代路线。

Locator: See reconciliation source window 1

## 2. Witness / adjudication

群平均可以产生不变的最优权重，但不保证所有最优权重都不变。因而只参数化 commutant 中的不变权重不能完成父节点要求的全部极值策略分类。

取 A=I_3，群 S_3 同时置换行列，U=V=I_3。令 H=[[1,1/2,0],[1/2,1,0],[0,0,1]]；其特征值为3/2、1/2、1且对角均为1，故正定并满足全部平衡条件。任意分解 H=TT^T 给出 X=Y=T，目标值 Tr(H)=3，达到谱上界。H 的非对角元不恒定，所以不与全部 S_3 置换矩阵交换，不属于 commutant。该具体极值策略没有被旧 commutant 路线覆盖。

Scope: argument_invalid

保留为失败的 all-extremizer 路线，不指控较窄的 invariant averaging 引理。独立可读节点将 commutant-classification 注册为通向 all vector extremizers 的路线，而正文只支持 invariant weights；该路线自身保留 REFUTED 评估及同日反例。A=I3、S3 作用下的非恒定非对角 correlation weight 正定、单位对角，给出最优策略但不属于 commutant，因此 invariant 参数化不能覆盖所有极值策略。未完成路线也属于本数据集允许分析的错误单位。

旧 historical_provenance_report 398-442 定位的是节点/路线目标与 premise 的范围错配，不是寻找正文里一个不存在的 all-invariant 句子。上一轮只审正文的 invariant 限定，遗漏了父 claim 与已保留的退休路线，故 pending 撤销。不得把后来的 spectrahedral 正确替代路线误当原错误。

补回原结构化记录遗漏的节点路线原文，并把错误单位限定为旧路线与 all-extremizer 父目标之间的范围错配；不捏造正文中不存在的‘all optimizers invariant’句子，也不要求该失败路线曾获 PROVED。

## 3. Evidence and verification

Read original premise artifact, retained route and parent claim, dated route-refutation event, and explicit I3/S3 witness. Checked PSD eigenvalues 3/2,1/2,1, unit diagonal and nonconstant off-diagonals analytically; no hidden reasoning or first-write recovery requirement imposed.

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-GROTHORB.extremizer-classification.yaml](original/M01-GROTHORB.extremizer-classification.yaml) — inherited_sanitized_source
- [M02-balanced-rank-theorem-draft-20260829.md](original/M02-balanced-rank-theorem-draft-20260829.md) — inherited_sanitized_source
- [M03-complete-extremizer-classification-20260829.md](original/M03-complete-extremizer-classification-20260829.md) — inherited_sanitized_source
- [M04-spectral-classification-repair-review-20260907.md](original/M04-spectral-classification-repair-review-20260907.md) — inherited_sanitized_source
- [M05-group-orbit-literature-positioning-20260907.md](original/M05-group-orbit-literature-positioning-20260907.md) — inherited_sanitized_source
- [M06-group-orbit-exploration-20260907.md](original/M06-group-orbit-exploration-20260907.md) — inherited_sanitized_source
- [R01-GROTHORB.extremizer-classification.yaml.context.md](reconciliation_sources/R01-GROTHORB.extremizer-classification.yaml.context.md) — reconciliation_source_window
- [R02-GROTHORB.extremizer-classification.yaml.context.md](reconciliation_sources/R02-GROTHORB.extremizer-classification.yaml.context.md) — reconciliation_source_window
- [R03-complete-extremizer-classification-20260829.md.context.md](reconciliation_sources/R03-complete-extremizer-classification-20260829.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
