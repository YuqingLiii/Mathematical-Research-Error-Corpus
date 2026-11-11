# Record 015 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> Since \(D_i\le\Delta_{\rm flat}<HE\), equations (1.6) and (2.4) give
> 
> $$
> m_i<
> \frac{H\,127^2K^2}
> {126^2(K-H)S_i}.
> $$
> 
> The exact strict-integer ceilings are
> 
> $$
> \boxed{
> \begin{aligned}
> (m_i)=(&60996,48631,44023,40693,39789,38265,39011,\\
>        &38265,39789,40693,44023,48631,60996).
> \end{aligned}}
> \tag{2.6}
> $$

**Recorded location:** round-59-response.md, lines 222–239

**Context (annotation, not a source quotation):** For each row, the source derives the strict real bound m_i<x_i, where x_i=H*127^2*K^2/[126^2*(K-H)*S_i]. It then labels a vector of ceilings as exact strict-integer values.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The largest integer strictly less than x is ceil(x)-1, not ceil(x).

### Argument or calculation

For integer m, m<x is equivalent to m<=ceil(x)-1. If x=2 exactly, the maximum admissible integer is 1, not 2; if x=2.3, it is 2, not 3. Consequently the printed thirteen ceilings must each be reduced by one to be sharp strict-integer maxima. Their use as conservative, larger deletion budgets may still be safe; the error is the exactness claim.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-59-response.md](original/M01-round-59-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md")
  - Coverage: Full bundled file; source lines 1–1109.
  - Relevant location(s): round-59-response.md, lines 222–239; lines 222-240
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md`

- [M02: concentrated_audit_4_rounds_59_81.md](original/M02-concentrated_audit_4_rounds_59_81.md "holevo-full-size/central-audit-2026-09-18/web-results/04_rounds_59_81/concentrated_audit_4_rounds_59_81.md")
  - Coverage: Full bundled file; source lines 1–268.
  - Relevant location(s): package F finding for M23
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/04_rounds_59_81/concentrated_audit_4_rounds_59_81.md`

- [M03: round58_response.md](original/M03-round58_response.md "holevo-full-size/work/round59_bundle/round58_response.md")
  - Coverage: Full bundled file; source lines 1–1058.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round58_response.md`

- [M04: round59_size3_reproducer.cpp](original/M04-round59_size3_reproducer.cpp "holevo-full-size/work/round59_bundle/round59_size3_reproducer.cpp")
  - Coverage: Full bundled file; source lines 1–108.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_size3_reproducer.cpp`

- [M05: round59_size2_keycounts.cpp](original/M05-round59_size2_keycounts.cpp "holevo-full-size/work/round59_bundle/round59_size2_keycounts.cpp")
  - Coverage: Full bundled file; source lines 1–13.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_size2_keycounts.cpp`

- [M06: round59_size2_merge_audit.cpp](original/M06-round59_size2_merge_audit.cpp "holevo-full-size/work/round59_bundle/round59_size2_merge_audit.cpp")
  - Coverage: Full bundled file; source lines 1–39.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_size2_merge_audit.cpp`

- [M07: round59_verify_global.py](original/M07-round59_verify_global.py "holevo-full-size/work/round59_bundle/round59_verify_global.py")
  - Coverage: Full bundled file; source lines 1–28.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_verify_global.py`

- [M08: round59_lowfiber_summary.csv](original/M08-round59_lowfiber_summary.csv "holevo-full-size/work/round59_bundle/round59_lowfiber_summary.csv")
  - Coverage: Full bundled file; source lines 1–15.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_lowfiber_summary.csv`

- [M09: round59_size3_summary.csv](original/M09-round59_size3_summary.csv "holevo-full-size/work/round59_bundle/round59_size3_summary.csv")
  - Coverage: Full bundled file; source lines 1–16.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_size3_summary.csv`

- [M10: round59_global_size2_summary.csv](original/M10-round59_global_size2_summary.csv "holevo-full-size/work/round59_bundle/round59_global_size2_summary.csv")
  - Coverage: Full bundled file; source lines 1–19.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_global_size2_summary.csv`

- [M11: round59_global_size2_detail.txt](original/M11-round59_global_size2_detail.txt "holevo-full-size/work/round59_bundle/round59_global_size2_detail.txt")
  - Coverage: Full bundled file; source lines 1–64.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_global_size2_detail.txt`

- [M12: round59_size2_checks.txt](original/M12-round59_size2_checks.txt "holevo-full-size/work/round59_bundle/round59_size2_checks.txt")
  - Coverage: Full bundled file; source lines 1–11.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_size2_checks.txt`

- [M13: round59_stream_sha256.txt](original/M13-round59_stream_sha256.txt "holevo-full-size/work/round59_bundle/round59_stream_sha256.txt")
  - Coverage: Full bundled file; source lines 1–41.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_stream_sha256.txt`

- [M14: round59_exact_inequality_checks.txt](original/M14-round59_exact_inequality_checks.txt "holevo-full-size/work/round59_bundle/round59_exact_inequality_checks.txt")
  - Coverage: Full bundled file; source lines 1–23.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_exact_inequality_checks.txt`

- [M15: round59_digest.txt](original/M15-round59_digest.txt "holevo-full-size/work/round59_bundle/round59_digest.txt")
  - Coverage: Full bundled file; source lines 1–20.
  - Relevant location(s): Referenced by holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md
  - Source: `holevo-full-size/work/round59_bundle/round59_digest.txt`
