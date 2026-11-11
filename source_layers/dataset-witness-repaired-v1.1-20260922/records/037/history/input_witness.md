# Record 037 — Optimal circuit distance of the Gross code

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> `T = 6` UNSAT is the sharp statement: **the gross code has no measurement-consistent
> single-ancilla SEC with six CNOT layers at all** — a 55-second exact result over the full
> 864-edge scheduling problem, with no assumption on the within-check orders, no tiling and no
> symmetry. Rows beyond the first are whatever closed inside the box.

**Recorded location:** Proof draft dated 20 August 2026, section 2.4(5), lines 315–318.

**Context (annotation, not a source quotation):** An UNSAT result from a scheduling encoding was promoted to a universal nonexistence statement. The encoding put both ancilla families entirely within one round window, whereas the schedule class under discussion permits ancilla lifetimes crossing period boundaries.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The verified search covered only unstaggered ancilla windows. Removing that restriction from the conclusion excludes legitimate staggered schedules without evidence.

### Argument or calculation

Use the Gross left/right check blocks L_X=A, R_X=B, L_Z=B^T, R_Z=A^T, each of degree three. In CNOT layers 0,1,2 run L_X in parallel with R_Z; in layers 3,4,5 run R_X in parallel with L_Z. Each layer is a matching. The X ancilla for period p lives within p; the Z ancilla labelled p is prepared before layer 3 of p and measured after layer 2 of p+1. This gives six CNOT layers per period (864 CNOTs). For each of the 648 overlapping pairs, the MC counts for X_p against Z_p and Z_{p−1} are respectively 0 and 2, both even. The archived independent simulation also found all detectors deterministic in both memory sectors. This contradicts the unqualified six-layer impossibility, not the UNSAT result for the narrower unstaggered encoding.

Scope: statement_false.


### Archived review excerpt

> 
> ### 5.3 The counterexample, built and checked
> 
> `lrc6.py` builds SBB's staggered LRC literally: block 1 (layers 0,1,2) runs `L_X ∥ R_Z`, block 2
> (layers 3,4,5) runs `R_X ∥ L_Z`; the X ancilla of period `p` lives inside period `p`; the Z ancilla
> instance `p` is prepared before layer 3 of period `p` and measured after layer 2 of period `p+1`.
> Every layer is asserted to be a matching (6 CNOT layers per period, 864 CNOTs per period). The
> within-check orders are then left-block-then-right-block for both types.
> 
> Evaluating the target's own (MC) parity on **absolute** times, for both staggered pairings:
> 
> ```
> overlapping (X,Z) pairs            : 648
> odd-parity pairs, X_p vs Z_p       : 0
> odd-parity pairs, X_p vs Z_{p-1}   : 0
> ```
> 
> and handing the circuit to `stim` 1.16.0:
> 
> ```
> stim, X-memory : 288 qubits, 504 detectors, 6 CNOT layers per period
>                  DEM BUILT OK -> all detectors deterministic. 14472 error mechanisms
>                  noiseless detector firings: 0 / 504
> stim, Z-memory : 288 qubits, 576 detectors, 6 CNOT layers per period
>                  DEM BUILT OK -> all detectors deterministic. 19656 error mechanisms
>                  noiseless detector firings: 0 / 576
> ```
> 
> The reason is a one-line computation the target's model cannot express. With shared qubits split
> one-left/one-right, for `X_p` versus `Z_p` both shared CNOTs of `Z` come *after* both of `X`
> (`c = 0`); for `X_p` versus `Z_{p−1}` both come *before* (`c = 2`). Even in both cases. The
> target's §7(7) correction — "with the shared pair split one-per-half, that pattern gives `c_ab = 1`
> for all 648 overlapping pairs — maximally measurement-inconsistent" — is the *unstaggered* pairing
> only, and staggering is precisely what removes it.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 受限编码的 UNSAT 在推理里已经被解释为一般六 CNOT 层不存在；后续写入重复这个范围扩张。并非 SAT 求解器返回错误。

- [2026-08-20T18:39:11.131Z — claude_visible_thinking](original/M06-agent-ace09be0f0bec8908.jsonl.readable.md) — source line 361; recorded role: generation.

## Original materials

- [M01: circdist_gross_sbbcert_20260820.md](original/M01-circdist_gross_sbbcert_20260820.md "artifacts/circdist_gross_sbbcert_20260820.md")
  - Coverage: Full bundled file; source lines 1–2910.
  - Relevant location(s): lines 315–318; Referenced by research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md
  - Source: `artifacts/circdist_gross_sbbcert_20260820.md`

- [M02: circdist_sbbcert_review_20260820.md](original/M02-circdist_sbbcert_review_20260820.md "research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–580.
  - Relevant location(s): §5.2; lines 296–329; #5.2,5.3; #5
  - Source: `research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md`

- [M03: sched.py](original/M03-sched.py "research-graph/circdist/artifacts/logs_circdist_gross_verdictreview_20260823/work/sched.py")
  - Coverage: Full bundled file; source lines 1–144.
  - Source: `research-graph/circdist/artifacts/logs_circdist_gross_verdictreview_20260823/work/sched.py`

- [M04: stimcheck.py](original/M04-stimcheck.py "research-graph/circdist/artifacts/logs_circdist_gross_verdictreview_20260823/work/stimcheck.py")
  - Coverage: Full bundled file; source lines 1–98.
  - Source: `research-graph/circdist/artifacts/logs_circdist_gross_verdictreview_20260823/work/stimcheck.py`

- [M05: noclass.py](original/M05-noclass.py "research-graph/circdist/artifacts/logs_circdist_gross_verdictreview_20260823/work/noclass.py")
  - Coverage: Full bundled file; source lines 1–20.
  - Source: `research-graph/circdist/artifacts/logs_circdist_gross_verdictreview_20260823/work/noclass.py`

- [M06: agent-ace09be0f0bec8908.jsonl](original/M06-agent-ace09be0f0bec8908.jsonl.readable.md "claude-session-archive/agent-ace09be0f0bec8908.jsonl") · [event data](original/M06-agent-ace09be0f0bec8908.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 355–367, 399–411.
  - Relevant location(s): lines 361; lines 405
  - Source: `claude-session-archive/agent-ace09be0f0bec8908.jsonl`

- [M07: circdist_gross_g1_20260820.md](original/M07-circdist_gross_g1_20260820.md "artifacts/circdist_gross_g1_20260820.md")
  - Coverage: Full bundled file; source lines 1–2193.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_gross_g1_20260820.md`

- [M08: CIRCDIST_PROBLEMS.md](original/M08-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md; Referenced by research-graph/circdist/reviews/circdist_sbbcert_review_20260820.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M09: circdist_lift_d3gate_20260820.md](original/M09-circdist_lift_d3gate_20260820.md "artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_lift_d3gate_20260820.md`

- [M10: circdist_lift_nonint_proof_20260820.md](original/M10-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M11: circdist_lift_proofs_review_20260820.md](original/M11-circdist_lift_proofs_review_20260820.md "artifacts/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_lift_proofs_review_20260820.md`

- [M12: circdist_gross_toolfeas_20260820.md](original/M12-circdist_gross_toolfeas_20260820.md "artifacts/circdist_gross_toolfeas_20260820.md")
  - Coverage: Full bundled file; source lines 1–62.
  - Relevant location(s): Referenced by artifacts/circdist_gross_sbbcert_20260820.md
  - Source: `artifacts/circdist_gross_toolfeas_20260820.md`
