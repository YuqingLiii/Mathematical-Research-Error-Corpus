# Record 060 — Channel additivity violations

**Review status:** `interpretation_check_pending`.

Selected response explicitly disclaims closure of the intended gate. Recover the earlier malformed E1 proposal if the record is to represent a source-generation error.

## Original statement and context

> # Verdict: **PROVED — for \((E1)\) exactly as stated**
> 
> The literal existential statement \((E1)\) is true. The decisive issue is that \((E1)\) imposes no upper bound on \(\eta\), hence no small-\(A\) or positive-gap condition. One may choose \(A=m\), at which point the one-copy bound and the orbit-block ratio bound become universally true.
> 
> This does **not** settle the physically relevant gate from Round 1. The strengthened statement with
> 
> $$
> \frac{\log_2m}{m}>2\log_2 A
> \qquad\Longleftrightarrow\qquad
> A^2<m^{1/m}
> \tag{Gap}
> $$
> 
> [...]
> 
> ## 7. Why this does not close the intended finite gate
> 
> The construction above has
> 
> $$
> A=m,
> $$
> 
> so
> 
> $$
> 2\log_2A=2\log_2m
> $$
> 
> while
> 
> $$
> \frac{\log_2m}{m}\ll2\log_2m.
> $$
> 
> It is maximally outside the positive-gap regime.
> 
> The intended strengthened statement should include
> 
> $$

**Recorded location:** round-02-response.md, lines 1–12, 1154–1178

**Context (annotation, not a source quotation):** The intended channel-purity gate requires the positive-defect condition A^2<m^(1/m). The displayed response explicitly distinguishes its literal E1 statement from that intended gate.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

The intended positive-defect hypothesis is missing from the literal E1 problem, but the response itself explicitly identifies that omission and does not claim the intended target is solved.

### Argument or calculation

For m>1, A=m yields A^2=m^2>m^(1/m), so the literal E1 witness cannot establish a positive defect. However, the original response says exactly this and explicitly states that the intended strengthened gate remains unresolved. The source-bound issue is the malformed problem statement; the selected response is not evidence of a false solution claim.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-02-response.md](original/M01-round-02-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-02-response.md")
  - Coverage: Full bundled file; source lines 1–1236.
  - Relevant location(s): round-02-response.md, lines 1–12, 1154–1178; lines 1-5, 1099-1105, 1149-1178
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-02-response.md`

- [M02: concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md "holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md")
  - Coverage: Full bundled file; source lines 1–585.
  - Relevant location(s): package F finding for M01
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
