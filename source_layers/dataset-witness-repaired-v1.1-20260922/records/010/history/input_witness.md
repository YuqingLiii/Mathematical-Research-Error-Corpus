# Record 010 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> It is strictly smaller and more structured than the original \(D^2\) baseline phase problem:
> 
> * parameters lie on four explicit ruling lines;
> * each distinct-slope line-pair contributes at most one product to each \(K_\Delta\);
> * rank-one differences are confined to the two ruling directions;
> * every other contribution is a fully explicit nondegenerate dual chirp.
> 
> No exact solution or contradiction is obtained.

**Recorded location:** round-29-response.md, lines 1356–1363

**Context (annotation, not a source quotation):** The finite-field construction uses two paired ruling directions in the rank-one quadratic cone, represented in coordinates (a,b,c) with discriminant 4ac-b^2. The claimed restriction concerns differences between points on the chosen rulings.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Cross-ruling differences can fall in a third ruling direction.

### Argument or calculation

Over F_7, take the selected-ruling points (1,1,0) and (2,3,1). Their difference is (6,5,6)=6(1,2,1), and 4*6*6-5^2=119=0 mod 7. It lies in the rank-one ruling of slope 2, not either chosen ruling direction 0 or 1. Thus the classification of cross differences is false.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-29-response.md](original/M01-round-29-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-29-response.md")
  - Coverage: Full bundled file; source lines 1–1525.
  - Relevant location(s): round-29-response.md, lines 1356–1363; lines 1356-1363
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-29-response.md`

- [M02: concentrated_audit_2_rounds_24_42.md](original/M02-concentrated_audit_2_rounds_24_42.md "holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md")
  - Coverage: Full bundled file; source lines 1–883.
  - Relevant location(s): package F finding for M14
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md`

- [M03: MASTER_AUDIT_PROTOCOL.md](original/M03-MASTER_AUDIT_PROTOCOL.md "holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–86.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md
  - Source: `holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md`

- [M04: round-23-local-audit.md](original/M04-round-23-local-audit.md "holevo-full-size/outputs/round-23-local-audit.md")
  - Coverage: Full bundled file; source lines 1–310.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md
  - Source: `holevo-full-size/outputs/round-23-local-audit.md`
