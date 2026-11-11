# Record 055 — Finite-dimensional Grothendieck bounds

**Review status:** `source_reviewed`.

The premise's identity is bound to the same archived bundle cited by the original route, not inferred from a later curator label. The referenced_definition field joins two explicitly separated verbatim excerpts of its constructor docstring.

## Original statement and context

> A feasible unrestricted degree-4 moment/SOS dual whose objective equals the stated integer is a global upper bound on the sign optimization problem.

**Recorded location:** Exact proof-node creation event, 2026-08-30T01:29:22.886Z; first event. Referenced archived system constructor, Mathematics represented by the output, lines22–45; archived JSON normalization and feasibility fields.

**Context (annotation, not a source quotation):** The implication names the full 746825-coordinate system with 20 PSD blocks as its premise and directly cites the archived system constructor. That constructor defines a moment functional L, with theta_empty=L(1), and imposes C*theta_empty-sum_t objective_B[t]*theta_t=-1. Thus the specifically referenced feasibility problem has L(f)=-1 for f=C-a^T A b; it is a separating moment problem, not an upper-bounding SOS certificate. The generic statement about a correctly oriented SOS dual is not the error.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

The direction of the moment/SOS separation was reversed.

### Argument or calculation

If a degree-four functional L is nonnegative on every allowed square and respects the Boolean relations, then any SOS representation f=sum_j p_j^2 modulo those relations implies L(f)=sum_j L(p_j^2)>=0. A feasible separating functional with L(f)<0 therefore excludes that SOS representation; it does not prove f>=0 on Boolean inputs. Such separation also need not supply an actual negative Boolean input.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: GROTH-H4-001-duality-direction.jsonl](original/M01-GROTH-H4-001-duality-direction.jsonl.readable.md "paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GROTH-H4-001-duality-direction.jsonl") · [event data](original/M01-GROTH-H4-001-duality-direction.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 1–10.
  - Relevant location(s): slice lines 1-2 original 7140-7141 create the wrong-direction DAG node; slice lines 3-9 original 7983-7985, 8002-8003, 8008-8009 diagnose, repair, format-fix, and validate; 1-2; original lines 7140-7141; 1-2; original lines 7140-7141 (2026-08-30T01:29:22.886Z / 2026-08-29 21:29:22.886 EDT); 3-9; original lines 7983-7985, 8002-8003, 8008-8009 (main repair at 2026-08-30T02:31:16.464Z)
  - Source: `paper/evidence_claim_gap_20260918/recovery_macstudio_august_sessions_20260918/raw/codex/GROTH-H4-001-duality-direction.jsonl`

- [M02: h4_full_invariant_dual_spec.py](original/M02-h4_full_invariant_dual_spec.py "research-graph/grothendieck-d4/artifacts/replay/h4_full_invariant_dual_spec_bundle/h4_full_invariant_dual_spec.py")
  - Coverage: Full bundled file; source lines 1–228.
  - Relevant location(s): lines22–45; matching JSON normalization/feasibility fields in h4_full_invariant_dual_spec.json
  - Source: `research-graph/grothendieck-d4/artifacts/replay/h4_full_invariant_dual_spec_bundle/h4_full_invariant_dual_spec.py`

- [M03: h4_full_invariant_dual_spec.json](original/M03-h4_full_invariant_dual_spec.json "research-graph/grothendieck-d4/artifacts/replay/h4_full_invariant_dual_spec_bundle/h4_full_invariant_dual_spec.json")
  - Coverage: Full bundled file; source lines 1.
  - Source: `research-graph/grothendieck-d4/artifacts/replay/h4_full_invariant_dual_spec_bundle/h4_full_invariant_dual_spec.json`

- [M04: d4-duality-direction-audit-20260829.md](original/M04-d4-duality-direction-audit-20260829.md "research-graph/grothendieck-d4/artifacts/d4-duality-direction-audit-20260829.md")
  - Coverage: Full bundled file; source lines 1–63.
  - Source: `research-graph/grothendieck-d4/artifacts/d4-duality-direction-audit-20260829.md`
