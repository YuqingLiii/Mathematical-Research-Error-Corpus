# Record 065 — Channel additivity violations

**Review status:** `source_or_fixture_check_pending`.

The archived corrected vector and implementation are bundled, but the reconstruction has not been independently rerun in this packaging pass. Check the determinant enumeration and constants together; a second printed vector alone does not establish the witness.

## Original statement and context

> \[
> (H_{4,i})=(
> 8437248,11517728,12835576,14928318,15308304,16650864,15684084,
> 16650864,15308304,14928318,12835576,11517728,8437248).
> \tag{98.10}
> \]

**Recorded location:** round-98-prompt-sent.md, lines 148–153

**Context (annotation, not a source quotation):** The transmitted input contains a thirteen-entry vector of raw-size-four determinant counts. Two entries were altered during prompt preparation; the receiving response recomputed the vector before use. This is an input-preparation error, not attributed to the receiving solver.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Two copied input-vector values disagree with the independently regenerated determinant counts.

### Argument or calculation

The transmitted vector contains 14928318 in zero-based rows 3 and 9. The regenerated raw-size-four vector is (8437248,11517728,12835576,14926862,15308304,16650864,15684084,16650864,15308304,14926862,12835576,11517728,8437248). The erroneous entries exceed the recomputed entries by 1456 each. The receiving response exposes and corrects this mismatch before using the data. The underlying determinant-count reconstruction is required to verify the corrected vector independently.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-98-prompt-sent.md](original/M01-round-98-prompt-sent.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-98-prompt-sent.md")
  - Coverage: Full bundled file; source lines 1–408.
  - Relevant location(s): round-98-prompt-sent.md, lines 148–153; lines 147-152
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-98-prompt-sent.md`

- [M02: round-98-response.md](original/M02-round-98-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-98-response.md")
  - Coverage: Full bundled file; source lines 1–856.
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-98-response.md`

- [M03: concentrated_audit_5_rounds_82_105.md](original/M03-concentrated_audit_5_rounds_82_105.md "holevo-full-size/central-audit-2026-09-18/web-results/05_rounds_82_105/concentrated_audit_5_rounds_82_105.md")
  - Coverage: Full bundled file; source lines 1–202.
  - Relevant location(s): package F finding for M27
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/05_rounds_82_105/concentrated_audit_5_rounds_82_105.md`

- [M04: explore_round82_global.cpp](original/M04-explore_round82_global.cpp "holevo-full-size/work/explore_round82_global.cpp")
  - Coverage: Full bundled file; source lines 1–840.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/05_rounds_82_105/concentrated_audit_5_rounds_82_105.md
  - Source: `holevo-full-size/work/explore_round82_global.cpp`

- [M05: round-104-prompt.md](original/M05-round-104-prompt.md "holevo-full-size/work/round-104-prompt.md")
  - Coverage: Full bundled file; source lines 1–412.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/05_rounds_82_105/concentrated_audit_5_rounds_82_105.md
  - Source: `holevo-full-size/work/round-104-prompt.md`
