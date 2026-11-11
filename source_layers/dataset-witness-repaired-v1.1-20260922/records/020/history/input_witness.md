# Record 020 — Werner–Holevo zero-capacity boundary

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> - **Pure-input structure (verify exactly first):** for a pure qutrit psi (take real psi and
>   generic complex psi), spec Λ_x(psi) = {x/2, x/2, 1-x} and
>   spec Λ_x^c(psi) = {1-x, x/2, x/2, 0} — B-side full rank, E-side one-dimensional kernel.

**Recorded location:** Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522

**Context (annotation, not a source quotation):** The claim concerns Lambda_x(rho)=(1-x)rho+(x/2)(Tr(rho)I-rho^T), and is explicitly requested for both real and generic complex pure inputs. The commission says “verify exactly first,” so this is an asserted working formula being tested, not a completed theorem.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The fixed spectrum is valid for real-up-to-phase inputs, not arbitrary complex inputs.

### Argument or calculation

Take x=9/20 and psi=(1,i,1)/sqrt(3). Then |psi^T psi|^2=1/9. Writing a=1-x and b=x/2, Lambda_x(|psi><psi|)=bI+a|psi><psi|-b|bar(psi)><bar(psi)| has eigenvalues b and [(1-b) +/- sqrt((1-b)^2-4ab|psi^T psi|^2)]/2. These are 9/40 and (31 +/- 3 sqrt(97))/80, not {11/20,9/40,9/40}.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 原始 commission 有 generic complex 的错误固定谱公式，但相邻推理只有 rank/kernel/entropy 路线，未找到同一泛化谱公式。

- [2026-07-29T17:11:03.650Z — claude_visible_thinking](original/M01-WHGAP-main-c5b96aec.jsonl.readable.md) — source line 1507; recorded role: generation.

## Original materials

- [M01: WHGAP-main-c5b96aec.jsonl](original/M01-WHGAP-main-c5b96aec.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl") · [event data](original/M01-WHGAP-main-c5b96aec.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1501–1513, 1516–1529, 1558–1570, 4867–4891.
  - Relevant location(s): Research commission write, 2026-07-29T17:13:33.094Z, JSONL line 1522; JSONL lines 1507 (route thinking) and 1522 (exact commission Write); 1507 and :1522; 1522 (2026-07-29T17:13:33.094Z); 1564; lines 1507
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/WHGAP-main-c5b96aec.jsonl`

- [M02: whgap_p9_necessary_20260729.md](original/M02-whgap_p9_necessary_20260729.md "artifacts/whgap_p9_necessary_20260729.md")
  - Coverage: Full bundled file; source lines 1–249.
  - Relevant location(s): 55-87; Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_p9_necessary_20260729.md`

- [M03: WHGAP-P9-019faef9.jsonl](original/M03-WHGAP-P9-019faef9.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/WHGAP-P9-019faef9.jsonl") · [event data](original/M03-WHGAP-P9-019faef9.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 75–87.
  - Relevant location(s): 81 and :120
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/WHGAP-P9-019faef9.jsonl`

- [M04: WERNER-HOLEVO-GAP_PROOF_DAG.md](original/M04-WERNER-HOLEVO-GAP_PROOF_DAG.md "channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md")
  - Coverage: Full bundled file; source lines 1–369.
  - Relevant location(s): #P9
  - Source: `channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md`

- [M05: whgap_p9_g0.py](original/M05-whgap_p9_g0.py "tools/whgap_p9_g0.py")
  - Coverage: Full bundled file; source lines 1–333.
  - Relevant location(s): Referenced by artifacts/whgap_p9_necessary_20260729.md
  - Source: `tools/whgap_p9_g0.py`

- [M06: whgap_p9_distillation.py](original/M06-whgap_p9_distillation.py "tools/whgap_p9_distillation.py")
  - Coverage: Full bundled file; source lines 1–571.
  - Relevant location(s): Referenced by artifacts/whgap_p9_necessary_20260729.md
  - Source: `tools/whgap_p9_distillation.py`

- [M07: whgap_lean_t1t2_20260730.md](original/M07-whgap_lean_t1t2_20260730.md "artifacts/whgap_lean_t1t2_20260730.md")
  - Coverage: Full bundled file; source lines 1–413.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_lean_t1t2_20260730.md`

- [M08: whgap_r8_review_20260730.md](original/M08-whgap_r8_review_20260730.md "artifacts/whgap_r8_review_20260730.md")
  - Coverage: Full bundled file; source lines 1–583.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_r8_review_20260730.md`

- [M09: whgap_r7_review_20260730.md](original/M09-whgap_r7_review_20260730.md "artifacts/whgap_r7_review_20260730.md")
  - Coverage: Full bundled file; source lines 1–605.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_r7_review_20260730.md`

- [M10: whgap_r6_review_20260730.md](original/M10-whgap_r6_review_20260730.md "artifacts/whgap_r6_review_20260730.md")
  - Coverage: Full bundled file; source lines 1–508.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_r6_review_20260730.md`

- [M11: whgap_p9b_noascent_20260729.md](original/M11-whgap_p9b_noascent_20260729.md "artifacts/whgap_p9b_noascent_20260729.md")
  - Coverage: Full bundled file; source lines 1–185.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_p9b_noascent_20260729.md`

- [M12: whgap_p6_relaxation_20260729.md](original/M12-whgap_p6_relaxation_20260729.md "artifacts/whgap_p6_relaxation_20260729.md")
  - Coverage: Full bundled file; source lines 1–222.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_p6_relaxation_20260729.md`

- [M13: whgap_p5_derivation_package_20260729.md](original/M13-whgap_p5_derivation_package_20260729.md "artifacts/whgap_p5_derivation_package_20260729.md")
  - Coverage: Full bundled file; source lines 1–360.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_p5_derivation_package_20260729.md`

- [M14: whgap_p3_review_20260729.md](original/M14-whgap_p3_review_20260729.md "artifacts/whgap_p3_review_20260729.md")
  - Coverage: Full bundled file; source lines 1–484.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_p3_review_20260729.md`

- [M15: whgap_p3_qonset_20260729.md](original/M15-whgap_p3_qonset_20260729.md "artifacts/whgap_p3_qonset_20260729.md")
  - Coverage: Full bundled file; source lines 1–315.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_p3_qonset_20260729.md`

- [M16: whgap_external_review_chatgpt_20260728.md](original/M16-whgap_external_review_chatgpt_20260728.md "artifacts/whgap_external_review_chatgpt_20260728.md")
  - Coverage: Full bundled file; source lines 1–57.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_external_review_chatgpt_20260728.md`

- [M17: main.tex](original/M17-main.tex "paper/main.tex")
  - Coverage: Full bundled file; source lines 1–1521.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `paper/main.tex`

- [M18: whgap_p4_review_20260728.md](original/M18-whgap_p4_review_20260728.md "artifacts/whgap_p4_review_20260728.md")
  - Coverage: Full bundled file; source lines 1–317.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `artifacts/whgap_p4_review_20260728.md`

- [M19: RESEARCH_STRUCTURE_PROTOCOL.md](original/M19-RESEARCH_STRUCTURE_PROTOCOL.md "publish/QuantumOpenQuestion/research/RESEARCH_STRUCTURE_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–179.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `publish/QuantumOpenQuestion/research/RESEARCH_STRUCTURE_PROTOCOL.md`

- [M20: DAG_PROTOCOL.md](original/M20-DAG_PROTOCOL.md "research/DAG_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–316.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `research/DAG_PROTOCOL.md`

- [M21: proof_dag_check.py](original/M21-proof_dag_check.py "tools/proof_dag_check.py")
  - Coverage: Full bundled file; source lines 1–930.
  - Relevant location(s): Referenced by channel-capacity/werner-holevo-gap/notes/WERNER-HOLEVO-GAP_PROOF_DAG.md
  - Source: `tools/proof_dag_check.py`
