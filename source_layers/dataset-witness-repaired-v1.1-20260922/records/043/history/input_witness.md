# Record 043 — Quantum k-sum with small alphabets

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> The bad
> event $\dist_q(T_\mu,t)\le P$ constrains the nonzero linear form $\nu\cdot w'$ to a set of at most
> $2P+1$ residues, so it forbids at most $(2P+1)q^{k-2}$ of the $q^{k-1}$ vectors $w'$.

**Recorded location:** Appendix all-targets lemma Edit event, 2026-07-18T02:44:18.919Z.

**Context (annotation, not a source quotation):** The appendix uses a fiber count for a nonzero linear form over Z_q without assuming its coefficients generate the whole ring modulo q.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

A nonzero modular linear form need not be surjective; fibers may have an extra gcd factor.

### Argument or calculation

For k=3, choose wrong block multiplicities mu=(3,0,0), so nu=(3,0), and choose t=0, q=228, P=12. There are9 multiples of3 in the circular interval[-12,12]. Each equation3w1=r mod228 for such a residue has3 solutions, and w2 is arbitrary. Thus the bad set has9*3*228=6156 pairs, exceeding (2P+1)q=25*228=5700. Here q>9(2P+1)=225, so even the displayed counting threshold does not validate the faulty per-pattern estimate. A gcd factor or an invertibility hypothesis is needed.

Scope: computation_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 把模合数的非零线性形式当作能逐坐标唯一解出的形式，遗漏系数与模数的 gcd 因子。

- [2026-07-18T02:43:50.483Z — claude_visible_thinking](original/M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.readable.md) — source line 127; recorded role: generation.

## Original materials

- [M01: KSUM-agent-acb57dcbbc16cfba2.jsonl](original/M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-agent-acb57dcbbc16cfba2.jsonl") · [event data](original/M01-KSUM-agent-acb57dcbbc16cfba2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 121–140.
  - Relevant location(s): JSONL lines 127 (plaintext thinking) and 133 (exact Edit); 127 and :133; 133 (2026-07-18T02:44:18.919Z); lines 127; lines 133
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-agent-acb57dcbbc16cfba2.jsonl`

- [M02: KSUM-main-b5fea9c2.jsonl](original/M02-KSUM-main-b5fea9c2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl") · [event data](original/M02-KSUM-main-b5fea9c2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1485–1497.
  - Relevant location(s): 1491 (2026-07-19T17:17:00.237Z)
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl`

- [M03: DATA6_ksum_ledger.md](original/M03-DATA6_ksum_ledger.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/DATA6_ksum_ledger.md`
