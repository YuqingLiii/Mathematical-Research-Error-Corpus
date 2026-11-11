# Record 011 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> 
> 1. the exceptional sequence \(T_\nu\);
> 2. ordinary coordinate magnitudes \(B\);
> 3. central evenness;
> 4. an ordinary support allowance of \(P_{\rm Sid}\) slots per \(\nu\);
> 5. total ordinary \(\ell_2\) energy \(\mathcal E_{\rm ord}\).
> 
> For each \(\nu\), distribute the required cancellation equally over the available ordinary slots. The minimum ordinary coefficient energy needed to cancel the exceptional term is
> 
> $$
> \frac{D+1}{P_{\rm Sid}}|T_\nu|^2.
> $$
> 
> Summed over \(\nu\),
> 
> $$
> \mathcal E_{\min}
> =
> \frac{D+1}{P_{\rm Sid}}\mathcal E_T.
> $$
> 
> [...]
> 
> Hence
> 
> $$
> \mathcal E_{\rm ord}
> \ge
> \frac{D-2}{4}\mathcal E_T
> >
> \frac{D+1}{P_{\rm Sid}}\mathcal E_T.
> $$
> 
> The remaining ordinary energy can be added in coefficient pairs whose physical contributions cancel identically.
> 
> Thus there is an abstract magnitude-compatible, centrally even coefficient relaxation satisfying:
> 
> * every scalar mirror equation;
> * the exact exceptional energy;
> * the exact ordinary total \(\ell_2\) energy;
> * the same support allowance.
> 
> It need not come from cofactor cross-correlations and need not satisfy the global Fourier-\(+1\) phase equations. Therefore:

**Recorded location:** round-37-response.md, lines 1044–1063, 1081–1100

**Context (annotation, not a source quotation):** The proposed relaxation fixes exceptional coefficients, ordinary magnitude constraints, central evenness, a support allowance per frequency, and one total squared-norm budget. The response infers existence of a compatible coefficient assignment from an aggregate energy comparison.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

An aggregate energy budget does not by itself construct coefficients obeying all the retained local magnitude, support, and symmetry constraints.

### Argument or calculation

The comparison E_ord>=(D-2)E_T/4 > (D+1)E_T/P_Sid is only an aggregate energy inequality. The proposed construction must additionally specify allowed coefficient positions, obey each magnitude constraint and central-even pairing, and solve every mirror equation simultaneously. The excerpt gives neither a compatible assignment nor an argument that adding cancelling pairs preserves the already used support and magnitude constraints. Thus the stated existence of the full relaxation is not established by the scalar energy calculation.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-37-response.md](original/M01-round-37-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-37-response.md")
  - Coverage: Full bundled file; source lines 1–1429.
  - Relevant location(s): round-37-response.md, lines 1044–1063, 1081–1100; lines 1044-1102
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-37-response.md`

- [M02: concentrated_audit_2_rounds_24_42.md](original/M02-concentrated_audit_2_rounds_24_42.md "holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md")
  - Coverage: Full bundled file; source lines 1–883.
  - Relevant location(s): package F finding for M15
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md`

- [M03: MASTER_AUDIT_PROTOCOL.md](original/M03-MASTER_AUDIT_PROTOCOL.md "holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–86.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md
  - Source: `holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md`

- [M04: round-23-local-audit.md](original/M04-round-23-local-audit.md "holevo-full-size/outputs/round-23-local-audit.md")
  - Coverage: Full bundled file; source lines 1–310.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md
  - Source: `holevo-full-size/outputs/round-23-local-audit.md`
