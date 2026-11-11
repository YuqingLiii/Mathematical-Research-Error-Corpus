# 003 — The asserted uniform bound on epsilon^(-4u) is false.

**Research problem:** P01 — Channel additivity violations

## Original statement

>  m^{4u}\le e^4,qquad u^{-2}=(1+\log m)^2,qquad
>  \varepsilon^{-4u}\le C,                                    \tag{234}

**Context:** The auxiliary parameters are m=floor(gamma n epsilon^2/log^2(n epsilon^2)), u=1/(1+log m), with m>=2 and epsilon>=2/sqrt(n). The claimed C is independent of epsilon and n.

**Original locator:** Proof-development artifact, equation (234), lines 4288–4295; original write 2026-08-21T16:15:33.756Z

## Why it is an error

The asserted uniform bound on epsilon^(-4u) is false.

## Witness / evidence

Fix X>4 and gamma>0 with m=floor(gamma X/log^2 X)>=2. Set epsilon=sqrt(X/n) and let n grow. Then n epsilon^2=X and epsilon>=2/sqrt(n); m and u>0 remain fixed. But epsilon^(-4u)=(n/X)^(2u) tends to infinity. For example X=10^6 and gamma=0.01 give m=52.

## Scope

statement_false

## Classification

- III: 计算与代数错误. 统一数量级估计错误：固定 n*epsilon^2 后 m、u 不变，但 epsilon^(-4u)=(n/X)^(2u) 无界，不能吸收入与参数无关的常数。

## Adjudication notes

The asserted uniform bound on epsilon^(-4u) is false.

Fix X>4 and gamma>0 with m=floor(gamma X/log^2 X)>=2. Set epsilon=sqrt(X/n) and let n grow. Then n epsilon^2=X and epsilon>=2/sqrt(n); m and u>0 remain fixed. But epsilon^(-4u)=(n/X)^(2u) tends to infinity. For example X=10^6 and gamma=0.01 give m=52.

Scope: statement_false

固定 n·epsilon²=10^6 时 m=52，而 epsilon^(-4u) 随 n 无界；直接推翻统一常数 C。这里确认的是错误估计，不额外推定存在一项已成立的受限结果被升级。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-PROOF.md](original/M01-PROOF.md)

[Back to all 65 errors](../../README.md)
