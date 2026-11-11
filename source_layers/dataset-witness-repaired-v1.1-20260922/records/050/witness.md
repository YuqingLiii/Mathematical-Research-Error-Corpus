# Record 050 — Finite-dimensional Grothendieck bounds

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> 等号面支撑核至少为 28 维，而非此前的 12 维，因此算子秩上界严格改进为 746,797。

Context: The assistant promoted a pre-projection equality-space dimension to a bound on the retained746825 coordinates.

Locator: Assistant message, 2026-08-29T02:46:52.613Z; transcript lines2965–2970.

## 2. Witness / adjudication

Projection can kill directions; independence before projection does not imply independence afterward.

Of the28 old directions,16 degree-3/4 Walsh directions are individually zero on all retained coordinates. The surviving image has rank12: a retained12-by-12 minor has determinant -120231596497305600, and the16 zero directions give the matching upper bound. Therefore the supported kernel bound is at least12, giving rank<=746825-12=746813; the claimed746825-28=746797 does not follow.

Scope: argument_invalid

28 个旧方向中 16 个在保留坐标上为零；归档非零 minor 与零向量证明像空间维度 12。投影前维数不能支持投影后的改进秩界。此次检查推导及归档证据，未重跑全尺寸 minor 计算。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-01a04050-2c65-7022-8844-6319c2da0799.md.excerpt.md](original/M01-01a04050-2c65-7022-8844-6319c2da0799.md.excerpt.md) — inherited_sanitized_source
- [M02-h4_degree4_equality_restriction_rank.py](original/M02-h4_degree4_equality_restriction_rank.py) — inherited_sanitized_source
- [M03-h4_effective_equality_rank_checker.py](original/M03-h4_effective_equality_rank_checker.py) — inherited_sanitized_source
- [M04-d4-effective-equality-rank-certificate-20260830.json](original/M04-d4-effective-equality-rank-certificate-20260830.json) — inherited_sanitized_source
- [M05-d4-effective-equality-rank-checker-output-20260830.json](original/M05-d4-effective-equality-rank-checker-output-20260830.json) — inherited_sanitized_source
- [M06-GROTHD4.degree4.equality-rank.yaml](original/M06-GROTHD4.degree4.equality-rank.yaml) — inherited_sanitized_source
- [M07-d4_n1_300x300.mat.degree4_equality_restriction_rank.json](original/M07-d4_n1_300x300.mat.degree4_equality_restriction_rank.json) — inherited_sanitized_source
- [M08-d4-sos-symmetry-20260830.md](original/M08-d4-sos-symmetry-20260830.md) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
