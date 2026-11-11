# Record 056 — Group-orbit Bell matrices

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> The proof also gives explicit extremizing vectors: the normalized rows of any
> paired top left/right singular bases.

Context: The theorem applies to real rectangular matrices with transitive row and column permutation actions and does not exclude the zero matrix.

Locator: Original balanced-rank theorem draft, GO-T4, lines 66–85.

## 2. Witness / adjudication

For a rectangular zero matrix, the full left and right top singular spaces have different dimensions and cannot be paired as required by the construction.

Let A be the 1-by-2 zero matrix. The two-element group acts trivially on its one row and swaps the two columns, so both actions are transitive and equivariance holds. The full top left space is R and the full top right space is R^2. Bases spanning these spaces have one and two columns, respectively; there is no pair with a common column count. Every feasible strategy still has the correct optimum value zero, so only the unconditional construction clause fails.

Scope: argument_invalid

保留为零矩阵边界处的构造范围越界，不是最优值定理为假。GO-T2 的 paired-basis 构造要求 sigma>0，但 GO-T4 单独量化 transitive equivariant 矩阵，并在不排除 A=0 时声称 normalized rows of any paired top bases 给出极值向量；同样遗漏进入独立哈希绑定的 transitive-optimum 节点。对 1×2 零矩阵，完整左右 top spaces 的维数分别为 1、2，不能按该定义选择同列数的完整 paired bases。后续范围修复明确承认 earlier unconditional wording was too broad。

上一轮 pending 忽略了同一档案的 F5/F5R 精确目标审查和 SC1 显式修复。GO-T2 的局部 sigma>0 假设不自动修复 GO-T4 与父节点中已无条件写出的构造承诺。恢复旧缺陷裁定，严格只指构造子句。

## 3. Evidence and verification

Read original GO-T2/GO-T4, immutable hash-bound F5/F5R review, and SC1 repair; directly checked 1-by-2 zero-matrix dimensions and transitive C2 actions. No numerical experiment required.

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-balanced-rank-theorem-draft-20260829.md](original/M01-balanced-rank-theorem-draft-20260829.md) — inherited_sanitized_source
- [M02-spectral-classification-review-20260907.md](original/M02-spectral-classification-review-20260907.md) — inherited_sanitized_source
- [M03-proof_dag_schema.py](original/M03-proof_dag_schema.py) — inherited_sanitized_source
- [M04-complete-extremizer-classification-20260829.md](original/M04-complete-extremizer-classification-20260829.md) — inherited_sanitized_source
- [M05-GROTHORB.spectral-upper.yaml](original/M05-GROTHORB.spectral-upper.yaml) — inherited_sanitized_source
- [M06-GROTHORB.balanced-criterion.yaml](original/M06-GROTHORB.balanced-criterion.yaml) — inherited_sanitized_source
- [M07-GROTHORB.invariant-projector.yaml](original/M07-GROTHORB.invariant-projector.yaml) — inherited_sanitized_source
- [M08-GROTHORB.equality-characterization.yaml](original/M08-GROTHORB.equality-characterization.yaml) — inherited_sanitized_source
- [M09-GROTHORB.transitive-optimum.yaml](original/M09-GROTHORB.transitive-optimum.yaml) — inherited_sanitized_source
- [M10-GROTHORB.extremizer-classification.yaml](original/M10-GROTHORB.extremizer-classification.yaml) — inherited_sanitized_source
- [M11-GROTHORB.counterexample.yaml](original/M11-GROTHORB.counterexample.yaml) — inherited_sanitized_source
- [M12-GROTHORB.noninvariant-extremizer.yaml](original/M12-GROTHORB.noninvariant-extremizer.yaml) — inherited_sanitized_source
- [R01-balanced-rank-theorem-draft-20260829.md.context.md](reconciliation_sources/R01-balanced-rank-theorem-draft-20260829.md.context.md) — reconciliation_source_window
- [R02-balanced-rank-theorem-draft-20260829.md.context.md](reconciliation_sources/R02-balanced-rank-theorem-draft-20260829.md.context.md) — reconciliation_source_window
- [R03-spectral-classification-review-20260907.md.context.md](reconciliation_sources/R03-spectral-classification-review-20260907.md.context.md) — reconciliation_source_window
- [R04-spectral-classification-scope-repair-20260907.md.context.md](reconciliation_sources/R04-spectral-classification-scope-repair-20260907.md.context.md) — reconciliation_source_window
- [A01-spectral-classification-scope-repair-20260907.md](reconciliation_sources/A01-spectral-classification-scope-repair-20260907.md) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
