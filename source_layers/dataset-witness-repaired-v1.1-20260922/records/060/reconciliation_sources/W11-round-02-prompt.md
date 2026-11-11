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

