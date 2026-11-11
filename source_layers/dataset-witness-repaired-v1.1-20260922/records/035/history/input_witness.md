# Record 035 — Circuit versus effective distance

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> *Derivation.* Take an optimal certificate `(r_i, u_i)`. For each `i` choose a fault `f_i` with
> `E(f_i) = E_i` and `u(f_i) = u_i` (one exists, by definition of `U(E_i)`) and place it in round
> `r_i`; these are `w = |γ|` distinct circuit locations, since distinct residuals force distinct
> locations. Their detector chain is `(1+x)(A_0 + xC)` by 4.2. Let `D := A_0 + xC ∈ V` and write

**Recorded location:** Proof draft dated 20 August 2026, derivation of Lemma 5.3, lines 672–675.

**Context (annotation, not a source quotation):** To construct a circuit lift, the draft chooses one elementary fault for each distinct effective residual and treats those choices as faults at distinct physical locations. The fault model allows only one Pauli assignment per location.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Distinct propagated residuals do not identify distinct locations: different Pauli faults at one CNOT location can produce different residuals. The proposed representative-by-representative construction therefore does not automatically yield a legal fault configuration.

### Argument or calculation

At a single ancilla-to-data CNOT a→q_j, the draft's own Proposition 1.13(4) lists possible residuals ∅, S_j, {q_j}, S_{j−1}. Here S_j is the subsequent data suffix and S_{j−1}=S_j⊕{q_j}. Choosing the ancilla-X and data-X faults for S_j and {q_j} selects the same physical location twice. Their product is one X⊗X fault of cost one with residual S_{j−1}, not two occupied locations. The formal effective basis vector [S_{j−1}] also need not equal [S_j]+[{q_j}]. This refutes the distinct-location inference; a repaired existence proof requires a collision argument.

Scope: argument_invalid.


### Archived review excerpt

> > "these are `w = |γ|` distinct circuit locations, since **distinct residuals force distinct
> > locations**."
> 
> This is false, and the document proves it false three pages earlier. Its own Proposition 1.13.4
> reads:
> 
> > "on a gate `a→q_j` the possible residuals are `∅, S_j, {q_j}, S_{j−1}`"
> 
> — four distinct residuals at one location. Since Definition 1.8 (and the frozen fault model) puts
> **one Pauli per location**, two of those cannot be placed as two weight-1 faults; the `X⊗X`
> composite is a *single* weight-1 fault whose residual is `S_{j−1}`, and whose `π₁` image is the
> basis vector `[S_{j−1}]`, not `[S_j] + [{q_j}]`.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 推理明确认定不同 residual 必须来自不同故障位置；正文重复这一步。单个二比特门的不同 Pauli 故障能产生不同 residual。

- [2026-08-20T15:54:10.293Z — claude_visible_thinking](original/M04-agent-afd9b18b206ce896f.jsonl.readable.md) — source line 18; recorded role: generation.

## Original materials

- [M01: circdist_lift_iff_proof_20260820.md](original/M01-circdist_lift_iff_proof_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): lines 672–675; #L250-252 (Prop1.13(4)), L668-681 (5.3), Def5.1
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md`

- [M02: circdist_lift_proofs_review_20260820.md](original/M02-circdist_lift_proofs_review_20260820.md "research-graph/circdist/reviews/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): §3.2; lines 161–172; #3.1,3.2; #3.2
  - Source: `research-graph/circdist/reviews/circdist_lift_proofs_review_20260820.md`

- [M03: circdist_lift_nonint_proof_20260820.md](original/M03-circdist_lift_nonint_proof_20260820.md "research-graph/circdist/artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): #Def2.8,Lemma7.2
  - Source: `research-graph/circdist/artifacts/circdist_lift_nonint_proof_20260820.md`

- [M04: agent-afd9b18b206ce896f.jsonl](original/M04-agent-afd9b18b206ce896f.jsonl.readable.md "claude-session-archive/agent-afd9b18b206ce896f.jsonl") · [event data](original/M04-agent-afd9b18b206ce896f.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 12–24, 50–62.
  - Relevant location(s): lines 18; lines 56
  - Source: `claude-session-archive/agent-afd9b18b206ce896f.jsonl`

- [M05: CIRCDIST_PROBLEMS.md](original/M05-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md; Referenced by research-graph/circdist/reviews/circdist_lift_proofs_review_20260820.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M06: circdist_lift_litverify2_20260820.md](original/M06-circdist_lift_litverify2_20260820.md "artifacts/circdist_lift_litverify2_20260820.md")
  - Coverage: Full bundled file; source lines 1–55.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_litverify2_20260820.md`

- [M07: circdist_lift_nonint_proof_20260820.md](original/M07-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M08: circdist_lift_d3gate_20260820.md](original/M08-circdist_lift_d3gate_20260820.md "artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_d3gate_20260820.md`
