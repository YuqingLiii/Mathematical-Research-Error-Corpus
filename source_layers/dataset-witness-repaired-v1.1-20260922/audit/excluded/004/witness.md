# Record 004 — Channel additivity violations

**Final admission:** excluded. **Overclaim:** not_applicable.

## 1. Original statement and context

> Hilbert–Schmidt Cauchy–Schwarz yields
> 
> $$
> \boxed{
> x
> \le
> \frac{uv}{n}
> +
> \sqrt{
> \left(a-\frac{v^2}{n}\right)
> \left(b-\frac{u^2}{n}\right)
> }.
> }
> \tag{Centered-Align}
> $$
> 
> [...]
> 
> | **PROVED**       | The complete direct scalar necessary system (9.1)–(9.13).                                                                                            |                                                           |       |

Context: The scalar variables are n=D^2-1, u=Tr(P), v=Tr(B), x=Tr(BP), a=Tr(B^2), and b=Tr(P^2). Centered-Align is the Hilbert–Schmidt bound after subtracting scalar parts.

Locator: round-06-response.md, lines 325–339, 2084

## 2. Witness / adjudication

This allegation is **not a positive mathematical-error record** in this release. The old witness is retained in history/input_witness.md for accountability, not endorsed here.

原 centered-Cauchy 下端点在完整原系统内严格为负，已经被 x≥0 蕴含；旧退化例 a=v²/n 违反同时存在的 B-rank 约束。新代数推导证明这是原 witness 的域错配，不是缺失材料。

旧审计确实指出没有写下 Cauchy 的另一端，但未检查它在全系统中的冗余性；本次用原有全部相关前提推翻该具体指控。

## 3. Evidence and verification

原始声明、已恢复历史裁定和对应 witness 对照；新增数学推导及计算层级单独标明。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-06-response.md](original/M01-round-06-response.md) — inherited_sanitized_source
- [M02-concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md) — inherited_sanitized_source
- [M03-01_r001_r023_physical_gate_CORE.md](original/M03-01_r001_r023_physical_gate_CORE.md) — inherited_sanitized_source
- [M04-MASTER_AUDIT_PROTOCOL.md](original/M04-MASTER_AUDIT_PROTOCOL.md) — inherited_sanitized_source
- [M05-BASELINE.md](original/M05-BASELINE.md) — inherited_sanitized_source
- [M06-round-02-local-audit.md](original/M06-round-02-local-audit.md) — inherited_sanitized_source
- [M07-round-03-local-audit.md](original/M07-round-03-local-audit.md) — inherited_sanitized_source
- [M08-round-06-local-audit.md](original/M08-round-06-local-audit.md) — inherited_sanitized_source
- [M09-round-18-local-audit.md](original/M09-round-18-local-audit.md) — inherited_sanitized_source
- [M10-round-20-local-audit.md](original/M10-round-20-local-audit.md) — inherited_sanitized_source
- [M11-round-21-local-audit.md](original/M11-round-21-local-audit.md) — inherited_sanitized_source
- [M12-round-23-local-audit.md](original/M12-round-23-local-audit.md) — inherited_sanitized_source
- [R01-M01-round-06-response.md.context.md](reconciliation_sources/R01-M01-round-06-response.md.context.md) — reconciliation_source_window
- [A01-reconciliation_004_redundancy.md](reconciliation_sources/A01-reconciliation_004_redundancy.md) — supplementary_artifact

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).

## v1.1 witness repair review

旧反例违反原系统中同时存在的秩约束。

使用全部前提重新推导：遗漏的 Cauchy 下端点严格为负，已由 x≥0 蕴含。故不能在原域内用它证伪该推断。

原指控不成立；不是 witness 文件缺失。
