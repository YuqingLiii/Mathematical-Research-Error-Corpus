# Record 021 — Werner–Holevo zero-capacity boundary

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> - D1 (derivation check, exact): verify the pure-output spectra claims symbolically; verify
>   the epsilon-expansion bookkeeping NUMERICALLY at high precision: for random (psi, phi)
>   kernel-avoiding pairs at x = 9/20, fit Ic((1-eps)psi + eps phi) against
>   c1*eps + O(eps^2 log eps) and confirm the fitted c1 matches
>   `-Tr[Λ(phi-psi) log Λ(psi)] + Tr[Λ^c(phi-psi) log Λ^c(psi)]` to >= 8 digits; also confirm
>   kernel-HITTING phi produce the -eps log(1/eps) plunge. GATE G0.
> 
> [...]
> 
>   over pure psi and kernel-avoiding states phi (parameterize phi on the 3-dim support
>   constraint; >= 150 restarts). A_1 > 0 anywhere

**Recorded location:** Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522

**Context (annotation, not a source quotation):** The proposed first-order test requires a distinct comparison state phi satisfying supp Lambda_x^c(phi) subset supp Lambda_x^c(psi). It treats this as a three-dimensional domain from which random kernel-avoiding pairs can be drawn.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

The environment-support restriction can force phi=|psi><psi|, so the assumed nontrivial comparison domain does not exist.

### Argument or calculation

For psi=|0> and 0<x<1, use Kraus operators K0=sqrt(1-x)I and K_(mu+1)=sqrt(x/2)A_mu, (A_mu)_(jk)=epsilon_(mu j k). The complementary output has kernel vector z=(0,1,0,0). Positivity and support inclusion imply Tr(K1 phi K1^dagger)=0, hence supp(phi) subset ker K1=span{|0>}. Since phi has trace one it equals |0><0|. The claimed random distinct-pair construction therefore fails already in this exact instance; generic tests in the recorded check also had one-dimensional allowed support.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 相邻推理探索 kernel-avoiding 方向是否可行，不明确断言存在满足全部条件的 distinct φ；后来的否定属于审计。

- [2026-07-29T17:11:03.650Z — claude_visible_thinking](original/M01-WHGAP-main-c5b96aec.jsonl.readable.md) — source line 1507; recorded role: generation.

## Original materials

- [M01: WHGAP-main-c5b96aec.jsonl](original/M01-WHGAP-main-c5b96aec.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl") · [event data](original/M01-WHGAP-main-c5b96aec.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1501–1513, 1516–1529, 1558–1570, 4867–4891.
  - Relevant location(s): Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522; JSONL lines 1507 (route thinking) and 1522 (exact commission Write); 1507 and :1522; 1522 (2026-07-29T17:13:33.094Z); 1564; lines 1507
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl`

- [M02: whgap_p9_necessary_20260729.md](original/M02-whgap_p9_necessary_20260729.md "artifacts/whgap_p9_necessary_20260729.md")
  - Coverage: Full bundled file; source lines 1–249.
  - Relevant location(s): 89-116
  - Source: `artifacts/whgap_p9_necessary_20260729.md`

- [M03: WHGAP-P9-019faef9.jsonl](original/M03-WHGAP-P9-019faef9.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/WHGAP-P9-019faef9.jsonl") · [event data](original/M03-WHGAP-P9-019faef9.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 75–87.
  - Relevant location(s): 81 and :120
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/WHGAP-P9-019faef9.jsonl`

- [M04: whgap_p9_g0.py](original/M04-whgap_p9_g0.py "tools/whgap_p9_g0.py")
  - Coverage: Full bundled file; source lines 1–333.
  - Relevant location(s): Referenced by artifacts/whgap_p9_necessary_20260729.md
  - Source: `tools/whgap_p9_g0.py`

- [M05: whgap_p9_distillation.py](original/M05-whgap_p9_distillation.py "tools/whgap_p9_distillation.py")
  - Coverage: Full bundled file; source lines 1–571.
  - Relevant location(s): Referenced by artifacts/whgap_p9_necessary_20260729.md
  - Source: `tools/whgap_p9_distillation.py`
