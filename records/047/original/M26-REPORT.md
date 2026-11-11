# T5 physical long cap: exact solvable faces and the uniform residual

Date: 2026-07-21  
Node: `SE.denom.Phi.legal.trace.t5`  
Write scope: this artifact directory only

## Verdict

**STILL BLOCKED** for the requested uniform admissible tame statement over
all parameters and all LR multiplicities `c`.

The following direction-sensitive statements are proved here.  They start
from the independently confirmed common-line compression

\[
 T_a=\sum_\mu f^\mu a_{0\mu}r_\mu,
 \qquad r_\mu=\|\ell_\mu^*u_\mu\|^2,
 \qquad a_{0\mu}=\|v_{0\mu}\|^2.                    \tag{1}
\]

No decreasing-eigenvalue global or isotype von Neumann surrogate occurs in
any proof, gate, or verdict.

| statement | verdict |
|---|---|
| common Pieri line and (1), every `c` | **PROVED and independently confirmed upstream** |
| all `j=1`, both orientations | **PROVED** |
| arbitrary `j,theta` on the pure-unbarred face `b=0` | **PROVED** |
| arbitrary `j` on the pure-barred column face `a=0, theta=(1^j)` | **PROVED** |
| every remaining mixed/non-column sector, uniformly in tame `n` and `c` | **STILL BLOCKED** |

Thus the exact `j=1` patterns in the 59-row sweep were not numerical
coincidences.  The two ratios are

\[
 \boxed{\frac{T_a}{B_\theta(q)^2T}=\frac{n-2}{n-1}}
 \quad(a,b)=(1,0),                                      \tag{2}
\]

\[
 \boxed{\frac{T_a}{B_\theta(q)^2T}=\frac{2n-3}{2n-1}}
 \quad(a,b)=(0,1).                                      \tag{3}
\]

Both tend to one from below.  Any uniform proof that spends a fixed positive
fraction of the cap is therefore impossible.

## 1. The exact `j=1` reduced masses

Put `q=2n` and `B=q/(q-1)`.  Realize
`V_(q-1,1)` as the standard space `1^perp` in `C^q`.  For a point `d`, the
normalized fixed-point fiber vector is

\[
 u_d=\sqrt{\frac q{q-1}}\left(e_d-\frac1q\mathbf1\right). \tag{4}
\]

The query-child projector sends an unqueried point vector to

\[
 Q_0u_i=\sqrt{\frac q{q-1}}
 \left(e_i-\frac1{q-1}\mathbf1_{[q]\setminus\{*\}}\right). \tag{5}
\]

### Unbarred orientation

Here the carrier is the `S_(n-1)` standard representation.  Its coordinates
sum to zero, so the constant term in (5) cancels after the physical state
sum.  The physical long block is exactly `B` times an isometry.  There is one
active isotype,

\[
 \mu=(n-2,1),\qquad f^\mu=n-2,qquad
 a_{0\mu}=B,\qquad r_\mu=B.                              \tag{6}
\]

Therefore `T_a=(n-2)B^2`; since `T=n-1`, (2) follows.

### Barred orientation

The `B`-standard carrier restricted to the matched `S_(n-1)` splits into its
matched standard part and the unmatched-point contrast line.  Directly from
(4)--(5), the source frame eigenvalues are `B` and `B/n`, respectively.
The exact common-line masses are

\[
\begin{array}{c|c|c|c}
 \mu&f^\mu&a_{0\mu}&r_\mu\\ \hline
 (n-2,1)&n-2&B&B\\
 (n-1)&1&B^2/2&B/n
\end{array}                                               \tag{7}
\]

so

\[
 T_a=B^2\left(n-2+\frac1{q-1}\right).
\]

Dividing by `B^2(n-1)` gives (3).  This is the actual physical direction
decomposition, including the unmatched-point direction; it is not a
spectrum rearrangement.

## 2. General `j`: the complete pure-unbarred face

Let `b=0`.  Then `alpha=theta`, `beta=empty`, `c=1`, and

\[
 \kappa=(n-1-j,\theta),\qquad \nu=(n).
\]

The physical `j`-sets are the complete `S_(n-1)` orbit in `A^circ`.  Hence
the reviewed free-orbit frame identity is an equality rather than only the
positive sub-orbit inequality.  Its sum is `H`-central.  On the unique
`(kappa,nu)` carrier it gives

\[
 \sum_{I\subset A^\circ,\ |I|=j}\Pi_I P_\xi
   =B_\theta(q)P_\xi.                                    \tag{8}
\]

The carrier is `S_B`-fixed and belongs only to the long query child
`tau_0=(q-j-1,theta)`; thus `P_comp` and `Q_0` act as the identity in (8).
Consequently the literal physical block satisfies

\[
 B_{h,0}=B_\theta(q)P_\xi,
 \qquad
 T_a=B_\theta(q)^2f^{(n-1-j,\theta)}.                     \tag{9}
\]

Since `T=binom(n-1,j)f^theta`, the exact ratio is

\[
 \boxed{
 \frac{T_a}{B_\theta(q)^2T}
 =\frac{f^{(n-1-j,\theta)}}{\binom{n-1}{j}f^\theta}<1.}    \tag{10}
\]

The inequality is also a purely combinatorial proof: the denominator is the
dimension of

\[
 \operatorname{Ind}_{S_j\times S_{n-1-j}}^{S_{n-1}}
 (V_\theta\boxtimes\mathbf1),
\]

and Pieri makes `V_(n-1-j,theta)` one proper constituent.  Formula (10) is a
hook-length closed form for arbitrary `theta`.  When `theta` itself is a
hook, it simplifies to

\[
 \frac{n-\theta_1-j}{n-\theta_1}.                         \tag{11}
\]

This includes the sweep's `j<=3` patterns; (11) is not asserted for a
non-hook shape such as `(2,2)`.

## 3. General `j`: the pure-barred column face

Let `a=0` and `theta=(1^j)`.  Use the exact hook model

\[
 V_{(q-j,1^j)}=\bigwedge^j\mathbf1_q^\perp.                \tag{12}
\]

For a `j`-set `D`, a normalized fixed-fiber Pluecker vector is

\[
 u_D=\sqrt{\frac q{q-j}}
 \bigwedge_{d\in D}\left(e_d-\frac1q\mathbf1\right).      \tag{13}
\]

The determinant of the cross Gram in (13) vanishes unless two sets are
equal or differ by one point.  After projection to the barred carrier and
to the long query child, the exact equal/adjacent Gram values are

\[
 g_{\rm in}^{=}=\frac{q(n-j)}{n(q-j)},\quad
 g_{\rm in}^{\sim}=-\frac q{n(q-j)},                       \tag{14}
\]

\[
 g_{\rm out}^{=}=\frac{q(q-j-1)}{(q-j)(q-1)},\quad
 g_{\rm out}^{\sim}=-\frac q{(q-j)(q-1)}.                 \tag{15}
\]

There are `M=binom(n-1,j)` diagonal ordered pairs and
`M j(n-1-j)` adjacent ordered pairs.  Thus the literal physical orbital sum
is

\[
\begin{aligned}
 T_a
 &=M\left(g_{\rm in}^{=}g_{\rm out}^{=}
       +j(n-1-j)g_{\rm in}^{\sim}g_{\rm out}^{\sim}\right)\\
 &=B_\theta(q)^2M\frac{q-2j-1}{q-1},
 \qquad B_\theta(q)=\frac q{q-j}.                          \tag{16}
\end{aligned}
\]

Equivalently, restriction to the matched `S_(n-1)` has two isotypes and the
actual products `a_(0,mu)r_mu` are

\[
\begin{array}{c|c|c}
 \mu&f^\mu&a_{0\mu}r_\mu\\ \hline
 (n-1-j,1^j)&\binom{n-2}{j}&B_\theta(q)^2\\
 (n-j,1^{j-1})&\binom{n-2}{j-1}&B_\theta(q)^2/(q-1).
\end{array}                                                \tag{17}
\]

Therefore

\[
 \boxed{\frac{T_a}{B_\theta(q)^2T}
 =\frac{2n-2j-1}{2n-1}<1.}                                \tag{18}
\]

For `j=1`, (17) specializes to the two products in (7).

## 4. Smallest separable uniform residual

The common-line theorem has removed the structural direction residual.  The
T2 exact orbital formula gives, with

\[
 (u,v,w,x)=(|I\cap I'|,|I\cap J'|,|J\cap I'|,|J\cap J'|),
\]

\[
 k_{u,v,w,x}=
 \binom au\binom bw\binom{p-j}{a-u-w}
 \binom{a-u}v\binom{b-w}x
 \binom{p-j-a+u+w}{b-v-x},                                \tag{19}
\]

and the exact physical carrier kernel `Phi_r`,

\[
 \sum_\mu f^\mu a_{0\mu}r_\mu
   =M\sum_{r}k_r\Phi_r.                                   \tag{20}
\]

Accordingly, after removing the three proved faces, the smallest honest
residual is the scalar family

\[
 \boxed{\Delta(n,j,\theta,a,b,\alpha,\beta;c)
 =B_\theta(q)^2T-M\sum_rk_r\Phi_r\ge0}                    \tag{21}
\]

for every remaining admissible tame mixed/non-column sector.  In (21),
`Phi_r` is the T2 character sum tracing the complete rank-`dc` carrier.  It
is exactly computable and retains signs, directions, and LR copies.  Taking
absolute values, a maximum over tails, or sorted eigenvalue pairings would
be a different and already disqualified problem.

This residual is sharply separable by the finite tuple
`(j,theta,a,b,alpha,beta,c)`.  For fixed tuple, (19)--(21) provide a finite
exact summation problem in `n`.  A counterexample is exactly a tuple with
`Delta<0`; equality or a positive formula proves that tuple.  The first
especially important untested multiplicity case is

`j=6, theta=(3,2,1), a=b=3, alpha=beta=(2,1), c=2`,

whose first tame value is `n=18`.  The existing non-tame `23296 x 1120`
carrier packet stops before the physical `L_h,S_(h,0)` pairing and therefore
does not decide (21).

There is no uniform slack to exploit: (2), (3), (10) on fixed hook data, and
(18) all approach one as `n` grows.  The most plausible finite
counterexample search is therefore the sign of the first `1/n` defect in
(21) for mixed/non-column data, followed by exact evaluation at the finitely
many small tame `n` if that coefficient is nonnegative.

## 5. Exact and certified gates

The attached script performs only actual-pairing checks.  It:

1. verifies all three upstream SHA-256 manifests (19 files);
2. checks (10) by exact hook arithmetic on 15,398 admissible symbolic rows
   with `1<=j<=12`;
3. checks both the two-isotype form and the independent Pluecker orbital form
   of (18) on 486 symbolic rows;
4. checks the explicit `j=1` `a,r` table for `3<=n<=20`;
5. audits all 59 certified actual T-a intervals and proves that all are below
   their exact caps;
6. matches the exact closed formulas to all 34 sweep rows lying on the proved
   faces, including all 16 `j=1` rows.

The remaining 25 sweep rows still pass as finite certified evidence, not as
a uniform theorem.  No `c>=2` physical pairing is relabeled or inferred.

## Final adjudication

**STILL BLOCKED.**  The `j=1` tight laws and two infinite general-`j` faces
are **PROVED**.  The all-parameter/all-`c` cap is neither proved nor refuted.
Its exact minimal residual is (21); no actual counterexample is currently on
disk.

No DAG, node, note, handoff, paper, `research/ksum` file, or git history was
modified.
