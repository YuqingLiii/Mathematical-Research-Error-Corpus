# 008 — For the alternating symplectic kernel, squaring the transform gives the identity, not reflection.

**Research problem:** P01 — Channel additivity violations

## Original statement

> The Fourier \(+1\) property implies the evenness independently because \(\mathscr F^2\) is phase-space reflection.

**Context:** The transform is the normalized symplectic Fourier transform (Ff)(k)=D^(-1) sum_p f(p) omega^[p,k] on F_D^2, where [p,k] is alternating and omega is a primitive Dth root of unity.

**Original locator:** round-23-response.md, lines 234

## Why it is an error

For the alternating symplectic kernel, squaring the transform gives the identity, not reflection.

## Witness / evidence

Compute F^2 f(l)=D^(-2) sum_(p,k) f(p) omega^([p,k]+[k,l]). Since [k,l]=-[l,k], the exponent is [p-l,k]. Character orthogonality makes the inner sum D^2 when p=l and zero otherwise, so F^2 f(l)=f(l). It does not give f(-l). Evenness must be justified separately.

## Scope

statement_false

## Classification

- II: 数学知识错误. 把当前交替辛 Fourier 变换的平方说成反射；按已给定义其平方为恒等。这是可见的变换性质错述，而不是已定位到某次数值运算。

II/III 边界：原文给出的是变换性质断言，没有展示出错的平方运算步骤，按可见性质错述归 II；不能据此断言模型内部记忆失误。 2026-09-23 核对原响应后，仍未见 F^2=反射这一错误前提的推导，保持 II。

## Adjudication notes

For the alternating symplectic kernel, squaring the transform gives the identity, not reflection.

Compute F^2 f(l)=D^(-2) sum_(p,k) f(p) omega^([p,k]+[k,l]). Since [k,l]=-[l,k], the exponent is [p-l,k]. Character orthogonality makes the inner sum D^2 when p=l and zero otherwise, so F^2 f(l)=f(l). It does not give f(-l). Evenness must be justified separately.

Scope: statement_false

交替辛核中两次变换的指数是 [p-l,k]，字符正交性给 F²f(l)=f(l)，不是 f(-l)。因此所述偶性推导无效，偶性是否另有证明不在此条判定内。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-round-23-response.md](original/M01-round-23-response.md)
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
