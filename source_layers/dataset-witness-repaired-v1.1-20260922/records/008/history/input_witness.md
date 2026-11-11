# Record 008 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> The Fourier \(+1\) property implies the evenness independently because \(\mathscr F^2\) is phase-space reflection.

**Recorded location:** round-23-response.md, lines 234

**Context (annotation, not a source quotation):** The transform is the normalized symplectic Fourier transform (Ff)(k)=D^(-1) sum_p f(p) omega^[p,k] on F_D^2, where [p,k] is alternating and omega is a primitive Dth root of unity.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

For the alternating symplectic kernel, squaring the transform gives the identity, not reflection.

### Argument or calculation

Compute F^2 f(l)=D^(-2) sum_(p,k) f(p) omega^([p,k]+[k,l]). Since [k,l]=-[l,k], the exponent is [p-l,k]. Character orthogonality makes the inner sum D^2 when p=l and zero otherwise, so F^2 f(l)=f(l). It does not give f(-l). Evenness must be justified separately.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-23-response.md](original/M01-round-23-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-23-response.md")
  - Coverage: Full bundled file; source lines 1–1389.
  - Relevant location(s): round-23-response.md, lines 234; lines 230-234
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-23-response.md`

- [M02: concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md "holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md")
  - Coverage: Full bundled file; source lines 1–585.
  - Relevant location(s): package F finding for M07
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
