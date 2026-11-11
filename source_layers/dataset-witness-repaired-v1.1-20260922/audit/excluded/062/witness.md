# Record 062 — Channel additivity violations

**Final admission:** excluded. **Overclaim:** not_applicable.

## 1. Original statement and context

> The adjacent \(14\)-root matrix circuit and its convex dual are correct. However, the holomorphic Plücker relation does **not** directly control the required sesquilinear circuit. The exact outcome is a rigorous method limit:
> 
> $$
> \boxed{
> \begin{gathered}
> \text{Any valid linear use of the adjacent holomorphic Plücker wedge is either}\\
> \text{inadmissible for the physical sesquilinear circuit, or—when a constant}\\
> \text{conjugation real structure makes it admissible—has identically zero target gain.}
> \end{gathered}}
> \tag{PlueckerLinearNoGo}
> $$
> 
> This is proved for arbitrary adjacent \(k+2\)-root/\(k\)-slope circuits over any odd prime field. An explicit frozen-dimensional canonical-cofactor family attains the zero-target conclusion with a nonzero ordinary Plücker coefficient, so the result is not merely formal.
> 
> It does **not** rule out:
> 
> * a constant separator using the transpose-symmetric matrix directions;
> * a constant separator combining those directions with the Plücker direction to reduce the ordinary denominator;
> * a genuinely frequency-dependent matrix multiplier;
> * the exact global shared-phase dual across all Fourier frequencies.

Context: The proof handles a pure alternating Pluecker direction under a constant conjugation real structure. Immediately after the broad headline, the response explicitly excludes mixed symmetric/alternating, frequency-dependent, and global constructions from its conclusion.

Locator: round-41-response.md, lines 17–36

## 2. Witness / adjudication

This allegation is **not a positive mathematical-error record** in this release. The old witness is retained in history/input_witness.md for accountability, not endorsed here.

原文在同一段明确保留 symmetric、混合分母和频率依赖等例外；现 witness 只列出这些已排除的方向。

不能把headline脱离相邻明确限定后再判全称越界。

## 3. Evidence and verification

原始声明、已恢复历史裁定和对应 witness 对照；新增数学推导及计算层级单独标明。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-41-response.md](original/M01-round-41-response.md) — inherited_sanitized_source
- [M02-concentrated_audit_2_rounds_24_42.md](original/M02-concentrated_audit_2_rounds_24_42.md) — inherited_sanitized_source
- [M03-MASTER_AUDIT_PROTOCOL.md](original/M03-MASTER_AUDIT_PROTOCOL.md) — inherited_sanitized_source
- [M04-round-23-local-audit.md](original/M04-round-23-local-audit.md) — inherited_sanitized_source
- [A01-witness.md](reconciliation_sources/A01-witness.md) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).

## v1.1 witness repair review

旧反例利用原文明确排除的对称、混合或频率依赖方向。

把原段全部限定接回后，所给例子不反驳其纯交替线性范围。

原反例不在断言范围；没有用另一个问题替换它。
