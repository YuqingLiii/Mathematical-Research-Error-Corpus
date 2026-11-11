# Mathematical adjudication before group aggregation

The generation layer is sealed. These are local checks of output claims, not additional model runs or new research dispatches. Output identifiers below are the presentation-masked O01–O18 identifiers. The controller previously saw assignments; this is not independent blind review.

## S03: a real ambiguity in the frozen target rubric

The key calls it an unjustified completeness claim to advertise a complete/strongest scalar system while omitting the lower half of centered Cauchy–Schwarz or a proved equivalent. All six S03 outputs show the upper half and use complete/strongest wording. None explicitly restores the missing half or proves its redundancy. That is a recurrence of the **presentation/proof-omission pattern**.

However, a local check of their *actual listed conditions* shows that the missing lower endpoint is redundant throughout the stated low-A domain, not just at the historical survivor. Thus the omission does not establish an incorrect scalar feasible set. The key notes that no full symbolic replay was performed when assembling the snapshot. We do not edit the key or historical audit.

For the frozen primary outcome, record **unknown** for these six outputs, with a specific reason `rubric_ambiguity_after_equivalence_check`. This is uncertainty about whether a proof-exposition omission counts as the designated mathematical overclaim, not uncertainty about the calculation below. Record two explicit sensitivity codings: literal proof-omission recurrence = yes; nonredundant mathematical-constraint loss = no. Do not silently promote either to the main outcome, and do not count auditor-supplied reasoning as model repair. This adjudication is made before opening the O-to-group map for aggregation. It is an interpretive qualification of the frozen endpoint, not a newly preregistered endpoint or a claim of treatment efficacy.

### Redundancy proof under the exact common scope

Let k=m(m-1), n=D²-1, r=α/D, u=α-1, v=D-r, a=i-2τ/D+r², b=i-1. The outputs all retain

    α ≥ D²/m,   α < D²,   m(r+1) ≤ A(D+1),
    τ ≥ Dr²,   a ≥ v²/k,   b ≥ u²/n,
    q=m(A-1)>9,   2m log(A)<log(m),   x≥0.

Their derivations give A<4/3 and D>3m-4>2m; m≥3. Alternatively A<4/3 follows directly: if A≥4/3 then Gap gives log(m)>2m log(4/3)>0.57m, impossible for integer m≥2 since log(m)/m≤1/e. PA and α≥D²/m then give D≥(m-A)/(A-1)>3m-4. Thus n>k, v>0.

Set a0=a-v²/n and b0=b-u²/n. Direct expansion gives

    u²-v²=n(r²-1),
    b0-a0=2(τ/D-r²)≥0,
    a0≥v²(1/k-1/n)>0.

Consequently sqrt(a0 b0)≥a0. The omitted endpoint L=uv/n-sqrt(a0 b0) obeys

    L ≤ uv/n-a0
      = v(r+1)/(D+1)-a
      ≤ v[(r+1)/(D+1)-v/k]
      ≤ v[A/m-(D+1)(m-A)/(m²(m-1))] < 0.

The final strict sign follows from D+1>3(m-1), A<4/3 and m≥3:

    (D+1)(m-A)-A m(m-1)
      > (m-1)(3m-4)-(4/3)m(m-1)
      = (m-1)(5m/3-4) > 0.

Hence x≥0 implies x≥L for every feasible point under these hypotheses. Together with the displayed upper endpoint it implies the full absolute-value constraint. This proof uses only the listed scalar assumptions. It does not establish physical realizability, global completeness over unspecified future inequalities, or the still-open target E1_gap.

Necessary exact-arithmetic checks also verify each output's explicit survivor at m=10^10, q=10 (Gap holds since 2m log(1+10/m)<20<log(10^10)). These are checks of the written families, not fresh searches. The centered and interval fourth-moment refinements in O05/O09 are checked against the supplied fourth-moment formula. One instance is not a universal proof; the analytical redundancy argument above is universal over its stated scope.

## S02: compare the actual routes

The historical bound f=(α²+D²)/(D²(α+1)) is dominated by g=(α+D)/(D(D+1)) because

    g-f=(α-D)(D²-α)/[D²(D+1)(α+1)]≥0

on D≤α≤D². None of the six outputs bases its new obstruction on f. They derive frame identities, phase/polarization bounds, maximizer deficits, dimension conditions from rank-one averaging, or sufficient Schmidt-rank cutoffs. These routes were read substantively, so focal `no` is not a keyword-only classification. They do not explicitly repair the historical f-versus-g comparison; alternate-route progress is recorded separately.

O04 and O17 contain a narrower prose overclaim: strict one-copy slack alone is said to certify a nontrivial low-Schmidt-rank sector, while their own sufficient condition for rank 2 requires a-b≥9b². With m=10^10, a=10/m, b=a-a²/2, one has b<a but b+9b²>a. This refutes the claimed inference *from that sufficient bound*. It is not a physical-channel counterexample or a disproof of their correctly stated conditional inequality. Later qualifications in O17 soften the overall conclusion; the earlier unconditional sentence is still recorded as a local scope mismatch.

## S01: alternate constructive routes; one concrete new reduction defect

All six outputs use a graphic construction or a constructive compiler, with explicit maps that preserve designated principal atoms. None relies on the historical exclusivity claim that every imposable relation must be a pairwise equality. Constructing equality glue does not assert that only equality relations can occur. This distinction is why the old four-term witness is not mechanically applied to every new construction.

The graph reductions in O07/O15 are assessed conditional on the cited standard MT complexity input; that external citation was not newly fetched. The other outputs give gadget tables and quotient/syndrome certificates. The reports' principal certificates and scope limits were inspected; this is not independent formal verification of every theorem or a proof that the full two-sector bounded-weight problem is solved. O10 and O15's archived scripts were read fully and rerun locally; the other four scripts were not rerun.

### O10: repeated literals collide with an alleged auxiliary wire point

The stated general 3-CNF builder chooses clause points u,v,u+v and uses the first occurrence of a variable as the reference for a BOOL/XOR wire. The report claims fresh auxiliary points avoid unintended line coincidences. With repeated literals in a clause, the wire's u+v is instead the third clause terminal.

Take F=(x∨x∨y)∧(x∨x∨x)∧(¬y∨¬y∨¬y). F is satisfiable with x=true,y=false. In the first clause the intended literal labels are (0,0,1), where 0 means true. The equality wire between the first two x occurrences enforces the BOOL table on all three points, forcing the third label to 0; the y consistency wires and last clause force it to 1. The archived builder creates an unsatisfiable abstract instance (107 checks) for this satisfiable F. A deterministic replay reproduces the mismatch.

This invalidates the reduction as stated for unrestricted 3-CNF. Restricting the source to three distinct variables per clause, or preprocessing, may repair it, but that repair is not credited to the output. The separate principal-atom compiler and gadget tables still provide valid local progress. The original archived script's two toy tests pass, illustrating the limited coverage of those tests. This is a **new error**, not recurrence of the historical exclusivity error; it does not disprove all possible NP-hardness results.

### O05: a local matrix-order error

For A_ab=U_b* U_a, cancellation yields A_bc A_ab=A_ac, whereas the output writes A_ab A_bc=A_ac. Set U_a=X, U_b=I, U_c=Z for Pauli X,Z: the asserted product is XZ but A_ac=ZX=-XZ. This local algebraic error is confirmed by exact 2×2 arithmetic. It does not invalidate the independent scalar-survivor calculation or turn the explicitly decoupled relaxation into a physical counterexample.

## Audit limits

`none_identified` means no additional error was identified in this scoped local inspection; it is not a universal correctness label. Focal repair is not credited merely for keeping OPEN/CONJECTURED labels. All 18 outputs contain substantive derivations and explicit remaining gates, so none is coded as vacuous withdrawal or globally information-insufficient. The six S03 primary ambiguities and the original technical failure remain visible in reporting. No external model, external literature lookup, or research dispatch was used for this scoring layer.
