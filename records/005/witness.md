# 005 — A discrete character-shift invariance is incorrectly extended to a continuous phase deformation, omitting derivatives of C_dep.

**Research problem:** P01 — Channel additivity violations

## Original statement

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

**Context:** The total cubic objective is C=C_dep+C_ind. The proposed continuous line-phase variation multiplies coefficients by exp(i t theta_L), where t is a balanced integer representative of a finite-field element. The displayed equations differentiate only C_ind.

**Original locator:** round-18-response.md, lines 796–829

## Why it is an error

A discrete character-shift invariance is incorrectly extended to a continuous phase deformation, omitting derivatives of C_dep.

## Witness / evidence

For odd D, set t=(D-1)/2. The same-line triple (t,t,1) sums to zero in F_D, so its cubic term belongs to C_dep. Its balanced integer sum is D, however, so the proposed continuous deformation multiplies that monomial by exp(iD theta_L), which is not constant. The gradient and Hessian of C_dep are therefore generally nonzero; equations using only C_ind are not the derivatives of the full objective. For D=5, the triple is (2,2,1).

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 把离散相位不变性沿用到连续变形，进而只对 C_ind 求导。witness 的同线单项在连续变形下含 exp(iD theta)，所以全目标驻点/Hessian 条件不能由该局部导数推出。

错误导数是错误不变性假设的后果，未单独定位另一处求导运算错误，因此不重复加 III。

## Adjudication notes

A discrete character-shift invariance is incorrectly extended to a continuous phase deformation, omitting derivatives of C_dep.

For odd D, set t=(D-1)/2. The same-line triple (t,t,1) sums to zero in F_D, so its cubic term belongs to C_dep. Its balanced integer sum is D, however, so the proposed continuous deformation multiplies that monomial by exp(iD theta_L), which is not constant. The gradient and Hessian of C_dep are therefore generally nonzero; equations using only C_ind are not the derivatives of the full objective. For D=5, the triple is (2,2,1).

Scope: argument_invalid

离散字符平移保持模 p 的关系，不保证连续相位变形不变；代表元和为 p 的项带 exp(ip theta) 相位。原论证以离散不变性支持连续变分时忽略 C_dep 的导数，属于适用范围越界。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-round-18-response.md](original/M01-round-18-response.md)
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
