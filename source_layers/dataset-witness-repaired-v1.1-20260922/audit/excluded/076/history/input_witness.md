# Record 076 — Quantum k-sum with small alphabets

**Review status:** `interpretation_check_pending`.

The quoted LP criterion is mathematically valid for the stated epsilon-approximate degree. Current ledger conflates approximation error with failure probability; an actual invalid transfer event is still required.

## Original statement and context

> The table gives the optimum correlation at each pure-high-degree band \(d\); bold entries exceed \(1/3\) and therefore certify \(\widetilde{\deg}_{1/3}\ge d\).

**Recorded location:** Report-writing event, 2026-07-19T18:54:14.287Z; P3 exact LP results.

**Context (annotation, not a source quotation):** The source explicitly uses sign-valued F and epsilon-approximate degree. A separate convention is needed to translate the polynomial approximation tolerance into a query algorithm's failure probability.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The supplied threshold criticism does not refute this quoted approximate-degree statement. It applies only to an unamplified direct transfer at query failure probability1/3.

### Argument or calculation

If p(x)=Pr[output1] and F(x)=2f(x)-1, then |p-f|<=1/3 gives |(2p-1)-F|<=2/3. A unit-l1 dual measure must have correlation>2/3 to contradict that particular approximant. But for epsilon=1/3 uniform polynomial approximation to F, correlation>1/3 is the correct dual threshold by |<mu,F-p>|<=||mu||1||F-p||infinity. Locate the claimed direct query transfer before counting this convention issue as an error.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: KSUM-L2-019f7bb0.jsonl](original/M01-KSUM-L2-019f7bb0.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/KSUM-L2-019f7bb0.jsonl") · [event data](original/M01-KSUM-L2-019f7bb0.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 244–264.
  - Relevant location(s): JSONL line 255 (successful exact report write; line 250 is a failed attempt); 255; 255 (2026-07-19T18:54:14.287Z; successful write)
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/codex/KSUM-L2-019f7bb0.jsonl`

- [M02: KSUM-main-b5fea9c2.jsonl](original/M02-KSUM-main-b5fea9c2.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl") · [event data](original/M02-KSUM-main-b5fea9c2.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1718–1730.
  - Relevant location(s): 1724 and :1727
  - Source: `paper/evidence_claim_gap_20260918/recovery_windows_ssd_20260918/raw/claude/KSUM-main-b5fea9c2.jsonl`

- [M03: KSUM_PROOF_DAG.md](original/M03-KSUM_PROOF_DAG.md "research/ksum/notes/KSUM_PROOF_DAG.md")
  - Coverage: Full bundled file; source lines 1–2730.
  - Relevant location(s): #B4bL2-threshold-repair
  - Source: `research/ksum/notes/KSUM_PROOF_DAG.md`
