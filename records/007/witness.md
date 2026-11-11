# 007 — A positive finite-M correction factor was discarded when simplifying the upper bound.

**Research problem:** P01 — Channel additivity violations

## Original statement

> \boxed{
> |\alpha_z\mathcal R_{\mathbf1_\Gamma}(z)|
> \le
> \sqrt8\,D
> \sqrt{\lambda_z^2+M^2+6M}
> <4DM,
> }
> \tag{8.5}

**Context:** D>0, M>0, and the stated scalar premise is |lambda_z|<=M. The last strict inequality is a simplification of an upper envelope, not a separately proved estimate.

**Original locator:** round-21-response.md, lines 1253–1260

## Why it is an error

A positive finite-M correction factor was discarded when simplifying the upper bound.

## Witness / evidence

Substituting the allowed endpoint |lambda_z|=M gives sqrt(8)D sqrt(2M^2+6M)=4DM sqrt(1+3/M)>4DM for every finite M>0. Thus the stated premise yields only the larger envelope, and cannot justify the strict inequality printed in (8.5).

## Scope

statement_false

## Classification

- III: 计算与代数错误. 把显式上包络化简成了更小的数值界。代入允许的 |lambda|=M，左边等于 4DM*sqrt(1+3/M)>4DM。

## Adjudication notes

A positive finite-M correction factor was discarded when simplifying the upper bound.

Substituting the allowed endpoint |lambda_z|=M gives sqrt(8)D sqrt(2M^2+6M)=4DM sqrt(1+3/M)>4DM for every finite M>0. Thus the stated premise yields only the larger envelope, and cannot justify the strict inequality printed in (8.5).

Scope: statement_false

M=D=1 时保留项给出的量为 8，而删项后的界为 4，简化不成立。这是界的代数处理错误，不据此另算范围扩张。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-round-21-response.md](original/M01-round-21-response.md)
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
