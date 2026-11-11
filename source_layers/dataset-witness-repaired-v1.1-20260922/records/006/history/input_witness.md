# Record 006 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> Consequently,
> 
> $$
> \begin{aligned}
> \mathbb E_{s,t}
> \langle\Delta_{L,s}\Theta_{M,t}\rangle
> &=
> \langle\overline\Delta\,\overline\Theta\rangle\\
> &=
> \sum_{k,j}
> \left(\frac1D-p_k\right)
> \left(\frac1D-r_j\right)
> \mathcal B_{kj}.
> \end{aligned}
> \tag{6.1}
> $$
> 
> The phases of \(\mathcal B_{kj}\) remain. The higher terms in
> `TwoLinePlaquette` similarly retain three- and four-point Bargmann data.
> 
> Thus neither the four-corner subtraction nor the full uniform average over the two cyclic shifts reduces the two-line condition to the two autocorrelation shadows.
> 
> A phase-free two-line contradiction is not obtained.

**Recorded location:** round-20-response.md, lines 653–675

**Context (annotation, not a source quotation):** Delta and Theta are perturbations from shifting two stabilizer lines. The full TwoLinePlaquette expression contains a bilinear term and higher-order terms. The excerpt computes only the bilinear average explicitly.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Phase dependence of one averaged summand does not prove phase dependence of the complete averaged expression.

### Argument or calculation

The source evaluates E<Delta Theta>=sum_(k,j)(1/D-p_k)(1/D-r_j) B_(kj), then says the higher terms “similarly retain” phase data without evaluating their sum. A full expression F1(theta)+F2(theta) can be phase-independent even when F1 is not (take F2=-F1+c). Therefore the displayed partial calculation does not imply the claimed noncancellation for TwoLinePlaquette. A complete average, or a coefficient that provably survives the complete sum, is required.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-20-response.md](original/M01-round-20-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-20-response.md")
  - Coverage: Full bundled file; source lines 1–1139.
  - Relevant location(s): round-20-response.md, lines 653–675; lines 632-675 and 1026-1036
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-20-response.md`

- [M02: concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md "holevo-full-size/central-audit-2026-09-18/web-results/01_rounds_1_23/concentrated_audit_1_rounds_1_23.md")
  - Coverage: Full bundled file; source lines 1–585.
  - Relevant location(s): package F finding for M05
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
