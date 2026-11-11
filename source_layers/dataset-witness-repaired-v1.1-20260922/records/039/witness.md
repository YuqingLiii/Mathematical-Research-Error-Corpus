# Record 039 — Complexity of distance-preserving schedules

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

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

Context: A follow-up continuation proposes a general 3-CNF-to-line-section reduction. Each clause uses three occurrence points a,b,a+b; a BOOL/XOR gadget plus a constant gadget wires repeated occurrences. The reported theorem remains CONJECTURED, but the construction asserts that all auxiliary points are fresh.

Locator: Follow-up generated proof artifact collected 20 September 2026, section 3.4, lines 251–276.

## 2. Witness / adjudication

With two occurrences of one variable in the same clause, the wire's auxiliary XOR point is the third clause terminal, not a fresh point. The added gadget imposes an unintended constraint and breaks the satisfiability-preserving direction.

Use F=(x∨x∨y)∧(x∨x∨x)∧(¬y∨¬y∨¬y), satisfiable at x=true,y=false. In the first clause, occurrence labels are (0,0,1), where 0 denotes a true literal. Wiring the first two x occurrences at a and b applies the BOOL/XOR gadget on {a,b,a+b}, forcing g(a+b)=g(a) XOR g(b)=0. But a+b is the y occurrence; consistency with the final ¬y clause forces its label to 1. Thus the compiled instance is inconsistent. The archived builder produces an unsatisfiable 107-check abstract CSP for this satisfiable input. A restriction to clauses with distinct variables or an explicit preprocessing step could repair the route, but neither is part of the stated general reduction.

Scope: argument_invalid

一般3-CNF构造遇同一子句重复变量时，连接wire的辅助点a+b与第三文字点相同；引入意外约束，破坏可满足性保持。

维持新重放中的独立构造错误，不重复计作旧038，不要求NP-hardness已被证明。

## 3. Evidence and verification

F=(x∨x∨y)∧(x∨x∨x)∧(¬y∨¬y∨¬y)手算矛盾；107-check CSP的确定性重放是既有见证。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-circdist_cplx_islandv_20260820.md](original/M01-circdist_cplx_islandv_20260820.md) — inherited_sanitized_source
- [M02-all-visible-expanded-dom.txt](original/M02-all-visible-expanded-dom.txt) — inherited_sanitized_source
- [M03-MATHEMATICAL_ADJUDICATION.md](original/M03-MATHEMATICAL_ADJUDICATION.md) — inherited_sanitized_source
- [M04-submitted-message.txt](original/M04-submitted-message.txt) — inherited_sanitized_source
- [M05-visible-conversation.txt](original/M05-visible-conversation.txt) — inherited_sanitized_source
- [M06-final-answer.md](original/M06-final-answer.md) — inherited_sanitized_source
- [M07-collection-limitations.json](original/M07-collection-limitations.json) — inherited_sanitized_source
- [M08-verify_math.py](original/M08-verify_math.py) — inherited_sanitized_source
- [M09-math-checks.json](original/M09-math-checks.json) — inherited_sanitized_source
- [M10-circdist_cplx_islandv_verify_20260820.py](original/M10-circdist_cplx_islandv_verify_20260820.py) — inherited_sanitized_source
- [M11-receipt.json](original/M11-receipt.json) — inherited_sanitized_source
- [R01-M01-circdist_cplx_islandv_20260820.md.context.md](reconciliation_sources/R01-M01-circdist_cplx_islandv_20260820.md.context.md) — reconciliation_source_window
- [R02-M03-MATHEMATICAL_ADJUDICATION.md.context.md](reconciliation_sources/R02-M03-MATHEMATICAL_ADJUDICATION.md.context.md) — reconciliation_source_window

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
