# Record 005 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> Choose balanced integer representatives of the three field coefficients \(t_u,t_v,t_w\), and let \(q_T\) be the corresponding vector in the real line-coordinate space. A continuous fixed-magnitude line-phase variation has
> 
> $$
> C_{\rm ind}(\theta)
> =
> 2\sum_T
> \operatorname{Re}
> \left(
> A_Te^{i\langle q_T,\theta\rangle}
> \right).
> $$
> 
> If \(C=1\), then the coefficient field is physical and gives a global maximum of \(C\) on the entire phase torus. Hence
> 
> $$
> \boxed{
> \sum_Tq_T\,\operatorname{Im}A_T=0,
> }
> \tag{10.1}
> $$
> 
> and
> 
> $$
> \boxed{
> \sum_T
> (\operatorname{Re}A_T)\,
> q_Tq_T^{\mathsf T}
> \succeq0.
> }
> \tag{10.2}
> $$
> 
> These are the exact stationarity and Hessian conditions.

**Recorded location:** round-18-response.md, lines 796–829

**Context (annotation, not a source quotation):** The total cubic objective is C=C_dep+C_ind. The proposed continuous line-phase variation multiplies coefficients by exp(i t theta_L), where t is a balanced integer representative of a finite-field element. The displayed equations differentiate only C_ind.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

A discrete character-shift invariance is incorrectly extended to a continuous phase deformation, omitting derivatives of C_dep.

### Argument or calculation

For odd D, set t=(D-1)/2. The same-line triple (t,t,1) sums to zero in F_D, so its cubic term belongs to C_dep. Its balanced integer sum is D, however, so the proposed continuous deformation multiplies that monomial by exp(iD theta_L), which is not constant. The gradient and Hessian of C_dep are therefore generally nonzero; equations using only C_ind are not the derivatives of the full objective. For D=5, the triple is (2,2,1).

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-18-response.md](original/M01-round-18-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-18-response.md")
  - Coverage: Full bundled file; source lines 1–1298.
  - Relevant location(s): round-18-response.md, lines 796–829; lines 796-832
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-18-response.md`

- [M02: concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md "holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md")
  - Coverage: Full bundled file; source lines 1–585.
  - Relevant location(s): package F finding for M04
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
