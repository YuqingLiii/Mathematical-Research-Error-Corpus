# Record 006 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> Consequently,
> 
> $$
> \begin{aligned}
> \mathbb E_{s,t}
> \langle\Delta_{L,s}\Theta_{M,t}\rangle
> &=
> \langle\overline\Delta\,\overline\Theta\rangle\\
> &=
> \sum_{k,j}
> \left(\frac1D-p_k\right)
> \left(\frac1D-r_j\right)
> \mathcal B_{kj}.
> \end{aligned}
> \tag{6.1}
> $$
> 
> The phases of \(\mathcal B_{kj}\) remain. The higher terms in
> `TwoLinePlaquette` similarly retain three- and four-point Bargmann data.
> 
> Thus neither the four-corner subtraction nor the full uniform average over the two cyclic shifts reduces the two-line condition to the two autocorrelation shadows.
> 
> A phase-free two-line contradiction is not obtained.

Context: Delta and Theta are perturbations from shifting two stabilizer lines. The full TwoLinePlaquette expression contains a bilinear term and higher-order terms. The excerpt computes only the bilinear average explicitly.

Locator: round-20-response.md, lines 653–675

## 2. Witness / adjudication

Phase dependence of one averaged summand does not prove phase dependence of the complete averaged expression.

The source evaluates E<Delta Theta>=sum_(k,j)(1/D-p_k)(1/D-r_j) B_(kj), then says the higher terms “similarly retain” phase data without evaluating their sum. A full expression F1(theta)+F2(theta) can be phase-independent even when F1 is not (take F2=-F1+c). Therefore the displayed partial calculation does not imply the claimed noncancellation for TwoLinePlaquette. A complete average, or a coefficient that provably survives the complete sum, is required.

Scope: argument_invalid

某个平均后求和项依赖相位，不推出全部项之和依赖相位，因为可以相消。witness 只击中这一步推理，不证明实际总和必定不变；按本轮口径属于直接无效推断，不自动记为 overclaim。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-20-response.md](original/M01-round-20-response.md) — inherited_sanitized_source
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

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
