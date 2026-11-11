# 002 — The self-pair tensor identity does not apply to a conjugate pair.

**Research problem:** P01 — Channel additivity violations

## Original statement

> This explains why simply tensoring a single Hastings counterexample with
> itself cannot settle the extensive question.

**Context:** Lemma 4 proves a zero normalized tensor-power gap for a literal self-pair (Phi,Phi). The following explanatory sentence extends its interpretation to a Hastings counterexample, which generally uses the distinct conjugate pair (Phi,conjugate(Phi)).

**Original locator:** Proof-development artifact, section 2, lines 150–151; original write 2026-08-20T23:41:57.547Z

## Why it is an error

The self-pair tensor identity does not apply to a conjugate pair.

## Witness / evidence

For a_m=S_min(Phi^tensor m), the self-pair gap is 2a_m-a_2m and its ratio to m tends to zero. For a conjugate pair the joint term is S_min((Phi tensor conjugate(Phi))^tensor m), not a_2m. Its normalized limit is a different regularized entropy and the cancellation used in Lemma 4 is unavailable.

## Scope

argument_invalid

## Classification

- IV: 逻辑推理错误. 关于自配对 (Phi,Phi) 的消去引理被用于共轭配对 (Phi,bar Phi)。后者的联合熵不是 a_2m，故引理的适用对象不满足原前提。

不把对象不同自动再计 II：这里可直接定位的是把一个正确引理应用到不满足对象前提的情形。

## Adjudication notes

The self-pair tensor identity does not apply to a conjugate pair.

For a_m=S_min(Phi^tensor m), the self-pair gap is 2a_m-a_2m and its ratio to m tends to zero. For a conjugate pair the joint term is S_min((Phi tensor conjugate(Phi))^tensor m), not a_2m. Its normalized limit is a different regularized entropy and the cancellation used in Lemma 4 is unavailable.

Scope: argument_invalid

恢复旧确认：自配对恒等式不能覆盖共轭信道对。原文纠正明确指向原 self-tensor 排除句，并给出共轭情形仍未排除的正则化差。

原始写入与定向纠正均已恢复；不再用本轮对单句的歧义取代完整时间链。与001同一事件相关但错误推断不同，不算独立运行。

## Original materials

- [original/M01-PROOF.md](original/M01-PROOF.md)
- [original/context/R01-PROOF.md.context.md](original/context/R01-PROOF.md.context.md)

[Back to all 65 errors](../../README.md)
