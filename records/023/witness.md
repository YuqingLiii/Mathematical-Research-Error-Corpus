# 023 — The proposed second basis vector is not in the complementary-output kernel for the script’s own canonical input.

**Research problem:** P02 — Werner–Holevo zero-capacity boundary

## Original statement

>     # environment kernel: analytic basis  (0, conj(u+iv)) and (1, -i kappa w),
>     # kappa = sqrt(2(1-x)/x); verified below to be a basis of ker Lambda^c(P_psi).
>     kappa = sp.sqrt(2 * (1 - x) / x)
>     k1 = sp.Matrix([0, *list(sp.simplify(sp.sqrt(2) * psi_bar))])
>     k2 = sp.Matrix([1, *list(sp.simplify(-sp.I * kappa * third))])
>     analytic_kernel_pass = zero_matrix(lamc_p * k1) and zero_matrix(lamc_p * k2)
>     analytic_kernel_orthogonal = zero((k1.H * k2)[0, 0])
>     pi_e = sp.simplify(projector(k1) + projector(k2))

**Context:** The script later instantiates psi=(0,1,-i)/sqrt(2) and third=(1,0,0). It labels third as the oriented cross product and uses the displayed formula for an environment-kernel basis. This release excerpt isolates the concrete basis defect from the legacy record, which also mentioned separate sign corrections.

**Original locator:** Preserved isotropic weight-operator script, function weight_operators, lines 92–101

## Why it is an error

The proposed second basis vector is not in the complementary-output kernel for the script’s own canonical input.

## Witness / evidence

Let kappa=sqrt(2(1-x)/x). For the script’s psi and Kraus convention, the complementary output has entries G00=1-x, G01=i sqrt(x(1-x)/2), G10=-i sqrt(x(1-x)/2), and G11=x/2. Its proposed k2=(1,-i kappa,0,0) gives G k2=(2(1-x),-i sqrt(2x(1-x)),0,0), nonzero for 0<x<1. At x=1/2 the residual is (1,-i/sqrt(2),0,0). Therefore the constructed projector and resulting weight operator are wrong. The archived script reports d1=1-x, whereas the corrected operator gives (1-x)(2-5x)/(2-x), equal to -11/124 at x=9/20 instead of 11/20.

## Scope

computation_false

## Classification

- III: 计算与代数错误. 核向量符号错误。按脚本 Kraus 约定直接相乘得到 G*k2 非零，导致后续投影与权算子计算错误。

## Adjudication notes

The proposed second basis vector is not in the complementary-output kernel for the script’s own canonical input.

Let kappa=sqrt(2(1-x)/x). For the script’s psi and Kraus convention, the complementary output has entries G00=1-x, G01=i sqrt(x(1-x)/2), G10=-i sqrt(x(1-x)/2), and G11=x/2. Its proposed k2=(1,-i kappa,0,0) gives G k2=(2(1-x),-i sqrt(2x(1-x)),0,0), nonzero for 0<x<1. At x=1/2 the residual is (1,-i/sqrt(2),0,0). Therefore the constructed projector and resulting weight operator are wrong. The archived script reports d1=1-x, whereas the corrected operator gives (1-x)(2-5x)/(2-x), equal to -11/124 at x=9/20 instead of 11/20.

Scope: computation_false

将脚本自己的 k2 代入互补输出矩阵，在 x=1/2 得非零残差 (1,-i/sqrt(2),0,0)。核投影器错误，不需要依靠后续地位升级来确认。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-whgap_p6b_v2_isotropic.py](original/M01-whgap_p6b_v2_isotropic.py)
- [original/M03-v2_isotropic.json](original/M03-v2_isotropic.json)
- [original/M04-whgap_p6b_v2_fable.py](original/M04-whgap_p6b_v2_fable.py)
- [original/M05-DATA5_whgap_ledger.md](original/M05-DATA5_whgap_ledger.md)

[Back to all 65 errors](../../README.md)
