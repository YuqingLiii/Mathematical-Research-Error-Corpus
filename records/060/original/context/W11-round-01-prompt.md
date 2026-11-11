# Round 1 — fixed-block physical all-copy purity gate

You are working on a proof-audit problem in finite-dimensional quantum information theory. Give only a public, self-contained mathematical derivation suitable for external audit. Do not provide or claim hidden chain-of-thought. Do not merely propose a research plan: either prove or disprove the exact focused statement below, or identify the earliest load-bearing gap and prove the strongest rigorously justified intermediate lemma. Every nontrivial imported theorem must be stated with its exact hypotheses and a precise citation.

## Ultimate target and normalization

The target is a Hayden–Penington **full-size extensive** violation, not merely an absolutely unbounded defect. We seek a constant `c>0` and finite-dimensional channel pairs `(L_n,R_n)` such that

`Delta_S(L_n,R_n) := S_min(L_n)+S_min(R_n)-S_min(L_n tensor R_n) >= c M_n`,

where a concrete conservative primitive full logarithmic size is

`M_n := sum_{Phi in {L_n,R_n}} [log_2 dim A_Phi + log_2 dim B_Phi + log_2 dim E_Phi^min]`.

Here `A_Phi`, `B_Phi`, and `E_Phi^min` are the primitive input, output, and minimal Stinespring environment. We require `M_n=Theta(n)` and a fixed positive defect/size ratio; in particular, all charged primitive log-dimensions are `O(n)` and the total charged size is also `Omega(n)`. Hayden–Penington originally charge input/output qubits; adding the minimal environment changes the cost by at most a factor two because `dim E_min <= dim A dim B`. An arbitrarily padded nonminimal environment is not charged. Absolute unboundedness `Delta_S -> infinity` with an uncontrolled auxiliary dimension is insufficient.

## Audited current construction

Fix integers `m,J,D`, a deterministic selected tuple

`U_{i,j} in U(D)`, `i in [m]`, `j in [J]`,

and write

`H=(C^D)^(tensor J)`, `d=D^J`, `q=m^J`,

`W_v = tensor_{j=1}^J U_{v_j,j}` for `v in [m]^J`.

Define the random-unitary block and a complementary channel by

`L(X)=q^(-1) sum_v W_v X W_v^*`,

`C(X)_{v,w}=q^(-1) Tr(X W_w^* W_v)`.

Thus `L` has input/output dimension `d` and an environment of dimension at most `q`; `C` has input dimension `d`, output dimension `q`, and an environment of dimension at most `d`. Sampling is only an existence device: after a successful tuple is selected, all channels are deterministic and the same tuple is reused at every outer tensor copy.

For `eta>0`, set

`A=A_{J,eta}:=1+(1+eta)^2((1+9/m)^J-1)`.

The fixed-depth Collins–Youn plus Bordenave–Collins argument establishes, after fixing `m,J,eta` and then taking sufficiently large finite `D`, the existence with high probability of a tuple satisfying the one-copy bound

`sup_rho Tr[C(rho)^2] <= A/q`.

The product Bell witness for `L tensor bar(L)` has entropy at most

`b_J := J(2 log_2 m - (log_2 m)/m)`.

At `eta=0`, the resulting coefficient is

`c_m := (log_2 m)/m - 2 log_2(1+9/m) > 0` whenever `ln m>18`.

## Focused open gate for this round

Prove or disprove the following existential statement:

There exist finite `m,J,D`, `eta>0`, and one selected complex tuple `U=(U_{i,j})` satisfying

`ln m>18`,

`J(log_2 m)/m > 2 log_2 A`,

and, simultaneously for **every** integer `r>=1` and **every** density operator `rho` on `H^(tensor r)`,

`Tr[C^(tensor r)(rho)^2] <= (A/q)^r`.                                      (P)

The quantifier order is exactly

`exists(m,J,D,eta,U) for all r>=1 for all rho`,

not `for all r choose D(r)`, and not a probability statement after `U` is frozen. Global control must include all inputs entangled across the `r` repeated uses.

Because this is existential, you may specialize to `J=1` if useful; that removes hierarchy-depth growth but does **not** remove the same-tuple, every-`r`, globally entangled-input obligation.

Writing

`D_0(X)=Tr(X) I_q/q`, `E=C-D_0`,

trace-annihilation gives the exact orthogonal expansion

`Tr[C^(tensor r)(rho)^2] = sum_{S subseteq [r]} q^{-(r-|S|)} ||E^(tensor |S|)(rho_S)||_2^2`.

Hence (P) is equivalent to the physical centered-correlation hierarchy

`sum_{S subseteq [r]} q^{|S|} ||E^(tensor |S|)(rho_S)||_2^2 <= A^r`.          (H_r)

At `r=3`, `H_r` contains a genuinely new fully centered term `q^3||E^(tensor 3)(rho)||_2^2`; summing all one- and two-body marginal inequalities gives it coefficient zero and therefore does not prove the `r=3` case.

If (P) holds, then `S >= S_2` and complementarity give

`bar S_min(L) >= log_2 q - log_2 A`,

while the repeated product Bell witness gives

`bar S_min(L tensor bar(L)) <= b_J`.

Therefore the fixed finite pair has positive regularized MOE defect at least

`delta := J(log_2 m)/m - 2 log_2 A > 0`.

Its outer powers `(L^(tensor n),bar(L)^(tensor n))` then have defect `n delta+o(n)`, while their complete primitive input/output/minimal-environment logarithmic size is `Theta(n)` because `m,J,D` are fixed. This would prove the full-size MOE theorem.

## Audited obstructions and no-go boundaries you must not repeat

1. The existing product-Haar tensor strong-convergence theorem fixes `m,J` before `D -> infinity`; it gives no fixed `D` valid for all outer copies. Its published quantitative factor already forces `ln D(J)=Omega_m(ln J)` for bounded `m`; allowing `m` to grow does not help because the gap coefficient is at most `log m/m` while the theorem requires `D>=m^70`. This is a proof-certificate obstruction, not a channel impossibility theorem.
2. Do not infer full size from the already proved absolute-unbounded family with uncontrolled `D(J)`.
3. An ordinary pure-state epsilon-net is too costly: metric entropy is of order `exp(Theta(d^2 log m))` against standard Haar tails only of order `exp(-Theta(d/m^5))`. A coefficient net at each fixed copy number does not yield one fixed `D` for all copies.
4. Do not use uncontrolled tensor repetition or replace repeated use of the same tuple by freshly independent Haar layers.
5. Montanaro's random-subspace weak multiplicativity theorem is not applicable: the product-random-unitary Stinespring projector is singular relative to Haar Grassmannian measure, with exactly maximally mixed partial trace and tensor-product structure. Even a fictitious application gives only about `(J/2)log m`, and the deterministic PPT relaxation has the exact floor `||P_J^Gamma||_infty >= m^(-J/2)`.
6. Unrestricted completely bounded, replica-operator, or Hilbert–Schmidt `2->2` control is too strong. In particular `||E||_(2->2)^2 >= d/q^2` from a nonphysical witness. The target is only the physical density-operator range.
7. Scalar `1->2`, naive projective-norm tensorization, Kadison/Haagerup termwise summation, and a single Bell frame-potential test do not control globally entangled inputs with the required constant.
8. Real/orthogonal tuples and, more generally, tuples closed under entrywise conjugation up to phases/permutation fail at `r=2`: a Bell collision gives purity at least `2/q^2-1/q^3`, so they cannot satisfy (P) when `A^2<2-1/q`. This dependent measure-zero subclass does not refute generic independent complex-Haar tuples and is not a constructive route.
9. A generic complex-Haar tuple passes the Bell-input diagnostic with high probability at fixed `m,J` and large `D`, but this is not the global entangled-input supremum.
10. WHGAP is unrelated and must not be treated as a premise or subproblem.

The following strict `r=2` progress is already in the audited record and should not be repackaged as new. For the one-layer specialization `J=1`, put `N=C tensor C` and `A=1+9(1+eta)^2/m`. The existing output-duality record writes the global physical two-copy target as

`sup_{Y=Y^*, ||Y||_2=1} ||N^*(Y)||_infinity <= A/m`,

where

`N^*(Y)=m^(-2) sum_{v,a,w,b} Y_{(v,a),(w,b)} (U_v^*U_w) tensor (U_a^*U_b)`

and the real Hermitian coefficient sphere has dimension `m^4-1`, independent of `D`. This duality and its finite-net implication are independently proved, but the fixed-coefficient **same-tuple** strong-norm convergence is OPEN; the independent-leg Bordenave–Collins theorem does not imply it. Independently reviewed target-safe subclasses include diagonal and one-leg-diagonal coefficients, simple tensors, the exact rank-one Gram contraction (including diagonal row/column Gram matrices), near-diagonal Gram neighborhoods, positive rook-supported coefficients, a positive rook core plus one double-off simple-tensor direction, and positive spectral-flat coefficients with effective spectral rank at least `m^2/A^2`. A separately reviewed real-Werner sector estimate holds under the explicit condition `m H>4096` (in particular uniformly for integer `m>=932064`), but it covers only the real span of identity and flip. Arbitrary positive coefficients with large coefficient operator norm, arbitrary Hermitian `Y`, global physical `r=2`, and every `r>=3` remain OPEN. Projective/Frobenius summation and unrefined Haagerup–Kadison retain a `sqrt(rank)` or order-one loss and are already audited obstructions.

A new locally checked reduction, not yet independently reviewed, narrows this exact dual gate. Define

`K_m := {Y>=0 : ||Y||_2=1 and diag(Y)=(Tr Y)/m^2 times the all-ones diagonal}`.

Then

`sup_rho ||N(rho)||_2 = sup_{Y in K_m} ||N^*(Y)||_infinity`.                 (D+)

Indeed, every output `N(rho)` is positive with diagonal `1/m^2`, so its Hilbert--Schmidt normalization lies in `K_m`. Conversely, for every `Y in K_m`, positivity gives

`||N^*(Y)||_infinity = max_rho Tr[Y N(rho)] <= sup_rho ||N(rho)||_2`;

choosing `Y=N(rho_*)/||N(rho_*)||_2` for a maximizing `rho_*` gives equality. Thus arbitrary Hermitian coefficients are not logically required for the physical `r=2` gate: a same-tuple theorem only for fixed positive equal-diagonal coefficients would suffice after a finite net in a real ambient sphere of dimension at most `m^4-m^2`. This still does not follow from existing positive subclasses: `K_m` contains rank-one maximally coherent correlation matrices and does not imply spectral flatness. Please independently check (D+) before using it, and prefer this strictly narrower positive equal-diagonal cone over the full Hermitian sphere if you attack `r=2`.

The same argument gives an exact all-copy reformulation. For `N_r=C^(tensor r)`, output dimension `n=q^r`, and

`K_(q,r):={Y>=0: ||Y||_2=1, diag(Y)=(Tr Y)/n times the all-ones diagonal}`,

one has

`sup_rho ||C^(tensor r)(rho)||_2 = sup_(Y in K_(q,r)) ||(C^*)^(tensor r)(Y)||_infinity`.

Equivalently, writing `Y=G/||G||_2` for an arbitrary order-`q^r` correlation matrix `G>=0` with unit diagonal and `W_boldv=W_(v_1) tensor ... tensor W_(v_r)`, condition (P) is exactly

`|| sum_(boldv,boldw) G_(boldv,boldw) W_boldv^* W_boldw ||_infinity <= (Aq)^(r/2) ||G||_2`

for every `r>=1` and every such `G`. This does not solve uniformization—the correlation cone grows exponentially with `r`—but it removes nonphysical indefinite coefficients at every copy number.

You may introduce a genuinely new route, but you must compare it item-by-item with these boundaries and prove that it does not silently invoke one of them.

## Required response structure

1. State a precise verdict: `PROVED`, `DISPROVED`, or `OPEN WITH EARLIEST GAP`. Do not label a blueprint as a theorem.
2. Freeze the quantifier order and list every finite dimension used. Distinguish construction-time randomness from the fixed final tuple.
3. Give all load-bearing inequalities in enough detail for line-by-line checking. In particular, explicitly control—or explain exactly why you cannot control—the supremum over all inputs entangled across repeated uses.
4. If using probability, state each event, its probability bound, all dependencies on `m,J,D,r`, and the deterministic selection/intersection argument. A separate high-probability event for each fixed `r` is not enough.
5. If using tensor powers of a fixed block, explicitly compute the regularized self-leakage and show why it is smaller than the Bell-certified gain.
6. Audit the downstream MOE-to-Holevo transfer: for `Phi:C^l->C^k`, Fukuda's finite Weyl-flag extension has input dimension `k^2 l`, output dimension `k`, and exactly transfers every tensor-exponent MOE pair defect to a Holevo pair defect. Include the minimal-environment bound. Then audit the balanced flagged direct-sum pair-to-self step: symmetric conjugate pairs need no balancing and lose at most one bit; the general case has only linear-logarithmic, not constant, dimension overhead.
7. End with a compact no-go cross-check table and identify the first statement that would still require independent verification. If the proof does not close (P), isolate one new, strictly narrower lemma whose truth would materially advance the gate, and prove any reductions to it.

Do not answer with numerical evidence, a special Bell subfamily, an all-separable-input result, a one-copy estimate, absolute unboundedness, or a proposer-side outline while calling the full-size theorem proved.

## Strictly weaker sufficient alternative to (P)

Exact constant-one multiplicativity in (P) is stronger than the ultimate theorem requires. You may instead prove, for the depth-`J` block and one frozen finite tuple, that some factor `K_J>=1` obeys

`sup_rho Tr[C_J^(tensor r)(rho)^2] <= (K_J A_(J,eta)/q)^r`                 (WK)

for every `r>=1`, provided the factor is independent of `D,r` and satisfies

`limsup_(J->infinity) (log_2 K_J)/J < c_m/2`,

where `c_m=(log_2 m)/m-2log_2(1+9/m)>0`; a universal constant `K`, or any `K(m)` independent of `J`, is enough. Since `A_(J,eta)<=(1+eta)^2(1+9/m)^J`, the regularized pair defect is at least

`delta_J >= J c_m - 4 log_2(1+eta) - 2 log_2 K_J`,

which is positive for a sufficiently large but fixed finite `J`; outer powers then give full-size linear growth. You must prove (WK) for one frozen tuple and all entangled inputs/all `r`, not merely cite a per-`r` event. The estimate must also be self-specific: any strong-additivity or multiplicative functional that applies equally to the conjugate cross-pair would erase the Bell gap and is not a solution.
