# 006 — Phase dependence of one averaged summand does not prove phase dependence of the complete averaged expression.

**Research problem:** P01 — Channel additivity violations

## Original statement

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

**Context:** Delta and Theta are perturbations from shifting two stabilizer lines. The full TwoLinePlaquette expression contains a bilinear term and higher-order terms. The excerpt computes only the bilinear average explicitly.

**Original locator:** round-20-response.md, lines 653–675

## Why it is an error

Phase dependence of one averaged summand does not prove phase dependence of the complete averaged expression.

## Witness / evidence

The source evaluates E<Delta Theta>=sum_(k,j)(1/D-p_k)(1/D-r_j) B_(kj), then says the higher terms “similarly retain” phase data without evaluating their sum. A full expression F1(theta)+F2(theta) can be phase-independent even when F1 is not (take F2=-F1+c). Therefore the displayed partial calculation does not imply the claimed noncancellation for TwoLinePlaquette. A complete average, or a coefficient that provably survives the complete sum, is required.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 只算出双线性项的相位依赖，就断言完整平均仍有相位依赖；没有排除高阶项抵消。缺的是全和不消去的推断，不是已展示加法算错。

## Adjudication notes

Phase dependence of one averaged summand does not prove phase dependence of the complete averaged expression.

The source evaluates E<Delta Theta>=sum_(k,j)(1/D-p_k)(1/D-r_j) B_(kj), then says the higher terms “similarly retain” phase data without evaluating their sum. A full expression F1(theta)+F2(theta) can be phase-independent even when F1 is not (take F2=-F1+c). Therefore the displayed partial calculation does not imply the claimed noncancellation for TwoLinePlaquette. A complete average, or a coefficient that provably survives the complete sum, is required.

Scope: argument_invalid

某个平均后求和项依赖相位，不推出全部项之和依赖相位，因为可以相消。witness 只击中这一步推理，不证明实际总和必定不变；按本轮口径属于直接无效推断，不自动记为 overclaim。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-round-20-response.md](original/M01-round-20-response.md)
- [original/M02-concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md)
- [original/M03-01_r001_r023_physical_gate_CORE.md](original/M03-01_r001_r023_physical_gate_CORE.md)
- [original/M04-MASTER_AUDIT_PROTOCOL.md](original/M04-MASTER_AUDIT_PROTOCOL.md)
- [original/M05-BASELINE.md](original/M05-BASELINE.md)
- [original/M06-round-02-local-audit.md](original/M06-round-02-local-audit.md)
- [original/M07-round-03-local-audit.md](original/M07-round-03-local-audit.md)
- [original/M08-round-06-local-audit.md](original/M08-round-06-local-audit.md)
- [original/M09-round-18-local-audit.md](original/M09-round-18-local-audit.md)
- [original/M10-round-20-local-audit.md](original/M10-round-20-local-audit.md)
- [original/M11-round-21-local-audit.md](original/M11-round-21-local-audit.md)
- [original/M12-round-23-local-audit.md](original/M12-round-23-local-audit.md)

[Back to all 65 errors](../../README.md)
