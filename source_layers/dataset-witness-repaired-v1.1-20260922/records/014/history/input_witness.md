# Record 014 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> with the fifth centered pair \(\{\pm m_r\}\) arbitrary and all twelve slopes distinct, the independently regenerated determinant census gives
> 
> $$
> \boxed{
> \Delta_{\rm ray}+\Delta_{\rm flat}>3318E.
> }
> $$
> 
> [...]
> 
> $$
> \Delta_{\rm ray}
> +\Delta_{\rm flat}
> +\Delta_{\rm Young}
> +\Delta_{\rm group}<HE.
> \tag{1.3}
> $$
> 
> Then, individually,
> 
> $$
> \Delta_{\rm ray}<HE,\qquad
> \Delta_{\rm flat}<HE.
> \tag{1.4}
> $$

**Recorded location:** round-59-response.md, lines 14–20, 118–132

**Context (annotation, not a source quotation):** The proof introduces four nonnegative slacks: ray, flat, Young, and group. Its detailed argument assumes their total is less than H E as a contradiction hypothesis, with H=3318 in this case.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

A consequence derived only inside a contradiction branch was stated as an unconditional strict bound on a subset of the slacks.

### Argument or calculation

Let T=Delta_ray+Delta_flat+Delta_Young+Delta_group. The argument derives (T<HE) => (Delta_ray+Delta_flat>HE), contradicting T<HE because all slacks are nonnegative. The valid unconditional conclusion is T>=HE, not Delta_ray+Delta_flat>HE. For a logical counterassignment, E=H=1, Delta_ray=Delta_flat=0, Delta_Young=1, Delta_group=0 makes T>=HE true and the claimed subsidiary bound false, while the contradiction implication holds vacuously.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-59-response.md](original/M01-round-59-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md")
  - Coverage: Full bundled file; source lines 1–1109.
  - Relevant location(s): round-59-response.md, lines 14–20, 118–132; lines 1-22 and 118-153
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-59-response.md`

- [M02: concentrated_audit_4_rounds_59_81.md](original/M02-concentrated_audit_4_rounds_59_81.md "holevo-full-size/central-audit-2026-09-18/web-results/04_rounds_59_81/concentrated_audit_4_rounds_59_81.md")
  - Coverage: Full bundled file; source lines 1–268.
  - Relevant location(s): package F finding for M22
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
