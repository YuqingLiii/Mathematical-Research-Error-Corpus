# 056 — For a rectangular zero matrix, the full left and right top singular spaces have different dimensions and cannot be paired as required by the construction.

**Research problem:** P12 — Group-orbit Bell matrices

## Original statement

> The proof also gives explicit extremizing vectors: the normalized rows of any
> paired top left/right singular bases.

**Context:** The theorem applies to real rectangular matrices with transitive row and column permutation actions and does not exclude the zero matrix.

**Original locator:** Original balanced-rank theorem draft, GO-T4, lines 66–85.

## Why it is an error

For a rectangular zero matrix, the full left and right top singular spaces have different dimensions and cannot be paired as required by the construction.

## Witness / evidence

Let A be the 1-by-2 zero matrix. The two-element group acts trivially on its one row and swaps the two columns, so both actions are transitive and equivariance holds. The full top left space is R and the full top right space is R^2. Bases spanning these spaces have one and two columns, respectively; there is no pair with a common column count. Every feasible strategy still has the correct optimum value zero, so only the unconditional construction clause fails.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 从顶奇异空间推出任意矩形矩阵都可使用等列数完整配对基，未处理零矩阵左右维数不同的情形；A=0 的 1x2 例子否定无条件构造。

零矩阵是新构造论断未覆盖的合法情形；原题未被重新定义，归 IV。

## Adjudication notes

For a rectangular zero matrix, the full left and right top singular spaces have different dimensions and cannot be paired as required by the construction.

Let A be the 1-by-2 zero matrix. The two-element group acts trivially on its one row and swaps the two columns, so both actions are transitive and equivariance holds. The full top left space is R and the full top right space is R^2. Bases spanning these spaces have one and two columns, respectively; there is no pair with a common column count. Every feasible strategy still has the correct optimum value zero, so only the unconditional construction clause fails.

Scope: argument_invalid

保留为零矩阵边界处的构造范围越界，不是最优值定理为假。GO-T2 的 paired-basis 构造要求 sigma>0，但 GO-T4 单独量化 transitive equivariant 矩阵，并在不排除 A=0 时声称 normalized rows of any paired top bases 给出极值向量；同样遗漏进入独立哈希绑定的 transitive-optimum 节点。对 1×2 零矩阵，完整左右 top spaces 的维数分别为 1、2，不能按该定义选择同列数的完整 paired bases。后续范围修复明确承认 earlier unconditional wording was too broad。

上一轮 pending 忽略了同一档案的 F5/F5R 精确目标审查和 SC1 显式修复。GO-T2 的局部 sigma>0 假设不自动修复 GO-T4 与父节点中已无条件写出的构造承诺。恢复旧缺陷裁定，严格只指构造子句。

## Original materials

- [original/M01-balanced-rank-theorem-draft-20260829.md](original/M01-balanced-rank-theorem-draft-20260829.md)
- [original/M02-spectral-classification-review-20260907.md](original/M02-spectral-classification-review-20260907.md)
- [original/M03-proof_dag_schema.py](original/M03-proof_dag_schema.py)
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
- [original/context/R01-balanced-rank-theorem-draft-20260829.md.context.md](original/context/R01-balanced-rank-theorem-draft-20260829.md.context.md)
- [original/context/R02-balanced-rank-theorem-draft-20260829.md.context.md](original/context/R02-balanced-rank-theorem-draft-20260829.md.context.md)
- [original/context/R03-spectral-classification-review-20260907.md.context.md](original/context/R03-spectral-classification-review-20260907.md.context.md)
- [original/context/R04-spectral-classification-scope-repair-20260907.md.context.md](original/context/R04-spectral-classification-scope-repair-20260907.md.context.md)

[Back to all 65 errors](../../README.md)
