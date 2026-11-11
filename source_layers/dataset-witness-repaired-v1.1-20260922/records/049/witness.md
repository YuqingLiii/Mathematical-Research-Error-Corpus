# Record 049 — Finite-dimensional Grothendieck bounds

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> \binom{600}{2}\,598=107281800

Context: The proof note counts index choices with an unordered pair of two distinct vertices and a third distinct vertex.

Locator: Triangle/hypermetric no-go note, lines114–123.

## 2. Witness / adjudication

The displayed integer product is incorrect.

binom(600,2)=600*599/2=179700; multiplying by598 gives107460600, not107281800. The discrepancy is178800. This is a local arithmetic/count-reporting error; it does not by itself invalidate the checker loops or the associated nonnegativity result.

Scope: computation_false

binom(600,2)·598=107460600，与报告值相差 178800。错误不自动污染遍历循环或非负性定理。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-d4-triangle-hypermetric-no-go-20260830.md](original/M01-d4-triangle-hypermetric-no-go-20260830.md) — inherited_sanitized_source
- [M02-GROTHD4.cut.triangle-no-go.yaml](original/M02-GROTHD4.cut.triangle-no-go.yaml) — inherited_sanitized_source
- [M03-rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl.readable.md](original/M03-rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl.readable.md) — inherited_sanitized_source
- [M03-rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl.visible.json](original/M03-rollout-2026-08-30T17-05-15-<session-id-redacted>.jsonl.visible.json) — inherited_sanitized_source
- [M04-h4_triangle_hypermetric_no_go_checker.py](original/M04-h4_triangle_hypermetric_no_go_checker.py) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
