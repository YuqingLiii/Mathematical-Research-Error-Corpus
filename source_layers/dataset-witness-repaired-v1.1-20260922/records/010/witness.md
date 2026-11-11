# Record 010 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> It is strictly smaller and more structured than the original \(D^2\) baseline phase problem:
> 
> * parameters lie on four explicit ruling lines;
> * each distinct-slope line-pair contributes at most one product to each \(K_\Delta\);
> * rank-one differences are confined to the two ruling directions;
> * every other contribution is a fully explicit nondegenerate dual chirp.
> 
> No exact solution or contradiction is obtained.

Context: The finite-field construction uses two paired ruling directions in the rank-one quadratic cone, represented in coordinates (a,b,c) with discriminant 4ac-b^2. The claimed restriction concerns differences between points on the chosen rulings.

Locator: round-29-response.md, lines 1356–1363

## 2. Witness / adjudication

Cross-ruling differences can fall in a third ruling direction.

Over F_7, take the selected-ruling points (1,1,0) and (2,3,1). Their difference is (6,5,6)=6(1,2,1), and 4*6*6-5^2=119=0 mod 7. It lies in the rank-one ruling of slope 2, not either chosen ruling direction 0 or 1. Thus the classification of cross differences is false.

Scope: statement_false

模 7 的两个给定点之差为 (6,5,6)，满足退化判别式且落入第三方向，反驳跨 ruling 差不会落入其他 ruling 的断言。只判这一几何断言。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-29-response.md](original/M01-round-29-response.md) — inherited_sanitized_source
- [M02-concentrated_audit_2_rounds_24_42.md](original/M02-concentrated_audit_2_rounds_24_42.md) — inherited_sanitized_source
- [M03-MASTER_AUDIT_PROTOCOL.md](original/M03-MASTER_AUDIT_PROTOCOL.md) — inherited_sanitized_source
- [M04-round-23-local-audit.md](original/M04-round-23-local-audit.md) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
