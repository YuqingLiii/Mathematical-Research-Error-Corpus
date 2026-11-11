# Record 019 — Werner–Holevo zero-capacity boundary

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> class ExtensionSDP:
>     def __init__(self) -> None:
>         self.rho = cp.Variable((SYM_DIM, SYM_DIM), symmetric=True, name="rho")
>         self.t = cp.Variable(name="t")
>         self.x = cp.Parameter(name="x")
>         self.eta = V @ self.rho @ V.T

Context: V is the isometry onto A tensor Sym^2(B), of dimension 3 times 6 = 18. The frozen task asked for an extension invariant under swapping two qutrit B systems, not necessarily supported only in their symmetric subspace.

Locator: Semidefinite-program script creation, 2026-07-28T22:15:31.150Z, JSONL line 130

## 2. Witness / adjudication

Swap invariance was replaced by the strictly stronger requirement of support in the symmetric subspace.

Let v=(|01>-|10>)/sqrt(2) and X=|0><0|_A tensor |v><v|. X is positive semidefinite and obeys S X S=X because Sv=-v. It is therefore swap-invariant, but its support lies entirely in the antisymmetric B sector and cannot be written V rho V^T. In the qutrit case the omitted block has dimension 3 times 3 = 9. The code solves a restricted feasibility problem, so its infeasibility cannot certify the original criterion.

Scope: argument_invalid

交换不变的反对称态不支撑在对称子空间；将前一种可行性替换为后一种，改变了编码模型。此 witness 不证明特定目标态在较大集合内必有扩张，也不自动建立某次最终容量 overclaim。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-WHGAP-P1-019faab6.jsonl.readable.md](original/M01-WHGAP-P1-019faab6.jsonl.readable.md) — inherited_sanitized_source
- [M01-WHGAP-P1-019faab6.jsonl.visible.json](original/M01-WHGAP-P1-019faab6.jsonl.visible.json) — inherited_sanitized_source
- [M02-whgap_p1_review_20260728.md](original/M02-whgap_p1_review_20260728.md) — inherited_sanitized_source
- [M03-WHGAP-main-c5b96aec.jsonl.readable.md](original/M03-WHGAP-main-c5b96aec.jsonl.readable.md) — inherited_sanitized_source
- [M03-WHGAP-main-c5b96aec.jsonl.visible.json](original/M03-WHGAP-main-c5b96aec.jsonl.visible.json) — inherited_sanitized_source
- [M04-whgap_p1_review_20260728.md](original/M04-whgap_p1_review_20260728.md) — inherited_sanitized_source
- [M05-whgap_independent_review.py](original/M05-whgap_independent_review.py) — inherited_sanitized_source
- [M06-whgap_full_sdp_crosscheck.py](original/M06-whgap_full_sdp_crosscheck.py) — inherited_sanitized_source
- [M07-whgap_independent_results.json](original/M07-whgap_independent_results.json) — inherited_sanitized_source
- [M08-whgap_support_margin_tolerance.log](original/M08-whgap_support_margin_tolerance.log) — inherited_sanitized_source
- [M09-whgap_support_margin.py](original/M09-whgap_support_margin.py) — inherited_sanitized_source
- [M10-whgap_proposer_reproduction.py](original/M10-whgap_proposer_reproduction.py) — inherited_sanitized_source
- [M11-SHA256SUMS.txt](original/M11-SHA256SUMS.txt) — inherited_sanitized_source
- [M12-SHA256SUMS.txt](original/M12-SHA256SUMS.txt) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
