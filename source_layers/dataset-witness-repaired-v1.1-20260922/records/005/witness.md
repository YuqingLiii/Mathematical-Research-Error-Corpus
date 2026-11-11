# Record 005 — Channel additivity violations

**Final admission:** included. **Overclaim:** yes.

## 1. Original statement and context

> Choose balanced integer representatives of the three field coefficients \(t_u,t_v,t_w\), and let \(q_T\) be the corresponding vector in the real line-coordinate space. A continuous fixed-magnitude line-phase variation has
> 
> $$
> C_{\rm ind}(\theta)
> =
> 2\sum_T
> \operatorname{Re}
> \left(
> A_Te^{i\langle q_T,\theta\rangle}
> \right).
> $$
> 
> If \(C=1\), then the coefficient field is physical and gives a global maximum of \(C\) on the entire phase torus. Hence
> 
> $$
> \boxed{
> \sum_Tq_T\,\operatorname{Im}A_T=0,
> }
> \tag{10.1}
> $$
> 
> and
> 
> $$
> \boxed{
> \sum_T
> (\operatorname{Re}A_T)\,
> q_Tq_T^{\mathsf T}
> \succeq0.
> }
> \tag{10.2}
> $$
> 
> These are the exact stationarity and Hessian conditions.

Context: The total cubic objective is C=C_dep+C_ind. The proposed continuous line-phase variation multiplies coefficients by exp(i t theta_L), where t is a balanced integer representative of a finite-field element. The displayed equations differentiate only C_ind.

Locator: round-18-response.md, lines 796–829

## 2. Witness / adjudication

A discrete character-shift invariance is incorrectly extended to a continuous phase deformation, omitting derivatives of C_dep.

For odd D, set t=(D-1)/2. The same-line triple (t,t,1) sums to zero in F_D, so its cubic term belongs to C_dep. Its balanced integer sum is D, however, so the proposed continuous deformation multiplies that monomial by exp(iD theta_L), which is not constant. The gradient and Hessian of C_dep are therefore generally nonzero; equations using only C_ind are not the derivatives of the full objective. For D=5, the triple is (2,2,1).

Scope: argument_invalid

离散字符平移保持模 p 的关系，不保证连续相位变形不变；代表元和为 p 的项带 exp(ip theta) 相位。原论证以离散不变性支持连续变分时忽略 C_dep 的导数，属于适用范围越界。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-18-response.md](original/M01-round-18-response.md) — inherited_sanitized_source
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
