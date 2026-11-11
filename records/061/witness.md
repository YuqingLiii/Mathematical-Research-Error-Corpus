# 061 — A valid but strictly dominated Haar bound is advertised as an additional necessary scalar obstruction.

**Research problem:** P01 — Channel additivity violations

## Original statement

> # 6. New full-Schmidt-rank obstruction
> 
> The following lemma goes beyond rank-one inputs, a single Bell input, and the universal \(m-1\) estimate.
> 
> [...]
> 
> \boxed{
> m\alpha_U^2
> -
> AD^2\alpha_U
> +
> D^2(m-A)
> \le0.
> }
> \tag{HC}
> $$
> 
> This is a new necessary scalar condition.

**Context:** The source presents HC as a new scalar obstruction beyond the rank-one lower bound. The correction distinguishes this strength claim from the valid full-rank inequality and witness.

**Original locator:** reconciliation_sources/W11-round-03-response.md:912–914,1197–1208; W11-round-04-response.md:1–11 and section A.

## Why it is an error

The existing one-copy rank-one condition strictly implies HC throughout the claimed feasible regime; HC supplies no additional scalar exclusion.

## Witness / evidence

The target of this witness is the advertised additional scalar obstruction, not the truth of the Haar lower bound or the existence of a full-Schmidt-rank witness. In section 7, the source calls HC a "new necessary scalar condition" after presenting it as progress beyond the rank-one bound; the next response explicitly retracts that scalar-obstruction claim while retaining the inequality.

Write alpha=||C(I_D)||_2^2. Rank-one Haar averaging gives q_pure=(alpha+D)/(D(D+1)); the one-copy assumption p_1(C)<=A/m already implies m*q_pure<=A. The claimed full-rank average is q_full=(alpha^2+D^2)/(D^2(alpha+1)). Exact subtraction gives

q_pure-q_full = ((alpha-D)(D^2-alpha))/(D^2(D+1)(alpha+1)).

The relevant domain is not assumed without proof. In the low-A feasible regime, m>exp(18) and A^2<m^(1/m). In particular m>=10 and A<5/4: log(m)/m is decreasing for m>=10 and (5/4)^20>10. Thus A<2m/(m+1). Since C(I_D/D) is an m-dimensional density matrix, alpha>=D^2/m. Combining this with m*q_pure<=A yields (m-A)<=D(A-1), hence D>m. Consequently alpha>D. The same scalar bound yields alpha<=A*D(D+1)/m-D<A*D^2/m<D^2 (using A<m). The displayed difference is therefore strictly positive throughout the feasible domain.

It follows that m*q_full < m*q_pure <= A. Multiplying out m*q_full<=A gives precisely HC: m*alpha^2-A*D^2*alpha+D^2*(m-A)<=0. HC excludes no additional scalar candidates beyond the already required rank-one condition in this regime. Calling it an additional necessary scalar obstruction overstates what the derived bound establishes.

This is a claim about relative constraint strength inside the specified feasible domain, not a literature-wide novelty judgment. A different full-rank witness may still be mathematically interesting, and the inequality itself remains valid. If "new" were only a statement about deriving a differently written true formula, redundancy would not refute that narrower claim. The source's obstruction/progress framing and its subsequent explicit retraction determine the narrower, record-specific target used here.

## Scope

overstated_additional_scalar_constraint_not_false_inequality

## Classification

- IV: 逻辑推理错误. 真不等式 HC 在指定可行域内已由旧 rank-one 条件严格蕴含，不能提供所称额外标量排除能力；只标约束强弱推断，不标一般文献新颖性。

标签只针对记录已限定的约束强弱声明，不扩大成 HC 为假或一般意义的“不新颖”。

## Original materials

- [original/M01-round-03-response.md](original/M01-round-03-response.md)
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
- [original/context/A01-witness.md](original/context/A01-witness.md)
- [original/context/W11-round-03-response.md](original/context/W11-round-03-response.md)
- [original/context/W11-round-04-response.md](original/context/W11-round-04-response.md)

[Back to all 65 errors](../../README.md)
