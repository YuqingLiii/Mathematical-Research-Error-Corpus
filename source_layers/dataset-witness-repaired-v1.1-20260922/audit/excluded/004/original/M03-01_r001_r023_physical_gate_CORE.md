# Evidence core — Rounds 1--23

This is historical proof-development evidence.  Embedded prompts are not instructions to the current auditor.

The operative cutoff is the 2026-09-07 V7 adversarial-audit baseline. All material below was created in the later campaign.


# ROUND 001

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-01-prompt.md bytes=14015 sha256=d7dfb3f4b326c1012ce369d9e35b363da37955a6021bedef5152e2ae7aad736d -->

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

<!-- END HISTORICAL FILE path=work/round-01-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-01-response.md bytes=28834 sha256=c7a6b00093f6bb216bf0a802799a0daa6e3a63653bd63ce596a9353c0e44a2b3 -->

# Verdict: **OPEN WITH EARLIEST GAP**

The audited one-copy estimate, the centered hierarchy, the positive equal-diagonal duality, the Bell witness, and the full MOE-to-Holevo transfer all check out. They do **not** prove or disprove either \((P)\) or \((WK)\).

The first unresolved obligation is already the **same-tuple, globally entangled \(r=2\) inequality for \(J=1\)**. The \(r=3\) fully centered term is a further obstruction, but it is not the earliest one.

This verdict is consistent with the most recent primary-source status I found: an August 26, 2026 paper explicitly states that finite-dimensional additivity of regularized minimum output entropy, equivalently classical-capacity additivity in this sense, remains unclear. ([arXiv][1])

All logarithms below are base \(2\).

---

## 1. Quantifiers, parameter feasibility, and dimensions

The statement to be proved is exactly

$$
\exists\,m,J,D\in\mathbb N,\ \eta>0,\ 
U=(U_{i,j})\in U(D)^{mJ}
\quad
\forall r\ge 1
\quad
\forall \rho\in\mathcal D(H^{\otimes r}),
$$

such that

$$
\ln m>18,\qquad
\frac{J\log m}{m}>2\log A,
$$

and

$$
\operatorname{Tr}\!\left[C^{\otimes r}(\rho)^2\right]
\le \left(\frac Aq\right)^r,
$$

where

$$
H=(\mathbb C^D)^{\otimes J},\qquad
d=D^J,\qquad q=m^J,
$$

$$
W_v=\bigotimes_{j=1}^J U_{v_j,j},
\qquad
A=1+(1+\eta)^2\left[\left(1+\frac 9m\right)^J-1\right].
$$

All existential parameters, including the complete tuple \(U\), must be frozen before \(r\) and \(\rho\) vary.

### Scalar inequality is not the obstruction

Since

$$
A\le (1+\eta)^2\left(1+\frac 9m\right)^J,
$$

we have

$$
\frac{J\log m}{m}-2\log A
\ge
J\left[
\frac{\log m}{m}
-2\log\left(1+\frac 9m\right)
\right]
-4\log(1+\eta)
=
Jc_m-4\log(1+\eta).
$$

Because

$$
2\ln\left(1+\frac9m\right)<\frac{18}{m}<\frac{\ln m}{m}
$$

whenever \(\ln m>18\), one has \(c_m>0\). Thus sufficiently large finite \(J\), followed by sufficiently small finite \(\eta>0\), satisfies the scalar inequality.

In fact, \(J=1\) is already scalar-feasible: at \(\eta=0\),

$$
\frac{\ln m}{m}
>
2\ln\left(1+\frac9m\right),
$$

and continuity permits a sufficiently small positive \(\eta\). Hence the first operator-theoretic gap can legitimately be isolated at \(J=1\).

### Stinespring dimensions

Define

$$
V:H\longrightarrow H\otimes\mathbb C^q,
\qquad
Vx=\frac1{\sqrt q}\sum_{v\in[m]^J}W_vx\otimes |v\rangle.
$$

Because \(W_v^*W_v=I\),

$$
V^*V=\frac1q\sum_v W_v^*W_v=I,
$$

so \(V\) is an isometry and

$$
L(X)=\operatorname{Tr}_{\mathbb C^q}(VXV^*),\qquad
C(X)=\operatorname{Tr}_{H}(VXV^*).
$$

The finite dimensions are therefore:

| Channel           |   Input |  Output | Explicit environment | Minimal environment |
| ----------------- | ------: | ------: | -------------------: | ------------------: |
| \(L\)             |   \(d\) |   \(d\) |                \(q\) |        \(e_L\le q\) |
| \(C\)             |   \(d\) |   \(q\) |                \(d\) |        \(e_C\le d\) |
| \(C^{\otimes r}\) | \(d^r\) | \(q^r\) |              \(d^r\) |           \(e_C^r\) |

The minimal environment dimension equals the minimum number of Kraus operators, hence the rank of the Choi matrix. Since

$$
J_{\Phi^{\otimes n}}
=
J_\Phi^{\otimes n}
$$

up to a fixed tensor-factor permutation,

$$
e_{\Phi^{\otimes n}}^{\min}
=
\operatorname{rank}(J_\Phi^{\otimes n})
=
\operatorname{rank}(J_\Phi)^n.
$$

Thus minimal-environment dimensions tensorize exactly.

### Randomness is only a selection device

For fixed \(m,J,D,\eta\), let \(\mu_D\) be product Haar measure on \(U(D)^{mJ}\), and define

$$
\mathcal E_r(D)
=
\left\{
U:
\sup_{\rho}
\operatorname{Tr}[C_U^{\otimes r}(\rho)^2]
\le \left(\frac Aq\right)^r
\right\}.
$$

Then \((P)\) requires

$$
U\in \mathcal E_\infty(D)
:=
\bigcap_{r=1}^{\infty}\mathcal E_r(D)
$$

for one finite \(D\). The sets \(\mathcal E_r(D)\) are closed because the optimized function is continuous on compact spaces.

Therefore either of the following would be sufficient:

$$
\inf_R
\mu_D\left(\bigcap_{r=1}^R\mathcal E_r(D)\right)>0
$$

for one finite \(D\), or, deterministically, nonemptiness of every finite intersection at one fixed \(D\), followed by compactness.

A result of the form

$$
\forall R\ \exists D(R)\ \exists U_R
\quad
U_R\in\bigcap_{r=1}^R\mathcal E_r(D(R))
$$

does not have the required quantifier order.

---

## 2. Exact centered hierarchy

Let

$$
D_0(X)=\operatorname{Tr}(X)\frac{I_q}{q},
\qquad
E=C-D_0.
$$

Then \(\operatorname{Tr}E(X)=0\), and

$$
C^{\otimes r}
=
(D_0+E)^{\otimes r}.
$$

For \(S\subseteq[r]\), write \(\rho_S=\operatorname{Tr}_{S^c}\rho\). Direct expansion gives

$$
C^{\otimes r}(\rho)
=
\sum_{S\subseteq[r]}
q^{-(r-|S|)}
I_{S^c}\otimes E^{\otimes |S|}(\rho_S),
$$

with the natural tensor ordering understood.

Two distinct summands are Hilbert–Schmidt orthogonal: on any coordinate in their symmetric difference, one factor is \(I_q\), while the other has trace zero. Moreover,

$$
\left\|
q^{-(r-|S|)}
I_{S^c}\otimes E^{\otimes |S|}(\rho_S)
\right\|_2^2
=
q^{-(r-|S|)}
\left\|E^{\otimes |S|}(\rho_S)\right\|_2^2.
$$

Hence

$$
\boxed{
\operatorname{Tr}[C^{\otimes r}(\rho)^2]
=
\sum_{S\subseteq[r]}
q^{-(r-|S|)}
\left\|E^{\otimes |S|}(\rho_S)\right\|_2^2
}
$$

and \((P)\) is exactly

$$
\boxed{
\sum_{S\subseteq[r]}
q^{|S|}
\left\|E^{\otimes |S|}(\rho_S)\right\|_2^2
\le A^r.
}
$$

At \(r=3\), this is

$$
\begin{aligned}
1
&+q\sum_{i=1}^3\|E(\rho_i)\|_2^2\\
&+q^2\sum_{1\le i<j\le3}
\|E^{\otimes2}(\rho_{ij})\|_2^2\\
&+q^3\|E^{\otimes3}(\rho)\|_2^2
\le A^3.
\end{aligned}
$$

The final term is genuinely new and is absent from every one- and two-body marginal inequality.

---

## 3. Exact regularized-purity formulation

Set

$$
p_r(C)
=
\sup_{\rho\in\mathcal D(H^{\otimes r})}
\operatorname{Tr}[C^{\otimes r}(\rho)^2].
$$

Product inputs imply

$$
p_{r+s}(C)\ge p_r(C)p_s(C).
$$

Thus \(\log p_r(C)\) is superadditive, and

$$
\gamma_2(C)
:=
\lim_{r\to\infty}p_r(C)^{1/r}
=
\sup_{r\ge1}p_r(C)^{1/r}.
$$

Consequently,

$$
(P)
\quad\Longleftrightarrow\quad
\gamma_2(C)\le\frac Aq,
$$

and

$$
(WK)
\quad\Longleftrightarrow\quad
\gamma_2(C)\le\frac{K_JA}{q}.
$$

This is an exact formulation, not merely an asymptotic weakening: because the limit is the supremum of all finite-copy roots, the bound on \(\gamma_2\) implies every finite-\(r\) bound.

---

## 4. Independent verification of the positive equal-diagonal duality

Let

$$
N_r=C^{\otimes r},
\qquad
n=q^r,
\qquad
\alpha_r=\sup_\rho\|N_r(\rho)\|_2.
$$

Every output \(X=N_r(\rho)\) satisfies

$$
X\succeq0,\qquad
\operatorname{Tr}X=1,\qquad
\operatorname{diag}X=\frac1n\mathbf1,
$$

because every diagonal entry of \(C(\sigma)\) is \(q^{-1}\operatorname{Tr}\sigma\).

Define

$$
\mathcal K_{q,r}
=
\left\{
Y\succeq0:
\|Y\|_2=1,\ 
\operatorname{diag}Y
=
\frac{\operatorname{Tr}Y}{n}\mathbf1
\right\}.
$$

### Upper bound

For \(Y\in\mathcal K_{q,r}\), complete positivity gives \(N_r^*(Y)\succeq0\). Therefore

$$
\begin{aligned}
\|N_r^*(Y)\|_\infty
&=
\max_{\rho\in\mathcal D(H^{\otimes r})}
\operatorname{Tr}[\rho N_r^*(Y)]\\
&=
\max_\rho\operatorname{Tr}[Y N_r(\rho)]\\
&\le
\max_\rho \|Y\|_2\|N_r(\rho)\|_2\\
&=\alpha_r.
\end{aligned}
$$

### Reverse bound

Let \(\rho_*\) attain \(\alpha_r\), and put

$$
Y_*=\frac{N_r(\rho_*)}{\alpha_r}.
$$

Then \(Y_*\in\mathcal K_{q,r}\), and

$$
\begin{aligned}
\|N_r^*(Y_*)\|_\infty
&\ge
\operatorname{Tr}[\rho_*N_r^*(Y_*)]\\
&=
\operatorname{Tr}[Y_*N_r(\rho_*)]\\
&=
\frac{\|N_r(\rho_*)\|_2^2}{\alpha_r}\\
&=\alpha_r.
\end{aligned}
$$

Hence

$$
\boxed{
\sup_\rho\|C^{\otimes r}(\rho)\|_2
=
\sup_{Y\in\mathcal K_{q,r}}
\|(C^*)^{\otimes r}(Y)\|_\infty.
}
\tag{D+}
$$

So \((D+)\) is correct.

### Correlation-matrix form

Every \(Y\in\mathcal K_{q,r}\) can be written uniquely up to scaling as

$$
Y=\frac{G}{\|G\|_2},
\qquad
G\succeq0,\qquad
\operatorname{diag}G=\mathbf1.
$$

Indeed, take \(G=nY/\operatorname{Tr}Y\).

Furthermore,

$$
(C^*)^{\otimes r}(Y)
=
q^{-r}
\sum_{\boldsymbol v,\boldsymbol w}
Y_{\boldsymbol v,\boldsymbol w}
W_{\boldsymbol v}^*W_{\boldsymbol w},
$$

where

$$
W_{\boldsymbol v}
=
W_{v_1}\otimes\cdots\otimes W_{v_r}.
$$

Therefore \((P)\) is exactly

$$
\boxed{
\left\|
\sum_{\boldsymbol v,\boldsymbol w}
G_{\boldsymbol v,\boldsymbol w}
W_{\boldsymbol v}^*W_{\boldsymbol w}
\right\|_\infty
\le
(Aq)^{r/2}\|G\|_2
}
\tag{CM\(_r\)}
$$

for every \(r\) and every order-\(q^r\) correlation matrix \(G\).

---

## 5. The earliest gap: \(J=1,r=2\)

For \(J=1\),

$$
q=m,\qquad W_v=U_v,\qquad
A=1+\frac{9(1+\eta)^2}{m}.
$$

At \(r=2\), condition \((CM_r)\) becomes

$$
\boxed{
\left\|
\sum_{v,a,w,b}
G_{(v,a),(w,b)}
(U_v^*U_w)\otimes(U_a^*U_b)
\right\|_\infty
\le
Am\,\|G\|_2
}
\tag{R2}
$$

for every

$$
G\succeq0,\qquad
\operatorname{diag}G=\mathbf1_{m^2}.
$$

This is the first unresolved statement.

The real Hermitian space of order \(n=m^2\) has dimension \(n^2=m^4\). Requiring all diagonal entries to be equal imposes \(n-1\) independent linear conditions, and unit Hilbert–Schmidt norm removes one further degree of freedom. Thus the equal-diagonal sphere has real dimension

$$
m^4-m^2.
$$

A finite net is therefore possible once a fixed-coefficient same-tuple norm theorem is available. The missing step is precisely that theorem.

### Why the published strong-convergence results do not supply it

Collins–Youn’s exact free-group estimate is the following. For \(N\) free generators, \(k\ge1\), and every scalar matrix \(a=(a_{vw})_{v,w\in E^k}\in M_{N^k}\) with \(\operatorname{tr}a=0\),

$$
\left\|
\sum_{v,w}a_{vw}U_v^*U_w
\right\|
\le
N^{k/2}
\sqrt{\left(1+\frac9N\right)^k-1}\,
\|a\|_2.
$$

It implies, for every density operator on the infinite-dimensional free-group input,

$$
\left\|
(\Phi_N^c)^{\otimes k}(S)
-\frac{I}{N^k}
\right\|_2
\le
N^{-k/2}
\sqrt{\left(1+\frac9N\right)^k-1}.
$$

These are Collins–Youn, arXiv:1907.07856v2, Theorems 3.3 and 3.4. Their construction is infinite-dimensional, and the paper explicitly notes that the finite-dimensional transfer is unclear. ([arXiv][2])

Bordenave–Collins prove a quantitative finite-dimensional theorem for a fixed number \(h\) of independent Haar \(N\times N\) unitaries. In their Theorem 1.1, assuming \(h^{70}\le N\) and taking

$$
p=N^{1/(16h+80)},
$$

they obtain a high-Schatten-norm comparison with the free counterpart. Corollary 1.2 upgrades this to operator norm for matrix coefficients of dimension

$$
n\le \exp\!\left(N^{1/(32h+160)}\right).
$$

Thus, for fixed finite \(N\), only a finite coefficient dimension is covered. ([arXiv][3])

More importantly for \((R2)\), their product-group theorem uses independent Haar families \(U_{i,j}\) on distinct tensor legs. The repeated-use expression in \((R2)\) has the **same** \(U_i\) in both legs. The published independent-leg result does not imply convergence of

$$
(U_i\otimes U_i)_i
$$

or of the four-index polynomial in \((R2)\). ([arXiv][3])

Hence neither theorem proves or refutes \((R2)\).

---

## 6. A new strictly narrower physical orbit-block reduction

The dual cone \(\mathcal K_{q,r}\) is exact but still large. There is a sharper primal reduction that retains only block matrices physically generated by one input state.

### Proposition: physical orbit-block recursion

For \(s\ge1\), let \(T:H\to H^{\otimes s}\) satisfy

$$
\|T\|_2=1,
$$

and use the vectorization convention

$$
|\psi_T\rangle
=
\sum_{i=1}^d |i\rangle\otimes T|i\rangle.
$$

Then \(\|\psi_T\|=1\). Put

$$
A_{vw}=W_w^*W_v,
$$

$$
\tau_T=TT^*,
\qquad
X_{vw}^{(T)}
=
T A_{vw}^{\mathsf T}T^*.
$$

One has

$$
\operatorname{Tr}_{H}
\!\left[
(A_{vw}\otimes I)
|\psi_T\rangle\langle\psi_T|
\right]
=
T A_{vw}^{\mathsf T}T^*,
$$

and therefore the \(v,w\) output block of
\(C^{\otimes(s+1)}(|\psi_T\rangle\langle\psi_T|)\) is

$$
\left[
C^{\otimes(s+1)}
(|\psi_T\rangle\langle\psi_T|)
\right]_{v,w}
=
\frac1q C^{\otimes s}(X_{vw}^{(T)}).
$$

Consequently,

$$
\boxed{
\begin{aligned}
&
\left\|
C^{\otimes(s+1)}
(|\psi_T\rangle\langle\psi_T|)
\right\|_2^2\\
&\qquad =
\frac1q
\|C^{\otimes s}(\tau_T)\|_2^2
+
\frac1{q^2}
\sum_{v\ne w}
\|C^{\otimes s}(X_{vw}^{(T)})\|_2^2.
\end{aligned}
}
\tag{OB}
$$

Indeed, the squared Hilbert–Schmidt norm of a block matrix is the sum of the squared Hilbert–Schmidt norms of its blocks.

The matrix

$$
[X_{vw}^{(T)}]_{v,w}
=
q(C\otimes\operatorname{id})
(|\psi_T\rangle\langle\psi_T|)
$$

has the following additional restrictions:

$$
[X_{vw}^{(T)}]\succeq0,\qquad
X_{vv}^{(T)}=\tau_T\quad\forall v,
$$

and

$$
\operatorname{rank}[X_{vw}^{(T)}]\le d.
$$

The rank bound follows because the block matrix is the reduced state of a pure Stinespring output after tracing out the \(d\)-dimensional \(L\)-output system.

Thus these are not arbitrary operator-valued coefficients: all blocks are simultaneous congruences of the fixed orbit

$$
\{(W_w^*W_v)^{\mathsf T}\}_{v,w}
$$

by one map \(T\).

### Physical leakage constants

Define

$$
\kappa_s(U)
=
\sup_{\substack{T:H\to H^{\otimes s}\\ \|T\|_2=1}}
\frac{
\displaystyle
\sum_{v\ne w}
\left\|
C^{\otimes s}
\!\left(
T(W_w^*W_v)^{\mathsf T}T^*
\right)
\right\|_2^2
}{
\displaystyle
q\,
\|C^{\otimes s}(TT^*)\|_2^2
}.
\tag{K}
$$

The denominator is nonzero because \(TT^*\) is a density operator and \(C^{\otimes s}(TT^*)\) has trace one.

Purity is a convex function of the input state, so \(p_{s+1}(C)\) is attained on a pure input. Applying \((OB)\) to a maximizing pure state gives

$$
\boxed{
p_{s+1}(C)
\le
\frac{1+\kappa_s(U)}{q}\,p_s(C).
}
\tag{Rec}
$$

Inductively, using \(p_1(C)\le A/q\),

$$
\boxed{
p_r(C)
\le
\frac{A}{q^r}
\prod_{s=1}^{r-1}(1+\kappa_s(U)).
}
\tag{Prod}
$$

Therefore:

$$
\boxed{
\kappa_s(U)\le A-1\quad\forall s\ge1
\quad\Longrightarrow\quad
(P).
}
\tag{PL}
$$

More generally, setting \(B=K_JA\),

$$
\boxed{
\kappa_s(U)\le B-1\quad\forall s\ge1
\quad\Longrightarrow\quad
(WK),
}
$$

because

$$
p_r(C)
\le
\frac{A B^{r-1}}{q^r}
\le
\left(\frac Bq\right)^r.
$$

This is a strictly narrower sufficient gate than arbitrary cb or operator-valued control:

* only pure physical inputs are tested;
* all off-diagonal blocks are generated by one \(T\);
* the block matrix is positive, equal-diagonal, and rank at most \(d\);
* the blocks are processed by the same self-channel \(C^{\otimes s}\);
* no conclusion for \(C\otimes\overline C\) is implied.

### Exact finite \(r=2\) primal formulation

At \(s=1\), \(r=2\) is exactly

$$
\boxed{
q\|C(TT^*)\|_2^2
+
\sum_{v\ne w}
\left\|
C\!\left(
T(W_w^*W_v)^{\mathsf T}T^*
\right)
\right\|_2^2
\le A^2
}
\tag{OB\(_2\)}
$$

for every \(T:H\to H\) with \(\|T\|_2=1\).

The stronger, simpler sufficient statement

$$
\boxed{
\sum_{v\ne w}
\left\|
C\!\left(
T(W_w^*W_v)^{\mathsf T}T^*
\right)
\right\|_2^2
\le
(A-1)q\,\|C(TT^*)\|_2^2
}
\tag{OL\(_1\)}
$$

would establish \(r=2\).

### Why this is not disguised cb control

Take \(T=I/\sqrt d\), corresponding to a maximally entangled state, and temporarily remove the self-processing \(C\). Then

$$
TT^*=\frac{I}{d},
$$

$$
T(W_w^*W_v)^{\mathsf T}T^*
=
\frac{(W_w^*W_v)^{\mathsf T}}{d},
$$

and

$$
\left\|
\frac{(W_w^*W_v)^{\mathsf T}}{d}
\right\|_2^2
=
\left\|\frac Id\right\|_2^2
=
\frac1d.
$$

Hence the unprocessed ratio is

$$
\frac{q(q-1)/d}{q/d}=q-1.
$$

The scalar gap condition implies

$$
A^2<m^{J/m}<q,
$$

so \(q-1>A-1\). Thus the corresponding identity-amplified or map-independent block inequality is false. A proof of \((OL_1)\) must use the specific action of the same \(C\) on all physical orbit blocks.

---

## 7. Consequences if \((P)\) or \((WK)\) is established

Let

$$
B=
\begin{cases}
A,&(P),\\
K_JA,&(WK).
\end{cases}
$$

Then

$$
p_r(C)\le\left(\frac Bq\right)^r.
$$

For a density matrix \(\sigma\),

$$
S(\sigma)\ge S_2(\sigma)
=
-\log\operatorname{Tr}\sigma^2.
$$

Indeed, concavity of \(\log\) gives

$$
\sum_i\lambda_i\log\lambda_i
\le
\log\sum_i\lambda_i^2.
$$

Therefore

$$
S_{\min}(C^{\otimes r})
\ge
r(\log q-\log B).
$$

A minimum-output-entropy minimizer can be chosen pure. For a pure input, complementary outputs have identical nonzero spectra. Hence

$$
S_{\min}(L^{\otimes r})
=
S_{\min}(C^{\otimes r}),
$$

and

$$
\boxed{
\overline S_{\min}(L)
\ge
\log q-\log B.
}
$$

### Explicit regularized self-leakage

Define the entropy loss from the maximally mixed \(q\)-level value by

$$
\ell_{\rm self}
=
\log q-\overline S_{\min}(L).
$$

Then

$$
\ell_{\rm self}\le\log B.
$$

The repeated Bell witness gives

$$
\overline S_{\min}(L\otimes\overline L)
\le
b_J
=
2J\log m-\frac{J\log m}{m}.
$$

Its certified gain below \(2\log q\) is

$$
g_{\rm Bell}
=
2\log q-b_J
=
\frac{J\log m}{m}.
$$

Thus

$$
\begin{aligned}
&
2\overline S_{\min}(L)
-
\overline S_{\min}(L\otimes\overline L)\\
&\qquad\ge
\frac{J\log m}{m}-2\log B.
\end{aligned}
$$

For \((P)\),

$$
\delta
=
\frac{J\log m}{m}-2\log A>0.
$$

For \((WK)\),

$$
\begin{aligned}
\delta_J
&\ge
\frac{J\log m}{m}
-2\log A
-2\log K_J\\
&\ge
Jc_m
-4\log(1+\eta)
-2\log K_J.
\end{aligned}
$$

If

$$
\limsup_{J\to\infty}
\frac{\log K_J}{J}
<
\frac{c_m}{2},
$$

then sufficiently large but finite \(J\) makes \(\delta_J>0\).

### Full-size outer powers

Set

$$
L_n=L^{\otimes n},
\qquad
R_n=\overline L^{\otimes n}.
$$

Subadditivity of \(S_{\min}(\Phi^{\otimes n})\) implies the regularized limits exist, and therefore

$$
\begin{aligned}
\Delta_S(L_n,R_n)
&=
2S_{\min}(L^{\otimes n})
-
S_{\min}((L\otimes\overline L)^{\otimes n})\\
&=
n\left[
2\overline S_{\min}(L)
-
\overline S_{\min}(L\otimes\overline L)
\right]
+o(n)\\
&\ge n\delta_J+o(n).
\end{aligned}
$$

Let \(e=e_L^{\min}\le q\). Then \(L_n\) and \(R_n\) each have

$$
\dim A=d^n,\qquad
\dim B=d^n,\qquad
\dim E_{\min}=e^n.
$$

Consequently,

$$
\boxed{
M_n
=
n\left(4\log d+2\log e\right)
=
\Theta(n).
}
$$

Hence

$$
\liminf_{n\to\infty}
\frac{\Delta_S(L_n,R_n)}{M_n}
\ge
\frac{\delta_J}{4\log d+2\log e}>0.
$$

Adding the minimal environment changes the input-output cost by at most a factor two because, for every channel \(M_a\to M_b\),

$$
e_{\min}=\operatorname{rank}J_\Phi\le ab,
\qquad
\log e_{\min}\le\log a+\log b.
$$

Thus \((P)\) or admissible \((WK)\) would indeed prove the stated full-size theorem, not merely absolute unboundedness.

---

## 8. Exact MOE-to-Holevo transfer

Let

$$
\Phi:M_l\to M_k
$$

be a channel, and let \(W_z\), \(z\in\mathbb Z_k^2\), be the discrete Weyl operators on \(\mathbb C^k\). Fukuda’s finite Weyl-flag extension is

$$
\widetilde\Phi:
M_{k^2l}\to M_k,
$$

$$
\widetilde\Phi(\rho)
=
\sum_{z\in\mathbb Z_k^2}
W_z\,
\Phi\!\left(
(\langle z|\otimes I_l)
\rho
(|z\rangle\otimes I_l)
\right)
W_z^*.
$$

Thus its dimensions are exactly

$$
\dim A_{\widetilde\Phi}=k^2l,
\qquad
\dim B_{\widetilde\Phi}=k.
$$

Fukuda’s Lemma 6.2 states that for channels
\(\Phi:M_l\to M_k\) and
\(\Omega:M_{l'}\to M_{k'}\), and all \(a,b\in\mathbb N\cup\{0\}\),

$$
\boxed{
\chi(\widetilde\Phi^{\otimes a}
\otimes
\widetilde\Omega^{\otimes b})
=
\log(k^a(k')^b)
-
S_{\min}(\Phi^{\otimes a}
\otimes
\Omega^{\otimes b}).
}
\tag{F}
$$

This is Fukuda, *Revisiting additivity violation of quantum channels*, arXiv:1307.0707v3, Lemma 6.2. ([arXiv][4])

Subtracting the \(b=0\) and \(a=0\) cases from \((F)\) gives the exact exponent-wise identity

$$
\boxed{
\begin{aligned}
&
\chi(\widetilde\Phi^{\otimes a}
\otimes
\widetilde\Omega^{\otimes b})
-\chi(\widetilde\Phi^{\otimes a})
-\chi(\widetilde\Omega^{\otimes b})\\
&\quad=
S_{\min}(\Phi^{\otimes a})
+
S_{\min}(\Omega^{\otimes b})
-
S_{\min}(\Phi^{\otimes a}\otimes\Omega^{\otimes b}).
\end{aligned}
}
$$

So every tensor-exponent MOE pair defect is transferred exactly to a Holevo pair defect.

### Minimal environment of the Weyl extension

Suppose \(\Phi\) has \(e_\Phi\) minimal Kraus operators \(A_\alpha\). Then

$$
K_{z,\alpha}
=
W_zA_\alpha(\langle z|\otimes I_l)
$$

is a Kraus representation of \(\widetilde\Phi\). Therefore

$$
\boxed{
e_{\widetilde\Phi}^{\min}
\le k^2e_\Phi
\le k^3l.
}
$$

For \(L:M_d\to M_d\), with \(e_L=e\le q\),

$$
\widetilde L:
M_{d^3}\to M_d,
\qquad
e_{\widetilde L}^{\min}\le d^2e\le d^2q.
$$

All logarithmic dimensions of its \(n\)-fold powers remain \(O(n)\).

---

## 9. Balanced flagged direct-sum pair-to-self reduction

For channels \(\Phi_i\), define the flagged direct sum

$$
\Gamma=\bigoplus_i\Phi_i
$$

by dephasing the direct-sum input flag, applying \(\Phi_i\) on branch \(i\), and retaining an orthogonal output flag.

Its one-shot Holevo quantity satisfies the exact formula

$$
\boxed{
\chi(\Gamma)
=
\log\sum_i 2^{\chi(\Phi_i)}.
}
\tag{DS}
$$

To see this, an ensemble induces branch probabilities \(p_i\), so its Holevo information is at most

$$
H(p)+\sum_i p_i\chi(\Phi_i).
$$

Maximizing over \(p\) gives \(\log\sum_i2^{\chi(\Phi_i)}\), attained by

$$
p_i=\frac{2^{\chi(\Phi_i)}}{\sum_j2^{\chi(\Phi_j)}}.
$$

### Symmetric conjugate pair

Let

$$
x=\chi(\Phi)=\chi(\Psi),
\qquad
z=\chi(\Phi\otimes\Psi),
\qquad
g=z-2x.
$$

Take

$$
\Gamma=\Phi\oplus\Psi.
$$

Then

$$
\chi(\Gamma)=x+1.
$$

The two cross branches \(\Phi\otimes\Psi\) and
\(\Psi\otimes\Phi\) imply

$$
\chi(\Gamma^{\otimes2})\ge z+1.
$$

Therefore

$$
\boxed{
\chi(\Gamma^{\otimes2})-2\chi(\Gamma)
\ge g-1.
}
$$

Thus equal-capacity conjugate pairs need no balancing and lose at most one bit.

The primitive dimensions are

$$
\dim A_\Gamma=\dim A_\Phi+\dim A_\Psi,
$$

$$
\dim B_\Gamma=\dim B_\Phi+\dim B_\Psi,
$$

and, because the Choi matrices occupy orthogonal blocks,

$$
e_\Gamma^{\min}=e_\Phi^{\min}+e_\Psi^{\min}.
$$

For the Weyl-extended conjugate pair at outer exponent \(n\),

$$
\dim A_{\Gamma_n}=2d^{3n},
\qquad
\dim B_{\Gamma_n}=2d^n,
\qquad
e_{\Gamma_n}^{\min}\le2(d^2e)^n.
$$

The self-Holevo defect is

$$
n\delta_J+o(n)-1,
$$

while all charged logarithmic dimensions are \(O(n)\).

### Unequal capacities

Let

$$
x=\chi(\Phi),\qquad
y=\chi(\Psi),\qquad
z=\chi(\Phi\otimes\Psi),
\qquad
g=z-x-y.
$$

Take

$$
\Gamma=\Phi^{\oplus a}\oplus\Psi^{\oplus b}.
$$

Then

$$
\chi(\Gamma)=\log(a2^x+b2^y),
$$

while the \(2ab\) ordered cross branches give

$$
\chi(\Gamma^{\otimes2})
\ge z+\log(2ab).
$$

Writing

$$
t=\frac{a2^x}{b2^y},
$$

one obtains

$$
\boxed{
\chi(\Gamma^{\otimes2})-2\chi(\Gamma)
\ge
g-
\log\frac{(1+t)^2}{2t}.
}
$$

If \(x\ge y\), choose

$$
a=1,\qquad
b=\left\lceil2^{x-y}\right\rceil.
$$

Then \(t\in[1/2,1]\), and

$$
\log\frac{(1+t)^2}{2t}
\le\log\frac94<1.17.
$$

The multiplicity satisfies

$$
\log(a+b)\le |x-y|+2.
$$

For an \(n\)-copy block,

$$
|x-y|
\le
\max\{\log\dim B_{\Phi_n},
\log\dim B_{\Psi_n}\}
=
O(n).
$$

Hence the general balancing construction has **linear overhead in charged logarithmic dimension**, not constant overhead. It nevertheless preserves a positive defect-to-size ratio.

---

## 10. Why an orientation-insensitive tensorization cannot work

The Bell witness also proves that the required estimate must be self-specific.

The pure Bell input for \(L\otimes\overline L\) has output entropy at most

$$
b_J
=
2\log q-\frac{J\log m}{m}.
$$

For that same pure input, the complementary output under
\(C\otimes\overline C\) has the same nonzero spectrum. Since \(S_2\le S\),

$$
p_1(C\otimes\overline C)
\ge
2^{-b_J}
=
q^{-2}m^{J/m}.
$$

Under the positive-gap condition,

$$
m^{J/m}>A^2
$$

and hence

$$
p_1(C\otimes\overline C)
>
\left(\frac Aq\right)^2.
$$

For \((WK)\), the same conclusion holds with \(A\) replaced by \(K_JA\) whenever the resulting defect is positive.

Therefore no functional that proves

$$
p_1(\Phi\otimes\Psi)
\le p_1(\Phi)p_1(\Psi)
$$

uniformly for both \(\Psi=C\) and \(\Psi=\overline C\) can establish the desired result. This explains why the new orbit-block criterion keeps the remaining map equal to \(C^{\otimes s}\) and does not automatically control the conjugate cross-pair.

---

## 11. No-go cross-check

| Candidate route                                                   | Audit result                                                                                                                                  |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed-\(r\) Haar strong convergence                               | Wrong quantifier order. It gives no one finite \(D\) and tuple valid for all \(r\).                                                           |
| Bordenave–Collins product-group theorem                           | Its tensor legs use independent Haar families; \((R2)\) repeats the same tuple on both legs.                                                  |
| Ordinary pure-state or coefficient nets                           | They can uniformize one fixed \(r\), but the cone dimension grows as \(q^{2r}\); no fixed-\(D\) all-\(r\) intersection follows.               |
| Positive equal-diagonal reduction                                 | Valid, but \(\mathcal K_{q,r}\) still contains rank-one maximally coherent correlation matrices.                                              |
| Existing positive \(r=2\) subclasses                              | They cover proper subsets of \(\mathcal K_{m,2}\), not all positive equal-diagonal coefficients.                                              |
| Unrestricted \(2\!\to\!2\), cb, or replica norm                   | Too strong. The replica operator has a maximally entangled eigenvector with eigenvalue one, and the unprocessed orbit-block ratio is \(q-1\). |
| Scalar \(1\!\to\!2\), projective norms, termwise Kadison/Haagerup | They retain a rank or order-one loss that is much larger than \(A-1\).                                                                        |
| Lower-marginal induction                                          | Fails already structurally at \(r=3\), where the fully centered term has zero coefficient in all marginal sums.                               |
| Montanaro random-subspace theorem                                 | The Stinespring projector here is singular relative to Haar Grassmannian measure; the resulting exponent is also too weak.                    |
| PPT relaxation                                                    | Its \(m^{-J/2}\) floor is parametrically larger than the required \(m^{-J}\)-scale purity.                                                    |
| Real, orthogonal, or conjugation-closed tuples                    | The \(r=2\) Bell collision violates the target in the positive-gap regime.                                                                    |
| Generic complex Bell diagnostic                                   | Passing one Bell input does not control the global entangled-input supremum.                                                                  |
| Fresh randomness at every copy                                    | Changes the channel and violates the frozen-tuple quantifier.                                                                                 |
| Absolute-unbounded construction                                   | Does not control \(D(J)\), hence does not establish a positive defect/full-size ratio.                                                        |
| Nonminimal environment padding                                    | Irrelevant because only the minimal Stinespring environment is charged.                                                                       |
| WHGAP                                                             | Not used and logically unrelated.                                                                                                             |

---

## First statement still requiring independent verification

The exact earliest unresolved statement is \((R2)\), equivalently \((OB_2)\), for one finite complex tuple satisfying the one-copy bound.

A new, strictly narrower sufficient lemma is:

$$
\boxed{
\exists\,m,D,\eta,U
\quad\text{such that}\quad
p_1(C)\le\frac Am
\quad\text{and}\quad
\kappa_1(U)\le A-1.
}
$$

Explicitly, for every \(T:\mathbb C^D\to\mathbb C^D\) with
\(\|T\|_2=1\),

$$
\sum_{v\ne w}
\left\|
C\!\left(
T(U_w^*U_v)^{\mathsf T}T^*
\right)
\right\|_2^2
\le
(A-1)m\,\|C(TT^*)\|_2^2.
\tag{First finite gate}
$$

Its truth would prove the full physical \(r=2\) bound. The all-copy sufficient extension is

$$
\sup_{s\ge1}\kappa_s(U)\le K_JA-1
$$

with

$$
\limsup_{J\to\infty}\frac{\log K_J}{J}<\frac{c_m}{2}.
$$

Neither the finite \(s=1\) statement nor its all-\(s\) extension follows from the currently cited strong-convergence theorems, and no counterexample to them for generic independent complex tuples has been established here.

[1]: https://arxiv.org/html/2608.25961 "https://arxiv.org/html/2608.25961"
[2]: https://arxiv.org/abs/1907.07856 "https://arxiv.org/abs/1907.07856"
[3]: https://arxiv.org/html/2304.05714v2 "https://arxiv.org/html/2304.05714v2"
[4]: https://arxiv.org/html/1307.0707v3 "https://arxiv.org/html/1307.0707v3"

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-01-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-01-local-audit.md bytes=5757 sha256=f9380ac394ccbebabd8b77a3d54b6f85037f3c26020260ffbfc342de54d1ea2a -->

# Round 1 local audit

Date: 2026-09-11

Status: equation-level local audit completed. This is not an independent external review.

## Verdict

The web answer does not prove or disprove the finite-dimensional full-size theorem. Its verdict
`OPEN WITH EARLIEST GAP` is correct relative to the supplied auditing record. The first
unresolved construction gate is the same-tuple, globally entangled `J=1, r=2` purity inequality.

The new physical orbit-block formulas are valid reductions. Existence of a tuple satisfying
their ratio or all-copy inequalities remains **CONJECTURED**.

## Status ledger

| Item | Local status | Meaning |
|---|---|---|
| Quantifier order and dimensions | VERIFIED | One finite tuple and `D` precede every `r` and every input. |
| Centered hierarchy | VERIFIED | Exact reformulation, but no induction from lower marginals. |
| Regularized-purity formulation | VERIFIED | Supermultiplicativity makes the limit the supremum of finite-copy roots. |
| Positive equal-diagonal duality | VERIFIED | Agrees with the earlier local derivation. |
| Orbit-block identity `(OB)` | VERIFIED | Exact for every pure input with the stated transpose convention. |
| `(Rec)`, `(Prod)`, and conditional `(PL)/(WK)` | VERIFIED | Correct conditional reductions. |
| Exact two-copy inequality `(OB_2)` | VERIFIED AS A REFORMULATION | Equivalent to the physical `r=2` target. |
| Ratio bound `(OL_1)` / `kappa_1<=A-1` | OPEN / CONJECTURED | Sufficient but stronger than `(OB_2)`. |
| Uniform all-copy control of `kappa_s` | OPEN / CONJECTURED | Still required for `(P)` or `(WK)`. |
| Fukuda transfer and dimension bounds | VERIFIED | Exact exponent-wise transfer; Kraus count gives the environment bound. |
| Flagged direct-sum algebra | VERIFIED | Symmetric loss at most one bit; unequal balancing adds `O(n)` log-size. |
| Full-size theorem | OPEN | Conditional on proving `(P)` or admissible `(WK)` for one frozen tuple. |

## Orbit-block check

Every unit vector on `H tensor H^(tensor s)` is

    |psi_T> = sum_i |i> tensor T|i>,    ||T||_2 = 1.

With `A_vw=W_w^*W_v`, direct expansion gives

    Tr_H[(A_vw tensor I)|psi_T><psi_T|] = T A_vw^T T^*.

Hence the `(v,w)` output block is

    q^(-1) C^(tensor s)(T A_vw^T T^*).

For `v=w` this is `q^(-1) C^(tensor s)(TT^*)`. Summing the squared
Hilbert--Schmidt norms of all blocks proves `(OB)` exactly. The block matrix
`[T A_vw^T T^*]_(v,w) = q(C tensor id)(|psi_T><psi_T|)` is positive, has
equal diagonal blocks, and rank at most `d`.

Define `p_s=sup_rho ||C^(tensor s)(rho)||_2^2`. Convexity permits a pure
maximizer. Substitution of the definition of `kappa_s` into `(OB)` gives

    p_(s+1) <= ((1+kappa_s)/q) p_s.

Together with `p_1<=A/q`,

    p_r <= (A/q^r) product_(s=1)^(r-1) (1+kappa_s).

Thus `kappa_s<=A-1` for every `s` implies `(P)`. With `B=K_J A`,
`kappa_s<=B-1` for every `s` implies `(WK)`. These are valid implications,
not proofs of the needed uniform bounds.

At `s=1`, multiplying `(OB)` by `q^2` yields the exact target

    q||C(TT^*)||_2^2 + sum_(v!=w)||C(T(W_w^*W_v)^T T^*)||_2^2 <= A^2.

The proposed ratio bound `(OL_1)` is strictly stronger. Combined with the
one-copy estimate it implies the displayed target, but failure of `(OL_1)`
would not refute `(OB_2)`.

## Sharp product-input lower bound

There is an additional exact check that was not stated in the web answer. For
unit vectors `x,y`, take the rank-one map

    T = |x><bar y|.

Then `TT^*=|x><x|` and

    T(W_w^*W_v)^T T^* = <y|W_w^*W_v|y> |x><x|.

Since the diagonal Gram entries are one,

    sum_(v!=w) |<y|W_w^*W_v|y>|^2
      = q^2 ||C(|y><y|)||_2^2 - q.

The factor `||C^(tensor s)(|x><x|)||_2^2` cancels from the defining ratio, so

    kappa_s(U) >= q p_1(C) - 1       for every s>=1.

Thus `kappa_s<=A-1` is threshold-sharp on product inputs when the one-copy
bound is close to saturation. At `s=1`, it is equivalent to the conditional
inequality

    ||(C tensor C)(|psi_T><psi_T|)||_2^2
       <= (A/q) ||C(TT^*)||_2^2.

This is stronger than the global two-copy target because its right side keeps
the actual purity of the second marginal output rather than replacing it by
the one-copy supremum. Any next-round proof must therefore rule out additional
conditional amplification from entangled `T`; product inputs already consume
all one-copy slack.

## Primary-source checks

1. Collins--Youn arXiv:1907.07856v2, Theorems 3.3--3.4, contains the quoted
   free-group coefficient and infinite-dimensional all-copy bounds; the paper
   says finite-dimensional transfer of its approach is unclear.
2. Bordenave--Collins arXiv:2304.05714v2, Theorem 1.1 and Corollary 1.2,
   confirms `d^70<=N`, `p=N^(1/(16d+80))`, and the coefficient-dimension
   threshold. Section 9.3 uses distinct independent `U_(i,j)` families on
   different tensor legs, not repeated `(U_i tensor U_i)` legs.
3. Fukuda arXiv:1307.0707v3, Lemma 6.2, gives the exact identity for all
   tensor exponents and defines `tilde Phi:M_(k^2 l)->M_k`. The explicit
   Kraus family has size at most `k^2 e_Phi`, hence minimal environment at
   most `k^2 e_Phi<=k^3 l`.
4. Lovitz--Wu arXiv:2608.25961v1 (26 August 2026), Section 1.3, explicitly
   records that finite-dimensional regularized-MOE / classical-capacity
   additivity remains unclear. This is a current status statement, not a proof
   that no later manuscript exists; a targeted arXiv search on 2026-09-11
   found no contrary result.

## Next-round boundary

The highest-leverage next target is the finite `J=1, r=2` physical gate:

1. prove `(OB_2)` directly for one frozen complex tuple;
2. prove the stronger `(OL_1)` ratio bound; or
3. find a universal physical `T` obstruction to `(OL_1)`, while explicitly
   distinguishing that from a refutation of `(OB_2)`.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-01-local-audit.md -->


# ROUND 002

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-02-prompt.md bytes=4965 sha256=904da6f3a10b6d69b2ed4712dce20492824ea6b0e92fe339d65955e3c26d5878 -->

# Round 2 — adversarial audit of the physical orbit-block ratio

Your previous answer correctly returned `OPEN WITH EARLIEST GAP` and proposed the
physical orbit-block constants `kappa_s(U)`. We independently checked the vectorization,
transpose convention, block-norm identity `(OB)`, recursion `(Rec)`, and product bound
`(Prod)`: those reductions are algebraically valid. Do not repeat the broad full-size
blueprint. This round must attack the first finite gate and must not call a conditional
reduction a proof.

## Frozen one-layer setup

Specialize to `J=1`, so `q=m`, `H=C^D`,

    C(X)_(v,w) = m^(-1) Tr(X U_w^* U_v),

for one finite deterministic complex tuple `U=(U_1,...,U_m) in U(D)^m`, and

    A = 1 + 9(1+eta)^2/m,        eta>0,        ln m>18.

Assume the audited one-copy bound

    p_1(C):=sup_rho ||C(rho)||_2^2 <= A/m.

For `T:H->H` with `||T||_2=1`, set

    rho_T = TT^*,
    X_vw(T) = T(U_w^*U_v)^T T^*,

and

    R_U(T) = [sum_(v!=w) ||C(X_vw(T))||_2^2]
             / [m ||C(rho_T)||_2^2],

    kappa_1(U)=sup_T R_U(T).

The exact pure-input identity is

    ||(C tensor C)(|psi_T><psi_T|)||_2^2
      = m^(-1)||C(rho_T)||_2^2
        + m^(-2) sum_(v!=w)||C(X_vw(T))||_2^2.            (OB)

Hence the exact physical two-copy target is

    m||C(rho_T)||_2^2
      + sum_(v!=w)||C(X_vw(T))||_2^2 <= A^2              (OB2)

for every Hilbert--Schmidt unit `T`. The stronger conditional ratio condition

    kappa_1(U) <= A-1                                      (OL1)

implies `(OB2)`, but is not equivalent to it.

## New sharpness observation to verify

For unit vectors `x,y`, take `T=|x><bar y|`. Then

    TT^*=|x><x|,
    X_vw(T)=<y|U_w^*U_v|y>|x><x|,

so the common output-purity factor cancels and

    R_U(T)=m||C(|y><y|)||_2^2-1.

Therefore

    kappa_1(U) >= m p_1(C)-1.                              (LB)

The same rank-one construction gives `kappa_s(U)>=m p_1(C)-1` for every `s`.
Thus `(OL1)` is threshold-sharp on product inputs when the one-copy estimate
nearly saturates. It asks whether entangled `T` causes any additional conditional
`2`-purity amplification.

## Exact task

Give one precise verdict on the existential finite-dimensional statement

    (E1)  There exist finite m,D, eta>0, and one complex tuple U such that
          ln m>18, p_1(C)<=A/m, and kappa_1(U)<=A-1.

The verdict must be `PROVED`, `DISPROVED`, or `OPEN WITH EARLIEST GAP`.

1. First rederive `(OB)`, `(OB2)`, and `(LB)` independently, checking every
   transpose, adjoint, normalization, and quantifier. If any is wrong, stop at the
   first wrong equality and give the corrected statement.
2. Determine the exact relation among `(OL1)`, maximum-output `2`-norm
   multiplicativity for `C tensor C`, and the weaker global target `(OB2)`.
   State implications and non-implications; do not silently replace the actual
   denominator `||C(TT^*)||_2^2` by `p_1(C)`.
3. Rewrite `R_U(T)` as an exact generalized Rayleigh quotient, positive-map
   inequality, frame inequality, or spectral condition if possible. The reformulation
   must retain the fact that all orbit blocks arise from the same physical `T` and
   the same tuple `U`.
4. Try to settle `(E1)` analytically. Either:
   - prove a uniform upper bound for one finite complex tuple;
   - construct, for every candidate tuple satisfying the one-copy bound, a physical
     entangled `T` with `R_U(T)>A-1`; or
   - identify the earliest exact inequality whose truth is presently unknown.
5. If you disprove `(OL1)`, separately test whether the same `T` violates `(OB2)`.
   Failure of the stronger ratio condition is not a disproof of the two-copy target.
6. If `(E1)` stays open, prove one new strictly narrower lemma that materially
   advances it. It must go beyond rank-one/product inputs, diagonal coefficients,
   a single Bell input, or an already audited simple-tensor/rook/spectral-flat
   subclass. Examples of acceptable progress include a sharp bound for a
   nontrivial Schmidt-rank range with explicit constants, a valid convex/extreme-point
   reduction for the physical `T`-set, or a theorem reducing the supremum to an
   explicitly characterized smaller family.
7. Any probabilistic argument must give a single finite-`D` event for the supremum
   over all `T`; a separate fixed-`T` or finite-net assertion without its Lipschitz
   and probability costs is insufficient. Do not use independent Haar copies on
   the two tensor legs.
8. Do not use unrestricted cb or `2->2` control, orientation-insensitive
   multiplicativity that would also suppress `C tensor bar C`, numerical evidence,
   or fresh randomness at each copy.
9. End with a short audit ledger: what is proved in this answer, what remains
   `CONJECTURED`, and the first statement needing independent verification.

All mathematical claims must be self-contained. Cite exact theorem numbers and
hypotheses for imported results. Do not provide hidden chain-of-thought; provide only
the public derivation.


<!-- END HISTORICAL FILE path=work/round-02-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-02-response.md bytes=19298 sha256=afe5076cb7d51fb85bddff968fb044ff85259b7d25960ae6f65719e8fa6a17ae -->

# Verdict: **PROVED — for \((E1)\) exactly as stated**

The literal existential statement \((E1)\) is true. The decisive issue is that \((E1)\) imposes no upper bound on \(\eta\), hence no small-\(A\) or positive-gap condition. One may choose \(A=m\), at which point the one-copy bound and the orbit-block ratio bound become universally true.

This does **not** settle the physically relevant gate from Round 1. The strengthened statement with

$$
\frac{\log_2m}{m}>2\log_2 A
\qquad\Longleftrightarrow\qquad
A^2<m^{1/m}
\tag{Gap}
$$

remains open.

No external theorem is used below; all claims follow from finite-dimensional linear algebra.

---

## 1. Independent derivation of \((OB)\), \((OB2)\), and \((LB)\)

Fix the computational basis in which the transpose is taken, and write

$$
A_{vw}=U_w^*U_v.
$$

For \(T\in M_D\) with \(\|T\|_2=1\), use the vectorization convention

$$
|\psi_T\rangle=\sum_{i=1}^D |i\rangle\otimes T|i\rangle .
$$

Then

$$
\langle\psi_T|\psi_T\rangle=\operatorname{Tr}(T^*T)=1.
$$

For arbitrary \(A,B\in M_D\),

$$
\begin{aligned}
\langle\psi_T|A\otimes B|\psi_T\rangle
&=\sum_{i,j}\langle i|A|j\rangle
   \langle Ti|B|Tj\rangle\\
&=\sum_{i,j}A_{ij}(T^*BT)_{ij}\\
&=\operatorname{Tr}(A^{\mathsf T}T^*BT)\\
&=\operatorname{Tr}(TA^{\mathsf T}T^*B).
\end{aligned}
\tag{1}
$$

The \(((v,a),(w,b))\) matrix entry of the two-copy output is therefore

$$
\begin{aligned}
&\bigl[(C\otimes C)(|\psi_T\rangle\langle\psi_T|)\bigr]_{(v,a),(w,b)}
\\
&\quad=
\frac1{m^2}
\langle\psi_T|A_{vw}\otimes A_{ab}|\psi_T\rangle\\
&\quad=
\frac1{m^2}
\operatorname{Tr}\!\left(
T A_{vw}^{\mathsf T}T^*A_{ab}
\right).
\end{aligned}
$$

With

$$
X_{vw}(T)=TA_{vw}^{\mathsf T}T^*,
$$

and

$$
C(X)_{a,b}=\frac1m\operatorname{Tr}(XA_{ab}),
$$

this becomes

$$
\boxed{
\bigl[(C\otimes C)(|\psi_T\rangle\langle\psi_T|)\bigr]_{(v,w)}
=
\frac1m\,C(X_{vw}(T)),
}
\tag{2}
$$

where the right-hand side is the \(m\times m\) block indexed by \(v,w\).

For \(v=w\),

$$
A_{vv}=I,\qquad X_{vv}(T)=TT^*=\rho_T.
$$

The Hilbert–Schmidt norm of a block matrix is the sum of the squared Hilbert–Schmidt norms of its blocks. Hence

$$
\begin{aligned}
\left\|
(C\otimes C)(|\psi_T\rangle\langle\psi_T|)
\right\|_2^2
&=
\frac1{m^2}
\sum_{v,w}\|C(X_{vw}(T))\|_2^2\\
&=
\frac1m\|C(\rho_T)\|_2^2
+
\frac1{m^2}
\sum_{v\ne w}\|C(X_{vw}(T))\|_2^2 .
\end{aligned}
$$

Thus

$$
\boxed{
\left\|
(C\otimes C)(|\psi_T\rangle\langle\psi_T|)
\right\|_2^2
=
m^{-1}\|C(\rho_T)\|_2^2
+
m^{-2}\sum_{v\ne w}\|C(X_{vw}(T))\|_2^2.
}
\tag{OB}
$$

The physical two-copy target is

$$
\left\|
(C\otimes C)(|\psi_T\rangle\langle\psi_T|)
\right\|_2^2
\le \frac{A^2}{m^2}.
$$

Multiplying \((OB)\) by \(m^2\) gives exactly

$$
\boxed{
m\|C(\rho_T)\|_2^2+
\sum_{v\ne w}\|C(X_{vw}(T))\|_2^2
\le A^2.
}
\tag{OB2}
$$

There is no missing transpose, adjoint, or normalization factor.

### Rank-one lower bound

Let \(x,y\) be unit vectors and take

$$
T=|x\rangle\langle\bar y|.
$$

Then

$$
TT^*=|x\rangle\langle x|.
$$

Moreover,

$$
\begin{aligned}
X_{vw}(T)
&=
|x\rangle
\langle\bar y|A_{vw}^{\mathsf T}|\bar y\rangle
\langle x|\\
&=
\langle y|A_{vw}|y\rangle
\,|x\rangle\langle x|,
\end{aligned}
$$

because

$$
\langle\bar y|A^{\mathsf T}|\bar y\rangle
=
\langle y|A|y\rangle.
$$

Put

$$
d_x=\|C(|x\rangle\langle x|)\|_2^2.
$$

Then

$$
\|C(X_{vw}(T))\|_2^2
=
|\langle y|A_{vw}|y\rangle|^2 d_x.
$$

Also,

$$
\begin{aligned}
\|C(|y\rangle\langle y|)\|_2^2
&=
\frac1{m^2}
\sum_{v,w}
|\langle y|A_{vw}|y\rangle|^2\\
&=
\frac1{m^2}
\left[
m+
\sum_{v\ne w}
|\langle y|A_{vw}|y\rangle|^2
\right].
\end{aligned}
$$

Therefore

$$
\sum_{v\ne w}
|\langle y|A_{vw}|y\rangle|^2
=
m^2\|C(|y\rangle\langle y|)\|_2^2-m.
$$

The common factor \(d_x>0\) cancels:

$$
\begin{aligned}
R_U(T)
&=
\frac{
d_x\left[
m^2\|C(|y\rangle\langle y|)\|_2^2-m
\right]
}{
m d_x
}\\
&=
m\|C(|y\rangle\langle y|)\|_2^2-1.
\end{aligned}
$$

The function \(\rho\mapsto\|C(\rho)\|_2^2\) is convex. If
\(\rho=\sum_i t_i|\phi_i\rangle\langle\phi_i|\), then

$$
\|C(\rho)\|_2^2
\le
\sum_i t_i\|C(|\phi_i\rangle\langle\phi_i|)\|_2^2,
$$

so its maximum is attained on a pure state. Taking the supremum over \(y\) yields

$$
\boxed{
\kappa_1(U)\ge mp_1(C)-1.
}
\tag{LB}
$$

The stated sharpness observation is correct.

---

## 2. Exact relation among \((OL1)\), multiplicativity, and \((OB2)\)

Write

$$
p=p_1(C),
\qquad
d_T=\|C(\rho_T)\|_2^2,
\qquad
r_T=R_U(T),
$$

and

$$
P_T=
\left\|
(C\otimes C)(|\psi_T\rangle\langle\psi_T|)
\right\|_2^2.
$$

From \((OB)\),

$$
\boxed{
P_T=\frac{d_T}{m}(1+r_T).
}
\tag{3}
$$

Because \(C(\rho_T)\) is a density matrix in dimension \(m\),

$$
\frac1m\le d_T\le p\le\frac Am.
\tag{4}
$$

### Three exact pointwise conditions

The ratio condition is

$$
(OL1)
\quad\Longleftrightarrow\quad
r_T\le A-1
\quad\text{for every }T.
\tag{5}
$$

Maximum-output \(2\)-norm multiplicativity for \(C\otimes C\) is

$$
\sup_\sigma
\|(C\otimes C)(\sigma)\|_2^2=p^2.
$$

Product inputs give the lower bound \(p^2\), and convexity allows restriction to pure inputs. Thus multiplicativity is equivalent to

$$
P_T\le p^2
\quad\text{for every }T,
$$

or, using (3),

$$
\boxed{
r_T\le\frac{mp^2}{d_T}-1
\quad\text{for every }T.
}
\tag{M2}
$$

The weaker physical target \((OB2)\) is equivalent to

$$
P_T\le\frac{A^2}{m^2},
$$

or

$$
\boxed{
r_T\le\frac{A^2}{m d_T}-1
\quad\text{for every }T.
}
\tag{6}
$$

### Proven implications

Since \(d_T\le A/m\),

$$
A-1
\le
\frac{A^2}{m d_T}-1.
$$

Therefore

$$
\boxed{(OL1)\Longrightarrow(OB2).}
$$

Indeed,

$$
P_T
\le
\frac{A}{m}d_T
\le
\frac{A^2}{m^2}.
$$

Similarly, since \(p\le A/m\),

$$
\frac{mp^2}{d_T}-1
\le
\frac{A^2}{m d_T}-1,
$$

and hence

$$
\boxed{\text{multiplicativity}\Longrightarrow(OB2).}
$$

A still stronger ratio statement is

$$
\kappa_1(U)\le mp-1.
\tag{7}
$$

It implies multiplicativity because

$$
P_T
\le
\frac{d_T}{m}(mp)
=
p\,d_T
\le p^2.
$$

By \((LB)\), condition (7) would be threshold-sharp:

$$
\kappa_1(U)=mp-1.
$$

### \((OL1)\) is not equivalent to multiplicativity

From \((OL1)\) alone one obtains only

$$
P_T\le\frac A m d_T\le \frac A m p.
$$

This is bounded by \(p^2\) exactly when

$$
\frac Am\le p.
$$

Combined with \(p\le A/m\), this requires

$$
p=\frac Am.
$$

Consequently:

* If \(p=A/m\), then \((OL1)\) implies multiplicativity.
* If \(p<A/m\), \((OL1)\) by itself does not yield multiplicativity; its derived upper bound \(Ap/m\) is strictly larger than \(p^2\).
* Multiplicativity does not imply \((OL1)\), even when \(p=A/m\). An exact counterexample is given in Section 4.
* Both \((OL1)\) and multiplicativity are stronger than \((OB2)\), but in different ways: \((OL1)\) uses a constant ratio threshold, whereas multiplicativity uses the \(T\)-dependent threshold \(mp^2/d_T-1\).

No replacement of \(d_T\) by \(p\) has been made inside the exact conditions.

---

## 3. Exact physical-frame and generalized Rayleigh formulation

Let

$$
\mathscr H_{\mathrm{HS}}=M_D
$$

with Hilbert–Schmidt inner product

$$
\langle X,Y\rangle_{\mathrm{HS}}
=
\operatorname{Tr}(X^*Y).
$$

For \(a,v\in[m]\), define

$$
z_{a,v}(T)=U_a T U_v^{\mathsf T}\in\mathscr H_{\mathrm{HS}}.
$$

Then

$$
\begin{aligned}
\langle z_{b,w}(T),z_{a,v}(T)\rangle_{\mathrm{HS}}
&=
\operatorname{Tr}\!\left[
\bar U_w T^*U_b^*U_aT U_v^{\mathsf T}
\right]\\
&=
\operatorname{Tr}\!\left[
T U_v^{\mathsf T}\bar U_w T^*U_b^*U_a
\right]\\
&=
\operatorname{Tr}\!\left[
X_{vw}(T)A_{ab}
\right].
\end{aligned}
$$

Therefore

$$
C(X_{vw}(T))_{a,b}
=
\frac1m
\langle z_{b,w}(T),z_{a,v}(T)\rangle_{\mathrm{HS}}.
\tag{8}
$$

Define the positive frame operators on \(\mathscr H_{\mathrm{HS}}\)

$$
F_{T,v}
=
\sum_{a=1}^m
|z_{a,v}(T)\rangle\!\rangle
\langle\!\langle z_{a,v}(T)|.
$$

Equation (8) gives

$$
\boxed{
\|C(X_{vw}(T))\|_2^2
=
\frac1{m^2}
\operatorname{Tr}_{\mathscr H_{\mathrm{HS}}}
(F_{T,v}F_{T,w}).
}
\tag{9}
$$

Let

$$
F_T=
\sum_{a=1}^m
|U_aT\rangle\!\rangle
\langle\!\langle U_aT|.
$$

Right multiplication

$$
\mathsf R_v(Z)=ZU_v^{\mathsf T}
$$

is unitary on \(\mathscr H_{\mathrm{HS}}\), and

$$
F_{T,v}=\mathsf R_vF_T\mathsf R_v^*.
$$

Thus all \(F_{T,v}\) have the same Hilbert–Schmidt norm. Put

$$
Q_T=\operatorname{Tr}(F_T^2).
$$

For every \(v\),

$$
\operatorname{Tr}(F_{T,v}^2)=Q_T.
$$

Taking \(v=w\) in (9),

$$
\boxed{
\|C(\rho_T)\|_2^2=\frac{Q_T}{m^2}.
}
\tag{10}
$$

Combining (9) and (10),

$$
\begin{aligned}
R_U(T)
&=
\frac{
m^{-2}\sum_{v\ne w}\operatorname{Tr}(F_{T,v}F_{T,w})
}{
Q_T/m
}\\
&=
\frac{
\sum_{v\ne w}\operatorname{Tr}(F_{T,v}F_{T,w})
}{
mQ_T
}.
\end{aligned}
$$

Adding the \(m\) diagonal terms gives the exact frame quotient

$$
\boxed{
1+R_U(T)
=
\frac{
\operatorname{Tr}\left(\sum_v F_{T,v}\right)^2
}{
m\,\operatorname{Tr}(F_T^2)
}.
}
\tag{FR}
$$

### Positive-map Rayleigh quotient

Define the random-unitary map on operators over \(\mathscr H_{\mathrm{HS}}\),

$$
\mathfrak R_U(F)
=
\frac1m
\sum_{v=1}^m
\mathsf R_vF\mathsf R_v^*.
$$

Then

$$
\sum_vF_{T,v}=m\,\mathfrak R_U(F_T),
$$

so

$$
\boxed{
1+R_U(T)
=
m\,
\frac{
\|\mathfrak R_U(F_T)\|_2^2
}{
\|F_T\|_2^2
}.
}
\tag{RQ}
$$

Equivalently,

$$
\boxed{
\kappa_1(U)+1
=
m\sup_{\|T\|_2=1}
\frac{
\langle F_T,\mathfrak R_U^*\mathfrak R_U(F_T)\rangle
}{
\langle F_T,F_T\rangle
}.
}
\tag{11}
$$

The supremum is not over all operators. It is restricted to the physical, nonconvex family

$$
\mathcal F_U
=
\left\{
F_T=
\sum_a|U_aT\rangle\!\rangle
\langle\!\langle U_aT|
:
\|T\|_2=1
\right\}.
$$

Every \(F_T\) satisfies

$$
F_T\succeq0,\qquad
\operatorname{rank}F_T\le m,\qquad
\operatorname{Tr}F_T=m.
$$

Most importantly, the same tuple \(U\) appears simultaneously:

1. in the left orbit defining \(F_T\);
2. in the right-multiplication map \(\mathfrak R_U\).

Thus \((OL1)\) is exactly the physical-cone quadratic inequality

$$
\boxed{
m\,
\langle F_T,\mathfrak R_U^*\mathfrak R_U(F_T)\rangle
\le
A\,\langle F_T,F_T\rangle
\quad
\text{for every }\|T\|_2=1.
}
\tag{12}
$$

This is the requested generalized Rayleigh/spectral reformulation.

---

## 4. A sharp universal frame bound

For positive frame operators \(F_{T,v},F_{T,w}\),

$$
\operatorname{Tr}(F_{T,v}F_{T,w})\ge0.
$$

Hilbert–Schmidt Cauchy–Schwarz gives

$$
\operatorname{Tr}(F_{T,v}F_{T,w})
\le
\|F_{T,v}\|_2\|F_{T,w}\|_2
=
Q_T.
$$

There are \(m(m-1)\) off-diagonal pairs. Hence

$$
\sum_{v\ne w}
\operatorname{Tr}(F_{T,v}F_{T,w})
\le
m(m-1)Q_T.
$$

Using the exact formula for \(R_U(T)\),

$$
\boxed{
0\le R_U(T)\le m-1
\quad\text{for every }T.
}
\tag{13}
$$

Therefore

$$
\boxed{
0\le\kappa_1(U)\le m-1
\quad\text{for every finite tuple }U.
}
\tag{14}
$$

This bound is sharp.

Equality \(R_U(T)=m-1\) holds exactly when equality holds in every pairwise Hilbert–Schmidt Cauchy–Schwarz inequality. Since the \(F_{T,v}\) are positive and have equal norms, this is equivalent to

$$
F_{T,1}=F_{T,2}=\cdots=F_{T,m}.
\tag{15}
$$

This lemma applies to arbitrary Schmidt rank and is not a product-input or diagonal-coefficient argument.

---

## 5. Exact Weyl example: \((OL1)\) can fail while \((OB2)\) and multiplicativity hold

This example verifies that failure of the stronger ratio condition need not violate the physical two-copy target.

Let \(D\ge2\), set

$$
m=D^2,
$$

and define the Weyl unitaries on \(\mathbb C^D\),

$$
X|j\rangle=|j+1\bmod D\rangle,
\qquad
Z|j\rangle=\omega^j|j\rangle,
\qquad
\omega=e^{2\pi i/D},
$$

$$
U_{p,q}=X^pZ^q,
\qquad
p,q\in\mathbb Z_D.
$$

### The random-unitary channel is completely depolarizing

For a matrix unit \(E_{jk}=|j\rangle\langle k|\),

$$
Z^qE_{jk}Z^{-q}
=
\omega^{q(j-k)}E_{jk}.
$$

Averaging over \(q\) kills \(E_{jk}\) unless \(j=k\). Averaging the remaining diagonal matrix unit over \(p\) gives

$$
\frac1D\sum_pX^pE_{jj}X^{-p}=\frac ID.
$$

Therefore

$$
\boxed{
L(X)=\frac{\operatorname{Tr}X}{D}I_D.
}
\tag{16}
$$

### Exact one-copy purity of the complement

The normalized Weyl matrices \(U_{p,q}/\sqrt D\) form an orthonormal basis of \(M_D\). Let

$$
\mathcal W:\mathbb C^{D^2}\longrightarrow M_D,
\qquad
\mathcal W|p,q\rangle=\frac{U_{p,q}}{\sqrt D}.
$$

Let \(R_\rho\) denote right multiplication by \(\rho\):

$$
R_\rho(Y)=Y\rho.
$$

Its matrix in the normalized Weyl basis has entries

$$
\left[\mathcal W^*R_\rho\mathcal W\right]_{h,g}
=
\frac1D\operatorname{Tr}(U_h^*U_g\rho).
$$

On the other hand,

$$
C(\rho)_{g,h}
=
\frac1{D^2}\operatorname{Tr}(\rho U_h^*U_g).
$$

Hence, up to matrix transpose,

$$
C(\rho)
=
\frac1D\,\mathcal W^*R_\rho\mathcal W.
$$

Transpose and unitary conjugation preserve the Hilbert–Schmidt norm. If the eigenvalues of \(\rho\) are \(\lambda_1,\ldots,\lambda_D\), then the eigenvalues of \(R_\rho\) are the \(\lambda_j\), each repeated \(D\) times. Therefore

$$
\boxed{
\|C(\rho)\|_2^2
=
\frac{\operatorname{Tr}\rho^2}{D}.
}
\tag{17}
$$

Consequently,

$$
\boxed{
p_1(C)=\frac1D=\frac1{\sqrt m}.
}
\tag{18}
$$

### Two-copy purity

The channel \(C\otimes C\) is complementary to \(L\otimes L\). For every pure bipartite input,

$$
(L\otimes L)(|\psi\rangle\langle\psi|)
=
\frac{I_{D^2}}{D^2}.
$$

The two complementary outputs of a pure Stinespring state have the same nonzero eigenvalues. Hence

$$
\boxed{
\left\|
(C\otimes C)(|\psi\rangle\langle\psi|)
\right\|_2^2
=
\frac1{D^2}
=
\frac1m
}
\tag{19}
$$

for every pure \(|\psi\rangle\).

Thus

$$
\sup_\sigma\|(C\otimes C)(\sigma)\|_2^2
=
\frac1m
=
p_1(C)^2.
$$

Maximum-output \(2\)-norm multiplicativity holds exactly.

For \(\rho_T=TT^*\), equations (3), (17), and (19) give

$$
\frac1m
=
\frac{1}{m}
\frac{\operatorname{Tr}\rho_T^2}{D}
(1+R_U(T)).
$$

Therefore

$$
\boxed{
R_U(T)
=
\frac{D}{\operatorname{Tr}\rho_T^2}-1.
}
\tag{20}
$$

Since

$$
\operatorname{Tr}\rho_T^2\ge\frac1D,
$$

with equality for

$$
T=\frac I{\sqrt D},
$$

one obtains

$$
\boxed{
\kappa_1(U)=D^2-1=m-1.
}
\tag{21}
$$

Rank-one \(T\) gives only

$$
mp_1(C)-1=D-1.
$$

Thus maximally entangled \(T\) creates a genuine additional conditional amplification:

$$
D-1
\quad\longrightarrow\quad
D^2-1.
$$

### Failure of \((OL1)\) without failure of \((OB2)\)

Choose

$$
A=D=\sqrt m.
$$

This is realizable by

$$
1+\eta=\frac{D\sqrt{D-1}}{3},
$$

because

$$
1+\frac{9(1+\eta)^2}{m}
=
1+(D-1)
=
D.
$$

Choose \(D>e^9\), so \(\ln m=2\ln D>18\) and \(\eta>0\).

Then

$$
p_1(C)=\frac1D=\frac Am,
$$

but

$$
\kappa_1(U)=D^2-1>D-1=A-1.
$$

Thus \((OL1)\) fails.

For the same maximally entangled \(T=I/\sqrt D\),

$$
d_T=\frac1m,
\qquad
R_U(T)=m-1.
$$

Hence

$$
\sum_{v\ne w}\|C(X_{vw}(T))\|_2^2
=
m d_T R_U(T)=m-1.
$$

The left side of \((OB2)\) is

$$
m d_T+(m-1)
=
1+(m-1)
=
m
=
A^2.
$$

Therefore

$$
\boxed{
(OB2)\text{ holds with equality although }(OL1)\text{ fails.}
}
$$

This gives an exact within-class proof that multiplicativity and \((OB2)\) do not imply \((OL1)\).

---

## 6. Proof of \((E1)\) as literally quantified

Choose any integer

$$
m>e^{18}.
$$

Set

$$
\boxed{
\eta=
\frac{\sqrt{m(m-1)}}{3}-1.
}
$$

Then \(\eta>0\), and

$$
\begin{aligned}
A
&=
1+\frac{9(1+\eta)^2}{m}\\
&=
1+\frac{9}{m}\frac{m(m-1)}9\\
&=
m.
\end{aligned}
\tag{22}
$$

For every channel \(C\),

$$
p_1(C)\le1=\frac Am,
$$

because the purity of a density matrix is at most one.

For every tuple \(U\), the frame bound (14) gives

$$
\kappa_1(U)\le m-1=A-1.
$$

Thus, in fact, once \(A=m\), **every** finite tuple satisfies the two inequalities in \((E1)\).

For a completely explicit deterministic witness, take

$$
D=1,
\qquad
U_1=\cdots=U_m=1\in U(1).
$$

The unique input density operator is \(1\), and

$$
C(1)=\frac1m
\begin{pmatrix}
1&\cdots&1\\
\vdots&&\vdots\\
1&\cdots&1
\end{pmatrix},
$$

which is a rank-one projection. Hence

$$
p_1(C)=1=\frac Am.
$$

Every Hilbert–Schmidt unit \(T\in M_1\) satisfies \(|T|=1\), and every \(X_{vw}(T)=1\). Therefore

$$
R_U(T)
=
\frac{m(m-1)}m
=
m-1=A-1.
$$

All quantifiers are frozen correctly:

$$
\exists\,m,D,\eta,U
\quad
\forall\,T,
$$

with no randomness and no copy-dependent choice.

Therefore

$$
\boxed{(E1)\text{ is PROVED.}}
$$

---

## 7. Why this does not close the intended finite gate

The construction above has

$$
A=m,
$$

so

$$
2\log_2A=2\log_2m
$$

while

$$
\frac{\log_2m}{m}\ll2\log_2m.
$$

It is maximally outside the positive-gap regime.

The intended strengthened statement should include

$$
\boxed{
A^2<m^{1/m}.
}
\tag{23}
$$

Call the resulting statement \((E1_{\mathrm{gap}})\). In the exact frame language, its unresolved core is:

$$
\boxed{
\begin{gathered}
\exists\,m,D,\eta,U:
\quad
\ln m>18,\quad
A^2<m^{1/m},\quad
p_1(C)\le\frac Am,\\[1mm]
m\|\mathfrak R_U(F_T)\|_2^2
\le
A\|F_T\|_2^2
\quad
\text{for every }\|T\|_2=1.
\end{gathered}
}
\tag{Gap-RQ}
$$

That statement remains **OPEN**.

The Weyl example proves that one-copy purity and even exact self-multiplicativity do not control this physical conditional Rayleigh quotient. An eventual proof in the low-\(A\) regime must exploit more than:

* the scalar one-copy value \(p_1(C)\);
* general frame positivity;
* maximum-output \(2\)-norm multiplicativity;
* the rank-one/product threshold.

---

## Audit ledger

| Status          | Claim                                                                                                      |
| --------------- | ---------------------------------------------------------------------------------------------------------- |
| **PROVED**      | The transpose and normalization in \((OB)\) are correct.                                                   |
| **PROVED**      | \((OB2)\) is exactly equivalent to the two-copy physical purity target.                                    |
| **PROVED**      | \(\kappa_1(U)\ge mp_1(C)-1\).                                                                              |
| **PROVED**      | \(P_T=d_T(1+R_U(T))/m\).                                                                                   |
| **PROVED**      | \((OL1)\Rightarrow(OB2)\).                                                                                 |
| **PROVED**      | Maximum-output \(2\)-norm multiplicativity \(\Rightarrow(OB2)\).                                           |
| **PROVED**      | \(\kappa_1\le mp_1-1\) would imply multiplicativity, but is not necessary.                                 |
| **PROVED**      | Exact physical-frame/Rayleigh formula \((RQ)\).                                                            |
| **PROVED**      | Universal sharp bound \(0\le\kappa_1(U)\le m-1\).                                                          |
| **PROVED**      | Full Weyl tuple: \(p_1=1/\sqrt m\), multiplicativity holds, but \(\kappa_1=m-1\).                          |
| **PROVED**      | The Weyl maximally entangled \(T\) violates \((OL1)\) while saturating, not violating, \((OB2)\).          |
| **PROVED**      | Literal \((E1)\), by taking \(A=m\).                                                                       |
| **CONJECTURED** | None promoted.                                                                                             |
| **OPEN**        | \((E1_{\mathrm{gap}})\), equivalently the low-\(A\) physical-cone inequality \((\mathrm{Gap\text{-}RQ})\). |

The first unresolved statement requiring independent attack is \((\mathrm{Gap\text{-}RQ})\). The first new identity an independent referee should recheck is the exact frame quotient \((FR)\); every subsequent frame bound is a direct consequence of it.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-02-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-02-local-audit.md bytes=6237 sha256=da8c11de73cab93d06a052e384c82375226dad83d08e199b3250e733530f1e35 -->

# Round 2 local audit

Date: 2026-09-12

Status: equation-level local audit completed. This is not an independent external review.

## Verdict

The response's literal verdict is correct:

    (E1) as written is PROVED.

However, this is a prompt-specification loophole, not progress that closes the intended
full-size gate. Round 2's displayed definition of (E1) omitted the positive-gap
condition inherited from Round 1. By taking eta large enough that A=m, the
one-copy and ratio bounds become vacuous. The physically relevant strengthened
statement

    ln m > 18,
    A^2 < m^(1/m),
    p_1(C) <= A/m,
    kappa_1(U) <= A-1

for one finite deterministic complex tuple remains **OPEN / CONJECTURED**.
Nothing in this response proves the full-size MOE or Holevo theorem.

## Status ledger

| Item | Local status | Meaning |
|---|---|---|
| Literal (E1) | VERIFIED | The explicit D=1, A=m witness satisfies every quantifier in the statement actually sent. |
| Relevance of literal (E1) to the main theorem | NEGATIVE | It violates the required positive-gap inequality by a maximal margin. |
| (OB) and (OB2) | VERIFIED | The transpose, block indices, and all factors of m are correct. |
| Product-input lower bound (LB) | VERIFIED | kappa_1(U) >= m p_1(C)-1 follows exactly from rank-one T. |
| Pointwise formulas (M2) and (6) | VERIFIED | They keep the actual marginal purity d_T; no illicit replacement by p_1 occurs. |
| (OL1) => (OB2) | VERIFIED | Uses d_T<=A/m. |
| Multiplicativity => (OB2) | VERIFIED | Uses p_1<=A/m. |
| Full implication/non-implication ledger | PARTIAL | The Weyl example proves multiplicativity and (OB2) do not imply (OL1). The answer only shows that (OL1) does not algebraically yield multiplicativity when p_1<A/m; it does not give a counterexample establishing the converse non-implication. |
| Frame identities (FR) and (RQ) | VERIFIED | Exact restricted Rayleigh quotient over the physical family F_T; the same tuple occurs in both left and right orbits. |
| Universal bound 0<=kappa_1<=m-1 | VERIFIED | Hilbert--Schmidt Cauchy--Schwarz on the positive equal-norm frame operators. |
| Equality condition for the universal bound | VERIFIED | Equality requires and is implied by F_(T,1)=...=F_(T,m). |
| Weyl tuple calculation | VERIFIED | p_1=1/D, self-multiplicativity holds, while kappa_1=D^2-1=m-1. |
| Weyl separation of (OL1) from (OB2) | VERIFIED | With A=D, maximally entangled T violates (OL1) but saturates (OB2). |
| Low-A gate (E1_gap) | OPEN / CONJECTURED | No tuple, obstruction, or uniform all-T estimate is supplied. |

## Direct check of the literal witness

Choose any integer m>exp(18) and

    eta = sqrt(m(m-1))/3 - 1.

Then eta>0 and

    A = 1 + 9(1+eta)^2/m = m.

For any channel with m-dimensional output, output purity is at most one, so

    p_1(C) <= 1 = A/m.

The response's frame estimate gives, for every tuple,

    kappa_1(U) <= m-1 = A-1.

For the fully explicit choice D=1 and U_1=...=U_m=1, the only input is
the scalar density operator 1, and

    C(1) = J_m/m,
    p_1(C)=1,
    R_U(T)=m-1

for every scalar Hilbert--Schmidt unit T. Thus both inequalities hold with
equality. All objects are finite and deterministic, so the quantifier order is
correct.

The same witness fails the needed gap:

    A^2 = m^2 > m^(1/m).

It therefore gives no positive regularized entropy defect.

## Check of the frame/Rayleigh reduction

With

    z_(a,v)(T)=U_a T U_v^T,
    F_(T,v)=sum_a |z_(a,v)>><<z_(a,v)|,
    F_T=sum_a |U_a T>><<U_a T|,

right multiplication R_v:Z->Z U_v^T is Hilbert--Schmidt unitary and

    F_(T,v)=R_v F_T R_v^*.

Directly,

    C(X_vw(T))_(a,b)
      = m^(-1) <z_(b,w)(T),z_(a,v)(T)>_HS,

so

    ||C(X_vw(T))||_2^2
      = m^(-2) Tr(F_(T,v) F_(T,w)).

All F_(T,v) have the same squared Hilbert--Schmidt norm
Q_T=Tr(F_T^2), and the diagonal case gives

    ||C(TT^*)||_2^2 = Q_T/m^2.

Consequently,

    1+R_U(T)
      = Tr[(sum_v F_(T,v))^2]/(m Tr(F_T^2))
      = m ||mathfrak R_U(F_T)||_2^2/||F_T||_2^2,

where

    mathfrak R_U(F)=m^(-1) sum_v R_v F R_v^*.

This is an exact reformulation, not a bound. Its domain is the nonconvex
physical family

    {F_T=sum_a |U_a T>><<U_a T| : ||T||_2=1},

not the full positive cone. That restriction is load-bearing.

For positive F_(T,v) of equal Hilbert--Schmidt norm,

    0 <= Tr(F_(T,v)F_(T,w)) <= Q_T.

Summing the m(m-1) off-diagonal pairs proves

    0 <= R_U(T) <= m-1.

This is sharp but far too weak when the positive-gap condition forces
A-1 < m^(1/(2m))-1 = O((ln m)/m).

## Check of the Weyl example

For the full D^2 Weyl tuple, m=D^2 and the associated random-unitary
channel is completely depolarizing:

    L(X)=Tr(X) I_D/D.

In the normalized Weyl operator basis, its complement is, up to transpose,

    C(rho)=D^(-1) W^* R_rho W,

where R_rho:Y->Y rho. The Hilbert--Schmidt singular values of R_rho
are the eigenvalues of rho, each repeated D times. Therefore

    ||C(rho)||_2^2 = Tr(rho^2)/D,
    p_1(C)=1/D=1/sqrt(m).

For every pure two-input state, L tensor L outputs I_(D^2)/D^2.
Complementarity therefore gives two-copy purity 1/D^2=1/m; convexity then
gives exact maximum-output 2-norm multiplicativity.

Combining this with (OB) yields

    R_U(T)=D/Tr[(TT^*)^2]-1.

The minimum possible input purity is 1/D, attained by T=I/sqrt(D), so

    kappa_1(U)=D^2-1=m-1.

With A=D (realized by the stated finite positive eta), one has
p_1=A/m; nevertheless (OL1) fails while (OB2) is saturated. This
validly separates the stronger conditional ratio gate from both
multiplicativity and the global two-copy target. It is outside the low-A
regime and does not refute (E1_gap).

## Corrected next gate

The next query must freeze the missing condition in the statement itself:

    (E1_gap)
    There exist finite m,D,eta>0 and U in U(D)^m such that
      ln m>18,
      A=1+9(1+eta)^2/m,
      A^2<m^(1/m),
      p_1(C)<=A/m,
      kappa_1(U)<=A-1.

Equivalently, after independently rechecking (FR), it asks for

    m ||mathfrak R_U(F_T)||_2^2 <= A ||F_T||_2^2

uniformly over every Hilbert--Schmidt unit T in the physical family. Literal
large-eta witnesses, full Weyl tuples, unrestricted cone norms, and ordinary
maximum-output multiplicativity do not settle this corrected statement.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-02-local-audit.md -->


# ROUND 003

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-03-prompt.md bytes=7321 sha256=ad45c3a2fc20f7503735eed296f31c1f8d2ac60ba865a3301f14b67276d1d708 -->

# Round 3 — the genuinely low-A physical-frame gate

Your Round 2 answer correctly noticed that the literal statement (E1) omitted
the positive-gap inequality. The resulting proof with A=m and D=1 is valid
for that literal statement but is irrelevant to the full-size theorem. Do not
repeat that loophole. This round builds the low-A condition into the quantified
statement itself.

No broad MOE-to-Holevo blueprint is needed. Attack only the exact finite
two-copy gate below. Give a public, self-contained derivation and no hidden
chain-of-thought.

## Frozen one-layer setup

Let m,D be finite positive integers, eta>0, and let

    U=(U_1,...,U_m) in U(D)^m

be one deterministic complex tuple. Define

    C(X)_(v,w) = m^(-1) Tr(X U_w^* U_v),
    A = 1 + 9(1+eta)^2/m,
    p = p_1(C) = sup_rho ||C(rho)||_2^2.

For every T in M_D with ||T||_2=1, set

    rho_T = TT^*,
    X_vw(T)=T(U_w^*U_v)^T T^*,
    d_T=||C(rho_T)||_2^2,

    R_U(T)=
      [sum_(v!=w) ||C(X_vw(T))||_2^2]
      / [m d_T],

    kappa_1(U)=sup_T R_U(T).

The exact statement for this round is

    (E1_gap)
    There exist finite m,D,eta>0 and one U in U(D)^m such that

      ln m > 18,
      A^2 < m^(1/m),
      p <= A/m,
      kappa_1(U) <= A-1.

All four displayed conditions are part of the same existential statement.
The tuple and D are frozen before the supremum over every physical T.

The condition A^2<m^(1/m) is equivalent to

    (log_2 m)/m > 2 log_2 A,

so any construction outside this regime is inadmissible.

## Independently checked input from Round 2

The following identities have now received an equation-level local check, but
you must independently rederive the frame identity before relying on it.

Every pure two-input vector is

    |psi_T> = sum_i |i> tensor T|i>,    ||T||_2=1,

and

    ||(C tensor C)(|psi_T><psi_T|)||_2^2
      = d_T/m + m^(-2) sum_(v!=w)||C(X_vw(T))||_2^2
      = d_T(1+R_U(T))/m.                         (OB)

Thus kappa_1<=A-1 is a sufficient condition for the global target

    sup_sigma ||(C tensor C)(sigma)||_2^2 <= A^2/m^2,

but is stronger than that target. Rank-one T gives the sharp product lower
bound

    kappa_1(U) >= m p-1.                          (LB)

For the Hilbert--Schmidt space M_D, define

    z_(a,v)(T)=U_a T U_v^T,
    F_(T,v)=sum_a |z_(a,v)(T)>><<z_(a,v)(T)|,
    F_T=sum_a |U_a T>><<U_a T|,

and let R_v be right multiplication by U_v^T. Then

    F_(T,v)=R_v F_T R_v^*.

Writing

    mathfrak R_U(F)=m^(-1) sum_v R_v F R_v^*,

Round 2 derived

    1+R_U(T)
      = Tr[(sum_v F_(T,v))^2]/[m Tr(F_T^2)]
      = m ||mathfrak R_U(F_T)||_2^2/||F_T||_2^2. (FR)

The supremum is only over the coupled physical family

    F_U={F_T=sum_a |U_aT>><<U_aT| : ||T||_2=1};

it is not over the full positive cone. The same tuple U occurs in both F_T
and mathfrak R_U.

The universal estimate 0<=kappa_1<=m-1 is valid but useless in the low-A
regime. A full Weyl tuple gives an exact separation:

    p=1/sqrt(m),
    maximum-output 2-norm multiplicativity holds,
    kappa_1=m-1.

With A=sqrt(m), it violates the ratio condition while saturating the weaker
two-copy target. This example is outside (E1_gap), so it neither proves nor
disproves the present statement.

## Structural consequences that must be exploited or audited

Let

    G_T(a,b)=<U_aT,U_bT>_HS
            =Tr(T^*U_a^*U_bT).

The nonzero spectra of G_T and F_T agree. The one-copy bound should imply,
for every Hilbert--Schmidt unit T,

    Tr F_T = m,
    Tr(F_T^2)=||G_T||_2^2=m^2 d_T <= A m,
    sum_(a!=b)|G_T(a,b)|^2 <= m(A-1).             (LF)

Check every equality and implication in (LF).

Also use the concrete column-vectorization convention

    |X>>=sum_i |i>_A tensor X|i>_B.

Derive from scratch the two partial traces of F_T and of
mathfrak R_U(F_T). Candidate identities to audit include

    Tr_A F_T = sum_a U_a rho_T U_a^*,
    Tr_B F_T = m(T^*T)^T,                          (PT)

with right multiplication acting on subsystem A. Correct the subsystem labels
or transposes if necessary. Do not invoke equality of complementary spectra
for a mixed rho_T.

The target frame inequality is

    m ||mathfrak R_U(F_T)||_2^2
      <= A ||F_T||_2^2

for every T. Equivalently,

    sum_(v!=w) Tr(F_(T,v)F_(T,w))
      <= m(A-1) Tr(F_T^2).                         (LowA-FR)

The left-frame flatness (LF) and the right-orbit overlap in (LowA-FR) use the
same tuple in different orientations. Determine rigorously whether (LF),
the partial-trace constraints, and the coupled form of F_T are sufficient,
insufficient by an explicit physical counterexample, or leave one exact
uncontrolled correlation.

## Exact task

1. Give one verdict on (E1_gap): PROVED, DISPROVED, or OPEN WITH EARLIEST
   GAP. A conditional reduction is not a proof.
2. Independently rederive (FR), (LF), and (PT), checking all adjoints,
   transposes, subsystem labels, normalizations, and quantifiers.
3. State the exact implication/non-implication diagram among:

      kappa_1<=A-1,
      maximum-output 2-norm multiplicativity of C tensor C,
      the global A^2/m^2 two-copy target.

   Round 2 proved that multiplicativity and the global target do not imply the
   ratio condition. If claiming the converse non-implication, give an actual
   channel in this class rather than merely observing that one upper-bound
   calculation is insufficient.
4. Try to settle (E1_gap) analytically. An admissible proof must supply one
   finite tuple and control the supremum over all T. An admissible disproof
   must construct, for every tuple satisfying the low-A one-copy bound, a
   physical T with R_U(T)>A-1.
5. If the statement remains open, isolate the first scalar or operator
   inequality not controlled by (LF) and (PT). Then prove one new,
   strictly narrower lemma that materially advances the low-A gate. Acceptable
   examples are:

   - a sharp uniform estimate for a nontrivial Schmidt-rank range with all
     constants explicit;
   - a valid reduction of the supremum to a smaller, explicitly characterized
     family of T;
   - a quantified lower-bound obstruction on kappa_1 stronger than (LB) under
     the low-A assumptions;
   - a theorem showing that (LF) plus an explicit additional same-tuple
     correlation condition is equivalent to (LowA-FR).

   The universal m-1 bound, rank-one inputs, a single maximally entangled
   input, diagonal/simple-tensor/rook/spectral-flat coefficient subclasses,
   or a restatement of (FR) do not count as new progress.
6. If using probability, state one finite-D event that is already uniform over
   all T, with its probability, Lipschitz constant, net size, and every
   dependence on m and D. Separate fixed-T events are insufficient.
7. Do not use independent Haar tuples on the two tensor legs, unrestricted cb
   or 2->2 bounds, fresh randomness per copy, a full Weyl tuple outside the
   low-A regime, numerical evidence, WHGAP, or any orientation-insensitive
   inequality that would also suppress C tensor bar(C).
8. End with an audit ledger separating PROVED, DISPROVED, OPEN, and
   CONJECTURED. Identify the first new statement requiring independent
   verification.

No claim about the full-size theorem may be promoted unless (E1_gap) itself is
closed and the earlier all-copy gate is separately handled. This round is only
the finite r=2 low-A gate.

<!-- END HISTORICAL FILE path=work/round-03-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-03-response.md bytes=20442 sha256=d6fe353d6833913f634552bd66b2c75d6d3fde83d8fb38f871307c93c702e468 -->

# Verdict: **OPEN WITH EARLIEST GAP**

The low-\(A\) existential statement

$$
(E1_{\rm gap})
$$

is neither proved nor disproved by the available identities.

The earliest unresolved pointwise quantity is the **double-centered same-tuple correlation**

$$
\Gamma_U(T):=
\left\|
\bigl(Q\otimes Q\bigr)
\bigl(|\psi_T\rangle\langle\psi_T|\bigr)
\right\|_2^2,
\qquad
Q:=L-\Delta_D,
$$

where

$$
L(X)=\frac1m\sum_{a=1}^m U_aXU_a^*,
\qquad
\Delta_D(X)=\operatorname{Tr}(X)\frac{I_D}{D}.
$$

The one-copy frame flatness and the exact partial traces determine all scalar, one-sided, and marginal contributions to the target, but do not bound \(\Gamma_U(T)\) uniformly over all physical \(T\).

A new deterministic obstruction is proved below: averaging over **full-Schmidt-rank** inputs gives

$$
\boxed{
\kappa_1(U)\ge
\frac{m\bigl(\alpha_U^2+D^2\bigr)}
     {D^2(\alpha_U+1)}-1,
\qquad
\alpha_U:=\|C(I_D)\|_2^2.
}
\tag{Haar-LB}
$$

Consequently, any solution of \((E1_{\rm gap})\) must obey a new quadratic constraint on \(\alpha_U\), strictly stronger than the one-copy constraint at the maximally mixed input.

No randomness in \(U\) is used in this result.

---

# 1. Vectorization conventions and the frame identity

Use

$$
|X\rangle\rangle
=
\sum_{i=1}^D |i\rangle_A\otimes X|i\rangle_B.
$$

For \(M,N,X\in M_D\),

$$
(M\otimes N)|X\rangle\rangle
=
|N X M^{\mathsf T}\rangle\rangle.
\tag{1.1}
$$

Indeed,

$$
\begin{aligned}
(M\otimes N)|X\rangle\rangle
&=
\sum_{i,j}M_{ji}|j\rangle\otimes NX|i\rangle\\
&=
\sum_j|j\rangle\otimes NXM^{\mathsf T}|j\rangle.
\end{aligned}
$$

The Hilbert–Schmidt inner product agrees with vector inner product:

$$
\langle\langle X|Y\rangle\rangle=\operatorname{Tr}(X^*Y).
\tag{1.2}
$$

For a rank-one operator on \(A\otimes B\),

$$
\boxed{
\operatorname{Tr}_A|X\rangle\rangle\langle\langle X|
=
XX^*,
}
\tag{1.3}
$$

and

$$
\boxed{
\operatorname{Tr}_B|X\rangle\rangle\langle\langle X|
=
(X^*X)^{\mathsf T}.
}
\tag{1.4}
$$

Let

$$
z_{a,v}(T)=U_aTU_v^{\mathsf T},
\qquad
F_{T,v}
=
\sum_{a=1}^m
|z_{a,v}(T)\rangle\rangle
\langle\langle z_{a,v}(T)|,
$$

and

$$
F_T
=
\sum_{a=1}^m
|U_aT\rangle\rangle
\langle\langle U_aT|.
$$

Right multiplication by \(U_v^{\mathsf T}\) acts as \(U_v\) on subsystem \(A\). Thus, with

$$
\mathsf R_v=U_v\otimes I_D,
$$

one has

$$
\boxed{
F_{T,v}=\mathsf R_vF_T\mathsf R_v^*.
}
\tag{1.5}
$$

Define

$$
\mathfrak R_U(F)
=
\frac1m\sum_{v=1}^m
\mathsf R_vF\mathsf R_v^*.
\tag{1.6}
$$

Then

$$
\sum_vF_{T,v}=m\,\mathfrak R_U(F_T).
\tag{1.7}
$$

## 1.1 Frame overlaps and \(C(X_{vw})\)

Set

$$
A_{vw}=U_w^*U_v.
$$

Since

$$
A_{vw}^{\mathsf T}
=
U_v^{\mathsf T}\overline{U_w},
$$

we have

$$
X_{vw}(T)
=
TU_v^{\mathsf T}\overline{U_w}T^*.
$$

Now

$$
\begin{aligned}
\langle\langle z_{b,w}(T)|z_{a,v}(T)\rangle\rangle
&=
\operatorname{Tr}
\left[
(U_bTU_w^{\mathsf T})^*
(U_aTU_v^{\mathsf T})
\right]\\
&=
\operatorname{Tr}
\left[
\overline{U_w}T^*U_b^*U_aTU_v^{\mathsf T}
\right]\\
&=
\operatorname{Tr}
\left[
TU_v^{\mathsf T}\overline{U_w}T^*
U_b^*U_a
\right]\\
&=
\operatorname{Tr}
\left[
X_{vw}(T)U_b^*U_a
\right]\\
&=
m\,C(X_{vw}(T))_{a,b}.
\end{aligned}
\tag{1.8}
$$

Therefore

$$
\begin{aligned}
\operatorname{Tr}(F_{T,v}F_{T,w})
&=
\sum_{a,b}
\left|
\langle\langle z_{b,w}|z_{a,v}\rangle\rangle
\right|^2\\
&=
m^2\|C(X_{vw}(T))\|_2^2.
\end{aligned}
\tag{1.9}
$$

When \(v=w\),

$$
X_{vv}(T)=TT^*=\rho_T.
$$

All \(F_{T,v}\) are unitarily conjugate, so

$$
\boxed{
\operatorname{Tr}(F_T^2)=m^2d_T.
}
\tag{1.10}
$$

Summing (1.9) over all \(v,w\),

$$
\begin{aligned}
1+R_U(T)
&=
\frac{
\sum_{v,w}\|C(X_{vw}(T))\|_2^2
}{
m d_T
}\\
&=
\frac{
m^{-2}\operatorname{Tr}
\left[
\left(\sum_vF_{T,v}\right)^2
\right]
}{
m^{-1}\operatorname{Tr}(F_T^2)
}.
\end{aligned}
$$

Hence

$$
\boxed{
1+R_U(T)
=
\frac{
\operatorname{Tr}\left[
\left(\sum_vF_{T,v}\right)^2
\right]
}{
m\,\operatorname{Tr}(F_T^2)
}
=
m\,
\frac{\|\mathfrak R_U(F_T)\|_2^2}
     {\|F_T\|_2^2}.
}
\tag{FR}
$$

All transposes and normalizations in the proposed identity are correct.

---

# 2. Verification of the left-frame flatness

Define the synthesis map

$$
Z_T:\mathbb C^m\longrightarrow M_D,
\qquad
Z_Te_a=|U_aT\rangle\rangle.
$$

Then

$$
F_T=Z_TZ_T^*,
$$

while

$$
G_T=Z_T^*Z_T
$$

has entries

$$
G_T(a,b)
=
\langle U_aT,U_bT\rangle_{\rm HS}
=
\operatorname{Tr}(T^*U_a^*U_bT).
$$

Thus \(F_T\) and \(G_T\) have identical nonzero eigenvalues. In particular,

$$
\operatorname{Tr}(F_T^2)
=
\operatorname{Tr}(G_T^2)
=
\|G_T\|_2^2.
\tag{2.1}
$$

Every diagonal entry is

$$
G_T(a,a)=\operatorname{Tr}(T^*T)=1.
$$

Also,

$$
\operatorname{Tr}F_T
=
\sum_a\|U_aT\|_2^2
=
m.
\tag{2.2}
$$

Since

$$
\begin{aligned}
C(\rho_T)_{v,w}
&=
\frac1m
\operatorname{Tr}(TT^*U_w^*U_v)\\
&=
\frac1m
\operatorname{Tr}(T^*U_w^*U_vT)\\
&=
\frac1mG_T(w,v),
\end{aligned}
$$

we have

$$
C(\rho_T)=\frac1mG_T^{\mathsf T}.
$$

Therefore

$$
\boxed{
\operatorname{Tr}(F_T^2)
=
\|G_T\|_2^2
=
m^2d_T.
}
\tag{2.3}
$$

The one-copy assumption gives

$$
d_T\le p\le\frac Am,
$$

so

$$
\boxed{
\operatorname{Tr}(F_T^2)\le Am.
}
\tag{2.4}
$$

Removing the \(m\) diagonal terms of the Gram matrix yields

$$
\boxed{
\sum_{a\ne b}|G_T(a,b)|^2
=
\operatorname{Tr}(F_T^2)-m
\le m(A-1).
}
\tag{LF}
$$

Thus every equality and implication in \((LF)\) is correct.

---

# 3. Partial traces

From (1.3),

$$
\begin{aligned}
\operatorname{Tr}_A F_T
&=
\sum_a
(U_aT)(U_aT)^*\\
&=
\sum_aU_aTT^*U_a^*.
\end{aligned}
$$

Hence

$$
\boxed{
\operatorname{Tr}_A F_T
=
\sum_aU_a\rho_TU_a^*
=
mL(\rho_T).
}
\tag{3.1}
$$

From (1.4),

$$
\begin{aligned}
\operatorname{Tr}_B F_T
&=
\sum_a
\left[
(U_aT)^*(U_aT)
\right]^{\mathsf T}\\
&=
\sum_a(T^*T)^{\mathsf T}.
\end{aligned}
$$

Therefore

$$
\boxed{
\operatorname{Tr}_B F_T
=
m(T^*T)^{\mathsf T}.
}
\tag{3.2}
$$

Define

$$
\sigma_T:=(T^*T)^{\mathsf T}.
$$

Both \(\rho_T\) and \(\sigma_T\) are density matrices and have the same eigenvalues, but no complementary-spectrum assertion for a mixed \(\rho_T\) is being used.

Because \(\mathsf R_v=U_v\otimes I\) acts on subsystem \(A\),

$$
\operatorname{Tr}_A\mathfrak R_U(F_T)
=
\operatorname{Tr}_A F_T
=
mL(\rho_T),
\tag{3.3}
$$

whereas

$$
\begin{aligned}
\operatorname{Tr}_B\mathfrak R_U(F_T)
&=
\frac1m\sum_v
U_v
\left[m\sigma_T\right]
U_v^*\\
&=
mL(\sigma_T).
\end{aligned}
\tag{3.4}
$$

Thus the fully corrected partial-trace identities are

$$
\boxed{
\begin{aligned}
\operatorname{Tr}_A F_T&=mL(\rho_T),&
\operatorname{Tr}_B F_T&=m\sigma_T,\\
\operatorname{Tr}_A\mathfrak R_U(F_T)&=mL(\rho_T),&
\operatorname{Tr}_B\mathfrak R_U(F_T)&=mL(\sigma_T).
\end{aligned}
}
\tag{PT}
$$

The subsystem assignment in the prompt is correct: right multiplication by \(U_v^{\mathsf T}\) acts on \(A\).

---

# 4. Exact implication diagram

Let

$$
P_T
=
\left\|
(C\otimes C)
(|\psi_T\rangle\langle\psi_T|)
\right\|_2^2.
$$

The audited identity is

$$
\boxed{
P_T=\frac{d_T}{m}\bigl(1+R_U(T)\bigr).
}
\tag{4.1}
$$

Let

$$
p_2(C):=\sup_TP_T.
$$

Product inputs give

$$
p_2(C)\ge p^2.
\tag{4.2}
$$

Define:

$$
K:\quad \kappa_1(U)\le A-1,
$$

$$
M:\quad p_2(C)=p^2,
$$

$$
G:\quad p_2(C)\le\frac{A^2}{m^2}.
$$

## 4.1 Proven arrows

Under \(K\),

$$
P_T
\le
\frac{A}{m}d_T
\le
\frac{A}{m}p.
$$

Hence

$$
\boxed{
K\Longrightarrow
p_2(C)\le\frac{Ap}{m}
\le\frac{A^2}{m^2}.
}
\tag{4.3}
$$

Therefore

$$
\boxed{K\Longrightarrow G.}
$$

Under \(M\),

$$
p_2(C)=p^2\le\frac{A^2}{m^2},
$$

so

$$
\boxed{M\Longrightarrow G.}
$$

If the one-copy estimate is saturated,

$$
p=\frac Am,
$$

then (4.3) becomes

$$
p_2(C)\le p^2.
$$

Together with (4.2),

$$
\boxed{
p=\frac Am
\quad\Longrightarrow\quad
K\Longrightarrow M.
}
\tag{4.4}
$$

Likewise, if \(p=A/m\), then \(G\) implies

$$
p_2(C)\le\frac{A^2}{m^2}=p^2,
$$

and hence

$$
\boxed{
p=\frac Am
\quad\Longrightarrow\quad
G\Longleftrightarrow M.
}
\tag{4.5}
$$

## 4.2 Reverse arrows

The independently checked full-Weyl example from Round 2 establishes, within this channel class,

$$
\boxed{M\nRightarrow K}
$$

and

$$
\boxed{G\nRightarrow K.}
$$

That example is not used anywhere in the present low-\(A\) analysis.

For \(p<A/m\), the estimate supplied by \(K\),

$$
p_2(C)\le\frac{Ap}{m},
$$

is strictly weaker than \(p_2(C)\le p^2\). This calculation alone is not a counterexample. Therefore:

$$
\boxed{
K\Longrightarrow M
\text{ for }p<A/m
\text{ is not established here,}
}
$$

and no converse non-implication is claimed.

Similarly, no actual channel is supplied here proving \(G\nRightarrow M\) in the strict-slack case \(p<A/m\).

The rigorous diagram is therefore

$$
\begin{array}{ccccc}
K&\longrightarrow&G&\longleftarrow&M,\\[1mm]
&&\nwarrow&&
\end{array}
$$

with \(M\nRightarrow K\) and \(G\nRightarrow K\), while \(K\to M\) is valid under the additional equality \(p=A/m\) and otherwise remains undecided.

---

# 5. Exact isolation of the uncontrolled same-tuple correlation

Let

$$
|\psi_T\rangle
=
\sum_i|i\rangle\otimes T|i\rangle,
\qquad
\Psi_T=|\psi_T\rangle\langle\psi_T|.
$$

From (1.1),

$$
F_T
=
\sum_a
(I\otimes U_a)\Psi_T(I\otimes U_a^*)
=
m(\operatorname{id}\otimes L)(\Psi_T).
\tag{5.1}
$$

Since \(\mathfrak R_U\) applies \(L\) on subsystem \(A\),

$$
\boxed{
\mathfrak R_U(F_T)
=
m(L\otimes L)(\Psi_T).
}
\tag{5.2}
$$

Consequently,

$$
d_T
=
\frac{\|F_T\|_2^2}{m^2}
=
\|(\operatorname{id}\otimes L)(\Psi_T)\|_2^2,
\tag{5.3}
$$

and \((FR)\) becomes

$$
\boxed{
1+R_U(T)
=
m\,
\frac{\|(L\otimes L)(\Psi_T)\|_2^2}
     {\|(\operatorname{id}\otimes L)(\Psi_T)\|_2^2}.
}
\tag{5.4}
$$

Thus the ratio condition is exactly

$$
\boxed{
m\|(L\otimes L)(\Psi_T)\|_2^2
\le
A\,d_T
\qquad
\text{for every }T.
}
\tag{5.5}
$$

## 5.1 Centered orthogonal decomposition

Write

$$
L=\Delta_D+Q,
\qquad
\Delta_D(X)=\operatorname{Tr}(X)\frac{I_D}{D}.
$$

Then

$$
Q(I_D)=0,
\qquad
\operatorname{Tr}Q(X)=0.
$$

The two marginals of \(\Psi_T\) are

$$
\operatorname{Tr}_B\Psi_T=\sigma_T,
\qquad
\operatorname{Tr}_A\Psi_T=\rho_T.
$$

First,

$$
(\operatorname{id}\otimes L)(\Psi_T)
=
\sigma_T\otimes\frac{I_D}{D}
+
(\operatorname{id}\otimes Q)(\Psi_T).
$$

The two terms are Hilbert–Schmidt orthogonal, because the second has zero partial trace over \(B\). Hence

$$
\boxed{
d_T
=
\frac{\operatorname{Tr}(\sigma_T^2)}{D}
+
\left\|
(\operatorname{id}\otimes Q)(\Psi_T)
\right\|_2^2.
}
\tag{5.6}
$$

For the two-sided output,

$$
\begin{aligned}
(L\otimes L)(\Psi_T)
={}&
\frac{I_D\otimes I_D}{D^2}\\
&+
Q(\sigma_T)\otimes\frac{I_D}{D}\\
&+
\frac{I_D}{D}\otimes Q(\rho_T)\\
&+
(Q\otimes Q)(\Psi_T).
\end{aligned}
\tag{5.7}
$$

All four terms are pairwise Hilbert–Schmidt orthogonal. Therefore

$$
\boxed{
\begin{aligned}
\|(L\otimes L)(\Psi_T)\|_2^2
={}&
\frac1{D^2}
+
\frac{\|Q(\sigma_T)\|_2^2}{D}\\
&+
\frac{\|Q(\rho_T)\|_2^2}{D}
+
\Gamma_U(T),
\end{aligned}
}
\tag{5.8}
$$

where

$$
\boxed{
\Gamma_U(T)
=
\|(Q\otimes Q)(\Psi_T)\|_2^2.
}
\tag{5.9}
$$

Substitution into (5.5) gives the exact condition

$$
\boxed{
\begin{aligned}
m\Gamma_U(T)
\le{}&
A d_T-\frac{m}{D^2}\\
&-\frac{m}{D}
\left(
\|Q(\sigma_T)\|_2^2+
\|Q(\rho_T)\|_2^2
\right)
\end{aligned}
}
\tag{DC}
$$

for every Hilbert–Schmidt unit \(T\).

This is the first exact uncontrolled inequality.

The data \((LF)\) determine \(d_T\) and bound it by \(A/m\). The partial traces determine \(L(\rho_T)\) and \(L(\sigma_T)\), hence also \(Q(\rho_T)\) and \(Q(\sigma_T)\). They do not provide a pointwise upper bound for the double-centered term \(\Gamma_U(T)\).

The coupled physical form of \(F_T\) may impose such a bound, but proving or refuting precisely that implication is the remaining finite gate.

---

# 6. New full-Schmidt-rank obstruction

The following lemma goes beyond rank-one inputs, a single Bell input, and the universal \(m-1\) estimate.

## Lemma 6.1

For every finite deterministic tuple \(U\), define

$$
\alpha_U
=
\|C(I_D)\|_2^2
=
\frac1{m^2}
\sum_{v,w}
\left|
\operatorname{Tr}(U_w^*U_v)
\right|^2.
\tag{6.1}
$$

Then there exists a full-rank \(T\in M_D\), \(\|T\|_2=1\), such that

$$
R_U(T)
\ge
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}
-1.
$$

Consequently,

$$
\boxed{
\kappa_1(U)
\ge
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}
-1.
}
\tag{6.2}
$$

### Proof

Let \(|\psi_T\rangle\) be Haar-uniform on the unit sphere of
\(\mathbb C^D\otimes\mathbb C^D\). Under vectorization this is Haar-uniform \(T\) on the Hilbert–Schmidt unit sphere. Such a \(T\) has rank \(D\) almost surely.

For an \(n\)-dimensional Haar-random pure state \(\Psi\),

$$
\mathbb E[\Psi^{\otimes2}]
=
\frac{I+F}{n(n+1)},
\tag{6.3}
$$

where \(F\) is the swap. This follows from unitary invariance: the expectation lies in the span of \(I,F\), and its trace and swap trace are both one.

For a completely positive map \(\Phi:M_n\to M_k\), the swap identity gives

$$
\boxed{
\mathbb E_\Psi
\operatorname{Tr}[\Phi(\Psi)^2]
=
\frac{
\operatorname{Tr}[\Phi(I_n)^2]
+
\|J_\Phi\|_2^2
}{
n(n+1)
}.
}
\tag{6.4}
$$

Indeed,

$$
\operatorname{Tr}[X^2]
=
\operatorname{Tr}[(X\otimes X)F_k],
$$

the \(I\)-term in (6.3) gives \(\operatorname{Tr}\Phi(I)^2\), and the \(F_n\)-term gives

$$
\sum_{i,j}
\operatorname{Tr}
\left[
\Phi(E_{ij})\Phi(E_{ji})
\right]
=
\|J_\Phi\|_2^2.
$$

For the present \(C\),

$$
\begin{aligned}
\|J_C\|_2^2
&=
\sum_{i,j}\|C(E_{ij})\|_2^2\\
&=
\frac1{m^2}
\sum_{v,w}\sum_{i,j}
\left|
(U_w^*U_v)_{j,i}
\right|^2\\
&=
\frac1{m^2}\sum_{v,w}D\\
&=
D.
\end{aligned}
\tag{6.5}
$$

Let

$$
P_T
=
\|(C\otimes C)(\Psi_T)\|_2^2.
$$

Applying (6.4) to \(\Phi=C\otimes C\), whose input dimension is \(D^2\), gives

$$
\boxed{
\mathbb E P_T
=
\frac{\alpha_U^2+D^2}
     {D^2(D^2+1)}.
}
\tag{6.6}
$$

Here

$$
\|(C\otimes C)(I_{D^2})\|_2^2
=
\alpha_U^2,
$$

and

$$
\|J_{C\otimes C}\|_2^2
=
\|J_C\|_2^4
=
D^2.
$$

Now let

$$
\rho_T=\operatorname{Tr}_A\Psi_T.
$$

Tracing (6.3) over the two \(A\)-systems gives

$$
\mathbb E[\rho_T^{\otimes2}]
=
\frac{D I+F}{D(D^2+1)}.
\tag{6.7}
$$

Therefore

$$
\begin{aligned}
\mathbb E d_T
&=
\mathbb E\operatorname{Tr}[C(\rho_T)^2]\\
&=
\frac{D\alpha_U+\|J_C\|_2^2}
       {D(D^2+1)}\\
&=
\boxed{
\frac{\alpha_U+1}{D^2+1}.
}
\end{aligned}
\tag{6.8}
$$

Let

$$
N_T=
\sum_{v\ne w}
\|C(X_{vw}(T))\|_2^2.
$$

From \((OB)\),

$$
N_T=m^2P_T-md_T.
$$

Hence

$$
\begin{aligned}
\frac{\mathbb E N_T}
     {\mathbb E[m d_T]}
&=
m\frac{\mathbb E P_T}{\mathbb E d_T}-1\\
&=
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}
-1.
\end{aligned}
\tag{6.9}
$$

Because \(m d_T>0\),

$$
N_T\le \kappa_1(U)\,m d_T
$$

pointwise. Taking expectations proves (6.2).

Moreover, the rank-deficient matrices form a Haar-null algebraic set. Thus the weighted average in (6.9) is attained or exceeded by at least one full-rank \(T\). ∎

This is not a probabilistic construction of \(U\). Haar averaging is only an exact device for selecting a deterministic entangled input for each already frozen tuple.

---

# 7. Consequences for any putative low-\(A\) solution

Since

$$
\frac{C(I_D)}{D}
=
C\left(\frac{I_D}{D}\right)
$$

is a density matrix on \(\mathbb C^m\),

$$
\frac{\alpha_U}{D^2}
=
\left\|
C\left(\frac{I_D}{D}\right)
\right\|_2^2
\ge\frac1m.
$$

The one-copy hypothesis gives the upper bound

$$
\frac{\alpha_U}{D^2}\le\frac Am.
$$

Thus

$$
\boxed{
\frac{D^2}{m}
\le
\alpha_U
\le
\frac{AD^2}{m}.
}
\tag{7.1}
$$

If \(\kappa_1(U)\le A-1\), Lemma 6.1 requires

$$
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}
\le A.
$$

Equivalently,

$$
\boxed{
m\alpha_U^2
-
AD^2\alpha_U
+
D^2(m-A)
\le0.
}
\tag{HC}
$$

This is a new necessary scalar condition.

## 7.1 Strict maximally mixed slack

At the one-copy upper endpoint

$$
\alpha_U=\frac{AD^2}{m},
$$

the left side of \((HC)\) equals

$$
D^2(m-A)>0.
$$

Here \(m>A\) follows from the low-\(A\) condition and \(m>1\). Therefore:

$$
\boxed{
\left\|
C\left(\frac{I_D}{D}\right)
\right\|_2^2
=
\frac Am
\quad\Longrightarrow\quad
\kappa_1(U)>A-1.
}
\tag{7.2}
$$

So a solution of \((E1_{\rm gap})\) cannot merely satisfy the one-copy inequality at the maximally mixed input with equality. It requires a quantitatively strict slack.

The roots of the quadratic in \((HC)\) are

$$
\boxed{
\alpha_\pm
=
\frac{
AD^2
\pm
D\sqrt{A^2D^2-4m(m-A)}
}{
2m}.
}
\tag{7.3}
$$

Thus a necessary condition is

$$
A^2D^2\ge4m(m-A),
\tag{7.4}
$$

and

$$
\boxed{
\alpha_-\le\alpha_U\le\alpha_+.
}
\tag{7.5}
$$

Moreover,

$$
\alpha_+
<
\frac{AD^2}{m},
$$

with exact gap

$$
\boxed{
\frac{AD^2}{m}-\alpha_+
=
\frac{
2D(m-A)
}{
AD+\sqrt{A^2D^2-4m(m-A)}
}.
}
\tag{7.6}
$$

This obstruction is genuinely entangled: its witness can be chosen full Schmidt rank. It is not a reformulation of the product lower bound

$$
\kappa_1(U)\ge mp-1.
$$

The obstruction still does not disprove \((E1_{\rm gap})\). For sufficiently large finite \(D\), the scalar interval (7.1) can intersect the quadratic interval (7.5). The remaining pointwise double-centered condition \((DC)\) is not settled by this average argument.

---

# 8. Why the proof stops

A proof of \((E1_{\rm gap})\) would require one finite tuple for which

$$
\Gamma_U(T)
\le
\frac{A}{m}d_T
-
\frac1{D^2}
-
\frac{
\|Q(\sigma_T)\|_2^2+
\|Q(\rho_T)\|_2^2
}{D}
\tag{8.1}
$$

holds for every Hilbert–Schmidt unit \(T\).

A disproof would require showing that every tuple satisfying

$$
p\le\frac Am
$$

and the low-\(A\) scalar constraints admits some physical \(T\) violating (8.1).

Neither conclusion follows from:

$$
\operatorname{Tr}(F_T^2)\le Am,
$$

the two partial traces,

$$
\operatorname{Tr}_A\mathfrak R_U(F_T)=mL(\rho_T),
\qquad
\operatorname{Tr}_B\mathfrak R_U(F_T)=mL(\sigma_T),
$$

or the new averaged obstruction \((HC)\).

The exact remaining correlation is the double-traceless component

$$
(Q\otimes Q)(\Psi_T),
$$

where both copies of \(Q\) are formed from the same frozen tuple \(U\).

---

# Audit ledger

| Status                                                        | Statement                                                                                           |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **PROVED**                                                    | The frame identity \((FR)\), including all transposes and normalizations.                           |
| **PROVED**                                                    | \(\operatorname{Tr}F_T=m\), \(\operatorname{Tr}F_T^2=m^2d_T\), and the off-diagonal bound \((LF)\). |
| **PROVED**                                                    | The partial traces \((PT)\), with right multiplication acting on subsystem \(A\).                   |
| **PROVED**                                                    | \(K\Rightarrow G\) and \(M\Rightarrow G\).                                                          |
| **PROVED**                                                    | If \(p=A/m\), then \(K\Rightarrow M\) and \(G\Leftrightarrow M\).                                   |
| **DISPROVED, from the independently checked Round 2 example** | \(M\Rightarrow K\) and \(G\Rightarrow K\).                                                          |
| **PROVED**                                                    | Exact centered reduction \((DC)\); all uncontrolled dependence is isolated in \(\Gamma_U(T)\).      |
| **PROVED**                                                    | Full-Schmidt-rank averaged lower bound \((\mathrm{Haar\text{-}LB})\).                               |
| **PROVED**                                                    | Necessary quadratic constraint \((HC)\) and strict maximally mixed slack (7.2)–(7.6).               |
| **OPEN**                                                      | The existential statement \((E1_{\rm gap})\).                                                       |
| **OPEN**                                                      | Uniform pointwise control of \(\Gamma_U(T)\) over every physical \(T\).                             |
| **OPEN**                                                      | Whether \(K\Rightarrow M\) when \(p<A/m\) in this channel class.                                    |
| **CONJECTURED**                                               | None promoted.                                                                                      |

The first new proved statement requiring independent verification is the full-rank bound

$$
\kappa_1(U)\ge
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}-1.
$$

The first unresolved statement is the uniform double-centered inequality \((8.1)\).

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-03-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-03-local-audit.md bytes=8397 sha256=3a3141a0769b490b3430c4a7f776781277b091d3fa87a41d30d6982bc3593894 -->

# Round 3 local audit

Date: 2026-09-12

Status: equation-level local audit completed. This is not an independent external review.

## Verdict

The response's headline verdict is justified:

    (E1_gap) remains OPEN WITH EARLIEST GAP.

It supplies neither one admissible low-A tuple with a uniform all-T bound nor a
universal violating T for every candidate tuple. Nothing here proves the full-size
MOE or Holevo theorem, and the earlier all-copy gate remains separate even if the
finite r=2 gate is eventually closed.

The headline new formula is a deterministic lower bound obtained by Haar-averaging
the physical input T for a tuple U that has already been frozen:

    kappa_1(U) >= m(alpha_U^2 + D^2) / [D^2(alpha_U + 1)] - 1,
    alpha_U = ||C(I_D)||_2^2.

The derivation and constants check out. However, a further adversarial comparison
shows that its scalar consequence is redundant in the low-A feasible regime: the
ordinary Haar average over rank-one inputs, combined with `p<=A/m`, is already
strictly stronger. The full-rank witness statement is valid, but it does not supply
the genuinely new gate progress claimed by the response.

## Status ledger

| Item | Local status | Meaning |
|---|---|---|
| Browser response capture | VERIFIED | The saved Markdown is byte-for-byte identical to ChatGPT's `Copy response` payload. |
| Verdict on (E1_gap) | VERIFIED | No construction or universal obstruction closes the existential statement. |
| Frame identity (FR) | VERIFIED | Vectorization, right-action subsystem, adjoints, transposes, and every factor of m are correct. |
| Left-frame flatness (LF) | VERIFIED | `Tr F_T=m`, `Tr(F_T^2)=||G_T||_2^2=m^2 d_T<=Am`, and the off-diagonal Gram bound follow exactly. |
| Partial traces (PT) | VERIFIED | The four displayed partial traces of `F_T` and `mathfrak R_U(F_T)` are correct for the stated column-vectorization convention. |
| Implication diagram | VERIFIED WITH SCOPE NOTE | `K=>G` and `M=>G`; at `p=A/m`, `K=>M` and `G<=>M`; Weyl gives `M !=> K` and `G !=> K` in the broader channel class. The strict-slack reverse relations remain undecided. |
| Centered decomposition (DC) | VERIFIED | The scalar, one-sided, and double-centered terms are Hilbert--Schmidt orthogonal and the displayed inequality is algebraically equivalent to the ratio target. |
| Haar second-moment identity | VERIFIED | The formula follows from `E[Psi^tensor2]=(I+F)/(n(n+1))` and the swap trick under the stated Choi convention. |
| `||J_C||_2^2=D` | VERIFIED | Summing the Frobenius norms of the `m^2` unitary products gives exactly D after the `m^-2` normalization. |
| Full-rank lower bound (Haar-LB) | VERIFIED BUT DOMINATED | The expectations, weighted-ratio argument, and full-rank selection step are correct; in the low-A feasible regime its scalar value is no larger than the existing rank-one Haar-average lower bound. |
| Quadratic constraint (HC) | ALGEBRAICALLY VERIFIED, REDUNDANT | Rearrangement, discriminant, roots, and endpoint exclusion are correct, but the full one-copy supremum assumption already gives a stronger upper bound on `alpha_U`. |
| Claim that Gamma is the first uncontrolled term | VERIFIED AS A ROUTE-RELATIVE STATEMENT | The decomposition isolates the exact term not bounded by the supplied LF/PT estimates. The answer does not prove a universal logical non-implication of all conceivable consequences of LF/PT, so this should not be read more broadly. |
| Full-size theorem | OPEN / CONJECTURED | Round 3 addresses only the finite r=2 low-A gate; uniform all-copy control remains absent. |

## Check of the frame and partial-trace formulas

For

    |X>> = sum_i |i>_A tensor X|i>_B,

one has

    (M tensor N)|X>> = |N X M^T>>,
    Tr_A |X>><<X| = XX^*,
    Tr_B |X>><<X| = (X^*X)^T.

Therefore right multiplication `X -> X U_v^T` is represented by `U_v tensor I`
and acts on subsystem A. With

    z_(a,v)=U_a T U_v^T,
    F_(T,v)=sum_a |z_(a,v)>><<z_(a,v)|,

direct expansion gives

    <z_(b,w),z_(a,v)>_HS
      = Tr[T(U_w^*U_v)^T T^* U_b^*U_a]
      = m C(X_vw)_(a,b).

Hence

    Tr(F_(T,v)F_(T,w)) = m^2 ||C(X_vw)||_2^2.

The diagonal case gives `Tr(F_T^2)=m^2 d_T`; summing all pairs and dividing by
the actual denominator `m d_T` proves (FR). No marginal purity was silently
replaced by the maximum p.

The partial traces then follow termwise:

    Tr_A F_T = sum_a U_a rho_T U_a^* = m L(rho_T),
    Tr_B F_T = m sigma_T,
    sigma_T=(T^*T)^T.

Averaging the A-side conjugations leaves the A partial trace invariant and sends
the B partial trace to its random-unitary average, giving

    Tr_A mathfrak R_U(F_T)=mL(rho_T),
    Tr_B mathfrak R_U(F_T)=mL(sigma_T).

## Check of the centered reduction

With `L=Delta_D+Q`, both `Q(I_D)=0` and `Tr Q(X)=0`. The decompositions

    (id tensor L)(Psi_T)
      = sigma_T tensor I_D/D + (id tensor Q)(Psi_T)

and

    (L tensor L)(Psi_T)
      = I tensor I/D^2
        + Q(sigma_T) tensor I/D
        + I/D tensor Q(rho_T)
        + (Q tensor Q)(Psi_T)

are pairwise Hilbert--Schmidt orthogonal in their displayed summands. Since

    F_T=m(id tensor L)(Psi_T),
    mathfrak R_U(F_T)=m(L tensor L)(Psi_T),

the ratio target is exactly (DC). The remaining quantity under this route is

    Gamma_U(T)=||(Q tensor Q)(Psi_T)||_2^2.

## Check of the new full-rank bound

For a Haar-random pure input on dimension `n`,

    E Tr[Phi(Psi)^2]
      = [Tr(Phi(I_n)^2)+||J_Phi||_2^2]/[n(n+1)].

For the present channel,

    ||J_C||_2^2
      = m^-2 sum_(v,w) ||U_w^*U_v||_2^2
      = D.

Applying the formula to `C tensor C` on input dimension `D^2` gives

    E P_T = (alpha_U^2+D^2)/[D^2(D^2+1)].

Tracing the Haar second moment over one pair of D-dimensional systems gives

    E[rho_T^tensor2]=(D I+F)/[D(D^2+1)],

and therefore

    E d_T=(alpha_U+1)/(D^2+1).

Using the exact orbit-block identity

    N_T=m^2 P_T-m d_T,

and the pointwise definition `N_T<=kappa_1(U) m d_T`, taking expectations yields
the stated Haar-LB. Rank-deficient T form a Haar-null algebraic set, while `d_T>0`,
so the weighted average is attained or exceeded by at least one full-rank T.

If `kappa_1(U)<=A-1`, Haar-LB rearranges to

    m alpha_U^2 - A D^2 alpha_U + D^2(m-A) <= 0.

At the one-copy upper endpoint `alpha_U=A D^2/m`, the first two terms cancel and
the remainder is `D^2(m-A)>0`. Thus a candidate cannot saturate the one-copy
bound at the maximally mixed input. The roots and exact gap in the response are
algebraically correct.

## Redundancy check omitted from the response

For a Haar-uniform rank-one input `|y><y|`, the same second-moment identity gives

    E_y ||C(|y><y|)||_2^2
      = (alpha_U+D)/[D(D+1)].

Therefore the actual one-copy supremum assumption already implies

    (alpha_U+D)/[D(D+1)] <= p <= A/m,

or

    m(alpha_U+D) <= A D(D+1).                    (Pure-avg)

Together with `alpha_U>=D^2/m`, this forces

    D >= (m-A)/(A-1).

Under `ln m>18` and `A^2<m^(1/m)`, one has `A<2m/(m+1)`, so this lower bound gives
`D>m`. Consequently

    D < alpha_U <= D^2,

where the upper bound follows because `C(I_D)` is positive with trace D.

On this interval, compare the rank-one Haar-average ratio with Haar-LB:

    (alpha_U+D)/[D(D+1)]
      - (alpha_U^2+D^2)/[D^2(alpha_U+1)]

    = (alpha_U-D)(D^2-alpha_U)
      / [D^2(D+1)(alpha_U+1)]
    >= 0.

Thus `(Pure-avg)` implies the quadratic condition `(HC)` throughout every
low-A-feasible parameter regime. It also gives the sharper explicit bound

    alpha_U <= A D(D+1)/m - D
             < A D^2/m.

Hence the response's claimed strict slack at the maximally mixed input was already
forced by the original one-copy supremum bound. Haar-LB is new only in asserting
that a full-Schmidt-rank witness can attain its weaker average ratio; it does not
add a new necessary scalar restriction for `(E1_gap)`.

## Remaining boundary

The response correctly isolates the double-centered term and proves a valid
full-Schmidt-rank averaging identity, but its advertised scalar obstruction is
dominated by the existing one-copy/rank-one average bound. It therefore does not
meet the prompt's requirement for a genuinely new material advance. It also does
not provide the required uniform pointwise upper bound on `Gamma_U(T)` or turn the
Haar average over T into a tuple-existence argument. The scientifically safe status
is therefore:

    (E1_gap): OPEN.
    full-size finite-dimensional theorem: OPEN / CONJECTURED.

<!-- END HISTORICAL FILE path=outputs/round-03-local-audit.md -->


# ROUND 004

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-04-prompt.md bytes=6075 sha256=3b656a4805182a9ea995bd65309f213595719c220768f8e007821f2e80cd875f -->

# Round 4 — audit the Haar-LB novelty and test a same-orientation Bell orbit

Continue in the same one-layer deterministic setup. This is an adversarial
correction round, not a request to repeat the broad full-size blueprint.

Let finite `m,D`, `eta>0`, and one frozen complex tuple

    U=(U_1,...,U_m) in U(D)^m

define

    C(X)_(v,w)=m^(-1) Tr(X U_w^*U_v),
    A=1+9(1+eta)^2/m,
    p=sup_rho ||C(rho)||_2^2,

with

    ln m>18,
    A^2<m^(1/m),
    p<=A/m.

For Hilbert--Schmidt unit `T`, retain the audited definitions of `d_T`,
`R_U(T)`, and `kappa_1(U)`. The corrected existential target is still

    (E1_gap):  kappa_1(U)<=A-1

for one finite tuple satisfying all the conditions above.

Round 3 correctly rederived `(FR)`, `(LF)`, `(PT)`, and the double-centered
reduction. It then claimed genuinely new progress from

    alpha = ||C(I_D)||_2^2,

    kappa_1(U) >=
      m(alpha^2+D^2)/[D^2(alpha+1)] - 1.        (Haar-LB)

The formula itself appears correct, but its claimed novelty appears false in
the low-A feasible regime. Audit the following comparison before using
`(Haar-LB)`.

## A. Suspected redundancy

For Haar-uniform unit `y in C^D`, the standard second moment gives

    E_y ||C(|y><y|)||_2^2
      = (alpha+D)/[D(D+1)].                     (PureAvg)

Here `||J_C||_2^2=D`. Hence the actual one-copy supremum assumption already
implies

    m(alpha+D) <= A D(D+1).                    (PA)

Also

    D^2/m <= alpha <= D^2.

Combining the lower bound on `alpha` with `(PA)` gives

    D >= (m-A)/(A-1).

The low-A assumptions imply `A<2m/(m+1)`, hence every feasible candidate has
`D>m` and therefore `alpha>D`.

On `D<=alpha<=D^2`, the proposed comparison is

    (alpha+D)/[D(D+1)]
      - (alpha^2+D^2)/[D^2(alpha+1)]

    = (alpha-D)(D^2-alpha)
      / [D^2(D+1)(alpha+1)] >= 0.               (Dom)

Thus the rank-one Haar-average bound already dominates `(Haar-LB)`, and `(PA)`
implies Round 3's quadratic condition `(HC)`. Its strict maximally-mixed slack
was already forced by `p<=A/m`:

    alpha <= A D(D+1)/m - D < A D^2/m.

Independently verify or refute every step. If it is correct, explicitly retract
the claim that `(HC)` is a new necessary scalar obstruction for `(E1_gap)`.
The existence of a full-rank witness for a weaker value may be valid, but does
not by itself materially advance the gate.

## B. Fixed-Schmidt-spectrum local-twirl no-go

Let `lambda_i>0`, `sum_i lambda_i=1`,

    t=sum_i lambda_i^2 in [1/D,1),
    |psi_lambda>=sum_i sqrt(lambda_i)|i,i>,

and independently Haar-randomize both input legs:

    Psi_(lambda,V,W)
      =(V tensor W)|psi_lambda><psi_lambda|(V^* tensor W^*).

Let

    d_(lambda,V,W)

be the corresponding `d_T`, and let

    P_(lambda,V,W)
      =||(C tensor C)(Psi_(lambda,V,W))||_2^2.

Define

    u=(alpha-1)/(D^2-1),
    v=(D^2-alpha)/[D(D^2-1)].

Candidate exact formulas to audit are

    E d_(lambda,V,W) = u+t v,                   (SD1)

    E P_(lambda,V,W) = u^2+v^2+2tuv.            (SD2)

They should follow by projecting the local two-copy twirl onto the basis
`{I,F}` with Gram matrix

    [[D^2,D],[D,D^2]]

and moment matrix

    [[1,t],[t,1]].

Since pointwise

    P_T=d_T(1+R_U(T))/m,

the ratio of expectations would imply

    kappa_1(U)+1 >=
      m [u^2+v^2+2tuv]/[u+tv].                 (SD-LB)

Differentiate the scalar quotient exactly. The candidate derivative is

    v(u^2-v^2)/(u+tv)^2.

In the feasible regime `alpha>D`, this is nonnegative, so the strongest
fixed-spectrum independent-local-Haar bound occurs at the rank-one boundary
`t=1` and equals

    m(alpha+D)/[D(D+1)].

If correct, prove the resulting no-go theorem: no full-rank fixed-Schmidt-
spectrum argument based only on independent local Haar second moments and the
single scalar `alpha` can improve the already available rank-one average bound.
Also verify that mixing over `t` with `E t=2D/(D^2+1)` recovers Round 3's
`(Haar-LB)`.

## C. First orientation-sensitive family

The independent local twirl erases the same-tuple orientation that is the
actual difficulty. Therefore examine the correlated, full-rank symmetric Bell
orbit

    T_V = V V^T/sqrt(D),       V Haar in U(D),
    Psi_V=|T_V>><<T_V|.

For every `V`,

    T_V T_V^*=I_D/D,
    d_(T_V)=alpha/D^2,

so the denominator of `R_U(T_V)` is constant. This is a genuine continuum of
full-Schmidt-rank physical inputs, not a single Bell test and not fresh channel
randomness.

Derive an exact expression for

    E_V R_U(T_V)                                (SymBell)

using the unitary Haar/Weingarten moment required by this orbit. Express the
answer as a finite linear combination of explicitly defined deterministic
same-tuple invariants (traces of products of the `U_a`), with all coefficients
and normalizations shown. Simplify using every identity forced by unitarity,
trace preservation, `(LF)`, and `p<=A/m`.

Then do exactly one of the following:

1. prove that the low-A assumptions force `E_V R_U(T_V)>A-1`, which would
   disprove `(E1_gap)`;
2. prove a uniform upper bound compatible with `A-1` for one explicit finite
   tuple; or
3. isolate the first specific orientation-sensitive invariant whose required
   inequality is not controlled, and prove the exact necessary inequality on
   that invariant for `(E1_gap)`.

Do not answer merely that Weingarten calculus is lengthy. If a fully expanded
index formula is unavoidable, give it and then group it into invariant
contractions. Do not use numerics, independent copies of the tuple, unrestricted
cb/2->2 estimates, real/orthogonal tuples, the full Weyl loophole, or a generic
fixed-T concentration claim.

## Required verdict and ledger

Start with separate verdicts on:

    (i) redundancy of Haar-LB/HC,
    (ii) the fixed-spectrum no-go,
    (iii) E1_gap.

End with an audit ledger separating `PROVED`, `DISPROVED`, `REDUNDANT`, `OPEN`,
and `CONJECTURED`. The full-size theorem must remain `OPEN` unless the finite
gate and the earlier all-copy gate are both actually closed. Give only a public,
self-contained derivation; do not provide hidden chain-of-thought.

<!-- END HISTORICAL FILE path=work/round-04-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-04-response.md bytes=27121 sha256=854e4a917ed52f528a9d0b0c06d5dd12d7fdbeccc2412b3261b1037a19e81736 -->

# Separate verdicts

**(i) Haar-LB / HC novelty:** **REDUNDANT.**
The formula

$$
\kappa_1(U)\ge
\frac{m(\alpha^2+D^2)}{D^2(\alpha+1)}-1
$$

is correct, and its witness may be chosen full Schmidt rank. However, throughout the low-\(A\) feasible regime it is strictly dominated by the rank-one Haar-average lower bound. Round 3’s claim that the associated quadratic condition \((HC)\) was a new scalar obstruction is therefore retracted.

**(ii) Fixed-Schmidt-spectrum local-twirl no-go:** **PROVED**, in the precise second-moment sense stated below. Independent local Haar randomization with a fixed Schmidt spectrum and using only the scalar \(\alpha\) cannot improve the rank-one Haar-average lower bound.

**(iii) \((E1_{\mathrm{gap}})\):** **OPEN WITH EARLIEST GAP.**
For the correlated symmetric-Bell orbit \(T_V=VV^{\mathsf T}/\sqrt D\), the exact average can be computed. It introduces the same-tuple fourth-order commutator invariant

$$
\mathsf C_U
=
\sum_{v,w,a,b}
\operatorname{Tr}\!\left(
U_w^*U_v\,U_b^*U_a\,
U_v^*U_w\,U_a^*U_b
\right).
$$

The low-\(A\) one-copy hypothesis supplies an upper bound on \(\mathsf C_U\), whereas the ratio gate requires a specific lower bound. Neither implication is presently strong enough to close the interval.

All randomness below is over test inputs after \(U\) has been frozen. No fresh channel tuple is introduced.

---

# A. The Haar-LB obstruction is redundant

Put

$$
A_{vw}=U_w^*U_v,
\qquad
\alpha=\|C(I_D)\|_2^2
=
\frac1{m^2}\sum_{v,w}
|\operatorname{Tr}A_{vw}|^2.
$$

## A.1 Pure-state Haar average

For Haar-uniform \(y\in\mathbb C^D\),

$$
\mathbb E_y\bigl[|y\rangle\langle y|^{\otimes2}\bigr]
=
\frac{I+F}{D(D+1)},
\tag{A.1}
$$

where \(F\) is the swap on \((\mathbb C^D)^{\otimes2}\). This follows from unitary invariance and the two conditions

$$
\operatorname{Tr}\mathbb E\rho_y^{\otimes2}=1,
\qquad
\operatorname{Tr}\!\left(F\mathbb E\rho_y^{\otimes2}\right)=1.
$$

For the Choi matrix convention

$$
J_C=\sum_{i,j}E_{ij}\otimes C(E_{ij}),
$$

one has

$$
\begin{aligned}
\|J_C\|_2^2
&=
\sum_{i,j}\|C(E_{ij})\|_2^2\\
&=
\frac1{m^2}
\sum_{v,w}\sum_{i,j}
|(A_{vw})_{ji}|^2\\
&=
\frac1{m^2}\sum_{v,w}D
=
D.
\end{aligned}
\tag{A.2}
$$

Applying \(C\otimes C\) to (A.1) and contracting with the output swap gives

$$
\boxed{
\mathbb E_y\,
\|C(|y\rangle\langle y|)\|_2^2
=
\frac{\alpha+D}{D(D+1)}.
}
\tag{PureAvg}
$$

Since the supremum \(p\) bounds the average,

$$
\boxed{
m(\alpha+D)\le AD(D+1).
}
\tag{PA}
$$

## A.2 Bounds on \(\alpha\) and \(D\)

The matrix \(C(I_D/D)\) is a density matrix in dimension \(m\). Therefore

$$
\frac{\alpha}{D^2}
=
\left\|C\left(\frac{I_D}{D}\right)\right\|_2^2
\ge \frac1m,
$$

so

$$
\boxed{\alpha\ge\frac{D^2}{m}.}
\tag{A.3}
$$

Also \(C(I_D)\succeq0\) and \(\operatorname{Tr}C(I_D)=D\), hence

$$
\boxed{\alpha\le D^2.}
\tag{A.4}
$$

Combining (A.3) with \((PA)\),

$$
D^2+mD
\le
AD(D+1),
$$

and consequently

$$
\boxed{
D\ge\frac{m-A}{A-1}.
}
\tag{A.5}
$$

The low-\(A\) assumption implies

$$
A<m^{1/(2m)}.
$$

For \(m>1\),

$$
\frac{\ln m}{2m}
<
\frac{m-1}{2m}
\le
\ln\!\left(\frac{2m}{m+1}\right).
$$

The first inequality is \(\ln m<m-1\); the second follows from

$$
\ln(1+x)=\int_0^x\frac{dt}{1+t}
\ge\frac{x}{1+x}
$$

with \(x=(m-1)/(m+1)\). Hence

$$
\boxed{
A<\frac{2m}{m+1}.
}
\tag{A.6}
$$

This makes the right side of (A.5) strictly larger than \(m\):

$$
\frac{m-A}{A-1}>m
\quad\Longleftrightarrow\quad
A<\frac{2m}{m+1}.
$$

Thus every feasible tuple satisfies

$$
\boxed{D>m}
\tag{A.7}
$$

and therefore

$$
\boxed{\alpha>D.}
\tag{A.8}
$$

In fact \((PA)\) also yields

$$
\alpha
\le
\frac{AD(D+1)}m-D
<
\frac{AD^2}{m}
<
D^2,
\tag{A.9}
$$

where the strict middle inequality uses \(A<m\).

## A.3 Direct comparison with Haar-LB

Define

$$
q_{\mathrm{pure}}
=
\frac{\alpha+D}{D(D+1)}
$$

and

$$
q_{\mathrm{full}}
=
\frac{\alpha^2+D^2}{D^2(\alpha+1)}.
$$

A direct common-denominator calculation gives

$$
\boxed{
q_{\mathrm{pure}}-q_{\mathrm{full}}
=
\frac{(\alpha-D)(D^2-\alpha)}
{D^2(D+1)(\alpha+1)}.
}
\tag{A.10}
$$

In the feasible regime \(D<\alpha<D^2\), this is strictly positive.

Rank-one inputs give

$$
\kappa_1(U)+1
\ge
m\sup_y\|C(|y\rangle\langle y|)\|_2^2
\ge
m q_{\mathrm{pure}}.
\tag{A.11}
$$

Round 3’s full-rank averaging gave only

$$
\kappa_1(U)+1\ge m q_{\mathrm{full}}.
\tag{A.12}
$$

Thus (A.11) strictly dominates (A.12).

Moreover, the Round 3 condition \((HC)\) was exactly

$$
m q_{\mathrm{full}}\le A.
$$

But \((PA)\) states

$$
m q_{\mathrm{pure}}\le A,
$$

and \(q_{\mathrm{full}}\le q_{\mathrm{pure}}\). Hence \((HC)\) is already implied by the pure-state average.

Finally,

$$
\alpha\le \frac{AD(D+1)}m-D
<
\frac{AD^2}{m},
$$

so the previously claimed “strict maximally mixed slack” is also already forced by \((PA)\).

Therefore:

$$
\boxed{
\text{Haar-LB is valid but redundant as an obstruction to }(E1_{\rm gap}).
}
$$

The existence of a full-rank witness for the weaker lower-bound value remains correct, but it does not materially advance the gate.

---

# B. Fixed-Schmidt-spectrum independent local twirling

Let

$$
\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_D),
\qquad
\lambda_i>0,
\qquad
\operatorname{Tr}\Lambda=1,
$$

and

$$
t=\operatorname{Tr}\Lambda^2\in[1/D,1).
$$

Under independent Haar \(V,W\),

$$
|\psi_{\lambda,V,W}\rangle
=
(V\otimes W)|\psi_\lambda\rangle.
$$

With the column-vectorization convention,

$$
T=W\Lambda^{1/2}V^{\mathsf T},
$$

so

$$
\rho_T=TT^*=W\Lambda W^*.
$$

Define

$$
u=\frac{\alpha-1}{D^2-1},
\qquad
v=\frac{D^2-\alpha}{D(D^2-1)}.
\tag{B.1}
$$

## B.1 Derivation of \((SD1)\)

The Haar twirl of \(\Lambda^{\otimes2}\) has the form

$$
\mathbb E_W
\left[
(W\Lambda W^*)^{\otimes2}
\right]
=
aI+bF.
$$

The conditions

$$
aD^2+bD=1,
\qquad
aD+bD^2=t
$$

give

$$
a=\frac{D-t}{D(D^2-1)},
\qquad
b=\frac{Dt-1}{D(D^2-1)}.
$$

Therefore

$$
\begin{aligned}
\mathbb E\,d_{\lambda,V,W}
&=
a\,\operatorname{Tr}C(I)^2
+
b\,\|J_C\|_2^2\\
&=
a\alpha+bD\\
&=
\boxed{u+tv.}
\end{aligned}
\tag{SD1}
$$

## B.2 Derivation of \((SD2)\)

Let

$$
F^0=I,\qquad F^1=F
$$

on two copies of \(\mathbb C^D\). Their Gram matrix is

$$
G_{ij}=\operatorname{Tr}(F^iF^j)
=
\begin{pmatrix}
D^2&D\\
D&D^2
\end{pmatrix}.
\tag{B.2}
$$

For the one-leg output-purity functional, the contraction vector is

$$
h=
\begin{pmatrix}
\operatorname{Tr}C(I)^2\\
\|J_C\|_2^2
\end{pmatrix}
=
\begin{pmatrix}
\alpha\\
D
\end{pmatrix}.
$$

Since

$$
G^{-1}
=
\frac1{D^2(D^2-1)}
\begin{pmatrix}
D^2&-D\\
-D&D^2
\end{pmatrix},
$$

one finds

$$
G^{-1}h=
\begin{pmatrix}u\\v\end{pmatrix}.
\tag{B.3}
$$

For the fixed-Schmidt pure state, the four local permutation moments are

$$
M_{ij}
=
\operatorname{Tr}
\left[
\Psi_\lambda^{\otimes2}
(F_A^i\otimes F_B^j)
\right]
=
\begin{pmatrix}
1&t\\
t&1
\end{pmatrix}_{ij}.
\tag{B.4}
$$

Consequently,

$$
\begin{aligned}
\mathbb E\,P_{\lambda,V,W}
&=
\begin{pmatrix}u&v\end{pmatrix}
\begin{pmatrix}1&t\\t&1\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix}\\
&=
\boxed{u^2+v^2+2tuv.}
\end{aligned}
\tag{SD2}
$$

## B.3 Ratio lower bound and monotonicity

Pointwise,

$$
P_T=\frac{d_T(1+R_U(T))}{m}
\le
\frac{d_T(1+\kappa_1(U))}{m}.
$$

Averaging gives

$$
\boxed{
\kappa_1(U)+1
\ge
m\,\frac{u^2+v^2+2tuv}{u+tv}.
}
\tag{SD-LB}
$$

For

$$
f(t)=\frac{u^2+v^2+2tuv}{u+tv},
$$

differentiation gives

$$
\boxed{
f'(t)
=
\frac{v(u^2-v^2)}{(u+tv)^2}.
}
\tag{B.5}
$$

Now

$$
u-v
=
\frac{\alpha-D}{D(D-1)},
\qquad
u+v
=
\frac{\alpha+D}{D(D+1)}.
\tag{B.6}
$$

In the feasible regime \(D<\alpha<D^2\),

$$
v>0,\qquad u>v,
$$

so

$$
f'(t)>0.
$$

Therefore the strongest value obtainable from this second-moment ratio occurs at the rank-one boundary \(t=1\):

$$
f(1)=u+v=\frac{\alpha+D}{D(D+1)}.
$$

Thus

$$
\boxed{
\sup_{t\in[1/D,1)}
m f(t)
=
m\,\frac{\alpha+D}{D(D+1)},
}
$$

with the supremum approached as the Schmidt spectrum approaches rank one.

This proves the precise no-go:

> Any lower bound on \(\kappa_1\) obtained solely from the independent-local-Haar averages \((SD1)\), \((SD2)\), the scalar \(\alpha\), and the inequality \(P_T\le d_T(1+\kappa_1)/m\), is no stronger than the rank-one Haar-average bound.

This statement does not exclude an argument using higher moments, tails, or additional same-tuple invariants.

## B.4 Recovery of Round 3’s Haar-LB

For a Haar-random pure state on \(\mathbb C^D\otimes\mathbb C^D\),

$$
\mathbb E t=\frac{2D}{D^2+1}.
\tag{B.7}
$$

Substitution gives

$$
u+\mathbb E[t]\,v
=
\frac{\alpha+1}{D^2+1},
$$

and

$$
u^2+v^2+2\mathbb E[t]uv
=
\frac{\alpha^2+D^2}{D^2(D^2+1)}.
$$

Hence

$$
m\frac{\mathbb E P}{\mathbb E d}
=
\boxed{
\frac{m(\alpha^2+D^2)}
{D^2(\alpha+1)},
}
$$

which is exactly Round 3’s Haar-LB.

Mixing fixed spectra with any distribution merely replaces \(t\) by \(\mathbb E t\), because both \((SD1)\) and \((SD2)\) are affine in \(t\). Since \(\mathbb E t\le1\), such mixing cannot exceed the rank-one boundary either.

---

# C. The correlated symmetric-Bell orbit

Set

$$
S_V=VV^{\mathsf T},
\qquad
T_V=\frac{S_V}{\sqrt D}.
$$

Then \(S_V\) is symmetric and unitary, and

$$
T_VT_V^*=T_V^*T_V=\frac{I_D}{D}.
$$

Therefore

$$
d_{T_V}
=
\left\|C\left(\frac{I_D}{D}\right)\right\|_2^2
=
\frac{\alpha}{D^2},
\tag{C.1}
$$

independently of \(V\).

For

$$
A=A_{vw}=U_w^*U_v,
\qquad
B=A_{ab}=U_b^*U_a,
$$

one has

$$
X_{vw}(T_V)
=
\frac1D S_VA^{\mathsf T}S_V^*,
$$

and therefore

$$
C(X_{vw}(T_V))_{a,b}
=
\frac1{mD}
\operatorname{Tr}(S_VA^{\mathsf T}S_V^*B).
\tag{C.2}
$$

Define

$$
g_V(A,B)
=
\operatorname{Tr}(S_VA^{\mathsf T}S_V^*B).
\tag{C.3}
$$

Then

$$
1+R_U(T_V)
=
\frac1{m^3\alpha}
\sum_{v,w,a,b}
|g_V(A_{vw},A_{ab})|^2.
\tag{C.4}
$$

The diagonal \(v=w\) contributions account exactly for the \(1\) in \(1+R\).

---

## C.1 Exact fourth moment of the \(V\otimes V\) orbit

Let

$$
|\Omega\rangle
=
\frac1{\sqrt D}\sum_i|i,i\rangle.
$$

Under column vectorization,

$$
|\phi_V\rangle
=
(V\otimes V)|\Omega\rangle
=
|S_V/\sqrt D\rangle\rangle.
$$

Thus

$$
g_V(A,B)
=
D\langle\phi_V|A\otimes B|\phi_V\rangle.
\tag{C.5}
$$

Let

$$
\mathcal M_D
=
\mathbb E_V
\left[
|\phi_V\rangle\langle\phi_V|^{\otimes2}
\right].
$$

Work on four tensor factors and let \(P_\pi\) denote the permutation operator associated with \(\pi\in S_4\). Let

$$
H=
\{
e,(12),(34),(12)(34),(13)(24),(14)(23),(1324),(1423)
\},
$$

the order-eight subgroup preserving the pairing
\(\{\{1,2\},\{3,4\}\}\). Define

$$
P_H=\frac18\sum_{h\in H}P_h,
\qquad
P_4=\frac1{24}\sum_{\pi\in S_4}P_\pi.
$$

The vector

$$
\xi=|\Omega\rangle^{\otimes2}
$$

is \(H\)-invariant. Moreover,

$$
\langle\xi|P_\pi|\xi\rangle
=
\begin{cases}
1,&\pi\in H,\\[1mm]
1/D,&\pi\notin H.
\end{cases}
\tag{C.6}
$$

Indeed, outside \(H\), the two distinct pairings jointly force all four indices to be equal, leaving \(D\) assignments rather than \(D^2\).

The \(H\)-invariant subspace decomposes as

$$
\operatorname{ran}P_H
=
\operatorname{Sym}^4(\mathbb C^D)
\oplus
\mathbb S_{(2,2)}(\mathbb C^D),
$$

with projector \(P_4\) onto the first summand and \(P_H-P_4\) onto the second. Their dimensions are

$$
d_4=\binom{D+3}{4}
=
\frac{D(D+1)(D+2)(D+3)}{24},
$$

and

$$
d_{22}
=
\frac{D^2(D^2-1)}{12}.
$$

From (C.6),

$$
w_4
=
\langle\xi|P_4|\xi\rangle
=
\frac{D+2}{3D},
$$

and

$$
w_{22}=1-w_4=\frac{2(D-1)}{3D}.
$$

Haar averaging is scalar on each of these two inequivalent irreducible summands, so

$$
\begin{aligned}
\mathcal M_D
&=
\frac{w_4}{d_4}P_4
+
\frac{w_{22}}{d_{22}}(P_H-P_4)\\
&=
\frac{8}{D^2(D+1)(D+3)}P_4
+
\frac{8}{D^3(D+1)}(P_H-P_4).
\end{aligned}
\tag{C.7}
$$

Equivalently,

$$
\boxed{
\mathcal M_D
=
\frac{
(D+3)\displaystyle\sum_{h\in H}P_h
-
\displaystyle\sum_{\pi\in S_4}P_\pi
}{
D^3(D+1)(D+3)
}.
}
\tag{C.8}
$$

This is the required fourth-order Haar/Weingarten moment for the symmetric-Bell orbit.

---

## C.2 Generic two-matrix contraction

For unitary \(A,B\), write

$$
x=\operatorname{Tr}A,\qquad
y=\operatorname{Tr}B,
$$

$$
z=\operatorname{Tr}(AB),\qquad
q=\operatorname{Tr}(AB^*),
$$

and

$$
c=\operatorname{Tr}(ABA^*B^*).
$$

For a permutation \(\pi\), the contraction

$$
\operatorname{Tr}\!\left[
P_\pi
(A\otimes B\otimes A^*\otimes B^*)
\right]
$$

is the product, over cycles of \(\pi\), of traces of the corresponding ordered matrix products.

Summing over the eight elements of \(H\) gives

$$
\boxed{
\begin{aligned}
\mathsf H(A,B)
={}&
D^2+2D+|z|^2+|q|^2+|x|^2|y|^2\\
&\quad+2\operatorname{Re}(xy\overline z).
\end{aligned}
}
\tag{C.9}
$$

Summing over all \(24\) permutations gives

$$
\boxed{
\begin{aligned}
\mathsf S(A,B)
={}&
D^2+4D
+(D+4)(|x|^2+|y|^2)\\
&+|z|^2+|q|^2+|x|^2|y|^2\\
&+2\operatorname{Re}(xy\overline z)\\
&+2\operatorname{Re}(x\overline y\,\overline q)\\
&+2\operatorname{Re}c.
\end{aligned}
}
\tag{C.10}
$$

Equations (C.5) and (C.8) therefore give

$$
\boxed{
\mathbb E_V|g_V(A,B)|^2
=
\frac{
(D+3)\mathsf H(A,B)-\mathsf S(A,B)
}{
D(D+1)(D+3)
}.
}
\tag{C.11}
$$

---

# D. Same-tuple invariants

Let

$$
\mathscr A_U
=
\{A_{vw}=U_w^*U_v:1\le v,w\le m\}
$$

as a multiset. It has \(m^2\) elements, is closed under adjoint, and contains \(m\) copies of \(I_D\).

Define

$$
\boxed{
\mathsf I_U
=
\sum_{A,B\in\mathscr A_U}
|\operatorname{Tr}(AB)|^2,
}
\tag{D.1}
$$

$$
\boxed{
\mathsf T_U
=
\sum_{A,B\in\mathscr A_U}
\operatorname{Tr}A\,
\operatorname{Tr}B\,
\overline{\operatorname{Tr}(AB)},
}
\tag{D.2}
$$

and

$$
\boxed{
\mathsf C_U
=
\sum_{A,B\in\mathscr A_U}
\operatorname{Tr}(ABA^*B^*).
}
\tag{D.3}
$$

Explicitly,

$$
\mathsf I_U
=
\sum_{v,w,a,b}
\left|
\operatorname{Tr}
(U_w^*U_vU_b^*U_a)
\right|^2,
$$

$$
\mathsf T_U
=
\sum_{v,w,a,b}
\operatorname{Tr}(U_w^*U_v)\,
\operatorname{Tr}(U_b^*U_a)\,
\overline{
\operatorname{Tr}(U_w^*U_vU_b^*U_a)
},
$$

and

$$
\mathsf C_U
=
\sum_{v,w,a,b}
\operatorname{Tr}
\left(
U_w^*U_vU_b^*U_a
U_v^*U_wU_a^*U_b
\right).
$$

## D.1 Positivity and reality properties

Let

$$
\mathbf R_U=\sum_v U_v\otimes\overline{U_v},
$$

and

$$
\mathbf K_U
=
\sum_{A\in\mathscr A_U}A\otimes\overline A
=
\mathbf R_U^*\mathbf R_U
\succeq0.
$$

Then

$$
\operatorname{Tr}\mathbf K_U=m^2\alpha
$$

and

$$
\boxed{
\mathsf I_U=\operatorname{Tr}\mathbf K_U^2.
}
\tag{D.4}
$$

Hence

$$
\boxed{
\mathsf I_U\ge\frac{m^4\alpha^2}{D^2}.
}
\tag{D.5}
$$

Next define

$$
\mathbf M_U
=
\sum_{A\in\mathscr A_U}
\operatorname{Tr}(A)\,A^*.
$$

The multiset is adjoint-closed, so \(\mathbf M_U\) is Hermitian. It is in fact positive semidefinite: for unit \(x\),

$$
\begin{aligned}
\langle x,\mathbf M_Ux\rangle
&=
\sum_{v,w}
\operatorname{Tr}(U_w^*U_v)
\langle U_vx,U_wx\rangle\\
&=
\operatorname{Tr}(G_{\rm HS}G_x)\ge0,
\end{aligned}
$$

where \(G_{\rm HS}\) and \(G_x\) are the two positive Gram matrices of the families \(\{U_v\}\) and \(\{U_vx\}\).

Moreover,

$$
\operatorname{Tr}\mathbf M_U=m^2\alpha,
$$

and

$$
\boxed{
\mathsf T_U=\operatorname{Tr}\mathbf M_U^2\ge0.
}
\tag{D.6}
$$

Therefore

$$
\boxed{
\mathsf T_U\ge\frac{m^4\alpha^2}{D}.
}
\tag{D.7}
$$

Finally, set

$$
\mathbf Z_U
=
\sum_{A\in\mathscr A_U}A\otimes A^*.
$$

It is Hermitian and commutes with the swap \(F\). One has

$$
\operatorname{Tr}\mathbf Z_U^2=\mathsf I_U
$$

and

$$
\boxed{
\mathsf C_U
=
\operatorname{Tr}(\mathbf Z_U^2F).
}
\tag{D.8}
$$

Thus \(\mathsf C_U\) is real and

$$
\boxed{
|\mathsf C_U|\le\mathsf I_U.
}
\tag{D.9}
$$

The quantity \(\mathsf C_U\) is the first explicitly orientation-sensitive contraction: it measures the aggregate ordered commutators \(ABA^*B^*\).

---

# E. Exact symmetric-Bell average

Because \(\mathscr A_U\) is adjoint-closed,

$$
\sum_{A,B}
|\operatorname{Tr}(AB^*)|^2
=
\mathsf I_U,
$$

and

$$
\sum_{A,B}
\operatorname{Re}
\left[
\operatorname{Tr}A\,
\overline{\operatorname{Tr}B}\,
\overline{\operatorname{Tr}(AB^*)}
\right]
=
\mathsf T_U.
$$

Summing (C.9) over \(A,B\in\mathscr A_U\) gives

$$
\boxed{
\mathsf H_U
=
m^4(D^2+2D+\alpha^2)
+
2\mathsf I_U
+
2\mathsf T_U.
}
\tag{E.1}
$$

Summing (C.10) gives

$$
\boxed{
\begin{aligned}
\mathsf S_U
={}&
m^4\left[
D^2+4D+\alpha^2+2(D+4)\alpha
\right]\\
&+
2\mathsf I_U
+
4\mathsf T_U
+
2\mathsf C_U.
\end{aligned}
}
\tag{E.2}
$$

Therefore

$$
\boxed{
\mathbb E_V[1+R_U(T_V)]
=
\frac{
(D+3)\mathsf H_U-\mathsf S_U
}{
m^3\alpha D(D+1)(D+3)
}.
}
\tag{SymBell}
$$

Equivalently, define

$$
B_0(D,\alpha)
=
D(D^2+4D+2)
+
(D+2)\alpha^2
-
2(D+4)\alpha.
\tag{E.3}
$$

Then

$$
\boxed{
\begin{aligned}
\mathbb E_V[1+R_U(T_V)]
={}&
\frac{1}{
m^3\alpha D(D+1)(D+3)
}
\Bigl[
m^4B_0(D,\alpha)\\
&\quad
+2(D+2)\mathsf I_U
+2(D+1)\mathsf T_U
-2\mathsf C_U
\Bigr].
\end{aligned}
}
\tag{E.4}
$$

This is the exact requested finite linear combination of deterministic same-tuple trace invariants.

---

# F. What \((LF)\), \((PT)\), and \(p\le A/m\) imply

## F.1 Partial traces are completely flat on this orbit

For \(T_V\),

$$
\rho_{T_V}
=
(T_V^*T_V)^{\mathsf T}
=
\frac{I_D}{D}.
$$

Since the random-unitary channel

$$
L(X)=\frac1m\sum_aU_aXU_a^*
$$

is unital,

$$
L(I_D/D)=I_D/D.
$$

Consequently, all four partial traces from \((PT)\) are

$$
\boxed{
\operatorname{Tr}_A F_{T_V}
=
\operatorname{Tr}_B F_{T_V}
=
\operatorname{Tr}_A\mathfrak R_U(F_{T_V})
=
\operatorname{Tr}_B\mathfrak R_U(F_{T_V})
=
\frac{mI_D}{D}.
}
\tag{F.1}
$$

Thus the partial-trace constraints provide no \(V\)-dependent control of the global frame purity on this orbit.

## F.2 A fourth-moment consequence of the one-copy bound

For a unit vector \(y\), define

$$
f_U(y)
=
\sum_{A\in\mathscr A_U}
|\langle y|A|y\rangle|^2
=
m^2\|C(|y\rangle\langle y|)\|_2^2.
\tag{F.2}
$$

The one-copy hypothesis gives the pointwise inequality

$$
f_U(y)\le Am.
\tag{F.3}
$$

The fourth Haar moment is

$$
\mathbb E_y
[|y\rangle\langle y|^{\otimes4}]
=
\frac{
\sum_{\pi\in S_4}P_\pi
}{
D(D+1)(D+2)(D+3)
}.
\tag{F.4}
$$

Using the same permutation contractions as in (C.10),

$$
\boxed{
\mathbb E_y f_U(y)^2
=
\frac{\mathsf S_U}
{D(D+1)(D+2)(D+3)}.
}
\tag{F.5}
$$

Also,

$$
\mathbb E_y f_U(y)
=
m^2\frac{\alpha+D}{D(D+1)}.
\tag{F.6}
$$

Because \(f_U(y)^2\le Am\,f_U(y)\), one gets

$$
\boxed{
\mathsf S_U
\le
A m^3(\alpha+D)(D+2)(D+3).
}
\tag{F.7}
$$

In terms of the commutator invariant, this is

$$
\boxed{
\begin{aligned}
\mathsf C_U
\le \frac12\Bigl[
&A m^3(\alpha+D)(D+2)(D+3)\\
&-m^4\bigl(D^2+4D+\alpha^2+2(D+4)\alpha\bigr)\\
&-2\mathsf I_U-4\mathsf T_U
\Bigr].
\end{aligned}
}
\tag{C-upper}
$$

Thus the one-copy bound provides an **upper** bound on \(\mathsf C_U\).

---

# G. The exact orientation-sensitive obstruction

If

$$
\kappa_1(U)\le A-1,
$$

then \(1+R_U(T_V)\le A\) for every \(V\), so in particular

$$
\mathbb E_V[1+R_U(T_V)]\le A.
$$

Using (E.4), this is equivalent to the necessary inequality

$$
\boxed{
\begin{aligned}
\mathsf C_U
\ge{}&
(D+2)\mathsf I_U
+
(D+1)\mathsf T_U\\
&+
\frac{m^4}{2}B_0(D,\alpha)\\
&-
\frac{
A m^3\alpha D(D+1)(D+3)
}{2}.
\end{aligned}
}
\tag{C-required}
$$

This is the first exact orientation-sensitive invariant inequality not supplied by \((LF)\) or \((PT)\).

If \((C\text{-required})\) fails, then

$$
\mathbb E_VR_U(T_V)>A-1,
$$

so at least one deterministic \(V\) produces a full-rank physical input violating \((OL1)\).

Conversely, satisfying \((C\text{-required})\) only passes the average symmetric-Bell test; it does not prove the pointwise supremum bound.

## G.1 Compatibility with the one-copy upper bound

A necessary condition for the lower bound \((C\text{-required})\) and upper bound \((C\text{-upper})\) to coexist is

$$
\boxed{
\begin{aligned}
&m^4\left[D(D+2)+\alpha^2\right]
+
2(\mathsf I_U+\mathsf T_U)\\
&\qquad\le
A m^3
\left[
\alpha D(D+1)
+
(\alpha+D)(D+2)
\right].
\end{aligned}
}
\tag{G.1}
$$

This follows by requiring the lower endpoint for \(\mathsf C_U\) not to exceed the upper endpoint.

Using only the universal lower bounds (D.5) and (D.7), one obtains the scalar relaxation

$$
\boxed{
\begin{aligned}
m\left[
D(D+2)+\alpha^2
+
\frac{2\alpha^2(D+1)}{D^2}
\right]
\le{}&
A\left[
\alpha D(D+1)
+
(\alpha+D)(D+2)
\right].
\end{aligned}
}
\tag{G.2}
$$

However, this scalar relaxation gives no new contradiction beyond \((PA)\). Indeed, \((PA)\) says

$$
A\ge A_0:=
\frac{m(\alpha+D)}{D(D+1)}.
$$

At \(A=A_0\), the right side of (G.2) minus the left side equals

$$
\boxed{
\frac{
m(D^2-\alpha)
\left[
\alpha(D^2+2D+2)-D^2(D+2)
\right]
}{
D^2(D+1)
}.
}
\tag{G.3}
$$

For \(D<\alpha\le D^2\), both factors in square brackets are nonnegative:

$$
\alpha(D^2+2D+2)-D^2(D+2)
>
D(D^2+2D+2)-D^2(D+2)
=
2D.
$$

Thus (G.2) already follows from \((PA)\).

The genuinely unresolved information is therefore not a scalar condition on \(\alpha\). It is the actual same-tuple placement of

$$
(\mathsf I_U,\mathsf T_U,\mathsf C_U),
$$

especially whether the commutator sum \(\mathsf C_U\) can be large enough to satisfy \((C\text{-required})\) while also obeying the one-copy upper bound \((C\text{-upper})\).

---

# Final status of the finite gate

The symmetric-Bell orbit does not presently prove a universal violation. It also does not provide an explicit low-\(A\) tuple satisfying the ratio gate.

It yields the rigorous implication

$$
\boxed{
(E1_{\rm gap})
\Longrightarrow
(C\text{-required})
\ \text{and}\
(C\text{-upper}).
}
$$

The first uncontrolled same-orientation correlation is the aggregate commutator invariant

$$
\boxed{
\mathsf C_U
=
\sum_{v,w,a,b}
\operatorname{Tr}
\left(
U_w^*U_vU_b^*U_a
U_v^*U_wU_a^*U_b
\right).
}
$$

The one-copy condition constrains it from above; the symmetric-Bell ratio test constrains it from below. No contradiction between those exact constraints has been proved for every feasible tuple, and no explicit tuple satisfying the required lower bound uniformly over all \(T\) has been constructed.

---

# Audit ledger

| Status          | Statement                                                                                                                                              |                   |                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- | ---------------------------- |
| **PROVED**      | (\mathbb E_y|C(                                                                                                                                        | y\rangle\langle y | )|_2^2=(\alpha+D)/[D(D+1)]). |
| **PROVED**      | \(m(\alpha+D)\le AD(D+1)\).                                                                                                                            |                   |                              |
| **PROVED**      | Low \(A\) implies \(A<2m/(m+1)\), hence \(D>m\) and \(D<\alpha<D^2\).                                                                                  |                   |                              |
| **PROVED**      | The rank-one Haar average strictly dominates Round 3’s Haar-LB throughout the feasible regime.                                                         |                   |                              |
| **REDUNDANT**   | Haar-LB as an obstruction to \((E1_{\rm gap})\).                                                                                                       |                   |                              |
| **REDUNDANT**   | Round 3’s quadratic condition \((HC)\).                                                                                                                |                   |                              |
| **DISPROVED**   | The Round 3 claim that \((HC)\) was a new necessary scalar obstruction.                                                                                |                   |                              |
| **PROVED**      | Fixed-spectrum formulas \((SD1)\) and \((SD2)\).                                                                                                       |                   |                              |
| **PROVED**      | The quotient derivative \(v(u^2-v^2)/(u+tv)^2\).                                                                                                       |                   |                              |
| **PROVED**      | Independent local second moments are maximized at the rank-one boundary \(t=1\).                                                                       |                   |                              |
| **PROVED**      | Mixing over \(t\) with mean \(2D/(D^2+1)\) recovers Haar-LB exactly.                                                                                   |                   |                              |
| **PROVED**      | Exact symmetric-Bell fourth-moment operator (C.8).                                                                                                     |                   |                              |
| **PROVED**      | Exact contraction formulas (C.9)–(C.11).                                                                                                               |                   |                              |
| **PROVED**      | Exact symmetric-Bell average (E.4).                                                                                                                    |                   |                              |
| **PROVED**      | \(\mathsf I_U=\operatorname{Tr}\mathbf K_U^2\), \(\mathsf T_U=\operatorname{Tr}\mathbf M_U^2\), and \(\mathsf C_U=\operatorname{Tr}(\mathbf Z_U^2F)\). |                   |                              |
| **PROVED**      | The one-copy bound gives the commutator upper bound \((C\text{-upper})\).                                                                              |                   |                              |
| **PROVED**      | The ratio gate requires the commutator lower bound \((C\text{-required})\).                                                                            |                   |                              |
| **OPEN**        | Whether any finite low-\(A\) tuple satisfies \((C\text{-required})\) and the full pointwise bound for every \(T\).                                     |                   |                              |
| **OPEN**        | \((E1_{\rm gap})\).                                                                                                                                    |                   |                              |
| **OPEN**        | The earlier all-copy gate, and therefore the full-size theorem.                                                                                        |                   |                              |
| **CONJECTURED** | None promoted.                                                                                                                                         |                   |                              |

The first new statement requiring independent verification is the exact symmetric-Bell moment formula

$$
\mathbb E_V[1+R_U(T_V)]
=
\frac{
m^4B_0(D,\alpha)
+2(D+2)\mathsf I_U
+2(D+1)\mathsf T_U
-2\mathsf C_U
}{
m^3\alpha D(D+1)(D+3)
}.
$$

The first unresolved mathematical requirement is the lower bound \((C\text{-required})\) on the same-tuple commutator invariant.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-04-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-04-local-audit.md bytes=7496 sha256=12bf33fa0f89db938a8f2ebb8533fb0a6ede7c83c154e88a23db9bfd14d9d073 -->

# Round 4 local audit

Date: 2026-09-12

Status: equation-level local audit completed. This is not an independent external review.

## Verdict

The response is correct on the three headline points:

    Haar-LB / HC novelty: REDUNDANT.
    Fixed-spectrum independent-local-Haar second-moment route: NO-GO PROVED.
    (E1_gap): OPEN WITH EARLIEST GAP.

The symmetric-Bell fourth-moment calculation is a real advance: it exposes a
same-tuple invariant that disappears under independent local twirling. It does
not construct an admissible tuple or give a universal violation, so neither the
finite r=2 gate nor the earlier all-copy gate is closed.

One local strengthening was missed by the response. Because the multiset
A_U consists specifically of all pair differences U_b^* U_a, rather than an
arbitrary adjoint-closed unitary multiset, its invariant C_U is automatically
nonnegative and has an exact random-unitary mixing-energy representation. This
is the most useful input for the next round.

## Capture and status ledger

| Item | Local status | Meaning |
|---|---|---|
| Browser response capture | VERIFIED | Saved Markdown is byte-for-byte identical to the browser Copy-response payload. |
| Browser payload SHA-256 | VERIFIED | 854e4a917ed52f528a9d0b0c06d5dd12d7fdbeccc2412b3261b1037a19e81736 |
| Haar-LB / HC redundancy | VERIFIED | The rank-one Haar average dominates throughout the feasible low-A regime. |
| Fixed-spectrum formulas SD1 and SD2 | VERIFIED | Twirl coefficients, ratio of expectations, derivative, and rank-one endpoint are correct. |
| Symmetric-Bell moment C.7 and C.8 | VERIFIED | The H-fixed sector splits into the [4] and [2,2] components with the displayed weights and dimensions. |
| Generic contractions C.9 through C.11 | VERIFIED | Direct permutation contraction gives the displayed H and S sums and denominator. |
| Invariants D.4 through D.9 | VERIFIED, BUT INCOMPLETE | K_U and M_U are positive, T_U is nonnegative, and the Z_U identities are correct. Pair-difference structure yields the stronger C_U nonnegativity identity below. |
| Aggregate formulas E.1 through E.4 | VERIFIED | Coefficients of I_U, T_U, C_U, alpha, and D all check. |
| Fourth-moment upper bound F.7 | VERIFIED | It follows from the pointwise bound f_U(y)^2 <= A m f_U(y). |
| C-upper and C-required | VERIFIED | The one-copy argument gives an upper endpoint; the symmetric-Bell test gives a necessary lower endpoint. |
| Compatibility G.1 through G.3 | VERIFIED | Rearrangement and scalar relaxation are correct and do not beat PA. |
| Partial-trace sentence in F.1 | NOTATION CORRECTION | rho_T means T T^*. The displayed expression (T^*T)^T is sigma_T. Both equal I_D/D on this orbit, so F.1 remains correct. |
| (E1_gap) | OPEN | No finite tuple with a uniform all-T ratio bound and no universal violating input has been proved. |
| Full-size theorem | OPEN / CONJECTURED | The finite r=2 gate and the separate all-copy gate remain open. |

## Independent check of the symmetric-Bell moment

For

    |Omega> = D^(-1/2) sum_i |i,i>,
    |phi_V> = (V tensor V)|Omega>,

the vector |Omega>^tensor2 is invariant under the order-eight stabilizer H of
the pairing {{1,2},{3,4}}. Its overlaps with permutation operators are 1 on H
and 1/D off H. The H-fixed sector contains exactly the U(D) irreducibles [4]
and [2,2]. Their weights and dimensions are

    w_4 = (D+2)/(3D),
    w_22 = 2(D-1)/(3D),

    d_4 = D(D+1)(D+2)(D+3)/24,
    d_22 = D^2(D^2-1)/12.

Dividing weights by dimensions gives exactly

    M_D =
      8 P_4/[D^2(D+1)(D+3)]
      + 8(P_H-P_4)/[D^3(D+1)],

equivalently C.8. Enumerating the eight H contractions and all 24 S_4
contractions gives C.9 and C.10. Summation over the pair-difference multiset
then gives

    H_U = m^4(D^2+2D+alpha^2)+2 I_U+2 T_U,

    S_U =
      m^4[D^2+4D+alpha^2+2(D+4)alpha]
      +2 I_U+4 T_U+2 C_U,

and hence the exact E.4 formula. A separate D=3, m=4 Haar spot-check agreed
with E.4 within Monte Carlo standard error; the verification above is algebraic
and does not rely on that numerical check.

## Independent check of the invariant identities

Let

    R_U = sum_v U_v tensor conjugate(U_v),
    K_U = R_U^* R_U
        = sum_A A tensor conjugate(A).

Then K_U is positive, Tr K_U=m^2 alpha, and

    I_U = Tr(K_U^2) >= m^4 alpha^2/D^2.

For

    M_U = sum_A Tr(A) A^*,

adjoint closure makes M_U Hermitian. For every unit vector x,

    <x,M_U x> = Tr(G_HS G_x) >= 0,

where both matrices are Gram matrices. Thus M_U is positive,

    Tr M_U=m^2 alpha,
    T_U=Tr(M_U^2) >= m^4 alpha^2/D.

Finally,

    Z_U=sum_A A tensor A^*

is Hermitian and commutes with swap F. The identities

    Tr(Z_U^2)=I_U,
    Tr(Z_U^2 F)=C_U

are exact, hence C_U is real and |C_U|<=I_U.

## Stronger identity forced by pair-difference structure

Define the random-unitary channel and its centered part by

    L(X)=m^(-1) sum_v U_v X U_v^*,
    Q=L-Delta_D,
    Delta_D(X)=Tr(X) I_D/D.

For X_ab=U_b^*U_a, cyclicity gives

    sum_(v,w) Tr(
      U_w^*U_v X_ab U_v^*U_w X_ab^*
    )
      = m^2 ||L(X_ab)||_2^2.

Summing over a,b proves the exact identity

    C_U
      = m^2 sum_(a,b) ||L(U_b^*U_a)||_2^2
      = m^4 alpha/D
        + m^2 sum_(a,b) ||Q(U_b^*U_a)||_2^2
      >= m^4 alpha/D
      >= 0.                                      (Pair-energy)

The second equality uses Hilbert-Schmidt orthogonality of the scalar and
traceless parts and

    sum_(a,b) |Tr(U_b^*U_a)|^2 = m^2 alpha.

There is also an exact aggregate commutator-defect form. For unitary A,B,

    Re Tr(A B A^* B^*)
      = D - (1/2)||A B^* - B^* A||_2^2.

Because the multiset is adjoint closed and C_U is real,

    C_U
      = m^4 D
        - (1/2) sum_(A,B in A_U) ||A B-B A||_2^2. (Comm-defect)

Thus the lower bound C-required demands that the full pair-difference family be
sufficiently close to commuting in aggregate, while the low one-copy purity
demands strong mixing. Quantifying that tension is a sharper formulation of the
remaining route than treating C_U as an unconstrained real scalar.

## Check of the endpoints

The exact symmetric-Bell formula is

    E_V[1+R_U(T_V)]
      = [
          m^4 B_0(D,alpha)
          +2(D+2) I_U
          +2(D+1) T_U
          -2 C_U
        ]
        /[
          m^3 alpha D(D+1)(D+3)
        ].

Therefore an all-T bound implies C-required with the direction shown in the
response. The pure-state fourth moment gives C-upper with the opposite
direction. Requiring the endpoints to coexist yields G.1. Substituting the
dimension lower bounds for I_U and T_U gives G.2, and direct expansion gives
the factorization G.3. Its sign is nonnegative on D<alpha<=D^2, so this scalar
relaxation is already implied by PA.

The response did not exploit Pair-energy, Comm-defect, or even its own
C_U<=I_U in the endpoint analysis. Their scalar relaxations alone may still be
redundant, but the exact pair-difference identities add structure that must be
used before declaring the commutator interval irreducible.

## Remaining boundary

The safe current status is

    (E1_gap): OPEN.
    finite r=2 low-A gate: OPEN.
    earlier all-copy gate: OPEN.
    full-size finite-dimensional MOE/Holevo theorem: OPEN / CONJECTURED.

The next audit should reformulate I_U, T_U, and C_U through L, Q, and
Phi=L^*L, then seek a quantitative incompatibility between low output purity
and the near-commutativity demanded by C-required. Passing only the averaged
symmetric-Bell test would still not prove the uniform supremum over all T.


<!-- END HISTORICAL FILE path=outputs/round-04-local-audit.md -->


# ROUND 005

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-05-prompt.md bytes=7842 sha256=f1cf0251fa40d710af379bf223251ce6cf38cfc8c3830cddb7dc558a3abe26b1 -->

# Round 5 — exploit pair-difference positivity and the mixing–commutation tension

Continue in the same deterministic one-layer setup. This is an adversarial
proof round focused only on the finite r=2 low-A gate.

Let finite m,D, eta>0 and one frozen tuple

    U=(U_1,...,U_m) in U(D)^m

define

    C(X)_(v,w)=m^(-1) Tr(X U_w^*U_v),
    L(X)=m^(-1) sum_v U_v X U_v^*,
    Q=L-Delta_D,
    Delta_D(X)=Tr(X) I_D/D,

    A=1+9(1+eta)^2/m,
    p=sup_rho ||C(rho)||_2^2,

with

    ln m>18,
    A^2<m^(1/m),
    p<=A/m.

For every Hilbert--Schmidt unit T, retain the audited definitions of d_T,
R_U(T), and kappa_1(U). The target remains

    (E1_gap): kappa_1(U)<=A-1

for one finite tuple satisfying all conditions above.

No broad MOE/Holevo blueprint is requested. Give a public, self-contained
derivation and no hidden chain-of-thought.

## Audited input from Round 4

Let

    A_vw=U_w^*U_v,
    alpha=||C(I_D)||_2^2
         =m^(-2) sum_(v,w)|Tr A_vw|^2,

and let A_U be the multiset of all m^2 matrices A_vw. Define

    I_U=sum_(A,B in A_U)|Tr(AB)|^2,

    T_U=sum_(A,B in A_U)
          Tr(A) Tr(B) overline{Tr(AB)},

    C_U=sum_(A,B in A_U) Tr(ABA^*B^*).

The following facts received an equation-level local audit:

    I_U=Tr(K_U^2),       K_U=sum_A A tensor conjugate(A) >=0,
    I_U>=m^4 alpha^2/D^2,

    T_U=Tr(M_U^2),       M_U=sum_A Tr(A)A^* >=0,
    T_U>=m^4 alpha^2/D,

    C_U=Tr(Z_U^2 F),     Z_U=sum_A A tensor A^*,
    |C_U|<=I_U.

For the symmetric-Bell orbit T_V=VV^T/sqrt(D), the exact average is

    E_V[1+R_U(T_V)]
      =[
          m^4 B_0(D,alpha)
          +2(D+2)I_U
          +2(D+1)T_U
          -2C_U
        ]
       /[
          m^3 alpha D(D+1)(D+3)
        ],                                           (SB)

where

    B_0(D,alpha)
      =D(D^2+4D+2)+(D+2)alpha^2-2(D+4)alpha.

Hence the ratio gate requires

    C_U >=
      (D+2)I_U+(D+1)T_U
      +(m^4/2)B_0(D,alpha)
      -(A m^3 alpha D(D+1)(D+3))/2.                 (C-required)

The pure-state fourth moment gives the opposite endpoint

    C_U <= (1/2)[
      A m^3(alpha+D)(D+2)(D+3)
      -m^4(D^2+4D+alpha^2+2(D+4)alpha)
      -2I_U-4T_U
    ].                                               (C-upper)

Combining these endpoints gives a valid compatibility condition, but replacing
I_U and T_U only by their dimension lower bounds produces no contradiction
beyond

    m(alpha+D)<=A D(D+1).                            (PA)

Round 4 also correctly proved that Haar-LB and its scalar HC condition are
redundant, and that every fixed-Schmidt-spectrum independent-local-Haar
second-moment ratio is maximized at the rank-one boundary.

There is one harmless notation slip to correct: rho_T=TT^*, whereas
(T^*T)^T is sigma_T. For T_V both equal I_D/D, so the flat partial-trace
conclusion remains correct.

## Stronger pair-difference identity to audit first

Round 4 treated C_U only as a real scalar satisfying |C_U|<=I_U. The special
pair-difference structure appears to imply much more.

For X_ab=U_b^*U_a, cyclicity gives the candidate exact identity

    sum_(v,w)
      Tr(
        U_w^*U_v X_ab U_v^*U_w X_ab^*
      )
      =m^2 ||L(X_ab)||_2^2.

Therefore

    C_U
      =m^2 sum_(a,b)||L(U_b^*U_a)||_2^2
      =m^4 alpha/D
       +m^2 sum_(a,b)||Q(U_b^*U_a)||_2^2
      >=m^4 alpha/D>=0.                             (Pair-energy)

Independently verify every adjoint, index, factor of m, and the scalar/traceless
orthogonality. If false, give the exact corrected formula. If true, explicitly
strengthen the Round 4 ledger: C_U is nonnegative for this pair-difference
multiset, not merely real.

There is also a candidate aggregate defect identity. For unitary A,B,

    Re Tr(ABA^*B^*)
      =D-(1/2)||AB^*-B^*A||_2^2.

Using adjoint closure of A_U should give

    C_U
      =m^4D
       -(1/2)sum_(A,B in A_U)||AB-BA||_2^2.          (Comm-defect)

Audit this carefully. If correct, C-required is an explicit upper bound on the
total noncommutativity of the entire pair-difference family, while p<=A/m
demands strong mixing.

## Operator reformulation that must use the same tuple

Set

    Phi=L^*L
       =m^(-2) sum_(a,b) Ad_(U_b^*U_a).

Derive a precise, convention-fixed dictionary expressing alpha, I_U, T_U, and
C_U through the Liouville matrix, Choi matrix, realignment/partial transpose,
and marginals of this single positive Hilbert--Schmidt superoperator Phi.
Do not guess a reshuffling: show indices and all m powers.

In particular, determine whether Pair-energy can be written as a positive
overlap between the Choi and Liouville representations of Phi, and identify
the exact representation of T_U. The purpose is to expose constraints that
are lost when A_U is replaced by a generic adjoint-closed multiset.

For a pure state rho_y, complementary-output spectra give

    ||L(rho_y)||_2^2=||C(rho_y)||_2^2<=A/m.

Thus, with

    epsilon=A/m-1/D,

one has the pointwise centered bound

    ||Q(rho_y)||_2^2<=epsilon                    (Pure-Q)

for every unit y. Use this and complete positivity, unitality, trace
preservation, and Phi=L^*L to control the quantities in Pair-energy or
Comm-defect. A generic unrestricted 2-to-2 or cb bound is inadmissible.

## Exact tasks

1. Give one verdict on (E1_gap): PROVED, DISPROVED, or OPEN WITH EARLIEST
   GAP. A conditional reduction or an averaged test is not a proof.

2. Audit Pair-energy and Comm-defect from first principles. Then rewrite
   C-required exactly both as:
   - a required lower bound on
     sum_(a,b)||Q(U_b^*U_a)||_2^2; and
   - a required upper bound on
     sum_(A,B)||[A,B]||_2^2.

3. Before claiming novelty, exhaust the immediate exact combinations:

       C-required with C_U<=I_U,
       C-required with C_U<=m^4D,
       C-upper with Pair-energy,
       C-upper with C_U>=0.

   For each, keep I_U and T_U exact first. If a scalar relaxation is already
   implied by PA, prove the factorization and label it REDUNDANT.

4. Then attack the genuine same-tuple problem. Prove either:

   (a) low output purity forces enough aggregate noncommutativity to violate
       C-required, thereby disproving (E1_gap); or

   (b) one explicit finite low-A tuple satisfies the full uniform all-T ratio
       bound, thereby proving (E1_gap).

   The tuple must be fixed before the supremum and all constants must be
   explicit.

5. If neither closure is possible, prove one new deterministic lemma that
   materially narrows the gap and genuinely uses A_vw=U_w^*U_v or
   Phi=L^*L. Acceptable forms include a nontrivial bound

       sum_(a,b)||Q(U_b^*U_a)||_2^2
         <= F(m,D,A,alpha,I_U,T_U),

   or

       sum_(A,B)||[A,B]||_2^2
         >= G(m,D,A,alpha,I_U,T_U),

   derived from Pure-Q and the same frozen tuple. It must be stronger than a
   generic norm bound and must shrink the exact C interval for some feasible
   low-A parameters.

   A mere dictionary, nonnegativity of C_U, a scalar relaxation already
   implied by PA, or a restatement of C-required does not count as the new
   lemma.

6. If the route remains open, isolate the first exact operator inequality
   needed to convert Pure-Q into control of Pair-energy or Comm-defect. State
   its quantifiers and whether it is proved, disproved, or conjectured. Do not
   call generic failure to find a bound a theorem.

7. Do not use independent copies of the tuple, fresh channel randomness,
   unrestricted cb/2-to-2 bounds, real/orthogonal substitution, the full Weyl
   loophole, numerical evidence, WHGAP, or orientation-insensitive estimates
   that also apply unchanged to C tensor conjugate(C).

8. End with an audit ledger separating PROVED, DISPROVED, REDUNDANT, OPEN, and
   CONJECTURED. Identify the first new statement requiring independent
   verification.

The full-size theorem remains OPEN unless both (E1_gap) and the earlier
all-copy gate are separately closed.

<!-- END HISTORICAL FILE path=work/round-05-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-05-response.md bytes=27503 sha256=c6a8e3a2471dfbfe276e38c94a6a8c77daca0db64cfb3653545aac011d63f4bb -->

# Verdict

$$
\boxed{\text{\((E1_{\mathrm{gap}})\) remains OPEN WITH EARLIEST GAP.}}
$$

The two proposed pair-difference identities are correct:

$$
\boxed{
\mathsf C_U
=
m^2\sum_{a,b}\|L(U_b^*U_a)\|_2^2
=
\frac{m^4\alpha}{D}
+
m^2\sum_{a,b}\|Q(U_b^*U_a)\|_2^2
\ge0,
}
$$

and

$$
\boxed{
\mathsf C_U
=
m^4D-\frac12
\sum_{A,B\in\mathcal A_U}\|[A,B]\|_2^2.
}
$$

Thus Round 4’s ledger should be strengthened: for this pair-difference multiset, \(\mathsf C_U\) is not merely real; it is nonnegative and is a positive Choi–Liouville overlap.

Two new deterministic bounds are proved:

1. **Mixing–marginal squeeze**

   $$
   \boxed{
   \frac{m^4\alpha^2}{D}
   \le \mathsf T_U
   \le
   m^4\alpha\sqrt{\alpha p}
   \le
   \sqrt A\,\frac{m^4\alpha^2}{D}.
   }
   \tag{MM}
   $$

   Thus, in the low-\(A\) regime, \(\mathsf T_U\) is forced to lie within a factor \(\sqrt A\) of its dimension-minimal value.

2. **Choi–Liouville alignment bound**

   $$
   \boxed{
   \sum_{a,b}\|Q(U_b^*U_a)\|_2^2
   \le
   \frac1{m^2}
   \sqrt{
   \left(
   \mathsf I_U-\frac{2\mathsf T_U}{D}
   +\frac{m^4\alpha^2}{D^2}
   \right)
   \left(\mathsf I_U-m^4\right)
   }.
   }
   \tag{Align-Q}
   $$

Equivalently,

$$
\boxed{
\begin{aligned}
\sum_{A,B\in\mathcal A_U}\|[A,B]\|_2^2
\ge{}&
2m^4\left(D-\frac{\alpha}{D}\right)\\
&-
2\sqrt{
\left(
\mathsf I_U-\frac{2\mathsf T_U}{D}
+\frac{m^4\alpha^2}{D^2}
\right)
\left(\mathsf I_U-m^4\right)
}.
\end{aligned}
}
\tag{Align-comm}
$$

This strictly improves the generic bound obtained from \(\mathsf C_U\le\mathsf I_U\) throughout the low-\(A\) feasible regime.

It still does not force a contradiction with \((C\text{-required})\). The first remaining uncontrolled quantity is the alignment between the traceless Liouville part of \(\Phi=L^*L\) and the corresponding traceless block of its Choi matrix.

---

# 1. Pair-energy identity

Let

$$
A_{vw}=U_w^*U_v,\qquad X_{ab}=U_b^*U_a.
$$

For an arbitrary \(X\in M_D\),

$$
L(X)=\frac1m\sum_vU_vXU_v^*.
$$

Therefore

$$
\begin{aligned}
m^2\|L(X)\|_2^2
&=
\sum_{v,w}
\operatorname{Tr}
\left[
(U_vXU_v^*)^*
(U_wXU_w^*)
\right]\\
&=
\sum_{v,w}
\operatorname{Tr}
\left[
U_vX^*U_v^*U_wXU_w^*
\right].
\end{aligned}
$$

Rename \(v\leftrightarrow w\) and cyclically permute the trace:

$$
\begin{aligned}
m^2\|L(X)\|_2^2
&=
\sum_{v,w}
\operatorname{Tr}
\left[
U_w^*U_vXU_v^*U_wX^*
\right]\\
&=
\sum_{v,w}
\operatorname{Tr}
\left[
A_{vw}XA_{vw}^*X^*
\right].
\end{aligned}
\tag{1.1}
$$

Taking \(X=X_{ab}\) and summing over \(a,b\) gives

$$
\begin{aligned}
\mathsf C_U
&=
\sum_{v,w,a,b}
\operatorname{Tr}
\left[
A_{vw}X_{ab}A_{vw}^*X_{ab}^*
\right]\\
&=
\boxed{
m^2\sum_{a,b}\|L(X_{ab})\|_2^2.
}
\end{aligned}
\tag{1.2}
$$

All indices and factors of \(m\) in the proposed identity are correct.

## 1.1 Scalar/traceless decomposition

Since

$$
L(X)=\frac{\operatorname{Tr}X}{D}I_D+Q(X)
$$

and \(Q\) is trace-annihilating,

$$
\left\langle
\frac{\operatorname{Tr}X}{D}I_D,
Q(X)
\right\rangle_{\mathrm{HS}}
=
\frac{\overline{\operatorname{Tr}X}}D
\operatorname{Tr}Q(X)
=0.
$$

Thus

$$
\|L(X)\|_2^2
=
\frac{|\operatorname{Tr}X|^2}{D}
+
\|Q(X)\|_2^2.
\tag{1.3}
$$

Because

$$
\sum_{a,b}
|\operatorname{Tr}X_{ab}|^2=m^2\alpha,
$$

equations (1.2)–(1.3) imply

$$
\boxed{
\mathsf C_U
=
\frac{m^4\alpha}{D}
+
m^2\Theta_Q,
}
\tag{Pair-energy}
$$

where

$$
\Theta_Q:=
\sum_{a,b}
\|Q(U_b^*U_a)\|_2^2.
\tag{1.4}
$$

In particular,

$$
\boxed{
\mathsf C_U\ge\frac{m^4\alpha}{D}\ge0.
}
\tag{1.5}
$$

---

# 2. Commutator-defect identity

For unitary \(A,B\),

$$
\begin{aligned}
\|AB^*-B^*A\|_2^2
={}&
\operatorname{Tr}
\left[
(BA^*-A^*B)(AB^*-B^*A)
\right]\\
={}&
2D-
\operatorname{Tr}(BA^*B^*A)
-
\operatorname{Tr}(A^*BAB^*).
\end{aligned}
$$

The last two terms are complex conjugates, and cyclicity gives

$$
\operatorname{Tr}(BA^*B^*A)
=
\operatorname{Tr}(ABA^*B^*).
$$

Hence

$$
\boxed{
\operatorname{Re}\operatorname{Tr}(ABA^*B^*)
=
D-\frac12\|AB^*-B^*A\|_2^2.
}
\tag{2.1}
$$

The ordered sum

$$
\sum_{A,B}\operatorname{Tr}(ABA^*B^*)
$$

is real because interchanging \(A\) and \(B\) conjugates each summand.

The multiset \(\mathcal A_U\) is closed under adjoint with multiplicities. Replacing \(B^*\) by a new variable \(B\) therefore gives

$$
\sum_{A,B\in\mathcal A_U}
\|AB^*-B^*A\|_2^2
=
\sum_{A,B\in\mathcal A_U}
\|AB-BA\|_2^2.
$$

There are \(m^4\) ordered pairs \((A,B)\). Summing (2.1) proves

$$
\boxed{
\mathsf C_U
=
m^4D-\frac12
\sum_{A,B\in\mathcal A_U}
\|[A,B]\|_2^2.
}
\tag{Comm-defect}
$$

Thus the two interpretations are exactly equivalent:

$$
m^2\Theta_Q+\frac{m^4\alpha}{D}
=
m^4D-\frac12\sum_{A,B}\|[A,B]\|_2^2.
\tag{2.2}
$$

---

# 3. Rewriting the symmetric-Bell requirement

Define

$$
\begin{aligned}
\mathcal C_{\mathrm{req}}
:={}&
(D+2)\mathsf I_U
+
(D+1)\mathsf T_U\\
&+
\frac{m^4}{2}B_0(D,\alpha)
-
\frac{
A m^3\alpha D(D+1)(D+3)
}{2}.
\end{aligned}
\tag{3.1}
$$

Round 4’s symmetric-Bell necessary condition is

$$
\mathsf C_U\ge\mathcal C_{\mathrm{req}}.
\tag{3.2}
$$

## 3.1 Required lower bound on pair energy

Using Pair-energy,

$$
\boxed{
\Theta_Q
\ge
\Theta_{\mathrm{req}}
:=
\frac{
\mathcal C_{\mathrm{req}}
-\dfrac{m^4\alpha}{D}
}{m^2}.
}
\tag{3.3}
$$

Explicitly,

$$
\boxed{
\begin{aligned}
\Theta_Q\ge\frac1{m^2}\Bigg[
&(D+2)\mathsf I_U
+(D+1)\mathsf T_U\\
&+\frac{m^4}{2}B_0(D,\alpha)
-\frac{
A m^3\alpha D(D+1)(D+3)
}{2}
-\frac{m^4\alpha}{D}
\Bigg].
\end{aligned}
}
\tag{Q-required}
$$

## 3.2 Required upper bound on aggregate noncommutativity

Using Comm-defect,

$$
\boxed{
\begin{aligned}
\sum_{A,B\in\mathcal A_U}\|[A,B]\|_2^2
\le{}&
2m^4D
-
2(D+2)\mathsf I_U\\
&-
2(D+1)\mathsf T_U
-
m^4B_0(D,\alpha)\\
&+
A m^3\alpha D(D+1)(D+3).
\end{aligned}
}
\tag{Comm-required}
$$

Thus the symmetric-Bell gate asks the pair-difference family to be sufficiently close to commuting in this aggregate sense.

---

# 4. Convention-fixed operator dictionary

Use column vectorization

$$
|X\rangle\rangle
=
\sum_i|i\rangle\otimes X|i\rangle.
$$

Then

$$
(M\otimes N)|X\rangle\rangle
=
|NXM^{\mathsf T}\rangle\rangle.
\tag{4.1}
$$

Let

$$
\Phi=L^*L.
$$

Because

$$
L^*(Y)=\frac1m\sum_bU_b^*YU_b,
$$

one has

$$
\boxed{
\Phi(X)
=
\frac1{m^2}\sum_{a,b}
A_{ab}XA_{ab}^*,
\qquad
A_{ab}=U_b^*U_a.
}
\tag{4.2}
$$

## 4.1 Liouville and Choi matrices

Define the Liouville matrix \(S_\Phi\) by

$$
|\Phi(X)\rangle\rangle
=
S_\Phi|X\rangle\rangle.
$$

Then

$$
\boxed{
S_\Phi
=
\frac1{m^2}
\sum_{A\in\mathcal A_U}
\overline A\otimes A.
}
\tag{4.3}
$$

The unnormalized Choi matrix is

$$
J_\Phi
=
\sum_{r,s}
|r\rangle\langle s|
\otimes\Phi(E_{rs}),
$$

and therefore

$$
\boxed{
J_\Phi
=
\frac1{m^2}
\sum_{A\in\mathcal A_U}
|A\rangle\rangle\langle\langle A|.
}
\tag{4.4}
$$

Both are positive semidefinite:

$$
J_\Phi\succeq0,
\qquad
S_\Phi=S_L^*S_L\succeq0.
$$

Because \(\Phi\) is trace-preserving and unital,

$$
\operatorname{Tr}_1J_\Phi
=
\operatorname{Tr}_2J_\Phi
=
I_D.
\tag{4.5}
$$

## 4.2 Exact realignment convention

Since

$$
|E_{rs}\rangle\rangle=|s\rangle\otimes|r\rangle,
$$

the matrix entries satisfy

$$
\left[S_\Phi\right]_{(l,k),(s,r)}
=
\left[J_\Phi\right]_{(r,k),(s,l)}.
\tag{4.6}
$$

Thus \(S_\Phi\) is the explicit realignment of \(J_\Phi\) given by (4.6). This is an entry permutation, so

$$
\|S_\Phi\|_2=\|J_\Phi\|_2.
$$

## 4.3 The four invariants

Let \(|I\rangle\rangle\) denote the unnormalized maximally entangled vector.

### Alpha

$$
\boxed{
\alpha
=
\operatorname{Tr}S_\Phi
=
\langle\langle I|J_\Phi|I\rangle\rangle.
}
\tag{4.7}
$$

### \(\mathsf I_U\)

Directly from (4.3),

$$
\operatorname{Tr}S_\Phi^2
=
\frac1{m^4}
\sum_{A,B}|\operatorname{Tr}(AB)|^2.
$$

Hence

$$
\boxed{
\mathsf I_U
=
m^4\operatorname{Tr}S_\Phi^2
=
m^4\operatorname{Tr}J_\Phi^2.
}
\tag{4.8}
$$

### \(\mathsf T_U\)

Define

$$
M_U
=
\sum_{A\in\mathcal A_U}\operatorname{Tr}(A)A^*.
$$

Adjoint closure also gives

$$
M_U
=
\sum_A\overline{\operatorname{Tr}A}\,A.
\tag{4.9}
$$

Then

$$
\boxed{
J_\Phi|I\rangle\rangle
=
\frac1{m^2}|M_U\rangle\rangle.
}
\tag{4.10}
$$

Moreover,

$$
\boxed{
\operatorname{Tr}_1S_\Phi
=
\frac{M_U}{m^2},
\qquad
\operatorname{Tr}_2S_\Phi
=
\frac{M_U^{\mathsf T}}{m^2}.
}
\tag{4.11}
$$

Consequently,

$$
\boxed{
\begin{aligned}
\mathsf T_U
&=
\operatorname{Tr}M_U^2\\
&=
m^4
\langle\langle I|J_\Phi^2|I\rangle\rangle\\
&=
m^4
\operatorname{Tr}
\left[
(\operatorname{Tr}_1S_\Phi)^2
\right].
\end{aligned}
}
\tag{4.12}
$$

### \(\mathsf C_U\)

Using (4.3)–(4.4),

$$
\begin{aligned}
m^4\operatorname{Tr}(J_\Phi S_\Phi)
&=
\sum_{A,B}
\langle\langle A|
(\overline B\otimes B)
|A\rangle\rangle\\
&=
\sum_{A,B}
\operatorname{Tr}(A^*BAB^*).
\end{aligned}
$$

Replacing \(A\) by \(A^*\) gives

$$
\boxed{
\mathsf C_U
=
m^4\operatorname{Tr}(J_\Phi S_\Phi).
}
\tag{4.13}
$$

Since both \(J_\Phi\) and \(S_\Phi\) are positive semidefinite,

$$
\operatorname{Tr}(J_\Phi S_\Phi)\ge0.
$$

This gives a second proof of \(\mathsf C_U\ge0\).

## 4.4 Partial transpose representation

Let \(F\) denote swap. Then

$$
m^2FS_\Phi F
=
\sum_AA\otimes\overline A
=
K_U.
\tag{4.14}
$$

Taking transpose on the second tensor factor,

$$
\boxed{
Z_U
=
K_U^{\Gamma_2}
=
\sum_AA\otimes A^*.
}
\tag{4.15}
$$

Finally,

$$
\operatorname{Tr}\bigl[(AB\otimes A^*B^*)F\bigr]
=
\operatorname{Tr}(ABA^*B^*),
$$

so

$$
\boxed{
\mathsf C_U
=
\operatorname{Tr}(Z_U^2F).
}
\tag{4.16}
$$

Thus Pair-energy is exactly a positive overlap between the Choi and Liouville representations of the same \(\Phi=L^*L\):

$$
\boxed{
\frac{\mathsf C_U}{m^4}
=
\operatorname{Tr}(J_\Phi S_\Phi).
}
$$

---

# 5. Pure-\(Q\) in the same dictionary

Let

$$
P_0=\frac{|I\rangle\rangle\langle\langle I|}{D}.
$$

This is the Liouville matrix of \(\Delta_D\).

Because \(L=\Delta_D+Q\), and because

$$
Q(I)=0,
\qquad
\operatorname{Tr}Q(X)=0,
$$

the cross terms vanish:

$$
\boxed{
\Phi=L^*L
=
\Delta_D+Q^*Q.
}
\tag{5.1}
$$

Hence

$$
\boxed{
S_\Phi=P_0+S_\circ,
\qquad
S_\circ:=S_{Q^*Q}\succeq0,
\qquad
S_\circ|I\rangle\rangle=0.
}
\tag{5.2}
$$

For a pure state \(\rho_y=|y\rangle\langle y|\),

$$
\boxed{
\langle\langle\rho_y|
S_\circ
|\rho_y\rangle\rangle
=
\|Q(\rho_y)\|_2^2
\le
\epsilon,
\qquad
\epsilon=\frac Am-\frac1D.
}
\tag{5.3}
$$

Also,

$$
\begin{aligned}
\langle\langle\rho_y|
J_\Phi
|\rho_y\rangle\rangle
&=
\frac1{m^2}
\sum_A
|\langle y|A|y\rangle|^2\\
&=
\|C(\rho_y)\|_2^2\\
&=
\|L(\rho_y)\|_2^2\\
&=
\langle\langle\rho_y|
S_\Phi
|\rho_y\rangle\rangle.
\end{aligned}
\tag{5.4}
$$

Thus \(J_\Phi\) and its realignment \(S_\Phi\) agree on the quadratic Veronese set of vectorized rank-one projectors. They need not agree on entangled directions in Hilbert–Schmidt space.

---

# 6. Immediate exact combinations

Define the Round 4 upper endpoint

$$
\boxed{
\begin{aligned}
\mathcal C_{\mathrm{up}}
:=\frac12\Big[
&A m^3(\alpha+D)(D+2)(D+3)\\
&-
m^4\bigl(
D^2+4D+\alpha^2+2(D+4)\alpha
\bigr)\\
&-
2\mathsf I_U
-
4\mathsf T_U
\Big].
\end{aligned}
}
\tag{6.1}
$$

Then

$$
\mathcal C_{\mathrm{req}}
\le\mathsf C_U
\le\mathcal C_{\mathrm{up}}.
$$

## 6.1 \(C\)-required with \(\mathsf C_U\le\mathsf I_U\)

The exact necessary condition is

$$
\boxed{
\begin{aligned}
0\ge\mathcal E_I:={}&
(D+1)(\mathsf I_U+\mathsf T_U)\\
&+
\frac{m^4}{2}B_0(D,\alpha)\\
&-
\frac{
A m^3\alpha D(D+1)(D+3)
}{2}.
\end{aligned}
}
\tag{6.2}
$$

## 6.2 \(C\)-required with \(\mathsf C_U\le m^4D\)

The exact necessary condition is

$$
\boxed{
\begin{aligned}
0\ge\mathcal E_D:={}&
(D+2)\mathsf I_U
+
(D+1)\mathsf T_U\\
&+
\frac{m^4}{2}B_0(D,\alpha)\\
&-
\frac{
A m^3\alpha D(D+1)(D+3)
}{2}
-
m^4D.
\end{aligned}
}
\tag{6.3}
$$

## 6.3 \(C\)-upper with Pair-energy

Using \(\mathsf C_U=m^4\alpha/D+m^2\Theta_Q\),

$$
\boxed{
\Theta_Q
\le
\frac{
\mathcal C_{\mathrm{up}}
-\dfrac{m^4\alpha}{D}
}{m^2}.
}
\tag{6.4}
$$

This remains a nontrivial exact invariant inequality.

## 6.4 \(C\)-upper with \(\mathsf C_U\ge0\)

The exact necessary condition is simply

$$
\boxed{\mathcal C_{\mathrm{up}}\ge0.}
\tag{6.5}
$$

---

# 7. The four scalar relaxations are redundant with PA

Let

$$
\mathsf I_0=\frac{m^4\alpha^2}{D^2},
\qquad
\mathsf T_0=\frac{m^4\alpha^2}{D},
$$

and define

$$
A_0
=
\frac{m(\alpha+D)}{D(D+1)}.
$$

The pure-state average inequality is exactly

$$
A\ge A_0.
$$

Set the PA slack

$$
s:=AD(D+1)-m(\alpha+D)\ge0.
\tag{7.1}
$$

In the low-\(A\) feasible regime,

$$
D<\alpha<D^2.
\tag{7.2}
$$

## 7.1 Scalar relaxation of \(\mathcal E_I\)

Let

$$
x=\frac{\alpha-D}{D^2-D}\in(0,1).
$$

After replacing \(\mathsf I_U,\mathsf T_U\) by
\(\mathsf I_0,\mathsf T_0\),

$$
\begin{aligned}
\mathcal E_I^{(0)}
={}&
\frac{m^4(D-1)}2
\Big[
-2\bigl((1-x)+Dx\bigr)\\
&\qquad
-(D-1)(D^2+4D+2)x(1-x)
\Big]\\
&-
\frac{m^3\alpha(D+3)}2\,s.
\end{aligned}
\tag{7.3}
$$

Every term on the right is nonpositive. Thus this scalar relaxation is already implied by PA.

## 7.2 Scalar relaxation of \(\mathcal E_D\)

One obtains

$$
\boxed{
\begin{aligned}
\mathcal E_D^{(0)}
={}&
\frac{m^4}{2D^2}
(\alpha-D^2)
\left[
\alpha(D+2)^2-D^2(D+4)
\right]\\
&-
\frac{m^3\alpha(D+3)}2\,s.
\end{aligned}
}
\tag{7.4}
$$

For \(\alpha\ge D\),

$$
\alpha(D+2)^2-D^2(D+4)
\ge4D>0,
$$

while \(\alpha-D^2\le0\). Hence this relaxation is also implied by PA.

## 7.3 Scalar relaxation of Pair-energy versus \(C\)-upper

Replacing \(\mathsf I_U,\mathsf T_U\) by their dimension lower bounds gives

$$
\boxed{
\begin{aligned}
\mathcal C_{\mathrm{up}}^{(0)}
-\frac{m^4\alpha}{D}
={}&
\frac{
m^4(D+\alpha)(D^2-\alpha)
}{
D^2(D+1)
}\\
&+
\frac{
m^3(\alpha+D)(D+2)(D+3)
}{
2D(D+1)
}s
\ge0.
\end{aligned}
}
\tag{7.5}
$$

So Pair-energy nonnegativity produces no new scalar contradiction beyond PA.

## 7.4 Scalar relaxation of \(C\)-upper with \(\mathsf C_U\ge0\)

Similarly,

$$
\boxed{
\begin{aligned}
\mathcal C_{\mathrm{up}}^{(0)}
={}&
\frac{
m^4(D^3+2D^2\alpha-\alpha^2)
}{
D^2(D+1)
}\\
&+
\frac{
m^3(\alpha+D)(D+2)(D+3)
}{
2D(D+1)
}s.
\end{aligned}
}
\tag{7.6}
$$

The quadratic

$$
D^3+2D^2\alpha-\alpha^2
$$

is positive at both endpoints \(\alpha=D\) and \(\alpha=D^2\), and it is concave in \(\alpha\). It is therefore positive throughout \([D,D^2]\).

Hence all four **dimension-only scalar relaxations** are REDUNDANT with PA. The exact inequalities retaining \(\mathsf I_U,\mathsf T_U\) are not redundant.

---

# 8. New lemma I: mixing forces \(\mathsf T_U\) near its minimum

Define the two \(m\times m\) Gram matrices

$$
H_{ab}
=
\operatorname{Tr}(U_a^*U_b),
\qquad
G_y(a,b)
=
\langle y|U_a^*U_b|y\rangle.
$$

Both \(H\) and \(G_y\) are positive semidefinite.

From the definitions,

$$
\|H\|_2^2=m^2\alpha,
\tag{8.1}
$$

and

$$
\|G_y\|_2^2
=
m^2\|C(\rho_y)\|_2^2
\le m^2p.
\tag{8.2}
$$

For \(M_U=\sum_A\operatorname{Tr}(A)A^*\),

$$
\begin{aligned}
\langle y|M_U|y\rangle
&=
\sum_{a,b}
\operatorname{Tr}(U_b^*U_a)
\langle y|U_a^*U_b|y\rangle\\
&=
\operatorname{Tr}(HG_y).
\end{aligned}
\tag{8.3}
$$

Hilbert–Schmidt Cauchy–Schwarz gives

$$
\operatorname{Tr}(HG_y)
\le
\|H\|_2\|G_y\|_2
\le
m^2\sqrt{\alpha p}.
$$

Since this holds for every unit \(y\),

$$
\boxed{
0\preceq M_U
\preceq
m^2\sqrt{\alpha p}\,I_D.
}
\tag{8.4}
$$

Also,

$$
\operatorname{Tr}M_U=m^2\alpha.
\tag{8.5}
$$

For a positive operator bounded above by \(cI\),

$$
M_U^2\preceq cM_U.
$$

Taking traces,

$$
\boxed{
\mathsf T_U
=
\operatorname{Tr}M_U^2
\le
m^4\alpha\sqrt{\alpha p}.
}
\tag{8.6}
$$

The dimension lower bound gives

$$
\mathsf T_U
\ge
\frac{(\operatorname{Tr}M_U)^2}{D}
=
\frac{m^4\alpha^2}{D}.
$$

Therefore

$$
\boxed{
1
\le
\frac{\mathsf T_U}{m^4\alpha^2/D}
\le
D\sqrt{\frac p\alpha}
\le
\sqrt{\frac{AD^2}{m\alpha}}
\le
\sqrt A.
}
\tag{8.7}
$$

The last inequality uses

$$
\alpha\ge\frac{D^2}{m}.
$$

Hence

$$
\boxed{
\frac{m^4\alpha^2}{D}
\le
\mathsf T_U
\le
\sqrt A\,
\frac{m^4\alpha^2}{D}.
}
\tag{MM}
$$

Equivalently, if

$$
\overline\mu=\frac{m^2\alpha}{D},
$$

then

$$
\boxed{
\left\|
M_U-\overline\mu I_D
\right\|_2^2
=
\mathsf T_U-\frac{m^4\alpha^2}{D}
\le
\frac{m^4\alpha^2}{D}(\sqrt A-1).
}
\tag{8.8}
$$

Because \(A^2<m^{1/m}\), the multiplicative slack \(\sqrt A-1\) is extremely small. This is a genuine same-tuple consequence of the pure-output bound.

---

# 9. New lemma II: Choi–Liouville alignment controls Pair-energy

Let

$$
e=\frac{|I\rangle\rangle}{\sqrt D},
\qquad
P_0=|e\rangle\langle e|,
\qquad
P_\perp=I-P_0.
$$

Write

$$
S_\Phi=P_0+S_\circ,
\qquad
S_\circ=P_\perp S_\Phi P_\perp\succeq0.
$$

Define the traceless Choi block

$$
B_\Phi:=P_\perp J_\Phi P_\perp\succeq0.
$$

Since \(S_\circ\) is supported on \(P_\perp\),

$$
\operatorname{Tr}(J_\Phi S_\circ)
=
\operatorname{Tr}(B_\Phi S_\circ).
\tag{9.1}
$$

From Pair-energy,

$$
\boxed{
\Theta_Q
=
m^2\operatorname{Tr}(B_\Phi S_\circ).
}
\tag{9.2}
$$

## 9.1 Purity of \(S_\circ\)

Since \(P_0S_\circ=0\),

$$
\operatorname{Tr}S_\circ^2
=
\operatorname{Tr}S_\Phi^2-1
=
\frac{\mathsf I_U-m^4}{m^4}.
\tag{9.3}
$$

## 9.2 Purity of \(B_\Phi\)

First,

$$
\langle e|J_\Phi|e\rangle
=
\frac{\alpha}{D}.
\tag{9.4}
$$

Also,

$$
\langle e|J_\Phi^2|e\rangle
=
\frac{\mathsf T_U}{Dm^4}.
\tag{9.5}
$$

Writing \(J_\Phi\) as a block matrix relative to
\(\mathbb Ce\oplus e^\perp\),

$$
J_\Phi=
\begin{pmatrix}
\alpha/D & b^*\\
b & B_\Phi
\end{pmatrix},
$$

one has

$$
\|b\|^2
=
\frac{\mathsf T_U}{Dm^4}
-
\frac{\alpha^2}{D^2}.
$$

Since

$$
\operatorname{Tr}J_\Phi^2
=
\frac{\mathsf I_U}{m^4},
$$

it follows that

$$
\boxed{
\operatorname{Tr}B_\Phi^2
=
\frac1{m^4}
\left(
\mathsf I_U
-\frac{2\mathsf T_U}{D}
+\frac{m^4\alpha^2}{D^2}
\right).
}
\tag{9.6}
$$

## 9.3 Alignment bound

Hilbert–Schmidt Cauchy–Schwarz for the two positive operators gives

$$
\operatorname{Tr}(B_\Phi S_\circ)
\le
\sqrt{
\operatorname{Tr}B_\Phi^2
\operatorname{Tr}S_\circ^2
}.
$$

Using (9.2), (9.3), and (9.6),

$$
\boxed{
\Theta_Q
\le
\frac1{m^2}
\sqrt{
\left(
\mathsf I_U-\frac{2\mathsf T_U}{D}
+\frac{m^4\alpha^2}{D^2}
\right)
\left(
\mathsf I_U-m^4
\right)
}.
}
\tag{Align-Q}
$$

This is an exact same-\(\Phi\) statement. It does not replace the physical problem by an unrestricted \(2\to2\) norm.

## 9.4 Strict improvement over \(\mathsf C_U\le\mathsf I_U\)

The generic bound \(\mathsf C_U\le\mathsf I_U\) gives only

$$
\Theta_Q
\le
\frac{
\mathsf I_U-\dfrac{m^4\alpha}{D}
}{m^2}.
\tag{9.7}
$$

Put

$$
i=\frac{\mathsf I_U}{m^4},
\qquad
\tau=\frac{\mathsf T_U}{m^4},
\qquad
r=\frac{\alpha}{D}.
$$

Since

$$
\tau\ge\frac{\alpha^2}{D}=Dr^2,
$$

the first factor in Align-Q obeys

$$
i-\frac{2\tau}{D}+r^2
\le
i-r^2.
$$

Moreover,

$$
i\ge\frac{\alpha^2}{D^2}=r^2.
$$

In the low-\(A\) feasible regime, PA implies \(D>m\), and hence

$$
\alpha\ge\frac{D^2}{m}>D,
\qquad r>1.
$$

Now

$$
\boxed{
(i-r)^2-(i-r^2)(i-1)
=
i(r-1)^2>0.
}
\tag{9.8}
$$

Since \(i>r\), equation (9.8) implies

$$
r+\sqrt{(i-r^2)(i-1)}<i.
$$

Therefore the Choi–Liouville upper bound on \(\mathsf C_U\),

$$
\boxed{
\begin{aligned}
\mathsf C_U
\le{}&
\frac{m^4\alpha}{D}\\
&+
\sqrt{
\left(
\mathsf I_U-\frac{2\mathsf T_U}{D}
+\frac{m^4\alpha^2}{D^2}
\right)
\left(\mathsf I_U-m^4\right)
},
\end{aligned}
}
\tag{9.9}
$$

is strictly smaller than \(\mathsf I_U\) for every low-\(A\) feasible tuple.

Using Comm-defect yields the new lower bound

$$
\boxed{
\begin{aligned}
\sum_{A,B}\|[A,B]\|_2^2
\ge{}&
2m^4\left(D-\frac{\alpha}{D}\right)\\
&-
2\sqrt{
\left(
\mathsf I_U-\frac{2\mathsf T_U}{D}
+\frac{m^4\alpha^2}{D^2}
\right)
\left(\mathsf I_U-m^4\right)
}.
\end{aligned}
}
\tag{Align-comm}
$$

---

# 10. The new exact necessary condition

Combining \(Q\)-required with Align-Q gives

$$
\boxed{
\begin{aligned}
&\mathcal C_{\mathrm{req}}
-\frac{m^4\alpha}{D}\\
&\qquad\le
\sqrt{
\left(
\mathsf I_U-\frac{2\mathsf T_U}{D}
+\frac{m^4\alpha^2}{D^2}
\right)
\left(
\mathsf I_U-m^4
\right)
}.
\end{aligned}
}
\tag{Alignment-required}
$$

Expanded,

$$
\boxed{
\begin{aligned}
&(D+2)\mathsf I_U
+(D+1)\mathsf T_U
+\frac{m^4}{2}B_0(D,\alpha)\\
&\quad
-\frac{
A m^3\alpha D(D+1)(D+3)
}{2}
-\frac{m^4\alpha}{D}\\
&\le
\sqrt{
\left(
\mathsf I_U-\frac{2\mathsf T_U}{D}
+\frac{m^4\alpha^2}{D^2}
\right)
\left(
\mathsf I_U-m^4
\right)
}.
\end{aligned}
}
\tag{10.1}
$$

Any tuple solving \((E1_{\mathrm{gap}})\) must satisfy:

$$
\frac{m^4\alpha^2}{D}
\le\mathsf T_U
\le
\sqrt A\,\frac{m^4\alpha^2}{D},
\tag{10.2}
$$

together with (10.1), PA, and the Round 4 fourth-moment upper endpoint.

These conditions are materially narrower than the Round 4 invariant interval, but they still leave a nonempty algebraic relaxation. In particular, at the weakest dimension bounds and at PA equality, the left side before the square root can be nonpositive; therefore those scalar bounds alone cannot close the gate.

---

# 11. Earliest remaining operator gap

Pure-\(Q\) gives, for every unit \(y\),

$$
\langle\langle\rho_y|
S_\circ
|\rho_y\rangle\rangle
\le\epsilon.
\tag{11.1}
$$

The quantity that governs Pair-energy is instead

$$
\operatorname{Tr}(B_\Phi S_\circ),
\qquad
B_\Phi=P_\perp J_\Phi P_\perp,
\tag{11.2}
$$

where \(J_\Phi\) and \(S_\Phi\) are related by the fixed realignment (4.6).

The exact lower threshold demanded by the symmetric-Bell gate is

$$
\boxed{
\operatorname{Tr}(B_\Phi S_\circ)
\ge
\frac{
\mathcal C_{\mathrm{req}}
-\dfrac{m^4\alpha}{D}
}{m^4}.
}
\tag{11.3}
$$

The proved Cauchy upper bound is

$$
\boxed{
\operatorname{Tr}(B_\Phi S_\circ)
\le
\frac1{m^4}
\sqrt{
\left(
\mathsf I_U-\frac{2\mathsf T_U}{D}
+\frac{m^4\alpha^2}{D^2}
\right)
\left(
\mathsf I_U-m^4
\right)
}.
}
\tag{11.4}
$$

What remains open is an orientation-sensitive implication of the following exact form:

> For every frozen tuple satisfying Pure-\(Q\), the random-unitary pair-difference structure, and the low-\(A\) conditions, does the coherent-state bound (11.1) force an upper bound on
> \(\operatorname{Tr}(B_\Phi S_\circ)\) strictly below the threshold in (11.3)?

No such universal strict upper bound is proved here. Nor is a tuple constructed for which the full pointwise condition \(\kappa_1(U)\le A-1\) holds.

This is not a generic \(2\to2\) question: it concerns the overlap of a Choi block with the traceless part of its own realignment, for the single positive superoperator \(\Phi=L^*L\).

---

# Audit ledger

| Status           | Statement                                                                                 |          |                                                                |
| ---------------- | ----------------------------------------------------------------------------------------- | -------- | -------------------------------------------------------------- |
| **PROVED**       | Pair-energy identity \(\mathsf C_U=m^2\sum_{a,b}\|L(U_b^*U_a)\|_2^2\).                    |          |                                                                |
| **PROVED**       | Scalar/traceless decomposition \(\mathsf C_U=m^4\alpha/D+m^2\Theta_Q\).                   |          |                                                                |
| **PROVED**       | \(\mathsf C_U\ge m^4\alpha/D\ge0\).                                                       |          |                                                                |
| **PROVED**       | Comm-defect identity \(\mathsf C_U=m^4D-\frac12\sum_{A,B}\|[A,B]\|_2^2\).                 |          |                                                                |
| **PROVED**       | Exact lower bound \(Q\)-required and exact upper bound Comm-required.                     |          |                                                                |
| **PROVED**       | Convention-fixed Choi/Liouville/realignment/partial-transpose dictionary.                 |          |                                                                |
| **PROVED**       | (\alpha=\operatorname{Tr}S_\Phi=\langle I                                                 | J_\Phi   | I\rangle).                                                     |
| **PROVED**       | \(\mathsf I_U=m^4\operatorname{Tr}S_\Phi^2=m^4\operatorname{Tr}J_\Phi^2\).                |          |                                                                |
| **PROVED**       | (\mathsf T_U=m^4\langle I                                                                 | J_\Phi^2 | I\rangle=m^4\operatorname{Tr}[(\operatorname{Tr}*1S*\Phi)^2]). |
| **PROVED**       | \(\mathsf C_U=m^4\operatorname{Tr}(J_\Phi S_\Phi)\).                                      |          |                                                                |
| **PROVED**       | Exact decomposition \(\Phi=\Delta_D+Q^*Q\).                                               |          |                                                                |
| **REDUNDANT**    | Scalar relaxation of \(C\)-required with \(\mathsf C_U\le\mathsf I_U\).                   |          |                                                                |
| **REDUNDANT**    | Scalar relaxation of \(C\)-required with \(\mathsf C_U\le m^4D\).                         |          |                                                                |
| **REDUNDANT**    | Scalar relaxation of \(C\)-upper with Pair-energy.                                        |          |                                                                |
| **REDUNDANT**    | Scalar relaxation of \(C\)-upper with \(\mathsf C_U\ge0\).                                |          |                                                                |
| **PROVED — new** | \(M_U\preceq m^2\sqrt{\alpha p}\,I_D\).                                                   |          |                                                                |
| **PROVED — new** | Mixing–marginal squeeze \(m^4\alpha^2/D\le\mathsf T_U\le\sqrt A\,m^4\alpha^2/D\).         |          |                                                                |
| **PROVED — new** | Choi–Liouville alignment bound Align-Q.                                                   |          |                                                                |
| **PROVED — new** | Strict improvement over \(\mathsf C_U\le\mathsf I_U\) for every feasible low-\(A\) tuple. |          |                                                                |
| **PROVED — new** | Aggregate commutator lower bound Align-comm.                                              |          |                                                                |
| **OPEN**         | Whether Alignment-required is incompatible with all low-\(A\) pair-difference tuples.     |          |                                                                |
| **OPEN**         | Existence of one finite tuple satisfying the uniform all-\(T\) ratio bound.               |          |                                                                |
| **OPEN**         | \((E1_{\mathrm{gap}})\).                                                                  |          |                                                                |
| **CONJECTURED**  | None promoted.                                                                            |          |                                                                |
| **DISPROVED**    | No new universal statement is disproved in this round.                                    |          |                                                                |

The first new statement requiring independent verification is

$$
\boxed{
M_U\preceq m^2\sqrt{\alpha p}\,I_D,
}
$$

and the first remaining open statement is the conversion of the pointwise Pure-\(Q\) bound into a sufficiently strong upper bound on the orientation-sensitive alignment

$$
\operatorname{Tr}
\left[
(P_\perp J_\Phi P_\perp)
(S_\Phi-P_0)
\right].
$$

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-05-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-05-local-audit.md bytes=7173 sha256=84ebf2b352228ca4222dd56a1e06602d2168de739f8d19218d48bb0130e3a259 -->

# Round 5 local audit

Date: 2026-09-12

Status: equation-level local audit completed. This is not an independent
external review, and it does not close the finite gate.

## Verdict

There is no substantive normalization, adjoint, or inequality-direction error
in the two new headline lemmas:

    Pair-energy / Comm-defect: VERIFIED.
    Mixing--marginal squeeze (MM): VERIFIED.
    Choi--Liouville alignment bound (Align-Q): VERIFIED.
    Strict improvement over C_U <= I_U: VERIFIED.
    (E1_gap): OPEN WITH EARLIEST GAP.

The response is materially useful, but incomplete. It missed an exact
realignment-defect identity and two further same-map constraints: a
trace-centered strengthening of Align-Q and a low-rank bound on the
traceless Choi block. These omissions do not make the response's proved
claims false. They provide the next deterministic attack.

## Capture and status ledger

| Item | Local status | Meaning |
|---|---|---|
| Browser response capture | VERIFIED | Saved Markdown is byte-for-byte identical to the browser Copy-response payload. |
| Browser payload SHA-256 | VERIFIED | c6a8e3a2471dfbfe276e38c94a6a8c77daca0db64cfb3653545aac011d63f4bb |
| Pair-energy identity | VERIFIED | All four indices, adjoints, and powers of m check. |
| Comm-defect identity | VERIFIED | Adjoint closure converts the ordered defect sum exactly. |
| Choi/Liouville dictionary | VERIFIED | The stated column-vectorization reshuffling and all four invariant formulas check. |
| Four scalar PA reductions | VERIFIED | Direct symbolic expansion reproduces equations (7.3)--(7.6). |
| MM | VERIFIED | Gram positivity gives M_U <= m^2 sqrt(alpha p) I and hence the stated T_U bound. |
| Align-Q | VERIFIED | The block purities and the factor 1/m^2 are correct. |
| Strictness versus C_U <= I_U | VERIFIED | The normalized comparison is strict for r=alpha/D>1. |
| Audit-table formatting | PRESENTATION ONLY | Unescaped vertical bars inside formulas split some Markdown cells; the preceding equations are intact. |
| (E1_gap) | OPEN | No admissible frozen tuple and no universal violating input is proved. |
| Full-size theorem | OPEN / CONJECTURED | The finite r=2 gate and the separate all-copy gate remain open. |

## Independent check of the new bounds

Use

    i   = I_U/m^4,
    tau = T_U/m^4,
    r   = alpha/D.

For the positive matrix

    M_U = sum_A Tr(A) A^*,

the two Gram matrices

    H_ab   = Tr(U_a^* U_b),
    G_y,ab = <y|U_a^* U_b|y>

are positive. Their Hilbert--Schmidt norms are

    ||H||_2^2   = m^2 alpha,
    ||G_y||_2^2 <= m^2 p.

The identity <y|M_U|y>=Tr(HG_y) therefore yields

    0 <= M_U <= m^2 sqrt(alpha p) I_D.

Together with Tr M_U=m^2 alpha and p<=A/m,

    m^4 alpha^2/D
      <= T_U
      <= m^4 alpha sqrt(alpha p)
      <= sqrt(A) m^4 alpha^2/D.

The last step uses alpha>=D^2/m. This verifies MM.

Now put

    e       = |I>>/sqrt(D),
    P_0     = |e><e|,
    P       = S_Phi-P_0,
    B       = P_perp J_Phi P_perp.

Then

    Tr(P^2) = i-1,
    Tr(B^2) = i-2 tau/D+r^2,
    Theta_Q = m^2 Tr(BP).

Hilbert--Schmidt Cauchy--Schwarz gives exactly

    Theta_Q
      <= m^(-2)
         sqrt[
           (I_U-2T_U/D+m^4 alpha^2/D^2)
           (I_U-m^4)
         ].

For a=i-2tau/D+r^2 and b=i-1, the resulting normalized upper
bound on C_U is r+sqrt(ab). The generic bound C_U<=I_U is i.
Since tau>=Dr^2, i>=r^2, and low-A feasibility gives r>1,

    (i-r)^2-(i-r^2)(i-1)=i(r-1)^2>0.

Thus r+sqrt(ab)<i. The response's strict-improvement claim is correct.

## Exact realignment defect omitted by the response

The reshuffling between S_Phi and J_Phi preserves Hilbert--Schmidt norm, and

    Tr(J_Phi S_Phi)=C_U/m^4.

Therefore

    I_U-C_U = (m^4/2)||S_Phi-J_Phi||_2^2.       (RD)

Projecting the defect onto its scalar and two one-body marginals gives

    I_U-C_U
      >= [T_U-2m^4 alpha+m^4D]/D
         -m^4(alpha-D)^2/(2D^2).                 (RD-PT2)

This does not beat Align-Q. In the normalized variables above, RD-PT2 gives

    C_U/m^4 <= r+(a+b)/2,

whereas Align-Q gives

    C_U/m^4 <= r+sqrt(ab).

The latter is at least as strong by arithmetic--geometric mean. Thus RD is
important exact geometry, but its two-marginal scalar relaxation is already
subsumed by Round 5's alignment lemma.

## Stronger trace-centered alignment

Both B and P act on the n=D^2-1 dimensional space e^perp. Their traces are

    u := Tr P = alpha-1,
    v := Tr B = D-r.

Centering each operator around the identity on e^perp gives the strictly
sharper deterministic bound

    Tr(BP)
      <= uv/n
         +sqrt[
            (i-2tau/D+r^2-v^2/n)
            (i-1-u^2/n)
          ].                                      (Centered-Align)

It is never weaker than Align-Q: this follows by applying Cauchy--Schwarz
after the orthogonal decomposition into scalar and traceless components.
Equality with the uncentered bound requires the two scalar/traceless norm
ratios to align.

The associated sharp trace-purity constraints are

    i-1 >= u^2/n,
    i-2tau/D+r^2 >= v^2/n.

Trace centering alone still does not close the gate. At

    tau = Dr^2,
    i   = 1+u^2/n,

the second lower bound is also an equality. At PA equality

    A=A_0=m(alpha+D)/[D(D+1)],

one obtains exactly

    C_up/m^4 = r+uv/n,

and

    C_req/m^4-(r+uv/n)
      =-(alpha-D)(D+3)(D^2-alpha)/[2(D-1)] <= 0.

So the trace-isotropic scalar corner remains feasible for these relaxations.

## Pair-difference rank and contraction constraints

The trace-isotropic corner above is not compatible with the available Choi
rank in the low-A regime. Indeed,

    B
      =m^(-2) sum_(a!=b)
         |P_perp(U_b^*U_a)>><<P_perp(U_b^*U_a)|.

The m diagonal terms vanish after P_perp. Hence

    rank(B) <= m(m-1),

and therefore

    i-2tau/D+r^2
      >= (D-r)^2/[m(m-1)].                       (B-rank)

Combining this with tau>=Dr^2 yields

    i >= r^2+(D-r)^2/[m(m-1)].

Low-A feasibility gives D>m, so this is much stronger than the ambient
dimension trace bound on B in the near-minimal-PA dimension range. It raises
I_U and can force C_up below Pair-energy in part of parameter space. A
global contradiction for arbitrary larger D has not been proved locally.

There is also an exact contraction constraint. Since L is a convex
combination of unitary conjugations,

    ||L||_(2->2) <= 1,
    0 <= S_Phi=L^*L <= I.

Consequently

    0 <= P <= P_perp,
    i=Tr(S_Phi^2) <= Tr(S_Phi)=alpha.

These rank and contraction constraints were absent from the Round 5 ledger
and should be audited together with Centered-Align before any claim that the
remaining invariant interval is irreducible.

## Remaining boundary

The safe status after the local audit is

    (E1_gap): OPEN.
    finite r=2 low-A gate: OPEN.
    earlier all-copy gate: OPEN.
    full-size finite-dimensional MOE/Holevo theorem: OPEN / CONJECTURED.

The next round should first test whether B-rank, Centered-Align, MM, C-upper,
and C-required partition the entire dimension range. If a scalar relaxation
survives, it must display an explicit feasible parameter family and then
attack the actual realignment/pair-difference operator structure rather than
repeating an orientation-insensitive norm bound.

<!-- END HISTORICAL FILE path=outputs/round-05-local-audit.md -->


# ROUND 006

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-06-prompt.md bytes=8097 sha256=550198e9b218ff1a54cc21aea2e8484ece5cf4abd26d0ecb2a14988ec9e29629 -->

# Round 6 — low Choi rank, centered alignment, and a two-regime closure attempt

Continue in the same deterministic one-layer setup and the same conversation.
This is an adversarial proof round focused only on the finite r=2 low-A gate.

Let finite m,D, eta>0 and one frozen tuple

    U=(U_1,...,U_m) in U(D)^m

define

    C(X)_(v,w)=m^(-1) Tr(X U_w^*U_v),
    L(X)=m^(-1) sum_v U_v X U_v^*,
    Q=L-Delta_D,
    Phi=L^*L,

    A=1+9(1+eta)^2/m,
    p=sup_rho ||C(rho)||_2^2,

with

    ln m>18,
    A^2<m^(1/m),
    p<=A/m.

For every Hilbert--Schmidt unit T, retain the audited definitions of d_T,
R_U(T), and kappa_1(U). The target remains

    (E1_gap): kappa_1(U)<=A-1

for one finite tuple satisfying all conditions above.

No broad MOE/Holevo blueprint is requested. Give a public, self-contained
derivation and no hidden chain-of-thought.

## Audited Round 5 input

For the pair-difference multiset

    A_U={A_ab=U_b^*U_a : 1<=a,b<=m},

put

    alpha=m^(-2) sum_(a,b)|Tr A_ab|^2,

    I_U=sum_(A,B in A_U)|Tr(AB)|^2,
    T_U=sum_(A,B in A_U) Tr(A)Tr(B) overline{Tr(AB)},
    C_U=sum_(A,B in A_U) Tr(ABA^*B^*).

Round 5 and a local equation-level audit verified

    C_U
      =m^2 sum_(a,b)||L(A_ab)||_2^2
      =m^4 alpha/D+m^2 Theta_Q,

    Theta_Q=sum_(a,b)||Q(A_ab)||_2^2,

and

    C_U
      =m^4D-(1/2)sum_(A,B)||[A,B]||_2^2.

Use column vectorization and let S and J be respectively the Liouville and
unnormalized Choi matrices of Phi. With e=|I>>/sqrt(D),

    P_0=|e><e|,
    P=S-P_0>=0,
    B=P_perp J P_perp>=0.

The same audit verified

    S=P_0+P,
    P|e>=0,

    I_U=m^4 Tr(S^2)=m^4 Tr(J^2),
    T_U=m^4 <I|J^2|I>,
    C_U=m^4 Tr(JS),

    Theta_Q=m^2 Tr(BP).

Use the normalized variables

    i=I_U/m^4,
    tau=T_U/m^4,
    r=alpha/D,
    n=D^2-1.

Then

    Tr(P)=u:=alpha-1,
    Tr(P^2)=i-1,

    Tr(B)=v:=D-r,
    Tr(B^2)=i-2tau/D+r^2.

The Round 5 mixing and uncentered alignment bounds are

    Dr^2 <= tau <= sqrt(A) Dr^2,                 (MM)

    Tr(BP)
      <= sqrt[(i-2tau/D+r^2)(i-1)].              (Align)

The two exact symmetric-Bell endpoints are

    C_req
      =(D+2)I_U+(D+1)T_U
       +(m^4/2)B_0(D,alpha)
       -(A m^3 alpha D(D+1)(D+3))/2,

    C_up
      =(1/2)[
         A m^3(alpha+D)(D+2)(D+3)
         -m^4(D^2+4D+alpha^2+2(D+4)alpha)
         -2I_U-4T_U
       ],

where

    B_0(D,alpha)
      =D(D^2+4D+2)+(D+2)alpha^2-2(D+4)alpha.

Every solution must satisfy

    C_req <= C_U <= C_up.

Round 5 correctly found that its four dimension-only scalar relaxations are
redundant with

    m(alpha+D)<=A D(D+1).                       (PA)

It did not close (E1_gap).

## New exact facts to audit first

### 1. Realignment defect

Because J is the fixed reshuffling of S and the reshuffling preserves the
Hilbert--Schmidt norm,

    I_U-C_U=(m^4/2)||S-J||_2^2.                 (RD)

The two-marginal projection gives

    I_U-C_U
      >=[T_U-2m^4 alpha+m^4D]/D
        -m^4(alpha-D)^2/(2D^2).                (RD-PT2)

In the variables above, RD-PT2 is exactly

    C_U/m^4 <= r+(a+b)/2,

where

    a=i-2tau/D+r^2,
    b=i-1.

Thus Round 5's Align upper bound r+sqrt(ab) is at least as strong by AM--GM.
Verify this; do not re-advertise RD-PT2 as stronger than Align.

### 2. Trace-centered alignment

Centering B and P on the n-dimensional space e^perp gives

    Tr(BP)
      <= uv/n
         +sqrt[
           (i-2tau/D+r^2-v^2/n)
           (i-1-u^2/n)
         ].                                    (Centered-Align)

This is never weaker than Align. Audit all traces, signs, and equality
conditions.

Trace centering alone still has a scalar escape. At

    tau=Dr^2,
    i=1+u^2/n,
    A=A_0:=m(alpha+D)/[D(D+1)],

both centered variances vanish and direct expansion gives

    C_up/m^4=r+uv/n,

    C_req/m^4-(r+uv/n)
      =-(alpha-D)(D+3)(D^2-alpha)/[2(D-1)]<=0.

Audit this factorization. It shows why merely centering the two purities is
not a closure.

### 3. Low rank of the traceless Choi block

The compression has the exact frame form

    B
      =m^(-2) sum_(a!=b)
        |P_perp A_ab>><<P_perp A_ab|.

The m diagonal pair differences equal I and vanish after P_perp. Therefore

    rank(B)<=m(m-1),

and, since low-A feasibility has D>m,

    i-2tau/D+r^2
      >=(D-r)^2/[m(m-1)].                      (B-rank)

Together with tau>=Dr^2 this yields

    i>=r^2+(D-r)^2/[m(m-1)].                   (I-rank)

Verify the rank argument and prove D>m from Gap, PA, and
alpha>=D^2/m rather than assuming it.

### 4. Hilbert--Schmidt contraction

Because L is a convex average of unitary conjugations,

    ||L||_(2->2)<=1,
    0<=S=L^*L<=I.

Hence

    0<=P<=P_perp,
    i=Tr(S^2)<=Tr(S)=alpha.                    (Contract)

Audit this and retain it in every optimization.

### 5. Pointwise Pure-Q extension

The local audit also derived, for every unitary W,

    ||Q(W)||_2^2
      <=epsilon(D^2-|Tr W|^2),

    epsilon=A/m-1/D.

Consequently

    Tr(BP)=Theta_Q/m^2
      <=epsilon(D^2-alpha).                    (Unitary-Q)

This estimate alone is too weak in part of the feasible regime. It may still
be useful in combination with B-rank and Centered-Align. Audit it before use.

## Exact tasks

1. Give one verdict on (E1_gap): PROVED, DISPROVED, or OPEN WITH EARLIEST
   GAP. An averaged necessary test or a scalar relaxation is not a proof.

2. Audit RD, Centered-Align, B-rank, Contract, and Unitary-Q from first
   principles. Correct any false formula explicitly.

3. Form the strongest scalar necessary system obtained from:

       Gap, PA, alpha>=D^2/m, alpha<D^2,
       MM,
       trace-purity for P and B,
       B-rank,
       Contract,
       Pair-energy,
       Centered-Align,
       Unitary-Q,
       C_req<=C_U<=C_up.

   Do not replace i and tau by lower bounds unless the relevant expression is
   proved monotone in the needed direction. Handle every square-root sign
   condition explicitly.

4. Analyze that system globally and analytically over the entire dimension
   range. A useful parameter is

       q=m(A-1)=9(1+eta)^2,

   with the exact Gap inequality

       2m log(1+q/m)<log m.

   Determine whether B-rank plus C_up rules out a near-minimal-D regime and
   whether Centered-Align or Unitary-Q rules out the complementary large-D
   regime.

   If the scalar system is infeasible for all allowed parameters, give the
   exact partition and factorizations. This disproves (E1_gap) only if every
   inequality used is a valid necessary condition.

   If it survives, exhibit an explicit symbolic or asymptotic parameter family
   satisfying every scalar inequality, with error terms controlled. Label it
   only as a surviving relaxation, not as a unitary tuple.

5. If a scalar family survives, attack the first operator obstruction:

       B=m^(-2) sum_(a!=b)|P_perp A_ab>><<P_perp A_ab|,
       P=Liouville(Q^*Q),
       J=realign(P_0+P)>=0,
       0<=P<=P_perp,
       sup_y <<rho_y|P|rho_y> <= epsilon.

   Prove either a stronger upper bound on Tr(BP) that genuinely uses both the
   low rank/unitary frame for B and the coherent-state bound for P, or prove
   that no such bound follows from a precisely stated relaxation by giving an
   exact counterexample inside that relaxation. A generic unrestricted
   2-to-2/cb estimate is inadmissible.

6. Closure still requires one of:

   (a) a universal deterministic violating T for every admissible tuple,
       thereby disproving (E1_gap); or

   (b) one explicit finite frozen tuple satisfying the full uniform all-T
       ratio bound, thereby proving (E1_gap).

   If neither is reached, state the earliest exact implication still missing.

7. Do not use the full-Weyl loophole, numerical evidence as proof, WHGAP,
   copy-dependent tuples, independent-local-Haar averages that erase
   orientation, or claims about the separate all-copy gate.

8. End with an audit ledger separating PROVED, DISPROVED, REDUNDANT, OPEN,
   and CONJECTURED. Identify the first new statement requiring independent
   verification.

The full-size theorem remains OPEN unless both (E1_gap) and the earlier
all-copy gate are separately closed.

<!-- END HISTORICAL FILE path=work/round-06-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-06-response.md bytes=31934 sha256=9fb8abbde279c6c61c9294fa24f57a84ed140e921eeacb056c83cf88f885e55d -->

# Verdict

$$
\boxed{\text{\((E1_{\mathrm{gap}})\) remains OPEN WITH EARLIEST GAP.}}
$$

All five proposed new facts—realignment defect, centered alignment, low Choi rank, Hilbert–Schmidt contraction, and the unitary extension of Pure-\(Q\)—are valid, with two qualifications:

1. \((RD\text{-}PT2)\) is exactly the arithmetic-mean relaxation of the previously proved alignment bound, hence is **REDUNDANT**.
2. Low Choi rank plus \(C_{\rm up}\) excludes a thin region near exact \(PA\)-saturation, but the complete scalar necessary system remains feasible. An exact symbolic large-\(D\) family satisfying every scalar inequality is given below.

Moreover, even a stronger decoupled operator relaxation survives: one can construct

* a positive contraction \(S=P_0+P\) satisfying the exact coherent-state Pure-\(Q\) bound,
* a positive Choi matrix \(\widetilde J=rP_0+B\) with correct bistochastic marginals and an exact rank-\(m(m-1)\) unitary frame,
* matching traces, purities, \(\alpha,i,\tau\), and all symmetric-Bell endpoint inequalities,

but without imposing that \(\widetilde J\) is the realignment of that same \(S\), or that its frame elements are the pair differences of one \(m\)-tuple.

Thus the earliest missing implication is genuinely the **same-map realignment and pair-difference coupling**, not another scalar trace-purity estimate.

---

# 1. Common block notation

Let

$$
e=\frac{|I_D\rangle\rangle}{\sqrt D},
\qquad
P_0=|e\rangle\langle e|,
\qquad
P_\perp=I-P_0.
$$

Relative to

$$
\mathbb C e\oplus e^\perp,
$$

write

$$
S=
\begin{pmatrix}
1&0\\
0&P
\end{pmatrix},
\qquad
J=
\begin{pmatrix}
r&z^*\\
z&B
\end{pmatrix},
\tag{1.1}
$$

where

$$
r=\frac{\alpha}{D},
\qquad
P\succeq0,
\qquad
B\succeq0.
$$

The normalized invariants are

$$
i=\frac{\mathsf I_U}{m^4}=\operatorname{Tr}S^2=\operatorname{Tr}J^2,
$$

$$
\tau=\frac{\mathsf T_U}{m^4}
=\langle\langle I|J^2|I\rangle\rangle.
$$

Since \(|I\rangle\rangle=\sqrt D\,e\),

$$
\langle e|J^2|e\rangle=\frac{\tau}{D}.
$$

The upper-left entry of \(J^2\) is \(r^2+\|z\|^2\), so

$$
\boxed{
h:=\|z\|^2=\frac{\tau}{D}-r^2.
}
\tag{1.2}
$$

Put

$$
u=\operatorname{Tr}P=\alpha-1,
\qquad
v=\operatorname{Tr}B=D-r,
\qquad
n=D^2-1.
$$

Also,

$$
b:=\operatorname{Tr}P^2=i-1.
\tag{1.3}
$$

Since

$$
\operatorname{Tr}J^2
=
r^2+2\|z\|^2+\operatorname{Tr}B^2,
$$

we obtain

$$
\boxed{
a:=\operatorname{Tr}B^2
=
i-\frac{2\tau}{D}+r^2.
}
\tag{1.4}
$$

Finally, Pair-energy gives

$$
\frac{\mathsf C_U}{m^4}
=
r+\frac{\Theta_Q}{m^2}.
$$

Because

$$
\Theta_Q=m^2\operatorname{Tr}(BP),
$$

define

$$
x:=\operatorname{Tr}(BP)\ge0.
$$

Then

$$
\boxed{
\frac{\mathsf C_U}{m^4}=r+x.
}
\tag{1.5}
$$

---

# 2. Audit of the realignment defect

Realignment is a permutation of matrix entries, so

$$
\|J\|_2=\|S\|_2.
$$

Moreover, \(S,J\succeq0\), so \(\operatorname{Tr}(SJ)\) is real and nonnegative. Therefore

$$
\begin{aligned}
\|S-J\|_2^2
&=
\operatorname{Tr}S^2+\operatorname{Tr}J^2
-2\operatorname{Tr}(SJ)\\
&=
2i-2\frac{\mathsf C_U}{m^4}.
\end{aligned}
$$

Multiplication by \(m^4/2\) gives

$$
\boxed{
\mathsf I_U-\mathsf C_U
=
\frac{m^4}{2}\|S-J\|_2^2.
}
\tag{RD}
$$

This identity is correct.

## 2.1 The proposed \(RD\text{-}PT2\) lower bound

From the blocks in (1.1),

$$
S-J=
\begin{pmatrix}
1-r&-z^*\\
-z&P-B
\end{pmatrix}.
$$

Hence

$$
\|S-J\|_2^2
=
(1-r)^2+2h+\|P-B\|_2^2.
$$

Dropping the last nonnegative term gives

$$
i-\frac{\mathsf C_U}{m^4}
\ge
\frac{(1-r)^2}{2}+h.
$$

Using \(h=\tau/D-r^2\),

$$
\boxed{
i-\frac{\mathsf C_U}{m^4}
\ge
\frac{\tau}{D}-r-\frac{r^2}{2}+\frac12.
}
\tag{2.1}
$$

In the original variables, this is exactly

$$
\boxed{
\mathsf I_U-\mathsf C_U
\ge
\frac{\mathsf T_U-2m^4\alpha+m^4D}{D}
-
\frac{m^4(\alpha-D)^2}{2D^2}.
}
\tag{RD-PT2}
$$

Now use

$$
\frac{\mathsf C_U}{m^4}=r+x
$$

and

$$
a+b
=
2i-\frac{2\tau}{D}+r^2-1.
$$

Rearranging (2.1) gives

$$
\boxed{
r+x\le r+\frac{a+b}{2}.
}
\tag{2.2}
$$

Thus \(RD\text{-}PT2\) is exactly the estimate

$$
x\le\frac{a+b}{2}.
$$

The previous alignment bound gives \(x\le\sqrt{ab}\), and

$$
\sqrt{ab}\le\frac{a+b}{2}.
$$

Therefore

$$
\boxed{
RD\text{-}PT2\text{ is valid but REDUNDANT with Align.}
}
$$

---

# 3. Centered alignment

Both \(B\) and \(P\) act on the \(n\)-dimensional space \(e^\perp\). Write

$$
B=\frac vnP_\perp+B_0,
\qquad
P=\frac unP_\perp+P_1,
$$

with

$$
\operatorname{Tr}B_0=\operatorname{Tr}P_1=0.
$$

Then

$$
\operatorname{Tr}(BP)
=
\frac{uv}{n}+\operatorname{Tr}(B_0P_1).
$$

Furthermore,

$$
\|B_0\|_2^2=a-\frac{v^2}{n},
\qquad
\|P_1\|_2^2=b-\frac{u^2}{n}.
$$

Hilbert–Schmidt Cauchy–Schwarz yields

$$
\boxed{
x
\le
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}.
}
\tag{Centered-Align}
$$

The radicands are nonnegative by the trace-purity inequalities.

## 3.1 It is never weaker than uncentered Align

Set

$$
\xi=\frac{v}{\sqrt{na}},
\qquad
\zeta=\frac{u}{\sqrt{nb}}.
$$

Then \(0\le\xi,\zeta\le1\), and after division by \(\sqrt{ab}\), the centered upper bound becomes

$$
\xi\zeta+\sqrt{1-\xi^2}\sqrt{1-\zeta^2}.
$$

This is at most \(1\). Hence

$$
\boxed{
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}
\le\sqrt{ab}.
}
\tag{3.1}
$$

Equality in the scalar comparison requires \(\xi=\zeta\). Equality in the full centered bound additionally requires \(B_0\) and \(P_1\) to be positively proportional.

---

# 4. The trace-centered scalar escape

Suppose

$$
\tau=Dr^2,
\qquad
i=1+\frac{u^2}{n}.
\tag{4.1}
$$

Then \(z=0\), \(P\) is trace-purity minimal, and

$$
b=\frac{u^2}{n}.
$$

A direct calculation gives

$$
1+\frac{(Dr-1)^2}{D^2-1}-r^2
=
\frac{(D-r)^2}{D^2-1}.
$$

Thus

$$
a=\frac{v^2}{n}.
$$

Both centered variances vanish, and

$$
x\le\frac{uv}{n}.
$$

Let

$$
A_0=\frac{m(\alpha+D)}{D(D+1)},
$$

the value at equality in \(PA\). Substitution into the exact endpoint formulas gives

$$
\boxed{
\frac{\mathsf C_{\rm up}}{m^4}
=
r+\frac{uv}{n},
}
\tag{4.2}
$$

and

$$
\boxed{
\frac{\mathsf C_{\rm req}}{m^4}
-
\left(r+\frac{uv}{n}\right)
=
-\frac{(\alpha-D)(D+3)(D^2-\alpha)}
{2(D-1)}
\le0.
}
\tag{4.3}
$$

Since the feasible regime has \(D<\alpha<D^2\), the right side is strictly negative.

Therefore centered trace-purity alone has an exact escape. Low Choi rank is needed to move away from this trace-minimal point.

---

# 5. Low rank of \(B\)

The Choi matrix of \(\Phi\) is

$$
J=
\frac1{m^2}
\sum_{a,b}
|A_{ab}\rangle\rangle
\langle\langle A_{ab}|,
\qquad
A_{ab}=U_b^*U_a.
$$

Compression to \(e^\perp\) gives

$$
B=
\frac1{m^2}
\sum_{a,b}
|P_\perp A_{ab}\rangle\rangle
\langle\langle P_\perp A_{ab}|.
$$

For \(a=b\),

$$
A_{aa}=I_D,
\qquad
P_\perp|I_D\rangle\rangle=0.
$$

Hence

$$
\boxed{
B=
\frac1{m^2}
\sum_{a\ne b}
|P_\perp A_{ab}\rangle\rangle
\langle\langle P_\perp A_{ab}|.
}
\tag{5.1}
$$

There are \(m(m-1)\) summands, so

$$
\boxed{
\operatorname{rank}B\le k:=m(m-1).
}
\tag{5.2}
$$

For a positive operator of rank at most \(k\) and trace \(v\),

$$
\operatorname{Tr}B^2\ge\frac{v^2}{k}.
$$

Therefore

$$
\boxed{
a\ge\frac{v^2}{m(m-1)}.
}
\tag{B-rank}
$$

Since

$$
a=i-\frac{2\tau}{D}+r^2
$$

and \(\tau\ge Dr^2\),

$$
a\le i-r^2.
$$

Consequently,

$$
\boxed{
i\ge
r^2+\frac{(D-r)^2}{m(m-1)}.
}
\tag{I-rank}
$$

Both proposed rank inequalities are correct.

---

# 6. Why low-\(A\) feasibility forces \(D>m\)

The pure-state Haar average from the preceding rounds gives

$$
m(\alpha+D)\le AD(D+1).
\tag{PA}
$$

Also,

$$
\alpha\ge\frac{D^2}{m}.
$$

Therefore

$$
D^2+mD\le AD(D+1),
$$

so

$$
\boxed{
D\ge\frac{m-A}{A-1}.
}
\tag{6.1}
$$

The Gap condition gives

$$
A<m^{1/(2m)}.
$$

For \(m>1\),

$$
\frac{\log m}{2m}
<
\frac{m-1}{2m}.
$$

Also, with \(x=(m-1)/(m+1)\),

$$
\log(1+x)\ge\frac{x}{1+x}=\frac{m-1}{2m}.
$$

Thus

$$
m^{1/(2m)}
<
\frac{2m}{m+1},
$$

and hence

$$
A<\frac{2m}{m+1}.
$$

This is equivalent to

$$
\frac{m-A}{A-1}>m.
$$

Therefore

$$
\boxed{D>m.}
\tag{6.2}
$$

In particular,

$$
m(m-1)<D^2-1=n,
$$

so the rank bound for \(B\) is genuinely stronger than the ambient trace-purity bound.

---

# 7. Hilbert–Schmidt contraction

For every \(X\),

$$
\begin{aligned}
\|L(X)\|_2
&=
\left\|
\frac1m\sum_vU_vXU_v^*
\right\|_2\\
&\le
\frac1m\sum_v\|U_vXU_v^*\|_2\\
&=\|X\|_2.
\end{aligned}
$$

Hence

$$
\|L\|_{2\to2}\le1.
$$

Since

$$
\Phi=L^*L,
$$

its Liouville matrix satisfies

$$
0\preceq S\preceq I.
$$

Moreover, \(L(I)=I\) and \(L^*(I)=I\), so

$$
Se=e.
$$

Consequently,

$$
\boxed{
0\preceq P\preceq P_\perp.
}
\tag{7.1}
$$

The eigenvalues of \(S\) lie in \([0,1]\), and

$$
\operatorname{Tr}S=\alpha.
$$

Therefore

$$
\boxed{
i=\operatorname{Tr}S^2\le\operatorname{Tr}S=\alpha.
}
\tag{Contract}
$$

Equivalently,

$$
b=i-1\le\alpha-1=u.
$$

The proposed contraction statement is correct.

---

# 8. Pointwise Pure-\(Q\) extension to unitaries

Let \(W\) be unitary and choose an orthonormal eigenbasis:

$$
W=\sum_{j=1}^D z_j\rho_j,
\qquad
|z_j|=1,
\qquad
\rho_j=|y_j\rangle\langle y_j|.
$$

Set

$$
q_j=Q(\rho_j).
$$

Since \(Q(I)=0\),

$$
\sum_jq_j=0.
$$

Let \(K\) be their Gram matrix:

$$
K_{jk}=\langle q_j,q_k\rangle_{\rm HS}.
$$

Then

$$
K\succeq0,
\qquad
K\mathbf1=0,
\qquad
K_{jj}\le\epsilon,
$$

where

$$
\epsilon=\frac Am-\frac1D.
$$

Therefore

$$
\operatorname{Tr}K\le D\epsilon
$$

and

$$
\lambda_{\max}(K)\le D\epsilon.
$$

Now

$$
\|Q(W)\|_2^2=z^*Kz.
$$

Because \(K\mathbf1=0\),

$$
z^*Kz
=
(P_{\mathbf1^\perp}z)^*K(P_{\mathbf1^\perp}z).
$$

Also,

$$
\|P_{\mathbf1^\perp}z\|^2
=
D-\frac{|\sum_jz_j|^2}{D}
=
D-\frac{|\operatorname{Tr}W|^2}{D}.
$$

Hence

$$
\boxed{
\|Q(W)\|_2^2
\le
\epsilon
\left(D^2-|\operatorname{Tr}W|^2\right).
}
\tag{8.1}
$$

Summing this over \(W=A_{ab}\),

$$
\begin{aligned}
\Theta_Q
&\le
\epsilon
\sum_{a,b}
\left(D^2-|\operatorname{Tr}A_{ab}|^2\right)\\
&=
m^2\epsilon(D^2-\alpha).
\end{aligned}
$$

Since \(x=\Theta_Q/m^2\),

$$
\boxed{
x\le\epsilon(D^2-\alpha).
}
\tag{Unitary-Q}
$$

The proposed unitary extension is correct.

---

# 9. Strongest direct scalar necessary system

Let

$$
q=m(A-1)=9(1+\eta)^2>9.
$$

Then

$$
A=1+\frac qm,
\qquad
2m\log\left(1+\frac qm\right)<\log m.
\tag{9.1}
$$

Every admissible tuple must produce real variables

$$
D,\alpha,r,u,v,n,\tau,i,a,b,h,x
$$

satisfying the following.

## 9.1 Dimension and one-copy constraints

$$
D\in\mathbb N,
\qquad
D>m,
$$

$$
\boxed{
\frac{D^2}{m}
\le
\alpha
\le
\frac{AD(D+1)}{m}-D
<
D^2.
}
\tag{9.2}
$$

Also

$$
r=\frac{\alpha}{D},
\quad
u=\alpha-1,
\quad
v=D-r,
\quad
n=D^2-1.
$$

## 9.2 Mixing and block positivity

$$
\boxed{
Dr^2\le\tau\le\sqrt A\,Dr^2.
}
\tag{9.3}
$$

Define

$$
h=\frac{\tau}{D}-r^2\ge0.
$$

Positivity of

$$
J=
\begin{pmatrix}r&z^*\\z&B\end{pmatrix}
$$

implies

$$
B\succeq\frac{zz^*}{r}.
$$

Hence

$$
\boxed{
h\le rv,
\qquad
a\ge\frac{h^2}{r^2}.
}
\tag{9.4}
$$

## 9.3 Trace-purity and rank constraints

$$
b=i-1,
\qquad
a=i-\frac{2\tau}{D}+r^2.
$$

For \(P\),

$$
\boxed{
\frac{u^2}{n}\le b\le u.
}
\tag{9.5}
$$

For \(B\),

$$
\boxed{
\frac{v^2}{m(m-1)}
\le a\le v^2.
}
\tag{9.6}
$$

Contraction adds

$$
\boxed{i\le\alpha.}
\tag{9.7}
$$

## 9.4 Alignment bounds

Define

$$
H_{\rm cen}
=
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}.
\tag{9.8}
$$

Then

$$
\boxed{
0\le x
\le
\min\left\{
H_{\rm cen},
\epsilon(D^2-\alpha),
v,
i-r
\right\}.
}
\tag{9.9}
$$

Here:

* \(x\le v\) follows from \(0\le P\le I\);
* \(x\le i-r\) follows from \(r+x=\operatorname{Tr}(JS)\le i\).

## 9.5 Exact symmetric-Bell endpoints

Define

$$
\begin{aligned}
\gamma_{\rm req}(i,\tau)
={}&
(D+2)i+(D+1)\tau\\
&+\frac12B_0(D,\alpha)\\
&-
\frac{A}{2m}
\alpha D(D+1)(D+3),
\end{aligned}
\tag{9.10}
$$

and

$$
\begin{aligned}
\gamma_{\rm up}(i,\tau)
=\frac12\Bigg[
&\frac{A}{m}
(\alpha+D)(D+2)(D+3)\\
&-
\left(
D^2+4D+\alpha^2+2(D+4)\alpha
\right)\\
&-2i-4\tau
\Bigg].
\end{aligned}
\tag{9.11}
$$

Then

$$
\boxed{
\gamma_{\rm req}(i,\tau)
\le r+x
\le
\gamma_{\rm up}(i,\tau).
}
\tag{9.12}
$$

Equivalently, scalar feasibility requires

$$
\boxed{
\max\{0,\gamma_{\rm req}-r\}
\le x
\le
\min\{
H_{\rm cen},
\epsilon(D^2-\alpha),
v,
i-r,
\gamma_{\rm up}-r
\}.
}
\tag{9.13}
$$

No lower bound on \(i\) or \(\tau\) has been substituted inside a nonmonotone expression in this system.

---

# 10. Near-\(PA\)-saturation is partially excluded

Let the \(PA\) slack be

$$
s:=AD(D+1)-m(\alpha+D)\ge0.
\tag{10.1}
$$

The upper endpoint \(\gamma_{\rm up}\) is strictly decreasing in both \(i\) and \(\tau\).

From B-rank,

$$
i\ge
\frac{2\tau}{D}-r^2+\frac{v^2}{m(m-1)}.
$$

After substituting this lower bound, the resulting upper endpoint remains decreasing in \(\tau\), so it is maximized at

$$
\tau=Dr^2,
\qquad
i=r^2+\frac{v^2}{m(m-1)}.
\tag{10.2}
$$

A direct expansion gives

$$
\boxed{
\begin{aligned}
\gamma_{\rm up}^{\rm rank}-r
={}&
\frac{(D+2)(D+3)(D+\alpha)}
{2Dm(D+1)}\,s\\
&+
\frac{
(D^2-\alpha)
\left[
m(m-1)(D+\alpha)
-(D+1)(D^2-\alpha)
\right]
}{
D^2m(D+1)(m-1)
}.
\end{aligned}
}
\tag{10.3}
$$

Define

$$
\Xi:=
(D+1)(D^2-\alpha)-m(m-1)(D+\alpha).
$$

If \(\Xi>0\), feasibility requires

$$
\boxed{
s\ge
\frac{
2(D^2-\alpha)\Xi
}{
D(D+2)(D+3)(D+\alpha)(m-1)
}.
}
\tag{10.4}
$$

Thus exact \(PA\)-saturation \(s=0\) is impossible whenever \(\Xi>0\).

This proves the anticipated near-boundary exclusion. It is not global: a modest positive \(PA\) slack can restore the upper endpoint.

---

# 11. Exact large-\(D\) scalar survivor

The full scalar system is not globally infeasible.

Choose

$$
q=10,
\qquad
\eta=\frac{\sqrt{10}}{3}-1,
\qquad
A=1+\frac{10}{m}.
$$

Let \(m\) be any sufficiently large multiple of \(5\), for example

$$
m>e^{20}.
$$

Then

$$
2m\log\left(1+\frac{10}{m}\right)<20<\log m,
$$

so Gap holds.

Set

$$
\boxed{
D=\frac{m^2}{5},
\qquad
\alpha=\frac{m^3}{25}.
}
\tag{11.1}
$$

Thus

$$
\alpha=\frac{D^2}{m},
\qquad
r=\frac m5.
$$

Choose

$$
\boxed{
\tau=Dr^2=\frac{m^4}{125},
}
\tag{11.2}
$$

and

$$
\boxed{
i=
r^2+\frac{(D-r)^2}{m(m-1)}
=
\frac{2m^2-m}{25}.
}
\tag{11.3}
$$

Then

$$
u=\frac{m^3}{25}-1,
\qquad
v=\frac{m(m-1)}5,
$$

$$
a=\frac{m(m-1)}{25},
\qquad
b=\frac{2m^2-m-25}{25}.
$$

Finally choose

$$
\boxed{x=0.}
\tag{11.4}
$$

This is only a scalar relaxation, not a tuple.

## 11.1 \(PA\), contraction, and rank

The exact \(PA\) slack is

$$
\boxed{
AD(D+1)-m(\alpha+D)
=
\frac{m(m^2+m+10)}5>0.
}
\tag{11.5}
$$

Also,

$$
\boxed{
\alpha-i=\frac{m(m-1)^2}{25}>0.
}
\tag{11.6}
$$

The B-rank inequality is saturated:

$$
a=\frac{v^2}{m(m-1)}.
$$

Moreover,

$$
v^2-a
=
\frac{m(m-1)(m^2-m-1)}{25}>0.
$$

## 11.2 Centered radicands

A direct calculation gives

$$
\boxed{
a-\frac{v^2}{n}
=
b-\frac{u^2}{n}
=
\frac{
m(m-1)
\left(m^4-25m^2+25m-25\right)
}{
25(m^2-5)(m^2+5)
}.
}
\tag{11.7}
$$

This is positive for all sufficiently large \(m\). Hence Centered-Align is well-defined, and \(x=0\) satisfies it.

Unitary-\(Q\), contraction, and \(x\le v\) are also automatic because all corresponding upper bounds are positive.

## 11.3 Exact endpoint check

For this family,

$$
\boxed{
\gamma_{\rm up}-r
=
\frac{
m^5+6m^4+35m^3+160m^2+410m+1500
}{250}
>0.
}
\tag{11.8}
$$

On the other hand,

$$
\boxed{
\begin{aligned}
\gamma_{\rm req}-r
={}&
-\frac{m}{1250}
\Big(
2m^6-5m^5+50m^4\\
&\qquad
-115m^3+360m^2-450m+350
\Big)
<0.
\end{aligned}
}
\tag{11.9}
$$

For \(m\ge3\), the polynomial in parentheses is positive; for example, group it as

$$
m^5(2m-5)
+
m^3(50m-115)
+
m(360m-450)
+
350.
$$

Thus

$$
\gamma_{\rm req}\le r+x\le\gamma_{\rm up}
$$

with \(x=0\).

Therefore:

$$
\boxed{
\text{Every scalar inequality listed in Section 9 survives exactly.}
}
$$

This disproves any attempted closure based only on that scalar system.

---

# 12. The exact realignment/coherent-state coupling omitted by the scalar system

For an actual tuple, \(J\) and \(S\) are not independent.

For every pure state \(\rho_y=|y\rangle\langle y|\),

$$
\begin{aligned}
\langle\langle\rho_y|S|\rho_y\rangle\rangle
&=
\operatorname{Tr}\bigl[\rho_y\Phi(\rho_y)\bigr]\\
&=
\|L(\rho_y)\|_2^2,
\end{aligned}
$$

while the Choi frame gives

$$
\begin{aligned}
\langle\langle\rho_y|J|\rho_y\rangle\rangle
&=
\frac1{m^2}
\sum_{a,b}
|\operatorname{Tr}(\rho_yA_{ab})|^2\\
&=
\|C(\rho_y)\|_2^2.
\end{aligned}
$$

For pure input, the two expressions are algebraically equal:

$$
\operatorname{Tr}
\left[
\rho_yA_{ab}\rho_yA_{ab}^*
\right]
=
|\langle y|A_{ab}|y\rangle|^2.
$$

Hence

$$
\boxed{
\langle\langle\rho_y|S|\rho_y\rangle\rangle
=
\langle\langle\rho_y|J|\rho_y\rangle\rangle
\quad
\forall y.
}
\tag{12.1}
$$

Write

$$
|\rho_y\rangle\rangle
=
\frac e{\sqrt D}+t_y,
\qquad
t_y\in e^\perp.
$$

Using the blocks (1.1), equation (12.1) becomes

$$
\boxed{
\langle t_y,(P-B)t_y\rangle
-
\frac{2}{\sqrt D}
\operatorname{Re}\langle z,t_y\rangle
=
\frac{r-1}{D}
\quad
\forall y.
}
\tag{12.2}
$$

This pointwise quartic identity is stronger than every scalar trace and purity relation used above.

When \(\tau=Dr^2\), one has \(z=0\), and it reduces to

$$
\boxed{
\langle t_y,(P-B)t_y\rangle
=
\frac{r-1}{D}
\quad
\forall y.
}
\tag{12.3}
$$

The scalar relaxation does not retain this identity.

---

# 13. Exact counterexample inside a decoupled operator relaxation

The preceding scalar survivor can be upgraded to a genuine operator model satisfying all of the following separately:

* \(0\le P\le P_\perp\);
* the exact Pure-\(Q\) coherent-state bound;
* correct \(\operatorname{Tr}P\) and \(\operatorname{Tr}P^2\);
* a positive Choi matrix \(\widetilde J\) with correct unital and trace-preserving marginals;
* an exact rank-\(m(m-1)\) unitary frame for \(B\);
* matching \(\alpha,i,\tau\);
* all scalar and symmetric-Bell endpoint constraints.

What is not imposed is

$$
\widetilde J=\operatorname{realign}(P_0+P)
$$

or the existence of one tuple whose pair differences give that frame.

This precisely shows what remains missing.

## 13.1 Dimensions

Choose \(m\) to be a sufficiently large multiple of \(10\), and retain

$$
D=\frac{m^2}{5}.
$$

Then \(D=2d\) is even.

Decompose

$$
\mathbb C^D=\mathbb C^d\oplus\mathbb C^d.
$$

Inside the Hilbert–Schmidt space \(M_D\), let

* \(\mathcal H_\times\) be the cross-block matrices;
* \(\mathcal H_\parallel\) be the block-diagonal traceless matrices.

Their dimensions are

$$
R_\times=\frac{D^2}{2},
\qquad
R_\parallel=\frac{D^2}{2}-1,
$$

and

$$
R_\times+R_\parallel=n.
$$

Let \(\Pi_\times,\Pi_\parallel\) be their orthogonal projections.

## 13.2 Choosing the spectrum of \(P\)

Retain

$$
u=\frac{m^3}{25}-1,
\qquad
b=\frac{2m^2-m-25}{25}.
$$

Set

$$
\Delta=b-\frac{u^2}{n}.
$$

Explicitly,

$$
\boxed{
\Delta=
\frac{
m(m-1)(m^4-25m^2+25m-25)
}{
25(m^2-5)(m^2+5)
}>0.
}
\tag{13.1}
$$

Put

$$
\lambda_0=\frac un,
$$

and define

$$
\boxed{
\lambda_\times
=
\lambda_0+
\sqrt{
\frac{R_\parallel\Delta}
{R_\times n}
},
}
\tag{13.2}
$$

$$
\boxed{
\lambda_\parallel
=
\lambda_0-
\sqrt{
\frac{R_\times\Delta}
{R_\parallel n}
}.
}
\tag{13.3}
$$

Then

$$
R_\times\lambda_\times
+
R_\parallel\lambda_\parallel
=u,
$$

and

$$
R_\times\lambda_\times^2
+
R_\parallel\lambda_\parallel^2
=b.
$$

Define

$$
\boxed{
P=
\lambda_\times\Pi_\times
+
\lambda_\parallel\Pi_\parallel.
}
\tag{13.4}
$$

### Positivity

The exact expression

$$
\boxed{
\lambda_0^2
-
\frac{R_\times\Delta}{R_\parallel n}
=
\frac{
m^5+25m^4-100m^3+1250
}{
(m^2-5)(m^2+5)(m^4-50)
}
>0
}
\tag{13.5}
$$

shows that \(\lambda_\parallel>0\).

Also,

$$
\lambda_\times
\le\frac{u}{R_\times}
<\frac2m<1.
$$

Hence

$$
0\le P\le P_\perp.
$$

## 13.3 Exact coherent-state bound

Let

$$
y=y_1\oplus y_2,
\qquad
s=\|y_1\|^2.
$$

For \(\rho_y=|y\rangle\langle y|\),

$$
\|\Pi_\times\rho_y\|_2^2
=
2s(1-s)\le\frac12,
$$

and

$$
\|\Pi_\parallel\rho_y\|_2^2
=
1-\frac1D-2s(1-s).
$$

Therefore

$$
\begin{aligned}
\langle\langle\rho_y|P|\rho_y\rangle\rangle
={}&
\lambda_\parallel\left(1-\frac1D\right)\\
&+
(\lambda_\times-\lambda_\parallel)2s(1-s).
\end{aligned}
$$

Using \(2s(1-s)\le1/2\),

$$
\begin{aligned}
\langle\langle\rho_y|P|\rho_y\rangle\rangle
&\le
\frac{\lambda_\times+\lambda_\parallel}{2}
-\frac{\lambda_\parallel}{D}.
\end{aligned}
$$

Because \(R_\times>R_\parallel\),

$$
\lambda_\times+\lambda_\parallel\le2\lambda_0.
$$

Thus

$$
\langle\langle\rho_y|P|\rho_y\rangle\rangle
\le\lambda_0.
$$

Finally,

$$
\boxed{
\epsilon-\lambda_0
=
\frac{
5(m^4+5m^2-5m-25)
}{
m^2(m^2-5)(m^2+5)
}
>0.
}
\tag{13.6}
$$

Hence

$$
\boxed{
\sup_y
\langle\langle\rho_y|P|\rho_y\rangle\rangle
\le\epsilon.
}
\tag{13.7}
$$

This is exactly the coherent-state Pure-\(Q\) constraint.

---

## 13.4 A rank-\(m(m-1)\) unitary frame

Let \(\{V_\ell\}_{\ell=1}^{d^2}\) be an orthogonal unitary error basis of \(M_d\).

The \(2d^2=D^2/2\) matrices

$$
W_{\ell,+}
=
\begin{pmatrix}
0&V_\ell\\
V_\ell&0
\end{pmatrix},
\qquad
W_{\ell,-}
=
\begin{pmatrix}
0&V_\ell\\
-V_\ell&0
\end{pmatrix}
\tag{13.8}
$$

are unitary, traceless, pairwise Hilbert–Schmidt orthogonal, and span \(\mathcal H_\times\).

Similarly, the matrices

$$
\begin{pmatrix}
V_\ell&0\\
0&V_\ell
\end{pmatrix},
\qquad
\begin{pmatrix}
V_\ell&0\\
0&-V_\ell
\end{pmatrix}
\tag{13.9}
$$

form an orthogonal unitary basis of the block-diagonal space; after removing the identity, they span \(\mathcal H_\parallel\).

Let

$$
k=m(m-1).
$$

Since \(D\gg m\),

$$
k<R_\times,\qquad k<R_\parallel.
$$

Choose any \(k\) orthogonal traceless unitaries \(W_1,\ldots,W_k\) from either subspace and define

$$
\boxed{
B=
\frac1{m^2}
\sum_{j=1}^k
|W_j\rangle\rangle\langle\langle W_j|.
}
\tag{13.10}
$$

Because \(\|W_j\|_2^2=D\),

$$
\operatorname{rank}B=k,
$$

$$
\operatorname{Tr}B
=
\frac{kD}{m^2}
=
\frac{D(m-1)}m
=
v,
$$

and

$$
\operatorname{Tr}B^2
=
\frac{kD^2}{m^4}
=
\frac{v^2}{k}
=
a.
$$

Thus B-rank is saturated.

Define

$$
\boxed{
\widetilde J
=
rP_0+B.
}
\tag{13.11}
$$

Equivalently,

$$
\widetilde J
=
\frac1{m^2}
\left[
m|I\rangle\rangle\langle\langle I|
+
\sum_{j=1}^k
|W_j\rangle\rangle\langle\langle W_j|
\right].
\tag{13.12}
$$

There are exactly

$$
m+k=m^2
$$

unitary frame elements, counting the \(m\) identity copies.

Every frame element is unitary, so

$$
\operatorname{Tr}_1\widetilde J
=
\operatorname{Tr}_2\widetilde J
=
I_D.
$$

Also,

$$
\langle\langle I|\widetilde J|I\rangle\rangle
=
\frac{D^2}{m}
=
\alpha,
$$

$$
\langle\langle I|\widetilde J^2|I\rangle\rangle
=
Dr^2
=
\tau,
$$

and

$$
\operatorname{Tr}\widetilde J^2
=
r^2+a
=
i.
$$

Meanwhile, with

$$
\widetilde S=P_0+P,
$$

one has

$$
\operatorname{Tr}\widetilde S=\alpha,
\qquad
\operatorname{Tr}\widetilde S^2=i.
$$

Thus all scalar traces and purities match exactly.

## 13.5 Alignment can be placed in either spectral sector

If the selected frame lies in \(\mathcal H_\times\),

$$
\operatorname{Tr}(BP)=v\lambda_\times.
$$

If it lies in \(\mathcal H_\parallel\),

$$
\operatorname{Tr}(BP)=v\lambda_\parallel.
$$

As \(m\to\infty\),

$$
\lambda_\times
=
\frac2m-\frac1{2m^2}+O(m^{-3}),
$$

$$
\lambda_\parallel
=
\frac1{2m^2}+O(m^{-3}).
$$

Thus the same separate spectral data permit alignments ranging from

$$
v\lambda_\parallel=\frac1{10}+O(m^{-1})
$$

to

$$
v\lambda_\times=\frac{2m}{5}+O(1).
$$

Both are compatible with the exact symmetric-Bell endpoints because

$$
\gamma_{\rm req}-r<0
$$

and

$$
\gamma_{\rm up}-r-D
=
\frac{
m^5+6m^4+35m^3+110m^2+410m+1500
}{250}
>0.
$$

Since \(v\lambda_\times<v<D\), both choices satisfy

$$
\gamma_{\rm req}\le r+x\le\gamma_{\rm up}.
$$

---

# 14. What the relaxed construction proves—and does not prove

The construction in Section 13 is not an admissible tuple for \((E1_{\rm gap})\). It deliberately does not establish

$$
\widetilde J=\operatorname{realign}(\widetilde S),
$$

and the \(m^2\) unitary frame elements are not shown to have the cocycle form

$$
W_{ab}=U_b^*U_a
$$

for one \(m\)-tuple.

It does prove the following exact negative result:

> Low rank of \(B\), a unitary frame for \(B\), positivity and contraction of \(P\), the uniform coherent-state Pure-\(Q\) bound, matching traces and purities, Choi marginal constraints, MM, PA, Centered-Align, Unitary-\(Q\), and the symmetric-Bell endpoints do not jointly imply a contradiction when the same-map realignment and pair-difference cocycle are omitted.

Thus no completion based only on those separate properties can settle \((E1_{\rm gap})\).

---

# 15. Earliest exact operator gap

For an actual tuple, one must simultaneously impose

$$
\boxed{
J=\operatorname{realign}(P_0+P)
=
\frac1{m^2}
\sum_{a,b}
|U_b^*U_a\rangle\rangle
\langle\langle U_b^*U_a|,
}
\tag{15.1}
$$

together with

$$
0\le P\le P_\perp,
\qquad
\sup_y
\langle\langle\rho_y|P|\rho_y\rangle\rangle
\le\epsilon,
\tag{15.2}
$$

and the pointwise coupling

$$
\boxed{
\langle t_y,(P-B)t_y\rangle
-
\frac{2}{\sqrt D}\operatorname{Re}\langle z,t_y\rangle
=
\frac{r-1}{D}
\quad\forall y.
}
\tag{15.3}
$$

The first missing implication is:

> **Realignment–pair-frame implication, OPEN.**
> Prove that every \(P,B,z\) arising from one frozen pair-difference tuple and satisfying (15.1)–(15.3), Gap, PA, and Pure-\(Q\), obeys an additional inequality that makes the interval (9.13) empty; or construct one tuple for which the full pointwise ratio bound holds.

No such inequality is proved here. The exact large-\(D\) scalar and decoupled-operator constructions show that it must use the actual realignment/cocycle coupling, not merely ranks, traces, purities, marginals, or coherent-state bounds considered separately.

---

# Audit ledger

| Status           | Statement                                                                                                                                            |                                                           |       |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----- |
| **PROVED**       | \(\mathsf I_U-\mathsf C_U=\frac{m^4}{2}\|S-J\|_2^2\).                                                                                                |                                                           |       |
| **PROVED**       | The proposed \(RD\text{-}PT2\) formula.                                                                                                              |                                                           |       |
| **REDUNDANT**    | \(RD\text{-}PT2\), because it is exactly \(x\le(a+b)/2\), weaker than Align.                                                                         |                                                           |       |
| **PROVED**       | Centered-Align, including all trace corrections and radicands.                                                                                       |                                                           |       |
| **PROVED**       | Centered-Align is never weaker than uncentered Align.                                                                                                |                                                           |       |
| **PROVED**       | The trace-centered escape and its exact factorization (4.3).                                                                                         |                                                           |       |
| **PROVED**       | (B=m^{-2}\sum_{a\ne b}                                                                                                                               | P_\perp A_{ab}\rangle\rangle\langle\langle P_\perp A_{ab} | ).    |
| **PROVED**       | \(\operatorname{rank}B\le m(m-1)\).                                                                                                                  |                                                           |       |
| **PROVED**       | B-rank and I-rank.                                                                                                                                   |                                                           |       |
| **PROVED**       | Gap, PA, and \(\alpha\ge D^2/m\) imply \(D>m\).                                                                                                      |                                                           |       |
| **PROVED**       | \(0\le S\le I\), \(0\le P\le P_\perp\), and \(i\le\alpha\).                                                                                          |                                                           |       |
| **PROVED**       | Unitary-\(Q\): (|Q(W)|_2^2\le\epsilon(D^2-                                                                                                           | \operatorname{Tr}W                                        | ^2)). |
| **PROVED**       | The complete direct scalar necessary system (9.1)–(9.13).                                                                                            |                                                           |       |
| **PROVED**       | Exact near-\(PA\)-saturation exclusion (10.3)–(10.4).                                                                                                |                                                           |       |
| **DISPROVED**    | Global infeasibility of the scalar system.                                                                                                           |                                                           |       |
| **PROVED**       | Exact large-\(D\) scalar survivor (11.1)–(11.9).                                                                                                     |                                                           |       |
| **DISPROVED**    | The claim that B-rank plus \(C_{\rm up}\), Centered-Align, and Unitary-\(Q\) close the two dimension regimes.                                        |                                                           |       |
| **PROVED**       | The pointwise same-map identity (12.2).                                                                                                              |                                                           |       |
| **PROVED — new** | Exact decoupled operator model with positive \(P\), uniform Pure-\(Q\), positive bistochastic \(\widetilde J\), and a rank-\(m(m-1)\) unitary frame. |                                                           |       |
| **DISPROVED**    | Sufficiency of the separate low-rank, frame, coherent-state, contraction, marginal, and endpoint constraints without realignment/cocycle coupling.   |                                                           |       |
| **OPEN**         | The realignment–pair-frame implication (15.1)–(15.3).                                                                                                |                                                           |       |
| **OPEN**         | Existence or nonexistence of one actual tuple satisfying \((E1_{\rm gap})\).                                                                         |                                                           |       |
| **OPEN**         | \((E1_{\rm gap})\).                                                                                                                                  |                                                           |       |
| **CONJECTURED**  | None promoted.                                                                                                                                       |                                                           |       |

The first new statement requiring independent verification is the exact decoupled operator construction in Section 13, especially the simultaneous coherent-state estimate (13.7) and unitary-frame realization (13.10)–(13.12).

The full-size theorem remains open because the finite \(r=2\) gate remains open, independently of the separate all-copy gate.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-06-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-06-local-audit.md bytes=6833 sha256=eda16191369ac890d90cee1b911fbfb2f21acc8d121525fecf8707f754a9fe13 -->

# Round 06 independent local audit

## Capture integrity

- Conversation: `Audit quantum construction`
- Mode/model observed at send time: ordinary Chat, GPT-5.6 Sol, Pro 5/5
- Browser completion indicator: `Worked for 20m 30s`
- Captured response: 31,934 bytes; 31,898 Unicode characters
- SHA-256: `9fb8abbde279c6c61c9294fa24f57a84ed140e921eeacb056c83cf88f885e55d`
- The artifact and output copies are byte-identical.

## Verdict

**OPEN WITH EARLIEST GAP.** Round 6 does not prove or disprove `(E1_gap)`. Its main negative result survives audit: the full scalar relaxation, and even a substantially stronger relaxation in which the Liouville and Choi sides are built separately, remain feasible. The first unresolved implication in this proof route must use the fact that the same map supplies both sides through exact realignment together with the pair-difference/autocorrelation structure.

No conclusion about the separate all-copy gate changes.

## Claims independently verified

1. **Realignment defect.** Equal Hilbert--Schmidt norms of the Liouville and Choi reshufflings give

   ```text
   I_U - C_U = (m^4/2) ||S-J||_2^2.
   ```

   In the block decomposition, dropping `||P-B||_2^2` yields the advertised `RD-PT2`. After substituting `C_U/m^4=r+x`, it is exactly `x <= (a+b)/2`, and is weaker than `x <= sqrt(ab)` by AM--GM.

2. **Centered alignment.** Centering `B` and `P` on the `n=D^2-1` dimensional traceless space gives the stated upper bound. Both radicands are nonnegative trace-purity defects. The comparison with uncentered alignment reduces to the cosine inequality

   ```text
   xi*zeta + sqrt(1-xi^2)*sqrt(1-zeta^2) <= 1.
   ```

   The response's equality conditions are correct.

3. **Low Choi rank and `D>m`.** The `m` diagonal pair differences are identities and vanish after traceless compression, leaving at most `m(m-1)` rank-one terms. The purity bound `a >= v^2/[m(m-1)]` and the derived `I-rank` inequality follow. Combining PA with `alpha >= D^2/m` gives `D >= (m-A)/(A-1)`; Gap implies `A < 2m/(m+1)`, hence `D>m`.

4. **Contraction.** A convex average of unitary conjugations is a Hilbert--Schmidt contraction. Thus `0 <= S=L^*L <= I`, `Se=e`, `0 <= P <= P_perp`, and `i<=alpha`.

5. **Unitary-Q.** Diagonalizing a unitary `W`, forming the Gram matrix of the `Q(rho_j)`, using its zero-sum vector, and applying `lambda_max(K)<=Tr(K)<=D epsilon` gives

   ```text
   ||Q(W)||_2^2 <= epsilon (D^2-|Tr W|^2).
   ```

   Summing over all pair differences gives `x <= epsilon(D^2-alpha)` with the stated normalization.

6. **Same-map pure-state identity.** For every pure projector `rho_y`, both `Tr[rho_y Phi(rho_y)]` and the Choi-frame quadratic form equal the same average of `|<y|U_b^*U_a|y>|^2`. Expanding `|rho_y>>=e/sqrt(D)+t_y` yields equation (12.2) with the displayed sign and factor `2/sqrt(D)`.

## Exact symbolic checks

The response formulas were re-expanded with exact rational symbolic algebra, not floating-point sampling.

| Formula | Result |
| --- | --- |
| Near-PA factorization (10.3) | Exact identity |
| PA slack (11.5) | `m(m^2+m+10)/5` |
| Contraction slack (11.6) | `m(m-1)^2/25` |
| Both centered radicands (11.7) | Exact and equal |
| Endpoint formulas (11.8), (11.9) | Exact identities |
| Spectral defect `Delta` (13.1) | Exact identity |
| Positivity certificate (13.5) | Exact identity |
| Coherent-state slack (13.6) | Exact identity |

The asymptotics also agree:

```text
lambda_cross    = 2/m - 1/(2m^2) - 101/(8m^3) + O(m^-4),
lambda_parallel = 1/(2m^2) + 101/(8m^3) + O(m^-4).
```

Therefore the weaker `O(m^-3)` statements in the response are valid.

## Scalar-survivor audit

For `q=10`, sufficiently large `m` divisible by `5`,

```text
D=m^2/5,  alpha=m^3/25,  r=m/5,
tau=m^4/125,
i=m(2m-1)/25,
x=0,
```

satisfy Gap, PA, `alpha>=D^2/m`, strict `alpha<D^2`, MM, both trace-purity conditions, B-rank, contraction, block positivity, Unitary-Q, Centered-Align, Pair-energy, and both symmetric-Bell endpoints. Thus a purely scalar contradiction is impossible from the displayed system.

One correction is needed: Section 9 is not literally the *strongest* scalar system obtainable from centered Cauchy--Schwarz, because it omits the companion lower bound

```text
x >= uv/n - sqrt[(a-v^2/n)(b-u^2/n)].
```

Together with `x>=0`, this should be included as a maximum. It does not damage the survivor. For the family above its omitted lower endpoint is exactly

```text
-m(m-1)(m^2-5m-20) / [25(m^2+5)] < 0,
```

so `x=0` still satisfies the corrected two-sided centered inequality.

Section 10 also does not give a full analytic partition of every near-minimal dimension. It proves the narrower, exact statement that when `Xi>0`, feasibility forces the PA slack to exceed (10.4). That is useful but should not be described as a complete dimension-regime exclusion.

## Decoupled operator construction audit

Subject to its explicit relaxation boundary, Section 13 is algebraically sound.

- The two traceless Hilbert--Schmidt sectors have dimensions `D^2/2` and `D^2/2-1`.
- Equations (13.2)--(13.4) give exactly the required trace and purity for `P`.
- Equation (13.5) makes `lambda_parallel>0`; positivity then gives `lambda_cross<u/R_cross<2/m<1`.
- The cross/block projection calculation for a pure state is correct, and (13.6) verifies the uniform coherent-state bound.
- A unitary error basis containing the identity supplies the stated orthogonal cross and block-diagonal traceless unitaries. With `k=m(m-1)`, the frame in (13.10) has trace `v`, purity `a`, rank `k`, and correct Choi marginals.
- `J_tilde=rP_0+B` has the advertised `alpha`, `tau`, and `i`; placing `B` in either spectral sector gives the stated alignment range, and both choices lie inside the very wide endpoint interval.

This is **not** an admissible counterexample to `(E1_gap)`: `J_tilde` is not shown to be the realignment of the chosen `S_tilde=P_0+P`, and its off-diagonal unitary frame is not shown to be the pair-difference frame of one `m`-tuple. The response states those limitations correctly. It proves only that the listed properties, when imposed separately, are insufficient.

The Markdown audit ledger has two malformed rows because vertical bars inside ket/norm notation were not escaped. This is a presentation defect only; it does not change the mathematical claims.

## Earliest remaining gate

Within this chain, the earliest unresolved step is to exploit simultaneously

```text
J = realign(P_0+P)
  = m^-2 sum_(a,b) |U_b^*U_a>><<U_b^*U_a|,
```

the uniform coherent-state bound on `P`, and the fact that the frame is an autocorrelation/pair-difference frame of one frozen tuple. Neither the scalar survivor nor the decoupled model resolves that coupled condition.

Status: **COMPLETED — LOCALLY AUDITED; `(E1_gap)` AND THE FULL-SIZE THEOREM REMAIN OPEN.**

<!-- END HISTORICAL FILE path=outputs/round-06-local-audit.md -->


# ROUND 007

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-07-prompt.md bytes=8161 sha256=7ff991bfd36a029069255893385a243691d2e0cedaaa47ce8175d7b8c81efd76 -->

# Round 7 — put the Choi frame back into one Weyl--Sidon autocorrelation tuple

Continue in the same deterministic one-layer setup and the same conversation.
This round is confined to the finite `r=2` low-`A` gate.

Let finite `m,D`, `eta>0`, and one frozen tuple

    U=(U_1,...,U_m) in U(D)^m

define

    C(X)_(v,w)=m^(-1) Tr(X U_w^*U_v),
    L(X)=m^(-1) sum_v U_v X U_v^*,
    Q=L-Delta_D,
    Phi=L^*L,

    A=1+9(1+eta)^2/m,
    p=sup_rho ||C(rho)||_2^2,

with

    ln m>18,
    A^2<m^(1/m),
    p<=A/m.

For every `T in M_D` with `||T||_2=1`, put

    rho_T=TT^*,
    X_vw(T)=T(U_w^*U_v)^T T^*,
    d_T=||C(rho_T)||_2^2,

    R_U(T)=
      [sum_(v!=w)||C(X_vw(T))||_2^2]
      /[m d_T],

    kappa_1(U)=sup_T R_U(T).

The target remains

    (E1_gap): kappa_1(U)<=A-1

for one finite tuple satisfying every condition above.

Give a public, self-contained derivation and no hidden chain-of-thought.

## Audited Round 6 boundary

The Round 6 response and an independent local equation audit established:

1. `RD`, `RD-PT2`, Centered-Align, B-rank, Contract, and Unitary-Q are
   correct.
2. `RD-PT2` is redundant with uncentered alignment.
3. The scalar system remains feasible. One exact survivor uses `q=10`,

       D=m^2/5,
       alpha=m^3/25,
       r=m/5,
       tau=m^4/125,
       i=m(2m-1)/25.

4. The decoupled operator construction in Round 6 is valid only after
   allowing its Liouville operator `S=P_0+P` and its Choi operator
   `J_tilde=rP_0+B` to be chosen independently. It is not an actual tuple.
5. For an actual tuple, with

       J=[[r,z^*],[z,B]],
       |rho_y>>=e/sqrt(D)+t_y,

   exact realignment gives the pointwise identity

       <t_y,(P-B)t_y>
       -(2/sqrt(D)) Re<z,t_y>
       =(r-1)/D                         (SamePure)

   for every unit vector `y`.

One correction to Round 6 must be retained. Centered Cauchy--Schwarz is
two-sided, so the scalar system should also contain

    x >= uv/n
         -sqrt[(a-v^2/n)(b-u^2/n)],

besides `x>=0`. For the exact scalar survivor above, the omitted lower
endpoint equals

    -m(m-1)(m^2-5m-20)/[25(m^2+5)]<0,

so this correction does not remove the survivor.

Do not claim that Round 6 supplied a full near-minimal-`D` partition. It
proved only its conditional PA-slack exclusion (10.3)--(10.4).

## A structured way to restore the pair-difference cocycle

The Round 6 decoupled frame need not remain arbitrary. Test the following
genuine one-tuple construction.

Let `D` be an odd prime and let

    {W_g : g in F_D^2}

be the standard generalized Weyl unitary error basis, with phases fixed once
and

    Tr(W_g^* W_h)=D delta_(g,h).

Choose distinct field elements

    t_1,...,t_m in F_D

and set

    s_a=(t_a,t_a^2),
    U_a=W_(s_a).

For `a!=b`, the proposed ordered difference label is

    g_ab=s_a-s_b
        =(t_a-t_b,(t_a-t_b)(t_a+t_b)).

Because `D` is odd, the candidate Sidon calculation says

    g_ab=g_cd, a!=b, c!=d
      implies (a,b)=(c,d).

Projective Weyl phases do not affect the rank-one Choi frame. If the Sidon
calculation is correct, every off-diagonal `A_ab=U_b^*U_a` is traceless and
all `m(m-1)` off-diagonal pair differences are Hilbert--Schmidt orthogonal.

Audit the following exact consequences:

    alpha=D^2/m,
    r=D/m,
    z=0,
    tau=D^3/m^2,

    B=(D/m^2) Pi_Gamma,
    rank(B)=m(m-1),
    a=Tr(B^2)=D^2(m-1)/m^3,

    i=Tr(J^2)=D^2(2m-1)/m^3.

Here `Pi_Gamma` is the orthogonal projection onto the span of the nonzero
pair-difference Weyl operators. These formulas would exactly saturate the
B-rank/I-rank bounds and would remove the `pair-difference frame omitted`
qualification from the Choi side of Round 6. They would **not** yet identify
the freely chosen `P` from Round 6 with the realignment of this `J`.

## The realigned Liouville side

For this actual Weyl tuple, derive rather than assume the multiplier formula

    L(W_h)=phi(h) W_h,

    phi(h)=m^(-1) sum_a chi_h(s_a),

with the correct symplectic character and phase convention. Thus

    Phi(W_h)=|phi(h)|^2 W_h,

so the actual `P` is diagonal in the nonidentity Weyl basis and its
eigenvalues are `|phi(h)|^2`.

Use Parseval and the exact additive energy of the Sidon set to recover

    Tr(P)=alpha-1,
    Tr(P^2)=i-1.

This is the exact same-map realignment coupling for the proposed family; `P`
is no longer free.

For a pure state `rho`, audit the exact formula

    ||L(rho)||_2^2
      =D^(-1) sum_h |phi(h)|^2
         |Tr(W_h^* rho)|^2.                    (PureFourier)

The one-copy problem is to prove this is at most `A/m` for **every** pure
state, not only on average.

## Stabilizer-line necessary test

For a Weyl stabilizer state associated with an isotropic line `ell`, character
orthogonality should give, up to the conventionally correct perpendicular
line,

    ||L(rho_ell)||_2^2
      =[m+N_ell]/m^2,                          (Line)

where `N_ell` is the number of ordered nonzero differences `g_ab` lying on
that line.

For the parabolic labels, a nonvertical difference has slope `t_a+t_b`.
Hence the proposed count is

    N_s=2 r_s,

where `r_s` is the number of unordered pairs `{a,b}`, `a!=b`, with

    t_a+t_b=s.

Writing

    q=m(A-1)=9(1+eta)^2,

the stabilizer tests alone require

    N_s<=q

for every `s`. In particular, at `q=10`, every field sum may occur for at
most five unordered pairs.

Audit every normalization and make clear that `(Line)` is only a family of
necessary pure-state tests unless a theorem proves stabilizers maximize
`(PureFourier)`.

## Exact tasks

1. Give one verdict on `(E1_gap)`: PROVED, DISPROVED, or OPEN WITH EARLIEST
   GAP. Do not promote a scalar, stabilizer-only, or averaged test.

2. Audit the Round 6 correction above. Then independently prove or refute the
   Weyl--Sidon uniqueness, Choi-frame, invariant, multiplier, additive-energy,
   PureFourier, and stabilizer-line formulas. Correct phases, transposes, and
   symplectic perpendiculars explicitly.

3. Determine whether there are exact finite parameters satisfying Gap and
   `D>m`, with odd prime `D` in a controlled `Theta(m^2)` range, and an
   explicit or rigorously frozen set `{t_a}` satisfying all stabilizer-line
   counts. You may use a deterministic construction or a complete
   probabilistic existence proof, but the final tuple must be one frozen
   finite set. A union-bound slogan is not a proof.

4. Settle the **full one-copy supremum** for this family. Do exactly one of:

   (a) prove `p<=A/m` uniformly over every pure state for one frozen set;

   (b) prove that every such parabolic Sidon set has a deterministic pure
       state with output purity greater than `A/m`; or

   (c) isolate the earliest exact inequality on the physical Weyl
       characteristic vector

           r_h=Tr(W_h^* rho)

       that is still missing. Parseval alone and the crude maximum Fourier
       multiplier are not enough unless proved sharp for physical pure
       states. Do not assume stabilizers maximize.

5. If one frozen tuple passes the one-copy gate, derive `R_U(T)` for the same
   tuple in exact phase-space form and attack the all-`T` ratio. Closure still
   requires either:

   (a) a physical `T` with `R_U(T)>A-1` for every admissible tuple in this
       family; or

   (b) one frozen finite tuple with `R_U(T)<=A-1` for every Hilbert--Schmidt
       unit `T`.

   A stabilizer-only calculation is not an all-`T` result.

6. If this family cannot close the gate, state the first precise missing
   combinatorial or operator inequality. Separate:

   - exact identities,
   - necessary tests,
   - existence results,
   - conjectures.

7. This is not the full-Weyl tuple: only `m` Weyl operators are selected and
   `D>m`. Do not use the `m=D^2` full-Weyl loophole, WHGAP, numerical evidence
   as proof, copy-dependent tuples, independent-local-Haar averaging that
   erases orientation, or claims about the separate all-copy gate.

8. End with an audit ledger separating PROVED, DISPROVED, REDUNDANT, OPEN,
   and CONJECTURED. Identify the first new claim requiring independent
   verification.

The full-size theorem remains OPEN unless `(E1_gap)` and the separate
all-copy gate are both closed.

<!-- END HISTORICAL FILE path=work/round-07-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-07-response.md bytes=26574 sha256=21f81f4f3452848a1cc9a979fd741c88c2686af432ac037bd89f2fd6ef5f79bf -->

# Verdict

$$
\boxed{\text{\((E1_{\mathrm{gap}})\) remains OPEN WITH EARLIEST GAP.}}
$$

The proposed parabolic Weyl tuple does restore the missing pair-difference cocycle exactly:

* the ordered nonzero differences are all distinct;
* the traceless Choi block has rank exactly \(m(m-1)\);
* the Choi invariants saturate the Round 6 rank lower bounds;
* the realigned Liouville operator is exactly diagonal in the Weyl basis, with eigenvalues \(|\phi(h)|^2\).

There also exist fully explicit, frozen finite choices with

$$
q:=m(A-1)=10,\qquad D=\Theta(m^2),
$$

for which every stabilizer-line test passes, in fact with \(N_\ell\le2\).

The first unresolved requirement is already the full one-copy inequality

$$
\boxed{
\sup_{\rho\ {\rm pure}}
\sum_{g\in\Gamma}
\left|\operatorname{Tr}(W_g^*\rho)\right|^2
\le 10,
}
\tag{PW10}
$$

where

$$
\Gamma=\{s_a-s_b:a\ne b\}.
$$

This is an exact necessary and sufficient reformulation of \(p\le A/m\) for the constructed tuple. Parseval, additive energy, stabilizer tests, and the maximum Liouville multiplier do not prove it. Since the one-copy gate remains open for this family, the uniform all-\(T\) ratio gate also remains open.

---

# 1. Round 6 centered-alignment correction

On the \(n=D^2-1\) dimensional space \(e^\perp\), write

$$
B=\frac vnP_\perp+B_0,\qquad
P=\frac unP_\perp+P_1,
$$

with

$$
\operatorname{Tr}B_0=\operatorname{Tr}P_1=0.
$$

Then

$$
x:=\operatorname{Tr}(BP)
=
\frac{uv}{n}+\operatorname{Tr}(B_0P_1).
$$

Therefore Hilbert–Schmidt Cauchy–Schwarz is indeed two-sided:

$$
\boxed{
\frac{uv}{n}
-
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}
\le x
\le
\frac{uv}{n}
+
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}.
}
\tag{1.1}
$$

Positivity also gives \(x\ge0\), so the actual scalar lower endpoint is the maximum of \(0\) and the left side of (1.1).

For the exact Round 6 scalar survivor

$$
D=\frac{m^2}{5},\qquad
\alpha=\frac{m^3}{25},\qquad
\tau=\frac{m^4}{125},\qquad
i=\frac{m(2m-1)}{25},
$$

the two centered variances are equal, and direct substitution gives

$$
\boxed{
\frac{uv}{n}
-
\sqrt{
\left(a-\frac{v^2}{n}\right)
\left(b-\frac{u^2}{n}\right)
}
=
-\frac{m(m-1)(m^2-5m-20)}
{25(m^2+5)}.
}
\tag{1.2}
$$

This is negative for the large \(m\) relevant here. Thus the omitted lower endpoint does not remove that scalar survivor.

---

# 2. Convention-fixed Weyl system

Let \(D\) be an odd prime, let

$$
\omega=e^{2\pi i/D},
$$

and interpret \(1/2\) in the exponents as the inverse of \(2\) in \(\mathbb F_D\).

On the computational basis \(\{|x\rangle:x\in\mathbb F_D\}\), define

$$
X|x\rangle=|x+1\rangle,\qquad
Z|x\rangle=\omega^x|x\rangle.
$$

For \(g=(p,q)\in\mathbb F_D^2\), set

$$
\boxed{
W_g=\omega^{-pq/2}Z^pX^q.
}
\tag{2.1}
$$

Use the symplectic form

$$
[g,h]=ps-qr,
\qquad
h=(r,s).
$$

A direct calculation gives

$$
\boxed{
W_gW_h=\omega^{[g,h]/2}W_{g+h},
}
\tag{2.2}
$$

$$
W_g^*=W_{-g},
\tag{2.3}
$$

$$
\boxed{
W_gW_hW_g^*
=
\omega^{[g,h]}W_h,
}
\tag{2.4}
$$

and

$$
\boxed{
\operatorname{Tr}(W_g^*W_h)=D\delta_{g,h}.
}
\tag{2.5}
$$

In particular,

$$
\operatorname{Tr}W_g=
\begin{cases}
D,&g=0,\\
0,&g\ne0.
\end{cases}
\tag{2.6}
$$

The transpose in this basis is

$$
\boxed{
W_{(p,q)}^{\mathsf T}=W_{(p,-q)}.
}
\tag{2.7}
$$

Indeed,

$$
(Z^pX^q)^{\mathsf T}=X^{-q}Z^p
=\omega^{pq}Z^pX^{-q}.
$$

Define the involution

$$
\vartheta(p,q)=(p,-q).
\tag{2.8}
$$

---

# 3. Parabolic ordered-difference uniqueness

Take distinct \(t_1,\ldots,t_m\in\mathbb F_D\) and set

$$
s_a=(t_a,t_a^2),
\qquad
U_a=W_{s_a}.
$$

For \(a\ne b\),

$$
g_{ab}:=s_a-s_b
=
\bigl(t_a-t_b,\ t_a^2-t_b^2\bigr)
$$

and hence

$$
\boxed{
g_{ab}
=
\bigl(\delta_{ab},\,
\delta_{ab}(t_a+t_b)\bigr),
\qquad
\delta_{ab}=t_a-t_b\ne0.
}
\tag{3.1}
$$

Suppose

$$
g_{ab}=g_{cd},
\qquad
a\ne b,\quad c\ne d.
$$

Equality of the first coordinates gives

$$
t_a-t_b=t_c-t_d=\delta\ne0.
$$

Equality of the second coordinates and division by \(\delta\) gives

$$
t_a+t_b=t_c+t_d.
$$

Since \(D\) is odd,

$$
t_a=\frac{(t_a+t_b)+(t_a-t_b)}2
=\frac{(t_c+t_d)+(t_c-t_d)}2=t_c,
$$

and similarly \(t_b=t_d\). Distinctness of the \(t_a\)'s then yields

$$
\boxed{
g_{ab}=g_{cd},\ a\ne b,\ c\ne d
\quad\Longrightarrow\quad
(a,b)=(c,d).
}
\tag{3.2}
$$

Thus the \(m(m-1)\) ordered nonzero differences are all distinct.

The pair-difference unitaries are

$$
\begin{aligned}
A_{ab}
&=U_b^*U_a\\
&=W_{-s_b}W_{s_a}\\
&=\omega^{[s_a,s_b]/2}W_{g_{ab}}.
\end{aligned}
\tag{3.3}
$$

The scalar phase in (3.3) disappears from every Choi rank-one operator

$$
|A_{ab}\rangle\rangle\langle\langle A_{ab}|.
$$

---

# 4. Exact Choi frame and invariants

The unnormalized Choi matrix of

$$
\Phi=L^*L
=
\frac1{m^2}\sum_{a,b}\operatorname{Ad}_{A_{ab}}
$$

is

$$
\boxed{
J_\Phi
=
\frac1{m^2}
\sum_{a,b}
|A_{ab}\rangle\rangle
\langle\langle A_{ab}|.
}
\tag{4.1}
$$

Let

$$
e=\frac{|I_D\rangle\rangle}{\sqrt D},
\qquad
P_0=|e\rangle\langle e|.
$$

## 4.1 Scalar block

For \(a=b\),

$$
A_{aa}=I_D.
$$

There are \(m\) diagonal terms, so their Choi contribution is

$$
\frac{m}{m^2}|I_D\rangle\rangle\langle\langle I_D|
=
\frac DmP_0.
$$

Hence

$$
\boxed{
r=\frac{\alpha}{D}=\frac Dm.
}
\tag{4.2}
$$

All off-diagonal \(A_{ab}\) are traceless, so there is no coupling between \(e\) and \(e^\perp\):

$$
\boxed{z=0.}
\tag{4.3}
$$

## 4.2 Traceless block

Let

$$
\Gamma=\{g_{ab}:a\ne b\}.
$$

By ordered-difference uniqueness, \(|\Gamma|=m(m-1)\). The normalized vectors

$$
\frac{|W_g\rangle\rangle}{\sqrt D},
\qquad g\in\Gamma,
$$

are orthonormal. Therefore

$$
\boxed{
B
=
\frac D{m^2}\Pi_\Gamma,
}
\tag{4.4}
$$

where \(\Pi_\Gamma\) projects onto their span. Consequently,

$$
\boxed{
\operatorname{rank}B=m(m-1),
}
\tag{4.5}
$$

$$
\boxed{
\operatorname{Tr}B
=
\frac{D(m-1)}m,
}
\tag{4.6}
$$

and

$$
\boxed{
a:=\operatorname{Tr}B^2
=
\frac{D^2(m-1)}{m^3}.
}
\tag{4.7}
$$

## 4.3 \(\alpha,\tau,i\)

Only the \(m\) diagonal pair differences have nonzero trace. Thus

$$
\begin{aligned}
\alpha
&=
\frac1{m^2}
\sum_{a,b}|\operatorname{Tr}A_{ab}|^2\\
&=
\frac{mD^2}{m^2}.
\end{aligned}
$$

Hence

$$
\boxed{
\alpha=\frac{D^2}{m}.
}
\tag{4.8}
$$

Since \(J_\Phi e=(D/m)e\),

$$
\begin{aligned}
\tau
&=
\langle\langle I|J_\Phi^2|I\rangle\rangle\\
&=
D\left(\frac Dm\right)^2,
\end{aligned}
$$

so

$$
\boxed{
\tau=\frac{D^3}{m^2}.
}
\tag{4.9}
$$

Finally,

$$
\begin{aligned}
i
&=\operatorname{Tr}J_\Phi^2\\
&=r^2+a\\
&=
\frac{D^2}{m^2}
+
\frac{D^2(m-1)}{m^3}.
\end{aligned}
$$

Therefore

$$
\boxed{
i=\frac{D^2(2m-1)}{m^3}.
}
\tag{4.10}
$$

These formulas exactly saturate

$$
a\ge \frac{(D-r)^2}{m(m-1)}
$$

and the resulting \(i\)-rank inequality.

Thus the Round 6 “pair-difference frame omitted” qualification is completely removed on the Choi side.

---

# 5. Exact realigned Liouville operator

Define

$$
\chi_h(s)=\omega^{[s,h]}.
$$

Using (2.4),

$$
\begin{aligned}
L(W_h)
&=
\frac1m\sum_aW_{s_a}W_hW_{s_a}^*\\
&=
\frac1m\sum_a\omega^{[s_a,h]}W_h.
\end{aligned}
$$

Therefore

$$
\boxed{
L(W_h)=\phi(h)W_h,
\qquad
\phi(h)=\frac1m\sum_{a=1}^m\chi_h(s_a).
}
\tag{5.1}
$$

Since \(L^*(W_h)=\overline{\phi(h)}W_h\),

$$
\boxed{
\Phi(W_h)=|\phi(h)|^2W_h.
}
\tag{5.2}
$$

Let

$$
E_h=\frac{W_h}{\sqrt D}.
$$

The Liouville matrix is therefore

$$
\boxed{
S_\Phi
=
\sum_{h\in\mathbb F_D^2}
|\phi(h)|^2
|E_h\rangle\langle E_h|.
}
\tag{5.3}
$$

Since \(\phi(0)=1\),

$$
P=S_\Phi-P_0
=
\sum_{h\ne0}
|\phi(h)|^2
|E_h\rangle\langle E_h|.
\tag{5.4}
$$

This is the exact realignment of the Choi frame in Section 4; \(P\) is no longer freely selectable.

---

# 6. Parseval and exact additive energy

Character orthogonality gives

$$
\sum_{h\in\mathbb F_D^2}
\chi_h(s-s')
=
D^2\delta_{s,s'}.
\tag{6.1}
$$

Thus

$$
\begin{aligned}
\sum_h|\phi(h)|^2
&=
\frac1{m^2}
\sum_{a,b}\sum_h
\chi_h(s_a-s_b)\\
&=
\frac{D^2m}{m^2}.
\end{aligned}
$$

Therefore

$$
\boxed{
\operatorname{Tr}S_\Phi
=
\sum_h|\phi(h)|^2
=
\frac{D^2}{m}
=
\alpha.
}
\tag{6.2}
$$

For the fourth moment, define

$$
n_g=
|\{(a,b):s_a-s_b=g\}|.
$$

Then

$$
\sum_h
\left|
\sum_a\chi_h(s_a)
\right|^4
=
D^2\sum_g n_g^2.
\tag{6.3}
$$

Here

$$
n_0=m
$$

and, by (3.2),

$$
n_g=
\begin{cases}
1,&g\in\Gamma,\\
0,&\text{otherwise}.
\end{cases}
$$

Hence the exact additive energy is

$$
\sum_g n_g^2
=
m^2+m(m-1)
=
2m^2-m.
\tag{6.4}
$$

It follows that

$$
\boxed{
\sum_h|\phi(h)|^4
=
\frac{D^2(2m^2-m)}{m^4}
=
\frac{D^2(2m-1)}{m^3}
=
i.
}
\tag{6.5}
$$

Therefore

$$
\boxed{
\operatorname{Tr}P=\alpha-1,
\qquad
\operatorname{Tr}P^2=i-1.
}
\tag{6.6}
$$

---

# 7. Pure-state Fourier formula

For arbitrary \(X\in M_D\), Weyl orthogonality gives

$$
X=
\frac1D
\sum_h
\operatorname{Tr}(W_h^*X)W_h.
\tag{7.1}
$$

For a pure state \(\rho\), define its Weyl characteristic function

$$
r_h=\operatorname{Tr}(W_h^*\rho).
\tag{7.2}
$$

Then

$$
L(\rho)
=
\frac1D
\sum_h\phi(h)r_hW_h.
$$

Using \(\operatorname{Tr}(W_h^*W_k)=D\delta_{h,k}\),

$$
\boxed{
\|L(\rho)\|_2^2
=
\frac1D
\sum_h
|\phi(h)|^2|r_h|^2.
}
\tag{PureFourier}
$$

For pure input, a direct Gram computation also gives

$$
\|C(\rho)\|_2^2=\|L(\rho)\|_2^2.
\tag{7.3}
$$

Indeed,

$$
\begin{aligned}
\|C(\rho)\|_2^2
&=
\frac1{m^2}
\sum_{a,b}
\left|
\operatorname{Tr}(\rho U_b^*U_a)
\right|^2\\
&=
\operatorname{Tr}
\left[
\left(
\frac1m\sum_aU_a\rho U_a^*
\right)^2
\right].
\end{aligned}
$$

---

# 8. Stabilizer-line test

Let \(\ell\subset\mathbb F_D^2\) be a one-dimensional isotropic line. Since the ambient symplectic space has dimension two,

$$
\ell^{\perp_{\rm sp}}=\ell.
\tag{8.1}
$$

A Weyl stabilizer projector associated with \(\ell\) has characteristic function of modulus one on \(\ell\) and zero off \(\ell\). Therefore PureFourier gives

$$
\|L(\rho_\ell)\|_2^2
=
\frac1D\sum_{h\in\ell}|\phi(h)|^2.
\tag{8.2}
$$

Now

$$
\begin{aligned}
\sum_{h\in\ell}|\phi(h)|^2
&=
\frac1{m^2}
\sum_{a,b}
\sum_{h\in\ell}
\chi_h(s_a-s_b).
\end{aligned}
$$

Character orthogonality on the line gives

$$
\sum_{h\in\ell}\chi_h(g)
=
\begin{cases}
D,&g\in\ell^{\perp_{\rm sp}}=\ell,\\
0,&g\notin\ell.
\end{cases}
$$

Let

$$
N_\ell=
|\{(a,b):a\ne b,\ g_{ab}\in\ell\}|.
$$

Then

$$
\boxed{
\|L(\rho_\ell)\|_2^2
=
\frac{m+N_\ell}{m^2}.
}
\tag{Line}
$$

There is no hidden Euclidean perpendicular here: with the convention (2.1), the character orthogonality condition uses the symplectic perpendicular, which equals the line itself.

## 8.1 Parabolic line counts

Every nonvertical line can be written

$$
\ell_s=\{(x,sx):x\in\mathbb F_D\}.
$$

By (3.1),

$$
g_{ab}\in\ell_s
\quad\Longleftrightarrow\quad
t_a+t_b=s.
$$

Let

$$
r_s=
|\{\{a,b\}:a\ne b,\ t_a+t_b=s\}|.
$$

Each unordered pair contributes the two ordered differences \(g_{ab}\) and \(g_{ba}\), so

$$
\boxed{
N_{\ell_s}=2r_s.
}
\tag{8.3}
$$

The vertical line contains no nonzero \(g_{ab}\), hence has \(N_\ell=0\).

Writing

$$
q=m(A-1)=9(1+\eta)^2,
$$

the stabilizer tests require

$$
\frac{m+N_\ell}{m^2}
\le
\frac{m+q}{m^2},
$$

or

$$
\boxed{N_\ell\le q.}
\tag{8.4}
$$

These are necessary tests only. Nothing proved so far shows that stabilizer states maximize PureFourier.

---

# 9. Explicit finite parameters passing all line tests

We now give a fully frozen deterministic construction with \(q=10\).

Set

$$
\boxed{
\eta=\frac{\sqrt{10}}3-1,
\qquad
A=1+\frac{10}{m}.
}
\tag{9.1}
$$

Choose any integer

$$
m>e^{20}.
\tag{9.2}
$$

Then

$$
\ln m>18
$$

and

$$
2m\ln A
=
2m\ln\left(1+\frac{10}{m}\right)
<20
<\ln m.
$$

Hence

$$
\boxed{A^2<m^{1/m}.}
\tag{9.3}
$$

The only imported number-theoretic result used below is the Bertrand–Chebyshev theorem:

> For every integer \(N>1\), there exists a prime \(p\) with \(N<p<2N\).

## 9.1 An integer Sidon set

Choose a prime

$$
m<\pi<2m.
$$

For \(j=0,\ldots,m-1\), let \(r_j\in\{0,\ldots,\pi-1\}\) be the least residue of \(j^2\pmod\pi\), and define

$$
\boxed{
t_j=2\pi j+r_j.
}
\tag{9.4}
$$

Then

$$
0\le t_j<2\pi^2.
\tag{9.5}
$$

Suppose

$$
t_i+t_j=t_k+t_l.
$$

Then

$$
2\pi(i+j-k-l)
=
-(r_i+r_j-r_k-r_l).
$$

The right side has absolute value strictly smaller than \(2\pi\), whereas the left side is a multiple of \(2\pi\). Therefore

$$
i+j=k+l,
\qquad
r_i+r_j=r_k+r_l.
$$

Modulo \(\pi\),

$$
i+j\equiv k+l,
\qquad
i^2+j^2\equiv k^2+l^2.
$$

Thus

$$
ij\equiv kl\pmod\pi.
$$

The monic quadratics

$$
(x-i)(x-j)
\quad\text{and}\quad
(x-k)(x-l)
$$

have the same coefficients over \(\mathbb F_\pi\), so

$$
\{i,j\}=\{k,l\}\pmod\pi.
$$

All indices lie in \(\{0,\ldots,\pi-1\}\), hence

$$
\boxed{
t_i+t_j=t_k+t_l
\Longrightarrow
\{i,j\}=\{k,l\}.
}
\tag{9.6}
$$

Thus \(\{t_j\}\) is an integer Sidon set.

## 9.2 Embedding into a prime field of size \(\Theta(m^2)\)

Choose an odd prime \(D\) satisfying

$$
4\pi^2<D<8\pi^2.
\tag{9.7}
$$

Again, Bertrand–Chebyshev guarantees such a prime.

Since every pair sum is less than \(4\pi^2<D\), equality of pair sums modulo \(D\) is the same as equality as integers. Therefore the images of the \(t_j\)'s in \(\mathbb F_D\) satisfy

$$
\boxed{
t_i+t_j=t_k+t_l\pmod D
\Longrightarrow
\{i,j\}=\{k,l\}.
}
\tag{9.8}
$$

Moreover,

$$
\boxed{
4m^2<D<32m^2.
}
\tag{9.9}
$$

Hence \(D\) is an odd prime in a controlled \(\Theta(m^2)\) range and \(D>m\).

For distinct indices, every field sum \(s\) occurs for at most one unordered pair. Consequently,

$$
r_s\le1,
\qquad
N_{\ell_s}\le2.
\tag{9.10}
$$

Since \(q=10\),

$$
\boxed{
N_\ell\le2<10=q
\quad\text{for every isotropic line }\ell.
}
\tag{9.11}
$$

Thus one fully frozen finite tuple passes every stabilizer-line test.

The necessary Haar-average condition also passes. Since \(\alpha=D^2/m\),

$$
\mathbb E_{\rho\ {\rm Haar\ pure}}
\|C(\rho)\|_2^2
=
\frac{\alpha+D}{D(D+1)}
=
\frac{D+m}{m(D+1)}.
$$

The inequality

$$
\frac{D+m}{m(D+1)}
\le
\frac{m+10}{m^2}
$$

reduces to

$$
m^2-m-10\le10D,
$$

which follows from \(D>4m^2\).

---

# 10. Exact full one-copy problem

For a pure state \(\rho\), define

$$
\mathcal F_\Gamma(\rho)
=
\sum_{g\in\Gamma}
\left|
\operatorname{Tr}(W_g^*\rho)
\right|^2.
\tag{10.1}
$$

The \(m\) diagonal pair differences contribute \(m\), and the off-diagonal labels are distinct. Hence

$$
\boxed{
\|C(\rho)\|_2^2
=
\frac{m+\mathcal F_\Gamma(\rho)}{m^2}.
}
\tag{10.2}
$$

Since

$$
\frac Am
=
\frac{m+q}{m^2},
$$

we obtain the exact equivalence

$$
\boxed{
p\le\frac Am
\quad\Longleftrightarrow\quad
\mathcal F_\Gamma(\rho)\le q
\quad
\text{for every pure }\rho.
}
\tag{10.3}
$$

For the explicit construction \(q=10\), the missing statement is exactly

$$
\boxed{
\sup_{\rho\ {\rm pure}}
\mathcal F_\Gamma(\rho)\le10.
}
\tag{PW10}
$$

## 10.1 Exact physical characteristic constraints

Let

$$
r_h=\operatorname{Tr}(W_h^*\rho).
$$

Every pure-state characteristic vector satisfies

$$
r_0=1,
\tag{10.4}
$$

$$
r_{-h}=\overline{r_h},
\tag{10.5}
$$

$$
\sum_h|r_h|^2=D,
\tag{10.6}
$$

and the twisted idempotence equations

$$
\boxed{
r_k
=
\frac1D
\sum_{h\in\mathbb F_D^2}
r_h\,r_{k-h}\,
\omega^{[h,k]/2}
\qquad
\forall k.
}
\tag{10.7}
$$

To derive (10.7), expand

$$
\rho=\frac1D\sum_hr_hW_h
$$

and compare the coefficient of \(W_k\) in \(\rho^2=\rho\), using

$$
W_hW_{k-h}
=
\omega^{[h,k]/2}W_k.
$$

Conversely, (10.4), (10.5), and (10.7) define a Hermitian idempotent of trace one, hence a rank-one projector. Thus the missing one-copy inequality can be stated entirely algebraically:

> For every sequence \(r\) satisfying the twisted pure-state equations (10.4)–(10.7),
>
> $$
> \sum_{g\in\Gamma}|r_g|^2\le10.
> $$

Parseval alone gives only

$$
\sum_{g\in\Gamma}|r_g|^2\le D-1,
$$

which is far too weak.

## 10.2 Why the maximum multiplier does not settle it

Let

$$
\widehat{\mathbf 1}_{\mathcal S}(h)
=
\sum_a\chi_h(s_a)
=
m\phi(h).
$$

From the exact energy calculations,

$$
\sum_{h\ne0}
\left|
\widehat{\mathbf 1}_{\mathcal S}(h)
\right|^2
=
D^2m-m^2,
\tag{10.8}
$$

and

$$
\sum_{h\ne0}
\left|
\widehat{\mathbf 1}_{\mathcal S}(h)
\right|^4
=
D^2(2m^2-m)-m^4.
\tag{10.9}
$$

Therefore

$$
\boxed{
\max_{h\ne0}
\left|
\widehat{\mathbf 1}_{\mathcal S}(h)
\right|^2
\ge
\frac{
D^2(2m^2-m)-m^4
}{
D^2m-m^2
}.
}
\tag{10.10}
$$

For \(D>4m^2\) and \(m>11\), the right side exceeds \(m+10\). Indeed, after subtracting \(m+10\), the numerator becomes

$$
D^2(m^2-11m)-m^4+m^3+10m^2>0.
$$

Thus

$$
\max_{h\ne0}|\phi(h)|^2
>
\frac{m+10}{m^2}
=
\frac Am.
\tag{10.11}
$$

Consequently, the unrestricted Liouville spectral estimate

$$
\|L(\rho)\|_2^2
\le
\max_h|\phi(h)|^2\,\|\rho\|_2^2
$$

cannot prove the required one-copy bound.

This does **not** disprove the physical bound: the Liouville eigenvector \(W_h\) is not a density operator. The missing content is precisely the twisted-idempotent restriction (10.7).

## 10.3 Stabilizer tests are not a proof of (PW10)

For stabilizer states,

$$
\mathcal F_\Gamma(\rho_\ell)=N_\ell\le2.
$$

For a general pure state, the characteristic mass may be spread over many distinct lines. No theorem has been proved here that stabilizer states maximize

$$
\sum_{g\in\Gamma}|r_g|^2.
$$

Thus the line tests remain necessary but not sufficient.

---

# 11. Conditional exact phase-space form of the all-\(T\) ratio

Although the one-copy gate is unresolved, the next ratio can be written exactly.

For an arbitrary matrix \(X\), define

$$
\mathcal F_\Gamma(X)
=
\sum_{g\in\Gamma}
|\operatorname{Tr}(W_g^*X)|^2.
$$

Because \(\Gamma=-\Gamma\),

$$
\boxed{
\|C(X)\|_2^2
=
\frac{
m|\operatorname{Tr}X|^2+\mathcal F_\Gamma(X)
}{m^2}.
}
\tag{11.1}
$$

Let

$$
\rho=TT^*,
\qquad
\sigma=T^*T.
$$

Then

$$
d_T
=
\frac{m+\mathcal F_\Gamma(\rho)}{m^2}.
\tag{11.2}
$$

For an off-diagonal pair-difference label \(g\), the transpose convention (2.7) gives, up to an irrelevant phase,

$$
A_{ab}^{\mathsf T}=W_{\vartheta g},
\qquad
\vartheta(p,q)=(p,-q).
$$

Define

$$
\mathcal G_\Gamma(T)
=
\sum_{g,h\in\Gamma}
\left|
\operatorname{Tr}
\left(
W_h^*T W_{\vartheta g}T^*
\right)
\right|^2.
\tag{11.3}
$$

Summing (11.1) over all off-diagonal \(g\) gives

$$
\boxed{
R_U(T)
=
\frac{
m\mathcal F_{\vartheta\Gamma}(\sigma)
+
\mathcal G_\Gamma(T)
}{
m\left[m+\mathcal F_\Gamma(\rho)\right]
}.
}
\tag{11.4}
$$

Since \(A-1=q/m\), the ratio gate is exactly

$$
\boxed{
m\mathcal F_{\vartheta\Gamma}(\sigma)
+
\mathcal G_\Gamma(T)
\le
q\left[m+\mathcal F_\Gamma(\rho)\right]
\quad
\forall\,\|T\|_2=1.
}
\tag{11.5}
$$

This is the first all-\(T\) inequality that would remain after closing (PW10).

---

# 12. Same-orientation maximally entangled test

Take

$$
T=\frac{I_D}{\sqrt D}.
$$

Then

$$
\rho=\sigma=\frac{I_D}{D},
\qquad
\mathcal F_\Gamma(\rho)=
\mathcal F_{\vartheta\Gamma}(\sigma)=0.
$$

Moreover,

$$
\begin{aligned}
\operatorname{Tr}
\left(
W_h^*T W_{\vartheta g}T^*
\right)
&=
\frac1D
\operatorname{Tr}(W_h^*W_{\vartheta g})\\
&=
\delta_{h,\vartheta g}.
\end{aligned}
$$

Therefore

$$
\boxed{
R_U(I/\sqrt D)
=
\frac{|\Gamma\cap\vartheta\Gamma|}{m^2}.
}
\tag{12.1}
$$

For the parabolic differences,

$$
\vartheta g_{ab}
=
\left(
t_a-t_b,\,
-(t_a-t_b)(t_a+t_b)
\right).
$$

By ordered-difference uniqueness,

$$
\vartheta g_{ab}=g_{cd}
$$

if and only if

$$
t_c=-t_b,
\qquad
t_d=-t_a.
$$

Let

$$
h_0=
|\mathcal T\cap(-\mathcal T)|,
\qquad
\mathcal T=\{t_1,\ldots,t_m\}.
$$

Then

$$
\boxed{
|\Gamma\cap\vartheta\Gamma|
=
h_0(h_0-1),
}
\tag{12.2}
$$

and hence

$$
\boxed{
R_U(I/\sqrt D)
=
\frac{h_0(h_0-1)}{m^2}.
}
\tag{12.3}
$$

For the explicit integer Sidon set of Section 9,

$$
0\le t_j<2\pi^2,
\qquad
D>4\pi^2.
$$

Thus for \(t_j>0\),

$$
-t_j\bmod D=D-t_j>2\pi^2,
$$

so it is not in \(\mathcal T\). Only \(t_0=0\) is fixed by negation. Therefore

$$
h_0=1
$$

and

$$
\boxed{
R_U(I/\sqrt D)=0.
}
\tag{12.4}
$$

Thus this genuine one-tuple construction also passes the basic same-orientation Bell collision test. This is still only one physical \(T\), not a uniform ratio proof.

---

# Earliest unresolved inequality

For the explicit frozen \(q=10\) tuple, the first missing statement is

$$
\boxed{
\sum_{g\in\Gamma}|r_g|^2\le10
}
$$

for every Weyl characteristic vector satisfying

$$
r_0=1,\qquad
r_{-g}=\overline{r_g},\qquad
r_k=\frac1D\sum_h
r_h r_{k-h}\omega^{[h,k]/2}.
$$

Equivalently, every pure-state orbit Gram matrix

$$
G_\psi(a,b)
=
\langle\psi|U_a^*U_b|\psi\rangle
$$

must satisfy

$$
\boxed{
\|G_\psi-I_m\|_2^2\le10.
}
\tag{13.1}
$$

No proof or counterexample to this inequality is obtained here. Until it is settled, the Weyl–Sidon family neither proves nor disproves \((E1_{\mathrm{gap}})\).

---

# Audit ledger

| Status                 | Statement                                                                                                                      |                           |         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------- | ------- |
| **PROVED**             | The two-sided centered Cauchy–Schwarz correction.                                                                              |                           |         |
| **PROVED**             | Its lower endpoint is negative on the exact Round 6 scalar survivor.                                                           |                           |         |
| **PROVED**             | Convention-fixed Weyl multiplication, adjoint, conjugation, orthogonality, and transpose formulas.                             |                           |         |
| **PROVED**             | Parabolic ordered-difference uniqueness.                                                                                       |                           |         |
| **PROVED**             | Every off-diagonal \(A_{ab}\) is a phase times a distinct traceless Weyl operator.                                             |                           |         |
| **PROVED**             | \(\alpha=D^2/m\), \(r=D/m\), \(z=0\), and \(\tau=D^3/m^2\).                                                                    |                           |         |
| **PROVED**             | \(B=(D/m^2)\Pi_\Gamma\), \(\operatorname{rank}B=m(m-1)\), and \(a=D^2(m-1)/m^3\).                                              |                           |         |
| **PROVED**             | \(i=D^2(2m-1)/m^3\); B-rank and I-rank are saturated.                                                                          |                           |         |
| **PROVED**             | Exact multiplier \(L(W_h)=\phi(h)W_h\) with \(\phi(h)=m^{-1}\sum_a\omega^{[s_a,h]}\).                                          |                           |         |
| **PROVED**             | Exact same-map Liouville spectrum (\Phi(W_h)=                                                                                  | \phi(h)                   | ^2W_h). |
| **PROVED**             | Parseval and additive-energy formulas for \(\operatorname{Tr}P\) and \(\operatorname{Tr}P^2\).                                 |                           |         |
| **PROVED**             | PureFourier.                                                                                                                   |                           |         |
| **PROVED**             | Stabilizer-line formula \((m+N_\ell)/m^2\), with the symplectic perpendicular convention corrected explicitly.                 |                           |         |
| **PROVED**             | For parabolic labels, \(N_{\ell_s}=2r_s\).                                                                                     |                           |         |
| **PROVED — existence** | A fully frozen finite \(q=10\), \(D=\Theta(m^2)\) tuple with \(N_\ell\le2\) for every line.                                    |                           |         |
| **PROVED**             | Exact one-copy equivalence \(p\le A/m\iff\sup_\rho\mathcal F_\Gamma(\rho)\le q\).                                              |                           |         |
| **PROVED**             | Exact twisted-idempotence characterization of physical pure-state Weyl characteristic vectors.                                 |                           |         |
| **PROVED**             | The maximum nontrivial Liouville multiplier exceeds the target; unrestricted \(2\to2\) control cannot prove the one-copy gate. |                           |         |
| **PROVED**             | Exact all-\(T\) phase-space ratio formula (11.4).                                                                              |                           |         |
| **PROVED**             | Maximally entangled same-orientation test (R(I/\sqrt D)=                                                                       | \Gamma\cap\vartheta\Gamma | /m^2).  |
| **PROVED**             | The explicit frozen Sidon set has \(\Gamma\cap\vartheta\Gamma=\varnothing\), hence \(R(I/\sqrt D)=0\).                         |                           |         |
| **OPEN**               | The physical characteristic inequality (PW10).                                                                                 |                           |         |
| **OPEN**               | The full one-copy bound \(p\le A/m\) for the frozen Weyl–Sidon tuple.                                                          |                           |         |
| **OPEN**               | The uniform all-\(T\) ratio inequality (11.5).                                                                                 |                           |         |
| **OPEN**               | \((E1_{\mathrm{gap}})\).                                                                                                       |                           |         |
| **DISPROVED**          | No new universal statement is disproved in this round.                                                                         |                           |         |
| **REDUNDANT**          | Stabilizer-line and maximum-multiplier tests are insufficient to replace the full physical supremum.                           |                           |         |
| **CONJECTURED**        | None promoted.                                                                                                                 |                           |         |

The first new claim requiring independent verification is the deterministic finite construction in Section 9, especially the integer Sidon embedding (9.4)–(9.8). The first unresolved operator inequality is the twisted-idempotent restricted-mass bound (PW10).

The full-size theorem remains open: the finite \(r=2\) gate is not closed, independently of the separate all-copy gate.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-07-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-07-local-audit.md bytes=8671 sha256=0d7b14dccdbfb0db8d7569de845689b7817a78211e8d7db0bae85f726b37597a -->

# Round 07 independent local audit

## Capture integrity

- Conversation: Audit quantum construction
- Mode/model observed at send time: ordinary Chat, GPT-5.6 Sol, Pro 5/5
- Browser completion indicator: Worked for 19m 59s
- Captured response: 26,574 bytes; 26,550 Unicode characters
- Response SHA-256: 21f81f4f3452848a1cc9a979fd741c88c2686af432ac037bd89f2fd6ef5f79bf
- The artifact and output response copies are byte-identical.
- The prompt file was rechecked after capture and retains its pre-send SHA-256:
  7ff991bfd36a029069255893385a243691d2e0cedaaa47ce8175d7b8c81efd76.

## Verdict

**OPEN WITH EARLIEST GAP.** Round 7 supplies a genuine one-tuple Weyl--Sidon
family and correctly couples its Choi and Liouville descriptions. It does not
prove or disprove the finite r=2 gate. The first unresolved condition is the
uniform pure-state restricted Weyl-mass inequality PW10:

$$
\sup_{\rho\ {\rm pure}}\sum_{g\in\Gamma}
  |\operatorname{Tr}(W_g^*\rho)|^2\le 10.
$$

The conditional all-T formula is valid, but no uniform all-T estimate follows
until PW10 is settled. No conclusion about the separate all-copy gate changes.

## Claims independently verified

### 1. Weyl convention and phases

With

$$
W_{(p,q)}=\omega^{-pq/2}Z^pX^q,\qquad ZX=\omega XZ,
$$

direct multiplication gives

$$
W_gW_h=\omega^{[g,h]/2}W_{g+h},\quad
W_g^*=W_{-g},\quad
W_gW_hW_g^*=\omega^{[g,h]}W_h.
$$

The transpose calculation is also correct:

$$
(Z^pX^q)^{\mathsf T}=X^{-q}Z^p
=\omega^{pq}Z^pX^{-q},
\qquad
W_{(p,q)}^{\mathsf T}=W_{(p,-q)}.
$$

Thus the phase and transpose conventions used later in the response are
consistent.

### 2. Ordered differences and the Choi frame

For

$$
s_a=(t_a,t_a^2),\qquad
g_{ab}=s_a-s_b
  =(t_a-t_b,(t_a-t_b)(t_a+t_b)),
$$

equality of two nonzero ordered differences first gives equal differences and
then equal sums. Since D is odd, this recovers both ordered endpoints. Hence
all m(m-1) nonzero ordered differences are distinct.

Consequently the off-diagonal pair-difference unitaries are phase multiples
of distinct traceless Weyl operators, and

$$
B=\frac{D}{m^2}\Pi_\Gamma,\qquad
\operatorname{rank}B=m(m-1).
$$

The scalar and traceless Choi blocks are orthogonal, so z=0. Direct trace
calculations give exactly

$$
\alpha=\frac{D^2}{m},\quad
r=\frac{D}{m},\quad
\tau=\frac{D^3}{m^2},\quad
a=\frac{D^2(m-1)}{m^3},\quad
i=\frac{D^2(2m-1)}{m^3}.
$$

The B-rank and resulting I-rank inequalities are equalities because

$$
\operatorname{Tr}B=\frac{D(m-1)}m,\qquad
a=\frac{(\operatorname{Tr}B)^2}{m(m-1)},\qquad
i=r^2+a.
$$

### 3. Same-map Liouville spectrum and additive energy

Conjugation by W_{s_a} multiplies W_h by
$\omega^{[s_a,h]}$. Therefore

$$
L(W_h)=\phi(h)W_h,\qquad
\phi(h)=\frac1m\sum_a\omega^{[s_a,h]},
$$

and L*L has eigenvalues $|\phi(h)|^2$ in the normalized Weyl basis.
Character orthogonality gives

$$
\sum_h|\phi(h)|^2=\frac{D^2}{m}.
$$

For the difference multiplicities n_g, ordered-difference uniqueness gives
n_0=m and n_g=1 on Gamma. Hence

$$
\sum_g n_g^2=2m^2-m
$$

and

$$
\sum_h|\phi(h)|^4
=\frac{D^2(2m-1)}{m^3}.
$$

Thus the claimed traces of P and P^2 agree with the Choi invariants of the
same map; the Round 6 decoupling defect is genuinely removed for this family.

### 4. PureFourier and the exact one-copy reduction

Expanding a pure state in the orthogonal Weyl basis gives

$$
\|L(\rho)\|_2^2
=\frac1D\sum_h|\phi(h)|^2
  |\operatorname{Tr}(W_h^*\rho)|^2.
$$

Independently expanding the m by m orbit Gram matrix gives

$$
\|C(\rho)\|_2^2
=\frac{m+\mathcal F_\Gamma(\rho)}{m^2},
\qquad
\mathcal F_\Gamma(\rho)
=\sum_{g\in\Gamma}|\operatorname{Tr}(W_g^*\rho)|^2.
$$

For q=m(A-1), this proves the response's exact equivalence

$$
p\le A/m
\quad\Longleftrightarrow\quad
\mathcal F_\Gamma(\rho)\le q
\ \hbox{for every pure }\rho.
$$

At q=10, PW10 is therefore necessary and sufficient for the one-copy gate of
this tuple, not merely a necessary test.

### 5. Stabilizer-line test

For a one-dimensional isotropic line in the two-dimensional symplectic
space, the symplectic perpendicular is the line itself. Character
orthogonality therefore yields

$$
\|L(\rho_\ell)\|_2^2
=\frac{m+N_\ell}{m^2}.
$$

The parabolic difference g_ab has nonvertical slope t_a+t_b, so an unordered
pair with a fixed sum contributes exactly the two ordered differences
g_ab and g_ba. Hence N_{\ell_s}=2r_s; the vertical line contains no nonzero
differences. These are only necessary pure-state tests. The response does not
silently promote stabilizers to global maximizers.

### 6. Deterministic Sidon construction and Gap

The integer construction itself is correct. If

$$
t_j=2p j+r_j,\qquad r_j\equiv j^2\pmod p,\quad 0\le r_j<p,
$$

where m<p<2m is prime, equality of two pair sums forces equality of the
index sums and residue sums. Modulo p the two unordered index pairs then have
the same sum and product, hence are equal. Since each t_j is below 2p^2,
choosing a prime D with 4p^2<D<8p^2 embeds all pair sums without modular
wraparound. It follows that every field sum occurs for at most one unordered
pair and N_\ell is at most 2.

For

$$
\eta=\sqrt{10}/3-1,\qquad A=1+10/m,
$$

and m>e^{20}, the response's estimate

$$
2m\log(1+10/m)<20<\log m
$$

correctly proves $A^2<m^{1/m}$. Bertrand--Chebyshev supplies the claimed
Theta(m^2) range for D.

One provenance correction is required: the response says "fully frozen" but
then says "choose any" m and "choose a prime" twice. That is a proved
parametric existence construction, not one frozen tuple as written.

The repair is immediate and introduces no new mathematical assumption. Define
uniquely

$$
m_0=\min\{n\in\mathbb N:n>e^{20}\},
$$

let p_0 be the least prime greater than m_0, let D_0 be the least prime
greater than 4p_0^2, and use the displayed formula for every
$j=0,\ldots,m_0-1$. Bertrand--Chebyshev gives

$$
m_0<p_0<2m_0,\qquad
4p_0^2<D_0<8p_0^2.
$$

This canonically selects one finite tuple and preserves every proof in
Section 9. The web response's existence result is sound, but its frozen-status
label needs this tie-breaking repair.

### 7. Physical characteristic constraints and the spectral obstruction

The twisted idempotence equation has the correct phase:

$$
r_k=\frac1D\sum_h r_h r_{k-h}\omega^{[h,k]/2}.
$$

Together with r_0=1 and $r_{-h}=\overline{r_h}$, it reconstructs a Hermitian
idempotent of trace one, hence a rank-one projector. This is an exact physical
characterization, not only a relaxation.

The second- and fourth-moment argument also correctly shows that the largest
nonidentity Fourier multiplier exceeds the target. After cross multiplication,
the difference from m+10 is

$$
D^2(m^2-11m)-m^4+m^3+10m^2,
$$

which is positive under D>4m^2 and m>11. This only rules out an unrestricted
Hilbert--Schmidt spectral proof; the corresponding Weyl eigenoperator is not
a state and therefore does not disprove PW10.

### 8. Conditional all-T formula

For arbitrary X, the symmetry Gamma=-Gamma gives

$$
\|C(X)\|_2^2
=\frac{m|\operatorname{Tr}X|^2+\mathcal F_\Gamma(X)}{m^2}.
$$

Applying this to
$X_g=T W_{\vartheta g}T^*$, summing once over every ordered nonzero
difference, and using $\rho=TT^*$ and $\sigma=T^*T$ gives

$$
R_U(T)=
\frac{
m\mathcal F_{\vartheta\Gamma}(\sigma)+\mathcal G_\Gamma(T)
}{
m\,[m+\mathcal F_\Gamma(\rho)]
}.
$$

There is no missing factor of m or D. For $T=I/\sqrt D$, this reduces to

$$
R_U(I/\sqrt D)=\frac{|\Gamma\cap\vartheta\Gamma|}{m^2}.
$$

Solving $\vartheta g_{ab}=g_{cd}$ gives
$t_c=-t_b$ and $t_d=-t_a$, hence
$|\Gamma\cap\vartheta\Gamma|=h_0(h_0-1)$. In the integer embedding only zero
is paired with its negative, so h_0=1 and this particular test has value zero.
This remains a single test, not an all-T bound.

## Presentation and status defects

- The "fully frozen" claim requires the canonical tie-breaking repair above.
- Several audit-ledger rows are malformed because unescaped vertical bars in
  formulas are interpreted as table separators. This is a rendering defect.
- Calling necessary tests "REDUNDANT" is imprecise. They are valid but
  insufficient; no mathematical claim is refuted by that wording.

## Earliest remaining gate

For the canonically frozen tuple, the earliest unresolved implication is

$$
\sum_{g\in\Gamma}|r_g|^2\le10
$$

for every solution of the pure-state twisted-idempotence system. Equivalently,
every orbit Gram matrix must obey

$$
\|G_\psi-I_m\|_2^2\le10.
$$

No argument in Round 7 proves this inequality or produces a violating state.
The full one-copy gate, the subsequent uniform all-T gate, E1_gap, and the
full-size theorem therefore remain open.

Status: **COMPLETED — LOCALLY AUDITED; PW10 IS THE EARLIEST OPEN GATE.**

<!-- END HISTORICAL FILE path=outputs/round-07-local-audit.md -->


# ROUND 008

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-08-prompt.md bytes=7017 sha256=42803d948018cf433a2105f9f974c7054e22ed77c174162de6e941307d93a33d -->

# Round 8 — attack PW10 through the doubled Weyl witness and affine-fiber states

Continue in the same deterministic one-layer setup and the same conversation.
This round is confined to the finite r=2 low-A gate. Give a public,
self-contained derivation and no hidden chain-of-thought.

## Audited Round 7 boundary

Let D be an odd prime and use

$$
W_{(p,q)}=\omega^{-pq/2}Z^pX^q,\qquad
[ (p,q),(r,s) ]=ps-qr.
$$

For distinct field elements t_a, set

$$
s_a=(t_a,t_a^2),\qquad U_a=W_{s_a},
$$

and

$$
\Gamma=\{s_a-s_b:a\ne b\}.
$$

Round 7 and an independent local audit established the following exact
facts.

1. The m(m-1) ordered nonzero differences are distinct.

2. The same actual tuple has the exact Choi and Liouville descriptions

$$
B=\frac{D}{m^2}\Pi_\Gamma,
\qquad
L(W_h)=\phi(h)W_h,
\qquad
\phi(h)=\frac1m\sum_a\omega^{[s_a,h]}.
$$

All advertised Choi invariants, Parseval, additive energy, PureFourier, and
the stabilizer-line formula were independently verified.

3. With

$$
q=m(A-1)=10,\qquad
\eta=\frac{\sqrt{10}}3-1,\qquad
A=1+\frac{10}{m},
$$

the full one-copy gate is exactly

$$
\boxed{
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)\le10,
}
\tag{PW10}
$$

where

$$
\mathcal F_\Gamma(\rho)
=\sum_{g\in\Gamma}
 |\operatorname{Tr}(W_g^*\rho)|^2.
$$

Equivalently, for every unit vector psi,

$$
\|G_\psi-I_m\|_2^2\le10,
\qquad
G_\psi(a,b)=\langle\psi|U_a^*U_b|\psi\rangle.
$$

4. Stabilizer states give only

$$
\mathcal F_\Gamma(\rho_\ell)=N_\ell\le2.
$$

They are necessary tests, not known maximizers.

5. The maximum nonidentity Liouville multiplier exceeds the one-copy target.
This only defeats an unrestricted Hilbert--Schmidt spectral proof because a
Weyl eigenoperator is not a density matrix.

6. The exact all-T formula from Round 7 is correct, but it is downstream of
PW10 and must not be promoted while PW10 is open.

The Round 7 phrase "fully frozen" needed one tie-breaking correction. Use the
following single, canonically frozen tuple in this round:

$$
m_0=\min\{n\in\mathbb N:n>e^{20}\},
$$

$$
p_0=\min\{p:p\ {\rm prime},\ p>m_0\},
\qquad
D_0=\min\{D:D\ {\rm prime},\ D>4p_0^2\},
$$

and, for j=0,...,m_0-1,

$$
r_j\in\{0,\ldots,p_0-1\},\qquad
r_j\equiv j^2\pmod {p_0},
$$

$$
t_j=2p_0j+r_j\pmod {D_0}.
\tag{Freeze}
$$

Bertrand--Chebyshev gives

$$
m_0<p_0<2m_0,\qquad
4p_0^2<D_0<8p_0^2,
$$

so the Round 7 Sidon and no-wrap proofs apply. This is one definite finite
tuple, not a family with unresolved choices. It has

$$
\mathcal T\cap(-\mathcal T)=\{0\}
$$

and no Gamma point with second coordinate zero.

## A doubled-Weyl formulation to audit

Define

$$
K_\Gamma
=\sum_{g\in\Gamma}W_g\otimes\overline{W_g}.
\tag{K}
$$

The cocycles should cancel in the doubled representation:

$$
(W_g\otimes\overline{W_g})
(W_h\otimes\overline{W_h})
=W_{g+h}\otimes\overline{W_{g+h}}.
\tag{K-rep}
$$

Thus these operators commute. With normalized vectorization, the Weyl Bell
vectors

$$
|E_x\rangle\rangle=D^{-1/2}|W_x\rangle\rangle
$$

should diagonalize K_Gamma, with eigenvalues, up to the conventionally
correct sign,

$$
\lambda_x
=\sum_{g\in\Gamma}\omega^{[g,x]}
=\left|\sum_a\omega^{[s_a,x]}\right|^2-m.
\tag{K-spec}
$$

For a pure rho=|psi><psi|,

$$
\mathcal F_\Gamma(\rho)
=\langle\psi\otimes\overline\psi|
 K_\Gamma
 |\psi\otimes\overline\psi\rangle.
\tag{K-prod}
$$

Equivalently, after partial transpose on the second factor,

$$
\mathcal F_\Gamma(\rho)
=\langle\psi\otimes\psi|
 K_\Gamma^{T_2}
 |\psi\otimes\psi\rangle.
\tag{K-PT}
$$

Audit all vectorization, conjugation, symplectic signs, and normalizations.
The unrestricted largest eigenvalue of K_Gamma is already known to exceed
10; that is not a PW10 counterexample because its eigenvectors are maximally
entangled Bell vectors rather than vectors psi tensor conjugate(psi).

## A concrete two-level witness test

For c nonzero and arbitrary x and theta, define

$$
|\psi_{x,c,\theta}\rangle
=\frac{|x\rangle+e^{i\theta}|x+c\rangle}{\sqrt2}.
\tag{Two}
$$

Let

$$
H_c=\{p\in\mathbb F_D:(p,c)\in\Gamma\}.
$$

Because the frozen Gamma has no point with second coordinate zero and is
centrally symmetric, direct matrix-element calculation appears to give

$$
\boxed{
\mathcal F_\Gamma(
 |\psi_{x,c,\theta}\rangle\langle\psi_{x,c,\theta}|
 )
=\frac{|H_c|+|H_{-c}|}{4}
=\frac{|H_c|}{2}.
}
\tag{Fiber}
$$

If this is correct, PW10 forces

$$
|H_c|\le20
\qquad\hbox{for every nonzero c}.
\tag{Fiber20}
$$

A rigorously identified c with at least 21 ordered pairs

$$
t_a^2-t_b^2=c\pmod D
$$

would therefore give an explicit pure-state violation of PW10 for the
frozen tuple. Conversely, proving Fiber20 only passes this new family of
tests; it does not prove PW10.

## Exact tasks

1. Give one verdict on PW10 for the canonically frozen tuple:
   PROVED, DISPROVED, or OPEN WITH EARLIEST GAP. Do not confuse failure of
   this tuple with a universal impossibility for all tuples.

2. Independently derive or refute K-rep, K-spec, K-prod, K-PT, Fiber, and
   Fiber20. Correct every sign and factor explicitly.

3. Settle the horizontal-fiber problem for the frozen set. Do one of:

   - prove |H_c|<=20 for every nonzero c;
   - give one exact c and at least 21 distinct ordered index pairs producing
     it; or
   - reduce the count to a strictly smaller, explicit number-theoretic
     equation and identify the first unproved estimate.

   Brute-force enumeration over the enormous frozen set, numerical sampling,
   or a heuristic collision estimate is not a proof.

4. Go beyond the two-level test and attack the restricted coherent/product
   norm

$$
\sup_{\|\psi\|=1}
\langle\psi\otimes\overline\psi|
K_\Gamma
|\psi\otimes\overline\psi\rangle.
\tag{SepDiag}
$$

Try exact symmetric-product, separable, PPT, partial-transpose, or
sum-of-squares bounds if useful. State precisely which relaxation is being
used. A relaxation value above 10 is not a counterexample unless a physical
psi is recovered; a relaxation value at most 10 with the correct containment
would prove PW10.

5. Use the explicit spectrum K-spec rather than discarding it. Determine
whether the set of eigenvalues above 10 and the Bell-overlap constraints of
psi tensor conjugate(psi) imply either an upper bound or a constructive
violating state. Do not assume arbitrary probability weights in the Bell
basis are physically attainable.

6. If PW10 remains open, the final earliest gap must be strictly more
   informative than merely restating PW10. Isolate one exact inequality or
   finite combinatorial condition whose proof would close it, and show the
   derivation from the audited identities.

7. Discuss the all-T ratio only if PW10 is first settled for this same frozen
   tuple. Do not claim anything about the separate all-copy gate.

8. End with an audit ledger separating PROVED, DISPROVED, NECESSARY-ONLY,
   OPEN, and CONJECTURED. Identify the first new claim requiring independent
   verification.

The finite r=2 gate and the full-size theorem remain OPEN unless all required
uniform inequalities are actually proved.

<!-- END HISTORICAL FILE path=work/round-08-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-08-response.md bytes=24807 sha256=b6f69056a998e9a6a1fd325334915dff8d5157922a39a69edc3fb06d2341d8cb -->

# Verdict

$$
\boxed{\text{PW10 for the canonically frozen tuple is OPEN WITH EARLIEST GAP.}}
$$

The doubled-Weyl identities and the two-level fiber formula are correct, with one harmless reflection in the Bell-eigenvector labeling:

$$
K_\Gamma |E_{\vartheta x}\rangle\rangle
=
\lambda_x |E_{\vartheta x}\rangle\rangle,
\qquad
\vartheta(p,q)=(p,-q).
$$

The horizontal-fiber problem reduces exactly to the one-variable condition

$$
\boxed{
|H_c|
=
\#\left\{
u\in\mathbb F_D^\times:
\frac{u+c/u}{2}\in\mathcal T,\
\frac{c/u-u}{2}\in\mathcal T
\right\},
}
\tag{HF}
$$

or equivalently to the difference multiplicity of the squared set

$$
\mathcal V=\{t_j^2:j=0,\ldots,m-1\}:
\qquad
\boxed{|H_c|=|\mathcal V\cap(\mathcal V+c)|.}
\tag{V-fiber}
$$

I do not prove \(|H_c|\le20\), nor produce a \(c\) with \(21\) representations.

The principal new reduction is an exact duality:

$$
\boxed{
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)
=
\sup_{\substack{c_{-g}=\overline{c_g}\\c\ne0}}
\frac{
\left\|\sum_{g\in\Gamma}c_gW_g\right\|_\infty^2
}{
\sum_{g\in\Gamma}|c_g|^2
}.
}
\tag{Dual}
$$

Thus PW10 is equivalent to the concrete finite Weyl-polynomial estimate

$$
\boxed{
\left\|\sum_{g\in\Gamma}c_gW_g\right\|_\infty
\le
\sqrt{10}
\left(\sum_{g\in\Gamma}|c_g|^2\right)^{1/2}
\quad
\forall\,c_{-g}=\overline{c_g}.
}
\tag{WR10}
$$

The two-level condition \(|H_c|\le20\) is only a \(2\times2\) compression of \((WR10)\).

Using the exact Bell spectrum, one can also prove that **at least \(D\) Bell eigenvalues exceed \(10\)**. Consequently, even the constraints

$$
w_x\ge0,\quad
\sum_xw_x=1,\quad
w_0=\frac1D,\quad
w_x\le\frac1D,\quad
w_{-x}=w_x
$$

do not force the expectation below \(10\). The still-missing information is precisely the pure-state twisted-idempotence/rank-one coupling.

---

# 1. Doubled Weyl representation

Use

$$
W_{(p,q)}=\omega^{-pq/2}Z^pX^q,
\qquad
[(p,q),(r,s)]=ps-qr.
$$

The Weyl multiplication law is

$$
W_gW_h=\omega^{[g,h]/2}W_{g+h}.
\tag{1.1}
$$

Taking entrywise conjugates,

$$
\overline{W_g}\,\overline{W_h}
=
\omega^{-[g,h]/2}\overline{W_{g+h}}.
$$

Hence the cocycles cancel:

$$
\boxed{
(W_g\otimes\overline{W_g})
(W_h\otimes\overline{W_h})
=
W_{g+h}\otimes\overline{W_{g+h}}.
}
\tag{K-rep}
$$

Thus \(g\mapsto W_g\otimes\overline{W_g}\) is an ordinary representation of the additive group \(\mathbb F_D^2\), and all its elements commute.

Because \(\Gamma=-\Gamma\),

$$
K_\Gamma^*=K_\Gamma.
$$

---

# 2. Exact Bell diagonalization and the reflected label

Use column vectorization

$$
|X\rangle\rangle=\sum_j|j\rangle\otimes X|j\rangle.
$$

Then

$$
(A\otimes B)|X\rangle\rangle
=
|BXA^{\mathsf T}\rangle\rangle.
\tag{2.1}
$$

Define the two linear reflections

$$
\kappa(p,q)=(-p,q),
\qquad
\vartheta(p,q)=(p,-q).
$$

Directly from the Weyl definition,

$$
\overline{W_g}=W_{\kappa g},
\qquad
W_g^{\mathsf T}=W_{\vartheta g}
=
W_{\kappa g}^*.
\tag{2.2}
$$

Therefore

$$
\begin{aligned}
(W_g\otimes\overline{W_g})|W_x\rangle\rangle
&=
|\overline{W_g}W_xW_g^{\mathsf T}\rangle\rangle\\
&=
|W_{\kappa g}W_xW_{\kappa g}^*\rangle\rangle\\
&=
\omega^{[\kappa g,x]}|W_x\rangle\rangle.
\end{aligned}
$$

Since

$$
[\kappa g,x]=[g,\vartheta x],
$$

the normalized Bell vectors

$$
|E_x\rangle\rangle=D^{-1/2}|W_x\rangle\rangle
$$

satisfy

$$
K_\Gamma|E_x\rangle\rangle
=
\lambda_{\vartheta x}|E_x\rangle\rangle,
$$

where

$$
\lambda_x=\sum_{g\in\Gamma}\omega^{[g,x]}.
$$

Equivalently,

$$
\boxed{
K_\Gamma|E_{\vartheta x}\rangle\rangle
=
\lambda_x|E_{\vartheta x}\rangle\rangle.
}
\tag{2.3}
$$

Thus the prompt’s spectrum is correct after the bijective relabeling
\(x\mapsto\vartheta x\).

For the difference set,

$$
\begin{aligned}
\lambda_x
&=
\sum_{a\ne b}\omega^{[s_a-s_b,x]}\\
&=
\left|\sum_a\omega^{[s_a,x]}\right|^2-m.
\end{aligned}
$$

Hence

$$
\boxed{
\lambda_x
=
\left|\sum_a\omega^{[s_a,x]}\right|^2-m.
}
\tag{K-spec}
$$

In particular,

$$
\lambda_0=m(m-1).
$$

---

# 3. Product and partial-transpose identities

For a unit vector \(\psi\),

$$
\begin{aligned}
&\langle\psi\otimes\overline\psi|
W_g\otimes\overline{W_g}
|\psi\otimes\overline\psi\rangle\\
&\qquad=
\langle\psi|W_g|\psi\rangle
\overline{\langle\psi|W_g|\psi\rangle}\\
&\qquad=
|\langle\psi|W_g|\psi\rangle|^2.
\end{aligned}
$$

Since

$$
|\langle\psi|W_g|\psi\rangle|
=
|\operatorname{Tr}(W_g^*|\psi\rangle\langle\psi|)|,
$$

we obtain

$$
\boxed{
\mathcal F_\Gamma(|\psi\rangle\langle\psi|)
=
\langle\psi\otimes\overline\psi|
K_\Gamma
|\psi\otimes\overline\psi\rangle.
}
\tag{K-prod}
$$

Now

$$
(\overline{W_g})^{\mathsf T}=W_g^*,
$$

so

$$
K_\Gamma^{T_2}
=
\sum_{g\in\Gamma}W_g\otimes W_g^*.
$$

Consequently,

$$
\boxed{
\mathcal F_\Gamma(|\psi\rangle\langle\psi|)
=
\langle\psi\otimes\psi|
K_\Gamma^{T_2}
|\psi\otimes\psi\rangle.
}
\tag{K-PT}
$$

No factor of \(D\) is missing in either formula.

---

# 4. The two-level state and the exact fiber formula

The Weyl action in the computational basis is

$$
W_{(p,q)}|y\rangle
=
\omega^{p(y+q/2)}|y+q\rangle.
\tag{4.1}
$$

Let \(c\ne0\) and

$$
|\psi\rangle
=
\frac{|x\rangle+e^{i\theta}|x+c\rangle}{\sqrt2}.
$$

Because \(D\) is odd, \(2c\ne0\).

For \(q=c\),

$$
\langle\psi|W_{(p,c)}|\psi\rangle
=
\frac12e^{-i\theta}
\omega^{p(x+c/2)},
$$

and hence its modulus squared is \(1/4\).

For \(q=-c\),

$$
\langle\psi|W_{(p,-c)}|\psi\rangle
=
\frac12e^{i\theta}
\omega^{p(x+c/2)},
$$

again with modulus squared \(1/4\).

For \(q\notin\{0,c,-c\}\), the expectation is zero. The frozen tuple has no \(\Gamma\)-point with \(q=0\), so there is no diagonal contribution.

Therefore

$$
\boxed{
\mathcal F_\Gamma(|\psi\rangle\langle\psi|)
=
\frac{|H_c|+|H_{-c}|}{4}.
}
\tag{4.2}
$$

Since \(\Gamma=-\Gamma\),

$$
H_{-c}=-H_c
$$

and thus

$$
|H_{-c}|=|H_c|.
$$

Hence

$$
\boxed{
\mathcal F_\Gamma(|\psi_{x,c,\theta}\rangle
\langle\psi_{x,c,\theta}|)
=
\frac{|H_c|}{2}.
}
\tag{Fiber}
$$

It is independent of \(x\) and \(\theta\).

Therefore PW10 implies

$$
\boxed{|H_c|\le20\quad\forall\,c\ne0.}
\tag{Fiber20}
$$

This is a necessary condition only.

---

# 5. Exact reduction of the frozen horizontal-fiber problem

Let

$$
\mathcal T=\{t_0,\ldots,t_{m-1}\}\subset\mathbb F_D.
$$

For \(g_{ab}=(p,c)\),

$$
p=t_a-t_b,
\qquad
c=t_a^2-t_b^2=p(t_a+t_b).
$$

Since \(p\ne0\),

$$
t_a+t_b=\frac cp.
$$

Therefore

$$
t_a=\frac{p+c/p}{2},
\qquad
t_b=\frac{c/p-p}{2}.
$$

The ordered-difference uniqueness proved in Round 7 implies that every \(p\in H_c\) corresponds to exactly one ordered pair. Hence

$$
\boxed{
|H_c|
=
\#\left\{
p\in\mathbb F_D^\times:
\frac{p+c/p}{2}\in\mathcal T,\
\frac{c/p-p}{2}\in\mathcal T
\right\}.
}
\tag{5.1}
$$

This is a one-variable finite-field equation.

## 5.1 Squared-set formulation

The frozen condition

$$
\mathcal T\cap(-\mathcal T)=\{0\}
$$

implies that squaring is injective on \(\mathcal T\). Define

$$
\mathcal V=\{t_j^2:j=0,\ldots,m-1\}.
$$

Then

$$
t_a^2-t_b^2=c
$$

is the same as

$$
v_a-v_b=c,
\qquad
v_a,v_b\in\mathcal V.
$$

Thus

$$
\boxed{
|H_c|
=
r_{\mathcal V-\mathcal V}(c)
=
|\mathcal V\cap(\mathcal V+c)|.
}
\tag{5.2}
$$

Because \(c\ne0\), translation by \(c\) is a single \(D\)-cycle. Since
\(|\mathcal V|=m<D\),

$$
\boxed{|H_c|\le m-1.}
\tag{5.3}
$$

This is rigorous but far too weak for Fiber20.

## 5.2 Integer lift for the canonically frozen set

Write \(P=p_0\), \(D=D_0\), and take the representatives

$$
t_j=2Pj+r_j,
\qquad
0\le t_j<2P^2<\frac D2.
$$

Let \(\widetilde c\in[-(D-1)/2,(D-1)/2]\) represent \(c\). Every solution satisfies

$$
\boxed{
(2Pa+r_a)^2-(2Pb+r_b)^2
=
\widetilde c+kD
}
\tag{5.4}
$$

for an integer \(k\) with

$$
\boxed{|k|\le P^2.}
\tag{5.5}
$$

Equivalently,

$$
\boxed{
\bigl(2P(a-b)+r_a-r_b\bigr)
\bigl(2P(a+b)+r_a+r_b\bigr)
=
\widetilde c+kD.
}
\tag{5.6}
$$

The first unproved number-theoretic estimate is therefore

$$
\boxed{
\sup_{c\ne0}
\#\left\{
p:
\frac{p+c/p}{2},\,
\frac{c/p-p}{2}
\in\mathcal T
\right\}
\le20.
}
\tag{HF20}
$$

No proof of \((HF20)\), and no exact \(21\)-collision, is obtained here.

---

# 6. Exact physical/product norm duality

Let

$$
\mathcal E_\Gamma
=
\operatorname{span}\{W_g:g\in\Gamma\}
\subset M_D.
$$

Because \(\Gamma=-\Gamma\), this subspace is closed under adjoint.

The Hilbert–Schmidt projection onto \(\mathcal E_\Gamma\) is

$$
\Pi_\Gamma(X)
=
\frac1D
\sum_{g\in\Gamma}
\operatorname{Tr}(W_g^*X)W_g.
$$

By Weyl orthogonality,

$$
\|\Pi_\Gamma(\rho)\|_2^2
=
\frac1D\mathcal F_\Gamma(\rho).
\tag{6.1}
$$

For a density operator \(\rho\),

$$
\|\Pi_\Gamma(\rho)\|_2
=
\sup_{\substack{H\in\mathcal E_\Gamma\\\|H\|_2=1}}
|\operatorname{Tr}(H^*\rho)|.
$$

Maximizing over \(\rho\) and interchanging the two compact suprema gives

$$
\sup_\rho\|\Pi_\Gamma(\rho)\|_2
=
\sup_{\substack{H\in\mathcal E_\Gamma\\\|H\|_2=1}}
w(H),
$$

where

$$
w(H)=\sup_{\|\psi\|=1}
|\langle\psi|H|\psi\rangle|
$$

is the numerical radius.

Because \(\mathcal E_\Gamma\) is adjoint-closed, the supremum may be restricted to Hermitian \(H\). Indeed, after multiplying \(H\) by a scalar phase, its Hermitian part has no larger Hilbert–Schmidt norm and has the same chosen real expectation value. For Hermitian \(H\),

$$
w(H)=\|H\|_\infty.
$$

Therefore

$$
\boxed{
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)
=
D
\sup_{\substack{H=H^*\in\mathcal E_\Gamma\\H\ne0}}
\frac{\|H\|_\infty^2}{\|H\|_2^2}.
}
\tag{6.2}
$$

Write

$$
H=\sum_{g\in\Gamma}c_gW_g.
$$

Hermiticity is equivalent to

$$
c_{-g}=\overline{c_g},
$$

and

$$
\|H\|_2^2=D\sum_g|c_g|^2.
$$

Thus

$$
\boxed{
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)
=
\sup_{\substack{c_{-g}=\overline{c_g}\\c\ne0}}
\frac{
\left\|\sum_gc_gW_g\right\|_\infty^2
}{
\sum_g|c_g|^2
}.
}
\tag{Dual}
$$

Consequently,

$$
\boxed{
\text{PW10}
\iff
\left\|\sum_{g\in\Gamma}c_gW_g\right\|_\infty
\le
\sqrt{10}\,\|c\|_2
\quad
\forall\,c_{-g}=\overline{c_g}.
}
\tag{WR10}
$$

This is an exact reformulation, not a relaxation.

If \((WR10)\) fails for a coefficient vector \(c\), a unit eigenvector of the corresponding Hermitian Weyl polynomial supplies a physical violating \(\psi\).

Conversely, for a violating \(\psi\), setting

$$
c_g=
\frac{
\overline{\langle\psi|W_g|\psi\rangle}
}{
\sqrt{\mathcal F_\Gamma(\psi)}
}
$$

produces a Hermitian coefficient vector of norm one violating \((WR10)\).

---

# 7. Fiber20 as only a \(2\times2\) compression

Fix \(c\ne0\), let \(h=|H_c|\), and choose \(x\in\mathbb F_D\).

For \((p,c)\in\Gamma\), set

$$
d_{(p,c)}
=
\frac1{\sqrt{2h}}
\omega^{-p(x+c/2)},
$$

and impose Hermiticity by

$$
d_{(-p,-c)}
=
\overline{d_{(p,c)}}.
$$

Then

$$
\sum_g|d_g|^2=1.
$$

For

$$
H_d=\sum_gd_gW_g,
$$

the matrix element from \(|x\rangle\) to \(|x+c\rangle\) is

$$
\begin{aligned}
\langle x+c|H_d|x\rangle
&=
\sum_{p\in H_c}
\frac1{\sqrt{2h}}\\
&=
\sqrt{\frac h2}.
\end{aligned}
$$

Hence

$$
\|H_d\|_\infty^2\ge\frac h2.
$$

The exact duality gives

$$
\boxed{
\sup_\rho\mathcal F_\Gamma(\rho)
\ge
\frac12\max_{c\ne0}|H_c|.
}
\tag{7.1}
$$

This recovers Fiber and Fiber20.

It also makes clear why Fiber20 is not sufficient: it controls only one matrix element, or equivalently one \(2\times2\) principal compression, of every Hermitian Weyl polynomial in \(\mathcal E_\Gamma\). PW10 requires the full operator norm.

---

# 8. Explicit frozen oscillatory-operator form

The integer Sidon property and no-wrap bounds imply that the first coordinates

$$
\Delta=\{t_a-t_b:a\ne b\}
$$

are distinct modulo \(D\). Hence \(\Gamma\) is the graph of a function

$$
q:\Delta\to\mathbb F_D,
\qquad
q(p)=t_a^2-t_b^2
$$

for the unique pair with \(p=t_a-t_b\).

For

$$
H_c=\sum_{p\in\Delta}c_pW_{(p,q(p))},
$$

the computational-basis action is

$$
\boxed{
(H_cf)(y)
=
\sum_{p\in\Delta}
c_p\,
\omega^{py-pq(p)/2}
f(y-q(p)).
}
\tag{8.1}
$$

Hermiticity is

$$
c_{-p}=\overline{c_p},
\qquad
q(-p)=-q(p).
$$

Thus PW10 is exactly the finite oscillatory estimate

$$
\boxed{
\sum_{y\in\mathbb F_D}
\left|
\sum_{p\in\Delta}
c_p\omega^{py-pq(p)/2}
f(y-q(p))
\right|^2
\le
10
\left(\sum_p|c_p|^2\right)
\left(\sum_y|f(y)|^2\right)
}
\tag{8.2}
$$

for every Hermitian coefficient vector \(c\) and every \(f\in\mathbb C^D\).

This is the first exact finite inequality whose proof would close PW10. A counterexample to it immediately gives a physical violating state.

---

# 9. Exact affine-fiber decomposition of the product norm

For a unit vector \(\psi\), define

$$
b_q^\psi(x)
=
\overline{\psi_{x+q}}\psi_x.
\tag{9.1}
$$

From the Weyl action,

$$
\langle\psi|W_{(p,q)}|\psi\rangle
=
\omega^{pq/2}
\sum_x b_q^\psi(x)\omega^{px}.
\tag{9.2}
$$

Therefore

$$
\boxed{
\mathcal F_\Gamma(\psi)
=
\sum_{q\ne0}
\sum_{p\in H_q}
\left|
\sum_xb_q^\psi(x)\omega^{px}
\right|^2.
}
\tag{AF}
$$

The arrays \(b_q^\psi\) are not independent. They obey

$$
\boxed{
b_{-q}(x+q)=\overline{b_q(x)},
}
\tag{9.3}
$$

$$
\boxed{
\sum_{q,x}|b_q(x)|^2=1,
}
\tag{9.4}
$$

and, crucially, the rank-one cocycle identities

$$
\boxed{
b_q(x)b_r(x+q)
=
b_{q+r}(x)b_0(x+q)
\quad
\forall x,q,r.
}
\tag{9.5}
$$

If one discards (9.5) and keeps only the norm condition (9.4), the resulting Fourier-restriction relaxation has value \(D\): for any nonempty \(H_q\), a single Fourier character gives restriction energy \(D\). Since \(D\gg10\), norm control alone is useless.

Thus another exact statement equivalent to PW10 is:

$$
\boxed{
\sum_{q\ne0}
\sum_{p\in H_q}
|\widehat b_q(p)|^2
\le10
}
\tag{AF10}
$$

for every collection \(b_q\) generated from one vector \(\psi\), equivalently satisfying the rank-one factorization (9.1). The first missing content is control supplied by the nonlinear cocycle (9.5).

---

# 10. Bell weights and the exact spectral formula

Define

$$
r_x=\operatorname{Tr}(W_x^*\rho).
$$

Use the relabeled Bell basis

$$
|\widetilde E_x\rangle\rangle
=
|E_{\vartheta x}\rangle\rangle.
$$

Then

$$
K_\Gamma|\widetilde E_x\rangle\rangle
=
\lambda_x|\widetilde E_x\rangle\rangle.
$$

Also,

$$
|\psi\rangle\otimes|\overline\psi\rangle
=
|\overline\rho\rangle\rangle.
$$

A direct vectorization calculation gives

$$
\boxed{
\left|
\langle\langle\widetilde E_x|
\psi\otimes\overline\psi
\rangle
\right|^2
=
\frac{|r_x|^2}{D}.
}
\tag{10.1}
$$

Therefore

$$
\boxed{
\mathcal F_\Gamma(\rho)
=
\frac1D\sum_{x\in\mathbb F_D^2}
\lambda_x|r_x|^2.
}
\tag{10.2}
$$

Equivalently, defining

$$
w_x=\frac{|r_x|^2}{D},
$$

one has

$$
\mathcal F_\Gamma(\rho)=\sum_x\lambda_xw_x.
\tag{10.3}
$$

Every pure state satisfies

$$
w_x\ge0,
\qquad
\sum_xw_x=1,
\tag{10.4}
$$

$$
w_0=\frac1D,
\qquad
w_x\le\frac1D,
\qquad
w_{-x}=w_x.
\tag{10.5}
$$

These are necessary, but not sufficient, Bell-overlap constraints.

---

# 11. At least \(D\) Bell eigenvalues exceed \(10\)

Put

$$
M=|\Gamma|=m(m-1).
$$

The spectrum satisfies

$$
\lambda_0=M,
\tag{11.1}
$$

$$
-m\le\lambda_x\le M,
\tag{11.2}
$$

$$
\sum_x\lambda_x=0,
\tag{11.3}
$$

and, by Fourier Parseval,

$$
\boxed{
\sum_x\lambda_x^2=D^2M.
}
\tag{11.4}
$$

Let

$$
\mathcal B=\{x:\lambda_x>10\},
\qquad
b=|\mathcal B|.
$$

Assume for contradiction that \(b\le D-1\).

Let

$$
P_+=\sum_{\lambda_x>0}\lambda_x.
$$

Since the total sum is zero,

$$
P_+=-\sum_{\lambda_x<0}\lambda_x.
$$

For negative eigenvalues,

$$
\sum_{\lambda_x<0}\lambda_x^2
\le mP_+.
\tag{11.5}
$$

For positive eigenvalues at most \(10\),

$$
\lambda_x^2\le10\lambda_x.
$$

For the \(b\) large positive eigenvalues,

$$
\sum_{\lambda_x>10}\lambda_x^2\le bM^2.
$$

Hence

$$
D^2M
\le
bM^2+(m+10)P_+.
\tag{11.6}
$$

Moreover,

$$
P_+
\le bM+10(D^2-b)
\le DM+10D^2.
\tag{11.7}
$$

Combining,

$$
D^2M
\le
DM^2+(m+10)(DM+10D^2).
$$

After division by \(D^2M\),

$$
1
\le
\frac MD
+
\frac{m+10}{D}
+
\frac{10(m+10)}{M}.
\tag{11.8}
$$

For the frozen parameters,

$$
m>e^{20}>100,
\qquad
D>4p_0^2>4m^2.
$$

Thus

$$
\frac MD<\frac14,
$$

$$
\frac{m+10}{D}
<
\frac1{300},
$$

and

$$
\frac{10(m+10)}M<\frac18.
$$

The right side of (11.8) is therefore strictly smaller than \(1\), a contradiction.

Hence

$$
\boxed{
|\{x:\lambda_x>10\}|\ge D.
}
\tag{11.9}
$$

Because \(\lambda_{-x}=\lambda_x\), the high-eigenvalue set is centrally symmetric and contains \(0\). Since \(D\) is odd, one may choose a centrally symmetric subset \(\mathcal S\) of exactly \(D\) high-eigenvalue labels containing \(0\).

Define the relaxed Bell weights

$$
w_x=
\begin{cases}
1/D,&x\in\mathcal S,\\
0,&x\notin\mathcal S.
\end{cases}
$$

Then (10.4)–(10.5) all hold, but

$$
\sum_x\lambda_xw_x>10.
$$

Therefore:

$$
\boxed{
\text{The cap, normalization, evenness, and fixed }w_0
\text{ constraints do not prove PW10.}
}
\tag{11.10}
$$

What fails is physical attainability: these weights have not been shown to arise from any pure-state characteristic function.

---

# 12. The exact remaining physical constraint

A pure-state characteristic vector satisfies

$$
r_0=1,
\qquad
r_{-x}=\overline{r_x},
\qquad
\sum_x|r_x|^2=D,
$$

and the twisted idempotence equations

$$
\boxed{
r_k
=
\frac1D
\sum_h
r_h r_{k-h}\omega^{[h,k]/2}
\quad
\forall k.
}
\tag{12.1}
$$

The Bell-cap relaxation in Section 11 omits precisely these phase-coupled quadratic equations.

The spectral formulation of the unresolved gate is therefore

$$
\boxed{
\frac1D
\sum_x\lambda_x|r_x|^2
\le10
}
\tag{12.2}
$$

for every \(r\) satisfying (12.1) and the Hermiticity/normalization conditions.

The fact that at least \(D\) eigenvalues exceed \(10\) shows that neither eigenvalue counting nor the elementary Bell-overlap cap can establish (12.2). A constructive violation must solve the twisted equations while placing enough characteristic mass on the high-\(\lambda\) set.

---

# 13. First precise unresolved inequality

For the canonically frozen graph

$$
\Gamma=\{(p,q(p)):p\in\Delta\},
$$

the earliest exact missing inequality is

$$
\boxed{
\left\|
\sum_{p\in\Delta}
c_pW_{(p,q(p))}
\right\|_\infty^2
\le
10\sum_{p\in\Delta}|c_p|^2
\quad
\forall\,c_{-p}=\overline{c_p}.
}
\tag{13.1}
$$

Equivalently, in coordinates,

$$
\boxed{
\sum_y
\left|
\sum_{p\in\Delta}
c_p
\omega^{py-pq(p)/2}
f(y-q(p))
\right|^2
\le
10\|c\|_2^2\|f\|_2^2.
}
\tag{13.2}
$$

This condition is strictly more informative than merely restating PW10:

* it is a linear operator-norm inequality on an explicitly specified finite family of Weyl shifts;
* a violating coefficient vector directly produces a physical violating eigenstate;
* Fiber20 is recovered by testing only one off-diagonal matrix entry;
* the Bell spectrum controls the commuting doubled representation, whereas (13.1) controls the noncommuting single-system Weyl polynomial.

No proof or counterexample to (13.1) is obtained here.

Because PW10 is not settled, the downstream all-\(T\) ratio is not analyzed in this round.

---

# Audit ledger

| Status             | Statement                                                                                                 |                              |           |                              |    |
| ------------------ | --------------------------------------------------------------------------------------------------------- | ---------------------------- | --------- | ---------------------------- | -- |
| **PROVED**         | \(g\mapsto W_g\otimes\overline{W_g}\) is an ordinary commuting representation.                            |                              |           |                              |    |
| **PROVED**         | Bell diagonalization with the corrected reflection \(K_\Gamma E_{\vartheta x}=\lambda_xE_{\vartheta x}\). |                              |           |                              |    |
| **PROVED**         | (\lambda_x=\left                                                                                          | \sum_a\omega^{[s_a,x]}\right | ^2-m).    |                              |    |
| **PROVED**         | \(K\)-product and partial-transpose identities.                                                           |                              |           |                              |    |
| **PROVED**         | Exact two-level formula (\mathcal F_\Gamma=                                                               | H_c                          | /2).      |                              |    |
| **NECESSARY-ONLY** | Fiber20: (                                                                                                | H_c                          | \le20).   |                              |    |
| **PROVED**         | One-variable horizontal-fiber equation (5.1).                                                             |                              |           |                              |    |
| **PROVED**         | Squared-set reduction (                                                                                   | H_c                          | =         | \mathcal V\cap(\mathcal V+c) | ). |
| **PROVED**         | General bound (                                                                                           | H_c                          | \le m-1). |                              |    |
| **OPEN**           | Whether the frozen squared set has difference multiplicity at most \(20\).                                |                              |           |                              |    |
| **OPEN**           | Whether an exact \(c\) has at least \(21\) frozen ordered representations.                                |                              |           |                              |    |
| **PROVED — new**   | Exact physical/Weyl-polynomial duality (Dual).                                                            |                              |           |                              |    |
| **PROVED — new**   | PW10 is equivalent to the \(\sqrt{10}\) Weyl-polynomial bound (WR10).                                     |                              |           |                              |    |
| **PROVED — new**   | Fiber20 is only a \(2\times2\) compression of WR10.                                                       |                              |           |                              |    |
| **PROVED — new**   | Exact affine-fiber Fourier decomposition (AF).                                                            |                              |           |                              |    |
| **PROVED — new**   | Exact rank-one cocycle constraints (9.3)–(9.5).                                                           |                              |           |                              |    |
| **DISPROVED**      | Sufficiency of the norm-only affine-fiber relaxation; its value is \(D\).                                 |                              |           |                              |    |
| **PROVED**         | Exact Bell spectral formula (\mathcal F=D^{-1}\sum_x\lambda_x                                             | r_x                          | ^2).      |                              |    |
| **PROVED — new**   | At least \(D\) Bell eigenvalues satisfy \(\lambda_x>10\).                                                 |                              |           |                              |    |
| **DISPROVED**      | Sufficiency of Bell-weight normalization, cap, evenness, and fixed \(w_0\).                               |                              |           |                              |    |
| **NECESSARY-ONLY** | Stabilizer-line tests and two-level fiber tests.                                                          |                              |           |                              |    |
| **OPEN**           | The restricted Weyl-polynomial estimate (13.1).                                                           |                              |           |                              |    |
| **OPEN**           | The twisted-idempotent high-spectrum mass inequality (12.2).                                              |                              |           |                              |    |
| **OPEN**           | PW10 for the canonically frozen tuple.                                                                    |                              |           |                              |    |
| **OPEN**           | \((E1_{\mathrm{gap}})\).                                                                                  |                              |           |                              |    |
| **CONJECTURED**    | None promoted.                                                                                            |                              |           |                              |    |

The first new claim needing independent verification is the exact duality

$$
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)
=
\sup_{c_{-g}=\overline{c_g}}
\frac{\|\sum_gc_gW_g\|_\infty^2}{\sum_g|c_g|^2}.
$$

The first unresolved statement is the finite oscillatory inequality (13.2), equivalently \((WR10)\).

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-08-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-08-local-audit.md bytes=9784 sha256=8ec599928987e9fef428f514d7c54ec4e6705125b09734e781ce236736a50289 -->

# Round 08 independent local audit

## Capture integrity

- Conversation: `Audit quantum construction`
- Surface/model observed at send time: ordinary Chat, GPT-5.6 Sol, Pro 5/5
- Browser completion indicator for this response: `Worked for 17m 33s`
- Captured response: 24,807 bytes; 24,785 Unicode characters
- Response SHA-256:
  `b6f69056a998e9a6a1fd325334915dff8d5157922a39a69edc3fb06d2341d8cb`
- The artifact and output copies are byte-identical to the text exported from
  the browser copy action.
- The prompt retains its pre-send SHA-256:
  `42803d948018cf433a2105f9f974c7054e22ed77c174162de6e941307d93a33d`.
  Its correct size is 7,017 bytes / 7,015 Unicode characters; the staging
  record's earlier `7,015 bytes` entry counted characters rather than UTF-8
  bytes. The browser composer contained the expected 7,014 characters after
  removal of the one terminal newline.

## Verdict

**OPEN WITH EARLIEST GAP.** Round 08 does not prove or disprove PW10 for the
canonically frozen tuple. It correctly verifies the doubled-Weyl formulas,
the two-level horizontal-fiber test, an exact Weyl-polynomial duality, and a
nontrivial obstruction to elementary Bell-weight relaxations. None of those
results supplies the required uniform constant-10 bound or a physical
violating state.

The most useful new exact reformulation is

$$
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)
=
\sup_{\substack{c_{-g}=\overline{c_g}\\c\ne0}}
\frac{\|\sum_{g\in\Gamma}c_gW_g\|_\infty^2}
     {\sum_{g\in\Gamma}|c_g|^2}.
$$

Consequently the still-open gate is the Hermitian Weyl-polynomial estimate

$$
\left\|\sum_{g\in\Gamma}c_gW_g\right\|_\infty^2
\le10\sum_{g\in\Gamma}|c_g|^2
\quad\text{for every }c_{-g}=\overline{c_g}.
\tag{WR10}
$$

This is an exact structural dual of PW10, not a proof and not a logically
smaller condition. The horizontal-fiber bound $|H_c|\le20$ remains only a
necessary test.

## Claims independently verified

### 1. Canonical parameters have an additional exact structure

High-precision evaluation gives

$$
m_0=485165196.
$$

Deterministic primality checks in the 64-bit range give

$$
p_0=485165237=m_0+41
$$

and

$$
D_0=941541228773064677=4p_0^2+1.
$$

In particular, $D_0$ is already the first integer after $4p_0^2$ and is
prime, so it is necessarily the least prime required by the frozen
definition. Therefore

$$
i:=2p_0\quad\text{satisfies}\quad i^2=-1\pmod {D_0},
$$

and the actual tuple may be written exactly as

$$
t_j=r_j+ij,
\qquad r_j=j^2\bmod p_0,
\qquad 0\le j\le p_0-42.
$$

The web response never uses these concrete equalities. They provide a real
next direction rather than another generic restatement of the frozen set.

### 2. Doubled representation and Bell-label reflection

Direct multiplication gives

$$
W_gW_h=\omega^{[g,h]/2}W_{g+h}.
$$

Entrywise conjugation reverses the cocycle, hence

$$
(W_g\otimes\overline{W_g})(W_h\otimes\overline{W_h})
=W_{g+h}\otimes\overline{W_{g+h}}.
$$

For the response's vectorization
$|X\rangle\rangle=\sum_j|j\rangle\otimes X|j\rangle$, one has

$$
(A\otimes B)|X\rangle\rangle=|BXA^{\mathsf T}\rangle\rangle,
$$

$$
\overline{W_{(p,q)}}=W_{(-p,q)},
\qquad
W_{(p,q)}^{\mathsf T}=W_{(p,-q)}.
$$

Thus the response's reflected label
$\vartheta(p,q)=(p,-q)$ is correct:

$$
K_\Gamma|E_{\vartheta x}\rangle\rangle
=\lambda_x|E_{\vartheta x}\rangle\rangle,
$$

where

$$
\lambda_x
=\sum_{g\in\Gamma}\omega^{[g,x]}
=\left|\sum_a\omega^{[s_a,x]}\right|^2-m.
$$

A direct $D=5$ matrix smoke test independently reproduced the product
identity and this reflected Bell spectrum to errors below
$4\times10^{-16}$; the symbolic identities above are the proof.

### 3. Product and partial-transpose identities

For every unit vector $\psi$,

$$
\langle\psi\otimes\overline\psi|
 W_g\otimes\overline{W_g}
|\psi\otimes\overline\psi\rangle
=|\langle\psi|W_g|\psi\rangle|^2.
$$

Also $(\overline W_g)^{\mathsf T}=W_g^*$, so partial transpose gives the
same scalar on $\psi\otimes\psi$. No factor of $D$ is missing from either
formula.

### 4. Exact two-level formula

The action

$$
W_{(p,q)}|y\rangle=\omega^{p(y+q/2)}|y+q\rangle
$$

shows that the two-level state supported on $\{x,x+c\}$ has a nonzero Weyl
expectation, among points of $\Gamma$, only for $q=c$ and $q=-c$. Each
contribution has squared modulus $1/4$. Since $D$ is odd, $2c\ne0$; since
$\Gamma$ has no point with second coordinate zero, there is no extra
diagonal term. Central symmetry gives $|H_{-c}|=|H_c|$. Therefore

$$
\mathcal F_\Gamma(\rho_{x,c,\theta})=\frac{|H_c|}{2}.
$$

Thus $|H_c|\le20$ is necessary for PW10, and an exact fiber of size at least
21 would be a physical counterexample.

### 5. Horizontal-fiber reductions

For $p=t_a-t_b\ne0$ and $c=t_a^2-t_b^2$,

$$
t_a=\frac{p+c/p}{2},
\qquad
t_b=\frac{c/p-p}{2}.
$$

Ordered-difference uniqueness makes this a bijective one-variable count,
so the response's equation (5.1) is exact. Because squaring is injective on
$\mathcal T$, the equivalent identity

$$
|H_c|=r_{\mathcal V-\mathcal V}(c)
=|\mathcal V\cap(\mathcal V+c)|,
\qquad
\mathcal V=\{t_j^2\},
$$

is also correct. The general $m-1$ bound follows because translation by a
nonzero element is a single cycle in the prime-order additive group.

The integer-lift estimate $|k|\le p_0^2$ is valid but far too weak. Using
the concrete modulus gives the sharper structural identity

$$
t_j^2\equiv(r_j^2-j^2)+2p_0(2jr_j)\pmod {4p_0^2+1}.
$$

No uniform fiber bound follows yet.

### 6. Exact Weyl-polynomial duality

Let $\Pi_\Gamma$ be Hilbert--Schmidt projection onto the adjoint-closed
space $\mathcal E_\Gamma=\operatorname{span}\{W_g:g\in\Gamma\}$. Then

$$
\mathcal F_\Gamma(\rho)=D\|\Pi_\Gamma(\rho)\|_2^2.
$$

Dualizing the Hilbert--Schmidt norm and maximizing over states gives the
maximum numerical radius over the unit Hilbert--Schmidt sphere in
$\mathcal E_\Gamma$. For any maximizing matrix, rotate its phase and take
its Hermitian part. This preserves the chosen real expectation, does not
increase Hilbert--Schmidt norm, and remains in $\mathcal E_\Gamma$. On
Hermitian matrices numerical radius equals operator norm. Finally

$$
H=\sum_gc_gW_g=H^*
\iff c_{-g}=\overline{c_g},
\qquad
\|H\|_2^2=D\sum_g|c_g|^2.
$$

These steps prove the displayed duality exactly. Conversely, an operator
violating WR10 has a physical extremal eigenvector, and a state violating
PW10 produces a violating coefficient vector by normalized conjugate Weyl
expectations.

### 7. Fiber compression, oscillatory form, and affine decomposition

The response's coefficient choice on one horizontal fiber is Hermitian and
has coefficient norm one. Its two-dimensional compression has off-diagonal
entry $\sqrt{|H_c|/2}$, proving

$$
\sup_\rho\mathcal F_\Gamma(\rho)
\ge\frac12\max_{c\ne0}|H_c|.
$$

The computational-basis formula for the Weyl polynomial is also correct.
For

$$
b_q(x)=\overline{\psi_{x+q}}\psi_x,
$$

the Fourier restriction identity and the relations

$$
b_{-q}(x+q)=\overline{b_q(x)},
$$

$$
\sum_{q,x}|b_q(x)|^2=1,
$$

$$
b_q(x)b_r(x+q)=b_{q+r}(x)b_0(x+q)
$$

all follow directly. If the nonlinear rank-one relation is discarded, full
Fourier Parseval gives relaxation value exactly $D$, so that relaxation
cannot prove a constant-10 bound.

### 8. Bell weights and the high-eigenvalue obstruction

For a pure-state Weyl characteristic vector
$r_x=\operatorname{Tr}(W_x^*\rho)$, the reflected Bell decomposition gives

$$
\mathcal F_\Gamma(\rho)=\frac1D\sum_x\lambda_x|r_x|^2.
$$

The elementary constraints

$$
w_x=|r_x|^2/D\ge0,
\quad
\sum_xw_x=1,
\quad
w_0=1/D,
\quad
w_x\le1/D,
\quad
w_{-x}=w_x
$$

are correct and necessary.

The response's proof that at least $D$ eigenvalues exceed 10 is valid. It
uses

$$
\lambda_0=m(m-1),
\quad
-m\le\lambda_x\le m(m-1),
\quad
\sum_x\lambda_x=0,
\quad
\sum_x\lambda_x^2=D^2m(m-1),
$$

and a contradiction bound on the positive spectral mass. The numerical
fractions used there are very loose but valid for $m>e^{20}$ and
$D>4m^2$.

A symmetric set of exactly $D$ high-eigenvalue labels therefore supports
relaxed weights obeying all the elementary constraints while having
expectation above 10. This correctly disproves that relaxation only. It
does not provide a pure state because the twisted-idempotence equations are
still absent.

## Corrections and limitations

1. WR10 is exactly equivalent to PW10. Calling it "strictly more
   informative" is defensible only as a change of coordinates exposing an
   operator-norm attack; it is not a logically narrower result and does not
   advance the theorem's truth status by itself.

2. The response does not use the strongest concrete arithmetic fact about
   the frozen tuple: $D_0=4p_0^2+1$. Its horizontal-fiber section therefore
   stops before the new Gaussian/base-$2p_0$ carry system that should be
   audited next.

3. Fiber20 remains necessary-only. Even a proof of every horizontal-fiber
   bound would not establish WR10 without controlling simultaneous fibers
   and their phases.

4. The statement about at least $D$ Bell eigenvalues above 10 is a valid
   obstruction to a weak relaxation, not evidence of a physical
   counterexample.

5. The final Markdown ledger is malformed because unescaped vertical bars
   inside formulas are parsed as table delimiters. This is a presentation
   defect, not a mathematical one.

## Earliest open gates after this audit

- Full one-copy gate: WR10/PW10 for the single frozen tuple.
- Necessary combinatorial subtest: prove $|H_c|\le20$ for all $c\ne0$, or
  exhibit one exact 21-collision.
- Physical spectral route: control high-$\lambda$ mass under the full
  twisted-idempotence equations, not only elementary Bell weights.
- Downstream all-$T$, $E1_{\rm gap}$, and the full-size theorem remain open.

Status: **COMPLETED — LOCALLY AUDITED; PW10 REMAINS OPEN.**

<!-- END HISTORICAL FILE path=outputs/round-08-local-audit.md -->


# ROUND 009

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-09-prompt.md bytes=6998 sha256=5c336cfbcc8d73e56d9a767ef6323239cf3918f32334e825f888faa04a273474 -->

# Round 9 — exploit the exact modulus: bounded carries and Weyl-polynomial moments

Continue in the same conversation and the same finite $r=2$ low-$A$ gate.
Give a public, self-contained derivation and no hidden chain-of-thought. Do
not repeat the broad Round 8 discussion; use the new exact arithmetic below.

## Audited boundary from Round 8

The following identities were independently checked.

For

$$
W_{(p,q)}=\omega^{-pq/2}Z^pX^q,
\qquad
\Gamma=\{(t_a-t_b,t_a^2-t_b^2):a\ne b\},
$$

the one-copy gate for the one frozen tuple is

$$
\boxed{
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)\le10,
\qquad
\mathcal F_\Gamma(\rho)
=\sum_{g\in\Gamma}|\operatorname{Tr}(W_g^*\rho)|^2.
}
\tag{PW10}
$$

It has the exact Hermitian Weyl-polynomial dual

$$
\boxed{
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)
=
\sup_{\substack{c_{-g}=\overline{c_g}\\c\ne0}}
\frac{\|\sum_{g\in\Gamma}c_gW_g\|_\infty^2}
{\sum_{g\in\Gamma}|c_g|^2}.
}
\tag{Dual}
$$

Thus PW10 is equivalent to

$$
\left\|\sum_{g\in\Gamma}c_gW_g\right\|_\infty^2
\le10\sum_{g\in\Gamma}|c_g|^2
\quad\forall c_{-g}=\overline{c_g}.
\tag{WR10}
$$

This equivalence is correct, but it is a structural change of coordinates,
not by itself progress on the truth of PW10.

For

$$
H_c=\{p:(p,c)\in\Gamma\},
$$

the two-level test is exactly

$$
\mathcal F_\Gamma(\rho_{x,c,\theta})=\frac{|H_c|}{2}.
\tag{Fiber}
$$

Hence $|H_c|\le20$ for every nonzero $c$ is necessary only. Also

$$
|H_c|
=\#\left\{u\ne0:
\frac{u+c/u}{2}\in\mathcal T,
\frac{c/u-u}{2}\in\mathcal T
\right\}
=r_{\mathcal V-\mathcal V}(c),
\quad
\mathcal V=\{t_j^2\}.
\tag{HF}
$$

Round 8 proved that elementary Bell-weight constraints are insufficient;
at least $D$ Bell eigenvalues exceed 10. This is not a physical
counterexample because twisted idempotence is still missing.

## New exact arithmetic of the single frozen tuple

Independent exact computation gives

$$
m_0=485165196,
\qquad
P:=p_0=485165237=m_0+41,
$$

and, crucially,

$$
\boxed{
D:=D_0=941541228773064677=4P^2+1.
}
\tag{ExactD}
$$

Both displayed large integers pass deterministic primality verification in
the 64-bit range. Since $D$ is the integer immediately after $4P^2$, this
also proves that it is the least prime required by the canonical freeze.
Audit the arithmetic, but do not replace it by a generic Bertrand bound.

Put

$$
i=2P\in\mathbb F_D.
$$

Then

$$
\boxed{i^2=-1\pmod D.}
$$

The index range is the nearly complete interval

$$
0\le j\le P-42.
$$

Writing

$$
r_j=j^2-Pk_j,
\qquad
k_j=\left\lfloor\frac{j^2}{P}\right\rfloor,
\qquad
0\le r_j<P,
$$

the actual frozen elements are

$$
\boxed{t_j=r_j+ij.}
\tag{GaussianT}
$$

Their squares have the exact two-coordinate form

$$
\boxed{
t_j^2\equiv A_j+iB_j\pmod D,
\qquad
A_j=r_j^2-j^2,
\qquad
B_j=2jr_j.
}
\tag{AB}
$$

The representation $A+iB$ is not automatically unique because $A$ and $B$
are larger than a balanced base-$i$ digit. Every use of it must explicitly
track the modulus/carry.

For two representations of the same nonzero squared difference, define

$$
\Delta A=(A_a-A_b)-(A_u-A_v),
\qquad
\Delta B=(B_a-B_b)-(B_u-B_v).
$$

Then the collision is exactly

$$
\Delta A+i\Delta B=n(i^2+1)
\tag{Carry0}
$$

for an integer $n$. Because $0\le j,r_j<P$, derive the best correct bounds
on $\Delta A,\Delta B,n$. Reducing modulo $i$ gives

$$
n\equiv\Delta A\pmod i,
$$

so once the correct bounded representative of $n$ is fixed, the remaining
integer equation is

$$
\Delta B=in+\frac{n-\Delta A}{i}.
\tag{Carry1}
$$

Audit this derivation and use it; do not silently treat $A+iB$ as a unique
Gaussian expansion.

Modulo $P$ one also has

$$
A_j\equiv j^4-j^2\pmod P,
\qquad
B_j\equiv2j^3\pmod P.
\tag{CurveP}
$$

Determine rigorously whether the polynomial curve in (CurveP), together
with the bounded carry in (Carry1) and the omission of only the final 41
residues, gives a uniform bound on squared-difference multiplicities.

## Exact tasks

1. Give one verdict for PW10 on this exact tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**. A numerical experiment,
   an unrestricted relaxation, or a generic asymptotic heuristic is not a
   verdict.

2. Verify the exact constants in (ExactD), the square root of minus one, the
   range $j\le P-42$, and (AB). If primality is used, give a short
   reproducible certificate or a deterministic verification route rather
   than saying only "computed."

3. Fully derive the bounded-carry collision system (Carry0)--(Carry1).
   Normalize all integer representatives and prove every range bound. Then
   do one of the following:

   - prove $|H_c|\le20$ for all $c\ne0$;
   - give one exact $c$ and 21 distinct ordered pairs for it; or
   - reduce the multiplicity to a genuinely smaller explicit collection of
     polynomial/carry equations, state how many carry cases remain, and
     identify one precise estimate not equivalent to merely restating HF.

   A Bezout or resultant count is acceptable only after showing that every
   carry case lands on the stated algebraic system and after treating
   degenerate components. Do not enumerate $m^2$ pairs.

4. Use $m=P-41$ rather than treating the index set as an arbitrary sparse
   subset. Decide whether completing the 41 missing residues helps by an
   exact comparison with the full set $j\in\mathbb F_P$. Any comparison
   between arithmetic modulo $P$ and modulo $D=4P^2+1$ must retain the carry;
   reduction modulo $P$ alone is not injective.

5. Attack WR10 using the new arithmetic. For

$$
H=\sum_{g\in\Gamma}c_gW_g=H^*,
$$

derive the exact twisted-convolution coefficients of $H^2$ and at least one
nontrivial even-moment, Cotlar--Stein, block-compression, or sum-of-squares
bound. Isolate a **sufficient** combinatorial estimate which would imply

$$
\|H\|_\infty^2\le10\|c\|_2^2.
$$

It must be strictly downstream of checkable collision/carry data, not WR10
written again. Check whether the frozen tuple satisfies it. If the bound is
too weak, compute its exact deficiency and do not promote it.

6. Search for a physical counterexample within an explicit structured
family suggested by (GaussianT): three-level or bounded-support states,
quadratic chirps, or eigenvectors of a Hermitian fiber polynomial. Derive
the objective exactly. A relaxation value above 10 is not a counterexample
without an explicit normalized vector whose exact $\mathcal F_\Gamma$
exceeds 10.

7. Keep the logical hierarchy explicit:

   - Fiber20 is necessary-only;
   - WR10 is equivalent to PW10;
   - Bell eigenvalue abundance is relaxation evidence only;
   - all-$T$, $E1_{\rm gap}$, and the full-size theorem remain downstream.

8. End with a plain list, not a Markdown table, separating **PROVED**,
   **DISPROVED**, **NECESSARY-ONLY**, **OPEN**, and **CONJECTURED**. State
   the first new claim that requires independent verification.

Do not call a reformulation a proof. The finite $r=2$ gate remains OPEN
unless the uniform constant-10 inequality is proved or an exact physical
violator is exhibited.

<!-- END HISTORICAL FILE path=work/round-09-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-09-response.md bytes=22194 sha256=1454072c19c899e810409d1e9a40adf81103a4484b26dacd97b8ce4c522e04df -->

# Verdict

$$
\boxed{\text{PW10 for the canonically frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The exact arithmetic does give two substantive advances:

1. The original carry \(n\), whose a priori range is \(O(P)\), can be replaced by a second exact normalization under which **every squared-difference collision belongs to only five carry classes**

   $$
   \kappa\in\{-2,-1,0,1,2\}.
   $$
2. A new explicit three-level physical witness strengthens the necessary fiber condition from

   $$
   |H_c|\le20
   $$

   to

   $$
   \boxed{
   4\bigl(|H_c|+|S_c|\bigr)+|H_{2c}|\le80,
   \qquad
   S_c:=\sum_{p\in H_c}\omega^{pc}.
   }
   \tag{3L-necessary}
   $$

   In particular, because \(S_c\neq0\) whenever \(H_c\neq\varnothing\),

   $$
   \boxed{|H_c|\le19.}
   \tag{Fiber19}
   $$

Neither result proves PW10. No exact \(c\) violating the three-level condition is produced, and no uniform Weyl-polynomial upper bound with constant \(10\) is proved.

---

# 1. Exact frozen arithmetic

Let

$$
m=485165196,\qquad
P=485165237,\qquad
D=941541228773064677.
$$

## 1.1 The value of \(m\)

Using the Taylor series for \(e^{20}\), with the tail bounded geometrically after any \(N>20\),

$$
\sum_{k=0}^{N}\frac{20^k}{k!}
<
e^{20}
<
\sum_{k=0}^{N}\frac{20^k}{k!}
+
\frac{20^{N+1}}{(N+1)!}
\frac{1}{1-\frac{20}{N+2}},
$$

and taking \(N=100\), one obtains

$$
485165195.40979027796910683054
<
e^{20}
<
485165195.40979027796910683055.
$$

Therefore

$$
\boxed{
m=\min\{n\in\mathbb N:n>e^{20}\}=485165196.
}
$$

Also,

$$
P-m=41,
$$

so the frozen indices are exactly

$$
0\le j\le m-1=P-42.
$$

## 1.2 \(P\) is the least prime above \(m\)

Every even integer between \(m\) and \(P\) is composite. The odd integers have the following displayed proper divisors:

$$
\begin{array}{rclcrcl}
485165197&:&11,
&
485165199&:&3,\\
485165201&:&37,
&
485165203&:&373,\\
485165205&:&3,
&
485165207&:&409,\\
485165209&:&19,
&
485165211&:&3,\\
485165213&:&13,
&
485165215&:&5,\\
485165217&:&3,
&
485165219&:&7,\\
485165221&:&31,
&
485165223&:&3,\\
485165225&:&5,
&
485165227&:&17,\\
485165229&:&3,
&
485165231&:&11779,\\
485165233&:&7,
&
485165235&:&3.
\end{array}
$$

It remains to certify that \(P\) itself is prime.

A short Lucas–Pocklington certificate uses the following complete factorizations and witnesses:

$$
\begin{array}{c|c|c}
N & N-1 & a\\ \hline
3&2&2\\
5&2^2&2\\
11&2\cdot5&2\\
13&2^2\cdot3&2\\
97&2^5\cdot3&5\\
157&2^2\cdot3\cdot13&5\\
389&2^2\cdot97&2\\
331&2\cdot3\cdot5\cdot11&3\\
366439&2\cdot3\cdot157\cdot389&6\\
P&2^2\cdot331\cdot366439&2\\
D&2^2P^2&2.
\end{array}
$$

For every row,

$$
a^{N-1}\equiv1\pmod N
$$

and, for every prime \(q\mid N-1\),

$$
\gcd\!\left(a^{(N-1)/q}-1,N\right)=1.
$$

Because the factorization of \(N-1\) is complete, these conditions force the order of \(a\) modulo every prime divisor of \(N\) to be \(N-1\); hence any prime divisor is at least \(N\), proving \(N\) prime. This is the standard Lucas–Pocklington certificate criterion. ([Inria HAL Science][1])

The entire certificate can be reproduced with exact integer arithmetic:

```python
from math import gcd, prod

cert = {
    3:      (2, {2: 1}),
    5:      (2, {2: 2}),
    11:     (2, {2: 1, 5: 1}),
    13:     (2, {2: 2, 3: 1}),
    97:     (5, {2: 5, 3: 1}),
    157:    (5, {2: 2, 3: 1, 13: 1}),
    389:    (2, {2: 2, 97: 1}),
    331:    (3, {2: 1, 3: 1, 5: 1, 11: 1}),
    366439: (6, {2: 1, 3: 1, 157: 1, 389: 1}),
    485165237:
             (2, {2: 2, 331: 1, 366439: 1}),
    941541228773064677:
             (2, {2: 2, 485165237: 2}),
}

proved = {2}
for N in [3, 5, 11, 13, 97, 157, 389, 331,
          366439, 485165237, 941541228773064677]:
    a, fac = cert[N]
    assert prod(q**e for q, e in fac.items()) == N - 1
    assert all(q in proved for q in fac)
    assert pow(a, N - 1, N) == 1
    assert all(gcd(pow(a, (N - 1)//q, N) - 1, N) == 1
               for q in fac)
    proved.add(N)
```

Thus \(P\) is indeed the least prime above \(m\).

## 1.3 Exact value and primality of \(D\)

Direct multiplication gives

$$
P^2=235385307193266169
$$

and

$$
4P^2+1
=
941541228773064677
=
D.
$$

The certificate above proves \(D\) prime. Since \(D\) is literally the integer immediately following \(4P^2\), it is automatically the least prime exceeding \(4P^2\).

Put

$$
\iota:=2P=970330474.
$$

Then, as an exact integer identity,

$$
\iota^2=4P^2=D-1,
$$

so

$$
\boxed{\iota^2\equiv-1\pmod D.}
$$

---

# 2. Exact Gaussian-coordinate formula

For

$$
0\le j\le P-42,
$$

write

$$
j^2=Pk_j+r_j,
\qquad
k_j=\left\lfloor\frac{j^2}{P}\right\rfloor,
\qquad
0\le r_j<P.
$$

The frozen point is

$$
t_j=2Pj+r_j=r_j+\iota j.
$$

Squaring modulo \(D\) and using \(\iota^2\equiv-1\) gives

$$
t_j^2
\equiv
r_j^2-j^2+\iota(2jr_j)
\pmod D.
$$

Thus the proposed coordinates are correct:

$$
\boxed{
t_j^2\equiv A_j+\iota B_j\pmod D,
}
$$

where

$$
\boxed{
A_j=r_j^2-j^2,\qquad
B_j=2jr_j.
}
$$

Modulo \(P\),

$$
r_j\equiv j^2\pmod P,
$$

and therefore

$$
\boxed{
A_j\equiv j^4-j^2\pmod P,
\qquad
B_j\equiv2j^3\pmod P.
}
$$

---

# 3. The original bounded-carry system

Suppose two ordered squared differences coincide:

$$
t_a^2-t_b^2
\equiv
t_u^2-t_v^2
\pmod D.
$$

Set

$$
\Delta A=(A_a-A_b)-(A_u-A_v),
$$

$$
\Delta B=(B_a-B_b)-(B_u-B_v).
$$

Then there is a unique integer \(n\) such that

$$
\boxed{
\Delta A+\iota\Delta B=nD=n(\iota^2+1).
}
\tag{3.1}
$$

This is exactly `Carry0`.

## 3.1 Sharp box bounds from the frozen index range

Let

$$
J=P-42.
$$

Since \(0\le j\le J\) and \(0\le r_j\le P-1\),

$$
-J^2\le A_j\le(P-1)^2
$$

and

$$
0\le B_j\le2J(P-1).
$$

Consequently,

$$
\boxed{
|\Delta A|
\le
2\bigl((P-1)^2+J^2\bigr)
=
4P^2-172P+3530.
}
\tag{3.2}
$$

Similarly,

$$
\boxed{
|\Delta B|
\le
4J(P-1)
=
4P^2-172P+168.
}
\tag{3.3}
$$

Call these bounds \(M_A\) and \(M_B\).

Then

$$
M_A+\iota M_B
=
(2P-85)D+(162P+3615).
$$

Because

$$
0<162P+3615<D,
$$

equation (3.1) gives

$$
\boxed{|n|\le2P-85=970330389.}
\tag{3.4}
$$

This is the correct bounded representative range.

## 3.2 Derivation of `Carry1`

Reducing (3.1) modulo \(\iota\) gives

$$
n\equiv\Delta A\pmod\iota.
$$

Hence

$$
\ell:=\frac{n-\Delta A}{\iota}\in\mathbb Z.
$$

Substitution into (3.1) gives

$$
\iota\Delta B
=
n\iota^2+n-\Delta A
=
n\iota^2+\iota\ell,
$$

so

$$
\boxed{
\Delta B=\iota n+\ell
=
\iota n+\frac{n-\Delta A}{\iota}.
}
\tag{Carry1}
$$

Equivalently,

$$
\boxed{
\Delta A=n-\iota\ell,
\qquad
\Delta B=\iota n+\ell.
}
\tag{3.5}
$$

There is a symmetric formula

$$
\ell=\frac{\Delta B-\iota\Delta A}{D}.
$$

Using the same box bounds,

$$
M_B+\iota M_A
=
(2P-85)D+(6886P+253),
$$

with

$$
0<6886P+253<D.
$$

Therefore

$$
\boxed{|\ell|\le2P-85.}
\tag{3.6}
$$

Two additional exact constraints are

$$
\boxed{
\Delta A^2+\Delta B^2
=
D(n^2+\ell^2),
}
\tag{3.7}
$$

and, since every \(B_j\) is even,

$$
\boxed{\ell\ \text{is even}.}
\tag{3.8}
$$

## 3.3 Number of possible lifts

Let \(\nu_A\in[-P,P-1]\) be the balanced representative of
\(\Delta A\bmod 2P\). Then the only possible values of \(n\) are

$$
n=\nu_A,
$$

and possibly one further value:

$$
n=
\begin{cases}
\nu_A-2P,&\nu_A\ge85,\\
\nu_A+2P,&\nu_A\le-85.
\end{cases}
$$

Thus there are at most two possible \(n\)-lifts.

The same statement applies to \(\ell\), using
\(\ell\equiv\Delta B\pmod{2P}\). Consequently, once the residues are fixed, there are at most

$$
\boxed{2\times2=4}
$$

possible \((n,\ell)\)-lift branches.

Modulo \(P\), the exact polynomial congruences are

$$
\boxed{
n\equiv
a^4-a^2-b^4+b^2-u^4+u^2+v^4-v^2
\pmod P,
}
\tag{3.9}
$$

$$
\boxed{
\ell\equiv
2(a^3-b^3-u^3+v^3)
\pmod P.
}
\tag{3.10}
$$

These are necessary but do not by themselves retain all quotient data.

---

# 4. A stronger normalization: only five global carry classes

The \(O(P)\) bound on \(n\) is not the best useful normalization.

For each \(j\), divide \(jr_j\) by \(P\):

$$
jr_j=P\sigma_j+h_j,
\qquad
\sigma_j=\left\lfloor\frac{jr_j}{P}\right\rfloor,
\qquad
0\le h_j<P.
$$

Then

$$
h_j\equiv j^3\pmod P.
$$

Because \(j\le P-42\) and \(r_j\le P-1\),

$$
0\le\sigma_j\le P-43.
$$

Define

$$
\boxed{
C_j:=4Ph_j+r_j^2-j^2-\sigma_j.
}
\tag{4.1}
$$

A direct calculation gives

$$
\begin{aligned}
t_j^2
&=4P^2j^2+4Pjr_j+r_j^2\\
&=(D-1)j^2+4P(P\sigma_j+h_j)+r_j^2\\
&=D(j^2+\sigma_j)+C_j.
\end{aligned}
$$

Therefore

$$
\boxed{
t_j^2\equiv C_j\pmod D.
}
\tag{4.2}
$$

Equivalently,

$$
A_j+\iota B_j=D\sigma_j+C_j.
\tag{4.3}
$$

## 4.1 Bounds on \(C_j\)

The frozen index bounds give

$$
\boxed{
-P^2+83P-1721
\le C_j
\le
5P^2-6P+1.
}
\tag{4.4}
$$

Indeed,

$$
C_j
\ge
-(P-42)^2-(P-43)
=
-P^2+83P-1721,
$$

while

$$
C_j
\le
4P(P-1)+(P-1)^2
=
5P^2-6P+1.
$$

Hence, for four indices,

$$
\begin{aligned}
|C_a-C_b-C_u+C_v|
&\le
2\left[
(5P^2-6P+1)-(-P^2+83P-1721)
\right]\\
&=
12P^2-178P+3444.
\end{aligned}
$$

But

$$
3D=12P^2+3,
$$

and

$$
3D-(12P^2-178P+3444)
=
178P-3441>0.
$$

Therefore every collision satisfies

$$
\boxed{
C_a-C_b-C_u+C_v=\kappa D
}
\tag{4.5}
$$

for one of exactly five possible carries:

$$
\boxed{
\kappa\in\{-2,-1,0,1,2\}.
}
\tag{4.6}
$$

This is the strongest useful carry reduction obtained here.

The relation with the original carry is

$$
\boxed{
n=
(\sigma_a-\sigma_b-\sigma_u+\sigma_v)+\kappa.
}
\tag{4.7}
$$

---

# 5. Explicit five-system reduction of horizontal fibers

Fix a reference representation \((u,v)\) of a nonzero squared difference. Put

$$
Y=C_u-C_v.
$$

Every other representation \((a,b)\) lies in one of the five exact systems

$$
\boxed{
C_a-C_b=Y+\kappa D,
\qquad
\kappa=-2,-1,0,1,2.
}
\tag{5.1}
$$

Writing out the quotient variables, the system for a fixed \(\kappa\) is

$$
a^2=Pk_a+r_a,\qquad
ar_a=P\sigma_a+h_a,
$$

$$
b^2=Pk_b+r_b,\qquad
br_b=P\sigma_b+h_b,
$$

with

$$
0\le a,b\le P-42,
$$

$$
0\le r_a,r_b,h_a,h_b<P,
$$

$$
0\le\sigma_a,\sigma_b\le P-43,
$$

and

$$
\boxed{
\begin{aligned}
4P(h_a-h_b)
&+(r_a^2-r_b^2)
-(a^2-b^2)\\
&-(\sigma_a-\sigma_b)
=
Y+\kappa D.
\end{aligned}
}
\tag{5.2}
$$

Modulo \(P\),

$$
\boxed{
a^4-a^2-\sigma_a
-
\bigl(b^4-b^2-\sigma_b\bigr)
\equiv Y+\kappa
\pmod P.
}
\tag{5.3}
$$

The quotient variables \(\sigma_j\) are load-bearing. Dropping them and retaining only the curve

$$
(A_j,B_j)\equiv(j^4-j^2,2j^3)\pmod P
$$

does not retain the exact lift modulo \(D\).

A concrete sufficient arithmetic target is:

$$
\boxed{
\#\{(a,b):C_a-C_b=Y+\kappa D\}\le4
}
\tag{5.4}
$$

for every \(Y\) and every \(\kappa\in\{-2,-1,0,1,2\}\). If (5.4) held, then every horizontal fiber would have size at most \(20\).

I do not prove (5.4). The exact remaining arithmetic problem has nevertheless been reduced from \(O(P)\) possible carries to five explicitly bounded integer systems.

---

# 6. Completing the final 41 residues

Let the completed index set be

$$
0\le j\le P-1.
$$

The frozen set is obtained by deleting exactly

$$
P-41,\ldots,P-1.
$$

For the completed set,

$$
0\le\sigma_j\le P-2
$$

and

$$
-P^2+P+1
\le C_j
\le
5P^2-6P+1.
$$

Thus

$$
|C_a-C_b-C_u+C_v|
\le
12P^2-14P
<
3D.
$$

So the completed set still has exactly the same five carry classes

$$
\kappa=-2,-1,0,1,2.
$$

## 6.1 Exact comparison of frozen and completed fibers

The completed values \(t_j\) are strictly increasing because

$$
t_{j+1}-t_j
=
2P+r_{j+1}-r_j
\ge P+1>0.
$$

Also,

$$
0\le t_j<2P^2<\frac D2.
$$

Therefore

$$
t_j^2\equiv t_k^2\pmod D
$$

implies

$$
t_j\equiv\pm t_k\pmod D.
$$

The positive representatives lie below \(D/2\), so the minus case is impossible except at zero. Thus the completed squared set is injective.

Consequently, for every \(c\),

$$
r_{\mathrm{frozen}}(c)
\le
r_{\mathrm{completed}}(c).
$$

Moreover, for a fixed \(c\), each deleted index can occur in at most one representation as the first endpoint and at most one as the second endpoint. Hence

$$
\boxed{
0\le
r_{\mathrm{completed}}(c)-r_{\mathrm{frozen}}(c)
\le82.
}
\tag{6.1}
$$

Completion is therefore a legitimate upper-bounding device, but it does not by itself prove a constant-\(20\) bound. The quotient term \(\sigma_j\) remains.

---

# 7. Exact twisted convolution for \(H^2\)

Let

$$
H=\sum_{g\in\Gamma}c_gW_g,
\qquad
c_{-g}=\overline{c_g}.
$$

Using

$$
W_gW_h=\omega^{[g,h]/2}W_{g+h},
$$

one obtains

$$
\boxed{
H^2=\sum_{k\in\mathbb F_D^2}d_kW_k,
}
\tag{7.1}
$$

where

$$
\boxed{
d_k
=
\sum_{\substack{g\in\Gamma\\k-g\in\Gamma}}
c_g c_{k-g}\,
\omega^{[g,k]/2}.
}
\tag{7.2}
$$

For \(k=0\),

$$
d_0=\sum_g c_gc_{-g}
=\sum_g|c_g|^2.
$$

Weyl orthogonality then gives the exact fourth moment

$$
\boxed{
\operatorname{Tr}H^4
=
D\sum_k|d_k|^2.
}
\tag{7.3}
$$

More generally,

$$
\boxed{
\begin{aligned}
\frac1D\operatorname{Tr}H^{2r}
={}&
\sum_{\substack{g_1,\ldots,g_{2r}\in\Gamma\\
g_1+\cdots+g_{2r}=0}}
\left(\prod_{j=1}^{2r}c_{g_j}\right)\\
&\times
\omega^{
\frac12\sum_{1\le j<k\le2r}[g_j,g_k]
}.
\end{aligned}
}
\tag{7.4}
$$

The Weyl phase is essential.

---

# 8. A sufficient phase-blind moment estimate—and its exact failure

Define the absolute zero-sum form

$$
\mathfrak A_r(c)
:=
\sum_{\substack{g_1,\ldots,g_{2r}\in\Gamma\\
g_1+\cdots+g_{2r}=0}}
\prod_{j=1}^{2r}|c_{g_j}|.
$$

Then

$$
\frac1D\operatorname{Tr}H^{2r}
\le\mathfrak A_r(c).
$$

Therefore the combinatorial condition

$$
\boxed{
\sup_{\substack{c_{-g}=\overline{c_g}\\
\|c\|_2=1}}
\mathfrak A_r(c)
\le10^r
\quad\text{for every }r
}
\tag{AbsMoment10}
$$

would imply WR10: taking \(2r\)-th roots and then \(r\to\infty\) gives

$$
\|H\|_\infty^2\le10.
$$

This is a genuine sufficient combinatorial estimate. It is stronger than WR10 because it discards every Weyl-phase cancellation.

## 8.1 The frozen tuple fails this sufficient estimate at \(r=14\)

Here

$$
M:=|\Gamma|=m(m-1)
=
235385266924553220.
$$

Since \(D\) is odd, \(\Gamma\) decomposes into

$$
N=\frac M2
$$

unordered inverse pairs \(\{g,-g\}\).

Take

$$
c_g=\frac1{\sqrt M}
\qquad(g\in\Gamma).
$$

This is Hermitian. In the \(28\)-fold absolute moment, choose \(14\) distinct inverse pairs and use each member of each pair exactly once. Every such word has zero total label.

There are

$$
\binom{M/2}{14}28!
$$

such words, each contributing \(M^{-14}\). Hence

$$
\begin{aligned}
\mathfrak A_{14}(c)
&\ge
\binom{M/2}{14}\frac{28!}{M^{14}}\\
&=
27!!
\prod_{j=0}^{13}
\left(1-\frac{2j}{M}\right).
\end{aligned}
$$

Now

$$
27!!=213458046676875
$$

and

$$
\prod_{j=0}^{13}
\left(1-\frac{2j}{M}\right)
\ge
1-\frac{182}{M}.
$$

Therefore

$$
\boxed{
\frac{\mathfrak A_{14}(c)}{10^{14}}
>
2.134580466768748.
}
\tag{8.1}
$$

Thus the frozen tuple does **not** satisfy the phase-blind sufficient condition. Its exact deficiency is already a factor exceeding \(2.13458\) at the \(28\)-th moment.

This is not a PW10 counterexample. It proves that any successful moment argument must exploit substantial cancellation of the symplectic phases in (7.4).

---

# 9. A finite twisted-square Schur target

Equation (7.2) gives a more phase-sensitive sufficient condition.

Using

$$
W_{(p,q)}|x\rangle
=
\omega^{p(x+q/2)}|x+q\rangle,
$$

the matrix entries of \(H^2\) are

$$
\boxed{
(H^2)_{x+q,x}
=
\sum_{p\in\mathbb F_D}
d_{(p,q)}
\omega^{p(x+q/2)}.
}
\tag{9.1}
$$

Because \(H^2\) is Hermitian,

$$
\|H^2\|_\infty
\le
\max_x
\sum_q
\left|
\sum_p d_{(p,q)}
\omega^{p(x+q/2)}
\right|.
$$

Consequently, the finite inequality

$$
\boxed{
\max_x
\sum_q
\left|
\sum_p d_{(p,q)}
\omega^{p(x+q/2)}
\right|
\le
10\sum_g|c_g|^2
}
\tag{TwistedSchur10}
$$

for every Hermitian \(c\) would imply WR10.

Unlike `AbsMoment10`, this retains the internal Weyl cancellations inside each output displacement. I do not prove `TwistedSchur10` for the frozen tuple, nor produce a coefficient vector violating it.

---

# 10. A new explicit three-level physical witness

For \(c\neq0\), define

$$
H_c=\{p:(p,c)\in\Gamma\},
\qquad
h_c:=|H_c|,
$$

and

$$
\boxed{
S_c:=\sum_{p\in H_c}\omega^{pc}.
}
\tag{10.1}
$$

Take three consecutive levels

$$
x,\qquad x+c,\qquad x+2c
$$

and the normalized state

$$
\boxed{
|\psi\rangle
=
\frac12|x\rangle
+
\frac{e^{i\theta}}{\sqrt2}|x+c\rangle
+
\frac{e^{i\phi}}2|x+2c\rangle.
}
\tag{10.2}
$$

For \(q=c\),

$$
\begin{aligned}
\langle\psi|W_{(p,c)}|\psi\rangle
={}&
\frac{e^{-i\theta}}{2\sqrt2}
\omega^{p(x+c/2)}\\
&+
\frac{e^{i(\theta-\phi)}}{2\sqrt2}
\omega^{p(x+3c/2)}.
\end{aligned}
\tag{10.3}
$$

For \(q=2c\),

$$
\langle\psi|W_{(p,2c)}|\psi\rangle
=
\frac{e^{-i\phi}}4\omega^{p(x+c)}.
\tag{10.4}
$$

The only nonzero position differences of this state are

$$
\pm c,\qquad \pm2c.
$$

Choose the phases so that

$$
\phi-2\theta=\arg S_c.
$$

Then the \(q=\pm c\) contribution is

$$
\frac{h_c+|S_c|}{2},
$$

and the \(q=\pm2c\) contribution is

$$
\frac{h_{2c}}8.
$$

Thus the state (10.2) satisfies the exact identity

$$
\boxed{
\mathcal F_\Gamma(|\psi\rangle\langle\psi|)
=
\frac{h_c+|S_c|}{2}
+
\frac{h_{2c}}8.
}
\tag{ThreeLevel}
$$

This is a genuine normalized physical state, not a relaxation.

Therefore PW10 requires

$$
\boxed{
4(h_c+|S_c|)+h_{2c}\le80
\quad
\forall c\neq0.
}
\tag{10.5}
$$

## 10.1 Strict improvement from Fiber20 to Fiber19

The exponents \(pc\bmod D\), \(p\in H_c\), are distinct because \(c\neq0\).

If

$$
S_c=\sum_{p\in H_c}\omega^{pc}=0,
$$

then the \(0/1\)-coefficient polynomial

$$
f(X)=\sum_{p\in H_c}X^{pc\bmod D}
$$

vanishes at a primitive \(D\)-th root. Since \(D\) is prime, the minimal polynomial is

$$
1+X+\cdots+X^{D-1}.
$$

Because \(0<h_c<D\), \(f\) cannot be a multiple of that polynomial. Hence

$$
\boxed{
H_c\neq\varnothing
\quad\Longrightarrow\quad
S_c\neq0.
}
\tag{10.6}
$$

If \(h_c=20\), then

$$
\frac{h_c+|S_c|}{2}>10,
$$

even without the nonnegative \(h_{2c}/8\) term. Therefore

$$
\boxed{
\text{PW10 implies }|H_c|\le19
\text{ for every }c\neq0.
}
$$

More sharply, if \(h_c=19\), then PW10 requires

$$
\boxed{
4|S_c|+h_{2c}\le4.
}
\tag{10.7}
$$

No exact \(c\) violating (10.5) is identified here.

Quadratic chirps are stabilizer states and remain covered by the previously audited line bound \(N_\ell\le2\); they do not supply a new counterexample.

---

# 11. What the exact arithmetic has and has not settled

The horizontal-fiber problem is now reduced to five integer lift equations, not \(O(P)\) carries. A sufficient finite arithmetic statement is the per-carry bound (5.4). It is unproved.

Even proving all fiber conditions would not prove PW10: a general vector can simultaneously use many horizontal displacements, and WR10 couples those fibers through the Weyl phases.

The phase-blind high-moment route is ruled out quantitatively by (8.1). A successful moment proof must retain symplectic cancellation.

A concrete sufficient operator target is `TwistedSchur10`. A concrete physical disproof target is the three-level condition

$$
4(h_c+|S_c|)+h_{2c}>80.
$$

Neither target is settled for the exact frozen tuple.

The first remaining arithmetic estimate is:

$$
\boxed{
\#\{(a,b):C_a-C_b=Y+\kappa D\}\le4
\quad
\text{for all }Y,\ 
\kappa\in\{-2,-1,0,1,2\}.
}
$$

The first remaining phase-sensitive operator estimate is:

$$
\boxed{\text{TwistedSchur10}}
$$

or another uniform estimate strong enough to imply WR10 while retaining the phases in the twisted convolution.

PW10 therefore remains open. Consequently, the all-\(T\) ratio gate, \((E1_{\rm gap})\), and the full-size theorem all remain downstream and open.

---

# Audit ledger

**PROVED**

* \(m=485165196\) is the least integer exceeding \(e^{20}\).
* \(P=485165237\) is the least prime exceeding \(m\).
* \(D=941541228773064677=4P^2+1\) is prime and is the least prime exceeding \(4P^2\).
* \(\iota=2P\) satisfies \(\iota^2\equiv-1\pmod D\).
* The frozen index range is exactly \(0\le j\le P-42\).
* \(t_j=r_j+\iota j\) and

  $$
  t_j^2\equiv(r_j^2-j^2)+\iota(2jr_j)\pmod D.
  $$
* The exact bounds

  $$
  |\Delta A|\le4P^2-172P+3530,
  \qquad
  |\Delta B|\le4P^2-172P+168.
  $$
* The original carries satisfy

  $$
  |n|,|\ell|\le2P-85.
  $$
* `Carry1`, the norm identity

  $$
  \Delta A^2+\Delta B^2=D(n^2+\ell^2),
  $$

  and the parity condition \(\ell\) even.
* Once residues modulo \(2P\) are fixed, at most four \((n,\ell)\) lift branches remain.
* The second quotient normalization

  $$
  t_j^2=D(j^2+\sigma_j)+C_j.
  $$
* Every squared-difference collision belongs to exactly one of five possible global carry classes

  $$
  \kappa=-2,-1,0,1,2.
  $$
* Completing the final \(41\) indices preserves the five-carry bound.
* The completed squared map is injective.
* For each \(c\), completion adds at most \(82\) ordered representations.
* The exact twisted-convolution formula for \(H^2\).
* The exact fourth-moment and general even-moment formulas.
* The phase-blind absolute-moment sufficient criterion.
* The frozen tuple fails that sufficient criterion at the \(28\)-th moment by a factor exceeding \(2.134580466768748\).
* The finite twisted-square Schur condition is sufficient for WR10.
* The exact three-level physical-state formula

  $$
  \mathcal F_\Gamma
  =
  \frac{|H_c|+|S_c|}{2}
  +
  \frac{|H_{2c}|}{8}.
  $$
* \(S_c\neq0\) for every nonempty proper fiber.
* PW10 necessarily implies \(|H_c|\le19\).

**DISPROVED**

* Sufficiency of a phase-blind absolute zero-sum moment count with constant \(10\); it already fails at moment \(28\).
* The possibility that \(|H_c|=20\) is compatible with PW10.

**NECESSARY-ONLY**

* Fiber19.
* The sharper three-level condition

  $$
  4(|H_c|+|S_c|)+|H_{2c}|\le80.
  $$
* All stabilizer-line tests.
* All bounded-support tests not accompanied by a uniform argument.

**OPEN**

* The five per-carry bounds in (5.4).
* A uniform bound on completed or frozen squared-difference multiplicities.
* Whether some exact \(c\) violates the three-level condition.
* `TwistedSchur10`.
* WR10.
* PW10 for the exact frozen tuple.
* The finite all-\(T\) ratio gate.
* \((E1_{\rm gap})\).

**CONJECTURED**

* No claim is promoted to conjectured status.

The first new claim requiring independent verification is the five-carry normalization

$$
t_j^2=D(j^2+\sigma_j)+C_j,
\qquad
C_a-C_b-C_u+C_v\in\{-2,-1,0,1,2\}D.
$$

The first unresolved arithmetic estimate is the per-carry multiplicity bound (5.4); the first unresolved global operator estimate is `TwistedSchur10`.

[1]: https://inria.hal.science/?utm_source=chatgpt.com "Primality Tests and Prime Certificate"

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-09-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-09-local-audit.md bytes=10206 sha256=dc11e3276160a5c4673238afa51814a1f83ab30893d291b5069a4516929fb493 -->

# Round 09 independent local audit

## Capture integrity

- Conversation: `Audit quantum construction`
- Surface/model observed at send time: ordinary Chat, GPT-5.6 Sol, Pro 5/5
- Browser completion indicator: `Worked for 20m 7s`
- Captured response: 22,188 bytes / 22,188 Unicode characters
- Response SHA-256:
  `1454072c19c899e810409d1e9a40adf81103a4484b26dacd97b8ce4c522e04df`
- The artifact and output copies are byte-identical to the TextEdit export of
  the browser's exact response-copy action.
- Prompt SHA-256:
  `5c336cfbcc8d73e56d9a767ef6323239cf3918f32334e825f888faa04a273474`
- Prompt size: 6,998 bytes / 6,996 Unicode characters. The browser composer
  contained 6,995 characters, exactly the source with its single terminal
  newline removed.

## Verdict

**OPEN WITH EARLIEST GAP.** Round 09 neither proves nor disproves PW10 for
the exact frozen tuple. It makes two genuine advances that survive local
audit:

1. an exact second normalization reduces the collision carry to the five
   values \(\kappa\in\{-2,-1,0,1,2\}\);
2. an exact normalized three-level state strengthens the necessary fiber
   condition from \(|H_c|\le20\) to \(|H_c|\le19\), together with the sharper
   necessary inequality
   \[
   4\bigl(|H_c|+|S_c|\bigr)+|H_{2c}|\le80.
   \]

Neither advance closes PW10. Round 09 itself drew only the weak total bound
\(|H_c|\le20\) from five relative carry labels. A further exact interval
observation below shows that one fiber can occupy at most three absolute
lifts, so the proposed per-lift bound would instead imply \(|H_c|\le12\).
That bound remains unproved. The proposed twisted Schur inequality is
sufficient for WR10 but is also unproved and is not reduced to the carry
systems.

## Claims independently verified

### 1. Exact constants and primality certificates

Exact integer computation reproduces
\[
m=485165196,\qquad P=485165237=m+41,
\]
\[
P^2=235385307193266169,\qquad
D=941541228773064677=4P^2+1.
\]
Thus \(i=2P=970330474\) satisfies \(i^2\equiv-1\pmod D\), and the frozen
range is \(0\le j\le P-42\).

The local verifier `work/verify_round09_constants.py` independently checks:

- the rational Taylor bracket locating \(e^{20}\) between
  \(485165195\) and \(485165196\);
- a proper divisor for every integer strictly between \(m\) and \(P\);
- every modular-power and gcd condition in the displayed recursive Lucas
  certificate for \(P\) and \(D\).

The complete-factor version of the Lucas criterion used in the response is
valid: for each prime divisor of \(N\), the displayed conditions force the
order of the witness to equal \(N-1\), hence that prime divisor is at least
\(N\). The generic HAL link in the web response is not needed for, and does
not replace, this executable exact check.

### 2. Gaussian coordinates and the original carry lattice

For \(r_j=j^2\bmod P\) in \([0,P-1]\),
\[
t_j=r_j+ij,\qquad
t_j^2\equiv(r_j^2-j^2)+i(2jr_j)\pmod D
\]
is correct. With \(J=P-42\), the response's elementary bounds are exactly
\[
|\Delta A|\le4P^2-172P+3530,
\qquad
|\Delta B|\le4P^2-172P+168.
\]
The two exact divisions used to bound the carries are
\[
M_A+iM_B=(2P-85)D+(162P+3615),
\]
\[
M_B+iM_A=(2P-85)D+(6886P+253),
\]
with both remainders strictly between \(0\) and \(D\). Hence
\[
|n|,|\ell|\le2P-85.
\]
The identities
\[
\Delta A=n-i\ell,\qquad \Delta B=in+\ell,
\]
\[
\Delta A^2+\Delta B^2=D(n^2+\ell^2)
\]
and the parity of \(\ell\) are all correct. Each balanced residue modulo
\(2P\) has at most two admissible lifts in the stated interval, so four
\((n,\ell)\) branches is a valid upper bound once both residues are fixed.

### 3. The five-carry normalization

Writing
\[
jr_j=P\sigma_j+h_j,\qquad 0\le h_j<P,
\]
and
\[
C_j=4Ph_j+r_j^2-j^2-\sigma_j
\]
gives the exact integer identity
\[
t_j^2=D(j^2+\sigma_j)+C_j.
\]
The frozen bounds
\[
-P^2+83P-1721\le C_j\le5P^2-6P+1
\]
are valid. Consequently
\[
|C_a-C_b-C_u+C_v|
\le12P^2-178P+3444<3D,
\]
where the exact margin is
\[
3D-(12P^2-178P+3444)=178P-3441=86359408745.
\]
A collision therefore has a unique integer \(\kappa\) and that integer lies
in \(\{-2,-1,0,1,2\}\). This means “at most these five possible classes”; it
does not establish that every one occurs.

For a fixed reference pair, the five equations
\[
C_a-C_b=Y+\kappa D
\]
are therefore an exact finite partition of all representations. The quotient
variables \(\sigma_j\) cannot be discarded when reducing modulo \(P\).

There is a sharper occupancy consequence. Put
\[
R=(5P^2-6P+1)-(-P^2+83P-1721)
=6P^2-89P+1722.
\]
Every exact difference \(C_a-C_b\) lies in \([-R,R]\), whose length satisfies
\[
2R<3D.
\]
Four lifts of one fixed residue would span \(3D\). Hence any horizontal
fiber occupies at most three absolute lifts; the five relative labels cannot
all be populated in the same fiber.

### 4. Completion by the final 41 indices

For \(0\le j\le P-1\), \(t_j\) is strictly increasing and
\[
0\le t_j<2P^2<D/2.
\]
Since \(D\) is prime, congruent squares in this interval force equal \(t_j\),
so the completed squared map is injective. Adding the 41 deleted indices can
add at most one representation per deleted value as a first endpoint and at
most one as a second endpoint. Thus
\[
0\le r_{\rm completed}(c)-r_{\rm frozen}(c)\le82
\]
is correct. It is far above the needed constant and supplies no PW10 bound.

### 5. Twisted convolution and moments

From
\[
W_gW_h=\omega^{[g,h]/2}W_{g+h}
\]
one gets
\[
H^2=\sum_k d_kW_k,\qquad
d_k=\sum_{\substack{g\in\Gamma\\k-g\in\Gamma}}
c_gc_{k-g}\omega^{[g,k]/2}.
\]
Weyl orthogonality gives
\[
\operatorname{Tr}H^4=D\sum_k|d_k|^2,
\]
and iteration gives the response's general zero-sum formula with phase
\(\frac12\sum_{j<k}[g_j,g_k]\). The phase cannot be removed.

The absolute-moment condition \(\mathfrak A_r(c)\le10^r\) for every \(r\)
would indeed imply WR10 after taking \(2r\)-th roots and sending \(r\) to
infinity.

### 6. Exact failure of the phase-blind sufficient condition

The response's count is correct:
\[
M=|\Gamma|=m(m-1)=235385266924553220,
\]
\[
27!!=213458046676875,
\]
and the selected zero-sum words contribute
\[
27!!\prod_{j=0}^{13}\left(1-\frac{2j}{M}\right).
\]
Exact rational arithmetic confirms that this quantity divided by \(10^{14}\)
is strictly greater than \(2.134580466768748\).

What fails is **satisfaction of the sufficient condition by this tuple**,
not the logical sufficiency of the condition. The response's DISPROVED
ledger phrase “sufficiency ... fails” is therefore semantically incorrect.
No PW10 counterexample follows, because this count deliberately discarded
all Weyl phases.

### 7. Twisted Schur target

The matrix entry formula
\[
(H^2)_{x+q,x}
=\sum_p d_{(p,q)}\omega^{p(x+q/2)}
\]
is correct. Hermiticity equates maximum row and column sums, so the displayed
row-sum inequality with constant 10 would imply
\(\|H\|_\infty^2\le10\sum_g|c_g|^2\).

This is only a sufficient target. The response neither proves it nor derives
it from the five carry equations. It is a generic phase-sensitive Schur
bound, not yet a checkable arithmetic consequence of this frozen tuple.

### 8. Three-level physical witness and Fiber19

For
\[
|\psi\rangle=\tfrac12|x\rangle+
\tfrac{e^{i\theta}}{\sqrt2}|x+c\rangle+
\tfrac{e^{i\phi}}2|x+2c\rangle,
\]
direct use of
\[
W_{(p,q)}|x\rangle=\omega^{p(x+q/2)}|x+q\rangle
\]
shows that only the shifts \(\pm c,\pm2c\) contribute. Optimizing the single
relative phase yields exactly
\[
\mathcal F_\Gamma(\psi)
=\frac{|H_c|+|S_c|}{2}+\frac{|H_{2c}|}{8},
\qquad
S_c=\sum_{p\in H_c}\omega^{pc}.
\]

For \(c\ne0\), the exponents \(pc\bmod D\) are distinct. Also
\(|H_c|\le|\Gamma|=m(m-1)<D\). A nonempty proper 0/1 polynomial of degree at
most \(D-1\) cannot vanish at a primitive \(D\)-th root, because its minimal
polynomial is \(1+X+\cdots+X^{D-1}\). Hence \(S_c\ne0\) whenever \(H_c\) is
nonempty.

It follows rigorously that \(|H_c|=20\) would give
\(\mathcal F_\Gamma(\psi)>10\). Therefore PW10 implies
\[
\boxed{|H_c|\le19}
\]
and, when \(|H_c|=19\), the sharper condition
\[
4|S_c|+|H_{2c}|\le4.
\]

## Remaining gap and next target

The web response's proposed per-carry estimate
\[
\#\{(a,b):C_a-C_b=Y+\kappa D\}\le4
\]
is unproved. The interval argument above means at most three of those exact
lift equations can be populated for one fiber. Thus the proposed per-lift
bound would imply
\(h_c\le12\), comfortably passing Fiber19. It is still only a proposed
estimate, and even proving it would not settle the global PW10 inequality.

A valid next round must do at least one of the following:

- prove the per-lift bound, or another aggregate bound totaling at most 19,
  and then test the exponential-sum condition;
- exhibit an exact \(c\) violating the three-level inequality;
- connect the five carry systems to a genuinely uniform phase-sensitive
  operator estimate; or
- replace this frozen tuple if the exact arithmetic shows that PW10 fails.

Even all three-level tests passing would remain necessary-only. The global
gate remains WR10/PW10.

## Audit ledger

**PROVED**

- The exact constants and recursive primality certificates.
- The original bounded-carry lattice identities and bounds.
- The five-carry normalization and exact five-system partition.
- The completion comparison and \(82\)-representation upper increment.
- The twisted-convolution and even-moment identities.
- Failure of the phase-blind absolute-moment condition at \(r=14\).
- Sufficiency, but not truth, of the twisted Schur inequality.
- The exact three-level physical-state formula.
- The necessary consequences Fiber19 and
  \(4(|H_c|+|S_c|)+|H_{2c}|\le80\).

**DISPROVED**

- The claim that this frozen tuple satisfies the phase-blind constant-10
  absolute-moment condition.
- Compatibility of a size-20 horizontal fiber with PW10.

**NECESSARY-ONLY**

- Fiber19 and all three-level inequalities.
- Stabilizer and other bounded-support tests.

**OPEN**

- The distribution of representations among the five carry classes.
- Every aggregate horizontal-fiber bound at 19 or below.
- Existence of an exact \(c\) violating the three-level condition.
- TwistedSchur10, WR10, and PW10.
- The downstream all-\(T\) ratio, \(E1_{\rm gap}\), and full-size theorem.

**CONJECTURED**

- None.

<!-- END HISTORICAL FILE path=outputs/round-09-local-audit.md -->


# ROUND 010

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-10-prompt.md bytes=7543 sha256=4a71de73d4ac9da45a2dd3e07915c6e745a38b779cb52e0a0507f782ae299fcf -->

# Round 10 — optimize the physical witness and make the five carry systems decisive

Continue in the same conversation and the same canonically frozen finite
\(r=2\) low-\(A\) gate. Give a public, self-contained derivation and no
hidden chain-of-thought. Do not repeat the general Round 8 or Round 9
discussion.

## Independently audited boundary

Use exactly
\[
m=485165196,\qquad
P=485165237=m+41,
\]
\[
D=941541228773064677=4P^2+1,\qquad i=2P,\qquad i^2=-1\pmod D,
\]
and
\[
0\le j\le P-42,\qquad
r_j=j^2\bmod P\text{ in }[0,P-1],\qquad
t_j=2Pj+r_j.
\]
The recursive Lucas certificates for \(P,D\), every composite between
\(m\) and \(P\), and the decimal bracket for \(e^{20}\) have now been
checked independently. Do not spend the round re-proving primality.

For
\[
\Gamma=\{(t_a-t_b,t_a^2-t_b^2):a\ne b\}
\]
the open one-copy gate is
\[
\boxed{
\sup_{\rho\ {\rm pure}}\mathcal F_\Gamma(\rho)\le10,
\qquad
\mathcal F_\Gamma(\rho)
=\sum_{g\in\Gamma}|\operatorname{Tr}(W_g^*\rho)|^2.
}
\tag{PW10}
\]
Its exact Hermitian Weyl-polynomial dual is
\[
\boxed{
\left\|\sum_{g\in\Gamma}c_gW_g\right\|_\infty^2
\le10\sum_{g\in\Gamma}|c_g|^2
\quad\forall c_{-g}=\overline{c_g}.
}
\tag{WR10}
\]
This equivalence is already audited and is not itself progress.

For horizontal fibers
\[
H_c=\{p:(p,c)\in\Gamma\},\qquad
h_c=|H_c|,\qquad
S_c=\sum_{p\in H_c}\omega^{pc},
\]
Round 9 correctly proved, using a normalized physical three-level state,
\[
\mathcal F_\Gamma
=\frac{h_c+|S_c|}{2}+\frac{h_{2c}}8
\tag{R9-3L}
\]
for one fixed choice of moduli. Since \(0<h_c<D\) implies \(S_c\ne0\),
PW10 requires
\[
\boxed{h_c\le19.}
\tag{Fiber19}
\]
Thus an exact fiber of size 20, not 21, already disproves PW10.

Round 9 also established the exact second normalization
\[
jr_j=P\sigma_j+h_j,\qquad 0\le h_j<P,
\]
\[
C_j=4Ph_j+r_j^2-j^2-\sigma_j,
\qquad
t_j^2=D(j^2+\sigma_j)+C_j,
\tag{C}
\]
with
\[
-P^2+83P-1721\le C_j\le5P^2-6P+1.
\]
Every collision therefore belongs to a unique one of at most five carry
classes:
\[
C_a-C_b-C_u+C_v=\kappa D,\qquad
\kappa\in\{-2,-1,0,1,2\}.
\tag{FiveCarry}
\]
This reduction is correct. But the proposed per-carry estimate
\[
\#\{(a,b):C_a-C_b=Y+\kappa D\}\le4
\tag{PC4}
\]
was not proved. Even if all five instances of PC4 held, their sum would give
only \(h_c\le20\), which is already too weak after Fiber19. Do not present
PC4 as a closing condition.

The exact twisted convolution
\[
d_k=\sum_{\substack{g\in\Gamma\\k-g\in\Gamma}}
c_gc_{k-g}\omega^{[g,k]/2}
\]
and the resulting row-sum condition called \(\mathrm{TwistedSchur10}\) are
also algebraically correct. The latter is only an unproved sufficient
condition and has not been derived from the five carry systems.

Finally, the phase-blind absolute-moment condition was shown to be false for
this tuple at \(r=14\). What failed was satisfaction of that sufficient
condition, not its logical sufficiency. Any moment argument must retain the
symplectic phases.

## New local calculation to audit: optimize all three moduli

For nonnegative \(u,v,w\) with \(u+v+w=1\), consider
\[
|\psi\rangle
=\sqrt u\,|x\rangle
+e^{i\theta}\sqrt v\,|x+c\rangle
+e^{i\phi}\sqrt w\,|x+2c\rangle.
\]
Direct expansion appears to give, after phase optimization,
\[
2h_cv(u+w)+4v\sqrt{uw}|S_c|+2h_{2c}uw.
\tag{3L-general}
\]
For fixed \(s=u+w\), nonnegativity should force the optimum at
\(u=w=s/2\), \(v=1-s\). Put
\[
A_c=h_c+|S_c|,\qquad B_c=h_{2c}.
\]
Then the exact optimum over this full arithmetic-progression three-level
family should be
\[
\boxed{
M_3(c)=\max_{0\le s\le1}
\left(2A_cs(1-s)+\frac{B_c}{2}s^2\right)
=
\begin{cases}
\dfrac{2A_c^2}{4A_c-B_c},&B_c\le2A_c,\\[6pt]
\dfrac{B_c}{2},&B_c\ge2A_c.
\end{cases}
}
\tag{Opt3L}
\]
The Round 9 state is just \(s=1/2\). In the interior branch, PW10 would
require
\[
\boxed{A_c^2-20A_c+5B_c\le0.}
\tag{Opt3L-necessary}
\]
In particular, for \(h_c=19\) and \(\delta=|S_c|>0\),
\[
h_{2c}\le\frac{(19+\delta)(1-\delta)}5.
\tag{19-edge}
\]
Audit every factor, phase, endpoint, and branch before using this.

## Exact tasks

1. Give one verdict for PW10 on this exact tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**. A failed sufficient
   relaxation is not a PW10 counterexample.

2. Prove or correct (3L-general), (Opt3L), (Opt3L-necessary), and (19-edge).
   Treat \(S_c=0\), endpoint optima, and all phase conventions explicitly.
   State the strongest exact necessary condition obtained for every pair
   \((h_c,h_{2c})\), not only for \(h_c=19\).

3. Make the five-carry arithmetic pay for a constant bound. For the exact
   \(P,D\), do one of the following:

   - exhibit an exact \(c\) and 20 distinct ordered pairs
     \((a,b)\) with \(t_a^2-t_b^2=c\pmod D\);
   - exhibit an exact \(c\), its fiber data, and a physical state violating
     Opt3L even with \(h_c\le19\);
   - prove the aggregate bound \(h_c\le19\) for every \(c\ne0\), with all
     five carry classes and degenerate cases accounted for; or
   - reduce each carry class to a bounded-degree equation or other explicit
     certificate whose total solution count is genuinely capable of being
     at most 19. State the exact remaining estimate and why it is stronger
     than PC4 summed over five classes.

   Congruences modulo \(P\) are not enough unless the quotient variables and
   integer lifts are recovered. A generic Bézout statement is not enough
   unless common components, singular cases, and the frozen interval are
   handled. Do not enumerate \(m^2\) pairs or substitute a heuristic.

4. Determine whether PC4 is even structurally justified. Either prove it for
   this exact tuple, refute it for this exact tuple with an exact certificate,
   or label it merely proposed. Do not infer a theorem at this enormous
   \(P\) from small-prime experiments.

5. Quantify the exponential-sum part rather than using only \(S_c\ne0\).
   Look for an exact lower bound strong enough to violate Opt3L in a
   high-multiplicity fiber, or an upper-bound mechanism that helps all
   three-level tests pass. Clearly distinguish a universal root-of-unity
   bound from structure specific to \(H_c\).

6. On the global operator side, do not simply restate TwistedSchur10.
   Either:

   - derive it, or a different constant-10 bound, from explicit
     intersection/carry data of \(\Gamma\);
   - give an exact Hermitian coefficient vector that falsifies
     TwistedSchur10 and explain whether it also violates WR10; or
   - derive a strictly smaller phase-sensitive finite condition with a
     proved containment implication.

   A violation of a Schur or moment upper bound alone only kills that proof
   route. A PW10 disproof requires an explicit physical state, or equivalently
   an actual WR10-violating Weyl polynomial with its extremal eigenvector
   argument carried through.

7. If useful, derive the exact optimized formula for arbitrary three-point
   supports, separating the arithmetic-progression case (two transitions
   share a displacement) from the three-distinct-difference case. Any
   resulting violation must specify actual frozen indices or fibers.

8. Do not discuss the all-\(T\) ratio unless PW10 is first settled for this
   same tuple. The all-copy gate remains separate and downstream.

9. End with a plain audit ledger separating **PROVED**, **DISPROVED**,
   **NECESSARY-ONLY**, **OPEN**, and **CONJECTURED**. State the first claim
   that requires independent verification.

The finite \(r=2\) gate remains OPEN unless the full uniform inequality is
proved or an exact physical violator is exhibited.

<!-- END HISTORICAL FILE path=work/round-10-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-10-response.md bytes=19496 sha256=5028fa0231b23a97a973cfc23a648b22f31207453678963f876821bcf6bef0a5 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The optimized three-level calculation is correct. It yields a strictly stronger family of necessary conditions than Round 9.

The five-carry arithmetic also admits an important refinement:

$$
\boxed{\text{A single fixed horizontal fiber can occupy at most three exact carry lifts, not five.}}
$$

The five values \(\kappa\in\{-2,-1,0,1,2\}\) remain correct when comparing arbitrary representations relative to a chosen one, but the total interval available to \(C_a-C_b\) has width \(<3D\). Consequently, if the proposed per-lift bound PC4 were true, it would imply

$$
h_c\le 3\cdot4=12,
$$

not merely \(20\). PC4 would therefore be more than sufficient for the fiber test. It is, however, still unproved for this exact tuple.

No exact fiber with \(20\) representations, no optimized three-level violation, and no global WR10 violation is obtained below.

---

# 1. Optimizing all three moduli

Let

$$
|\psi\rangle
=
\sqrt u\,|x\rangle
+
e^{i\theta}\sqrt v\,|x+c\rangle
+
e^{i\phi}\sqrt w\,|x+2c\rangle,
$$

where

$$
u,v,w\ge0,\qquad u+v+w=1,\qquad c\ne0.
$$

Recall

$$
W_{(p,q)}|y\rangle
=
\omega^{p(y+q/2)}|y+q\rangle.
$$

For displacement \(q=c\),

$$
\begin{aligned}
\langle\psi|W_{(p,c)}|\psi\rangle
={}&
e^{-i\theta}\sqrt{uv}\,
\omega^{p(x+c/2)}\\
&+
e^{i(\theta-\phi)}\sqrt{vw}\,
\omega^{p(x+3c/2)}.
\end{aligned}
$$

After extracting the first common phase,

$$
\begin{aligned}
\left|
\langle\psi|W_{(p,c)}|\psi\rangle
\right|^2
={}&
uv+vw\\
&+
2v\sqrt{uw}\,
\operatorname{Re}\!\left(
e^{i(2\theta-\phi)}\omega^{pc}
\right).
\end{aligned}
$$

Summing over \(p\in H_c\),

$$
\sum_{p\in H_c}
\left|
\langle\psi|W_{(p,c)}|\psi\rangle
\right|^2
=
h_cv(u+w)
+
2v\sqrt{uw}\,
\operatorname{Re}\!\left(
e^{i(2\theta-\phi)}S_c
\right).
$$

The contribution from displacement \(-c\) is identical. For \(q=2c\), only the transition \(x\to x+2c\) appears, giving \(uw\) per Weyl label; \(q=-2c\) gives the same contribution. Therefore

$$
\boxed{
\mathcal F_\Gamma(\psi)
=
2h_cv(u+w)
+
4v\sqrt{uw}\,
\operatorname{Re}\!\left(
e^{i(2\theta-\phi)}S_c
\right)
+
2h_{2c}uw.
}
\tag{1.1}
$$

Writing

$$
S_c=|S_c|e^{i\gamma},
$$

the phase is optimized by choosing

$$
2\theta-\phi=-\gamma
\qquad\Longleftrightarrow\qquad
\phi-2\theta=\gamma.
$$

Thus

$$
\boxed{
\max_{\theta,\phi}\mathcal F_\Gamma(\psi)
=
2h_cv(u+w)
+
4v\sqrt{uw}|S_c|
+
2h_{2c}uw.
}
\tag{3L-general}
$$

If \(S_c=0\), the phase is immaterial. For the actual frozen tuple,

$$
0<h_c<D\quad\Longrightarrow\quad S_c\ne0,
$$

so \(S_c=0\) occurs only when \(h_c=0\).

---

## 1.1 Optimization over \(u,v,w\)

Set

$$
s=u+w,\qquad v=1-s.
$$

For fixed \(s\),

$$
uw\le\frac{s^2}{4},
\qquad
\sqrt{uw}\le\frac s2,
$$

and both coefficients multiplying these terms in (3L-general) are nonnegative. Hence a maximizer exists with

$$
u=w=\frac s2.
$$

Define

$$
A_c=h_c+|S_c|,
\qquad
B_c=h_{2c}.
$$

Then the exact optimization becomes

$$
f_c(s)
=
2A_cs(1-s)+\frac{B_c}{2}s^2,
\qquad 0\le s\le1.
\tag{1.2}
$$

Its derivative is

$$
f_c'(s)=2A_c+(B_c-4A_c)s.
$$

### Case \(A_c=0\)

Then necessarily \(h_c=0=S_c\), and

$$
M_3(c)=\max_s \frac{B_c}{2}s^2=\frac{B_c}{2}.
$$

### Case \(A_c>0\) and \(B_c\le2A_c\)

The critical point

$$
s_*=\frac{2A_c}{4A_c-B_c}
$$

belongs to \((0,1]\), and

$$
M_3(c)
=
\frac{2A_c^2}{4A_c-B_c}.
$$

At \(B_c=2A_c\), one has \(s_*=1\).

### Case \(B_c\ge2A_c\)

The function is maximized at \(s=1\), giving

$$
M_3(c)=\frac{B_c}{2}.
$$

Consequently,

$$
\boxed{
M_3(c)=
\begin{cases}
\dfrac{B_c}{2},
& A_c=0,\\[6pt]
\dfrac{2A_c^2}{4A_c-B_c},
& A_c>0,\ B_c\le2A_c,\\[9pt]
\dfrac{B_c}{2},
& B_c\ge2A_c.
\end{cases}
}
\tag{Opt3L}
$$

At \(B_c=2A_c\), the two displayed values agree.

---

# 2. The exact necessary condition from optimized three-level states

PW10 requires

$$
M_3(c)\le10
\qquad\text{for every }c\ne0.
$$

Thus the strongest exact condition supplied by this family is:

$$
\boxed{
\begin{cases}
B_c\le20,
& A_c=0\text{ or }B_c\ge2A_c,\\[3pt]
A_c^2-20A_c+5B_c\le0,
& A_c>0\text{ and }B_c\le2A_c.
\end{cases}
}
\tag{2.1}
$$

In the interior branch, this is equivalent to

$$
10-\sqrt{100-5B_c}
\le A_c
\le
10+\sqrt{100-5B_c},
$$

and in particular requires \(B_c\le20\).

This proves the proposed condition

$$
\boxed{A_c^2-20A_c+5B_c\le0}
\tag{Opt3L-necessary}
$$

under its correct branch hypothesis \(B_c\le2A_c\).

---

## 2.1 The \(h_c=19\) edge

Let

$$
h_c=19,\qquad \delta=|S_c|>0.
$$

Then

$$
A_c=19+\delta.
$$

The endpoint branch \(B_c\ge2A_c\) is impossible under \(B_c\le20\), because \(2A_c>38\). Hence the interior inequality applies:

$$
(19+\delta)^2-20(19+\delta)+5B_c\le0.
$$

Therefore

$$
\boxed{
B_c=h_{2c}
\le
\frac{(19+\delta)(1-\delta)}5.
}
\tag{19-edge}
$$

In particular:

* \(\delta>1\) is an immediate physical violation;
* if PW10 holds, then \(0<\delta\le1\);
* since \(B_c\) is an integer,

  $$
  \boxed{h_c=19\Longrightarrow h_{2c}\le3.}
  $$

More precisely,

$$
\delta\le\sqrt{100-5B_c}-9.
$$

---

## 2.2 Necessary integer bounds depending only on \(h_c\)

Eliminating the unknown positive number \(\delta=|S_c|\), but retaining its strict positivity when \(h_c>0\), gives:

$$
\begin{array}{c|c}
h_c & \text{necessary upper bound on }h_{2c}\\ \hline
0,\ldots,9 & 20\\
10,11,12 & 19\\
13 & 18\\
14 & 16\\
15 & 14\\
16 & 12\\
17 & 10\\
18 & 7\\
19 & 3.
\end{array}
\tag{2.2}
$$

For example, at \(h_c=15\),

$$
\frac{h_c(20-h_c)}5=15,
$$

but the actual \(A_c\) is strictly larger than \(15\), so the integer bound improves to \(h_{2c}\le14\).

Thus Fiber19 is only the first member of a much stronger doubling-orbit constraint.

---

# 3. Quantitative bounds on \(S_c\)

Let \(E\subset\mathbb F_D\) be the set

$$
E=\{pc:p\in H_c\},
\qquad |E|=h_c.
$$

Because \(c\ne0\), multiplication by \(c\) is injective, so the exponents in

$$
S_c=\sum_{e\in E}\omega^e
$$

are distinct.

## 3.1 Universal nonzero lower bound

For \(0<h_c<D\), \(S_c\) is a nonzero algebraic integer in
\(\mathbb Q(\omega)\). Its field norm is a nonzero integer:

$$
1
\le
\left|
\prod_{k=1}^{D-1}
\sum_{e\in E}\omega^{ke}
\right|.
$$

Every conjugate has modulus at most \(h_c\). Isolating the original embedding gives

$$
\boxed{
|S_c|\ge h_c^{-(D-2)}.
}
\tag{3.1}
$$

This proves strict positivity, but for the present value of \(D\) it is far too small to improve the integer bounds in (2.2).

## 3.2 Universal upper bound

For any \(h\) distinct \(D\)-th roots of unity, the magnitude of their sum is maximized by \(h\) consecutive roots. Hence

$$
\boxed{
|S_c|
\le
\frac{\sin(\pi h_c/D)}{\sin(\pi/D)}
<h_c
\qquad(1<h_c<D).
}
\tag{3.2}
$$

Indeed, after rotating so that the sum points along the positive real axis, its magnitude is the sum of the projections of the selected roots. The \(h\) largest projections are attained by \(h\) consecutive roots nearest that axis, whose geometric-series sum has the displayed magnitude.

For \(h_c\le19\) and the present enormous \(D\), this upper bound is extremely close to \(h_c\), so it does not prove that the optimized three-level tests pass.

No stronger structure-specific lower or upper bound for the actual sets \(H_c\) is proved here.

---

# 4. A fixed fiber occupies at most three exact lifts

Retain the audited bounds

$$
L:=-P^2+83P-1721\le C_j
$$

and

$$
C_j\le U:=5P^2-6P+1.
$$

Put

$$
R:=U-L=6P^2-89P+1722.
$$

For the exact value of \(P\),

$$
\boxed{
R=1412311799979892643.
}
$$

Every pair difference lies in

$$
-R\le C_a-C_b\le R.
$$

The width of this interval is

$$
2R
=
2824623599959785286.
$$

On the other hand,

$$
3D
=
2824623686319194031,
$$

so

$$
\boxed{
3D-2R=86359408745>0.
}
\tag{4.1}
$$

Fix \(c\ne0\) and choose its balanced representative

$$
\bar c\in\left[-\frac{D-1}{2},\frac{D-1}{2}\right].
$$

Every representation of the fiber satisfies

$$
C_a-C_b=\bar c+kD
$$

for an integer \(k\) such that

$$
-R\le\bar c+kD\le R.
$$

Distinct allowed values are separated by \(D\). Since the containing interval has width strictly less than \(3D\), there can be at most three of them:

$$
\boxed{
K(c):=
\{k\in\mathbb Z:-R\le\bar c+kD\le R\}
\quad\text{satisfies}\quad
|K(c)|\le3.
}
\tag{4.2}
$$

Consequently,

$$
\boxed{
h_c
=
\sum_{k\in K(c)}
\nu(\bar c+kD),
}
\tag{4.3}
$$

where

$$
\nu(N)
=
\#\{(a,b):C_a-C_b=N\}.
$$

This does not contradict FiveCarry. The five values
\(\kappa=-2,-1,0,1,2\) are the possible relative differences between two lifts after one representation is selected. A single fiber cannot realize all five simultaneously.

Therefore:

$$
\boxed{
\text{If PC4 were true, then }h_c\le12\text{ for every }c\ne0.
}
\tag{4.4}
$$

PC4 would close the horizontal-fiber problem decisively. It remains unproved.

---

# 5. An exact non-\(m^2\) certificate for the per-lift problem

The fixed-lift count can be encoded without enumerating all ordered pairs.

First note that all \(C_j\) are distinct.

Indeed,

$$
t_{j+1}-t_j
=
2P+r_{j+1}-r_j
\ge P+1>0,
$$

so the \(t_j\)'s are strictly increasing. Moreover,

$$
0\le t_j<2P^2=\frac{D-1}{2}.
$$

If \(C_j=C_k\), then

$$
t_j^2\equiv t_k^2\pmod D.
$$

As \(D\) is prime,

$$
t_j\equiv\pm t_k\pmod D.
$$

The minus case is impossible because \(t_j+t_k<D\), and the plus case gives \(j=k\).

Define the squarefree integer polynomial

$$
\boxed{
F(X)=\prod_{j=0}^{P-42}(X-C_j)\in\mathbb Z[X].
}
\tag{5.1}
$$

For every nonzero integer \(N\),

$$
\boxed{
\nu(N)
=
\deg\gcd_{\mathbb Q[X]}
\bigl(F(X),F(X-N)\bigr).
}
\tag{5.2}
$$

A common root \(X=C_a\) is exactly the condition

$$
C_a-N=C_b.
$$

---

## 5.1 A uniform certificate capable of proving \(h_c\le18\)

Let

$$
\operatorname{psc}_r(Y),
\qquad r=0,\ldots,6,
$$

be the principal subresultant coefficients, with respect to \(X\), of

$$
F(X)
\quad\text{and}\quad
F(X-Y).
$$

For a fixed \(N\ne0\),

$$
\nu(N)\ge7
$$

if and only if

$$
\operatorname{psc}_0(N)=\cdots=\operatorname{psc}_6(N)=0.
\tag{5.3}
$$

Thus the following exact polynomial certificate would prove

$$
\nu(N)\le6
\quad\text{for every }N\ne0:
$$

find \(A_0(Y),\ldots,A_6(Y)\in\mathbb Z[Y]\), an integer \(M\ne0\), and \(L\ge0\) such that

$$
\boxed{
\sum_{r=0}^6
A_r(Y)\operatorname{psc}_r(Y)
=
M Y^L.
}
\tag{5.4}
$$

The factor \(Y^L\) is necessary because \(Y=0\) gives
\(F(X-Y)=F(X)\), so all low subresultants vanish there. At every nonzero integer \(N\), the right side of (5.4) is nonzero, proving that not all seven subresultants vanish.

Combining (5.4) with the three-lift lemma gives

$$
\boxed{
h_c\le3\cdot6=18.
}
$$

This is an exact algebraic certificate capable of proving the required constant bound without enumerating \(m^2\) pairs.

No such Bézout/subresultant certificate is produced in this answer. Its existence is the first precise unresolved arithmetic estimate in this route.

For PC4, the corresponding certificate would use the first five principal subresultants. Its status for the exact frozen tuple is likewise unresolved.

---

# 6. Status of PC4

PC4 is not justified merely by:

* the five possible relative carries;
* injectivity of \(j\mapsto C_j\);
* the size of the interval containing the \(C_j\)'s;
* the congruences modulo \(P\).

Those facts control possible lifts but not the number of representations within one lift.

Accordingly,

$$
\boxed{\text{PC4 is presently only a proposed estimate for this tuple.}}
$$

It has neither been proved nor refuted by an exact certificate for the displayed \(P,D\).

The fixed-fiber three-lift refinement changes its logical significance:

$$
\text{PC4}\Longrightarrow h_c\le12,
$$

but does not supply its proof.

---

# 7. Arbitrary three-point supports

The arithmetic-progression family is the only three-point configuration in which two distinct transitions share the same displacement and can interfere through an exponential sum.

Let \(x_0,x_1,x_2\) be three distinct points which are not an arithmetic progression, and define

$$
q_{01}=x_1-x_0,\qquad
q_{12}=x_2-x_1,\qquad
q_{02}=x_2-x_0.
$$

Up to signs, these three displacements are distinct.

For a state with probabilities \(u,v,w\), the exact objective is then

$$
\boxed{
\mathcal F_\Gamma
=
2\left(
h_{q_{01}}uv+
h_{q_{12}}vw+
h_{q_{02}}uw
\right).
}
\tag{7.1}
$$

There is no phase dependence.

Put

$$
A=h_{q_{01}},\qquad
B=h_{q_{12}},\qquad
C=h_{q_{02}}.
$$

If \(A,B,C\) satisfy the strict triangle inequalities, define

$$
\Delta
=
2(AB+AC+BC)-A^2-B^2-C^2.
$$

Then the interior maximizer is

$$
u=\frac{B(A-B+C)}{\Delta},
$$

$$
v=\frac{C(A+B-C)}{\Delta},
$$

$$
w=\frac{A(-A+B+C)}{\Delta},
$$

and

$$
\boxed{
M_{\rm nonAP}(A,B,C)
=
\frac{2ABC}{\Delta}.
}
\tag{7.2}
$$

If one triangle inequality fails, the maximum lies on an edge and is

$$
\boxed{
M_{\rm nonAP}(A,B,C)
=
\frac12\max\{A,B,C\}.
}
\tag{7.3}
$$

At equality in a triangle inequality, the two expressions agree.

Thus PW10 also requires

$$
M_{\rm nonAP}
\left(
h_c,h_d,h_{c+d}
\right)
\le10
\tag{7.4}
$$

for every non-arithmetic-progression triple.

A simple consequence comes from \(u=v=w=1/3\):

$$
\boxed{
h_c+h_d+h_{c+d}\le45
}
\tag{7.5}
$$

whenever the three displacements are distinct up to sign.

In particular, three such fibers of size at least \(16\) would already give an exact physical violation, even though each individual fiber satisfies Fiber19.

No such frozen triple is identified here.

---

# 8. A strictly weaker phase-sensitive replacement for TwistedSchur10

Let

$$
H=\sum_{g\in\Gamma}c_gW_g=H^*
$$

and retain the exact twisted-convolution coefficients

$$
d_k
=
\sum_{\substack{g\in\Gamma\\k-g\in\Gamma}}
c_gc_{k-g}\omega^{[g,k]/2}.
$$

For \(k=(p,q)\), define

$$
R_q(x)
=
\sum_{p\in\mathbb F_D}
d_{(p,q)}\omega^{p(x+q/2)}.
\tag{8.1}
$$

Then

$$
(H^2)_{x+q,x}=R_q(x).
$$

Define the nonnegative matrix \(\mathcal M_c\) on \(\mathbb F_D\) by

$$
\boxed{
(\mathcal M_c)_{y,x}
=
\left|R_{y-x}(x)\right|.
}
\tag{8.2}
$$

Because \(H^2\) is Hermitian,

$$
(\mathcal M_c)_{y,x}=(\mathcal M_c)_{x,y}.
$$

For every unit vector \(f\),

$$
\begin{aligned}
\langle f,H^2f\rangle
&\le
\sum_{x,y}
|f_y|(\mathcal M_c)_{y,x}|f_x|\\
&\le
\rho(\mathcal M_c),
\end{aligned}
$$

where \(\rho\) denotes the largest eigenvalue of the real symmetric nonnegative matrix. Hence

$$
\boxed{
\|H\|_\infty^2
\le
\rho(\mathcal M_c).
}
\tag{8.3}
$$

It follows that the finite condition

$$
\boxed{
\rho(\mathcal M_c)
\le
10\sum_{g\in\Gamma}|c_g|^2
\quad
\text{for every Hermitian }c
}
\tag{Perron-Schur10}
$$

would imply WR10.

---

## 8.1 Weighted form

A directly checkable sufficient condition for a fixed \(c\) is the existence of positive weights

$$
w_x>0
$$

such that, for every \(y\),

$$
\boxed{
\sum_{q\in\mathbb F_D}
|R_q(y-q)|\,w_{y-q}
\le
10\|c\|_2^2\,w_y.
}
\tag{8.4}
$$

Indeed,

$$
\mathcal M_cw\le10\|c\|_2^2w
$$

implies

$$
\rho(\mathcal M_c)\le10\|c\|_2^2.
$$

The unweighted choice \(w_x=1\) is exactly TwistedSchur10. Thus Perron-Schur10 is strictly less restrictive.

For example, the nonnegative symmetric matrix

$$
\begin{pmatrix}
9&2\\
2&1
\end{pmatrix}
$$

has maximum row sum \(11\), while its spectral radius is

$$
5+2\sqrt5<10.
$$

So weighted Schur control can succeed where the unweighted row-sum test fails.

This is a genuinely smaller phase-sensitive finite sufficient condition. It retains all cancellations inside the coefficients \(d_k\).

For the frozen tuple,

$$
d_k
=
\sum_{g\in\Gamma\cap(k-\Gamma)}
c_gc_{k-g}\omega^{[g,k]/2}.
$$

Thus checking Perron-Schur10 requires twisted two-dimensional intersection data

$$
\Gamma\cap(k-\Gamma),
$$

not merely the horizontal-fiber counts \(h_c\). The current five-carry analysis does not control these intersections uniformly. No proof or exact counterexample to Perron-Schur10 is obtained here.

A failure of Perron-Schur10 would only defeat this sufficient route; it would not by itself disprove WR10.

---

# 9. Exact remaining gaps

The bounded-support physical tests now give the following hierarchy:

1. Two-level states require \(h_c\le20\).
2. Optimized arithmetic-progression three-level states strengthen this to Fiber19 and the full condition (2.1).
3. Non-arithmetic-progression three-level states impose the coupled condition (7.4), including

   $$
   h_c+h_d+h_{c+d}\le45.
   $$
4. A single fiber has at most three exact \(C\)-lifts.
5. A uniform per-lift bound \(\nu(N)\le6\) would prove \(h_c\le18\), but its subresultant certificate remains unavailable.
6. Even complete control of all horizontal fibers would not establish PW10, because general states couple many displacements.

The first unresolved arithmetic assertion is the saturated subresultant condition (5.4), or any comparable proof of a uniform per-lift constant.

The first unresolved global operator assertion is Perron-Schur10—or some different phase-sensitive estimate strong enough to imply WR10. Current carry information does not yet control the twisted intersections appearing in \(H^2\).

Therefore no conclusion about the downstream all-\(T\) ratio is warranted.

---

# Audit ledger

**PROVED**

* The full three-modulus formula

  $$
  2h_cv(u+w)+4v\sqrt{uw}|S_c|+2h_{2c}uw.
  $$
* For fixed \(u+w\), a maximizer exists with \(u=w\).
* The exact optimized formula Opt3L, including the endpoint \(B_c=2A_c\).
* The exact branchwise PW10 necessary condition (2.1).
* The formula

  $$
  h_{2c}\le\frac{(19+|S_c|)(1-|S_c|)}5
  $$

  when \(h_c=19\).
* The integer doubling bounds listed in (2.2).
* The universal algebraic lower bound

  $$
  |S_c|\ge h_c^{-(D-2)}.
  $$
* The universal consecutive-root upper bound (3.2).
* A single fixed fiber occupies at most three exact \(C_a-C_b\) lifts.
* Therefore PC4, if true, would imply \(h_c\le12\).
* The \(C_j\)'s are pairwise distinct.
* The exact identity

  $$
  \nu(N)=\deg\gcd(F(X),F(X-N)).
  $$
* The saturated subresultant/Bézout condition (5.4) would imply \(\nu(N)\le6\) for all \(N\ne0\), and hence \(h_c\le18\).
* The exact optimized formula for non-arithmetic-progression three-point states.
* The necessary condition

  $$
  h_c+h_d+h_{c+d}\le45
  $$

  for three distinct displacement classes.
* The Perron-Schur10 condition implies WR10.
* Weighted Perron-Schur10 is strictly weaker than the previously proposed unweighted TwistedSchur10.

**DISPROVED**

* The fixed-fiber interpretation that all five relative carry classes can contribute independently to one \(h_c\). At most three exact lifts can occur.
* Consequently, the statement that PC4 would yield only \(h_c\le20\) is false; it would yield \(h_c\le12\).

**NECESSARY-ONLY**

* Fiber19.
* The optimized branchwise condition (2.1).
* The doubling table (2.2).
* The non-arithmetic-progression three-point conditions (7.4)–(7.5).
* All two-level and three-level physical witness tests.
* Any bound obtained solely from horizontal fibers.

**OPEN**

* PC4 for the exact frozen tuple.
* The weaker uniform per-lift estimate \(\nu(N)\le6\).
* The saturated subresultant certificate (5.4).
* Whether an exact \(c\) violates Opt3L.
* Whether an exact non-arithmetic-progression triple violates (7.4).
* Uniform control of the twisted intersections

  $$
  \Gamma\cap(k-\Gamma).
  $$
* Perron-Schur10 for all Hermitian coefficient vectors.
* WR10.
* PW10.

**CONJECTURED**

* No statement is promoted to conjectured status.
* PC4 remains merely proposed.

The first new claim requiring independent verification is the fixed-fiber three-lift lemma (4.2). The first unresolved arithmetic certificate is (5.4), and the first unresolved global phase-sensitive estimate is Perron-Schur10.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-10-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-10-local-audit.md bytes=10808 sha256=fbe53226b5014219a1e08b7c9ea27a4520d43b1be9068d1c6cb03362260b740d -->

# Round 10 independent local audit

## Capture integrity

- Conversation: `Audit quantum construction`
- Surface/model observed at send time: ordinary Chat, GPT-5.6 Sol, Pro 5/5
- Browser completion indicator: `Worked for 19m 4s`
- Captured response: 19,496 bytes / 19,490 Unicode characters
- Response SHA-256:
  `5028fa0231b23a97a973cfc23a648b22f31207453678963f876821bcf6bef0a5`
- The artifact and output copies are byte-identical to the TextEdit export of
  the browser's exact response-copy action.
- Prompt SHA-256:
  `4a71de73d4ac9da45a2dd3e07915c6e745a38b779cb52e0a0507f782ae299fcf`
- Prompt size: 7,543 bytes / 7,540 Unicode characters. The browser composer
  contained 7,539 characters, exactly the source with its single terminal
  newline removed.

## Verdict

**OPEN WITH EARLIEST GAP.** Round 10 neither proves nor disproves PW10 for
the exact frozen tuple. Its optimized three-point formulas, the three-lift
lemma, and the Perron domination inequality survive independent checking.
They are useful exact reductions and witness tests, but none supplies the
missing uniform arithmetic or operator bound.

The proposed subresultant expression is a valid *schema for a possible
certificate*, not a produced certificate. It starts from a polynomial of
degree
\[
m=485{,}165{,}196
\]
and leaves the required Bezout identity entirely open. It therefore avoids
writing down all \(m^2\) ordered pairs only formally; it is not yet a small or
tractable bounded subproblem and cannot be counted as evidence for
\(\nu(N)\le6\).

Likewise, Perron-Schur10 is strictly weaker than unweighted row-sum control
for a fixed coefficient vector, but it still quantifies over every Hermitian
coefficient vector and requires the spectral radius of a \(D\)-by-\(D\)
matrix. No frozen-tuple estimate for that matrix is supplied.

## Claims independently verified

### 1. Full optimization of the arithmetic-progression three-level state

For probabilities \(u,v,w\) on \(x,x+c,x+2c\), direct expansion gives
\[
2h_cv(u+w)+4v\sqrt{uw}\,|S_c|+2h_{2c}uw
\]
after phase optimization. At fixed \(s=u+w\), the coefficients of both
\(\sqrt{uw}\) and \(uw\) are nonnegative, so an optimum has
\(u=w=s/2\). With
\[
A=h_c+|S_c|,\qquad B=h_{2c},
\]
the exact remaining maximum is
\[
M_3(c)=\max_{0\le s\le1}
\left(2As(1-s)+\frac B2s^2\right)
=
\begin{cases}
B/2,&A=0,\\[2mm]
2A^2/(4A-B),&A>0,\ B\le2A,\\[2mm]
B/2,&B\ge2A.
\end{cases}
\]
The formulas agree at \(B=2A\). The branchwise necessary condition for
PW10 is therefore exactly the one stated in the response:
\[
B\le20
\quad\text{on the endpoint branch},
\]
and
\[
A^2-20A+5B\le0
\quad\text{on the interior branch}.
\]

The local script `work/verify_round10_claims.py` checks the branch formula
over an exact rational grid and reproduces the integer table
\[
\begin{array}{c|cccccccccccccccccccc}
h_c&0&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17&18&19\\ \hline
\max h_{2c}&20&20&20&20&20&20&20&20&20&20&19&19&19&18&16&14&12&10&7&3.
\end{array}
\]
The strict improvements at integral thresholds, such as \(h_c=15\), use
the already proved fact \(|S_c|>0\) for a nonempty proper fiber.

These are necessary conditions from a restricted family of physical states;
they do not imply PW10.

### 2. Bounds for the exponential sum

For \(0<h_c<D\), the sum
\[
S_c=\sum_{e\in E}\omega^e
\]
is a nonzero algebraic integer. Its full cyclotomic norm is a nonzero
integer, while every other conjugate has modulus at most \(h_c\). Hence
\[
|S_c|\ge h_c^{-(D-2)}.
\]
This is correct but quantitatively useless here.

The consecutive-root extremal bound
\[
|S_c|\le\frac{\sin(\pi h_c/D)}{\sin(\pi/D)}<h_c,
\qquad 1<h_c<D,
\]
is also correct. Rotating toward the sum and selecting the largest
projections reduces the extremizer to a consecutive arc. At the present
enormous \(D\), this upper bound is too close to \(h_c\) to certify any of
the optimized three-level inequalities.

### 3. Three absolute lifts per fixed fiber

With
\[
L=-P^2+83P-1721,\qquad U=5P^2-6P+1,
\]
exact arithmetic gives
\[
R=U-L=6P^2-89P+1722
=1{,}412{,}311{,}799{,}979{,}892{,}643.
\]
Therefore
\[
2R=2{,}824{,}623{,}599{,}959{,}785{,}286,
\]
while
\[
3D=2{,}824{,}623{,}686{,}319{,}194{,}031,
\]
with exact positive margin
\[
3D-2R=86{,}359{,}408{,}745.
\]
Four integers in one residue class modulo \(D\) would span at least \(3D\).
Thus a fixed residue can contribute at most three exact values in
\([-R,R]\), and
\[
h_c=\sum_{k\in K(c)}\nu(\bar c+kD),\qquad |K(c)|\le3.
\]
Consequently PC4, if proved, would give \(h_c\le12\).

This sharpens the earlier five-relative-carry upper bound. It does not
invalidate the implication PC4 \(\Rightarrow h_c\le20\), which remains a
true but non-sharp implication. The response's `DISPROVED` label should
therefore be read as correcting the word “only” or the simultaneous-occupancy
interpretation, not as refuting FiveCarry itself.

### 4. Distinctness of the \(C_j\)'s

The proof is valid. Since
\[
t_{j+1}-t_j=2P+r_{j+1}-r_j\ge P+1,
\]
the \(t_j\)'s are strictly increasing, and the frozen range lies in
\([0,(D-1)/2)\). If \(C_j=C_k\), then
\(t_j^2\equiv t_k^2\pmod D\). Primality of \(D\) gives
\(t_j\equiv\pm t_k\pmod D\); the size interval rules out the minus case
except the common zero, and the plus case forces \(j=k\).

### 5. What the subresultant construction does and does not prove

For the squarefree polynomial
\[
F(X)=\prod_j(X-C_j),
\]
the identity
\[
\nu(N)=\deg\gcd_{\mathbb Q[X]}(F(X),F(X-N))
\]
is correct for \(N\ne0\): a common root is exactly an ordered pair with
\(C_a-C_b=N\).

Because both polynomials stay monic of fixed degree after specializing
\(Y=N\), standard subresultant specialization gives
\[
\nu(N)\ge7
\iff
\operatorname{psc}_0(N)=\cdots=\operatorname{psc}_6(N)=0.
\]
Thus an actual identity
\[
\sum_{r=0}^6 A_r(Y)\operatorname{psc}_r(Y)=MY^L,
\qquad M\ne0,
\]
would prove \(\nu(N)\le6\) at every nonzero integer \(N\), and the
three-lift lemma would then give \(h_c\le18\). Any such identity must have
\(L\ge1\), although the response harmlessly allowed \(L\ge0\) in the
existential statement.

No \(A_r\), \(M\), or \(L\) is produced, no degree or coefficient-size bound
is given, and no principal subresultant is evaluated. Calling Section 5 an
“exact ... certificate” is therefore too strong: it is an exact certificate
*format*. PC4 and the weaker \(\nu(N)\le6\) remain completely unproved.

### 6. Non-arithmetic-progression three-point states

When the three unordered differences are distinct up to sign, no two
transitions share a displacement, so phases disappear and
\[
\mathcal F_\Gamma=2(Auv+Bvw+Cuw).
\]
For positive \(A,B,C\) satisfying the strict triangle inequalities, exact
Lagrange optimization yields
\[
\Delta=2(AB+AC+BC)-A^2-B^2-C^2>0,
\]
\[
(u,v,w)=\frac1\Delta
\bigl(B(A-B+C),\ C(A+B-C),\ A(-A+B+C)\bigr),
\]
and
\[
M_{\rm nonAP}=\frac{2ABC}{\Delta}.
\]
If a triangle inequality fails, the maximum is one half of the largest edge
weight. The formulas agree at equality. The local verifier checks these
identities for every positive integer triple in \([1,20]^3\) satisfying the
strict triangle inequalities.

The equal-probability corollary
\[
h_c+h_d+h_{c+d}\le45
\]
is valid whenever the three displacement classes are distinct up to sign.
It is another necessary-only test; the response identifies no violating
frozen triple.

### 7. Perron-Schur domination

The matrix
\[
(\mathcal M_c)_{y,x}=|R_{y-x}(x)|
\]
is real, symmetric, and nonnegative because \(H^2\) is Hermitian. For a unit
vector \(f\), entrywise domination and the Rayleigh principle give
\[
\langle f,H^2f\rangle
\le |f|^T\mathcal M_c|f|
\le\rho(\mathcal M_c).
\]
Hence
\[
\|H\|_\infty^2\le\rho(\mathcal M_c),
\]
and Perron-Schur10 would indeed imply WR10. The positive-vector form follows
from the Collatz-Wielandt/Perron bound. Taking the all-ones vector recovers
the unweighted Schur row-sum condition.

The numerical example is correct:
\[
\rho\begin{pmatrix}9&2\\2&1\end{pmatrix}=5+2\sqrt5<10
\]
although its largest row sum is 11. This proves strict logical weakening in
the class of nonnegative symmetric matrices, not that the frozen tuple
satisfies the weaker condition.

Perron-Schur10 retains the same unresolved continuous quantifier over
Hermitian coefficients and introduces a matrix of order \(D\). The response
does not connect the five-carry equations to the intersections
\(\Gamma\cap(k-\Gamma)\), so this is a valid sufficient reformulation but
not a closure step.

## Remaining gap and next target

The earliest arithmetic gap is still a uniform exact bound on
\(\nu(N)\), or an actual frozen \(c\) or triple violating one of the physical
tests. A useful next step must replace the degree-\(m\) subresultant schema by
an explicit low-complexity consequence of the quotient/carry equations, with
a proved constant and a checkable certificate.

The global gap remains stronger: even perfect horizontal-fiber control does
not imply PW10. A valid global advance must derive a coefficient-uniform
phase-sensitive estimate for \(\Gamma\cap(k-\Gamma)\), produce an exact
physical counterexample, or justify replacing the frozen construction.

## Audit ledger

**PROVED**

- The full optimization and branchwise formula for AP three-level states.
- The integer doubling table, conditional as necessary consequences of PW10.
- The generic algebraic lower and consecutive-root upper bounds for \(S_c\).
- The three-absolute-lift lemma and the sharp implication PC4
  \(\Rightarrow h_c\le12\).
- Pairwise distinctness of the \(C_j\)'s.
- The gcd/subresultant equivalence and sufficiency of a *produced* Bezout
  identity of the displayed form.
- The optimized non-AP three-point formula.
- Perron domination and sufficiency of Perron-Schur10.

**CORRECTED / OVERSTATED**

- FiveCarry was not disproved; a five-class relative bound was sharpened to a
  three-lift absolute occupancy bound.
- No subresultant certificate was produced. Only a certificate schema was
  specified, using degree-\(m\) input.
- “Strictly smaller” for Perron-Schur10 is valid only as a weaker inequality
  for a fixed matrix, not as a smaller frozen-tuple verification problem.

**NECESSARY-ONLY**

- Every two-level and three-level physical-state condition.
- Fiber19, the doubling table, and the non-AP coupled conditions.
- Any conclusion based only on horizontal fibers.

**SUFFICIENT-ONLY AND OPEN**

- The uninstantiated subresultant/Bezout identity.
- Perron-Schur10 and weighted Schur control for the frozen tuple.

**OPEN**

- PC4 and the weaker uniform estimate \(\nu(N)\le6\).
- Whether an exact frozen \(c\) violates the optimized AP test.
- Whether an exact frozen triple violates the non-AP test.
- Uniform control of \(\Gamma\cap(k-\Gamma)\).
- WR10 and PW10.
- Every downstream all-\(T\) conclusion.

**CONJECTURED**

- None.

<!-- END HISTORICAL FILE path=outputs/round-10-local-audit.md -->


# ROUND 011

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-11-prompt.md bytes=8178 sha256=b85c867cd5740ff4dc49afc3a2607cbe63cd5781ea7492b92f300b4c41a33ecd -->

# Round 11 — globalize through the orbit channel; no new uninstantiated certificate schemas

Continue in the same conversation and the same canonically frozen finite
\(r=2\) low-\(A\) gate. Give a public, self-contained derivation and no
hidden chain-of-thought. Do not repeat the Round 8--10 narrative.

## Exact frozen boundary

Use exactly
\[
m=485165196,\qquad P=485165237=m+41,
\]
\[
D=941541228773064677=4P^2+1,
\qquad i=2P,
\qquad i^2=-1\pmod D,
\]
\[
0\le j\le P-42,
\qquad
r_j=j^2\bmod P\text{ in }[0,P-1],
\qquad
t_j=2Pj+r_j.
\]
Put
\[
a_j=(t_j,t_j^2)\in\mathbb F_D^2,
\qquad
A=\{a_j:0\le j\le P-42\},
\]
and
\[
\Gamma=\{a_a-a_b:a\ne b\}.
\]
The open one-copy gate is
\[
\boxed{
\mathcal F_\Gamma(\rho)
=\sum_{g\in\Gamma}|\operatorname{Tr}(W_g^*\rho)|^2
\le10
\quad\text{for every pure }\rho.
}
\tag{PW10}
\]
Its Hermitian Weyl-polynomial dual WR10 is already audited. Restating that
duality is not progress.

## Independently audited Round 10 boundary

The following facts are now independently checked.

1. For an arithmetic-progression three-level state, with
   \(h_c=|H_c|\), \(S_c=\sum_{p\in H_c}\omega^{pc}\),
   \(A_c=h_c+|S_c|\), and \(B_c=h_{2c}\), the exact optimum is
   \[
   M_3(c)=
   \begin{cases}
   B_c/2,&A_c=0,\\[2mm]
   2A_c^2/(4A_c-B_c),&A_c>0,\ B_c\le2A_c,\\[2mm]
   B_c/2,&B_c\ge2A_c.
   \end{cases}
   \]
   These give necessary-only tests, including \(h_c\le19\) and the exact
   doubling table. They do not prove PW10.

2. With
   \[
   C_j=4Ph_j+r_j^2-j^2-\sigma_j,
   \qquad
   t_j^2=D(j^2+\sigma_j)+C_j,
   \]
   and the audited interval for \(C_j\), every fixed horizontal fiber
   occupies at most three absolute lifts, because
   \[
   2(U-L)<3D,
   \qquad
   3D-2(U-L)=86359408745>0.
   \]
   Thus PC4, if it were true, would imply \(h_c\le12\). PC4 itself remains
   merely proposed.

3. The degree-\(m\) polynomial
   \[
   F(X)=\prod_j(X-C_j)
   \]
   correctly encodes
   \(\nu(N)=\deg\gcd(F(X),F(X-N))\), and a *produced* saturated
   subresultant Bezout identity would imply a constant bound. Round 10 did
   not produce one coefficient of that identity, a degree bound, or a
   coefficient-size bound. Starting from a polynomial of degree
   \(485165196\) is a certificate schema, not a genuinely small certificate
   or evidence that \(\nu(N)\le6\). Do not present it as progress again.

4. Perron-Schur10 is a valid sufficient inequality and is weaker than an
   unweighted row-sum estimate for a fixed matrix. It still quantifies over
   every Hermitian coefficient vector and a \(D\)-by-\(D\) matrix, and no
   frozen-tuple estimate was proved. Renaming another large sufficient
   condition is not progress.

5. FiveCarry itself was not disproved. The previous relative five-class
   bound was sharpened to three absolute lifts for one residue. Keep this
   logical distinction exact.

## New local calculation to audit: orbit Gram, channel, and Bell spectrum

First audit every normalization and sign below.

The ordered-difference map is injective. Indeed, from
\[
(p,q)=(t_a-t_b,t_a^2-t_b^2),\qquad p\ne0,
\]
one recovers
\[
t_a=\frac{q/p+p}{2},
\qquad
t_b=\frac{q/p-p}{2}.
\]
Thus \(|\Gamma|=m(m-1)\) without multiplicity.

For a unit vector \(\psi\), set
\[
\psi_j=W_{a_j}\psi,
\qquad
G_\psi=(\langle\psi_a,\psi_b\rangle)_{a,b},
\qquad
S_\psi=\sum_j|\psi_j\rangle\langle\psi_j|.
\]
The proposed exact identities are
\[
\boxed{
\mathcal F_\Gamma(\psi)
=\operatorname{Tr}(G_\psi^2)-m
=\operatorname{Tr}(S_\psi^2)-m.
}
\tag{Gram}
\]
Equivalently, for the random-unitary channel
\[
\Phi_A(\rho)=\frac1m\sum_{a\in A}W_a\rho W_a^*,
\]
PW10 is exactly
\[
\boxed{
\operatorname{Tr}(\Phi_A(\rho)^2)
\le\frac{m+10}{m^2}
\quad\text{for every pure }\rho.
}
\tag{Channel10}
\]

Next define
\[
U_g=W_g\otimes\overline{W_g},
\qquad
K_\Gamma=\sum_{g\in\Gamma}U_g.
\]
The Weyl multipliers cancel, so the \(U_g\)'s form a commuting ordinary
representation. In its Bell eigenbasis, the proposed eigenvalues are
\[
\boxed{
\lambda_z
=\sum_{g\in\Gamma}\omega^{[g,z]}
=\left|\sum_{a\in A}\omega^{[a,z]}\right|^2-m.
}
\tag{Spectrum}
\]
For
\[
\alpha_z=\operatorname{Tr}(W_z^*\rho),
\]
the claimed exact physical restriction is
\[
|\langle\Phi_z|\psi\otimes\bar\psi\rangle|^2
=\frac{|\alpha_z|^2}{D},
\]
and hence
\[
\boxed{
\mathcal F_\Gamma(\psi)
=\frac1D\sum_z
\left(
\left|\sum_{a\in A}\omega^{[a,z]}\right|^2-m
\right)|\alpha_z|^2.
}
\tag{Bell-Fourier}
\]
Here
\[
\alpha_0=1,
\qquad
|\alpha_z|\le1,
\qquad
\sum_z|\alpha_z|^2=D,
\]
plus the nonlinear twisted-convolution identities coming from
\(\rho^2=\rho\). The trivial Bell mode contributes the fixed amount
\[
\frac{m(m-1)}D,
\]
not an arbitrary spectral weight.

Fourier bookkeeping should also give
\[
\lambda_0=m(m-1),
\qquad
\sum_z\lambda_z=0,
\qquad
\sum_z\lambda_z^2=D^2m(m-1).
\tag{Moments}
\]
Therefore the nontrivial spectrum cannot be uniformly bounded by a constant.
A maximum-eigenvalue relaxation discards the essential
product-conjugate/pure-state restriction.

## Exact tasks

1. Give one verdict for PW10 on this exact frozen tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**. Failure of a relaxation is
   not a PW10 counterexample.

2. Prove or correct ordered-difference injectivity, (Gram), (Channel10),
   (Spectrum), (Bell-Fourier), and (Moments), including every factor of
   \(D\), conjugation convention, symplectic-character sign, and the
   \(z=0\) contribution. Show explicitly how a stabilizer ambiguity line
   recovers \(|\Gamma\cap L|\).

3. Do not stop at another equivalent reformulation. Choose one primary route
   and carry it as far as a checkable frozen-tuple conclusion:

   **Proof route.** Derive a quantitative inequality on *physically
   admissible* \((|\alpha_z|^2)_z\), using the purity/twisted-convolution
   identities rather than only box and mass constraints, and combine it with
   explicit bounds for the frozen spectrum to prove the constant 10. Every
   numerical constant must be evaluated at the displayed \(m,P,D\); no
   asymptotic \(O(\cdot)\) claim is enough.

   **Disproof route.** Give an explicit normalized physical state \(\psi\)
   (finite support and exact phases, or certified rational/algebraic
   enclosures) and compute a rigorous lower bound
   \(\mathcal F_\Gamma(\psi)>10\). Alternatively, give an actual
   WR10-violating Hermitian coefficient vector and carry the extremal
   eigenvector through to a physical PW10 violator. A large Bell eigenvalue,
   failed Schur bound, or feasible nonphysical weight vector is not enough.

   **Obstruction route.** If neither proof nor disproof is reached, identify
   the first exact missing inequality after Bell-Fourier. Prove that the
   weaker relaxation you reject really cannot certify 10 by an explicit
   violating feasible point or dual separation, then derive the smallest
   additional pure-state constraint that would remove that obstruction.
   State its exact dimension/degree and why it is genuinely smaller than the
   original PW10 problem. An unnamed future SDP or a \(D\)-sized matrix is
   not a deliverable.

4. You may return to the carry arithmetic only if you produce one of the
   following: an exact frozen collision certificate, a proved uniform
   constant for \(\nu(N)\), or a bounded-degree system with an explicit
   degree and an actual solution-count proof. Do not repeat the degree-\(m\)
   subresultant schema, generic Bezout existence, or small-prime evidence.

5. If the exact frozen tuple cannot plausibly meet PW10, explain the precise
   proved obstruction before proposing a replacement. Do not silently change
   \(m\), \(D\), \(A\), the factor 10, or the downstream theorem.

6. End with an audit ledger separating **PROVED**, **DISPROVED**,
   **NECESSARY-ONLY**, **SUFFICIENT-ONLY**, **OPEN**, and **CONJECTURED**.
   The ledger must distinguish a proven identity, satisfaction of that
   identity's hypothesis by the frozen tuple, and an uninstantiated
   certificate format.

The objective of this round is a real contraction of the global gap. A new
name for PW10, a degree-\(m\) resultant, or a \(D\)-dimensional sufficient
matrix inequality does not count as closure or as a smaller certificate.

<!-- END HISTORICAL FILE path=work/round-11-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-11-response.md bytes=19453 sha256=d6c157aa1c4a908fc2db7d708fa94281ed01e0ed84d56d754f548ed1c122a652 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The orbit-Gram, channel, doubled-Weyl spectrum, Bell-overlap, Fourier-moment, and stabilizer-line formulas are all correct after fixing the Bell-vector convention explicitly.

The elementary Bell-weight relaxation

$$
w_z\ge0,\qquad
\sum_z w_z=1,\qquad
w_0=\frac1D,\qquad
w_z=w_{-z}\le\frac1D
$$

cannot certify \(10\): the exact frozen spectrum has at least \(D\) eigenvalues strictly larger than \(10\), producing a canonical feasible point with objective \(>10\).

The first genuinely physical constraint missing from that relaxation can be made completely local. For

$$
x_z:=|\alpha_z|^2=Dw_z,
$$

every pure state satisfies, for all \(g,h\),

$$
\boxed{
x_gx_h
\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le
(1-x_g)(1-x_h).
}
\tag{LC}
$$

This is a quadratic inequality in two real variables. It follows from two overlapping \(3\times3\) Weyl-orbit Gram matrices. It excludes the canonical \(>10\) Bell-weight pseudo-point because its unit-weight support necessarily contains two noncommuting labels.

That is a real contraction of the obstruction, but it does not prove that all weights satisfying these pairwise conditions have Bell expectation at most \(10\). No physical violating state is constructed.

---

## 1. Ordered-difference injectivity

Let

$$
a_j=(t_j,t_j^2)\in\mathbb F_D^2.
$$

Suppose

$$
a_a-a_b=(p,q),
\qquad a\ne b.
$$

Then

$$
p=t_a-t_b\ne0
$$

and

$$
q=t_a^2-t_b^2
=p(t_a+t_b).
$$

Therefore

$$
t_a+t_b=\frac qp,
$$

and, since \(D\) is odd,

$$
\boxed{
t_a=\frac{q/p+p}{2},
\qquad
t_b=\frac{q/p-p}{2}.
}
\tag{1.1}
$$

The frozen \(t_j\)'s are distinct, so \((p,q)\) uniquely determines the ordered pair \((a,b)\). Hence

$$
\boxed{|\Gamma|=m(m-1)}
\tag{1.2}
$$

without multiplicity.

Put

$$
M:=|\Gamma|=m(m-1)=235385266924553220.
$$

---

## 2. Orbit Gram matrix and channel purity

For a unit vector \(\psi\), define

$$
\psi_j=W_{a_j}\psi,
$$

and let \(V_\psi:\mathbb C^m\to\mathbb C^D\) be the synthesis map

$$
V_\psi e_j=\psi_j.
$$

Then

$$
G_\psi=V_\psi^*V_\psi,
\qquad
S_\psi=V_\psi V_\psi^*
=\sum_j|\psi_j\rangle\langle\psi_j|.
$$

Thus \(G_\psi\) and \(S_\psi\) have the same nonzero eigenvalues, so

$$
\operatorname{Tr}(G_\psi^2)=\operatorname{Tr}(S_\psi^2).
\tag{2.1}
$$

For \(a,b\),

$$
\begin{aligned}
G_\psi(a,b)
&=
\langle\psi|W_{a_a}^*W_{a_b}|\psi\rangle\\
&=
\omega^{-[a_a,a_b]/2}
\langle\psi|W_{a_b-a_a}|\psi\rangle.
\end{aligned}
$$

The phase disappears after taking absolute values. The diagonal terms equal \(1\), and ordered-difference injectivity implies that the off-diagonal labels \(a_b-a_a\) run through \(\Gamma\) exactly once. Hence

$$
\begin{aligned}
\operatorname{Tr}(G_\psi^2)
&=
\sum_{a,b}|G_\psi(a,b)|^2\\
&=
m+\sum_{g\in\Gamma}
|\langle\psi|W_g|\psi\rangle|^2\\
&=
m+\mathcal F_\Gamma(\psi).
\end{aligned}
$$

Therefore

$$
\boxed{
\mathcal F_\Gamma(\psi)
=
\operatorname{Tr}(G_\psi^2)-m
=
\operatorname{Tr}(S_\psi^2)-m.
}
\tag{Gram}
$$

For

$$
\Phi_A(\rho)=\frac1m\sum_jW_{a_j}\rho W_{a_j}^*,
$$

a pure input \(\rho=|\psi\rangle\langle\psi|\) gives

$$
\Phi_A(\rho)=\frac{S_\psi}{m}.
$$

Consequently,

$$
\operatorname{Tr}\Phi_A(\rho)^2
=
\frac{m+\mathcal F_\Gamma(\psi)}{m^2}.
$$

Thus

$$
\boxed{
\mathcal F_\Gamma(\psi)\le10
\quad\Longleftrightarrow\quad
\operatorname{Tr}\Phi_A(\rho)^2
\le\frac{m+10}{m^2}
}
\tag{Channel10}
$$

for every pure \(\rho\).

---

## 3. Doubled Weyl representation and Bell basis

Use

$$
W_gW_h=\omega^{[g,h]/2}W_{g+h}.
$$

Entrywise conjugation reverses the cocycle:

$$
\overline{W_g}\,\overline{W_h}
=
\omega^{-[g,h]/2}\overline{W_{g+h}}.
$$

Therefore

$$
\boxed{
(W_g\otimes\overline{W_g})
(W_h\otimes\overline{W_h})
=
W_{g+h}\otimes\overline{W_{g+h}}.
}
\tag{3.1}
$$

Hence

$$
U_g:=W_g\otimes\overline{W_g}
$$

is an ordinary commuting representation of the additive group
\(\mathbb F_D^2\).

Define

$$
\vartheta(p,q)=(p,-q).
$$

For the chosen Weyl convention,

$$
W_z^{\mathsf T}=W_{\vartheta z}.
\tag{3.2}
$$

Use column vectorization and define

$$
\boxed{
|\Phi_z\rangle
=
\frac1{\sqrt D}|W_{\vartheta z}\rangle\rangle
=
\frac1{\sqrt D}|W_z^{\mathsf T}\rangle\rangle.
}
\tag{3.3}
$$

These vectors form an orthonormal Bell basis.

Since

$$
(A\otimes B)|X\rangle\rangle
=
|BXA^{\mathsf T}\rangle\rangle,
$$

one obtains

$$
\begin{aligned}
U_g|W_{\vartheta z}\rangle\rangle
&=
|\overline{W_g}W_{\vartheta z}W_g^{\mathsf T}\rangle\rangle\\
&=
\omega^{[g,z]}|W_{\vartheta z}\rangle\rangle.
\end{aligned}
$$

Thus

$$
\boxed{
U_g|\Phi_z\rangle
=
\omega^{[g,z]}|\Phi_z\rangle.
}
\tag{3.4}
$$

For

$$
K_\Gamma=\sum_{g\in\Gamma}U_g,
$$

the eigenvalue at \(|\Phi_z\rangle\) is therefore

$$
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]}.
$$

Using \(\Gamma=(A-A)\setminus\{0\}\) and ordered-difference injectivity,

$$
\begin{aligned}
\lambda_z
&=
\sum_{a\ne b}\omega^{[a_a-a_b,z]}\\
&=
\left|\sum_a\omega^{[a_a,z]}\right|^2-m.
\end{aligned}
$$

Hence

$$
\boxed{
\lambda_z
=
\left|\sum_{a\in A}\omega^{[a,z]}\right|^2-m.
}
\tag{Spectrum}
$$

In particular,

$$
-m\le\lambda_z\le m(m-1)=M.
\tag{3.5}
$$

Because \(\Gamma=-\Gamma\),

$$
\lambda_z\in\mathbb R,
\qquad
\lambda_{-z}=\lambda_z.
\tag{3.6}
$$

---

## 4. Physical Bell overlaps

For

$$
\rho=|\psi\rangle\langle\psi|,
\qquad
\alpha_z=\operatorname{Tr}(W_z^*\rho),
$$

one has

$$
|\psi\rangle\otimes|\overline\psi\rangle
=
|\rho^{\mathsf T}\rangle\rangle.
$$

Using \(W_{\vartheta z}=W_z^{\mathsf T}\),

$$
\begin{aligned}
\langle\Phi_z|
\psi\otimes\overline\psi\rangle
&=
\frac1{\sqrt D}
\operatorname{Tr}\!\left[
(W_z^{\mathsf T})^*\rho^{\mathsf T}
\right]\\
&=
\frac1{\sqrt D}
\operatorname{Tr}(W_z^*\rho)\\
&=
\frac{\alpha_z}{\sqrt D}.
\end{aligned}
$$

Therefore

$$
\boxed{
\left|
\langle\Phi_z|
\psi\otimes\overline\psi\rangle
\right|^2
=
\frac{|\alpha_z|^2}{D}.
}
\tag{4.1}
$$

Diagonalizing \(K_\Gamma\) in this basis yields

$$
\boxed{
\mathcal F_\Gamma(\psi)
=
\frac1D
\sum_z
\left(
\left|\sum_{a\in A}\omega^{[a,z]}\right|^2-m
\right)
|\alpha_z|^2.
}
\tag{Bell-Fourier}
$$

The physical coefficients satisfy

$$
\alpha_0=1,
\qquad
\alpha_{-z}=\overline{\alpha_z},
\qquad
|\alpha_z|\le1,
\qquad
\sum_z|\alpha_z|^2=D.
\tag{4.2}
$$

The last equality is Weyl Parseval for a pure state.

The \(z=0\) term is fixed:

$$
\boxed{
\frac{\lambda_0|\alpha_0|^2}{D}
=
\frac{m(m-1)}D
=
\frac{235385266924553220}
{941541228773064677}.
}
\tag{4.3}
$$

It is not a freely assignable spectral weight.

The full pure-state restriction additionally includes

$$
\boxed{
\alpha_k
=
\frac1D
\sum_h
\alpha_h\alpha_{k-h}\,
\omega^{[h,k]/2}
\quad\text{for every }k,
}
\tag{4.4}
$$

which is the coefficient form of \(\rho^2=\rho\).

---

## 5. Fourier moments of the spectrum

At \(z=0\),

$$
\boxed{\lambda_0=M=m(m-1).}
\tag{5.1}
$$

Since \(0\notin\Gamma\), character orthogonality gives

$$
\begin{aligned}
\sum_z\lambda_z
&=
\sum_{g\in\Gamma}\sum_z\omega^{[g,z]}\\
&=0.
\end{aligned}
$$

Hence

$$
\boxed{\sum_z\lambda_z=0.}
\tag{5.2}
$$

Fourier Parseval on the group of order \(D^2\) gives

$$
\sum_z|\lambda_z|^2
=
D^2|\Gamma|.
$$

The eigenvalues are real, so

$$
\boxed{
\sum_z\lambda_z^2
=
D^2m(m-1).
}
\tag{Moments}
$$

These moments already preclude a constant uniform upper bound on the nontrivial \(\lambda_z\), but they say nothing by themselves about physical Bell weights.

---

## 6. Stabilizer ambiguity lines

Let \(L\subset\mathbb F_D^2\) be an isotropic line through \(0\). A stabilizer state associated with \(L\) has

$$
|\alpha_z|^2=
\begin{cases}
1,&z\in L,\\
0,&z\notin L.
\end{cases}
$$

Therefore Bell-Fourier gives

$$
\mathcal F_\Gamma(\rho_L)
=
\frac1D\sum_{z\in L}\lambda_z.
$$

Now

$$
\begin{aligned}
\sum_{z\in L}\lambda_z
&=
\sum_{g\in\Gamma}
\sum_{z\in L}\omega^{[g,z]}\\
&=
D\,|\Gamma\cap L^{\perp_{\rm sp}}|.
\end{aligned}
$$

In a two-dimensional nondegenerate symplectic space,

$$
L^{\perp_{\rm sp}}=L.
$$

Thus

$$
\boxed{
\mathcal F_\Gamma(\rho_L)
=
|\Gamma\cap L|.
}
\tag{6.1}
$$

For the frozen set, every line contains at most two \(\Gamma\)-points.

Indeed, the vertical line contains none because every nonzero difference has first coordinate \(t_a-t_b\ne0\). For a nonvertical line of slope \(s\),

$$
(t_a-t_b,t_a^2-t_b^2)\in L_s
\quad\Longleftrightarrow\quad
t_a+t_b=s.
$$

The frozen \(\{t_j\}\) is a sum-Sidon set modulo \(D\). A direct proof is short. Since

$$
t_j=2Pj+r_j,
$$

all pair sums lie strictly between \(0\) and \(D\), so equality modulo \(D\) is integer equality. If

$$
t_a+t_b=t_c+t_d,
$$

then

$$
2P(a+b-c-d)
=
-(r_a+r_b-r_c-r_d).
$$

The right side has absolute value \(<2P\), hence both sides vanish:

$$
a+b=c+d,
\qquad
r_a+r_b=r_c+r_d.
$$

Reducing modulo \(P\),

$$
a^2+b^2\equiv c^2+d^2\pmod P.
$$

Together with equality of the sums, this gives

$$
ab\equiv cd\pmod P.
$$

Thus the two unordered pairs are the same in \(\mathbb F_P\), and all indices lie in \([0,P-1]\), so

$$
\{a,b\}=\{c,d\}.
$$

Therefore

$$
\boxed{|\Gamma\cap L|\le2}
\tag{6.2}
$$

for every isotropic line.

---

# 7. The elementary Bell-weight relaxation fails

Define physical Bell weights

$$
w_z=\frac{|\alpha_z|^2}{D}.
$$

Every pure state satisfies

$$
w_z\ge0,\qquad
\sum_z w_z=1,\qquad
w_0=\frac1D,
$$

$$
w_z=w_{-z},
\qquad
w_z\le\frac1D.
\tag{7.1}
$$

Consider the relaxation consisting only of these constraints.

## 7.1 At least \(D\) eigenvalues exceed \(10\)

Let

$$
\mathcal H=\{z:\lambda_z>10\},
\qquad
b=|\mathcal H|.
$$

Suppose \(b\le D-1\). Let

$$
P_+=\sum_{\lambda_z>0}\lambda_z.
$$

Since \(\sum_z\lambda_z=0\), the total negative absolute mass also equals \(P_+\).

For negative eigenvalues,

$$
\lambda_z^2\le m(-\lambda_z).
$$

For positive eigenvalues at most \(10\),

$$
\lambda_z^2\le10\lambda_z.
$$

For the \(b\) eigenvalues exceeding \(10\),

$$
\lambda_z^2\le M^2.
$$

Consequently,

$$
D^2M
=
\sum_z\lambda_z^2
\le
bM^2+(m+10)P_+.
\tag{7.2}
$$

Also,

$$
P_+
\le
bM+10(D^2-b)
\le
DM+10D^2.
\tag{7.3}
$$

Thus \(b\le D-1\) would imply

$$
D^2M
\le
DM^2+(m+10)(DM+10D^2).
\tag{7.4}
$$

But the reverse inequality holds. After division by \(D\), it is enough to show

$$
D\bigl(M-10(m+10)\bigr)
>
M(m^2+10).
$$

Now

$$
M-10(m+10)=m^2-11m-100>0,
$$

and

$$
D=4P^2+1>4m^2.
$$

Therefore the left side minus the right side is strictly larger than

$$
\begin{aligned}
&4m^2(m^2-11m-100)
-
m(m-1)(m^2+10)\\
&\qquad=
m(3m^3-43m^2-410m+10)>0,
\end{aligned}
$$

using the displayed exact \(m\). This contradicts (7.4). Hence

$$
\boxed{|\mathcal H|\ge D.}
\tag{7.5}
$$

The set \(\mathcal H\) is centrally symmetric and contains \(0\).

## 7.2 An exact feasible pseudo-weight with value \(>10\)

Order inverse pairs \(\{z,-z\}\) lexicographically using their representatives in \(\{0,\ldots,D-1\}^2\). Let \(\mathcal S\) consist of \(0\) together with the first \((D-1)/2\) inverse pairs contained in \(\mathcal H\). Then

$$
|\mathcal S|=D,
\qquad
\mathcal S=-\mathcal S,
\qquad
0\in\mathcal S.
$$

Define

$$
w_z^{\rm cap}
=
\begin{cases}
1/D,&z\in\mathcal S,\\
0,&z\notin\mathcal S.
\end{cases}
\tag{7.6}
$$

This satisfies every constraint in (7.1), but

$$
\sum_z\lambda_zw_z^{\rm cap}
=
\frac1D\sum_{z\in\mathcal S}\lambda_z
>10.
\tag{7.7}
$$

Therefore

$$
\boxed{
\text{mass, symmetry, the cap }w_z\le1/D,
\text{ and fixed }w_0
\text{ cannot certify PW10.}
}
\tag{7.8}
$$

This is an exact frozen-spectrum obstruction, not numerical sampling.

---

# 8. The first local pure-state constraint missing from that relaxation

Set

$$
\beta_z=\langle\psi|W_z|\psi\rangle
=\overline{\alpha_z}.
$$

For any \(g,h\), the Gram matrix of

$$
|\psi\rangle,\qquad W_g|\psi\rangle,\qquad W_h|\psi\rangle
$$

is

$$
\boxed{
\mathcal M(g,h)=
\begin{pmatrix}
1 & \beta_g & \beta_h\\
\overline{\beta_g}
&1
&\omega^{-[g,h]/2}\beta_{h-g}\\
\overline{\beta_h}
&\omega^{[g,h]/2}\overline{\beta_{h-g}}
&1
\end{pmatrix}
\succeq0.
}
\tag{8.1}
$$

Its determinant condition is

$$
\boxed{
\begin{aligned}
1
&-|\beta_g|^2
-|\beta_h|^2
-|\beta_{h-g}|^2\\
&+
2\operatorname{Re}\!\left(
\omega^{-[g,h]/2}
\beta_g\beta_{h-g}\overline{\beta_h}
\right)
\ge0.
\end{aligned}
}
\tag{8.2}
$$

The \(2\times2\) principal minors of these matrices give only

$$
|\beta_z|\le1,
$$

which is exactly the already-used Bell-weight cap. Thus \(3\times3\) is the first orbit-Gram level containing new information.

---

## 8.1 Eliminating the intermediate coefficient

Put

$$
\kappa=[g,h]\in\mathbb F_D.
$$

Apply (8.1) first to the labels

$$
0,\quad g,\quad g+h.
$$

The determinant can be written as

$$
\boxed{
\left|
\beta_{g+h}
-
\omega^{-\kappa/2}\beta_g\beta_h
\right|^2
\le
(1-|\beta_g|^2)(1-|\beta_h|^2).
}
\tag{8.3}
$$

Apply it again to

$$
0,\quad h,\quad g+h.
$$

This gives

$$
\boxed{
\left|
\beta_{g+h}
-
\omega^{\kappa/2}\beta_g\beta_h
\right|^2
\le
(1-|\beta_g|^2)(1-|\beta_h|^2).
}
\tag{8.4}
$$

The two disks in (8.3)–(8.4) must intersect. Their centers have distance

$$
2|\beta_g\beta_h|
\left|
\sin\left(\frac{\pi\kappa}{D}\right)
\right|.
$$

Each radius equals

$$
\sqrt{(1-|\beta_g|^2)(1-|\beta_h|^2)}.
$$

Hence every physical pure state satisfies

$$
\boxed{
|\beta_g|^2|\beta_h|^2
\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le
(1-|\beta_g|^2)(1-|\beta_h|^2).
}
\tag{8.5}
$$

Since \(|\beta_z|=|\alpha_z|\), this is

$$
\boxed{
x_gx_h
\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le
(1-x_g)(1-x_h),
\qquad
x_z:=|\alpha_z|^2.
}
\tag{LC}
$$

In Bell-weight variables,

$$
\boxed{
D^2w_gw_h
\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le
(1-Dw_g)(1-Dw_h).
}
\tag{8.6}
$$

This is a degree-two scalar inequality in the two weights \(w_g,w_h\).

A useful equivalent consequence is

$$
\boxed{
x_g+x_h
\le
\frac{2}{
1+\left|\sin(\pi[g,h]/D)\right|
}.
}
\tag{8.7}
$$

The maximum is attained in the scalar relaxation at

$$
x_g=x_h=
\frac1{1+|\sin(\pi[g,h]/D)|}.
$$

---

# 9. Why the local constraint excludes the pseudo-weight

Suppose every pair of elements in \(\mathcal S\) were symplectically orthogonal. Choose a nonzero \(g\in\mathcal S\). Then

$$
\mathcal S\subseteq g^{\perp_{\rm sp}}.
$$

In two dimensions,

$$
g^{\perp_{\rm sp}}=\operatorname{span}(g),
$$

which is a line containing exactly \(D\) points. Since \(|\mathcal S|=D\),

$$
\mathcal S=\operatorname{span}(g).
$$

But every \(z\in\mathcal S\) has \(\lambda_z>10\), so

$$
\frac1D\sum_{z\in\mathcal S}\lambda_z>10.
$$

The stabilizer-line identity gives instead

$$
\frac1D\sum_{z\in\mathcal S}\lambda_z
=
|\Gamma\cap\mathcal S|
\le2,
$$

a contradiction.

Therefore there exist \(g,h\in\mathcal S\) with

$$
[g,h]\ne0.
\tag{9.1}
$$

At the pseudo-weight (7.6),

$$
x_g=Dw_g^{\rm cap}=1,
\qquad
x_h=Dw_h^{\rm cap}=1.
$$

The right side of (LC) is zero, whereas the left side is

$$
\sin^2\!\left(\frac{\pi[g,h]}D\right)>0.
$$

Thus the pseudo-weight violates the exact local pure-state constraint.

Equivalently, no assignment of phases to the unit-modulus coefficients on \(\mathcal S\) can make all of the \(3\times3\) Weyl-orbit Gram matrices positive semidefinite.

---

# 10. The precise remaining gap

The elementary Bell-weight relaxation is now conclusively separated from the physical set:

$$
\text{Bell mass/cap relaxation}
\quad\supsetneq\quad
\text{physical pure-state weights}.
$$

The separation is witnessed by one noncommuting pair and the scalar inequality (LC).

This is the smallest local orbit-moment correction:

* \(2\times2\) Gram positivity gives only \(|\alpha_z|\le1\);
* \(3\times3\) Gram positivity produces (LC);
* each constraint uses only two squared moduli and one known symplectic product;
* it is degree two in the Bell weights;
* excluding the canonical pseudo-point requires only two overlapping \(3\times3\) minors involving

  $$
  0,\quad g,\quad h,\quad g+h.
  $$

No \(D\times D\) matrix or uninstantiated certificate is involved.

What remains open is the genuinely global implication

$$
\boxed{
\begin{gathered}
x_0=1,\quad
x_z=x_{-z}\in[0,1],\quad
\sum_zx_z=D,\\
x_gx_h\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le(1-x_g)(1-x_h)
\quad\forall g,h\\
\stackrel{?}{\Longrightarrow}\quad
\frac1D\sum_z\lambda_zx_z\le10.
\end{gathered}
}
\tag{10.1}
$$

Every physical pure state satisfies the hypotheses, but their sufficiency is not proved and is not claimed. The full twisted-convolution identities (4.4) are stronger still.

Thus the first exact missing step after Bell-Fourier is no longer “exclude arbitrary capped Bell weights.” That obstruction has been removed. It is now:

> **Open local-to-global step.** Determine whether the pairwise commutation inequalities (LC), possibly together with a finite higher orbit-moment constraint derived from (4.4), force the frozen spectral functional below \(10\), or produce a physical characteristic vector violating it.

No exact physical violator and no constant-\(10\) proof is obtained. The carry arithmetic is not used because no new exact collision certificate or constant multiplicity theorem is produced.

---

# Audit ledger

## PROVED

* The ordered-difference map \((a,b)\mapsto a_a-a_b\) is injective.
* \(|\Gamma|=m(m-1)\).
* The orbit identities

  $$
  \mathcal F_\Gamma=\operatorname{Tr}G_\psi^2-m
  =\operatorname{Tr}S_\psi^2-m.
  $$
* The exact channel equivalence Channel10.
* \(g\mapsto W_g\otimes\overline{W_g}\) is an ordinary commuting representation.
* With

  $$
  |\Phi_z\rangle=D^{-1/2}|W_z^{\mathsf T}\rangle\rangle,
  $$

  the eigenvalue is

  $$
  \lambda_z=
  \left|\sum_{a\in A}\omega^{[a,z]}\right|^2-m.
  $$
* The exact overlap

  $$
  |\langle\Phi_z|\psi\otimes\bar\psi\rangle|^2
  =|\alpha_z|^2/D.
  $$
* Bell-Fourier, including the fixed \(z=0\) contribution \(m(m-1)/D\).
* The spectral moment identities

  $$
  \lambda_0=m(m-1),\quad
  \sum_z\lambda_z=0,\quad
  \sum_z\lambda_z^2=D^2m(m-1).
  $$
* A stabilizer ambiguity line gives exactly

  $$
  \mathcal F_\Gamma(\rho_L)=|\Gamma\cap L|.
  $$
* For the frozen set, every line has \(|\Gamma\cap L|\le2\).
* At least \(D\) Bell eigenvalues are strictly larger than \(10\).
* The canonical capped Bell-weight relaxation has an exact feasible point with objective \(>10\).
* The \(3\times3\) Weyl-orbit Gram constraint (8.1).
* The two-disk inequalities (8.3)–(8.4).
* The two-mode commutation inequality (LC).
* The canonical capped pseudo-point violates (LC).

## DISPROVED

* Sufficiency of Bell-weight nonnegativity, normalization, evenness, the cap \(w_z\le1/D\), and fixed \(w_0=1/D\) for proving the constant \(10\).
* The possibility that the canonical \(D\)-point high-spectrum pseudo-weight is physical.

## NECESSARY-ONLY

* The two-mode commutation inequality (LC).
* The pairwise cap (8.7).
* Stabilizer-line tests.
* The mass, cap, symmetry, and twisted-convolution identities for physical characteristic coefficients.
* The degree-two relaxation (10.1).

## SUFFICIENT-ONLY

* No new sufficient-only frozen-tuple criterion is claimed in this round.

## OPEN

* Whether the pairwise constraints (LC) already force the Bell-Fourier value to be at most \(10\).
* What finite higher orbit-moment consequence of twisted idempotence is first needed if they do not.
* PW10 for the canonically frozen tuple.
* The finite \(r=2\) low-\(A\) gate.

## CONJECTURED

* No statement is promoted to conjectured status.

The first new claim requiring independent verification is the exact two-mode inequality

$$
|\alpha_g|^2|\alpha_h|^2
\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le
(1-|\alpha_g|^2)(1-|\alpha_h|^2),
$$

derived from the two overlapping \(3\times3\) Weyl-orbit Gram matrices.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-11-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-11-local-audit.md bytes=7842 sha256=c43c9c3978d20788ee785ef79b2bf4c8360d9b830f3644726b917457eee684ca -->

# Round 11 local audit

## Capture integrity

- Conversation: `<private-chat-link-removed>`
- Surface: ordinary Chat
- Model: GPT-5.6 Sol
- Thinking power: Pro, 5 of 5
- Browser receipt: `Worked for 26m 28s`
- Captured response: 19,445 Unicode characters, 19,453 UTF-8 bytes, 1,227 lines
- Response SHA-256: `d6c157aa1c4a908fc2db7d708fa94281ed01e0ed84d56d754f548ed1c122a652`
- The artifact and output copies have identical hashes.

## Verdict

The web response's main verdict is correct:

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN.}}
\]

It neither proves the uniform physical inequality nor constructs a physical
state with value greater than 10.  Its new two-label inequality is valid, but
the response stops one step too early: the proposed global implication from
all such inequalities is now exactly disproved by a fractional feasible point.
This disproves the relaxation, not PW10.

## Claims independently checked

The following normalization-level claims agree with the pre-response local
derivation and with the deterministic convention test at `D=13, m=4`:

1. The ordered-difference map is injective and
   \(|\Gamma|=m(m-1)=235385266924553220\).
2. The orbit identities are
   \[
   \mathcal F_\Gamma(\psi)=\operatorname{Tr}(G_\psi^2)-m
   =\operatorname{Tr}(S_\psi^2)-m.
   \]
3. PW10 is equivalent to
   \[
   \operatorname{Tr}(\Phi_A(\rho)^2)\le\frac{m+10}{m^2}
   \]
   for every pure input.
4. With the response's column-vectorization and reflection convention, the
   Bell eigenvalue and overlap formulas are consistent:
   \[
   \lambda_z=\left|\sum_{a\in A}\omega^{[a,z]}\right|^2-m,
   \qquad
   |\langle\Phi_z|\psi\otimes\bar\psi\rangle|^2
   =\frac{|\alpha_z|^2}{D}.
   \]
5. The moment identities and the fixed zero-mode contribution are correct:
   \[
   \lambda_0=m(m-1),\quad \sum_z\lambda_z=0,\quad
   \sum_z\lambda_z^2=D^2m(m-1),
   \]
   \[
   \frac{\lambda_0|\alpha_0|^2}{D}
   =\frac{m(m-1)}D.
   \]
6. A stabilizer ambiguity line gives
   \(\mathcal F_\Gamma=|\Gamma\cap L|\), and the frozen sum-Sidon argument
   gives \(|\Gamma\cap L|\le2\).

The small-prime program returned:

```text
Round 11 small-prime convention checks: PASS
D=13, m=4, |Gamma|=12, stabilizer intersection=2
```

This is a convention test only; it is not evidence that the frozen large
tuple satisfies PW10.

## Audit of the new local constraint

For \(U=W_g\), \(V=W_h\), and
\(UV=\zeta VU\), centered-unitary Cauchy--Schwarz applied in both orders gives

\[
|1-\zeta|\,|\langle U\rangle\langle V\rangle|
\le
2\sqrt{(1-|\langle U\rangle|^2)(1-|\langle V\rangle|^2)}.
\]

With \(x_g=|\alpha_g|^2\), \(x_h=|\alpha_h|^2\), and
\(|1-\omega^{[g,h]}|^2=4\sin^2(\pi[g,h]/D)\), this is exactly the web
response's constraint

\[
\boxed{
x_gx_h\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le(1-x_g)(1-x_h).
}
\tag{LC}
\]

The response's overlapping-disk derivation and its scalar consequence

\[
x_g+x_h\le
\frac{2}{1+|\sin(\pi[g,h]/D)|}
\]

are correct.  LC excludes the old saturated \(D\)-point high-spectrum
pseudo-weight because such a support cannot be an isotropic line.

The response is also right that this is the first new *local matrix-size*
level: `2 x 2` orbit-Gram positivity gives only the cap, whereas `3 x 3`
positivity contains a Bargmann-phase constraint.  This does not make the
global relaxation small: imposing LC for all ordered label pairs is a
family on the order of \(D^4\).

## Exact correction: the LC implication is false

Let

\[
M=m(m-1),\qquad
\mathcal B=\{z:\lambda_z>10\},\qquad b=|\mathcal B|.
\]

The web response proves only \(b\ge D\).  Keeping its same moment argument
without replacing \(b\) by \(D\) gives the stronger exact bound

\[
\boxed{
b\ge
\left\lceil
\frac{D^2\bigl(M-10(m+10)\bigr)}
{M^2+(m+10)(M-10)}
\right\rceil
=3766165474002670825
=4D+558910412117.
}
\tag{HC}
\]

Because \(D\) is odd, \(\mathcal B=-\mathcal B\), and \(0\in\mathcal B\),
choose a centrally symmetric \(S\subset\mathcal B\) of size \(2D-1\)
containing zero.  Define

\[
x_0=1,\qquad
x_z=\frac12\quad(z\in S\setminus\{0\}),\qquad
x_z=0\quad(z\notin S).
\tag{Half}
\]

Then \(x_z=x_{-z}\), \(0\le x_z\le1\), and

\[
\sum_zx_z=1+\frac{2D-2}{2}=D.
\]

Every active label has \(\lambda_z>10\), so

\[
\boxed{\frac1D\sum_z\lambda_zx_z>10.}
\]

Nevertheless, (Half) satisfies every LC constraint.  If either weight is
zero the claim is immediate.  If two nonzero active labels are used, then
both weights are \(1/2\) and

\[
\frac14\sin^2\!\left(\frac{\pi[g,h]}D\right)\le\frac14.
\]

The only unit weight is \(x_0\), and zero commutes symplectically with every
label.  Hence the exact implication displayed as equation (10.1) in the web
response is false.

The same half-point even satisfies every phase-free `3 x 3` consequence

\[
x_z+x_w+x_{w-z}
\le1+2\sqrt{x_zx_wx_{w-z}}.
\tag{TriGram}
\]

If no displayed label is zero, its weights are in \(\{0,1/2\}\): with at
most two active terms the left side is at most one, and with all three it is
\(3/2\le1+1/\sqrt2\).  If one label is zero, evenness or equality of the
other two labels makes their weights equal and TriGram holds with equality.

The exact checker returned:

```text
Round 12 exact high-count and half-point checks: PASS
b_min=3766165474002670825
b_min-4D=558910412117
```

## Further contraction beyond the web response

Pure-state ambiguity weights also satisfy the exact self-Fourier identity

\[
x_u=\frac1D\sum_zx_z\omega^{[u,z]}.
\tag{SF}
\]

For a half-point this forces \(T=S\setminus\{0\}\) to be a partial
difference set with parameters

\[
(v,k,\lambda,\mu)=(D^2,2(D-1),D-2,2).
\]

Taking magnitudes in twisted idempotence supplies another necessary condition,

\[
D\sqrt{x_k}\le\sum_h\sqrt{x_hx_{k-h}}.
\tag{ConvMag}
\]

For every nonzero \(k\in S\), the partial-difference-set count makes the
right side \(\sqrt2+(D-2)/2\), while the left side is \(D/\sqrt2\).  The
left side exceeds the right side by

\[
\frac{(\sqrt2-1)(D-2)}2>0.
\]

Therefore every half-point is excluded once these two global magnitude
consequences of purity are imposed.  This does not restore the false LC-only
implication; it gives a strictly stronger next relaxation and confirms that
the half-point is not a physical PW10 counterexample.

## Correct boundary after Round 11

### PROVED

- All orbit/channel/Bell identities listed above.
- The two-disk inequality LC and its pair-sum consequence.
- LC strictly excludes the old saturated high-spectrum pseudo-point.
- The strengthened exact high-count bound (HC).
- The half-point satisfies mass, cap, evenness, every LC constraint, and every
  phase-free TriGram constraint while its Bell objective is greater than 10.
- Self-Fourier purity plus ConvMag excludes every such half-point exactly.

### DISPROVED

- The global implication (10.1) from mass, cap, evenness, and all LC
  constraints to Bell objective at most 10.
- Sufficiency of LC even after adding every magnitude-only TriGram inequality.

### NECESSARY-ONLY

- LC, the phase-sensitive `3 x 3` determinant inequalities, and twisted
  idempotence for physical characteristic coefficients.

### OPEN

- Whether mass, cap, LC, TriGram, self-Fourier purity, and ConvMag together
  certify 10 or admit a new exact fractional obstruction.
- A bounded phase-sensitive constraint if the strengthened magnitude
  relaxation still does not close.
- PW10 for the exact frozen tuple.
- The finite low-\(A\) gate and every downstream all-copy claim.

### CONJECTURED

- Nothing is promoted.

The first useful next target is therefore to test the strengthened global
magnitude relaxation containing (SF) and (ConvMag).  If it still fails, the
next target is an explicit phase-cycle or overlapping `4 x 4` orbit-Gram
compatibility condition, demonstrated on a finite label configuration rather
than merely listed at ambient scale.

<!-- END HISTORICAL FILE path=outputs/round-11-local-audit.md -->


# ROUND 012

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-12-prompt.md bytes=8220 sha256=332181139ed6630cc644a3650b3a018b70d9d515928bde9a16cecd13060d8c33 -->

# Round 12 — the LC-only implication is false; add exact global purity before using phases

Continue in the same conversation and the same canonically frozen finite
\(r=2\) low-\(A\) gate.  Give a public, self-contained derivation and no
hidden chain-of-thought.  Do not repeat the Round 8--11 narrative.

## Exact frozen boundary

Use exactly
\[
m=485165196,\qquad P=485165237=m+41,
\]
\[
D=941541228773064677=4P^2+1,
\qquad i=2P,
\qquad i^2=-1\pmod D,
\]
\[
0\le j\le P-42,
\qquad r_j=j^2\bmod P\text{ in }[0,P-1],
\qquad t_j=2Pj+r_j.
\]
Put
\[
a_j=(t_j,t_j^2),\qquad
A=\{a_j:0\le j\le P-42\},\qquad
\Gamma=(A-A)\setminus\{0\}.
\]
The ordered-difference map is injective, so
\[
M:=|\Gamma|=m(m-1)=235385266924553220.
\]

The open gate is
\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

With
\[
\alpha_z=\operatorname{Tr}(W_z^*|\psi\rangle\langle\psi|),
\qquad x_z=|\alpha_z|^2,
\]
the audited Bell--Fourier formula is
\[
\mathcal F_\Gamma(\psi)
=\frac1D\sum_z\lambda_zx_z,
\qquad
\lambda_z=\left|\sum_{a\in A}\omega^{[a,z]}\right|^2-m.
\tag{BF}
\]
Also
\[
\lambda_0=M,\qquad
\sum_z\lambda_z=0,\qquad
\sum_z\lambda_z^2=D^2M,
\tag{Mom}
\]
and every frozen isotropic line obeys
\[
|\Gamma\cap L|\le2,
\qquad
\frac1D\sum_{z\in L}\lambda_z=|\Gamma\cap L|.
\tag{Line}
\]

## Independently audited Round 11 contribution

The two overlapping \(3\times3\) orbit-Gram matrices correctly imply, for
every physical pure state and all labels \(g,h\),
\[
\boxed{
x_gx_h\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le(1-x_g)(1-x_h).
}
\tag{LC}
\]
Equivalently,
\[
x_g+x_h\le
\frac{2}{1+|\sin(\pi[g,h]/D)|}.
\]
LC excludes the old saturated \(D\)-point pseudo-weight.  It is a genuine
local contraction, but the global family contains on the order of \(D^4\)
ordered pair constraints; local matrix size is not the same as a small global
certificate.

## Exact correction: the implication left open in Round 11 is false

Let
\[
\mathcal B=\{z:\lambda_z>10\},\qquad b=|\mathcal B|.
\]
Keeping the Round 11 moment estimate quantitative gives
\[
\boxed{
b\ge
\left\lceil
\frac{D^2\bigl(M-10(m+10)\bigr)}
{M^2+(m+10)(M-10)}
\right\rceil
=3766165474002670825
=4D+558910412117.
}
\tag{HC}
\]

The high set is centrally symmetric and contains zero.  Choose any centrally
symmetric \(S\subset\mathcal B\) of size \(2D-1\) containing zero, and put
\[
x_0=1,\qquad
x_z=\frac12\ (z\in S\setminus\{0\}),\qquad
x_z=0\ (z\notin S).
\tag{Half}
\]
Then
\[
0\le x_z\le1,\qquad x_z=x_{-z},\qquad \sum_zx_z=D,
\]
and
\[
\frac1D\sum_z\lambda_zx_z>10.
\]
Nevertheless (Half) satisfies every LC inequality: two nonzero active weights
give at most \(\sin^2(\cdot)/4\le1/4\), and the only unit weight is at the
commuting zero label.  It also satisfies every phase-free \(3\times3\)
consequence
\[
x_z+x_w+x_{w-z}
\le1+2\sqrt{x_zx_wx_{w-z}}.
\tag{TriGram}
\]
Therefore the exact LC-only implication displayed as (10.1) in Round 11 is
**DISPROVED**.  This is a nonphysical relaxation point, not a PW10
counterexample.

## New exact global purity calculation to audit

There is a missing magnitude-only rank-one condition.  Weyl conjugation and
Hilbert--Schmidt Parseval appear to give
\[
\boxed{
x_u=\frac1D\sum_zx_z\omega^{[u,z]}
\quad\text{for every }u.
}
\tag{SF}
\]
A global sign in the character is harmless because \(x_z=x_{-z}\).  Audit
the convention, the factor \(D\), and the use of rank one.

For (Half), write
\[
x=\frac12\mathbf1_S+\frac12\delta_0.
\]
Then (SF) should be equivalent to
\[
\sum_{z\in S}\omega^{[u,z]}=
\begin{cases}
2D-1,&u=0,\\
D-1,&u\in S\setminus\{0\},\\
-1,&u\notin S.
\end{cases}
\tag{S-char}
\]
Thus \(T=S\setminus\{0\}\) is a regular partial difference set with
\[
\boxed{(v,k,\lambda,\mu)=(D^2,2(D-1),D-2,2).}
\tag{PDS}
\]

Taking absolute values in the already-audited twisted idempotence equation
appears to give another necessary condition:
\[
\boxed{
D\sqrt{x_k}\le\sum_h\sqrt{x_hx_{k-h}}
\quad\text{for every }k.
}
\tag{ConvMag}
\]
If a half-point satisfies (SF), then for every
\(k\in T\) the PDS parameter \(\lambda=D-2\) gives exactly
\[
|\{h\in S:k-h\in S\}|=D.
\]
The right side of ConvMag is therefore
\[
\sqrt2+\frac{D-2}{2},
\]
whereas the left side is \(D/\sqrt2\).  Their difference is
\[
\boxed{
\frac{D}{\sqrt2}-\left(\sqrt2+\frac{D-2}{2}\right)
=\frac{(\sqrt2-1)(D-2)}2>0.
}
\tag{Half-kill}
\]
Hence (SF) plus ConvMag should exclude **every** half-point, without any
classification theorem for the PDS and without assigning phases.  This is a
strictly stronger necessary relaxation, but still not a proof of PW10.

As a consistency check, the union of two distinct isotropic lines is an exact
solution of (S-char), yet it fails ConvMag as above.  Its frozen Bell objective
is at most
\[
\frac12\bigl(|\Gamma\cap L_1|+|\Gamma\cap L_2|\bigr)\le2.
\]

## Exact tasks

1. Give one verdict for PW10 on this exact frozen tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**.  A feasible point of a
   necessary relaxation is not a physical counterexample.

2. Audit every inequality and integer in (HC), including the ceiling.  Audit
   the construction (Half), its strict objective, its satisfaction of every
   LC and TriGram constraint, and the conclusion that Round 11 equation
   (10.1) is false.

3. Prove or correct (SF), (S-char), (PDS), ConvMag, and (Half-kill), including
   every Fourier normalization, sign, exceptional zero term, and ordered-pair
   count.  Explicitly distinguish:

   - LC-only relaxation failure;
   - exclusion of Half by the stronger necessary relaxation;
   - physical PW10, which remains separate.

4. Define the strengthened magnitude relaxation consisting of
   \[
   x_0=1,\quad x_z=x_{-z}\in[0,1],\quad\sum_zx_z=D,
   \]
   together with LC, TriGram, SF, and ConvMag.  Then make a checkable advance
   by doing one of the following:

   - prove that this strengthened relaxation forces
     \(D^{-1}\sum_z\lambda_zx_z\le10\) for the frozen spectrum;
   - give an explicit exact algebraic feasible point of this full relaxation
     with objective greater than 10; or
   - derive one additional necessary constraint, prove strict containment by
     applying it to an explicit feasible obstruction, and state its exact
     local dimension/degree and global indexing cost.

   Cardinality of \(\mathcal B\) alone is not enough to choose a structured
   support satisfying SF or ConvMag.  Do not silently assume that a subset of
   the high set is a subgroup, a line union, or a partial difference set.

5. Use the exact Fourier relation rather than merely renaming it.  In
   particular, audit
   \[
   \frac1D\sum_z\lambda_zx_z=\sum_{g\in\Gamma}x_g
   \tag{Exchange}
   \]
   under SF, and determine whether the PDS/additive representation constraints
   yield a frozen-tuple upper bound beyond the line tests.

6. If a phase-sensitive step is genuinely first after the strengthened
   magnitude relaxation, write an explicit overlapping \(4\times4\) Gram or
   finite phase-cycle constraint.  Specify all complex variables and Weyl
   phases, derive the determinant/minor inequality, and demonstrate strict
   separation on a concrete finite label configuration.  Merely listing all
   \(D^6\) four-vector constraints or restating the full twisted-idempotence
   system is not a smaller certificate.

7. Do not return to the five-carry arithmetic unless you produce an exact
   frozen collision, an actual uniform multiplicity proof, or a bounded-degree
   certificate with its solution count proved.  Do not repeat the degree-\(m\)
   resultant schema, Perron-Schur10, or an unnamed future SDP.

8. Do not discuss the all-\(T\) ratio or downstream theorem unless PW10 is
   first settled for this same tuple.

9. End with a plain audit ledger separating **PROVED**, **DISPROVED**,
   **NECESSARY-ONLY**, **SUFFICIENT-ONLY**, **OPEN**, and **CONJECTURED**.
   State the first new claim requiring independent verification.

The goal of this round is to move from pairwise orbit-Gram constraints to the
first exact global purity relaxation and either close it or break it with a
new explicit point.  Do not leave the already-disproved LC-only implication
listed as open.

<!-- END HISTORICAL FILE path=work/round-12-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-12-response.md bytes=19843 sha256=5c86b1287b7ee5b59aa3bb2197921a8e9bbac62ed25c78f5e87b311c4ab6f4ac -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The correction in the prompt is valid:

* the LC-only implication left open in Round 11 is false;
* every half-point of the form \((\mathrm{Half})\) is excluded once the exact self-Fourier identity and the magnitude convolution inequality are imposed;
* nevertheless, the strengthened magnitude relaxation consisting of SF, LC, TriGram, and ConvMag still does **not** imply the constant \(10\).

The last claim is proved below by an explicit frozen-spectrum algebraic point \(x^\star\) satisfying every one of those conditions while having

$$
\frac1D\sum_z\lambda_zx^\star_z>10.
$$

It is nonphysical: no compatible phases satisfying rank-one twisted idempotence are produced.

---

# 1. Quantitative audit of the high-spectrum cardinality

Let

$$
\mathcal B=\{z:\lambda_z>10\},
\qquad b=|\mathcal B|.
$$

Recall

$$
-m\le\lambda_z\le M,
\qquad
\sum_z\lambda_z=0,
\qquad
\sum_z\lambda_z^2=D^2M.
$$

Let

$$
P_+=\sum_{\lambda_z>0}\lambda_z.
$$

The negative eigenvalues have absolute total mass \(P_+\). Hence

$$
\sum_{\lambda_z<0}\lambda_z^2
\le mP_+.
$$

The positive eigenvalues at most \(10\) satisfy

$$
\lambda_z^2\le10\lambda_z,
$$

while the \(b\) eigenvalues larger than \(10\) satisfy the crude bound

$$
\lambda_z^2\le M^2.
$$

Therefore

$$
D^2M
\le
bM^2+(m+10)P_+.
\tag{1.1}
$$

Also,

$$
P_+
\le
bM+10(D^2-b)
=
10D^2+b(M-10).
\tag{1.2}
$$

Combining (1.1) and (1.2),

$$
D^2M
\le
10(m+10)D^2
+
b\left[M^2+(m+10)(M-10)\right].
$$

Thus

$$
\boxed{
b\ge
\left\lceil
\frac{D^2\bigl(M-10(m+10)\bigr)}
{M^2+(m+10)(M-10)}
\right\rceil.
}
\tag{1.3}
$$

For the exact integers in the prompt, the numerator and denominator are

$$
\begin{aligned}
N={}&
208669007871187211310981246345684810716589949716721640,\\
Q={}&
55406223999343909613327541199979660.
\end{aligned}
$$

Exact Euclidean division gives

$$
\begin{aligned}
N={}&
3766165474002670824\,Q\\
&+
283546726959779805433215241281800,
\end{aligned}
$$

with strictly positive remainder smaller than \(Q\). Hence

$$
\boxed{
b\ge3766165474002670825.
}
$$

Finally,

$$
4D+558910412117
=
3766165474002670825,
$$

so the integer in \((HC)\) is correct:

$$
\boxed{
b\ge4D+558910412117.
}
\tag{HC}
$$

---

# 2. The half-point refutes the LC-only implication

The high set \(\mathcal B\) is centrally symmetric and contains \(0\). Since

$$
b>2D-1,
$$

one may choose a centrally symmetric subset

$$
S\subset\mathcal B,
\qquad
|S|=2D-1,
\qquad
0\in S.
$$

Define

$$
x_0=1,
\qquad
x_z=\frac12\quad(z\in S\setminus\{0\}),
\qquad
x_z=0\quad(z\notin S).
$$

Then

$$
0\le x_z\le1,
\qquad
x_z=x_{-z},
$$

and

$$
\sum_zx_z
=
1+\frac{2D-2}{2}
=
D.
$$

Because every \(z\in S\) satisfies \(\lambda_z>10\),

$$
\begin{aligned}
\frac1D\sum_z\lambda_zx_z
&=
\frac1D
\left[
\lambda_0+
\frac12\sum_{z\in S\setminus\{0\}}\lambda_z
\right]\\
&>10.
\end{aligned}
\tag{2.1}
$$

## 2.1 LC

If \(g,h\ne0\) are both active, then \(x_g=x_h=1/2\), so

$$
x_gx_h
\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le\frac14
=
(1-x_g)(1-x_h).
$$

If either weight is zero, LC is immediate. If one label is \(0\), then its symplectic product with every label is zero, and both sides of LC vanish because \(x_0=1\).

Thus every LC inequality is satisfied.

## 2.2 TriGram

The phase-free \(3\times3\) condition is

$$
x_z+x_w+x_{w-z}
\le
1+2\sqrt{x_zx_wx_{w-z}}.
$$

If one of \(z,w,w-z\) is zero, the other two weights are equal and the inequality is an equality.

If none is zero, each of the three weights is \(0\) or \(1/2\):

* zero active weights: \(0\le1\);
* one active weight: \(1/2\le1\);
* two active weights: \(1\le1\);
* three active weights:

  $$
  \frac32
  \le
  1+\frac1{\sqrt2}.
  $$

Thus every TriGram inequality is satisfied.

Therefore the Round 11 implication based only on mass, symmetry, LC, and TriGram is disproved. The point is nonphysical.

---

# 3. Exact self-Fourier identity

Let

$$
\rho=|\psi\rangle\langle\psi|,
\qquad
\alpha_z=\operatorname{Tr}(W_z^*\rho),
\qquad
x_z=|\alpha_z|^2.
$$

For rank-one \(\rho\),

$$
x_u
=
\operatorname{Tr}(\rho W_u\rho W_u^*).
\tag{3.1}
$$

Weyl Parseval says that for arbitrary \(X,Y\),

$$
\operatorname{Tr}(X^*Y)
=
\frac1D
\sum_z
\overline{\operatorname{Tr}(W_z^*X)}
\operatorname{Tr}(W_z^*Y).
\tag{3.2}
$$

Apply this to

$$
X=\rho,
\qquad
Y=W_u\rho W_u^*.
$$

Since

$$
W_u^*W_z^*W_u
=
\omega^{[u,z]}W_z^*,
$$

the Weyl coefficient of \(Y\) is

$$
\operatorname{Tr}(W_z^*Y)
=
\omega^{[u,z]}\alpha_z.
$$

Substituting into (3.2),

$$
\boxed{
x_u
=
\frac1D\sum_zx_z\omega^{[u,z]}.
}
\tag{SF}
$$

The plus sign is correct for the displayed Weyl convention. Replacing it by a minus sign would be harmless because \(x_z=x_{-z}\).

Rank one is load-bearing in (3.1). For a mixed state, the overlap
\(\operatorname{Tr}(\rho W_u\rho W_u^*)\) need not equal
\(|\operatorname{Tr}(W_u^*\rho)|^2\).

At \(u=0\), SF gives

$$
\sum_zx_z=Dx_0=D.
$$

---

# 4. Half-points satisfying SF are partial difference sets

Write the half-point as

$$
x=\frac12\mathbf1_S+\frac12\delta_0.
$$

Substitution into SF gives

$$
\frac12\mathbf1_S(u)+\frac12\delta_{u,0}
=
\frac1{2D}
\left(
\sum_{z\in S}\omega^{[u,z]}+1
\right).
$$

Therefore

$$
\boxed{
\sum_{z\in S}\omega^{[u,z]}
=
\begin{cases}
2D-1,&u=0,\\
D-1,&u\in S\setminus\{0\},\\
-1,&u\notin S.
\end{cases}
}
\tag{S-char}
$$

Let

$$
T=S\setminus\{0\}.
$$

Then

$$
|T|=2D-2=2(D-1),
$$

and its character values are

$$
\sum_{z\in T}\omega^{[u,z]}
=
\begin{cases}
2(D-1),&u=0,\\
D-2,&u\in T,\\
-2,&u\notin S.
\end{cases}
\tag{4.1}
$$

Fourier inversion of the difference-counting function

$$
N_T(g)
=
|\{(a,b)\in T^2:a-b=g\}|
$$

then gives

$$
N_T(g)=
\begin{cases}
2(D-1),&g=0,\\
D-2,&g\in T,\\
2,&g\notin S.
\end{cases}
$$

Thus \(T\) is a regular partial difference set with

$$
\boxed{
(v,k,\lambda_{\rm PDS},\mu_{\rm PDS})
=
(D^2,\,2(D-1),\,D-2,\,2).
}
\tag{PDS}
$$

---

# 5. ConvMag excludes every half-point

The rank-one twisted-idempotence equation is

$$
\alpha_k
=
\frac1D
\sum_h
\alpha_h\alpha_{k-h}
\omega^{[h,k]/2}.
$$

Taking absolute values gives

$$
\boxed{
D\sqrt{x_k}
\le
\sum_h\sqrt{x_hx_{k-h}}.
}
\tag{ConvMag}
$$

Now assume a half-point satisfies SF, and let \(k\in T\).

There are exactly \(D\) labels \(h\in S\) for which \(k-h\in S\):

* \(h=0\);
* \(h=k\);
* \(D-2\) values with \(h,k-h\in T\), from the PDS parameter
  \(\lambda_{\rm PDS}=D-2\).

Therefore the right side of ConvMag is

$$
\frac1{\sqrt2}
+
\frac1{\sqrt2}
+
\frac{D-2}{2}
=
\sqrt2+\frac{D-2}{2}.
$$

The left side is

$$
D\sqrt{x_k}=\frac D{\sqrt2}.
$$

Their difference is

$$
\boxed{
\frac D{\sqrt2}
-
\left(\sqrt2+\frac{D-2}{2}\right)
=
\frac{(\sqrt2-1)(D-2)}2>0.
}
\tag{Half-kill}
$$

Thus every half-point satisfying SF violates ConvMag.

This excludes all half-points without classifying the associated partial difference sets.

## 5.1 Union of two lines

If \(S=L_1\cup L_2\) for two distinct isotropic lines, then

$$
\sum_{z\in S}\omega^{[u,z]}
=
D\mathbf1_{L_1}(u)+D\mathbf1_{L_2}(u)-1,
$$

so S-char holds exactly. This gives a concrete SF half-point.

It fails ConvMag by the preceding calculation. Its frozen Bell objective is nevertheless small:

$$
\sum_{g\in\Gamma}x_g
=
\frac12
\left(
|\Gamma\cap L_1|+|\Gamma\cap L_2|
\right)
\le2.
$$

---

# 6. Exact Fourier exchange

Under SF,

$$
\begin{aligned}
\frac1D\sum_z\lambda_zx_z
&=
\frac1D
\sum_z
\sum_{g\in\Gamma}
\omega^{[g,z]}x_z\\
&=
\sum_{g\in\Gamma}
\left[
\frac1D
\sum_zx_z\omega^{[g,z]}
\right]\\
&=
\boxed{
\sum_{g\in\Gamma}x_g.
}
\end{aligned}
\tag{Exchange}
$$

Thus the frozen Bell objective is exactly the \(x\)-mass placed on \(\Gamma\), once SF is imposed.

The PDS calculation controls only the special two-valued half-points. It does not give a comparable additive-representation theorem for a general fractional self-Fourier function.

---

# 7. The full strengthened magnitude relaxation still fails

Define the strengthened magnitude relaxation by

$$
x_0=1,\qquad
x_z=x_{-z}\in[0,1],
$$

together with SF, LC, TriGram, and ConvMag.

I now construct an exact algebraic feasible point of this entire relaxation whose frozen objective is \(>10\).

## 7.1 Normalized symplectic Fourier transform

For a real even function \(f\) on \(\mathbb F_D^2\), define

$$
(\mathscr Ff)(u)
=
\frac1D\sum_zf(z)\omega^{[u,z]}.
$$

Then

$$
\mathscr F^2f(u)=f(-u)=f(u).
$$

Let

$$
f=\mathbf1_\Gamma.
$$

Since \(\Gamma=-\Gamma\),

$$
\mathscr Ff=\frac{\lambda}{D},
\qquad
\mathscr F\!\left(\frac{\lambda}{D}\right)=f.
\tag{7.1}
$$

## 7.2 A strictly positive self-Fourier baseline

Define

$$
b_0=1,
\qquad
b_z=\frac1{D+1}\quad(z\ne0).
$$

Equivalently,

$$
b=
\frac D{D+1}\delta_0
+
\frac1{D+1}\mathbf1.
$$

Since

$$
\mathscr F\delta_0=\frac1D\mathbf1,
\qquad
\mathscr F\mathbf1=D\delta_0,
$$

one has

$$
\boxed{\mathscr Fb=b.}
\tag{7.2}
$$

Also

$$
\sum_zb_z=D.
$$

## 7.3 A frozen-spectrum self-Fourier direction

Set

$$
y=f+\frac{\lambda}{D}.
$$

By (7.1),

$$
\mathscr Fy=y.
$$

Since \(f(0)=0\) and \(\lambda_0=M\),

$$
y_0=\frac MD.
$$

Define

$$
d:=y-\frac MD\,b.
$$

Then

$$
\boxed{
\mathscr Fd=d,\qquad d_0=0,\qquad \sum_zd_z=0.
}
\tag{7.3}
$$

For \(z\ne0\),

$$
d_z
=
\mathbf1_\Gamma(z)
+
\frac{\lambda_z}{D}
-
\frac{M}{D(D+1)}.
\tag{7.4}
$$

Now set

$$
\boxed{
x_z^\star=b_z+\frac{20}{M}d_z.
}
\tag{7.5}
$$

This is an exact element of the real cyclotomic field generated by \(\omega\).

It satisfies

$$
x_0^\star=1,
\qquad
x_z^\star=x_{-z}^\star,
\qquad
\mathscr Fx^\star=x^\star,
\qquad
\sum_zx_z^\star=D.
$$

## 7.4 Positivity and the box constraint

The spectrum obeys

$$
-m\le\lambda_z\le M.
$$

For \(z\ne0\),

$$
d_z
\ge
-\frac mD-\frac{M}{D(D+1)}.
$$

Hence

$$
\boxed{
x_z^\star
\ge
\frac1{D+1}
\left[
1-
\frac{20(D+m)}{(m-1)D}
\right]
=:\beta.
}
\tag{7.6}
$$

Since \(D>m\),

$$
\frac{20(D+m)}{(m-1)D}
<
\frac{40}{m-1}<1,
$$

so \(\beta>0\).

For the upper bound,

$$
d_z\le1+\frac MD.
$$

The exact frozen dimensions satisfy

$$
D-4M=332m+6725>0,
$$

so \(M/D<1/4\). Therefore

$$
\begin{aligned}
x_z^\star
&\le
\frac1{D+1}
+
\frac{20}{M}
\left(1+\frac MD\right)\\
&<
\frac1{4M}+\frac{25}{M}\\
&=
\boxed{\frac{101}{4M}=:\delta.}
\end{aligned}
\tag{7.7}
$$

Since \(M>101\),

$$
0<\beta\le x_z^\star<\delta<\frac14<1
\qquad(z\ne0).
$$

Thus \(x^\star\) satisfies the full box constraint.

## 7.5 LC

If \(g,h\ne0\),

$$
x_g^\star x_h^\star
\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le\delta^2
<
(1-\delta)^2
\le
(1-x_g^\star)(1-x_h^\star).
$$

If either label is \(0\), its symplectic product is zero and LC holds with equality.

Thus every LC constraint is satisfied.

## 7.6 TriGram

If none of \(z,w,w-z\) is zero, then

$$
x_z^\star+x_w^\star+x_{w-z}^\star
<3\delta<1,
$$

while the right side of TriGram is at least \(1\).

If one label is zero, the other two weights agree by evenness, and TriGram is an equality.

Thus every TriGram constraint is satisfied.

## 7.7 ConvMag

For \(k=0\), evenness gives

$$
\sum_h\sqrt{x_h^\star x_{-h}^\star}
=
\sum_hx_h^\star
=
D
=
D\sqrt{x_0^\star}.
$$

Now take \(k\ne0\). Every term in the convolution sum is at least \(\beta\):

* if both factors are nonzero, their square-root product is at least \(\beta\);
* if one factor is \(x_0^\star=1\), the other is at least \(\beta\), and
  \(\sqrt{\beta}\ge\beta\).

Therefore

$$
\sum_h\sqrt{x_h^\star x_{k-h}^\star}
\ge D^2\beta.
\tag{7.8}
$$

Moreover,

$$
\frac{20(D+m)}{(m-1)D}
<
\frac{40}{m-1}
<
\frac14,
$$

and \(D/(D+1)>3/4\), so

$$
D\beta>\frac9{16}.
\tag{7.9}
$$

On the other hand,

$$
\sqrt{x_k^\star}<\sqrt\delta<\frac12.
$$

Thus

$$
D^2\beta
>
D\sqrt{x_k^\star}.
$$

Every ConvMag inequality is satisfied.

## 7.8 Frozen objective

Using Exchange,

$$
\frac1D\sum_z\lambda_zx_z^\star
=
\sum_{g\in\Gamma}x_g^\star.
$$

Now

$$
\sum_{g\in\Gamma}b_g=\frac{M}{D+1},
$$

and

$$
\begin{aligned}
\sum_{g\in\Gamma}d_g
&=
M+
\frac1D\sum_{g\in\Gamma}\lambda_g
-
\frac{M^2}{D(D+1)}\\
&\ge
M\left[
1-\frac mD-\frac{M}{D(D+1)}
\right].
\end{aligned}
$$

Here \(\lambda_g\ge-m\) was used. Since \(D>4m^2\) and \(D>4M\),

$$
\frac mD+\frac{M}{D(D+1)}<\frac12.
$$

Therefore

$$
\sum_{g\in\Gamma}d_g>\frac M2.
$$

Consequently,

$$
\begin{aligned}
\sum_{g\in\Gamma}x_g^\star
&=
\frac{M}{D+1}
+
\frac{20}{M}
\sum_{g\in\Gamma}d_g\\
&>
\frac{M}{D+1}+10\\
&>10.
\end{aligned}
\tag{7.10}
$$

Thus:

$$
\boxed{
\text{SF+LC+TriGram+ConvMag do not imply the constant }10.
}
$$

This \(x^\star\) is an exact frozen-spectrum feasible point of the entire strengthened magnitude relaxation. It is not shown to be physical.

---

# 8. The first phase-sensitive local constraint

The preceding obstruction shows that the next missing information must involve phases or an equivalent global rank condition.

Let

$$
\beta_z=\langle\psi|W_z|\psi\rangle.
$$

For labels \(g,h\), consider the four orbit vectors

$$
|\psi\rangle,\quad
W_g|\psi\rangle,\quad
W_h|\psi\rangle,\quad
W_{g+h}|\psi\rangle.
$$

Put

$$
\zeta=\omega^{[g,h]/2}.
$$

Their Gram matrix is

$$
\boxed{
G_4(g,h)=
\begin{pmatrix}
1&\beta_g&\beta_h&\beta_{g+h}\\
\overline{\beta_g}&1&
\overline\zeta\,\beta_{h-g}&
\overline\zeta\,\beta_h\\
\overline{\beta_h}&
\zeta\,\overline{\beta_{h-g}}&
1&
\zeta\,\beta_g\\
\overline{\beta_{g+h}}&
\zeta\,\overline{\beta_h}&
\overline\zeta\,\overline{\beta_g}&1
\end{pmatrix}
\succeq0.
}
\tag{8.1}
$$

This is an exact \(4\times4\) phase-cycle constraint.

## 8.1 Strict separation from all \(3\times3\) phase-free constraints

Choose the concrete labels

$$
g=(1,0),
\qquad
h=(0,2),
$$

so

$$
[g,h]=2,
\qquad
\zeta=\omega.
$$

Consider the local magnitude data

$$
|\beta_g|=|\beta_h|=\frac1{\sqrt2},
\qquad
\beta_{g+h}=\beta_{h-g}=0.
$$

Phases of \(\beta_g,\beta_h\) can be removed by diagonal unitary conjugation of the Gram matrix, so put

$$
\beta_g=\beta_h=r=\frac1{\sqrt2}.
$$

Then

$$
G_4=
\begin{pmatrix}
1&r&r&0\\
r&1&0&r\overline\zeta\\
r&0&1&r\zeta\\
0&r\zeta&r\overline\zeta&1
\end{pmatrix}.
$$

Every \(3\times3\) principal submatrix is positive semidefinite; its nontrivial determinant is

$$
1-2r^2=0.
$$

Thus all corresponding LC and TriGram conditions pass.

But direct expansion gives

$$
\det G_4
=
1-4r^2+4r^4\sin^2\!\left(\frac{2\pi}{D}\right).
$$

At \(r^2=1/2\),

$$
\boxed{
\det G_4
=
-\cos^2\!\left(\frac{2\pi}{D}\right)<0.
}
\tag{8.2}
$$

Hence \(4\times4\) orbit-Gram positivity is strictly stronger than the entire \(3\times3\) phase-free layer.

---

# 9. Even all small orbit-Gram constraints do not eliminate \(x^\star\)

The local \(4\times4\) constraint is genuinely stronger in general, but it does not remove the explicit obstruction \(x^\star\).

Choose the global phase assignment

$$
\beta_z^\star=\sqrt{x_z^\star}\in\mathbb R_{\ge0}.
$$

It satisfies

$$
\beta_{-z}^\star=\overline{\beta_z^\star}.
$$

For any \(N\) distinct orbit labels, every off-diagonal Gram entry has magnitude at most

$$
\sqrt\delta
<
\sqrt{\frac{101}{4M}}.
$$

Therefore every row has off-diagonal absolute sum at most

$$
(N-1)\sqrt\delta.
$$

Exact integer arithmetic gives

$$
101(96551482)^2
\le4M
<
101(96551483)^2,
$$

more precisely,

$$
4M-101(96551482)^2=11382184156,
$$

$$
101(96551483)^2-4M=8121215309.
$$

Consequently, whenever

$$
N\le96551483,
$$

one has

$$
(N-1)\sqrt\delta<1.
$$

Every such Hermitian orbit-Gram matrix is therefore strictly diagonally dominant with positive diagonal, and hence positive definite.

Thus the explicit magnitude obstruction \(x^\star\) survives not only every \(3\times3\) and \(4\times4\) orbit-Gram test, but every orbit-Gram positivity test involving as many as

$$
\boxed{96551483}
$$

distinct orbit vectors, for this explicit global phase assignment.

The failure of physicality, if it occurs, is consequently genuinely global. It must use the full twisted-idempotence/rank structure rather than a fixed small Gram minor.

---

# 10. Precise remaining gap

The strengthened magnitude relaxation has now been explicitly broken:

$$
\boxed{
\begin{gathered}
x_0=1,\quad
x_z=x_{-z}\in[0,1],\quad
\sum_zx_z=D,\\
\text{SF, LC, TriGram, and ConvMag}
\end{gathered}
}
$$

do not imply

$$
\frac1D\sum_z\lambda_zx_z\le10.
$$

The exact point \(x^\star\) has objective \(>10\).

To turn it into a physical counterexample, one would need phases
\(\theta_z\) such that

$$
\alpha_z=\sqrt{x_z^\star}\,e^{i\theta_z}
$$

satisfies

$$
\alpha_0=1,\qquad
\alpha_{-z}=\overline{\alpha_z},
$$

and the rank-one equations

$$
\boxed{
\alpha_k
=
\frac1D
\sum_h
\alpha_h\alpha_{k-h}
\omega^{[h,k]/2}
\quad\forall k.
}
\tag{10.1}
$$

No such phase lift is produced.

Conversely, no theorem is proved showing that every phase lift with the frozen objective \(>10\) is impossible.

The first unresolved issue is therefore a global phase/rank implication:

> Determine whether a self-Fourier magnitude profile satisfying all currently proved magnitude constraints and having frozen \(\Gamma\)-mass \(>10\) can admit a rank-one twisted-convolution phase lift.

The explicit obstruction survives all fixed local Gram tests through dimension \(96{,}551{,}483\). A completion must therefore use a substantially global consequence of rank one, not merely another fixed-size orbit-Gram minor.

PW10 itself remains open.

---

# Audit ledger

## PROVED

* The quantitative cardinality estimate

  $$
  |\{z:\lambda_z>10\}|
  \ge3766165474002670825
  =
  4D+558910412117.
  $$
* The exact Euclidean division establishing the ceiling.
* Existence of a centrally symmetric high-spectrum set of size \(2D-1\).
* The Half point has Bell objective strictly larger than \(10\).
* Half satisfies every LC and TriGram inequality.
* The LC-only implication from Round 11 is false.
* The rank-one self-Fourier identity

  $$
  x_u=D^{-1}\sum_zx_z\omega^{[u,z]}.
  $$
* S-char and the regular partial-difference-set parameters

  $$
  (D^2,2(D-1),D-2,2).
  $$
* ConvMag.
* ConvMag excludes every SF half-point by the exact Half-kill gap.
* The union of two isotropic lines satisfies S-char but fails ConvMag.
* The exact Exchange identity

  $$
  D^{-1}\sum_z\lambda_zx_z=\sum_{g\in\Gamma}x_g.
  $$
* The explicit frozen-spectrum algebraic point \(x^\star\).
* \(x^\star\) satisfies the box constraints, SF, LC, TriGram, and ConvMag.
* \(x^\star\) has frozen objective strictly greater than \(10\).
* The strengthened magnitude relaxation is therefore insufficient.
* The exact \(4\times4\) orbit-Gram matrix (8.1).
* A concrete four-label configuration passes every \(3\times3\) principal test but has negative \(4\times4\) determinant.
* The point \(x^\star\) admits a phase assignment for which every orbit-Gram matrix on at most \(96{,}551{,}483\) distinct labels is positive definite.

## DISPROVED

* The LC-only implication displayed as Round 11 equation (10.1).
* Sufficiency of LC plus TriGram.
* Sufficiency of SF, LC, TriGram, and ConvMag together.
* Physicality of every SF half-point.
* Sufficiency of all fixed small orbit-Gram constraints for eliminating the explicit magnitude obstruction.

## NECESSARY-ONLY

* SF.
* LC.
* TriGram.
* ConvMag.
* S-char and the PDS conditions within the Half ansatz.
* Every finite orbit-Gram positivity condition.
* The full twisted-idempotence equations.

## SUFFICIENT-ONLY

* No new frozen-tuple sufficient condition for PW10 is proved.

## OPEN

* Whether the explicit magnitude obstruction \(x^\star\) has a rank-one phase lift.
* Whether some other magnitude profile with objective \(>10\) has a physical phase lift.
* Whether global rank-one twisted idempotence forces the frozen objective to be at most \(10\).
* PW10 for the canonically frozen tuple.

## CONJECTURED

* No statement is promoted to conjectured status.

The first new claim requiring independent verification is the explicit self-Fourier perturbation \(x^\star\) in (7.5), including its simultaneous satisfaction of SF, LC, TriGram, and ConvMag and its strict frozen objective \(>10\).

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-12-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-12-local-audit.md bytes=5411 sha256=630c9d472261842af50384c18aac3604c017f530abced8af6b32d8ed1a649777 -->

# Round 12 local audit

- Audit completed (UTC): `2026-09-13T00:54:11Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=m(m-1)=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-12-response.md`
- Web response SHA-256:
  `5c86b1287b7ee5b59aa3bb2197921a8e9bbac62ed25c78f5e87b311c4ab6f4ac`
- Capture equality: the artifact and output copies are byte-identical,
  each `19,843` bytes and `1,313` lines.

## Verdict

The Round 12 web response passes the independent checks below.  Its logically
correct conclusion is still

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN.}}
\]

Round 12 does not produce a physical state with objective above `10`, and it
does not prove the uniform physical upper bound.  It instead proves that the
strengthened magnitude relaxation `SF + LC + TriGram + ConvMag` is
insufficient.

## Independently verified claims

### 1. High-spectrum count

The displayed numerator and denominator are exact:

\[
N=208669007871187211310981246345684810716589949716721640,
\]
\[
Q=55406223999343909613327541199979660.
\]

The Euclidean division is also exact:

\[
N=3766165474002670824\,Q
+283546726959779805433215241281800,
\]

with remainder strictly between `0` and `Q`.  Therefore

\[
b\ge3766165474002670825=4D+558910412117.
\]

### 2. Half-point obstruction and its removal

The centrally symmetric half-point has mass exactly `D`, frozen objective
strictly above `10`, and satisfies every LC and TriGram case.  Hence the
Round 11 LC-only implication is false.

For a rank-one state, the factor and sign in

\[
x_u=\frac1D\sum_zx_z\omega^{[u,z]}
\]

are correct.  Within the half-point ansatz, Fourier inversion gives the
regular partial-difference-set parameters

\[
(D^2,2(D-1),D-2,2).
\]

ConvMag then fails by the exact positive gap

\[
\frac{(\sqrt2-1)(D-2)}2.
\]

Thus SF plus ConvMag excludes every such half-point; this is a necessary-state
argument, not a classification assumption.

### 3. The `20/M` self-Fourier perturbation

The dimension identity used in the response is exact:

\[
D-4M=332m+6725>0.
\]

For the web response's point

\[
x^\star=b+\frac{20}{M}d,
\]

the displayed lower bound `beta` is positive and the displayed upper bound

\[
x_z^\star<\delta=\frac{101}{4M}<\frac14
\qquad(z\ne0)
\]

is valid.  These bounds suffice for every LC and TriGram inequality.  They
also make the ConvMag proof valid: the convolution contains `D^2` terms, each
at least `beta`, including the two terms incident to the zero label because
`sqrt(beta) >= beta`.

The exact lower bound used for the frozen objective is approximately

\[
20.249999946925300>10.
\]

This verifies relaxation feasibility only.  No phase lift is supplied.

### 4. Four-vector Weyl-orbit Gram matrix

Starting from

\[
G(a,b)=\omega^{-[a,b]/2}\beta_{b-a},
\]

the six upper-triangular entries in the response's matrix (8.1) have the
correct Weyl phases.  For its example with
`beta_g=beta_h=r`, `beta_{g+h}=beta_{h-g}=0`, and
`zeta=exp(i theta)`, direct determinant expansion gives

\[
\det G_4
=1-4r^2+r^4(2-\zeta^2-\zeta^{-2})
=1-4r^2+4r^4\sin^2\theta.
\]

All four `3 x 3` principal determinants are `1-2r^2`.  At
`r^2=1/2` they vanish, while

\[
\det G_4=-\cos^2(2\pi/D)<0.
\]

So the local `4 x 4` phase-cycle constraint is genuinely stronger than its
`3 x 3` principal constraints.  This is a local constraint separation, not a
physical global ambiguity function.

### 5. Small-Gram survival bound

The response's exact integer comparisons are correct:

\[
4M-101(96551482)^2=11382184156>0,
\]
\[
101(96551483)^2-4M=8121215309>0.
\]

With the globally consistent trial phases
`beta_z^star=sqrt(x_z^star)`, every candidate orbit-Gram matrix on at most
`96,551,483` distinct labels is therefore strictly diagonally dominant and
positive definite.  This does not prove physicality; it proves that bounded
local Gram positivity through that size cannot reject this point.

## Stronger local refinement prepared for Round 13

Using the same exact self-Fourier direction but the smaller perturbation

\[
x=b+\frac{10}{M}d,
\]

gives the rigorous objective lower bound

\[
\frac{M}{D+1}
+10\left(1-\frac mD-\frac{M}{D(D+1)}\right)
=10+\frac{m((m-11)D-10m)}{D(D+1)}
>10,
\]

numerically `10.249999952078184...`.  Its nonzero entries obey

\[
\frac1{2(D+1)}\le x_z\le
U:=\frac1{D+1}+\frac{10}{M}+\frac{10}{D}<\frac1{16}.
\]

Exact square comparison yields

\[
(135873434)^2U<1<(135873435)^2U.
\]

Thus this sharper obstruction survives every orbit-Gram PSD test on at most
`135,873,435` distinct labels under the same real phase assignment.

## Earliest remaining gap

The next valid advance must use a genuinely global consequence of rank one:
either construct phases satisfying the full twisted-idempotence equations for
an objective-above-`10` profile, or prove that no such phase lift can exist.
Neither another magnitude-only inequality already implied by the audited
constraints nor a modest fixed-size Gram minor closes PW10.

## Reproducibility

- `work/verify_round12_web_response.py`
  SHA-256 `9306d200d24228e8b1deb0a96b75f18f7a439ee0271b292678472c038a50a61c`
- `work/verify_round13_smoothed_obstruction.py`
  SHA-256 `65c62f9f550dfd2dc35d716de6ca3441b939bfd3363978aea5b317180f56604d`
- `work/round-13-independent-derivations.md`
  SHA-256 `3c305b898df728c478319426000f667855d475ffda126476c9d32142664cfd01`

Both exact checkers print `PASS`.

<!-- END HISTORICAL FILE path=outputs/round-12-local-audit.md -->


# ROUND 013

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-13-prompt.md bytes=8919 sha256=9bb2ce765128313641e6e39b9cc622c128f8d0050809e23227a5d5b60ad145e1 -->

# Round 13 — audit the sharper obstruction and compress the global phase-lift gate

Continue in the same conversation and the same canonically frozen finite
`r=2`, low-`A` gate.  Give a public, self-contained derivation and no hidden
chain-of-thought.  Do not repeat the Round 8--12 narrative.  Every assertion
must be tied to the exact frozen tuple below.

## Exact frozen boundary

Use exactly
\[
m=485165196,\qquad P=485165237=m+41,
\]
\[
D=941541228773064677=4P^2+1,
\qquad i=2P,
\qquad i^2=-1\pmod D,
\]
\[
0\le j\le P-42,
\qquad r_j=j^2\bmod P\text{ in }[0,P-1],
\qquad t_j=2Pj+r_j,
\]
\[
a_j=(t_j,t_j^2),\qquad
A=\{a_j:0\le j\le P-42\},\qquad
\Gamma=(A-A)\setminus\{0\}.
\]
The ordered-difference map is injective, so
\[
M:=|\Gamma|=m(m-1)=235385266924553220.
\]

The open gate is
\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use the fixed odd-dimensional Weyl convention
\[
W_uW_v=\omega^{[u,v]/2}W_{u+v},
\qquad W_u^*=W_{-u}.
\]
For a pure state put
\[
\alpha_z=\operatorname{Tr}(W_z^*|\psi\rangle\langle\psi|),
\qquad x_z=|\alpha_z|^2.
\]
The audited formulas are
\[
\mathcal F_\Gamma(\psi)
=\frac1D\sum_z\lambda_zx_z,
\qquad
\lambda_z=\left|\sum_{a\in A}\omega^{[a,z]}\right|^2-m,
\tag{BF}
\]
\[
\lambda_0=M,
\quad -m\le\lambda_z\le M,
\quad \sum_z\lambda_z=0,
\quad \sum_z\lambda_z^2=D^2M.
\tag{Mom}
\]

## Audited Round 12 boundary

Round 12 correctly established all of the following.

1. The high-spectrum set has
   \[
   |\{z:\lambda_z>10\}|
   \ge3766165474002670825
   =4D+558910412117.
   \]

2. The centrally symmetric half-point refutes the former LC-only implication,
   but every self-Fourier half-point is excluded by ConvMag.  The exact
   Half-kill gap is
   \[
   \frac{(\sqrt2-1)(D-2)}2>0.
   \]

3. Every physical magnitude profile obeys
   \[
   x_u=\frac1D\sum_zx_z\omega^{[u,z]}
   \tag{SF}
   \]
   and
   \[
   D\sqrt{x_k}\le\sum_h\sqrt{x_hx_{k-h}}.
   \tag{ConvMag}
   \]

4. `SF + LC + TriGram + ConvMag` still does not force the bound `10`.
   Round 12 gave an exact full-support self-Fourier magnitude point using
   perturbation `20/M`.  It is not physical because no compatible phases or
   rank-one operator were produced.

5. The displayed `4 x 4` Weyl-orbit Gram matrix and its strict local
   separation from its four `3 x 3` principal constraints are correct.  The
   `20/M` point, with the real trial phases, nevertheless survives every
   orbit-Gram PSD test on at most `96,551,483` distinct labels.

Therefore PW10 remains open.  A feasible magnitude point is not a physical
counterexample.

## Sharper exact obstruction to audit

Use the normalized symplectic Fourier transform
\[
(\mathscr Ff)(u)=\frac1D\sum_zf(z)\omega^{[u,z]}.
\]
Let
\[
b_0=1,
\qquad b_z=\frac1{D+1}\quad(z\ne0),
\]
\[
y=\mathbf1_\Gamma+\frac\lambda D,
\qquad
d=y-\frac MD b,
\qquad
\boxed{x^{(10)}=b+\frac{10}{M}d.}
\tag{X10}
\]
Because `Gamma=-Gamma`, the proposed exact identities are
\[
\mathscr Fb=b,
\qquad \mathscr Fy=y,
\qquad \mathscr Fd=d,
\qquad d_0=0,
\]
and hence
\[
x^{(10)}_0=1,
\quad x^{(10)}_z=x^{(10)}_{-z},
\quad \mathscr Fx^{(10)}=x^{(10)},
\quad \sum_zx^{(10)}_z=D.
\]

For every nonzero `z`, exact frozen arithmetic gives
\[
\boxed{
\frac1{2(D+1)}\le x^{(10)}_z\le
U:=\frac1{D+1}+\frac{10}{M}+\frac{10}{D}<\frac1{16}.
}
\tag{Bounds10}
\]
These bounds should imply every LC, TriGram, and ConvMag constraint, with the
zero-label cases treated separately.

Exchange gives the proposed objective lower bound
\[
\begin{aligned}
\frac1D\sum_z\lambda_zx^{(10)}_z
&=\sum_{g\in\Gamma}x^{(10)}_g\\
&\ge\frac{M}{D+1}
+10\left(1-\frac mD-\frac{M}{D(D+1)}\right)\\
&=10+\frac{m((m-11)D-10m)}{D(D+1)}\\
&>10.
\end{aligned}
\tag{Obj10}
\]
The displayed lower bound is approximately `10.249999952078184`.

For the real trial phases
\[
\beta_z=\sqrt{x^{(10)}_z}\in\mathbb R_{\ge0},
\]
exact reduction of `U` gives numerator and denominator
\[
U=
\frac{94190609356686178298989929062516930}
{1738908434768135059241251074769290641999621851114161}.
\]
The proposed exact square gaps are
\[
\operatorname{den}(U)
-(135873434)^2\operatorname{num}(U)
=16668547867312617600534570541272542097727081>0,
\]
\[
(135873435)^2\operatorname{num}(U)
-\operatorname{den}(U)
=8927455314568955567791688543998538889265089>0.
\]
Thus this point should survive every orbit-Gram PSD test on at most
\[
\boxed{135873435}
\]
distinct labels under the same globally consistent real phase assignment.
Audit every factor, inequality, exceptional case, and integer.  Do not call
`x^(10)` physical.

## Candidate exact compression of the global phase gate

The next issue is not another modest fixed-size minor.  Audit the following
candidate theorem from first principles.

Take any coefficient field satisfying
\[
\alpha_0=1,
\qquad \alpha_{-z}=\overline{\alpha_z},
\qquad \sum_z|\alpha_z|^2=D,
\]
and reconstruct the Hermitian operator
\[
R_\alpha:=\frac1D\sum_z\alpha_zW_z.
\tag{R}
\]
Then
\[
\operatorname{Tr}R_\alpha=1,
\qquad \operatorname{Tr}R_\alpha^2=1.
\]

For all `a,b` in `F_D^2`, define the full twisted orbit matrix
\[
G_\alpha(a,b)
=\operatorname{Tr}(R_\alpha W_a^*W_b)
=\omega^{-[a,b]/2}\,\overline{\alpha_{b-a}}.
\tag{FullG}
\]
Check the conjugation in the last expression carefully.  In the orthonormal
Hilbert--Schmidt Weyl basis `W_a/sqrt(D)`, `G_alpha/D` appears to be the matrix
of right multiplication `X -> X R_alpha`.  If so, prove or correct
\[
\boxed{
\operatorname{spec}(G_\alpha)
=\{D\mu_j(R_\alpha):1\le j\le D\},
\text{ each repeated }D,
}
\tag{SpecG}
\]
and
\[
G_\alpha\succeq0
\iff R_\alpha\succeq0,
\qquad
\operatorname{rank}G_\alpha=D\operatorname{rank}R_\alpha.
\]

There is also a proposed scalar compression.  Direct Weyl multiplication
should give the real cubic phase functional
\[
\boxed{
C(\alpha):=\operatorname{Tr}(R_\alpha^3)
=\frac1{D^2}\sum_{u,v}
\alpha_u\alpha_v\alpha_{-u-v}
\omega^{[u,v]/2}.
}
\tag{Cubic}
\]
Because `Tr(R_alpha^2)=1`, every eigenvalue of `R_alpha` lies in `[-1,1]`, so
`I-R_alpha` is positive semidefinite.  Audit the proposed identity and
rigidity statement
\[
\boxed{
1-C(\alpha)
=\operatorname{Tr}\bigl(R_\alpha^2(I-R_\alpha)\bigr)\ge0,
}
\tag{Defect}
\]
with equality if and only if `R_alpha` is a rank-one orthogonal projector.
If correct, then under the three coefficient constraints above the following
are equivalent:

- `alpha` is the Weyl coefficient field of a pure state;
- twisted idempotence holds;
- `R_alpha` is positive semidefinite;
- the full matrix `G_alpha` is positive semidefinite;
- `C(alpha)=1`.

Track `alpha` versus `beta=<psi|W_z|psi>` and all conjugations exactly.  A
normalization or conjugation error invalidates the theorem.

## Exact tasks

1. Give one verdict for PW10 on the exact frozen tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**.

2. Audit `(X10)`, `(Bounds10)`, `(Obj10)`, the exact rational `U`, both square
   gaps, and the `135,873,435` diagonal-dominance conclusion.  Separate
   magnitude-relaxation feasibility from physical realizability.

3. Prove or correct `(FullG)`, `(SpecG)`, `(Cubic)`, and `(Defect)`.  State the
   exact matrix dimension, number of cubic summands, and global indexing cost.
   Explain whether the cubic equality is truly sufficient under the displayed
   Hermiticity, trace, and purity hypotheses.

4. Apply the global criterion to the actual frozen point `x^(10)`.  Seek, in
   this order:

   - compatible phases with `C(alpha)=1`, which would give a physical PW10
     counterexample;
   - a rigorous phase-uniform gap `C(alpha)<=1-eta` with an explicit positive
     `eta`, which would exclude `x^(10)`;
   - an exact phase-sensitive consequence of `(Defect)` that strictly cuts
     `x^(10)` or another explicit frozen-objective-above-`10` obstruction.

   If none is proved, say so.  Merely proposing a numerical phase search,
   writing an unnamed SDP, or restating all twisted-idempotence equations is
   not a solution.

5. A proof that only the all-real trial phase fails does not exclude other
   phases.  Conversely, local Gram positivity below the audited threshold
   does not establish a full phase lift.  Keep these quantifiers explicit.

6. Do not return to five-carry arithmetic, the degree-`m` resultant schema,
   Perron--Schur10, or the all-`T` ratio unless you produce a completed exact
   certificate for this same frozen tuple.

7. End with a plain audit ledger separating **PROVED**, **DISPROVED**,
   **NECESSARY-ONLY**, **SUFFICIENT-ONLY**, **EQUIVALENT**, **OPEN**, and
   **CONJECTURED**.  State the first new claim requiring independent
   verification.

The goal of this round is to replace an enormous collection of small local
tests by an exact, convention-safe global phase-lift criterion, then use that
criterion on the sharper full-support obstruction.  Do not promote a phase
optimization formulation into a solution of PW10.

<!-- END HISTORICAL FILE path=work/round-13-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-13-response.md bytes=19279 sha256=d486ae66f47714c322a2f6694fbbdf81665d53b582021780175312777a4663fe -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The sharper point \(x^{(10)}\) is an exact feasible point of the full magnitude relaxation:

$$
\text{SF}+\text{LC}+\text{TriGram}+\text{ConvMag},
$$

and its frozen objective is rigorously larger than \(10\). With the globally consistent real trial phases, it passes every orbit-Gram positive-semidefiniteness test on at most

$$
135\,873\,435
$$

distinct labels.

The proposed global phase-lift theorem is also correct. Under

$$
\alpha_0=1,\qquad
\alpha_{-z}=\overline{\alpha_z},\qquad
\sum_z|\alpha_z|^2=D,
$$

all of the following are equivalent:

$$
\begin{aligned}
&\alpha\text{ is the Weyl coefficient field of a pure state},\\
&R_\alpha^2=R_\alpha,\\
&R_\alpha\succeq0,\\
&G_\alpha\succeq0,\\
&C(\alpha)=1.
\end{aligned}
$$

Thus physical phase lifting of \(x^{(10)}\) is compressed exactly to whether a single cubic phase functional reaches its universal upper bound \(1\). However, that cubic still contains \(D^4\) indexed terms and depends on \((D^2-1)/2\) independent phases. No compatible phases, no phase-uniform positive gap, and no further exact inequality excluding \(x^{(10)}\) are proved here.

---

# 1. The normalized symplectic Fourier transform

Let

$$
(\mathscr Ff)(u)=\frac1D\sum_zf(z)\omega^{[u,z]}.
$$

Because the pairing is alternating,

$$
\mathscr F^2f=f
$$

with this same-sign convention. Indeed,

$$
\frac1{D^2}\sum_z\omega^{[u,z]+[z,v]}
=
\frac1{D^2}\sum_z\omega^{[u-v,z]}
=
\delta_{u,v}.
$$

Let \(f=\mathbf 1_\Gamma\). Since \(\Gamma=-\Gamma\),

$$
\begin{aligned}
(\mathscr Ff)(u)
&=\frac1D\sum_{g\in\Gamma}\omega^{[u,g]}\\
&=\frac1D\sum_{g\in\Gamma}\omega^{[g,u]}\\
&=\frac{\lambda_u}{D}.
\end{aligned}
\tag{1.1}
$$

The middle equality uses the substitution \(g\mapsto-g\). Therefore

$$
\boxed{
\mathscr F\mathbf1_\Gamma=\frac{\lambda}{D},
\qquad
\mathscr F\!\left(\frac{\lambda}{D}\right)=\mathbf1_\Gamma.
}
\tag{1.2}
$$

Now write

$$
b=\frac D{D+1}\delta_0+\frac1{D+1}\mathbf1.
$$

Since

$$
\mathscr F\delta_0=\frac1D\mathbf1,
\qquad
\mathscr F\mathbf1=D\delta_0,
$$

one has

$$
\boxed{\mathscr Fb=b.}
\tag{1.3}
$$

Define

$$
y=\mathbf1_\Gamma+\frac{\lambda}{D},
\qquad
d=y-\frac MD\,b,
$$

and

$$
x^{(10)}=b+\frac{10}{M}d.
$$

Equations (1.2)–(1.3) give

$$
\boxed{
\mathscr Fy=y,\qquad
\mathscr Fd=d,\qquad
\mathscr Fx^{(10)}=x^{(10)}.
}
\tag{1.4}
$$

At the zero label,

$$
y_0=\frac MD,\qquad b_0=1,
$$

so

$$
d_0=0,\qquad x^{(10)}_0=1.
$$

Furthermore,

$$
\sum_zd_z=D(\mathscr Fd)(0)=Dd_0=0,
$$

and hence

$$
\boxed{\sum_zx^{(10)}_z=D.}
\tag{1.5}
$$

All functions involved are real and even, so

$$
x^{(10)}_z=x^{(10)}_{-z}.
$$

---

# 2. Exact pointwise bounds for \(x^{(10)}\)

For \(z\ne0\),

$$
d_z
=
\mathbf1_\Gamma(z)
+\frac{\lambda_z}{D}
-\frac{M}{D(D+1)}.
$$

Thus

$$
\boxed{
x^{(10)}_z
=
\frac1{D+1}
+
\frac{10}{M}
\left[
\mathbf1_\Gamma(z)
+\frac{\lambda_z}{D}
-\frac{M}{D(D+1)}
\right].
}
\tag{2.1}
$$

## 2.1 Lower bound

Using

$$
\mathbf1_\Gamma(z)\ge0,\qquad \lambda_z\ge-m,
$$

and \(M=m(m-1)\),

$$
x^{(10)}_z
\ge
\frac1{D+1}
-\frac{10}{(m-1)D}
-\frac{10}{D(D+1)}.
$$

Subtracting \(1/[2(D+1)]\) gives

$$
\begin{aligned}
&\frac1{D+1}
-\frac{10}{(m-1)D}
-\frac{10}{D(D+1)}
-\frac1{2(D+1)}
\\
&\qquad=
\frac{D(m-21)-20m}
{2D(D+1)(m-1)}.
\end{aligned}
\tag{2.2}
$$

For the exact frozen integers, the numerator is

$$
D(m-21)-20m
=
456803015027398949599719555>0.
$$

Therefore

$$
\boxed{
x^{(10)}_z\ge\frac1{2(D+1)}
\qquad(z\ne0).
}
\tag{2.3}
$$

## 2.2 Upper bound

Using

$$
\mathbf1_\Gamma(z)\le1,\qquad \lambda_z\le M,
$$

one gets

$$
x^{(10)}_z
\le
\frac1{D+1}
+\frac{10}{M}
+\frac{10}{D}
-\frac{10}{D(D+1)}
<
U,
$$

where

$$
\boxed{
U=
\frac1{D+1}+\frac{10}{M}+\frac{10}{D}.
}
\tag{2.4}
$$

In lowest terms,

$$
\boxed{
U=
\frac{
94190609356686178298989929062516930
}{
1738908434768135059241251074769290641999621851114161
}.
}
\tag{2.5}
$$

The exact comparison with \(1/16\) is

$$
\begin{aligned}
&1738908434768135059241251074769290641999621851114161\\
&\quad
-16\cdot94190609356686178298989929062516930\\
&=
1738908434768133552191501367790437858160756850843281>0.
\end{aligned}
$$

Hence

$$
\boxed{
0<x^{(10)}_z<U<\frac1{16}
\qquad(z\ne0).
}
\tag{2.6}
$$

This verifies all of \((\mathrm{Bounds10})\).

---

# 3. The magnitude constraints

## 3.1 LC

If \(g,h\ne0\), then

$$
x_gx_h\sin^2\!\left(\frac{\pi[g,h]}D\right)
\le U^2,
$$

whereas

$$
(1-x_g)(1-x_h)\ge(1-U)^2.
$$

Since \(U<1/2\),

$$
U^2<(1-U)^2.
$$

If one label is zero, its symplectic product with the other label is zero, while \(x_0=1\), so both sides of LC vanish. Thus every LC inequality holds.

## 3.2 TriGram

If \(z,w,w-z\) are all nonzero,

$$
x_z+x_w+x_{w-z}\le3U<\frac3{16}<1,
$$

while the right side of TriGram is at least \(1\).

If one of \(z,w,w-z\) is zero, the other two weights are equal by evenness. For example, when \(z=0\),

$$
1+2x_w
=
1+2\sqrt{1\cdot x_w\cdot x_w}.
$$

Thus every exceptional zero-label case is an equality, and all TriGram inequalities hold.

## 3.3 ConvMag

For \(k=0\),

$$
\sum_h\sqrt{x_hx_{-h}}
=
\sum_hx_h
=
D
=
D\sqrt{x_0}.
$$

Now let \(k\ne0\). Every summand satisfies

$$
\sqrt{x_hx_{k-h}}\ge\frac1{2(D+1)}.
$$

For \(h=0\) or \(h=k\), this follows from

$$
\sqrt{x_k}\ge\sqrt{\frac1{2(D+1)}}>
\frac1{2(D+1)}.
$$

Hence

$$
\sum_h\sqrt{x_hx_{k-h}}
\ge
\frac{D^2}{2(D+1)}.
\tag{3.1}
$$

On the other hand,

$$
D\sqrt{x_k}
<
D\sqrt U
<
\frac D4,
$$

whereas

$$
\frac{D^2}{2(D+1)}>\frac D4.
$$

Therefore every nonzero-\(k\) ConvMag inequality holds strictly.

Thus \(x^{(10)}\) satisfies

$$
\boxed{\text{SF}+\text{LC}+\text{TriGram}+\text{ConvMag}.}
$$

---

# 4. The exact frozen objective

Because \(x^{(10)}\) is self-Fourier, Exchange gives

$$
\frac1D\sum_z\lambda_zx^{(10)}_z
=
\sum_{g\in\Gamma}x^{(10)}_g.
$$

Now

$$
\sum_{g\in\Gamma}b_g=\frac{M}{D+1}
$$

and

$$
\begin{aligned}
\sum_{g\in\Gamma}d_g
&=
M+\frac1D\sum_{g\in\Gamma}\lambda_g
-\frac{M^2}{D(D+1)}\\
&\ge
M-\frac{mM}{D}
-\frac{M^2}{D(D+1)}.
\end{aligned}
$$

Therefore

$$
\begin{aligned}
\frac1D\sum_z\lambda_zx^{(10)}_z
&\ge
\frac{M}{D+1}
+
10\left(
1-\frac mD-\frac{M}{D(D+1)}
\right)\\
&=
\boxed{
10+
\frac{m\bigl((m-11)D-10m\bigr)}
{D(D+1)}.
}
\end{aligned}
\tag{4.1}
$$

The excess over \(10\) is exactly

$$
\boxed{
\frac{
3357953467987716774306702559357710
}{
13431816446658977517442074781790591
}>0.
}
\tag{4.2}
$$

Numerically, the lower bound is

$$
\boxed{10.249999952078184\ldots}
$$

Thus \(x^{(10)}\) is an exact frozen-objective-above-\(10\) point of the strengthened magnitude relaxation.

It is not yet a physical state.

---

# 5. Exact local orbit-Gram survival threshold

Choose the globally consistent real trial coefficient field

$$
\alpha_z^{\rm re}=\sqrt{x^{(10)}_z}.
$$

It satisfies

$$
\alpha_0^{\rm re}=1,\qquad
\alpha_{-z}^{\rm re}=\overline{\alpha_z^{\rm re}},
\qquad
\sum_z|\alpha_z^{\rm re}|^2=D.
$$

For distinct orbit labels \(a\ne b\), the associated orbit-matrix entry has magnitude

$$
|\alpha_{b-a}^{\rm re}|\le\sqrt U.
$$

The exact square comparisons are

$$
\boxed{
\begin{aligned}
\operatorname{den}(U)
&-(135873434)^2\operatorname{num}(U)\\
&=
16668547867312617600534570541272542097727081>0,
\end{aligned}
}
\tag{5.1}
$$

and

$$
\boxed{
\begin{aligned}
(135873435)^2\operatorname{num}(U)
&-\operatorname{den}(U)\\
&=
8927455314568955567791688543998538889265089>0.
\end{aligned}
}
\tag{5.2}
$$

Consequently,

$$
135873434
<
\frac1{\sqrt U}
<
135873435.
\tag{5.3}
$$

Take any set of \(N\) distinct orbit labels with

$$
N\le135873435.
$$

Every row of the corresponding orbit matrix has diagonal entry \(1\) and off-diagonal absolute row sum at most

$$
(N-1)\sqrt U
\le
135873434\sqrt U
<1.
$$

The matrix is Hermitian and strictly diagonally dominant with positive diagonal, so it is positive definite. Hence:

$$
\boxed{
\text{The real trial phases pass every orbit-Gram PSD test on at most }
135873435\text{ distinct labels.}
}
\tag{5.4}
$$

This does not imply positivity of the full \(D^2\times D^2\) orbit matrix.

---

# 6. Reconstruction from a coefficient field

Let a coefficient field satisfy

$$
\alpha_0=1,\qquad
\alpha_{-z}=\overline{\alpha_z},\qquad
\sum_z|\alpha_z|^2=D,
\tag{6.1}
$$

and define

$$
R_\alpha=\frac1D\sum_z\alpha_zW_z.
$$

The conjugation condition implies

$$
R_\alpha^*
=
\frac1D\sum_z\overline{\alpha_z}W_{-z}
=
R_\alpha.
$$

Moreover,

$$
\operatorname{Tr}R_\alpha=\alpha_0=1.
\tag{6.2}
$$

Using Weyl orthogonality,

$$
\begin{aligned}
\operatorname{Tr}R_\alpha^2
&=
\frac1{D^2}
\sum_{u,v}
\alpha_u\alpha_v
\operatorname{Tr}(W_uW_v)\\
&=
\frac1D\sum_u\alpha_u\alpha_{-u}\\
&=
\frac1D\sum_u|\alpha_u|^2\\
&=1.
\end{aligned}
\tag{6.3}
$$

Thus every admissible phase assignment reconstructs a Hermitian trace-one operator with Hilbert–Schmidt purity one, though it need not be positive.

For a physical pure state \(\rho\),

$$
\alpha_z=\operatorname{Tr}(W_z^*\rho),
\qquad
R_\alpha=\rho.
$$

The expectation convention used in orbit Gram matrices is instead

$$
\beta_z:=\operatorname{Tr}(\rho W_z)
=\alpha_{-z}
=\overline{\alpha_z}.
\tag{6.4}
$$

---

# 7. The full twisted orbit matrix

Define

$$
G_\alpha(a,b)
=
\operatorname{Tr}(R_\alpha W_a^*W_b).
$$

Since

$$
W_a^*W_b
=
W_{-a}W_b
=
\omega^{-[a,b]/2}W_{b-a},
$$

and

$$
\operatorname{Tr}(R_\alpha W_{b-a})
=
\alpha_{a-b}
=
\overline{\alpha_{b-a}},
$$

one obtains

$$
\boxed{
G_\alpha(a,b)
=
\omega^{-[a,b]/2}\,
\overline{\alpha_{b-a}}.
}
\tag{FullG}
$$

This is convention-correct.

If \(R_\alpha=\rho=|\psi\rangle\langle\psi|\), then

$$
G_\alpha(a,b)
=
\langle W_a\psi,W_b\psi\rangle,
$$

so it is literally the full Weyl-orbit Gram matrix.

For a general coefficient field it is a Hermitian twisted orbit matrix, but need not be positive.

---

# 8. \(G_\alpha/D\) is right multiplication by \(R_\alpha\)

Let

$$
E_a=\frac{W_a}{\sqrt D}.
$$

The \(\{E_a\}_{a\in\mathbb F_D^2}\) form an orthonormal basis of \(M_D\). Let

$$
\mathcal R_{R_\alpha}:X\longmapsto XR_\alpha.
$$

Its matrix entry in this basis is

$$
\begin{aligned}
\langle E_a,\mathcal R_{R_\alpha}(E_b)\rangle_{\rm HS}
&=
\operatorname{Tr}(E_a^*E_bR_\alpha)\\
&=
\frac1D
\operatorname{Tr}(W_a^*W_bR_\alpha)\\
&=
\frac1D\,G_\alpha(a,b).
\end{aligned}
$$

Therefore

$$
\boxed{
\frac{G_\alpha}{D}
\text{ is exactly the matrix of }
X\mapsto XR_\alpha.
}
\tag{8.1}
$$

Let

$$
\mu_1,\ldots,\mu_D
$$

be the eigenvalues of \(R_\alpha\). In an eigenbasis of \(R_\alpha\),

$$
|k\rangle\langle j|\,R_\alpha
=
\mu_j|k\rangle\langle j|.
$$

For each \(j\), this eigenvalue occurs for all \(k=1,\ldots,D\). Hence

$$
\boxed{
\operatorname{spec}(G_\alpha)
=
\{D\mu_j:1\le j\le D\},
\quad
\text{each repeated }D\text{ times}.
}
\tag{SpecG}
$$

It follows immediately that

$$
\boxed{
G_\alpha\succeq0
\iff
R_\alpha\succeq0,
}
\tag{8.2}
$$

and

$$
\boxed{
\operatorname{rank}G_\alpha
=
D\,\operatorname{rank}R_\alpha.
}
\tag{8.3}
$$

For completeness, the matrix \(G_\alpha\) has dimension

$$
D^2\times D^2,
$$

where

$$
\boxed{
D^2=
886499885479492515209635706825114329.
}
$$

It contains \(D^4\) entries.

---

# 9. The cubic phase functional

Expanding \(R_\alpha^3\),

$$
R_\alpha^3
=
\frac1{D^3}
\sum_{u,v,w}
\alpha_u\alpha_v\alpha_w
W_uW_vW_w.
$$

The trace vanishes unless

$$
u+v+w=0.
$$

When \(w=-u-v\),

$$
W_uW_vW_{-u-v}
=
\omega^{[u,v]/2}I_D,
$$

because the second Weyl cocycle contributes

$$
[u+v,-u-v]=0.
$$

Therefore

$$
\boxed{
C(\alpha):=\operatorname{Tr}R_\alpha^3
=
\frac1{D^2}
\sum_{u,v}
\alpha_u\alpha_v\alpha_{-u-v}
\omega^{[u,v]/2}.
}
\tag{Cubic}
$$

The expression is real because \(R_\alpha\) is Hermitian.

There are exactly

$$
\boxed{
D^4=
785882046955153344413318682126777865183404929125560156462076203921120241
}
$$

ordered \((u,v)\) summands.

The independent phase count, after

$$
\alpha_{-z}=\overline{\alpha_z}
$$

and \(\alpha_0=1\), is

$$
\boxed{
\frac{D^2-1}{2}
=
443249942739746257604817853412557164.
}
$$

Thus the cubic criterion is one scalar equality, but not a computationally small expression.

The same cubic is encoded by the orbit matrix:

$$
\boxed{
\operatorname{Tr}G_\alpha^3
=
D^4C(\alpha).
}
\tag{9.1}
$$

---

# 10. The defect identity and rigidity

Let the eigenvalues of \(R_\alpha\) be \(\mu_1,\ldots,\mu_D\). From (6.2)–(6.3),

$$
\sum_j\mu_j=1,
\qquad
\sum_j\mu_j^2=1.
$$

In particular,

$$
|\mu_j|\le1
$$

for every \(j\), and hence

$$
I-R_\alpha\succeq0.
$$

Since \(R_\alpha^2\) and \(I-R_\alpha\) commute and are both positive semidefinite,

$$
R_\alpha^2(I-R_\alpha)\succeq0.
$$

Therefore

$$
\boxed{
1-C(\alpha)
=
\operatorname{Tr}\!\left(
R_\alpha^2(I-R_\alpha)
\right)
=
\sum_j\mu_j^2(1-\mu_j)
\ge0.
}
\tag{Defect}
$$

Equality occurs exactly when

$$
\mu_j^2(1-\mu_j)=0
\quad\text{for every }j,
$$

so every eigenvalue belongs to \(\{0,1\}\). Since their sum is \(1\), exactly one eigenvalue is \(1\), and all others are \(0\). Thus

$$
\boxed{
C(\alpha)=1
\iff
R_\alpha
\text{ is a rank-one orthogonal projector}.
}
\tag{10.1}
$$

The cubic equality is therefore genuinely sufficient under (6.1).

---

# 11. Exact equivalence theorem

Under the three coefficient constraints

$$
\alpha_0=1,\qquad
\alpha_{-z}=\overline{\alpha_z},\qquad
\sum_z|\alpha_z|^2=D,
$$

the following are equivalent.

### 1. Pure-state coefficient field

There exists a unit vector \(\psi\) such that

$$
\alpha_z
=
\operatorname{Tr}
\left(
W_z^*|\psi\rangle\langle\psi|
\right).
$$

### 2. Twisted idempotence

For every \(k\),

$$
\boxed{
\alpha_k
=
\frac1D
\sum_u
\alpha_u\alpha_{k-u}
\omega^{[u,k]/2}.
}
\tag{11.1}
$$

This is exactly the Weyl-coefficient form of

$$
R_\alpha^2=R_\alpha.
$$

### 3. Positivity of the reconstructed operator

$$
R_\alpha\succeq0.
$$

Indeed, positivity together with

$$
\operatorname{Tr}R_\alpha
=
\operatorname{Tr}R_\alpha^2
=
1
$$

forces rank one.

### 4. Positivity of the full twisted orbit matrix

$$
G_\alpha\succeq0.
$$

This is equivalent to \(R_\alpha\succeq0\) by (8.2).

### 5. Cubic equality

$$
C(\alpha)=1.
$$

This is equivalent to rank-one projection by the defect identity.

Hence

$$
\boxed{
\text{pure}
\iff
\text{twisted idempotence}
\iff
R_\alpha\succeq0
\iff
G_\alpha\succeq0
\iff
C(\alpha)=1.
}
\tag{11.2}
$$

This is an exact logical compression of the global phase-lift gate.

---

# 12. Application to \(x^{(10)}\)

Put

$$
\xi_z=\sqrt{x^{(10)}_z}.
$$

Every Hermitian phase assignment has the form

$$
\alpha_z=\xi_ze^{i\theta_z},
\qquad
\theta_0=0,
\qquad
\theta_{-z}=-\theta_z.
$$

Because \(x^{(10)}\) has the correct total mass,

$$
\operatorname{Tr}R_\alpha
=
\operatorname{Tr}R_\alpha^2
=
1
$$

for every such phase assignment.

The cubic becomes

$$
\boxed{
\begin{aligned}
C_{10}(\theta)
=
\frac1{D^2}\sum_{u,v}
&\xi_u\xi_v\xi_{u+v}\\
&\times
\operatorname{Re}\!\left[
e^{i(\theta_u+\theta_v-\theta_{u+v})}
\omega^{[u,v]/2}
\right].
\end{aligned}
}
\tag{12.1}
$$

Retaining \(\omega^{[u,v]/2}\) avoids any ambiguity about the finite-field representative of \(1/2\).

The defect theorem gives

$$
C_{10}(\theta)\le1
\quad\text{for every phase assignment}.
$$

Define the exact phase-lift defect

$$
\boxed{
\eta_{10}
=
1-\max_{\substack{\theta_0=0\\
\theta_{-z}=-\theta_z}}
C_{10}(\theta)
\ge0.
}
\tag{12.2}
$$

The phase torus is compact, so the maximum is attained. Therefore:

$$
\boxed{
\eta_{10}=0
\iff
x^{(10)}
\text{ has a pure-state phase lift}.
}
\tag{12.3}
$$

If \(\eta_{10}=0\), the resulting pure state satisfies

$$
\mathcal F_\Gamma>10
$$

by (4.1), and PW10 is disproved.

If \(\eta_{10}>0\), the specific obstruction \(x^{(10)}\) is excluded, but PW10 does not follow; another magnitude profile could still lift physically and violate the gate.

## What is not proved

No phase assignment satisfying

$$
C_{10}(\theta)=1
$$

is constructed.

No explicit constant

$$
\eta>0
$$

is proved such that

$$
C_{10}(\theta)\le1-\eta
$$

for every phase assignment.

No additional exact phase-sensitive inequality is obtained that excludes all phase lifts of \(x^{(10)}\).

The real trial phase assignment is known to pass every orbit-Gram PSD test on up to \(135\,873\,435\) labels, but that does not determine the sign of the full \(D^2\times D^2\) orbit matrix or the value of its cubic defect.

Thus the first unresolved binary problem is now precisely

$$
\boxed{
\max_\theta C_{10}(\theta)
\stackrel{?}{=}1.
}
\tag{12.4}
$$

This is substantially more compressed logically than the full family of twisted-idempotence equations, but it still has global \(D^4\) indexing cost.

---

# Audit ledger

## PROVED

* \(\mathscr Fb=b\), \(\mathscr Fy=y\), and \(\mathscr Fd=d\).
* \(d_0=0\), \(x^{(10)}_0=1\), \(x^{(10)}\) is real, even, self-Fourier, and has total mass \(D\).
* For every nonzero \(z\),

  $$
  \frac1{2(D+1)}
  \le x^{(10)}_z<U<\frac1{16}.
  $$
* The exact rational value of \(U\).
* Both displayed exact square gaps.
* The real trial phases pass every orbit-Gram PSD test on at most \(135\,873\,435\) distinct labels.
* \(x^{(10)}\) satisfies LC, TriGram, and ConvMag, including all zero-label cases.
* The exact frozen objective lower bound

  $$
  10+
  \frac{m((m-11)D-10m)}{D(D+1)}
  >10.
  $$
* The proposed formula for \(G_\alpha(a,b)\), including its conjugation and Weyl phase.
* \(G_\alpha/D\) is exactly the matrix of right multiplication by \(R_\alpha\).
* The spectrum and rank formulas for \(G_\alpha\).
* The cubic formula for \(\operatorname{Tr}R_\alpha^3\).
* The defect identity

  $$
  1-C(\alpha)
  =
  \operatorname{Tr}\bigl(R_\alpha^2(I-R_\alpha)\bigr)\ge0.
  $$
* Equality in the defect identity is rigid and forces a rank-one orthogonal projector.
* The exact equivalence of pure-state coefficients, twisted idempotence, positivity of \(R_\alpha\), positivity of \(G_\alpha\), and \(C(\alpha)=1\).
* The exact scalar phase-lift criterion

  $$
  \eta_{10}=0
  \iff
  x^{(10)}\text{ admits a physical pure-state phase lift}.
  $$

## DISPROVED

* No new statement is disproved in this round.
* In particular, the existence of a physical lift of \(x^{(10)}\) is not disproved.

## NECESSARY-ONLY

* SF, LC, TriGram, and ConvMag as magnitude conditions for physical pure states.
* All finite principal orbit-Gram PSD tests.
* The universal inequality \(C(\alpha)\le1\) before equality is established.

## SUFFICIENT-ONLY

* No merely sufficient frozen-tuple criterion is introduced.

## EQUIVALENT

Under Hermiticity, trace \(1\), and Hilbert–Schmidt purity \(1\):

* \(C(\alpha)=1\);
* \(R_\alpha\) is a rank-one projector;
* \(R_\alpha\succeq0\);
* \(G_\alpha\succeq0\);
* twisted idempotence;
* physical pure-state realizability.

## OPEN

* Whether compatible phases for \(x^{(10)}\) satisfy \(C(\alpha)=1\).
* Whether there is a uniform phase gap

  $$
  C(\alpha)\le1-\eta
  $$

  for this magnitude profile.
* The sign of \(\eta_{10}\).
* Whether some other frozen-objective-above-\(10\) magnitude profile has a physical phase lift.
* PW10 for the exact frozen tuple.

## CONJECTURED

* No claim is promoted to conjectured status.

The first new claim requiring independent verification is the convention-sensitive identification

$$
\frac{G_\alpha}{D}
=
[\text{right multiplication by }R_\alpha]_{\{W_a/\sqrt D\}},
$$

and the resulting equivalence

$$
C(\alpha)=1
\iff
R_\alpha\text{ is a rank-one projector}.
$$

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-13-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-13-local-audit.md bytes=5789 sha256=1d088e476fb8ccf8dae0d629d086352e57b3a06133aa7a23378cb3b42da0e9ac -->

# Round 13 local audit

- Audit completed (UTC): `2026-09-13T01:12:54Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-13-response.md`
- Web-response SHA-256:
  `d486ae66f47714c322a2f6694fbbdf81665d53b582021780175312777a4663fe`
- Capture equality: artifact and output copies are byte-identical, each
  `19,279` bytes and `1,336` lines.

## Verdict

The substantive Round 13 claims pass independent arithmetic, algebraic, and
small-prime convention checks.  The correct frozen-tuple status remains
\[
\boxed{\text{PW10 remains OPEN.}}
\]
The round establishes an exact global phase-lift equivalence, but neither
constructs a physical objective-above-`10` state nor proves the physical upper
bound.

## Verified sharper magnitude obstruction

For
\[
x^{(10)}=b+\frac{10}{M}d,
\]
the self-Fourier normalization, zero coefficient, evenness, and mass are
correct.  The exact lower-bound numerator is
\[
D(m-21)-20m=456803015027398949599719555>0,
\]
which verifies
\[
x_z^{(10)}\ge\frac1{2(D+1)}>0\qquad(z\ne0).
\]

The displayed reduced upper bound
\[
U=
\frac{94190609356686178298989929062516930}
{1738908434768135059241251074769290641999621851114161}
<\frac1{16}
\]
is exact.  Its `1/16` cross-multiplication gap is
\[
1738908434768133552191501367790437858160756850843281>0.
\]
These bounds correctly prove every LC, TriGram, and ConvMag case.

The objective exceeds `10` by the exact reduced fraction
\[
\frac{3357953467987716774306702559357710}
{13431816446658977517442074781790591}>0,
\]
giving the lower bound `10.249999952078184...`.

The two exact square gaps are correct.  Hence the real nonnegative trial
phases make every orbit matrix on at most `135,873,435` distinct labels
strictly diagonally dominant and positive definite.  This is local principal
positivity, not a physical phase lift.

## Verified global phase-lift theorem

With
\[
R_\alpha=\frac1D\sum_z\alpha_zW_z,
\quad
\alpha_0=1,
\quad
\alpha_{-z}=\overline{\alpha_z},
\quad
\sum_z|\alpha_z|^2=D,
\]
one has
\[
R_\alpha=R_\alpha^*,
\qquad
\operatorname{Tr}R_\alpha=
\operatorname{Tr}R_\alpha^2=1.
\]

The conjugation and Weyl phase in the full orbit matrix are correct:
\[
G_\alpha(a,b)
=\operatorname{Tr}(R_\alpha W_a^*W_b)
=\omega^{-[a,b]/2}\overline{\alpha_{b-a}}.
\]
In the orthonormal Hilbert--Schmidt basis `W_a/sqrt(D)`, `G_alpha/D` is
exactly right multiplication `X -> X R_alpha`.  Therefore every eigenvalue
of `R_alpha` occurs in `G_alpha/D` with multiplicity `D`, and
\[
G_\alpha\succeq0\iff R_\alpha\succeq0,
\qquad
\operatorname{rank}G_\alpha=D\operatorname{rank}R_\alpha.
\]

The cubic formula is also convention-correct:
\[
C(\alpha)=\operatorname{Tr}R_\alpha^3
=\frac1{D^2}\sum_{u,v}
\alpha_u\alpha_v\alpha_{-u-v}\omega^{[u,v]/2}.
\]
Since all eigenvalues of the Hermitian `R_alpha` lie in `[-1,1]`,
\[
1-C(\alpha)
=\operatorname{Tr}(R_\alpha^2(I-R_\alpha))
=\sum_j\mu_j^2(1-\mu_j)\ge0.
\]
Equality holds exactly when the eigenvalues are one `1` and otherwise `0`.
Thus, under the three displayed coefficient hypotheses, physical pure-state
coefficients, twisted idempotence, positivity of `R_alpha`, positivity of the
full `G_alpha`, and `C(alpha)=1` are genuinely equivalent.

The global counts in the response are exact:
\[
D^2=886499885479492515209635706825114329,
\]
\[
D^4=
785882046955153344413318682126777865183404929125560156462076203921120241,
\]
and the compatible phase torus has `(D^2-1)/2` independent angles.

## Independent advance beyond the web response

The response leaves the full-matrix sign and cubic defect of the real
nonnegative trial phases undetermined.  They are in fact exactly separable.

For the audited Weyl convention, let parity be
\[
\Pi|y\rangle=|-y\rangle.
\]
Then
\[
\Pi=\frac1D\sum_zW_z,
\qquad
\operatorname{Tr}(\Pi W_z)=1.
\]
For `Pi_-=(I-Pi)/2` and the real trial
`alpha_z=sqrt(x_z^(10))`,
\[
\operatorname{Tr}(\Pi_-R_\alpha)
=\frac12\left(1-\frac1D\sum_z\sqrt{x_z^{(10)}}\right)<0,
\]
because every nonzero weight lies strictly between `0` and `1` and
`sum_z x_z^(10)=D`.

Thus this particular `R_alpha` is not positive semidefinite, its full orbit
matrix has a negative eigenvalue, and its cubic is strictly below `1`.
Using the pointwise lower bound and Cauchy--Schwarz gives the explicit coarse
gap
\[
\boxed{C(\alpha)<31/32}
\]
for the real nonnegative trial phases.

This does not exclude other complex phase assignments for the same magnitude
profile.  The sign of the phase-uniform defect `eta_10` remains open.

## Textual defects in the web capture

Three duplicated TeX fragments are present in the captured answer:

- a repeated denominator line after equation (2.2);
- a repeated summation line in the display for `R_alpha^*`;
- a repeated `\qquad` before `theta_0=0` in section 12.

They are transcription/layout defects.  The surrounding derivations and all
values used later are correct.

## Earliest remaining gap

For the concrete frozen profile, define
\[
\eta_{10}=1-\max_\theta C_{10}(\theta)\ge0.
\]
Compactness makes
\[
\eta_{10}=0
\iff
x^{(10)}\text{ has a physical pure-state phase lift}.
\]
The real phase has now been quantitatively excluded, but no proof determines
whether some complex phase field attains `C=1`.  Even excluding this one
profile would not by itself prove PW10; another physical profile could violate
the gate.

## Reproducibility

- `work/verify_round13_web_response.py`
  SHA-256 `da0dec7d9c9a3caeb3292ec498dd324d8d17d1d63085dc04c0da20d1a8b84bd5`
- `work/verify_round13_global_gate.py`
  SHA-256 `342712b72001fac6a2f176bd829b0f16f872d864076adc7bf98ac575205d9623`
- `work/round-13-global-gate-independent.md`
  SHA-256 `39b9ab3064d6cd9385e25a4d5ec2214b0f8fc177fd9804f9b73d6360f99978f4`

Both checkers print `PASS`.

<!-- END HISTORICAL FILE path=outputs/round-13-local-audit.md -->


# ROUND 014

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-14-prompt.md bytes=8558 sha256=89e017d1b076e0cd8d4876eea28bb517d715c7609b46edafa242f758bef49b6a -->

# Round 14 — displaced parity kills the coherent phase orbit; audit and go beyond the parity-cap relaxation

Continue in the same ordinary Chat conversation and the same canonically
frozen finite `r=2`, low-`A` gate.  Give a public, self-contained derivation
and no hidden chain-of-thought.  Do not repeat the Round 8--13 narrative.

## Exact frozen boundary

Use exactly
\[
m=485165196,
\qquad P=485165237=m+41,
\]
\[
D=941541228773064677=4P^2+1,
\qquad i=2P,
\qquad i^2=-1\pmod D,
\]
\[
0\le j\le P-42,
\qquad r_j=j^2\bmod P\text{ in }[0,P-1],
\qquad t_j=2Pj+r_j,
\]
\[
a_j=(t_j,t_j^2),
\qquad A=\{a_j:0\le j\le P-42\},
\qquad \Gamma=(A-A)\setminus\{0\},
\]
\[
M=|\Gamma|=m(m-1)=235385266924553220.
\]
The open gate is
\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use
\[
W_{(p,q)}|y\rangle
=\omega^{p(y+q/2)}|y+q\rangle,
\qquad
W_uW_v=\omega^{[u,v]/2}W_{u+v},
\qquad W_u^*=W_{-u}.
\]

## Independently audited Round 13 boundary

The following are now independently verified.

1. The exact full-support magnitude point
   \[
   x^{(10)}=b+\frac{10}{M}d
   \]
   is real, even, self-Fourier, has `x_0=1` and total mass `D`, and satisfies
   SF, LC, TriGram, and ConvMag.  For every nonzero label,
   \[
   \frac1{2(D+1)}\le x_z^{(10)}<
   U:=\frac1{D+1}+\frac{10}{M}+\frac{10}{D}<\frac1{16}.
   \]
   Its frozen objective has the exact lower bound
   \[
   10+
   \frac{m((m-11)D-10m)}{D(D+1)}
   =10.249999952078184\ldots>10.
   \]
   This is not a physical state.

2. For the real trial phases `alpha_z=sqrt(x_z^(10))`, every principal
   orbit matrix on at most `135,873,435` distinct labels is positive definite
   by an exact diagonal-dominance calculation.  This does not decide the full
   matrix.

3. For any coefficient field satisfying
   \[
   \alpha_0=1,
   \qquad \alpha_{-z}=\overline{\alpha_z},
   \qquad \sum_z|\alpha_z|^2=D,
   \]
   put
   \[
   R_\alpha=\frac1D\sum_z\alpha_zW_z.
   \]
   Then `R_alpha` is Hermitian and
   \[
   \operatorname{Tr}R_\alpha
   =\operatorname{Tr}R_\alpha^2=1.
   \]
   The full orbit matrix satisfies
   \[
   G_\alpha(a,b)
   =\omega^{-[a,b]/2}\overline{\alpha_{b-a}},
   \]
   and `G_alpha/D` is the Hilbert--Schmidt matrix of right multiplication
   `X -> X R_alpha`.  Hence
   \[
   G_\alpha\succeq0\iff R_\alpha\succeq0.
   \]

4. The convention-correct cubic is
   \[
   C(\alpha)=\operatorname{Tr}R_\alpha^3
   =\frac1{D^2}\sum_{u,v}
   \alpha_u\alpha_v\alpha_{-u-v}\omega^{[u,v]/2},
   \]
   with
   \[
   1-C(\alpha)
   =\sum_j\mu_j^2(1-\mu_j)\ge0.
   \]
   Under the three coefficient hypotheses,
   \[
   \boxed{
   C(\alpha)=1
   \iff R_\alpha\text{ is a rank-one projector}
   \iff\alpha\text{ is a physical pure-state coefficient field}.
   }
   \tag{CubicLift}
   \]

Thus PW10 remains **OPEN**.  The sign of
\[
\eta_{10}=1-\max_\theta C_{10}(\theta)
\]
for the fixed magnitude profile is unknown.

## New exact displaced-parity calculation to audit

Define parity and its displacements by
\[
\Pi|y\rangle=|-y\rangle,
\qquad
\Pi_a=W_a\Pi W_a^*.
\]
Direct Weyl summation proposes
\[
\boxed{
\Pi=\frac1D\sum_zW_z,
\quad
\Pi^2=I,
\quad
\operatorname{Tr}\Pi=1,
\quad
\operatorname{Tr}(\Pi W_z)=1,
}
\tag{Parity}
\]
and
\[
\Pi_a=\frac1D\sum_z\omega^{[a,z]}W_z.
\]
Consequently
\[
\boxed{
w_a:=\operatorname{Tr}(\Pi_aR_\alpha)
=\frac1D\sum_z\alpha_z\omega^{-[a,z]}\in\mathbb R.
}
\tag{Wigner}
\]
Because `Pi_a` has eigenvalues `+-1`, physical positivity requires
\[
\boxed{-1\le w_a\le1\quad\text{for every }a.}
\tag{ParityCap}
\]

Let `r_z=sqrt(x_z^(10))`.  For every `c in F_D^2`, consider the full
affine-character phase orbit
\[
\alpha_z^{(c)}=r_z\omega^{[c,z]}.
\tag{CharacterPhase}
\]
The evenness of `r` should imply
\[
R_c=W_cR_0W_c^*,
\qquad
[R_c,\Pi_c]=0.
\]
At the matching phase point,
\[
w_c=\frac1D\sum_zr_z>1,
\]
because every nonzero `x_z^(10)` lies strictly between zero and one and
`sum_z x_z^(10)=D`.  Hence every one of these `D^2` character phases is
nonphysical.

Using
\[
r_z\ge\frac1{\sqrt{2(D+1)}}\qquad(z\ne0)
\]
gives
\[
s:=\frac1D\sum_zr_z
\ge
\frac{1+(D^2-1)/\sqrt{2(D+1)}}{D}
>\frac{\sqrt D}{3}.
\]
Since `D>144`, the negative-parity trace has magnitude greater than
`sqrt(D)/8`.  Cauchy--Schwarz in the commuting odd-parity block of dimension
`(D-1)/2` should then give the uniform character-orbit gap
\[
\boxed{C(\alpha^{(c)})<31/32\quad\text{for every }c.}
\tag{CharacterGap}
\]
Audit the commutation, the eigenspace dimension, every strict inequality, and
the passage from negative trace to cubic defect.  This conclusion concerns
only `(CharacterPhase)`, not arbitrary phases.

## Candidate proof that all ParityCap constraints are still insufficient

Choose one representative `H` from each nonzero pair `{z,-z}`.  Let the
angles `theta_z`, `z in H`, be independent uniform angles and set
\[
\alpha_z=r_ze^{i\theta_z},
\qquad
\alpha_{-z}=r_ze^{-i\theta_z},
\qquad
\alpha_0=1.
\]
For fixed `a`,
\[
Dw_a=1+Y_a,
\qquad
Y_a=2\sum_{z\in H}r_z
\cos(\theta_z-2\pi[a,z]/D).
\]
The summands are independent and mean zero, with range lengths at most
`4r_z`, and
\[
\sum_{z\in H}r_z^2=\frac{D-1}{2}.
\]
Hoeffding therefore proposes
\[
\Pr\{|Y_a|\ge D-1\}
\le2e^{-(D-1)/4}.
\]
A union bound over all `D^2` labels gives
\[
\Pr\{\text{some ParityCap fails}\}
\le2D^2e^{-(D-1)/4}<1.
\tag{Union}
\]
The final strict inequality has the exact elementary certificate
\[
\boxed{
(D-1)^3>768D^2,
}
\]
using `e^t>t^3/6` at `t=(D-1)/4`.

Thus there should exist compatible phases satisfying every ParityCap
strictly.  Moreover, `1-C` is a nonzero real-analytic function on the phase
torus because `(CharacterGap)` supplies a point where it is positive.  Its
zero set has measure zero.  Therefore phases can be chosen simultaneously so
that every ParityCap is strict and `C<1`; density of rational angles then
allows algebraic root-of-unity phases.  This is an existence proof, not an
explicit enumeration of `D^2` angles.

If all steps are valid, conclude only
\[
\boxed{
\text{Hermiticity + mass + all ParityCap constraints do not imply }C=1.
}
\tag{ParityBreak}
\]
These same phases automatically pass all principal Gram tests through the
audited `135,873,435` threshold because that bound is magnitude-only.

## Exact tasks

1. Give one verdict for PW10 on this exact frozen tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**.

2. Prove or correct `(Parity)`, `(Wigner)`, and `(ParityCap)`, including every
   Weyl phase and Fourier sign.  State the dimensions and global indexing
   cost.

3. Prove or correct the exclusion of the full affine-character phase orbit
   and `(CharacterGap)`.  A bound for these `D^2` phases is not a bound for
   the continuous phase torus.

4. Audit the random-phase Hoeffding calculation, `(Union)`, the exact integer
   certificate, the real-analytic zero-set step, and the rational-angle
   density step.  If correct, record `(ParityBreak)` as a strict failure of a
   stronger phase-sensitive relaxation.  If any step fails, identify the
   first precise failure and repair it if possible.

5. Then seek a genuinely phase-uniform advance for the actual `x^(10)`.  In
   priority order:

   - construct compatible phases with `C=1`, which would physically disprove
     PW10;
   - prove `C<=1-eta` for every compatible phase with one explicit `eta>0`,
     which would exclude this particular obstruction;
   - derive one additional exact consequence of positivity or cubic equality
     that cuts an explicit algebraic phase field which already passes every
     ParityCap and all audited small-Gram tests.

   Do not promote a numerical search, an unnamed SDP, the definition of
   `eta_10`, or a failed special phase orbit into a solution.

6. Even a proof that `x^(10)` has no phase lift would not by itself prove
   PW10 for every physical magnitude profile.  Preserve this quantifier.

7. Do not return to five-carry arithmetic, the degree-`m` resultant schema,
   Perron--Schur10, or the all-`T` ratio without a completed exact certificate
   for this same tuple.

8. End with a plain audit ledger separating **PROVED**, **DISPROVED**,
   **NECESSARY-ONLY**, **SUFFICIENT-ONLY**, **EQUIVALENT**, **OPEN**, and
   **CONJECTURED**.  State the first new claim requiring independent
   verification.

The purpose of this round is to turn the first explicit global witness into a
quantitative separation, then determine whether the entire displaced-parity
layer is still too weak.  Do not stop after merely restating cubic lifting.

<!-- END HISTORICAL FILE path=work/round-14-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-14-response.md bytes=19514 sha256=bc42715023aaeec679e9d59091b27c3941729f2c13f037affc6cc27140f3fae6 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The displaced-parity calculation is correct. It gives two distinct conclusions:

1. Every affine-character phase field

   $$
   \alpha_z^{(c)}=\sqrt{x_z^{(10)}}\,\omega^{[c,z]}
   $$

   is nonphysical, and in fact satisfies the uniform quantitative bound

   $$
   C(\alpha^{(c)})<\frac{31}{32}.
   $$

2. All \(D^2\) displaced-parity caps remain far too weak globally. There exists an exact compatible **sign phase field**

   $$
   \alpha_z^\star=\pm\sqrt{x_z^{(10)}}
   $$

   satisfying every parity cap strictly, every previously audited magnitude constraint, and every orbit-Gram PSD test on at most \(135{,}873{,}435\) labels, while

   $$
   \boxed{C(\alpha^\star)<\frac{2}{15}.}
   $$

   Hence its rank-one idempotence defect is quantitatively large:

   $$
   \boxed{
   \sum_k\left|
   \alpha_k^\star-
   \frac1D\sum_u
   \alpha_u^\star\alpha_{k-u}^\star
   \omega^{[u,k]/2}
   \right|^2
   >
   \frac{169}{225}D.
   }
   $$

This proves a stronger form of `ParityBreak`, but it neither constructs phases with \(C=1\) nor gives a phase-uniform gap for all phase assignments of \(x^{(10)}\).

---

# 1. Audit of the sharper magnitude obstruction

Let

$$
(\mathscr Ff)(u)=\frac1D\sum_z f(z)\omega^{[u,z]}.
$$

Because the symplectic form is alternating,

$$
\mathscr F^2f=f.
$$

For \(f=\mathbf 1_\Gamma\), central symmetry \(\Gamma=-\Gamma\) gives

$$
\mathscr F\mathbf1_\Gamma=\frac{\lambda}{D},
\qquad
\mathscr F\left(\frac{\lambda}{D}\right)=\mathbf1_\Gamma.
$$

Also

$$
b=\frac{D}{D+1}\delta_0+\frac1{D+1}\mathbf1
$$

satisfies \(\mathscr Fb=b\). Consequently, with

$$
y=\mathbf1_\Gamma+\frac{\lambda}{D},
\qquad
d=y-\frac MD\,b,
\qquad
x^{(10)}=b+\frac{10}{M}d,
$$

one has

$$
\boxed{
\mathscr Fx^{(10)}=x^{(10)},\qquad
x^{(10)}_0=1,\qquad
\sum_zx^{(10)}_z=D,
}
$$

and \(x^{(10)}\) is real and even.

For \(z\neq0\),

$$
x_z^{(10)}
=
\frac1{D+1}
+
\frac{10}{M}
\left[
\mathbf1_\Gamma(z)+\frac{\lambda_z}{D}
-\frac{M}{D(D+1)}
\right].
\tag{1.1}
$$

Using \(-m\le\lambda_z\le M\), one obtains

$$
\frac1{2(D+1)}
\le x_z^{(10)}
<
U:=
\frac1{D+1}+\frac{10}{M}+\frac{10}{D}.
$$

The exact reduced fraction is

$$
\boxed{
U=
\frac{
94190609356686178298989929062516930
}{
1738908434768135059241251074769290641999621851114161
}.
}
$$

The supplied square comparisons are exact:

$$
\begin{aligned}
\operatorname{den}(U)
&-(135873434)^2\operatorname{num}(U)\\
&=
16668547867312617600534570541272542097727081>0,
\end{aligned}
$$

and

$$
\begin{aligned}
(135873435)^2\operatorname{num}(U)
&-\operatorname{den}(U)\\
&=
8927455314568955567791688543998538889265089>0.
\end{aligned}
$$

Thus

$$
\boxed{
135873434<\frac1{\sqrt U}<135873435.
}
\tag{1.2}
$$

In particular \(U<1/16\).

Because self-Fourier functions obey Exchange,

$$
\frac1D\sum_z\lambda_zx_z^{(10)}
=
\sum_{g\in\Gamma}x_g^{(10)}.
$$

Using \(\lambda_g\ge-m\) for \(g\in\Gamma\),

$$
\boxed{
\begin{aligned}
\frac1D\sum_z\lambda_zx_z^{(10)}
&\ge
\frac{M}{D+1}
+
10\left(
1-\frac mD-\frac{M}{D(D+1)}
\right)\\
&=
10+
\frac{m((m-11)D-10m)}{D(D+1)}
>10.
\end{aligned}
}
\tag{1.3}
$$

This is the stated lower bound

$$
10.249999952078184\ldots.
$$

It remains a magnitude-relaxation point, not a physical state.

## 1.1 Small orbit-Gram tests

For any compatible phase assignment

$$
\alpha_z=\sqrt{x_z^{(10)}}e^{i\theta_z},
\qquad
\theta_{-z}=-\theta_z,
$$

every off-diagonal entry of an orbit Gram matrix has magnitude at most
\(\sqrt U\).

Therefore, on any set of \(N\le135873435\) distinct orbit labels, each row has off-diagonal absolute sum at most

$$
(N-1)\sqrt U
\le135873434\sqrt U<1.
$$

The Hermitian matrix is strictly diagonally dominant with diagonal \(1\), hence positive definite.

Thus the \(135{,}873{,}435\) threshold is actually **phase-independent**; it is not limited to the all-real trial phase.

---

# 2. Parity and displaced parity

Define

$$
\Pi|y\rangle=|-y\rangle.
$$

For \(x,y\in\mathbb F_D\),

$$
\begin{aligned}
\left\langle x\left|
\frac1D\sum_{p,q}W_{(p,q)}
\right|y\right\rangle
&=
\frac1D\sum_p
\omega^{p(y+(x-y)/2)}\\
&=
\frac1D\sum_p\omega^{p(x+y)/2}\\
&=\delta_{x,-y}.
\end{aligned}
$$

Hence

$$
\boxed{\Pi=\frac1D\sum_zW_z.}
\tag{2.1}
$$

Since \(D\) is odd, the only fixed computational basis vector is \(|0\rangle\). Therefore

$$
\boxed{
\Pi^2=I,\qquad
\operatorname{Tr}\Pi=1.
}
$$

Also,

$$
\begin{aligned}
\operatorname{Tr}(\Pi W_z)
&=
\frac1D\sum_u\operatorname{Tr}(W_uW_z)\\
&=1,
\end{aligned}
$$

because only \(u=-z\) contributes, with no cocycle phase. Thus

$$
\boxed{\operatorname{Tr}(\Pi W_z)=1\quad\forall z.}
\tag{2.2}
$$

The parity eigenspace dimensions are

$$
\boxed{
d_+=\frac{D+1}{2},
\qquad
d_-=\frac{D-1}{2}.
}
\tag{2.3}
$$

For

$$
\Pi_a=W_a\Pi W_a^*,
$$

Weyl conjugation gives

$$
\boxed{
\Pi_a
=
\frac1D\sum_z\omega^{[a,z]}W_z.
}
\tag{2.4}
$$

These \(D^2\) displaced parities form an orthogonal operator basis:

$$
\boxed{
\operatorname{Tr}(\Pi_a\Pi_b)=D\,\delta_{a,b}.
}
\tag{2.5}
$$

---

# 3. Wigner values and the parity cap

Let

$$
R_\alpha=\frac1D\sum_z\alpha_zW_z,
$$

where

$$
\alpha_0=1,\qquad
\alpha_{-z}=\overline{\alpha_z},\qquad
\sum_z|\alpha_z|^2=D.
$$

Then \(R_\alpha\) is Hermitian with

$$
\operatorname{Tr}R_\alpha
=
\operatorname{Tr}R_\alpha^2=1.
$$

Since

$$
\operatorname{Tr}(W_zR_\alpha)=\alpha_{-z},
$$

equations (2.4) and the substitution \(z\mapsto-z\) give

$$
\boxed{
w_a:=\operatorname{Tr}(\Pi_aR_\alpha)
=
\frac1D\sum_z
\alpha_z\omega^{-[a,z]}.
}
\tag{Wigner}
$$

The value is real because both \(\Pi_a\) and \(R_\alpha\) are Hermitian.

If \(R_\alpha\succeq0\), it is a density operator and \(\Pi_a\) is a Hermitian unitary. Hence

$$
\boxed{-1\le w_a\le1\quad\forall a.}
\tag{ParityCap}
$$

There are exactly

$$
D^2=
886499885479492515209635706825114329
$$

such inequalities. Naively evaluating all of them from the coefficient field uses \(D^4\) indexed summands.

The orthogonality (2.5) also gives the exact global identities

$$
\boxed{
\sum_aw_a=D,\qquad
\sum_aw_a^2=D.
}
\tag{3.1}
$$

These hold for every coefficient field satisfying the trace and purity hypotheses, whether or not it is positive.

---

# 4. The affine-character phase orbit is uniformly nonphysical

Put

$$
r_z=\sqrt{x_z^{(10)}}
$$

and, for \(c\in\mathbb F_D^2\),

$$
\alpha_z^{(c)}=r_z\omega^{[c,z]}.
$$

Let

$$
R_0=\frac1D\sum_zr_zW_z.
$$

Then

$$
\boxed{
R_c=W_cR_0W_c^*.
}
\tag{4.1}
$$

Since \(r_{-z}=r_z\), parity sends \(W_z\) to \(W_{-z}\), so

$$
[R_0,\Pi]=0.
$$

Conjugating gives

$$
\boxed{[R_c,\Pi_c]=0.}
\tag{4.2}
$$

At the matching point \(a=c\),

$$
\boxed{
w_c
=
\frac1D\sum_zr_z
=:s.
}
\tag{4.3}
$$

Every nonzero \(x_z^{(10)}\) lies strictly between \(0\) and \(1\). Thus

$$
\sqrt{x_z^{(10)}}>x_z^{(10)}
\quad(z\ne0),
$$

and hence

$$
\sum_zr_z>\sum_zx_z^{(10)}=D.
$$

Therefore

$$
\boxed{s>1.}
\tag{4.4}
$$

Every affine-character phase field violates ParityCap and is nonphysical.

---

## 4.1 Quantitative lower bound on \(s\)

The pointwise lower bound gives

$$
s
\ge
\frac{
1+(D^2-1)/\sqrt{2(D+1)}
}{D}.
$$

Since

$$
\frac{D^2-1}{\sqrt{2(D+1)}}
=
(D-1)\sqrt{\frac{D+1}{2}},
$$

one has, for \(D>2\),

$$
\frac{D-1}{D}
\sqrt{\frac{D+1}{2D}}
>
\frac1{2\sqrt2}
>
\frac13.
$$

Consequently,

$$
\boxed{s>\frac{\sqrt D}{3}.}
\tag{4.5}
$$

As \(D>144\),

$$
s-1>\frac{\sqrt D}{4}.
\tag{4.6}
$$

---

# 5. The uniform character-orbit cubic gap

Because \(R_c\) commutes with \(\Pi_c\), it splits into even- and odd-parity blocks. The trace on the odd block is

$$
t_-=
\operatorname{Tr}\left(\frac{I-\Pi_c}{2}R_c\right)
=
\frac{1-s}{2}<0.
$$

Let the negative eigenvalues in that block be
\(-q_1,\ldots,-q_\ell\), \(q_j>0\). Their total negative mass obeys

$$
\sum_jq_j\ge\frac{s-1}{2}.
$$

By Cauchy–Schwarz and \(\ell\le d_-=(D-1)/2\),

$$
\sum_jq_j^2
\ge
\frac{(s-1)^2}{2(D-1)}.
\tag{5.1}
$$

For every negative eigenvalue \(\mu=-q\),

$$
\mu^2(1-\mu)=q^2(1+q)>q^2.
$$

All other terms in the cubic defect are nonnegative. Hence

$$
\boxed{
1-C(\alpha^{(c)})
>
\frac{(s-1)^2}{2(D-1)}.
}
\tag{5.2}
$$

Using (4.6),

$$
1-C(\alpha^{(c)})
>
\frac{D}{32(D-1)}
>
\frac1{32}.
$$

Therefore

$$
\boxed{
C(\alpha^{(c)})<\frac{31}{32}
\quad\forall c\in\mathbb F_D^2.
}
\tag{CharacterGap}
$$

A stronger exact lower bound for the defect is

$$
1-C(\alpha^{(c)})
>
\frac{D-1}{2D^2}
\left(
\sqrt{\frac{D+1}{2}}-1
\right)^2,
$$

which is close to \(1/4\) for the displayed \(D\).

This conclusion applies only to the \(D^2\) affine-character phase fields.

---

# 6. Audit of the random-phase parity argument

Choose one representative set \(\mathcal H\) for the nonzero pairs
\(\{z,-z\}\). Its size is

$$
|\mathcal H|
=
\frac{D^2-1}{2}
=
443249942739746257604817853412557164.
$$

Let the angles \(\theta_z\), \(z\in\mathcal H\), be independent and uniform, and set

$$
\alpha_z=r_ze^{i\theta_z},
\qquad
\alpha_{-z}=r_ze^{-i\theta_z}.
$$

For fixed \(a\),

$$
Dw_a=1+Y_a,
$$

where

$$
Y_a=
2\sum_{z\in\mathcal H}
r_z
\cos\left(
\theta_z-\frac{2\pi[a,z]}D
\right).
$$

The summands are independent, mean zero, and have interval lengths at most \(4r_z\). Moreover,

$$
\sum_{z\in\mathcal H}r_z^2
=
\frac12\sum_{z\ne0}x_z^{(10)}
=
\frac{D-1}{2}.
$$

Hoeffding’s elementary exponential-moment argument gives

$$
\boxed{
\Pr\{|Y_a|\ge D-1\}
\le
2e^{-(D-1)/4}.
}
\tag{6.1}
$$

If \(|Y_a|<D-1\), then

$$
-1<w_a<1.
$$

A union bound over all \(D^2\) phase-space points yields

$$
\Pr\{\text{some parity cap fails}\}
\le
2D^2e^{-(D-1)/4}.
\tag{6.2}
$$

Put \(t=(D-1)/4\). Since \(e^t>t^3/6\),

$$
2D^2e^{-t}
<
\frac{768D^2}{(D-1)^3}.
$$

The exact proposed certificate holds because

$$
\begin{aligned}
(D-1)^3-768D^2
&=
D^2(D-771)+3D-1\\
&>0.
\end{aligned}
$$

Thus

$$
\boxed{
2D^2e^{-(D-1)/4}<1.
}
\tag{Union}
$$

There is therefore a positive-measure open set of compatible phases satisfying all parity caps strictly.

---

## 6.1 The analytic zero-set step

The function

$$
\theta\longmapsto1-C(\alpha(\theta))
$$

is a finite real trigonometric polynomial and hence real analytic. It is not identically zero because the affine-character phase points satisfy CharacterGap.

A nonzero real-analytic function on a finite-dimensional torus has a zero set of Haar measure zero. This follows, for example, by repeatedly restricting to one angle: a nonzero one-variable analytic function has isolated zeros, and induction handles the exceptional lower-dimensional restrictions.

Therefore the positive-measure parity-success set contains phases with

$$
C(\alpha)<1.
$$

Because that success set is open and rational angles are dense, one may choose all phases to be rational multiples of \(2\pi\), hence roots of unity.

The proposed analytic argument is valid. The next section gives a stronger finite sign version with an explicit cubic gap.

---

# 7. Stronger result: exact sign phases with \(C<2/15\)

Choose independent signs

$$
\varepsilon_z\in\{-1,+1\},
\qquad z\in\mathcal H,
$$

and set

$$
\alpha_0=1,
\qquad
\alpha_z=\alpha_{-z}=r_z\varepsilon_z.
\tag{7.1}
$$

These are exact algebraic phases.

The same Hoeffding calculation applies, because each Wigner sum is now a sum of independent centered variables

$$
2r_z\varepsilon_z
\cos\left(\frac{2\pi[a,z]}D\right).
$$

Let \(E\) be the event that every parity cap is strict, and set

$$
\varepsilon_{\rm bad}
=
\Pr(E^c).
$$

Then

$$
\varepsilon_{\rm bad}
\le
2D^2e^{-(D-1)/4}.
$$

A slightly stronger elementary estimate gives

$$
\boxed{\varepsilon_{\rm bad}<\frac1{16}.}
\tag{7.2}
$$

Indeed,

$$
\varepsilon_{\rm bad}
<
\frac{768D^2}{(D-1)^3},
$$

while \(D-1>D/2\) and \(D>98304\) imply

$$
\frac{768D^2}{(D-1)^3}
<
\frac{6144}{D}
<
\frac1{16}.
$$

## 7.1 Expected cubic

In the cubic sum

$$
C(\alpha)
=
\frac1{D^2}
\sum_{u,v}
\alpha_u\alpha_v\alpha_{-u-v}
\omega^{[u,v]/2},
$$

a sign monomial has nonzero expectation only if every nonzero inverse-pair sign appears an even number of times.

With three coefficient factors, the surviving triples are precisely:

* \((0,0,0)\);
* the three ordered placements of \((0,z,-z)\), for each \(z\ne0\).

All corresponding Weyl phases equal \(1\). Therefore

$$
\begin{aligned}
\mathbb E C(\alpha)
&=
\frac1{D^2}
\left[
1+3\sum_{z\ne0}r_z^2
\right]\\
&=
\boxed{
\frac{3D-2}{D^2}.
}
\tag{7.3}
$$

Since \(D>48\),

$$
\mathbb E C(\alpha)<\frac1{16}.
\tag{7.4}
$$

For every phase assignment, the eigenvalues of \(R_\alpha\) lie in
\([-1,1]\) because \(\operatorname{Tr}R_\alpha^2=1\). Hence

$$
-1\le C(\alpha)\le1.
$$

Let

$$
c_E=\inf_{\alpha\in E}C(\alpha).
$$

Then

$$
\mathbb E C(\alpha)
\ge
c_E(1-\varepsilon_{\rm bad})-\varepsilon_{\rm bad}.
$$

Consequently,

$$
c_E
\le
\frac{
\mathbb E C+\varepsilon_{\rm bad}
}{
1-\varepsilon_{\rm bad}
}
<
\frac{1/16+1/16}{15/16}
=
\boxed{\frac{2}{15}}.
\tag{7.5}
$$

Therefore there exists an exact sign assignment \(\varepsilon^\star\) such that

$$
\boxed{
-1<w_a(\alpha^\star)<1\quad\forall a,
\qquad
C(\alpha^\star)<\frac{2}{15}.
}
\tag{7.6}
$$

Because the orbit-Gram diagonal-dominance threshold depends only on the magnitudes, this same field passes every orbit-Gram PSD test involving at most \(135{,}873{,}435\) distinct labels.

It also retains the frozen objective \(>10\), since Bell–Fourier depends only on \(x_z=|\alpha_z|^2\).

This proves a quantitatively stronger statement than the proposed analytic `ParityBreak`:

$$
\boxed{
\begin{gathered}
\text{SF, LC, TriGram, ConvMag, every ParityCap,}\\
\text{and all audited small orbit-Gram tests}
\end{gathered}
\quad\nRightarrow\quad
C(\alpha)=1.
}
\tag{7.7}
$$

The sign field is nonphysical precisely because its cubic is far below \(1\).

---

# 8. A quantitative global idempotence constraint

Define the twisted-convolution coefficient

$$
Q_k(\alpha)
=
\frac1D
\sum_u
\alpha_u\alpha_{k-u}
\omega^{[u,k]/2}.
$$

Then

$$
R_\alpha^2
=
\frac1D\sum_kQ_k(\alpha)W_k.
$$

Put

$$
\Delta_k(\alpha)=Q_k(\alpha)-\alpha_k.
$$

Weyl Parseval gives

$$
\boxed{
\frac1D\sum_k|\Delta_k(\alpha)|^2
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
}
\tag{8.1}
$$

Let \(\mu_j\) be the eigenvalues of \(R_\alpha\). Then

$$
1-C(\alpha)
=
\sum_j\mu_j^2(1-\mu_j).
$$

Cauchy–Schwarz, using \(\sum_j\mu_j^2=1\), gives

$$
\begin{aligned}
(1-C(\alpha))^2
&\le
\sum_j\mu_j^2(1-\mu_j)^2\\
&=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
\end{aligned}
$$

Thus every coefficient field satisfies the exact global sum-of-squares bound

$$
\boxed{
\frac1D\sum_k|\Delta_k(\alpha)|^2
\ge
(1-C(\alpha))^2.
}
\tag{8.2}
$$

For the sign field in (7.6),

$$
1-C(\alpha^\star)>\frac{13}{15},
$$

so

$$
\boxed{
\sum_k|\Delta_k(\alpha^\star)|^2
>
\frac{169}{225}D.
}
\tag{8.3}
$$

Physical pure-state coefficients require every \(\Delta_k=0\). Equation (8.3) therefore gives a quantitative global separation of an exact algebraic field that passes all parity caps and all audited local Gram tests.

This is one scalar degree-four sum-of-squares constraint. In compact form it has \(D^2\) residual coordinates; each residual contains \(D^2\) twisted-convolution terms. A fully expanded evaluation has \(D^4\) indexing cost.

---

# 9. What remains unresolved for \(x^{(10)}\)

The parity layer is now decisively separated from the physical phase-lift set:

* every affine-character phase is excluded, with cubic gap \(>1/32\);
* nevertheless, exact sign phases exist that satisfy **all** parity caps and all previously audited local or magnitude constraints;
* those sign phases can have cubic \(<2/15\), so the parity layer does not even force the cubic close to its physical value \(1\).

What is not proved is a statement uniform over all compatible phases:

$$
\boxed{
\max_{\theta}C_{10}(\theta)<1.
}
$$

No phase assignment with \(C=1\) is constructed, and no positive phase-uniform gap

$$
C_{10}(\theta)\le1-\eta
$$

is established.

The quantitative sign witness only proves that some phases are very nonphysical. It does not rule out a different phase assignment lifting the same magnitudes to a rank-one projector.

There is also a useful exact interpretation of the baseline magnitude profile

$$
b_0=1,\qquad b_z=\frac1{D+1}\quad(z\ne0).
$$

A pure-state phase lift of \(b\) would produce a Weyl orbit of \(D^2\) unit vectors whose distinct squared overlaps are all \(1/(D+1)\). Thus even the unperturbed baseline phase-lift problem is an exact Weyl-covariant equiangular-line construction. The perturbation \(x^{(10)}\) retains the same genuinely global phase-retrieval difficulty.

Accordingly, PW10 itself remains open.

---

# Audit ledger

## PROVED

* The exact rational value of \(U\), both square gaps, and

  $$
  135873434<1/\sqrt U<135873435.
  $$
* The bounds

  $$
  \frac1{2(D+1)}
  \le x_z^{(10)}<U<\frac1{16}
  \quad(z\ne0).
  $$
* The exact frozen objective lower bound \(>10\).
* Every compatible phase assignment passes all orbit-Gram PSD tests on at most \(135{,}873{,}435\) distinct labels.
* The parity expansion

  $$
  \Pi=D^{-1}\sum_zW_z.
  $$
* \(\Pi^2=I\), \(\operatorname{Tr}\Pi=1\), and
  \(\operatorname{Tr}(\Pi W_z)=1\).
* The displaced-parity expansion and Wigner formula.
* Orthogonality of the \(D^2\) displaced parities.
* The global identities

  $$
  \sum_aw_a=\sum_aw_a^2=D.
  $$
* The affine-character conjugacy \(R_c=W_cR_0W_c^*\).
* The commutation \([R_c,\Pi_c]=0\).
* The matching parity expectation

  $$
  w_c=D^{-1}\sum_z\sqrt{x_z^{(10)}}>1.
  $$
* Exclusion of every affine-character phase.
* The uniform character-orbit bound

  $$
  C(\alpha^{(c)})<31/32.
  $$
* The random-phase Hoeffding bound and the exact union-bound certificate.
* The real-analytic zero-set and rational-angle density steps.
* The stronger exact sign-phase existence result:

  $$
  \text{all ParityCaps strict},\qquad C<2/15.
  $$
* The quantitative global idempotence-residual bound

  $$
  \sum_k|\Delta_k|^2>\frac{169}{225}D
  $$

  for such a sign field.

## DISPROVED

* Physicality of any affine-character phase field.
* Sufficiency of all displaced-parity caps for cubic lifting.
* Sufficiency of

  $$
  \text{SF+LC+TriGram+ConvMag+ParityCap}
  $$

  even when supplemented by every audited small orbit-Gram PSD test.
* The implication labeled `ParityCap \(\Rightarrow C=1\)` in any form.

## NECESSARY-ONLY

* Every individual ParityCap.
* The \(D^2\)-constraint displaced-parity layer.
* SF, LC, TriGram, and ConvMag.
* Finite principal orbit-Gram positivity.
* Vanishing of each twisted-idempotence residual \(\Delta_k\).

## SUFFICIENT-ONLY

* No new merely sufficient criterion for PW10 is asserted.

## EQUIVALENT

Under Hermiticity, trace one, and Hilbert–Schmidt purity one:

* \(C(\alpha)=1\);
* \(R_\alpha\) is positive semidefinite;
* \(R_\alpha\) is a rank-one projector;
* all twisted-idempotence residuals vanish;
* the full orbit matrix is positive semidefinite;
* \(\alpha\) is a physical pure-state coefficient field.

## OPEN

* Whether \(x^{(10)}\) admits any compatible phase assignment with \(C=1\).
* Whether all compatible phases satisfy a uniform gap \(C\le1-\eta\).
* Whether a different frozen-objective-above-\(10\) magnitude profile has a physical lift.
* PW10 for the exact frozen tuple.

## CONJECTURED

* No statement is promoted to conjectured status.

The first new claim requiring independent verification is the quantitative sign-phase theorem:

$$
\exists\,\alpha^\star:
\quad
-1<w_a(\alpha^\star)<1\ \forall a,
\qquad
C(\alpha^\star)<\frac{2}{15},
$$

together with its global idempotence-residual consequence

$$
\sum_k|\Delta_k(\alpha^\star)|^2
>
\frac{169}{225}D.
$$

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-14-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-14-local-audit.md bytes=5811 sha256=e171e282ab08632da4ce27c5598de3411aacab7a4545e97e36f67a716cc3409f -->

# Round 14 local audit

- Audit completed (UTC): `2026-09-13T01:44:25Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-14-response.md`
- Web-response SHA-256:
  `bc42715023aaeec679e9d59091b27c3941729f2c13f037affc6cc27140f3fae6`
- Capture equality: the browser clipboard payload, artifact, and output copy
  are text-identical; the two files are byte-identical, each `19,514` bytes
  and `1,179` lines.

## Verdict

The substantive Round 14 claims pass independent convention, arithmetic,
combinatorial, and spectral checks.  The correct frozen-tuple status is still

\[
\boxed{\text{PW10 remains OPEN.}}
\]

The new sign-phase theorem is a valid exact existence theorem obtained by the
probabilistic method.  It is not an explicit enumeration or algorithm for the
`(D^2-1)/2` signs, and it does not provide a physical phase lift.

## Verified parity layer

For the frozen Weyl convention, direct small-prime matrix checks at
`D=3,5,7` verify all signs and normalizations in

\[
\Pi=D^{-1}\sum_zW_z,
\qquad
\Pi_a=D^{-1}\sum_z\omega^{[a,z]}W_z,
\]

\[
w_a=\operatorname{Tr}(\Pi_aR_\alpha)
=D^{-1}\sum_z\alpha_z\omega^{-[a,z]}.
\]

The parity dimensions `(D+1)/2` and `(D-1)/2`, orthogonality
`Tr(Pi_a Pi_b)=D delta_(a,b)`, and the global identities

\[
\sum_aw_a=D,
\qquad
\sum_aw_a^2=D
\]

are correct.  Positivity implies every ParityCap, but the caps are only
necessary.

For every affine-character field

\[
\alpha_z^{(c)}=\sqrt{x_z^{(10)}}\,\omega^{[c,z]},
\]

the conjugacy, parity commutation, and matching value
`w_c=D^{-1} sum_z sqrt(x_z^(10))>1` are correct.  The lower bound on this
value, the odd-block negative-trace argument, and Cauchy--Schwarz give the
strict uniform conclusion

\[
C(\alpha^{(c)})<31/32.
\]

This excludes exactly the `D^2` character orbit, not the continuous phase
torus.

## Verified random-phase separation

For continuous independent pair phases, the range-squared denominator in
Hoeffding is `8(D-1)`, so at threshold `D-1`

\[
\Pr\{|Y_a|\ge D-1\}
\le 2e^{-(D-1)/4}.
\]

The union bound over all `D^2` labels and the exact integer certificate

\[
(D-1)^3>768D^2
\]

are valid.  The strict-cap event therefore has positive measure.  Since
`1-C` is a nonzero nonnegative real-analytic function on the phase torus, its
zero set has measure zero.  Intersecting the two sets and then using density
of rational angles correctly gives algebraic root-of-unity phases with all
caps strict and `C<1`.

## Verified stronger sign-phase theorem

For independent Rademacher signs shared by each pair `{z,-z}`, the same
Hoeffding bound applies.  The stronger exact comparison

\[
(D-1)^3>12288D^2
\]

verifies that the probability of any cap failure is strictly below `1/16`.

The cubic-expectation classification is complete.  A cubic sign monomial has
nonzero expectation only for `(0,0,0)` or an ordered placement of
`(0,z,-z)`.  There are exactly `1+3(D^2-1)` such ordered terms, all with Weyl
phase one.  Hence

\[
\mathbb E C
=\frac{1+3\sum_{z\ne0}x_z^{(10)}}{D^2}
=\frac{3D-2}{D^2}<\frac1{16}.
\]

Combining this with `-1<=C<=1` and the cap-success probability proves that
some exact sign field has all caps strict and

\[
C<\frac{2}{15}.
\]

This is a sound finite probabilistic-existence argument.  It gives no named
sign vector, compact construction, or efficient recovery procedure.

## Verified idempotence residual

With

\[
Q_k=D^{-1}\sum_u\alpha_u\alpha_{k-u}\omega^{[u,k]/2},
\qquad
\Delta_k=Q_k-\alpha_k,
\]

the Weyl coefficient and Parseval normalizations are correct:

\[
D^{-1}\sum_k|\Delta_k|^2
=\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
\]

Spectral Cauchy--Schwarz gives

\[
D^{-1}\sum_k|\Delta_k|^2\ge(1-C(\alpha))^2.
\]

Thus the sign witness with `C<2/15` satisfies

\[
\sum_k|\Delta_k|^2>\frac{169}{225}D.
\]

This quantitatively separates that nonphysical witness from rank-one
idempotence, but it is not a phase-uniform inequality against every phase
assignment for the same magnitudes.

## Classification corrections

Two wording distinctions are needed.

1.  “Exact algebraic sign field” is correct as an existential statement:
    the finite probabilistic argument proves that at least one algebraic
    sign assignment exists.  It should not be described as an explicit field,
    because the response supplies neither the signs nor a deterministic rule
    selecting them.

2.  In the ledger, “vanishing of each residual” is ambiguous under
    `NECESSARY-ONLY`.  Any one equation `Delta_k=0` is only necessary, whereas
    simultaneous vanishing of all residuals is equivalent to physical
    rank-one lifting under the frozen trace, Hermiticity, and purity
    hypotheses.  The later `EQUIVALENT` entry states the collective version
    correctly.

No conclusion in the response determines whether another compatible phase
assignment for `x^(10)` reaches `C=1`.  Even a proof excluding this one
magnitude profile would not prove PW10 for all physical profiles.

## Earliest remaining gap

For the exact full-support profile,

\[
\eta_{10}=1-\max_\theta C_{10}(\theta)\ge0
\]

still has unknown sign.  The sign-phase theorem establishes that many phases
are far from physical; it provides neither a physical maximizer nor a
positive bound uniform over the entire compatible phase torus.

## Reproducibility

- `work/verify_round14_parity_bounds.py`
  SHA-256 `3f5f95384f9c04f13582f02126393d3aae9413a723b13c10d89b0ebb8bca71ab`
- `work/verify_round14_weyl_identities.py`
  SHA-256 `f6e54a44edf870b0c0f237062619e406cb86e79e071a6c7a7836e69b580b8253`
- `work/verify_round14_web_response.py`
  SHA-256 `bff3e7099e5e45c3f0e3a5f07c518b5b4f70354f2481b9dbcf752ab1cdaad840`

All three checkers print `PASS`; the Python files also pass bytecode
compilation.

<!-- END HISTORICAL FILE path=outputs/round-14-local-audit.md -->


# ROUND 015

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-15-prompt.md bytes=8595 sha256=439402f456d8ad637c1f0a2e97a273157a0e303c12b56f5a1e8edbc912b3cc88 -->

# Round 15 — audit the exact sign theorem, then pass from parity caps to full stabilizer-line positivity

Continue in the same ordinary Chat conversation and the same canonically
frozen finite `r=2`, low-`A` gate.  Give a public, self-contained derivation
and no hidden chain-of-thought.  Do not repeat the Round 8--13 narrative.

## Exact frozen boundary

Use exactly

\[
m=485165196,
\qquad P=485165237=m+41,
\]

\[
D=941541228773064677=4P^2+1,
\qquad i=2P,
\qquad i^2=-1\pmod D,
\]

\[
0\le j\le P-42,
\quad r_j=j^2\bmod P,
\quad t_j=2Pj+r_j,
\quad a_j=(t_j,t_j^2),
\]

\[
A=\{a_j\},
\qquad
\Gamma=(A-A)\setminus\{0\},
\qquad
M=m(m-1)=235385266924553220.
\]

The open gate is

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10
\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use

\[
W_{(p,q)}|y\rangle
=\omega^{p(y+q/2)}|y+q\rangle,
\quad
W_uW_v=\omega^{[u,v]/2}W_{u+v},
\quad
W_u^*=W_{-u}.
\]

The exact magnitude point remains

\[
b_0=1,
\qquad b_z=\frac1{D+1}\ (z\ne0),
\]

\[
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\quad
y=\mathbf1_\Gamma+\frac\lambda D,
\quad
d=y-\frac MD b,
\quad
\boxed{x^{(10)}=b+\frac{10}{M}d.}
\]

It is real, even, self-Fourier, has `x_0=1` and total mass `D`, satisfies
SF+LC+TriGram+ConvMag, and has frozen objective strictly above `10`.  For
every nonzero label,

\[
\frac1{2(D+1)}\le x_z^{(10)}<U<\frac1{16}.
\]

Every compatible phase field therefore passes all principal orbit-Gram tests
on at most `135873435` distinct labels.  This is phase-independent.

For

\[
R_\alpha=\frac1D\sum_z\alpha_zW_z,
\quad
\alpha_0=1,
\quad
\alpha_{-z}=\overline{\alpha_z},
\quad
|\alpha_z|^2=x_z^{(10)},
\]

one has `Tr R_alpha=Tr R_alpha^2=1` and the exact global equivalence

\[
C(\alpha):=\operatorname{Tr}R_\alpha^3=1
\iff R_\alpha\text{ is a rank-one projector}
\iff\alpha\text{ is a physical pure-state field}.
\tag{CubicLift}
\]

## Audited Round 14 boundary

The parity/Wigner formulas and all Fourier signs were independently checked:

\[
\Pi=D^{-1}\sum_zW_z,
\quad
\Pi_a=D^{-1}\sum_z\omega^{[a,z]}W_z,
\quad
w_a=D^{-1}\sum_z\alpha_z\omega^{-[a,z]}.
\]

Physical positivity requires `-1<=w_a<=1` for all `D^2` labels.

Every affine-character field

\[
\alpha_z^{(c)}=\sqrt{x_z^{(10)}}\,\omega^{[c,z]}
\]

is nonphysical and satisfies the uniform exact bound

\[
C(\alpha^{(c)})<31/32.
\]

Continuous random phases prove that all ParityCaps together are insufficient.
Round 14 strengthened this with independent signs shared by `{z,-z}`.  The
claimed sign-monomial classification gives

\[
\mathbb E C(\alpha)=\frac{3D-2}{D^2}<\frac1{16},
\]

while the probability that any ParityCap fails is below `1/16`.  Therefore a
finite probabilistic argument gives the existential theorem

\[
\exists\alpha^\star:\quad
-1<w_a(\alpha^\star)<1\ \forall a,
\qquad
C(\alpha^\star)<\frac2{15}.
\tag{SignExist}
\]

It also gives

\[
\sum_k\left|
\frac1D\sum_u\alpha_u^\star\alpha_{k-u}^\star
\omega^{[u,k]/2}-\alpha_k^\star
\right|^2
>\frac{169}{225}D.
\]

An independent exact checker found no missing cubic sign monomials and
verified all integer comparisons.  Treat `(SignExist)` as an exact
**existence** theorem, not as an explicitly listed sign vector or a physical
state.  It does not control the maximum of `C` over all phases.

## Proposed next exact layer: every stabilizer projector

Let `L=<v>` be one of the `D+1` isotropic lines through zero.  For
`k in F_D`, define

\[
P_{L,k}=\frac1D\sum_{t\in\mathbb F_D}\omega^{kt}W_{tv}.
\]

The proposed convention-correct marginal is

\[
\boxed{
p_{L,k}:=\operatorname{Tr}(R_\alpha P_{L,k})
=\frac1D\sum_t\alpha_{tv}\omega^{-kt}.
}
\tag{StabMarg}
\]

The full orbit-Gram principal matrix on the labels `{tv}` is

\[
B_L(s,t)=\alpha_{(s-t)v}.
\]

It should have eigenvalues `D p_(L,k)`, so

\[
\boxed{B_L\succeq0\iff p_{L,k}\ge0\quad\forall k.}
\tag{LinePSD}
\]

These are full `D x D` tests, not covered by the small-Gram threshold.
Physical positivity requires all `D(D+1)` stabilizer probabilities to be
nonnegative.

## Magnitude shadow and Radon identity

If one line has a nonnegative marginal `p_L`, its cyclic autocorrelation is

\[
q_{L,s}:=\sum_kp_{L,k}p_{L,k+s}
=\frac1D\sum_tx_{tv}^{(10)}\omega^{-st}.
\tag{LineAuto}
\]

Self-Fourier symmetry proposes the exact finite Radon formula

\[
\boxed{
q_{L,s}
=\frac1D\sum_{z:[v,z]=s}x_z^{(10)}>0.
}
\tag{Radon}
\]

In fact the pointwise lower bound should give

\[
q_{L,s}\ge\frac1{2(D+1)}\quad(s\ne0),
\qquad
q_{L,0}\ge\frac{3D+1}{2D(D+1)},
\]

and `sum_s q_(L,s)=1`.  Thus the entire magnitude-only autocorrelation shadow
passes strictly.  Do not assume that a nonnegative autocorrelation
automatically has a nonnegative cyclic convolution square root.

The nonzero labels partition among the `D+1` lines.  Hence phases used on
different lines are disjoint, and simultaneous stabilizer feasibility should
be equivalent to solving, independently for every line,

\[
\boxed{
p_{L,k}=\frac1D\sum_t
\sqrt{x_{tv}^{(10)}}e^{i\theta_{L,t}}\omega^{-kt}\ge0
\quad\forall k,
\qquad
\theta_{L,-t}=-\theta_{L,t}.
}
\tag{SpectralFactor}
\]

For the unperturbed baseline `b`, the all-positive line phases give

\[
p_{L,0}=\frac{1+(D-1)/\sqrt{D+1}}D,
\qquad
p_{L,k}=\frac{1-1/\sqrt{D+1}}D>0\quad(k\ne0).
\tag{BaselineFactor}
\]

## Same-line cubic bridge

Let `C_dep` denote the portion of `C` with `[u,v]=0`.  The proposed exact
decomposition is

\[
\boxed{
C_{\rm dep}
=\sum_L\sum_kp_{L,k}^3-\frac1D,
\qquad
\sum_L\sum_kp_{L,k}^2=2.
}
\tag{LineCubic}
\]

The subtraction corrects the overcounting of `(u,v)=(0,0)` across all lines.
The linearly independent pairs remain a genuinely cross-line phase problem.

## Exact tasks

1. Give one verdict for PW10 on this exact frozen tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**.

2. Independently audit `(SignExist)`: classify every cubic sign monomial,
   verify the conditional-expectation inequality and the residual
   normalization, and preserve its existential/nonconstructive status.

3. Prove or correct `(StabMarg)` and `(LinePSD)`, including projector rank,
   eigenvalue signs, the `D+1`-line partition, and all global counts.

4. Prove or correct `(LineAuto)`, `(Radon)`, both strict lower bounds, and the
   exact decoupling into cyclic spectral-factor problems.  Explicitly state
   why positivity of `q_L` is only a magnitude shadow unless you prove a
   nonnegative convolution-square-root theorem.

5. Settle `(SpectralFactor)` for the actual frozen `x^(10)` as far as exact
   proof permits.  In priority order:

   - give a deterministic phase rule for every line and prove every
     `p_(L,k)>=0`;
   - or exhibit one exact line together with a dual/trigonometric-polynomial
     certificate proving that no compatible phases can make all its
     marginals nonnegative;
   - or reduce the question to one explicit frozen-structure inequality
     involving the restriction of `lambda` or exact affine-line counts, and
     identify its first unproved estimate.

   You may test the all-positive radii against `(BaselineFactor)`, but a norm
   bound must be strong enough to preserve the displayed positive margin.
   Do not replace the enormous exact line by sampling or a generic unnamed
   SDP.

6. Prove or correct `(LineCubic)`.  If the stabilizer layer is feasible, use
   nonnegative marginals and the frozen structure to seek a rigorous bound on
   the linearly independent-pair contribution.  Do not assume that choosing
   line phases independently enforces the global cubic equality.

7. A genuinely closing advance must still be either a compatible phase field
   with `C=1` or an explicit `eta>0` valid for **every** compatible phase field
   of `x^(10)`.  A witness with small `C`, failure of one chosen phase rule,
   or feasibility of all stabilizer marginals is not such an advance.

8. Even exclusion of `x^(10)` would not prove PW10 for every physical
   magnitude profile.  Preserve that quantifier.  Do not return to the
   five-carry arithmetic, Perron--Schur10, or the all-`T` ratio without a new
   exact certificate for this same tuple.

9. End with a plain audit ledger separating **PROVED**, **DISPROVED**,
   **NECESSARY-ONLY**, **SUFFICIENT-ONLY**, **EQUIVALENT**, **OPEN**, and
   **CONJECTURED**.  State the first new claim requiring independent
   verification.

The purpose of this round is to replace the weak parity-cap layer by the full
stabilizer-projector layer, expose exactly what self-Fourier magnitudes already
guarantee, and isolate the first phase-coherent obstruction that still
couples different lines.

<!-- END HISTORICAL FILE path=work/round-15-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-15-response.md bytes=25441 sha256=21985d12bfdeb4d3bba3b2bad12a0885d072ba0092b9e76debf2a704341576f1 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The Round 14 sign theorem is correct as an exact nonconstructive existence result.

The full stabilizer-projector layer has the following exact structure:

* each \(P_{L,k}\) is a rank-one projector;
* the \(D\times D\) line orbit matrix has eigenvalues \(Dp_{L,k}\);
* simultaneous stabilizer positivity decomposes into \(D+1\) independent cyclic spectral-factor problems, one for each isotropic line;
* the autocorrelation shadow of every one of these problems is strictly positive for \(x^{(10)}\).

The strict positivity of the autocorrelation is not enough to produce a nonnegative spectral factor. For the actual frozen point, neither a phase rule solving every line nor an infeasible-line certificate is proved.

Conditional on linewise feasibility, the next obstruction is genuinely cross-line: physical cubic lifting would require linearly independent Weyl pairs to contribute at least

$$
1-2\sqrt{\frac3D}+\frac1D
>
0.9999999964.
$$

Moreover, independent character shifts on the lines preserve every stabilizer marginal but average the cross-line cubic contribution to zero. Thus, conditional on linewise feasibility, the entire stabilizer layer is still insufficient to force physicality.

---

# 1. Audit of the exact sign theorem

Choose one representative set \(\mathcal H\) from the nonzero inverse pairs

$$
\{z,-z\}\subset\mathbb F_D^2.
$$

Thus

$$
|\mathcal H|=\frac{D^2-1}{2}.
$$

Let

$$
r_z=\sqrt{x_z^{(10)}},
$$

choose independent signs

$$
\varepsilon_z\in\{-1,+1\},
\qquad z\in\mathcal H,
$$

and define

$$
\alpha_0=1,\qquad
\alpha_z=\alpha_{-z}=r_z\varepsilon_z.
$$

This satisfies

$$
\alpha_{-z}=\overline{\alpha_z},
\qquad
\sum_z|\alpha_z|^2=D.
$$

## 1.1 Parity-cap probability

For every phase-space point \(a\),

$$
Dw_a
=
1+
2\sum_{z\in\mathcal H}
r_z\varepsilon_z
\cos\left(\frac{2\pi[a,z]}D\right).
$$

Put

$$
Y_a
=
2\sum_{z\in\mathcal H}
r_z\varepsilon_z
\cos\left(\frac{2\pi[a,z]}D\right).
$$

The summands are independent and centered. The summand indexed by \(z\) lies in an interval of length at most \(4r_z\). Moreover,

$$
\sum_{z\in\mathcal H}r_z^2
=
\frac12\sum_{z\ne0}x_z^{(10)}
=
\frac{D-1}{2}.
$$

Hoeffding’s exponential-moment argument therefore gives

$$
\Pr\{|Y_a|\ge D-1\}
\le
2\exp\left(
-\frac{2(D-1)^2}
{16\sum_{z\in\mathcal H}r_z^2}
\right)
=
2e^{-(D-1)/4}.
$$

If \(|Y_a|<D-1\), then

$$
-1<w_a<1.
$$

A union bound over all \(D^2\) points gives

$$
\Pr\{\text{some parity cap is not strict}\}
\le
2D^2e^{-(D-1)/4}.
$$

Using

$$
e^t>\frac{t^3}{6},
\qquad
t=\frac{D-1}{4},
$$

one obtains

$$
2D^2e^{-(D-1)/4}
<
\frac{768D^2}{(D-1)^3}.
$$

Since \(D-1>D/2\) and \(D>98304\),

$$
\frac{768D^2}{(D-1)^3}
<
\frac{6144}{D}
<
\frac1{16}.
$$

Hence, with probability greater than \(15/16\), all parity caps are strict.

---

## 1.2 Complete classification of surviving cubic sign monomials

The cubic is

$$
C(\alpha)
=
\frac1{D^2}
\sum_{u,v}
\alpha_u\alpha_v\alpha_{-u-v}
\omega^{[u,v]/2}.
$$

A monomial has nonzero expectation only if each independent sign variable occurs an even number of times.

There are three coefficient factors. Consequently, the only surviving possibilities are:

1. the triple

   $$
   (u,v,-u-v)=(0,0,0);
   $$

2. one zero label and one inverse pair:

   $$
   (0,z,-z),\qquad
   (z,0,-z),\qquad
   (z,-z,0),
   \qquad z\ne0.
   $$

There are no further cases:

* three nonzero labels involving three different inverse-pair signs have three signs occurring once;
* two signs from one inverse pair and one from another leave one odd sign;
* three occurrences of one sign variable contribute
  \(\mathbb E\varepsilon_z^3=0\);
* because \(D\ne3\), a nonzero label cannot satisfy \(3z=0\).

Every surviving Weyl phase equals \(1\). Therefore

$$
\begin{aligned}
\mathbb EC(\alpha)
&=
\frac1{D^2}
\left[
1+
3\sum_{z\ne0}r_z^2
\right]\\
&=
\boxed{\frac{3D-2}{D^2}}.
\end{aligned}
$$

Since \(D>48\),

$$
\mathbb EC(\alpha)<\frac1{16}.
$$

---

## 1.3 Conditional-expectation argument

Let \(E\) be the event that all parity caps are strict, and let

$$
\varepsilon_{\rm bad}=\Pr(E^c)<\frac1{16}.
$$

For every phase assignment,

$$
-1\le C(\alpha)\le1.
$$

Indeed, if \(\mu_j\) are the eigenvalues of \(R_\alpha\), then

$$
\sum_j\mu_j^2=1
$$

and therefore

$$
|C(\alpha)|
=
\left|\sum_j\mu_j^3\right|
\le
\sum_j|\mu_j|^3
\le
\sum_j\mu_j^2
=1.
$$

Suppose every sign field in \(E\) satisfied \(C\ge2/15\). Then

$$
\begin{aligned}
\mathbb EC
&\ge
\frac{2}{15}(1-\varepsilon_{\rm bad})
-\varepsilon_{\rm bad}\\
&>
\frac{2}{15}\frac{15}{16}
-\frac1{16}\\
&=
\frac1{16},
\end{aligned}
$$

contradicting \(\mathbb EC<1/16\).

Hence there exists a sign field \(\alpha^\star\) such that

$$
\boxed{
-1<w_a(\alpha^\star)<1\quad\forall a,
\qquad
C(\alpha^\star)<\frac2{15}.
}
$$

This is an exact existential theorem over a finite sign space. It does not explicitly list the signs and does not construct a physical state.

---

## 1.4 Residual normalization

Define

$$
Q_k(\alpha)
=
\frac1D
\sum_u
\alpha_u\alpha_{k-u}
\omega^{[u,k]/2},
\qquad
\Delta_k=Q_k(\alpha)-\alpha_k.
$$

Then

$$
R_\alpha^2-R_\alpha
=
\frac1D\sum_k\Delta_kW_k.
$$

Weyl Parseval gives

$$
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2
=
\frac1D\sum_k|\Delta_k|^2.
$$

Also,

$$
1-C(\alpha)
=
\sum_j\mu_j^2(1-\mu_j).
$$

Cauchy–Schwarz, using \(\sum_j\mu_j^2=1\), yields

$$
\begin{aligned}
(1-C(\alpha))^2
&\le
\sum_j\mu_j^2(1-\mu_j)^2\\
&=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
\end{aligned}
$$

For the sign field above,

$$
1-C(\alpha^\star)>\frac{13}{15}.
$$

Therefore

$$
\boxed{
\sum_k|\Delta_k(\alpha^\star)|^2
>
\frac{169}{225}D.
}
$$

The Round 14 sign theorem and its normalization are correct.

---

# 2. Stabilizer projectors

Let

$$
L=\langle v\rangle
=
\{tv:t\in\mathbb F_D\}
$$

be an isotropic line, with \(v\ne0\). Define

$$
P_{L,k}
=
\frac1D
\sum_{t\in\mathbb F_D}
\omega^{kt}W_{tv}.
$$

Because all Weyl operators on \(L\) commute,

$$
W_{tv}W_{sv}=W_{(t+s)v}.
$$

## 2.1 Projection identities

Hermiticity follows from \(W_{tv}^*=W_{-tv}\):

$$
P_{L,k}^*
=
\frac1D\sum_t\omega^{-kt}W_{-tv}
=
P_{L,k}.
$$

Furthermore,

$$
\begin{aligned}
P_{L,k}P_{L,\ell}
&=
\frac1{D^2}
\sum_{t,s}
\omega^{kt+\ell s}W_{(t+s)v}\\
&=
\delta_{k,\ell}P_{L,k}.
\end{aligned}
$$

Also,

$$
\sum_{k\in\mathbb F_D}P_{L,k}=I.
$$

Only the \(t=0\) term contributes to the trace, so

$$
\operatorname{Tr}P_{L,k}=1.
$$

Thus:

$$
\boxed{
P_{L,k}\text{ is a rank-one orthogonal projector.}
}
$$

The operator \(W_{sv}\) acts on its range with eigenvalue

$$
\omega^{-ks}.
$$

Changing the generator \(v\) only permutes the label \(k\).

---

## 2.2 Marginal formula

For

$$
R_\alpha=\frac1D\sum_z\alpha_zW_z,
$$

one has

$$
\operatorname{Tr}(R_\alpha W_{tv})=\alpha_{-tv}.
$$

Therefore

$$
\begin{aligned}
p_{L,k}
&=
\operatorname{Tr}(R_\alpha P_{L,k})\\
&=
\frac1D
\sum_t
\omega^{kt}\alpha_{-tv}\\
&=
\boxed{
\frac1D
\sum_t
\alpha_{tv}\omega^{-kt}.
}
\end{aligned}
\tag{StabMarg}
$$

The Hermiticity relation

$$
\alpha_{-tv}=\overline{\alpha_{tv}}
$$

makes every \(p_{L,k}\) real.

Moreover,

$$
\sum_kp_{L,k}=\alpha_0=1.
$$

If \(R_\alpha\succeq0\), then

$$
p_{L,k}\ge0
$$

for every line and every \(k\).

---

# 3. The full line orbit matrix

Restrict the full orbit matrix to the labels \(sv,tv\in L\). Since

$$
[sv,tv]=0,
$$

the Weyl phase disappears:

$$
G_\alpha(sv,tv)
=
\overline{\alpha_{(t-s)v}}
=
\alpha_{(s-t)v}.
$$

Thus

$$
\boxed{
B_L(s,t)=\alpha_{(s-t)v}.
}
$$

For

$$
f_k(t)=D^{-1/2}\omega^{kt},
$$

one computes

$$
\begin{aligned}
(B_Lf_k)(s)
&=
D^{-1/2}
\sum_t
\alpha_{(s-t)v}\omega^{kt}\\
&=
D p_{L,k}f_k(s).
\end{aligned}
$$

Hence

$$
\boxed{
\operatorname{spec}B_L
=
\{Dp_{L,k}:k\in\mathbb F_D\}.
}
$$

Consequently,

$$
\boxed{
B_L\succeq0
\iff
p_{L,k}\ge0\quad\forall k.
}
\tag{LinePSD}
$$

This is an exact equivalence, not merely a necessary implication.

---

# 4. Global line count and decoupling

The nonzero vectors of \(\mathbb F_D^2\) partition into the \(D+1\) one-dimensional subspaces. Indeed,

$$
\frac{D^2-1}{D-1}=D+1.
$$

Thus:

* there are exactly \(D+1=941541228773064678\) isotropic lines;
* every nonzero Weyl label belongs to exactly one line;
* each line contains \(D-1\) nonzero labels.

The total number of stabilizer projectors is

$$
\boxed{
D(D+1)
=
886499885479492516151176935598179006.
}
$$

After imposing

$$
\theta_{L,-t}=-\theta_{L,t},
$$

the number of independent nonzero phase angles is

$$
(D+1)\frac{D-1}{2}
=
\frac{D^2-1}{2}.
$$

Because distinct lines share only the zero label, their phase variables are disjoint. Therefore:

$$
\boxed{
\begin{aligned}
&\text{There exists one coefficient field satisfying every stabilizer}\\
&\text{marginal inequality}\\
&\iff
\text{each of the }D+1\text{ linewise spectral-factor problems is feasible.}
\end{aligned}
}
\tag{4.1}
$$

The common coefficient \(\alpha_0=1\) causes no coupling between the line problems.

---

# 5. Autocorrelation of a line marginal

Assume the line phases have been chosen and put

$$
p_k=p_{L,k}.
$$

Define

$$
q_{L,s}
=
\sum_kp_kp_{k+s}.
$$

Using the line Fourier representation,

$$
p_k
=
\frac1D\sum_t\alpha_{tv}\omega^{-kt},
$$

one obtains

$$
q_{L,s}
=
\frac1D
\sum_t
x_{tv}^{(10)}\omega^{st}.
$$

Because \(x_{tv}^{(10)}=x_{-tv}^{(10)}\), this is equivalently

$$
\boxed{
q_{L,s}
=
\frac1D
\sum_t
x_{tv}^{(10)}\omega^{-st}.
}
\tag{LineAuto}
$$

---

# 6. Radon identity

Self-Fourier symmetry says

$$
x_u^{(10)}
=
\frac1D
\sum_zx_z^{(10)}\omega^{[u,z]}.
$$

Substituting \(u=tv\) into LineAuto gives

$$
\begin{aligned}
q_{L,s}
&=
\frac1{D^2}
\sum_zx_z^{(10)}
\sum_t
\omega^{t([v,z]-s)}\\
&=
\boxed{
\frac1D
\sum_{z:[v,z]=s}
x_z^{(10)}.
}
\tag{Radon}
\end{aligned}
$$

The affine set

$$
\{z:[v,z]=s\}
$$

contains exactly \(D\) points.

## 6.1 Strict lower bounds

For \(s\ne0\), that affine line does not contain \(0\). Hence every one of its \(D\) points satisfies

$$
x_z^{(10)}
\ge
\frac1{2(D+1)}.
$$

Therefore

$$
\boxed{
q_{L,s}\ge\frac1{2(D+1)}
\qquad(s\ne0).
}
$$

For \(s=0\), the line contains \(0\) and \(D-1\) nonzero points. Hence

$$
\begin{aligned}
q_{L,0}
&\ge
\frac1D
\left[
1+\frac{D-1}{2(D+1)}
\right]\\
&=
\boxed{
\frac{3D+1}{2D(D+1)}.
}
\end{aligned}
$$

Finally, the affine fibers partition phase space, so

$$
\boxed{
\sum_sq_{L,s}=1.
}
$$

All of the proposed Radon and lower-bound formulas are correct.

---

# 7. Why this is only a magnitude shadow

If \(p_L\ge0\), then \(q_L\) is its cyclic autocorrelation:

$$
q_{L,s}
=
\sum_kp_{L,k}p_{L,k+s}.
$$

Conversely, the data \(q_L\) determine only

$$
|\widehat p_L(t)|^2=x_{tv}^{(10)}.
$$

They do not determine the phases of \(\widehat p_L(t)\). Positivity of every \(q_{L,s}\), positive definiteness of the associated circulant matrix, and nonnegativity of its Fourier transform are insufficient by themselves to show that one can choose those phases so that the inverse Fourier transform is entrywise nonnegative.

The missing condition is exactly the existence of a **nonnegative cyclic spectral factor**:

$$
\boxed{
\exists\,p\in\mathbb R_+^D:
\quad
\sum_kp_k=1,\qquad
q_{L,s}=\sum_kp_kp_{k+s}\quad\forall s.
}
\tag{7.1}
$$

No theorem proving this for all of the frozen \(q_L\)'s is established here.

---

# 8. Exact frozen structure of each line restriction

The line problems can be reduced further to the projection of the frozen set \(A\).

Fix \(L=\langle v\rangle\), and define the projection multiplicities

$$
\nu_L(r)
=
\#\{j:[v,a_j]=r\},
\qquad r\in\mathbb F_D.
$$

Let

$$
\ell_L=|\Gamma\cap L|.
$$

Pairs of frozen points with equal projection are precisely the ordered differences lying in \(L\). Hence

$$
\boxed{
\ell_L
=
\sum_r\nu_L(r)(\nu_L(r)-1).
}
\tag{8.1}
$$

The independently audited line bound gives

$$
\ell_L\le2.
$$

Since \(\Gamma=-\Gamma\), \(\ell_L\) is even. Therefore

$$
\ell_L\in\{0,2\}.
$$

It follows that:

* if \(\ell_L=0\), every nonzero \(\nu_L(r)\) equals \(1\);
* if \(\ell_L=2\), exactly one projection value has multiplicity \(2\), and all other nonzero multiplicities equal \(1\).

Thus every projection of \(A\) is injective except possibly for one double point.

---

## 8.1 Affine-difference counts

Define

$$
N_L(s)
=
\#\{(a,b):a\ne b,\ [v,a_a-a_b]=s\}.
$$

Then

$$
\boxed{
N_L(s)
=
\sum_r\nu_L(r)\nu_L(r-s)-m\delta_{s,0}.
}
\tag{8.2}
$$

In particular,

$$
N_L(0)=\ell_L.
$$

For \(s\ne0\),

$$
\boxed{
N_L(s)\le m+1.
}
\tag{8.3}
$$

Indeed:

* in the injective case, \(N_L(s)\le m\);
* in the one-double case, write

  $$
  \nu_L=\mathbf1_S+\delta_{r_0},
  \qquad |S|=m-1,
  $$

  and expand the autocorrelation; the support-intersection term is at most
  \(m-1\), and the two double-point cross terms contribute at most \(2\).

---

## 8.2 Restriction of the Bell spectrum

For \(t\in\mathbb F_D\),

$$
\begin{aligned}
\sum_j\omega^{[a_j,tv]}
&=
\sum_r\nu_L(r)\omega^{-tr}.
\end{aligned}
$$

Hence

$$
\boxed{
\lambda_{tv}
=
\left|
\sum_r\nu_L(r)\omega^{-tr}
\right|^2-m.
}
\tag{8.4}
$$

Let

$$
\chi_L(s)
=
\sum_{t:tv\in\Gamma}\omega^{-st}.
$$

Because \(\Gamma\cap L\) is either empty or a pair \(\{\pm t_0v\}\),

$$
\chi_L(s)
=
\begin{cases}
0,&\ell_L=0,\\[2mm]
2\cos(2\pi st_0/D),&\ell_L=2.
\end{cases}
\tag{8.5}
$$

---

## 8.3 Exact formula for the autocorrelation shadow

Let

$$
q^b_s=
\begin{cases}
2/(D+1),&s=0,\\
1/(D+1),&s\ne0.
\end{cases}
$$

This is the baseline autocorrelation associated with \(b\).

From the exact definition of \(x^{(10)}\), equations (8.2)–(8.5) give

$$
\boxed{
q_{L,s}
=
q^b_s+
\frac{10}{MD}
\left[
N_L(s)+\chi_L(s)-M q^b_s
\right].
}
\tag{8.6}
$$

This is a completely explicit frozen-structure formula. Its inputs are:

* the almost-injective projection multiplicities \(\nu_L\);
* the affine-difference counts \(N_L(s)\);
* the at-most-two-point line character \(\chi_L(s)\).

At \(s=0\),

$$
\boxed{
q_{L,0}
=
\frac{2(D-10)}{D(D+1)}
+
\frac{20\ell_L}{MD}.
}
\tag{8.7}
$$

Thus the line purities take only two possible values.

Since every nonzero difference lies on exactly one line,

$$
\#\{L:\ell_L=2\}
=
\frac M2
=
117692633462276610,
$$

while

$$
\#\{L:\ell_L=0\}
=
D+1-\frac M2
=
823848595310788068.
$$

---

# 9. The deterministic all-positive phase rule

For the baseline \(b\), put

$$
c=\frac1{\sqrt{D+1}}.
$$

The all-positive Fourier phases give

$$
p^b_{L,0}
=
\frac{1+(D-1)c}{D},
$$

and, for \(k\ne0\),

$$
p^b_{L,k}
=
\frac{1-c}{D}>0.
$$

For the actual frozen restriction, define

$$
X_L(t)=x^{(10)}_{tv}.
$$

Its exact frozen formula is

$$
\boxed{
X_L(t)
=
b_{tv}
+
\frac{10}{M}
\left[
\mathbf1_\Gamma(tv)
+
\frac{
\left|\sum_r\nu_L(r)\omega^{-tr}\right|^2-m
}{D}
-
\frac MD\,b_{tv}
\right].
}
\tag{9.1}
$$

Choose the all-positive line phases

$$
\alpha_{tv}=\sqrt{X_L(t)}.
$$

The resulting marginal is

$$
p^+_{L,k}
=
\frac1D
\sum_t\sqrt{X_L(t)}\,\omega^{-kt}.
$$

Because \(X_L(t)=X_L(-t)\), this is real.

For \(k=0\), it is strictly positive. For \(k\ne0\), use

$$
\sum_{t\ne0}\omega^{-kt}=-1
$$

to obtain

$$
\boxed{
Dp^+_{L,k}
=
1-c+
\sum_{t\ne0}
\left(\sqrt{X_L(t)}-c\right)
\cos\left(\frac{2\pi kt}{D}\right).
}
\tag{9.2}
$$

Therefore the explicit frozen inequality

$$
\boxed{
\sum_{t\ne0}
\left(\sqrt{X_L(t)}-c\right)
\cos\left(\frac{2\pi kt}{D}\right)
\ge-(1-c)
}
\tag{9.3}
$$

for every \(L\) and every \(k\ne0\) would give a deterministic simultaneous solution of all stabilizer marginals.

This is the first unproved estimate in the all-positive phase route.

The available pointwise bounds on \(X_L(t)\) are not strong enough to prove (9.3): the naive triangle and Cauchy–Schwarz estimates lose factors growing with \(D\), while the positive margin \(1-c\) in (9.3) is order one.

No line is proved infeasible either. Thus the actual frozen SpectralFactor problem remains open.

---

# 10. Exact decoupling of the full stabilizer layer

For each line \(L\), choose phases satisfying

$$
\alpha_{-tv}=\overline{\alpha_{tv}}.
$$

Then

$$
p_{L,k}
=
\frac1D
\sum_t
\alpha_{tv}\omega^{-kt}.
$$

Because every nonzero label belongs to one line only, the phase choices on different lines are independent. Consequently:

$$
\boxed{
\begin{aligned}
&\text{All }D(D+1)\text{ stabilizer probabilities can be made nonnegative}\\
&\iff
\text{each one of the }D+1\text{ cyclic spectral-factor problems is feasible.}
\end{aligned}
}
\tag{10.1}
$$

Strict positivity of all \(q_{L,s}\) proves that every magnitude shadow passes. It does not settle either side of (10.1).

---

# 11. Audit of the same-line cubic formula

For one line,

$$
p_{L,k}
=
\frac1D
\sum_t\alpha_{tv}\omega^{-kt}.
$$

Expanding the third moment,

$$
\begin{aligned}
\sum_kp_{L,k}^3
&=
\frac1{D^3}
\sum_{r,s,t}
\alpha_{rv}\alpha_{sv}\alpha_{tv}
\sum_k\omega^{-k(r+s+t)}\\
&=
\frac1{D^2}
\sum_{r,s}
\alpha_{rv}\alpha_{sv}\alpha_{-(r+s)v}.
\end{aligned}
\tag{11.1}
$$

On a common line,

$$
[rv,sv]=0,
$$

so (11.1) is exactly the portion of the global cubic indexed by pairs \(u,v\in L\).

Every linearly dependent ordered pair \((u,v)\ne(0,0)\) lies on one unique line. The pair \((0,0)\) lies on all \(D+1\) lines. Its global cubic contribution is \(1/D^2\), so summing the line cubics overcounts it \(D\) times. Therefore

$$
\boxed{
C_{\rm dep}
=
\sum_L\sum_kp_{L,k}^3-\frac1D.
}
\tag{LineCubic}
$$

This formula is correct.

---

## 11.1 Second moments

Line Parseval gives

$$
\sum_kp_{L,k}^2
=
\frac1D\sum_t|\alpha_{tv}|^2
=
q_{L,0}.
$$

Summing over the \(D+1\) lines counts \(x_0=1\) exactly \(D+1\) times and each nonzero \(x_z\) once:

$$
\begin{aligned}
\sum_L\sum_kp_{L,k}^2
&=
\frac1D
\left[
(D+1)x_0+\sum_{z\ne0}x_z
\right]\\
&=
\frac1D[(D+1)+(D-1)]\\
&=
\boxed{2.}
\end{aligned}
$$

Thus the proposed second identity is also correct.

---

# 12. Bounds on the same-line cubic under stabilizer feasibility

Assume now that all stabilizer marginals are nonnegative. Then each \(p_L\) is a probability distribution:

$$
p_{L,k}\ge0,\qquad
\sum_kp_{L,k}=1.
$$

Put

$$
q_L=q_{L,0}=\sum_kp_{L,k}^2.
$$

For every probability vector,

$$
\left(\sum_kp_k^2\right)^2
\le
\sum_kp_k^3,
\tag{12.1}
$$

by Cauchy–Schwarz:

$$
\left(\sum_kp_k^{3/2}p_k^{1/2}\right)^2
\le
\left(\sum_kp_k^3\right)\left(\sum_kp_k\right).
$$

Also,

$$
\sum_kp_k^3
\le
\left(\sum_kp_k^2\right)^{3/2},
\tag{12.2}
$$

because

$$
\max_kp_k\le\sqrt{\sum_kp_k^2}.
$$

From (8.7) and \(\ell_L\le2\),

$$
0<q_L<\frac3D.
$$

Moreover,

$$
\sum_Lq_L=2.
$$

Therefore

$$
\begin{aligned}
\sum_Lq_L^2
&\ge
\frac{(\sum_Lq_L)^2}{D+1}
=
\frac4{D+1},
\end{aligned}
$$

and

$$
\sum_Lq_L^{3/2}
\le
\sqrt{\frac3D}\sum_Lq_L
=
2\sqrt{\frac3D}.
$$

Using LineCubic,

$$
\boxed{
\frac{3D-1}{D(D+1)}
\le
C_{\rm dep}
<
2\sqrt{\frac3D}-\frac1D.
}
\tag{12.3}
$$

Numerically,

$$
C_{\rm dep}<3.571\times10^{-9}.
$$

If a phase field were physical, then \(C=1\). Its linearly independent-pair contribution

$$
C_{\rm ind}=C-C_{\rm dep}
$$

would therefore have to satisfy

$$
\boxed{
C_{\rm ind}
>
1-2\sqrt{\frac3D}+\frac1D
>
0.9999999964.
}
\tag{12.4}
$$

This is the first exact cross-line phase-coherence burden exposed by the full stabilizer layer.

---

# 13. Independent line shifts kill the cross-line cubic on average

Assume, conditionally, that every line spectral-factor problem is feasible. Choose one feasible coefficient field on each line.

Fix, for each line \(L=\langle v_L\rangle\), a generator \(v_L\). For independently chosen

$$
\kappa_L\in\mathbb F_D,
$$

replace

$$
\alpha_{tv_L}
\longmapsto
\alpha_{tv_L}\omega^{\kappa_Lt}.
\tag{13.1}
$$

This preserves:

* all magnitudes \(x_{tv_L}\);
* Hermiticity;
* the line autocorrelation;
* line positivity.

Indeed,

$$
p_{L,k}
\longmapsto
p_{L,k-\kappa_L},
$$

so the line marginal is merely cyclically permuted.

The dependent cubic \(C_{\rm dep}\) is also unchanged, because

$$
t+s-(t+s)=0
$$

within one line.

Now consider a linearly independent pair \(u,v\). Then

$$
u,\qquad v,\qquad -u-v
$$

are nonzero and lie on three distinct lines. The corresponding cubic term acquires a product of three independent line characters. Averaging over the independent \(\kappa_L\)'s makes this term zero.

Hence

$$
\boxed{
\mathbb E_{\{\kappa_L\}}C_{\rm ind}=0,
\qquad
\mathbb E_{\{\kappa_L\}}C=C_{\rm dep}.
}
\tag{13.2}
$$

Therefore some choice of line shifts satisfies

$$
C\le C_{\rm dep}
<
2\sqrt{\frac3D}-\frac1D
<1.
$$

This proves the conditional statement:

> If every frozen line spectral-factor problem is feasible, then there exists a global coefficient field with the magnitudes \(x^{(10)}\) that satisfies every stabilizer-projector positivity condition but is nonphysical.

Thus even the complete stabilizer-projector layer would not, by itself, enforce cubic lifting.

This does **not** exclude a different choice of cross-line phases with \(C=1\).

---

# 14. Earliest remaining gaps

For the specific obstruction \(x^{(10)}\), there are now two successive unresolved gates.

## 14.1 Linewise gate

For every isotropic line \(L\), determine whether the explicitly known sequence

$$
q_{L,s}
=
q^b_s+
\frac{10}{MD}
\left[
N_L(s)+\chi_L(s)-Mq^b_s
\right]
$$

has a nonnegative cyclic spectral factor.

Equivalently, determine whether phases can be chosen so that all

$$
p_{L,k}
=
\frac1D\sum_t
\sqrt{x_{tv}^{(10)}}e^{i\theta_{L,t}}
\omega^{-kt}
$$

are nonnegative.

No deterministic phase rule and no infeasible-line certificate is proved.

The first explicit unproved estimate for the natural all-positive rule is (9.3).

## 14.2 Cross-line gate

Even if every line is feasible, physical lifting requires the linearly independent cubic terms to contribute almost exactly one:

$$
C_{\rm ind}>0.9999999964.
$$

Independent character shifts show that stabilizer positivity imposes no automatic positive lower bound of this scale on \(C_{\rm ind}\).

No compatible phases with \(C=1\) are constructed, and no phase-uniform bound

$$
C\le1-\eta
$$

is proved.

PW10 therefore remains open.

Excluding \(x^{(10)}\) would still not prove PW10 for all physical magnitude profiles.

---

# Audit ledger

## PROVED

* The complete cubic sign-monomial classification.
* The expectation

  $$
  \mathbb EC=\frac{3D-2}{D^2}.
  $$
* The parity-cap Hoeffding and union-bound estimates.
* The exact existential sign theorem

  $$
  \exists\alpha^\star:
  \quad
  -1<w_a(\alpha^\star)<1\ \forall a,
  \qquad
  C(\alpha^\star)<2/15.
  $$
* The residual bound

  $$
  \sum_k|\Delta_k(\alpha^\star)|^2>
  \frac{169}{225}D.
  $$
* \(P_{L,k}\) is a rank-one orthogonal projector.
* The marginal formula StabMarg.
* The line orbit matrix is circulant with eigenvalues \(Dp_{L,k}\).
* LinePSD.
* The exact global count \(D(D+1)\) of stabilizer projectors.
* The partition of nonzero Weyl labels among \(D+1\) lines.
* LineAuto and Radon, with the conventionally correct Fourier sign.
* Both strict Radon lower bounds.
* The exact linewise decoupling of stabilizer feasibility.
* The projection multiplicity identity

  $$
  \ell_L=\sum_r\nu_L(r)(\nu_L(r)-1).
  $$
* Every line projection is injective except possibly for one double point.
* The affine-count formula for \(N_L(s)\) and the bound

  $$
  N_L(s)\le m+1\quad(s\ne0).
  $$
* The exact restriction

  $$
  \lambda_{tv}
  =
  \left|\sum_r\nu_L(r)\omega^{-tr}\right|^2-m.
  $$
* The exact frozen autocorrelation formula (8.6).
* BaselineFactor.
* LineCubic.
* The identity

  $$
  \sum_L\sum_kp_{L,k}^2=2.
  $$
* Under stabilizer feasibility, the bounds (12.3) on \(C_{\rm dep}\).
* The resulting cross-line burden (12.4).
* Conditional on linewise feasibility, independent character shifts preserve every stabilizer marginal and average the cross-line cubic to zero.

## DISPROVED

* Sufficiency of all ParityCaps for physicality, by the audited sign theorem.
* No additional unconditional statement is disproved in this round.
* In particular, stabilizer feasibility for \(x^{(10)}\) is not disproved.

## NECESSARY-ONLY

* Nonnegativity of all \(D(D+1)\) stabilizer marginals.
* Positivity of every line orbit matrix.
* The autocorrelation shadow \(q_{L,s}\).
* The Radon lower bounds.
* The near-unit cross-line cubic burden required by a physical lift.

## SUFFICIENT-ONLY

* The all-positive phase inequalities (9.3) are sufficient to solve every line, but they are not proved for the frozen tuple.
* A nonnegative cyclic spectral factor for each \(q_L\) is sufficient and necessary for stabilizer feasibility, but its existence remains open.

## EQUIVALENT

* For a fixed line:

  $$
  B_L\succeq0
  \iff
  p_{L,k}\ge0\quad\forall k.
  $$
* Globally:

  $$
  \text{all stabilizer marginals feasible}
  \iff
  \text{all }D+1\text{ line spectral-factor problems feasible}.
  $$

## OPEN

* SpectralFactor for each actual frozen line restriction.
* The all-positive line inequality (9.3).
* Whether some line admits an exact infeasibility certificate.
* Whether \(x^{(10)}\) has any global phase lift with \(C=1\).
* Whether every compatible phase field has a uniform cubic gap.
* PW10 for the exact frozen tuple.

## CONJECTURED

* No statement is promoted to conjectured status.

The first new claim requiring independent verification is the conditional random-line-character theorem:

$$
\text{linewise stabilizer feasibility}
\Longrightarrow
\exists\text{ stabilizer-positive phase field with }
C\le C_{\rm dep}<1.
$$

Its proof uses the exact separation between same-line and linearly independent cubic terms and the independent cyclic shifts of the \(D+1\) line marginals.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-15-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-15-local-audit.md bytes=7279 sha256=14f471a8ea0b7716ecacaf6fe340e2c39356b1d3b62a0359521a652edcd3759c -->

# Round 15 local audit

- Audit completed (UTC): `2026-09-13T02:14:37Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-15-response.md`
- Web-response SHA-256:
  `21985d12bfdeb4d3bba3b2bad12a0885d072ba0092b9e76debf2a704341576f1`
- Capture equality: the browser clipboard payload, artifact, and output copy
  are text-identical; the two files are byte-identical, each `25,441` bytes
  and `1,640` lines.

## Verdict

The substantive Round 15 claims pass independent convention, exact
arithmetic, finite-geometry, and small-prime matrix checks.  The correct
frozen-tuple status remains

\[
\boxed{\text{PW10 remains OPEN.}}
\]

The round gives a genuine stronger relaxation and a useful conditional
cross-line theorem.  It neither solves the actual cyclic spectral-factor
problems nor constructs/excludes a physical phase lift of `x^(10)`.

## Round 14 sign theorem

The response correctly rederives the finite Rademacher argument.  The only
surviving expected cubic terms are `(0,0,0)` and the three zero-position
families `(0,z,-z)`, with the orientation counted by summing over every
nonzero `z`.  Hence

\[
\mathbb E C=\frac{3D-2}{D^2}<\frac1{16}.
\]

The cap-success probability exceeds `15/16`, the conditional-expectation
argument is strict in the correct direction, and the existential conclusion
`C<2/15` follows.  The residual Parseval normalization and the
`169D/225` lower bound are also correct.  This remains nonconstructive finite
existence, not a listed sign vector.

## Stabilizer projectors and full line matrices

For each isotropic line `L=<v>`, the sign convention in

\[
P_{L,k}=D^{-1}\sum_t\omega^{kt}W_{tv},
\qquad
p_{L,k}=D^{-1}\sum_t\alpha_{tv}\omega^{-kt}
\]

is correct.  The projectors are rank one, orthogonal, and sum to the identity.
The full line orbit matrix

\[
B_L(s,t)=\alpha_{(s-t)v}
\]

has eigenvalues `D p_(L,k)`.  Thus line PSD and nonnegativity of all line
marginals are exactly equivalent.

The global counts are exact:

\[
D+1=941541228773064678,
\]

\[
D(D+1)=886499885479492516151176935598179006.
\]

Because nonzero labels partition among the projective lines, all stabilizer
feasibility variables decouple line by line; the common value `alpha_0=1`
introduces no additional choice.

## Autocorrelation and frozen line structure

The line autocorrelation and Radon identities have the correct `D` factors
and Fourier signs:

\[
q_{L,s}=D^{-1}\sum_tx_{tv}^{(10)}\omega^{-st}
=D^{-1}\sum_{z:[v,z]=s}x_z^{(10)}.
\]

Both strict lower bounds and `sum_s q_(L,s)=1` are correct.  Small-prime
checks verify the displayed frozen refinement

\[
q_{L,s}=q_s^b+\frac{10}{MD}
\bigl(N_L(s)+\chi_L(s)-Mq_s^b\bigr).
\]

In this formula the inverse Fourier transform initially produces `N_L(-s)`;
the displayed `N_L(s)` is valid because the ordered difference set is
centrally symmetric.  Likewise `chi_L` is even when the line intersection is
the pair `+-t_0v`.

The projection-multiplicity identity is correct.  The audited line bound
forces `ell_L` to be `0` or `2`, so the projection is injective or has exactly
one double value.  Consequently exactly

\[
M/2=117692633462276610
\]

lines are occupied and `823848595310788068` are empty.  The two exact line
collision values sum to `2` with these multiplicities.

The response's bound `N_L(s)<=m+1` for nonzero `s` is valid but not sharp.
The support intersection is strictly smaller than its support because a
proper subset of the prime cyclic group cannot be invariant under a nonzero
shift.  Thus the same proof gives `N_L(s)<=m-1` in the injective case and
`N_L(s)<=m` in the one-double case.  This one-unit improvement does not settle
the spectral-factor inequality.

## Why the magnitude shadow does not solve the line problem

Strict positivity of `q_L` is necessary but is not a nonnegative spectral
factor.  An independent exact counterexample on `Z/5Z` makes this distinction
concrete:

\[
q_0=\frac{11}{25},
\quad q_{\pm1}=\frac1{100},
\quad q_{\pm2}=\frac{27}{100}.
\]

Every entry and every Fourier value is strictly positive, with nontrivial
Fourier values `(30+-13sqrt(5))/100`.  Yet a nonnegative probability factor
would obey the weighted five-cycle bound `q_2<=1/4`, contradicting
`q_2=27/100`.  Therefore the response is right not to promote Radon
positivity into line feasibility.

For the actual frozen line, the all-positive phase identity

\[
Dp^+_{L,k}=1-c+\sum_{t\ne0}
(\sqrt{X_L(t)}-c)\cos(2\pi kt/D)
\]

is correct.  The required lower bound `(9.3)` is genuinely unproved; the
available pointwise and norm bounds do not certify its order-one numerator
margin.

## Same-line cubic and conditional random-line theorem

The dependent-pair decomposition correctly subtracts the `D` extra copies of
the `(0,0)` pair:

\[
C_{\rm dep}=\sum_L\sum_kp_{L,k}^3-\frac1D.
\]

The complete-MUB collision identity `sum_(L,k) p_(L,k)^2=2` is also correct.
Conditional on nonnegative line marginals, the probability-vector moment
bounds give

\[
\frac{3D-1}{D(D+1)}
\le C_{\rm dep}
<2\sqrt{\frac3D}-\frac1D
<3.571\times10^{-9}.
\]

The exact decimal comparison was checked without floating-point assumptions.
A physical lift would consequently require

\[
C_{\rm ind}>1-2\sqrt{3/D}+1/D>0.9999999964.
\]

The new conditional random-line-character theorem is valid.  Multiplying the
coefficients on line `L` by `omega^(kappa_L t)` only cyclically permutes that
line's marginal.  Dependent triples are unchanged.  If `u,v` are linearly
independent, then `u`, `v`, and `-u-v` lie on three distinct lines, so
independent uniform line shifts annihilate that cubic term in expectation.
Therefore, conditional on feasibility of every line, some stabilizer-positive
global field satisfies

\[
C\le C_{\rm dep}<1.
\]

This proves only a conditional counterexample for the fixed magnitude
profile.  It does not prove that the antecedent is satisfiable, and it does
not rule out a different cross-line phase choice with `C=1`.

## Earliest remaining gaps

The first unresolved gate is now the exact nonnegative cyclic spectral-factor
problem for each frozen sequence `q_L`.  The natural all-positive rule reduces
to the response's inequality `(9.3)`, for which no uniform proof is known.

If all lines are feasible, the next gate is cross-line: either construct
phases giving `C_ind=1-C_dep`, or prove an explicit upper bound below that
required value for every compatible choice.  Neither result is present.

Even excluding `x^(10)` would still not prove PW10 for every physical
magnitude profile.

## Reproducibility

- `work/verify_round15_stabilizer_lines.py`
  SHA-256 `866871a16a94ca523ccf7787bb569ceca28b99dc79a728d605c03d6177618b2b`
- `work/verify_round15_cross_line.py`
  SHA-256 `9412197f466f08f98ebf2c3e1f6ad8d9b22ce8eaf90f9f0851aaf970db9cac5f`
- `work/verify_round15_web_response.py`
  SHA-256 `8b0f15f44af8f8c61e34c3ea41299f49174684dd25d5b72cf4caf0e4c19b18de`
- `work/round-15-independent-derivations.md`
  SHA-256 `894f24ec932ec22179b61dac75012c01fa5b6f843f80f9ba0b276d1043b118a9`
- `work/round-15-cross-line-independent.md`
  SHA-256 `9cbecb248cc9c7db002b88ea1a633847f780a6a774182ff6f1a5f797b492f353`

All three checkers print `PASS`; the Python files also pass bytecode
compilation.

<!-- END HISTORICAL FILE path=outputs/round-15-local-audit.md -->


# ROUND 016

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-16-prompt.md bytes=8286 sha256=8fa00354acf53a00aceae7a73762c4aedcce6bbd85a8cf5da6ba598b56f1d9ba -->

# Round 16 — attack the frozen line factors with exact Cayley-graph and circulant-copositive cuts

Continue in the same ordinary Chat conversation and the same canonically
frozen finite `r=2`, low-`A` gate.  Give a public, self-contained derivation
and no hidden chain-of-thought.  Do not repeat the Round 8--14 narrative.

## Exact frozen boundary

Use exactly

\[
m=485165196,
\quad P=485165237=m+41,
\quad D=941541228773064677=4P^2+1,
\]

\[
0\le j\le P-42,
\quad r_j=j^2\bmod P,
\quad t_j=2Pj+r_j,
\quad a_j=(t_j,t_j^2),
\]

\[
A=\{a_j\},
\quad
\Gamma=(A-A)\setminus\{0\},
\quad
M=m(m-1)=235385266924553220.
\]

The open gate remains

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10
\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use

\[
W_{(p,q)}|y\rangle=\omega^{p(y+q/2)}|y+q\rangle,
\quad
W_uW_v=\omega^{[u,v]/2}W_{u+v}.
\]

The exact full-support magnitude point is

\[
b_0=1,
\qquad b_z=\frac1{D+1}\ (z\ne0),
\]

\[
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\quad
y=\mathbf1_\Gamma+\lambda/D,
\quad
d=y-(M/D)b,
\quad
x^{(10)}=b+(10/M)d.
\]

It is positive, even, self-Fourier, has total mass `D`, passes every audited
magnitude and small-Gram condition, and has frozen objective strictly above
`10`.  A physical lift is equivalent to compatible phases with

\[
C(\alpha)=\operatorname{Tr}R_\alpha^3=1,
\qquad
R_\alpha=D^{-1}\sum_z\alpha_zW_z.
\]

PW10 remains open.

## Independently audited Round 15 boundary

For each isotropic line `L=<v>` and `k in F_D`, define

\[
P_{L,k}=D^{-1}\sum_t\omega^{kt}W_{tv},
\qquad
p_{L,k}=D^{-1}\sum_t\alpha_{tv}\omega^{-kt}.
\]

The `P_(L,k)` are rank-one stabilizer projectors.  The full line orbit matrix

\[
B_L(s,t)=\alpha_{(s-t)v}
\]

has eigenvalues `D p_(L,k)`.  Hence the entire stabilizer layer is feasible
for `x^(10)` if and only if all `D+1` linewise problems admit phases making
`p_(L,k)>=0`.

The magnitude shadow is

\[
q_{L,s}:=\sum_kp_{L,k}p_{L,k+s}
=D^{-1}\sum_tx_{tv}^{(10)}\omega^{-st}
=D^{-1}\sum_{z:[v,z]=s}x_z^{(10)}>0.
\]

Let

\[
\nu_L(r)=\#\{j:[v,a_j]=r\},
\qquad
\ell_L=|\Gamma\cap L|.
\]

Then

\[
\ell_L=\sum_r\nu_L(r)(\nu_L(r)-1)\in\{0,2\}.
\]

Thus the projection is injective or has exactly one double value.  Put

\[
N_L(s)=\sum_r\nu_L(r)\nu_L(r-s)-m\delta_{s,0},
\]

and

\[
\chi_L(s)=\sum_{t:tv\in\Gamma}\omega^{-st}.
\]

The exact frozen shadow is

\[
\boxed{
q_{L,s}=q_s^b+\frac{10}{MD}
\left[N_L(s)+\chi_L(s)-Mq_s^b\right],
}
\tag{FrozenShadow}
\]

where

\[
q_s^b=
\begin{cases}
2/(D+1),&s=0,\\
1/(D+1),&s\ne0.
\end{cases}
\]

The response proved `N_L(s)<=m+1` for `s!=0`.  The same support-shift argument
sharpens this to

\[
\boxed{N_L(s)\le m\quad(s\ne0),}
\tag{Nsharp}
\]

because a proper subset of the prime cyclic group cannot be invariant under a
nonzero shift.  Audit this sharpening.

At zero,

\[
q_{L,0}=\frac{2(D-10)}{D(D+1)}+\frac{20\ell_L}{MD}.
\]

Exactly `M/2=117692633462276610` lines have `ell_L=2`; all others have
`ell_L=0`.

The all-positive line phase rule is reduced exactly to

\[
1-c+\sum_{t\ne0}
\left(\sqrt{x_{tv}^{(10)}}-c\right)
\cos(2\pi kt/D)\ge0,
\qquad c=1/\sqrt{D+1},
\tag{PositiveRoot}
\]

for every line and nonzero `k`.  It is unproved.

Strict positivity of `q_L` is not sufficient for a nonnegative cyclic
spectral factor.  An independently checked exact counterexample on `Z/5Z` is

\[
q_0=11/25,
\quad q_{\pm1}=1/100,
\quad q_{\pm2}=27/100.
\]

All entries and all Fourier values are strictly positive, but any
nonnegative probability factor would obey the five-cycle bound
`q_2<=1/4`, contradicted by `q_2=27/100`.

Round 15 also proved, conditional on all lines being feasible,

\[
\frac{3D-1}{D(D+1)}
\le C_{\rm dep}
<2\sqrt{3/D}-1/D<3.571\times10^{-9}.
\]

Independent character shifts on the lines preserve all stabilizer marginals,
leave `C_dep` fixed, and average the linearly independent cubic part to zero.
This conditionally constructs a stabilizer-positive nonphysical field, but it
does not prove line feasibility and does not exclude another field with
`C=1`.

## New exact Cayley-graph cuts

Fix one line and suppose `q_s=sum_k p_k p_(k+s)` for a nonnegative probability
vector `p`.  For a symmetric connection set

\[
S=-S\subset\mathbb F_D\setminus\{0\},
\]

let `G_S=Cay(F_D,S)` and let `omega(G_S)` be its clique number.  The weighted
edge identity and Motzkin--Straus propose

\[
\boxed{
\sum_{s\in S}q_s
\le1-\frac1{\omega(G_S)}.
}
\tag{CayleyCut}
\]

Substitution of `(FrozenShadow)` gives

\[
\boxed{
\frac{|S|}{D+1}
+\frac{10}{MD}
\left[
N_L(S)+\chi_L(S)-\frac{M|S|}{D+1}
\right]
\le1-\frac1{\omega(G_S)},
}
\tag{FrozenCayleyCut}
\]

where `N_L(S)=sum_(s in S)N_L(s)` and similarly for `chi_L(S)`.

This cut detects the exact length-five counterexample by taking
`S={+-2}`.  For the frozen dimension, the first nearly complete choice

\[
S=\mathbb F_D^*\setminus\{a,-a\}
\]

has `omega(G_S)=(D-1)/2`; its complement cut is

\[
q_{L,0}+2q_{L,a}\ge2/(D-1),
\]

and the audited pointwise bounds prove the strictly stronger lower bound

\[
q_{L,0}+2q_{L,a}
\ge\frac{5D+1}{2D(D+1)}>\frac2{D-1}.
\]

Thus that easiest high-density cut passes.

## More general dual certificate

Let `h_s=h_(-s)` and let the symmetric circulant matrix `H_h` have entries

\[
(H_h)_{jk}=h_{k-j}.
\]

If `H_h` is copositive,

\[
p\ge0\Longrightarrow p^TH_hp\ge0,
\]

then every nonnegative spectral factor must satisfy

\[
\boxed{
\sum_sh_sq_{L,s}\ge0.
}
\tag{CopositiveCut}
\]

Therefore a named line `L` and an exact copositivity certificate for `h`
with negative frozen pairing would exclude every phase lift of `x^(10)`.
CayleyCut is a structured subfamily of this dual route.

## Exact tasks

1. Give one verdict for PW10 on this exact frozen tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**.

2. Audit `(Nsharp)`, `(CayleyCut)`, `(FrozenCayleyCut)`, the complement-cycle
   example, and `(CopositiveCut)`.  Check every orientation, factor two,
   Fourier sign, and clique-number claim.

3. Use the exact projection data, not numerical sampling, to seek a line
   obstruction.  In priority order:

   - exhibit a named `L` and symmetric `S` with a proved clique number for
     which `(FrozenCayleyCut)` fails;
   - or exhibit a symmetric circulant `h` with a finite exact copositivity
     proof and negative pairing with the actual `q_L`;
   - or prove that a nontrivial explicit family of cuts always passes and
     isolate the first frozen projection-discrepancy estimate needed for a
     possible violation.

   Natural families may include complements of cycle powers, interval
   connection sets, or another family with an exact clique certificate.  Do
   not invoke an unknown Paley clique number, numerical graph search, or an
   unnamed copositive program as proof.

4. Express every proposed cut in terms of the almost-injective projection
   multiplicities `nu_L` and the oriented difference counts `N_L(s)`.  A
   generic bound that loses the `10/(MD)` scale is not enough; show the exact
   slack against the clique bound.

5. If no cut excludes a line, return to `(PositiveRoot)` or construct a
   different deterministic nonnegative spectral factor.  Positivity of the
   shadow alone, a signed factor, or a mixture of autocorrelations is not a
   single nonnegative factor.

6. Even feasibility of every stabilizer line does not give a physical lift;
   the independent-line-character theorem already separates that relaxation.
   A closing result for `x^(10)` still requires phases with `C=1` or an
   explicit `eta>0` valid for every compatible phase field.

7. Even excluding `x^(10)` would not prove PW10 for every physical magnitude
   profile.  Preserve this quantifier.  Do not return to five-carry
   arithmetic, Perron--Schur10, or the all-`T` ratio without a new exact
   certificate for this tuple.

8. End with a plain audit ledger separating **PROVED**, **DISPROVED**,
   **NECESSARY-ONLY**, **SUFFICIENT-ONLY**, **EQUIVALENT**, **OPEN**, and
   **CONJECTURED**.  State the first new claim requiring independent
   verification.

The purpose of this round is to turn the unresolved one-dimensional phase
retrieval problem into a concrete exact separation search, with graph or
copositive certificates that can genuinely rule out all phases on a frozen
line.

<!-- END HISTORICAL FILE path=work/round-16-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-16-response.md bytes=19099 sha256=44b488b79b840cf48519e874985bae6c816ac6838c72da36f0bc082aced50778 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

No frozen line is excluded in this round, and no nonnegative spectral factor is constructed for every line.

The main exact advances are:

1. The sharpening

   $$
   N_L(s)\le m\qquad(s\ne0)
   $$

   is correct.

2. Every Cayley-graph cut passes on every line with
   \(\ell_L=|\Gamma\cap L|=0\). There are exactly

   $$
   823848595310788068
   $$

   such lines.

3. On a line with \(\ell_L=2\), any violating Cayley cut must have an exceptionally dense, almost Turán-extremal connection set and a large positive line character. An explicit necessary density defect is derived below.

4. For every frozen line, every complement-of-a-cycle-power Cayley cut passes, for every radius and every additive generator.

5. No copositive separator belonging to the cone

   $$
   \{\text{positive semidefinite}\}
   +
   \{\text{entrywise nonnegative}\}
   $$

   can exclude a frozen line. Any successful circulant copositive certificate must therefore be exceptional, not merely PSD-plus-nonnegative.

The first unresolved linewise step remains the existence or nonexistence of a nonnegative cyclic spectral factor for the exact \(q_L\).

---

# 1. The sharpened projection bound

Fix an isotropic line \(L=\langle v\rangle\) and write

$$
\nu(r)=\nu_L(r)=\#\{j:[v,a_j]=r\}.
$$

Recall

$$
N_L(s)=\sum_r\nu(r)\nu(r-s)-m\delta_{s,0}.
$$

The audited structure is

$$
\ell_L:=N_L(0)\in\{0,2\}.
$$

## 1.1 Injective projection: \(\ell_L=0\)

Then

$$
\nu=\mathbf 1_T
$$

for a set \(T\subset\mathbb F_D\) of size \(m\). For \(s\ne0\),

$$
N_L(s)=|T\cap(T+s)|.
$$

If this intersection had size \(m\), then \(T=T+s\). Since \(D\) is prime, every nonzero \(s\) generates the additive group, so a nonempty shift-invariant set must be all of \(\mathbb F_D\). That is impossible because \(m<D\). Hence

$$
N_L(s)\le m-1.
\tag{1.1}
$$

## 1.2 One double projection: \(\ell_L=2\)

There is a support set \(T\) of size \(m-1\) and one point \(r_0\in T\) such that

$$
\nu=\mathbf1_T+\delta_{r_0}.
$$

For \(s\ne0\),

$$
\boxed{
N_L(s)
=
|T\cap(T+s)|
+\mathbf1_T(r_0+s)
+\mathbf1_T(r_0-s).
}
\tag{1.2}
$$

Again \(T\ne T+s\), so

$$
|T\cap(T+s)|\le |T|-1=m-2.
$$

The two remaining indicators contribute at most \(2\). Therefore

$$
N_L(s)\le m.
$$

Thus the proposed sharpening is correct:

$$
\boxed{N_L(s)\le m\quad(s\ne0).}
\tag{Nsharp}
$$

We will also use

$$
\boxed{\sum_sN_L(s)=m^2-m=M.}
\tag{1.3}
$$

This follows by summing the definition over \(s\).

---

# 2. Weighted Cayley cuts

Let

$$
S=-S\subset\mathbb F_D\setminus\{0\},
$$

and let \(G_S=\operatorname{Cay}(\mathbb F_D,S)\). Put

$$
\omega=\omega(G_S).
$$

For a probability vector \(p=(p_k)\), define

$$
q_s=\sum_kp_kp_{k+s}.
$$

Then

$$
\sum_{s\in S}q_s
=
\sum_{k}\sum_{s\in S}p_kp_{k+s}
=
p^{\mathsf T}A_Sp,
\tag{2.1}
$$

where \(A_S\) is the adjacency matrix. The ordered sum counts every undirected edge twice.

## 2.1 Self-contained Motzkin–Straus argument

Let

$$
E(p)=\sum_{\{j,k\}\in E(G_S)}p_jp_k.
$$

If two support vertices \(u,v\) are nonadjacent, keeping \(p_u+p_v\) fixed and moving all their mass to whichever of \(u,v\) has the larger weighted neighbor sum cannot decrease \(E(p)\). Iterating reduces the support to a clique.

On a clique of size \(r\le\omega\),

$$
E(p)
=
\frac12\left[
\left(\sum_jp_j\right)^2-\sum_jp_j^2
\right]
\le
\frac12\left(1-\frac1r\right)
\le
\frac12\left(1-\frac1\omega\right).
$$

Since \(p^{\mathsf T}A_Sp=2E(p)\),

$$
\boxed{
\sum_{s\in S}q_s
\le
1-\frac1{\omega(G_S)}.
}
\tag{CayleyCut}
$$

Equality is attained by the uniform probability vector on a maximum clique.

There is no missing factor of two.

---

# 3. Frozen form of the Cayley cut

For one frozen line, let

$$
N_L(S)=\sum_{s\in S}N_L(s),
\qquad
\chi_L(S)=\sum_{s\in S}\chi_L(s).
$$

Since \(0\notin S\), the baseline value is \(q_s^b=1/(D+1)\), and hence

$$
\boxed{
\sum_{s\in S}q_{L,s}
=
\frac{|S|}{D+1}
+
\frac{10}{MD}
\left[
N_L(S)+\chi_L(S)
-\frac{M|S|}{D+1}
\right].
}
\tag{FrozenCayleyCut}
$$

The orientation agrees with the definition

$$
q_{L,s}=\sum_kp_{L,k}p_{L,k+s}.
$$

No extra symmetry factor is present: a symmetric \(S\) already contains both \(s\) and \(-s\).

---

# 4. Audit of the finite-cycle example

On \(\mathbb Z/5\mathbb Z\), take

$$
q_0=\frac{11}{25},
\qquad
q_{\pm1}=\frac1{100},
\qquad
q_{\pm2}=\frac{27}{100}.
$$

The entries are strictly positive and sum to \(1\).

Its Fourier values are

$$
\widehat q(0)=1,
$$

$$
\widehat q(\pm1)
=
\frac{30-13\sqrt5}{100}>0,
$$

$$
\widehat q(\pm2)
=
\frac{30+13\sqrt5}{100}>0.
$$

The first positivity follows from

$$
30^2-5\cdot13^2=55>0.
$$

Thus the circulant shadow is strictly positive definite.

Take

$$
S=\{\pm2\}.
$$

The graph is a five-cycle, so \(\omega(G_S)=2\). CayleyCut requires

$$
q_2+q_{-2}\le\frac12,
$$

but

$$
q_2+q_{-2}=\frac{54}{100}>\frac12.
$$

Hence it admits no nonnegative probability spectral factor. This confirms exactly that strict pointwise and Fourier positivity of \(q\) are insufficient.

---

# 5. The nearly complete frozen cut

Take

$$
S=\mathbb F_D^*\setminus\{a,-a\},
\qquad a\ne0.
$$

The missing-edge graph is the \(D\)-cycle generated by \(a\). Consequently,

$$
\omega(G_S)=\alpha(C_D)=\frac{D-1}{2}.
$$

The Cayley cut is equivalent to

$$
q_{L,0}+2q_{L,a}\ge\frac2{D-1}.
\tag{5.1}
$$

The audited pointwise bounds give

$$
q_{L,0}
\ge
\frac{3D+1}{2D(D+1)},
\qquad
q_{L,a}\ge\frac1{2(D+1)}.
$$

Therefore

$$
q_{L,0}+2q_{L,a}
\ge
\frac{5D+1}{2D(D+1)}.
$$

The exact slack over (5.1) is

$$
\boxed{
\frac{5D+1}{2D(D+1)}
-\frac2{D-1}
=
\frac{D^2-8D-1}
{2D(D+1)(D-1)}
>0.
}
\tag{5.2}
$$

Thus this high-density cut passes on every frozen line.

---

# 6. Every complement-of-a-cycle-power cut passes

This gives a nontrivial infinite family of exact cuts that can now be removed from consideration.

Fix \(a\ne0\) and

$$
1\le r\le\frac{D-3}{2}.
$$

Put

$$
T_{a,r}
=
\{0,\pm a,\ldots,\pm ra\},
$$

$$
S_{a,r}
=
\mathbb F_D^*\setminus
\{\pm a,\ldots,\pm ra\}.
$$

Let

$$
k=r+1,
\qquad
n=\left\lfloor\frac Dk\right\rfloor\ge2.
$$

After scaling by \(a^{-1}\), the complement graph of \(G_{S_{a,r}}\) is the \(r\)-th power \(C_D^r\) of a \(D\)-cycle.

An independent set in \(C_D^r\) has circular gaps at least \(r+1=k\); their sum is \(D\). Hence its size is at most \(\lfloor D/k\rfloor\). Equality is attained by

$$
0,k,2k,\ldots,(n-1)k.
$$

Therefore

$$
\boxed{\omega(G_{S_{a,r}})=n.}
\tag{6.1}
$$

CayleyCut is equivalent to

$$
Q_{L,a,r}:=
\sum_{s\in T_{a,r}}q_{L,s}
\ge\frac1n.
\tag{6.2}
$$

The exact frozen expression is

$$
Q_{L,a,r}
=
\frac{2k}{D+1}
+
\frac{10}{MD}
\left[
N_L(T_{a,r})+\chi_L(T_{a,r})
-\frac{2kM}{D+1}
\right].
\tag{6.3}
$$

Here

$$
N_L(T_{a,r})\ge0,
$$

and, because \(\ell_L\le2\),

$$
\chi_L(T_{a,r})\ge-2(2k-1)>-4k.
$$

Thus

$$
Q_{L,a,r}
\ge
\frac{2k}{D+1}
-\frac{20k}{D(D+1)}
-\frac{40k}{MD}.
\tag{6.4}
$$

Write

$$
D=nk+\rho,
\qquad
0\le\rho<k.
$$

Then

$$
\begin{aligned}
\frac{2k}{D+1}-\frac1n
&=
\frac{2kn-D-1}{n(D+1)}\\
&=
\frac{nk-\rho-1}{n(D+1)}\\
&\ge
\frac{k(n-1)}{n(D+1)}
\ge
\frac{k}{2(D+1)}.
\end{aligned}
\tag{6.5}
$$

Combining (6.4)–(6.5),

$$
\boxed{
Q_{L,a,r}-\frac1n
\ge
\frac{
k\left[M(D-40)-80(D+1)\right]
}{
2MD(D+1)
}.
}
\tag{6.6}
$$

For the exact frozen integers,

$$
\boxed{
M(D-40)-80(D+1)
=
221624933455219572717033699561306900>0.
}
$$

Therefore:

$$
\boxed{
\text{Every complement-of-a-cycle-power Cayley cut passes,
for every frozen line, every }a\ne0,\text{ and every admissible }r.
}
\tag{6.7}
$$

This includes the nearly complete cut of Section 5.

---

# 7. Every Cayley cut passes on every injective line

There are exactly

$$
D+1-\frac M2
=
823848595310788068
$$

lines with \(\ell_L=0\).

Fix any such line and any nonempty symmetric connection set \(S\). Put

$$
d=|S|,
\qquad
\omega=\omega(G_S),
\qquad
\gamma=1-\frac1\omega.
$$

Applying CayleyCut to the uniform probability vector on all \(D\) vertices gives

$$
\frac dD\le\gamma.
$$

Define the density defect

$$
\boxed{
\sigma:=\gamma-\frac dD\ge0.
}
\tag{7.1}
$$

Because \(\ell_L=0\),

$$
\chi_L(S)=0.
$$

Apply CayleyCut to the projection probability vector

$$
p_r=\frac{\nu_L(r)}m.
$$

Since

$$
\frac{N_L(S)}{m^2}=p^{\mathsf T}A_Sp,
$$

we obtain

$$
N_L(S)\le m^2\gamma.
\tag{7.2}
$$

Using FrozenCayleyCut,

$$
\begin{aligned}
\sum_{s\in S}q_{L,s}
&\le
\frac d{D+1}
\left(1-\frac{10}{D}\right)
+
\frac{10m}{(m-1)D}\gamma.
\end{aligned}
$$

A direct substitution of

$$
d=D(\gamma-\sigma)
$$

gives the exact margin

$$
\boxed{
\begin{aligned}
\gamma-\sum_{s\in S}q_{L,s}
\ge
\frac{
D(m-1)(D-10)\sigma
+
\gamma\bigl[D(m-11)-10m\bigr]
}{
D(D+1)(m-1)
}.
\end{aligned}
}
\tag{7.3}
$$

For the displayed frozen integers,

$$
\boxed{
D(m-11)-10m
=
456803024442811242182018285>0.
}
\tag{7.4}
$$

Both terms in the numerator of (7.3) are nonnegative, and the second is strictly positive. Hence

$$
\boxed{
\text{Every CayleyCut passes on every line with }\ell_L=0.
}
\tag{7.5}
$$

This excludes the entire Cayley-graph dual family on more than \(8.23\times10^{17}\) of the frozen lines.

---

# 8. What a Cayley violation on a double line would require

Now suppose

$$
\ell_L=2.
$$

The same projection-vector argument still gives

$$
N_L(S)\le m^2\gamma.
$$

The only additional term is \(\chi_L(S)\). The analogue of (7.3) is

$$
\boxed{
\begin{aligned}
\gamma-\sum_{s\in S}q_{L,s}
\ge{}&
\frac{
D(m-1)(D-10)\sigma
+
\gamma[D(m-11)-10m]
}{
D(D+1)(m-1)
}\\
&-\frac{10\,\chi_L(S)}{MD}.
\end{aligned}
}
\tag{8.1}
$$

Therefore a violation requires

$$
\boxed{
\begin{aligned}
\chi_L(S)>
\frac{m}{10(D+1)}
\Bigl[
D(m-1)(D-10)\sigma\\
+\gamma\bigl(D(m-11)-10m\bigr)
\Bigr].
\end{aligned}
}
\tag{8.2}
$$

In particular:

* \(\chi_L(S)\) must be positive;
* the connection set must have a large positive Fourier coefficient at the unique doubled line frequency.

Since \(\Gamma\cap L=\{\pm\tau v\}\),

$$
\chi_L(S)
=
2\operatorname{Re}
\sum_{s\in S}\omega^{-s\tau},
$$

and hence

$$
\chi_L(S)\le2d=2D(\gamma-\sigma).
\tag{8.3}
$$

Combining (8.2) and (8.3) gives the exact necessary density condition

$$
\boxed{
\sigma<\gamma\,\mathcal R_*,
}
\tag{8.4}
$$

where

$$
\boxed{
\mathcal R_*=
\frac{
20D(D+1)-m[D(m-11)-10m]
}{
mD(m-1)(D-10)+20D(D+1)
}.
}
\tag{8.5}
$$

For the exact tuple,

$$
\mathcal R_*
=
\frac{
17508372780702661015919296343045971260
}{
208669012172176222401073570554748968050323871822570100
}
$$

and therefore

$$
\boxed{
\mathcal R_*
=
8.3904996714395789\ldots\times10^{-17}.
}
\tag{8.6}
$$

Thus any Cayley separator must simultaneously satisfy all of the following:

$$
\boxed{
\ell_L=2,\qquad
\chi_L(S)>0,\qquad
0\le\sigma<
8.391\times10^{-17}\,\gamma,
}
\tag{8.7}
$$

as well as the stronger quantitative character lower bound (8.2).

This is the first exact frozen projection-discrepancy estimate remaining in the Cayley route.

No such \(L,S\) are exhibited.

---

# 9. General circulant copositive cuts

Let \(h_s=h_{-s}\), and let

$$
(H_h)_{jk}=h_{k-j}.
$$

For a nonnegative spectral factor \(p\),

$$
\begin{aligned}
p^{\mathsf T}H_hp
&=
\sum_{j,k}h_{k-j}p_jp_k\\
&=
\sum_s h_s\sum_jp_jp_{j+s}\\
&=
\boxed{\sum_sh_sq_{L,s}.}
\end{aligned}
\tag{9.1}
$$

Therefore, if \(H_h\) is copositive,

$$
p\ge0\Longrightarrow p^{\mathsf T}H_hp\ge0,
$$

then every nonnegative factor must satisfy

$$
\boxed{\sum_sh_sq_{L,s}\ge0.}
\tag{CopositiveCut}
$$

The Cayley cut corresponds to the copositive matrix

$$
H_S=
\left(1-\frac1{\omega(G_S)}\right)J-A_S.
$$

Indeed,

$$
p^{\mathsf T}H_Sp
=
\left(1-\frac1\omega\right)(\mathbf1^{\mathsf T}p)^2
-p^{\mathsf T}A_Sp
\ge0.
$$

---

# 10. PSD-plus-nonnegative copositive matrices can never separate the frozen shadow

Let

$$
Q_L(j,k)=q_{L,k-j}.
$$

The Fourier eigenvalues of this circulant matrix are exactly

$$
x^{(10)}_{tv}\ge0.
$$

Thus

$$
Q_L\succeq0.
$$

Moreover, every \(q_{L,s}\) is strictly positive, so \(Q_L\) is entrywise positive.

Suppose a circulant copositive matrix has a decomposition

$$
H_h=P+N,
$$

where

$$
P\succeq0,
\qquad
N\ge0
$$

entrywise. Then

$$
\operatorname{Tr}(PQ_L)\ge0
$$

because both matrices are positive semidefinite, and

$$
\operatorname{Tr}(NQ_L)\ge0
$$

because both are entrywise nonnegative.

Since \(h_s\) and \(q_s\) are even,

$$
\operatorname{Tr}(H_hQ_L)
=
D\sum_sh_sq_{L,s}.
$$

Consequently,

$$
\boxed{
H_h=P+N,\quad P\succeq0,\ N\ge0
\quad\Longrightarrow\quad
\sum_sh_sq_{L,s}\ge0.
}
\tag{10.1}
$$

Therefore:

$$
\boxed{
\text{Any circulant copositive certificate excluding a frozen line
must be non-SPN—outside PSD plus entrywise nonnegative.}
}
\tag{10.2}
$$

The \(\mathbb Z/5\mathbb Z\) cycle obstruction is of precisely the exceptional type that this result does not eliminate.

---

# 11. Returning to the all-positive spectral factor

No graph or copositive cut above excludes a frozen line. We therefore return to the deterministic all-positive phase rule.

Put

$$
X_L(t)=x^{(10)}_{tv},
\qquad
c=\frac1{\sqrt{D+1}},
$$

and choose

$$
\alpha_{tv}=\sqrt{X_L(t)}.
$$

For \(k\ne0\),

$$
\boxed{
Dp^+_{L,k}
=
1-c+
\sum_{t\ne0}
\left(\sqrt{X_L(t)}-c\right)\omega^{-kt}.
}
\tag{11.1}
$$

The sum is real because \(X_L(t)=X_L(-t)\).

A sufficient condition is

$$
\left|
\sum_{t\ne0}
(\sqrt{X_L(t)}-c)\omega^{-kt}
\right|
\le1-c
\quad\forall k\ne0.
\tag{11.2}
$$

## 11.1 A checkable quadratic sufficient condition

By Cauchy–Schwarz, (11.2) follows from

$$
\boxed{
\sum_{t\ne0}
(\sqrt{X_L(t)}-c)^2
\le
\frac{(1-c)^2}{D-1}.
}
\tag{11.3}
$$

Since

$$
X_L(t)\ge\frac1{2(D+1)}=\frac{c^2}{2}
\qquad(t\ne0),
$$

we have

$$
|\sqrt{X_L(t)}-c|
\le
\frac{|X_L(t)-c^2|}
{c(1+1/\sqrt2)}.
\tag{11.4}
$$

Define the exact projection discrepancy

$$
E_L(s)
=
N_L(s)+\chi_L(s)-M q_s^b.
$$

From FrozenShadow and Parseval,

$$
\boxed{
\sum_t|X_L(t)-b_t|^2
=
\frac{100}{M^2D}
\sum_sE_L(s)^2.
}
\tag{11.5}
$$

Combining (11.3)–(11.5), the all-positive phase rule is guaranteed by the explicit finite condition

$$
\boxed{
\sum_sE_L(s)^2
\le
\frac{
M^2D(1+1/\sqrt2)^2(1-c)^2
}{
100(D^2-1)
}.
}
\tag{11.6}
$$

This is a genuine frozen projection-discrepancy estimate, not a reformulation of the phase variables.

## 11.2 What \(Nsharp\) currently proves

We have

$$
\sum_sN_L(s)=M,
\qquad
0\le N_L(s)\le m,
$$

so

$$
\sum_sN_L(s)^2\le mM.
$$

Furthermore,

$$
\sum_s\chi_L(s)^2
\le2D.
$$

For the baseline,

$$
\sum_s(q_s^b)^2
=
\frac{D+3}{(D+1)^2}.
$$

Using \((a+b+c)^2\le3(a^2+b^2+c^2)\),

$$
\boxed{
\sum_sE_L(s)^2
\le
3\left[
mM+2D+
\frac{M^2(D+3)}{(D+1)^2}
\right].
}
\tag{11.7}
$$

For the displayed frozen integers, the upper bound in (11.7) is approximately

$$
1.99778888348\times10^{11}
$$

times larger than the right side of the sufficient condition (11.6).

This does not show that (11.6) is false for an actual line. It shows precisely that \(Nsharp\), the total-count identity, and the second-moment character bound are far too coarse to prove the all-positive spectral factor.

A much stronger cancellation estimate for the nonlinear Fourier coefficients of

$$
t\longmapsto\sqrt{x^{(10)}_{tv}}
$$

is still needed.

---

# 12. Earliest remaining linewise gap

The exact linewise search has now contracted as follows.

A Cayley-graph obstruction cannot occur:

* on any of the \(823848595310788068\) lines with \(\ell_L=0\);
* for any complement-of-a-cycle-power connection set on any line.

On a line with \(\ell_L=2\), a Cayley obstruction would require:

$$
\sigma<
8.391\times10^{-17}\gamma
$$

and the large positive Fourier-character bound (8.2).

A general circulant copositive obstruction must be exceptional:

$$
H_h\notin
\{\text{PSD}\}+\{\text{entrywise nonnegative}\}.
$$

No such exact exceptional circulant is produced.

On the constructive side, the all-positive factor would follow from (11.6), but the currently proved projection-discrepancy bounds miss that sufficient threshold by about \(2\times10^{11}\).

Thus the first unresolved frozen-line statement is:

> Determine whether one of the \(M/2\) double-projection lines admits either
> (i) an exceptional non-SPN circulant copositive separator, necessarily satisfying the near-Turán conditions in Section 8, or
> (ii) a nonnegative cyclic spectral factor, for example via a substantially sharper nonlinear Fourier estimate than (11.7).

Even settling every line would not establish a physical lift with \(C=1\); the cross-line cubic gate remains downstream.

PW10 therefore remains open.

---

# Audit ledger

## PROVED

* The sharpening

  $$
  N_L(s)\le m\quad(s\ne0).
  $$
* CayleyCut, with the ordered-edge factor and clique constant correct.
* FrozenCayleyCut, including all orientations and normalization factors.
* The exact \(\mathbb Z/5\mathbb Z\) counterexample and its strictly positive Fourier spectrum.
* The clique number

  $$
  \omega\!\left(
  \operatorname{Cay}(\mathbb F_D,
  \mathbb F_D^*\setminus\{\pm a\})
  \right)=\frac{D-1}{2}.
  $$
* The strict complement-cycle inequality

  $$
  q_{L,0}+2q_{L,a}>\frac2{D-1}.
  $$
* For every radius, every generator, and every frozen line, every complement-of-a-cycle-power Cayley cut passes.
* Every Cayley cut passes on every line with \(\ell_L=0\).
* The exact necessary conditions (8.2)–(8.7) for any Cayley violation on a line with \(\ell_L=2\).
* CopositiveCut.
* No circulant copositive matrix in the PSD-plus-entrywise-nonnegative cone can exclude a frozen line.
* The quadratic all-positive-root sufficient condition (11.6).
* The exact projection-discrepancy bound (11.7) obtainable from \(Nsharp\).

## DISPROVED

* Sufficiency of strict entrywise positivity and strict Fourier positivity of a cyclic autocorrelation shadow.
* The possibility that a complement-of-a-cycle-power Cayley cut excludes a frozen line.
* The possibility that any Cayley cut excludes an injective-projection line.
* The possibility that an SPN circulant copositive certificate excludes a frozen line.

## NECESSARY-ONLY

* CayleyCut and general CopositiveCut.
* The near-Turán density and positive-character conditions for a double-projection Cayley obstruction.
* Nonnegativity of all line stabilizer marginals.
* Positivity of the autocorrelation shadow.

## SUFFICIENT-ONLY

* The all-positive-root condition (11.2).
* Its quadratic projection-discrepancy sufficient condition (11.6).

## EQUIVALENT

For a fixed line:

$$
\text{nonnegative cyclic spectral factor}
\iff
p_{L,k}\ge0\ \forall k
\iff
B_L\succeq0.
$$

## OPEN

* Existence of an exceptional non-SPN copositive separator on a double-projection line.
* Whether the near-Turán requirements in Section 8 can occur for an actual symmetric Cayley connection set.
* The all-positive-root inequalities for the exact frozen restrictions.
* Existence of any nonnegative cyclic spectral factor for every frozen line.
* Existence of a global phase field with \(C=1\).
* PW10.

## CONJECTURED

* No statement is promoted to conjectured status.

The first new claim requiring independent verification is the exact theorem

$$
\boxed{
\ell_L=0
\quad\Longrightarrow\quad
\text{every symmetric CayleyCut passes on }q_L,
}
$$

with its explicit margin (7.3).

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-16-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-16-local-audit.md bytes=8400 sha256=ea9ad14605b03012e77073b386bdbb31efe76ca04c5e31d309559d8990bce44e -->

# Round 16 local audit

- Audit completed (UTC): `2026-09-13T02:50:53Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-16-response.md`
- Web-response SHA-256:
  `44b488b79b840cf48519e874985bae6c816ac6838c72da36f0bc082aced50778`
- Capture equality: the browser clipboard payload, artifact, and output copy
  are text-identical; the two files are byte-identical, each `19,099` bytes
  and `1,233` lines.

## Verdict

The Round 16 response's displayed Cayley-cut, copositive, and all-positive
factor calculations pass the independent checks.  Its final search boundary
is nevertheless materially superseded by a stronger exact local theorem:

\[
\boxed{
\text{every frozen line shadow lies in the convex hull of genuine
nonnegative-probability autocorrelations.}
}
\]

Consequently no symmetric circulant copositive linear functional can exclude
any frozen line.  In particular, the response's remaining search for an
exceptional non-SPN separator on a one-double line is now **disproved as a
possible route**.

This convex-hull theorem does not construct a single factor for any shadow.
The exact named-line factor, all-line spectral-factor feasibility, the
physical `C(alpha)=1` lift, and PW10 all remain open.

## Verified claims from the web response

The sharpened projection bound is correct.  If the projection is injective,
then for nonzero `s` its support cannot be invariant under translation by
`s`, so `N_L(s)<=m-1`.  With exactly one doubled value, writing
`nu=1_T+delta_(r_0)` gives

\[
N_L(s)=|T\cap(T+s)|+\mathbf1_T(r_0+s)+\mathbf1_T(r_0-s)\le m.
\]

The weighted Cayley inequality has the correct ordered-edge factor:

\[
\sum_{s\in S}q_s=p^{\mathsf T}A_Sp
\le1-\frac1{\omega(G_S)}.
\]

Substitution into the frozen shadow has no missing factor or reversed
orientation.  The exact `Z/5Z` example has strictly positive entries and
strictly positive Fourier spectrum, yet violates the five-cycle inequality;
it correctly proves that those two positivity conditions do not imply a
nonnegative factor.

The nearly complete connection set has clique number `(D-1)/2`, and its cut
passes with exact positive slack

\[
\frac{D^2-8D-1}{2D(D+1)(D-1)}>0.
\]

The response's stronger complement-of-cycle-power argument is also valid for
every admissible radius.  Its uniform margin reduces to

\[
M(D-40)-80(D+1)
=221624933455219572717033699561306900>0.
\]

The response correctly proves that every Cayley cut passes on every
collision-free line.  Its necessary near-Turan condition for a Cayley
violation on a one-double line is algebraically valid, including

\[
\mathcal R_*=8.3904996714395789\ldots\times10^{-17}.
\]

That condition is now moot rather than false: the all-line convex-hull theorem
below rules out every Cayley violation on the one-double lines as well.

The general copositive pairing identity

\[
p^{\mathsf T}H_hp=\sum_sh_sq_s
\]

and the response's no-SPN argument are correct.  The quadratic condition
`(11.6)` is a valid sufficient condition for the all-positive square-root
factor, and the generic estimate `(11.7)` indeed misses it by about
`1.99778888348e11`.  Neither statement is a necessity result.

## Stronger exact all-line convex-hull theorem

For an arbitrary projection multiplicity `nu` of total mass `m`, put

\[
A_s=\sum_r\nu(r)\nu(r-s),
\qquad q_s^\nu=A_s/m^2.
\]

This is the autocorrelation of the nonnegative probability vector `nu/m`.
Let `u_s=1/D`, the autocorrelation of the uniform distribution, and let
`delta_0` be the point-mass autocorrelation.  Direct substitution into the
exact frozen shadow gives

\[
q_L=a u+bq^\nu+c\delta_0+\frac{10}{MD}\chi_L,
\]

where

\[
a=\frac{D-10}{D+1},
\qquad
b=\frac{10m}{(m-1)D},
\qquad
c=\frac{D(m-11)-10m}{D(D+1)(m-1)}.
\]

Exact integer arithmetic verifies

\[
a>0,\qquad b>0,\qquad c>0,\qquad a+b+c=1.
\]

For every collision-free line, `chi_L=0`, so this is already a convex
combination of three genuine autocorrelations.

For a one-double line,

\[
\chi_L(s)=2\cos(2\pi s t_0/D).
\]

The explicit probability vector

\[
p_k^{\cos}=\frac{1+\cos(2\pi t_0k/D)}D
\]

is nonnegative, sums to one, and has autocorrelation

\[
q_s^{\cos}=u_s+\frac1{4D}\chi_L(s).
\]

Taking `w=40/M` yields the exact decomposition

\[
\boxed{
q_L=(a-w)u+bq^\nu+c\delta_0+wq^{\cos},
}
\]

with all coefficients positive and summing to one.  This proves the theorem
for all `D+1` frozen lines, including all `M/2` one-double lines.

Every symmetric circulant copositive functional is nonnegative on every
genuine autocorrelation, hence on their convex hull.  Therefore

\[
\boxed{
\text{no Cayley, SPN, or exceptional non-SPN circulant-copositive linear
certificate can exclude a frozen line.}
}
\]

This is the precise correction to the Round 16 endpoint.  Convex combination
does not preserve rank one, so it does not prove that `q_L` itself equals the
autocorrelation of one nonnegative probability vector.

## Explicit Sidon line and the nonlinear boundary

For `L=< (0,1) >`, up to the fixed sign convention, the projected set is

\[
T=\{t_j=2Pj+(j^2\bmod P):0\le j\le P-42\}.
\]

It lies in an interval shorter than `D/2`.  Equality of two oriented integer
differences first forces equality of the `2P` block differences.  Reduction
of the remaining equality modulo the prime `P` then gives

\[
2(j-k)(k-k')=0\pmod P,
\]

which forces the ordered pairs to agree for a nonzero difference.  No new
collision is introduced modulo `D`.  Thus `T` is an oriented cyclic Sidon
set.  If `Delta=(T-T)\setminus{0}`, then `|Delta|=M` and

\[
q_{L,0}=\frac{2(D-10)}{D(D+1)},
\]

\[
q_{L,s}=\frac{D-10}{D(D+1)}
+\frac{10}{MD}\mathbf1_\Delta(s)
\quad(s\ne0).
\]

For the response's discrepancy `E(s)=N_L(s)-Mq_s^b`, exact counting gives

\[
\boxed{
\sum_sE(s)^2=M-\frac{M^2(D-1)}{(D+1)^2}.
}
\]

Using

\[
(1+1/\sqrt2)^2<583/200
\]

and exact rational cross multiplication proves that this value is more than
`100` times the right side of the quadratic sufficient test `(11.6)`.  This
is much sharper for the named line than the generic `2e11` upper-bound gap,
but it still only shows that the sufficient norm test fails.  It neither
finds a negative coordinate in the all-positive trial nor excludes another
phase/factor.

## Corrected status ledger

### VERIFIED

- `N_L(s)<=m` for every nonzero `s`, with `m-1` in the injective case.
- `CayleyCut`, `FrozenCayleyCut`, and the exact `Z/5Z` counterexample.
- Every complement-of-cycle-power cut passes on every frozen line.
- Every Cayley cut passes on every collision-free line.
- The response's one-double near-Turan necessary condition.
- The SPN limitation and the all-positive sufficient estimates.
- The exact all-line autocorrelation convex-hull theorem.
- The named Sidon line and its two-level frozen shadow.

### CORRECTED / SUPERSEDED

- The Round 16 endpoint proposed an exceptional non-SPN circulant separator
  as a remaining possible route.  The all-line convex-hull theorem eliminates
  that entire linear route, including every exceptional copositive matrix.

### DISPROVED

- Any symmetric circulant copositive linear separation of any frozen line.
- Any Cayley violation on a one-double line.
- Usefulness of the Round 16 quadratic sufficient test for the named Sidon
  line: its exact discrepancy exceeds the threshold by a factor above `100`.

### OPEN

- Whether the named two-level Sidon shadow is one nonnegative cyclic
  autocorrelation.
- Whether every frozen line has a nonnegative cyclic spectral factor.
- Whether the frozen global magnitude profile admits phases with
  `C(alpha)=1`.
- A phase-uniform gap below `C=1` if it does not.
- PW10 for the exact frozen tuple.

## Reproducibility

- `work/verify_round16_cayley_cuts.py`
  SHA-256 `ea24aaf7c677b93c38649358a34b1982bb95c5d475692a3e205cd6223222fe02`
- `work/verify_round16_cycle_powers.py`
  SHA-256 `2729e53a93b2b3f3e507f16517aeb070f10c6e55205c1502980443cfee713ff2`
- `work/verify_round16_convex_hull.py`
  SHA-256 `c2702a33b45c7e1aabd9434580d2df6ed6e14e38b48532ea6e35f7558cc36e16`
- `work/verify_round16_web_response.py`
  SHA-256 `c7733673c8be47f998026273dab5af7562b205147438f2add4d538e13cc571c0`
- `work/round-16-independent-convex-hull.md`
  SHA-256 `0ee5d226140f0680aa97885aaf0df8409e466bfb90e2cd29e6af1c13fd43f911`

All four Python checkers print `PASS`; all four also pass bytecode
compilation.

<!-- END HISTORICAL FILE path=outputs/round-16-local-audit.md -->


# ROUND 017

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-17-prompt.md bytes=6914 sha256=d49276c73fbd6523857297df40d3139809a3ae11c2a8eceb7707d5effd700909 -->

# Round 17 — audit the all-line autocorrelation hull and attack the nonlinear rank-one factor gap

Continue in the same ordinary Chat conversation and the same canonically
frozen finite `r=2`, low-`A` gate.  Give a public, self-contained derivation
and no hidden chain-of-thought.  Do not repeat the Round 8--16 narrative.

## Exact frozen boundary

Use exactly

\[
m=485165196,
\quad P=485165237=m+41,
\quad D=941541228773064677=4P^2+1,
\]

\[
0\le j\le P-42,
\quad r_j=j^2\bmod P,
\quad t_j=2Pj+r_j,
\quad a_j=(t_j,t_j^2),
\]

\[
A=\{a_j\},
\quad \Gamma=(A-A)\setminus\{0\},
\quad M=m(m-1)=235385266924553220.
\]

The open gate remains

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10
\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

The exact frozen full-support magnitude point is

\[
b_0=1,
\qquad b_z=\frac1{D+1}\quad(z\ne0),
\]

\[
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\quad y=\mathbf1_\Gamma+\lambda/D,
\quad d=y-(M/D)b,
\quad x^{(10)}=b+(10/M)d.
\]

It is positive, even, self-Fourier, has total mass `D`, passes every audited
magnitude and small-Gram condition, and has frozen objective strictly above
`10`.  A physical lift still requires compatible phases with

\[
C(\alpha)=\operatorname{Tr}R_\alpha^3=1,
\qquad
R_\alpha=D^{-1}\sum_z\alpha_zW_z.
\]

Do not promote a line relaxation into a physical lift or into PW10.

## Audited line notation

For a projective isotropic line `L=<v>`, let

\[
\nu_L(r)=\#\{j:[v,a_j]=r\},
\qquad
A_L(s)=\sum_r\nu_L(r)\nu_L(r-s),
\]

\[
q^\nu_{L,s}=A_L(s)/m^2,
\qquad
N_L(s)=A_L(s)-m\delta_{s,0}.
\]

The projection has either no collision or exactly one double value, so
`ell_L=|Gamma cap L|` is `0` or `2`.  The exact frozen line shadow is

\[
q_{L,s}
=q_s^b+\frac{10}{MD}
\left(N_L(s)+\chi_L(s)-Mq_s^b\right),
\]

where

\[
q_0^b=\frac2{D+1},
\qquad q_s^b=\frac1{D+1}\quad(s\ne0),
\]

and `chi_L=0` if `ell_L=0`, while

\[
\chi_L(s)=2\cos(2\pi s t_0/D)
\]

if `Gamma cap L={+-t_0v}`.  Line feasibility asks whether there is one
nonnegative probability vector `p_L` whose cyclic autocorrelation is `q_L`.

## New exact all-line convex-hull theorem to audit first

Let `u_s=1/D` and let `delta_0` be the point-mass autocorrelation.  Direct
substitution gives, for every line,

\[
q_L=a u+bq_L^\nu+c\delta_0+\frac{10}{MD}\chi_L,
\tag{H1}
\]

with

\[
a=\frac{D-10}{D+1},
\qquad
b=\frac{10m}{(m-1)D},
\qquad
c=\frac{D(m-11)-10m}{D(D+1)(m-1)}.
\tag{H2}
\]

For the frozen integers,

\[
a>0,\quad b>0,\quad c>0,\quad a+b+c=1.
\tag{H3}
\]

When `ell_L=0`, equation (H1) is already a convex combination of the
autocorrelations of the uniform distribution, `nu_L/m`, and a point mass.

When `ell_L=2`, define the explicit probability vector

\[
p_k^{\cos}=\frac{1+\cos(2\pi t_0k/D)}D\ge0.
\]

Its autocorrelation is

\[
q_s^{\cos}=u_s+\frac1{4D}\chi_L(s).
\tag{H4}
\]

With

\[
w=\frac{40}{M},
\qquad a-w>0,
\]

(H1) becomes

\[
\boxed{
q_L=(a-w)u+bq_L^\nu+c\delta_0+wq^{\cos}.
}
\tag{H5}
\]

Thus every one of the `D+1` exact frozen line shadows lies in the convex
hull of genuine nonnegative-probability autocorrelations.

Audit (H1)--(H5), including all Fourier normalizations and the exact sign of
every coefficient.  If valid, state the following correction explicitly:

\[
\boxed{
\text{No symmetric circulant copositive linear functional can exclude any
frozen line.}
}
\tag{NoLinearSeparator}
\]

This rules out not only Cayley cuts and SPN certificates, but also the
Round-16 proposed search for an exceptional non-SPN circulant separator.
Convex-hull membership does **not** prove that `q_L` itself is a single
autocorrelation; that is the remaining nonlinear/rank-one gap.

## Named Sidon line and an exact failed sufficient test

Take `L_0=< (0,1) >`, up to the fixed symplectic sign convention.  Its
projection values are the integers `t_j`.  Because they lie in an interval
of length less than `D/2`, and because

\[
t_j-t_k=t_{j'}-t_{k'}
\]

first forces `j-k=j'-k'` from the `2P` blocks and then forces `k=k'` modulo
the prime `P`, they form an oriented cyclic Sidon set.  Hence, with
`Delta=(T-T)\setminus{0}` and `|Delta|=M`,

\[
N_{L_0}(s)=\mathbf1_\Delta(s),
\qquad \chi_{L_0}=0,
\]

and

\[
q_{L_0,0}=\frac{2(D-10)}{D(D+1)},
\]

\[
q_{L_0,s}=\frac{D-10}{D(D+1)}
+\frac{10}{MD}\mathbf1_\Delta(s)
\quad(s\ne0).
\tag{S1}
\]

For

\[
E(s)=N_{L_0}(s)-Mq_s^b,
\]

the exact squared discrepancy is

\[
\boxed{
\sum_sE(s)^2
=M-\frac{M^2(D-1)}{(D+1)^2}.
}
\tag{S2}
\]

Round 16's quadratic sufficient condition for the all-positive square-root
factor has right side

\[
T=\frac{M^2D(1+1/\sqrt2)^2(1-1/\sqrt{D+1})^2}
{100(D^2-1)}.
\tag{S3}
\]

For the frozen integers, exact rational comparison using
`(1+1/sqrt(2))^2 < 583/200` proves

\[
\sum_sE(s)^2>100T.
\tag{S4}
\]

Audit the Sidon proof and (S1)--(S4).  This only disproves the usefulness of
that sufficient test on this line; it does not disprove factor existence.

## Required nonlinear attack

After the audits above, do not spend effort on any linear copositive or
Cayley separator.  Attack first the exact named-line question

\[
\exists p\in\mathbb R_+^D,
\quad \sum_kp_k=1,
\quad \sum_kp_kp_{k+s}=q_{L_0,s}\quad\forall s?
\tag{RankOne-L0}
\]

Use the special two-level Sidon form (S1), not merely the generic bound
`N_L(s)<=m`.  Pursue both directions as far as exact mathematics permits:

1. **Constructive route.**  Give an explicit finite rule for `p`, or an
   explicit phase rule for the fixed Fourier magnitudes, and prove every
   coordinate is nonnegative and every autocorrelation equation holds.
2. **Obstruction route.**  Derive an exact nonlinear inequality satisfied by
   every single nonnegative autocorrelation but not merely by its convex
   hull.  Evaluate it on (S1) with an exact finite certificate.
3. **Structural route.**  Exploit `D=4P^2+1`, the embedded Sidon set
   `t_j=2Pj+(j^2 mod P)`, and the exact multiplicities.  State clearly whether
   any theorem invoked applies to cyclic groups of this prime order and to
   real nonnegative factors.

Numerics may guide a proof but are not a certificate.  Do not claim
infeasibility from solver status, rounded eigenvalues, asymptotics, or a
convex-hull separation.  Do not claim feasibility without an explicit exact
factor or a theorem whose hypotheses are checked at the frozen integers.

If `RankOne-L0` is settled exactly, explain whether and how the argument
extends to all collision-free and one-double lines.  If it is not settled,
identify the earliest exact missing lemma and give the strongest rigorous
new bound you can prove.

End with separate `VERIFIED`, `CORRECTED`, `DISPROVED`, and `OPEN` lists.
The final verdict must state independently the status of:

- the all-line convex-hull theorem;
- exceptional non-SPN linear separation;
- the named-line single-factor problem;
- all-line spectral-factor feasibility;
- the physical `C(alpha)=1` lift; and
- PW10.

<!-- END HISTORICAL FILE path=work/round-17-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-17-response.md bytes=16899 sha256=1101f03bfdb93302a5e0ae92711561667b6e5a71e7f47ea7c540256f745340a5 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The linewise problem, however, is now closed:

$$
\boxed{
\text{Every one of the }D+1\text{ frozen line shadows }q_L
\text{ has a strictly positive cyclic probability factor.}
}
$$

In particular:

$$
\boxed{\text{\(\mathrm{RankOne}\text{-}L_0\) is PROVED feasible.}}
$$

The proposed convex-hull identities are also correct. Consequently,

$$
\boxed{
\text{no symmetric circulant copositive linear functional—SPN or non-SPN—can exclude any frozen line.}
}
$$

The remaining obstruction is no longer linewise phase retrieval. It is the genuinely two-dimensional cross-line condition

$$
C(\alpha)=1.
$$

No compatible global phase field with \(C(\alpha)=1\) is constructed, and no phase-uniform gap below \(1\) is proved.

---

# 1. Exact all-line convex-hull identity

Let

$$
q^\nu_{L,s}=\frac{A_L(s)}{m^2},
\qquad
A_L(s)=\sum_r\nu_L(r)\nu_L(r-s).
$$

Since \(\nu_L/m\) is a probability vector, \(q_L^\nu\) is its cyclic autocorrelation.

Also,

$$
N_L(s)=m^2q^\nu_{L,s}-m\delta_{s,0}.
$$

Starting from the frozen-shadow formula,

$$
q_{L,s}
=
q_s^b+
\frac{10}{MD}
\left[
N_L(s)+\chi_L(s)-Mq_s^b
\right],
$$

and using \(M=m(m-1)\), one obtains

$$
\begin{aligned}
q_L
={}&
\left(1-\frac{10}{D}\right)q^b
+
\frac{10m}{(m-1)D}q_L^\nu\\
&-
\frac{10}{(m-1)D}\delta_0
+
\frac{10}{MD}\chi_L.
\end{aligned}
\tag{1.1}
$$

The baseline satisfies

$$
q^b=\frac{D}{D+1}u+\frac1{D+1}\delta_0,
\qquad
u_s=\frac1D.
$$

Therefore

$$
\boxed{
q_L=a\,u+b\,q_L^\nu+c\,\delta_0+\frac{10}{MD}\chi_L,
}
\tag{H1}
$$

where

$$
\boxed{
a=\frac{D-10}{D+1},
\qquad
b=\frac{10m}{(m-1)D},
}
$$

and

$$
\boxed{
c=
\frac{D(m-11)-10m}
{D(D+1)(m-1)}.
}
\tag{H2}
$$

Direct common-denominator arithmetic gives

$$
a+b+c=1.
$$

For the exact integers,

$$
D(m-11)-10m
=
456803024442811242182018285>0.
$$

Hence

$$
\boxed{a>0,\qquad b>0,\qquad c>0,\qquad a+b+c=1.}
\tag{H3}
$$

When \(\ell_L=0\), one has \(\chi_L=0\), so \(q_L\) is already a convex combination of three genuine probability autocorrelations:

* the uniform distribution;
* the projection distribution \(\nu_L/m\);
* a point mass.

---

# 2. The double-projection lines

Suppose

$$
\Gamma\cap L=\{\pm t_0v\}.
$$

Define

$$
p_k^{\cos}
=
\frac{1+\cos(2\pi t_0k/D)}{D}.
$$

This is nonnegative, and

$$
\sum_kp_k^{\cos}=1.
$$

Its autocorrelation is

$$
\begin{aligned}
q_s^{\cos}
&=
\frac1{D^2}
\sum_k
\left[1+\cos\frac{2\pi t_0k}{D}\right]
\left[1+\cos\frac{2\pi t_0(k+s)}{D}\right]\\
&=
\frac1D+
\frac1{2D}
\cos\frac{2\pi t_0s}{D}.
\end{aligned}
$$

Since

$$
\chi_L(s)=2\cos\frac{2\pi t_0s}{D},
$$

this is

$$
\boxed{
q_s^{\cos}=u_s+\frac1{4D}\chi_L(s).
}
\tag{H4}
$$

Put

$$
w=\frac{40}{M}.
$$

Then

$$
wq^{\cos}=wu+\frac{10}{MD}\chi_L,
$$

so H1 becomes

$$
\boxed{
q_L=(a-w)u+bq_L^\nu+c\delta_0+wq^{\cos}.
}
\tag{H5}
$$

The remaining coefficient is strictly positive. Indeed,

$$
a-w
=
\frac{(D-10)M-40(D+1)}{M(D+1)},
$$

and the numerator is

$$
221624933455219617440240858220490620>0.
$$

Thus H5 is a genuine convex combination.

---

# 3. No circulant copositive separator exists

Let \(h_s=h_{-s}\), and let

$$
(H_h)_{jk}=h_{k-j}.
$$

For any probability vector \(p\) with autocorrelation

$$
q_s(p)=\sum_kp_kp_{k+s},
$$

one has

$$
p^{\mathsf T}H_hp
=
\sum_sh_sq_s(p).
$$

If \(H_h\) is copositive, then this pairing is nonnegative for every probability autocorrelation.

Every frozen \(q_L\) is, by H1 or H5, a convex combination of genuine probability autocorrelations. Hence

$$
\boxed{
\sum_sh_sq_{L,s}\ge0
}
$$

for every symmetric circulant copositive \(H_h\).

Therefore

$$
\boxed{
\text{No symmetric circulant copositive linear functional can exclude any frozen line.}
}
\tag{3.1}
$$

This includes exceptional non-SPN copositive matrices. The Round 16 proposal to search for such an exceptional separator is therefore definitively closed.

Convex-hull membership alone does not imply that \(q_L\) is one autocorrelation. That nonlinear question is addressed below.

---

# 4. The named line \(L_0\) is an oriented cyclic Sidon line

Take the generator sign so that the projection values are \(t_j\).

The largest frozen integer satisfies

$$
t_j
\le
2P(P-42)+(P-1)
=
2P^2-83P-1
<
2P^2
=
\frac{D-1}{2}.
$$

Hence all \(t_j\) lie in \([0,D/2)\).

Suppose

$$
t_j-t_k\equiv t_{j'}-t_{k'}\pmod D.
$$

Both differences are balanced representatives in \((-D/2,D/2)\), so the congruence is integer equality:

$$
2P(j-k-j'+k')
=
-(r_j-r_k-r_{j'}+r_{k'}).
$$

The right side has absolute value \(<2P\), while the left side is a multiple of \(2P\). Therefore

$$
j-k=j'-k'
$$

and

$$
r_j-r_k=r_{j'}-r_{k'}.
$$

Modulo \(P\),

$$
j^2-k^2\equiv j'^2-k'^2.
$$

Writing

$$
d=j-k=j'-k',
$$

gives

$$
2d(k-k')\equiv0\pmod P.
$$

For an off-diagonal difference, \(d\not\equiv0\pmod P\). Since \(P\) is an odd prime,

$$
k=k'\pmod P.
$$

All indices lie in \([0,P-1]\), so \(k=k'\), and then \(j=j'\).

Thus the nonzero ordered differences are unique. If

$$
\Delta=(T-T)\setminus\{0\},
\qquad T=\{t_j\},
$$

then

$$
|\Delta|=M,
$$

and

$$
\boxed{
N_{L_0}(s)=\mathbf1_\Delta(s),
\qquad
\chi_{L_0}=0.
}
$$

Consequently,

$$
\boxed{
q_{L_0,0}
=
\frac{2(D-10)}{D(D+1)},
}
$$

and, for \(s\ne0\),

$$
\boxed{
q_{L_0,s}
=
\frac{D-10}{D(D+1)}
+
\frac{10}{MD}\mathbf1_\Delta(s).
}
\tag{S1}
$$

---

# 5. Audit of the failed all-positive sufficient test

Put

$$
E(s)=N_{L_0}(s)-Mq_s^b.
$$

At \(s=0\),

$$
E(0)=-\frac{2M}{D+1}.
$$

For \(s\ne0\),

$$
E(s)=
\mathbf1_\Delta(s)-\frac{M}{D+1}.
$$

Since \(|\Delta|=M\),

$$
\boxed{
\sum_sE(s)^2
=
M-\frac{M^2(D-1)}{(D+1)^2}.
}
\tag{S2}
$$

Round 16’s quadratic sufficient threshold was

$$
T=
\frac{
M^2D(1+1/\sqrt2)^2
(1-1/\sqrt{D+1})^2
}{
100(D^2-1)
}.
$$

Now

$$
\left(1+\frac1{\sqrt2}\right)^2
=
\frac32+\sqrt2
<
\frac{583}{200},
$$

and

$$
\left(1-\frac1{\sqrt{D+1}}\right)^2<1.
$$

Thus

$$
100T
<
\frac{583M^2D}{200(D^2-1)}.
$$

The exact rational comparison reduces to the positive integer

$$
\begin{aligned}
&200(D^2-1)
\left[(D+1)^2-M(D-1)\right]\\
&\qquad
-583MD(D+1)^2\\
&=
3340025017235458794984328999875431866760348525178444365675305037471184720
>0.
\end{aligned}
$$

Therefore

$$
\boxed{
\sum_sE(s)^2>100T.
}
\tag{S4}
$$

This disproves only that particular sufficient estimate on \(L_0\). It does not obstruct factorization. The factor constructed below uses nontrivial imaginary Fourier phases rather than the all-positive root.

---

# 6. A universal Fourier floor for every frozen line

For a line \(L=\langle v\rangle\), define the prescribed line Fourier magnitudes

$$
X_L(t)=x^{(10)}_{tv}.
$$

Thus

$$
q_{L,s}
=
\frac1D\sum_tX_L(t)\omega^{-st}.
$$

For every nonzero label \(z\),

$$
x_z^{(10)}
=
\frac1{D+1}
+
\frac{10}{M}
\left[
\mathbf1_\Gamma(z)
+\frac{\lambda_z}{D}
-\frac{M}{D(D+1)}
\right].
$$

Using

$$
\mathbf1_\Gamma(z)\ge0,
\qquad
\lambda_z\ge-m,
$$

gives the exact lower bound

$$
x_z^{(10)}
\ge
\frac1{D+1}
-
\frac{10}{(m-1)D}
-
\frac{10}{D(D+1)}.
$$

Define

$$
\boxed{
\gamma
=
\frac{D(m-11)-10m}
{D(D+1)(m-1)}.
}
\tag{6.1}
$$

This is precisely the coefficient \(c\) from H2. It is positive, and

$$
\boxed{
X_L(t)\ge\gamma
\quad(t\ne0)
}
\tag{6.2}
$$

for every frozen line.

Put

$$
\rho=\sqrt\gamma.
$$

Since

$$
0<\gamma<\frac1{D+1}<\frac14,
$$

one has

$$
0<\rho<\frac12.
$$

---

# 7. Exact excess energy on a line

Line Parseval at \(s=0\) gives

$$
\sum_tX_L(t)=Dq_{L,0}.
$$

Using the audited formula

$$
q_{L,0}
=
\frac{2(D-10)}{D(D+1)}
+
\frac{20\ell_L}{MD},
$$

where \(\ell_L\in\{0,2\}\), one gets

$$
\sum_tX_L(t)
=
\frac{2(D-10)}{D+1}
+
\frac{20\ell_L}{M}.
$$

Define

$$
\mathcal E_L
=
\sum_{t\ne0}\left(X_L(t)-\gamma\right).
$$

A direct substitution of (6.1) gives

$$
\boxed{
\mathcal E_L
=
\frac{10(D-m)}{D(m-1)}
+
\frac{20\ell_L}{M}.
}
\tag{7.1}
$$

Since \(\ell_L\le2\),

$$
\mathcal E_L
<
\frac{10}{m-1}
+
\frac{40}{m(m-1)}
<
\frac{11}{m-1}.
\tag{7.2}
$$

Because

$$
m-1=485165195>10560,
$$

we have

$$
\boxed{\mathcal E_L<\frac1{960}.}
\tag{7.3}
$$

This small excess energy is the quantitative input that closes the nonlinear factor problem.

---

# 8. A strictly positive spectral factor for every line

Fix one representative set \(H_L\) from the nonzero pairs

$$
\{t,-t\}\subset\mathbb F_D.
$$

For \(t\in H_L\), put

$$
\eta_t=\sqrt{X_L(t)-\gamma}.
$$

Choose signs

$$
\varepsilon_t\in\{-1,+1\}
$$

and define the Fourier coefficients

$$
\widehat p_L(0)=1,
$$

$$
\boxed{
\widehat p_L(t)=\rho+i\varepsilon_t\eta_t,
\qquad
\widehat p_L(-t)=\rho-i\varepsilon_t\eta_t.
}
\tag{8.1}
$$

Then

$$
|\widehat p_L(t)|^2
=
\rho^2+\eta_t^2
=
X_L(t).
$$

Define the inverse transform

$$
p_{L,k}
=
\frac1D\sum_t
\widehat p_L(t)\omega^{-kt}.
$$

It is real, and

$$
\sum_kp_{L,k}=\widehat p_L(0)=1.
$$

At \(k=0\),

$$
\boxed{
p_{L,0}
=
\frac{1+(D-1)\rho}{D}>0.
}
\tag{8.2}
$$

For \(k\ne0\),

$$
\boxed{
p_{L,k}
=
\frac{1-\rho}{D}
+
\frac2D
\sum_{t\in H_L}
\varepsilon_t\eta_t
\sin\frac{2\pi kt}{D}.
}
\tag{8.3}
$$

The deterministic term is positive. It remains to choose the signs so that the fluctuating term never cancels it.

---

# 9. Exact sign-balancing estimate

Choose the signs independently and uniformly.

For fixed \(k\ne0\), the random summands in (8.3) are independent and centered. The summand indexed by \(t\) ranges over an interval of length at most

$$
\frac{4\eta_t}{D}.
$$

Moreover,

$$
\sum_{t\in H_L}\eta_t^2
=
\frac{\mathcal E_L}{2}.
$$

For any \(\tau>0\),

$$
\mathbb E e^{-\tau X}
=
\cosh(\tau a)
\le e^{\tau^2a^2/2}
$$

for a symmetric two-point variable \(X=\pm a\). Hence, with

$$
\mu=\frac{1-\rho}{D},
$$

one obtains

$$
\Pr\{p_{L,k}\le0\}
\le
\exp\left(
-\frac{(1-\rho)^2}{4\mathcal E_L}
\right).
\tag{9.1}
$$

Define

$$
K_L=\frac{(1-\rho)^2}{4\mathcal E_L}.
$$

Since \(\rho<1/2\),

$$
(1-\rho)^2>\frac14.
$$

Together with (7.2),

$$
K_L
>
\frac{m-1}{176}
>60.
\tag{9.2}
$$

Therefore

$$
\Pr\{\exists k\ne0:p_{L,k}\le0\}
\le
(D-1)e^{-K_L}
<
De^{-60}.
$$

Now

$$
D<2^{60},
\qquad
2^{60}-D=211380275833782299>0,
$$

and \(e>2\), so

$$
De^{-60}<D2^{-60}<1.
$$

Consequently, there exists a sign assignment for which

$$
\boxed{
p_{L,k}>0\quad\forall k.
}
\tag{9.3}
$$

Finally,

$$
\widehat q_L(t)
=
|\widehat p_L(t)|^2
=
X_L(t),
$$

so Fourier inversion gives

$$
\boxed{
q_{L,s}=\sum_kp_{L,k}p_{L,k+s}
\quad\forall s.
}
\tag{9.4}
$$

This proves the existence of a single strictly positive factor—not merely convex-hull membership.

---

# 10. An explicit finite deterministic sign rule

The preceding probabilistic proof can be derandomized.

Order the representatives

$$
H_L=\{t_1,\ldots,t_{(D-1)/2}\}
$$

by their least positive residues. Put

$$
a_{j,k}
=
\frac{2\eta_{t_j}}{D}
\sin\frac{2\pi kt_j}{D},
\qquad
\mu=\frac{1-\rho}{D},
$$

and set

$$
\tau=
\frac{D(1-\rho)}{2\mathcal E_L}.
$$

After signs \(\varepsilon_1,\ldots,\varepsilon_r\) have been fixed, define

$$
\begin{aligned}
\Phi_r
=
\sum_{k=1}^{D-1}
&
\exp\left[
-\tau
\left(
\mu+\sum_{j\le r}\varepsilon_ja_{j,k}
\right)
\right]\\
&\times
\prod_{j>r}\cosh(\tau a_{j,k}).
\end{aligned}
\tag{10.1}
$$

At each step choose the sign \(\varepsilon_{r+1}\) giving the smaller value of \(\Phi_{r+1}\), choosing \(+1\) on a tie.

Because the average of the two possible next values equals \(\Phi_r\), the potential never increases.

Furthermore,

$$
\sum_ja_{j,k}^2
\le
\frac{2\mathcal E_L}{D^2},
$$

so

$$
\Phi_0
\le
(D-1)e^{-K_L}<1.
$$

At the final stage,

$$
\Phi_{(D-1)/2}
=
\sum_{k=1}^{D-1}e^{-\tau p_{L,k}}<1.
$$

If some \(p_{L,k}\le0\), its summand would be at least \(1\), a contradiction. Thus the greedy rule produces the required strictly positive factor.

This is an explicit finite rule, although its direct execution at the displayed \(D\) is enormous.

---

# 11. Consequences

## 11.1 The named line

Applying the construction to \(L_0\) proves

$$
\boxed{
\exists p_{L_0}>0:
\quad
q_{L_0,s}
=
\sum_kp_{L_0,k}p_{L_0,k+s}.
}
$$

Therefore

$$
\boxed{\mathrm{RankOne}\text{-}L_0\text{ is feasible}.}
$$

The failure of the all-positive-root sufficient test in S4 does not indicate infeasibility; it merely shows that nontrivial phases are needed.

## 11.2 Every frozen line

The argument used only:

* the universal nonzero-mode floor \(X_L(t)\ge\gamma\);
* the exact line purity \(q_{L,0}\);
* \(\ell_L\in\{0,2\}\).

Hence it applies uniformly to all \(D+1\) lines:

$$
\boxed{
\forall L\ \exists p_L>0:
\quad
q_{L,s}
=
\sum_kp_{L,k}p_{L,k+s}.
}
\tag{11.1}
$$

Thus

$$
\boxed{\text{the full stabilizer-projector layer is feasible for }x^{(10)}.}
$$

Because the nonzero labels partition among the lines, the linewise Fourier phases can be combined into one global coefficient field having all stabilizer marginals strictly positive.

---

# 12. The stabilizer layer is now unconditionally insufficient

Round 15 proved conditionally that independent character shifts on the lines preserve all line marginals, preserve the same-line cubic contribution \(C_{\rm dep}\), and average the linearly independent cubic contribution to zero.

Line feasibility has now been proved, so that conditional statement becomes unconditional.

There exists a global coefficient field with magnitudes \(x^{(10)}\) such that

$$
p_{L,k}>0
\quad\text{for every }L,k,
$$

but, after suitable independent line shifts,

$$
C(\alpha)
\le
C_{\rm dep}
<
2\sqrt{\frac3D}-\frac1D
<
3.571\times10^{-9}
<1.
$$

Hence

$$
\boxed{
\text{all stabilizer-projector positivity constraints do not imply physicality.}
}
\tag{12.1}
$$

This field is nonphysical because \(C(\alpha)\ne1\).

This does not exclude a different global choice of cross-line phases with \(C(\alpha)=1\).

---

# 13. Earliest remaining gap

The entire one-dimensional phase-retrieval layer is now closed:

$$
\boxed{
\text{every exact frozen line shadow has a strictly positive single factor.}
}
$$

The first unresolved issue for \(x^{(10)}\) is therefore the cross-line phase coherence needed to make

$$
C(\alpha)=1.
$$

Equivalently, one must decide whether the line phases can be selected jointly so that the linearly independent Weyl-pair contribution raises the cubic from its tiny same-line value to exactly one.

No such phase field is constructed.

No uniform bound

$$
C(\alpha)\le1-\eta
$$

for every compatible global phase field is proved.

Even excluding \(x^{(10)}\) would not prove PW10 for every physical magnitude profile.

Therefore PW10 remains open.

---

# VERIFIED

* The all-line decomposition H1–H3.
* The cosine autocorrelation H4.
* The convex decomposition H5.
* Positivity of all four H5 coefficients at the exact frozen integers.
* No symmetric circulant copositive linear functional can separate any frozen line.
* The named projection \(T=\{t_j\}\) is an oriented cyclic Sidon set.
* The exact two-level shadow S1.
* The exact discrepancy identity S2.
* The exact comparison S4 showing failure of the all-positive quadratic sufficient test.
* The universal Fourier floor

  $$
  X_L(t)\ge\gamma\quad(t\ne0).
  $$
* The exact excess-energy formula

  $$
  \mathcal E_L
  =
  \frac{10(D-m)}{D(m-1)}
  +
  \frac{20\ell_L}{M}.
  $$
* The uniform bound \(\mathcal E_L<11/(m-1)\).
* The finite sign-balancing construction.
* The deterministic greedy derandomization.
* Strictly positive cyclic spectral factors for every frozen line.
* Feasibility of \(\mathrm{RankOne}\text{-}L_0\).
* Feasibility of the complete stabilizer-projector layer.
* Unconditional insufficiency of the complete stabilizer-projector layer for physical cubic lifting.

# CORRECTED

* Convex-hull membership does not by itself give one factor, but in this frozen problem a separate sign-balancing argument does.
* The failed all-positive-root estimate on \(L_0\) is not evidence of line infeasibility.
* The Round 16 exceptional non-SPN copositive-separator search is impossible: H1–H5 rule out every circulant copositive linear separator, not merely SPN ones.
* The first remaining obstruction is no longer linewise spectral factorization.

# DISPROVED

* Existence of a symmetric circulant copositive linear separator for any frozen line.
* Infeasibility of the named line \(L_0\).
* Infeasibility of any frozen stabilizer line.
* Sufficiency of all stabilizer-projector positivity constraints for physicality.

# OPEN

* Whether the exact magnitude profile \(x^{(10)}\) admits global compatible phases with

  $$
  C(\alpha)=1.
  $$
* Whether every compatible global phase field for \(x^{(10)}\) satisfies a uniform cubic gap below \(1\).
* Whether some different objective-above-\(10\) magnitude profile has a physical lift.
* PW10 for the exact frozen tuple.
* The finite \(r=2\) low-\(A\) gate.

The first new claim requiring independent verification is the uniform line-factor theorem of Sections 6–10, especially the exact excess-energy identity (7.1) and the sign-balancing bound

$$
(D-1)\exp\!\left(
-\frac{(1-\sqrt\gamma)^2}{4\mathcal E_L}
\right)<1.
$$

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-17-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-17-local-audit.md bytes=8765 sha256=9c0a79c46fb5d0d20354201129311469601ea752e60b2ee3cc94d59e2f12f4ef -->

# Round 17 local audit

- Audit completed (UTC): `2026-09-13T03:12:24Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-17-response.md`
- Web-response SHA-256:
  `1101f03bfdb93302a5e0ae92711561667b6e5a71e7f47ea7c540256f745340a5`
- Browser completion indicator: `Worked for 18m 30s`
- Capture equality: the browser response-copy payload, artifact, and output
  copy are text-identical; the two files are byte-identical, each `16,899`
  bytes, `16,885` Unicode characters, and `1,176` lines.

## Verdict

The central new theorem in the Round 17 response survives independent
checking:

\[
\boxed{
\text{every one of the }D+1\text{ exact frozen line shadows has a strictly
positive cyclic probability factor.}
}
\]

This is a finite exact existence proof, not numerical evidence and not only
convex-hull membership.  It closes the named-line and all-line spectral-factor
gates.  The factors on the different projective lines use disjoint nonzero
Weyl labels, so they assemble into one global compatible coefficient field
passing every stabilizer-projector inequality strictly.

Combining this theorem with the independently audited line-character shifts
from Round 15 makes the previous conditional separation unconditional: there
exists a field with the exact magnitudes `x^(10)` which passes the complete
stabilizer layer but has

\[
C(\alpha)\le C_{\rm dep}
<2\sqrt{3/D}-1/D
<3.571\times10^{-9}<1.
\]

Thus the complete stabilizer layer is rigorously insufficient for physicality.
This does not exclude another compatible phase field with `C(alpha)=1`.
PW10 and the finite `r=2` low-`A` gate remain open.

## Convex-hull and named-line audits

The response correctly expands the frozen shadow as

\[
q_L=a u+bq_L^\nu+c\delta_0+\frac{10}{MD}\chi_L,
\]

where

\[
a=\frac{D-10}{D+1},\qquad
b=\frac{10m}{(m-1)D},\qquad
c=\frac{D(m-11)-10m}{D(D+1)(m-1)}.
\]

Exact common-denominator arithmetic gives `a+b+c=1`, and every coefficient
is positive.  On a one-double line, the probability vector

\[
p_k^{\cos}=\frac{1+\cos(2\pi t_0k/D)}D
\]

has autocorrelation

\[
q_s^{\cos}=\frac1D+\frac1{4D}\chi_L(s).
\]

Therefore, with `w=40/M`,

\[
q_L=(a-w)u+bq_L^\nu+c\delta_0+wq^{\cos}.
\]

The exact numerator proving `a-w>0` is

\[
221624933455219617440240858220490620.
\]

It follows that no symmetric circulant copositive linear functional, whether
SPN or exceptional non-SPN, can exclude any frozen line.  This closes the
entire linear-separator route.

The response's Sidon proof for `L_0=< (0,1) >` is correct.  The interval
bound removes modular wraparound; equality of oriented differences forces
equal index differences, and reduction modulo the prime `P` then forces both
ordered pairs to agree.  Hence

\[
N_{L_0}(s)=\mathbf1_\Delta(s),\qquad |\Delta|=M,
\]

and the displayed two-level shadow is exact.  The discrepancy identity

\[
\sum_sE(s)^2=M-\frac{M^2(D-1)}{(D+1)^2}
\]

also checks.  The rational comparison used to prove that this exceeds one
hundred times the Round 16 sufficient threshold reduces to the stated
positive integer

\[
3340025017235458794984328999875431866760348525178444365675305037471184720.
\]

As the response correctly notes, failure of that sufficient test is not
evidence of factor infeasibility.

## Independent audit of the Fourier-floor factor theorem

For each line put `X_L(t)=x^(10)_(tv)`.  From

\[
\lambda_z=\left|\sum_j\omega^{[a_j,z]}\right|^2-m\ge-m
\]

and `1_Gamma(z)>=0`, every nonzero line mode has the exact common floor

\[
X_L(t)\ge\gamma,
\qquad
\gamma=
\frac{D(m-11)-10m}{D(D+1)(m-1)}>0.
\]

Moreover `gamma<1/(D+1)<1/4`.  Set `rho=sqrt(gamma)`.  Line Parseval and the
two possible values `ell_L in {0,2}` give the exact excess energy

\[
\boxed{
\mathcal E_L
=\sum_{t\ne0}(X_L(t)-\gamma)
=\frac{10(D-m)}{D(m-1)}+\frac{20\ell_L}{M}.
}
\]

The frozen integers imply

\[
0<\mathcal E_L<\frac{11}{m-1}<\frac1{960}.
\]

For one representative `t` of every inverse pair, define

\[
\widehat p_L(t)=\rho+i\varepsilon_t\sqrt{X_L(t)-\gamma},
\qquad
\widehat p_L(-t)=\overline{\widehat p_L(t)},
\qquad
\widehat p_L(0)=1.
\]

This has exactly the required Fourier magnitudes.  Its inverse transform is
real, sums to one, and satisfies

\[
p_{L,0}=\frac{1+(D-1)\rho}{D}>0,
\]

\[
p_{L,k}=\frac{1-\rho}{D}
+\frac2D\sum_{t\in H_L}\varepsilon_t
\sqrt{X_L(t)-\gamma}\sin(2\pi kt/D)
\quad(k\ne0).
\]

For fixed nonzero `k`, Hoeffding's one-sided bound has exactly the exponent

\[
K_L=\frac{(1-\rho)^2}{4\mathcal E_L}.
\]

There is no missing factor two: the squared amplitudes on representatives
sum to `E_L/2`, while each centered summand has range length at most
`4 eta_t/D`.  Since `rho<1/2`,

\[
K_L>\frac{m-1}{176}>60.
\]

The union bound on one line is therefore

\[
(D-1)e^{-K_L}<De^{-60}<D2^{-60}<1,
\]

where the exact integer check is

\[
2^{60}-D=211380275833782299>0.
\]

Positive probability in a finite sign space proves existence of one sign
assignment with every coordinate strictly positive.  Fourier inversion then
gives the prescribed autocorrelation exactly.

The response's conditional-expectation derandomization is also valid.  Its
potential is the conditional exponential-moment union bound; averaging its
two possible next-sign values reproduces the current potential.  The initial
potential is below one, so the greedy smaller-child rule ends with every
`p_(L,k)>0`.  This is an explicit finite rule, although direct execution at
the frozen dimension is enormous.

An independent variant gives an even more direct simultaneous theorem.  The
exact hull Fourier transform can be written, for `t!=0`, as

\[
X_L(t)=\gamma+\zeta_L(t),
\]

\[
\zeta_L(t)=\frac{10}{MD}|S_L(t)|^2
+\frac{10}{M}\mathbf1_{\Gamma\cap L}(tv)\ge0.
\]

Using unnormalized Parseval,

\[
\sum_t|S_L(t)|^2=D(m+\ell_L),
\]

one obtains

\[
\sum_{t\in H_L}\zeta_L(t)
<\frac{5m+20}{M}<\frac1{10000}.
\]

The corresponding one-sided exponent exceeds `312.5`.  A single union bound
over all `(D+1)(D-1)=D^2-1` nonzero line marginals is below one because
`D^2-1<2^300<e^300`.  Thus one finite simultaneous sign assignment also
proves the all-line result without invoking a separate choice on each line.

## Verification receipts

- `work/verify_round17_web_response.py` checks the captured response hash,
  required claims, every displayed frozen integer, the convex coefficients,
  the Sidon-threshold comparison, the Fourier floor, the exact excess-energy
  identity, and the Hoeffding normalization.  Result: `PASS`.
- Checker SHA-256:
  `1cf585000d167944a64cfda93781cf500f892ef02fd13a2d6d1a8855a40b5511`
- `work/verify_round17_random_quadrature.py` independently checks the
  simultaneous variant's rational inequalities.  Result: `PASS`.
- Independent checker SHA-256:
  `71eafc9749953c5ceffb835130e268603634a649c02eeff13444120af0e40e69`
- Independent derivation:
  `work/round-17-independent-random-quadrature-factor.md`
- Independent-derivation SHA-256:
  `3cc06b4b66a3ab70c9c15598eaca72dedf0d72110652afd2aa24f6b141e8fed6`

Both Python files also pass `py_compile`.

## Corrected status ledger

### VERIFIED

- The all-line convex-hull identities and positivity of every coefficient.
- Impossibility of every symmetric circulant copositive linear separator.
- The named Sidon line and its exact two-level shadow.
- Failure of the Round 16 quadratic sufficient test on the named line.
- The universal positive Fourier floor and exact excess-energy formula.
- The randomized sign-balancing proof and deterministic greedy version.
- One strictly positive cyclic probability factor for every frozen line.
- Simultaneous feasibility of all stabilizer-projector inequalities.
- Existence of a stabilizer-positive but nonphysical field with the exact
  magnitudes `x^(10)`.

### CORRECTED / SUPERSEDED

- The named-line factor problem is no longer open.
- The all-line spectral-factor problem is no longer open.
- The first remaining obstruction for `x^(10)` is now genuinely cross-line,
  not one-dimensional phase retrieval.

### DISPROVED

- Existence of any symmetric circulant copositive separator for a frozen
  line.
- Infeasibility of the named line or of any other frozen line.
- Sufficiency of the complete stabilizer-projector layer for physicality.

### OPEN

- Whether `x^(10)` has any compatible phase field with `C(alpha)=1`.
- Whether every compatible phase field for `x^(10)` has a uniform cubic gap
  below one.
- Whether another objective-above-10 magnitude profile has a physical lift.
- PW10 for the exact frozen tuple.
- The finite `r=2` low-`A` gate and all downstream conclusions.

Even an exact exclusion of `x^(10)` would not prove PW10 for all physical
magnitude profiles.  No such quantifier promotion is made here.

<!-- END HISTORICAL FILE path=outputs/round-17-local-audit.md -->


# ROUND 018

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-18-prompt.md bytes=8680 sha256=b94d3d03e6d96f5c1d2b2658dbf03fcd6e035ee746f7b8c059ab5ba8222afa07 -->

# Round 18 — close the line chapter and attack the first cross-line invariant

Continue in the same ordinary Chat conversation and the same canonically
frozen finite `r=2`, low-`A` gate.  Give a public, self-contained derivation
and no hidden chain-of-thought.  Do not repeat the Round 8--16 narrative.

## Exact frozen boundary

Use exactly

\[
m=485165196,
\quad P=485165237=m+41,
\quad D=941541228773064677=4P^2+1,
\]

\[
0\le j\le P-42,
\quad r_j=j^2\bmod P,
\quad t_j=2Pj+r_j,
\quad a_j=(t_j,t_j^2),
\]

\[
A=\{a_j\},
\quad \Gamma=(A-A)\setminus\{0\},
\quad M=m(m-1)=235385266924553220.
\]

The open physical gate remains

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10
\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use

\[
W_{(p,q)}|y\rangle=\omega^{p(y+q/2)}|y+q\rangle,
\qquad
W_uW_v=\omega^{[u,v]/2}W_{u+v}.
\]

The exact magnitude pseudo-point is

\[
b_0=1,
\qquad b_z=\frac1{D+1}\quad(z\ne0),
\]

\[
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\quad y=\mathbf1_\Gamma+\lambda/D,
\quad d=y-(M/D)b,
\quad x^{(10)}=b+(10/M)d.
\]

It is positive, even, self-Fourier, has mass `D`, passes every audited
magnitude, small-Gram, parity, and stabilizer condition, and has frozen
objective strictly above `10`.  A physical lift requires compatible phases
with

\[
R_\alpha=D^{-1}\sum_z\alpha_zW_z,
\qquad
C(\alpha)=\operatorname{Tr}R_\alpha^3=1.
\tag{PhysicalCubic}
\]

Do not promote a pseudo-field into a physical state or exclusion of this one
pseudo-point into PW10.

## Independently checked Round 17 theorem

For a projective isotropic line `L=<v>`, write

\[
X_L(t)=x^{(10)}_{tv},
\qquad
q_{L,s}=D^{-1}\sum_tX_L(t)\omega^{-st},
\]

and let `ell_L=|Gamma cap L| in {0,2}`.  Define

\[
\gamma=
\frac{D(m-11)-10m}{D(D+1)(m-1)},
\qquad
\rho=\sqrt\gamma.
\]

The exact pointwise floor and excess energy are

\[
X_L(t)\ge\gamma\quad(t\ne0),
\]

\[
\boxed{
\mathcal E_L
=\sum_{t\ne0}(X_L(t)-\gamma)
=\frac{10(D-m)}{D(m-1)}+\frac{20\ell_L}{M}
<\frac{11}{m-1}<\frac1{960}.
}
\tag{LineExcess}
\]

For one representative of every inverse pair `{t,-t}`, put

\[
\widehat p_L(t)
=\rho+i\varepsilon_t\sqrt{X_L(t)-\gamma},
\qquad
\widehat p_L(-t)=\overline{\widehat p_L(t)},
\qquad
\widehat p_L(0)=1.
\tag{Quadrature}
\]

For `k!=0`, its inverse Fourier transform is

\[
p_{L,k}=\frac{1-\rho}{D}
+\frac2D\sum_{t\in H_L}\varepsilon_t
\sqrt{X_L(t)-\gamma}\sin(2\pi kt/D).
\]

The exact one-sided bound is

\[
\Pr\{p_{L,k}\le0\}
\le
\exp\!\left[-\frac{(1-\rho)^2}{4\mathcal E_L}\right].
\]

Since the exponent is greater than `(m-1)/176>60` and `D<2^60`, a union
bound is below one.  Thus every line has a strictly positive factor.  The
conditional-expectation potential also gives a finite greedy sign rule.
Different lines have disjoint nonzero labels, so all `D+1` factors assemble
into one global phase field satisfying all `D(D+1)` stabilizer inequalities.

An independent stronger bookkeeping variant chooses all line signs at once:
for `t!=0`,

\[
X_L(t)=\gamma+\zeta_L(t),
\qquad
\zeta_L(t)=\frac{10}{MD}|S_L(t)|^2
+\frac{10}{M}\mathbf1_{\Gamma\cap L}(tv),
\]

and

\[
\sum_{t\in H_L}\zeta_L(t)<\frac{5m+20}{M}<\frac1{10000}.
\]

The exponent then exceeds `312.5`, and the union bound over all
`D^2-1<2^300` nonzero line marginals is below one.  Audit all of these
normalizations, including the two versions of the exponent, before using the
theorem.

Round 15's independent line-character shifts now make this consequence
unconditional:

\[
\boxed{
\exists\alpha:\quad
p_{L,k}>0\ \forall L,k,
\qquad
C(\alpha)\le C_{\rm dep}
<2\sqrt{3/D}-1/D<3.571\times10^{-9}<1.
}
\tag{StabilizerNotPhysical}
\]

This proves only that the complete stabilizer layer is insufficient.  It does
not exclude another phase field with `C(alpha)=1`.

## First cross-line statistic to audit

Fix one generator `v_L` for each projective line and write each nonzero label
uniquely as `z=t_z v_(L_z)`.  For arbitrary line-character shifts

\[
\alpha_z\longmapsto
\alpha_z\omega^{\kappa_{L_z}t_z},
\qquad
\kappa_L\in\mathbb F_D,
\]

let `C_ind(kappa)` be the portion of the cubic from linearly independent
ordered pairs.  If `u+v+w=0` and `u,v,w` lie on three distinct lines, grouping
the six permutations proposes

\[
\sum_{\text{six orders}}
\omega^{[\cdot,\cdot]/2}
=3\left(\omega^{[u,v]/2}+\omega^{-[u,v]/2}\right)
=6\operatorname{Re}\omega^{[u,v]/2}.
\tag{SixPerm}
\]

Let `T` run over unordered nonzero zero-sum triples on three distinct lines,
with `T` and `-T` retained as distinct triples.  Character orthogonality then
proposes the exact line-shift Parseval identity

\[
\boxed{
\mathbb E_\kappa |C_{\rm ind}(\kappa)|^2
=\frac{36}{D^4}
\sum_T
\left(\operatorname{Re}\omega^{[u,v]/2}\right)^2
x_u^{(10)}x_v^{(10)}x_w^{(10)}.
}
\tag{ShiftParseval-T}
\]

Equivalently,

\[
\boxed{
\mathbb E_\kappa |C_{\rm ind}(\kappa)|^2
=\frac6{D^4}
\sum_{u,v\ \mathrm{independent}}
\left(\operatorname{Re}\omega^{[u,v]/2}\right)^2
x_u^{(10)}x_v^{(10)}x_{-u-v}^{(10)}.
}
\tag{ShiftParseval-ord}
\]

Audit this carefully.  In particular, use the field inverse of `2`; do not
silently replace `Re omega^([u,v]/2)` by a real-angle cosine with the wrong
representative.  Check whether distinct unordered triples really give
distinct characters of the product shift group, and correct the factor `6`
or the treatment of `T,-T` if necessary.

## Exact tasks

1. Give one verdict for PW10 on this exact frozen tuple: **PROVED**,
   **DISPROVED**, or **OPEN WITH EARLIEST GAP**.

2. Audit `LineExcess`, `Quadrature`, both sign-balancing union bounds, the
   greedy derandomization, and `StabilizerNotPhysical`.  State explicitly that
   the named line and all-line spectral-factor gates are closed.

3. Prove or correct `SixPerm` and the two `ShiftParseval` formulas.  Then use
   the exact formula for `x^(10)`, not only `x<=1`, to obtain the strongest
   exact upper bound you can on the shift RMS.  Separate an average/RMS bound
   from a uniform bound; a tiny average does not exclude one phase choice with
   `C=1`.

4. Attack the physical lift itself.  In priority order, produce one of:

   - compatible phases satisfying the full twisted-idempotence equations,
     hence `C(alpha)=1` and an exact physical PW10 counterexample;
   - an explicit positive `eta` and a proof that every compatible phase field
     for `x^(10)` obeys `C(alpha)<=1-eta`;
   - a finite cross-line Hessian, moment, or sum-of-squares certificate whose
     verified sign would exclude `C=1`, together with an exact evaluation on
     the frozen data.

   For the Hessian route, use the fact that any `C=1` phase field is a global
   maximizer of `C` on the Hermitian fixed-magnitude phase torus.  Derive the
   first- and second-variation matrices explicitly and determine whether a
   bounded principal minor or a symmetry-averaged direction gives a
   phase-free contradiction.  Naming stationarity without evaluating it is
   not a certificate.

5. If the exact `x^(10)` lift remains unresolved, do not spend another round
   constructing a nonphysical pseudo-field.  Return to the direct product
   problem

\[
\mathcal F_\Gamma(\psi)
=\langle\psi\otimes\bar\psi|K_\Gamma|
\psi\otimes\bar\psi\rangle,
\qquad
K_\Gamma=\sum_{g\in\Gamma}W_g\otimes\overline{W_g},
\]

   and derive a genuinely stronger exact product-state/SOS constraint than
   the already-passed magnitude, parity, small-Gram, and stabilizer layers.
   Either prove it bounds the objective by `10`, or exhibit an exact physical
   vector above `10`.  A relaxation value above `10` is not a counterexample.

6. Preserve the quantifiers.  Excluding `x^(10)` alone would not prove PW10,
   while a physical lift of `x^(10)` would disprove PW10 because its frozen
   objective is strictly above `10`.

7. Do not return to Cayley/circulant line separators, the all-positive line
   factor, five-carry arithmetic, Perron--Schur10, or the downstream all-`T`
   ratio without a new exact certificate.  Those routes have already been
   exhausted or remain strictly weaker than the current gate.

8. End with a plain ledger separating **VERIFIED**, **CORRECTED**,
   **DISPROVED**, **NECESSARY-ONLY**, **SUFFICIENT-ONLY**, and **OPEN**.  State
   separately the status of the line-factor theorem, complete stabilizer
   feasibility, `ShiftParseval`, the physical `C=1` lift, `x^(10)`, PW10, and
   the finite `r=2` gate.  Identify the first new claim requiring independent
   verification.

The purpose of this round is to stop treating one-dimensional positivity as
the bottleneck and obtain the first exact two-dimensional phase-coherence
certificate—or to expose precisely why the line-shift moment route cannot be
uniformized.

<!-- END HISTORICAL FILE path=work/round-18-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-18-response.md bytes=23320 sha256=b1fa58adab6a2b9007273febee95a33b57ec33629b339bf9817fde9bd0afe49d -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The one-dimensional chapter is closed:

$$
\boxed{
\text{the named line and every one of the }D+1\text{ frozen line shadows admit a strictly positive factor.}
}
$$

The complete stabilizer-projector layer is therefore feasible. It is also unconditionally insufficient for physicality: there is a compatible stabilizer-positive field with cubic \(C<3.571\times10^{-9}\).

The proposed six-permutation identity and both line-shift Parseval formulas are correct. They give the exact bound

$$
\boxed{
\left(\mathbb E_\kappa|C_{\mathrm{ind}}(\kappa)|^2\right)^{1/2}
<
2.682\times10^{-27}.
}
$$

This is only an average bound. An explicit degree-three character polynomial with the same \(D^{-3/2}\) RMS scale and supremum \(1\) proves that the line-shift moment cannot, by itself, be uniformized into a phase-independent cubic gap.

The first exact cross-line layer can nevertheless be compressed substantially. Stabilizer positivity together with a family of \(2\times2\) cross-basis Cauchy inequalities is **equivalent** to physical rank-one lifting. Equivalently, the structured stabilizer residuals

$$
\delta_{L,k}
=
\operatorname{Tr}\!\left[P_{L,k}(R_\alpha^2-R_\alpha)\right]
$$

obey the exact sum-of-squares identity

$$
\boxed{
\sum_{L,k}\delta_{L,k}^2
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
}
$$

For the stabilizer-positive nonphysical field already constructed, this sum is strictly positive and forces a definite cross-line \(2\times2\) violation. What remains open is whether some other choice of phases for the same magnitudes \(x^{(10)}\) makes every one of these cross-line residuals vanish.

---

# 1. Audit of the line-factor theorem

Fix a projective line \(L=\langle v_L\rangle\), and define

$$
S_L(t)
=
\sum_{j=0}^{m-1}\omega^{[a_j,tv_L]}.
$$

For \(t\neq0\),

$$
\lambda_{tv_L}=|S_L(t)|^2-m.
$$

From the exact definition of \(x^{(10)}\),

$$
x^{(10)}_{tv_L}
=
\gamma+\zeta_L(t),
$$

where

$$
\gamma
=
\frac{D(m-11)-10m}
{D(D+1)(m-1)}
$$

and

$$
\boxed{
\zeta_L(t)
=
\frac{10}{MD}|S_L(t)|^2
+
\frac{10}{M}\mathbf 1_{\Gamma\cap L}(tv_L).
}
\tag{1.1}
$$

Thus the stated quadrature form is

$$
\widehat p_L(t)
=
\rho+i\varepsilon_t\sqrt{\zeta_L(t)},
\qquad
\rho=\sqrt\gamma,
$$

on one representative of each inverse pair, with conjugate values at \(-t\) and \(\widehat p_L(0)=1\).

## 1.1 Parseval bookkeeping on a line

Let

$$
\ell_L=|\Gamma\cap L|\in\{0,2\}.
$$

The projection multiplicities satisfy

$$
\sum_r\nu_L(r)^2=m+\ell_L.
$$

Therefore finite Fourier Parseval gives

$$
\sum_{t\in\mathbb F_D}|S_L(t)|^2
=
D(m+\ell_L).
$$

Since \(S_L(0)=m\), and the nonzero terms occur in inverse pairs,

$$
\sum_{t\in H_L}|S_L(t)|^2
=
\frac{D(m+\ell_L)-m^2}{2}.
$$

Also,

$$
\sum_{t\in H_L}
\mathbf 1_{\Gamma\cap L}(tv_L)
=
\frac{\ell_L}{2}.
$$

Consequently,

$$
\begin{aligned}
Z_L
&:=
\sum_{t\in H_L}\zeta_L(t)\\
&=
\frac{5[D(m+\ell_L)-m^2]}{MD}
+
\frac{5\ell_L}{M}\\
&=
\boxed{
\frac{5(D-m)}{D(m-1)}
+
\frac{10\ell_L}{M}.
}
\end{aligned}
\tag{1.2}
$$

The full excess energy is therefore

$$
\boxed{
\mathcal E_L=2Z_L
=
\frac{10(D-m)}{D(m-1)}
+
\frac{20\ell_L}{M},
}
$$

which is exactly `LineExcess`.

Using \(\ell_L\le2\),

$$
\mathcal E_L
<
\frac{10}{m-1}
+
\frac{40}{m(m-1)}
<
\frac{11}{m-1}
<
\frac1{960}.
$$

All factors and normalizations in the first bookkeeping version are correct.

---

# 2. Audit of the linewise sign balancing

For \(k\neq0\), the inverse Fourier transform is

$$
p_{L,k}
=
\mu+
\frac2D
\sum_{t\in H_L}
\varepsilon_t\sqrt{\zeta_L(t)}
\sin\frac{2\pi kt}{D},
\qquad
\mu=\frac{1-\rho}{D}.
$$

For fixed \(k\), the random summand indexed by \(t\) ranges over an interval of length at most

$$
\frac{4\sqrt{\zeta_L(t)}}{D}.
$$

Hence the sum of squared range lengths is bounded by

$$
\frac{16}{D^2}Z_L
=
\frac{8}{D^2}\mathcal E_L.
$$

The one-sided Hoeffding estimate is therefore

$$
\boxed{
\Pr\{p_{L,k}\le0\}
\le
\exp\left[
-\frac{(1-\rho)^2}{4\mathcal E_L}
\right].
}
\tag{2.1}
$$

Since

$$
\gamma<\frac1{D+1}<\frac14,
\qquad
\rho<\frac12,
$$

and \(\mathcal E_L<11/(m-1)\),

$$
\frac{(1-\rho)^2}{4\mathcal E_L}
>
\frac{m-1}{176}
>60.
$$

Thus

$$
\Pr\{\exists k\neq0:p_{L,k}\le0\}
<
De^{-60}.
$$

The exact frozen comparison

$$
2^{60}-D
=
211380275833782299>0
$$

and \(e>2\) give

$$
De^{-60}<D2^{-60}<1.
$$

So every line admits a strictly positive factor.

This confirms the first union bound.

---

# 3. Audit of the simultaneous all-line variant

From (1.1),

$$
Z_L
<
\frac{5m+20}{M}.
$$

Indeed,

$$
\frac{5(D-m)}{D(m-1)}<\frac5{m-1}=\frac{5m}{M},
\qquad
\frac{10\ell_L}{M}\le\frac{20}{M}.
$$

The exact comparison

$$
M-10000(5m+20)
=
235361008664553220>0
$$

gives

$$
\boxed{Z_L<\frac1{10000}.}
\tag{3.1}
$$

Working directly with \(Z_L\), the one-sided exponent is

$$
\frac{(1-\rho)^2}{8Z_L}
>
\frac{1}{32Z_L}
>
312.5.
$$

There are exactly

$$
(D+1)(D-1)=D^2-1
$$

nonzero line marginals. Since \(D<2^{60}\),

$$
D^2-1<2^{120}.
$$

Thus the global failure probability is bounded by

$$
(D^2-1)e^{-312.5}
<
2^{120}e^{-312.5}
<
e^{-192.5}<1.
$$

The stronger simultaneous bookkeeping is therefore correct.

## 3.1 Greedy derandomization

Order all line-sign variables. For one event \((L,k)\), write its fluctuating coefficients as \(a_{j,L,k}\), and put

$$
\tau_L
=
\frac{D(1-\rho)}{4Z_L}
=
\frac{D(1-\rho)}{2\mathcal E_L}.
$$

After fixing the first \(r\) signs, use the potential

$$
\begin{aligned}
\Phi_r
=
\sum_{L,k\neq0}
&
\exp\left[
-\tau_L\left(
\mu+
\sum_{j\le r}\varepsilon_ja_{j,L,k}
\right)
\right]\\
&\times
\prod_{j>r}
\cosh(\tau_La_{j,L,k}).
\end{aligned}
$$

The average of the two possible next values is the current value, so one sign choice does not increase \(\Phi_r\). The initial bound is strictly below one by the preceding exponential estimate. At the final stage, any nonpositive marginal would contribute at least one to the potential. Hence the greedy rule returns strictly positive factors.

The probabilistic and greedy versions are both valid finite existence proofs.

---

# 4. Complete stabilizer feasibility and nonphysicality

Because distinct projective lines share only the zero label, the line factors assemble into a single Hermitian coefficient field with magnitudes \(x^{(10)}\) and

$$
p_{L,k}>0
\quad\text{for every }L,k.
$$

Thus:

$$
\boxed{
\text{the named line and the all-line spectral-factor gates are closed.}
}
$$

Independent line-character shifts

$$
\alpha_{tv_L}
\longmapsto
\alpha_{tv_L}\omega^{\kappa_Lt}
$$

cyclically permute each positive line marginal and preserve its positivity.

The same-line cubic is

$$
C_{\rm dep}
=
\sum_L\sum_kp_{L,k}^3-\frac1D.
$$

Because

$$
\sum_L\sum_kp_{L,k}^2=2
$$

and each line purity is smaller than \(3/D\),

$$
C_{\rm dep}
<
2\sqrt{\frac3D}-\frac1D.
$$

At the exact frozen \(D\),

$$
2\sqrt{\frac3D}-\frac1D
=
3.5700224891701977\ldots\times10^{-9}.
$$

Every linearly independent cubic term uses three distinct lines. Averaging independent line-character shifts annihilates each such term. Therefore some shift choice satisfies

$$
\boxed{
C(\alpha)
\le C_{\rm dep}
<
3.571\times10^{-9}<1.
}
\tag{4.1}
$$

This verifies `StabilizerNotPhysical` unconditionally.

It proves insufficiency of the complete stabilizer layer, not impossibility of a different phase choice with \(C=1\).

---

# 5. Six-permutation identity

Let

$$
u+v+w=0
$$

with \(u,v,w\) nonzero and on three distinct lines. Put

$$
\zeta=\omega^{2^{-1}[u,v]},
$$

where \(2^{-1}\) is the field inverse of \(2\). No replacement by an ordinary half-angle representative is being made.

The six ordered pairs give:

$$
\begin{array}{c|c}
\text{ordered pair} & \text{Weyl phase}\\ \hline
(u,v)&\zeta\\
(v,u)&\overline\zeta\\
(u,w)&\overline\zeta\\
(w,u)&\zeta\\
(v,w)&\zeta\\
(w,v)&\overline\zeta.
\end{array}
$$

Therefore

$$
\boxed{
\sum_{\text{six orders}}
\omega^{2^{-1}[\cdot,\cdot]}
=
3(\zeta+\overline\zeta)
=
6\operatorname{Re}\zeta.
}
\tag{SixPerm}
$$

The proposed factor is correct.

---

# 6. Character indexing under line shifts

Choose a generator \(v_L\) for each projective line. Every nonzero label has a unique form

$$
z=t_zv_{L_z},
\qquad
t_z\in\mathbb F_D^\times.
$$

For an unordered zero-sum triple

$$
T=\{u,v,w\},
$$

define its character of the line-shift group by

$$
\chi_T(\kappa)
=
\omega^{
\kappa_{L_u}t_u+
\kappa_{L_v}t_v+
\kappa_{L_w}t_w
}.
$$

Distinct unordered triples give distinct characters:

* the support of the character identifies the three lines;
* its three nonzero coefficients identify \(u,v,w\) on those lines.

Moreover, \(T\) and \(-T\) give inverse, distinct characters. They cannot coincide because \(D\) is odd and a nonzero three-element triple cannot equal its negative without containing zero.

Let \(\mathcal T\) contain all unordered nonzero zero-sum triples on three distinct lines, with \(T\) and \(-T\) both retained. For any ordering of \(T\), set

$$
r_T=\operatorname{Re}\omega^{2^{-1}[u,v]}.
$$

This is independent of the ordering up to conjugation, hence has the same real value.

The linearly independent cubic is exactly

$$
\boxed{
C_{\rm ind}(\kappa)
=
\frac6{D^2}
\sum_{T\in\mathcal T}
r_T\,
\alpha_u\alpha_v\alpha_w\,
\chi_T(\kappa).
}
\tag{6.1}
$$

---

# 7. Exact shift Parseval identities

Character orthogonality gives

$$
\begin{aligned}
\mathbb E_\kappa|C_{\rm ind}(\kappa)|^2
&=
\frac{36}{D^4}
\sum_{T\in\mathcal T}
r_T^2
|\alpha_u|^2|\alpha_v|^2|\alpha_w|^2\\
&=
\boxed{
\frac{36}{D^4}
\sum_T
\left(\operatorname{Re}
\omega^{2^{-1}[u,v]}\right)^2
x_u^{(10)}x_v^{(10)}x_w^{(10)}.
}
\end{aligned}
\tag{ShiftParseval-T}
$$

Each unordered triple contributes exactly six ordered independent pairs. Therefore

$$
\sum_{\substack{u,v\\\text{linearly independent}}}
r_{u,v}^2x_ux_vx_{-u-v}
=
6\sum_{T\in\mathcal T}r_T^2x_ux_vx_w.
$$

Consequently,

$$
\boxed{
\mathbb E_\kappa|C_{\rm ind}(\kappa)|^2
=
\frac6{D^4}
\sum_{\substack{u,v\\\text{linearly independent}}}
\left(\operatorname{Re}
\omega^{2^{-1}[u,v]}\right)^2
x_u^{(10)}x_v^{(10)}x_{-u-v}^{(10)}.
}
\tag{ShiftParseval-ord}
$$

Both proposed formulas, including the factors \(36\) and \(6\), are correct.

---

# 8. Exact RMS bound from \(x^{(10)}\)

Because \(x^{(10)}\) is self-Fourier,

$$
x_k
=
\frac1D\sum_zx_z\omega^{[k,z]}.
$$

It follows that

$$
\boxed{
\sum_{u,v}
x_ux_vx_{-u-v}
=
D\sum_zx_z^3.
}
\tag{8.1}
$$

Indeed, substitute the self-Fourier formula for \(x_{-u-v}\) and perform the two character sums.

Dropping the independent-pair restriction and using \(r_T^2\le1\),

$$
\mathbb E_\kappa|C_{\rm ind}|^2
\le
\frac6{D^4}
\sum_{u,v}x_ux_vx_{-u-v}
=
\frac6{D^3}\sum_zx_z^3.
$$

Now

$$
x_0=1,\qquad
0<x_z<U\quad(z\neq0),
\qquad
\sum_{z\neq0}x_z=D-1.
$$

Therefore

$$
\sum_zx_z^3
\le
1+U^2(D-1).
$$

Hence the exact bound is

$$
\boxed{
\mathbb E_\kappa|C_{\rm ind}|^2
\le
\frac6{D^3}
\left[1+(D-1)U^2\right].
}
\tag{8.2}
$$

Using the audited inequality

$$
U<\frac1{135873434^2}
$$

and the exact integer comparison

$$
135873434^4-10^{14}D
=
246676184922887428794697973950736>0,
$$

one obtains

$$
(D-1)U^2<10^{-14}.
$$

Thus

$$
\boxed{
\left(\mathbb E_\kappa|C_{\rm ind}|^2\right)^{1/2}
<
\frac{\sqrt{6(1+10^{-14})}}{D^{3/2}}
<
2.682\times10^{-27}.
}
\tag{8.3}
$$

This is an average/RMS statement. It is not a uniform phase bound.

In particular, some line shift satisfies

$$
|C_{\rm ind}(\kappa)|
<
2.682\times10^{-27},
$$

which sharpens the earlier existence of a shift with merely
\(C_{\rm ind}\le0\). It does not constrain the maximum.

---

# 9. Why the RMS cannot be uniformized by degree alone

Define on \(\mathbb F_D\)

$$
h(s)=\mathbf1_{\{0\}}(s)-\frac1D
=
\frac1D\sum_{t\neq0}\omega^{ts}.
$$

On three line-shift coordinates put

$$
F(\kappa_1,\kappa_2,\kappa_3)
=
\frac{
h(\kappa_1)h(\kappa_2)h(\kappa_3)
}{
(1-1/D)^3
}.
$$

Then:

* \(F(0,0,0)=1\);
* \(F\) has mean zero;
* every Fourier character uses a nonzero frequency on exactly three distinct coordinates;
* \(|F|\le1\);
* and

  $$
  \boxed{
  \mathbb E|F|^2=\frac1{(D-1)^3}.
  }
  $$

Thus a degree-three line-character polynomial can have supremum \(1\) while its RMS is of order \(D^{-3/2}\), exactly the scale in (8.3).

This is not a frozen cubic and not a physical counterexample. It proves that ShiftParseval plus degree-three support cannot, without further coefficient-specific structure, yield a uniform bound.

---

# 10. First and second variations on the line-shift torus

Choose one representative from each pair \(\{T,-T\}\). Write

$$
A_T
=
\frac6{D^2}
\left(\operatorname{Re}
\omega^{2^{-1}[u,v]}\right)
\alpha_u\alpha_v\alpha_w.
$$

Choose balanced integer representatives of the three field coefficients \(t_u,t_v,t_w\), and let \(q_T\) be the corresponding vector in the real line-coordinate space. A continuous fixed-magnitude line-phase variation has

$$
C_{\rm ind}(\theta)
=
2\sum_T
\operatorname{Re}
\left(
A_Te^{i\langle q_T,\theta\rangle}
\right).
$$

If \(C=1\), then the coefficient field is physical and gives a global maximum of \(C\) on the entire phase torus. Hence

$$
\boxed{
\sum_Tq_T\,\operatorname{Im}A_T=0,
}
\tag{10.1}
$$

and

$$
\boxed{
\sum_T
(\operatorname{Re}A_T)\,
q_Tq_T^{\mathsf T}
\succeq0.
}
\tag{10.2}
$$

These are the exact stationarity and Hessian conditions.

They are not phase-free: the signs of \(\operatorname{Re}A_T\) and
\(\operatorname{Im}A_T\) are not determined by \(x^{(10)}\). The model in Section 9 has a unit spike, the same \(D^{-3/2}\) RMS scale, vanishing gradient, and a negative-semidefinite Hessian at its maximum. Therefore neither the RMS nor the abstract Hessian sign yields a bounded principal-minor contradiction for the frozen data.

No phase-uniform cubic gap follows from this route.

---

# 11. A stronger exact cross-line sum-of-squares layer

Let

$$
H_\alpha:=R_\alpha^2-R_\alpha.
$$

For every stabilizer projector \(P_{L,k}\), define

$$
\boxed{
\delta_{L,k}
=
\operatorname{Tr}(P_{L,k}H_\alpha).
}
\tag{11.1}
$$

The complete set of stabilizer projectors satisfies the exact two-design identity

$$
\boxed{
\sum_{L,k}
P_{L,k}\otimes P_{L,k}
=
I+F,
}
\tag{11.2}
$$

where \(F\) is swap.

To verify it, expand

$$
P_{L,k}
=
\frac1D\sum_t\omega^{kt}W_{tv}.
$$

Summing over \(k\) forces the two line parameters to add to zero. Summing over all \(D+1\) lines counts every nonzero Weyl label exactly once and the zero label \(D+1\) times. Using

$$
F=\frac1D\sum_zW_z\otimes W_z^*
$$

gives (11.2).

Since

$$
\operatorname{Tr}H_\alpha
=
\operatorname{Tr}R_\alpha^2-\operatorname{Tr}R_\alpha
=0,
$$

equation (11.2) yields

$$
\begin{aligned}
\sum_{L,k}\delta_{L,k}^2
&=
\operatorname{Tr}
\left[
(H_\alpha\otimes H_\alpha)(I+F)
\right]\\
&=
(\operatorname{Tr}H_\alpha)^2
+
\operatorname{Tr}H_\alpha^2.
\end{aligned}
$$

Therefore

$$
\boxed{
\sum_{L,k}\delta_{L,k}^2
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
}
\tag{11.3}
$$

This is an exact structured global SOS certificate with \(D(D+1)\) scalar residuals.

Moreover,

$$
\delta_{L,k}
=
\frac1D
\sum_t
\bigl(Q_{tv}-\alpha_{tv}\bigr)\omega^{-kt},
$$

where

$$
Q_z
=
\frac1D
\sum_u
\alpha_u\alpha_{z-u}\omega^{[u,z]/2}
$$

is the twisted-convolution coefficient of \(R_\alpha^2\). Thus the line residuals are precisely the linewise Fourier transforms of the global idempotence residual.

Because the stabilizer projectors span \(M_D\),

$$
\boxed{
\delta_{L,k}=0\ \forall L,k
\iff
R_\alpha^2=R_\alpha.
}
\tag{11.4}
$$

Under the standing Hermiticity and trace-one assumptions, this is equivalent to a rank-one physical state.

---

# 12. Cross-basis \(2\times2\) Cauchy constraints

Let

$$
P=|\phi\rangle\langle\phi|,
\qquad
Q=|\chi\rangle\langle\chi|
$$

be stabilizer projectors from two distinct stabilizer bases. Positivity of \(R_\alpha\) implies

$$
\boxed{
\operatorname{Tr}(PR_\alpha QR_\alpha)
\le
\operatorname{Tr}(PR_\alpha)\,
\operatorname{Tr}(QR_\alpha).
}
\tag{12.1}
$$

This is simply

$$
|\langle\phi|R_\alpha|\chi\rangle|^2
\le
\langle\phi|R_\alpha|\phi\rangle
\langle\chi|R_\alpha|\chi\rangle.
$$

It is the positivity of a \(2\times2\) \(R_\alpha\)-Gram matrix.

Choose any fixed-point-free partner map \(L\mapsto\tau(L)\) on the \(D+1\) stabilizer bases. Suppose:

1. every stabilizer marginal is nonnegative; and
2. (12.1) holds for every \(P_{L,k}\) and every
   \(P_{\tau(L),j}\).

For fixed \(L,k\), summing (12.1) over \(j\) gives

$$
\operatorname{Tr}(P_{L,k}R_\alpha^2)
\le
\operatorname{Tr}(P_{L,k}R_\alpha).
$$

Hence

$$
\delta_{L,k}\le0.
$$

But for each \(L\),

$$
\sum_k\delta_{L,k}
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)=0.
$$

Therefore every \(\delta_{L,k}=0\), and (11.4) gives a rank-one projector.

Conversely, a physical rank-one projector makes every inequality in (12.1) an equality.

Thus:

$$
\boxed{
\begin{aligned}
&\text{stabilizer positivity plus the designated cross-basis}\\
&2\times2\text{ Cauchy inequalities}\\
&\iff
\text{physical pure-state lifting}.
\end{aligned}
}
\tag{12.2}
$$

This uses local \(2\times2\) constraints but has global indexing cost

$$
\boxed{
(D+1)D^2
=
834676191481542500102529837710713256761115423061571062
}
$$

quadratic inequalities. It is still substantially smaller than imposing positivity of the full \(D^2\times D^2\) orbit matrix entry by entry.

---

# 13. Quantitative detection of the known nonphysical field

For any Hermitian trace-one, purity-one \(R_\alpha\),

$$
1-C(\alpha)
\le
\sqrt{
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2
}.
$$

Therefore the stabilizer-positive field from Section 4, with

$$
C(\alpha)\le
c_0:=
2\sqrt{\frac3D}-\frac1D,
$$

satisfies

$$
\sum_{L,k}\delta_{L,k}^2
\ge
(1-c_0)^2.
\tag{13.1}
$$

Choose a line with

$$
\sum_k\delta_{L,k}^2
\ge
\frac{(1-c_0)^2}{D+1}.
$$

For \(D\) real numbers of sum zero, if their largest positive entry is \(p\), then

$$
\sum_k\delta_k^2\le D(D-1)p^2.
$$

Hence some \(k\) obeys

$$
\delta_{L,k}
\ge
\frac{1-c_0}
{\sqrt{D(D^2-1)}}.
\tag{13.2}
$$

Now fix the designated partner basis \(\tau(L)\), and define

$$
e_j
=
\operatorname{Tr}
\left(
P_{L,k}R_\alpha
P_{\tau(L),j}R_\alpha
\right)
-
p_{L,k}p_{\tau(L),j}.
$$

Summing over \(j\) gives

$$
\sum_je_j=\delta_{L,k}.
$$

Thus at least one \(j\) satisfies

$$
\boxed{
e_j
\ge
\frac{1-c_0}
{D\sqrt{D(D^2-1)}}.
}
\tag{13.3}
$$

Numerically, the right side is larger than

$$
1.1625\times10^{-45}.
$$

So the already constructed stabilizer-positive field necessarily violates a concrete cross-line \(2\times2\) Cauchy inequality by a strictly positive amount.

This is the first exact cross-line SOS layer that detects what all linewise tests miss.

It does not prove that every phase assignment with magnitudes \(x^{(10)}\) violates such an inequality.

---

# 14. Remaining physical-lift gate

For the fixed magnitude profile \(x^{(10)}\), physical lifting is now equivalently the feasibility of either of the following structured systems:

$$
\delta_{L,k}=0
\quad
\text{for all }D(D+1)\text{ stabilizer projectors},
$$

or, after stabilizer positivity,

$$
\operatorname{Tr}(P_{L,k}R_\alpha
P_{\tau(L),j}R_\alpha)
\le
p_{L,k}p_{\tau(L),j}
$$

for the designated \(D^2(D+1)\) cross-basis pairs.

No compatible phase assignment satisfying these conditions is constructed.

No phase-uniform positive lower bound on the SOS in (11.3) is proved for all compatible phase fields of \(x^{(10)}\).

Therefore:

* the line-shift RMS is far too small to be useful as a uniform bound;
* the Hessian conditions remain phase-dependent;
* the new cross-line SOS system is exact and strictly stronger than the complete stabilizer layer;
* but its feasibility for \(x^{(10)}\) remains open.

A physical lift of \(x^{(10)}\) would disprove PW10 because its frozen objective is strictly larger than \(10\). Excluding this one magnitude profile would still not prove PW10 for every pure state.

---

# VERIFIED

* `LineExcess`, including every factor of \(2\).
* The quadrature factor construction.
* The per-line sign-balancing exponent.
* The stronger all-line bookkeeping:

  $$
  \sum_{t\in H_L}\zeta_L(t)
  <
  \frac{5m+20}{M}
  <
  \frac1{10000}.
  $$
* The simultaneous union bound over all \(D^2-1\) nonzero marginals.
* The greedy conditional-expectation derandomization.
* Strictly positive factors for the named line and every frozen line.
* Feasibility of all \(D(D+1)\) stabilizer inequalities.
* `StabilizerNotPhysical`.
* `SixPerm`.
* `ShiftParseval-T`.
* `ShiftParseval-ord`.
* Distinctness of the line-shift characters attached to distinct unordered triples.
* The exact RMS upper bound

  $$
  \mathbb E|C_{\rm ind}|^2
  \le
  \frac6{D^3}[1+(D-1)U^2].
  $$
* The numerical enclosure

  $$
  \operatorname{RMS}(C_{\rm ind})
  <2.682\times10^{-27}.
  $$
* The exact degree-three spike showing that this RMS scale does not control the supremum.
* The line-shift first- and second-variation formulas.
* The stabilizer two-design identity.
* The global residual SOS

  $$
  \sum_{L,k}\delta_{L,k}^2
  =
  \operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
  $$
* The cross-basis \(2\times2\) Cauchy characterization.
* The quantitative cross-line violation for the known stabilizer-positive nonphysical field.

# CORRECTED

* The line-shift RMS is much smaller than the previous same-line cubic scale, but it is only an average and cannot be promoted to a uniform cubic bound.
* The complete stabilizer layer is no longer a bottleneck.
* The first unresolved obstruction is not a one-dimensional factor problem; it is the simultaneous vanishing of cross-line idempotence residuals.
* A bounded local matrix size does not make the global cross-line system small: the exact \(2\times2\) characterization still contains \(D^2(D+1)\) indexed inequalities.

# DISPROVED

* Any claim that the line-factor problem remains open.
* Any claim that the complete stabilizer layer might itself enforce physicality.
* Any inference from the tiny line-shift RMS to a phase-uniform bound.
* Sufficiency of line-shift stationarity or Hessian negativity without coefficient-specific phase information.

# NECESSARY-ONLY

* The line-shift stationarity equations.
* The line-shift Hessian semidefiniteness condition.
* Every individual cross-basis Cauchy inequality.
* Vanishing of every stabilizer residual \(\delta_{L,k}\).
* Positivity of all stabilizer marginals.

# SUFFICIENT-ONLY

* Stabilizer positivity together with all designated cross-basis Cauchy inequalities is sufficient for physical lifting; in fact, under the standing trace and purity hypotheses it is also necessary.
* Vanishing of all stabilizer residuals is sufficient for physical lifting; again it is also necessary.

# OPEN

* Whether \(x^{(10)}\) admits compatible phases with

  $$
  C(\alpha)=1.
  $$
* Whether all compatible phases for \(x^{(10)}\) have a uniform positive residual

  $$
  \sum_{L,k}\delta_{L,k}^2\ge\eta>0.
  $$
* Whether the exact cross-basis \(2\times2\) system is feasible for
  \(x^{(10)}\).
* Whether another objective-above-\(10\) magnitude profile has a physical lift.
* PW10 for the frozen tuple.
* The finite \(r=2\) low-\(A\) gate.

The first new claim requiring independent verification is the exact cross-line equivalence:

$$
\boxed{
\text{stabilizer positivity}
+
\text{designated cross-basis }2\times2\text{ Cauchy inequalities}
\iff
R_\alpha\text{ is a rank-one projector},
}
$$

together with the quantitative violation bound in (13.3).

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-18-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-18-local-audit.md bytes=10821 sha256=8a4d154ef9bf8972f5aa87c5a4b5927f10c73521344be3c34ee7b4ca68238633 -->

# Round 18 local audit

- Audit completed (UTC): `2026-09-13T03:43:58Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-18-response.md`
- Web-response SHA-256:
  `b1fa58adab6a2b9007273febee95a33b57ec33629b339bf9817fde9bd0afe49d`
- Browser completion indicator: `Worked for 11m 53s`
- Capture equality: the browser response-copy payload, artifact, and output
  copy are text-identical; the two Markdown files are byte-identical, each
  `23,320` bytes, `23,320` Unicode characters, and `1,297` lines.

## Verdict

Round 18 makes one valid cross-line organizational advance, but it does not
settle the physical gate:

\[
\boxed{
\sum_{L,k}\delta_{L,k}^2
=\operatorname{Tr}(R_\alpha^2-R_\alpha)^2,
\qquad
\delta_{L,k}=\operatorname{Tr}
\left[P_{L,k}(R_\alpha^2-R_\alpha)\right].
}
\]

Together with the complete stabilizer MUB, these residuals vanish exactly
when the reconstructed operator is a rank-one projector.  A designated
family of cross-basis `2 x 2` Cauchy inequalities is likewise equivalent to
physicality under the standing Hermiticity, trace-one, and purity-one
hypotheses.  These identities are verified below.

One advertised component does not survive audit.  The response's continuous
"line-shift Hessian" differentiates only `C_ind`, but the same-line cubic
`C_dep` is invariant only under the **discrete** field-character shifts.  It
varies under the continuous balanced-representative deformation used in the
response.  Equations (10.1)--(10.2) are therefore not established necessary
conditions as written.

No compatible phases with `C(alpha)=1` are constructed, and no positive
phase-uniform residual gap is proved.  Consequently `x^(10)` physicality,
PW10, and the finite `r=2` low-`A` gate remain open.

## Line theorem and line-shift Parseval

The response correctly rechecks the Round 17 line theorem.  The exact
half-excess is

\[
Z_L=\sum_{t\in H_L}\zeta_L(t)
=\frac{5(D-m)}{D(m-1)}+\frac{10\ell_L}{M},
\]

so `E_L=2Z_L`, with all factors of two correct.  Both probabilistic bounds
are valid:

\[
\frac{(1-\rho)^2}{4\mathcal E_L}
>\frac{m-1}{176}>60
\]

for one line, and

\[
Z_L<\frac{5m+20}{M}<\frac1{10000},
\qquad
\frac{(1-\rho)^2}{8Z_L}>312.5
\]

for a simultaneous union bound over
`(D+1)(D-1)=D^2-1<2^120` nonzero marginals.  The conditional-expectation
potential is the corresponding finite greedy derandomization.  Thus the
named line, all line factors, and complete stabilizer feasibility remain
closed and verified.

For every independent zero-sum triple on three distinct projective lines,
the six Weyl phases are three copies of `zeta` and three of its conjugate.
Distinct unordered triples give distinct product-shift characters; `T` and
`-T` are inverse distinct characters because `D` is odd.  Therefore both
Parseval formulas are correct:

\[
\mathbb E_\kappa|C_{\rm ind}(\kappa)|^2
=\frac{36}{D^4}\sum_T r_T^2x_ux_vx_w
\]

and

\[
\mathbb E_\kappa|C_{\rm ind}(\kappa)|^2
=\frac6{D^4}\sum_{u,v\ \mathrm{independent}}
r_{u,v}^2x_ux_vx_{-u-v}.
\]

The independent checker explicitly verifies the sixfold multiplicity and
character injectivity for `p=3,5`, and enumerates the full line-shift second
moment for `p=3`.

## Sharpened frozen RMS bound

Self-Fourier symmetry gives the exact convolution identity

\[
\sum_{u,v}x_ux_vx_{-u-v}=D\sum_zx_z^3.
\]

For the exact nonzero cap

\[
U=\frac{11}{D+1}+\frac{10}{M},
\]

the already audited integer comparison gives

\[
U<\frac1{135873434^2},
\qquad
(D-1)U^2<10^{-14}.
\]

Thus

\[
\boxed{
\mathbb E_\kappa|C_{\rm ind}|^2
\le\frac6{D^3}\left[1+(D-1)U^2\right],
\qquad
\operatorname{RMS}(C_{\rm ind})<2.682\times10^{-27}.
}
\]

This is a correct average statement and not a uniform upper bound.  The
response's three-coordinate example

\[
F(\kappa_1,\kappa_2,\kappa_3)
=\frac{h(\kappa_1)h(\kappa_2)h(\kappa_3)}{(1-1/D)^3},
\qquad
h(s)=\mathbf1_{\{0\}}(s)-1/D,
\]

has supremum one but squared `L2` norm `1/(D-1)^3`.  It correctly proves
that support on three line coordinates plus a `D^(-3/2)` RMS scale alone
cannot control the supremum.  It is not itself the frozen cubic or a physical
counterexample.

## Verified MUB residual SOS

For the complete set of `D(D+1)` stabilizer projectors,

\[
\sum_{L,k}P_{L,k}\otimes P_{L,k}=I+F.
\]

Pairing this identity with
`H tensor H`, where `H=R_alpha^2-R_alpha` and `Tr H=0`, proves

\[
\sum_{L,k}\delta_{L,k}^2=\operatorname{Tr}H^2.
\]

The stabilizer projectors span all Hermitian matrices because Fourier
inversion within each basis recovers the Weyl labels on that line and the
projective lines partition the nonzero labels.  Hence all residuals vanish
if and only if `H=0`, equivalently `R_alpha` is a rank-one projector.

This is a valid structured SOS with `D(D+1)` scalar residuals.  It is also a
repackaging of the full global idempotence condition, not a phase-free
certificate that excludes the frozen magnitude profile.

## Verified cross-basis characterization

For rank-one projectors `P,Q`, positivity of `R` implies

\[
\operatorname{Tr}(PRQR)
=|\langle\phi|R|\chi\rangle|^2
\le\operatorname{Tr}(PR)\operatorname{Tr}(QR).
\]

Choose one distinct partner basis `tau(L)` for every stabilizer basis.  If
the inequality holds for all `P_(L,k),P_(tau(L),j)`, summing over `j` gives
`delta_(L,k)<=0`.  The `D` residuals on each line sum to zero, so all vanish;
the spanning argument then gives `R^2=R`.  Conversely a rank-one projector
makes every inequality an equality.  The equivalence is correct under the
standing assumptions.  The indexed system contains exactly

\[
D^2(D+1)
=834676191481542500102529837710713256761115423061571062
\]

inequalities.  Stabilizer positivity is physically necessary but is not
actually used in this sufficiency implication.

## Verified quantitative detection of the known field

For eigenvalues `mu_j` of a Hermitian trace-one, purity-one `R`,

\[
1-C
=\sum_j\mu_j^2(1-\mu_j)
\le\sqrt{\sum_j\mu_j^2}
\sqrt{\sum_j\mu_j^2(1-\mu_j)^2}
=\sqrt{\operatorname{Tr}(R^2-R)^2}.
\]

Combining this with the known field's

\[
C\le c_0=2\sqrt{3/D}-1/D
\]

proves total residual mass at least `(1-c_0)^2`.  The response's zero-sum
residual argument and averaging over a partner basis then yield an
existential cross-basis violation of at least

\[
\frac{1-c_0}{D\sqrt{D(D^2-1)}}
>1.1625\times10^{-45}.
\]

The direction, powers of `D`, exact indexed count, and decimal enclosure all
check.  This detects the already known nonphysical phase field; it does not
detect every phase assignment with the same magnitudes.

## Rejected continuous Hessian step

The line shifts preserving `C_dep` are the finite transformations

\[
\alpha_{tv_L}\mapsto\alpha_{tv_L}\omega^{\kappa_Lt},
\qquad \kappa_L\in\mathbb F_D.
\]

The response differentiates instead through

\[
\alpha_{tv_L}\mapsto\alpha_{tv_L}e^{i\bar t\theta_L}
\]

using balanced integer representatives.  That continuous path preserves
magnitudes and Hermiticity, but not the dependent cubic.  Set
`t=(D-1)/2`.  The same-line zero-sum triple with coordinates `t,t,1` has
balanced integer sum `D`, so its monomial acquires `e^(iD theta_L)` rather
than remaining fixed.  Its inverse triple supplies the conjugate term.  For
all-positive compatible phases the frequency-`D` coefficient is strictly
positive, making the variation explicit.

Consequently a maximum of total `C=C_dep+C_ind` does not imply the response's
stationarity or Hessian condition for `C_ind` alone.  The valid discrete
replacement, if the unshifted field is physical, is

\[
C_{\rm ind}(\kappa)\le C_{\rm ind}(0)
\quad\text{for every discrete line shift }\kappa.
\]

This yields finite-difference constraints, not the claimed continuous
Hessian.

## Verification receipts

- `work/verify_round18_web_response.py` checks the captured response hash,
  frozen rational and integer bounds, RMS enclosure, MUB two-design and SOS
  normalizations at `p=3`, the rank-one cross-basis equalities, the defect
  inequality, the quantitative violation, and a small-prime counterexample
  to continuous invariance of the same-line cubic.  Result: `PASS (with
  Hessian flaw detected)`.
- Web-response checker SHA-256:
  `685604d170436a6739e347a13bb91caf421bcb498b68ef83226ad901fa2943da`
- `work/verify_round18_line_shift_parseval.py` independently checks the
  six-permutation and Parseval convention, explicit character injectivity at
  `p=3,5`, the normalized self-Fourier convolution factor, and frozen caps.
  Result: `PASS`.
- Parseval checker SHA-256:
  `b69a40003e886b1adc3c231c30b296421a9ba3f92377b3b7e4133312e34ec110`
- Independent Parseval derivation:
  `work/round-18-independent-line-shift-parseval.md`
- Parseval derivation SHA-256:
  `5eb04e96f15fdf421d44ad74a8683db0259b02dfdbabe296da5b76ed8272fa5c`
- Independent cross-line audit:
  `work/round-18-independent-cross-line-sos-audit.md`
- Independent cross-line audit SHA-256:
  `0519ef16fea441fc65e9c2c3f5c04083578635e30f7fa4cbc4b8af6a6a539920`

Both Python files pass `py_compile`.

## Corrected status ledger

### VERIFIED

- The Round 17 line-factor theorem, both union bounds, and greedy rule.
- Feasibility and insufficiency of the complete stabilizer layer.
- `SixPerm` and both `ShiftParseval` identities.
- The exact self-Fourier convolution identity and RMS bound below
  `2.682e-27`.
- The degree-three spike showing why RMS scale alone is not uniform.
- The complete-MUB two-design and residual SOS identities.
- The designated cross-basis `2 x 2` characterization under the standing
  hypotheses.
- The existential `1.1625e-45` violation bound for the already constructed
  nonphysical field.

### CORRECTED / REJECTED

- The response's continuous line-shift Hessian conditions are invalid as
  written because they omit the varying same-line cubic.
- The exact replacement currently available is a family of discrete
  maximum/finite-difference inequalities.
- The residual SOS and cross-basis system characterize the full physicality
  gate but do not provide a phase-free lower bound for `x^(10)`.

### DISPROVED

- Any inference from the tiny shift RMS to a uniform cubic gap.
- Sufficiency of linewise/stabilizer positivity for physicality.
- Validity of the response's `C_ind`-only continuous Hessian argument as a
  necessary condition.

### OPEN

- Whether `x^(10)` admits compatible phases with `C(alpha)=1`.
- Whether all compatible phases for `x^(10)` have a uniform positive MUB
  residual SOS.
- Whether the exact cross-basis system is feasible for `x^(10)`.
- Whether a different objective-above-10 magnitude profile has a physical
  lift.
- PW10 for the exact frozen tuple.
- The finite `r=2` low-`A` gate and all downstream conclusions.

Even excluding `x^(10)` would not prove PW10 for every physical magnitude
profile.  No quantifier promotion is made.

<!-- END HISTORICAL FILE path=outputs/round-18-local-audit.md -->


# ROUND 019

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-19-prompt.md bytes=8805 sha256=082a356943966895410f9978843f0ef08cd88785592e01d27e2f12efa27d0726 -->

# Round 19 — correct the false continuous Hessian and test the MUB residual system

Continue in the same ordinary Chat conversation and the same canonically
frozen finite `r=2`, low-`A` gate.  Give a public, self-contained derivation
and no hidden chain-of-thought.  Do not repeat the Round 8--17 narrative.

## Exact frozen boundary

Use exactly

\[
m=485165196,
\quad P=m+41=485165237,
\quad D=941541228773064677=4P^2+1,
\]

\[
M=m(m-1)=235385266924553220,
\quad
\Gamma=(A-A)\setminus\{0\},
\]

where

\[
A=\{(t_j,t_j^2):0\le j\le P-42\},
\quad
t_j=2Pj+(j^2\bmod P).
\]

The open physical gate is

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10
\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use

\[
W_{(p,q)}|y\rangle=\omega^{p(y+q/2)}|y+q\rangle,
\qquad
W_uW_v=\omega^{[u,v]/2}W_{u+v}.
\]

The exact magnitude pseudo-point remains

\[
b_0=1,
\quad b_z=(D+1)^{-1}\ (z\ne0),
\]

\[
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\quad
y=\mathbf1_\Gamma+\lambda/D,
\quad
x^{(10)}=b+(10/M)(y-(M/D)b).
\]

It is positive, even, self-Fourier, has mass `D`, passes every audited
magnitude, small-Gram, parity, and stabilizer condition, and has frozen
objective strictly above `10`.  A physical lift requires compatible phases
with

\[
R_\alpha=D^{-1}\sum_z\alpha_zW_z,
\qquad
C(\alpha)=\operatorname{Tr}R_\alpha^3=1.
\]

Excluding this one pseudo-point would not prove PW10; a physical lift would
disprove PW10.

## Independently verified Round 18 results

The all-line factor theorem is closed.  There is a compatible global field
with the exact magnitudes `x^(10)` and every stabilizer marginal strictly
positive.  Another choice of line-character shifts has

\[
C(\alpha)\le C_{\rm dep}
<2\sqrt{3/D}-1/D<3.571\times10^{-9}<1,
\]

so the complete stabilizer layer is unconditionally insufficient.

The six-permutation identity and both line-shift Parseval identities are
correct.  If `T` ranges over unordered independent zero-sum triples, with
`T` and `-T` distinct, then

\[
C_{\rm ind}(\kappa)
=\frac6{D^2}\sum_T
r_T\alpha_u\alpha_v\alpha_w\chi_T(\kappa),
\qquad
r_T=\operatorname{Re}\omega^{2^{-1}[u,v]},
\]

and

\[
\mathbb E_\kappa|C_{\rm ind}|^2
=\frac6{D^4}
\sum_{u,v\ \mathrm{independent}}
r_{u,v}^2x_ux_vx_{-u-v}.
\]

Self-Fourier symmetry gives

\[
\sum_{u,v}x_ux_vx_{-u-v}=D\sum_zx_z^3.
\]

With

\[
U=\frac{11}{D+1}+\frac{10}{M}
<\frac1{135873434^2},
\]

the exact frozen bound is

\[
\boxed{
\mathbb E_\kappa|C_{\rm ind}|^2
\le\frac6{D^3}[1+(D-1)U^2],
\qquad
\operatorname{RMS}(C_{\rm ind})<2.682\times10^{-27}.
}
\tag{ShiftRMS}
\]

This is average-only.  The exact three-coordinate spike from Round 18 has
supremum one and squared RMS `1/(D-1)^3`, so degree-three support and RMS
scale alone cannot yield a uniform gap.

## Mandatory correction to Round 18 Section 10

Round 18's continuous `C_ind`-only Hessian is not valid as written.  The
exact line shifts

\[
\alpha_{tv_L}\mapsto\alpha_{tv_L}\omega^{\kappa_Lt},
\qquad \kappa_L\in\mathbb F_D,
\tag{DiscreteShift}
\]

preserve `C_dep`, but they form a finite group.  Replacing them by balanced
integer phases

\[
\alpha_{tv_L}\mapsto\alpha_{tv_L}e^{i\bar t\theta_L}
\tag{ContinuousLift}
\]

does not preserve the same-line cubic.  Take

\[
t=(D-1)/2.
\]

The dependent zero-sum triple on any line with coordinates `t,t,1` has
balanced integer sum `D`; under `(ContinuousLift)` its monomial acquires
`e^(iD theta_L)`.  Its inverse triple acquires the conjugate factor.  Thus
the derivatives of `C_dep` cannot be omitted.

Audit this objection first.  Explicitly retract or repair the prior
equations (10.1)--(10.2); do not retain them merely because their formal
signs looked plausible.

The valid discrete consequence of a physical unshifted field is only

\[
\boxed{
C_{\rm ind}(\kappa)\le C_{\rm ind}(0)
\quad\forall\kappa\in\mathbb F_D^{D+1},
}
\tag{DiscreteMaximum}
\]

because `C_dep` is discretely invariant and every shifted Hermitian
trace-one, purity-one field obeys `C<=1`.  The `D^2`-element subgroup induced
by global Weyl characters leaves every zero-sum triple character invariant,
as it must for displaced copies of a physical state.

For comparison, a correct full fixed-magnitude phase variation
`alpha_z(s)=alpha_z exp(i s h_z)`, with `h_-z=-h_z`, has

\[
A=R'(0)=\frac{i}{D}\sum_zh_z\alpha_zW_z.
\]

At a physical lift `R=P` the fixed Hilbert--Schmidt norm implies

\[
\boxed{
C''(0)=6\operatorname{Tr}(PA^2)-3\operatorname{Tr}(A^2).
}
\tag{FullHessian}
\]

If `A` is decomposed relative to `P` and `P^perp`, this should reduce to
`-3 Tr[(P^perp A P^perp)^2]`.  Audit or correct this formula and explain why
it is automatic at a true lift rather than a phase-free contradiction.

## New MUB residual system to audit

Put

\[
H_\alpha=R_\alpha^2-R_\alpha,
\qquad
\delta_{L,k}=\operatorname{Tr}(P_{L,k}H_\alpha).
\]

Round 18 proposed

\[
\sum_{L,k}P_{L,k}\otimes P_{L,k}=I+F,
\tag{MUB2}
\]

\[
\boxed{
\sum_{L,k}\delta_{L,k}^2
=\operatorname{Tr}(R_\alpha^2-R_\alpha)^2,
}
\tag{ResidualSOS}
\]

and, with

\[
Q_z=D^{-1}\sum_u\alpha_u\alpha_{z-u}\omega^{[u,z]/2},
\]

\[
\delta_{L,k}
=D^{-1}\sum_t(Q_{tv_L}-\alpha_{tv_L})\omega^{-kt}.
\tag{ResidualFourier}
\]

It also proposed the following equivalence.  Choose a distinct partner basis
`tau(L)` for every `L`.  Under the standing Hermiticity, trace-one, and
purity-one hypotheses, the inequalities

\[
\operatorname{Tr}(P_{L,k}R_\alpha P_{\tau(L),j}R_\alpha)
\le
\operatorname{Tr}(P_{L,k}R_\alpha)
\operatorname{Tr}(P_{\tau(L),j}R_\alpha)
\tag{Cross2x2}
\]

for all `L,k,j` are equivalent to a rank-one physical lift.  The system has
exactly

\[
D^2(D+1)
=834676191481542500102529837710713256761115423061571062
\]

inequalities.  For the already constructed nonphysical field, the proposed
violation lower bound is

\[
\frac{1-c_0}{D\sqrt{D(D^2-1)}}
>1.1625\times10^{-45},
\qquad
c_0=2\sqrt{3/D}-1/D.
\tag{KnownViolation}
\]

Audit every transpose, conjugation, normalization, inequality direction,
and quantifier in `(MUB2)`--`(KnownViolation)`.  State that this is an exact
repackaging of global idempotence unless you derive a phase-free frozen
consequence.

## Required new attack

After the correction and audits, do not stop at restating
`R^2=R`, `C=1`, or positivity of the full orbit matrix.  Obtain a
coefficient-specific cross-line statement for the frozen data.  Pursue these
in order:

1. Compute exactly the discrete line-shift average

   \[
   \mathbb E_\kappa
   \operatorname{Tr}(R_{\alpha,\kappa}^2-R_{\alpha,\kappa})^2
   =\mathbb E_\kappa\operatorname{Tr}R_{\alpha,\kappa}^4
   -2C_{\rm dep}+1.
   \tag{ShiftSOSMean}
   \]

   Classify all surviving four-label patterns.  Independent line shifts
   force each represented line's field coefficients to sum to zero, so the
   only nonzero-line multiplicity patterns should be `4` and `2+2`.  Prove or
   correct this.  Evaluate every `2+2` term exactly from the frozen
   magnitudes and isolate the genuinely phase-dependent same-line fourth
   moments.  Do not call a positive average a uniform gap.

2. Use `(DiscreteMaximum)` or the nonnegativity of the residual SOS on the
   quotient by the global-Weyl-character subgroup to derive an exact
   finite-difference or Fourier-coefficient constraint.  Test it on the
   actual coefficients `r_T sqrt(x_u x_v x_w)`, not only on an arbitrary
   degree-three polynomial.

3. Sum or weight `(Cross2x2)` so that phases cancel and obtain a necessary
   inequality depending only on `x^(10)` and the frozen difference data.
   Evaluate it exactly.  A family equivalent to full idempotence but still
   containing all unknown phases is not a new exclusion certificate.

4. If none of these yields a uniform positive residual for `x^(10)`, return
   to the direct product-state operator

   \[
   K_\Gamma=\sum_{g\in\Gamma}W_g\otimes\overline{W_g}
   \]

   and derive a genuinely stronger exact product-state/SOS inequality than
   the already passed magnitude, parity, small-Gram, and stabilizer layers.
   Either prove the bound `10` or exhibit an exact physical vector above
   `10`.  Solver labels, rounded numerics, or relaxation values are not
   certificates.

## Required verdict discipline

Give one verdict for PW10: **PROVED**, **DISPROVED**, or **OPEN WITH EARLIEST
GAP**.  End with a ledger separating **VERIFIED**, **CORRECTED**,
**DISPROVED**, **NECESSARY-ONLY**, **SUFFICIENT-ONLY**, and **OPEN**.  State
separately the status of:

- the Round 18 continuous Hessian;
- the correct full-phase Hessian and discrete maximum condition;
- `MUB2`, `ResidualSOS`, `Cross2x2`, and `KnownViolation`;
- the new line-shift SOS mean;
- the physical `C=1` lift of `x^(10)`;
- `x^(10)` as a candidate, PW10, and the finite `r=2` gate.

Identify the first genuinely new claim requiring independent verification.

<!-- END HISTORICAL FILE path=work/round-19-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-19-response.md bytes=23912 sha256=6fbf0af07648a42e68e8e66a7d25117f09eb54833a2b23bc38b43ad82c473046 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The mandatory correction is valid: the continuous Hessian written only for \(C_{\mathrm{ind}}\) in Round 18 must be retracted. Continuous real phase lifts do not preserve \(C_{\mathrm{dep}}\).

The correct full fixed-magnitude Hessian is

$$
\boxed{
C''(0)
=
6\operatorname{Tr}(PA^2)-3\operatorname{Tr}(A^2)
=
-3\operatorname{Tr}\!\left[(P^\perp A P^\perp)^2\right]\le0
}
$$

at a physical lift \(P\). This is automatic at a true rank-one projector and supplies no phase-free contradiction.

The MUB identities, residual sum of squares, Fourier residual formula, cross-basis \(2\times2\) equivalence, and the quantitative known violation are all correct. They are an exact structured repackaging of global idempotence, not yet a magnitude-only exclusion of \(x^{(10)}\).

The new exact result in this round is the complete line-shift fourth-moment decomposition. After averaging over independent discrete line shifts, every surviving ordered quadruple is either:

1. supported on one projective line, including cases with zero labels; or
2. of the form \(\{u,-u,v,-v\}\) on two distinct lines.

The entire two-line contribution is phase-free and can be evaluated explicitly from the frozen magnitudes. The remaining same-line fourth moments retain the unresolved line-phase data.

---

# 1. Retraction of the continuous \(C_{\mathrm{ind}}\)-only Hessian

For one line, let \(t=(D-1)/2\). In \(\mathbb F_D\),

$$
t+t+1=0.
$$

The dependent same-line cubic therefore contains a monomial with line coordinates

$$
(t,t,1).
$$

Under the discrete shift

$$
\alpha_{sv_L}\longmapsto
\alpha_{sv_L}\omega^{\kappa_Ls},
$$

its multiplier is

$$
\omega^{\kappa_L(2t+1)}
=
\omega^{\kappa_LD}=1.
$$

Thus \(C_{\mathrm{dep}}\) is invariant under the actual finite shift group.

Under the proposed continuous lift

$$
\alpha_{sv_L}\longmapsto
\alpha_{sv_L}e^{i\bar s\theta_L},
$$

where \(\bar s\) is a balanced integer representative, the same monomial acquires

$$
e^{i(2t+1)\theta_L}
=
e^{iD\theta_L}.
$$

Its inverse triple acquires \(e^{-iD\theta_L}\). Hence \(C_{\mathrm{dep}}\) generally has nonzero continuous derivatives.

Therefore the prior \(C_{\mathrm{ind}}\)-only stationarity and Hessian equations are invalid and are retracted.

The valid finite consequence is only

$$
\boxed{
C_{\mathrm{ind}}(\kappa)
\le
C_{\mathrm{ind}}(0)
\quad
\forall\kappa\in\mathbb F_D^{D+1},
}
\tag{1.1}
$$

provided the unshifted coefficient field is physical. Indeed, discrete shifts preserve \(C_{\mathrm{dep}}\), while every shifted Hermitian trace-one, purity-one field satisfies \(C\le1\).

The \(D^2\)-element subgroup induced by global Weyl characters acts trivially on every zero-sum cubic character, as required for displaced copies of the same physical state.

---

# 2. Correct full fixed-magnitude Hessian

Let

$$
\alpha_z(s)=\alpha_ze^{ish_z},
\qquad
h_{-z}=-h_z,
\qquad
h_0=0,
$$

and put

$$
R(s)=\frac1D\sum_z\alpha_z(s)W_z.
$$

Then \(R(s)\) is Hermitian and

$$
\operatorname{Tr}R(s)
=
\operatorname{Tr}R(s)^2=1
$$

for every \(s\). Define

$$
A=R'(0)
=
\frac{i}{D}\sum_zh_z\alpha_zW_z,
$$

and \(B=R''(0)\).

Suppose \(R(0)=P\) is a rank-one projector. Differentiating the fixed Hilbert–Schmidt norm gives

$$
\operatorname{Tr}(PA)=0,
\tag{2.1}
$$

and

$$
\operatorname{Tr}(A^2)+\operatorname{Tr}(PB)=0.
\tag{2.2}
$$

For

$$
C(s)=\operatorname{Tr}R(s)^3,
$$

one has

$$
C''(0)
=
6\operatorname{Tr}(PA^2)
+
3\operatorname{Tr}(PB).
$$

Using (2.2),

$$
\boxed{
C''(0)
=
6\operatorname{Tr}(PA^2)
-
3\operatorname{Tr}(A^2).
}
\tag{FullHessian}
$$

Decompose \(A\) relative to

$$
\operatorname{ran}P\oplus\operatorname{ran}P^\perp:
\qquad
A=
\begin{pmatrix}
0&b^*\\
b&A_\perp
\end{pmatrix}.
$$

The upper-left entry is zero by (2.1). Therefore

$$
\operatorname{Tr}(PA^2)=\|b\|^2,
$$

and

$$
\operatorname{Tr}(A^2)
=
2\|b\|^2+\operatorname{Tr}(A_\perp^2).
$$

Consequently,

$$
\boxed{
C''(0)
=
-3\operatorname{Tr}(A_\perp^2)
=
-3\operatorname{Tr}\!\left[
(P^\perp A P^\perp)^2
\right]
\le0.
}
\tag{2.3}
$$

This is automatic at every true physical lift. It is not a phase-free obstruction to such a lift.

---

# 3. Audit of the MUB two-design identity

For a projective isotropic line \(L=\langle v\rangle\),

$$
P_{L,k}
=
\frac1D\sum_{t\in\mathbb F_D}
\omega^{kt}W_{tv}.
$$

For a fixed line,

$$
\begin{aligned}
\sum_kP_{L,k}\otimes P_{L,k}
&=
\frac1{D^2}
\sum_{t,s}\sum_k
\omega^{k(t+s)}
W_{tv}\otimes W_{sv}\\
&=
\frac1D\sum_t
W_{tv}\otimes W_{-tv}.
\end{aligned}
$$

Summing over the \(D+1\) lines:

* the zero Weyl label is counted \(D+1\) times;
* every nonzero Weyl label is counted exactly once.

Thus

$$
\begin{aligned}
\sum_{L,k}P_{L,k}\otimes P_{L,k}
&=
\frac{D+1}{D}I\otimes I
+
\frac1D\sum_{z\ne0}W_z\otimes W_z^*\\
&=
I\otimes I+
\frac1D\sum_zW_z\otimes W_z^*.
\end{aligned}
$$

Using

$$
F=\frac1D\sum_zW_z\otimes W_z^*,
$$

one obtains

$$
\boxed{
\sum_{L,k}P_{L,k}\otimes P_{L,k}=I+F.
}
\tag{MUB2}
$$

All tensor orientations and normalizations are correct.

---

# 4. Residual sum of squares

Let

$$
H_\alpha=R_\alpha^2-R_\alpha,
$$

and

$$
\delta_{L,k}
=
\operatorname{Tr}(P_{L,k}H_\alpha).
$$

Because \(H_\alpha\) and \(P_{L,k}\) are Hermitian, every \(\delta_{L,k}\) is real. From MUB2,

$$
\begin{aligned}
\sum_{L,k}\delta_{L,k}^2
&=
\operatorname{Tr}
\left[
(H_\alpha\otimes H_\alpha)(I+F)
\right]\\
&=
(\operatorname{Tr}H_\alpha)^2
+
\operatorname{Tr}H_\alpha^2.
\end{aligned}
$$

Now

$$
\operatorname{Tr}H_\alpha
=
\operatorname{Tr}R_\alpha^2-\operatorname{Tr}R_\alpha
=0.
$$

Hence

$$
\boxed{
\sum_{L,k}\delta_{L,k}^2
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
}
\tag{ResidualSOS}
$$

This identity is exact.

---

# 5. Fourier form of the MUB residuals

Write

$$
R_\alpha^2
=
\frac1D\sum_zQ_zW_z,
$$

where Weyl multiplication gives

$$
\boxed{
Q_z=
\frac1D\sum_u
\alpha_u\alpha_{z-u}
\omega^{[u,z]/2}.
}
\tag{5.1}
$$

Thus

$$
H_\alpha
=
\frac1D\sum_z(Q_z-\alpha_z)W_z.
$$

Using

$$
P_{L,k}
=
\frac1D\sum_t\omega^{kt}W_{tv}
$$

and

$$
\operatorname{Tr}(W_{tv}W_z)
=
D\,\delta_{z,-tv},
$$

one obtains

$$
\begin{aligned}
\delta_{L,k}
&=
\frac1D
\sum_t
\omega^{kt}
(Q_{-tv}-\alpha_{-tv})\\
&=
\boxed{
\frac1D
\sum_t
(Q_{tv}-\alpha_{tv})\omega^{-kt}.
}
\end{aligned}
\tag{ResidualFourier}
$$

The sign and normalization are correct.

---

# 6. Cross-basis \(2\times2\) system

Let

$$
P=|\phi\rangle\langle\phi|,
\qquad
Q=|\chi\rangle\langle\chi|
$$

be projectors from distinct stabilizer bases. For Hermitian \(R_\alpha\),

$$
\operatorname{Tr}(PR_\alpha QR_\alpha)
=
|\langle\phi|R_\alpha|\chi\rangle|^2.
$$

If \(R_\alpha\succeq0\), Cauchy–Schwarz in the positive form induced by \(R_\alpha\) gives

$$
\boxed{
\operatorname{Tr}(PR_\alpha QR_\alpha)
\le
\operatorname{Tr}(PR_\alpha)
\operatorname{Tr}(QR_\alpha).
}
\tag{Cross2x2}
$$

Now choose, for each line \(L\), one distinct partner basis \(\tau(L)\). Assume:

1. every stabilizer marginal is nonnegative;
2. Cross2x2 holds for all

   $$
   P_{L,k},\quad P_{\tau(L),j}.
   $$

Fix \(L,k\) and sum over \(j\). Since

$$
\sum_jP_{\tau(L),j}=I,
$$

the left side becomes

$$
\operatorname{Tr}(P_{L,k}R_\alpha^2),
$$

while the right side becomes

$$
\operatorname{Tr}(P_{L,k}R_\alpha)
\operatorname{Tr}R_\alpha
=
\operatorname{Tr}(P_{L,k}R_\alpha).
$$

Therefore

$$
\delta_{L,k}\le0.
$$

For each \(L\),

$$
\sum_k\delta_{L,k}
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)=0.
$$

Hence every \(\delta_{L,k}=0\). MUB2 then gives

$$
H_\alpha=0.
$$

Thus \(R_\alpha^2=R_\alpha\), and the standing trace-one Hermiticity condition makes \(R_\alpha\) a rank-one projector.

Conversely, a rank-one projector makes every Cross2x2 inequality an equality.

Therefore, under the standing trace, purity, and Hermiticity assumptions,

$$
\boxed{
\begin{aligned}
&\text{stabilizer positivity plus all designated Cross2x2 inequalities}\\
&\quad\Longleftrightarrow\quad
R_\alpha\text{ is a rank-one physical projector}.
\end{aligned}
}
\tag{6.1}
$$

The number of inequalities is exactly

$$
\boxed{
D^2(D+1)
=
834676191481542500102529837710713256761115423061571062.
}
$$

This is an exact repackaging of global idempotence. It is not yet a phase-free frozen-data criterion.

## 6.1 The unweighted phase-cancelled sum is trivial

For a fixed pair of bases,

$$
\sum_{k,j}
\operatorname{Tr}
(P_{L,k}R_\alpha P_{\tau(L),j}R_\alpha)
=
\operatorname{Tr}R_\alpha^2=1,
$$

while

$$
\sum_{k,j}
p_{L,k}p_{\tau(L),j}
=
1.
$$

Thus summing all Cross2x2 inequalities without weights gives the identity \(1=1\). No nontrivial magnitude-only inequality results from that summation.

---

# 7. Audit of the quantitative known violation

For the already constructed stabilizer-positive nonphysical field,

$$
C(\alpha)\le
c_0:=
2\sqrt{\frac3D}-\frac1D.
$$

Since

$$
1-C(\alpha)
\le
\sqrt{\operatorname{Tr}(R_\alpha^2-R_\alpha)^2},
$$

ResidualSOS gives

$$
\sum_{L,k}\delta_{L,k}^2
\ge
(1-c_0)^2.
$$

Some line \(L\) therefore satisfies

$$
\sum_k\delta_{L,k}^2
\ge
\frac{(1-c_0)^2}{D+1}.
$$

Because \(\sum_k\delta_{L,k}=0\), let \(p\) be the largest positive \(\delta_{L,k}\). If the total positive mass is \(A\), then

$$
A\le(D-1)p.
$$

The positive squares sum to at most \(pA\), and the negative squares sum to at most \(A^2\). Hence

$$
\sum_k\delta_{L,k}^2
\le
D(D-1)p^2.
$$

Therefore some \(k\) has

$$
\delta_{L,k}
\ge
\frac{1-c_0}{\sqrt{D(D^2-1)}}.
$$

For its designated partner basis, define

$$
e_j=
\operatorname{Tr}
(P_{L,k}R_\alpha
P_{\tau(L),j}R_\alpha)
-
p_{L,k}p_{\tau(L),j}.
$$

Since

$$
\sum_je_j=\delta_{L,k},
$$

some \(j\) satisfies

$$
\boxed{
e_j
\ge
\frac{1-c_0}
{D\sqrt{D(D^2-1)}}.
}
\tag{7.1}
$$

At the exact frozen \(D\),

$$
\boxed{
\frac{1-c_0}
{D\sqrt{D(D^2-1)}}
=
1.16252324007657\ldots\times10^{-45}
>
1.1625\times10^{-45}.
}
$$

`KnownViolation` is correct.

---

# 8. Exact discrete line-shift fourth moment

Let \(\kappa=(\kappa_L)_L\) be independent and uniform in

$$
\mathbb F_D^{D+1},
$$

and let \(R_\kappa\) denote the shifted reconstructed operator.

The fourth moment is

$$
\operatorname{Tr}R_\kappa^4
=
\frac1{D^3}
\sum_{z_1+\cdots+z_4=0}
\left(\prod_{r=1}^4\alpha_{z_r}\right)
\omega^{\frac12\sum_{r<s}[z_r,z_s]}
\chi_\kappa(z_1,\ldots,z_4).
\tag{8.1}
$$

Averaging over \(\kappa\) forces, on every represented projective line, the sum of its scalar coordinates to vanish in \(\mathbb F_D\).

## 8.1 Correct classification of surviving patterns

The literal phrase “only multiplicity patterns \(4\) and \(2+2\)” needs qualification.

If zero labels are counted, one-line survivors may have two, three, or four nonzero labels. The correct classification is:

1. **one-line class:** every nonzero \(z_r\) lies on a single projective line; this includes configurations with zero labels;
2. **two-line class:** the four labels are

   $$
   \{u,-u,v,-v\}
   $$

   with \(u\) and \(v\) on distinct lines.

No other class survives:

* a line represented once has a nonzero scalar sum;
* with two distinct lines, the only allowed multiplicity is \(2+2\), and each pair must be inverse;
* three or four distinct nonzero lines necessarily contain a singleton line.

So the proposed \(4/2+2\) picture is correct only after interpreting “4” as “all labels supported on one line.”

---

# 9. Same-line fourth moments

For one line \(L=\langle v\rangle\), write

$$
p_{L,k}
=
\frac1D\sum_t\alpha_{tv}\omega^{-kt}.
$$

Then

$$
\sum_kp_{L,k}^4
=
\frac1{D^3}
\sum_{t_1+\cdots+t_4=0}
\alpha_{t_1v}\alpha_{t_2v}
\alpha_{t_3v}\alpha_{t_4v}.
$$

Summing this over all \(D+1\) lines counts every one-line survivor exactly once, except that the all-zero quadruple is counted \(D+1\) times. Its actual fourth-moment contribution is \(D^{-3}\), so the overcount is

$$
D\cdot D^{-3}=D^{-2}.
$$

Therefore the exact one-line contribution is

$$
\boxed{
T_{4,\mathrm{line}}
=
\sum_{L,k}p_{L,k}^4-\frac1{D^2}.
}
\tag{9.1}
$$

These are the genuinely phase-dependent same-line fourth moments.

---

# 10. Exact evaluation of every \(2+2\) term

Fix noncollinear nonzero \(u,v\). Consider the \(24\) orderings of

$$
u,-u,v,-v.
$$

In units of \([u,v]\), the total Weyl exponent

$$
\frac12\sum_{r<s}[z_r,z_s]
$$

takes the values

$$
0\quad\text{16 times},
$$

$$
+[u,v]\quad\text{4 times},
$$

and

$$
-[u,v]\quad\text{4 times}.
$$

Thus the total phase sum is

$$
16+4\omega^{[u,v]}+4\omega^{-[u,v]}
=
16+8\operatorname{Re}\omega^{[u,v]}.
\tag{10.1}
$$

Because

$$
\alpha_u\alpha_{-u}\alpha_v\alpha_{-v}
=
x_ux_v,
$$

the entire two-line contribution can be written as

$$
\boxed{
T_{22}
=
\frac1{D^3}
\sum_{\substack{u,v\ne0\\
u,v\text{ linearly independent}}}
\left(
2+\operatorname{Re}\omega^{[u,v]}
\right)x_ux_v.
}
\tag{10.2}
$$

The sum is over ordered independent pairs. The coefficient is correct because each unordered set
\(\{\pm u,\pm v\}\) corresponds to eight such ordered pairs.

In particular,

$$
T_{22}\ge0.
$$

---

# 11. Closed frozen formula for \(T_{22}\)

Let

$$
S_2=\sum_zx_z^2
$$

and

$$
s_L=\sum_{z\in L\setminus\{0\}}x_z.
$$

First,

$$
\sum_{\substack{u,v\ne0\\u,v\text{ independent}}}x_ux_v
=
(D-1)^2-\sum_Ls_L^2.
\tag{11.1}
$$

Next, self-Fourier symmetry gives

$$
\sum_vx_v\omega^{[u,v]}=Dx_u.
$$

Hence

$$
\sum_{u,v}x_ux_v\omega^{[u,v]}
=
D\sum_ux_u^2=DS_2.
$$

Removing all pairs with \(u=0\) or \(v=0\), whose total mass is \(2D-1\), and all nonzero collinear pairs, whose character equals \(1\), gives

$$
\sum_{\substack{u,v\ne0\\u,v\text{ independent}}}
x_ux_v\operatorname{Re}\omega^{[u,v]}
=
DS_2-(2D-1)-\sum_Ls_L^2.
\tag{11.2}
$$

Substituting (11.1)–(11.2) into (10.2),

$$
\boxed{
T_{22}
=
\frac{
DS_2+2D^2-6D+3-3\sum_Ls_L^2
}{D^3}.
}
\tag{11.3}
$$

This evaluates every \(2+2\) contribution from the frozen magnitudes alone.

## 11.1 Exact line sum

The audited line purity gives

$$
s_L
=
Dq_{L,0}-1
=
\frac{D-21}{D+1}
+
\frac{20\ell_L}{M},
$$

where \(\ell_L\in\{0,2\}\). Put

$$
s_0=\frac{D-21}{D+1}.
$$

Exactly \(M/2\) lines have \(\ell_L=2\). Therefore

$$
\boxed{
\sum_Ls_L^2
=
(D+1)s_0^2+40s_0+\frac{800}{M}.
}
\tag{11.4}
$$

## 11.2 Exact \(S_2\) relation

Let

$$
\mathcal O_{10}:=\sum_{g\in\Gamma}x_g^{(10)}
$$

be the frozen objective of the pseudo-point. Then

$$
\boxed{
S_2
=
\frac{2D}{D+1}
+
\frac{20}{M}
\left(
\mathcal O_{10}-\frac{M}{D+1}
\right).
}
\tag{11.5}
$$

A concise derivation is as follows. Write

$$
x^{(10)}=b+\frac{10}{M}d.
$$

The self-Fourier vectors \(b,d\) satisfy

$$
\langle b,d\rangle=0,
\qquad
\|b\|_2^2=\frac{2D}{D+1},
\qquad
\|d\|_2^2=2\langle\mathbf1_\Gamma,d\rangle.
$$

Using

$$
\mathcal O_{10}
=
\frac{M}{D+1}
+
\frac{10}{M}\langle\mathbf1_\Gamma,d\rangle
$$

gives (11.5).

Equations (11.3)–(11.5) are an exact frozen-data expression for the entire \(2+2\) fourth-moment contribution.

## 11.3 Uniform numerical enclosure

For nonzero labels,

$$
x_z^{(10)}
\le
U=
\frac{11}{D+1}+\frac{10}{M}.
$$

Thus

$$
S_2\le1+U(D-1).
$$

Dropping the negative term in (11.3) gives

$$
\boxed{
0\le T_{22}
\le
\frac{
D[1+U(D-1)]+2D^2-6D+3
}{D^3}
<
2.124177\times10^{-18}.
}
\tag{11.6}
$$

This bound is phase-independent.

---

# 12. Exact line-shift SOS mean

Because

$$
\operatorname{Tr}R_\kappa^3
=
C_{\mathrm{dep}}+
C_{\mathrm{ind}}(\kappa)
$$

and the independent part has zero line-shift average,

$$
\mathbb E_\kappa\operatorname{Tr}R_\kappa^3
=
C_{\mathrm{dep}}.
$$

The preceding fourth-moment decomposition gives

$$
\boxed{
\mathbb E_\kappa\operatorname{Tr}R_\kappa^4
=
\sum_{L,k}p_{L,k}^4
-\frac1{D^2}
+
T_{22}.
}
\tag{12.1}
$$

Therefore

$$
\boxed{
\begin{aligned}
\mathbb E_\kappa
\operatorname{Tr}(R_\kappa^2-R_\kappa)^2
={}&
1+
\frac2D-\frac1{D^2}\\
&+
\sum_{L,k}p_{L,k}^4
-
2\sum_{L,k}p_{L,k}^3
+
T_{22}.
\end{aligned}
}
\tag{ShiftSOSMean}
$$

Using

$$
\sum_{L,k}p_{L,k}^2=2,
$$

this is equivalently

$$
\boxed{
\mathbb E_\kappa
\operatorname{Tr}(R_\kappa^2-R_\kappa)^2
=
\sum_{L,k}p_{L,k}^2(1-p_{L,k})^2
-
\left(1-\frac1D\right)^2
+
T_{22}.
}
\tag{12.2}
$$

This is the exact corrected line-shift SOS mean.

For a putative physical lift, all stabilizer marginals are probabilities and the audited bound

$$
C_{\mathrm{dep}}
<
c_0=
2\sqrt{\frac3D}-\frac1D
$$

holds. Since every fourth moment is nonnegative,

$$
\boxed{
\mathbb E_\kappa
\operatorname{Tr}(R_\kappa^2-R_\kappa)^2
\ge
1-2c_0
>
0.999999992859955.
}
\tag{12.3}
$$

Thus a physical unshifted field would be a zero of a nonnegative discrete-shift residual whose mean is almost one. This is not contradictory: a low-degree character polynomial can have an isolated unit spike with \(D^{-3/2}\)-scale RMS.

---

# 13. Slightly sharper exact shift-RMS bound

The audited formula is

$$
\mathbb E_\kappa|C_{\mathrm{ind}}|^2
\le
\frac6{D^3}\sum_zx_z^3.
$$

For \(z\ne0\),

$$
x_z^3\le Ux_z^2,
$$

so

$$
\sum_zx_z^3
\le
1+U(S_2-1).
$$

Since

$$
\mathcal O_{10}\le MU,
$$

equation (11.5) gives

$$
S_2-1
\le
1+\frac{198}{D+1}+\frac{200}{M}.
$$

Hence

$$
\boxed{
\mathbb E_\kappa|C_{\mathrm{ind}}|^2
\le
\frac6{D^3}
\left[
1+
U\left(
1+\frac{198}{D+1}+\frac{200}{M}
\right)
\right].
}
\tag{13.1}
$$

At the exact frozen integers,

$$
\boxed{
\operatorname{RMS}(C_{\mathrm{ind}})
<
2.681123\times10^{-27}.
}
\tag{13.2}
$$

This improves the previous \(2.682\times10^{-27}\) enclosure, but it remains average-only.

---

# 14. Correct finite-difference substitute for the false Hessian

Choose one representative from each pair \(\{T,-T\}\) of independent unordered zero-sum triples, and define

$$
A_T
=
\frac6{D^2}
\left(\operatorname{Re}\omega^{[u,v]/2}\right)
\alpha_u\alpha_v\alpha_w.
$$

Then

$$
C_{\mathrm{ind}}(\kappa)
=
2\operatorname{Re}
\sum_TA_T\chi_T(\kappa).
$$

If the unshifted field is physical, DiscreteMaximum gives

$$
\boxed{
2\operatorname{Re}
\sum_T
A_T\bigl(1-\chi_T(\kappa)\bigr)
\ge0
\quad\forall\kappa.
}
\tag{14.1}
$$

For a shift \(s\) on one line \(L\) only,

$$
\boxed{
2\operatorname{Re}
\sum_{T\ni L}
A_T
\left(
1-\omega^{s\,t_{T,L}}
\right)
\ge0
\quad\forall s\in\mathbb F_D.
}
\tag{14.2}
$$

Averaging over \(s\) yields

$$
\boxed{
2\operatorname{Re}
\sum_{T\ni L}A_T\ge0.
}
\tag{14.3}
$$

More generally, averaging independently over a set \(\mathcal J\) of lines gives

$$
\boxed{
2\operatorname{Re}
\sum_{T:T\cap\mathcal J\ne\varnothing}A_T\ge0.
}
\tag{14.4}
$$

These are the valid finite-difference replacements for the invalid continuous \(C_{\mathrm{ind}}\)-Hessian.

They remain phase-sensitive. The frozen magnitudes determine only

$$
|A_T|
=
\frac6{D^2}
\left|
\operatorname{Re}\omega^{[u,v]/2}
\right|
\sqrt{x_ux_vx_w},
$$

and therefore

$$
|A_T|
\le
\frac{6U^{3/2}}{D^2}
<
2.70\times10^{-60}.
$$

They do not determine the signs of the real parts in (14.2)–(14.4).

The complete Fourier-support size is

$$
\binom{D+1}{3}(D-1),
$$

because every three distinct projective lines admit \(D-1\) nonzero scalar zero-sum relations. This enormous support is consistent with a unit-sized value at one shift despite the tiny RMS.

No magnitude-only contradiction follows.

---

# 15. Why phase-cancelling Cross2x2 sums do not close the gate

For each fixed partnered pair of stabilizer bases,

$$
\sum_{k,j}
\operatorname{Tr}
(P_{L,k}R_\alpha
P_{\tau(L),j}R_\alpha)
=
\operatorname{Tr}R_\alpha^2=1,
$$

and

$$
\sum_{k,j}
p_{L,k}p_{\tau(L),j}=1.
$$

Thus the total signed Cross2x2 slack is identically zero, independent of phases.

The first nontrivial phase-cancelled quantity is the squared residual sum

$$
\sum_{L,k}\delta_{L,k}^2
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
$$

Averaging this over the discrete line shifts gives exactly `ShiftSOSMean`. Its \(2+2\) portion is entirely fixed by \(x^{(10)}\), but its same-line fourth moments retain the line phases.

Accordingly:

* unweighted Cross2x2 summation gives only \(1=1\);
* ResidualSOS is exact but phase-sensitive;
* line-shift averaging yields the new fourth-moment decomposition, not a pointwise frozen obstruction;
* no phase-uniform positive lower bound for the unshifted residual is obtained.

---

# 16. Earliest remaining gap

For the fixed pseudo-magnitude \(x^{(10)}\), physical lifting is equivalent to any of:

$$
R_\alpha^2=R_\alpha,
$$

$$
C(\alpha)=1,
$$

$$
\delta_{L,k}=0
\quad\forall L,k,
$$

or stabilizer positivity plus all designated Cross2x2 inequalities.

The new line-shift fourth-moment identity proves that:

* the averaged residual of a hypothetical physical lift is almost one;
* the entire two-line fourth-order contribution is explicitly known and smaller than \(2.125\times10^{-18}\);
* all unresolved fourth-order dependence is confined to the same-line fourth moments.

It does **not** show that the unshifted residual is positive.

No compatible phase field with \(C=1\) is constructed.

No explicit \(\eta>0\) is proved such that

$$
C(\alpha)\le1-\eta
$$

for every phase assignment with magnitudes \(x^{(10)}\).

No exact physical vector with

$$
\mathcal F_\Gamma>10
$$

is exhibited.

Therefore \(x^{(10)}\) remains an unresolved pseudo-candidate, and PW10 remains open.

---

# Audit ledger

## VERIFIED

* The objection to the Round 18 continuous \(C_{\mathrm{ind}}\)-only Hessian.
* The correct full fixed-magnitude Hessian:

  $$
  C''(0)
  =
  -3\operatorname{Tr}[(P^\perp A P^\perp)^2]\le0.
  $$
* DiscreteMaximum.
* MUB2, with all tensor orientations and normalizations.
* ResidualSOS.
* ResidualFourier.
* Cross2x2 and its equivalence to rank-one lifting under stabilizer positivity.
* The exact count

  $$
  D^2(D+1)
  =
  834676191481542500102529837710713256761115423061571062.
  $$
* KnownViolation, including

  $$
  >1.1625\times10^{-45}.
  $$
* The corrected classification of line-shift fourth-moment survivors.
* The exact same-line fourth contribution.
* The exact \(2+2\) phase sum \(16+8\operatorname{Re}\omega^{[u,v]}\).
* The exact frozen \(T_{22}\) formulas.
* ShiftSOSMean.
* The strengthened frozen ShiftRMS bound.
* The valid discrete finite-difference conditions replacing the false Hessian.

## CORRECTED

* Round 18 equations (10.1)–(10.2) for \(C_{\mathrm{ind}}\) alone are retracted.
* “Only patterns \(4\) and \(2+2\)” is corrected to:

  * all nonzero labels on one line; or
  * two inverse pairs on two distinct lines.
* A tiny line-shift RMS is confirmed to be average-only.
* The MUB residual and Cross2x2 systems are identified explicitly as exact structured forms of global idempotence, not independent phase-free exclusions.

## DISPROVED

* Continuous invariance of \(C_{\mathrm{dep}}\) under balanced-integer line-phase lifts.
* Validity of the prior \(C_{\mathrm{ind}}\)-only continuous Hessian.
* Any inference from the line-shift RMS scale to a uniform cubic gap.
* Any claim that unweighted summation of Cross2x2 produces a nontrivial frozen-magnitude inequality.

## NECESSARY-ONLY

* FullHessian stationarity and semidefiniteness.
* DiscreteMaximum and its finite-difference consequences.
* MUB stabilizer positivity.
* Every Cross2x2 inequality.
* Vanishing of all MUB residuals.
* The phase-sensitive same-line fourth-moment conditions.

## SUFFICIENT-ONLY

* Stabilizer positivity plus all designated Cross2x2 inequalities is sufficient for a physical lift; under the standing hypotheses it is also necessary.
* Vanishing of all residuals is sufficient and necessary for a physical lift.

## OPEN

* Whether \(x^{(10)}\) has compatible phases with

  $$
  C(\alpha)=1.
  $$
* Whether all such phase fields have a uniform positive residual gap.
* Whether a different objective-above-\(10\) magnitude profile is physically liftable.
* PW10 for the exact frozen tuple.
* The finite \(r=2\), low-\(A\) gate.

The first new claim requiring independent verification is the exact discrete line-shift fourth-moment decomposition:

$$
\boxed{
\mathbb E_\kappa\operatorname{Tr}R_\kappa^4
=
\sum_{L,k}p_{L,k}^4-\frac1{D^2}
+
\frac1{D^3}
\sum_{\substack{u,v\ne0\\u,v\ \mathrm{independent}}}
\left(2+\operatorname{Re}\omega^{[u,v]}\right)x_ux_v.
}
$$

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-19-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-19-local-audit.md bytes=11449 sha256=7b0d0754c810012a80fc6aa6a5623666522ad54e97f17113ccfb5429efed09c8 -->

# Round 19 local audit

- Audit completed (UTC): `2026-09-13T04:14:20Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-19-response.md`
- Web-response SHA-256:
  `6fbf0af07648a42e68e8e66a7d25117f09eb54833a2b23bc38b43ad82c473046`
- Browser completion indicator: `Worked for 12m 29s`
- Capture equality: the browser response-copy payload and the TextEdit capture
  were exactly equal at `23,884` Unicode characters.  The artifact and output
  copies are byte-identical UTF-8 files, each `23,912` bytes and `1,471`
  newline-terminated lines.

## Verdict

Round 19 supplies a correct exact decomposition of the discrete line-shift
fourth moment.  For the frozen magnitude profile, every cross-line `2+2`
term is phase-free and explicitly evaluable.  All remaining fourth-order
phase dependence is confined to the same-line fourth moments:

\[
\boxed{
\mathbb E_\kappa\operatorname{Tr}R_{\alpha,\kappa}^4
=\sum_{L,k}p_{L,k}^4-\frac1{D^2}
+\frac1{D^3}
\sum_{\substack{u,v\ne0\\u,v\ {m independent}}}
\left(2+\operatorname{Re}\omega^{[u,v]}\right)x_ux_v.
}
\]

This is a genuine coefficient-specific cross-line identity, but it is an
**orbit average**.  It does not prove that the unshifted candidate has a
positive residual.  No compatible phases with `C(alpha)=1` are constructed,
and no positive phase-uniform gap is proved.  Therefore the physical lift of
`x^(10)`, PW10, and the finite `r=2`, low-`A` gate remain open.

## Corrected continuous variation

The response correctly retracts the Round 18 `C_ind`-only continuous
Hessian.  For `t=(D-1)/2`, the same-line zero-sum triple `(t,t,1)` has
balanced-integer sum `D`; under the proposed real deformation its monomial
acquires `exp(i D theta_L)`.  Thus `C_dep` is invariant under the finite
field-character shifts but not under that continuous interpolation.

The exact surviving discrete necessary condition at a physical unshifted
field is

\[
C_{\rm ind}(\kappa)\le C_{\rm ind}(0)
\qquad\text{for every }\kappa\in\mathbb F_D^{D+1}.
\]

For an arbitrary genuine fixed-magnitude phase path, the response's full
second derivative is correct.  With `A=R'(0)` and `R(0)=P` rank one,

\[
\boxed{
C''(0)=6\operatorname{Tr}(PA^2)-3\operatorname{Tr}(A^2)
=-3\operatorname{Tr}[(P^\perp A P^\perp)^2]\le0.
}
\]

The small-prime checker verifies the differentiated purity identity and the
block reduction for `p=3,5`.  This inequality is automatic at a projector;
it is not a magnitude-only obstruction.

## MUB residual and cross-basis audit

The Round 19 re-audit confirms the Round 18 conclusions:

\[
\sum_{L,k}P_{L,k}\otimes P_{L,k}=I+F,
\]

\[
\sum_{L,k}\delta_{L,k}^2
=\operatorname{Tr}(R_\alpha^2-R_\alpha)^2,
\]

and

\[
\delta_{L,k}
=\frac1D\sum_t(Q_{tv_L}-\alpha_{tv_L})\omega^{-kt}.
\]

In the two-design expansion, the second Weyl factor is
`W_(-z)=W_z^dagger`; this is the matrix-basis completeness identity that
produces the swap `F`.  The conjugations, signs, and `1/D` normalizations
match the small-prime matrix check.

For one distinct partner basis per line, all designated `Cross2x2`
inequalities imply `delta_(L,k)<=0`.  Their sum over `k` is zero, so all
residuals vanish and `R_alpha` is rank-one.  The converse holds with equality.
The exact number of inequalities is

\[
D^2(D+1)
=834676191481542500102529837710713256761115423061571062.
\]

Stabilizer positivity is physically necessary but is not used in the
sufficiency implication itself.  Accordingly the web ledger's placement of
the equivalence under the heading `SUFFICIENT-ONLY` is only a labeling
oddity: the prose correctly states an equivalence under the standing
Hermiticity, trace-one, and purity-one assumptions.

For the already known nonphysical field, the existential designated
cross-basis violation remains

\[
\frac{1-c_0}{D\sqrt{D(D^2-1)}}
=1.162523240076574845\ldots\times10^{-45}
>1.1625\times10^{-45}.
\]

This detects that one known field.  It does not exclude every phase lift of
the frozen magnitudes.

## Exact fourth-moment survivor classification

Independent averaging over the `D+1` line shifts forces the nonzero scalar
labels on each represented line to sum to zero in `F_D`.

- If all four labels are nonzero, the only possibilities are one line
  (`4`) or two inverse pairs on distinct lines (`2+2`).
- With zero labels included, the one-line sector also contains the `0`,
  `2+0+0`, and `3+0` patterns.
- No line may occur exactly once, so no three-line or four-line pattern
  survives.

The full same-line sector is

\[
\sum_{L,k}p_{L,k}^4-\frac1{D^2}.
\]

The subtraction is exactly the overcount of the all-zero quadruple when the
`D+1` line fourth moments are summed.

For noncollinear nonzero `u,v`, exhaustive enumeration of the 24 orderings
of `{u,-u,v,-v}` gives the Weyl phase sum

\[
16+8\operatorname{Re}\omega^{[u,v]}.
\]

The ordered-pair normalization in the response is correct: each unordered
pair of inverse-pair classes occurs through eight ordered `(u,v)` choices,
turning the coefficient `2+Re omega^[u,v]` into the 24-ordering phase sum.
The checker verifies this and the full averaged fourth moment by exhaustive
line-shift enumeration at `p=3,5`.

## Frozen cross-line evaluation

Let

\[
B_{22}=\sum_{u,v\ {m independent}}
\left(2+\operatorname{Re}\omega^{[u,v]}\right)x_ux_v,
\quad
S_2=\sum_zx_z^2,
\quad
s_L=\sum_{z\in L\setminus\{0\}}x_z.
\]

For a self-Fourier magnitude profile of mass `D`, direct character summation
gives

\[
\boxed{
B_{22}=DS_2+2D^2-6D+3-3\sum_Ls_L^2.
}
\]

The frozen line masses obey

\[
s_L=\frac{D-21}{D+1}+\frac{20\ell_L}{M},
\qquad \ell_L\in\{0,2\},
\]

with exactly `M/2` lines of the second type.  Hence

\[
\sum_Ls_L^2
=D-3-\frac{396}{D+1}+\frac{800}{M},
\]

and therefore

\[
B_{22}=DS_2+2D^2-9D+12
+\frac{1188}{D+1}-\frac{2400}{M}.
\]

The web response's equivalent expression for the line-square sum and its
`S_2` relation both check exactly.  The phase-free numerical enclosure is

\[
0\le \frac{B_{22}}{D^3}
<2.124176763460723\times10^{-18}
<2.124177\times10^{-18}.
\]

## Exact residual mean and its limitation

Using

\[
C_{\rm dep}=\sum_{L,k}p_{L,k}^3-\frac1D,
\qquad
\sum_{L,k}p_{L,k}^2=2,
\]

the exact mean is

\[
\boxed{
\begin{aligned}
\mathbb E_\kappa\operatorname{Tr}(R_\kappa^2-R_\kappa)^2
={}&\sum_{L,k}p_{L,k}^2(1-p_{L,k})^2\\
&-\left(1-\frac1D\right)^2+\frac{B_{22}}{D^3}.
\end{aligned}}
\]

For a hypothetical physical unshifted lift, the audited bound on `C_dep`
implies the response's valid estimate

\[
\mathbb E_\kappa\operatorname{Tr}(R_\kappa^2-R_\kappa)^2
>0.999999992859955.
\]

The independent audit slightly sharpens it by using
`Tr(R_kappa^4)>=1/D`, rather than only nonnegativity:

\[
\mathbb E_\kappa\operatorname{Tr}(R_\kappa^2-R_\kappa)^2
>1+\frac3D-4\sqrt{\frac3D}.
\]

Neither bound is pointwise.  A physical unshifted field could have residual
zero at one shift while the remaining enormous orbit supplies the positive
mean.  No inference from this mean to a uniform cubic or residual gap is
accepted.

## Discrete finite differences and RMS

Pairing inverse independent triples writes

\[
C_{\rm ind}(\kappa)=2\operatorname{Re}\sum_TA_T\chi_T(\kappa).
\]

The response correctly derives from the discrete maximum

\[
2\operatorname{Re}\sum_TA_T(1-\chi_T(\kappa))\ge0
\]

and its one-line and subset-averaged consequences.  These constraints remain
phase-sensitive because the frozen data determine `|A_T|`, not the needed
real parts.  Their support count

\[
\binom{D+1}{3}(D-1)
\]

is correct: every three distinct projective lines have a one-dimensional
linear relation with `D-1` nonzero scalar multiples.

The strengthened shift RMS bound also checks:

\[
\operatorname{RMS}(C_{\rm ind})
<2.681122222466348\times10^{-27}
<2.681123\times10^{-27}.
\]

It remains average-only.

## Verification receipts

- `work/verify_round19_web_response.py` checks the exact capture hash and
  dimensions, mandatory verdict/correction markers, frozen integer and
  rational identities, inequality count, line-mass sum, `S_2` upper-bound
  algebra, and every displayed decimal enclosure.  Result: `PASS`.
- Web-response checker SHA-256:
  `419e4c5b4621a04f5627cb29149388e70736bbc9a8af05c67524675b9d2317d3`
- `work/verify_round19_shift_sos.py` exhaustively checks the 24-ordering phase
  sum and all discrete line shifts for `p=3,5`, including the cubic mean,
  fourth moment, residual mean, generic `B_22`, self-Fourier specialization,
  and exact frozen line-mass identity.  Result: `PASS`.
- Shift-SOS checker SHA-256:
  `5ed370b1a6bd705f0907854720853e21a31569b9aab2c54999a8ed55c5c60400`
- `work/verify_round19_full_hessian.py` independently checks the full Hessian
  and projector-block reduction for `p=3,5`.  Result: `PASS`.
- Full-Hessian checker SHA-256:
  `7210cdd5ac38baec33f19f3eab67ffd0efe69eca2149312d400694330625c090`
- Independent derivation:
  `work/round-19-independent-shift-sos.md`
- Independent-derivation SHA-256:
  `d189970e8c24dcdc457293d68d7279040018588da2bee1705f44e2fc5f955b47`
- The Round 18 MUB/SOS checker was rerun after capture and again returned
  `PASS (with Hessian flaw detected)`; Round 19 supplies the corrected full
  Hessian rather than reviving that rejected step.

All three Round 19 Python files pass `py_compile`.

## Corrected status ledger

### VERIFIED

- The correction to the false continuous `C_ind`-only Hessian.
- The full fixed-magnitude Hessian and its automatic semidefiniteness at a
  true projector.
- `DiscreteMaximum` and the stated finite-difference consequences.
- `MUB2`, `ResidualSOS`, `ResidualFourier`, and the designated `Cross2x2`
  equivalence under the standing hypotheses.
- The `1.1625e-45` existential violation for the already known nonphysical
  phase field.
- The corrected fourth-moment survivor classification, including zero-label
  terms.
- The same-line contribution, 24-ordering phase sum, frozen `B_22` formula,
  exact shift-SOS mean, and strengthened shift RMS bound.

### CORRECTED / DISPROVED

- The Round 18 continuous invariance of `C_dep` and the resulting
  `C_ind`-only differential conditions are false.
- “Only `4` and `2+2`” is valid only in the all-four-nonzero sector; the full
  one-line sector also contains zero-label patterns.
- An orbit-average residual near one does not imply a pointwise residual gap.
- An unweighted sum of all `Cross2x2` inequalities is only the identity
  `1=1`.

### NECESSARY BUT NOT EXCLUDING

- The full Hessian, discrete maximum, finite differences, stabilizer
  positivity, and each `Cross2x2` inequality are necessary at a physical
  lift but do not exclude the frozen magnitudes.
- The same-line fourth moments retain unknown phase data.

### EQUIVALENT REPACKAGINGS

- Vanishing of every MUB residual, global idempotence, `C(alpha)=1`, and the
  complete designated `Cross2x2` system are equivalent physicality tests
  under the standing assumptions.  They are not new phase-free certificates.

### OPEN

- Whether `x^(10)` admits compatible phases with `C(alpha)=1`.
- Whether all compatible phases for `x^(10)` have a positive pointwise
  residual gap.
- Whether another objective-above-10 magnitude profile is physically
  liftable.
- PW10 for the exact frozen tuple.
- The finite `r=2`, low-`A` gate and all downstream claims.

Even a future exclusion of this single pseudo-point would not prove PW10 for
all physical magnitude profiles.  No quantifier promotion is made.

<!-- END HISTORICAL FILE path=outputs/round-19-local-audit.md -->


# ROUND 020

## PROMPT

<!-- BEGIN HISTORICAL FILE path=work/round-20-prompt.md bytes=8840 sha256=7e9f597e4117ce4769166d3dc681b5eadd5529f231ac0b8f7f6e01fe7b32bd5e -->

# Round 20 — exploit the exact single-line residual slice and attack two-line compatibility

Continue in this same ordinary Chat conversation, with the same model/tier and
the same canonically frozen finite `r=2`, low-`A` gate.  Give a public,
self-contained derivation and no hidden chain-of-thought.  Do not repeat the
Round 8--19 narrative.  Audit the new lemma below, then use it to make a
genuinely new attack on the physical lift.

## Exact frozen boundary

Use exactly

\[
m=485165196,
\quad P=m+41=485165237,
\quad D=941541228773064677=4P^2+1,
\]

\[
M=m(m-1)=235385266924553220,
\quad
\Gamma=(A-A)\setminus\{0\},
\]

where

\[
A=\{(t_j,t_j^2):0\le j\le P-42\},
\qquad
t_j=2Pj+(j^2\bmod P).
\]

The open physical gate is

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10
\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use

\[
W_{(p,q)}|y\rangle=\omega^{p(y+q/2)}|y+q\rangle,
\qquad
W_uW_v=\omega^{[u,v]/2}W_{u+v}.
\]

The exact magnitude pseudo-point is

\[
b_0=1,
\quad b_z=(D+1)^{-1}\ (z\ne0),
\]

\[
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\quad
y=\mathbf1_\Gamma+\lambda/D,
\quad
x^{(10)}=b+(10/M)(y-(M/D)b).
\]

It is positive, even, self-Fourier, has mass `D`, passes every audited
magnitude, small-Gram, parity, stabilizer, and line-factor condition, and has
frozen objective strictly above `10`.  A physical lift requires phases

\[
\alpha_{-z}=\overline{\alpha_z},
\quad |\alpha_z|^2=x_z^{(10)},
\quad
R_\alpha=D^{-1}\sum_z\alpha_zW_z,
\]

with `R_alpha` a rank-one projector, equivalently `C(alpha)=Tr R_alpha^3=1`.
Excluding this one pseudo-point would still not prove PW10; a physical lift
would disprove PW10.

## Audited Round 19 boundary

The Round 18 continuous `C_ind`-only Hessian is retracted.  Continuous
balanced-integer line phases do not preserve `C_dep`.  The correct full
fixed-magnitude Hessian at a physical lift `P` is

\[
C''(0)=6\operatorname{Tr}(PA^2)-3\operatorname{Tr}(A^2)
=-3\operatorname{Tr}[(P^\perp A P^\perp)^2]\le0,
\]

and is automatic rather than excluding.  The valid finite condition is

\[
C_{\rm ind}(\kappa)\le C_{\rm ind}(0)
\quad\forall\kappa\in\mathbb F_D^{D+1}.
\tag{DiscreteMaximum}
\]

`MUB2`, `ResidualSOS`, `ResidualFourier`, the designated `Cross2x2`
equivalence, and the known-field violation above `1.1625e-45` have all been
independently checked.  They repackage global idempotence and do not yet
exclude the frozen magnitudes.

Round 19's new exact line-shift fourth moment is also independently checked:

\[
\boxed{
\mathbb E_\kappa\operatorname{Tr}R_{\alpha,\kappa}^4
=\sum_{L,k}p_{L,k}^4-\frac1{D^2}
+\frac{B_{22}}{D^3},
}
\]

\[
B_{22}=\sum_{u,v\ {m independent}}
\left(2+\operatorname{Re}\omega^{[u,v]}\right)x_ux_v
\]

\[
=D\sum_zx_z^2+2D^2-9D+12
+\frac{1188}{D+1}-\frac{2400}{M}.
\]

Every cross-line `2+2` term is phase-free; the same-line fourth moments retain
the line-factor data.  The exact residual mean is larger than
`0.999999992859955` for a hypothetical physical unshifted lift, but this is
only an orbit average and is not a pointwise contradiction.  The sharpened
`C_ind` RMS below `2.681123e-27` is likewise average-only.

## New exact single-line slice to audit

Assume, only for deriving necessary consequences, that the unshifted field is
a physical projector

\[
P=|\psi\rangle\langle\psi|.
\]

Fix one stabilizer line `L`, work in its eigenbasis, and put

\[
p_k=\langle k|P|k\rangle.
\]

Multiplying the nonzero line coefficients by `omega^(s t)` cyclically
permutes these probabilities.  Up to the Fourier-sign convention write

\[
q_k=p_{k-s},
\qquad d_k=q_k-p_k.
\]

The shifted reconstructed operator should be

\[
R_s=P+\Delta_s,
\qquad
\Delta_s=\sum_kd_k|k\rangle\langle k|.
\]

Since `P^2=P`, direct matrix multiplication proposes

\[
(R_s^2-R_s)_{kk}=d_k(p_k+q_k-1),
\]

and, for `k != j`,

\[
(R_s^2-R_s)_{kj}=P_{kj}(d_k+d_j).
\]

Therefore

\[
\boxed{
\begin{aligned}
f_L(s)
&:=\operatorname{Tr}(R_s^2-R_s)^2\\
&=\sum_kd_k^2(1-p_k-q_k)^2
+\sum_{k\ne j}p_kp_j(d_k+d_j)^2.
\end{aligned}}
\tag{SingleLineSOS}
\]

Audit every sign, orientation, ordered-pair multiplicity, and use of
Hermiticity in this formula.  Do not assume it merely because it is an SOS.

The exact frozen line collision obeys

\[
c_L:=\sum_kp_k^2<\frac3D,
\]

so `p_k,q_k<=sqrt(3/D)`.  Every nonzero frozen line coefficient has the exact
floor

\[
x_{tv_L}^{(10)}\ge\gamma,
\qquad
\gamma=
\frac{D(m-11)-10m}{D(D+1)(m-1)}>0.
\]

For every nonzero `s`, Parseval should give

\[
\sum_kd_k^2
=\frac2D\sum_{t\ne0}x_{tv_L}^{(10)}
\left(1-\cos\frac{2\pi st}{D}\right)
\ge2\gamma.
\]

If correct, the diagonal part of `SingleLineSOS` proves the explicit
pointwise conditional gap

\[
\boxed{
f_L(s)\ge
2\gamma\left(1-2\sqrt{3/D}\right)^2
>2.12417670\times10^{-18}
\quad(s\ne0).
}
\tag{SingleLineGap}
\]

This does **not** exclude an unshifted physical lift.  It says that, if such a
lift exists, changing exactly one line character gives a uniformly
nonphysical field.

The global-Weyl-character subgroup is

\[
\mathcal H
=\{\kappa(g):g\in\mathbb F_D^2\},
\qquad
\kappa(g)_L=[g,v_L],
\qquad |\mathcal H|=D^2.
\]

Every `h in H` displaces a physical lift and has zero residual.  By applying
`SingleLineGap` after a displacement, every Hamming-one neighbor
`h+s e_L`, `s!=0`, should have the same positive lower bound.  Audit this
quantifier carefully.

## Required new attack after the audit

Do not stop after verifying `SingleLineSOS` or restating that a generic
nonnegative polynomial can have isolated zeros.  Use the actual frozen
coefficients and proceed in this order.

### 1. Two-line plaquette compatibility

For distinct stabilizer lines `L,M`, derive the exact residual of

\[
R_{s,t}=P+\Delta_{L,s}+\Delta_{M,t}.
\]

The two diagonal perturbations are diagonal in mutually unbiased bases and
need not commute.  Expand the residual without dropping the mixed products.
Then average or take a signed mixed finite difference over nonzero `s,t` so
that every cancellable phase disappears.  Express the result in terms of the
two line probability factors, their frozen autocorrelations, and any genuinely
unresolved cross-basis Bargmann phases.

Seek one of the following exact outcomes:

- a phase-free two-line lower bound incompatible with zero residual on all
  global-character patterns;
- an explicit compatibility equation that the independently feasible line
  factors must satisfy across every pair of MUBs;
- or a rigorous no-go showing this entire two-line averaging route collapses
  to already known identities.

A formula that silently retains all entries of the unknown projector is not a
new frozen-data constraint.

### 2. Zero-set/Fourier test on the quotient

Let

\[
f(\kappa)=\operatorname{Tr}(R_\kappa^2-R_\kappa)^2\ge0.
\]

It vanishes on the exact subgroup `H` and, conditional on a lift, has the
explicit positive lower bound on every Hamming-one boundary point of `H`.
Compute the actual Fourier support and coefficient relations of this specific
quartic residual, quotient by `H`, and test whether these zero and boundary
conditions are compatible with the frozen `x^(10)` coefficients.  Use exact
finite-group identities or rational/trigonometric inequalities.  Do not infer
a pointwise statement from an average and do not replace the coefficient
structure by an arbitrary low-degree polynomial.

### 3. Direct product-state SOS if the slice route does not close

Use

\[
U_a=W_a\otimes\overline{W_a},
\qquad S_A=\sum_{a\in A}U_a.
\]

Because doubled Weyl phases cancel and the ordered nonzero differences of
`A` are distinct, audit the exact identity

\[
\boxed{K_\Gamma=S_AS_A^*-mI.}
\tag{DifferenceFrame}
\]

For `zeta=psi tensor bar(psi)`, PW10 is equivalent to

\[
\|S_A^*\zeta\|^2\le m+10.
\]

Derive a genuinely stronger product-vector/SOS inequality from the rank-one
vectorization constraint.  The unrestricted operator norm, Bell eigenvalue
counting, elementary Bell-weight caps, and already passed magnitude/parity/
small-Gram/stabilizer layers are not sufficient.  Either prove the bound `10`
or exhibit an exact physical vector above `10`; rounded numerics and solver
labels are not certificates.

## Verdict discipline

Give one verdict for PW10: **PROVED**, **DISPROVED**, or **OPEN WITH EARLIEST
GAP**.  End with a ledger separating **VERIFIED**, **CORRECTED**,
**DISPROVED**, **NECESSARY-ONLY**, **EQUIVALENT**, and **OPEN**.  State
separately:

- `SingleLineSOS`, its Parseval normalization, and the exact numerical gap;
- the zero set on `H` and its Hamming-one boundary;
- any two-line plaquette or quotient-Fourier constraint;
- `DifferenceFrame` and any new product-state consequence;
- the physical `C(alpha)=1` lift of `x^(10)`;
- `x^(10)` as a candidate, PW10, and the finite `r=2` gate.

Identify the first genuinely new claim requiring independent verification.

<!-- END HISTORICAL FILE path=work/round-20-prompt.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-20-response.md bytes=20169 sha256=1bf725e86a5e33c84e8c7cc72d42447d8baa3398546e28ccf507cdc27710f5f9 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The new single-line lemma is correct, including its Parseval normalization and numerical constant. Conditional on a physical lift of \(x^{(10)}\), every nontrivial one-line character shift has residual at least

$$
\boxed{
g_{\rm line}
=
2\gamma\left(1-2\sqrt{\frac3D}\right)^2
=
2.1241767045114586\ldots\times10^{-18}.
}
$$

The same bound holds at every Hamming-one neighbor of every global Weyl-character displacement of that lift.

The first two-line calculation can also be completed exactly. Its mixed four-corner term contains several explicitly identified cross-basis Bargmann invariants. Those terms are not determined by the two line shadows or their autocorrelations, and even the complete uniform average over the two cyclic shifts retains them.

The quotient-zero-set route does not close the problem. I give an explicit nonnegative \(\mathcal H\)-invariant Fourier polynomial which:

* has Fourier characters supported on only three projective lines;
* vanishes exactly on the global-character subgroup \(\mathcal H\);
* is at least \(2/(D-1)>g_{\rm line}\) at every Hamming-one boundary point;
* and is globally bounded by \(2\).

Thus the known zero set, Fourier support, nonnegativity, global boundedness, and single-line gap are mutually compatible. A contradiction must use the actual frozen coefficients, not only those structural properties.

---

# 1. Audit of the single-line residual

Assume only in this section that the unshifted coefficient field is physical:

$$
P=|\psi\rangle\langle\psi|.
$$

Fix an isotropic line \(L\), and let

$$
\{|k\rangle:k\in\mathbb F_D\}
$$

be its stabilizer eigenbasis. Put

$$
p_k=\langle k|P|k\rangle.
$$

Multiplication of the nonzero line coefficients by \(\omega^{st}\) sends

$$
p_k\longmapsto q_k=p_{k-s}.
$$

The sign of \(s\) changes if the opposite Fourier convention is used, but all formulas below are invariant under \(s\mapsto-s\).

Set

$$
d_k=q_k-p_k,
\qquad
\Delta_s=\sum_kd_k|k\rangle\langle k|.
$$

Then

$$
R_s=P+\Delta_s.
$$

Because both \(p\) and \(q\) are probability vectors,

$$
\sum_kd_k=0.
$$

Since \(P^2=P\),

$$
R_s^2-R_s
=
P\Delta_s+\Delta_sP+\Delta_s^2-\Delta_s.
$$

## 1.1 Matrix entries

For a diagonal entry,

$$
\begin{aligned}
(R_s^2-R_s)_{kk}
&=
2p_kd_k+d_k^2-d_k\\
&=
d_k(2p_k+d_k-1)\\
&=
\boxed{d_k(p_k+q_k-1)}.
\end{aligned}
$$

For \(k\ne j\),

$$
\begin{aligned}
(R_s^2-R_s)_{kj}
&=
P_{kj}d_j+d_kP_{kj}\\
&=
\boxed{P_{kj}(d_k+d_j)}.
\end{aligned}
$$

The residual is Hermitian. Therefore its squared Hilbert–Schmidt norm is the sum of the squared moduli of all entries:

$$
\begin{aligned}
f_L(s)
&:=
\operatorname{Tr}(R_s^2-R_s)^2\\
&=
\sum_kd_k^2(1-p_k-q_k)^2\\
&\quad+
\sum_{k\ne j}|P_{kj}|^2(d_k+d_j)^2.
\end{aligned}
$$

Since \(P\) has rank one,

$$
|P_{kj}|^2=p_kp_j.
$$

Hence

$$
\boxed{
\begin{aligned}
f_L(s)
&=
\sum_kd_k^2(1-p_k-q_k)^2\\
&\quad+
\sum_{k\ne j}p_kp_j(d_k+d_j)^2.
\end{aligned}
}
\tag{SingleLineSOS}
$$

The second sum is over ordered pairs \(k\ne j\), exactly as required by the Hilbert–Schmidt norm. There is no missing factor \(1/2\).

---

# 2. Parseval normalization and the exact gap

Use the line Fourier convention

$$
p_k=\frac1D\sum_t\alpha_{tv_L}\omega^{-kt}.
$$

Then

$$
q_k-p_k
=
\frac1D\sum_t
\alpha_{tv_L}
(\omega^{st}-1)\omega^{-kt}.
$$

Cyclic Parseval gives

$$
\begin{aligned}
\sum_kd_k^2
&=
\frac1D
\sum_t
|\alpha_{tv_L}|^2|\omega^{st}-1|^2\\
&=
\frac2D
\sum_{t\ne0}
x^{(10)}_{tv_L}
\left(
1-\cos\frac{2\pi st}{D}
\right).
\end{aligned}
\tag{2.1}
$$

For \(s\ne0\),

$$
\sum_{t\ne0}
\left(
1-\cos\frac{2\pi st}{D}
\right)=D.
$$

Using the audited pointwise floor

$$
x^{(10)}_{tv_L}\ge\gamma
\qquad(t\ne0),
$$

one gets

$$
\boxed{
\sum_kd_k^2\ge2\gamma.
}
\tag{2.2}
$$

The collision probability on every frozen line is

$$
c_L=\sum_kp_k^2=q_{L,0}<\frac3D.
$$

Consequently,

$$
p_k,q_k\le\sqrt{\frac3D}.
$$

Thus

$$
1-p_k-q_k
\ge
1-2\sqrt{\frac3D}>0.
$$

Dropping the nonnegative off-diagonal part of `SingleLineSOS` gives

$$
\boxed{
f_L(s)
\ge
2\gamma
\left(
1-2\sqrt{\frac3D}
\right)^2
\quad(s\ne0).
}
\tag{SingleLineGap}
$$

For the exact frozen integers,

$$
\gamma
=
\frac{D(m-11)-10m}
{D(D+1)(m-1)}
=
1.06208835983908795088646\ldots\times10^{-18}.
$$

Also

$$
\frac{1785011245}{10^{18}}
<
\sqrt{\frac3D}
<
\frac{1785011246}{10^{18}},
$$

as is verified by squaring the rational endpoints. Therefore

$$
\boxed{
g_{\rm line}
=
2.1241767045114586038878\ldots\times10^{-18}
>
2.12417670\times10^{-18}.
}
$$

This agrees with the proposed constant.

---

# 3. The global-character zero set and its Hamming boundary

Choose one generator \(v_L\) for every projective line and define

$$
\kappa(g)_L=[g,v_L].
$$

Then

$$
\mathcal H
=
\{\kappa(g):g\in\mathbb F_D^2\}
\subset\mathbb F_D^{D+1}.
$$

The map \(g\mapsto\kappa(g)\) is injective: if \([g,v_L]=0\) for every projective line, then \(g\) is symplectically orthogonal to all of \(\mathbb F_D^2\), hence \(g=0\). Thus

$$
|\mathcal H|=D^2.
$$

For \(h=\kappa(g)\),

$$
\alpha_z\longmapsto\alpha_z\omega^{[g,z]}
$$

reconstructs

$$
W_gPW_g^*.
$$

It is again a physical rank-one projector. Therefore the residual function

$$
f(\kappa)
=
\operatorname{Tr}(R_\kappa^2-R_\kappa)^2
$$

satisfies

$$
f(h)=0
\qquad(h\in\mathcal H).
$$

Now fix \(h\in\mathcal H\), a line \(L\), and \(s\ne0\). First displacing by \(h\) merely permutes the line probabilities. Applying the additional one-line character shift gives the same collision probability, the same line magnitudes, and the same lower bound. Hence

$$
\boxed{
f(h+se_L)\ge g_{\rm line}
\quad
\forall h\in\mathcal H,\ L,\ s\ne0.
}
\tag{3.1}
$$

The cosets

$$
se_L+\mathcal H,
\qquad
L\text{ a line},\ s\ne0,
$$

are all distinct. Indeed, if

$$
se_L-te_M\in\mathcal H
$$

with support on at most two projective lines, then the corresponding \(g\) is orthogonal to every third line, forcing \(g=0\), and hence \(L=M\) and \(s=t\).

Thus the quotient has exactly

$$
(D+1)(D-1)=D^2-1
$$

distinct Hamming-one boundary points around its guaranteed zero.

---

# 4. Exact two-line residual expansion

Now take two distinct stabilizer lines \(L\) and \(M\). Let

$$
\Delta=\Delta_{L,s},
\qquad
\Theta=\Delta_{M,t}.
$$

These are traceless Hermitian operators, diagonal in two mutually unbiased bases.

The doubly shifted field reconstructs

$$
R_{s,t}=P+\Delta+\Theta.
$$

Define

$$
H_\Delta
=
P\Delta+\Delta P+\Delta^2-\Delta,
$$

$$
H_\Theta
=
P\Theta+\Theta P+\Theta^2-\Theta.
$$

Then

$$
R_{s,t}^2-R_{s,t}
=
H_\Delta+H_\Theta+\Delta\Theta+\Theta\Delta.
\tag{4.1}
$$

Put

$$
f_{L,M}(s,t)
=
\operatorname{Tr}(R_{s,t}^2-R_{s,t})^2.
$$

The mixed four-corner quantity is

$$
\mathfrak P_{L,M}(s,t)
=
f_{L,M}(s,t)-f_L(s)-f_M(t).
$$

Use the notation

$$
\langle X\rangle=\operatorname{Tr}(PX).
$$

Because the two eigenbases are mutually unbiased,

$$
\operatorname{Tr}\bigl(F(\Delta)G(\Theta)\bigr)
=
\frac1D
\operatorname{Tr}F(\Delta)
\operatorname{Tr}G(\Theta)
\tag{4.2}
$$

for arbitrary scalar functions \(F,G\) on the two spectra.

A direct expansion of (4.1) gives

$$
\boxed{
\begin{aligned}
\mathfrak P_{L,M}(s,t)
={}&
4\langle\Delta\rangle\langle\Theta\rangle
-4\operatorname{Re}\langle\Delta\Theta\rangle\\
&+
8\operatorname{Re}
\langle\Delta^2\Theta+\Delta\Theta^2\rangle\\
&+
4\langle\Delta\Theta\Delta+\Theta\Delta\Theta\rangle\\
&+
2\operatorname{Tr}(\Delta\Theta\Delta\Theta)\\
&+
\frac4D
\operatorname{Tr}(\Delta^2)
\operatorname{Tr}(\Theta^2).
\end{aligned}
}
\tag{TwoLinePlaquette}
$$

Every term is real after the indicated real parts:

* \(\Delta\Theta\Delta\) and \(\Theta\Delta\Theta\) are Hermitian;
* \(\operatorname{Tr}(\Delta\Theta\Delta\Theta)\) is real because its adjoint is cyclically equivalent to itself.

Since every fixed-magnitude shift preserves Hilbert–Schmidt purity,

$$
2\langle\Delta\rangle+\operatorname{Tr}\Delta^2=0,
$$

and similarly for \(\Theta\). Therefore an equivalent form is

$$
\boxed{
\begin{aligned}
\mathfrak P_{L,M}(s,t)
={}&
\left(1+\frac4D\right)
\operatorname{Tr}\Delta^2\operatorname{Tr}\Theta^2\\
&-4\operatorname{Re}\langle\Delta\Theta\rangle\\
&+
8\operatorname{Re}
\langle\Delta^2\Theta+\Delta\Theta^2\rangle\\
&+
4\langle\Delta\Theta\Delta+\Theta\Delta\Theta\rangle\\
&+
2\operatorname{Tr}(\Delta\Theta\Delta\Theta).
\end{aligned}
}
\tag{4.3}
$$

This is the exact two-line plaquette compatibility condition.

---

# 5. The unresolved cross-basis Bargmann data

Let

$$
\{|k\rangle\}
\quad\text{and}\quad
\{|\widetilde j\rangle\}
$$

be the two stabilizer bases. Write

$$
\psi_k=\langle k|\psi\rangle,
\qquad
\widetilde\psi_j=\langle\widetilde j|\psi\rangle,
$$

and define the cross-basis Bargmann amplitudes

$$
\boxed{
\mathcal B_{kj}
=
\overline{\psi_k}
\langle k|\widetilde j\rangle
\widetilde\psi_j.
}
\tag{5.1}
$$

Their moduli are fixed by the two probability vectors:

$$
\boxed{
|\mathcal B_{kj}|^2
=
\frac{p_k r_j}{D}.
}
\tag{5.2}
$$

If

$$
\Delta=\sum_kd_k|k\rangle\langle k|,
\qquad
\Theta=\sum_je_j|\widetilde j\rangle\langle\widetilde j|,
$$

then

$$
\boxed{
\langle\Delta^a\Theta^b\rangle
=
\sum_{k,j}d_k^ae_j^b\mathcal B_{kj}.
}
\tag{5.3}
$$

In particular, the first three phase-sensitive terms in
`TwoLinePlaquette` depend on the phases of \(\mathcal B_{kj}\), not merely their moduli.

The remaining expectation terms are

$$
\boxed{
\langle\Delta\Theta\Delta\rangle
=
\sum_j e_j
\left|
\langle\widetilde j|\Delta|\psi\rangle
\right|^2,
}
\tag{5.4}
$$

$$
\boxed{
\langle\Theta\Delta\Theta\rangle
=
\sum_k d_k
\left|
\langle k|\Theta|\psi\rangle
\right|^2.
}
\tag{5.5}
$$

Finally,

$$
\boxed{
\begin{aligned}
\operatorname{Tr}(\Delta\Theta\Delta\Theta)
=
\sum_{k,\ell,j,n}
&d_kd_\ell e_je_n\\
&\times
\langle k|\widetilde j\rangle
\langle\widetilde j|\ell\rangle
\langle\ell|\widetilde n\rangle
\langle\widetilde n|k\rangle.
\end{aligned}
}
\tag{5.6}
$$

The last quantity is determined by the two bases and the two line probability factors. Equations (5.3)–(5.5), however, contain the unresolved cross-basis phases of the putative state.

This is the first exact two-line compatibility layer not contained in the independently feasible one-line factors.

---

# 6. Uniform averaging does not eliminate the cross-basis phases

Averaging the line shift over all \(s\in\mathbb F_D\) gives

$$
\overline\Delta
=
\mathbb E_s\Delta_{L,s}
=
\frac ID-\sum_kp_k|k\rangle\langle k|.
$$

Similarly,

$$
\overline\Theta
=
\frac ID-\sum_jr_j|\widetilde j\rangle
\langle\widetilde j|.
$$

Consequently,

$$
\begin{aligned}
\mathbb E_{s,t}
\langle\Delta_{L,s}\Theta_{M,t}\rangle
&=
\langle\overline\Delta\,\overline\Theta\rangle\\
&=
\sum_{k,j}
\left(\frac1D-p_k\right)
\left(\frac1D-r_j\right)
\mathcal B_{kj}.
\end{aligned}
\tag{6.1}
$$

The phases of \(\mathcal B_{kj}\) remain. The higher terms in
`TwoLinePlaquette` similarly retain three- and four-point Bargmann data.

Thus neither the four-corner subtraction nor the full uniform average over the two cyclic shifts reduces the two-line condition to the two autocorrelation shadows.

A phase-free two-line contradiction is not obtained.

---

# 7. Exact quotient Fourier support

Let

$$
\mathcal G=\mathbb F_D^{D+1}
$$

be the complete line-character shift group. A coefficient on the label

$$
z=t_zv_{L_z}
$$

acquires the character

$$
\omega^{t_z\kappa_{L_z}}.
$$

The residual

$$
f(\kappa)
=
\operatorname{Tr}(R_\kappa^2-R_\kappa)^2
=
\operatorname{Tr}R_\kappa^4
-2\operatorname{Tr}R_\kappa^3+1
$$

is a Fourier polynomial whose nonconstant characters involve at most four projective lines.

A monomial with labels \(z_1,\ldots,z_r\), \(r\le4\), survives the Weyl trace only when

$$
z_1+\cdots+z_r=0.
$$

Its line-character vector \(q=(q_L)\) therefore satisfies

$$
\sum_Lq_Lv_L=0.
$$

But this is exactly the annihilator condition

$$
q\in\mathcal H^\perp.
$$

Hence

$$
\boxed{
\operatorname{supp}\widehat f
\subseteq
\mathcal H^\perp,
}
\tag{7.1}
$$

and every nonconstant Fourier character is supported on three or four projective lines. A nontrivial relation on only one or two distinct projective lines is impossible.

---

# 8. The zero set and Hamming gap are harmonically compatible

Take the standard projective generators

$$
v_\infty=(0,1),
\qquad
v_0=(1,0),
\qquad
v_a=(1,a)
\quad(a\in\mathbb F_D^\times).
$$

For \(\kappa\in\mathcal G\), define

$$
r_a(\kappa)
=
\kappa_a-\kappa_0-a\kappa_\infty.
$$

For a global character \(\kappa(g)\), one has

$$
\kappa_a=\kappa_0+a\kappa_\infty,
$$

so

$$
\mathcal H
=
\{\kappa:r_a(\kappa)=0\ \forall a\ne0\}.
$$

Now define the explicit function

$$
\boxed{
F_{\rm model}(\kappa)
=
\frac{2}{D-1}
\sum_{a\in\mathbb F_D^\times}
\left[
1-\mathbf1_{\{r_a(\kappa)=0\}}
\right].
}
\tag{8.1}
$$

It has the following exact properties.

### Nonnegativity and global bound

$$
0\le F_{\rm model}\le2.
$$

### Exact zero set

$$
F_{\rm model}(\kappa)=0
\iff
\kappa\in\mathcal H.
$$

### Hamming-one boundary

For \(s\ne0\),

$$
F_{\rm model}(h+se_a)=\frac2{D-1}
\quad(a\ne0),
$$

while

$$
F_{\rm model}(h+se_0)
=
F_{\rm model}(h+se_\infty)=2.
$$

Since

$$
\gamma<\frac1D,
$$

one has

$$
g_{\rm line}<\frac2D<\frac2{D-1}.
$$

Therefore

$$
F_{\rm model}(h+se_L)>g_{\rm line}
$$

at every Hamming-one boundary point.

### Fourier support

Using

$$
\mathbf1_{\{r=0\}}
=
\frac1D\sum_{\ell\in\mathbb F_D}\omega^{\ell r},
$$

every nonconstant Fourier character in \(F_{\rm model}\) has the form

$$
\ell(e_a-e_0-ae_\infty),
$$

which is supported on exactly three projective lines and belongs to
\(\mathcal H^\perp\).

Thus:

$$
\boxed{
\begin{gathered}
f\ge0,\quad f\le4,\quad
f|_{\mathcal H}=0,\quad
f\ge g_{\rm line}\text{ on the Hamming boundary},\\
\operatorname{supp}\widehat f
\subseteq\{\text{characters on at most four lines}\}
\end{gathered}
}
$$

is not a contradictory collection of properties. The explicit
\(F_{\rm model}\) satisfies the stronger global bound \(F_{\rm model}\le2\) and uses only three-line characters.

Therefore the zero-set/Fourier-support route cannot close the problem without exploiting the actual frozen coefficients of \(f\).

---

# 9. Audit of the doubled difference-frame identity

Define

$$
U_a=W_a\otimes\overline{W_a},
\qquad
S_A=\sum_{a\in A}U_a.
$$

The doubled Weyl cocycles cancel, so

$$
U_aU_b^*=U_{a-b}.
$$

Hence

$$
\begin{aligned}
S_AS_A^*
&=
\sum_{a,b\in A}U_{a-b}\\
&=
mI+\sum_{g\in\Gamma}U_g,
\end{aligned}
$$

because the ordered nonzero differences of \(A\) are distinct. Therefore

$$
\boxed{
K_\Gamma=S_AS_A^*-mI.
}
\tag{DifferenceFrame}
$$

For

$$
\zeta=\psi\otimes\overline\psi,
$$

one has

$$
\langle\zeta|U_g|\zeta\rangle
=
|\langle\psi|W_g|\psi\rangle|^2.
$$

Consequently,

$$
\boxed{
m+\mathcal F_\Gamma(\psi)
=
\|S_A^*\zeta\|^2.
}
\tag{9.1}
$$

Thus PW10 is equivalent to

$$
\boxed{
\|S_A^*(\psi\otimes\overline\psi)\|^2
\le m+10
\quad\forall\psi.
}
\tag{9.2}
$$

## 9.1 Reshaped form

Let

$$
\rho=|\psi\rangle\langle\psi|,
\qquad
\rho_a=W_a^*\rho W_a.
$$

With column vectorization,

$$
\psi\otimes\overline\psi=|\rho^{\mathsf T}\rangle\rangle.
$$

Therefore

$$
S_A^*\zeta
=
\left|
\left(\sum_{a\in A}\rho_a\right)^{\mathsf T}
\right\rangle\rangle,
$$

and

$$
\boxed{
m+\mathcal F_\Gamma(\psi)
=
\operatorname{Tr}
\left(\sum_{a\in A}\rho_a\right)^2.
}
\tag{9.3}
$$

This recovers exactly the previously audited orbit-Gram and channel-purity formulation. The algebraic factorization `DifferenceFrame` is correct, but by itself gives no stronger product-state upper bound.

The remaining product restriction is that all \(\rho_a\) are conjugates of the same rank-one projector. The unrestricted norm of \(S_A\), Bell eigenvalue counting, and the already passed magnitude, parity, small-Gram, and stabilizer tests do not control that constraint.

---

# 10. Earliest remaining gap

The exact situation is now:

1. Every frozen line shadow has a strictly positive factor.
2. A physical lift would have a zero residual on the global-character subgroup \(\mathcal H\).
3. Every Hamming-one neighbor has the explicit residual gap

   $$
   f\ge g_{\rm line}.
   $$
4. The two-line four-corner residual is known exactly.
5. Its first unresolved terms are the cross-basis Bargmann amplitudes

   $$
   \mathcal B_{kj}
   =
   \overline{\psi_k}
   \langle k|\widetilde j\rangle
   \widetilde\psi_j.
   $$
6. Uniform line-shift averaging does not eliminate those phases.
7. The guaranteed zero set, Hamming gap, Fourier support, nonnegativity, and global boundedness are harmonically compatible, by the explicit model (8.1).
8. The direct doubled-frame factorization returns exactly to the product-conjugate orbit problem and does not produce a new constant-\(10\) bound.

Thus the first missing statement is now a genuinely two-dimensional compatibility theorem:

> Determine whether the independently feasible line probability factors can arise from one vector \(\psi\) whose cross-basis Bargmann tensors satisfy `TwoLinePlaquette` simultaneously for every pair of stabilizer lines—and ultimately make all MUB residuals vanish.

No such vector is constructed.

No phase-free contradiction is proved.

No exact physical vector with \(\mathcal F_\Gamma>10\) is exhibited.

Therefore \(x^{(10)}\) remains a nonphysical pseudo-candidate of unresolved liftability, PW10 remains open, and the finite \(r=2\) low-\(A\) gate remains open.

---

# VERIFIED

* `SingleLineSOS`, including the diagonal sign and ordered off-diagonal multiplicity.
* The line Parseval identity

  $$
  \sum_kd_k^2
  =
  \frac2D\sum_{t\ne0}x_{tv_L}
  \left(1-\cos\frac{2\pi st}{D}\right).
  $$
* The lower bound \(\sum_kd_k^2\ge2\gamma\).
* The exact conditional line gap

  $$
  f_L(s)\ge
  2\gamma(1-2\sqrt{3/D})^2.
  $$
* The numerical enclosure

  $$
  g_{\rm line}
  =
  2.1241767045114586\ldots\times10^{-18}.
  $$
* The global-character subgroup has size \(D^2\).
* The same line gap holds at every Hamming-one neighbor of every point in that subgroup.
* The exact two-line residual decomposition (4.1).
* `TwoLinePlaquette`.
* The cross-basis Bargmann representations (5.1)–(5.6).
* The actual residual Fourier support lies in \(\mathcal H^\perp\) and uses at most four projective lines.
* `DifferenceFrame`.
* The exact product-conjugate identity (9.1).

# CORRECTED

* A two-line average does not eliminate the unresolved phases: even

  $$
  \mathbb E_{s,t}\langle\Delta_{L,s}\Theta_{M,t}\rangle
  $$

  retains the Bargmann amplitudes.
* The guaranteed zero subgroup and its Hamming-one boundary are insufficient as a harmonic obstruction, even when combined with nonnegativity, a global bound, and at-most-four-line Fourier support.
* `DifferenceFrame` is an exact factorization, but not a stronger bound than the orbit-channel formulation.

# DISPROVED

* Any proposed contradiction based only on:

  $$
  \mathcal H\text{-invariance}
  +\mathcal H\text{ zeros}
  +\text{Hamming-one gap}
  +\text{at-most-four-line Fourier support}
  +0\le f\le4.
  $$

  The explicit \(F_{\rm model}\) satisfies all of these structural properties.
* Any claim that unweighted uniform averaging of the two-line plaquette produces a magnitude-only expression.

# NECESSARY-ONLY

* `SingleLineGap`, conditional on a physical lift.
* `TwoLinePlaquette`.
* The full family of cross-basis Bargmann compatibility equations.
* The quotient Fourier-support restrictions.
* The product-conjugate constraint in `DifferenceFrame`.

# EQUIVALENT

* PW10 and

  $$
  \|S_A^*(\psi\otimes\overline\psi)\|^2\le m+10.
  $$
* PW10 and

  $$
  \operatorname{Tr}\left(\sum_{a\in A}W_a^*\rho W_a\right)^2
  \le m+10
  \quad(\rho\text{ pure}).
  $$

# OPEN

* Simultaneous two-line Bargmann compatibility for the independently feasible line factors.
* Existence of phases for \(x^{(10)}\) with \(C(\alpha)=1\).
* A uniform residual gap excluding every such phase assignment.
* A physical vector with \(\mathcal F_\Gamma>10\).
* \(x^{(10)}\) as a physically liftable candidate.
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first new claim requiring independent verification is the exact mixed four-corner identity `TwoLinePlaquette`, together with the quotient no-go polynomial \(F_{\rm model}\).

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-20-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-20-local-audit.md bytes=6288 sha256=7bd41f77277e250c7b5c747453782183ea75aa06ebc5f6fbe62b046612610188 -->

# Round 20 local audit

- Audit completed (UTC): `2026-09-13T04:45:34Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-20-response.md`
- Web-response SHA-256:
  `1bf725e86a5e33c84e8c7cc72d42447d8baa3398546e28ccf507cdc27710f5f9`
- Browser completion indicator: `Worked for 11m 37s`
- Capture equality: the browser response-copy payload, the TextEdit plain-text
  capture, the artifact copy, and the output copy are exactly equal.  Each
  UTF-8 Markdown copy has `20,157` Unicode characters, `20,169` bytes, and
  `1,138` newline characters.

## Verdict

Round 20 does **not** close PW10.  It establishes a useful conditional
single-line residual gap, gives a correct universal two-line plaquette
expansion, identifies exact quotient symmetries, and verifies the product-
vector difference-frame identity.  None of these results constructs phases
for the frozen magnitudes or excludes every such phase choice.

The exact current status is therefore

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

The physical lift of `x^(10)` and the finite `r=2`, low-`A` gate remain open.
In particular, `x^(10)` is a pseudo-candidate of **unresolved physical
liftability**; it has not been proved nonphysical.

## Exact single-line slice

Assume conditionally that the unshifted reconstruction is a rank-one
projector `P`.  Shifting one stabilizer line gives `R_s=P+Delta_s`, where in
that line's eigenbasis

\[
q_k=p_{k-s},\qquad d_k=q_k-p_k.
\]

The independently checked exact sum of squares is

\[
\boxed{
f_L(s)=
\sum_kd_k^2(1-p_k-q_k)^2
+\sum_{k\ne j}p_kp_j(d_k+d_j)^2.
}
\]

Using the frozen line-purity bound and the exact coefficient floor

\[
\gamma=
\frac{D(m-11)-10m}{D(D+1)(m-1)},
\]

every nonzero one-line shift obeys

\[
\boxed{
f_L(s)\ge
2\gamma\left(1-2\sqrt{3/D}\right)^2
=2.1241767045114586038878\ldots\times10^{-18}>0.
}
\]

This is pointwise and phase-free, but conditional on the existence of the
unshifted physical lift.  It constrains the Hamming-one boundary of the zero
set; it does not contradict the `D^2` globally displaced physical copies.

## Two-line plaquette

For perturbations `X` and `Y` supported on two distinct stabilizer lines,

\[
R^2-R=H_X+H_Y+XY+YX.
\]

The exact cross term is

\[
\begin{aligned}
 f(X+Y)-f(X)-f(Y)
={}&4\operatorname{Tr}(PX)\operatorname{Tr}(PY)
 -4\operatorname{Re}\operatorname{Tr}(PXY)\\
&+8\operatorname{Re}\operatorname{Tr}(PX^2Y+PXY^2)\\
&+4\operatorname{Tr}(PXYX+PYXY)
 +4\operatorname{Tr}(X^2Y^2)+2\operatorname{Tr}(XYXY).
\end{aligned}
\]

Mutual unbiasedness gives

\[
\operatorname{Tr}(X^2Y^2)
=\frac1D\operatorname{Tr}(X^2)\operatorname{Tr}(Y^2),
\]

but it does not similarly remove the alternating word
`Tr(XYXY)` or the terms containing `P`.  Those retain cross-basis
Kirkwood--Dirac and Bargmann phase data.

The response correctly displays these unresolved terms.  Its later claim
that the **full uniform average over both cyclic shifts** still retains phase
dependence is not established: it explicitly averages only one component
and says the higher terms behave similarly, without calculating the full
plaquette sum or excluding cancellation among all terms.  That no-go claim
is therefore **underived**, not accepted.

## Quotient zero set and the model limitation

For global character shifts

\[
\kappa(g)_L=[g,v_L],
\]

Weyl conjugation gives

\[
R_{\kappa+\kappa(g)}=W_gR_\kappa W_g^*,
\qquad
f(\kappa+\kappa(g))=f(\kappa).
\]

The subgroup `H` has exactly `D^2` elements.  Conditional on a physical
lift, the residual vanishes on `H`, while every nontrivial Hamming-one coset
has the same explicit `SingleLineGap` lower bound.

The response's generic quotient polynomial

\[
F_{\rm model}(\kappa)
=\frac2{D-1}\sum_{a\ne0}{\bf1}\{r_a\ne0\},
\qquad
r_a=\kappa_a-\kappa_0-a\kappa_\infty,
\]

does have zero set exactly `H`, Hamming-one boundary at least `2/(D-1)`,
range at most `2`, and three-line Fourier support.  Exhaustive checks at
`D=3,5` confirm these properties.  It shows that this **coarse package of
properties alone** cannot force a larger residual.  It does not use or test
the actual frozen coefficients, so it does not prove that every quotient-
Fourier route for the frozen instance must fail.

## Difference frame

With `U_a=W_a tensor conjugate(W_a)` and `S_A=sum_(a in A) U_a`, the Sidon
difference property gives the exact identity

\[
\boxed{K_\Gamma=S_AS_A^*-mI.}
\]

For `zeta=psi tensor conjugate(psi)`,

\[
\mathcal F_\Gamma(\psi)
=\|S_A^*\zeta\|^2-m.
\]

Thus PW10 is the product-vector estimate

\[
\|S_A^*(\psi\otimes\bar\psi)\|^2\le m+10.
\]

This reformulation is correct.  An unrestricted operator-norm bound loses
the rank-one vectorization constraint and supplies no closure by itself.

## Independent verification record

- `work/round-20-independent-single-line-slice.md` — SHA-256
  `8c6ccfd55ed5462cc7343d31f4f0850eac94f4f721ffa72306649c3c38660cd6`
- `work/verify_round20_single_line_slice.py` — SHA-256
  `f58d18f5ade1b5279bc16dd66e37a345a9dd7ae14815e41f248b30f016ae6971`;
  exact frozen arithmetic and small-prime checks at `D=3,5,7`: `PASS`
- `work/round-20-independent-two-line-plaquette.md` — SHA-256
  `68b961dfc3172777fc8ca0eeb8488c23ad50560c97eeac494b46f46ba9303164`
- `work/verify_round20_two_line_plaquette.py` — SHA-256
  `e27e922b2486d4e58501a32b7ab9726169e474e283a96a29d0b75dd59554c88c`;
  matrix checks at `D=3,5,7`: `PASS`
- `work/round-20-independent-quotient-frame.md` — SHA-256
  `f12d7e55c3922a5d98561a7f1668365bfe3ad72d4e232340d73f1b691d59d479`
- `work/verify_round20_quotient_and_frame.py` — SHA-256
  `802058c3dea004ba4080aff8b28a56e8cecacf5c87cbe957ba749eb3e279be88`;
  exact quotient and difference-frame checks at `D=3,5`: `PASS`
- `work/verify_round20_web_response.py` — SHA-256
  `eccecac9feeb5ccce9301a23a38db4820aef606b96d4759cf20f1afff59b51f7`;
  capture, frozen-gap, and quotient-model checks: `PASS`
- All four Python checkers pass `py_compile`.

The first genuinely new Round 20 claim accepted after independent checking
is `SingleLineSOS`, together with its exact conditional frozen gap.  The
full-average no-go and the word `nonphysical` are explicitly rejected at
the current evidence level.

<!-- END HISTORICAL FILE path=outputs/round-20-local-audit.md -->


# ROUND 021

## PROMPT

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-21-prompt-sent.md bytes=10772 sha256=c6632acf5204ff09851670ba86755731d53509bc8dce29c31c386eb8c672d769 -->

# Round 21 — correct the two-line audit and exploit rank-two displacement identities

Continue in this same ordinary Chat conversation, with the same model and
thinking tier and the same canonically frozen finite r=2, low-A gate.  Give a
public, self-contained derivation and no hidden chain-of-thought.  Do not
repeat the Round 8--20 narrative.  Correct the three overstatements below,
audit the new rank-two identities, and then make a genuinely coefficient-
specific attack on the physical lift.

## Exact frozen boundary

Use exactly

\[
m=485165196,
\quad P_0=m+41=485165237,
\quad D=941541228773064677=4P_0^2+1,
\]

\[
M=m(m-1)=235385266924553220,
\qquad
\Gamma=(A-A)\setminus\{0\},
\]

where

\[
A=\{(t_j,t_j^2):0\le j\le P_0-42\},
\qquad
t_j=2P_0j+(j^2\bmod P_0).
\]

The open physical gate is

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10
\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use

\[
W_{(p,q)}|y\rangle=\omega^{p(y+q/2)}|y+q\rangle,
\qquad
W_uW_v=\omega^{[u,v]/2}W_{u+v}.
\]

The exact magnitude pseudo-point is

\[
b_0=1,\qquad b_z=(D+1)^{-1}\quad(z\ne0),
\]

\[
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\qquad
y=\mathbf1_\Gamma+\lambda/D,
\]

\[
x^{(10)}
=b+\frac{10}{M}\left(y-\frac MD b\right).
\]

It is positive, even, self-Fourier, has mass D, passes every audited
magnitude, small-Gram, parity, stabilizer, and line-factor condition, and has
frozen objective strictly above 10.  A physical lift requires phases

\[
\alpha_{-z}=\overline{\alpha_z},
\qquad |\alpha_z|^2=x_z^{(10)},
\qquad
P=\frac1D\sum_z\alpha_zW_z
\]

with P a rank-one projector, equivalently with the full twisted-convolution
idempotence equations.  Excluding this one pseudo-point would still not prove
PW10; a physical lift would disprove PW10.

## Independently audited Round 20 boundary

Conditionally on an unshifted physical lift, a nonzero character shift of one
stabilizer line has the exact phase-free residual sum of squares

\[
f_L(s)
=\sum_kd_k^2(1-p_k-q_k)^2
+\sum_{k\ne j}p_kp_j(d_k+d_j)^2,
\tag{SingleLineSOS}
\]

and hence

\[
\boxed{
f_L(s)\ge
2\gamma\left(1-2\sqrt{3/D}\right)^2
=2.1241767045114586038878\ldots\times10^{-18},
}
\tag{SingleLineGap}
\]

where

\[
\gamma=
\frac{D(m-11)-10m}{D(D+1)(m-1)}.
\]

The global-character subgroup

\[
\mathcal H=\{\kappa(g):g\in\mathbb F_D^2\},
\qquad
\kappa(g)_L=[g,v_L],
\]

has size D^2.  The residual is invariant on its cosets.  Conditional on a
physical lift it is zero on \(\mathcal H\), and every nontrivial Hamming-one
coset has the same SingleLineGap lower bound.

For two distinct lines, with perturbations X and Y, the exact universal
identities independently checked at D=3,5,7 are

\[
R^2-R=H_X+H_Y+XY+YX
\]

and

\[
\begin{aligned}
 f(X+Y)-f(X)-f(Y)
={}&4\operatorname{Tr}(PX)\operatorname{Tr}(PY)
 -4\operatorname{Re}\operatorname{Tr}(PXY)\\
&+8\operatorname{Re}\operatorname{Tr}(PX^2Y+PXY^2)\\
&+4\operatorname{Tr}(PXYX+PYXY)\\
&+4\operatorname{Tr}(X^2Y^2)+2\operatorname{Tr}(XYXY).
\end{aligned}
\tag{TwoLinePlaquette}
\]

Mutual unbiasedness turns

\[
\operatorname{Tr}(X^2Y^2)
=D^{-1}\operatorname{Tr}(X^2)\operatorname{Tr}(Y^2),
\]

but does not by itself remove the alternating or P-containing
Kirkwood--Dirac and Bargmann terms.

The quotient model from Round 20 really has zero set \(\mathcal H\), the
claimed Hamming-one boundary, range at most 2, and three-line Fourier
support.  It is only a generic model matching those coarse properties.  It
does not use the actual frozen coefficients and therefore does not rule out
all coefficient-specific quotient-Fourier attacks.

Finally, with

\[
U_a=W_a\otimes\overline{W_a},
\qquad
S_A=\sum_{a\in A}U_a,
\]

the exact difference-frame identity is

\[
\boxed{K_\Gamma=S_AS_A^*-mI.}
\tag{DifferenceFrame}
\]

For \(\zeta=\psi\otimes\overline\psi\), PW10 is equivalent to

\[
\|S_A^*\zeta\|^2\le m+10.
\]

The unrestricted norm of \(S_A\) loses the product-vector constraint and is
not sufficient.

## Mandatory corrections before the new attack

1. Round 20 did not prove that the full uniform two-line shift average retains
   unknown phases.  It explicitly averaged only one term and asserted that
   the higher terms behave similarly.  Compute the entire average of
   TwoLinePlaquette, including every P-containing and alternating term, with
   the shift domain and normalization stated exactly.  Distinguish averaging
   over all \(s,t\in\mathbb F_D\) from averaging only over nonzero shifts.
   Either obtain a fully derived formula and identify its remaining data, or
   retract the no-go.  Do not infer noncancellation from one summand.

2. The phrase “nonphysical pseudo-candidate of unresolved liftability” was an
   overclaim.  The correct status is: \(x^{(10)}\) is a pseudo-candidate of
   unresolved physical liftability.  No nonphysicality certificate exists.

3. The generic quotient model disproves only an argument based on the coarse
   zero-set, boundary, range, and support package.  It does not test the
   actual frozen Fourier coefficients.  State this narrower conclusion.

## New exact rank-two displacement system to audit

Assume only while deriving necessary consequences that the frozen magnitudes
have a physical lift \(P=|\psi\rangle\langle\psi|\).  For every
\(g\in\mathbb F_D^2\), put

\[
Q_g=W_gPW_g^*,
\qquad
\Delta_g=Q_g-P,
\qquad
x_g=\operatorname{Tr}(PQ_g).
\]

Since \(\Delta_g\) is a traceless Hermitian difference of two rank-one
projectors, it has rank at most two and nonzero eigenvalues
\(\pm\sqrt{1-x_g}\).  Audit the exact matrix identities

\[
\boxed{
\Delta_g^3=(1-x_g)\Delta_g,
\qquad
\Delta_g^4=(1-x_g)\Delta_g^2,
}
\tag{RankTwoPolynomial}
\]

and their trace consequences

\[
\boxed{
\operatorname{Tr}\Delta_g^2=2(1-x_g),\quad
\operatorname{Tr}\Delta_g^3=0,\quad
\operatorname{Tr}\Delta_g^4=2(1-x_g)^2.
}
\tag{RankTwoMoments}
\]

With

\[
\chi_g(z)=\omega^{[g,z]},
\qquad
\beta_z^{(g)}=(\chi_g(z)-1)\alpha_z,
\]

Weyl conjugation proposes

\[
\Delta_g=\frac1D\sum_z\beta_z^{(g)}W_z.
\tag{DisplacementExpansion}
\]

Audit all conjugations, signs, half-symplectic phases, and powers of D in

\[
\boxed{
\frac1{D^2}\sum_{u,v}
\beta_u^{(g)}\beta_v^{(g)}\beta_{-u-v}^{(g)}
\omega^{[u,v]/2}=0
}
\tag{DisplacementCubic}
\]

and, with \(z_4=-z_1-z_2-z_3\),

\[
\boxed{
\frac1{D^3}\sum_{z_1,z_2,z_3}
\left(\prod_{j=1}^4\beta_{z_j}^{(g)}\right)
\omega^{([z_1,z_2]+[z_1+z_2,z_3])/2}
=2(1-x_g)^2.
}
\tag{DisplacementQuartic}
\]

The stronger coefficientwise relation should be

\[
\boxed{
\beta^{(g)}\star\beta^{(g)}\star\beta^{(g)}
=(1-x_g)\beta^{(g)},
}
\tag{CoefficientRankTwo}
\]

where

\[
(a\star b)_z
=\frac1D\sum_u a_u b_{z-u}\omega^{[u,z]/2}.
\]

These identities have been independently checked by direct matrices at
D=3,5,7, but the derivation and their usefulness at the frozen dimension
still require your audit.

## Required coefficient-specific attack

Do not stop after saying that RankTwoPolynomial follows from \(P^2=P\).
The same unknown phase field \(\alpha\) must satisfy CoefficientRankTwo for
every g, and the right sides contain the actual frozen \(x_g^{(10)}\).
Exploit that coupled family.

Proceed in this order:

### 1. Exact weighted coefficient extraction

Expand CoefficientRankTwo fully and use finite-field character orthogonality
to sum or contract it with at least the three natural weights

\[
1_\Gamma(g),\qquad
\lambda_g=\sum_{h\in\Gamma}\omega^{[h,g]},
\qquad
\sum_{a\in A}\omega^{[a,g]}.
\]

If a proposed weight is complex, pair g with -g and state the resulting real
identity.  Also test one or more nonzero Weyl coefficients z, rather than
only taking the trace.  Separate:

- terms fixed entirely by \(x^{(10)}\), \(\lambda\), and the Sidon
  difference counts;
- phase terms that survive;
- terms that are exactly old purity, autocorrelation, cubic, or residual
  identities in disguise.

For any surviving phase sum, derive the strongest valid triangle,
Cauchy--Schwarz, positive-semidefinite, or sum-of-squares bound using the
actual frozen magnitudes.  Evaluate the exact rational or rigorously enclosed
cyclotomic quantities for the frozen tuple.  A formal weighted identity that
still contains unrestricted phases is not an obstruction.

The acceptable outcomes are: an exact contradiction excluding a physical
lift; an exact compatible phase construction; a new rigorously quantified
necessary inequality; or a precise algebraic reduction proving that this
whole weighted rank-two route adds no information beyond a named old
identity.  “It seems equivalent” is not enough.

### 2. Rank-one-input orbit channel

Define

\[
\Phi_A(P)=\sum_{a\in A}W_aPW_a^*.
\]

The ordered-difference property gives

\[
\boxed{
\operatorname{Tr}\Phi_A(P)^2
=m+\sum_{g\in\Gamma}x_g
=m+\mathcal F_\Gamma(\psi).
}
\tag{OrbitPurity}
\]

Use the rank-one input and the exact arithmetic form of A to seek a stronger
moment, principal-minor, or SOS inequality implying

\[
\operatorname{Tr}\Phi_A(P)^2\le m+10.
\]

Equivalently, use the orbit Gram matrix

\[
G_{ab}=\langle\psi|W_a^*W_b|\psi\rangle.
\]

Retain its Weyl cocycles and the fact that every entry comes from one common
rank-one state.  A generic positive-semidefinite Gram bound, the unrestricted
norm of \(S_A\), Bell eigenvalue counting, and the already passed magnitude,
parity, small-Gram, and stabilizer layers are not new.

### 3. Resolve the full two-line average

Use the completed calculation demanded above.  If it becomes phase-free,
evaluate it against the exact frozen line autocorrelations and test whether
it contradicts global-character zeros.  If phases remain, identify a concrete
KD or Bargmann invariant with its exact coefficient and explain why the
available frozen constraints do or do not bound it.  Do not claim a no-go
without showing the whole averaged expression.

## Certificate and verdict discipline

Either prove PW10 by an exact inequality valid for every unit vector, or
disprove it with an exact physical vector or exact symbolic construction
whose objective is strictly above 10.  Rounded numerics, solver labels,
relaxation values, or a pseudo-point are not certificates.

Give one verdict for PW10: PROVED, DISPROVED, or OPEN WITH EARLIEST GAP.  End
with a ledger separating VERIFIED, CORRECTED, DISPROVED, NECESSARY-ONLY,
EQUIVALENT, and OPEN.  State separately:

- the corrected full two-line average;
- RankTwoPolynomial, RankTwoMoments, DisplacementCubic,
  DisplacementQuartic, and CoefficientRankTwo;
- every weighted coefficient extraction and whether it is genuinely new;
- OrbitPurity and any new rank-one-input consequence;
- the physical lift of \(x^{(10)}\);
- \(x^{(10)}\) as an unresolved candidate, PW10, and the finite r=2 gate.

Identify the first genuinely new claim requiring independent verification.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-21-prompt-sent.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-21-response.md bytes=24405 sha256=8b719f8fcebe3298849dcf6b64f25375ad1280e2383fb1dd17c39b4bc750ae7f -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The three mandatory corrections are valid:

1. The complete two-line shift average can be evaluated, and it **does retain** explicit cross-basis Kirkwood–Dirac/Bargmann data. The earlier no-cancellation claim is now justified by the full formula, not by one sample term.
2. \(x^{(10)}\) is a **pseudo-candidate of unresolved physical liftability**. No nonphysicality certificate is known.
3. The quotient model rules out only arguments based on the coarse zero-set/boundary/range/support package. It says nothing conclusive about the actual frozen Fourier coefficients.

The proposed rank-two displacement identities are all correct. Their strongest phase-free full-group contraction is the new exact spectral identity

$$
\boxed{
\operatorname{Tr}R_\alpha^4
=
1+\frac4D\bigl(\operatorname{Tr}R_\alpha^3-1\bigr),
}
\tag{RT4-average}
$$

or equivalently

$$
\boxed{
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2
=
2\left(1-\frac2D\right)
\bigl(1-\operatorname{Tr}R_\alpha^3\bigr).
}
\tag{RT-residual}
$$

However, the full rank-two displacement system has an exact anti-projector symmetry:

$$
P\longmapsto \widetilde P=\frac{2I}{D}-P.
$$

The transformed operator has the same Weyl magnitudes and satisfies every displacement polynomial, while being nonpositive. Consequently, these identities and all their weighted contractions cannot by themselves select the physical branch.

The orbit-channel attack gives the exact frozen upper bound

$$
\mathcal F_\Gamma<\frac{51}{4}=12.75,
$$

but does not reach \(10\).

---

# 1. Correct full two-line shift average

Assume only in this section that an unshifted physical lift exists:

$$
P=|\psi\rangle\langle\psi|.
$$

Let \(L,M\) be two distinct stabilizer lines, with rank-one eigenprojectors

$$
E_k=|k\rangle\langle k|,
\qquad
F_j=|\widetilde j\rangle\langle\widetilde j|.
$$

Put

$$
p_k=\operatorname{Tr}(PE_k),
\qquad
r_j=\operatorname{Tr}(PF_j).
$$

Define the diagonal dephasings

$$
A_L=\sum_kp_kE_k,
\qquad
A_M=\sum_jr_jF_j.
$$

For cyclic shifts \(s,t\in\mathbb F_D\), let

$$
X_s=\sum_k(p_{k-s}-p_k)E_k,
\qquad
Y_t=\sum_j(r_{j-t}-r_j)F_j.
$$

The doubly shifted reconstructed operator is

$$
R_{s,t}=P+X_s+Y_t.
$$

## 1.1 First and second line moments

All expectations in this section are uniform over the full fields:

$$
\mathbb E_s=\frac1D\sum_{s\in\mathbb F_D},
\qquad
\mathbb E_{s,t}=\frac1{D^2}\sum_{s,t}.
$$

Define the cyclic autocorrelations

$$
q^L_a=\sum_kp_kp_{k+a},
\qquad
q^M_a=\sum_jr_jr_{j+a},
$$

and line collision probabilities

$$
c_L=q^L_0=\sum_kp_k^2,
\qquad
c_M=q^M_0=\sum_jr_j^2.
$$

Then

$$
\boxed{
\overline X_L:=\mathbb E_sX_s=\frac ID-A_L,
}
\tag{1.1}
$$

and

$$
\boxed{
V_L:=\mathbb E_sX_s^2
=
A_L^2-\frac2D A_L+\frac{c_L}{D}I.
}
\tag{1.2}
$$

The corresponding formulas hold for \(M\).

For later use define the covariance kernel

$$
\boxed{
C^L_{k\ell}
=
\mathbb E_s
\bigl[(p_{k-s}-p_k)(p_{\ell-s}-p_\ell)\bigr]
=
\frac{q^L_{\ell-k}}D
-\frac{p_k+p_\ell}{D}
+p_kp_\ell.
}
\tag{1.3}
$$

Define the linear map

$$
\boxed{
\mathcal K_L(Z)
=
\sum_{k,\ell}C^L_{k\ell}E_kZE_\ell.
}
\tag{1.4}
$$

Then

$$
\mathbb E_s(X_sZX_s)=\mathcal K_L(Z).
$$

Analogous notation applies to \(M\).

---

## 1.2 Averaging the complete plaquette

Let

$$
H(Z)=Z^2-Z.
$$

The independently audited two-line identity is

$$
\begin{aligned}
&\operatorname{Tr}H(P+X+Y)^2
-\operatorname{Tr}H(P+X)^2
-\operatorname{Tr}H(P+Y)^2\\
={}&
4\operatorname{Tr}(PX)\operatorname{Tr}(PY)
-4\operatorname{Re}\operatorname{Tr}(PXY)\\
&+8\operatorname{Re}\operatorname{Tr}(PX^2Y+PXY^2)\\
&+4\operatorname{Tr}(PXYX+PYXY)\\
&+4\operatorname{Tr}(X^2Y^2)
+2\operatorname{Tr}(XYXY).
\end{aligned}
\tag{1.5}
$$

Averaging every term gives the exact formula

$$
\boxed{
\begin{aligned}
\overline{\mathfrak P}_{L,M}
:={}&
\mathbb E_{s,t}
\bigl[
f_{L,M}(s,t)-f_L(s)-f_M(t)
\bigr]\\
={}&
4\operatorname{Tr}(P\overline X_L)
 \operatorname{Tr}(P\overline X_M)\\
&-4\operatorname{Re}
  \operatorname{Tr}(P\overline X_L\overline X_M)\\
&+8\operatorname{Re}\Bigl[
  \operatorname{Tr}(PV_L\overline X_M)
 +\operatorname{Tr}(P\overline X_LV_M)
 \Bigr]\\
&+4\Bigl[
  \operatorname{Tr}\bigl(P\mathcal K_L(\overline X_M)\bigr)
 +\operatorname{Tr}\bigl(P\mathcal K_M(\overline X_L)\bigr)
 \Bigr]\\
&+4\operatorname{Tr}(V_LV_M)
+2\Xi_{L,M},
\end{aligned}
}
\tag{FullTwoLineAverage}
$$

where

$$
\boxed{
\Xi_{L,M}
=
\sum_{k,\ell,j,n}
C^L_{k\ell}C^M_{jn}
\operatorname{Tr}(E_kF_jE_\ell F_n).
}
\tag{1.6}
$$

Because the two bases are mutually unbiased,

$$
\operatorname{Tr}(V_LV_M)
=
\frac1D\operatorname{Tr}(V_L)\operatorname{Tr}(V_M),
$$

and

$$
\operatorname{Tr}(V_L)
=
2\left(c_L-\frac1D\right).
$$

Thus the fifth line of `FullTwoLineAverage` is phase-free.

---

## 1.3 The terms which retain cross-basis phases

Define the Kirkwood–Dirac amplitudes

$$
\mathcal B_{kj}
=
\operatorname{Tr}(PE_kF_j)
=
\overline{\psi_k}
\langle k|\widetilde j\rangle
\widetilde\psi_j.
$$

Then, for example,

$$
\operatorname{Tr}(P\overline X_L\overline X_M)
=
\sum_{k,j}
\overline x_k\,\overline y_j\,\mathcal B_{kj},
$$

where

$$
\overline x_k=\frac1D-p_k,
\qquad
\overline y_j=\frac1D-r_j.
$$

Likewise,

$$
\operatorname{Tr}\bigl(P\mathcal K_L(\overline X_M)\bigr)
=
\sum_{k,\ell,j}
C^L_{k\ell}\overline y_j
\operatorname{Tr}(PE_kF_jE_\ell).
$$

These three-point amplitudes contain the phases of

$$
\overline{\psi_k}
\langle k|\widetilde j\rangle
\langle\widetilde j|\ell\rangle
\psi_\ell.
$$

Finally, \(\Xi_{L,M}\) contains the fixed basis four-cycles

$$
\operatorname{Tr}(E_kF_jE_\ell F_n)
=
\langle k|\widetilde j\rangle
\langle\widetilde j|\ell\rangle
\langle\ell|\widetilde n\rangle
\langle\widetilde n|k\rangle.
$$

Therefore the **complete** uniform average retains cross-basis phase information. The earlier no-cancellation claim is now fully derived.

## 1.4 Averaging over nonzero shifts

The mixed plaquette vanishes whenever \(s=0\) or \(t=0\). Hence

$$
\boxed{
\frac1{(D-1)^2}
\sum_{\substack{s\ne0\\t\ne0}}
\mathfrak P_{L,M}(s,t)
=
\frac{D^2}{(D-1)^2}
\overline{\mathfrak P}_{L,M}.
}
\tag{1.7}
$$

No additional cancellation occurs by merely deleting the zero shifts.

---

# 2. Rank-two displacement identities

Assume again that

$$
P=|\psi\rangle\langle\psi|
$$

is a physical lift. For \(g\in\mathbb F_D^2\), define

$$
Q_g=W_gPW_g^*,
\qquad
\Delta_g=Q_g-P,
\qquad
x_g=\operatorname{Tr}(PQ_g).
$$

Since \(P,Q_g\) are rank-one projectors,

$$
P Q_g P=x_gP,
\qquad
Q_g P Q_g=x_gQ_g.
$$

Expanding,

$$
\begin{aligned}
(Q_g-P)^3
&=
Q_g-P-Q_gPQ_g+PQ_gP\\
&=
(1-x_g)(Q_g-P).
\end{aligned}
$$

Therefore

$$
\boxed{
\Delta_g^3=(1-x_g)\Delta_g.
}
\tag{RankTwoPolynomial}
$$

Multiplying once more by \(\Delta_g\),

$$
\boxed{
\Delta_g^4=(1-x_g)\Delta_g^2.
}
\tag{2.1}
$$

The nonzero eigenvalues are consequently

$$
\pm\sqrt{1-x_g}.
$$

This gives

$$
\boxed{
\operatorname{Tr}\Delta_g^2=2(1-x_g),
}
$$

$$
\boxed{
\operatorname{Tr}\Delta_g^3=0,
}
$$

and

$$
\boxed{
\operatorname{Tr}\Delta_g^4=2(1-x_g)^2.
}
\tag{RankTwoMoments}
$$

---

# 3. Weyl coefficient form

Write

$$
P=\frac1D\sum_z\alpha_zW_z.
$$

Weyl conjugation gives

$$
W_gW_zW_g^*
=
\omega^{[g,z]}W_z.
$$

Thus, with

$$
\chi_g(z)=\omega^{[g,z]},
\qquad
\beta_z^{(g)}=(\chi_g(z)-1)\alpha_z,
$$

one has

$$
\boxed{
\Delta_g
=
\frac1D\sum_z\beta_z^{(g)}W_z.
}
\tag{DisplacementExpansion}
$$

No half-symplectic phase appears in conjugation; it cancels between the two Weyl multiplications.

---

## 3.1 Cubic trace

For an arbitrary coefficient field \(a\),

$$
R(a)=\frac1D\sum_za_zW_z
$$

satisfies

$$
\operatorname{Tr}R(a)^3
=
\frac1{D^2}
\sum_{u,v}
a_ua_va_{-u-v}\omega^{[u,v]/2}.
$$

Applying this to \(\beta^{(g)}\) and using
\(\operatorname{Tr}\Delta_g^3=0\) gives

$$
\boxed{
\frac1{D^2}
\sum_{u,v}
\beta_u^{(g)}
\beta_v^{(g)}
\beta_{-u-v}^{(g)}
\omega^{[u,v]/2}
=0.
}
\tag{DisplacementCubic}
$$

---

## 3.2 Quartic trace

Let

$$
z_4=-z_1-z_2-z_3.
$$

Sequential Weyl multiplication gives the phase

$$
\omega^{
([z_1,z_2]+[z_1+z_2,z_3])/2
}.
$$

The final multiplication by \(W_{z_4}\) contributes no further phase because

$$
[z_1+z_2+z_3,z_4]=0.
$$

Therefore

$$
\boxed{
\begin{aligned}
\frac1{D^3}
\sum_{z_1,z_2,z_3}
\left(\prod_{j=1}^4\beta_{z_j}^{(g)}\right)
\omega^{
([z_1,z_2]+[z_1+z_2,z_3])/2
}
=
2(1-x_g)^2.
\end{aligned}
}
\tag{DisplacementQuartic}
$$

All powers of \(D\) are correct.

---

## 3.3 Coefficientwise rank-two relation

Define twisted convolution by

$$
(a\star b)_z
=
\frac1D
\sum_u
a_ub_{z-u}\omega^{[u,z]/2}.
$$

Then

$$
R(a)R(b)=R(a\star b).
$$

Consequently `RankTwoPolynomial` is equivalent coefficientwise to

$$
\boxed{
\beta^{(g)}\star\beta^{(g)}\star\beta^{(g)}
=
(1-x_g)\beta^{(g)}.
}
\tag{CoefficientRankTwo}
$$

---

# 4. A phase-free cross-displacement Gram consequence

For any \(g,h\),

$$
\begin{aligned}
\operatorname{Tr}(\Delta_g\Delta_h)
&=
\operatorname{Tr}(Q_gQ_h)
-\operatorname{Tr}(Q_gP)
-\operatorname{Tr}(PQ_h)
+\operatorname{Tr}P\\
&=
\boxed{
1-x_g-x_h+x_{h-g}.
}
\end{aligned}
\tag{4.1}
$$

Thus the matrix

$$
K_{g,h}=1-x_g-x_h+x_{h-g}
$$

must be positive semidefinite.

For the present pseudo-magnitude this gives no new obstruction. Indeed, the circulant matrix

$$
X_{g,h}=x_{h-g}
$$

has Fourier eigenvalues \(Dx_z\ge0\), by self-Fourier symmetry. Moreover,

$$
K_{g,h}
=
X_{g,h}-X_{g,0}-X_{0,h}+X_{0,0},
$$

so \(K\) is the Gram matrix obtained by centering the vectors represented by \(X\). Hence \(K\succeq0\) follows already from positivity and self-Fourier symmetry of \(x^{(10)}\).

This is an exact reduction showing that the first phase-free cross-\(g\) consequence adds no information.

---

# 5. Full-group average of the quartic displacement identity

This is the strongest new phase-free contraction obtained from the rank-two family.

Let

$$
R=R_\alpha,
\qquad
Q_g=W_gRW_g^*,
\qquad
C=\operatorname{Tr}R^3,
\qquad
R_4=\operatorname{Tr}R^4,
$$

and

$$
S_2=\sum_zx_z^2.
$$

Assume the coefficient magnitudes are self-Fourier, so

$$
\operatorname{Tr}(RQ_g)=x_g.
$$

Average over all \(D^2\) displacements.

The expansion

$$
\begin{aligned}
\operatorname{Tr}(Q_g-R)^4
={}&
2R_4
-4\operatorname{Tr}(Q_g^3R)
-4\operatorname{Tr}(Q_gR^3)\\
&+4\operatorname{Tr}(Q_g^2R^2)
+2\operatorname{Tr}(Q_gRQ_gR)
\end{aligned}
$$

gives the following averages.

Weyl twirling yields

$$
\mathbb E_g\operatorname{Tr}(Q_g^3R)
=
\mathbb E_g\operatorname{Tr}(Q_gR^3)
=
\frac CD,
$$

and

$$
\mathbb E_g\operatorname{Tr}(Q_g^2R^2)=\frac1D.
$$

For the alternating term, Weyl expansion gives

$$
\begin{aligned}
\mathbb E_g\operatorname{Tr}(Q_gRQ_gR)
&=
\frac1{D^3}
\sum_{u,v}
x_ux_v\omega^{[u,v]}\\
&=
\frac{S_2}{D^2},
\end{aligned}
$$

because self-Fourier symmetry gives

$$
\sum_vx_v\omega^{[u,v]}=Dx_u.
$$

Therefore

$$
\boxed{
\mathbb E_g\operatorname{Tr}\Delta_g^4
=
2R_4-\frac{8C}{D}
+\frac4D+\frac{2S_2}{D^2}.
}
\tag{5.1}
$$

On the other hand, `RankTwoMoments` gives

$$
\begin{aligned}
\mathbb E_g\operatorname{Tr}\Delta_g^4
&=
2\mathbb E_g(1-x_g)^2\\
&=
2-\frac4D+\frac{2S_2}{D^2}.
\end{aligned}
$$

Cancelling the \(S_2\) terms yields

$$
\boxed{
R_4
=
1+\frac4D(C-1).
}
\tag{RT4-average}
$$

Equivalently,

$$
\boxed{
\operatorname{Tr}(R^2-R)^2
=
2\left(1-\frac2D\right)(1-C).
}
\tag{RT-residual}
$$

This is a genuinely global necessary identity for any phase field satisfying every rank-two displacement polynomial.

It does not close the lift problem.

---

# 6. Exact anti-projector symmetry

The rank-two displacement family cannot distinguish positivity from the following anti-projector branch.

Given a rank-one projector \(P\), define

$$
\boxed{
\widetilde P=\frac{2I}{D}-P.
}
\tag{6.1}
$$

Then

$$
\operatorname{Tr}\widetilde P=1,
\qquad
\operatorname{Tr}\widetilde P^2=1.
$$

Its Weyl coefficients are

$$
\widetilde\alpha_0=1,
\qquad
\widetilde\alpha_z=-\alpha_z
\quad(z\ne0).
$$

Thus it has exactly the same magnitude profile:

$$
|\widetilde\alpha_z|^2=|\alpha_z|^2.
$$

Moreover,

$$
\widetilde Q_g
=
\frac{2I}{D}-Q_g,
$$

so

$$
\widetilde\Delta_g
=
\widetilde Q_g-\widetilde P
=
-\Delta_g.
$$

Consequently,

$$
\widetilde\Delta_g^3
=
(1-x_g)\widetilde\Delta_g,
$$

and all cubic, quartic, coefficientwise, and weighted rank-two identities remain valid.

The eigenvalues of \(\widetilde P\) are

$$
-\frac{D-2}{D}
\quad\text{once},
\qquad
\frac2D
\quad\text{\(D-1\) times}.
$$

Thus

$$
\boxed{
\operatorname{Tr}\widetilde P^3
=
-\frac{D^2-6D+4}{D^2},
}
$$

and

$$
\boxed{
\operatorname{Tr}\widetilde P^4
=
\frac{D^3-8D^2+24D-16}{D^3}.
}
$$

These satisfy `RT4-average` exactly.

Therefore:

$$
\boxed{
\text{the entire rank-two displacement system alone cannot select the positive physical branch.}
}
\tag{6.2}
$$

This does not show that \(x^{(10)}\) has either branch. It shows that weighted rank-two identities cannot, by themselves, be a positivity certificate.

---

# 7. Exact weighted coefficient extraction

Let

$$
V=\mathbb F_D^2,
\qquad
\chi_g(r)=\omega^{[g,r]}.
$$

For a weight \(w:V\to\mathbb C\), define the unnormalized symplectic Fourier transform

$$
\widehat w(r)=\sum_gw(g)\chi_g(r).
$$

For fixed output coefficient \(z\), put

$$
\Omega_z(u,v)
=
\omega^{([u,v]+[u+v,z])/2}.
$$

Expanding `CoefficientRankTwo`, multiplying by \(w(g)\), and summing over \(g\) gives

$$
\boxed{
\begin{aligned}
\frac1{D^2}
\sum_{u,v}
&\alpha_u\alpha_v\alpha_{z-u-v}
\Omega_z(u,v)\,
\mathcal K_w(z;u,v)\\
&=
\alpha_z\,\mathcal R_w(z),
\end{aligned}
}
\tag{7.1}
$$

where

$$
\boxed{
\begin{aligned}
\mathcal K_w(z;u,v)
={}&
\widehat w(z)
-\widehat w(u+v)
-\widehat w(z-u)
-\widehat w(z-v)\\
&+\widehat w(u)
+\widehat w(v)
+\widehat w(z-u-v)
-\widehat w(0),
\end{aligned}
}
\tag{7.2}
$$

and

$$
\boxed{
\mathcal R_w(z)
=
\widehat w(z)-\widehat w(0)
-\widehat{wx}(z)+\widehat{wx}(0).
}
\tag{7.3}
$$

At \(z=0\), the right side vanishes and one recovers a weighted cubic trace identity. For \(z\ne0\), equation (7.1) is a genuine nonzero Weyl-coefficient constraint.

---

## 7.1 Weight \(w=\mathbf1_\Gamma\)

Here

$$
\widehat w(r)=\lambda_r.
$$

Define

$$
\mu_\Gamma(r)
=
\sum_{g\in\Gamma}x_g\omega^{[g,r]},
\qquad
\mathcal O_\Gamma=\sum_{g\in\Gamma}x_g.
$$

Then

$$
\boxed{
\mathcal R_{\mathbf1_\Gamma}(z)
=
\lambda_z-M-\mu_\Gamma(z)+\mathcal O_\Gamma.
}
\tag{7.4}
$$

Everything on the right is fixed by the frozen magnitudes and frozen difference set. The left remains a cubic phase sum.

---

## 7.2 Weight \(w=\lambda\)

Character orthogonality gives

$$
\boxed{
\widehat\lambda(r)=D^2\mathbf1_\Gamma(r).
}
\tag{7.5}
$$

Self-Fourier symmetry of \(x\) gives

$$
\boxed{
\widehat{\lambda x}(r)
=
D\sum_{h\in\Gamma}x_{r-h}.
}
\tag{7.6}
$$

Therefore

$$
\boxed{
\begin{aligned}
\mathcal R_\lambda(z)
={}&
D^2\mathbf1_\Gamma(z)\\
&-
D\left[
\sum_{h\in\Gamma}x_{z-h}
-\sum_{h\in\Gamma}x_h
\right].
\end{aligned}
}
\tag{7.7}
$$

The kernel \(\mathcal K_\lambda/D^2\) is the exact seven-term incidence expression obtained by replacing every Fourier transform in (7.2) by \(\mathbf1_\Gamma\).

---

## 7.3 Weight given by the frozen exponential sum

Put

$$
\mathcal S(g)
=
\sum_{a\in A}\omega^{[a,g]}.
$$

Then

$$
\boxed{
\widehat{\mathcal S}(r)=D^2\mathbf1_A(r),
}
\tag{7.8}
$$

and

$$
\boxed{
\widehat{\mathcal Sx}(r)
=
D\sum_{a\in A}x_{r-a}.
}
\tag{7.9}
$$

Hence

$$
\boxed{
\begin{aligned}
\mathcal R_{\mathcal S}(z)
={}&
D^2\bigl(\mathbf1_A(z)-1\bigr)\\
&-
D\left[
\sum_{a\in A}x_{z-a}
-\sum_{a\in A}x_{-a}
\right].
\end{aligned}
}
\tag{7.10}
$$

Because \(\mathcal S\) is complex, the equation at \(z\) should be paired with the conjugate equation at \(-z\). Equivalently one may use the two real weights

$$
2\operatorname{Re}\mathcal S,
\qquad
2\operatorname{Im}\mathcal S.
$$

---

# 8. Testing a concrete nonzero coefficient

Take

$$
z_\star=(0,1).
$$

It is not in \(A\): the only point of \(A\) with first coordinate \(0\) is \((0,0)\).

It is not in \(\Gamma\): every nonzero ordered difference has first coordinate \(t_a-t_b\ne0\).

Thus

$$
\mathbf1_A(z_\star)=\mathbf1_\Gamma(z_\star)=0.
$$

The exact fixed right sides become

$$
\boxed{
\mathcal R_\lambda(z_\star)
=
-D\left[
\sum_{h\in\Gamma}x_{z_\star-h}
-\mathcal O_\Gamma
\right],
}
\tag{8.1}
$$

and

$$
\boxed{
\mathcal R_{\mathcal S}(z_\star)
=
-D^2
-
D\left[
\sum_{a\in A}x_{z_\star-a}
-\sum_{a\in A}x_{-a}
\right].
}
\tag{8.2}
$$

These are exact frozen coefficient constraints.

## 8.1 Phase-free Cauchy bounds

Let

$$
T_z
=
\sum_{u,v}
x_ux_vx_{z-u-v}.
$$

Since \(0\le x\le1\) and \(\sum x=D\),

$$
T_z\le D^2.
$$

For the \(\lambda\)-weight at \(z_\star\), the incidence kernel contains six signed indicators. Each associated affine map
\((u,v)\mapsto r\) has \(D^2\) preimages for every \(r\), so

$$
\sum_{u,v}
\left|\frac{\mathcal K_\lambda}{D^2}\right|^2
\le36MD^2.
$$

Cauchy–Schwarz therefore gives

$$
\boxed{
|\alpha_{z_\star}\mathcal R_\lambda(z_\star)|
\le6D^2\sqrt M.
}
\tag{8.3}
$$

The frozen point satisfies

$$
x_z\le
U=
\frac{11}{D+1}+\frac{10}{M},
$$

and

$$
MU
=
10+\frac{11M}{D+1}
<
\frac{51}{4}.
$$

Since \(z_\star\notin\Gamma\), both sums in (8.1) lie in
\([0,MU]\). Hence

$$
|\alpha_{z_\star}\mathcal R_\lambda(z_\star)|
<
\frac{51}{4}D.
$$

This is enormously below the Cauchy envelope (8.3); no contradiction results.

For the centered frozen exponential sum

$$
\widetilde{\mathcal S}
=
\mathcal S-1
=
\sum_{a\in A\setminus\{0\}}\omega^{[a,g]},
$$

the analogous estimate is

$$
\boxed{
|\alpha_{z_\star}\mathcal R_{\widetilde{\mathcal S}}(z_\star)|
\le
6D^2\sqrt{m-1},
}
\tag{8.4}
$$

whereas the fixed right side has magnitude at most

$$
D(m-1)U<61(m-1).
$$

Again the phase-free bound is far too weak.

For \(w=\mathbf1_\Gamma\), the exact estimate

$$
\sum_{u,v}|\mathcal K_w|^2
\le
8D^4\bigl(\lambda_z^2+M^2+6M\bigr)
$$

gives

$$
\boxed{
|\alpha_z\mathcal R_{\mathbf1_\Gamma}(z)|
\le
\sqrt8\,D
\sqrt{\lambda_z^2+M^2+6M}
<4DM,
}
\tag{8.5}
$$

whereas the frozen right side is smaller than \(3M\).

Thus all three requested weighted extractions are exact and coefficient-specific, but their strongest immediate phase-free Cauchy bounds do not approach a contradiction.

## 8.2 Algebraic status

Every weighted equation is a linear combination of `CoefficientRankTwo`. Under

$$
P\mapsto\frac{2I}{D}-P,
$$

one has

$$
\beta^{(g)}\mapsto-\beta^{(g)}.
$$

Both sides of every cubic coefficient equation change sign. Hence every weighted extraction is invariant under the pure/anti-pure ambiguity.

This proves that the weighted rank-two route, without an additional positivity input, cannot distinguish the physical branch.

---

# 9. Rank-one orbit channel

Define

$$
\Phi_A(P)
=
\sum_{a\in A}W_aPW_a^*.
$$

Let

$$
Q_a=W_aPW_a^*.
$$

Then

$$
\operatorname{Tr}\Phi_A(P)=m.
$$

Moreover,

$$
\begin{aligned}
\operatorname{Tr}\Phi_A(P)^2
&=
\sum_{a,b}\operatorname{Tr}(Q_aQ_b)\\
&=
m+\sum_{a\ne b}
|\langle\psi|W_a^*W_b|\psi\rangle|^2.
\end{aligned}
$$

Ordered-difference injectivity gives

$$
\boxed{
\operatorname{Tr}\Phi_A(P)^2
=
m+\sum_{g\in\Gamma}x_g
=
m+\mathcal F_\Gamma(\psi).
}
\tag{OrbitPurity}
$$

Equivalently, if

$$
G_{ab}
=
\langle\psi|W_a^*W_b|\psi\rangle,
$$

then

$$
\operatorname{Tr}G^2
=
m+\mathcal F_\Gamma(\psi).
$$

---

## 9.1 The exact frozen entrywise bound

For the pseudo-magnitude \(x^{(10)}\),

$$
x_g\le U
=
\frac{11}{D+1}+\frac{10}{M}
\qquad(g\ne0).
$$

Therefore any physical lift of this magnitude would satisfy

$$
\mathcal F_\Gamma
\le MU
=
10+\frac{11M}{D+1}.
$$

Because

$$
D+1-4M
=
161074851798>0,
$$

one has

$$
\frac{M}{D+1}<\frac14.
$$

Hence

$$
\boxed{
\mathcal F_\Gamma
<
10+\frac{11}{4}
=
\frac{51}{4}.
}
\tag{9.1}
$$

This is the strongest immediate coefficientwise orbit bound, but it is \(2.75\) above the target.

---

## 9.2 Third orbit moment

Since \(\Phi_A(P)\succeq0\),

$$
\operatorname{Tr}\Phi_A(P)^3
\ge
\frac{
\operatorname{Tr}\Phi_A(P)^2{}^2
}{
\operatorname{Tr}\Phi_A(P)
}
=
\frac{(m+\mathcal F_\Gamma)^2}{m}.
\tag{9.2}
$$

On the other hand, expanding its third moment:

* all three orbit labels equal: contribution \(m\);
* exactly two equal: contribution \(3\mathcal F_\Gamma\);
* all distinct: each Bargmann term has magnitude at most \(U^{3/2}\).

Therefore

$$
\operatorname{Tr}\Phi_A(P)^3
\le
m+3\mathcal F_\Gamma
+
m(m-1)(m-2)U^{3/2}.
\tag{9.3}
$$

The exact frozen dimensions satisfy

$$
D>4m^2,
\qquad
D<5M,
$$

so

$$
U<\frac{61}{D}.
$$

Consequently,

$$
m(m-1)(m-2)U^{3/2}
<
\frac{61^{3/2}}8<60.
$$

Combining (9.2)–(9.3) gives

$$
\boxed{
\frac{\mathcal F_\Gamma^2}{m}
-\mathcal F_\Gamma
<60.
}
\tag{9.4}
$$

For the relevant range

$$
0\le\mathcal F_\Gamma<\frac{51}{4}\ll m,
$$

the left side is negative. Thus the third-moment inequality is automatic and gives no improvement over (9.1).

No stronger rank-one-input SOS bound reaching \(10\) is obtained.

---

# 10. Status of the physical lift

The exact new information is:

* the complete two-line average is known and retains cross-basis phase data;
* all rank-two displacement identities are verified;
* their full-group quartic contraction gives `RT4-average`;
* all three requested weighted coefficient extractions are explicit;
* the pure/anti-pure symmetry proves that the rank-two family alone cannot certify positivity;
* the orbit-channel entrywise bound reaches \(12.75\), not \(10\).

No compatible phase field for \(x^{(10)}\) satisfying

$$
R_\alpha^2=R_\alpha
$$

is constructed.

No positive phase-uniform residual gap is proved.

No exact unit vector with

$$
\mathcal F_\Gamma>10
$$

is exhibited.

Accordingly, \(x^{(10)}\) remains a pseudo-candidate of unresolved physical liftability.

---

# Ledger

## VERIFIED

* The complete full-field two-line shift average `FullTwoLineAverage`.
* The exact conversion between full-field and nonzero-shift averages.
* The persistence of cross-basis KD/Bargmann data in the complete average.
* `RankTwoPolynomial`.
* `RankTwoMoments`.
* `DisplacementExpansion`.
* `DisplacementCubic`.
* `DisplacementQuartic`.
* `CoefficientRankTwo`.
* The phase-free displacement Gram kernel

  $$
  1-x_g-x_h+x_{h-g}.
  $$
* The global averaged quartic identity

  $$
  \operatorname{Tr}R^4
  =
  1+\frac4D(\operatorname{Tr}R^3-1).
  $$
* The equivalent averaged residual relation.
* All three weighted coefficient extractions:
  \(\mathbf1_\Gamma\), \(\lambda\), and the frozen exponential sum.
* The concrete nonzero-coefficient test at \(z_\star=(0,1)\).
* `OrbitPurity`.
* The exact frozen upper bound

  $$
  \mathcal F_\Gamma<51/4.
  $$

## CORRECTED

* The earlier full two-line-average no-go is now supported by the complete calculation; previously only one term had been averaged.
* \(x^{(10)}\) is a pseudo-candidate of **unresolved** physical liftability.
* The quotient model excludes only arguments using the coarse structural package; it does not test the frozen coefficients.
* The rank-two displacement system is not a positivity criterion because of the exact anti-projector branch.

## DISPROVED

* Any claim that the rank-two displacement identities alone distinguish a pure projector from

  $$
  2I/D-P.
  $$
* Any claim that their weighted contractions alone certify physical positivity.
* Any claim that the immediate third orbit moment improves the frozen \(51/4\) bound.

## NECESSARY-ONLY

* `FullTwoLineAverage` and all of its KD/Bargmann compatibility terms.
* Every rank-two displacement identity.
* `RT4-average`.
* All three weighted coefficient equations.
* The rank-one orbit-channel moment inequalities.

## EQUIVALENT

For an actual physical lift:

* `CoefficientRankTwo` and the operator identity

  $$
  \Delta_g^3=(1-x_g)\Delta_g;
  $$
* `OrbitPurity` and the orbit-Gram frame potential;
* PW10 and

  $$
  \operatorname{Tr}\Phi_A(P)^2\le m+10.
  $$

## OPEN

* Whether \(x^{(10)}\) has a physical phase lift.
* Whether every phase field with these magnitudes has a positive residual gap.
* Whether the full KD/Bargmann two-line compatibility system is feasible.
* Whether a stronger orbit-channel SOS inequality reaches \(10\).
* PW10 for the exact frozen tuple.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the global displacement-average identity

$$
\boxed{
\operatorname{Tr}R_\alpha^4
=
1+\frac4D\bigl(\operatorname{Tr}R_\alpha^3-1\bigr),
}
$$

together with the exact anti-projector symmetry showing why the complete rank-two displacement family cannot, by itself, select the physical branch.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-21-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-21-local-audit.md bytes=7641 sha256=c9a739067103dd540fcaf4fb6c89270d244e373bb36d9f396d4f484200fd8072 -->

# Round 21 local audit

- Audit completed (UTC): `2026-09-13T05:48:42Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-21-response.md`
- Web-response SHA-256:
  `8b719f8fcebe3298849dcf6b64f25375ad1280e2383fb1dd17c39b4bc750ae7f`
- Browser completion indicator: `Worked for 12m 36s`
- Capture equality: the browser response-copy payload, the artifact copy, and
  the output copy are exactly equal. Each UTF-8 Markdown copy has `24,397`
  Unicode characters, `24,405` bytes, and `1,612` newline characters.

## Verdict

Round 21 does **not** close PW10. It correctly derives the complete
two-line average, the rank-two displacement identities, a global quartic
contraction, the anti-projector symmetry, three weighted coefficient
formulas, and the conditional frozen orbit bound

\[
\mathcal F_\Gamma<\frac{51}{4}.
\]

None constructs a physical phase lift of `x^(10)`, excludes every possible
lift, proves a phase-uniform residual gap, or proves PW10. The exact status is

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

The physical lift of `x^(10)` and the finite `r=2`, low-`A` gate remain open.

## Complete two-line average

The displayed `FullTwoLineAverage` formula is correct. Independent direct
matrix checks at `D=3,5,7` agree with the average of the entire plaquette,
including the covariance terms and the alternating four-cycle. The
nonzero-shift average is exactly `D^2/(D-1)^2` times the all-shift average.

The formula leaves explicit terms such as

\[
\operatorname{Tr}(P\overline X_L\overline X_M),\qquad
\operatorname{Tr}\bigl(P\mathcal K_L(\overline X_M)\bigr),
\]

which are expressed through cross-basis Kirkwood--Dirac and three-point
Bargmann amplitudes. This verifies the narrower statement that the complete
calculation still contains unresolved cross-basis data.

The response's stronger sentence that “no-cancellation is now fully derived”
is not accepted literally. Displaying the combined formula and naming its KD
terms does not prove that the complete expression cannot simplify further on
the physical compatibility locus, nor does it produce a phase obstruction.
No such cancellation theorem is needed for accepting the formula itself.

## Rank-two system and global contraction

For a physical projector `P`, all of the following are correct with the
stated Weyl convention and normalizations:

\[
\Delta_g^3=(1-x_g)\Delta_g,
\qquad
\Delta_g^4=(1-x_g)\Delta_g^2,
\]

the quadratic, cubic, and quartic trace moments, the Weyl expansion of
`Delta_g`, and the coefficientwise twisted-convolution identity. The
phase-free cross-displacement Gram entry

\[
1-x_g-x_h+x_{h-g}
\]

is also correct. For the self-Fourier nonnegative frozen magnitude, its PSD
condition is already inherited from the centered circulant Gram matrix.

Averaging the fourth displacement moment gives

\[
\boxed{
\operatorname{Tr}R^4
=1+\frac4D\bigl(\operatorname{Tr}R^3-1\bigr)
}
\]

and equivalently

\[
\operatorname{Tr}(R^2-R)^2
=2\left(1-\frac2D\right)
\bigl(1-\operatorname{Tr}R^3\bigr).
\]

The Weyl twirls, the alternating-term normalization `S_2/D^2`, and the final
algebra were independently checked on both the projector and anti-projector
branches at `D=3,5`.

## Exact anti-projector symmetry and its scope

The transformation

\[
P\longmapsto \widetilde P=\frac{2I}{D}-P
\]

has trace and purity one, negates every nonzero Weyl coefficient, preserves
all coefficient magnitudes, and sends every displacement to its negative.
The response's eigenvalues and cubic and quartic moments are exact. Hence the
rank-two family and any linear weighted contraction of it cannot serve as a
positivity or pure-versus-anti-pure branch selector.

This symmetry is **not** a no-go theorem for using the uncontracted rank-two
equations to reject this particular frozen magnitude. If those equations
were inconsistent for every phase field with magnitude `x^(10)`, they would
exclude both branches and therefore exclude a physical lift. Round 21 does
not establish either consistency or inconsistency.

## Weighted coefficient extraction

The master kernel `K_w`, right side `R_w`, and all three specializations

\[
w=\mathbf1_\Gamma,\qquad w=\lambda,\qquad
w(g)=\sum_{a\in A}\omega^{[a,g]}
\]

have the correct character signs and powers of `D`. Direct small-prime tests
at `D=3,5` verify the formulas coefficient by coefficient for all output
labels. The claims `z_star=(0,1) notin A` and `z_star notin Gamma` follow from
the strict integer separation of the first coordinates `t_j`.

Two limitations remain:

1. The requested frozen cyclotomic sums at `z_star` were not evaluated.
   They remain symbolic and are replaced by the coarse entrywise cap `U`.
   Thus this is an exact coefficient-specific reformulation, not an exact
   frozen obstruction.
2. The displayed strict simplification

   \[
   \sqrt8\,D\sqrt{\lambda_z^2+M^2+6M}<4DM
   \]

   does not follow from the stated bound `|lambda_z|<=M`. At that envelope,
   the coefficient is

   \[
   4DM\sqrt{1+3/M}>4DM.
   \]

   A sharper estimate for the chosen nonzero `lambda_(z_star)` could repair
   the constant, but none is supplied. This does not change the conclusion:
   either envelope is enormously larger than the fixed right side and gives
   no contradiction.

The lambda- and centered-exponential-sum Cauchy bounds and their frozen
comparisons are otherwise arithmetically correct.

## Orbit channel

`OrbitPurity` is exact. For a hypothetical lift of the frozen magnitude,

\[
x_g\le U=\frac{11}{D+1}+\frac{10}{M}
\]

gives

\[
\mathcal F_\Gamma\le MU
=10+\frac{11M}{D+1}<\frac{51}{4}.
\]

The integer receipt

\[
D+1-4M=161074851798>0
\]

is correct. The third-moment lower and upper bounds, `D>4m^2`, `D<5M`,
`DU<61`, and the strict all-distinct contribution below `60` also check.
After rearrangement they yield only

\[
\frac{\mathcal F_\Gamma^2}{m}-\mathcal F_\Gamma<60,
\]

which is automatic in the relevant range and supplies no improvement.

## Verification receipts

- `work/verify_round21_web_response.py` — SHA-256
  `7ed7f994e35e2e3150982c063a8b8636a9abfa32994b843efa1077a0d336da55`;
  capture, prompt receipt, frozen arithmetic, and unsupported `<4DM` step:
  `PASS` with the limitation detected.
- `work/verify_round21_global_contractions.py` — SHA-256
  `6a32da085811c839fa3485a60751850aa0bc964bc6b6fda9cdd291425a19b77a`;
  anti-projector, global quartic average, weighted master formulas at
  `D=3,5`, and exact frozen inequalities: `PASS`.
- `work/verify_round21_rank_two_displacement.py` — SHA-256
  `03a6dbae1894b5c24d91593fb67177500d9187eb9724efd5c4595f93365d62ad`;
  rank-two displacement identities at `D=3,5,7`: `PASS`.
- `work/verify_round21_two_line_average.py` — SHA-256
  `713a0750b0ebbb82386678420764d7d89498da004178841ec1c3b627063f38a2`;
  complete two-line average at `D=3,5,7`: `PASS`.
- Independent notes:
  `work/round-21-independent-rank-two-displacement.md` — SHA-256
  `e0892fca4b432375d8a5e73a31ab484222ba72cf3b6b16f44d1d97a1a585ecd2`;
  `work/round-21-independent-two-line-average.md` — SHA-256
  `8a91c06a11edb08ede7d32327c490b96923329e960aff187d6f0b474f9286d47`.

All four Python checkers pass `py_compile`.

The first genuinely new Round 21 claim accepted after independent checking
is `RT4-average`, together with the exact anti-projector symmetry. Both are
necessary-only. The earliest unresolved gate remains a physical phase lift
or a phase-uniform exclusion for `x^(10)`; even excluding that one
pseudo-point would still not prove PW10 for all physical magnitudes.

<!-- END HISTORICAL FILE path=outputs/round-21-local-audit.md -->


# ROUND 022

## PROMPT

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-22-prompt-sent.md bytes=8252 sha256=24714161eab119539b29848fd6140e86861e1f65817465e37c740a213a649b99 -->

# Round 22 — break the anti-projector symmetry with centered idempotence

Continue in this same ordinary Chat conversation, with the same model and
thinking tier and the same canonically frozen finite `r=2`, low-`A` gate.
Give a public, self-contained derivation and no hidden chain-of-thought. Do
not repeat the Round 8--21 narrative. First correct the limited Round 21
overstatements listed below, then pursue one orientation-sensitive attack on
the actual physical-lift equation. Do not ask me to choose another branch;
carry the strongest valid branch through yourself.

## Exact frozen boundary

Use exactly

\[
m=485165196,\qquad P_0=m+41=485165237,
\]

\[
D=941541228773064677=4P_0^2+1,
\qquad M=m(m-1)=235385266924553220,
\]

\[
A=\{(t_j,t_j^2):0\le j\le P_0-42\},
\qquad t_j=2P_0j+(j^2\bmod P_0),
\]

\[
\Gamma=(A-A)\setminus\{0\}.
\]

The open physical gate is

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2
\le10
\quad\text{for every unit }\psi.
}
\tag{PW10}
\]

Use

\[
W_{(p,q)}|y\rangle=\omega^{p(y+q/2)}|y+q\rangle,
\qquad
W_uW_v=\omega^{[u,v]/2}W_{u+v}.
\]

The exact magnitude pseudo-point is

\[
b_0=1,\qquad b_z=(D+1)^{-1}\quad(z\ne0),
\]

\[
\lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\qquad y=\mathbf1_\Gamma+\lambda/D,
\]

\[
x^{(10)}
=b+\frac{10}{M}\left(y-\frac MD b\right).
\]

It is positive, even, self-Fourier, has mass `D`, passes all already audited
magnitude, parity, stabilizer, line-factor, and small-Gram tests. Its exact
frozen objective `O_10=sum_(g in Gamma) x_g^(10)` obeys the rigorous bound

\[
\mathcal O_{10}\ge
10+\frac{3357953467987716774306702559357710}
{13431816446658977517442074781790591}
=10.249999952078184\ldots>10.
\]

The decimal is a lower bound, not the exact value of the unevaluated frozen
cyclotomic sum.

Its physical liftability remains unresolved. A physical lift requires

\[
\alpha_0=1,\qquad
\alpha_{-z}=\overline{\alpha_z},\qquad
|\alpha_z|^2=x_z^{(10)},
\]

\[
R_\alpha=\frac1D\sum_z\alpha_zW_z,
\qquad R_\alpha^2=R_\alpha.
\]

A physical lift would disprove PW10. Excluding only this pseudo-point would
not prove PW10 for all physical magnitudes.

## Round 21 results that may be used

The complete two-line shift average formula was independently checked at
`D=3,5,7`; it leaves explicit cross-basis KD/Bargmann terms. The rank-two
displacement polynomial, its coefficientwise version, the weighted kernel,
and

\[
\operatorname{Tr}R^4
=1+\frac4D(\operatorname{Tr}R^3-1)
\tag{RT4-average}
\]

were independently checked. The exact transformation

\[
R\longmapsto\frac{2I}{D}-R
\]

preserves the nonzero Weyl magnitudes and the entire rank-two displacement
family, so that family is not a positivity or branch selector. The frozen
orbit entrywise bound reaches only

\[
\mathcal F_\Gamma<51/4.
\]

## Mandatory Round 21 corrections

State these before the new attack.

1. `FullTwoLineAverage` is verified and explicitly contains unresolved KD
   data. That alone does not prove a theorem that the complete expression
   can never simplify or cancel on the physical compatibility locus. Replace
   “no-cancellation is fully derived” by this narrower statement unless you
   supply an actual noncancellation proof.
2. The displayed step

   \[
   \sqrt8D\sqrt{\lambda_z^2+M^2+6M}<4DM
   \]

   does not follow from `|lambda_z|<=M`; that envelope equals
   `4DM sqrt(1+3/M)>4DM`. Repair it with a proved sharper bound at the stated
   nonzero `z`, or retain the safe envelope. This numerical correction does
   not create a contradiction.
3. The anti-projector symmetry shows that rank-two identities cannot select
   positivity when a solution exists. It does **not** show that the
   uncontracted equations cannot be inconsistent for the particular frozen
   magnitude and thereby exclude it.
4. The Round 21 values called “exact frozen right sides” at
   `z_star=(0,1)` were left as unevaluated cyclotomic sums and then bounded by
   `U`. Label that honestly.

## New branch-breaking identity to audit

Write

\[
\alpha=\delta_0+\beta,\qquad \beta_0=0,
\]

with normalized twisted convolution

\[
(a\star b)_z
=\frac1D\sum_u a_ub_{z-u}\omega^{[u,z]/2}.
\]

The full idempotence equation, unlike the rank-two displacement system,
proposes the exact centered identity

\[
\boxed{
\beta\star\beta
=\frac{D-2}{D}\,\beta+\frac{D-1}{D}\,\delta_0.
}
\tag{CenteredIdempotence}
\]

Equivalently, for every nonzero `z`,

\[
\boxed{
\sum_{u\in\mathbb F_D^2}
\beta_u\beta_{z-u}\omega^{[u,z]/2}
=(D-2)\beta_z.
}
\tag{OrientedCoefficient}
\]

Audit all signs, excluded zero terms, and powers of `D`. Under the
anti-projector transformation, `beta -> -beta`: the left side is unchanged
and the nonzero right side changes sign. Thus this is genuinely
orientation-sensitive.

## Required structured attack

Do not stop after observing that `CenteredIdempotence` is equivalent to
`R^2=R`. Use the actual frozen `Gamma=A-A` structure and proceed in this
order.

### 1. Gamma-restricted trilinear identity

Multiply `OrientedCoefficient` by `conjugate(beta_z)`, sum over
`z in Gamma`, pair inverse labels so every asserted scalar is real, and audit

\[
\boxed{
(D-2)\mathcal F_\Gamma
=\sum_{z\in\Gamma}\sum_u
\overline{\beta_z}\,\beta_u\beta_{z-u}
\omega^{[u,z]/2}.
}
\tag{GammaOriented}
\]

Reindex every `z in Gamma` by its unique ordered pair `z=a-b`, with
`a,b in A`, `a!=b`. Preserve the Weyl cocycle. Determine exactly whether the
result is:

- a genuinely new restricted trilinear form;
- exactly a previously named orbit moment or cubic identity;
- or PW10 itself in disguise.

An “it looks equivalent” statement is not acceptable: give both directions
with all normalizations if claiming equivalence.

### 2. Exact restricted-convolution energy

Square `OrientedCoefficient` and sum over `z in Gamma` to obtain

\[
(D-2)^2\mathcal F_\Gamma
=\sum_{z\in\Gamma}
\left|\sum_u\beta_u\beta_{z-u}
\omega^{[u,z]/2}\right|^2.
\tag{GammaEnergy}
\]

Expand the right side completely. Separate diagonal, collision, and genuine
off-diagonal quadruples using the ordered-difference injectivity of `A` and
the exact polynomial form of `t_j`. Compute every magnitude-only term for
the frozen `x^(10)` exactly or by rigorous rational enclosure. Keep surviving
phase cycles explicit.

Seek a phase-free SOS, PSD, large-sieve, or operator-norm bound strong enough
to force either

\[
\mathcal F_\Gamma\le10
\]

for every physical field, or incompatibility of `GammaEnergy` with every
admissible exact `O_10` satisfying the rigorous lower bound
`O_10>=10.249999952078184...` for `x^(10)`. Do not substitute that lower
bound as an equality. A bound with ambient scale
`D`, `M`, or `sqrt(M)` and no comparison to the required threshold is not an
advance.

### 3. Preserve rank-one information

If useful, translate the same trilinear form into the orbit Gram matrix

\[
G_{ab}=\langle\psi|W_a^*W_b|\psi\rangle
\]

or the rank-one-input channel

\[
\Phi_A(P)=\sum_{a\in A}W_aPW_a^*.
\]

But prove the translation exactly and retain the common-state Weyl cocycles.
Do not replace the problem by an unrestricted PSD matrix, an unrestricted
operator norm, or only entrywise bounds. Explicitly test whether any proposed
moment/minor is already automatic for `F_gamma<<m`.

### 4. If the inequality still does not close

Do not call the whole idempotence route impossible. Identify the exact first
surviving phase sum or exact restricted operator norm, state the numerical
threshold it would have to meet, and prove only the no-go for the particular
relaxation actually used. If a finite certificate is proposed, write the
certificate and verification equations explicitly rather than merely naming
an SDP or SOS hierarchy.

## Required final ledger

End with separate headings:

- `VERIFIED`
- `CORRECTED`
- `DISPROVED`
- `NECESSARY-ONLY`
- `EQUIVALENT`
- `OPEN`

State explicitly whether you have produced any one of:

1. an exact physical unit vector with `F_Gamma>10`;
2. an exact contradiction excluding a lift of `x^(10)`;
3. a phase-uniform proof of PW10.

If none is produced, the verdict must remain

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

Name the first genuinely new claim that requires independent verification.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-22-prompt-sent.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-22-response.md bytes=21118 sha256=fa330184728b4fc95bd5dec84e04b1777c5a6135021a524bdcdff91b8d977511 -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The centered idempotence equation is correct and genuinely breaks the anti-projector symmetry. Its restriction to \(\Gamma\) yields an exact oriented cubic identity and an exact quartic energy identity. Together, those two scalar identities are equivalent to all centered idempotence equations on the \(\Gamma\)-coefficients.

For the frozen pseudo-magnitude \(x^{(10)}\), the restricted cubic splits exactly into:

1. an orbit-channel third-moment contribution involving triples from \(A\); and
2. an “external-label” trilinear contribution over labels outside the translated set \(A-a\).

The orbit contribution has absolute value below \(60\), while the external contribution would have to exceed

$$
9.650797549803547\times 10^{18}.
$$

The restricted quartic energy similarly splits into magnitude-only diagonal and swap-collision terms plus a genuine four-phase cycle. The magnitude-only terms contribute at most \(2.401\times10^{19}\), whereas the full required energy is above

$$
9.086623783682114\times10^{36}.
$$

Thus essentially all the required energy must come from the genuine off-diagonal phase-cycle sum. No phase-uniform upper bound near that threshold is proved.

No physical vector above \(10\), no contradiction excluding a lift of \(x^{(10)}\), and no proof of PW10 is obtained.

---

# 1. Mandatory corrections to Round 21

## 1.1 Full two-line average

`FullTwoLineAverage` is verified and explicitly contains unresolved cross-basis Kirkwood–Dirac and Bargmann quantities.

What has **not** been proved is that those quantities can never simplify, cancel, or become determined after imposing the full physical compatibility equations. The correct conclusion is only:

$$
\boxed{
\text{the unrestricted averaged expression retains explicit KD/Bargmann data.}
}
$$

It is not a theorem that no physical-locus simplification exists.

## 1.2 Correction of the \(\sqrt8\) envelope

From

$$
|\lambda_z|\le M,
$$

the safe estimate is

$$
\begin{aligned}
\sqrt8\,D
\sqrt{\lambda_z^2+M^2+6M}
&\le
\sqrt8\,D\sqrt{2M^2+6M}\\
&=
\boxed{
4DM\sqrt{1+\frac3M}.
}
\end{aligned}
\tag{1.1}
$$

This is strictly larger than \(4DM\), not smaller.

No sharper evaluated value of \(\lambda_{z_\star}\) was obtained at

$$
z_\star=(0,1).
$$

## 1.3 Scope of the anti-projector symmetry

The transformation

$$
R\longmapsto \frac{2I}{D}-R
$$

shows that the rank-two displacement equations do not select positivity when a solution is already present.

It does **not** imply that the uncontracted displacement equations are consistent for the particular frozen magnitude \(x^{(10)}\). They could still exclude that magnitude profile.

## 1.4 Unevaluated frozen right sides

The expressions at \(z_\star\) involving

$$
\lambda_{z_\star},\qquad
\sum_{h\in\Gamma}x_{z_\star-h},\qquad
\sum_{a\in A}x_{z_\star-a}
$$

remain exact but unevaluated cyclotomic sums. They were only bounded using the frozen pointwise upper bound. They should not be called explicitly evaluated frozen values.

---

# 2. Centered idempotence

Let

$$
\alpha=\delta_0+\beta,
\qquad
\beta_0=0.
$$

Use the normalized twisted convolution

$$
(a\star b)_z
=
\frac1D
\sum_u
a_u b_{z-u}
\omega^{[u,z]/2}.
$$

The Weyl reconstruction map

$$
R(a)=\frac1D\sum_z a_zW_z
$$

satisfies

$$
R(a)R(b)=R(a\star b).
$$

For the point mass,

$$
\delta_0\star\delta_0=\frac1D\delta_0,
$$

and

$$
\delta_0\star\beta
=
\beta\star\delta_0
=
\frac1D\beta.
$$

Thus

$$
\alpha\star\alpha=\alpha
$$

is equivalent to

$$
\frac1D\delta_0+\frac2D\beta+\beta\star\beta
=
\delta_0+\beta.
$$

Therefore

$$
\boxed{
\beta\star\beta
=
\frac{D-2}{D}\beta
+
\frac{D-1}{D}\delta_0.
}
\tag{CenteredIdempotence}
$$

For \(z\ne0\),

$$
\boxed{
\sum_u
\beta_u\beta_{z-u}
\omega^{[u,z]/2}
=
(D-2)\beta_z.
}
\tag{OrientedCoefficient}
$$

At \(z=0\), the equation is

$$
\sum_u|\beta_u|^2=D-1,
$$

which is exactly the nonzero Weyl mass condition.

## 2.1 Operator form and rigidity

Set

$$
B=R_\alpha-\frac ID=R(\beta).
$$

Then centered idempotence is

$$
\boxed{
B^2
=
\frac{D-2}{D}B
+
\frac{D-1}{D^2}I.
}
\tag{2.1}
$$

The two roots of the scalar polynomial are

$$
\frac{D-1}{D},
\qquad
-\frac1D.
$$

Because \(\operatorname{Tr}B=0\), the positive root must have multiplicity one. Hence

$$
B+\frac ID
$$

is a rank-one orthogonal projector.

Thus centered idempotence is a genuine branch selector.

## 2.2 Breaking the anti-projector branch

Under

$$
R\longmapsto\frac{2I}{D}-R,
$$

one has

$$
B\longmapsto-B,
\qquad
\beta\longmapsto-\beta.
$$

The left side of `CenteredIdempotence` is unchanged:

$$
(-\beta)\star(-\beta)=\beta\star\beta,
$$

while the nonzero part of the right side changes sign. Therefore, for every \(z\ne0\),

$$
\frac{D-2}{D}\beta_z
\longmapsto
-\frac{D-2}{D}\beta_z.
$$

Since \(x_z^{(10)}>0\) for every nonzero \(z\), the two branches cannot both satisfy the centered equations.

---

# 3. The exact \(\Gamma\)-restricted cubic identity

For \(z\ne0\), define

$$
S_z
:=
\sum_u
\beta_u\beta_{z-u}
\omega^{[u,z]/2}.
$$

A physical lift requires

$$
S_z=(D-2)\beta_z.
$$

Multiply by \(\overline{\beta_z}\) and sum over \(z\in\Gamma\):

$$
\boxed{
(D-2)\mathcal F_\Gamma
=
\sum_{z\in\Gamma}\sum_u
\overline{\beta_z}\,
\beta_u\beta_{z-u}
\omega^{[u,z]/2}.
}
\tag{GammaOriented}
$$

Here

$$
\mathcal F_\Gamma
=
\sum_{z\in\Gamma}|\beta_z|^2.
$$

The right side is real. One operator proof is useful.

Define the Weyl coefficient projection

$$
B_\Gamma
=
\frac1D
\sum_{z\in\Gamma}\beta_zW_z.
$$

Because \(\Gamma=-\Gamma\) and \(\beta_{-z}=\overline{\beta_z}\),

$$
B_\Gamma=B_\Gamma^*.
$$

Moreover,

$$
\boxed{
\sum_{z\in\Gamma}\overline{\beta_z}S_z
=
D^2\operatorname{Tr}(B_\Gamma B^2).
}
\tag{3.1}
$$

The trace of the product of two Hermitian operators is real.

## 3.1 What this identity is—and is not

`GammaOriented` is exactly one Hilbert–Schmidt projection of centered idempotence. It is:

* genuinely orientation-sensitive;
* not equal to PW10;
* not, by itself, an upper bound on \(\mathcal F_\Gamma\);
* not equivalent to all centered coefficient equations.

It is therefore a new restricted trilinear necessary identity, not PW10 in disguise.

---

# 4. Exact reindexing by the Sidon difference set

For \(a,b\in A\), write

$$
z_{ba}=b-a.
$$

Ordered-difference injectivity means every \(z\in\Gamma\) has one unique representation \(z=b-a\) with \(a\ne b\).

Reindex `GammaOriented` as

$$
\begin{aligned}
(D-2)\mathcal F_\Gamma
=
\sum_{a\ne b}
\sum_u
\overline{\beta_{b-a}}\,
\beta_u\beta_{b-a-u}
\omega^{[u,b-a]/2}.
\end{aligned}
\tag{4.1}
$$

Now let

$$
Q_a=W_aPW_a^*
$$

for a hypothetical physical lift \(P\).

For \(c\in A\), choose

$$
u=c-a.
$$

Then

$$
b-a-u=b-c,
$$

and direct Weyl multiplication gives

$$
\boxed{
\overline{\beta_{b-a}}\,
\beta_{c-a}\beta_{b-c}
\omega^{[c-a,b-a]/2}
=
\operatorname{Tr}(Q_aQ_bQ_c).
}
\tag{4.2}
$$

If \(c=a\) or \(c=b\), one \(\beta\)-factor is \(\beta_0=0\). Hence the contribution from \(u\in A-a\) is exactly

$$
T_A
:=
\sum_{\substack{a,b,c\in A\\
a,b,c\ {\rm pairwise\ distinct}}}
\operatorname{Tr}(Q_aQ_bQ_c).
$$

Define the external-label contribution

$$
\boxed{
T_{\rm ext}
:=
\sum_{a\ne b}
\sum_{u\notin A-a}
\overline{\beta_{b-a}}\,
\beta_u\beta_{b-a-u}
\omega^{[u,b-a]/2}.
}
\tag{4.3}
$$

Then

$$
\boxed{
(D-2)\mathcal F_\Gamma
=
T_A+T_{\rm ext}.
}
\tag{4.4}
$$

---

# 5. Exact orbit-channel interpretation

Define the unnormalized orbit channel output

$$
\Phi_A(P)=\sum_{a\in A}Q_a.
$$

Its third moment expands as follows.

* All three indices equal: contribution \(m\).
* Exactly two indices equal: contribution \(3\mathcal F_\Gamma\).
* All three indices distinct: contribution \(T_A\).

Therefore

$$
\boxed{
\operatorname{Tr}\Phi_A(P)^3
=
m+3\mathcal F_\Gamma+T_A.
}
\tag{5.1}
$$

Combining with (4.4),

$$
\boxed{
T_{\rm ext}
=
m+(D+1)\mathcal F_\Gamma
-
\operatorname{Tr}\Phi_A(P)^3.
}
\tag{5.2}
$$

This is the exact relationship between the centered \(\Gamma\)-restricted cubic and the orbit-channel third moment.

## 5.1 The orbit part is uniformly small

For pairwise distinct \(a,b,c\),

$$
\left|
\operatorname{Tr}(Q_aQ_bQ_c)
\right|
=
\sqrt{
x_{b-a}x_{c-b}x_{a-c}
}.
$$

For the frozen pseudo-magnitude,

$$
x_z^{(10)}
\le
U:=
\frac{11}{D+1}+\frac{10}{M}
\qquad(z\ne0).
$$

Therefore

$$
|T_A|
\le
m(m-1)(m-2)U^{3/2}.
\tag{5.3}
$$

The exact dimensions satisfy

$$
D>4m^2,
\qquad
D<5M,
$$

and consequently

$$
U<\frac{61}{D}.
$$

Hence

$$
\begin{aligned}
m(m-1)(m-2)U^{3/2}
&<
m^3\left(\frac{61}{D}\right)^{3/2}\\
&<
\frac{61^{3/2}}8\\
&<60.
\end{aligned}
\tag{5.4}
$$

The last inequality follows from

$$
61^3=226981<230400=480^2.
$$

Thus

$$
\boxed{
|T_A|<60.
}
\tag{5.5}
$$

## 5.2 Required external coherence

Let

$$
L_{10}
=
10+
\frac{
3357953467987716774306702559357710
}{
13431816446658977517442074781790591
}.
$$

The frozen objective satisfies

$$
\mathcal F_\Gamma=\mathcal O_{10}\ge L_{10}.
$$

Equations (4.4) and (5.5) imply

$$
\boxed{
T_{\rm ext}
>
(D-2)L_{10}-60.
}
\tag{5.6}
$$

At the exact frozen integers,

$$
\boxed{
T_{\rm ext}
>
9.650797549803547\times10^{18}.
}
\tag{5.7}
$$

Thus essentially the entire oriented cubic required by centered idempotence must come from labels outside the translated frozen set \(A-a\).

---

# 6. Why elementary Cauchy bounds do not close the cubic gate

Let

$$
\xi_z=
\begin{cases}
x_z^{(10)},&z\ne0,\\
0,&z=0.
\end{cases}
$$

Then

$$
\sum_z\xi_z=D-1,
\qquad
0\le\xi_z\le U.
$$

For each ordered \(a\ne b\), let

$$
R_{a,b}
=
\sum_{u\notin A-a}
\beta_u\beta_{b-a-u}
\omega^{[u,b-a]/2}.
$$

Then

$$
T_{\rm ext}
=
\sum_{a\ne b}
\overline{\beta_{b-a}}R_{a,b}.
$$

Cauchy–Schwarz gives

$$
|T_{\rm ext}|
\le
\sqrt{\mathcal F_\Gamma}
\left(
\sum_{a\ne b}|R_{a,b}|^2
\right)^{1/2}.
$$

Each \(u\)-sum has at most \(D^2\) terms, so

$$
|R_{a,b}|^2
\le
D^2\sum_u\xi_u\xi_{b-a-u}.
$$

Define

$$
D_\Gamma
=
\sum_{z\in\Gamma}\sum_u\xi_u\xi_{z-u}.
$$

Then

$$
\sum_{a\ne b}|R_{a,b}|^2
\le D^2D_\Gamma.
$$

Furthermore,

$$
D_\Gamma
\le
MU(D-1),
\qquad
\mathcal F_\Gamma\le MU.
$$

Therefore

$$
\boxed{
|T_{\rm ext}|
\le
DMU\sqrt{D-1}.
}
\tag{6.1}
$$

For the exact integers,

$$
DMU\sqrt{D-1}
<
1.165\times10^{28}.
$$

This is more than \(1.2\times10^9\) times larger than the required lower bound (5.7).

Thus this particular Cauchy relaxation is rigorously too weak; it does not exclude the pseudo-candidate.

---

# 7. Restricted convolution energy

Squaring `OrientedCoefficient` and summing over \(\Gamma\) gives

$$
\boxed{
(D-2)^2\mathcal F_\Gamma
=
\sum_{z\in\Gamma}
\left|
\sum_u
\beta_u\beta_{z-u}
\omega^{[u,z]/2}
\right|^2.
}
\tag{GammaEnergy}
$$

Define

$$
A_{z,u}
=
\beta_u\beta_{z-u}\omega^{[u,z]/2}.
$$

For each \(z\), partition the ordered pairs \((u,v)\) in

$$
\left|\sum_uA_{z,u}\right|^2
=
\sum_{u,v}A_{z,u}\overline{A_{z,v}}
$$

into:

1. diagonal pairs \(v=u\);
2. swap collisions \(v=z-u\ne u\);
3. genuine off-diagonal pairs

   $$
   v\ne u,\qquad v\ne z-u.
   $$

This yields

$$
\boxed{
(D-2)^2\mathcal F_\Gamma
=
D_\Gamma+C_\Gamma+G_\Gamma.
}
\tag{7.1}
$$

---

# 8. Magnitude-only diagonal term

The diagonal term is

$$
\boxed{
D_\Gamma
=
\sum_{z\in\Gamma}\sum_u
\xi_u\xi_{z-u}.
}
\tag{8.1}
$$

It has the exact frozen Fourier form

$$
\boxed{
D_\Gamma
=
\frac1{D^2}
\sum_{r\in\mathbb F_D^2}
\lambda_r\bigl(Dx_r^{(10)}-1\bigr)^2.
}
\tag{8.2}
$$

To see this, use:

$$
\widehat{\xi}(r)
=
\sum_z\xi_z\omega^{[r,z]}
=
Dx_r^{(10)}-1,
$$

and

$$
\widehat{\mathbf1_\Gamma}(r)=\lambda_r,
$$

where central symmetry removes the sign ambiguity.

The rigorous pointwise bound is

$$
\boxed{
D_\Gamma\le MU(D-1).
}
\tag{8.3}
$$

Numerically,

$$
D_\Gamma
<
1.200465022391\times10^{19}.
$$

---

# 9. Magnitude-only swap-collision term

The swap term is

$$
\boxed{
C_\Gamma
=
\sum_{z\in\Gamma}
\sum_{\substack{u\\2u\ne z}}
\xi_u\xi_{z-u}
\omega^{[u,z]}.
}
\tag{9.1}
$$

It is real: the terms indexed by \(u\) and \(z-u\) are complex conjugates.

Moreover,

$$
\boxed{|C_\Gamma|\le D_\Gamma.}
\tag{9.2}
$$

For the frozen parabola, write

$$
z=a_a-a_b
=
\left(
t_a-t_b,\,
(t_a-t_b)(t_a+t_b)
\right).
$$

If \(u=(r,s)\), then

$$
\boxed{
[u,z]
=
(t_a-t_b)
\bigl(r(t_a+t_b)-s\bigr).
}
\tag{9.3}
$$

Thus (9.1) is a completely explicit, phase-free cyclotomic sum determined by the frozen magnitudes and the exact \(t_j\)'s.

---

# 10. Genuine four-phase cycles

The remaining term is

$$
\boxed{
\begin{aligned}
G_\Gamma
=
\sum_{z\in\Gamma}
\sum_{\substack{u,v\\
v\ne u,\ v\ne z-u}}
&
\beta_u\beta_{z-u}
\overline{\beta_v\beta_{z-v}}\\
&\times
\omega^{[u-v,z]/2}.
\end{aligned}
}
\tag{10.1}
$$

Writing

$$
u=(r,s),\qquad v=(r',s'),
$$

and \(z=a_a-a_b\), the fixed Weyl phase is

$$
\boxed{
\omega^{
\frac{t_a-t_b}{2}
\left[
(r-r')(t_a+t_b)-(s-s')
\right]
}.
}
\tag{10.2}
$$

Ordered-difference injectivity eliminates multiplicity in the outer \(z\)-sum. It does **not** collapse the inner \(u,v\)-sum, because \(u,v\) range over the entire phase space, not over \(A\) or \(\Gamma\).

This is the first genuinely unresolved quartic phase-cycle statistic.

---

# 11. Frozen lower bound on the genuine phase cycles

From (7.1),

$$
G_\Gamma
=
(D-2)^2\mathcal F_\Gamma
-
D_\Gamma-C_\Gamma.
$$

Using

$$
|C_\Gamma|\le D_\Gamma
$$

and (8.3),

$$
G_\Gamma
\ge
(D-2)^2\mathcal F_\Gamma
-
2MU(D-1).
$$

For the frozen pseudo-magnitude,

$$
\boxed{
G_\Gamma
\ge
(D-2)^2L_{10}
-
2MU(D-1).
}
\tag{11.1}
$$

The right side is an explicit rational number. Numerically,

$$
\boxed{
G_\Gamma
>
9.086623783682114\times10^{36}.
}
\tag{11.2}
$$

By comparison,

$$
2MU(D-1)
<
2.401\times10^{19}.
$$

Thus the magnitude-only diagonal and swap terms account for at most

$$
2.643\times10^{-18}
$$

of the required energy. More than

$$
1-2.643\times10^{-18}
$$

of the restricted energy must be supplied by the genuine four-phase cycles.

This is a strong coherence requirement, but not a contradiction.

## 11.1 Size of the elementary upper relaxation

The elementary bound

$$
\left|
\sum_uA_{z,u}
\right|
\le
\sum_u\sqrt{\xi_u\xi_{z-u}}
\le D-1
$$

gives

$$
\sum_{z\in\Gamma}
\left|\sum_uA_{z,u}\right|^2
\le
M(D-1)^2.
$$

This upper envelope exceeds the required lower bound by a factor greater than

$$
2.29\times10^{16}.
$$

Therefore the elementary triangle/Bhattacharyya relaxation is decisively too weak.

---

# 12. Restricted residual interpretation

Define the centered coefficient residual

$$
r_z
=
S_z-(D-2)\beta_z.
$$

Then

$$
\begin{aligned}
\sum_{z\in\Gamma}|r_z|^2
={}&
\sum_{z\in\Gamma}|S_z|^2
+
(D-2)^2\mathcal F_\Gamma\\
&-
2(D-2)
\operatorname{Re}
\sum_{z\in\Gamma}\overline{\beta_z}S_z.
\end{aligned}
\tag{12.1}
$$

Consequently:

$$
\boxed{
\text{GammaOriented}+\text{GammaEnergy}
\iff
r_z=0\quad\forall z\in\Gamma.
}
\tag{12.2}
$$

Thus the two restricted scalar identities together are exactly equivalent to the full family of centered idempotence equations on the coefficients indexed by \(\Gamma\).

They remain only a restriction of global idempotence.

## 12.1 Anti-projector separation on \(\Gamma\)

If \(\beta\) solves the restricted equations, then under \(\beta\mapsto-\beta\),

$$
S_z\mapsto S_z
$$

but

$$
(D-2)\beta_z\mapsto-(D-2)\beta_z.
$$

Hence the transformed restricted residual is

$$
2(D-2)\beta_z,
$$

and its squared norm is

$$
\boxed{
4(D-2)^2\mathcal F_\Gamma.
}
\tag{12.3}
$$

The \(\Gamma\)-restricted centered equations therefore already separate the physical orientation from the anti-projector orientation.

---

# 13. Rank-one orbit-channel moment check

The orbit output satisfies

$$
\operatorname{Tr}\Phi_A(P)=m,
\qquad
\operatorname{Tr}\Phi_A(P)^2=m+\mathcal F_\Gamma.
$$

For a positive operator,

$$
\operatorname{Tr}\Phi_A(P)^3
\ge
\frac{
\left(\operatorname{Tr}\Phi_A(P)^2\right)^2
}{
\operatorname{Tr}\Phi_A(P)
}
=
\frac{(m+\mathcal F_\Gamma)^2}{m}.
\tag{13.1}
$$

On the other hand, (5.1) and (5.5) give

$$
\operatorname{Tr}\Phi_A(P)^3
\le
m+3\mathcal F_\Gamma+60.
\tag{13.2}
$$

Combining,

$$
\boxed{
\frac{\mathcal F_\Gamma^2}{m}
-
\mathcal F_\Gamma
<60.
}
\tag{13.3}
$$

For the entire frozen entrywise range

$$
0\le\mathcal F_\Gamma<\frac{51}{4}\ll m,
$$

the left side is negative. Thus this rank-one orbit moment gives no improvement.

The common-state orbit structure has been retained, but this particular moment inequality is automatic at the relevant scale.

---

# 14. Earliest surviving obstruction

The centered equation has now reduced the frozen lift problem to two exact phase-coherence requirements:

### Cubic orientation requirement

The external trilinear sum (4.3) must satisfy

$$
T_{\rm ext}
>
9.650797549803547\times10^{18}.
$$

The best elementary frozen-magnitude Cauchy bound obtained here is approximately \(1.165\times10^{28}\), leaving a factor exceeding \(1.2\times10^9\).

### Quartic restricted-energy requirement

The genuine four-phase cycle (10.1) must satisfy

$$
G_\Gamma
>
9.086623783682114\times10^{36}.
$$

All magnitude-only terms are negligible at this scale, but the elementary phase-free upper bound is still more than \(2.29\times10^{16}\) too large.

The exact first surviving phase sum is therefore

$$
\boxed{
G_\Gamma
=
\sum_{\substack{z\in\Gamma\\
u,v:\ v\ne u,\ z-u}}
\beta_u\beta_{z-u}
\overline{\beta_v\beta_{z-v}}
\omega^{[u-v,z]/2}.
}
$$

A proof excluding \(x^{(10)}\) would follow from any exact upper bound

$$
G_\Gamma
<
(D-2)^2L_{10}-2MU(D-1).
$$

No such upper bound is proved.

---

# 15. Status of the requested outcomes

No exact physical unit vector with

$$
\mathcal F_\Gamma>10
$$

has been produced.

No exact contradiction excluding a phase lift of \(x^{(10)}\) has been produced.

No phase-uniform proof of PW10 has been produced.

Accordingly,

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

---

# VERIFIED

* `CenteredIdempotence`, including all \(D\)-normalizations.
* `OrientedCoefficient`.
* The operator polynomial for \(B=R-I/D\).
* Exact branch selection and failure of the anti-projector branch.
* `GammaOriented`.
* Its Hilbert–Schmidt projection interpretation.
* The exact reindexing by \(z=b-a\).
* The identity of the \(u=c-a\) sub-sum with the all-distinct orbit-channel cubic.
* The exact decomposition

  $$
  (D-2)\mathcal F_\Gamma=T_A+T_{\rm ext}.
  $$
* The orbit identity

  $$
  \operatorname{Tr}\Phi_A(P)^3=m+3\mathcal F_\Gamma+T_A.
  $$
* The bound \(|T_A|<60\).
* The external coherence lower bound above \(9.6507\times10^{18}\).
* `GammaEnergy`.
* The diagonal/swap/genuine-phase decomposition.
* The exact Fourier expression for \(D_\Gamma\).
* The swap-collision formula with the frozen parabolic phase.
* The genuine four-phase cycle formula.
* The frozen lower bound above \(9.0866\times10^{36}\).
* The equivalence between `GammaOriented` plus `GammaEnergy` and vanishing of every centered residual on \(\Gamma\).

# CORRECTED

* `FullTwoLineAverage` is known to contain unresolved KD/Bargmann data; no theorem of irreducible noncancellation on the physical locus has been proved.
* The safe weighted-extraction envelope is

  $$
  4DM\sqrt{1+3/M},
  $$

  not a quantity strictly below \(4DM\).
* The anti-projector symmetry does not establish consistency of the rank-two equations for \(x^{(10)}\).
* The \(z_\star\) right sides remain unevaluated cyclotomic sums bounded by frozen magnitude estimates.
* \(x^{(10)}\) remains a pseudo-candidate of unresolved physical liftability.

# DISPROVED

* Sufficiency of the elementary external-label Cauchy bound for excluding the frozen pseudo-candidate; its upper envelope is over \(10^9\) too large.
* Sufficiency of the elementary restricted-convolution triangle bound; it is over \(10^{16}\) too large.
* Sufficiency of the orbit-channel third-moment inequality at the scale \(\mathcal F_\Gamma<51/4\).

# NECESSARY-ONLY

* `GammaOriented`.
* `GammaEnergy`.
* The external trilinear coherence threshold.
* The genuine four-phase-cycle threshold.
* The rank-one orbit-channel moment inequalities.
* All \(\Gamma\)-restricted centered residual equations.

# EQUIVALENT

* Full centered idempotence and

  $$
  R_\alpha^2=R_\alpha.
  $$
* Under Hermiticity and trace one, full centered idempotence and a rank-one physical projector.
* `GammaOriented` plus `GammaEnergy` and centered idempotence restricted to all \(z\in\Gamma\).

# OPEN

* Whether the external trilinear phase sum can attain its required value.
* Whether the genuine four-phase-cycle sum can attain its required value.
* Whether \(x^{(10)}\) admits a physical phase lift.
* Whether every phase assignment for \(x^{(10)}\) has a positive idempotence residual.
* Whether another objective-above-\(10\) magnitude profile is physical.
* PW10 for the frozen tuple.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the exact orbit/external decomposition

$$
\boxed{
(D-2)\mathcal F_\Gamma
=
\left[
\operatorname{Tr}\Phi_A(P)^3-m-3\mathcal F_\Gamma
\right]
+
T_{\rm ext},
}
$$

together with the diagonal/swap/genuine-cycle decomposition of `GammaEnergy` and the resulting frozen threshold for \(G_\Gamma\).

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-22-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-22-local-audit.md bytes=8321 sha256=690efe30b6e2989ba80c257e3f43b8fab1be960030e7df7608f4b66506e63133 -->

# Round 22 local audit

- Audit completed (UTC): `2026-09-13T06:26:52Z`
- Scope: exact frozen tuple
  `m=485165196`, `D=941541228773064677`,
  `M=235385266924553220`
- Web response:
  `artifacts/web-gpt56sol-pro/round-22-response.md`
- Web-response SHA-256:
  `fa330184728b4fc95bd5dec84e04b1777c5a6135021a524bdcdff91b8d977511`
- Browser completion indicator: `Worked for 14m 23s`
- Capture equality: the browser response-copy payload, artifact copy, and
  output copy are byte-identical. Each UTF-8 Markdown copy has `21,104`
  Unicode characters, `21,118` bytes, and `1,357` newline characters.

## Verdict

Round 22 does **not** close PW10. It correctly replaces the
anti-projector-invariant displacement equations by the orientation-sensitive
centered idempotence equation and derives exact restricted cubic and quartic
bookkeeping identities. The new orbit/external and
diagonal/swap/genuine-cycle decompositions are correct, including their
normalizations and frozen numerical thresholds.

They leave unrestricted external cubic phases and genuine four-coefficient
phase cycles. No upper bound close to either required threshold is proved.
Therefore

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

There is still no physical lift or exclusion of `x^(10)`, and no
phase-uniform proof of PW10.

## Corrected send receipt

The first Round 22 browser generation was stopped after a post-send audit
found that the prompt had called `10.249999952078184...` the exact objective.
That number is only a rigorous lower bound. The same user message was edited
and regenerated with the correct statement

\[
\mathcal O_{10}:=\sum_{g\in\Gamma}x_g^{(10)}
\ge
10+
\frac{3357953467987716774306702559357710}
{13431816446658977517442074781790591}.
\]

The corrected browser payload is exactly the archived prompt with its single
terminal newline removed: `8,237` Unicode characters, `8,251` bytes, `309`
newlines, SHA-256
`c50d6316f3930ec96d48b5deb442b47ac5be2b4d340de8c9fdaf8d28aa80f09f`.
The completed answer belongs to that corrected branch.

## Centered idempotence

With `alpha=delta_0+beta`, `beta_0=0`, and normalized twisted convolution,
the exact projector equation is

\[
\boxed{
\beta\star\beta
=\frac{D-2}{D}\beta+\frac{D-1}{D}\delta_0.
}
\]

For nonzero `z`, this is

\[
\sum_u\beta_u\beta_{z-u}\omega^{[u,z]/2}
=(D-2)\beta_z.
\]

The zero-coordinate equation is precisely the nonzero Weyl mass `D-1`.
All factors of `D` and Weyl phases check directly at `D=3,5,7`.

The operator form

\[
B^2=\frac{D-2}{D}B+\frac{D-1}{D^2}I,
\qquad B=R-I/D,
\]

has roots `(D-1)/D` and `-1/D`. Hermiticity and `Tr B=0` force the first
root to have multiplicity one, so `B+I/D` is a rank-one orthogonal
projector. This is a genuine branch selector. Under `beta -> -beta`, the
quadratic left side is fixed and the nonzero linear right side changes sign.

## Restricted cubic and residual equivalence

The exact contraction

\[
(D-2)\mathcal F_\Gamma
=\sum_{z\in\Gamma,u}
\overline{\beta_z}\beta_u\beta_{z-u}
\omega^{[u,z]/2}
\tag{GammaOriented}
\]

is correct and real. Its operator normalization is

\[
\sum_{z\in\Gamma}\overline{\beta_z}S_z
=D^2\operatorname{Tr}(B_\Gamma B^2).
\]

The squared equation

\[
(D-2)^2\mathcal F_\Gamma
=\sum_{z\in\Gamma}|S_z|^2
\tag{GammaEnergy}
\]

is also exact. Together, these two scalar equalities imply

\[
\sum_{z\in\Gamma}|S_z-(D-2)\beta_z|^2=0,
\]

and are therefore equivalent to every centered coefficient equation on
`Gamma`. They remain only a restriction of global idempotence. They are not
an independent bound and are not PW10 in disguise.

## Orbit/external decomposition

Ordered-difference injectivity permits the unique reindexing `z=b-a`. For
`u=c-a`, direct Weyl multiplication gives

\[
\overline{\beta_{b-a}}\beta_{c-a}\beta_{b-c}
\omega^{[c-a,b-a]/2}
=\operatorname{Tr}(Q_aQ_bQ_c).
\]

Independent direct-matrix checks at `D=3,5,7` confirm the sign, orientation,
and cocycle. Hence

\[
(D-2)\mathcal F_\Gamma=T_A+T_{\rm ext},
\]

where `T_A` is the sum over pairwise-distinct orbit triples, and

\[
\operatorname{Tr}\Phi_A(P)^3
=m+3\mathcal F_\Gamma+T_A.
\]

Thus

\[
T_{\rm ext}
=m+(D+1)\mathcal F_\Gamma
-\operatorname{Tr}\Phi_A(P)^3.
\]

The frozen entrywise cap gives `|T_A|<60`. Using only the rigorous lower
bound `L_10` on the exact objective gives the valid conditional requirement

\[
T_{\rm ext}>(D-2)L_{10}-60
>9.650797549803547\times10^{18}.
\]

This is an exact reduction, not an obstruction. The response's own Cauchy
upper envelope is below `1.165e28`, more than `1.2e9` times the required
lower threshold, so that relaxation is decisively nonclosing.

## Restricted energy decomposition

Writing

\[
A_{z,u}=\beta_u\beta_{z-u}\omega^{[u,z]/2},
\]

the partition of `(u,v)` into diagonal `v=u`, swap
`v=z-u != u`, and the remaining pairs is disjoint and exhaustive. It gives

\[
(D-2)^2\mathcal F_\Gamma
=D_\Gamma+C_\Gamma+G_\Gamma.
\]

The diagonal term is the phase-free convolution

\[
D_\Gamma=\sum_{z\in\Gamma,u}\xi_u\xi_{z-u}
=\frac1{D^2}\sum_r
\lambda_r(Dx_r^{(10)}-1)^2.
\]

The swap term is also fixed by magnitudes and the Weyl cocycle:

\[
C_\Gamma
=\sum_{z\in\Gamma}\sum_{2u\ne z}
\xi_u\xi_{z-u}\omega^{[u,z]},
\qquad |C_\Gamma|\le D_\Gamma.
\]

For `z=(t_a-t_b,(t_a-t_b)(t_a+t_b))`, the displayed phase

\[
[u,z]=(t_a-t_b)(r(t_a+t_b)-s)
\]

is correct. The remaining `G_Gamma` is exactly the genuine unknown
four-coefficient phase-cycle sum. Small-prime tests at `D=3,5,7` reproduce
the full energy, every component, and the Fourier formula for `D_Gamma`.

Exact rational arithmetic verifies

\[
D_\Gamma<MU(D-1)<1.200465022391\times10^{19},
\]

and therefore

\[
\boxed{
G_\Gamma>(D-2)^2L_{10}-2MU(D-1)
>9.086623783682114\times10^{36}.
}
\]

The magnitude-only envelope is less than `2.643e-18` of the required total
energy. This correctly shows that a hypothetical lift requires a very large
coherent off-diagonal sum. It does **not** show that such a sum is impossible:
the elementary triangle upper bound is still more than `2.29e16` times the
required lower threshold.

## Corrections and evidence level

- Round 21's `<4DM` error is correctly repaired to
  `4DM sqrt(1+3/M)`.
- The two-line result is correctly narrowed to an explicit unresolved-KD
  formula, without asserting irreducible noncancellation on the physical
  locus.
- The anti-projector scope and the unevaluated `z_star` cyclotomic sums are
  correctly described.
- The orbit/external and energy decompositions are algebraically new
  bookkeeping reductions, but every equality is a contraction or component
  of centered idempotence. They should not be promoted as an independent
  certificate.
- The shorthand display for `G_Gamma` in section 14 has a transcription
  defect: its subscript ends with the dangling condition `z-u`. The complete
  and correct condition `v != u, v != z-u` appears in equation (10.1), which
  is the audited definition.

## Verification receipts

- `work/verify_round22_web_response.py` — SHA-256
  `6bc25c0a0a3d4a41a6a354cc070814262a6f10ecbcc15351c98d85e866928c59`;
  capture, corrected prompt, exact lower bound, and all frozen thresholds:
  `PASS`.
- `work/verify_round22_centered_idempotence.py` — SHA-256
  `9937123418efc127b56cabaac48d7c8f251e033dbcea7991103a0c3d74bd68cc`;
  centered equation, anti-branch separation, restricted cubic/energy, and
  the objective lower-bound receipt at `D=3,5,7`: `PASS`.
- `work/verify_round22_orbit_external_energy.py` — SHA-256
  `50910fd65a3fc60305dd6b47959097978de90cd5b75ed2c84a7c46568bd340d1`;
  orbit/external split, phase convention, collision partition, Fourier
  diagonal, and operator normalization at `D=3,5,7`: `PASS`.
- `work/round-22-independent-centered-idempotence.md` — SHA-256
  `eb01c42c13320daf97c9262e5587c6193a99d9a0c7d6322acbc58c0cfa49c743`.
- `work/verify_round22_pre_send.py` — SHA-256
  `a18634b13af47b3ed4ad1bd9c2ff4ca399c1b8eed9a3cbc50385c5ddf8d9653a`.

All four Round 22 Python checkers pass `py_compile`.

The first new Round 22 claims accepted after independent checking are the
exact orbit/external decomposition and the diagonal/swap/genuine-cycle
decomposition. Their surviving gate is an upper bound on the external cubic
or genuine four-phase-cycle sum at the displayed frozen threshold. No such
bound is currently present.

<!-- END HISTORICAL FILE path=outputs/round-22-local-audit.md -->


# ROUND 023

## PROMPT

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-23-prompt-sent.md bytes=8006 sha256=d996deb7742792dde8266db941a061bf70122969ecd5a7ee66322d669b046fc0 -->

# Round 23 — edge-Fourier phase retrieval and cross-h consistency

Continue in this same ordinary Chat conversation with the same model,
thinking tier, and canonically frozen finite `r=2`, low-`A` gate. Give a
public, self-contained derivation and no hidden chain-of-thought. Do not
repeat the Round 8--22 narrative. Audit the new edge-Fourier identities and
then test them on the exact frozen pseudo-magnitude. Proceed autonomously
through the strongest valid branch.

## Exact frozen boundary

Use exactly

\[
m=485165196,\quad P_0=m+41=485165237,
\]

\[
D=941541228773064677=4P_0^2+1,
\quad M=m(m-1)=235385266924553220,
\]

\[
A=\{(t_j,t_j^2):0\le j\le P_0-42\},
\quad t_j=2P_0j+(j^2\bmod P_0),
\quad \Gamma=(A-A)\setminus\{0\}.
\]

The open gate is

\[
\boxed{
\mathcal F_\Gamma(\psi)
=\sum_{g\in\Gamma}|\langle\psi|W_g|\psi\rangle|^2\le10
}
\tag{PW10}
\]

for every unit vector. Use

\[
W_{(p,q)}|y\rangle=\omega^{p(y+q/2)}|y+q\rangle,
\qquad W_uW_v=\omega^{[u,v]/2}W_{u+v}.
\]

The exact pseudo-magnitude is

\[
b_0=1,\quad b_z=(D+1)^{-1}\ (z\ne0),
\quad \lambda_z=\sum_{g\in\Gamma}\omega^{[g,z]},
\]

\[
y=\mathbf1_\Gamma+\lambda/D,
\qquad
x^{(10)}=b+\frac{10}{M}\left(y-\frac MD b\right).
\]

It is positive, even, self-Fourier, has mass `D`, and passes all previously
audited magnitude, parity, stabilizer, line-factor, and bounded-Gram tests.
Its exact frozen objective

\[
\mathcal O_{10}:=\sum_{g\in\Gamma}x_g^{(10)}
\]

is an unevaluated frozen cyclotomic quantity with the rigorous lower bound

\[
\mathcal O_{10}\ge L_{10}:=
10+\frac{3357953467987716774306702559357710}
{13431816446658977517442074781790591}
=10.249999952078184\ldots>10.
\]

Do not substitute this lower bound as an equality.

A physical lift requires

\[
\alpha_0=1,\qquad
\alpha_{-z}=\overline{\alpha_z},\qquad
|\alpha_z|^2=x_z^{(10)},
\]

\[
P=\frac1D\sum_z\alpha_zW_z,
\qquad P^2=P.
\]

A lift would disprove PW10. Excluding this one pseudo-point would not prove
PW10 for every other physical magnitude profile.

## Audited Round 22 boundary

Centered idempotence and its `GammaOriented` and `GammaEnergy` contractions
were independently checked. The exact decompositions

\[
(D-2)\mathcal F_\Gamma=T_A+T_{\rm ext}
\]

and

\[
(D-2)^2\mathcal F_\Gamma
=D_\Gamma+C_\Gamma+G_\Gamma
\]

were independently reproduced at `D=3,5,7`. A hypothetical frozen lift
would require

\[
T_{\rm ext}>9.650797549803547\times10^{18},
\]

\[
G_\Gamma>9.086623783682114\times10^{36}.
\]

The available elementary upper bounds miss by factors above `1.2e9` and
`2.29e16`, respectively. These thresholds are exact necessary reductions,
not contradictions. In the shorthand display for `G_Gamma` in Round 22,
replace the dangling condition `z-u` by the correct
`v != u, v != z-u` from equation (10.1).

## New audited edge-Fourier family

Let `V=F_D^2`. For `h,p in V`, define

\[
d_h(p)=
\alpha_{p+h/2}\overline{\alpha_{p-h/2}},
\qquad
\widehat d_h(k)=\sum_pd_h(p)\omega^{[p,k]}.
\]

Direct matrix checks at `D=3,5,7` support

\[
\boxed{
\widehat d_h(k)
=D\alpha_{h/2+k}\alpha_{h/2-k}.
}
\tag{EdgeFourier}
\]

Therefore

\[
\boxed{
|d_h(p)|^2=x_{p+h/2}x_{p-h/2},
\qquad
|\widehat d_h(k)|^2
=D^2x_{h/2+k}x_{h/2-k}.
}
\tag{EdgeFourierMagnitude}
\]

Audit the derivation from rank one, all half-label signs, and the Fourier
normalization. Also audit

\[
d_h(-p)=d_h(p),
\qquad d_{-h}(p)=\overline{d_h(p)}.
\]

The different `h` fields must arise from the single rank-one matrix

\[
Y_{a,b}=\alpha_a\overline{\alpha_b}
=d_{a-b}\!\left(\frac{a+b}{2}\right),
\]

so they obey

\[
\boxed{
d_{a-b}\!\left(\frac{a+b}{2}\right)
d_{b-c}\!\left(\frac{b+c}{2}\right)
=x_b,d_{a-c}\!\left(\frac{a+c}{2}\right).
}
\tag{EdgeCycle}
\]

For the centered field `beta=alpha-delta_0`, check the endpoint subtraction

\[
\widehat d_h^\beta(k)
=D\alpha_{h/2+k}\alpha_{h/2-k}
-\alpha_h\left(
\omega^{[h,k]/2}+\omega^{-[h,k]/2}
\right)
\quad(h\ne0),
\tag{CenteredEdgeFourier}
\]

and `hat d_0^beta(k)=D x_k-1`.

## Required phase-retrieval attack

Do not stop after saying that `EdgeFourier` follows from rank one. It gives a
new family in which both the time and Fourier magnitudes of every edge field
are fixed by `x^(10)`. Exploit that family in this order.

### 1. One-h pure phase-retrieval feasibility

For each `h`, put

\[
E_h=\sum_p x_{p+h/2}x_{p-h/2},
\]

\[
q_h(p)=\frac{x_{p+h/2}x_{p-h/2}}{E_h},
\qquad
\widetilde q_h(k)=
\frac{x_{h/2+k}x_{h/2-k}}{E_h}.
\]

If a lift exists, one normalized vector `d_h/sqrt(E_h)` has computational
probabilities `q_h` and probabilities `tilde q_h` in the symplectic Fourier
basis. Derive the exact fixed autocorrelation

\[
\sum_p d_h(p)\overline{d_h(p-s)}
=\sum_kx_{h/2+k}x_{h/2-k}\omega^{-[s,k]}.
\tag{EdgeAutocorrelation}
\]

Test genuine phase-free necessary conditions, including at minimum:

- the two-MUB collision inequality

  \[
  \frac{2\sum_p
  x_{p+h/2}^2x_{p-h/2}^2}{E_h^2}
  \le1+\frac1{D^2};
  \]

- every reverse-triangle/polygon inequality obtained from
  `EdgeAutocorrelation`;
- a sharp support or majorization/uncertainty condition if one is stronger.

Evaluate these with exact rational or rigorously enclosed cyclotomic
quantities for at least

\[
h=0,
\qquad z_\star=(0,1),
\qquad
h_\star=(970330475,1940660948)=a_1-a_0\in\Gamma.
\]

First verify the stated exact value of `h_star`. Mark the `h=0` consequences
that are merely old self-Fourier identities. A symbolic sum with no certified
comparison is not an evaluated test.

### 2. Exact two-basis PSD relaxation

For a fixed `h`, formulate explicitly the rank-relaxed feasibility problem

\[
K^{(h)}\succeq0,\qquad \operatorname{Tr}K^{(h)}=1,
\]

with diagonal `q_h` in the standard basis and diagonal `tilde q_h` in the
symplectic Fourier basis. This relaxation is necessary for the desired pure
edge vector.

Either:

- produce an exact dual infeasibility certificate for one frozen `h`; or
- produce and verify an explicit analytic PSD witness, thereby proving only
  that this rank-relaxed two-basis test cannot exclude that `h`.

Write the primal witness or dual matrix and all verification equations. Do
not merely say “solve an SDP.” If exact frozen cyclotomic evaluation is the
first blocker, identify the precise quantity and give a rigorous enclosure
target.

### 3. Restore cross-h rank-one consistency

Passing every separate `h` does not give one common `alpha`. Use `EdgeCycle`,
not independent edge phases. Contract it first over pairwise-distinct triples
from `A`, preserving the Weyl cocycle, and determine exactly whether the
result is old `T_A`, `T_ext`, `GammaOriented`, or a new constraint. Give both
directions for any claimed equivalence.

If that contraction is old, identify the smallest explicit coupled set of
`h` values whose cycle equations are not contained in the Round 22 scalar
contractions. Derive a finite phase-cycle equality or PSD minor on that set
and compare it to the exact frozen magnitudes. Do not replace `Y=alpha
alpha^*` by an unrelated unrestricted PSD matrix without recording the lost
rank-one information.

### 4. Threshold and no-go discipline

An acceptable advance is one of:

1. an exact physical lift with objective above `10`;
2. an exact contradiction for `x^(10)`;
3. a new rigorously evaluated necessary inequality with a stated frozen
   margin;
4. an explicit witness proving that a precisely named relaxation is too
   weak, followed by the exact first surviving cross-`h` condition.

Do not call the entire edge-Fourier or idempotence route impossible merely
because one triangle, uncertainty, or PSD relaxation passes.

## Required final ledger

End with separate headings:

- `VERIFIED`
- `CORRECTED`
- `DISPROVED`
- `NECESSARY-ONLY`
- `EQUIVALENT`
- `OPEN`

State explicitly whether an exact violating vector, an exact exclusion of
`x^(10)`, or a phase-uniform proof of PW10 has been produced. If none has,
retain

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

Name the first genuinely new claim requiring independent verification.

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-23-prompt-sent.md -->

## RESPONSE

<!-- BEGIN HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-23-response.md bytes=21761 sha256=a599b8aaf756c1aef06ce7f78582f59f9cf22d56c98a4f02e8794c1a1ff3688e -->

# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The edge-Fourier identity is correct, but it has a stronger consequence than the stated equality of two probability distributions:

$$
\boxed{\mathscr F d_h=d_h\qquad\text{for every }h,}
$$

where \(\mathscr F\) is the normalized symplectic Fourier transform. Thus every physical edge field must be a \(+1\) Fourier eigenvector with prescribed pointwise magnitudes.

For the exact frozen pseudo-magnitude \(x^{(10)}\):

* all one-\(h\) collision, polygon, support, and two-basis mixed-state tests pass;
* for every nonzero \(h\), an explicit analytic positive-semidefinite two-basis witness exists;
* this applies in particular to \(z_\star=(0,1)\) and

  $$
  h_\star=(970330475,1940660948)=a_1-a_0;
  $$
* the remaining one-\(h\) requirement is the **pure Fourier-eigenvector phase retrieval problem**, not merely compatibility of two measurement marginals;
* across different \(h\), the first surviving condition is a rank-one triangle phase cycle.

The centered Fourier identity at the special frequency \(k=h/2\) is exactly the already audited oriented centered-idempotence equation. Thus the full edge-Fourier family contains the global physical-lift problem rather than bypassing it.

No physical lift, no contradiction excluding \(x^{(10)}\), and no phase-uniform proof of PW10 is obtained.

---

# 1. Mandatory Round 21 corrections

The following narrower formulations are retained.

1. `FullTwoLineAverage` is verified and explicitly contains unresolved KD/Bargmann quantities. This does **not** prove that no cancellation or simplification occurs after all physical compatibility equations are imposed.

2. The safe weighted-extraction envelope is

   $$
   \sqrt8D\sqrt{\lambda_z^2+M^2+6M}
   \le
   4DM\sqrt{1+\frac3M},
   $$

   which is slightly larger than \(4DM\). No sharper exact value of the relevant \(\lambda_z\) was evaluated.

3. The anti-projector symmetry proves that the rank-two displacement equations are not a positivity selector when a solution exists. It does not prove consistency of those equations for \(x^{(10)}\).

4. The quantities at \(z_\star=(0,1)\) involving translated frozen sums remain exact but unevaluated cyclotomic expressions. Only rigorous pointwise bounds were supplied.

5. In the shorthand formula for \(G_\Gamma\), the genuine off-diagonal restriction is

   $$
   v\ne u,\qquad v\ne z-u.
   $$

---

# 2. Derivation of the edge-Fourier identity

Let

$$
P=|\psi\rangle\langle\psi|,
\qquad
\alpha_z=\operatorname{Tr}(W_z^*P),
\qquad
\alpha_{-z}=\overline{\alpha_z}.
$$

For

$$
d_h(p)
=
\alpha_{p+h/2}\overline{\alpha_{p-h/2}},
$$

define the unnormalized Fourier transform

$$
\widehat d_h(k)
=
\sum_p d_h(p)\omega^{[p,k]}.
$$

Because \(P\) has rank one,

$$
\operatorname{Tr}(PA)\operatorname{Tr}(PB)
=
\operatorname{Tr}(PAPB).
$$

Apply this with

$$
A=W_{-h/2-k},
\qquad
B=W_{-h/2+k}.
$$

Then

$$
\begin{aligned}
&\alpha_{h/2+k}\alpha_{h/2-k}\\
&\quad=
\operatorname{Tr}
\left(
PW_{-h/2-k}
P
W_{-h/2+k}
\right).
\end{aligned}
$$

Insert

$$
P=\frac1D\sum_r\alpha_rW_r.
$$

Weyl multiplication gives

$$
W_{-h/2-k}W_rW_{-h/2+k}
=
\omega^{[r,k]-[h,k]/2}W_{r-h}.
$$

Since

$$
\operatorname{Tr}(PW_{r-h})=\alpha_{h-r},
$$

we get

$$
\alpha_{h/2+k}\alpha_{h/2-k}
=
\frac1D
\sum_r
\alpha_r\alpha_{h-r}
\omega^{[r,k]-[h,k]/2}.
$$

Set \(r=p+h/2\). Then

$$
\alpha_{h-r}
=
\alpha_{h/2-p}
=
\overline{\alpha_{p-h/2}},
$$

and the phase becomes \(\omega^{[p,k]}\). Therefore

$$
\boxed{
\widehat d_h(k)
=
D\alpha_{h/2+k}\alpha_{h/2-k}.
}
\tag{EdgeFourier}
$$

All half-labels are well defined because \(D\) is odd.

---

# 3. The stronger self-Fourier consequence

Using Hermiticity,

$$
\alpha_{h/2-k}
=
\overline{\alpha_{k-h/2}}.
$$

Consequently,

$$
\alpha_{h/2+k}\alpha_{h/2-k}
=
d_h(k).
$$

Hence EdgeFourier is equivalently

$$
\boxed{\widehat d_h(k)=Dd_h(k).}
\tag{3.1}
$$

Define the normalized Fourier transform on the \(D^2\)-point phase space by

$$
(\mathscr Ff)(k)
=
\frac1D\sum_pf(p)\omega^{[p,k]}.
$$

Then

$$
\boxed{\mathscr Fd_h=d_h.}
\tag{3.2}
$$

This is stronger than merely prescribing the magnitudes in two mutually unbiased bases.

## 3.1 Symmetries

A direct use of \(\alpha_{-z}=\overline{\alpha_z}\) gives

$$
\boxed{d_h(-p)=d_h(p),}
\tag{3.3}
$$

and

$$
\boxed{d_{-h}(p)=\overline{d_h(p)}.}
\tag{3.4}
$$

The Fourier \(+1\) property implies the evenness independently because \(\mathscr F^2\) is phase-space reflection.

## 3.2 Magnitudes

The time-domain magnitude is

$$
\boxed{
|d_h(p)|^2
=
x_{p+h/2}x_{p-h/2}.
}
$$

The Fourier magnitude is

$$
\boxed{
|\widehat d_h(k)|^2
=
D^2x_{h/2+k}x_{h/2-k}.
}
$$

These are the proposed `EdgeFourierMagnitude` identities.

---

# 4. Centered edge identity

Put

$$
\beta=\alpha-\delta_0,
\qquad
\beta_0=0,
$$

and

$$
d_h^\beta(p)
=
\beta_{p+h/2}\overline{\beta_{p-h/2}}.
$$

For \(h\ne0\), the only removed terms occur at \(p=\pm h/2\). Each removed value equals \(\alpha_h\). Thus

$$
\boxed{
\begin{aligned}
\widehat d_h^\beta(k)
={}&
D\alpha_{h/2+k}\alpha_{h/2-k}\\
&-
\alpha_h
\left(
\omega^{[h,k]/2}
+
\omega^{-[h,k]/2}
\right).
\end{aligned}
}
\tag{CenteredEdgeFourier}
$$

For \(h=0\),

$$
d_0^\beta(p)=x_p-\delta_{p,0},
$$

so self-Fourier symmetry of \(x\) gives

$$
\boxed{
\widehat d_0^\beta(k)=Dx_k-1.
}
\tag{4.1}
$$

## 4.1 The diagonal slice is exactly centered idempotence

Set \(k=h/2\). Then

$$
\widehat d_h^\beta(h/2)
=
(D-2)\alpha_h.
\tag{4.2}
$$

On the other hand,

$$
\begin{aligned}
\widehat d_h^\beta(h/2)
&=
\sum_p
\beta_{p+h/2}
\beta_{h/2-p}
\omega^{[p,h]/2}\\
&=
\sum_u
\beta_u\beta_{h-u}
\omega^{[u,h]/2}.
\end{aligned}
$$

Therefore

$$
\boxed{
\sum_u
\beta_u\beta_{h-u}
\omega^{[u,h]/2}
=
(D-2)\beta_h,
}
\tag{4.3}
$$

which is precisely `OrientedCoefficient`.

Thus:

$$
\boxed{
\text{the }k=h/2\text{ slice of centered EdgeFourier is full centered idempotence.}
}
$$

The edge-Fourier route contains the old global lift equation rather than replacing it by an independent weaker structure.

---

# 5. Edge autocorrelation

Let

$$
E_h
=
\sum_p|d_h(p)|^2
=
\sum_p
x_{p+h/2}x_{p-h/2}.
$$

Unnormalized Fourier Parseval on \(D^2\) points gives

$$
\sum_k|\widehat d_h(k)|^2=D^2E_h.
$$

For a displacement \(s\),

$$
\begin{aligned}
&\sum_p
d_h(p)\overline{d_h(p-s)}\\
&\quad=
\frac1{D^2}
\sum_k|\widehat d_h(k)|^2\omega^{-[s,k]}.
\end{aligned}
$$

Substituting EdgeFourierMagnitude yields

$$
\boxed{
\sum_p
d_h(p)\overline{d_h(p-s)}
=
\sum_k
x_{h/2+k}x_{h/2-k}
\omega^{-[s,k]}.
}
\tag{EdgeAutocorrelation}
$$

The Fourier sign is correct for the transform convention used above.

---

# 6. Normalized one-\(h\) phase retrieval

Put

$$
r_h(p)=x_{p+h/2}x_{p-h/2}.
$$

Then

$$
E_h=\sum_pr_h(p).
$$

Define

$$
q_h(p)=\frac{r_h(p)}{E_h},
\qquad
\widetilde q_h(k)=
\frac{x_{h/2+k}x_{h/2-k}}{E_h}.
$$

These are in fact the same numerical function:

$$
\boxed{q_h=\widetilde q_h.}
\tag{6.1}
$$

If

$$
v_h=\frac{d_h}{\sqrt{E_h}},
$$

then \(q_h\) is its standard-basis distribution and \(\widetilde q_h\) is its symplectic-Fourier-basis distribution.

The physical requirement is stronger:

$$
\boxed{\mathscr Fv_h=v_h.}
\tag{6.2}
$$

Thus the true one-\(h\) problem is Fourier-eigenvector phase retrieval.

---

# 7. Frozen pointwise bounds

For every nonzero \(z\), the exact formula for \(x^{(10)}\) gives

$$
\boxed{
\gamma\le x_z^{(10)}\le U,
}
\tag{7.1}
$$

where

$$
\gamma=
\frac{D(m-11)-10m}
{D(D+1)(m-1)}
$$

and

$$
U=
\frac{11}{D+1}+\frac{10}{M}.
$$

At the exact frozen integers,

$$
U<7\times10^{-17},
\tag{7.2}
$$

and

$$
D\gamma>1-3\times10^{-8}.
\tag{7.3}
$$

The value \(x_0=1\) also satisfies \(x_0\ge\gamma\).

---

# 8. A uniform enclosure for every nonzero \(h\)

Write

$$
x^{(10)}=b+\eta.
$$

The exact self-Fourier construction gives

$$
\boxed{
\|\eta\|_2^2
=
\frac{20}{M}
\left(
\mathcal O_{10}-\frac{M}{D+1}
\right).
}
\tag{8.1}
$$

Since \(\mathcal O_{10}\le MU\),

$$
\|\eta\|_2^2
\le
\frac{200}{D+1}+\frac{200}{M}.
$$

Exact cross multiplication yields

$$
\boxed{
\|\eta\|_2^2
<
\frac{49}{4\cdot10^{16}}.
}
\tag{8.2}
$$

Also

$$
\|b\|_2^2=\frac{2D}{D+1}<2.
$$

Define

$$
\varepsilon_x
=
2\|b\|_2\|\eta\|_2+\|\eta\|_2^2.
$$

Then

$$
\boxed{
\varepsilon_x<\frac{53}{5\cdot10^8}
=1.06\times10^{-7}.
}
\tag{8.3}
$$

For \(h\ne0\), the baseline edge energy is

$$
E_h^{\,b}
=
\frac{D(D+2)}{(D+1)^2}<1.
$$

Translation is unitary on \(\ell_2(V)\), so

$$
|E_h-E_h^{\,b}|\le\varepsilon_x.
$$

Therefore

$$
\boxed{
D^2\gamma^2
\le E_h
<
1+1.06\times10^{-7}.
}
\tag{8.4}
$$

Moreover,

$$
2D^2\gamma^2
>
2(1-3\times10^{-8})^2
>
1.99999988.
$$

Hence

$$
\boxed{
\frac{\gamma^2}{E_h}>
\frac1{2D^2}.
}
\tag{8.5}
$$

This lower bound is the key to the exact two-basis PSD witness below.

---

# 9. Two-MUB collision test

Let

$$
N=D^2.
$$

For any pure vector in dimension \(N\), the collision probabilities in two mutually unbiased bases obey

$$
\sum_pq(p)^2+\sum_k\widetilde q(k)^2
\le1+\frac1N.
\tag{9.1}
$$

A self-contained proof is obtained by writing the pure density matrix as

$$
\tau=\frac IN+A
$$

with \(A\) traceless. The two traceless diagonal subspaces associated with mutually unbiased bases are Hilbert–Schmidt orthogonal. The sum of the squared norms of the two diagonal projections of \(A\) is therefore at most

$$
\|A\|_2^2=1-\frac1N.
$$

Adding the two uniform contributions gives (9.1).

Because \(q_h=\widetilde q_h\),

$$
\boxed{
2\sum_pq_h(p)^2
\le1+\frac1{D^2}.
}
\tag{9.2}
$$

## 9.1 Uniform frozen margin for every \(h\ne0\)

There are two values \(p=\pm h/2\) at which one factor in \(r_h(p)\) is \(x_0\); hence

$$
r_h(p)\le U
$$

at those two points. At every other point,

$$
r_h(p)\le U^2.
$$

Therefore

$$
\sum_pr_h(p)^2
\le
2U^2+(D^2-2)U^4.
$$

Using

$$
D<10^{18},
\qquad
U<7\times10^{-17},
\qquad
D\gamma>1-3\times10^{-8},
$$

gives the rigorous enclosure

$$
\boxed{
2\sum_pq_h(p)^2
<
5\times10^{-29}.
}
\tag{9.3}
$$

Thus the two-MUB collision inequality passes with an enormous margin for every nonzero \(h\).

---

# 10. Every polygon inequality from EdgeAutocorrelation passes

For fixed \(h,s\), put

$$
\ell_p
=
|d_h(p)|\,|d_h(p-s)|
=
\sqrt{r_h(p)r_h(p-s)}.
$$

A complex number \(R\) can be a sum of vectors having lengths \(\ell_p\) only if

$$
\boxed{
\max\{0,2\ell_{\max}-L\}
\le |R|\le L,
\qquad
L=\sum_p\ell_p.
}
\tag{10.1}
$$

This is the complete polygon/reverse-triangle condition.

For \(h\ne0\) and \(s\ne0\),

$$
L\ge D^2\gamma^2>0.99999994.
\tag{10.2}
$$

Also \(r_h(p)\le U\), so

$$
\ell_{\max}\le U<7\times10^{-17}.
$$

Hence

$$
2\ell_{\max}-L<0.
$$

The reverse-triangle lower endpoint is therefore zero.

For the upper endpoint, compare with the baseline \(b\). For \(h,s\ne0\),

$$
\left|
\sum_pr_h^{\,b}(p)\omega^{-[s,p]}
\right|
\le
\frac2{D+1}.
$$

The \(\ell_1\)-difference between the frozen and baseline edge products is bounded by \(\varepsilon_x\). Therefore

$$
\boxed{
\left|
\sum_kr_h(k)\omega^{-[s,k]}
\right|
<
1.07\times10^{-7}.
}
\tag{10.3}
$$

Combining (10.2)–(10.3), every polygon condition passes strictly.

For \(s=0\), EdgeAutocorrelation is the identity \(E_h=E_h\).

---

# 11. The three requested values of \(h\)

## 11.1 \(h=0\)

Here

$$
d_0(p)=x_p^{(10)}.
$$

Since \(x^{(10)}\) is self-Fourier,

$$
\mathscr Fd_0=d_0.
$$

Thus the normalized vector

$$
v_0=\frac{x^{(10)}}{\sqrt{E_0}}
$$

is an explicit pure one-\(h\) solution. Its norm is

$$
\boxed{
E_0
=
\frac{2D}{D+1}
+
\frac{20}{M}
\left(
\mathcal O_{10}-\frac{M}{D+1}
\right).
}
\tag{11.1}
$$

This is the old global self-Fourier identity, not a new physical-lift constraint.

## 11.2 \(z_\star=(0,1)\)

This is nonzero, so all uniform bounds in Sections 8–10 apply:

$$
D^2\gamma^2\le E_{z_\star}<1+1.06\times10^{-7},
$$

the collision expression is below \(5\times10^{-29}\), and every polygon inequality passes.

No exact pure edge phase vector is constructed.

## 11.3 \(h_\star=a_1-a_0\)

One has

$$
t_0=0,\qquad t_1=2P_0+1=970330475.
$$

Using

$$
D=4P_0^2+1,
$$

$$
t_1^2
=
(2P_0+1)^2
\equiv4P_0
=
1940660948
\pmod D.
$$

Therefore

$$
\boxed{
h_\star
=
(970330475,1940660948).
}
$$

It is a nonzero element of \(\Gamma\), and the same uniform certified bounds apply.

---

# 12. Exact analytic two-basis PSD witness

The two-basis rank-relaxed problem asks for a density matrix \(K^{(h)}\) such that

$$
K^{(h)}\succeq0,
\qquad
\operatorname{Tr}K^{(h)}=1,
$$

whose standard-basis diagonal and symplectic-Fourier-basis diagonal both equal \(q_h\).

Let \(\mathsf F\) be the normalized \(D^2\times D^2\) symplectic Fourier matrix,

$$
\mathsf F_{k,p}
=
\frac1D\omega^{[p,k]}.
$$

For \(h\ne0\), define

$$
\boxed{
K^{(h)}
=
\operatorname{Diag}(q_h)
+
\mathsf F^*
\operatorname{Diag}(q_h)
\mathsf F
-
\frac1{D^2}I.
}
\tag{12.1}
$$

Because every entry of a Fourier basis vector has squared modulus \(1/D^2\),

$$
\operatorname{diag}
\left(
\mathsf F^*\operatorname{Diag}(q_h)\mathsf F
\right)
=
\frac1{D^2}\mathbf1.
$$

Hence

$$
\operatorname{diag}K^{(h)}=q_h.
$$

Similarly,

$$
\operatorname{diag}
\left(
\mathsf F K^{(h)}\mathsf F^*
\right)=q_h.
$$

Its trace is

$$
1+1-1=1.
$$

## 12.1 Positivity

Let

$$
q_{\min}=\min_pq_h(p).
$$

From (8.5),

$$
q_{\min}>
\frac1{2D^2}.
$$

Write

$$
q_h=q_{\min}\mathbf1+r,
\qquad r\ge0.
$$

Then

$$
\boxed{
\begin{aligned}
K^{(h)}
={}&
\left(
2q_{\min}-\frac1{D^2}
\right)I\\
&+
\operatorname{Diag}(r)
+
\mathsf F^*\operatorname{Diag}(r)\mathsf F.
\end{aligned}
}
\tag{12.2}
$$

Every term on the right is positive semidefinite. Thus

$$
\boxed{K^{(h)}\succeq0.}
$$

This is an exact analytic primal witness for every nonzero \(h\), including \(z_\star\) and \(h_\star\).

For \(h=0\), the rank-one witness

$$
K^{(0)}
=
|v_0\rangle\langle v_0|
$$

works.

Therefore:

$$
\boxed{
\text{the exact two-basis PSD relaxation is feasible for every }h.
}
$$

It cannot exclude the frozen pseudo-magnitude.

It does not solve the pure edge-vector problem because \(K^{(h)}\) need not have rank one or be supported in the \(+1\) Fourier eigenspace.

---

# 13. Cross-\(h\) rank-one consistency

For \(a,b\in V\), define

$$
Y_{a,b}^{\mathrm{time}}
=
d_{a-b}\!\left(\frac{a+b}{2}\right).
$$

Then

$$
Y_{a,b}^{\mathrm{time}}
=
\alpha_a\overline{\alpha_b}.
$$

Also define

$$
Y_{a,b}^{\mathrm{freq}}
=
\frac1D
\widehat d_{a-b}\!\left(\frac{a+b}{2}\right).
$$

EdgeFourier gives

$$
Y_{a,b}^{\mathrm{freq}}
=
\alpha_a\overline{\alpha_b}.
$$

Hence a physical family must satisfy

$$
\boxed{
Y^{\mathrm{time}}=Y^{\mathrm{freq}}
=\alpha\alpha^*.
}
\tag{13.1}
$$

In particular, the full matrix \(Y\) is positive semidefinite of rank one and has diagonal \(x\).

The rank-one minors give

$$
\boxed{
Y_{a,b}Y_{b,c}
=
x_bY_{a,c},
}
\tag{EdgeCycle}
$$

which is the corrected form of the proposed equation.

---

# 14. Contraction over triples from \(A\)

For pairwise distinct \(a,b,c\in A\), summing EdgeCycle gives

$$
\boxed{
\sum_{\substack{a,b,c\in A\\\mathrm{distinct}}}
Y_{a,b}Y_{b,c}
=
\sum_{\substack{a,b,c\in A\\\mathrm{distinct}}}
x_bY_{a,c}.
}
\tag{14.1}
$$

This is true term by term. It is not \(T_A\), \(T_{\rm ext}\), or `GammaOriented`.

Indeed, the orbit-channel Bargmann term is

$$
\boxed{
\operatorname{Tr}(Q_aQ_bQ_c)
=
\omega^{-([a,b]+[b,c]+[c,a])/2}
\alpha_{a-b}\alpha_{b-c}\alpha_{c-a}.
}
\tag{14.2}
$$

Equation (14.1), by contrast, uses

$$
\alpha_a\overline{\alpha_b}
\alpha_b\overline{\alpha_c}
$$

and contains no Weyl cocycle. It is a rank-one consistency identity for the coefficient field restricted to \(A\), not an orbit moment.

Thus contracting EdgeCycle over \(A\) does not generate a new scalar obstruction.

---

# 15. The smallest explicit cross-\(h\) phase cycle

The first nontrivial cross-\(h\) compatibility condition uses three labels.

Take

$$
a_0=(0,0),
$$

$$
a_1=(970330475,1940660948),
$$

and, since \(r_2=4\),

$$
a_2=(1940660952,15525287596).
$$

Define

$$
Y_{rs}
=
\frac1D
\widehat d_{a_r-a_s}
\!\left(
\frac{a_r+a_s}{2}
\right).
$$

Then a physical family must satisfy

$$
\boxed{
Y_{01}Y_{12}Y_{20}
=
x_{a_0}x_{a_1}x_{a_2}
=
x_{a_1}x_{a_2}>0.
}
\tag{15.1}
$$

Equivalently,

$$
\arg Y_{01}+\arg Y_{12}+\arg Y_{20}=0
\pmod{2\pi}.
$$

The magnitude equality is automatic:

$$
|Y_{01}Y_{12}Y_{20}|
=
x_{a_0}x_{a_1}x_{a_2}.
$$

Thus this minimal triangle detects only phase inconsistency. It gives no magnitude contradiction for \(x^{(10)}\).

Separate one-\(h\) phase retrieval problems do not enforce (15.1). It is the first explicit cross-\(h\) condition that they lose.

---

# 16. Relation to centered idempotence

Although the triangle phase cycle is not one of the Round 22 scalar contractions, the full edge-Fourier family is not a new route around idempotence.

For every \(h\ne0\),

$$
\widehat d_h^\beta(h/2)
=
(D-2)\alpha_h
$$

is exactly `OrientedCoefficient`.

Consequently:

* solving the full centered edge equations at \(k=h/2\) for all \(h\ne0\) is equivalent to centered idempotence;
* `GammaOriented` and `GammaEnergy` are contractions of this diagonal slice over \(h\in\Gamma\);
* the remaining edge conditions consist of:

  1. pure \(+1\)-Fourier phase retrieval for each \(d_h\);
  2. rank-one consistency of the resulting edge fields across different \(h\).

The analytic \(K^{(h)}\) witness proves only that the two-basis **mixed-state** relaxation is too weak. It does not address either of these two surviving conditions.

---

# 17. Earliest exact remaining gap

The edge-Fourier attack reduces the frozen lift problem to the following hierarchy.

## One-\(h\) pure constraint

For every \(h\), find a vector \(d_h\) satisfying

$$
|d_h(p)|^2
=
x_{p+h/2}^{(10)}x_{p-h/2}^{(10)},
$$

and

$$
\boxed{\mathscr Fd_h=d_h.}
\tag{17.1}
$$

All phase-free collision, polygon, support, and mixed-state two-basis tests pass. No such pure vector is constructed for \(h=z_\star\), \(h=h_\star\), or all \(h\).

## Cross-\(h\) constraint

The edge fields must satisfy

$$
d_{a-b}\!\left(\frac{a+b}{2}\right)
d_{b-c}\!\left(\frac{b+c}{2}\right)
=
x_b
d_{a-c}\!\left(\frac{a+c}{2}\right)
$$

for all triples \(a,b,c\).

Equivalently, the matrix assembled from the edge fields must be one common rank-one matrix

$$
Y=\alpha\alpha^*.
$$

## Centered orientation constraint

At the diagonal frequency \(k=h/2\), the centered edge equation is the full oriented idempotence equation.

Thus the first unresolved statement is:

> Do there exist \(+1\)-Fourier edge vectors with the frozen prescribed magnitudes which can be assembled into one common rank-one matrix and whose centered diagonal slices satisfy idempotence?

No contradiction or construction is obtained.

---

# Status of the three closing outcomes

No exact unit vector with

$$
\mathcal F_\Gamma>10
$$

has been produced.

No exact contradiction excluding a physical lift of \(x^{(10)}\) has been produced.

No phase-uniform proof of PW10 has been produced.

Therefore

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

---

# VERIFIED

* `EdgeFourier`, including the half-label and Fourier signs.
* `EdgeFourierMagnitude`.
* The stronger identity

  $$
  \mathscr Fd_h=d_h.
  $$
* \(d_h(-p)=d_h(p)\).
* \(d_{-h}(p)=\overline{d_h(p)}\).
* `EdgeCycle`.
* `CenteredEdgeFourier`, including both endpoint subtractions.
* \(\widehat d_0^\beta(k)=Dx_k-1\).
* `EdgeAutocorrelation`.
* The two-MUB collision inequality.
* The exact values

  $$
  z_\star=(0,1),
  \qquad
  h_\star=(970330475,1940660948).
  $$
* The exact uniform enclosures for every nonzero \(h\).
* Every collision and polygon test for \(z_\star\) and \(h_\star\).
* The analytic two-basis PSD witness \(K^{(h)}\).
* Feasibility of the rank-relaxed two-basis problem for every \(h\).
* The rank-one edge matrix \(Y=\alpha\alpha^*\).
* The minimal three-edge phase cycle.

# CORRECTED

* The new edge relation is not merely equality of time and Fourier probabilities: the edge field itself is a \(+1\) Fourier eigenvector.
* The one-\(h\) PSD relaxation is strictly weaker than the required pure Fourier-eigenvector problem.
* Contracting EdgeCycle over triples in \(A\) is not \(T_A\), \(T_{\rm ext}\), or `GammaOriented`.
* The centered diagonal edge slice is exactly the old oriented centered-idempotence equation.
* The Round 22 shorthand restriction on \(G_\Gamma\) is

  $$
  v\ne u,\qquad v\ne z-u.
  $$

# DISPROVED

* Sufficiency of the two-MUB collision inequality for excluding any nonzero \(h\).
* Sufficiency of all polygon/reverse-triangle autocorrelation inequalities.
* Sufficiency of the rank-relaxed two-basis PSD test.
* Any claim that separate one-\(h\) feasibility automatically supplies one common coefficient field.

# NECESSARY-ONLY

* Pure \(+1\)-Fourier edge phase retrieval for every \(h\).
* The triangle and higher rank-one edge cycles.
* Centered edge idempotence.
* The exact rank-one matrix condition \(Y=\alpha\alpha^*\).

# EQUIVALENT

* `EdgeFourier` and \(\mathscr Fd_h=d_h\).
* The \(k=h/2\) centered edge equation and `OrientedCoefficient`.
* Rank-one cross-\(h\) consistency and vanishing of all \(2\times2\) minors of \(Y\), together with its fixed positive diagonal.

# OPEN

* Pure one-\(h\) Fourier phase retrieval for \(z_\star\).
* Pure one-\(h\) Fourier phase retrieval for \(h_\star\).
* Simultaneous pure edge retrieval for all \(h\).
* Cross-\(h\) rank-one consistency.
* A physical phase lift of \(x^{(10)}\).
* An exact physical vector with objective above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first new claim requiring independent verification is the universal analytic witness

$$
\boxed{
K^{(h)}
=
\operatorname{Diag}(q_h)
+
\mathsf F^*\operatorname{Diag}(q_h)\mathsf F
-\frac1{D^2}I
\succeq0
\qquad(h\ne0),
}
$$

together with the frozen lower bound

$$
\min_pq_h(p)>\frac1{2D^2}.
$$

<!-- END HISTORICAL FILE path=artifacts/web-gpt56sol-pro/round-23-response.md -->

## AUDIT

<!-- BEGIN HISTORICAL FILE path=outputs/round-23-local-audit.md bytes=7999 sha256=6d1cd626d818e0652039ba30b28ad677505114800f9c9cd73d38e3100dd540a6 -->

# Round 23 local audit

## Verdict

`PARTIAL ADVANCE — ONE CORRECTION — PW10 OPEN`

Round 23 produced a valid analytic witness showing that the rank-relaxed
two-basis marginal test is feasible for every frozen edge `h`. More
importantly, the edge identity strengthens to the exact eigenvector equation

\[
\mathscr F d_h=d_h.
\]

The response did not construct a pure edge vector for either requested
nonzero edge, did not assemble a common rank-one coefficient matrix, and did
not prove or disprove PW10. Its final open status is therefore correct.

There is one definite but non-central error: for the antisymmetric symplectic
Fourier kernel used here, `mathscr F^2=I`, not phase-space reflection.
Evenness of `d_h` follows from Hermiticity of `alpha`, not from squaring this
Fourier transform.

## Capture receipt

- Browser completion indicator: `Worked for 11m 26s`.
- Exact response copies:
  `artifacts/web-gpt56sol-pro/round-23-response.md` and
  `outputs/round-23-gpt56sol-pro-response.md`.
- Both response files are byte-identical to the browser `Copy response`
  payload.
- Response SHA-256:
  `a599b8aaf756c1aef06ce7f78582f59f9cf22d56c98a4f02e8794c1a1ff3688e`.
- Response size: 21,755 Unicode characters, 21,761 bytes, and 1,388 newline
  characters.
- Prompt source and archived sent copy are byte-identical, with SHA-256
  `d996deb7742792dde8266db941a061bf70122969ecd5a7ee66322d669b046fc0`.
- The browser-copied send payload equals the prompt with its single terminal
  newline removed; its SHA-256 is
  `580f65c1831025fef65340d79f7b64dd8242ae9299fb151fde56868370102eb4`.

## VERIFIED

### 1. Edge Fourier and the stronger eigenvector identity

The independently checked identity is

\[
\widehat d_h(k)
=D\alpha_{h/2+k}\alpha_{h/2-k}.
\]

Hermiticity gives

\[
\alpha_{h/2-k}=\overline{\alpha_{k-h/2}},
\]

so its right side is exactly `D d_h(k)`. With the normalized symplectic
Fourier transform

\[
(\mathscr Ff)(k)=D^{-1}\sum_p f(p)\omega^{[p,k]},
\]

this proves `mathscr F d_h=d_h`. The half-labels and signs were also
reproduced by direct random-projector checks at `D=3,5,7`.

The separate relations

\[
d_h(-p)=d_h(p),\qquad
d_{-h}(p)=\overline{d_h(p)}
\]

follow directly from `alpha_{-z}=conjugate(alpha_z)`.

### 2. Centering and autocorrelation

Removing the two endpoint terms `p=plus_or_minus h/2` gives the stated
`CenteredEdgeFourier` equation. At `k=h/2` its phase factor is one and it
reduces exactly to

\[
\sum_u\beta_u\beta_{h-u}\omega^{[u,h]/2}
=(D-2)\beta_h,
\]

the previously audited oriented centered-idempotence coefficient equation.
The `h=0` formula `widehat d_0^beta(k)=D x_k-1` is also correct.

Parseval with `D^2` phase-space points gives the stated exact
`EdgeAutocorrelation` identity, including the negative Fourier sign.

### 3. Frozen pointwise and energy bounds

Using the exact Sidon-spectrum bound `-m <= lambda_z <= M`, every nonzero
entry obeys

\[
\gamma\le x_z^{(10)}\le U,
\]

where

\[
\gamma=
\frac{D(m-11)-10m}{D(D+1)(m-1)},
\qquad
U=\frac{11}{D+1}+\frac{10}{M}.
\]

Exact rational checks give

\[
U=5.4166514736151412\times10^{-17}<7\times10^{-17},
\]

\[
D\gamma=0.9999999793884637\ldots>1-3\times10^{-8}.
\]

The previously derived exact norm relation for `eta=x-b`, together with
`O_10<=M U`, yields

\[
\|\eta\|_2^2
\le \frac{200}{D+1}+\frac{200}{M}
<\frac{49}{4\cdot10^{16}}.
\]

Exact squaring, with no floating-point square-root inference, verifies

\[
2\|b\|_2\|\eta\|_2+\|\eta\|_2^2
<\frac{53}{5\cdot10^8}.
\]

Consequently, for every nonzero `h`,

\[
D^2\gamma^2\le E_h<1+1.06\times10^{-7},
\]

and the checked lower endpoint is

\[
D^2\gamma^2=0.9999999587769279\ldots.
\]

### 4. Phase-free one-edge tests

The two distributions are identical because `x` is even:

\[
q_h(p)=\widetilde q_h(p).
\]

The response's crude but rigorous collision bound is valid. Direct exact
rational evaluation of its stated envelope gives

\[
2\sum_pq_h(p)^2
<1.5274468280089911\times10^{-29}
<5\times10^{-29}.
\]

For every nonzero shift, all edge-product lengths are positive and their
total is at least `D^2 gamma^2`, whereas twice the largest length is below
`2U`. Thus the reverse-triangle endpoint is zero. The frozen
autocorrelation target is bounded by

\[
\frac2{D+1}+\frac{53}{5\cdot10^8}
<1.07\times10^{-7}
<D^2\gamma^2,
\]

so each individual polygon test passes. These are only separate
autocorrelation tests; they do not ensure a single globally consistent phase
assignment.

The exact computations of `h_star` and the third Sidon label are correct:

\[
h_\star=(970330475,1940660948),
\]

\[
a_2=(1940660952,15525287596).
\]

### 5. Analytic two-basis PSD witness

Let `N=D^2`, and let `F` be the normalized symplectic Fourier matrix. The
proposed matrix

\[
K^{(h)}=\operatorname{Diag}(q_h)
+F^*\operatorname{Diag}(q_h)F-N^{-1}I
\]

has trace one and diagonal `q_h` in both bases. The exact frozen bounds imply

\[
q_{\min}\ge\frac{\gamma^2}{E_h}>rac1{2N}.
\]

Writing `q_h=q_min 1+r`, with `r>=0`, gives

\[
K^{(h)}=
(2q_{\min}-N^{-1})I
+\operatorname{Diag}(r)
+F^*\operatorname{Diag}(r)F\succeq0.
\]

This proof is exact and applies to every nonzero `h`. The matrix identities
and decomposition were also checked numerically at `D=3,5,7`.

### 6. Cross-edge rank-one consistency

The reconstruction

\[
Y_{a,b}=d_{a-b}((a+b)/2)
=D^{-1}\widehat d_{a-b}((a+b)/2)
=\alpha_a\overline{\alpha_b}
\]

is correct. It implies

\[
Y_{a,b}Y_{b,c}=x_bY_{a,c}
\]

and the three-label phase cycle. Its magnitude is automatic, so the
displayed triangle gives no magnitude-only contradiction for the frozen
pseudo-point. It is a genuine condition lost when the edge problems are
relaxed independently.

The response also correctly distinguishes this raw coefficient-matrix cycle
from the Weyl-cocycle-weighted orbit Bargmann moment. Summing a termwise
rank-one identity over triples in `A` does not create a new scalar
obstruction.

## CORRECTED

The sentence saying that the Fourier eigenvalue equation implies evenness
because `mathscr F^2` is reflection is false for the transform actually used.
Antisymmetry gives

\[
\begin{aligned}
(\mathscr F^2f)(\ell)
&=\frac1{D^2}\sum_{p,k}f(p)
  \omega^{[p,k]+[k,\ell]}\\
&=\frac1{D^2}\sum_{p,k}f(p)\omega^{[p-\ell,k]}\\
&=f(\ell).
\end{aligned}
\]

Thus

\[
\boxed{\mathscr F^2=I.}
\]

This does not invalidate `mathscr F d_h=d_h`, the PSD witness, or the direct
Hermiticity proof of `d_h(-p)=d_h(p)`.

## NECESSARY-ONLY / TOO WEAK

- The collision and individual polygon inequalities are necessary but far
  from excluding either requested nonzero edge.
- The analytic `K^(h)` is a mixed-state marginal witness. It need not have
  rank one and need not be supported in the `+1` Fourier eigenspace.
- Separate pure edge solutions, even if found, still have to assemble into
  one Hermitian rank-one matrix with the fixed diagonal `x`.
- The three-edge phase cycle is not numerically evaluable from magnitudes
  alone.

## OPEN / earliest gap

No exact violating vector, no exact exclusion of `x^(10)`, and no
phase-uniform proof of PW10 was produced. The earliest sharpened gap is:

1. for a selected nonzero `h`, does an even `+1` symplectic-Fourier
   eigenvector exist with squared magnitudes `r_h`;
2. if separate edge vectors exist, can they satisfy the common rank-one
   cross-edge cycles and centered idempotence simultaneously?

Therefore

\[
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
\]

## Local verification artifacts

- `work/verify_round23_pre_send.py`: prompt integrity and frozen arithmetic.
- `work/verify_round23_edge_fourier.py`: direct projector checks at
  `D=3,5,7`.
- `work/verify_round23_web_response.py`: exact capture, rational bounds,
  collision envelope, polygon margins, and the Fourier-square correction.
- `work/verify_round23_psd_witness.py`: Fourier involution, two-basis
  diagonals, trace, PSD decomposition, and small-prime quadratic-form checks.

All four scripts pass `py_compile` and their executable assertions.

<!-- END HISTORICAL FILE path=outputs/round-23-local-audit.md -->

