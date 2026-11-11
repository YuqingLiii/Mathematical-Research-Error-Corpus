# Record 044 — Quantum k-sum with small alphabets

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> There exist constants
> \(\eta>1/6\), \(c_0>0\), and \(\delta>0\) such that, uniformly for
> \(3\le q\le N\)

**Recorded location:** Report-writing event, 2026-07-19T18:54:14.287Z; P4 conjectured joint-histogram witness lemma.

**Context (annotation, not a source quotation):** The report explicitly labels this a conjectured asymptotic witness lemma and states that it has not been proved. The source-writing command uses the placeholder § for a backslash before saving.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The uncapped exponent is impossible at the top endpoint q=N.

### Argument or calculation

The proposed signed measure has unit l1 norm, correlation at least1/3+delta, and annihilates every query polynomial of degree below c0*sqrt(N)*q^eta. It would therefore force approximate degree Omega(N^(1/2+eta)) at q=N. A bounded-error quantum-walk algorithm uses O(N^(2/3)) queries for2-sum; constant-error amplification gives an approximating polynomial of degree O(N^(2/3)) at the required fixed accuracy. For eta>1/6, N^(1/2+eta) grows faster. This refutes the candidate as stated, not a claimed completed proof.

Scope: tentative_candidate_refuted.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: KSUM-L2-019f7bb0.jsonl](original/M01-KSUM-L2-019f7bb0.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/KSUM-L2-019f7bb0.jsonl") · [event data](original/M01-KSUM-L2-019f7bb0.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 244–264.
  - Relevant location(s): JSONL line 255 (successful exact report write; line 250 is a failed attempt); 255; 255 (2026-07-19T18:54:14.287Z; successful write)
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/KSUM-L2-019f7bb0.jsonl`

- [M02: KSUM-main-b5fea9c2.jsonl](original/M02-KSUM-main-b5fea9c2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl") · [event data](original/M02-KSUM-main-b5fea9c2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1721–1733.
  - Relevant location(s): 1727 (2026-07-19T19:11:28.790Z)
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl`

- [M03: KSUM_PROOF_DAG.md](original/M03-KSUM_PROOF_DAG.md "research/ksum/notes/KSUM_PROOF_DAG.md")
  - Coverage: Full bundled file; source lines 1–2730.
  - Relevant location(s): #B4bL2-phase-1-review
  - Source: `research/ksum/notes/KSUM_PROOF_DAG.md`
