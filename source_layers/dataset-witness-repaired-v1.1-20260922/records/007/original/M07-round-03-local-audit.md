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
