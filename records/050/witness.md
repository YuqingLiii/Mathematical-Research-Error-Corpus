# 050 — Projection can kill directions; independence before projection does not imply independence afterward.

**Research problem:** P11 — Finite-dimensional Grothendieck bounds

## Original statement

> 等号面支撑核至少为 28 维，而非此前的 12 维，因此算子秩上界严格改进为 746,797。

**Context:** The assistant promoted a pre-projection equality-space dimension to a bound on the retained746825 coordinates.

**Original locator:** Assistant message, 2026-08-29T02:46:52.613Z; transcript lines2965–2970.

## Why it is an error

Projection can kill directions; independence before projection does not imply independence afterward.

## Witness / evidence

Of the28 old directions,16 degree-3/4 Walsh directions are individually zero on all retained coordinates. The surviving image has rank12: a retained12-by-12 minor has determinant -120231596497305600, and the16 zero directions give the matching upper bound. Therefore the supported kernel bound is at least12, giving rank<=746825-12=746813; the claimed746825-28=746797 does not follow.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 投影前 28 个独立方向不推出保留坐标上的像仍为 28 维；16 个方向被投影为零，所报秩改进没有依据。

## Adjudication notes

Projection can kill directions; independence before projection does not imply independence afterward.

Of the28 old directions,16 degree-3/4 Walsh directions are individually zero on all retained coordinates. The surviving image has rank12: a retained12-by-12 minor has determinant -120231596497305600, and the16 zero directions give the matching upper bound. Therefore the supported kernel bound is at least12, giving rank<=746825-12=746813; the claimed746825-28=746797 does not follow.

Scope: argument_invalid

28 个旧方向中 16 个在保留坐标上为零；归档非零 minor 与零向量证明像空间维度 12。投影前维数不能支持投影后的改进秩界。此次检查推导及归档证据，未重跑全尺寸 minor 计算。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-01a04050-2c65-7022-8844-6319c2da0799.md.excerpt.md](original/M01-01a04050-2c65-7022-8844-6319c2da0799.md.excerpt.md)
- [original/M02-h4_degree4_equality_restriction_rank.py](original/M02-h4_degree4_equality_restriction_rank.py)
- [original/M03-h4_effective_equality_rank_checker.py](original/M03-h4_effective_equality_rank_checker.py)
- [original/M04-d4-effective-equality-rank-certificate-20260830.json](original/M04-d4-effective-equality-rank-certificate-20260830.json)
- [original/M05-d4-effective-equality-rank-checker-output-20260830.json](original/M05-d4-effective-equality-rank-checker-output-20260830.json)
- [original/M06-GROTHD4.degree4.equality-rank.yaml](original/M06-GROTHD4.degree4.equality-rank.yaml)
- [original/M07-d4_n1_300x300.mat.degree4_equality_restriction_rank.json](original/M07-d4_n1_300x300.mat.degree4_equality_restriction_rank.json)
- [original/M08-d4-sos-symmetry-20260830.md](original/M08-d4-sos-symmetry-20260830.md)

[Back to all 65 errors](../../README.md)
