# Independent review: T5 common Pieri line and actual-sum compression

Date: 2026-07-21  
Reviewed node: `SE.denom.Phi.legal.trace.t5`  
Review scope: only `artifacts/logs_se_trace_t5_common_line_20260721/` and the
registered T5/T3, direction-law, majorization, and physical-factorization
dependencies needed to check its definitions

## Verdict

**CONFIRMED**, with the verdict restricted exactly as follows.

| statement | independent verdict |
|---|---|
| registered physical factorization `S_gamma=b_gamma Q_gamma JF` | **CONFIRMED** |
| fixed-`mu` common Pieri line / branch cross-Gram rank at most one | **CONFIRMED, all `c`** |
| exact long and complete multi-tail actual-sum compression | **CONFIRMED, all `c`** |
| uniform (T-a)/(T-b) caps | **NOT PROVED; remains OPEN** |
| T5 as a completed route | **NOT CONFIRMED; remains OPEN** |

The theorem is a structural exact identity.  It removes the common-line
recoupling residual, but it does not control the resulting scalar masses.
The recommended node status is therefore **T5 stays OPEN**, while the
common-line and actual-sum-compression subclaims may be recorded as
independently reviewed `PROVED` facts.

## 1. Registered types and the physical factorization

The registered source definition is R3b.23:

\[
 S_{h,\gamma}(y_D)_D
 =P_{\rm comp}\sum_D\rho_JQ_\gamma y_D,
 \qquad D=(I,J),\quad L=I\cup J.
\]

On a normalized colored fiber isometry `E_D`, its block is therefore

\[
 P_{\rm comp}\rho_JQ_\gamma E_D.                       \tag{1}
\]

This is not a new model introduced by the common-line report.  It is the
literal registered physical block.  In the registered convention the extra
scalar is `b_gamma=1`; a later branch normalization may be represented by a
scalar independent of `D`.

Every `rho_J` fixes the query, and every element of the completion subgroup
also fixes the query.  Both are therefore in the `S_(q-1)` group algebra in
which `Q_gamma` is central.  Consequently

\[
 [Q_\gamma,\rho_J]=[Q_\gamma,P_{\rm comp}]=0.             \tag{2}
\]

Transport maps the full fixed-set fiber for
`D=I union bar(J)` unitarily onto the full fixed-set fiber for the uncolored
set `L=I union J`.  For arbitrary normalized fiber gauges there is therefore
a unitary internal matrix on `V_theta`,

\[
 \rho_JE_D=E_LU_D.                                        \tag{3}
\]

The internal matrix need not be scalar when `f^theta>1`; no scalarization is
used.  Define the raw physical fold

\[
 (Fx)_L=\sum_{D:\,I\cup J=L}U_Dx_D,
 \qquad J|_L=P_{\rm comp}E_L.                              \tag{4}
\]

Substituting (2)--(4) into (1), block by block and then summing, gives

\[
 \boxed{S_\gamma=Q_\gamma JF}.                             \tag{5}
\]

If `F` is divided by `sqrt(binomial(j,a))`, (5) instead has the compensating
scalar `b_gamma=sqrt(binomial(j,a))`.  This changes coordinates and branch
normalization, not the physical map.

### Precise equivariance point

There is a small point worth stating more explicitly than the proposer did.
For diagonal `g in S_(n-1)`, the permutations

`rho_(gJ) g_diag` and `g_unbar rho_J`

need not be equal on the whole ambient alphabet.  Their quotient fixes every
point of the colored set `D`, hence lies in the complement subgroup averaged
by `Pi_D`.  They are therefore exactly equal **on `Ran Pi_D`**.  This is the
required fiber covariance and proves that the canonical fold `F` is
`S_(n-1)`-equivariant.  The independent script checked this quotient/fiber
statement in 31,287 instances through `n=6`.

This clarification repairs no false step: the report says “natural
transport makes `F` equivariant,” which is correct.  It only identifies the
exact level on which the equality holds.

## 2. Pieri compression and the fixed-`mu` line

The uncolored intermediate module is

\[
 \mathscr Y=\operatorname{Ind}_{S_j\times S_{p-j}}^{S_p}
 (V_\theta\boxtimes\mathbf1).
\]

Pieri gives

\[
 \mathscr Y=\bigoplus_\mu
 c^\mu_{\theta,(p-j)}V_\mu,
 \qquad c^\mu_{\theta,(p-j)}\in\{0,1\}.                    \tag{6}
\]

The independent audit enumerated 876 `(p,j,theta)` rows through `p=12` and
checked both the horizontal-strip `0/1` criterion and the dimension identity

\[
 \binom pjf^\theta
 =\sum_{\mu:\,\mu/\theta\ {m horizontal}}f^\mu.
\]

Thus for
`X_mu = V_mu tensor C^(m_mu^X)`, Schur's lemma forces

\[
 F|_\mu=I_{V_\mu}\otimes\varphi_\mu,
 \qquad \varphi_\mu:\mathbb C^{m_\mu^X}\to\mathbb C.      \tag{7}
\]

Every physical branch post-composes the same row `varphi_mu`.  In the
registered T3 output typing the branch output is itself Pieri
multiplicity-free, so its reduced map is literally
`s_(gamma,mu)=d_(gamma,mu)varphi_mu`.  Even without output
multiplicity-freeness, factorization through the one-copy intermediate
would still give a column times this same row and the same rank-one input
Gram; hence the conclusion does not depend on an unnoticed output
scalarization.

It follows that all active adjoint branch vectors have the form

\[
 v_{\gamma\mu}=\overline{d_{\gamma\mu}}\varphi_\mu^*,
\]

and the complete long-plus-all-tails cross-Gram at fixed `mu` has rank at
most one.  All two-branch Gram determinants are exactly zero.  This remains
true for `m_mu^X>1` and for any number of tail corners.

## 3. Exact actual-sum compression

Let

\[
 u_\mu={\varphi_\mu^*\over\|\varphi_\mu\|},\qquad
 r_\mu=\|\ell_\mu^*u_\mu\|^2,qquad
 a_{\gamma\mu}=\|v_{\gamma\mu}\|^2,
\]

with `r_mu=0` when the common row vanishes.  Direct substitution gives the
formal identity

\[
 \boxed{\|\ell_\mu^*v_{\gamma\mu}\|^2
 =a_{\gamma\mu}r_\mu}.                                    \tag{8}
\]

Therefore

\[
 \operatorname{Tr}(A_0D_h)
 =\sum_\mu f^\mu a_{0\mu}r_\mu,
\]

\[
 \operatorname{Tr}(A_{\rm tail}D_h)
 =\sum_\mu f^\mu r_\mu\sum_z a_{z\mu}.                    \tag{9}
\]

Equation (9) retains the complete tail sum and never replaces it with a
maximum.  The rerun recovers the exact killer values
`408935/2744` and `7633/24696`; its killer gate includes both tail children.

## 4. Multiplicities, phases, and gauges

### `c`-independence

The LR multiplicity `c=c_(alpha,beta)^theta` indexes carrier copies in the
domain of

\[
 \ell_\mu:\mathbb C^{m_\mu^C}\to\mathbb C^{m_\mu^X}.
\]

It is not a copy index in `X`, `F`, or `S_gamma`.  The proof of (5)--(9)
places no restriction on the number of columns of `ell_mu`.  Hence the
common-line and actual-sum identities are genuinely all-`c` statements.

This does **not** construct the missing `c=2` `ell_mu`, evaluate its actual
sum, or prove a cap.  Thus the structural all-`c` theorem is consistent with
the T5 node's still-unmet `23296 x 1120` computational obligation.

### Independent hostile algebra

The independent audit used an exact complex model with
`m_X=4`, `m_C=3`, one long branch, and three tail branches.  Its common
Rayleigh factor was `321/34`; the direct and compressed positive weighted
sums both equaled `35631/4`.  This exercises more than one carrier column,
more than one input multiplicity direction, a genuine multi-tail sum, and
nontrivial relative complex phases.

### Gauge and phase invariance

An `X`-multiplicity gauge transforms `ell_mu` and every `v_(gamma,mu)` by the
same left unitary.  A carrier gauge right-multiplies `ell_mu`.  A branch phase
multiplies one `v_(gamma,mu)` by a unit scalar.  An uncolored-fiber gauge
inserts mutually inverse unitaries between `J` and `F`.  The cross-Gram rank,
all norms, (8), and (9) are invariant in each case.  The independent exact
model checked all three nontrivial matrix/phase transformations.

## 5. What is formal, conditional, and still unproved

| class | content |
|---|---|
| formal consequence of registered definitions | transport to uncolored fibers; `Q_gamma` commutation; `S_gamma=Q_gamma JF`; Pieri one-copy intermediate; fixed-`mu` common row; (8)--(9); all-`c`, multi-tail, and gauge invariance |
| explicit hypotheses already satisfied by the registered physical model | full colored fixed-set fibers are retained; `Q_gamma` is the central child projector; branch normalization is independent of `D`; query is not moved by `rho_J` or completion |
| would need a new hypothesis in a different model | a noncentral child operator, a `D`-dependent branch scalar, deletion of fiber/LR directions from `X`, or a transport moving the query would not be covered |
| not proved here or by the proposer theorem | either uniform (T-a)/(T-b) scalar cap; an explicit multiplicity-resolved `c>=2` `ell_mu`; any claimed numerical `c>=2` bound; completion of T5/TRACE |

No additional hidden assumption was found relative to the registered T3/T5
physical definitions.

## 6. Gate and hash audit

All three source manifests passed before rerun:

- `logs_se_trace_t5_common_line_20260721`: PASS;
- `logs_se_trace_t5_direction_law_20260721`: PASS;
- `logs_se_trace_t3_majorization_20260721`: PASS.

The proposer exact gate was rerun into this review directory, without
overwriting its source outputs.  It passed both exact color folds, all six
hostile Gram determinants (including both `m_X=2` standard blocks), and all
three actual-sum reconstructions.

The exact fold gates use `theta=(2)` and `(1,1)`, so their fiber dimension is
one and they do not by themselves test a nonscalar internal `U_D`.  The
general fiber-unitary proof above covers arbitrary `f^theta`; the independent
transport quotient audit checks its gauge-free covariance.  The proposer's
supporting numerical `theta=(2,1)`, `f^theta=2`, two-tail probe was also
rerun and returned combined rank `8` under its predicted rank cap `9`.
That numerical probe is supporting evidence only and is not needed for the
verdict.

## 7. Status recommendation

Keep `SE.denom.Phi.legal.trace.t5` **OPEN**.  Its current text should, when a
controller next edits it, distinguish:

1. fixed-`mu` common Pieri line and actual-sum compression: **PROVED and now
   independently CONFIRMED, all `c`**;
2. actual uniform (T-a)/(T-b) scalar inequalities: **OPEN**;
3. explicit `c>=2` carrier/`ell_mu` construction and cap gate: **UNTESTED**.

No DAG, notes, handoff, paper, `research/ksum` file, or git history was
modified by this review.
