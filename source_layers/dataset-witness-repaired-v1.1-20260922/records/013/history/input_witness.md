# Record 013 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> For cofactor \(i\), pad the magnitude array with zeros to length \(S_i\), and let
> 
> $$
> \bar a_i=\frac{L_i}{S_i}.
> $$
> 
> Then
> 
> $$
> \frac{D_i}{S_i}
> =
> \sum_{\xi=1}^{S_i}
> \bigl(|A_i(\xi)|-\bar a_i\bigr)^2,
> \qquad
> D_i=S_ie_i^2-L_i^2.
> \tag{6.1}
> $$
> 
> Restrict this sum to:
> 
> * the \(G_i\) surviving unit anchors;
> * the \(N_i\) surviving complete opposite-sign pairs.
> 
> For arbitrary \(\mu\in\mathbb R\),
> 
> $$
> \frac{D_i}{S_i}
> \ge
> G_i(1-\mu)^2
> +
> \sum_{p=1}^{N_i}
> \left[
> (r_{p,+}-\mu)^2+(r_{p,-}-\mu)^2
> \right].
> \tag{6.2}
> $$

**Recorded location:** round-55-response.md, lines 577–612

**Context (annotation, not a source quotation):** D_i=S_i e_i^2-L_i^2 is S_i times the squared-deviation sum about the actual mean bar(a)_i=L_i/S_i. G_i counts retained unit anchors and N_i counts retained opposite-sign pairs with magnitudes r_(p,+),r_(p,-).

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

A variance about its minimizing mean cannot bound squared deviations about every arbitrary center.

### Argument or calculation

For any nonempty selected coordinate set, the right side of (6.2) grows quadratically as |mu| tends to infinity, whereas D_i/S_i is fixed and finite. As a minimal exact example, one unit coordinate has S_i=L_i=e_i^2=G_i=1 and N_i=0, so D_i/S_i=0; choosing mu=0 makes the asserted right side 1. The valid route evaluates the selected deviations at the actual mean first, then lower-bounds them by their minimum over mu.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: round-55-response.md](original/M01-round-55-response.md "holevo-full-size/artifacts/web-gpt56sol-pro/round-55-response.md")
  - Coverage: Full bundled file; source lines 1–1146.
  - Relevant location(s): round-55-response.md, lines 577–612; lines 575-635
  - Source: `holevo-full-size/artifacts/web-gpt56sol-pro/round-55-response.md`

- [M02: concentrated_audit_3_rounds_43_58.md](original/M02-concentrated_audit_3_rounds_43_58.md "holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md")
  - Coverage: Full bundled file; source lines 1–1348.
  - Relevant location(s): package F finding for M19
  - Source: `holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md`

- [M03: 03_r043_r058_finite_slope_foundation_CORE.md](original/M03-03_r043_r058_finite_slope_foundation_CORE.md "holevo-full-size/central-audit-2026-09-18/generated/03_r043_r058_finite_slope_foundation_CORE.md")
  - Coverage: Full bundled file; source lines 1–24691.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/central-audit-2026-09-18/generated/03_r043_r058_finite_slope_foundation_CORE.md`

- [M04: MASTER_AUDIT_PROTOCOL.md](original/M04-MASTER_AUDIT_PROTOCOL.md "holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–86.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/central-audit-2026-09-18/MASTER_AUDIT_PROTOCOL.md`

- [M05: BASELINE.md](original/M05-BASELINE.md "holevo-full-size/central-audit-2026-09-18/BASELINE.md")
  - Coverage: Full bundled file; source lines 1–89.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/central-audit-2026-09-18/BASELINE.md`

- [M06: verify_round43_translation.py](original/M06-verify_round43_translation.py "holevo-full-size/work/verify_round43_translation.py")
  - Coverage: Full bundled file; source lines 1–178.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round43_translation.py`

- [M07: verify_round43_web_response.py](original/M07-verify_round43_web_response.py "holevo-full-size/work/verify_round43_web_response.py")
  - Coverage: Full bundled file; source lines 1–313.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round43_web_response.py`

- [M08: verify_round44_candidate.py](original/M08-verify_round44_candidate.py "holevo-full-size/work/verify_round44_candidate.py")
  - Coverage: Full bundled file; source lines 1–77.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round44_candidate.py`

- [M09: verify_round44_web_response.py](original/M09-verify_round44_web_response.py "holevo-full-size/work/verify_round44_web_response.py")
  - Coverage: Full bundled file; source lines 1–152.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round44_web_response.py`

- [M10: enumerate_round45_matchings.py](original/M10-enumerate_round45_matchings.py "holevo-full-size/work/enumerate_round45_matchings.py")
  - Coverage: Full bundled file; source lines 1–101.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round45_matchings.py`

- [M11: verify_round45_web_response.py](original/M11-verify_round45_web_response.py "holevo-full-size/work/verify_round45_web_response.py")
  - Coverage: Full bundled file; source lines 1–223.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round45_web_response.py`

- [M12: enumerate_round46_one_defect.py](original/M12-enumerate_round46_one_defect.py "holevo-full-size/work/enumerate_round46_one_defect.py")
  - Coverage: Full bundled file; source lines 1–76.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round46_one_defect.py`

- [M13: verify_round46_web_response.py](original/M13-verify_round46_web_response.py "holevo-full-size/work/verify_round46_web_response.py")
  - Coverage: Full bundled file; source lines 1–256.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round46_web_response.py`

- [M14: enumerate_round47_ratio_two.py](original/M14-enumerate_round47_ratio_two.py "holevo-full-size/work/enumerate_round47_ratio_two.py")
  - Coverage: Full bundled file; source lines 1–99.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round47_ratio_two.py`

- [M15: verify_round47_web_response.py](original/M15-verify_round47_web_response.py "holevo-full-size/work/verify_round47_web_response.py")
  - Coverage: Full bundled file; source lines 1–177.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round47_web_response.py`

- [M16: enumerate_round48_kappa_frontier.py](original/M16-enumerate_round48_kappa_frontier.py "holevo-full-size/work/enumerate_round48_kappa_frontier.py")
  - Coverage: Full bundled file; source lines 1–83.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round48_kappa_frontier.py`

- [M17: verify_round48_web_response.py](original/M17-verify_round48_web_response.py "holevo-full-size/work/verify_round48_web_response.py")
  - Coverage: Full bundled file; source lines 1–240.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round48_web_response.py`

- [M18: verify_round49_frontier.cpp](original/M18-verify_round49_frontier.cpp "holevo-full-size/work/verify_round49_frontier.cpp")
  - Coverage: Full bundled file; source lines 1–296.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round49_frontier.cpp`

- [M19: verify_round49_web_response.py](original/M19-verify_round49_web_response.py "holevo-full-size/work/verify_round49_web_response.py")
  - Coverage: Full bundled file; source lines 1–105.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round49_web_response.py`

- [M20: enumerate_round50_three_ratio.cpp](original/M20-enumerate_round50_three_ratio.cpp "holevo-full-size/work/enumerate_round50_three_ratio.cpp")
  - Coverage: Full bundled file; source lines 1–248.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round50_three_ratio.cpp`

- [M21: verify_round50_pre_send.py](original/M21-verify_round50_pre_send.py "holevo-full-size/work/verify_round50_pre_send.py")
  - Coverage: Full bundled file; source lines 1–78.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round50_pre_send.py`

- [M22: enumerate_round51_four_ratio.cpp](original/M22-enumerate_round51_four_ratio.cpp "holevo-full-size/work/enumerate_round51_four_ratio.cpp")
  - Coverage: Full bundled file; source lines 1–281.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/enumerate_round51_four_ratio.cpp`

- [M23: verify_round51_low_collision.cpp](original/M23-verify_round51_low_collision.cpp "holevo-full-size/work/verify_round51_low_collision.cpp")
  - Coverage: Full bundled file; source lines 1–299.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round51_low_collision.cpp`

- [M24: verify_round51_web_response.py](original/M24-verify_round51_web_response.py "holevo-full-size/work/verify_round51_web_response.py")
  - Coverage: Full bundled file; source lines 1–238.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round51_web_response.py`

- [M25: verify_round52_laurent.cpp](original/M25-verify_round52_laurent.cpp "holevo-full-size/work/verify_round52_laurent.cpp")
  - Coverage: Full bundled file; source lines 1–475.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round52_laurent.cpp`

- [M26: verify_round52_web_response.py](original/M26-verify_round52_web_response.py "holevo-full-size/work/verify_round52_web_response.py")
  - Coverage: Full bundled file; source lines 1–243.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round52_web_response.py`

- [M27: verify_round53_web_response.py](original/M27-verify_round53_web_response.py "holevo-full-size/work/verify_round53_web_response.py")
  - Coverage: Full bundled file; source lines 1–226.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round53_web_response.py`

- [M28: verify_round54_lowfiber.cpp](original/M28-verify_round54_lowfiber.cpp "holevo-full-size/work/verify_round54_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–505.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round54_lowfiber.cpp`

- [M29: verify_round55_lowfiber.cpp](original/M29-verify_round55_lowfiber.cpp "holevo-full-size/work/verify_round55_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–512.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round55_lowfiber.cpp`

- [M30: verify_round56_lowfiber.cpp](original/M30-verify_round56_lowfiber.cpp "holevo-full-size/work/verify_round56_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–512.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round56_lowfiber.cpp`

- [M31: verify_round57_lowfiber.cpp](original/M31-verify_round57_lowfiber.cpp "holevo-full-size/work/verify_round57_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–493.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round57_lowfiber.cpp`

- [M32: verify_round58_lowfiber.cpp](original/M32-verify_round58_lowfiber.cpp "holevo-full-size/work/verify_round58_lowfiber.cpp")
  - Coverage: Full bundled file; source lines 1–594.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/verify_round58_lowfiber.cpp`

- [M33: round58_size2_merge.cpp](original/M33-round58_size2_merge.cpp "holevo-full-size/work/round58_bundle/round58_size2_merge.cpp")
  - Coverage: Full bundled file; source lines 1–17.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/round58_bundle/round58_size2_merge.cpp`

- [M34: round58_size2_merge_detail.cpp](original/M34-round58_size2_merge_detail.cpp "holevo-full-size/work/round58_bundle/round58_size2_merge_detail.cpp")
  - Coverage: Full bundled file; source lines 1–19.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/round58_bundle/round58_size2_merge_detail.cpp`

- [M35: round58_response.md](original/M35-round58_response.md "holevo-full-size/work/round59_bundle/round58_response.md")
  - Coverage: Full bundled file; source lines 1–1058.
  - Relevant location(s): Referenced by holevo-full-size/central-audit-2026-09-18/web-results/03_rounds_43_58/concentrated_audit_3_rounds_43_58.md
  - Source: `holevo-full-size/work/round59_bundle/round58_response.md`
