# Record 009 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> At \(|T|=777716\), this is the first undecided finite determinant/kernel system. The dictionary has at most
> 
> $$
> r_1^2+r_1+1
> =
> 970353651
> $$
> 
> columns, but the coefficient vector has the special nonlinear form (8.2). Merely proving \(G_T\) singular would be necessary, not sufficient: its kernel must contain a vector with that exact conjugate-quadratic structure.

Context: The displayed dictionary-count expression uses r1=777716. This is a local arithmetic display, not the main theorem’s proof.

Locator: round-28-response.md, lines 725–733

## 2. Witness / adjudication

The displayed polynomial has been evaluated incorrectly.

Exact integer arithmetic gives 777716^2+777716+1=604842954373, whereas 970353651=31151*31150+1. The printed number belongs to a different expression.

Scope: computation_false

777716²+777716+1=604842954373，与原文求值不符；这是局部精确算术错误。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-28-response.md](original/M01-round-28-response.md) — inherited_sanitized_source
- [M02-concentrated_audit_2_rounds_24_42.md](original/M02-concentrated_audit_2_rounds_24_42.md) — inherited_sanitized_source
- [M03-MASTER_AUDIT_PROTOCOL.md](original/M03-MASTER_AUDIT_PROTOCOL.md) — inherited_sanitized_source
- [M04-round-23-local-audit.md](original/M04-round-23-local-audit.md) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
