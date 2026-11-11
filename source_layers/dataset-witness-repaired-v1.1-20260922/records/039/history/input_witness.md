# Record 039 — Complexity of distance-preserving schedules

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

> Given a 3-CNF formula, give clause `t` two fresh basis vectors `a_t,b_t` and use the three occurrence points
> 
> `p_{t1}=a_t`, `p_{t2}=b_t`, `p_{t3}=a_t+b_t`.
> 
> They are a binary line by construction.
> 
> For every literal occurrence point `p`, attach a private BOOL gadget on `{p,r_p,p+r_p}` with fresh `r_p`; hence `g(p) in {0,1}`.
> 
> For each Boolean variable, choose one occurrence as reference. Wire every other occurrence to the reference:
> 
> * same literal polarity -> equality wire;
> * opposite polarity -> negation wire.
> 
> Interpret occurrence value `0` as “this literal is true”.
> 
> Finally, for each clause add the single zero-map constraint
> 
> `(0,0,0)`
> 
> on its occurrence line. It is hit iff at least one of the three occurrence bits is zero, exactly the OR condition for the clause.
> 
> All auxiliary points use fresh basis coordinates, so unintended line coincidences are avoided. The number of points and constraints is linear in the formula size.
> 
> **Correctness.** A Boolean satisfying assignment sets every literal occurrence to `0` iff that literal is true; the wires and clause check are then satisfied, and all private helpers can be filled from the finite gadget tables. Conversely any section solution can be totalised. The private BOOL gadgets make every occurrence Boolean, the wires give a consistent truth value per variable, and every zero-map clause has a zero occurrence, hence a true literal.
> 
> Therefore LINE-SECTION is NP-hard already with `dim L_0=2`. Combining with Theorem 2 gives NP-hardness for **code-realizable** Island-V X-sector instances with weight-4 X checks, `d_X=4`, and `k>=2`.

**Recorded location:** Follow-up generated proof artifact collected 20 September 2026, section 3.4, lines 251–276.

**Context (annotation, not a source quotation):** A follow-up continuation proposes a general 3-CNF-to-line-section reduction. Each clause uses three occurrence points a,b,a+b; a BOOL/XOR gadget plus a constant gadget wires repeated occurrences. The reported theorem remains CONJECTURED, but the construction asserts that all auxiliary points are fresh.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

With two occurrences of one variable in the same clause, the wire's auxiliary XOR point is the third clause terminal, not a fresh point. The added gadget imposes an unintended constraint and breaks the satisfiability-preserving direction.

### Argument or calculation

Use F=(x∨x∨y)∧(x∨x∨x)∧(¬y∨¬y∨¬y), satisfiable at x=true,y=false. In the first clause, occurrence labels are (0,0,1), where 0 denotes a true literal. Wiring the first two x occurrences at a and b applies the BOOL/XOR gadget on {a,b,a+b}, forcing g(a+b)=g(a) XOR g(b)=0. But a+b is the y occurrence; consistency with the final ¬y clause forces its label to 1. Thus the compiled instance is inconsistent. The archived builder produces an unsatisfiable 107-check abstract CSP for this satisfiable input. A restriction to clauses with distinct variables or an explicit preprocessing step could repair the route, but neither is part of the stated general reduction.

Scope: argument_invalid.


### Archived review excerpt

> The stated general 3-CNF builder chooses clause points u,v,u+v and uses the first occurrence of a variable as the reference for a BOOL/XOR wire. The report claims fresh auxiliary points avoid unintended line coincidences. With repeated literals in a clause, the wire's u+v is instead the third clause terminal.
> 
> Take F=(x∨x∨y)∧(x∨x∨x)∧(¬y∨¬y∨¬y). F is satisfiable with x=true,y=false. In the first clause the intended literal labels are (0,0,1), where 0 means true. The equality wire between the first two x occurrences enforces the BOOL table on all three points, forcing the third label to 0; the y consistency wires and last clause force it to 1. The archived builder creates an unsatisfiable abstract instance (107 checks) for this satisfiable F. A deterministic replay reproduces the mismatch.
> 
> This invalidates the reduction as stated for unrestricted 3-CNF. Restricting the source to three distinct variables per clause, or preprocessing, may repair it, but that repair is not credited to the output. The separate principal-atom compiler and gadget tables still provide valid local progress. The original archived script's two toy tests pass, illustrating the limited coverage of those tests. This is a **new error**, not recurrence of the historical exclusivity error; it does not disprove all possible NP-hardness results.

## Original materials

- [M01: circdist_cplx_islandv_20260820.md](original/M01-circdist_cplx_islandv_20260820.md "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/artifacts/circdist_cplx_islandv_20260820.md")
  - Coverage: Full bundled file; source lines 1–912.
  - Relevant location(s): lines 251–276
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/artifacts/circdist_cplx_islandv_20260820.md`

- [M02: all-visible-expanded-dom.txt](original/M02-all-visible-expanded-dom.txt "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/all-visible-expanded-dom.txt")
  - Coverage: Full bundled file; source lines 1–324.
  - Relevant location(s): final response and tool-written artifact; tool code is not reasoning summary
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/all-visible-expanded-dom.txt`

- [M03: MATHEMATICAL_ADJUDICATION.md](original/M03-MATHEMATICAL_ADJUDICATION.md "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/MATHEMATICAL_ADJUDICATION.md")
  - Coverage: Full bundled file; source lines 1–77.
  - Relevant location(s): lines 64–68
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/MATHEMATICAL_ADJUDICATION.md`

- [M04: submitted-message.txt](original/M04-submitted-message.txt "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/submitted-message.txt")
  - Coverage: Full bundled file; source lines 1–4.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/submitted-message.txt`

- [M05: visible-conversation.txt](original/M05-visible-conversation.txt "outputs/<session-id-redacted>/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/visible-conversation.txt")
  - Coverage: Full bundled file; source lines 1–1463.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/visible-conversation.txt`

- [M06: final-answer.md](original/M06-final-answer.md "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/final-answer.md")
  - Coverage: Full bundled file; source lines 1–13.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/final-answer.md`

- [M07: collection-limitations.json](original/M07-collection-limitations.json "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/collection-limitations.json")
  - Coverage: Full bundled file; source lines 1–25.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/collection-limitations.json`

- [M08: verify_math.py](original/M08-verify_math.py "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/verify_math.py")
  - Coverage: Full bundled file; source lines 1–119.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/verify_math.py`

- [M09: math-checks.json](original/M09-math-checks.json "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/verification/math-checks.json")
  - Coverage: Full bundled file; source lines 1–240.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/verification/math-checks.json`

- [M10: circdist_cplx_islandv_verify_20260820.py](original/M10-circdist_cplx_islandv_verify_20260820.py "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/artifacts/circdist_cplx_islandv_verify_20260820.py")
  - Coverage: Full bundled file; source lines 1–535.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/artifacts/circdist_cplx_islandv_verify_20260820.py`

- [M11: receipt.json](original/M11-receipt.json "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/artifacts/receipt.json")
  - Coverage: Full bundled file; source lines 1–17.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R08/artifacts/receipt.json`
