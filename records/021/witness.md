# 021 — The environment-support restriction can force phi=|psi><psi|, so the assumed nontrivial comparison domain does not exist.

**Research problem:** P02 — Werner–Holevo zero-capacity boundary

## Original statement

> - D1 (derivation check, exact): verify the pure-output spectra claims symbolically; verify
>   the epsilon-expansion bookkeeping NUMERICALLY at high precision: for random (psi, phi)
>   kernel-avoiding pairs at x = 9/20, fit Ic((1-eps)psi + eps phi) against
>   c1*eps + O(eps^2 log eps) and confirm the fitted c1 matches
>   `-Tr[Λ(phi-psi) log Λ(psi)] + Tr[Λ^c(phi-psi) log Λ^c(psi)]` to >= 8 digits; also confirm
>   kernel-HITTING phi produce the -eps log(1/eps) plunge. GATE G0.
> 
> [...]
> 
>   over pure psi and kernel-avoiding states phi (parameterize phi on the 3-dim support
>   constraint; >= 150 restarts). A_1 > 0 anywhere

**Context:** The proposed first-order test requires a distinct comparison state phi satisfying supp Lambda_x^c(phi) subset supp Lambda_x^c(psi). It treats this as a three-dimensional domain from which random kernel-avoiding pairs can be drawn.

**Original locator:** Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522

## Why it is an error

The environment-support restriction can force phi=|psi><psi|, so the assumed nontrivial comparison domain does not exist.

## Witness / evidence

For psi=|0> and 0<x<1, use Kraus operators K0=sqrt(1-x)I and K_(mu+1)=sqrt(x/2)A_mu, (A_mu)_(jk)=epsilon_(mu j k). The complementary output has kernel vector z=(0,1,0,0). Positivity and support inclusion imply Tr(K1 phi K1^dagger)=0, hence supp(phi) subset ker K1=span{|0>}. Since phi has trace one it equals |0><0|. The claimed random distinct-pair construction therefore fails already in this exact instance; generic tests in the recorded check also had one-dimensional allowed support.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 所选探索路线假定存在非平凡 kernel-avoiding 扰动态域，但支撑条件在精确例子中强制 phi=psi；因此所宣称的随机不同对构造不可行。

## Adjudication notes

The environment-support restriction can force phi=|psi><psi|, so the assumed nontrivial comparison domain does not exist.

For psi=|0> and 0<x<1, use Kraus operators K0=sqrt(1-x)I and K_(mu+1)=sqrt(x/2)A_mu, (A_mu)_(jk)=epsilon_(mu j k). The complementary output has kernel vector z=(0,1,0,0). Positivity and support inclusion imply Tr(K1 phi K1^dagger)=0, hence supp(phi) subset ker K1=span{|0>}. Since phi has trace one it equals |0><0|. The claimed random distinct-pair construction therefore fails already in this exact instance; generic tests in the recorded check also had one-dimensional allowed support.

Scope: argument_invalid

psi=|0> 时环境支撑约束与正性迫使 phi=|0><0|，不存在要求的不同随机配对。错误在试验/构造所假定的非平凡可行域，不在一个已完成容量定理。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M02-whgap_p9_necessary_20260729.md](original/M02-whgap_p9_necessary_20260729.md)
- [original/M04-whgap_p9_g0.py](original/M04-whgap_p9_g0.py)
- [original/M05-whgap_p9_distillation.py](original/M05-whgap_p9_distillation.py)

[Back to all 65 errors](../../README.md)
