# 001 — Necessity for the particular localization proof is not necessity for every construction.

**Research problem:** P01 — Channel additivity violations

## Original statement

> The entire problem is therefore to choose *different* tuples \(U^{(r)}\) so
> that entangled inputs within \(\mathcal R^{[k]}\) do not appreciably lower its
> minimum output entropy.

**Context:** The argument uses different finite unitary tuples at different tensor positions to control minimum output entropy by iterated localization. The selected sentence presents this route choice as necessary for the entire extensive-gap problem.

**Original locator:** Proof-development artifact, section 3, lines 211–213; original write 2026-08-20T23:41:57.547Z

## Why it is an error

Necessity for the particular localization proof is not necessity for every construction.

## Witness / evidence

For any fixed channel pair (Phi,Psi), the normalized tensor-power gap tends to Sbar_min(Phi)+Sbar_min(Psi)-Sbar_min(Phi tensor Psi). For Psi=conjugate(Phi), this is 2 Sbar_min(Phi)-Sbar_min(Phi tensor conjugate(Phi)), which the localization argument does not show to be zero. Thus the derivation leaves a fixed-pair alternative unexcluded. This diagnoses an unsupported necessity inference; it does not establish that a positive fixed-pair regularized gap exists.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 某一 localization 路线需要不同 tuple，不推出整个问题的所有可行路线都必须使用不同 tuple；witness 指出固定共轭对的正则化间隙并未被排除。

## Adjudication notes

Necessity for the particular localization proof is not necessity for every construction.

For any fixed channel pair (Phi,Psi), the normalized tensor-power gap tends to Sbar_min(Phi)+Sbar_min(Psi)-Sbar_min(Phi tensor Psi). For Psi=conjugate(Phi), this is 2 Sbar_min(Phi)-Sbar_min(Phi tensor conjugate(Phi)), which the localization argument does not show to be zero. Thus the derivation leaves a fixed-pair alternative unexcluded. This diagnoses an unsupported necessity inference; it does not establish that a positive fixed-pair regularized gap exists.

Scope: argument_invalid

恢复旧确认：同一来源的 dated correction 明确限定不同 tuples 只对所给 iterated-localization 路线必要，并指名原“entire problem”过强；这不是假设全局替代路线已成功，而是该必要性推断没有成立。

上一轮把路线措辞当孤立歧义，遗漏原文对同一句的定向纠正以及固定共轭对的精确公式。恢复为论证范围错误，不称全局定理已被反例推翻。

## Original materials

- [original/M01-PROOF.md](original/M01-PROOF.md)
- [original/context/R01-PROOF.md.context.md](original/context/R01-PROOF.md.context.md)

[Back to all 65 errors](../../README.md)
