# Record 063 — Channel additivity violations

**Review status:** `source_or_fixture_check_pending`.

The archived corrected vector and implementation are bundled, but the reconstruction has not been independently rerun in this packaging pass. Check the determinant enumeration and constants together; a second printed vector alone does not establish the witness.

## Original statement and context

>     constexpr std::array<std::uint64_t, N> SUPPORT = {
>         53624480, 67257904, 74298900, 80378416, 82204926, 85479258, 83844372,
>         85479258, 82204926, 80378416, 74298900, 67257904, 53624480,
>     };
> 
> [...]
> 
>         weighted_surviving += static_cast<u128>(SUPPORT[deleted]) *
>                               static_cast<u128>(
>                                   matched > BUDGET[deleted] ? matched - BUDGET[deleted] : 0
>                               );

**Recorded location:** explore_round82_global.cpp, lines 340–343, 458–461

**Context (annotation, not a source quotation):** The exploratory program computes weighted_surviving using the active SUPPORT array for a later finite-slope instance whose exact support total is K=970337664. The selected constants come from a prior instance.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

A stale support vector is used in the exploratory weighted calculation.

### Argument or calculation

The thirteen printed SUPPORT entries sum to 970332140. The independently enumerated target vector reported in the round-82 thirteen-row census is (53624480,67257904,74299396,80379126,82205586,85479878,83844924,85479878,82205586,80379126,74299396,67257904,53624480), whose sum is 970337664. The difference is 5524. Because weighted_surviving multiplies each row by SUPPORT[deleted], these are not interchangeable constants. The archived final proof did not depend on this exploratory diagnostic. Independent verification of the target vector requires the determinant enumeration fixture, not just the two printed totals.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: explore_round82_global.cpp](original/M01-explore_round82_global.cpp "holevo-full-size/work/explore_round82_global.cpp")
  - Coverage: Full bundled file; source lines 1–840.
  - Relevant location(s): explore_round82_global.cpp, lines 340–343, 458–461; lines 340-343 and 458-461; Referenced by holevo-full-size/central-audit-2026-09-18/web-results/05_rounds_82_105/concentrated_audit_5_rounds_82_105.md
  - Source: `holevo-full-size/work/explore_round82_global.cpp`

- [M02: round-82-response.md](original/M02-round-82-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-82-response.md")
  - Coverage: Full bundled file; source lines 1–1119.
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-82-response.md`

- [M03: concentrated_audit_5_rounds_82_105.md](original/M03-concentrated_audit_5_rounds_82_105.md "holevo-full-size/central-audit-2026-09-18/web-results/05_rounds_82_105/concentrated_audit_5_rounds_82_105.md")
  - Coverage: Full bundled file; source lines 1–202.
  - Relevant location(s): package F finding for M25
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/05_rounds_82_105/concentrated_audit_5_rounds_82_105.md`

- [M04: round-104-prompt.md](original/M04-round-104-prompt.md "holevo-full-size/work/round-104-prompt.md")
  - Coverage: Full bundled file; source lines 1–412.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/05_rounds_82_105/concentrated_audit_5_rounds_82_105.md
  - Source: `holevo-full-size/work/round-104-prompt.md`
