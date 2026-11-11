# Record 062 — Channel additivity violations

**Review status:** `interpretation_check_pending`.

Broad headline is immediately scoped by explicit exclusions. Needs substantive adjudication, not blind retention of prior label.

## Original statement and context

> The adjacent \(14\)-root matrix circuit and its convex dual are correct. However, the holomorphic Plücker relation does **not** directly control the required sesquilinear circuit. The exact outcome is a rigorous method limit:
> 
> $$
> \boxed{
> \begin{gathered}
> \text{Any valid linear use of the adjacent holomorphic Plücker wedge is either}\\
> \text{inadmissible for the physical sesquilinear circuit, or—when a constant}\\
> \text{conjugation real structure makes it admissible—has identically zero target gain.}
> \end{gathered}}
> \tag{PlueckerLinearNoGo}
> $$
> 
> This is proved for arbitrary adjacent \(k+2\)-root/\(k\)-slope circuits over any odd prime field. An explicit frozen-dimensional canonical-cofactor family attains the zero-target conclusion with a nonzero ordinary Plücker coefficient, so the result is not merely formal.
> 
> It does **not** rule out:
> 
> * a constant separator using the transpose-symmetric matrix directions;
> * a constant separator combining those directions with the Plücker direction to reduce the ordinary denominator;
> * a genuinely frequency-dependent matrix multiplier;
> * the exact global shared-phase dual across all Fourier frequencies.

**Recorded location:** round-41-response.md, lines 17–36

**Context (annotation, not a source quotation):** The proof handles a pure alternating Pluecker direction under a constant conjugation real structure. Immediately after the broad headline, the response explicitly excludes mixed symmetric/alternating, frequency-dependent, and global constructions from its conclusion.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The headline quantifier exceeds the pure alternating direction treated in the derivation, but explicit adjacent exclusions may already delimit the intended statement.

### Argument or calculation

The displayed proof controls the alternating J contribution under a constant real structure. A general constant separator S+tJ also has a symmetric contribution S and an ordinary denominator that can depend on t; a zero alternating target numerator does not alone exclude improvement of that ratio. Frequency-dependent and globally coupled constructions are additional unaddressed cases. However, the original text expressly lists these exclusions, so one must decide whether its headline is actually intended universally before counting a positive error.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-41-response.md](original/M01-round-41-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-41-response.md")
  - Coverage: Full bundled file; source lines 1–1302.
  - Relevant location(s): round-41-response.md, lines 17–36; lines 17-35
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-41-response.md`

- [M02: concentrated_audit_2_rounds_24_42.md](original/M02-concentrated_audit_2_rounds_24_42.md "holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md")
  - Coverage: Full bundled file; source lines 1–883.
  - Relevant location(s): package F finding for M16
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md`

- [M03: MASTER_AUDIT_PROTOCOL.md](original/M03-MASTER_AUDIT_PROTOCOL.md "holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–86.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md
  - Source: `holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md`

- [M04: round-23-local-audit.md](original/M04-round-23-local-audit.md "holevo-full-size/outputs/round-23-local-audit.md")
  - Coverage: Full bundled file; source lines 1–310.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/02_rounds_24_42/concentrated_audit_2_rounds_24_42.md
  - Source: `holevo-full-size/outputs/round-23-local-audit.md`
