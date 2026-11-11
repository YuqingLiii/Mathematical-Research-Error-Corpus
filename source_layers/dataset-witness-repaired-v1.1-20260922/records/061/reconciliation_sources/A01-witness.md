# Record 061 — Channel additivity violations

**Review status:** `interpretation_check_pending`.

Redundancy of a true scalar lower bound is not automatically a mathematical error; verify that an asserted strict-strength comparison is actually false.

## Original statement and context

> A new deterministic obstruction is proved below: averaging over **full-Schmidt-rank** inputs gives
> 
> $$
> \boxed{
> \kappa_1(U)\ge
> \frac{m\bigl(\alpha_U^2+D^2\bigr)}
>      {D^2(\alpha_U+1)}-1,
> \qquad
> \alpha_U:=\|C(I_D)\|_2^2.
> }
> \tag{Haar-LB}
> 
> [...]
> 
> # 6. New full-Schmidt-rank obstruction
> 
> The following lemma goes beyond rank-one inputs, a single Bell input, and the universal \(m-1\) estimate.
> 
> [...]
> 
> This obstruction is genuinely entangled: its witness can be chosen full Schmidt rank. It is not a reformulation of the product lower bound
> 
> $$
> \kappa_1(U)\ge mp-1.
> $$
> 
> The obstruction still does not disprove \((E1_{\rm gap})\). For sufficiently large finite \(D\), the scalar interval (7.1) can intersect the quadratic interval (7.5). The remaining pointwise double-centered condition \((DC)\) is not settled by this average argument.

**Recorded location:** round-03-response.md, lines 33–43, 912–914, 1296–1302

**Context (annotation, not a source quotation):** For a deterministic unitary tuple U, alpha=||C(I_D)||_2^2. The response contrasts a full-Schmidt-rank Haar lower bound with the rank-one/product lower bound and describes a new scalar obstruction.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

The full-rank Haar scalar condition is dominated by a rank-one scalar condition in the relevant low-A range. Whether “new” asserts stronger mathematical content rather than merely a different witness needs adjudication.

### Argument or calculation

Let q_pure=(alpha+D)/(D(D+1)) and q_full=(alpha^2+D^2)/(D^2(alpha+1)). Direct subtraction gives q_pure-q_full=((alpha-D)(D^2-alpha))/(D^2(D+1)(alpha+1))>=0 for D<=alpha<=D^2. Hence the full-rank condition adds no stronger scalar obstruction in that range. The inequality and the existence of a full-rank witness may still be correct; redundancy alone does not refute either.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-03-response.md](original/M01-round-03-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-03-response.md")
  - Coverage: Full bundled file; source lines 1–1387.
  - Relevant location(s): round-03-response.md, lines 33–43, 912–914, 1296–1302; lines 33-43, 912-933, 1208, 1296-1302
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-03-response.md`

- [M02: concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md "holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md")
  - Coverage: Full bundled file; source lines 1–585.
  - Relevant location(s): package F finding for M02
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md`

- [M03: 01_r001_r023_physical_gate_CORE.md](original/M03-01_r001_r023_physical_gate_CORE.md "holevo-full-size/central-audit-2026-09-18/generated/01_r001_r023_physical_gate_CORE.md")
  - Coverage: Full bundled file; source lines 1–45578.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/central-audit-2026-09-18/generated/01_r001_r023_physical_gate_CORE.md`

- [M04: MASTER_AUDIT_PROTOCOL.md](original/M04-MASTER_AUDIT_PROTOCOL.md "holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–86.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md`

- [M05: BASELINE.md](original/M05-BASELINE.md "holevo-full-size/central-audit-2026-09-18/BASELINE.md")
  - Coverage: Full bundled file; source lines 1–89.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/central-audit-2026-09-18/BASELINE.md`

- [M06: round-02-local-audit.md](original/M06-round-02-local-audit.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-02-local-audit.md")
  - Coverage: Full bundled file; source lines 1–190.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-02-local-audit.md`

- [M07: round-03-local-audit.md](original/M07-round-03-local-audit.md "holevo-full-size/outputs/round-03-local-audit.md")
  - Coverage: Full bundled file; source lines 1–216.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/outputs/round-03-local-audit.md`

- [M08: round-06-local-audit.md](original/M08-round-06-local-audit.md "holevo-full-size/outputs/round-06-local-audit.md")
  - Coverage: Full bundled file; source lines 1–130.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/outputs/round-06-local-audit.md`

- [M09: round-18-local-audit.md](original/M09-round-18-local-audit.md "holevo-full-size/outputs/round-18-local-audit.md")
  - Coverage: Full bundled file; source lines 1–338.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/outputs/round-18-local-audit.md`

- [M10: round-20-local-audit.md](original/M10-round-20-local-audit.md "holevo-full-size/outputs/round-20-local-audit.md")
  - Coverage: Full bundled file; source lines 1–202.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/outputs/round-20-local-audit.md`

- [M11: round-21-local-audit.md](original/M11-round-21-local-audit.md "holevo-full-size/outputs/round-21-local-audit.md")
  - Coverage: Full bundled file; source lines 1–224.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/outputs/round-21-local-audit.md`

- [M12: round-23-local-audit.md](original/M12-round-23-local-audit.md "holevo-full-size/outputs/round-23-local-audit.md")
  - Coverage: Full bundled file; source lines 1–310.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md
  - Source: `holevo-full-size/outputs/round-23-local-audit.md`
