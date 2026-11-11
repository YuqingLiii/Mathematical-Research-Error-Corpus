# Record 009 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> At \(|T|=777716\), this is the first undecided finite determinant/kernel system. The dictionary has at most
> 
> $$
> r_1^2+r_1+1
> =
> 970353651
> $$
> 
> columns, but the coefficient vector has the special nonlinear form (8.2). Merely proving \(G_T\) singular would be necessary, not sufficient: its kernel must contain a vector with that exact conjugate-quadratic structure.

**Recorded location:** round-28-response.md, lines 725–733

**Context (annotation, not a source quotation):** The displayed dictionary-count expression uses r1=777716. This is a local arithmetic display, not the main theorem’s proof.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The displayed polynomial has been evaluated incorrectly.

### Argument or calculation

Exact integer arithmetic gives 777716^2+777716+1=604842954373, whereas 970353651=31151*31150+1. The printed number belongs to a different expression.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-28-response.md](original/M01-round-28-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-28-response.md")
  - Coverage: Full bundled file; source lines 1–1152.
  - Relevant location(s): round-28-response.md, lines 725–733; lines 725-733
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-28-response.md`

- [M02: concentrated_audit_2_rounds_24_42.md](original/M02-concentrated_audit_2_rounds_24_42.md "holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md")
  - Coverage: Full bundled file; source lines 1–883.
  - Relevant location(s): package F finding for M13
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md`

- [M03: MASTER_AUDIT_PROTOCOL.md](original/M03-MASTER_AUDIT_PROTOCOL.md "holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–86.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md
  - Source: `holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md`

- [M04: round-23-local-audit.md](original/M04-round-23-local-audit.md "holevo-full-size/outputs/round-23-local-audit.md")
  - Coverage: Full bundled file; source lines 1–310.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md
  - Source: `holevo-full-size/outputs/round-23-local-audit.md`
