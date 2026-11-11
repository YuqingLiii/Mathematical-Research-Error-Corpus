# Independent review: dimension-certified carrier inequality

Date: 2026-07-22  
Reviewed source: `artifacts/logs_se_trace_t5_carrier_dimension_20260722/`  
Corrected predecessor: `artifacts/logs_se_trace_t5_carrier_aware_tb_20260722/`

## Overall verdict

**PARTIAL**, with the following claim-level decisions.

| Claim | Independent verdict |
|---|---|
| `f^kappa f^nu c <= T` implies `R_h<=B_theta(q)T` | **CONFIRMED, uniformly and for all `c` subject to the dimension gate** |
| The same gate implies the registered physical `T-b` cap | **CONFIRMED**, using the already confirmed output-frame inequality |
| Complete admissible `j<=2` carrier layer | **CONFIRMED uniformly** |
| Arbitrary-`j,theta` extreme faces `a=0` and `b=0` | **CONFIRMED uniformly** |
| Two mixed `j=2` exact Rayleigh ratios | **CONFIRMED** |
| Four `n=9,j=3` dimension-excess probes | **REPRODUCED as numerical physical probes only** |
| Carrier inequality on all dimension-excess sectors | **OPEN / NOT PROVED** |
| Two tame `c=2` gates | Dimension condition is **not necessary**; no uniform `c>=2` inference |
| Corrected carrier-aware dependency declaration | **CONFIRMED fixed** |

No physical `T-b` counterexample is present. T5 is not completed by this
packet.

## 1. Operator and type audit

Let `m=binomial(j,a)`. For each uncoloured set `L`, the raw fold has one
orthogonal input summand for each of its `m` colourings:

`F_L=[U_1 ... U_m]`,

where every `U_i` is unitary onto the same output fibre. Therefore

`F_L F_L^*=sum_i U_iU_i^*=mI`.

Consequently `F~=F/sqrt(m)` is a coisometry. The review script checks this
exactly for 30 independent signed-permutation block systems and also verifies
that `F~^*F~` is an orthogonal projection. This normalization is consistent
with the common-line review: changing from raw `F` to `F~` moves the
compensating `sqrt(m)` into the branch scalar without changing the physical
map.

Write `A=F~L_h`. Equivariance and the unitary isotypic decomposition give

`A=direct_sum_mu I_(V_mu) tensor A_mu`,

and hence

`||A||_HS^2=sum_mu f^mu ||A_mu||_HS^2`.

The independently reviewed fixed-`mu` common-line normalization identifies
`||A_mu||_HS^2=r_mu`. Thus

`R_h=sum_mu f^mu r_mu=||F~L_h||_HS^2`.

No colour-diagonal pinching or eigenvalue surrogate occurs here; the coherent
cross-colour terms remain inside `F~L_h`.

On the carrier `C=P_xi V_lambda`,

`L_h^*L_h=P_C(sum_D Pi_D)P_C`.

The physical `D` family is a positive subfamily of the complete fixed-set
frame. Compression of its exact frame identity therefore yields

`L_h^*L_h <= B_theta(q) I_C`.

The Hilbert--Schmidt trace is where the carrier dimension must be retained:

`R_h <= ||L_h||_HS^2 <= B_theta(q) dim(C)`

`=B_theta(q) f^kappa f^nu c`.

There is no missing or removable dimension factor. Therefore

`f^kappa f^nu c <= T  =>  R_h<=B_theta(q)T`.

Together with the confirmed common-line physical identity and output-frame
bound from the corrected carrier-aware packet, this implies

`T_b<=B_theta(q)R_h/(delta_min+1)<=B_theta(q)^2T/(delta_min+1)`.

This proves physical `T-b` only for dimension-certified sectors, not for all
parameters.

## 2. Independent dimension algebra

The review imports no proposer module. It computes representation dimensions
with the Frobenius/Vandermonde formula

`f^lambda=N! product_(i<j)(l_i-l_j)/product_i l_i!`,

where `l_i=lambda_i+r-i`, rather than the source's hook-cell routine.

For `j=2`, all six admissible sectors have `c=1`; the exact ratios are
independently recovered as

| `theta` | `a,b` | `f^kappa f^nu/T` |
|---|---:|---:|
| `(2)` | `0,2` | `n(n-3)/((n-1)(n-2))` |
| `(2)` | `1,1` | `1` |
| `(2)` | `2,0` | `(n-4)/(n-2)` |
| `(1,1)` | `0,2` | `1` |
| `(1,1)` | `1,1` | `1` |
| `(1,1)` | `2,0` | `(n-3)/(n-1)` |

All are at most one for every `n>=6`. Exact independent checks cover every
`n=6,...,80`. Together with the extreme-face proof for `j=1`, this confirms
the complete `j<=2` uniform claim.

For `b=0`, Pieri makes `V_kappa` a constituent of
`Ind_(S_j x S_(n-1-j))^(S_(n-1))(V_theta tensor 1)`, so its dimension is at
most the induction dimension `binomial(n-1,j)f^theta=T`.

For `a=0`, a standard tableau of `(n-j,theta)` is injected into the pair
consisting of its `j` lower-row labels and their standardized `theta` tableau.
The lower labels lie in `{2,...,n}`, giving
`f^nu<=binomial(n-1,j)f^theta=T`. These are uniform arguments, not finite
interpolation. As a separate check, 1,626 Frobenius-formula instances pass for
`j<=12` at `n=3j,3j+1,3j+5`.

## 3. Independent mixed `j=2` calculation

For the mixed carrier, identify it with the row- and column-zero subspace of
`p x n` matrices, `p=n-1`. The orthogonal projection of a matrix unit obeys

`||P E_ij||^2=(n-2)/n`,

`<P E_ij,P E_ji>=1/[n(n-1)]` for `i!=j`.

The row shape uses the `+` coherent fold and the column shape the `-` fold.
There are `binomial(p,2)` output fibres; the normalized fold contributes
`1/2`, and the common frame scalar cancels against `B_theta`. This gives

`R_h/(B_(2)T)=(n^2-3n+3)/(2n(n-1))`,

`R_h/(B_(1,1)T)=(n^2-3n+1)/(2n(n-1))`.

The derivation is exact and independent of the source's hard-coded formulas.
It passes symbolically reduced rational checks for `n=6,...,150`; at `n=6`
the values are exactly `7/20` and `19/60`.

## 4. First dimension excess and `c=2` scope

The size-three Pieri products independently recover the four first excess
sectors at `n=9,j=3,a=1,b=2`. Their dimension ratios are

`9/8, 9/8, 7/6, 7/6`.

Thus the dimension proof genuinely stops before these sectors. The isolated
physical probe rerun reproduces all four archived results byte-for-byte:

`51/224, 3/14, 25/108, 47/216` as numerical rational-recovery candidates.

They are **not exact theorems**. Their archived carrier residuals and spectral
gaps support the numerical construction, but neither four points nor their
rational approximants prove a uniform `j=3` statement.

For the two tame `c=2` sectors, independent Frobenius dimensions give

`dc/T=3` at `n=18`, and `dc/T=38/13` at `n=19`.

The dimension condition fails while the independently checked carrier and
physical `T-b` gates pass. This proves only that the dimension condition is
sufficient rather than necessary. It does not prove uniform `c>=2`.

## 5. Integrity, corrected predecessor, and isolation

- The dimension packet manifest passes `9/9`; the corrected carrier-aware
  packet passes `6/6`.
- Every declared dependency manifest passes. The full isolated closure also
  includes the repository-level `artifacts/se_bigate_20260719.md` target named
  by the bigate manifest.
- Both verifiers pass under the isolated repository root.
- The dimension generator, corrected carrier-aware generator, and `j=3`
  physical probe reproduce their archived JSON and log files byte-for-byte.
- The corrected carrier-aware JSON now explicitly declares and verifies
  `logs_se_trace_t3_expanded_spectra_20260721`. The omission found by the
  earlier review is fixed in the current source packet.

One provenance boundary is worth retaining: the standalone probe verifies
the sweep and bigate manifests, while the sweep imports the T1 enumeration
module transitively. The dimension theorem entry point declares and verifies
that T1 packet, and this review verifies it independently. Thus the full
artifact closure is covered, although the probe entry point alone does not
enforce the transitive T1 hash.

## Strict scope

The uniform theorem is precisely the dimension-certified implication and its
proved `j<=2` and extreme-face consequences. General dimension-excess
carrier control, all-`c=1`, and uniform `c>=2` remain open. The four `j=3`
rows are numerical probes only, and the two exact `c=2` gates establish
non-necessity of the sufficient condition only.

