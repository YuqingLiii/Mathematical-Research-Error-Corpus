# Record 068 — Circuit versus effective distance

**Review status:** `interpretation_check_pending`.

The original does not contain the literal alleged equation 'the voltage set equals zero'; it uses an underspecified phrase and the same assembly supplies its intended interpretation. Decide whether this is an admissible mathematical error rather than wording/type ambiguity before counting it as a positive record.

## Original statement and context

> > In graph-like detector error models with fixed boundaries, a proven necessary-and-sufficient
> > structural criterion (in graph-covering, voltage-graph, or chain-complex form) characterizes when
> > d_circ = d_eff, of the shape "d_circ equals the minimum over nontrivial effective logicals gamma
> > of the length of the shortest closed spacetime lift of gamma", with zero time-direction
> > voltage/monodromy as the equal-weight liftability condition; the criterion recovers the
> > non-interleaved equality d_circ = d_eff as a corollary and is accompanied by an explicit
> > interleaved example with d_circ > d_eff.

**Recorded location:** Root assembly dated 22 August 2026, verbatim root statement, lines 121–127.

**Context (annotation, not a source quotation):** The root statement describes equal-weight liftability through 'zero time-direction voltage/monodromy'. In the constructed model each effective residual may have several circuit representatives with different detector voltages.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

A zero criterion must specify the choice of a circuit representative and the round assignment. The archived critique identifies a type/definition ambiguity, not an actual source equation asserting that a voltage set literally equals the scalar zero.

### Argument or calculation

In the archived [[4,2,2]] example, the residual E={0} has voltage spectrum U(E)={0,1}; the same effective residual admits both voltage values. Thus no unique scalar voltage is determined by E alone. A same-weight lift criterion can quantify over u∈U(E) and round assignments, or use a minimum repair cost. It cannot silently equate 'all available voltages vanish' with 'some zero-repair realization exists'. The assembly itself explicitly explains this distinction and says the clause is substantively discharged but verbally imprecise.

Scope: argument_invalid.


### Archived review excerpt

> **The correction.** The root says "*zero* time-direction voltage/monodromy", which reads as the
> vanishing of a single well-defined quantity attached to `γ`. It is not one. Because a residual `E`
> admits a *set* `U(E)` of unit-weight voltages, the voltage of `γ` is a set, and the liftability
> condition is a **minimum over that set and over round assignments** being zero, not the vanishing
> of a scalar. §7 R2 proposes the minimal rewording. Substantively the clause is discharged; verbally
> it overstates the sharpness of the object.

## Visible CoT summaries and reasoning excerpts

The original visible text is retained in the linked source events below. These are not complete internal chains of thought; generation/review roles and alignment notes are inherited from the supplied archive.

**Alignment note (inherited):** 根节点组装者的推理解释了 voltage spectrum 上取最小值，属于对给定问题的重述/修正语境；未绑定最早把集合写成零的生成事件。

- [2026-08-22T21:32:37.672Z — claude_visible_thinking](original/M05-agent-a54f4eb22e936ab7c.jsonl.readable.md) — source line 42; recorded role: assembly_or_correction.
- [2026-08-22T21:35:14.406Z — claude_visible_thinking](original/M05-agent-a54f4eb22e936ab7c.jsonl.readable.md) — source line 59; recorded role: assembly_or_correction.

## Original materials

- [M01: circdist_lift_root_assembly_20260822.md](original/M01-circdist_lift_root_assembly_20260822.md "research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md")
  - Coverage: Full bundled file; source lines 1–931.
  - Relevant location(s): lines 121–127; lines 257–262
  - Source: `research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md`

- [M02: circdist_lift_root_review_20260822.md](original/M02-circdist_lift_root_review_20260822.md "research-graph/circdist/reviews/circdist_lift_root_review_20260822.md")
  - Coverage: Full bundled file; source lines 1–498.
  - Relevant location(s): §5 R2 / set-valued voltage; #5-R2,3.5
  - Source: `research-graph/circdist/reviews/circdist_lift_root_review_20260822.md`

- [M03: circdist_lift_iff_proof_20260820.md](original/M03-circdist_lift_iff_proof_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): #9.3,Prop1.13; Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md`

- [M04: CIRCDIST.lift.iff.yaml](original/M04-CIRCDIST.lift.iff.yaml "research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml")
  - Coverage: Full bundled file; source lines 1–170.
  - Relevant location(s): #claim
  - Source: `research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml`

- [M05: agent-a54f4eb22e936ab7c.jsonl](original/M05-agent-a54f4eb22e936ab7c.jsonl.readable.md "claude-session-archive/agent-a54f4eb22e936ab7c.jsonl") · [event data](original/M05-agent-a54f4eb22e936ab7c.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 36–48, 53–65.
  - Relevant location(s): lines 42; lines 59
  - Source: `claude-session-archive/agent-a54f4eb22e936ab7c.jsonl`

- [M06: CIRCDIST.lift.yaml](original/M06-CIRCDIST.lift.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml")
  - Coverage: Full bundled file; source lines 1–198.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.yaml`

- [M07: CIRCDIST.lift.iff.yaml](original/M07-CIRCDIST.lift.iff.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml")
  - Coverage: Full bundled file; source lines 1–188.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml`

- [M08: CIRCDIST.lift.nonint.yaml](original/M08-CIRCDIST.lift.nonint.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml")
  - Coverage: Full bundled file; source lines 1–94.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.nonint.yaml`

- [M09: CIRCDIST.lift.gap-example.yaml](original/M09-CIRCDIST.lift.gap-example.yaml "research/circdist/proof-dag/nodes/CIRCDIST.lift.gap-example.yaml")
  - Coverage: Full bundled file; source lines 1–107.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `research/circdist/proof-dag/nodes/CIRCDIST.lift.gap-example.yaml`

- [M10: circdist_lift_iff_proof_20260820.md](original/M10-circdist_lift_iff_proof_20260820.md "artifacts/circdist_lift_iff_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–1498.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_lift_iff_proof_20260820.md`

- [M11: circdist_lift_iff_amendment1_20260820.md](original/M11-circdist_lift_iff_amendment1_20260820.md "artifacts/circdist_lift_iff_amendment1_20260820.md")
  - Coverage: Full bundled file; source lines 1–619.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_lift_iff_amendment1_20260820.md`

- [M12: circdist_lift_iff_amendment2_20260820.md](original/M12-circdist_lift_iff_amendment2_20260820.md "artifacts/circdist_lift_iff_amendment2_20260820.md")
  - Coverage: Full bundled file; source lines 1–240.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_lift_iff_amendment2_20260820.md`

- [M13: circdist_lift_nonint_proof_20260820.md](original/M13-circdist_lift_nonint_proof_20260820.md "artifacts/circdist_lift_nonint_proof_20260820.md")
  - Coverage: Full bundled file; source lines 1–943.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_nonint_proof_20260820.md`

- [M14: circdist_lift_proofs_review_20260820.md](original/M14-circdist_lift_proofs_review_20260820.md "artifacts/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_lift_proofs_review_20260820.md`

- [M15: circdist_amendments_review_20260820.md](original/M15-circdist_amendments_review_20260820.md "artifacts/circdist_amendments_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–571.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_amendments_review_20260820.md`

- [M16: circdist_amendments2_review_20260820.md](original/M16-circdist_amendments2_review_20260820.md "artifacts/circdist_amendments2_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–362.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `artifacts/circdist_amendments2_review_20260820.md`

- [M17: circdist_numerical_review_20260820.md](original/M17-circdist_numerical_review_20260820.md "artifacts/circdist_numerical_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–2246.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md
  - Source: `artifacts/circdist_numerical_review_20260820.md`

- [M18: circdist_lift_d3gate_20260820.md](original/M18-circdist_lift_d3gate_20260820.md "artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_d3gate_20260820.md`

- [M19: CIRCDIST_PROBLEMS.md](original/M19-CIRCDIST_PROBLEMS.md "research/circdist/notes/CIRCDIST_PROBLEMS.md")
  - Coverage: Full bundled file; source lines 1–244.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `research/circdist/notes/CIRCDIST_PROBLEMS.md`

- [M20: circdist_lift_root_assembly_20260822.md](original/M20-circdist_lift_root_assembly_20260822.md "artifacts/circdist_lift_root_assembly_20260822.md")
  - Coverage: Full bundled file; source lines 1–931.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_root_assembly_20260822.md; Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `artifacts/circdist_lift_root_assembly_20260822.md`

- [M21: proof_dag_v6.py](original/M21-proof_dag_v6.py "tools/proof_dag_v6.py")
  - Coverage: Full bundled file; source lines 1–841.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `tools/proof_dag_v6.py`

- [M22: ksum_L2_phase27_shared_no_rule7_review_20260721.md](original/M22-ksum_L2_phase27_shared_no_rule7_review_20260721.md "artifacts/ksum_L2_phase27_shared_no_rule7_review_20260721.md")
  - Coverage: Full bundled file; source lines 1–520.
  - Relevant location(s): Referenced by research-graph/circdist/reviews/circdist_lift_root_review_20260822.md
  - Source: `artifacts/ksum_L2_phase27_shared_no_rule7_review_20260721.md`

- [M23: circdist_lift_litverify2_20260820.md](original/M23-circdist_lift_litverify2_20260820.md "artifacts/circdist_lift_litverify2_20260820.md")
  - Coverage: Full bundled file; source lines 1–55.
  - Relevant location(s): Referenced by research-graph/circdist/artifacts/circdist_lift_iff_proof_20260820.md
  - Source: `artifacts/circdist_lift_litverify2_20260820.md`

- [M24: circdist_lift_proofs_review_20260820.md](original/M24-circdist_lift_proofs_review_20260820.md "research-graph/circdist/reviews/circdist_lift_proofs_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–704.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_lift_proofs_review_20260820.md`

- [M25: circdist_stim_crossval_20260823.md](original/M25-circdist_stim_crossval_20260823.md "research-graph/artifacts/circdist_stim_crossval_20260823.md")
  - Coverage: Full bundled file; source lines 1–439.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/artifacts/circdist_stim_crossval_20260823.md`

- [M26: circdist_iff_scope_adjudication_20260823.md](original/M26-circdist_iff_scope_adjudication_20260823.md "research-graph/artifacts/circdist_iff_scope_adjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–449.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/artifacts/circdist_iff_scope_adjudication_20260823.md`

- [M27: circdist_iff_endtoend_review_20260823.md](original/M27-circdist_iff_endtoend_review_20260823.md "research-graph/circdist/reviews/circdist_iff_endtoend_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–512.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_iff_endtoend_review_20260823.md`

- [M28: circdist_iff_amendment3_review_20260823.md](original/M28-circdist_iff_amendment3_review_20260823.md "research-graph/circdist/reviews/circdist_iff_amendment3_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–325.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_iff_amendment3_review_20260823.md`

- [M29: circdist_amendments2_review_20260820.md](original/M29-circdist_amendments2_review_20260820.md "research-graph/circdist/reviews/circdist_amendments2_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–362.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_amendments2_review_20260820.md`

- [M30: circdist_lift_claimrepair2_review_20260823.md](original/M30-circdist_lift_claimrepair2_review_20260823.md "research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md")
  - Coverage: Full bundled file; source lines 1–477.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_lift_claimrepair2_review_20260823.md`

- [M31: circdist_lift_iff_amendment1_20260820.md](original/M31-circdist_lift_iff_amendment1_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_amendment1_20260820.md")
  - Coverage: Full bundled file; source lines 1–619.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_amendment1_20260820.md`

- [M32: circdist_lift_iff_amendment2_20260820.md](original/M32-circdist_lift_iff_amendment2_20260820.md "research-graph/circdist/artifacts/circdist_lift_iff_amendment2_20260820.md")
  - Coverage: Full bundled file; source lines 1–240.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_amendment2_20260820.md`

- [M33: circdist_lift_iff_amendment3_20260823.md](original/M33-circdist_lift_iff_amendment3_20260823.md "research-graph/circdist/artifacts/circdist_lift_iff_amendment3_20260823.md")
  - Coverage: Full bundled file; source lines 1–1389.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_amendment3_20260823.md`

- [M34: circdist_lift_iff_amendment4_20260823.md](original/M34-circdist_lift_iff_amendment4_20260823.md "research-graph/circdist/artifacts/circdist_lift_iff_amendment4_20260823.md")
  - Coverage: Full bundled file; source lines 1–921.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_iff_amendment4_20260823.md`

- [M35: circdist_iff_scope_adjudication_20260823.md](original/M35-circdist_iff_scope_adjudication_20260823.md "research-graph/circdist/reviews/circdist_iff_scope_adjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–449.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_iff_scope_adjudication_20260823.md`

- [M36: CIRCDIST.lift.iff.yaml](original/M36-CIRCDIST.lift.iff.yaml "research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.lift.iff.yaml")
  - Coverage: Full bundled file; source lines 1–455.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/history/pre_protocol_20260826/nodes/CIRCDIST.lift.iff.yaml`

- [M37: circdist_readjudication_20260823.md](original/M37-circdist_readjudication_20260823.md "research-graph/circdist/reviews/circdist_readjudication_20260823.md")
  - Coverage: Full bundled file; source lines 1–617.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_readjudication_20260823.md`

- [M38: circdist_amendments_review_20260820.md](original/M38-circdist_amendments_review_20260820.md "research-graph/circdist/reviews/circdist_amendments_review_20260820.md")
  - Coverage: Full bundled file; source lines 1–571.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_amendments_review_20260820.md`

- [M39: circdist_lift_d3gate_20260820.md](original/M39-circdist_lift_d3gate_20260820.md "research-graph/circdist/artifacts/circdist_lift_d3gate_20260820.md")
  - Coverage: Full bundled file; source lines 1–1170.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_d3gate_20260820.md`

- [M40: circdist_lift_litverify2_20260820.md](original/M40-circdist_lift_litverify2_20260820.md "research-graph/circdist/artifacts/circdist_lift_litverify2_20260820.md")
  - Coverage: Full bundled file; source lines 1–55.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_litverify2_20260820.md`

- [M41: circdist_lift_recon_20260820.md](original/M41-circdist_lift_recon_20260820.md "research-graph/circdist/artifacts/circdist_lift_recon_20260820.md")
  - Coverage: Full bundled file; source lines 1–679.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/circdist_lift_recon_20260820.md`

- [M42: legacy_DAG_PROTOCOL.md](original/M42-legacy_DAG_PROTOCOL.md "research-graph/circdist/artifacts/history/legacy_DAG_PROTOCOL.md")
  - Coverage: Full bundled file; source lines 1–254.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/artifacts/history/legacy_DAG_PROTOCOL.md`

- [M43: circdist_stim_crossval_20260823.md](original/M43-circdist_stim_crossval_20260823.md "research-graph/circdist/reviews/circdist_stim_crossval_20260823.md")
  - Coverage: Full bundled file; source lines 1–439.
  - Relevant location(s): Referenced by research-graph/circdist/proof-dag/nodes/CIRCDIST.lift.iff.yaml
  - Source: `research-graph/circdist/reviews/circdist_stim_crossval_20260823.md`
