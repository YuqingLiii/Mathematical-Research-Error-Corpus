# Record 034 — Circuit versus effective distance

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> > In graph-like detector error models with fixed boundaries, a proven necessary-and-sufficient
> > structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when
> > d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma
> > of the length of the shortest closed spacetime lift of gamma", with zero time-direction
> > voltage/monodromy as the equal-weight liftability condition; the criterion recovers the
> > non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit
> > interleaved example with d_circ > d_eff.

**Recorded location:** Root assembly dated 22 August 2026, root statement, lines 121–127; imported criterion in section 2.1.

**Context (annotation, not a source quotation):** An assembly imported a proved-under-assumptions equality criterion from a child theorem into an unrestricted root statement. The original child theorem explicitly assumes a memory experiment with R≥d rounds.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The premise R≥d is lost in the root statement and its carried-forward caveats. An implication established under that hypothesis does not by itself establish the same implication for every round count.

### Argument or calculation

The assembly restates the imported result as: for every legal, measurement-consistent schedule M and R≥d, d_circ(C_R(M))=d_eff(M) iff a minimum effective logical γ has repair(γ)=0. Its root claim instead says the structural criterion characterizes d_circ=d_eff without an R quantifier or restriction. None of the assembly's listed caveats restores R≥d. This is a direct premise-versus-conclusion scope mismatch. The independent audit found no counterexample at R=1 on its d=2 test instance, so the witness invalidates the unrestricted inference, not the theorem for small R.

Scope: argument_invalid.


### Archived review excerpt

> The assembly's own restatement of the certified criterion (§2.1) reads:
> 
> > "For every legal, measurement-consistent single-ancilla CSS schedule `M`, **and `R ≥ d`**,
> > `d_circ(C_R(M)) = d_eff(M) ⟺ ∃γ ∈ L_eff` with `|γ| = d_eff(M)` and `repair(γ) = 0`."
> 
> I checked the source: iff CONJECTURED 5.7 does carry `R ≥ d`. But:
> 
> * the **root claim** has no `R` quantifier and no `C_R(M)` — it says "characterizes when
>   `d_circ = d_eff`", unrestricted;
> * the **`lift.iff` child claim** has no `R` quantifier either;
> * §6 of the assembly — the section whose entire job is "every caveat carried forward, none may be
>   dropped by a promotion of the root" — lists C-R1..3, C-M1..6, C-S1..3, C-O1..6 and **`R ≥ d` is
>   in none of them**. It appears once, in §2.1, and never again.
> 
> This is exactly the failure mode §0.3 was written to prevent, applied to the assembly itself. I
> probed for a live counterexample and did not find one at `d = 2`: my enumeration gives
> `d_circ = 2` for the interleaved witness and `1` for its non-interleaved partner at `R = 1` as
> well as `R ≥ 2`, so `R ≥ d` is not demonstrably load-bearing *on this instance*. That does not
> discharge it — a hypothesis of the certified theorem is a hypothesis of anything assembled from
> it, and `d_R` is only known to be non-increasing and constant for `R ≥ d`.
>

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 子节点及组装推理分散提到 MC、R 条件；安装到根定理时的遗漏可由工件看出，但没有完整同一生成节点的推理对照来确定形成阶段。

- [2026-08-22T21:32:37.672Z — claude_visible_thinking](original/M04-agent-a54f4eb22e936ab7c.jsonl.readable.md) — source line 42; recorded role: generation.
- [2026-08-22T21:35:14.406Z — claude_visible_thinking](original/M04-agent-a54f4eb22e936ab7c.jsonl.readable.md) — source line 59; recorded role: generation.

## Original materials

- [M01: circdist_lift_root_assembly_20260822.md](original/M01-circdist_lift_root_assembly_20260822.md "research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md")
  - Coverage: Full bundled file; source lines 1–931.
  - Relevant location(s): lines 121–127; #2.1,6
  - Source: `research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md`

- [M02: circdist_lift_root_review_20260822.md](original/M02-circdist_lift_root_review_20260822.md "research-graph/circdist/reviews/circdist_lift_root_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–498.
  - Relevant location(s): §4.2; lines 302–322; #4.2
  - Source: `research-graph/circdist/reviews/circdist_lift_root_review_20260822.md`

- [M03: circdist_lift_iff_proof_20260820.md](original/M03-circdist_lift_iff_proof_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): #5.7
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md`

- [M04: agent-a54f4eb22e936ab7c.jsonl](original/M04-agent-a54f4eb22e936ab7c.jsonl.readable.md "claude-session-archive/agent-a54f4eb22e936ab7c.jsonl") · [event data](original/M04-agent-a54f4eb22e936ab7c.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 36–48, 53–65.
  - Relevant location(s): lines 42; lines 59
  - Source: `claude-session-archive/agent-a54f4eb22e936ab7c.jsonl`

- [M05: CIRCDIST.lift.yaml](original/M05-CIRCDIST.lift.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml")
  - Coverage: Full bundled file; source lines 1–198.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml`

- [M06: CIRCDIST.lift.iff.yaml](original/M06-CIRCDIST.lift.iff.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml")
  - Coverage: Full bundled file; source lines 1–188.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml`

- [M07: CIRCDIST.lift.nonint.yaml](original/M07-CIRCDIST.lift.nonint.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml")
  - Coverage: Full bundled file; source lines 1–94.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml`

- [M08: CIRCDIST.lift.gap-example.yaml](original/M08-CIRCDIST.lift.gap-example.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.gap-example.yaml")
  - Coverage: Full bundled file; source lines 1–107.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.gap-example.yaml`

- [M09: circdist_lift_iff_proof_20260820.md](original/M09-circdist_lift_iff_proof_20260820.md "artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_lift_iff_proof_20260820.md`

- [M10: circdist_lift_iff_amendment1_20260820.md](original/M10-circdist_lift_iff_amendment1_20260820.md "artifacts/circdist_lift_iff_amendment1_20260820.md")
  - Coverage: Full bundled file; source lines 1–619.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_lift_iff_amendment1_20260820.md`

- [M11: circdist_lift_iff_amendment2_20260820.md](original/M11-circdist_lift_iff_amendment2_20260820.md "artifacts/circdist_lift_iff_amendment2_20260820.md")
  - Coverage: Full bundled file; source lines 1–240.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_lift_iff_amendment2_20260820.md`

- [M12: circdist_lift_nonint_proof_20260820.md](original/M12-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M13: circdist_lift_proofs_review_20260820.md](original/M13-circdist_lift_proofs_review_20260820.md "artifacts/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_lift_proofs_review_20260820.md`

- [M14: circdist_amendments_review_20260820.md](original/M14-circdist_amendments_review_20260820.md "artifacts/circdist_amendments_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–571.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_amendments_review_20260820.md`

- [M15: circdist_amendments2_review_20260820.md](original/M15-circdist_amendments2_review_20260820.md "artifacts/circdist_amendments2_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–362.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `artifacts/circdist_amendments2_review_20260820.md`

- [M16: circdist_numerical_review_20260820.md](original/M16-circdist_numerical_review_20260820.md "artifacts/circdist_numerical_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–2246.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_numerical_review_20260820.md`

- [M17: circdist_lift_d3gate_20260820.md](original/M17-circdist_lift_d3gate_20260820.md "artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_d3gate_20260820.md`

- [M18: CIRCDIST_PROBLEMS.md](original/M18-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M19: circdist_lift_root_assembly_20260822.md](original/M19-circdist_lift_root_assembly_20260822.md "artifacts/circdist_lift_root_assembly_20260822.md")
  - Coverage: Full bundled file; source lines 1–931.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `artifacts/circdist_lift_root_assembly_20260822.md`

- [M20: proof_dag_v6.py](original/M20-proof_dag_v6.py "tools/proof_dag_v6.py")
  - Coverage: Full bundled file; source lines 1–841.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `tools/proof_dag_v6.py`

- [M21: ksum_L2_phase27_shared_no_rule7_review_20260721.md](original/M21-ksum_L2_phase27_shared_no_rule7_review_20260721.md "artifacts/ksum_L2_phase27_shared_no_rule7_review_20260721.md")
  - Coverage: Full bundled file; source lines 1–520.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `artifacts/ksum_L2_phase27_shared_no_rule7_review_20260721.md`

- [M22: circdist_lift_litverify2_20260820.md](original/M22-circdist_lift_litverify2_20260820.md "artifacts/circdist_lift_litverify2_20260820.md")
  - Coverage: Full bundled file; source lines 1–55.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_litverify2_20260820.md`
