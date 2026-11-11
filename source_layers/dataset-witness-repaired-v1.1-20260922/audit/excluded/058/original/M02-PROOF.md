# Additivity gaps for minimum output entropy

All logarithms are natural.  Thus one bit is \(\log 2\).  For a finite-dimensional
channel \(\Phi\), write
\[
 S_{\min}(\Phi)=\min_{\rho}S(\Phi(\rho)),\qquad
 \Delta(\Phi,\Psi)=S_{\min}(\Phi)+S_{\min}(\Psi)
                      -S_{\min}(\Phi\otimes\Psi).
\]

The main result developed below is stronger than the previously recorded
constant lower bounds but weaker than the Hayden--Penington extensive-dimension
problem:

> **Theorem A (unbounded finite-dimensional gap).**  For every \(L>0\) there
> are finite-dimensional quantum channels \(\Phi_L,\Psi_L\) such that
> \(\Delta(\Phi_L,\Psi_L)>L\).
>
> More quantitatively, fix any integer \(N>e^{18}\).  For every \(k\) and every
> \(\theta>0\) there are finite-dimensional channels \(\Phi_k,\overline\Phi_k\)
> satisfying
> \[
> \begin{split}
> \Delta(\Phi_k,\overline\Phi_k)
> &\ge {k\log N\over N}
> -4\log\!\left(1+\sqrt{(1+9/N)^k-1}+\theta\right).                 \tag{A1}
> \end{split}
> \]
> Consequently
> \[
> \liminf_{k\to\infty}{1\over k}\Delta(\Phi_k,\overline\Phi_k)
> \ge c_N:={\log N\over N}-2\log(1+9/N)>0.                         \tag{A2}
> \]

The channels in Theorem A have output dimension that can be chosen to be
\(N^k\), by passing to complementary channels.  The proof presently gives no
upper bound of the form \(\log d_{\rm in}=O(k)\) for their input dimension.
Therefore it does **not** prove the full Hayden--Penington formulation in which
all channel dimensions must use only \(O(k)\) qubits.  The absence of a
quantitative input-dimension bound is isolated precisely in Lemma 7 below.

The proof uses three published operator-algebra inputs, stated explicitly in
Section 4.  Everything after those inputs, including the finite localization,
channel construction, and entropy estimates, is proved here.

## 1. Elementary channel facts

### Lemma 1 (pure inputs and complements)

The minimum defining \(S_{\min}(\Phi)\) may be restricted to pure inputs.  If
\(\Phi^c\) is any complementary channel, then
\[
 S_{\min}(\Phi)=S_{\min}(\Phi^c).
\]
Moreover \((\Phi\otimes\Psi)^c\) may be chosen as
\(\Phi^c\otimes\Psi^c\), and hence
\[
 \Delta(\Phi,\Psi)=\Delta(\Phi^c,\Psi^c).                          \tag{1}
\]

**Proof.**  If \(\rho=\sum_jp_j|x_j\rangle\langle x_j|\), concavity of entropy
gives
\[
 S(\Phi(\rho))\ge\sum_jp_jS(\Phi(|x_j\rangle\langle x_j|))
 \ge\min_xS(\Phi(|x\rangle\langle x|)).
\]
For a pure input, the two outputs of a Stinespring isometry have the same
nonzero eigenvalues by Schmidt decomposition, so have the same entropy.  The
tensor product of Stinespring isometries is a Stinespring isometry for the
tensor product channel.  Applying the first assertion to all three channels
proves (1). \(\square\)

### Lemma 2 (a universal information upper bound)

If a pure state \(|\xi\rangle\) minimizes
\(S((\Phi\otimes\Psi)(|\xi\rangle\langle\xi|))\), and its output is
\(\omega_{B_1B_2}\), then
\[
 \Delta(\Phi,\Psi)\le I(B_1:B_2)_\omega
 \le I(A_1:A_2)_\xi=2S(\xi_{A_1}).                                \tag{2}
\]
In particular,
\[
 \Delta(\Phi,\Psi)\le2\min\{\log d_{A_1},\log d_{A_2},
                                      \log d_{B_1},\log d_{B_2}\}. \tag{3}
\]

**Proof.**  Each marginal input of \(\xi\) can be mixed, but by Lemma 1 and
concavity every channel output has entropy at least its minimum output entropy.
Thus
\[
 \begin{split}
 \Delta(\Phi,\Psi)
 &\le S(\omega_{B_1})+S(\omega_{B_2})-S(\omega_{B_1B_2})\\
 &=I(B_1:B_2)_\omega.
 \end{split}
\]
Data processing for mutual information gives the second inequality.  A pure
bipartite input has mutual information twice either marginal entropy.  Finally
\(I(B_1:B_2)\le2\min\{S(B_1),S(B_2)\}\), by the Araki--Lieb inequality, and
entropy is at most the logarithm of dimension. \(\square\)

The bound (3) shows that the linear target is dimensionally possible, but it
does not impose any dimension-independent ceiling.

## 2. What ordinary tensor-power amplification can and cannot do

Define the regularized minimum output entropy
\[
 \overline S_{\min}(\Phi)=\lim_{m\to\infty}{1\over m}
 S_{\min}(\Phi^{\otimes m}).                                      \tag{4}
\]
The limit exists because \(a_m=S_{\min}(\Phi^{\otimes m})\) is subadditive:
product minimizers show \(a_{m+n}\le a_m+a_n\); Fekete's lemma then gives
the limit as \(\inf_m a_m/m\).  For completeness, Fekete's assertion follows
by writing \(n=qm+r\):
\(a_n/n\le q a_m/n+a_r/n\), taking \(n\to\infty\), and then the infimum over
\(m\).

### Lemma 3 (fixed-pair tensor powers)

For fixed finite-dimensional channels \(\Phi,\Psi\),
\[
 \lim_{m\to\infty}{1\over m}\Delta(\Phi^{\otimes m},\Psi^{\otimes m})
 =\overline S_{\min}(\Phi)+\overline S_{\min}(\Psi)
  -\overline S_{\min}(\Phi\otimes\Psi).                           \tag{5}
\]

**Proof.**  After permuting tensor factors,
\(\Phi^{\otimes m}\otimes\Psi^{\otimes m}\) is unitarily equivalent to
\((\Phi\otimes\Psi)^{\otimes m}\).  Divide the definition of \(\Delta\) by
\(m\) and use (4) three times. \(\square\)

Thus fixed-pair tensor powers give an extensive gap exactly when the
regularized minimum output entropy is itself nonadditive for that pair.

### Lemma 4 (self-powers never amplify extensively)

For every fixed finite-dimensional channel \(\Phi\),
\[
 \lim_{m\to\infty}{1\over m}\Delta(\Phi^{\otimes m},\Phi^{\otimes m})=0.
                                                                        \tag{6}
\]

**Proof.**  With \(a_m=S_{\min}(\Phi^{\otimes m})\), the left side before
taking the limit is \((2a_m-a_{2m})/m\).  Since both \(a_m/m\) and
\(a_{2m}/(2m)\) tend to \(\overline S_{\min}(\Phi)\), the expression tends to
zero. \(\square\)

This explains why simply tensoring a single Hastings counterexample with
itself cannot settle the extensive question.

## 3. Random-unitary channels and the Bell entropy saving

Let \(U=(U_1,\ldots,U_N)\) be unitaries on \(\mathbb C^d\).  Define
\[
 \mathcal R_U(\rho)={1\over N}\sum_{i=1}^NU_i\rho U_i^*,             \tag{7}
\]
with complementary channel
\[
 \mathcal C_U(\rho)={1\over N}
 \big[\operatorname {Tr}(U_i\rho U_j^*)\big]_{i,j=1}^N.             \tag{8}
\]
Equation (8) follows from the Stinespring isometry
\(Vx=N^{-1/2}\sum_iU_ix\otimes|i\rangle\).

### Lemma 5 (Bell witness, with no randomness assumption)

For every unitary tuple \(U\),
\[
 S_{\min}(\mathcal R_U\otimes\overline{\mathcal R_U})
 \le 2\log N-{\log N\over N}.                                     \tag{9}
\]

**Proof.**  Let \(|\Omega_d\rangle=d^{-1/2}\sum_se_s\otimes e_s\).  The
identity
\((A\otimes\overline A)|\Omega_d\rangle=|\Omega_d\rangle\) holds for every
unitary \(A\).  The output of the product channel on \(|\Omega_d\rangle\) is
the equiprobable mixture of the \(N^2\) pure vectors
\[
 (U_i\otimes\overline{U_j})|\Omega_d\rangle,qquad 1\le i,j\le N.
\]
The \(N\) vectors with \(i=j\) are identical.  Grouping those ensemble entries
gives weights
\[
 {1\over N},\quad
 \underbrace{{1\over N^2},\ldots,{1\over N^2}}_{N^2-N\ \mathrm{times}}.
\]
The entropy of a mixture of pure states is at most the Shannon entropy of its
mixing weights.  Here is a direct proof.  Put columns \(\sqrt{p_r}x_r\) in a
matrix \(X\).  The state \(XX^*\) and Gram matrix \(G=X^*X\) have the same
nonzero eigenvalues \(\lambda_j\).  If \(V\) diagonalizes \(G\), then
\(p_r=G_{rr}=\sum_j|V_{rj}|^2\lambda_j\).  The matrix
\((|V_{rj}|^2)_{rj}\) is doubly stochastic.  Applying concavity of
\(-t\log t\) row by row and then using that every column also sums to one gives
\(H(p)\ge H(\lambda)=S(XX^*)\).
For the displayed weights,
\[
 H(p)={\log N\over N}+(N^2-N){2\log N\over N^2}
     =2\log N-{\log N\over N}.
\]
This particular input therefore proves (9). \(\square\)

For tuples \(U^{(r)}\) on dimensions \(d_r\), set
\(\mathcal R^{[k]}=\bigotimes_{r=1}^k\mathcal R_{U^{(r)}}\).  Applying
Lemma 5 to the product of the \(k\) Bell states gives
\[
 S_{\min}(\mathcal R^{[k]}\otimes\overline{\mathcal R^{[k]}})
 \le k\left(2\log N-{\log N\over N}\right).                       \tag{10}
\]
The entire problem is therefore to choose *different* tuples \(U^{(r)}\) so
that entangled inputs within \(\mathcal R^{[k]}\) do not appreciably lower its
minimum output entropy.

## 4. Three operator-algebra inputs

Only the following published results are imported.

1. **Product free-group norm estimate.**  Let \(u_1,\ldots,u_N\) be the
   canonical generators in \(A=C_r^*(\mathbb F_N)\).  For
   \(v=(v_1,\ldots,v_k)\in[N]^k\), put
   \(u_v=u_{v_1}\otimes\cdots\otimes u_{v_k}\in A^{\otimes_{\min}k}\).
   Collins--Youn, Theorem 3.3, proves that every trace-zero
   \(a=(a_{vw})\in M_{N^k}\) satisfies
   \[
   \left\|\sum_{v,w\in[N]^k}a_{vw}u_v^*u_w\right\|
   \le K_{N,k}\|a\|_2,\qquad
   K_{N,k}=N^{k/2}\sqrt{(1+9/N)^k-1}.                              \tag{11}
   \]
   Their channel consequence and constants appear in Theorems 3.4--3.5.
   Source actually opened: [Collins--Youn, *Additivity violation of the
   regularized minimum output entropy*, pp. 1309--1313]
   (https://ems.press/content/serial-article-files/26678).

2. **Strong finite-matrix models for free Haar unitaries.**  There is a
   deterministic sequence of dimensions \(d(m)\to\infty\) and unitary tuples
   \(U^{(m)}=(U_1^{(m)},\ldots,U_N^{(m)})\in U(d(m))^N\) such that, for every
   noncommutative \(*\)-polynomial \(P\),
   \[
   \|P(U^{(m)},U^{(m)*})\|\longrightarrow\|P(u,u^*)\|.             \tag{12}
   \]
   One obtains a deterministic sequence by choosing a sample point in the
   probability-one strong-convergence event for independent Haar matrices.
   Source actually opened: [Collins--Male, *The strong asymptotic freeness of
   Haar and deterministic matrices*]
   (https://numdam.org/articles/10.24033/asens.2211/).

3. **Exact operator coefficients.**  The algebra \(C_r^*(\mathbb F_N)\) is
   exact; exactness is preserved by minimal tensor products and by matrix
   amplification.  If (12) holds and \(B\) is exact, then for every fixed
   polynomial \(P\) with coefficients in \(B\),
   \[
   \|P(U^{(m)},U^{(m)*})\|\longrightarrow\|P(u,u^*)\|.             \tag{13}
   \]
   A concise proof of (13) is included next.  The exactness statement and the
   operator-coefficient lemma were actually opened as Definition 2.17 and
   Lemma 2.18 in [van Handel, *The strong convergence phenomenon*, pp. 19--20]
   (https://web.math.princeton.edu/~rvan/cdm250630.pdf).

For clarity, (13) does **not** assert convergence uniformly over matrix
coefficient dimensions growing with \(m\).  That assertion is false in this
generality and is the obstruction in simultaneous tensor limits.  The argument
below takes iterated limits, fixing all earlier matrix coefficients before the
next limit.

### Lemma 6 (proof of the exact-coefficient implication)

Assume scalar strong convergence (12), its standard fixed-matrix amplification,
and exactness of \(B\).  Then (13) holds.

**Proof.**  Let \(E\subset B\) be the finite-dimensional span of the
coefficients of \(P\).  The finite-dimensional characterization of exactness
says that, for every \(\varepsilon>0\), there are \(D\) and a linear embedding
\(j:E\to M_D\) such that for every C*-algebra \(D_0\) and every
\(x\in E\otimes D_0\),
\[
 \|(j\otimes\mathrm{id})(x)\|\le\|x\|
 \le(1+\varepsilon)\|(j\otimes\mathrm{id})(x)\|.                  \tag{14}
\]
Apply this first with \(D_0=M_{d(m)}\), and then with
\(D_0=C^*(u_1,\ldots,u_N)\).  The middle objects now have fixed
\(D\times D\) matrix coefficients, so fixed-matrix strong convergence gives
\[
 \|(j\otimes\mathrm{id})P(U^{(m)})\|
 \longrightarrow\|(j\otimes\mathrm{id})P(u)\|.
\]
Sandwiching with (14), and then letting \(\varepsilon\downarrow0\), proves
(13). \(\square\)

## 5. Finite localization of the product free-group inequality

This is the step that moves the Collins--Youn estimate from their
infinite-dimensional commuting model to ordinary finite-dimensional tensor
products.  The unequal, iteratively chosen dimensions are essential.

### Lemma 7 (finite localization)

For every \(N,k\in\mathbb N\) and \(\eta>0\), there are finite dimensions
\(d_1,\ldots,d_k\) and unitary tuples
\[
 U^{(r)}=(U_1^{(r)},\ldots,U_N^{(r)})\in U(d_r)^N,qquad 1\le r\le k,
\]
such that, writing
\(U_v=U_{v_1}^{(1)}\otimes\cdots\otimes U_{v_k}^{(k)}\), every trace-zero
\(a\in M_{N^k}\) obeys
\[
 \left\|\sum_{v,w}a_{vw}U_v^*U_w\right\|
 \le (K_{N,k}+\eta)\|a\|_2.                                      \tag{15}
\]

**Proof.**  First fix a finite set \(\mathcal F\) in the algebraic tensor
product \(A^{\odot k}\).  Replace the last free factor in every
\(x\in\mathcal F\) by \(U^{(m_k)}\).  This is a polynomial in
\(U^{(m_k)}\) with coefficients in the exact algebra
\(A^{\otimes_{\min}(k-1)}\).  Lemma 6 shows that, for a sufficiently large
fixed \(m_k\), all norms change by at most a prescribed \(\delta\).

Now keep this finite matrix tuple fixed and replace the \((k-1)\)-st free
factor by \(U^{(m_{k-1})}\).  The coefficient algebra is a matrix amplification
of \(A^{\otimes_{\min}(k-2)}\), hence is exact.  Lemma 6 applies again.  Continue
one factor at a time.  After \(k\) steps, the elements of \(\mathcal F\) are
represented on a finite tensor product and their norms exceed their original
norms by at most \(k\delta\).  Notice that each limit sees only a *fixed*
coefficient algebra and all previously selected matrix dimensions are frozen.

Apply this construction to a finite \(\varepsilon\)-net of the Hilbert--Schmidt
unit sphere in the trace-zero subspace of \(M_{N^k}\), through the linear map
\[
 T(a)=\sum_{v,w}a_{vw}u_v^*u_w.
\]
Both the free and finite evaluation maps are \(N^k\)-Lipschitz from
Hilbert--Schmidt norm to operator norm: by the triangle and Cauchy--Schwarz
inequalities,
\[
 \|T(a-b)\|\le\sum_{v,w}|a_{vw}-b_{vw}|
 \le N^k\|a-b\|_2,                                                \tag{16}
\]
and the same proof applies to the finite unitaries.  Choose
\(2N^k\varepsilon+k\delta<\eta\).  The net estimate, (16), and the free bound
(11) then give (15) on the whole unit sphere.  Homogeneity completes the proof.
\(\square\)

Lemma 7 is qualitative: neither the strong-convergence theorem nor the
iterated choice above supplies a useful bound on \(d_1\cdots d_k\).  This is
the sole dimension-control loss in Theorem A.

## 6. Uniform entropy lower bound from the localized norm inequality

For the tuples in Lemma 7, define
\[
 \mathcal R^{[k]}=\bigotimes_{r=1}^k\mathcal R_{U^{(r)}},\qquad
 \mathcal C^{[k]}=\bigotimes_{r=1}^k\mathcal C_{U^{(r)}}.           \tag{17}
\]
The latter is a complementary channel of the former and has output dimension
\(D=N^k\).

### Lemma 8 (minimum output entropy lower bound)

If (15) holds, then
\[
 S_{\min}(\mathcal R^{[k]})=S_{\min}(\mathcal C^{[k]})
 \ge k\log N
 -2\log\!\left(1+\sqrt{(1+9/N)^k-1}+{\eta\over N^{k/2}}\right).    \tag{18}
\]

**Proof.**  Let \(\rho\) be any input state and put
\[
 X=\mathcal C^{[k]}(\rho)-I_D/D.
\]
Then \(X=X^*\) and \(\operatorname {Tr}X=0\).  Since
\(\operatorname {Tr}(XI_D/D)=0\),
\[
 \begin{split}
 \|X\|_2^2
 &=\operatorname {Tr}\bigl(X\mathcal C^{[k]}(\rho)\bigr)\\
 &=\operatorname {Tr}\bigl(\rho\,\mathcal C^{[k]*}(X)\bigr)
 \le\|\mathcal C^{[k]*}(X)\|_\infty.                              \tag{19}
 \end{split}
\]
Up to transposing the scalar coefficient matrix,
\[
 \mathcal C^{[k]*}(X)={1\over D}\sum_{v,w}X_{vw}U_v^*U_w.
\]
The transpose does not change Hilbert--Schmidt norm, so (15) and (19) give
\[
 \|X\|_2^2\le {K_{N,k}+\eta\over D}\|X\|_2.
\]
If \(X\ne0\), divide by \(\|X\|_2\); the conclusion is also immediate when
\(X=0\).  Hence
\[
 \|X\|_2\le {K_{N,k}+\eta\over D}.
\]
The triangle inequality and \(\|I_D/D\|_2=D^{-1/2}\) yield
\[
 \|\mathcal C^{[k]}(\rho)\|_2
 \le N^{-k/2}\left(1+\sqrt{(1+9/N)^k-1}+{\eta\over N^{k/2}}\right).\tag{20}
\]
For every state \(\sigma\), monotonicity of Renyi entropies (or weighted
Jensen applied to \(-\log\)) gives
\[
 S(\sigma)\ge-\log\operatorname {Tr}\sigma^2=-2\log\|\sigma\|_2. \tag{21}
\]
Combining (20) and (21) proves the bound for \(\mathcal C^{[k]}\).  Equality of
the two minimum output entropies is Lemma 1. \(\square\)

The same lower bound holds for the entrywise conjugate channel because
operator and Hilbert--Schmidt norms are invariant under conjugation.

## 7. Proof of Theorem A

In Lemma 7 choose \(\eta=\theta N^{k/2}\), and let
\(\Phi_k=\mathcal R^{[k]}\).  Lemma 8 applied to \(\Phi_k\) and its conjugate
gives
\[
 S_{\min}(\Phi_k)+S_{\min}(\overline\Phi_k)
 \ge2k\log N-4\log\!\left(1+\sqrt{(1+9/N)^k-1}+\theta\right).      \tag{22}
\]
Equation (10) gives
\[
 S_{\min}(\Phi_k\otimes\overline\Phi_k)
 \le2k\log N-{k\log N\over N}.                                  \tag{23}
\]
Subtracting (23) from (22) is exactly (A1).

As \(a=1+9/N>1\),
\[
 {1\over k}\log(1+\sqrt{a^k-1}+\theta)\longrightarrow{1\over2}\log a.
\]
This proves (A2).  Finally
\[
 2\log(1+9/N)<{18\over N}
\]
by \(\log(1+x)<x\).  Hence \(N>e^{18}\) implies \(c_N>0\), and (A1) exceeds
any prescribed \(L\) for all sufficiently large \(k\).  All channels constructed
are finite-dimensional, proving Theorem A. \(\square\)

Passing from \(\Phi_k,\overline\Phi_k\) to their complementary channels leaves
the gap unchanged by Lemma 1 and makes both output dimensions exactly \(N^k\).

## 8. Audit of the localization step

Three nearby but invalid arguments should not be confused with Lemma 7.

1. Taking the same matrix size to infinity in all tensor factors creates
   polynomial coefficients whose dimensions grow with the approximation
   parameter.  Scalar strong convergence does not control those coefficients.
   Lemma 7 instead takes iterated limits and freezes every chosen matrix factor.

2. A single ultraproduct representation of commuting copies naturally controls
   the maximal tensor norm, not automatically the minimal tensor norm.  Lemma 6
   is applied directly at each spatial tensor stage; exactness of the already
   fixed coefficient algebra is what keeps the target norm minimal.

3. The tuple used at tensor position \(r\) is allowed to differ from the tuple at
   position \(s\).  Lemma 4 shows why taking powers of one fixed finite channel
   cannot produce the claimed normalized self-gap.

The price of the iterated limit is uncontrolled growth of the selected dimensions
\(d_r\).  A quantitative version strong enough to ensure
\[
 \sum_{r=1}^k\log d_r=O(k)                                       \tag{24}
\]
would upgrade Theorem A to the Hayden--Penington extensive formulation.  No
such quantitative localization is proved here.

## 9. Relation to the established one-bit construction

Belinschi--Collins--Nechita computed the asymptotic minimum output entropy for
a standard random-subspace model and proved that its conjugate-channel Bell
witness approaches but does not reach \(\log2\).  The source actually opened is
[Belinschi--Collins--Nechita, *Almost one bit violation for the additivity of the
minimum output entropy*, Theorems 1.2 and 6.3]
(https://arxiv.org/abs/1305.1567).  Theorem A does not improve their single-block
optimization.  It uses different finite approximants of the product free-group
model so that the Bell saving in (9) adds over blocks while the single-side
minimum output entropy is controlled globally by (15).

Hayden--Penington formulate the extensive alternative and its black-hole
dichotomy in [*Black hole microstates vs. the additivity conjectures*]
(https://arxiv.org/abs/2012.07861).  Theorem A proves unboundedness and a linear
gap in the block count with output dimension \(N^k\), but condition (24), needed
to make the input dimension qubit-linear in that block count, remains open.

## 10. Current boundary

What is proved here, subject only to the three established operator-algebra
theorems in Section 4, is:

* finite-dimensional von Neumann minimum-output-entropy gaps are unbounded;
* an explicit analytic lower bound (A1) grows linearly in a block parameter;
* the output dimension of complementary witnesses is exponential in that
  parameter, hence uses linearly many output qubits;
* ordinary powers of one fixed channel cannot give a normalized self-gap;
* the remaining full-strength obstruction is quantitative control of the input
  dimensions in the finite localization lemma.

No deterministic numerical matrices are extracted from the strong-convergence
argument, so this does not solve the explicit-counterexample problem.

## 11. Finite numerical check of the analytic rate

The positivity test in Section 7 and one concrete value of the lower bound are
finitely checkable.  The following is the verbatim output of a 60-decimal
`python3`/`mpmath` evaluation.  Here \(N=178482301\), \(\theta=10^{-9}\), and
`gap(k)` is exactly the right-hand side of (A1).

```text
142727554 0.69314717462124424842141331186559316244972676460883 minus_log2= -0.000000005938701060995818809592583405625773369751
142727555 0.69314718283762012890653101768969863210260471859703 minus_log2= 0.000000002277674819489298896231522064027104584237
c_N= 0.0000000056027989802347425726155273859298182200430357210276
```

Thus the proved lower bound itself already exceeds one bit at
\(k=142727555\) for this choice of parameters.  This calculation verifies only
the elementary evaluation of (A1); existence of the finite unitary tuples is
the qualitative content of Lemma 7.

## Round 2026-08-20: the smallest positive-rate alphabet

Section 7 gives the convenient sufficient hypothesis \(N>e^{18}\), but leaves
open the smallest integer \(N\) for which the rate \(c_N\) in (A2) is actually
positive.  This round settles only that finite threshold.

### Lemma 9 (sharp integer threshold for the rate in (A2))

For an integer \(N\ge1\),
\[
 c_N={\log N\over N}-2\log(1+9/N)>0
 \quad\Longleftrightarrow\quad N\ge 65{,}659{,}889.               \tag{25}
\]

**Proof.**  Multiplication by \(N\) shows that the sign in question is the
sign of
\[
 g(x)=\log x-2x\log(1+9/x).                                     \tag{26}
\]
Put \(t=9/x\) and
\[
 h(t)=\log(1+t)-{t\over1+t}
     =\int_0^t {s\over(1+s)^2}\,ds.
\]
Consequently \(0<h(t)<t^2/2\) for \(t>0\), and direct differentiation gives
\[
 g'(x)={1\over x}-2h(9/x)
       >{1\over x}-{81\over x^2}={x-81\over x^2}.               \tag{27}
\]
Thus \(g\) is strictly increasing on \([81,\infty)\).  There cannot be an
earlier positive integer: the function
\(q(x)=x\log(1+9/x)\) has derivative \(q'(x)=h(9/x)>0\), so for
\(1\le x<100\),
\[
 2q(x)\ge2q(1)=2\log 10=\log100>\log x,
\]
and hence \(g(x)<0\).

It remains only to certify the signs at the two consecutive integers in
(25).  The certification below used only exact `fractions.Fraction`
arithmetic.  For \(0<z<1\), it bounded every logarithm by
\[
 2\sum_{j=0}^{m}{z^{2j+1}\over2j+1}
 \le \log{1+z\over1-z}
 \le 2\sum_{j=0}^{m}{z^{2j+1}\over2j+1}
       +{2z^{2m+3}\over(2m+3)(1-z^2)}.                           \tag{28}
\]
The right inequality follows by replacing every denominator in the remaining
positive series by \(2m+3\).  To bound \(\log N\), write
\(N=2^q y\), with \(1\le y<2\), and apply (28) to \(\log2\) using
\(z=1/3\), and to \(\log y\) using
\(z=(N-2^q)/(N+2^q)\).  For \(\log(1+9/N)\), use
\(z=9/(2N+9)\).  Here is the verbatim `python3` output; the displayed decimals
are renderings of rational interval endpoints, while the numerator tests are
performed on the exact fractions.

```text
method: exact fractions; 41 terms for log(2) and the reduced log, 5 terms for log(1+9/N)
N = 65659888
g_lower = -2.090892713519350869437129609078597588187640557350878231669826E-9
g_upper = -2.090892713519350869437129609078427195607821691402209832936885E-9
lower_numerator_positive = False
upper_numerator_negative = True
N = 65659889
g_lower = 1.313908694705151849532412894165131754383411553147782025188807E-8
g_upper = 1.313908694705151849532412894165148793641494432466743402381884E-8
lower_numerator_positive = True
upper_numerator_negative = False
```

Therefore \(g(65{,}659{,}888)<0<g(65{,}659{,}889)\).  The negativity below
\(100\) and strict increase from \(81\) onward prove (25). \(\square\)

Accordingly, Theorem A and its proof remain valid with the hypothesis
\(N>e^{18}\) replaced by the sharp integer condition
\(N\ge65{,}659{,}889\).  This improves only the smallest admissible value of
the already-proved analytic rate; it does not address the dimension-control
condition (24).

## Round 2026-08-20: Schatten duality and the collision spectrum

The estimate (15) is naturally a dual estimate for the complementary
channel.  Making this duality exact reveals an orthogonal decomposition that
was lost in the triangle inequality in (20).  This gives a strictly stronger
finite-\(k\) bound and removes the finite-size correction from the existential
linear envelope.

For this round fix the tuples in Lemma 7, put \(D=N^k\), and abbreviate
\(W_v=U_v\).  Let \(S_p\) denote the Schatten \(p\)-class, with its usual
norm, and let
\[
 M_D^0=\{a\in M_D:\operatorname {Tr}a=0\},\qquad
 P_0(a)=a-{\operatorname {Tr}a\over D}I_D.                       \tag{29}
\]
Define the coefficient map
\[
 \mathcal T(a)=\sum_{v,w\in[N]^k}a_{vw}W_v^*W_w.                 \tag{30}
\]

### Lemma 10 (exact Schatten-dual form of localization)

For the complementary channel \(\mathcal C^{[k]}\) in (17),
\[
 \bigl\|\mathcal T|_{M_D^0}\bigr\|_{S_2\to S_\infty}
   =D\bigl\|P_0\mathcal C^{[k]}\bigr\|_{S_1\to S_2}.           \tag{31}
\]
Consequently, (15) is equivalent to
\[
 \bigl\|P_0\mathcal C^{[k]}(X)\bigr\|_2
 \le {K_{N,k}+\eta\over D}\|X\|_1
 \quad\hbox{for every }X.                                      \tag{32}
\]

**Proof.**  Use the Hilbert--Schmidt pairing in both matrix spaces.  Directly
from (8),
\[
 \begin{split}
 \langle\mathcal T(a),X\rangle
 &=\sum_{v,w}\overline {a_{vw}}\operatorname {Tr}(W_w^*W_vX),\\
 \bigl(\mathcal T^*(X)\bigr)_{vw}
 &=\operatorname {Tr}(W_w^*W_vX)
   =D\bigl(\mathcal C^{[k]}(X)\bigr)_{vw}.
 \end{split}                                                     \tag{33}
\]
Thus \((\mathcal TP_0)^*=D P_0\mathcal C^{[k]}\).  Schatten
duality gives, for every linear map \(A\),
\[
 \begin{split}
 \|A\|_{S_2\to S_\infty}
 &=\sup_{\|a\|_2=1,\ \|X\|_1=1}|\langle X,Aa\rangle|\\
 &=\sup_{\|X\|_1=1}\|A^*X\|_2
 =\|A^*\|_{S_1\to S_2}.                                       \tag{34}
 \end{split}
\]
Finally, \(P_0\) is the Hilbert--Schmidt orthogonal projection onto
\(M_D^0\), so
\(\|\mathcal TP_0\|_{2\to\infty}
=\|\mathcal T|_{M_D^0}\|_{2\to\infty}\).  Equations (33)--(34)
prove (31), and (32) is precisely its norm inequality. \(\square\)

This identifies Lemma 7 with a centered \(1\)-to-\(2\) expansion estimate.
In particular, for every input state \(\rho\), trace preservation gives
\[
 P_0\mathcal C^{[k]}(\rho)
 =\mathcal C^{[k]}(\rho)-I_D/D.                                  \tag{35}
\]
Thus (32) proves the deviation estimate in Lemma 8 directly, without the
self-pairing argument (19).

### Lemma 11 (orthogonal spectral improvement)

Under (15),
\[
 S_{\min}(\mathcal C^{[k]})=S_{\min}(\mathcal R^{[k]})
 \ge \log D-\log\left(1+{(K_{N,k}+\eta)^2\over D}\right).       \tag{36}
\]

**Proof.**  Put \(\sigma=\mathcal C^{[k]}(\rho)\).  Equations
(32)--(35) and \(\|\rho\|_1=1\) give
\[
 \|\sigma-I_D/D\|_2\le {K_{N,k}+\eta\over D}.                 \tag{37}
\]
The two summands in
\(\sigma=I_D/D+(\sigma-I_D/D)\) are Hilbert--Schmidt orthogonal,
because the second has trace zero.  Pythagoras, rather than the triangle
inequality used in (20), therefore gives
\[
 \operatorname {Tr}\sigma^2=\|\sigma\|_2^2
 ={1\over D}+\|\sigma-I_D/D\|_2^2
 \le {1\over D}+{(K_{N,k}+\eta)^2\over D^2}.                    \tag{38}
\]
Now (21) gives (36).  Equality of the two minimum output entropies follows
from Lemma 1. \(\square\)

### Proposition 12 (strengthened finite-block gap)

For every \(N,k\in\mathbb N\) and every \(\theta>0\), the channels in
Theorem A can be chosen so that, with \(a=1+9/N\),
\[
 \Delta(\Phi_k,\overline\Phi_k)
 \ge {k\log N\over N}
 -2\log\left(1+\left[\sqrt{a^k-1}+\theta\right]^2\right).       \tag{39}
\]
This is strictly stronger than (A1).

**Proof.**  In Lemma 7 take \(\eta=\theta N^{k/2}=\theta\sqrt D\).
Since
\[
 {K_{N,k}+\eta\over\sqrt D}=\sqrt{a^k-1}+\theta,
\]
Lemma 11 lower-bounds each of the two single-channel entropies by
\[
 k\log N-\log\left(1+left[\sqrt{a^k-1}+\theta\right]^2\right).
\]
Subtracting the Bell-witness upper bound (23) proves (39).  If
\(q=\sqrt{a^k-1}+\theta>0\), then
\(1+q^2<(1+q)^2\).  Hence
\(2\log(1+q^2)<4\log(1+q)\), which proves the strict comparison with
(A1). \(\square\)

### Corollary 13 (linear envelope with arbitrarily small loss)

For every \(N,k\in\mathbb N\) and every \(\varepsilon>0\), there are
finite-dimensional channels from the construction above such that
\[
 \Delta(\Phi_k,\overline\Phi_k)\ge k c_N-\varepsilon,
 \qquad c_N={\log N\over N}-2\log(1+9/N).                        \tag{40}
\]

**Proof.**  The right side of (39) is continuous as \(\theta\downarrow0\).
At \(\theta=0\),
\[
 1+\left(\sqrt{a^k-1}\right)^2=a^k,
\]
so that the right side becomes
\(k\log N/N-2k\log a=kc_N\).  Choose a sufficiently small positive
\(\theta\) and apply Proposition 12. \(\square\)

Thus the qualitative choice of matrix dimensions in Lemma 7 causes no fixed
additive loss in the existential statement: for each fixed block number, the
localization tolerance can be chosen after the desired loss in (40).  The
same qualitative choice still prevents any conclusion about (24).

There is also a tensor-sector interpretation of the factor
\((1+9/N)^k-1\).  For the \(r\)-th complementary channel define
\[
 \mathcal D_r(X)=\operatorname {Tr}(X)I_N/N,
 \qquad \mathcal E_r=\mathcal C_{U^{(r)}}-\mathcal D_r.          \tag{41}
\]
For \(S\subseteq[k]\), let \(\mathcal E_S\) be the tensor-product map
whose \(r\)-th factor is \(\mathcal E_r\) for \(r\in S\) and
\(\mathcal D_r\) for \(r\notin S\).

### Lemma 14 (orthogonal subset decomposition)

For every input matrix \(X\),
\[
 P_0\mathcal C^{[k]}(X)=\sum_{\varnothing\ne S\subseteq[k]}
 \mathcal E_S(X),                                                \tag{42}
\]
and the summands on the right are pairwise Hilbert--Schmidt orthogonal.
Consequently,
\[
 \bigl\|P_0\mathcal C^{[k]}(X)\bigr\|_2^2
 =\sum_{\varnothing\ne S\subseteq[k]}\|\mathcal E_S(X)\|_2^2.\tag{43}
\]

**Proof.**  Expanding
\(\bigotimes_{r=1}^k(\mathcal D_r+\mathcal E_r)\) gives the sum over
all subsets.  The empty-set term is
\[
 (\mathcal D_1\otimes\cdots\otimes\mathcal D_k)(X)
 =\operatorname {Tr}(X)I_D/D,
\]
which is exactly the scalar component removed by \(P_0\), proving (42).
The range of \(\mathcal D_r\) consists of scalar matrices, whereas every
matrix in the range of \(\mathcal E_r\) is traceless.  If \(S\ne T\), choose
\(r\) in their symmetric difference.  In the \(r\)-th output tensor factor,
one range is scalar and the other traceless, so the corresponding tensor
subspaces are Hilbert--Schmidt orthogonal.  This proves (43). \(\square\)

In the zero-tolerance envelope, the squared centered radius in (32) is
\[
 {K_{N,k}^2\over D^2}
 ={1\over D}\left((1+9/N)^k-1\right)
 ={1\over D}\sum_{\varnothing\ne S\subseteq[k]}
                       (9/N)^{|S|}.                              \tag{44}
\]
Thus (44) is the generating function for the nonempty orthogonal sectors in
(43).  Adding the empty scalar sector \(1/D\) yields the collision-purity
envelope
\[
 {1\over D}+{K_{N,k}^2\over D^2}
 ={1\over D}(1+9/N)^k
 =\left({N+9\over N^2}\right)^k.                                \tag{45}
\]
Equivalently, the single-channel entropy lower envelope exposed by the dual
representation is
\[
 -\log\left[\left({N+9\over N^2}\right)^k\right]
 =k\log{N^2\over N+9}.                                         \tag{46}
\]
Equation (43) also locates the remaining quantitative issue more precisely:
one needs finite matrix models of total input dimension \(\exp(O(k))\) that
control all nonempty tensor sectors on entangled trace-class inputs at the
combined radius (44).  Lemma 7 supplies that combined control but gives no
rate for the matrix dimensions.

The algebra in (44)--(45) was checked with exact rational arithmetic at
\(N=5,k=4\).  The verbatim `python3` output is:

```text
subset_sum = 37791/390625 = 0.09674496
closed_form = 37791/390625 = 0.09674496
identical = True
purity_cap = 38416/390625 = 0.09834496
purity_closed_form = 38416/390625 = 0.09834496
purity_identical = True
```

For the numerical alphabet used in Section 11, the strengthened bound already
exceeds one bit at a smaller displayed block number.  An 80-decimal
`python3`/`mpmath` evaluation of (39) gives:

```text
N = 178482301, theta = 1e-9, k = 123714448
q = 22.60527551276656168999918114237559099468423597037968091017917196956594
new_bound = 0.6931471829180998488997343276295443963039308539138593853811865473164447
new_bound_minus_log2 = 0.000000002358154539482502206171367828228430719553604131260506537823051053042473
old_bound = 0.5239095965178743185845569371146032919382375824486103423982623234019942
old_bound_minus_log2 = -0.1692375840420709908326751843435732761372625519116449117224176860913994
```

This spectral improvement changes finite-block performance, but (40) shows
that its limiting slope is still exactly the rate \(c_N\) already identified
in (A2).

### Dated correction 2026-08-20

In the proof of Proposition 12, the malformed expression
\[
 \text{~~\(\log(1+\texttt{left}[\sqrt{a^k-1}+\theta]^2)\)~~}
\]
is a transcription error.  The entropy bound used there, consistently with
(36) and (39), is
\[
 k\log N-\log\left(1+\left[\sqrt{a^k-1}+\theta\right]^2\right). \tag{47}
\]
Also, the generating-function language following (44) refers only to the
aggregate constant indexed by subset cardinality.  Neither (44) nor Lemma 14
asserts the separate estimate
\(\|\mathcal E_S\|_{1\to2}^2\le D^{-1}(9/N)^{|S|}\) for each
\(S\).  What is proved is the orthogonal identity (43) together with the
combined bound (32).

For literal clarity, the erroneous source string is
~~`\log(1+left[\sqrt{a^k-1}+\theta]^2)`~~; equation (47) is the corrected
formula.

## Round 2026-08-20: sharp one-bit block threshold for the proved envelope

The numerical check following (46) exhibits a one-bit lower bound at
(k=123{,}714{,}448), using (N=178{,}482{,}301).  It leaves open whether a
different integer alphabet makes the rate (c_N) larger and thereby lowers
the block count.  This round settles exactly that optimization for the bound
(39)--(40).

### Proposition 15 (unique optimal integer alphabet)

Among all positive integers (N), the rate

\[
 c_N={\log N\over N}-2\log(1+9/N)
\]

has its unique maximum at

\[
 N_*=178{,}482{,}139.                                           \tag{48}
\]

**Proof.**  Extend the definition to real (x\ge1), and differentiate:

\[
 c'(x)={F(x)\over x^2},\qquad
 F(x)=19-\log x-{162\over x+9}.                                \tag{49}
\]

Moreover,

\[
 F'(x)=-{x^2-144x+81\over x(x+9)^2}.                            \tag{50}
\]

The two numerator roots in (50) are
(72\mathbin\pm\sqrt{5103}).  Since (F(1)=14/5>0), equation (50) says
that (F) first increases on the part of ([1,\infty)) preceding
(72+\sqrt{5103}), and then strictly decreases to (-\infty).  It therefore
has exactly one zero (x_*), and (c) increases up to (x_*) and decreases
after (x_*).

It remains to locate (x_*) and compare its two neighboring integers.  The
exact rational computation below applies the enclosure (28), with 46 terms
for each reduced large logarithm and four terms for
(\log(1+9/N)).  Thus every displayed endpoint is the decimal rendering of
an exact rational number, and every Boolean sign test is exact.

```text
method: exact fractions; 46 terms for reduced large logarithms, 4 terms for log(1+9/N)
N = 178482138
F_lower = 5.396176019433930125755276434809425346274795322087441302295844839879741538091797947977E-9
F_upper = 5.396176019433930125755276434809425349046753316453537748104643851852785097581453671140E-9
certified_F_positive = True
certified_F_negative = False
N = 178482139
F_lower = -2.066204326392977429163842729852020702666593749867069239530963205703461275647905201761E-10
F_upper = -2.066204326392977429163842729852020674947013806206104781442973085973025680751304929445E-10
certified_F_positive = False
certified_F_negative = True
c_178482139-minus-c_178482138_lower = 8.145366896147174806317054075462867532537952209090759218863477600202151169267241305189E-26
c_178482139-minus-c_178482138_upper = 8.145366896147174806317054078569013635069211149748752764549812710405131896423691485275E-26
certified_difference_positive = True
c_178482139_lower = 5.602798980237051511187867130022912492645102351604313988633487777063849977794951924539E-9
c_178482139_upper = 5.602798980237051511187867130022912492645102367135044457781982083127208555088529239571E-9
k = 123714447
k*c_178482139-minus-log2_lower = -3.067754552800110826357914851718519729673396775358270550679165683341812788059811136582E-9
k*c_178482139-minus-log2_upper = -3.067754552800110826357914851718519727649355932959066000210451529545785056208311197506E-9
certified_negative = True
certified_positive = False
k = 123714448
k*c_178482139-minus-log2_lower = 2.535044427436940684829952278304392762971705576246043437954322093722037189735140787957E-9
k*c_178482139-minus-log2_upper = 2.535044427436940684829952278304392764995746434175978457571530553581423498880218042066E-9
certified_negative = False
certified_positive = True
```

The first two sign enclosures put (x_*) strictly between
(178{,}482{,}138) and (178{,}482{,}139).  Monotonicity therefore reduces
the integer optimization to those two integers.  The certified positive
difference selects (178{,}482{,}139) uniquely, proving (48). \(\square\)

### Corollary 16 (smallest one-bit block count certified by (39))

The sharp block threshold for the one-bit target in the analytic envelope is

\[
 \min\{k\in\mathbb N:\text{ some }N\in\mathbb N\text{ has }
                    kc_N>\log2\}=123{,}714{,}448.                \tag{51}
\]

Consequently, at (N=N_*) and the block count in (51), the construction
gives finite-dimensional channels satisfying
(\Delta(\Phi_k,\overline\Phi_k)>\log2).

**Proof.**  The last four sign enclosures in the exact computation prove

\[
 123{,}714{,}447c_{N_*}<\log2
 <123{,}714{,}448c_{N_*}.                                      \tag{52}
\]

Proposition 15 gives (c_N\le c_{N_*}) for every integer (N\).  Hence no
(k\le123{,}714{,}447) and no integer alphabet can satisfy the inequality
inside (51), while the right inequality in (52) supplies a witness at the
next block count.  This proves (51).

For the channel assertion, set
(\delta=123{,}714{,}448c_{N_*}-\log2>0) and apply Corollary 13 with
(\varepsilon=\delta/2).  It gives

\[
 \Delta(\Phi_k,\overline\Phi_k)
 \ge kc_{N_*}-\delta/2=\log2+\delta/2>\log2.
\]

Finally, for every positive localization tolerance (\theta), the right
side of (39) is strictly smaller than (kc_N), because

\[
 1+\left[\sqrt{(1+9/N)^k-1}+\theta\right]^2>(1+9/N)^k.
\]

Thus (51) is also the smallest block count at which the finite-tolerance
bound (39) can certify a one-bit violation.  This is a sharp statement about
the present lower bound; it does not assert that the unknown exact gaps of
these or other channels cannot exceed one bit at a smaller block count.
\(\square\)

### Dated correction 2026-08-20

Several inline formulas in this round lost their Markdown delimiter
backslashes during transcription.  Thus, for example, the malformed strings
~~(k=123{,}714{,}448)~~, ~~(N=178{,}482{,}301)~~, ~~(c_N)~~,
~~(x\ge1)~~, and ~~(N=N_*)~~ are to be read, respectively, as
\[
 k=123{,}714{,}448,\qquad N=178{,}482{,}301,\qquad c_N,\qquad
 x\ge1,\qquad N=N_*.
\]
The same correction applies to the other plain-parenthesis TeX expressions
in the prose of Proposition 15 and Corollary 16.  The displayed equations,
the exact-arithmetic output, and all mathematical assertions are unchanged.

## Round 2026-08-20: the two-copy conic dual and the exact collision spectrum

The Schatten duality in Lemma 10 still relaxes the positive state space to the
entire trace-norm unit ball, and (21) still replaces the full output spectrum
by one collision moment.  This round separates and solves those two
relaxations.  A swap lift identifies the first as a quartic-positive conic
dual, while an exact spectral moment calculation removes the second.  The
result is a strict finite-block improvement of (40) for almost every alphabet,
although the sharp one-bit block count in (51) is unchanged.

### Lemma 17 (two-copy swap lift)

Let \(\mathcal C:M_d\to M_D\) be a channel, let

\[
 \mathcal L=P_0\mathcal C,
 \qquad \mathcal L(\rho)=\mathcal C(\rho)-{I_D\over D}
 \quad(\operatorname {Tr}\rho=1),
\]

and let \(F_D\) be the swap on \(\mathbb C^D\otimes\mathbb C^D\).  On the
two-copy input space define

\[
 Q_{\mathcal L}=(\mathcal L^*\otimes\mathcal L^*)(F_D).          \tag{53}
\]

Then, writing

\[
 r_+(\mathcal L)=\max_{\rho\ge0,\ \operatorname {Tr}\rho=1}
                         \|\mathcal L(\rho)\|_2,
\]

one has

\[
 \begin{split}
 \max_\rho\operatorname {Tr}\mathcal C(\rho)^2
 &= {1\over D}+r_+(\mathcal L)^2,\\
 r_+(\mathcal L)^2
 &=\max_{\|x\|=1}\langle x^{\otimes2},Q_{\mathcal L}
                                      x^{\otimes2}\rangle .     \tag{54}
 \end{split}
\]

**Proof.**  For arbitrary matrices \(A,B\),
\(\operatorname {Tr}(F_D(A\otimes B))=\operatorname {Tr}(AB)\).
Since \(\mathcal L(\rho)\) is Hermitian for a state \(\rho\), adjointness
therefore gives

\[
 \begin{split}
 \|\mathcal L(\rho)\|_2^2
 &=\operatorname {Tr}\!\left[F_D
       (\mathcal L(\rho)\otimes\mathcal L(\rho))\right]\\
 &=\operatorname {Tr}\!\left[Q_{\mathcal L}(\rho\otimes\rho)\right].
                                                                    \tag{55}
 \end{split}
\]

The squared norm on the left is convex in \(\rho\).  If
\(\rho=\sum_jp_j|x_j\rangle\langle x_j|\), convexity shows that its value is
at most \(\sum_jp_j\|\mathcal L(|x_j\rangle\langle x_j|)\|_2^2\), so some
pure component has at least the value at \(\rho\).  Substitution of a pure
state in (55) proves the second equality in (54).  The two terms in
\(\mathcal C(\rho)=I_D/D+\mathcal L(\rho)\) are Hilbert--Schmidt orthogonal,
which proves the first equality. \(\square\)

Let \(P_{\rm sym}\) be the projection onto
\(\operatorname {Sym}^2(\mathbb C^d)\), put
\(Q_s=P_{\rm sym}Q_{\mathcal L}P_{\rm sym}\), and introduce the cone

\[
 \mathfrak B_{\rm Ver}=
 \{Y=Y^*:\langle x^{\otimes2},Yx^{\otimes2}\rangle\ge0
                         \text{ for every }x\}.                 \tag{56}
\]

This is the cone of Hermitian forms nonnegative on the quadratic Veronese
image \(x\mapsto x^{\otimes2}\).

### Proposition 18 (exact conic dual and its SDP relaxation)

The state-restricted radius in Lemma 17 has the exact dual representation

\[
 r_+(\mathcal L)^2
 =\min\{t\in\mathbb R:tI_{\rm sym}-Q_s\in\mathfrak B_{\rm Ver}\}. \tag{57}
\]

Relaxing the convex hull of the Veronese projectors to all density matrices
on the symmetric subspace gives the semidefinite program and its dual

\[
 \begin{split}
 \max\ &\operatorname {Tr}(Q_sZ)
       && Z\ge0,\quad\operatorname {Tr}Z=1,\\
 =\min\ &t
       && tI_{\rm sym}-Q_s\ge0,
 \end{split}                                                     \tag{58}
\]

whose common value is \(\lambda_{\max}(Q_s)\).  Hence

\[
 r_+(\mathcal L)^2\le\lambda_{\max}(Q_s).                       \tag{59}
\]

For the localized channels, (32) supplies the exact quartic-positive
certificate

\[
 \left({K_{N,k}+\eta\over D}\right)^2I_{\rm sym}-Q_s
       \in\mathfrak B_{\rm Ver}.                                \tag{60}
\]

It does not assert that the operator in (60) is positive semidefinite.

**Proof.**  By (54), a scalar \(t\) dominates \(r_+(\mathcal L)^2\) exactly
when
\(\langle x^{\otimes2},(tI_{\rm sym}-Q_s)x^{\otimes2}\rangle\ge0\)
for every unit vector \(x\).  Homogeneity extends this to every \(x\), which
is precisely (57).  The feasible set in the first line of (58) is the set of
all density matrices on the symmetric subspace.  Linear optimization over
that set gives the largest eigenvalue; equivalently,
\(tI_{\rm sym}-Q_s\ge0\) holds exactly when
\(t\ge\lambda_{\max}(Q_s)\).  This proves (58)--(59).  Equation (32), applied
to a state and then squared, gives
\(\langle x^{\otimes2},Q_sx^{\otimes2}\rangle
 \le((K_{N,k}+\eta)/D)^2\); (60) follows from (56). \(\square\)

Thus the norm localization is naturally a certificate in a
quartic-positive cone.  Replacing that cone by the PSD cone is an SDP
relaxation, while replacing positive states by the full trace-norm ball is a
different relaxation.  The next example shows that this distinction is
already strict in dimension two.

### Example 19 (a factor-two positivity gap)

Let \(X,Y,Z\) be the Pauli matrices and define the qubit channel

\[
 \mathcal C(A)={1\over2}A+{1\over4}XAX+{1\over4}ZAZ.             \tag{61}
\]

This is a convex mixture of unitary conjugations.  If
\(\mathcal L(A)=\mathcal C(A)-\operatorname {Tr}(A)I_2/2\), then

\[
 r_+(\mathcal L)^2={1\over8},\qquad
 \|\mathcal L\|_{S_1\to S_2}^2={1\over4},\qquad
 \lambda_{\max}(Q_s)={1\over4}.                               \tag{62}
\]

**Proof.**  For
\(\rho=(I+xX+yY+zZ)/2\),

\[
 \mathcal C(\rho)={I\over2}+{xX+zZ\over4},\qquad
 \|\mathcal L(\rho)\|_2^2={x^2+z^2\over8}.                   \tag{63}
\]

The Bloch-ball condition gives \(x^2+y^2+z^2\le1\), and equality in the
first value of (62) is obtained by an \(X\)-eigenstate.  On arbitrary input,

\[
 \mathcal L(A)={\operatorname {Tr}(XA)X+\operatorname {Tr}(ZA)Z\over4},
 \quad
 \|\mathcal L(A)\|_2^2=
 { |\operatorname {Tr}(XA)|^2+|\operatorname {Tr}(ZA)|^2\over8}. \tag{64}
\]

Schatten duality bounds each absolute trace in (64) by \(\|A\|_1\), so the
full norm squared is at most \(1/4\).  If \(|y_+\rangle,|y_-\rangle\) are
the two \(Y\)-eigenvectors, then
\(A=|y_+\rangle\langle y_-|\) has trace norm one and both matrix elements in
(64) have modulus one.  This proves the middle value of (62).  Directly from
(53), or by comparing (55) and (63),

\[
 Q_s=P_{\rm sym}{X\otimes X+Z\otimes Z\over8}P_{\rm sym}.       \tag{65}
\]

The symmetric Bell vector \((|00\rangle+|11\rangle)/\sqrt2\) has eigenvalue
\(1/4\) in (65), and the other two symmetric eigenvalues are zero.  This
proves the remaining value in (62). \(\square\)

In this example the exact maximum output purity is \(1/2+1/8=5/8\), whereas
the SDP relaxation gives \(1/2+1/4=3/4\).  The following was the verbatim
`python3` numerical check of the Choi matrix, the trace-norm witness, and the
symmetric compression:

```text
choi_eigenvalues = [0.0, 0.5, 0.5, 1.0]
state_radius_squared = 0.125
trace_norm_witness = 1.0
witness_image_squared = 0.25
symmetric_Q_eigenvalues = [0.0, 0.0, 0.25]
actual_max_output_purity = 0.625
sdp_purity_upper_bound = 0.75
```

The second relaxation, from purity to entropy, can be solved exactly.

### Lemma 20 (exact entropy at fixed collision cap)

For \(D\ge2\) and \(1/D\le p\le1\), define

\[
 \mathsf H_D(p)=\min\left\{-\sum_{i=1}^D\lambda_i\log\lambda_i:
 \lambda_i\ge0,\ \sum_i\lambda_i=1,\ \sum_i\lambda_i^2\le p\right\}.
                                                                    \tag{66}
\]

Put \(m=\lfloor1/p\rfloor\) and

\[
 s=\sqrt{{(m+1)p-1\over m}},\qquad
 x={1+s\over m+1},\qquad
 y={1-ms\over m+1}.                                             \tag{67}
\]

With the convention \(0\log0=0\),

\[
 \mathsf H_D(p)=-mx\log x-y\log y.                             \tag{68}
\]

The minimizing spectrum consists of \(m\) copies of \(x\), one copy of
\(y\), and zeros; a zero copy of \(y\) is omitted.  In particular,

\[
 \mathsf H_D(p)\ge-\log p,                                     \tag{69}
\]

with equality exactly when \(1/p\) is an integer.

**Proof.**  Compactness gives a minimizer.  Except at the forced uniform case
\(p=1/D\), its collision constraint is active.  Indeed, if the collision
sum were strictly below \(p\), transferring a sufficiently small mass from
one positive coordinate to another would increase collision while decreasing
the strictly concave entropy; the transfer can be repeated away from the
uniform point.  This contradicts minimality.

Work in the relative interior of the face determined by the positive
coordinates of a minimizing vector.  If they are not all equal, the gradients
of normalization and collision are independent.  Lagrange multipliers give

\[
 -\log\lambda_i-1=\alpha+2\beta\lambda_i.                       \tag{70}
\]

The equation in (70) has at most two positive solutions: after rearrangement
it is a level-set equation for a function whose derivative is monotone and
has at most one zero.  Suppose its two solutions are \(a>b>0\).  Set

\[
 L={\log(a/b)\over a-b}.
\]

Subtracting (70) at \(a\) and \(b\) gives \(2\beta=-L\).  The Hessian of the
Lagrangian in a coordinate having value \(b\) is consequently

\[
 -{1\over b}-2\beta=L-{1\over b}<0,                             \tag{71}
\]

where the strict inequality is the mean-value theorem applied to \(\log\).
If two coordinates had the smaller value \(b\), the vector that adds to one
and subtracts from the other would be tangent to both equality constraints,
but (71) would give a negative second variation.  This violates the
second-order necessary condition for a constrained local minimum.  Hence the
smaller positive value occurs once.

There are therefore \(r\) copies of a larger value \(a\) and one smaller
value \(b\), unless the positive spectrum is uniform.  The equations
\(ra+b=1\) and \(ra^2+b^2=p\), together with \(0\le b<a\), imply

\[
 {1\over r+1}<p\le {1\over r},\qquad r=\lfloor1/p\rfloor=m.
\]

Solving the two equations gives exactly (67), proving (68); the reciprocal
boundary cases give a uniform positive spectrum and the same formula with
\(y=0\).  Inequality (69) is Jensen's inequality applied to \(-\log\) with
weights \(\lambda_i\):

\[
 -\sum_i\lambda_i\log\lambda_i
 \ge-\log\sum_i\lambda_i^2.
\]

Equality requires all positive \(\lambda_i\) to be equal, which is possible
at collision \(p\) exactly when \(1/p\) is an integer. \(\square\)

For example, at \(D=7\) and \(p=3/10\), the exact optimizer has three copies
of \(x\) and one copy of \(y\).  A 50-decimal `python3` check gave:

```text
D = 7 p = 3/10 m = 3
x = 0.3145497224367902814196544233297066601805486950882
y = 0.05635083268962915574103673001088001945835391473542
m*x+y = 1.0000000000000000000000000000000000000000000000000
m*x^2+y^2 = 0.30000000000000000000000000000000000000000000000001
H_min = 1.2535109162116579219263852878110139300769459225042
-log(p) = 1.2039728043259359926227462177618385029536109308060
strict_improvement = 0.0495381118857219293036390700491754271233349916982
```

The last digit in the displayed collision sum is the rounding error from the
50-decimal square root; equations (67) satisfy both constraints algebraically.
For the Pauli channel in Example 19, Lemma 20 is attained by the spectrum
\((3/4,1/4)\), and the same numerical check gives

```text
qubit_exact_min_entropy = 0.562335144618808
qubit_collision_lower_bound = 0.470003629245736
entropy_gain_from_exact_spectrum = 0.092331515373073
```

### Corollary 21 (the exact spectral refinement of the gap envelope)

Fix \(N\ge4\), \(k\ge1\), and set

\[
 D=N^k,\qquad
 p_{N,k}=\left({N+9\over N^2}\right)^k,\qquad
 R_{N,k}={1\over p_{N,k}}=\left({N^2\over N+9}\right)^k.       \tag{72}
\]

Define

\[
 \delta_{N,k}=\mathsf H_D(p_{N,k})-\log R_{N,k}.                \tag{73}
\]

For every \(\varepsilon>0\), the channels in Theorem A can be chosen so that

\[
 \Delta(\Phi_k,\overline\Phi_k)
 \ge k c_N+2\delta_{N,k}-\varepsilon.                           \tag{74}
\]

Moreover, if \(m=\lfloor R_{N,k}\rfloor\), then

\[
 0\le\delta_{N,k}< {1\over m}.                                 \tag{75}
\]

The first inequality is strict unless \(N\in\{18,72\}\).

**Proof.**  With the tolerance choice in Proposition 12, (38) gives the
purity cap

\[
 p(\theta)={1\over D}
 \left(1+\left[\sqrt{(1+9/N)^k-1}+\theta\right]^2\right),       \tag{76}
\]

which decreases to \(p_{N,k}\) as \(\theta\downarrow0\).  Lemma 20 applied
to every output replaces (36) by
\(S_{\min}(\mathcal C^{[k]})\ge\mathsf H_D(p(\theta))\).
The explicit formula (67)--(68) is continuous, including at reciprocal
boundary points.  Subtracting (23), taking \(\theta\) sufficiently small,
and using

\[
 2\log R_{N,k}-2k\log N+{k\log N\over N}=kc_N
\]

proves (74).

Lemma 20 gives \(\delta_{N,k}\ge0\).  Its optimizer has support at most
\(m+1\), so

\[
 \delta_{N,k}\le\log(m+1)-\log R_{N,k}
 \le\log(1+1/m)<1/m,                                           \tag{77}
\]

with the integer case even giving \(\delta_{N,k}=0\).  Equality in (69)
shows that \(\delta_{N,k}=0\) exactly when \(R_{N,k}\) is an integer.  A
power of a reduced positive rational is an integer only when that rational
already is an integer.  Also,

\[
 {N^2\over N+9}\in\mathbb N
 \quad\Longleftrightarrow\quad N+9\mid N^2
 \quad\Longleftrightarrow\quad N+9\mid81.                      \tag{78}
\]

For \(N\ge4\), the eligible divisors of \(81\) are \(27\) and \(81\),
giving \(N=18\) and \(N=72\).  This proves all assertions. \(\square\)

Thus (74) is the strongest entropy conclusion obtainable from only the trace
and the collision cap (38).  For every alphabet except \(18\) and \(72\), it
strictly improves (40) at each fixed block number.  Bound (75) also shows why
the gain becomes extremely small when the effective collision rank
\(R_{N,k}\) is large.

The integer assertion in (78) was checked directly over a redundant finite
range; the proof itself reduces the search to divisors of \(81\):

```text
integer N^2/(N+9) for 4 <= N < 500: [(18, 12), (72, 64)]
divisors of 81 at least 13: [27, 81]
```

### Proposition 22 (stability of the sharp one-bit certificate)

Let \(N_*=178{,}482{,}139\) and \(K=123{,}714{,}448\).  For the refined
zero-tolerance envelope

\[
 B_{N,k}=kc_N+2\delta_{N,k}\qquad(N\ge4),                       \tag{79}
\]

one has

\[
 \min\{k:\text{there is an integer }N\ge4
                 \text{ with }B_{N,k}>\log2\}=K.               \tag{80}
\]

Hence the exact collision-spectrum conversion improves the certified gap but
does not lower the block count in (51).

**Proof.**  At \(N=N_*\) and \(k=K\), (52) and
\(\delta_{N,k}\ge0\) give \(B_{N_*,K}>\log2\).

It remains to exclude \(k<K\).  First suppose \(c_N\le0\), and put
\(m=\lfloor R_{N,k}\rfloor\).  If \(m\ge3\), (75) gives

\[
 B_{N,k}< {2\over m}\le {2\over3}<\log2,                       \tag{81}
\]

where the last strict inequality follows already from the first positive
term \(2/3\) in the series (28) for \(\log2\).  Since
\(N^2/(N+9)\) is increasing in \(N\), the cases \(N\ge7\) have \(m\ge3\).
The cases with \(N\ge4\) and \(m\le2\) are exactly

\[
 (N,k)=(4,1),(4,2),(4,3),(4,4),(4,5),(5,1),(6,1).              \tag{82}
\]

For a distribution supported on at most \(m+1\) points,
\(\mathsf H_D(p)\le\log(m+1)\).  Consequently the value in (79), written
in its pre-\(\delta\) form, obeys

\[
 B_{N,k}\le2\log(m+1)-k(2-1/N)\log N.                         \tag{83}
\]

For the three alphabets in (82), negativity of (83) follows respectively
from
\(3^8<4^7\), \(2^{10}<5^9\), and \(3^{12}<6^{11}\).  Thus (81) also holds
in all the exceptional small-rank cases.

Now suppose \(c_N>0\).  Lemma 9 gives \(N\ge65{,}659{,}889\), Proposition
15 gives \(c_N\le c_{N_*}<6\cdot10^{-9}\), and
\(\lfloor N^2/(N+9)\rfloor=N-9\).  For \(k<100\), (75) therefore gives

\[
 B_{N,k}<100(6\cdot10^{-9})+{2\over65{,}659{,}880}
 <10^{-6}<\log2.                                                \tag{84}
\]

For \(100\le k\le K-1\), monotonicity of \(N^2/(N+9)\) and exact rational
arithmetic give

\[
 m\ge\left\lfloor(16/13)^{100}\right\rfloor
   =1{,}041{,}509{,}018.                                       \tag{85}
\]

The certified interval in Proposition 15 shows
\(\log2-(K-1)c_{N_*}>3\cdot10^{-9}\), whereas

\[
 {2\over1{,}041{,}509{,}018}<3\cdot10^{-9}.                    \tag{86}
\]

Equations (75), (85), and (86) imply
\(B_{N,k}\le kc_{N_*}+2/m<\log2\).  This covers every \(N\ge4\) and every
\(k<K\), proving (80).  For \(N\le3\), the cap in (72) exceeds one and its
only spectral consequence is the trivial entropy lower bound zero, which
cannot certify a positive one-bit gap. \(\square\)

Here is the verbatim exact-arithmetic `python3` output for the finite checks
in (82), (85), and (86):

```text
pairs_with_floor_R_at_most_2 = [(4, 1, 1), (4, 2, 1), (4, 3, 1), (4, 4, 2), (4, 5, 2), (5, 1, 1), (6, 1, 2)]
3^8 < 4^7 = True
2^10 < 5^9 = True
3^12 < 6^11 = True
(16/13)^5 < 3 = True
(16/13)^6 > 3 = True
floor((16/13)^100) = 1041509018
2/floor = 1.9202906220059248685257183246011989883701611885611E-9
2/floor < 3e-9 = True
```

The conic representation also isolates a remaining route not visible in the
collision-spectrum calculation.  The entropy argument needs only
\(r_+(P_0\mathcal C^{[k]})\), while Lemma 10 controls the larger norm
\(\|P_0\mathcal C^{[k]}\|_{S_1\to S_2}\).  Example 19 proves that these can
differ even for a mixed-unitary qubit channel.  A state-positive localization
bound improving (32) at exponential scale would improve the rate \(c_N\);
whether the product free-unitary model admits such an improvement is
**[UNPROVED]**.

## Round 2026-08-20: adversarial rank obstruction and a fixed-pair correction

This round attempted to contradict the finite localization step by forcing its
matrix dimension to be too small.  The attempt produces an explicit violating
coefficient matrix below every admissible dimension threshold.  It does not
contradict Lemma 7, because that lemma places no upper bound on the selected
matrix dimensions.  The calculation nevertheless gives a necessary
exponential dimension and identifies exactly why a rank-based counterexample
cannot settle the remaining qubit-linear question.

### Lemma 23 (a universal finite-rank obstruction to localization)

Let (W_1,\ldots,W_D\) be unitaries on \(\mathbb C^d\), and define

\[
 \mathcal T_W(a)=\sum_{v,w=1}^D a_{vw}W_v^*W_w.
\]

If (r=\min\{d,D\}), then

\[
 \left\|\mathcal T_W|_{M_D^0}\right\|_{S_2\to S_\infty}
 \ge \sqrt{{D^2\over r}-D}.                                    \tag{87}
\]

More explicitly, whenever the right side is positive, a trace-zero matrix
violating any smaller proposed norm bound can be constructed from the Gram
matrix of the vectors (W_vx) for an arbitrary unit vector (x).

**Proof.**  Fix a unit vector (x), and let

\[
 G_{vw}=\langle W_vx,W_wx\rangle
       =\langle x,W_v^*W_wx\rangle .                            \tag{88}
\]

The matrix (G) is positive, has trace (D), and has rank at most (r).
If \(\lambda_1,\ldots,\lambda_r\) are its eigenvalues, Cauchy--Schwarz gives

\[
 \operatorname {Tr}G^2=\sum_j\lambda_j^2
 \ge {\left(\sum_j\lambda_j\right)^2\over r}={D^2\over r}.
                                                                    \tag{89}
\]

Since (P_0G=G-I_D), Hilbert--Schmidt orthogonality gives

\[
 \|P_0G\|_2^2=\operatorname {Tr}G^2-D
 \ge {D^2\over r}-D.                                           \tag{90}
\]

When (P_0G\ne0), put

\[
 a={\overline {P_0G}\over\|P_0G\|_2}.
\]

Then \(\operatorname {Tr}a=0\), \(\|a\|_2=1\), and (88) gives

\[
 \begin{split}
 \|\mathcal T_W(a)\|_\infty
 &\ge |\langle x,\mathcal T_W(a)x\rangle|\\
 &= {\left|\sum_{v,w}\overline{(P_0G)_{vw}}G_{vw}\right|
       \over\|P_0G\|_2}
 =\|P_0G\|_2.
 \end{split}                                                     \tag{91}
\]

Equations (90)--(91) prove (87).  If the right side of (87) is zero, the
claim is immediate. \(\square\)

### Corollary 24 (necessary total input dimension)

For the product tuple in Lemma 7, put

\[
 D=N^k,\qquad d=\prod_{j=1}^k d_j,
 \qquad a=1+{9\over N}.
\]

If (15) holds, then necessarily

\[
 d\ge {D^2\over D+(K_{N,k}+\eta)^2}.                           \tag{92}
\]

With the tolerance \(\eta=\theta\sqrt D\) used in Proposition 12, this is

\[
 d\ge {D\over
  1+\left[\sqrt{a^k-1}+\theta\right]^2}.                       \tag{93}
\]

Consequently, for all sufficiently small positive \(\theta\), the integer
dimension obeys

\[
 d\ge \left\lceil\left({N^2\over N+9}\right)^k\right\rceil . \tag{94}
\]

Here (94) is the eventual small-tolerance statement; no finite tuple with
positive tolerance is asserted to attain the zero-tolerance endpoint.

**Proof.**  Lemma 23 and (15) imply

\[
 {D^2\over r}-D\le(K_{N,k}+\eta)^2,
 \qquad r=\min\{d,D\}.
\]

Rearranging and using (d\ge r) proves (92).  Since

\[
 K_{N,k}^2=D(a^k-1),
\]

substitution gives (93).  Its right side converges as
\(\theta\downarrow0\) to

\[
 {D\over a^k}=\left({N^2\over N+9}\right)^k.                  \tag{95}
\]

Continuity and integrality imply (94): if the limit is nonintegral, the
ceiling is locally constant from below, while if it is an integer (q), the
right side of (93) lies in ((q-1,q)) for all sufficiently small positive
\(\theta\), and hence its ceiling is (q). \(\square\)

There is an equivalent channel interpretation.  For a pure input, the output
of \(\mathcal C^{[k]}\) is the Gram matrix of (D) vectors in
\(\mathbb C^d\), divided by (D), and hence has rank at most (d).  Its
purity is therefore at least (1/d).  Combining this with (38) gives exactly
(92).  Thus the obstruction is not an artifact of Schatten duality: a model
below (92) necessarily has an output state that is too low-rank to satisfy the
claimed collision cap.

The rank mechanism in Lemma 23 is sharp for a single Gram state.  Indeed, for
(1\le d\le D), let

\[
 (z_v)_j={1\over\sqrt d}\exp(2\pi i jv/D),
 \qquad 0\le j<d,\quad0\le v<D.                               \tag{96}
\]

The (z_v) are unit vectors and the root-of-unity sum gives

\[
 \sum_{v=0}^{D-1}|z_v\rangle\langle z_v|={D\over d}I_d.
\]

Their Gram matrix therefore has (d) eigenvalues equal to (D/d) and
(D-d) zero eigenvalues, so equality holds in (89)--(90).  Fixing a unit
vector (x), each assignment (x\mapsto z_v) extends to a unitary (W_v).
Hence no argument using only the rank, trace, and one selected input vector can
improve (87).  A stronger obstruction would have to use the simultaneous
supremum over all input vectors and all coefficient matrices, or the product
structure of the (W_v).  Whether those features force a superexponential
dimension is **[UNPROVED]**.

For comparison, the lower bound (95) already has logarithm linear in (k):

\[
 \log d\ge k\log{N^2\over N+9}.                                \tag{97}
\]

Therefore it is fully compatible with the desired condition
\(\log d=O(k)\).  This is exactly what blocks the rank attack: it proves that
exponentially large matrices are necessary, while a counterexample to the
qubit-linear localization route would need an obstruction stronger than every
\(\exp(Ck)\) upper bound.

The following is the verbatim `python3` output for a (D=7,d=3) Fourier
frame.  It checks the equality case of (90); it is not used in its proof.

```text
D = 7 d = 3
column_norms = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
gram_eigenvalues = [-0.0, -0.0, 0.0, 0.0, 2.333333333333, 2.333333333333, 2.333333333333]
centered_frobenius_squared = 9.333333333333
rank_lower_bound_squared = 9.333333333333
absolute_difference = 7.105e-15
```

At the sharp one-bit parameters of Proposition 22, the rank obstruction is
nearly as large as the complementary output dimension.  Solving (39) exactly
for its permitted tolerance gives

\[
 \theta_{\max}=
 \sqrt{\exp\!\left({k\log N/N-\log2\over2}\right)-1}
 -\sqrt{(1+9/N)^k-1}.                                          \tag{98}
\]

The right side of (39) exceeds one bit precisely for
\(0<\theta<\theta_{\max}\).  Here is the verbatim 80-decimal
`python3`/`decimal` output at (N=N_*), (k=K), including a test at half
the permitted tolerance:

```text
N = 178482139
k = 123714448
log2_zero_tolerance_rank_lower = 3391162020.7392034823848379909904044207430613751838751346638305677579766739418705
log2_output_dimension = 3391162029.7392073709712621868311547408644493592245506153579897789330838832308001
output_minus_rank_lower_bits = 9.0000038885864241958407503201213879840406754806941592111751072092889296
q0 = 22.605339635306755984371888510290455434827469975112299905508596621424118920352955
theta_max_for_strict_one_bit_bound = 1.4354420975632821608706818053152129008080501257290310319224018458598728E-8
theta_test = theta_max/2 = 7.177210487816410804353409026576064504040250628645155159612009229299364E-9
log2_rank_lower_at_theta_test = 3391162020.7392034814705139848717031733788438136719342905217254916800990531214195
gap_bound_minus_log2_at_theta_test = 1.26752221351803677805649379615326255508116542400040259517805022477492028E-9
theta_test_positive = True
gap_margin_positive = True
```

Thus this certificate needs at least about (3.391\) billion input qubits, but
that number is still a constant times (k).  More strikingly, the
zero-tolerance rank lower bound is only about nine qubits below the
(N^k)-dimensional output at this optimized threshold.  This illustrates the
severity of the necessary dimension without turning it into a contradiction.

### Lemma 25 (the fixed conjugate-pair route is not ruled out by Lemma 4)

For every finite-dimensional channel \(\Phi\),

\[
 \lim_{m\to\infty}{1\over m}
 \Delta(\Phi^{\otimes m},\overline\Phi^{\otimes m})
 =2\overline S_{\min}(\Phi)
  -\overline S_{\min}(\Phi\otimes\overline\Phi).              \tag{99}
\]

There is no algebraic reason in Lemma 4 for the right side of (99) to vanish.

**Proof.**  Entrywise conjugation preserves every output spectrum, so

\[
 S_{\min}(\overline\Phi^{\otimes m})
 =S_{\min}(\Phi^{\otimes m}).
\]

After permuting tensor factors,
\(\Phi^{\otimes m}\otimes\overline\Phi^{\otimes m}\) is
unitarily equivalent to
\((\Phi\otimes\overline\Phi)^{\otimes m}\).  Divide the definition of
the gap by (m) and take the three regularized limits, exactly as in Lemma 3.
This proves (99).  Lemma 4 instead uses the special identity
\(\Phi^{\otimes m}\otimes\Phi^{\otimes m}=\Phi^{\otimes2m}\), which has
no analogue for a general conjugate pair. \(\square\)

### Dated correction 2026-08-20

The sentence in Section 2 that Lemma 4 explains why
~~simply tensoring a single Hastings counterexample with itself cannot settle
the extensive question~~ is valid only for literal self-pairs
\((\Phi,\Phi)\).  It does not rule out powers of a fixed conjugate pair
\((\Phi,\overline\Phi)\); their normalized gap is (99).

Likewise, the sentence in Section 3 that
~~the entire problem is therefore to choose different tuples~~ and the final
sentence of item 3 in Section 8 are too strong as necessity statements.
Different tuples are essential to the *iterated localization proof given
here*.  The possibility that one fixed finite tuple has a positive right side
in (99) is **[UNPROVED in this document]**.  This correction does not affect
Lemma 7, Theorem A, or any subsequent numerical bound.

Finally, an exhaustive lattice search was used to attack the independent
spectral minimization in Lemma 20.  It enumerated every probability vector on
the indicated grids and retained exactly those meeting the rational collision
cap.  No grid point fell below (68).  This is only a finite falsification
attempt, not an additional proof of Lemma 20.  The verbatim `python3` output
was:

```text
D=4 grid=1/60 p=3/10 checked=39711 feasible=5089
  grid_min = 1.262074185283268 formula = 1.253510916211658 excess = 0.008563269071610 below_formula = False arg = (4, 16, 18, 22)
D=4 grid=1/60 p=2/5 checked=39711 feasible=22431
  grid_min = 0.987619922731819 formula = 0.980132210439209 excess = 0.007487712292611 below_formula = False arg = (0, 8, 23, 29)
D=4 grid=1/60 p=4/5 checked=39711 feasible=39375
  grid_min = 0.360230521194607 formula = 0.352126806119068 excess = 0.008103715075539 below_formula = False arg = (0, 0, 7, 53)
D=5 grid=1/50 p=11/50 checked=316251 feasible=5841
  grid_min = 1.549801049034985 formula = 1.547011621628514 excess = 0.002789427406471 below_formula = False arg = (4, 10, 11, 12, 13)
D=5 grid=1/50 p=7/20 checked=316251 feasible=195251
  grid_min = 1.073653448656075 formula = 1.071918037669576 excess = 0.001735410986499 below_formula = False arg = (0, 0, 12, 17, 21)
D=5 grid=1/50 p=13/20 checked=316251 feasible=311226
  grid_min = 0.551079928086973 formula = 0.534568454961381 excess = 0.016511473125592 below_formula = False arg = (0, 0, 0, 12, 38)
```

The attempted counterexample is therefore blocked at two precise places.
For Theorem A itself, any tuple below (92) is refuted explicitly by (91), but
Lemma 7 is free to choose a larger finite dimension, and its finite-net proof
has no quantitative ceiling to contradict.  For the stronger qubit-linear
formulation, the only dimension obstruction proved here is (97), which is
already linear in (k) qubits.  A disproof by dimension would require a new
global lower bound forcing \(\log d/k\to\infty\); no such bound is presently
proved.  Separately, powers of one fixed conjugate pair remain a logically
available route by (99), despite the earlier self-power wording.

### Dated formatting correction 2026-08-20

Several inline formulas in this round lost their opening Markdown delimiter
backslashes during transcription.  Thus plain-parenthesis expressions such as
~~(W_1,\ldots,W_D)~~, ~~(r=\min\{d,D\})~~, ~~(P_0G=G-I_D)~~,
~~(N=N_*)~~, ~~(k=K)~~, and ~~(N^k)~~ are to be read as
\[
 W_1,\ldots,W_D,\qquad r=\min\{d,D\},\qquad P_0G=G-I_D,\qquad
 N=N_*,\qquad k=K,\qquad N^k.
\]
The malformed string ~~(3.391\)~~ is \(3.391\).  The same delimiter correction
applies to every other plain-parenthesis TeX expression in the prose of this
round.  The displayed equations, proofs, numerical output, and mathematical
assertions are unchanged.

## Round 2026-08-21: exact collapse of the two-unitary alphabet

The fixed conjugate-pair possibility left open after Lemma 25 can first be
tested inside the random-unitary construction at alphabet size (N=2).  The
case (N=1) is immediate because the channel is a single unitary
conjugation.  The next proposition settles the smallest nontrivial alphabet,
including unequal tuples in different tensor positions.

### Proposition 26 (two-unitary products have zero conjugate gap)

For (1\le r\le k), let

\[
 U^{(r)}=(U^{(r)}_1,U^{(r)}_2)\in U(d_r)^2,
 \qquad
 \Phi=\bigotimes_{r=1}^k\mathcal R_{U^{(r)}}.
\]

Then

\[
 S_{\min}(\Phi)=S_{\min}(\overline\Phi)
 =S_{\min}(\Phi\otimes\overline\Phi)=0,
 \qquad
 \Delta(\Phi,\overline\Phi)=0.                               \tag{100}
\]

In particular, for a fixed two-unitary tuple (U) and every (m\ge1),

\[
 \Delta(\mathcal R_U^{\otimes m},
        \overline{\mathcal R_U}^{\otimes m})=0,                \tag{101}
\]

and the regularized expression on the right of (99) is zero.

**Proof.**  For every (r), the unitary

\[
 V_r=(U^{(r)}_1)^*U^{(r)}_2
\]

has a unit eigenvector (x_r), say (V_rx_r=\lambda_rx_r) with
(|\lambda_r|=1).  Therefore

\[
 U^{(r)}_2x_r=U^{(r)}_1V_rx_r
 =\lambda_rU^{(r)}_1x_r.                                     \tag{102}
\]

The two pure states in the defining mixture (7) are consequently the same:

\[
 \mathcal R_{U^{(r)}}(|x_r\rangle\langle x_r|)
 =|U^{(r)}_1x_r\rangle\langle U^{(r)}_1x_r|.                  \tag{103}
\]

Thus every factor has a pure output.  On the product input
(x=x_1\otimes\cdots\otimes x_k), equation (103) shows that
(Phi(|x\rangle\langle x|)) is pure, and hence
(S_{\min}(\Phi)=0).  Complex conjugating (102) gives the same conclusion
for (overline\Phi), using the input (overline x).  Finally,
(x\otimes\overline x) produces a pure output of
(Phi\otimes\overline\Phi).  Entropy is nonnegative, so all three minima
in (100) are exactly zero, which proves (100).

Taking all (U^{(r)}=U) proves (101).  It also shows for every (m) that

\[
 S_{\min}(\mathcal R_U^{\otimes m})
 =S_{\min}((\mathcal R_U\otimes
             \overline{\mathcal R_U})^{\otimes m})=0.
\]

Dividing by (m) gives
(overline S_{\min}(\mathcal R_U)=
\overline S_{\min}(\mathcal R_U\otimes
\overline{\mathcal R_U})=0), so (99) vanishes.  By Lemma 1, replacing any
of these channels by complementary channels leaves the conclusions
unchanged. \(\square\)

Hence neither the distinct-block localization construction nor the
fixed-tuple route can yield a positive gap with two unitaries per block.  The
mechanism is exact and precedes every norm or collision-entropy relaxation:
two unitary images of an eigenvector of (U_1^*U_2) determine the same pure
state.  Alphabet size (N=3) is therefore the smallest random-unitary case
not decided by this eigenvector argument.

The following exact `python3`/`sympy` computation checks a representative
finite instance, with (U_1=I_3), (U_2=\operatorname{diag}(1,i,-1)), and
(x=(0,1,0)^T).  It verifies both channel outputs and the conjugate-product
witness.  The general proof above does not depend on this example.

```text
U1starU2*x = [0, I, 0]
R = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
rank(R) = 1 charpoly(R) = lambda**2*(lambda - 1)
C = [[1/2, -I/2], [I/2, 1/2]]
rank(C) = 1 charpoly(C) = lambda*(lambda - 1)
rank(R tensor conjugate(R)) = 1
charpoly(R tensor conjugate(R)) = lambda**8*(lambda - 1)
purities = 1 1 1
```

### Dated formatting correction 2026-08-21

Several inline formulas in this round lost their opening and closing Markdown
delimiter backslashes during transcription.  Thus the malformed strings
~~(N=2)~~, ~~(N=1)~~, ~~(1\le r\le k)~~, ~~(U)~~, ~~(m\ge1)~~,
~~(V_rx_r=\lambda_rx_r)~~, ~~(|\lambda_r|=1)~~, and ~~(N=3)~~ are
to be read, respectively, as

\[
 N=2,\qquad N=1,\qquad 1\le r\le k,\qquad U,\qquad m\ge1,
 \qquad V_rx_r=\lambda_rx_r,\qquad |\lambda_r|=1,\qquad N=3.
\]

The same correction applies to every other plain-parenthesis TeX expression
in the prose of this round.  In particular, plain text produced from
\(\Phi\), \(\overline\Phi\), \(\overline S_{\min}\), and their arguments
denotes those mathematical symbols with the displayed backslashes restored.
Equations (100)--(103), the proof, and the exact-arithmetic output are
unchanged.

## Round 2026-08-21: the Segre dual, off-diagonal coherences, and Weyl modes

Lemma 23 tested the localization map on positive rank-one inputs, through a
single Gram matrix.  The Schatten dual in Lemma 10 has a larger natural
domain: the extreme points of the trace-norm ball are all rank-one
coherences \(|x\rangle\langle y|\), including \(x\ne y\).  Vectorization
turns this distinction into the difference between a full Segre variety and
its conjugate diagonal.  Mining the off-diagonal part gives a stronger
necessary input-dimension bound for every nontrivial finite model.

### Lemma 27 (Segre spectral dual of the trace-to-collision norm)

Let \(\mathcal L:M_d\to M_D\) be linear.  Use the Hilbert--Schmidt isometry

\[
 \operatorname {vec}:M_d\longrightarrow
       \mathbb C^d\otimes\overline{\mathbb C^d},
 \qquad
 \operatorname {vec}(|x\rangle\langle y|)=x\otimes\overline y,
\]

and let \(\widehat{\mathcal L}\) be the matrix of \(\mathcal L\) under
vectorization.  Put

\[
 M_{\mathcal L}=\widehat{\mathcal L}^{,*}
                 \widehat{\mathcal L}\ge0.                    \tag{104}
\]

Then

\[
 \begin{split}
 \|\mathcal L\|_{S_1\to S_2}^2
 &=\max_{\|x\|=\|y\|=1}
   \langle x\otimes\overline y,
       M_{\mathcal L}(x\otimes\overline y)\rangle,\\
 r_+(\mathcal L)^2
 &=\max_{\|x\|=1}
   \langle x\otimes\overline x,
       M_{\mathcal L}(x\otimes\overline x)\rangle,            \tag{105}
 \end{split}
\]

where \(r_+\) is the state-restricted radius from Lemma 17.  Define the two
cones

\[
 \begin{split}
 \mathfrak B_{\rm Seg}
 &=\{Y=Y^*: \langle x\otimes\overline y,
                    Y(x\otimes\overline y)\rangle\ge0
                    \text{ for all }x,y\},\\
 \mathfrak B_{\Delta}
 &=\{Y=Y^*: \langle x\otimes\overline x,
                    Y(x\otimes\overline x)\rangle\ge0
                    \text{ for all }x\}.
                                                                    \tag{106}
 \end{split}
\]

The corresponding exact conic duals are

\[
 \begin{split}
 \|\mathcal L\|_{S_1\to S_2}^2
 &=\min\{t:tI-M_{\mathcal L}\in\mathfrak B_{\rm Seg}\},\\
 r_+(\mathcal L)^2
 &=\min\{t:tI-M_{\mathcal L}\in\mathfrak B_{\Delta}\}.
                                                                    \tag{107}
 \end{split}
\]

Moreover,

\[
 \{Y:Y\ge0\}\subseteq\mathfrak B_{\rm Seg}
       \subseteq\mathfrak B_{\Delta},
\]

so the common PSD relaxation of either problem has value

\[
 \min\{t:tI-M_{\mathcal L}\ge0\}
 =\lambda_{\max}(M_{\mathcal L}),                              \tag{108}
\]

and

\[
 r_+(\mathcal L)\le\|\mathcal L\|_{S_1\to S_2}
 \le\sqrt{\lambda_{\max}(M_{\mathcal L})}.                    \tag{109}
\]

**Proof.**  If
\(X=\sum_js_j|x_j\rangle\langle y_j|\) is a singular-value
decomposition, then

\[
 \|\mathcal L(X)\|_2
 \le\sum_js_j\|\mathcal L(|x_j\rangle\langle y_j|)\|_2
 \le\|X\|_1\max_{x,y}
       \|\mathcal L(|x\rangle\langle y|)\|_2.
\]

Rank-one matrices themselves belong to the trace-norm unit sphere, so equality
holds after taking the supremum.  Vectorization and (104) give the first line
of (105).  The squared Hilbert--Schmidt norm of \(\mathcal L(\rho)\) is
convex in the state \(\rho\).  Decomposing a mixed state into pure states
therefore shows that its maximum occurs at a pure state, proving the second
line.

For unit vectors, \(tI-M_{\mathcal L}\) has nonnegative expectation on the
appropriate product variety exactly when \(t\) dominates the corresponding
maximum in (105).  Homogeneity removes the unit-vector restriction and proves
(107).  The cone inclusions are immediate from their definitions.  A
Hermitian matrix \(tI-M_{\mathcal L}\) is positive semidefinite exactly when
\(t\ge\lambda_{\max}(M_{\mathcal L})\), proving (108)--(109).
\(\square\)

Thus the positivity relaxation isolated after Proposition 22 has a precise
geometry.  The entropy problem tests only the conjugate diagonal
\(x\otimes\overline x\), the localization norm tests every product vector
\(x\otimes\overline y\), and the SDP tests every vector in
\(\mathbb C^d\otimes\overline{\mathbb C^d}\).

### Lemma 28 (exact cross-Gram representation)

Let \(W_1,\ldots,W_D\in U(d)\), let \(\mathcal C\) be their complementary
channel with uniform weights, and put \(\mathcal L=P_0\mathcal C\).  Define

\[
 \mathcal T_W(a)=\sum_{v,w=1}^D a_{vw}W_v^*W_w
\]

and, for unit vectors \(x,y\),

\[
 F_W(x,y)=\sum_{v,w=1}^D
       |\langle y,W_v^*W_wx\rangle|^2
       -D|\langle y,x\rangle|^2.                              \tag{110}
\]

Then

\[
 \begin{split}
 \left\|\mathcal T_W|_{M_D^0}\right\|_{S_2\to S_\infty}^2
 &=D^2\|\mathcal L\|_{S_1\to S_2}^2
 =\max_{\|x\|=\|y\|=1}F_W(x,y),\\
 D^2r_+(\mathcal L)^2
 &=\max_{\|x\|=1}F_W(x,x).                                  \tag{111}
 \end{split}
\]

**Proof.**  For fixed \(x,y\), form the cross-Gram matrix

\[
 B_{x,y}=(\langle y,W_v^*W_wx\rangle)_{v,w}.
\]

Its trace is \(D\langle y,x\rangle\), and Hilbert--Schmidt orthogonality of
the scalar and traceless subspaces gives

\[
 \|P_0B_{x,y}\|_2^2
 =\sum_{v,w}|\langle y,W_v^*W_wx\rangle|^2
       -D|\langle y,x\rangle|^2=F_W(x,y).                    \tag{112}
\]

For trace-zero \(a\),

\[
 \langle y,\mathcal T_W(a)x\rangle
 =\sum_{v,w}a_{vw}\langle y,W_v^*W_wx\rangle.
\]

Hilbert--Schmidt duality in the coefficient matrix, followed by the
two-vector characterization of operator norm, therefore identifies the
first and last terms in the first line of (111).  The middle equality is also
(31), and follows directly from

\[
 \mathcal L(|x\rangle\langle y|)_{vw}
 ={1\over D}\langle y,W_w^*W_vx\rangle
       -{\langle y,x\rangle\over D}\delta_{vw}.               \tag{113}
\]

Transposition of the two coefficient indices does not change the
Hilbert--Schmidt norm.  Restricting (113) to \(y=x\), and using the pure-state
reduction in Lemma 27, proves the second line of (111). \(\square\)

The cross-Gram formula makes the loss from positivity literal: Lemma 23 uses
the diagonal \(F_W(x,x)\), whereas (15) must also control every off-diagonal
\(F_W(x,y)\).

### Proposition 29 (universal off-diagonal dimension obstruction)

For every \(D\)-tuple of unitaries on \(\mathbb C^d\),

\[
 \left\|\mathcal T_W|_{M_D^0}\right\|_{S_2\to S_\infty}^2
 \ge {D(D-1)\over d},
 \qquad
 \|P_0\mathcal C\|_{S_1\to S_2}^2
 \ge {D-1\over dD}.                                          \tag{114}
\]

More explicitly, every fixed orthonormal basis of \(\mathbb C^d\) contains
a pair \(x,y\), not necessarily distinct, for which the first inequality is
witnessed through (110).

**Proof.**  Let \(e_1,\ldots,e_d\) be any orthonormal basis.  Since each
\(W_v^*W_w\) is unitary,

\[
 \sum_{i,j=1}^d|\langle e_j,W_v^*W_we_i\rangle|^2
 =\|W_v^*W_w\|_2^2=d.                                       \tag{115}
\]

Also \(\sum_{i,j}|\langle e_j,e_i\rangle|^2=d\).  Averaging (110) over
the \(d^2\) ordered basis pairs consequently gives the exact identity

\[
 {1\over d^2}\sum_{i,j=1}^dF_W(e_i,e_j)
 ={D^2d-Dd\over d^2}={D(D-1)\over d}.                        \tag{116}
\]

At least one pair is no smaller than the average.  Lemma 28 proves the first
inequality in (114), and division by \(D^2\) proves the second. \(\square\)

When \(d>1\) and \(D>1\), (114) strictly strengthens the rank obstruction
(87).  If \(d<D\), the difference between the new squared lower bound and
the one in (87) is \(D(d-1)/d>0\); if \(d\ge D\), (87) is zero while
(114) remains positive.  This improvement is possible precisely because a
trace-norm extreme point need not be positive.

### Corollary 30 (strengthened necessary dimension for finite localization)

For the product tuple in Lemma 7, put

\[
 D=N^k,\qquad d=\prod_{r=1}^kd_r,qquad a=1+{9\over N}.
\]

If (15) holds, then

\[
 d\ge {D(D-1)\over(K_{N,k}+\eta)^2}.                          \tag{117}
\]

With \(\eta=\theta\sqrt D\), this becomes

\[
 d\ge {D-1\over[\sqrt{a^k-1}+\theta]^2}.                     \tag{118}
\]

For all sufficiently small positive \(\theta\), integrality therefore gives

\[
 d\ge
 \left\lceil{N^k-1\over(1+9/N)^k-1}\right\rceil.            \tag{119}
\]

For \(N\ge4\), the zero-tolerance endpoint in (119) is strictly larger than
the endpoint \(D/a^k\) in (95).  In the single-block case it reads

\[
 d\ge\left\lceil{N(N-1)\over9}\right\rceil                  \tag{120}
\]

for all sufficiently small tolerance.

**Proof.**  Combine the first inequality in (114) with the upper bound (15)
and rearrange to get (117).  Since

\[
 K_{N,k}^2=D(a^k-1),
\]

substitution yields (118).  Its right side increases to
\((D-1)/(a^k-1)\) as \(\theta\downarrow0\).  Taking the ceiling is locally
constant from below at this endpoint, including when the endpoint is an
integer, which proves (119).  Put \(k=1\) to obtain (120).

To compare with (95), write \(A=a^k\).  Direct subtraction gives

\[
 {D-1\over A-1}-{D\over A}
 ={D-A\over A(A-1)}.                                         \tag{121}
\]

For \(N\ge4\), one has \(N>1+9/N\), hence \(D=N^k>A=a^k\), so
(121) is positive. \(\square\)

The stronger obstruction still has exactly the admissible exponential scale:
for fixed \(N\ge4\),

\[
 \lim_{k\to\infty}{1\over k}
 \log {N^k-1\over(1+9/N)^k-1}
 =\log{N^2\over N+9}.                                        \tag{122}
\]

Thus it raises the necessary finite dimension, dramatically so at small
\(k\), but it still does not contradict \(\log d=O(k)\).  At the optimized
one-bit parameters of Proposition 22, it raises the zero-tolerance lower
bound by about \(0.00282\) input qubits and reduces the output-to-input slack
from about \(9.00000\) to about \(8.99718\) qubits.

The off-diagonal sector can be diagonalized exactly for Weyl unitaries.  This
provides a finite Fourier model in which all three relaxations in Lemma 27 are
visible.

### Proposition 31 (twisted-difference Fourier spectrum of a Weyl tuple)

Let \(q\ge2\), let \(\omega=e^{2\pi i/q}\), and on \(\mathbb C^q\) define

\[
 Xe_j=e_{j+1\pmod q},\qquad Ze_j=\omega^je_j.
\]

Index \(D=q^2\) unitaries by \(g=(p,r)\in\mathbb Z_q^2\), and put
\(W_g=X^pZ^r\).  Then the coefficient map has a twisted-difference
decomposition

\[
 \mathcal T_W(a)=\sum_{t\in\mathbb Z_q^2}b_tW_t,
 \qquad
 b_t=\sum_{g\in\mathbb Z_q^2}\kappa(g,t)a_{g,g+t},            \tag{123}
\]

where every \(\kappa(g,t)\) has modulus one and \(b_0=\operatorname {Tr}a\).
On the trace-zero subspace,

\[
 \left\|\mathcal T_W|_{M_D^0}\right\|_{S_2\to S_\infty}^2=q^3.
                                                                    \tag{124}
\]

For the centered complementary channel \(\mathcal L=P_0\mathcal C\),

\[
 \|\mathcal L\|_{S_1\to S_2}^2={1\over q},
 \qquad
 r_+(\mathcal L)^2={q-1\over q^2}.                            \tag{125}
\]

Hence the squared positivity gap is

\[
 {\|\mathcal L\|_{S_1\to S_2}^2\over r_+(\mathcal L)^2}
 ={q\over q-1}.                                               \tag{126}
\]

Nevertheless the associated random-unitary channel is completely
depolarizing and has zero conjugate gap.

**Proof.**  The Weyl multiplication law gives
\(W_g^*W_h=\kappa(g,h-g)W_{h-g}\) for a phase \(\kappa\).  Grouping the
coefficient matrix by the difference \(t=h-g\) proves (123); at \(t=0\),
the phase is one and the coefficient is the trace.

The matrices \(W_t/\sqrt q\) are an orthonormal Hilbert--Schmidt basis of
\(M_q\).  Parseval therefore gives, for every pair of unit vectors,

\[
 \sum_{t\in\mathbb Z_q^2}|\langle y,W_tx\rangle|^2=q.         \tag{127}
\]

Every difference \(t\) occurs for exactly \(D=q^2\) ordered pairs \((g,h)\).
Equations (110) and (127) consequently reduce the entire cross-Gram spectrum
to

\[
 F_W(x,y)=q^3-q^2|\langle y,x\rangle|^2.                      \tag{128}
\]

Choosing \(y\perp x\) proves (124) through Lemma 28.  Setting \(y=x\)
in (128), and dividing the two maxima by \(D^2=q^4\), proves (125)--(126).

It remains to identify the channel.  Averaging \(Z^rAZ^{-r}\) over \(r\)
removes every off-diagonal matrix entry.  Averaging the resulting diagonal
matrix under all powers of \(X\) replaces every diagonal entry by
\(\operatorname {Tr}(A)/q\).  Hence

\[
 {1\over q^2}\sum_{p,r}W_{p,r}AW_{p,r}^*
 ={\operatorname {Tr}(A)\over q}I_q.                          \tag{129}
\]

The minimum output entropy is therefore \(\log q\), while the tensor product
with its conjugate has constant output \(I_{q^2}/q^2\) and minimum output
entropy \(2\log q\).  Its conjugate gap is zero. \(\square\)

Equation (123) is the promised Fourier change of representation: the
\(D^2\)-dimensional coefficient matrix collapses to \(D\) twisted difference
modes.  Yet (128) shows that the largest localization witness is a pure
off-diagonal coherence \(x\perp y\), not a state.  Thus even a channel whose
positive outputs have a completely flat, exactly additive spectrum can have
a substantially larger trace-to-collision localization norm.  Any attempt to
improve the entropy rate by replacing (32) with state-positive localization
must therefore discard these coherence modes before applying a dimension
estimate; their contribution cannot be inferred from output-state ranks.

The finite checks below used the \(q=3\) Weyl matrices and exact rational
arithmetic for the dimension comparisons.  Floating error appears only in
the numerical construction of the third roots of unity.  This is the verbatim
`python3` output:

```text
q = 3 D = 9
max_HS_Gram_error = 8.882e-16
cross_sum_perpendicular = 27.000000000000
centered_cross_perpendicular = 27.000000000000
predicted_full_norm_squared = 27
cross_sum_diagonal = 27.000000000000
centered_cross_diagonal = 18.000000000000
predicted_state_sector_squared = 18
full_channel_norm_squared = 1/3
state_radius_squared = 2/9
ratio = 3/2
average_lower_bound_squared = 24
actual_minus_average = 3
N=5 k=1 old=25/14 new=20/9 new_gt_old=True ceil_new=3
N=5 k=2 old=625/196 new=200/57 new_gt_old=True ceil_new=4
N=100 k=1 old=10000/109 new=1100 new_gt_old=True ceil_new=1100
N=178482139 k=1 old=31855873942015321/178482148 new=10618624587844394/3 new_gt_old=True ceil_new=3539541529281465
```

At the one-bit parameters, an 80-decimal evaluation of the two
zero-tolerance endpoints gave:

```text
N = 178482139 k = 123714448
old_zero_tolerance_rank_lower_bits = 3391162020.73920348238483799099040442074306137518387513466383056775797667394
new_offdiagonal_lower_bits = 3391162020.74202399383746876059319643911806463609800948901193052798076951854
new_minus_old_bits = 0.00282051145263076960279201837500326091413435434809996022279284459573444236245
output_minus_new_bits = 8.99718337713379342623795830174638472312654112634605925095231436469319505238
new_strictly_larger = True
```

### Dated correction 2026-08-21

In (104), the malformed adjoint factor
~~\(\widehat{\mathcal L}^{,*}\)~~ is a transcription error.  The definition
used throughout Lemma 27 is

\[
 M_{\mathcal L}=\widehat{\mathcal L}^{\,*}
                 \widehat{\mathcal L}\ge0.
\]

No later formula or assertion is changed.

### Corollary 32 (the Weyl SDP spectrum)

For the Weyl channel in Proposition 31, the vectorized collision operator is

\[
 M_{\mathcal L}={1\over q}P_{\{I_q\}^{\perp}},                \tag{130}
\]

where the projection is taken in Hilbert--Schmidt space.  Its spectrum is
zero with multiplicity one and \(1/q\) with multiplicity \(q^2-1\).  Hence

\[
 r_+(\mathcal L)^2={q-1\over q^2}
 <\|\mathcal L\|_{S_1\to S_2}^2
 =\lambda_{\max}(M_{\mathcal L})={1\over q}.                 \tag{131}
\]

Thus the Segre conic problem and its PSD relaxation coincide in this model;
the only strict step is restriction from all coherences to positive states.

**Proof.**  From the complementary-channel formula and the Weyl difference
law,

\[
 \begin{split}
 \|\mathcal C(X)\|_2^2
 &={1\over q^4}\sum_{g,h}
       |\operatorname {Tr}(W_h^*W_gX)|^2\\
 &={1\over q^2}\sum_t|\operatorname {Tr}(W_tX)|^2
 ={1\over q}\|X\|_2^2,                                     \tag{132}
 \end{split}
\]

where the last equality is Parseval.  The scalar component of
\(\mathcal C(X)\) has squared norm
\(|\operatorname {Tr}X|^2/q^2\).  Orthogonal subtraction therefore gives

\[
 \|\mathcal L(X)\|_2^2
 ={1\over q}\|X\|_2^2-{1\over q^2}|\operatorname {Tr}X|^2
 ={1\over q}\|P_{\{I_q\}^{\perp}}X\|_2^2.                  \tag{133}
\]

Equation (130) and its asserted multiplicities follow.  Combining its largest
eigenvalue with (125) proves (131). \(\square\)

The \(q=3\) vectorized superoperator gives the following numerical spectrum;
the output is verbatim from `python3`:

```text
q = 3
M_L_eigenvalues = [0.0, 0.333333333333, 0.333333333333, 0.333333333333, 0.333333333333, 0.333333333333, 0.333333333333, 0.333333333333, 0.333333333333]
predicted_zero_multiplicity = 1
predicted_1/q_multiplicity = 8
lambda_max = 0.333333333333
full_trace_to_collision_norm_squared = 0.333333333333
state_radius_squared = 0.222222222222
```

## Round 2026-08-21: adversarial pure states and the frame-potential barrier

Proposition 29 obtained its dimension obstruction by averaging over all
rank-one coherences \(|x\rangle\langle y|\).  It was therefore still possible
that discarding the off-diagonal coherences would remove the obstruction at
the exponential scale relevant to (24).  This round tests that possibility
directly.  Haar averaging only the positive pure states gives, up to one
dimension, the same necessary bound as Corollary 30.  A second adversarial
input, constructed block by block from eigenvectors of relative unitaries,
gives a dimension-independent obstruction.  Neither obstruction contradicts
Lemma 7, for the precise quantitative reasons recorded below.

### Lemma 33 (positive-state frame-potential obstruction)

For a \(D\)-tuple of unitaries \(W_1,\ldots,W_D\in U(d)\), let \(F_W\) be
as in (110), and put

\[
 \mathsf P_W=\sum_{v,w=1}^D
       \left|\operatorname {Tr}(W_v^*W_w)\right|^2.           \tag{134}
\]

With normalized Haar measure on the unit sphere of \(\mathbb C^d\),

\[
 \int F_W(x,x)\,dx
 ={D^2d+\mathsf P_W-Dd(d+1)\over d(d+1)}.                    \tag{135}
\]

Consequently,

\[
 \max_{\|x\|=1}F_W(x,x)\ge
 \begin{cases}
 \displaystyle {D(D-1)\over d+1},&D\le d^2,\\[6pt]
 \displaystyle {D(D-d)\over d},&D\ge d^2.
 \end{cases}                                                  \tag{136}
\]

At \(D=d^2\) the two expressions agree.  Equivalently, for the centered
complementary channel \(\mathcal L=P_0\mathcal C\),

\[
 r_+(\mathcal L)^2\ge
 \begin{cases}
 \displaystyle {D-1\over D(d+1)},&D\le d^2,\\[6pt]
 \displaystyle {D-d\over dD},&D\ge d^2.
 \end{cases}                                                  \tag{137}
\]

**Proof.**  If \(g\) is a standard complex Gaussian vector and
\(g=rx\), then \(x\) is Haar distributed on the unit sphere and is
independent of \(r\).  Expanding in coordinates and using independence gives

\[
 \mathbb E|g^*Ag|^2=\operatorname {Tr}(AA^*)
                       +|\operatorname {Tr}A|^2,
 \qquad \mathbb E r^4=d(d+1).                                \tag{138}
\]

Indeed, the only nonzero fourth moments are summarized by
\(\mathbb E(\overline g_i g_j g_k\overline g_l)
=\delta_{ij}\delta_{kl}+\delta_{il}\delta_{jk}\); this follows directly
from the second and fourth moments of one standard complex Gaussian and
independence of distinct coordinates.  Dividing the two identities in (138)
therefore proves

\[
 \int|\langle x,Ax\rangle|^2\,dx
 ={\operatorname {Tr}(AA^*)+|\operatorname {Tr}A|^2
    \over d(d+1)}.                                            \tag{139}
\]

Apply (139) to the \(D^2\) unitaries \(A=W_v^*W_w\), and subtract the
last term \(D\) in (110).  This gives (135).

For the lower bound on \(\mathsf P_W\), regard
\(z_v=\operatorname {vec}(W_v)/\sqrt d\) as \(D\) unit vectors in a
space of dimension \(d^2\), and let \(G=(\langle z_v,z_w\rangle)\) be
their Gram matrix.  Since \(G\ge0\), \(\operatorname {Tr}G=D\), and
\(\operatorname {rank}G\le\min\{D,d^2\}\), Cauchy--Schwarz on its
nonzero eigenvalues yields

\[
 {\mathsf P_W\over d^2}=\operatorname {Tr}G^2
 \ge {D^2\over\min\{D,d^2\}}.
                                                                    \tag{140}
\]

Thus \(\mathsf P_W\ge Dd^2\) when \(D\le d^2\), and
\(\mathsf P_W\ge D^2\) when \(D\ge d^2\).  Substitution in (135),
followed by "maximum at least average," gives (136).  The second line of
(111) says that its left side is \(D^2r_+(\mathcal L)^2\); division by
\(D^2\) proves (137). \(\square\)

The second branch of (137) is the purity/rank obstruction already underlying
Lemma 23.  The first branch is new: when the input space is larger than
\(\sqrt D\), averaging positive states is stronger than selecting one
low-rank Gram state.

### Corollary 34 (positive states come within one dimension of Corollary 30)

Use the notation

\[
 D=N^k,\qquad a=1+{9\over N},\qquad A=a^k,
 \qquad q_\theta=\sqrt{A-1}+\theta.                            \tag{141}
\]

Suppose the product tuple satisfies (15) with
\(\eta=\theta\sqrt D\).  If \(N\ge7\), then for every sufficiently small
positive \(\theta\), its total input dimension \(d\) necessarily obeys

\[
 d\ge
 \left\lceil {D-A\over A-1}\right\rceil
 =\left\lceil {D-1\over A-1}\right\rceil-1.                 \tag{142}
\]

This uses only positive pure inputs.  Its real zero-tolerance endpoint is
strictly larger than the rank endpoint \(D/A\), because

\[
 {D-A\over A-1}-{D\over A}
 ={D-A^2\over A(A-1)}>0.                                     \tag{143}
\]

It is exactly one below the off-diagonal endpoint in (119).  Nevertheless,

\[
 \lim_{k\to\infty}{1\over k}
 \log {N^k-(1+9/N)^k\over(1+9/N)^k-1}
 =\log {N^2\over N+9}.                                      \tag{144}
\]

Thus positive states alone reproduce the off-diagonal dimension obstruction
at exponential scale, but still require only linearly many input qubits.

**Proof.**  Equations (15), (111), and (141) give

\[
 \max_xF_W(x,x)\le (K_{N,k}+\eta)^2=Dq_\theta^2.
\]

The rank bound (93) first gives \(d\ge D/(1+q_\theta^2)\).  For \(N\ge7\),

\[
 N>(1+9/N)^2.
\]

To verify this last inequality without approximation, at \(N=7\) it is
\(343>256\) after multiplying by \(N^2\), and the derivative of
\(x^3-(x+9)^2\) is positive for \(x\ge7\).  Hence \(D>A^2\), so
\(D/A>\sqrt D\).  For all sufficiently small \(\theta>0\), the rank
bound forces \(d>\sqrt D\).  The first branch of (136) then applies and
gives

\[
 d\ge {D-1\over q_\theta^2}-1.                               \tag{145}
\]

As \(\theta\downarrow0\), the right side increases to

\[
 {D-1\over A-1}-1={D-A\over A-1}.
\]

Integrality gives (142), including when the endpoint is an integer.  Equations
(143)--(144) follow by direct algebra; in (144), divide numerator and
denominator by \(A\) and use \(D/A=(N^2/(N+9))^k\). \(\square\)

The frame-potential estimate is attained by a finite family, so its constants
cannot be increased universally.  Take the \(n^2\) Weyl unitaries on
\(\mathbb C^n\) and repeat every unitary \(s\) times.  Then
\(d=n\), \(D=sn^2\), and (128) gives, for every unit vector \(x\),

\[
 F_W(x,x)=s^2n^3-sn^2={D(D-d)\over d}.                        \tag{146}
\]

For \(s=1\), this is also equality in the first branch at \(D=d^2\).
Thus any stronger positive-state dimension obstruction must use hypotheses
beyond the mere number and dimension of the unitaries.  In the present
problem the unused hypothesis is their tensor-product organization together
with the unusually small upper bound (15).

The following is verbatim `python3` output for the \(n=3\) Weyl family and
its twice-repeated version.  The sampled values are constant as asserted by
(146); the displayed errors come only from floating evaluation of third
roots of unity.

```text
q=3 repeats=1 d=3 D=9 branch=D<=d^2
 frame_potential=81.000000000000 welch_value=81.000000000000
 sampled_diagonal_F = [18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0, 18.0]
 predicted_constant_F=18 lower_bound=18.000000000000
 max_abs_error=2.842e-14
q=3 repeats=2 d=3 D=18 branch=D>=d^2
 frame_potential=324.000000000000 welch_value=324.000000000000
 sampled_diagonal_F = [90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 90.0, 90.0]
 predicted_constant_F=90 lower_bound=90.000000000000
 max_abs_error=1.990e-13
```

### Proposition 35 (blockwise eigenvector collision obstruction)

Let \(N\ge2\), and for \(1\le r\le k\) let
\(U^{(r)}=(U^{(r)}_1,\ldots,U^{(r)}_N)\) be any unitary tuple.  Put

\[
 \Phi=\bigotimes_{r=1}^k\mathcal R_{U^{(r)}},\qquad D=N^k.
\]

There is a product pure input \(\rho\) such that

\[
 \operatorname {Tr}\Phi(\rho)^2
 =\operatorname {Tr}\mathcal C^{[k]}(\rho)^2
 \ge\left({N+2\over N^2}\right)^k.                           \tag{147}
\]

Consequently every such product tuple satisfies the dimension-independent
lower bounds

\[
 \begin{split}
 \max_xF_W(x,x)&\ge (N+2)^k-N^k,\\
 \left\|\mathcal T_W|_{M_D^0}\right\|_{2\to\infty}^2
     &\ge (N+2)^k-N^k,                                      \tag{148}\\
 S_{\min}(\Phi)&\le
 k\left(\log N-{2\log2\over N}\right).
 \end{split}
\]

**Proof.**  For each block choose a unit eigenvector \(x_r\) of
\((U^{(r)}_1)^*U^{(r)}_2\).  As in (102), the two output vectors
\(U^{(r)}_1x_r\) and \(U^{(r)}_2x_r\) determine the same pure state.  If
\(\sigma_r=\mathcal R_{U^{(r)}}(|x_r\rangle\langle x_r|)\), then the
ensemble formula for purity gives

\[
 \operatorname {Tr}\sigma_r^2
 ={1\over N^2}\sum_{i,j=1}^N
   |\langle U^{(r)}_ix_r,U^{(r)}_jx_r\rangle|^2
 \ge {N+2\over N^2}.                                       \tag{149}
\]

Here the \(N\) diagonal terms and the two ordered cross terms \((1,2)\) and
\((2,1)\) are all one.  On the product of the \(x_r\), purity multiplies,
which proves the first expression in (147).  The complementary output has the
same nonzero spectrum on a pure input, proving the second expression.

For the chosen input, subtracting its scalar collision contribution gives

\[
 D^2\left(\operatorname {Tr}\mathcal C^{[k]}(\rho)^2-{1\over D}\right)
 \ge (N+2)^k-N^k.
\]

Equations (111) and (109) prove (148).  For the entropy assertion, group the
two identical ensemble states in each block.  The resulting classical weights
are \(2/N\) once and \(1/N\) another \(N-2\) times, whose entropy is
\(\log N-2\log2/N\).  Entropy of a pure-state mixture is no greater than the
entropy of its weights, as proved in Lemma 5.  The selected output is a tensor
product over the blocks, so its entropy is at most the asserted multiple.
\(\square\)

Proposition 35 recovers the exact collapse at \(N=2\): the lower bound in
(147) is one.  More generally, it rules out any uniform product collision
cap of the form

\[
 \operatorname {Tr}\mathcal C^{[k]}(\rho)^2
 \le\left({N+c\over N^2}\right)^k
 \quad\hbox{for every state and every product tuple}          \tag{150}
\]

when \(c<2\).  This is an obstruction before any entropy conversion or
finite-dimensional approximation.

It does not contradict the localized free bound.  At zero tolerance, (38)
has collision cap

\[
 \left({N+9\over N^2}\right)^k,                              \tag{151}
\]

and (147) fits strictly below it because \(2<9\).  The associated entropy
bounds are compatible as well:

\[
 \log(1+9/N)>{2\log2\over N}.                                \tag{152}
\]

Indeed, Bernoulli's inequality gives
\((1+9/N)^N\ge1+9=10>4\), which proves (152).  Thus the eigenvector attack
would refute a collision constant below \(2\), but the established
Collins--Youn constant is \(9\).  The interval from \(2\) to \(9\) is the
exact slack left by this attempted counterexample.

The rational calculations below are verbatim `python3` output.  They compare
the old rank endpoint, the positive-state endpoint (142), and the
off-diagonal endpoint (119), and check the collision witness in several
small cases.

```text
N=7 k=1 D=7 A=16/7
 old_endpoint = 49/16 ceil = 4
 positive_state_endpoint = 11/3 ceil = 4
 offdiagonal_endpoint = 14/3 ceil = 5
 off_minus_state = 1
N=100 k=1 D=100 A=109/100
 old_endpoint = 10000/109 ceil = 92
 positive_state_endpoint = 1099 ceil = 1099
 offdiagonal_endpoint = 1100 ceil = 1100
 off_minus_state = 1
N=100 k=2 D=10000 A=11881/10000
 old_endpoint = 100000000/11881 ceil = 8417
 positive_state_endpoint = 1009981/19 ceil = 53157
 offdiagonal_endpoint = 1010000/19 ceil = 53158
 off_minus_state = 1
N=2 k=1 unavoidable_purity=1 localized_cap=11/4 compatible=True centered_witness=2
N=3 k=1 unavoidable_purity=5/9 localized_cap=4/3 compatible=True centered_witness=2
N=3 k=2 unavoidable_purity=25/81 localized_cap=16/9 compatible=True centered_witness=16
N=10 k=3 unavoidable_purity=27/15625 localized_cap=6859/1000000 compatible=True centered_witness=728
qutrit_two_block_purity = 25/81
qutrit_two_block_centered_F = 16
```

The attempted disproof is blocked at two exact scales.  First, positive pure
states force nearly the same dimension as arbitrary coherences, but (144)
is still only exponential in \(k\), precisely the size allowed by (24).  A
dimension counterexample would need a lower bound whose logarithm divided by
\(k\) is unbounded; neither the frame potential nor output rank can supply
one.  Second, tensor-product structure supplies the universal collision
witness (147), but its forced constant is \(2\), while the proved upper
envelope has constant \(9\).  Closing that numerical interval would require
a new simultaneous statement about many relative unitaries, not merely one
eigenvector per block.  No such statement is proved here **[UNPROVED]**.

## Round 2026-08-21: quantitative localization from tensor-Haar strong approximation

The sole load-bearing dimension loss in Lemma 7 can be separated from the
constant (9).  A quantitative strong-approximation theorem for Haar matrices
acting on disjoint tensor factors supplies an explicit, though still
superlinear, input-qubit bound.  This round gives the exact reduction and
closes the qualitative dimension gap up to a factor (O(k\log k)) in the
number of input qubits.

The external result used here is the tensor-model theorem of
Chen--Garza-Vargas--van Handel, Theorem 9.7, together with the Haar-unitary
extension explicitly stated immediately after its proof.  Their Theorem 1.5
and the proof in Section 7.6 give the Haar logarithmic correction and the
dependence of the constant on the degree and number of variables.  The source
actually opened was [Chen--Garza-Vargas--van Handel, *A new approach to strong
convergence II. The classical ensembles*, arXiv:2412.00593v3, Theorems 1.5
and 9.7 and Section 7.6](https://arxiv.org/html/2412.00593v3).

In the notation needed below, their result has the following consequence.
Let (q\times q) independent Haar unitaries

\[
 U_i^{(r,q)},\qquad i\in[N],\quad r\in[k],
\]

act on the (r)-th factor of ((\mathbb C^q)^{\otimes k}), and let the
limiting variables be (k) commuting tensor copies of (N) free Haar
unitaries.  If (P) has degree at most (2k), then, for fixed
(0<\varepsilon\le1/2) and all sufficiently large (q),

\[
 \mathbb P\{\|P(U^{(\cdot,q)})\|>
        (1+\varepsilon)\|P(u^{(\cdot)})\|\}
 \le {q^k\over c_{N,k}\varepsilon}
 \exp\!\left[-{c_{N,k}q\varepsilon^2
                    \over\log^2(q\varepsilon^2)}\right],       \tag{153}
\]

where tracking the displayed constants in their proofs gives

\[
 \log c_{N,k}^{-1}=O_N(k\log(k+1)).                            \tag{154}
\]

For precision about (154), Theorem 9.7 displays
(c^{-1}=(CLr)^{2q_0}q_0^2) in the Gaussian tensor model.  In the Haar proof,
Section 7.6 replaces this by a constant bounded by
((CLr)^{6q_0}[q_0(1+\log q_0)]^2), and introduces the denominator
(\log^2(q\varepsilon^2)) in (153).  Substitution of
(L=k), (r=N), and (q_0=2k) proves (154).  Enlarging the universal
constant absorbs the finitely many threshold conditions on (q).  Thus
(153), rather than an unnamed uniform-convergence hypothesis, is the precise
external theorem to which the quantitative part below is reduced.

### Lemma 36 (multiplicative finite localization with a dimension bound)

Fix (N\ge4) and (0<\varepsilon\le1/2).  For every (k\ge1), there is an
integer

\[
 q_k\le \exp\!igl(C_{N,\varepsilon}k\log(k+1)\bigr)          \tag{155}
\]

and (N)-tuples of unitaries
(U^{(r)}\in U(q_k)^N), (1\le r\le k), such that, with

\[
 W_v=U_{v_1}^{(1)}\otimes\cdots\otimes U_{v_k}^{(k)},
 \qquad D=N^k,
\]

every trace-zero (a\in M_D) satisfies

\[
 \left\|\sum_{v,w}a_{vw}W_v^*W_w\right\|
 \le(1+2\varepsilon)K_{N,k}\|a\|_2.                           \tag{156}
\]

Consequently the total input dimension (d_k=q_k^k) obeys

\[
 \log d_k=O_{N,\varepsilon}(k^2\log(k+1)).                    \tag{157}
\]

**Proof.**  Let

\[
 H_D=\{a\in M_D:\operatorname {Tr}a=0\},\qquad
 \mathbb S_D=\{a\in H_D:\|a\|_2=1\}.
\]

This is a real unit sphere in dimension (2(D^2-1)).  Put

\[
 \delta={\varepsilon K_{N,k}\over D}.
\]

Since (N\ge4), one has (0<\delta<1).  The standard volumetric argument
gives a finite (delta)-net (mathcal M\subset\mathbb S_D) with

\[
 |\mathcal M|\le(1+2/\delta)^{2(D^2-1)}.                       \tag{158}
\]

For (b\in\mathcal M), apply (153) to the scalar-coefficient polynomial

\[
 P_b(X)=\sum_{v,w}b_{vw}
 \bigotimes_{r=1}^k X_{v_r}^{(r)*}X_{w_r}^{(r)}.              \tag{159}
\]

Its degree is at most (2k), and Theorem 3.3 of Collins--Youn, recorded as
(11), gives (|P_b(u)|\le K_{N,k}).  A union bound therefore shows that
there is a simultaneous good realization whenever

\[
 (1+2/\delta)^{2(D^2-1)}
 {q^k\over c_{N,k}\varepsilon}
 \exp\!\left[-{c_{N,k}q\varepsilon^2
                    \over\log^2(q\varepsilon^2)}\right]<1.    \tag{160}
\]

Such a (q) may be chosen as in (155).  Indeed,

\[
 \log|\mathcal M|=O_{N,\varepsilon}(kN^{2k}),
\]

because
(K_{N,k}/D=D^{-1/2}\sqrt{(1+9/N)^k-1}).  On the other hand, (154) implies
that for
(q=\lceil\exp(C_{N,\varepsilon}k\log(k+1))\rceil), with the constant
chosen sufficiently large, the negative exponent in (160) dominates
(log|\mathcal M|+k\log q+\log(c_{N,k}^{-1}\varepsilon^{-1})).
This proves both (160) and (155).

Fix a realization for which every (b\in\mathcal M) is good.  If
(a\in\mathbb S_D), choose (b\in\mathcal M) with
(|a-b|_2\le\delta).  The finite evaluation map is (D)-Lipschitz by
the same Cauchy--Schwarz estimate as (16).  Hence

\[
 \begin{split}
 \|P_a(U)\|
 &\le\|P_b(U)\|+D\|a-b\|_2\\
 &\le(1+\varepsilon)K_{N,k}+D\delta
 =(1+2\varepsilon)K_{N,k}.
 \end{split}
\]

Homogeneity proves (156).  Finally,
(log d_k=k\log q_k), so (155) gives (157). \(\square\)

### Proposition 37 (same entropy-gap rate with explicit input size)

For every fixed (N\ge4), (0<\varepsilon\le1/2), and (k\ge1), there
are finite-dimensional conjugate channels with input dimension satisfying
(157), complementary output dimension (N^k), and

\[
 \Delta(\Phi_k,\overline\Phi_k)
 \ge {k\log N\over N}
 -2\log\!\left(1+(1+2\varepsilon)^2
       \left[(1+9/N)^k-1\right]\right).                       \tag{161}
\]

In particular,

\[
 \liminf_{k\to\infty}{1\over k}
 \Delta(\Phi_k,\overline\Phi_k)\ge c_N.                      \tag{162}
\]

**Proof.**  Lemma 10 turns (156) into

\[
 \|P_0\mathcal C^{[k]}(X)\|_2
 \le{(1+2\varepsilon)K_{N,k}\over D}\|X\|_1.
\]

The orthogonal purity calculation (38) consequently gives, for every state
(ho),

\[
 \operatorname {Tr}\mathcal C^{[k]}(\rho)^2
 \le {1\over D}\left(1+(1+2\varepsilon)^2
                   [(1+9/N)^k-1]\right).                     \tag{163}
\]

Applying (S\ge-\log\operatorname {Tr}\rho^2) to both conjugate channels
and subtracting the Bell upper bound (23) proves (161).  For fixed
(arepsilon),

\[
 {1\over k}\log\left(1+(1+2\varepsilon)^2
                   [(1+9/N)^k-1]\right)
 \longrightarrow\log(1+9/N).
\]

This proves (162).  Passing to complementary channels preserves the gap and
makes the output dimension (N^k), while their input dimension is
(q_k^k). \(\square\)

Thus the finite-dimensional construction can now be taken with
(O_N(k^2\log k)) input qubits and (O_N(k)) output qubits, rather than with
no quantitative input bound.  The exact qubit-linear target (24) is reduced
to removing the growth of the local matrix size (q_k): a fixed
(q=q(N,\varepsilon)) version of (156), or any direct tensor-length estimate
with (sup_k q_k<\infty), would give (log d_k=O(k)).  The named external
theorem used above takes the opposite limit (q\to\infty) for each fixed
tensor length; its tail estimate forces the choice (155) after the uniform
net in (158).  It therefore proves (157), but does not by itself prove (24).

The finite arithmetic in the net radius and the collision cap was checked at
(N=5), (k=3), and (arepsilon=1/4).  All fractions below were computed
with `fractions.Fraction`; only the square root and logarithm are decimal
renderings.  The output is verbatim from `python3`:

```text
N = 5 k = 3 epsilon = 1/4
D = 125 real_trace_zero_dimension = 31248
A = 2744/125 K_squared = 2619
delta_squared = 2619/250000
delta_decimal = 0.1023523326553918848202768712281266598571
log_net_cardinality_upper = 94443.67560526172848107691362440199786296
multiplicative_radius_factor_squared = 9/4
purity_cap = 24071/62500 = 0.385136
D_times_purity_cap = 24071/500
identity_check = True
```

This calculation verifies only the finite algebra in (158) and (163); the
existence assertion is the probabilistic consequence of (153) and (160).

### Dated formatting correction 2026-08-21

In the immediately preceding round, several inline TeX delimiters were lost
during transcription.  Thus plain-parenthesis strings such as
~~(9)~~, ~~(O(k\log k))~~, ~~(q\times q)~~, ~~(r)~~, ~~(P)~~,
~~(2k)~~, ~~(c^{-1}=(CLr)^{2q_0}q_0^2)~~, ~~(N\ge4)~~,
~~(b\in\mathcal M)~~, ~~(\|a-b\|_2\le\delta)~~, and
~~(\log d_k=O(k))~~ are to be read, respectively, as

\[
 9,\quad O(k\log k),\quad q\times q,\quad r,\quad P,\quad 2k,
 \quad c^{-1}=(CLr)^{2q_0}q_0^2,\quad N\ge4,\quad
 b\in\mathcal M,\quad \|a-b\|_2\le\delta,\quad
 \log d_k=O(k).
\]

The same delimiter restoration applies to every other plain-parenthesis TeX
expression in that round.  In addition, the corrupted inline state symbol and
the two corrupted inline tolerance symbols mean \(\rho\) and
\(\varepsilon\), respectively.

The malformed equation (155), whose big-delimiter command acquired a control
character, is struck and replaced by

\[
 \text{~~malformed equation (155)~~},\qquad
 q_k\le \exp\!\bigl(C_{N,\varepsilon}k\log(k+1)\bigr).        \tag{164}
\]

Equation (164) is the bound used in the proof of Lemma 36.  All other
displayed equations (153)--(163), the probabilistic reduction, and the
finite-arithmetic output are unchanged.

## Round 2026-08-21: exact qubit minimax at the three-unitary boundary

Proposition 26 leaves (N=3) as the first alphabet not annihilated by the
two-unitary eigenvector mechanism.  Proposition 35 gives a universal
single-block entropy upper bound at this alphabet, but does not say whether
the bound is sharp.  Exhaustive computation over the qubit Clifford group
suggests that it is sharp and that all equality cases are orthogonal Pauli
triples.  The Bloch-sphere argument below proves both observations and then
computes the two-copy entropy exactly.

Write

\[
 h_2(p)=-p\log p-(1-p)\log(1-p).
\]

### Proposition 38 (sharp three-unitary qubit minimax)

Let (U_1,U_2,U_3\in U(2)), and define

\[
 \Phi(A)={1\over3}\sum_{i=1}^3U_iAU_i^*.
\]

Then

\[
 S_{\min}(\Phi)\le h_2(2/3)
 =\log3-{2\log2\over3}.                                      \tag{165}
\]

The bound is sharp.  Moreover, equality holds in (165) if and only if,
after multiplying every (U_i) on the left and right by fixed unitaries,
multiplying the individual (U_i)'s by phases, and relabeling them, the
tuple is

\[
 (I_2,X,Y),                                                    \tag{166}
\]

where (X,Y) are two Pauli matrices with orthogonal rotation axes.

**Proof.**  Write a qubit state as

\[
 \rho_r={I_2+r\mathbin\cdot\sigma\over2},\qquad |r|\le1.
\]

Conjugation by (U_i) induces a rotation (R_i\in SO(3)).  Thus the Bloch
matrix of (Phi) is

\[
 M={R_1+R_2+R_3\over3}.                                      \tag{167}
\]

For a pure input, the output eigenvalues are
((1\pm|Mr|)/2).  Consequently

\[
 S_{\min}(\Phi)
 =h_2\!\left({1+\|M\|_{\rm op}\over2}\right).              \tag{168}
\]

Put (S=R_1+R_2+R_3).  Every rotation in (SO(3)) has trace at least
(-1), so

\[
 \begin{split}
 \|S\|_{\rm F}^2
 &=9+2\sum_{1\le i<j\le3}\operatorname {Tr}(R_i^TR_j)\ge3,\\
 \|S\|_{\rm op}^2&\ge {1\over3}\|S\|_{\rm F}^2\ge1.
 \end{split}                                                   \tag{169}
\]

Hence (|M|_{\rm op}\ge1/3).  Since (h_2((1+s)/2)) decreases for
(0\le s\le1), equations (168)--(169) prove (165).

It remains to classify equality.  If (|M|_{\rm op}=1/3), then both
inequalities in (169) are equalities.  In particular,

\[
 \operatorname {Tr}(R_i^TR_j)=-1\qquad(i\ne j).               \tag{170}
\]

Common left and right rotations let us take (R_1=I_3).  The other two
rotations are then half-turns.  If their unit axes are (a,b), their
matrices are (2aa^T-I_3) and (2bb^T-I_3), and

\[
 \operatorname {Tr}(R_2^TR_3)=4|a\mathbin\cdot b|^2-1.       \tag{171}
\]

Equation (170) therefore says (a\perp b).  A simultaneous rotation of
the axes makes them the (x)- and (y)-axes.  Lifting back from (SO(3))
to qubit unitaries gives (166), up to the harmless phases.  Conversely, for
two orthogonal half-turn axes,

\[
 I_3+(2aa^T-I_3)+(2bb^T-I_3)=2aa^T+2bb^T-I_3
\]

is an orthogonal reflection.  Its three singular values are one, so
(|M|_{\rm op}=1/3), and equality holds in (165). (square)

Thus the (k=1,N=3) entropy bound in Proposition 35 is optimal already on
qubits, and Proposition 38 identifies every qubit optimizer.  The optimizer
does not, however, produce an additivity gap.

### Corollary 39 (the extremal triple has zero conjugate gap)

If a uniform three-unitary qubit channel attains equality in (165), then

\[
 S_{\min}(\Phi\otimes\overline\Phi)
 =2S_{\min}(\Phi)=2h_2(2/3),
 \qquad \Delta(\Phi,\overline\Phi)=0.                         \tag{172}
\]

**Proof.**  The equivalences in Proposition 38 are unitary pre- and
post-compositions and do not change any of the minimum output entropies in
(172).  It is therefore enough to use

\[
 \Phi_0(A)={A+XAX+YAY\over3}.
\]

Direct evaluation on the Pauli basis gives

\[
 \Phi_0(A)={\operatorname {Tr}(A)I_2+XA^TX\over3}.           \tag{173}
\]

An output conjugation by (X) makes this channel unitarily equivalent to

\[
 \Psi(A)={\operatorname {Tr}(A)I_2+A^T\over3}.               \tag{174}
\]

The covariance identity

\[
 \Psi(VAV^*)=\overline V\Psi(A)\overline V^{,*}             \tag{175}
\]

shows that the output spectrum of (Psi\otimes\Psi) on a bipartite pure
input depends only on its Schmidt coefficients.  We may therefore use

\[
 |\psi_t\rangle=\sqrt t\,|00\rangle+\sqrt{1-t}\,|11\rangle,
 \qquad0\le t\le1.
\]

Expanding the four terms in
((\operatorname {Tr}(\cdot)I+T)^{\otimes2}/9) gives

\[
 (\Psi\otimes\Psi)(|\psi_t\rangle\langle\psi_t|)
 ={1\over9}
 \begin{pmatrix}
 1+3t&0&0&\sqrt{t(1-t)}\\
 0&2&0&0\\
 0&0&2&0\\
 \sqrt{t(1-t)}&0&0&4-3t
 \end{pmatrix}.                                               \tag{176}
\]

Its spectrum is

\[
 {2\over9},\quad {2\over9},\quad
 {5+d_t\over18},\quad {5-d_t\over18},
 \qquad
 d_t=\sqrt{1+32(t-1/2)^2}.                                   \tag{177}
\]

Here (1\le d_t\le3).  The last two eigenvalues have fixed sum (5/9),
and their entropy contribution is strictly decreasing in (d_t), since its
derivative is

\[
 -{1\over18}\log{5+d_t\over5-d_t}<0.                         \tag{178}
\]

Thus the entropy in (177) is minimized at (t=0) or (t=1).  At either
endpoint the spectrum is

\[
 \left({4\over9},{2\over9},{2\over9},{1\over9}\right)
 =\left({2\over3},{1\over3}\right)^{\otimes2}.              \tag{179}
\]

It follows that (S_{\min}(\Psi\otimes\Psi)=2h_2(2/3)).  Finally,
(overline{\Phi_0}=\Phi_0), because entrywise conjugation changes (Y)
to (-Y) and hence leaves its conjugation channel unchanged.  Transporting
the conclusion back through the unitary equivalences proves (172).
(square)

The initial finite search enumerated all (24) orientation-preserving signed
permutation matrices, normalized the first rotation to the identity, and
tested all (24^2=576) ordered Clifford triples.  The following is verbatim
`python3` output.  The displayed squared norms are floating renderings of
eigenvalues of integer matrices; the proof of their minimum is (169).

```text
rotations = 24 normalized_ordered_triples = 576
minimum ||I+A+B||_op^2 = 1.0
minimum average Bloch singular value = 0.3333333333333333
number attaining minimum = 24
squared_norm_distribution =
  1.0 : 24
  4.0 : 96
  5.828427124746 : 144
  6.561552812809 : 72
  7.464101615138 : 144
  9.0 : 96
representative_A = [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]
representative_B = [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]
pair_relative_traces = [-1, -1, -1]
S^T_S = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

An exact `sympy` calculation of (176), followed by an exhaustive
(10{,}001)-point grid check of its entropy, gave the following verbatim
output.  The grid is only a falsification check; equations (177)--(178) prove
the continuous minimum.

```text
trace = 1
characteristic_polynomial = -(9*lambda - 2)**2*(-81*lambda**2 + 45*lambda + 8*t**2 - 8*t - 4)/6561
variable_block_discriminant = 32*t**2 - 32*t + 9
t = 0 spectrum = ['4/9', '2/9', '2/9', '1/9'] entropy = 1.273028336589626
t = 1/4 spectrum = ['sqrt(3)/18 + 5/18', '2/9', '2/9', '5/18 - sqrt(3)/18'] entropy = 1.346074532643466
t = 1/2 spectrum = ['1/3', '2/9', '2/9', '2/9'] entropy = 1.368922360740219
t = 3/4 spectrum = ['sqrt(3)/18 + 5/18', '2/9', '2/9', '5/18 - sqrt(3)/18'] entropy = 1.346074532643466
t = 1 spectrum = ['4/9', '2/9', '2/9', '1/9'] entropy = 1.273028336589626
single_min_entropy = log(3)-2*log(2)/3 = 0.636514168294813
two_copy_endpoint_entropy = 1.273028336589626
grid_points = 10001
grid_min_entropy = 1.273028336589626 at_t = 0.0
grid_min_minus_2Smin = 0.000e+00
```

This settles the sharp local-entropy problem for three uniform unitaries on
a qubit and shows that its unique extremal geometry is exactly additive.
It does not prove that every three-unitary qubit channel is additive, nor
does it settle the (N=3) problem in higher input dimension; both extensions
remain **[UNPROVED]**.

### Dated formatting correction 2026-08-21

In the immediately preceding round, the inline TeX delimiters were stripped
during transcription.  Thus plain-parenthesis strings such as
~~(N=3)~~, ~~(U_1,U_2,U_3\in U(2))~~, ~~(R_i\in SO(3))~~,
~~((1\pm|Mr|)/2)~~, ~~(\|M\|_{\rm op}\ge1/3)~~,
~~(a\perp b)~~, ~~(\Psi\otimes\Psi)~~, ~~(1\le d_t\le3)~~,
and ~~(\overline{\Phi_0}=\Phi_0)~~ are to be read, respectively, as

\[
 N=3,\quad U_1,U_2,U_3\in U(2),\quad R_i\in SO(3),\quad
 {1\pm|Mr|\over2},\quad \|M\|_{\rm op}\ge{1\over3},\quad
 a\perp b,\quad \Psi\otimes\Psi,\quad 1\le d_t\le3,\quad
 \overline{\Phi_0}=\Phi_0.
\]

The same delimiter restoration applies to every other plain-parenthesis TeX
expression in that round.  The two malformed proof-ending strings
~~(square)~~ mean \(\square\).

In (175), the malformed adjoint ~~\(\overline V^{,*}\)~~ is a
transcription error.  The covariance identity used in Corollary 39 is

\[
 \Psi(VAV^*)=\overline V\,\Psi(A)\,\overline V^{\,*}.          \tag{180}
\]

Equation (180) is the corrected form of (175).  The propositions, their
proofs, equations (165)--(174) and (176)--(179), and the computational output
are otherwise unchanged.

### Proposition 40 (tetrahedral representation and strong additivity)

The channel \(\Psi\) in (174) is measure-and-prepare.  More explicitly, let

\[
 \begin{split}
 r_1&=(1,1,1)/\sqrt3,&r_2&=(1,-1,-1)/\sqrt3,\\
 r_3&=(-1,1,-1)/\sqrt3,&r_4&=(-1,-1,1)/\sqrt3,
 \end{split}
\]

put \(\rho_j=(I_2+r_j\mathbin\cdot\sigma)/2\), and let
\(\overline{\rho_j}\) denote entrywise conjugation.  Then
\(E_j=\rho_j/2\) is a POVM and

\[
 \Psi(A)=\sum_{j=1}^4\operatorname {Tr}(E_jA)\,
                         \overline{\rho_j}.                    \tag{181}
\]

For every finite-dimensional channel \(\Omega\),

\[
 S_{\min}(\Psi\otimes\Omega)
 =S_{\min}(\Psi)+S_{\min}(\Omega)
 =h_2(2/3)+S_{\min}(\Omega).                                  \tag{182}
\]

Consequently, if \(\Phi\) is any equality case in Proposition 38, then for
every \(m\ge1\),

\[
 \Delta(\Phi^{\otimes m},\overline\Phi^{\otimes m})=0,         \tag{183}
\]

and the regularized expression in (99) is zero.

**Proof.**  The four tetrahedral vectors satisfy

\[
 \sum_{j=1}^4r_j=0,\qquad
 \sum_{j=1}^4r_jr_j^T={4\over3}I_3.                            \tag{184}
\]

The first identity gives \(\sum_jE_j=I_2\).  To check (181), write
\(A=(a_0I_2+a\mathbin\cdot\sigma)/2\).  Complex conjugation of a
Bloch matrix replaces \((r_x,r_y,r_z)\) by
\(\widetilde r=(r_x,-r_y,r_z)\).  Equations (184) therefore give

\[
 \begin{split}
 \sum_j\operatorname {Tr}(E_jA)\overline{\rho_j}
 &= {1\over8}\sum_j(a_0+a\mathbin\cdot r_j)
                       (I_2+\widetilde r_j\mathbin\cdot\sigma)\\
 &= {a_0\over2}I_2+
 {a_xX-a_yY+a_zZ\over6}
 ={\,\operatorname {Tr}(A)I_2+A^T\over3}.
 \end{split}                                                   \tag{185}
\]

This is (181).

We next record a self-contained entropy argument.  For every finite ensemble
\((p_j,\alpha_j,\beta_j)\),

\[
 S\!\left(\sum_jp_j\alpha_j\otimes\beta_j\right)
 \ge S\!\left(\sum_jp_j\alpha_j\right)+\sum_jp_jS(\beta_j).
                                                                    \tag{186}
\]

Indeed, start from the classical-quantum state
\(\sum_jp_j|j\rangle\langle j|\otimes\beta_j\), and apply to its
classical register the channel \(|j\rangle\langle j|\mapsto\alpha_j\).
Data processing gives \(I(A:B)\le I(J:B)\).  Substituting
\(I(A:B)=S(A)+S(B)-S(AB)\) and
\(I(J:B)=S(B)-\sum_jp_jS(\beta_j)\) proves (186).

Apply (181) to the first half of an arbitrary bipartite input \(\tau\).
There are probabilities \(p_j\) and conditional states \(\tau_j\) such that

\[
 (\Psi\otimes\Omega)(\tau)
 =\sum_jp_j\,\overline{\rho_j}\otimes\Omega(\tau_j),\qquad
 \sum_jp_j\overline{\rho_j}=\Psi(\tau_A).                     \tag{187}
\]

Equations (186)--(187) imply

\[
 \begin{split}
 S((\Psi\otimes\Omega)(\tau))
 &\ge S(\Psi(\tau_A))+\sum_jp_jS(\Omega(\tau_j))\\
 &\ge S_{\min}(\Psi)+S_{\min}(\Omega).
 \end{split}                                                   \tag{188}
\]

Product minimizers give the reverse inequality, proving (182).

Every equality case in Proposition 38 is unitarily equivalent, by pre- and
post-composition, to \(\Psi\); it therefore obeys (182), as does its
conjugate.  Repeated application of (182) gives

\[
 S_{\min}(\Phi^{\otimes m})=mS_{\min}(\Phi),\qquad
 S_{\min}(\Phi^{\otimes m}\otimes\overline\Phi^{\otimes m})
 =2mS_{\min}(\Phi).
\]

This proves (183), and division by \(m\) proves the assertion about
(99). \(\square\)

The tetrahedral identities and the channel equality in (181) were checked
with exact sympy arithmetic.  Here is the verbatim `python3` output:

~~~text
sum_Bloch_vectors = [0, 0, 0]
second_moment = Matrix([[4/3, 0, 0], [0, 4/3, 0], [0, 0, 4/3]])
sum_POVM_elements = Matrix([[1, 0], [0, 1]])
basis_images_identical = [True, True, True, True]
Psi(|0><0|) = Matrix([[2/3, 0], [0, 1/3]])
Psi_pure_output_eigenvalues = [2/3, 1/3]
Choi_matrix = Matrix([[2/3, 0, 0, 0], [0, 1/3, 1/3, 0], [0, 1/3, 1/3, 0], [0, 0, 0, 2/3]])
Choi_eigenvalues_with_multiplicity = {2/3: 3, 0: 1}
~~~

Thus the small-parameter computation closes more than the two-copy question:
the unique maximally noisy three-unitary qubit geometry is strongly additive,
so it cannot realize the fixed conjugate-pair route in Lemma 25 at any tensor
power.  Nonextremal qubit triples and triples in dimensions at least three
remain **[UNPROVED]**.

## Round 2026-08-21: unitary support graphs classify the extremal qutrit triple

The preceding round used Bloch-sphere geometry, which is unavailable in
dimension three.  This round imports a tool from combinatorial matrix theory:
replace a matrix by the bipartite graph of its nonzero entries and use row and
column orthogonality to forbid local support patterns.  The source actually
opened for this zero-pattern viewpoint was [Larson--Lins--Mitchell, *Graphs of
Unitary Matrices and Positive Semidefinite Zero Forcing*](https://digitalcommons.usf.edu/fac_publications/4020/).
No classification theorem from that paper is assumed below; the required
three-by-three support argument is proved directly.  Applied end-to-end, the
method classifies every qutrit equality case in the universal three-unitary
bound and reduces it to a finite Weyl-phase-space calculation.

### Lemma 41 (spectral zero pattern forced by entropy equality)

Let (U_1,U_2,U_3\in U(d)), and put

\[
 \Phi(A)={1\over3}\sum_{i=1}^3U_iAU_i^*.
\]

If

\[
 S_{\min}(\Phi)=h_2(2/3),                                    \tag{189}
\]

then the following holds.  For distinct (i,j,\ell), if (P_\lambda)
is a spectral projection of (U_i^*U_j), then

\[
 P_\lambda U_i^*U_\ell P_\lambda=0,
 \qquad
 P_\lambda U_j^*U_\ell P_\lambda=0.                         \tag{190}
\]

In particular, the three unitaries are pairwise Hilbert--Schmidt orthogonal:

\[
 \operatorname {Tr}(U_i^*U_j)=0\qquad(i\ne j).              \tag{191}
\]

**Proof.**  Let (x) be a unit eigenvector of (U_i^*U_j), with
(U_i^*U_jx=\lambda x).  Then (U_jx=\lambda U_ix), so the output on
(|x\rangle\langle x|) is a mixture of two pure states,

\[
 \Phi(|x\rangle\langle x|)
 ={2\over3}|U_ix\rangle\langle U_ix|
  +{1\over3}|U_\ell x\rangle\langle U_\ell x|.              \tag{192}
\]

If (c=|\langle U_ix,U_\ell x\rangle|), the two nonzero eigenvalues in
(192) are

\[
 {1\over2}\left(1\mathbin\pm {1\over3}\sqrt{1+8c^2}\right).
\]

Their entropy is at most (h_2(2/3)), with equality exactly when (c=0):
the larger eigenvalue is at least (2/3), strictly larger when (c>0), and
binary entropy is strictly decreasing on ([1/2,1]).  Assumption (189) says
that every output has entropy at least (h_2(2/3)).  Hence equality must hold
in (192), and (U_\ell x\perp U_ix).  Since (U_jx=\lambda U_ix), it is
also orthogonal to (U_jx).

The same assertion holds for every vector in the range of (P_\lambda).
Applying it to (x+ty), with arbitrary (x,y\in\operatorname {ran}
P_\lambda) and (t\in\mathbb C), shows by comparing the coefficients in
(t) and \(\overline t\) that both compressed sesquilinear forms vanish.
This proves (190).

To prove (191), fix (i\ne j), and let \(\ell\) be the third index.  Sum
the diagonal matrix elements of the first relation in (190), now using the
spectral projections of (U_i^*U_\ell).  This gives

\[
 \operatorname {Tr}(U_i^*U_j)
 =\sum_\lambda\operatorname {Tr}
   (P_\lambda U_i^*U_jP_\lambda)=0.
\]

The indices were arbitrary, so (191) follows. \(\square\)

### Proposition 42 (complete qutrit equality classification)

Let (U_1,U_2,U_3\in U(3)).  Equality holds in the universal bound

\[
 S_{\min}\!\left({1\over3}\sum_{i=1}^3U_i(\,\cdot\,)U_i^*\right)
 \le h_2(2/3)                                                 \tag{193}
\]

if and only if, up to common left and right unitary multiplication,
individual phases, and relabeling, the tuple has one of the two forms

\[
 (I_3,Z,X),\qquad (I_3,Z,X^{-1}),                             \tag{194}
\]

where, for (omega=e^{2\pi i/3}),

\[
 Ze_j=\omega^je_j,\qquad Xe_j=e_{j+1\pmod3}.                 \tag{195}
\]

Both normal forms have minimum output entropy exactly (h_2(2/3)).

**Proof.**  The upper bound (193) is Proposition 35 with (N=3,k=1).
Suppose equality holds.  Common left multiplication lets us take
(U_1=I_3); write (A=U_2) and (B=U_3).  Lemma 41 gives

\[
 \operatorname {Tr}A=\operatorname {Tr}B=0.                 \tag{196}
\]

Three unit complex numbers with zero sum are a rotated copy of
(1,\omega,\omega^2).  Indeed, after dividing by the first one, write
(1+z+w=0), where (|z|=|w|=1).  Then
(|1+z|=1), so (2+2\operatorname {Re}z=1); hence
(z\in\{\omega,\omega^2\}), and (w) is the other value.  Thus (A)
has simple spectrum, and an individual phase and a change of basis put

\[
 A=Z.
\]

Apply (190) to the three one-dimensional spectral projections of (A),
with (i=1,j=2,\ell=3).  It says exactly that (B) has zero diagonal in
this basis.

We now use the support graph.  Two different rows of a unitary matrix cannot
have supports meeting in exactly one column: their inner product would then
be a single nonzero summand and could not vanish.  The same statement holds
for columns.  Write

\[
 B=\begin{pmatrix}0&a&b\\ c&0&d\\ e&f&0\end{pmatrix}.
\]

If (a\ne0), rows one and three force (f=0); row three then forces
(e\ne0), rows two and three force (c=0), row two forces (d\ne0),
and rows one and two force (b=0).  Thus the support is the directed
three-cycle ((1,2),(2,3),(3,1)).  If (a=0), row one forces (b\ne0),
and the same argument gives the opposite three-cycle.  In either case each
nonzero entry has modulus one.  Hence

\[
 Be_j=\beta_j e_{j+s\pmod3},\qquad |\beta_j|=1,quad
 s\in\{1,-1\}.                                                \tag{197}
\]

A diagonal conjugation, which leaves (Z) fixed, makes the three phases in
(197) equal: choose a cube root (gamma) of
(eta_0\beta_1\beta_2) and solve successively for diagonal phases
(d_j) in (d_{j+s}\beta_j\overline {d_j}=\gamma).  Their cyclic
consistency is exactly (gamma^3=\beta_0\beta_1\beta_2).  Removing the
remaining common phase from (B) gives (B=X^s).  This proves the
necessity of (194).

Conversely, fix (s\in\{1,-1\}), let

\[
 \Phi_s(A)={A+ZAZ^*+X^sAX^{-s}\over3},                       \tag{198}
\]

and take a pure input (ho=|x\rangle\langle x|).  The nine qutrit Weyl
operators (X^pZ^q), divided by (sqrt3), form a Hilbert--Schmidt
orthonormal basis.  Parseval therefore gives

\[
 \sum_{p,q\in\mathbb F_3}
   |\operatorname {Tr}(\rho X^pZ^q)|^2
 =3\operatorname {Tr}\rho^2=3.                              \tag{199}
\]

The eight nonidentity indices split into the four one-dimensional subspaces
of (mathbb F_3^2).  The two Weyl operators on one such line are adjoints
up to phase, so their expectation values have equal modulus.  Removing the
identity term from (199) and taking one representative per line gives a sum
of four squared moduli equal to one.  The three pairwise overlaps among
(x,Zx,X^sx) correspond, up to phase, to the three distinct lines

\[
 (0,1),\qquad(s,0),\qquad(s,-1).
\]

Consequently their squared moduli sum to at most one, and the pure-state
mixture formula gives

\[
 \begin{split}
 \operatorname {Tr}\Phi_s(\rho)^2
 &={1\over9}\left(3+2\sum_{1\le i<j\le3}
              |\langle U_ix,U_jx\rangle|^2\right)\\
 &\le {5\over9}.                                             \tag{200}
 \end{split}
\]

Lemma 20 at (D=3,p=5/9) has (m=1) and minimizing spectrum
((2/3,1/3,0)).  Equations (66)--(68) and (200) thus give

\[
 S(\Phi_s(\rho))\ge h_2(2/3).                               \tag{201}
\]

Lemma 1 reduces the minimum to pure inputs.  For (x=e_0), the first two
states (x) and (Zx) coincide projectively while (X^sx\perp x), so the
output spectrum is exactly ((2/3,1/3,0)).  Equality holds in (201), proving
the converse and the asserted exact minimum. \(\square\)

### Corollary 43 (finite reduction of the extremal qutrit gap)

Let (Phi) be a uniform three-unitary qutrit channel satisfying (189).
Then its conjugate-pair gap is unitarily equivalent to one of the two
problems

\[
 \Delta(\Phi_s,\overline{\Phi_s})
 =2h_2(2/3)-S_{\min}(\Phi_s\otimes\Phi_{-s}),
 \qquad s\in\{1,-1\}.                                      \tag{202}
\]

Here the second equality uses unitary equivalence of
(overline{\Phi_s}) and (Phi_{-s}).

**Proof.**  Proposition 42 reduces (Phi) to (Phi_s), and all allowed
tuple equivalences preserve the three minimum output entropies defining the
gap.  Let (P e_j=e_{-j\pmod3}).  Directly from (195),

\[
 P\overline ZP=Z,\qquad P\overline XP=X^{-1}.
\]

Thus conjugating the input and output bases of (overline{\Phi_s}) by
(P) gives (Phi_{-s}).  Proposition 42 supplies both single-channel
minimum entropies, proving (202). \(\square\)

The support classification and the finite phase-space bookkeeping were
checked by exact enumeration and exact symbolic arithmetic.  The support
program examined all (2^6=64) zero-diagonal patterns and imposed the
necessary row and column rule that no pair meet in exactly one position.
Here is the verbatim `python3` output:

```text
zero_diagonal_supports_checked = 64
supports_passing_row_and_column_orthogonality_obstruction = 2
  ((0, 2), (1, 0), (2, 1))
  ((0, 1), (1, 2), (2, 0))
projective_lines_in_F3^2 = [(0, 1), (1, 0), (1, 1), (1, 2)]
epsilon = 1 selected_lines = [(0, 1), (1, 0), (1, 2)] distinct = True omitted_line = [(1, 1)]
epsilon = -1 selected_lines = [(0, 1), (1, 0), (1, 1)] distinct = True omitted_line = [(1, 2)]
purity_cap = 5/9
collision_optimizer_spectrum = [Fraction(2, 3), Fraction(1, 3), Fraction(0, 1)]
optimizer_purity = 5/9
P*conjugate(Z)*P = Z: True
P*conjugate(X)*P = X^(-1): True
basis_input_output = Matrix([[2/3, 0, 0], [0, 1/3, 0], [0, 0, 0]])
basis_input_output_eigenvalues = [2/3, 1/3, 0]
```

This closes the equality classification left open after Proposition 40 in
the first higher input dimension: every maximally noisy uniform
three-unitary qutrit channel is a Weyl triangle.  Unlike the tetrahedral
qubit channel, (Phi_s) has not been shown here to be measure-and-prepare,
and the product minimum on the right of (202) remains **[UNPROVED]**.

### Dated formatting correction 2026-08-21

In the immediately preceding round, the inline TeX delimiters were stripped
during transcription.  Thus plain-parenthesis strings such as
~~(U_1,U_2,U_3\in U(d))~~, ~~(i,j,\ell)~~, ~~(P_\lambda)~~,
~~(c=|\langle U_ix,U_\ell x\rangle|)~~, ~~(N=3,k=1)~~,
~~(A=U_2)~~, ~~(B=U_3)~~, ~~(s\in\{1,-1\})~~,
~~(X^pZ^q)~~, ~~(\mathbb F_3^2)~~, and ~~(\Phi_s)~~ are to be
read, respectively, as

\[
 \begin{gathered}
 U_1,U_2,U_3\in U(d),\quad i,j,\ell,\quad P_\lambda,\quad
 c=|\langle U_ix,U_\ell x\rangle|,\quad N=3,\ k=1,\\
 A=U_2,\quad B=U_3,\quad s\in\{1,-1\},\quad
 X^pZ^q,\quad \mathbb F_3^2,\quad \Phi_s .
 \end{gathered}
\]

The same delimiter restoration applies to every other plain-parenthesis TeX
expression in that round, including tuples and intervals with doubled outer
parentheses.

In addition, equation (197) lost a backslash before its spacing command.  Its
corrected form is

\[
 Be_j=\beta_j e_{j+s\pmod3},\qquad |\beta_j|=1,\quad
 s\in\{1,-1\}.                                                \tag{203}
\]

The control character in the sentence after (197) is a corrupted
\(\beta\), and the formulas used there are

\[
 \gamma^3=\beta_0\beta_1\beta_2,\qquad
 d_{j+s}\beta_j\overline {d_j}=\gamma.                        \tag{204}
\]

The corrupted pure-state phrase before (199), and the two delimiter-stripped
expressions in the same sentence, are to be read as

\[
 \rho=|x\rangle\langle x|,\qquad
 X^pZ^q,\qquad \sqrt3.                                       \tag{205}
\]

Finally, the malformed plain strings ~~(omega=e^{2\pi i/3})~~,
~~(gamma)~~, ~~(Phi)~~, and ~~(overline{\Phi_s})~~ mean
\(\omega=e^{2\pi i/3}\), \(\gamma\), \(\Phi\), and
\(\overline{\Phi_s}\), respectively.  Equations (189)--(202), the proofs,
the exact computation, and all mathematical assertions are otherwise
unchanged; equation (203) is the corrected rendering of (197).

## Round 2026-08-21: support-sensitive Haar localization removes the logarithmic exponent

Lemma 36 used the tensor-Haar tail estimate with its generic dependence on
the degree and the total number of variables.  For the particular
localization polynomials (159), that loses a factor of \(\log k\) in the
input-qubit bound: a generic word of length \(2k\) may choose its next
letter from all \(Nk\) variables, whereas (159) contains exactly one
two-letter block in each tensor leg.  Keeping the actual reduced-word
support in the proof of the tail estimate improves (157) to

\[
 \log d_k=O_{N,\varepsilon}(k^2).                             \tag{206}
\]

The only external input in this round is the same result used in the round
containing Lemma 36.  The source actually reopened was
[Chen--Garza-Vargas--van Handel, *A new approach to strong convergence II.
The classical ensembles*, Theorem 1.5, the proof in Section 7.6, and
Theorem 9.7](https://arxiv.org/html/2412.00593v3).  The point needed below
is visible before their final generic word count is substituted: the
constant is controlled by the full-C*-norm to limiting-norm ratio of the
polynomial.  The next lemma records that coefficient-sensitive form.

### Lemma 44 (coefficient-sensitive tensor-Haar tail)

Let \(P\) be a polynomial of degree \(q_0\) in \(L\) disjoint tensor
copies of Haar-unitary variables.  Write

\[
 X_{\rm F}=P(u),\qquad
 K_{\rm full}=\|P\|_{C^*(\mathbb F_{Lr})},\qquad
 R(P)=\max\left\{1,{K_{\rm full}\over\|X_{\rm F}\|}\right\}, \tag{207}
\]

where matrix coefficients are included in both norms.  If
\(X_{\rm F}\ne0\), then for \(0<\varepsilon\le1/2\) and all sufficiently
large local matrix sizes \(n\),

\[
 \mathbb P\{\|P(U^{(\cdot,n)})\|>
                 (1+\varepsilon)\|X_{\rm F}\|\}
 \le {n^L\over\gamma_P\varepsilon}
 \exp\!\left[-{\gamma_Pn\varepsilon^2
                    \over\log^2(n\varepsilon^2)}\right],     \tag{208}
\]

where a universal constant \(C\) may be chosen so that

\[
 \gamma_P^{-1}\le
 C R(P)^6\,[q_0(1+\log q_0)]^2.                              \tag{209}
\]

The same statement holds for a non-self-adjoint polynomial after its
standard \(2\)-by-\(2\) self-adjoint dilation.

**Proof.**  In the proof of Theorem 1.5 in the cited source, denote
\(\widetilde q_0=q_0(1+\log q_0)\).  Immediately before the final choice
of the tail constant, their displayed estimate has the two controlling
terms

\[
 \left({R(P)^3\widetilde q_0\,m^{1+2u}
       \over\varepsilon^{1+2u}u n}\right)^m,
 \qquad
 \left({R(P)^6\widetilde q_0^2\,m^{1+4u}
       \over\varepsilon^{2(1+2u)}u^2 n}\right)^m.             \tag{210}
\]

In the published display, \(R(P)\) has already been replaced by the
generic estimate \((Cr)^{q_0}\), proved there by counting every reduced
word of length at most \(q_0\).  Retaining \(K_{\rm full}/\|X_{\rm F}\|\)
instead gives (210), because the preceding test-function argument uses the
full norm only as the radius of the interval containing every finite
evaluation.  Their choices

\[
 u={1\over1+\log m},\qquad
 m=\left\lfloor{n\varepsilon^2
       \over eR(P)^6\widetilde q_0^2
                    \log^2(n\varepsilon^2)}\right\rfloor
\]

then give (208)--(209), after changing a universal constant and absorbing
the finitely many threshold conditions on \(n\).  The proof of their
Theorem 9.7 repeats this argument for \(L\) disjoint tensor factors; the
only change in the trace estimate is the prefactor \(n^L\).  Its
Haar-unitary extension is stated immediately after that proof and uses the
same Section 7.6 estimate.  Finally,

\[
 \begin{pmatrix}0&P\\P^*&0\end{pmatrix}
\]

has the same finite, limiting, and full norms as \(P\), and has the same
degree.  This proves the last assertion. \(\square\)

The gain comes from an exact count of the words that survive the unitary
cancellations.  Put

\[
 m_N=N^2-N+1.                                                 \tag{211}
\]

### Lemma 45 (reduced support of a localization polynomial)

Let \(D=N^k\), let \(b\in M_D\) have trace zero, and set

\[
 P_b(U)=\sum_{v,w\in[N]^k}b_{vw}
       \bigotimes_{r=1}^k U_{v_r}^{(r)*}U_{w_r}^{(r)}.         \tag{212}
\]

If \(P_b\) is not identically zero, then

\[
 {\|P_b\|_{C^*(\mathbb F_{Nk})}
      \over\|P_b(u)\|_{A^{\otimes_{\min}k}}}
 \le\sqrt{m_N^k-1}.                                         \tag{213}
\]

Here the full-group norm treats the \(Nk\) formal generators as free, while
the denominator evaluates the \(N\) generators belonging to distinct legs
in the minimal tensor product.

**Proof.**  For one leg, record the reduced symbol

\[
 \alpha(i,j)=
 \begin{cases}
 0,&i=j,\\
 (i,j),&i\ne j.
 \end{cases}
\]

There are \(1+N(N-1)=m_N\) possibilities.  For
\(s=(s_1,\ldots,s_k)\) in this symbol set to the \(k\)-th power, define

\[
 c_s=\sum_{\alpha(v_r,w_r)=s_r\ \forall r}b_{vw}.             \tag{214}
\]

After the cancellations \(U_i^*U_i=I\), equation (212) becomes

\[
 P_b=\sum_s c_s w_s,                                         \tag{215}
\]

where \(w_s\) is the ordered product of the nonidentity two-letter blocks
specified by \(s\).  The all-zero coefficient is
\(c_{(0,\ldots,0)}=\operatorname {Tr}b=0\).  All remaining \(w_s\) are
distinct reduced words in the full free group: generators in adjacent
blocks carry different tensor-leg labels, so no new cancellation is
possible.  The triangle and Cauchy--Schwarz inequalities therefore give

\[
 \|P_b\|_{C^*(\mathbb F_{Nk})}
 \le\sum_{s\ne0}|c_s|
 \le\sqrt{m_N^k-1}\left(\sum_{s\ne0}|c_s|^2\right)^{1/2}.    \tag{216}
\]

In the product free-group trace, the tensor words \(w_s\) are orthonormal.
Consequently

\[
 \|P_b(u)\|\ge\|P_b(u)\|_2
 =\left(\sum_{s\ne0}|c_s|^2\right)^{1/2}.                    \tag{217}
\]

Equations (216)--(217) prove (213).  If every \(c_s\) vanishes, (215)
shows directly that every unitary evaluation vanishes, so this excluded case
never contributes a bad event in a union bound. \(\square\)

### Proposition 46 (quadratic input-qubit localization)

Fix \(N\ge4\) and \(0<\varepsilon\le1/2\).  For every \(k\ge1\), there
is an integer

\[
 n_k\le\exp(C_{N,\varepsilon}k)                               \tag{218}
\]

and \(N\)-tuples \(U^{(r)}\in U(n_k)^N\), \(1\le r\le k\), such
that, with \(W_v=\bigotimes_rU_{v_r}^{(r)}\), every trace-zero
\(a\in M_{N^k}\) satisfies

\[
 \left\|\sum_{v,w}a_{vw}W_v^*W_w\right\|
 \le(1+2\varepsilon)K_{N,k}\|a\|_2.                         \tag{219}
\]

Thus the total input dimension \(d_k=n_k^k\) satisfies the improved
exponent

\[
 \log d_k\le C_{N,\varepsilon}k^2.                           \tag{220}
\]

**Proof.**  Use the same trace-zero Hilbert--Schmidt unit sphere
\(\mathbb S_D\), net radius

\[
 \delta={\varepsilon K_{N,k}\over D},\qquad D=N^k,
\]

and volumetric net \(\mathcal M\) as in Lemma 36.  Thus

\[
 |\mathcal M|\le(1+2/\delta)^{2(D^2-1)},\qquad
 \log|\mathcal M|=O_{N,\varepsilon}(kN^{2k}).                \tag{221}
\]

For each \(b\in\mathcal M\), apply Lemma 44 to the self-adjoint dilation
of \(P_b\).  Lemma 45, with \(q_0=2k\) and \(L=k\), makes the tail
constant uniform over the net:

\[
 \gamma_k^{-1}
 \le C(m_N^k-1)^3[2k(1+\log(2k))]^2
 \le \exp(A_Nk)                                              \tag{222}
\]

after increasing \(A_N\) to cover all \(k\ge1\).  The zero polynomials
are identically zero at finite size and may be omitted.  Since (11) gives
\(\|P_b(u)\|\le K_{N,k}\), a union bound succeeds whenever

\[
 |\mathcal M|{n^k\over\gamma_k\varepsilon}
 \exp\!\left[-{\gamma_kn\varepsilon^2
                    \over\log^2(n\varepsilon^2)}\right]<1.   \tag{223}
\]

Choose \(n=\lceil e^{C_{N,\varepsilon}k}\rceil\).  By (222), the
magnitude of the negative exponent in (223) is at least

\[
 {\varepsilon^2e^{(C_{N,\varepsilon}-A_N)k}
       \over O_{N,\varepsilon}(k^2)}.                         \tag{224}
\]

On the other hand, (221) gives
\(\log|\mathcal M|=\exp((2\log N+o(1))k)\), while
\(k\log n+\log\gamma_k^{-1}=O_{N,\varepsilon}(k^2)\).
Taking \(C_{N,\varepsilon}>A_N+2\log N\), with a further fixed margin,
makes (224) dominate every positive term in the logarithm of (223).
Increasing the constant handles the finitely many remaining \(k\).  Hence
a simultaneous good realization exists and satisfies (218).

For arbitrary \(a\in\mathbb S_D\), choose \(b\in\mathcal M\) with
\(\|a-b\|_2\le\delta\).  The finite evaluation is \(D\)-Lipschitz by
(16), so the good-net estimate gives

\[
 \begin{split}
 \|P_a(U)\|
 &\le\|P_b(U)\|+D\delta\\
 &\le(1+\varepsilon)K_{N,k}+\varepsilon K_{N,k}
 =(1+2\varepsilon)K_{N,k}.
 \end{split}
\]

Homogeneity proves (219), and
\(\log d_k=k\log n_k\le C_{N,\varepsilon}k^2\) proves (220).
\(\square\)

### Corollary 47 (the gap rate with \(O(k^2)\) input qubits)

For every fixed \(N\ge4\), \(0<\varepsilon\le1/2\), and \(k\ge1\),
there are finite-dimensional conjugate channels with complementary output
dimension \(N^k\), input dimension satisfying (220), and

\[
 \Delta(\Phi_k,\overline\Phi_k)
 \ge {k\log N\over N}
 -2\log\!\left(1+(1+2\varepsilon)^2
       \left[(1+9/N)^k-1\right]\right).                     \tag{225}
\]

In particular,

\[
 \liminf_{k\to\infty}{1\over k}
 \Delta(\Phi_k,\overline\Phi_k)\ge c_N.                     \tag{226}
\]

**Proof.**  Proposition 46 is exactly Lemma 36 with (164) strengthened to
(218).  Lemma 10 and the orthogonal collision calculation (38) therefore
give

\[
 \operatorname {Tr}\mathcal C^{[k]}(\rho)^2
 \le {1\over N^k}\left(1+(1+2\varepsilon)^2
       [(1+9/N)^k-1]\right)
\]

for every input state.  Apply \(S(\rho)\ge-log\operatorname {Tr}\rho^2\)
to both conjugate channels and subtract the Bell bound (23) to obtain
(225).  Dividing by \(k\) gives (226), exactly as in Proposition 37.
The local space is \((\mathbb C^{n_k})^{\otimes k}\), so (220) is its
input-dimension bound. \(\square\)

Thus the best proved quantitative construction now uses
\(O_{N,\varepsilon}(k^2)\) input qubits and \(O_N(k)\) output qubits.  The
remaining gap to the qubit-linear target (24) is one power of \(k\), rather
than one power together with a logarithmic factor.  The support argument
does not make \(n_k\) bounded: (222) still decays exponentially because the
localization polynomial has exponentially many genuine tensor words.

For completeness, the reduced-symbol count in Lemma 45 was checked by
explicit enumeration.  The multiplicity of a symbol is the number of
coefficient pairs \((v,w)\) that collapse to it.  Here is the verbatim
`python3` output:

```text
N=3 k=2 D=9
coefficient_pairs=81
enumerated_reduced_modes=49 formula=49 identical=True
nonidentity_modes=48 formula=48
multiplicity_histogram={1: 36, 3: 12, 9: 1}
sum_of_multiplicities=81 pairs_match=True
N=4 k=3 D=64
coefficient_pairs=4096
enumerated_reduced_modes=2197 formula=2197 identical=True
nonidentity_modes=2196 formula=2196
multiplicity_histogram={1: 1728, 4: 432, 16: 36, 64: 1}
sum_of_multiplicities=4096 pairs_match=True
```

### Dated formatting correction 2026-08-21

In the proof of Corollary 47, the malformed expression
~~\(S(\rho)\ge-log\operatorname {Tr}\rho^2\)~~ is a transcription error.
The entropy inequality used there is

\[
 S(\rho)\ge-\log\operatorname {Tr}\rho^2.
\]

Equations (225)--(226) and the proof are unchanged.

## Round 2026-08-21: uniformity audit of the coefficient-sensitive Haar tail

The strongest quantitative assertion presently recorded is the quadratic
input-qubit estimate (220).  Its only genuinely new probabilistic step is
Lemma 44: Lemma 45 and the net argument are elementary once the tail in
(208)--(209) is uniform over the coefficient net.  This round audits that
uniformity at the point where the full-group norm is compared with the
limiting tensor norm.

### Dated correction 2026-08-21

The sentence in the proof of Lemma 44 saying that the opened source's
display already contains the two terms in (210) with (R(P)) is inaccurate.
In the proof of its Theorem 1.5, the source's displayed estimate has already
used its Lemma 7.12 to replace

\[
 {K\over\|X_{\rm F}\|}
 \quad\hbox{by}\quad (Cr)^{q_0}.                              \tag{227}
\]

Moreover, its Theorem 9.7 is displayed for the tensor GUE model; the
corresponding Haar assertion is stated in the sentence immediately after
the proof, rather than as a separately displayed theorem.  Thus the old
attribution alone did not prove (208)--(209).  The retained-(K) calculation
needed to repair the gap is given next.

The source reopened for this audit was
[Chen--Garza-Vargas--van Handel, *A new approach to strong convergence II.
The classical ensembles*, Theorem 1.5, Sections 7.3--7.6, and Theorem 9.7
with the sentence following its proof]
(https://arxiv.org/html/2412.00593v3).  In particular, its Section 7 defines

\[
 K=\|P\|_{M_s\otimes C^*(\mathbb F_r)}
\]

before the generic estimate in its Lemma 7.12 is invoked.

### Lemma 48 (retained-radius tensor-Haar estimate)

Let (P) be a nonzero self-adjoint polynomial of degree at most (q_0)
in (L) disjoint tensor copies of independent Haar-unitary variables, with
matrix coefficients of fixed size (s).  Write

\[
 \rho=\|P(u)\|>0,\qquad
 K=\|P\|_{M_s\otimes C^*(\mathbb F_{Lr})},\qquad
 R={K\over\rho}\ge1,qquad
 \widetilde q_0=q_0(1+\log q_0).                              \tag{228}
\]

There are universal constants (c,C>0) such that, whenever
(0<\varepsilon\le1/2) and (n) satisfies the elementary threshold
conditions in the proof below,

\[
 \mathbb P\{\|P(U^{(\cdot,n)})\|>(1+\varepsilon)\rho\}
 \le {C R s n^L\over\varepsilon}
 \exp\!\left[-{c n\varepsilon^2
       \over R^6\widetilde q_0^{,2}\log^2(n\varepsilon^2)}\right].
                                                                    \tag{229}
\]

The threshold can be chosen using only
(R,q_0,s,arepsilon), and not the coefficients of (P) separately.
Consequently (208)--(209) hold, after changing a universal constant, for
the scalar polynomials and their (2\)-by-(2) self-adjoint dilations used
in Proposition 46.

**Proof.**  We first isolate exactly how (K) enters the opened proof.  The
smooth expansion in its Theorem 7.8 is obtained from the master inequality
by writing

\[
 f(\vartheta)=h(K\cos\vartheta).
\]

The master-inequality constants depend on the polynomial only through
(q_0) and the interval radius (K).  In the proof of Theorem 1.5, the test
function (h) vanishes on the (arepsilon\rho/2)-neighborhood of
([-ho,ho]), equals one outside its (arepsilon\rho)-neighborhood,
and is differentiated after the substitution above.  Hence every derivative
ratio contributed by the cutoff is a power of

\[
 {K\over\varepsilon\rho}={R\over\varepsilon}.                \tag{230}
\]

The source next uses (K/\rho\le(Cr)^{q_0}).  If that one substitution is
deferred, the identical calculation, with
(m'=\lceil(1+u)m\rceil\le3m), gives

\[
 \begin{split}
 &\mathbb P\{\|P(U^{(\cdot,n)})\|>(1+\varepsilon)\rho\}\\
 &\quad\le {C R s n^L\over\varepsilon}
 \left[
 \left({C R^3\widetilde q_0m^{1+2u}
        \over\varepsilon^{1+2u}u n}\right)^m
 +\left({C R^6\widetilde q_0^{,2}m^{1+4u}
        \over\varepsilon^{2(1+2u)}u^2 n}\right)^m
 \right].                                                     \tag{231}
 \end{split}
\]

For completeness, passing from one Haar space to (L) disjoint tensor
spaces changes only the trace prefactor from (sn) to (sn^L).  Indeed, a
monomial in a spectral moment splits by tensor leg, normalized trace and
expectation both factor, and the total number of Haar letters over all legs
is at most the degree of that monomial.  If these leg degrees are
(a_1,\ldots,a_L), then

\[
 \sum_{j:a_j>0}a_j\log a_j
 \le\left(\sum_j a_j\right)
       \log\left(\sum_j a_j\right).                           \tag{232}
\]

Thus multiplying the legwise rational moment formulas does not increase the
(q_0(1+\log q_0)) degree envelope in the Haar master inequality.  This is
the bookkeeping behind the Haar extension stated after Theorem 9.7 in the
opened source.  The full norm in (228) bounds every finite tensor evaluation,
because the (Lr) unitaries acting on the tensor space define a unitary
representation of (C^*(\mathbb F_{Lr})).  The support-bootstrapping part of
the cited proof uses qualitative tensor strong convergence to place all
asymptotic distributions in ([-ho,ho]); it introduces no coefficient
constant into (231).  These observations prove (231) for the tensor model.

It remains to choose the auxiliary parameters without coefficient-dependent
thresholds.  Put

\[
 \gamma={c_0\over R^6\widetilde q_0^{,2}},\qquad
 m=\left\lfloor{\gamma n\varepsilon^2
             \over\log^2(n\varepsilon^2)}\right\rfloor,
 \qquad u={1\over1+\log m},                                  \tag{233}
\]

where (c_0>0) is a sufficiently small universal constant.  Require
(m\ge2), (s\le e^m), and the source's Haar condition
(arepsilon\ge2/\sqrt n).  These conditions depend only on the displayed
parameters.  Now

\[
 m^{4u}\le e^4,qquad u^{-2}=(1+\log m)^2,qquad
 \varepsilon^{-4u}\le C,                                    \tag{234}
\]

where the last estimate follows from
(arepsilon\ge2/\sqrt n) and (233), exactly as in the parameter choice in
Section 7.6 of the source.  Substitution of (233)--(234) into the second base
in (231) makes it at most (e^{-2}) after decreasing (c_0).  The square of
the first base is bounded by a universal constant times (m/n) times the
second base, so it is at most (e^{-2}) as well after the same adjustment.
Absorbing the floor in (233) and the two summands into universal constants
gives (229).

For a non-self-adjoint (P), its self-adjoint dilation

\[
 \begin{pmatrix}0&P\\P^*&0\end{pmatrix}                     \tag{235}
\]

has coefficient size (2s), the same degree, and exactly the same finite,
full, and limiting norms.  Since (s=1) before dilation in Proposition 46,
this fixed factor is absorbed into (C).  Finally, the prefactor in (229)
is at most (n^L/(\gamma'\varepsilon)), and its exponent is at least
(gamma'n\varepsilon^2/\log^2(n\varepsilon^2)), for

\[
 (\gamma')^{-1}\le C R^6\widetilde q_0^{,2}.                \tag{236}
\]

This is precisely (208)--(209), with uniform threshold conditions. \(\square\)

### Corollary 49 (the net in Proposition 46 has a uniform tail)

For every nonzero net polynomial (P_b) in (212), after self-adjoint
dilation,

\[
 L=k,qquad q_0\le2k,qquad s=2,qquad
 R(P_b)\le\sqrt{m_N^k-1}.                                   \tag{237}
\]

Therefore every member of the net has (229) with one common constant
(gamma_k) satisfying

\[
 \gamma_k^{-1}le
 C(m_N^k-1)^3[2k(1+\log(2k))]^2\le e^{A_Nk}.                \tag{238}
\]

In particular, the choice (n_k\le e^{C_{N,\varepsilon}k}) in
Proposition 46 is valid, and (220), (225), and (226) remain proved.

**Proof.**  The first three assertions in (237) follow directly from (212)
and (235).  Lemma 45 proves the fourth.  Lemma 48 now gives (238) uniformly
over (b); zero polynomials give no bad event.  All threshold conditions in
(233)--(234) also depend only on the right side of (237), so increasing
(C_{N,\varepsilon}) handles them simultaneously rather than taking an
uncontrolled maximum over the net.

With (n=\lceil e^{C_{N,\varepsilon}k}\rceil), the magnitude of the
negative logarithm in (229) is

\[
 {e^{(C_{N,\varepsilon}-A_N)k}\over O_{N,\varepsilon}(k^2)},
\]

whereas (221) is (O_{N,\varepsilon}(kN^{2k})).  Choosing
(C_{N,\varepsilon}>A_N+2\log N) with fixed positive margin makes the
former larger for all sufficiently large (k); increasing the constant
once more covers the remaining finite set of (k).  The union bound and
the deterministic net extension in Proposition 46 then apply unchanged.
This proves the claims. \(\square\)

As a finite check of the coefficient grouping used in the only
coefficient-sensitive input, the following `python3` computation used an
integer trace-zero coefficient matrix at (N=3,k=2).  It verifies the
identity mode cancellation, the count (m_N^k-1=48), and the exact
Cauchy--Schwarz inequality in (216).  The output is verbatim:

```text
N=3 k=2 D=9
trace_b=0
identity_mode=0
mode_cap=48 enumerated_nonidentity_modes=48
nonzero_coefficients=45
l1_squared=28224
mode_cap_times_l2_squared=38400
cauchy_schwarz_verified=True
```

The audit therefore changes the attribution but not the quadratic
input-qubit conclusion.  The remaining quantitative loss is the exponential
radius ratio in (237): even after the coefficient-sensitive repair, (238)
forces the local Haar size to grow exponentially with (k).  Removing one
power of (k) from (220) would require a tail estimate governed by a smaller
quantity than the full-to-minimal norm ratio, or a localization argument
that avoids a uniform net over all trace-zero coefficients.  Neither is
proved here **[UNPROVED]**.

### Dated formatting correction 2026-08-21

Several backslashes in the immediately preceding round were consumed during
transcription.  The mathematical content is unchanged, but the malformed
renderings are struck and replaced below.

All plain-parenthesis expressions in that round are inline mathematics.  In
particular, strings such as ~~(R(P))~~, ~~(K)~~, ~~(P)~~, ~~(q_0)~~,
~~(L)~~, ~~(s)~~, ~~(c,C>0)~~, ~~(n)~~, ~~(sn^L)~~,
~~(a_1,\ldots,a_L)~~, ~~(C^*(\mathbb F_{Lr}))~~,
~~(m\ge2)~~, ~~(s\le e^m)~~, ~~(e^{-2})~~, ~~(c_0)~~,
~~(P_b)~~, ~~(b)~~, and ~~(N=3,k=2)~~ mean, respectively,
\[
 \begin{gathered}
 R(P),\ K,\ P,\ q_0,\ L,\ s,\ c,C>0,\ n,\ sn^L,\quad
 a_1,\ldots,a_L,\quad C^*(\mathbb F_{Lr}),\\
 m\ge2,\quad s\le e^m,\quad e^{-2},\quad c_0,\quad
 P_b,\quad b,\quad N=3,\ k=2.
 \end{gathered}
\]
The corrupted control characters in the prose and formulas mean
\(\varepsilon\) and \(\rho\).  Thus the cutoff neighborhoods are the
\(\varepsilon\rho/2\)- and \(\varepsilon\rho\)-neighborhoods of
\([-\rho,\rho]\), the support interval is \([-\rho,\rho]\), and the Haar
condition is \(\varepsilon\ge2/\sqrt n\).

The malformed display (229) is struck and replaced by
\[
 \text{~~malformed equation (229)~~},\qquad
 \mathbb P\{\|P(U^{(\cdot,n)})\|>(1+\varepsilon)\rho\}
 \le {C R s n^L\over\varepsilon}
 \exp\!\left[-{c n\varepsilon^2
       \over R^6\widetilde q_0^{\,2}\log^2(n\varepsilon^2)}\right].
                                                                    \tag{239}
\]

The malformed display (231) is struck and replaced by
\[
 \begin{split}
 &\text{~~malformed equation (231)~~},\\
 &\mathbb P\{\|P(U^{(\cdot,n)})\|>(1+\varepsilon)\rho\}\\
 &\quad\le {C R s n^L\over\varepsilon}
 \left[
 \left({C R^3\widetilde q_0m^{1+2u}
        \over\varepsilon^{1+2u}u n}\right)^m
 +\left({C R^6\widetilde q_0^{\,2}m^{1+4u}
        \over\varepsilon^{2(1+2u)}u^2 n}\right)^m
 \right].
                                                                    \tag{240}
 \end{split}
\]

The malformed displays (233), (236), (237), and (238) are struck and
replaced, respectively, by
\[
 \text{~~malformed equation (233)~~},\qquad
 \gamma={c_0\over R^6\widetilde q_0^{\,2}},\qquad
 m=\left\lfloor{\gamma n\varepsilon^2
             \over\log^2(n\varepsilon^2)}\right\rfloor,
 \qquad u={1\over1+\log m},                                  \tag{241}
\]
\[
 \text{~~malformed equation (236)~~},\qquad
 (\gamma')^{-1}\le C R^6\widetilde q_0^{\,2},                \tag{242}
\]
\[
 \text{~~malformed equation (237)~~},\qquad
 L=k,\qquad q_0\le2k,\qquad s=2,\qquad
 R(P_b)\le\sqrt{m_N^k-1},                                   \tag{243}
\]
and
\[
 \text{~~malformed equation (238)~~},\qquad
 \gamma_k^{-1}\le
 C(m_N^k-1)^3[2k(1+\log(2k))]^2\le e^{A_Nk}.                \tag{244}
\]

The missing delimiters in the proof of Lemma 48 also restore
\[
 K/\rho\le(Cr)^{q_0},\qquad
 m'=\lceil(1+u)m\rceil\le3m,
\]
and those in Corollary 49 restore
\[
 n_k\le e^{C_{N,\varepsilon}k},\qquad
 \gamma_k,\qquad
 n=\lceil e^{C_{N,\varepsilon}k}\rceil,\qquad
 O_{N,\varepsilon}(kN^{2k}),\qquad
 C_{N,\varepsilon}>A_N+2\log N.
\]
Equations (239)--(244) are the forms used by Lemma 48 and Corollary 49.

### Dated mathematical correction 2026-08-21

The assertion \(\varepsilon^{-4u}\le C\) in (234) does not follow from
\(\varepsilon\ge2/\sqrt n\), (233), and \(m\ge2\).  There is a direct
counterfamily.  Fix \(X>4\) and \(\gamma>0\) so that
\[
 m=\left\lfloor{\gamma X\over\log^2X}\right\rfloor\ge2,
 \qquad u={1\over1+\log m},
\]
and let \(n\to\infty\) while \(\varepsilon=\sqrt{X/n}\).  Then
\[
 n\varepsilon^2=X,\qquad \varepsilon\ge {2\over\sqrt n},
\]
so \(m\) and \(u>0\) stay fixed, but
\[
 \varepsilon^{-4u}=(n/X)^{2u}\longrightarrow\infty.          \tag{245}
\]
Thus the uniform-in-\(\varepsilon\) passage from (240) to (239) is not
proved by the parameter choice given above.  The claims in Lemma 48 that
(239) follows with \((\gamma')^{-1}\) bounded as in (242), uniformly for
all \(0<\varepsilon\le1/2\), are **[UNPROVED]**.  This does not challenge
the generic external Theorem 1.5 quoted from the opened source; it diagnoses
only the new retained-\(R\) derivation in this document.

The quadratic input-qubit result needs only a fixed tolerance.  The following
weaker form of the tail is sufficient and follows rigorously from (240).
Fix \(0<\varepsilon_0\le1/2\).  With
\[
 \gamma_{\varepsilon_0}
 ={c_0\varepsilon_0^4\over R^6\widetilde q_0^{\,2}},\qquad
 m=\left\lfloor{\gamma_{\varepsilon_0}n\varepsilon_0^2
              \over\log^2(n\varepsilon_0^2)}\right\rfloor,
 \qquad u={1\over1+\log m},                                  \tag{246}
\]
one has
\[
 \mathbb P\{\|P(U^{(\cdot,n)})\|>(1+\varepsilon_0)\rho\}
 \le {C R s n^L\over\varepsilon_0}
 \exp\!\left[-{c\varepsilon_0^4 n\varepsilon_0^2
       \over R^6\widetilde q_0^{\,2}
                    \log^2(n\varepsilon_0^2)}\right]          \tag{247}
\]
whenever the explicit threshold conditions following (233) hold.

Indeed, now
\[
 \varepsilon_0^{-4u}\le\varepsilon_0^{-4}.
\]
Using (246), \(m^{4u}\le e^4\), and
\(u^{-2}=(1+\log m)^2\), the second base in (240) is at most a universal
constant times
\[
 R^6\widetilde q_0^{\,2}
 {\gamma_{\varepsilon_0}\over\varepsilon_0^4}=c_0.           \tag{248}
\]
Choose \(c_0\) so this is at most \(e^{-2}\).  As before, the square of
the first base is at most a universal constant times \(m/n\) times the
second base, and decreasing \(c_0\) controls it simultaneously.  This proves
(247), including its coefficient-uniform threshold.

Consequently the correct uniform estimate for the net is
\[
 \gamma_{k,\varepsilon_0}^{-1}
 \le C_{\varepsilon_0}
 (m_N^k-1)^3[2k(1+\log(2k))]^2
 \le e^{A_{N,\varepsilon_0}k}.                               \tag{249}
\]
The proof of Corollary 49 then goes through with
\(A_N,C_{N,\varepsilon}\) replaced by
\(A_{N,\varepsilon_0},C_{N,\varepsilon_0}\).  Proposition 46 already fixes
\(\varepsilon\) before choosing the matrix size, so (247)--(249) still prove
(218)--(220), and hence (225)--(226).  What fails is only the stronger
uniform-in-\(\varepsilon\) formulation of Lemma 48.

Here is verbatim Python 3 output for a finite check of the counterfamily in
(245).  It uses \(X=10^6\) and \(\gamma=10^{-2}\); the analytic divergence
in (245), not this sample, proves the failure.

~~~text
X = 1000000 gamma = 0.01 m = 52 u = 0.201969455926219
n = 1000000000000 epsilon = 1.000e-03 epsilon>=2/sqrt(n) = True epsilon^(-4u) = 2.652366115725e+02
n = 1000000000000000000 epsilon = 1.000e-06 epsilon>=2/sqrt(n) = True epsilon^(-4u) = 7.035046011846e+04
n = 1000000000000000000000000 epsilon = 1.000e-09 epsilon>=2/sqrt(n) = True epsilon^(-4u) = 1.865951766439e+07
n = 1000000000000000000000000000000 epsilon = 1.000e-12 epsilon>=2/sqrt(n) = True epsilon^(-4u) = 4.949187238879e+09
~~~

## Round 2026-08-21: the stabilizer sector of the extremal qutrit pair

Corollary 43 reduces the smallest undecided random-unitary case to the
qutrit Weyl-triangle pair

\[
 \Phi_1\otimes\Phi_{-1},\qquad
 \Phi_s(A)={A+ZAZ^*+X^sAX^{-s}\over3}.
\]

The unrestricted input problem remains continuous.  The smallest exact
entangled-input sector inside it is the two-qutrit stabilizer sector.  This
round settles that entire sector.  In fact, every entangled stabilizer input
has an entropy margin of at least \(2\log2/3\) above the product minimum.

Write \(W_{p,q}=X^pZ^q\), with \((p,q)\in\mathbb F_3^2\).  On
\(V=\mathbb F_3^2\oplus\mathbb F_3^2\), use the symplectic form

\[
 [(p,q,r,t),(p',q',r',t')]
 =pq'-qp'+rt'-tr'.                                           \tag{250}
\]

The nine Weyl errors in the product channel have phase-space support

\[
 E=T_+\times T_-,\qquad
 T_+=\{0,(0,1),(1,0)\},\qquad
 T_-=\{0,(0,1),(2,0)\}.                                    \tag{251}
\]

A pure two-qutrit stabilizer state is specified by a two-dimensional
Lagrangian subspace \(L\subset V\), together with a character of \(L\).
The character will not affect any spectrum below.

### Lemma 50 (coset spectrum for a stabilizer input)

Let \(|\psi_L\rangle\) be a stabilizer state with Lagrangian plane \(L\).
For each coset \(C\in V/L\), put

\[
 n_C=|E\cap C|.
\]

The nonzero eigenvalues of
\((\Phi_1\otimes\Phi_{-1})(|\psi_L\rangle\langle\psi_L|)\)
are exactly

\[
 \left\{{n_C\over9}:n_C>0\right\},                         \tag{252}
\]

with multiplicity.

**Proof.**  Up to an irrelevant phase, the inner product between two orbit
vectors \(W_e|\psi_L\rangle\) and \(W_f|\psi_L\rangle\) is the stabilizer
expectation of \(W_{f-e}\).  If \(f-e\in L\), the two vectors lie on the
same ray.  If \(f-e\notin L=L^\perp\), there is an \(\ell\in L\) with
\([\ell,f-e]\ne0\).  Commuting \(W_\ell\) through \(W_{f-e}\) multiplies
the expectation by a nontrivial third root of unity, so the expectation is
zero.  Thus errors in one coset give one ray, while errors in different
cosets give orthogonal rays.  Grouping the nine equally weighted ensemble
members by coset proves (252). \(\square\)

### Proposition 51 (all forty Lagrangian spectra)

As \(L\) ranges over the forty Lagrangian planes in \(V\), the nonzero
intersection histograms \((n_C:n_C>0)\), sorted decreasingly, are precisely

\[
\begin{array}{c|c|c}
\text{kind of }L&\text{number of planes}&\text{histogram}\
\hline
\text{product, edge--edge}&9&(4,2,2,1)\\
\text{product, edge--omitted}&6&(2,2,2,1,1,1)\\
\text{product, omitted--omitted}&1&(1,1,1,1,1,1,1,1,1)\\
\text{entangled, generic}&18&(2,2,1,1,1,1,1)\\
\text{entangled, aligned I}&3&(2,2,2,1,1,1)\\
\text{entangled, aligned II}&3&(3,1,1,1,1,1,1).
\end{array}                                                   \tag{253}
\]

**Proof.**  First suppose that \(L\) contains a nonzero local vector
\((a,0)\).  Isotropy forces the first component of every vector of \(L\) to
belong to the line spanned by \(a\).  Subtracting a multiple of \((a,0)\)
from a second generator then exhibits a vector \((0,b)\in L\).  Hence

\[
 L=\langle a\rangle\oplus\langle b\rangle.                  \tag{254}
\]

There are four lines in each copy of \(\mathbb F_3^2\), so (254) gives
sixteen product planes.  The three edge directions of either triangle in
(251) have coset-intersection histogram \((2,1)\); its one omitted direction
has histogram \((1,1,1)\).  Taking products of these one-factor counts gives
the first three rows of (253), with multiplicities
\(3\cdot3=9\), \(3\cdot1+1\cdot3=6\), and \(1\).

Every remaining Lagrangian plane meets both local phase spaces only at zero.
Its first projection is therefore invertible, and it is uniquely the graph

\[
 L=\{(x,Ax):x\in\mathbb F_3^2\}                             \tag{255}
\]

of a linear map \(A\).  In two dimensions,
\([Ax,Ay]=\det(A)[x,y]\); hence (255) is isotropic exactly when
\(\det A=-1=2\) in \(\mathbb F_3\).  There are twenty-four such maps.

Let \(e_1=(1,0)\), \(e_2=(0,1)\), and put
\(a=Ae_1\), \(b=Ae_2\).  The cosets of (255) are labeled by
\(z=y-Ax\), and their counts are

\[
 n_z=|\{(x,y)\in T_+\times T_-:y-Ax=z\}|.                  \tag{256}
\]

Thus only the twenty-four ordered bases \((a,b)\) satisfying
\(\det(a,b)=2\) must be checked.  The triangle \(T_-\) omits the direction
\(\langle(1,2)\rangle\).  For the eighteen bases for which
\(\{0,a,b\}\) omits a different direction, direct subtraction in (256)
gives \((2,2,1,1,1,1,1)\).  The six aligned bases split as

\[
\begin{array}{c|c}
(a,b)&(n_z:n_z>0)\\
\hline
((0,1),(1,1)),\ ((1,0),(0,2)),\ ((2,2),(2,0))
 &(2,2,2,1,1,1)\\
((0,2),(2,2)),\ ((1,1),(1,0)),\ ((2,0),(0,1))
 &(3,1,1,1,1,1,1).
\end{array}                                                   \tag{257}
\]

Equations (256)--(257) give the last three rows of (253).  The sixteen
planes in (254) and twenty-four planes in (255) exhaust all cases. \(\square\)

### Corollary 52 (no stabilizer additivity gap)

For every pure two-qutrit stabilizer state \(|\psi\rangle\),

\[
 S((\Phi_1\otimes\Phi_{-1})(|\psi\rangle\langle\psi|))
 \ge 2h_2(2/3).                                               \tag{258}
\]

Equality holds exactly for the nine edge--edge product stabilizer planes in
(253).  Every entangled stabilizer state satisfies the stronger estimate

\[
 S((\Phi_1\otimes\Phi_{-1})(|\psi\rangle\langle\psi|))
 \ge 2h_2(2/3)+{2\log2\over3}.                               \tag{259}
\]

The same conclusions hold with the two channel factors interchanged.

**Proof.**  A histogram \(n=(n_j)\) in (253) gives, by Lemma 50,

\[
 H(n/9)=2\log3-{1\over9}\sum_jn_j\log n_j.                 \tag{260}
\]

The edge--edge value is

\[
 H((4,2,2,1)/9)=2\log3-{4\over3}\log2=2h_2(2/3).          \tag{261}
\]

In the order displayed in the exact computation below, the other entropy
excesses over (261) are

\[
 {4\over3}\log2,\quad {8\over9}\log2,\quad
 {2\over3}\log2,\quad {1\over3}\log(16/3),               \tag{262}
\]

all strictly positive.  Among the three entangled rows of (253), the smallest
excess is \(2\log2/3\), proving (258)--(259).  Interchanging the factors
merely swaps \(T_+\) and \(T_-\), which leaves all coset counts unchanged.
\(\square\)

The finite classification was independently enumerated using only exact
integer arithmetic in \(\mathbb F_3\).  The entropy expressions were then
simplified symbolically.  Here is the verbatim `python3` output:

```text
arithmetic = exact integers in F_3
lagrangian_planes = 40
product_planes = 16
entangled_planes = 24
all_histograms = [((1, 1, 1, 1, 1, 1, 1, 1, 1), 1), ((2, 2, 1, 1, 1, 1, 1), 18), ((2, 2, 2, 1, 1, 1), 9), ((3, 1, 1, 1, 1, 1, 1), 3), ((4, 2, 2, 1), 9)]
product_histograms = [((1, 1, 1, 1, 1, 1, 1, 1, 1), 1), ((2, 2, 2, 1, 1, 1), 6), ((4, 2, 2, 1), 9)]
entangled_histograms = [((2, 2, 1, 1, 1, 1, 1), 18), ((2, 2, 2, 1, 1, 1), 3), ((3, 1, 1, 1, 1, 1, 1), 3)]
target_histogram = (4, 2, 2, 1)
target_entropy = -4*log(2)/3 + 2*log(3)
gap (1, 1, 1, 1, 1, 1, 1, 1, 1) = 4*log(2)/3 status = strictly_positive
gap (2, 2, 1, 1, 1, 1, 1) = 8*log(2)/9 status = strictly_positive
gap (2, 2, 2, 1, 1, 1) = 2*log(2)/3 status = strictly_positive
gap (3, 1, 1, 1, 1, 1, 1) = -log(3)/3 + 4*log(2)/3 status = strictly_positive
gap (4, 2, 2, 1) = 0 status = equality
last_strict_gap_positive_reduces_to = 16 > 3
```

This eliminates all 360 two-qutrit stabilizer inputs, including all 216
entangled ones, from the extremal qutrit additivity search.  It does not extend
from stabilizer states to arbitrary two-qutrit pure states; the continuous
minimum in (202) remains **[UNPROVED]**.

### Dated formatting correction 2026-08-21

The header row of the array in (253) ends with the malformed single row
terminator ~~`\text{histogram}\`~~.  The corrected header is

\[
 \text{kind of }L&\text{number of planes}&\text{histogram}\\
\]

All six data rows, the classification, and its proof are unchanged.

## Round 2026-08-21: the noncommutative Fourier dual of the qutrit pair

The stabilizer calculation diagonalizes only a finite family of inputs.
There is a different diagonalization that applies to every input: regard the
channel itself as a Fourier multiplier on the qutrit Weyl basis.  This
representation exactly solves the maximal output collision norm, exposes the
precise failure of a collision-only entropy proof, and gives a cycle
generating function for the higher spectral data that remain.

The Fourier estimate used below is a specialization of a result whose proof
was actually opened in [Fukuda--Holevo, *On Weyl-covariant channels*,
Theorems 1--3](https://arxiv.org/html/quant-ph/0510148v3).  The needed
special case, including its ancillary extension, is reproved here.

For \(s\in\{1,-1\}\), retain the notation

\[
 \Phi_s(A)={A+ZAZ^*+X^sAX^{-s}\over3},\qquad
 W_{p,q}=X^pZ^q,\quad (p,q)\in\mathbb F_3^2,
\]

and put

\[
 L_s=\{(t,st):t\in\mathbb F_3\}.                             \tag{261}
\]

Let \(\mathcal D(A)=\operatorname {Tr}(A)I_3/3\), and let
\(\mathcal E_s\) be the Hilbert--Schmidt conditional expectation onto
\(\operatorname {span}\{W_{t,st}:t\in\mathbb F_3\}\).  This span is a
maximal abelian Weyl algebra.

### Lemma 53 (Fourier spectrum and collision semigroup)

With \(\omega=e^{2\pi i/3}\),

\[
 \Phi_s(W_{p,q})=\varphi_s(p,q)W_{p,q},\qquad
 \varphi_s(p,q)={1+\omega^p+\omega^{-sq}\over3}.             \tag{262}
\]

Its squared multiplier spectrum is

\[
 |\varphi_s(p,q)|^2=
 \begin{cases}
  1,&(p,q)=(0,0),\\
  0,&(p,q)\in L_s\setminus\{0\},\\
  1/3,&(p,q)\notin L_s.
 \end{cases}                                                 \tag{263}
\]

Consequently,

\[
 \Phi_s^*\Phi_s
 =\mathcal D+{1\over3}(\operatorname {Id}-\mathcal E_s).     \tag{264}
\]

**Proof.**  The Weyl commutation relation gives

\[
 ZW_{p,q}Z^*=\omega^pW_{p,q},\qquad
 X^sW_{p,q}X^{-s}=\omega^{-sq}W_{p,q},
\]

which proves (262).  If \((p,q)\ne(0,0)\), the three phases in
(262) either consist of all three cube roots of unity, in which case their
sum is zero, or have squared sum modulus \(3\).  They consist of all three
roots exactly when \(q=sp\ne0\).  This proves (263).

The maps in (264) are simultaneously diagonal in the Weyl basis.
On the identity, the right side has eigenvalue one.  On the two traceless
modes in \(L_s\), it has eigenvalue zero.  On the remaining six modes, it
has eigenvalue \(1/3\).  These are exactly the squared multipliers in
(263), proving (264). \(\square\)

The identity (264) is a spectral version of the collision calculation.  It
says that one application of \(\Phi_s^*\Phi_s\) deletes one maximal
commutative Fourier line, contracts its six-dimensional orthogonal
complement by \(1/3\), and leaves only the scalar mode fixed.

For a completely positive map \(\Omega\), write

\[
 \nu_2(\Omega)=\max_{\rho\ge0,\ \operatorname {Tr}\rho=1}
                         \|\Omega(\rho)\|_2.                  \tag{265}
\]

### Lemma 54 (exact ancillary collision norm)

For every finite-dimensional completely positive map \(\Omega\),

\[
 \nu_2(\Phi_s\otimes\Omega)
 ={ \sqrt5\over3}\,\nu_2(\Omega).                            \tag{266}
\]

In particular, the equality holds with an arbitrary ancillary output
dimension and does not require \(\Omega\) to be Weyl-covariant.

**Proof.**  First let \(Y\) be any operator on
\(\mathbb C^3\otimes\mathcal K\).  Expand it in the Weyl basis as

\[
 Y=\sum_{p,q}W_{p,q}\otimes A_{p,q}.
\]

Weyl orthogonality gives

\[
 \|Y\|_2^2=3\sum_{p,q}\|A_{p,q}\|_2^2,\qquad
 \|\operatorname {Tr}_{\mathbb C^3}Y\|_2^2=9\|A_{0,0}\|_2^2.
\]

Using (263) and bounding every nonidentity squared multiplier by \(1/3\)
therefore gives

\[
 \|(\Phi_s\otimes\operatorname {Id})(Y)\|_2^2
 \le {2\over9}\|\operatorname {Tr}_{\mathbb C^3}Y\|_2^2
{1\over3}\|Y\|_2^2.                                         \tag{267}
\]

We next prove the ancillary stability

\[
 \nu_2(\operatorname {Id}_{\mathcal R}\otimes\Omega)
 =\nu_2(\Omega).                                             \tag{268}
\]

The lower bound follows by adjoining a pure state.  For the upper bound it
suffices, by convexity of the squared Hilbert--Schmidt norm, to use a pure
input with Schmidt form

\[
 |\psi\rangle=\sum_i\sqrt{\lambda_i}\,|i\rangle|x_i\rangle.
\]

Put \(A_{ij}=\Omega(|x_i\rangle\langle x_j|)\).  Complete positivity
implies

\[
 \begin{pmatrix}A_{ii}&A_{ij}\\A_{ji}&A_{jj}\end{pmatrix}\ge0.
\]

Hence \(A_{ij}=A_{ii}^{1/2}K A_{jj}^{1/2}\) for a contraction \(K\)
on the relevant supports.  If \(a_r,c_t\) are the eigenvalues of
\(A_{ii},A_{jj}\), respectively, then

\[
 \begin{split}
 \|A_{ij}\|_2^2
 &=\sum_{r,t}a_rc_t|K_{rt}|^2\\
 &\le\left(\sum_ra_r^2\right)^{1/2}
       \left(\sum_tc_t^2\right)^{1/2}
 \le\nu_2(\Omega)^2.                                        \tag{269}
 \end{split}
\]

For the first inequality, the matrix \((|K_{rt}|^2)\) has every row and
column sum at most one; completing it to a doubly stochastic matrix,
then applying the rearrangement and Cauchy--Schwarz inequalities, proves
the displayed bound.  Orthogonality of the Schmidt matrix units now gives

\[
 \|(\operatorname {Id}\otimes\Omega)
       (|\psi\rangle\langle\psi|)\|_2^2
 =\sum_{i,j}\lambda_i\lambda_j\|A_{ij}\|_2^2
 \le\nu_2(\Omega)^2,
\]

which proves (268).

Apply (267) to
\(Y=(\operatorname {Id}\otimes\Omega)(\rho)\).  Then

\[
 \operatorname {Tr}_{\mathbb C^3}Y=\Omega(\rho_{\mathcal K}),
\]

so (265) and (268) bound both squared norms on the right of (267) by
\(\nu_2(\Omega)^2\).  Thus

\[
 \nu_2(\Phi_s\otimes\Omega)^2
 \le\left({2\over9}+{1\over3}\right)\nu_2(\Omega)^2
 ={5\over9}\nu_2(\Omega)^2.                                 \tag{270}
\]

On the basis input \(|0\rangle\), the first two orbit states under
\(I,Z,X^s\) coincide and the third is orthogonal.  Hence the output
spectrum is \((2/3,1/3,0)\), and
\(\nu_2(\Phi_s)^2=5/9\).  Tensoring this input with a maximizer for
\(\Omega\) gives equality in (270), proving (266). \(\square\)

### Proposition 55 (the collision dual is exact but entropy-incomplete)

For the extremal conjugate pair,

\[
 \max_\rho\operatorname {Tr}
 [(\Phi_1\otimes\Phi_{-1})(\rho)]^2={25\over81}.             \tag{271}
\]

Equivalently, its minimum output Rényi-2 entropy is additive:

\[
 S_{2,\min}(\Phi_1\otimes\Phi_{-1})
 =2\log{9\over5}
 =S_{2,\min}(\Phi_1)+S_{2,\min}(\Phi_{-1}).                 \tag{272}
\]

Nevertheless, trace and the sharp collision cap (271) alone can certify
only

\[
 S_{\min}(\Phi_1\otimes\Phi_{-1})
 \ge\mathsf H_9(25/81),                                     \tag{273}
\]

where, with

\[
 x={27+\sqrt {57}\over108},\qquad
 y={9-\sqrt {57}\over36},
\]

Lemma 20 gives

\[
 \mathsf H_9(25/81)=-3x\log x-y\log y
 <2h_2(2/3).                                                 \tag{274}
\]

Thus even the exact collision SDP leaves a strictly positive spectral
relaxation gap.

**Proof.**  Apply Lemma 54 with
\(\Omega=\Phi_{-1}\).  Since each single-channel squared norm is
\(5/9\), (266) gives (271).  Taking minus the logarithm proves (272).

For \(p=25/81\), Lemma 20 has
\(m=\lfloor1/p\rfloor=3\).  Substitution in (67) gives the values
\(x,y\) above and the abstract optimizing spectrum

\[
 (x,x,x,y,0,0,0,0,0).                                      \tag{275}
\]

On the other hand, the product of the two single-channel minimizing basis
inputs has output spectrum

\[
 (4/9,2/9,2/9,1/9,0,0,0,0,0),                              \tag{276}
\]

whose entropy is \(2h_2(2/3)\) and whose purity is also \(25/81\).
The equality characterization in Lemma 20 says that (275), up to
permutation, is the unique entropy minimizer at this collision cap.
The spectra (275) and (276) are distinct, so the inequality in (274) is
strict.  This proves every assertion. \(\square\)

The spectrum (275) is not asserted to be an output of the channel.  Its role
is dual: it proves that no argument retaining only normalization and the
sharp quadratic moment (271) can establish the desired entropy lower bound.
Additional channel-specific information must exclude (275) and nearby
spectra.

The Choi representation rules out one tempting way to obtain that additional
information.

### Proposition 56 (the extremal qutrit channel is NPT)

Let

\[
 J_s=(\Phi_s\otimes\operatorname {Id})
        (|\Omega_3\rangle\langle\Omega_3|)
\]

be the normalized Choi state.  Its partial transpose has characteristic
polynomial

\[
 \det(\lambda I_9-J_s^\Gamma)
 =\left(\lambda^3-{1\over3}\lambda^2+{1\over243}\right)^3.   \tag{277}
\]

In particular, \(J_s^\Gamma\) has three negative eigenvalues, and
\(\Phi_s\) is not measure-and-prepare.

**Proof.**  For \(s=1\), put \(U_1=I,U_2=Z,U_3=X\).  Since
\((|\Omega_3\rangle\langle\Omega_3|)^\Gamma=F/3\), where \(F\)
is the swap,

\[
 J_1^\Gamma={1\over9}\sum_{i=1}^3(U_i\otimes U_i^*)F.       \tag{278}
\]

In the standard product basis, (278) leaves invariant the three subspaces

\[
 \begin{split}
 &\operatorname {span}\{|00\rangle,|12\rangle,|21\rangle\},\\
 &\operatorname {span}\{|01\rangle,|22\rangle,|10\rangle\},\\
 &\operatorname {span}\{|02\rangle,|20\rangle,|11\rangle\}.
 \end{split}
\]

After diagonal phase changes and cyclic reordering inside the three
subspaces, every restriction is

\[
 B={1\over9}
 \begin{pmatrix}
 2&1&0\\
 1&0&-\omega\\
 0&-\overline\omega&1
 \end{pmatrix}.                                             \tag{279}
\]

A direct determinant expansion gives

\[
 \det(\lambda I_3-B)
 ={243\lambda^3-81\lambda^2+1\over243},
\]

which proves (277) for \(s=1\).  Replacing \(X\) by \(X^{-1}\)
permutes and conjugates the three blocks, so the same polynomial holds for
\(s=-1\).

The cubic numerator takes the values \(-1/3\) at \(\lambda=-1/9\)
and \(1\) at \(\lambda=0\), so it has a negative root.  Since the three
blocks have the same characteristic polynomial, that root has multiplicity
three in \(J_s^\Gamma\).  A measure-and-prepare channel has a separable
Choi state, and the partial transpose of every separable state is positive.
Thus \(\Phi_s\) is not measure-and-prepare. \(\square\)

Proposition 56 does not imply nonadditivity.  It says only that the
measure-and-prepare route used in Proposition 40 for the tetrahedral qubit
channel cannot be transferred to the qutrit Weyl triangle.

The full output spectrum has a compact generating representation.  Let

\[
 E=T_+\times T_-,\qquad
 K_{(a,b)}=W_a\otimes W_b,\quad (a,b)\in E,
\]

where the phase-space triangles are those in (251).

### Lemma 57 (Gram and cycle generating functions)

For a unit vector \(\psi\in\mathbb C^3\otimes\mathbb C^3\), define the
\(9\)-by-\(9\) positive Gram matrix

\[
 G_\psi(e,f)=\langle\psi,K_e^*K_f\psi\rangle,\qquad e,f\in E.
                                                                    \tag{280}
\]

The output

\[
 \sigma_\psi=(\Phi_1\otimes\Phi_{-1})
                  (|\psi\rangle\langle\psi|)
\]

and \(G_\psi/9\) have the same nonzero eigenvalues.  For every integer
\(m\ge1\),

\[
 \operatorname {Tr}\sigma_\psi^m
 ={1\over9^m}\sum_{e_1,\ldots,e_m\in E}
 \prod_{j=1}^m
 \langle\psi,K_{e_j}^*K_{e_{j+1}}\psi\rangle,
 \qquad e_{m+1}=e_1.                                        \tag{281}
\]

Consequently, for \(|z|<1\),

\[
 \det(I_9-z\sigma_\psi)
 =\exp\!\left[-\sum_{m=1}^\infty
                   {z^m\over m}\operatorname {Tr}\sigma_\psi^m\right].
                                                                    \tag{282}
\]

The first nine cycle sums in (281) determine the complete output spectrum.

**Proof.**  Let \(V_\psi:\mathbb C^9\to\mathbb C^9\) have columns
\(K_e\psi/3\).  Then

\[
 V_\psi V_\psi^*=\sigma_\psi,\qquad
 V_\psi^*V_\psi=G_\psi/9.
\]

The two products have the same nonzero eigenvalues, proving the first
assertion.  Expanding
\(\operatorname {Tr}(G_\psi/9)^m\) entry by entry gives exactly the
closed-cycle sum (281).  Finally,

\[
 \log\det(I-z\sigma_\psi)
 =\operatorname {Tr}\log(I-z\sigma_\psi)
 =-\sum_{m\ge1}{z^m\over m}\operatorname {Tr}\sigma_\psi^m,
\]

which proves (282).  Newton's identities express the nine elementary
symmetric functions of the eigenvalues in terms of the first nine power
sums, proving the last assertion. \(\square\)

For \(m=2\), Fourier orthogonality collapses (281) to the quadratic
multiplier problem solved in Proposition 55.  For a stabilizer input, every
factor in (281) is zero or a third root of unity, and grouping identical rays
recovers the coset spectra of Lemma 50.  For a general input, the cycles of
length at least three retain phase-sensitive products that are invisible to
the collision norm.  Equations (274) and (281) therefore isolate the next
necessary task: control these higher Weyl cycles strongly enough to exclude
entropy below (276).  Such a cycle inequality is **[UNPROVED]**.

All finite algebra in this round was checked with exact sympy arithmetic;
only the displayed entropy values are decimal evaluations.  Here is the
verbatim python3 output:

~~~text
s = 1 squared_multiplier_histogram = {'1': 1, '1/3': 6, '0': 2}
s = 1 zero_modes = [(1, 1), (2, 2)]
s = -1 squared_multiplier_histogram = {'1': 1, '1/3': 6, '0': 2}
s = -1 zero_modes = [(1, 2), (2, 1)]
partial_transpose_block_charpoly = (243*lambda**3 - 81*lambda**2 + 1)/243
full_partial_transpose_charpoly = (243*lambda**3 - 81*lambda**2 + 1)**3/14348907
cubic_at_-1/9 = -1/3
cubic_at_0 = 1
single_witness_spectrum = [2/3, 1/3, 0]
single_witness_purity = 5/9
product_witness_spectrum = [4/9, 2/9, 2/9, 1/9, 0, 0, 0, 0, 0]
product_witness_purity = 25/81
collision_optimizer_normalization = 1
collision_optimizer_purity = 25/81
H_9(25/81) = 1.2231980949951667873609609405401352442087902783577
2*h_2(2/3) = 1.2730283365896256369008476452341493185276476031652
spectral_relaxation_deficit = 0.049830241594458849539886704694014074318857324807473
~~~

### Proof supplement 2026-08-21

For completeness, the exact count of negative eigenvalues in Proposition 56
uses one further elementary observation.  If

\[
 f(\lambda)=243\lambda^3-81\lambda^2+1,
\]

then

\[
 f'(\lambda)=81\lambda(9\lambda-2)>0\qquad(\lambda<0).
\]

Thus \(f\) is strictly increasing on the negative half-line.  Together with
\(f(-1/9)<0<f(0)\), this proves that each block in (279) has exactly one
negative eigenvalue, not merely at least one.  The three blocks therefore
give exactly three negative eigenvalues as asserted.

### Dated numbering correction 2026-08-21

The immediately preceding round inadvertently reused the labels (261) and
(262), which already belong to the stabilizer entropy formulas above it.
All displayed equation labels and all parenthetical equation references
within the Fourier-dual round are therefore struck and replaced by the
following uniform translation:

\[
\begin{array}{c|ccccccccccc}
\text{old local label}&261&262&263&264&265&266&267&268&269&270&271\\
\text{corrected label}&283&284&285&286&287&288&289&290&291&292&293\\
\hline
\text{old local label}&272&273&274&275&276&277&278&279&280&281&282\\
\text{corrected label}&294&295&296&297&298&299&300&301&302&303&304
\end{array}
\]

For example, the Fourier multiplier formula is (284), the exact product
purity is (293), the Choi polynomial is (299), and the cycle determinant is
(304).  The pre-existing stabilizer equations (261)--(262) retain their
original labels.  No formula or proof is otherwise changed.

## Round 2026-08-21: counterexample search, failure of majorization, and a local entropy wall

The preceding round leaves a concrete continuous question: can an arbitrary
two-qutrit pure input make the entropy of

\[
 \Lambda:=\Phi_1\otimes\Phi_{-1}
\]

smaller than

\[
 H_*:=2h_2(2/3)
 =2\log3-{4\over3}\log2?                                    \tag{305}
\]

This round attacked that question by direct optimization over all complex
pure inputs and by testing the strongest obvious spectral certificate.  No
entropy counterexample was found.  Two exact obstructions explain why the
search is difficult: the product-minimizing spectrum does not majorize all
outputs, while the canonical product minimizer is protected against every
analytic perturbation by either a nonanalytic leakage term or a positive
quadratic term.

### Proposition 58 (the product spectrum is not a majorization bound)

Let

\[
 p_*={1\over9}(4,2,2,1,0,0,0,0,0),                          \tag{306}
\]

the output spectrum of \(\Lambda\) on \(|00\rangle\).  There is a
product input whose output has largest eigenvalue strictly greater than
\(4/9\).  Consequently \(p_*\) does not majorize every output spectrum
of \(\Lambda\), so Schur concavity applied to the fixed vector \(p_*\)
cannot prove the desired entropy lower bound.

**Proof.**  Put

\[
 \zeta=e^{\pi i/3},\qquad
 x={1\over\sqrt6}(1,\zeta,2\zeta)^T,\qquad
 \tau=\Phi_1(|x\rangle\langle x|).
\]

Direct multiplication gives

\[
 \tau=
 \begin{pmatrix}
 1/3&(1+i\sqrt3)/36&2/9\\
 (1-i\sqrt3)/36&1/6&(1-i\sqrt3)/12\\
 2/9&(1+i\sqrt3)/12&1/2
 \end{pmatrix}                                               \tag{307}
\]

and

\[
 \det(\lambda I_3-\tau)
 ={1944\lambda^3-1944\lambda^2+438\lambda-25\over1944},
 \qquad
 \det\!\left({2\over3}I_3-\tau\right)=-{7\over648}.       \tag{308}
\]

As \(\tau\) is a state, at most one of its eigenvalues can exceed
\(2/3\).  The negative determinant in (308) therefore implies
\(\lambda_{\max}(\tau)>2/3\).  The channels \(\Phi_1\) and
\(\Phi_{-1}\) are unitarily equivalent after conjugation, as shown in
Corollary 43.  Hence there is a pure input \(x_-\) for \(\Phi_{-1}\)
whose output has the same spectrum as \(\tau\).  On the product input
\(x\otimes x_-\), the largest output eigenvalue is

\[
 \lambda_{\max}(\tau)^2>{4\over9}.                           \tag{309}
\]

The first majorization inequality for \(p_*\) would require the reverse
inequality, so majorization fails.  This product input is not an entropy
counterexample: additivity on product inputs and Proposition 42 give

\[
 S(\Phi_1(|x\rangle\langle x|))
 +S(\Phi_{-1}(|x_-\rangle\langle x_-|))\ge H_*.
\]

Thus (309) exhibits spectral incomparability, not an additivity violation.
\(\square\)

The witness is also strictly inside the collision constraint:

\[
 \operatorname {Tr}\tau^2={89\over162}<{5\over9}.
\]

Therefore the failure of majorization is not caused by violating the sharp
purity bound in Proposition 55.

### Proposition 59 (directional entropy barrier at the product witness)

Let \(\psi_0=|00\rangle\).  Along every nonconstant analytic curve of
pure inputs issuing from \(\psi_0\), the entropy of the output of
\(\Lambda\) is strictly larger than \(H_*\) for all sufficiently small
nonzero values of the curve parameter.  More precisely, write the leading
part of such a curve as

\[
 \psi(t)={\psi_0+t\eta\over
              \sqrt{1+t^2\|\eta\|^2}}+O(t^2),\qquad
 \langle\psi_0,\eta\rangle=0.                               \tag{310}
\]

There is a two-dimensional exceptional tangent space

\[
 \mathcal T=\operatorname {span}\{|02\rangle,|10\rangle\}   \tag{311}
\]

with the following alternatives.

* If \(\eta\notin\mathcal T\), then for a number
  \(c(\eta)>0\),
  \[
  S(\Lambda(|\psi(t)\rangle\langle\psi(t)|))
  =H_*+2c(\eta)t^2\log{1\over|t|}+O(t^2).                   \tag{312}
  \]
* If \(\eta=a|02\rangle+b|10\rangle\), then
  \[
  S(\Lambda(|\psi(t)\rangle\langle\psi(t)|))
  =H_*+{\log2\over3}(|a|^2+|b|^2)t^2+o(t^2).               \tag{313}
  \]

**Proof.**  Order the nine random-unitary errors as

\[
 K_e\in\{I,Z,X\}\otimes\{I,Z,X^{-1}\},
\]

and let \(V_\psi\) be the \(9\)-by-\(9\) matrix whose columns are
\(K_e\psi/3\).  Then

\[
 \Lambda(|\psi\rangle\langle\psi|)=V_\psi V_\psi^*.
                                                                    \tag{314}
\]

At \(\psi_0\), the nine columns occupy the four rays

\[
 |00\rangle,\ |02\rangle,\ |10\rangle,\ |12\rangle
\]

with multiplicities \(4,2,2,1\).  Thus the four nonzero singular values
of \(V_{\psi_0}\) are

\[
 {2\over3},\quad {\sqrt2\over3},\quad
 {\sqrt2\over3},\quad {1\over3},                            \tag{315}
\]

and their squares give (306).

Let \(P\) project onto the orthogonal complement of the four output rays,
and let \(Q_0\) project onto \(\ker V_{\psi_0}\) in the coefficient
space.  Define the linear tangent-leakage map

\[
 \mathcal Q(\eta)=P V_\eta Q_0.                              \tag{316}
\]

A direct comparison of the four column groups gives

\[
 \ker\mathcal Q=\mathcal T.                                 \tag{317}
\]

Here is the coordinate verification of (317).  Within each group of errors
that sends \(\psi_0\) to the same ray, \(\ker V_{\psi_0}\) consists of
coefficient vectors whose entries sum to zero.  Hence
\(\mathcal Q(\eta)=0\) exactly when the projected vectors
\(PK_e\eta\) are equal inside each of the groups

\[
 \{I,Z\}\otimes\{I,Z\},\qquad
 \{I,Z\}\otimes\{X^{-1}\},\qquad
 \{X\}\otimes\{I,Z\}.                                    \tag{318}
\]

Writing \(\eta=\sum_{(j,k)\ne(0,0)}\eta_{jk}|jk\rangle\),
the first group in (318) eliminates all projected coefficients on which
either diagonal phase is nontrivial.  Comparing the remaining coefficients
in the second and third groups eliminates every term except
\(\eta_{02}|02\rangle\) and \(\eta_{10}|10\rangle\).
Conversely those two terms give equal projected columns in every group in
(318).  This proves (317).  As an independent check, in the ordered tangent
basis \(|01\rangle,\ldots,|22\rangle\) with \(|00\rangle\) omitted,
direct multiplication gives

\[
 \operatorname {spec}(\mathcal Q^*\mathcal Q)
 =\left\{{3\over4},{7\over12},{7\over12},
          {1\over2},{1\over2},{1\over3},0,0\right\}.        \tag{319}
\]

Use the range and kernel decompositions of \(V_{\psi_0}\) to write
\(V_{\psi(t)}\) as a \(2\)-by-\(2\) block matrix.  Elementary block
elimination shows that its singular values issuing from zero are

\[
 |t|s_j(\mathcal Q(\eta))+O(t^2),                            \tag{320}
\]

where \(s_j\) are the singular values.  The corresponding output
eigenvalues are therefore
\(t^2s_j(\mathcal Q(\eta))^2+O(t^3)\).  The first variation of the
four old eigenvalues makes no entropy contribution.  Indeed, the diagonal
entries of the first output variation in each of the four ray spaces are
zero because

\[
 \langle K_e\psi_0,K_e\eta\rangle
 =\langle\psi_0,\eta\rangle=0,
\]

and the trace of the first variation on the degenerate \(2/9\)-eigenspace
is zero for the same reason.  The old spectral contribution is consequently
\(H_*+O(t^2)\).  Applying \(-u\log u\) to the new eigenvalues in (320)
proves (312), with

\[
 c(\eta)=\|\mathcal Q(\eta)\|_2^2>0.                         \tag{321}
\]

It remains to handle the kernel (311).  Put
\(\eta=a|02\rangle+b|10\rangle\).  Substitution of the nine columns in
(314), followed by expansion of the four eigenvalues that are nonzero at
\(t=0\), gives a Hermitian quadratic coefficient in \((a,b)\).  On the
four test pairs \((1,0),(0,1),(1,1),(1,i)\), its values are respectively

\[
 {\log2\over3},\quad {\log2\over3},\quad
 {2\log2\over3},\quad {2\log2\over3}.                      \tag{322}
\]

Polarization of the Hermitian quadratic form in (322) removes both mixed
terms and yields exactly the coefficient in (313).  For example, on either
coordinate axis the relevant varying one-qutrit output has two large
eigenvalues

\[
 {2\over3}-{t^2\over3}+O(t^4),\qquad
 {1\over3}+{t^2\over3}+O(t^4),                              \tag{323}
\]

and its remaining eigenvalue is \(O(t^4)\), which gives the first two
values in (322).  Direct multiplication for \((1,1)\) and \((1,i)\)
gives the last two.  The eigenvalues issuing from zero contribute only
\(O(t^4\log(1/|t|))=o(t^2)\).  This proves (313).

Both leading corrections are positive.  If an analytic curve first leaves
\(\psi_0\) at order \(t^r\) rather than order \(t\), the same argument
applies with \(t\) replaced by \(t^r\).  Hence no nonconstant analytic
curve supplies a local entropy descent. \(\square\)

The same calculation applies to the computational-basis product witnesses
obtained from \(|00\rangle\) by the discrete Weyl symmetries.  Proposition
59 is deliberately local; it does not claim that all global product
minimizers have been classified.

### Numerical falsification attempt over the full pure-state space

The objective was optimized directly over the real and imaginary parts of a
normalized vector in \(\mathbb C^9\).  The starts consisted of the nine
computational basis vectors, one maximally entangled vector, and 120 complex
Gaussian vectors.  This is a finite search and is not a proof of the global
minimum.  Of the 130 runs, 129 converged numerically to the product value;
the remaining run reached a higher stationary value.  Every best input had
Schmidt rank one to numerical precision.

The following is verbatim `python3` output.  Exact `sympy` arithmetic was
used for (307)--(308); the leakage spectrum and optimization used
double-precision `numpy`/`scipy` arithmetic.

```text
exact_witness_output = Matrix([[1/3, 1/36 + sqrt(3)*I/36, 2/9], [1/36 - sqrt(3)*I/36, 1/6, 1/12 - sqrt(3)*I/12], [2/9, 1/12 + sqrt(3)*I/12, 1/2]])
characteristic_polynomial = (1944*lambda**3 - 1944*lambda**2 + 438*lambda - 25)/1944
det((2/3)I-output) = -7/648
purity = 89/162
V_|00>_singular_values = [0.666666666667, 0.471404520791, 0.471404520791, 0.333333333333, 0.0, 0.0, 0.0, 0.0, 0.0]
Q_shape = (25, 8) Q_rank = 6
Q_singular_values_squared = [0.75, 0.583333333333, 0.583333333333, 0.5, 0.5, 0.333333333333, 0.0, 0.0]
Q_zero_coordinate_directions = [2, 3]
optimizer = scipy_L-BFGS-B random_seed = 20260821
starts = 130
product_target = 1.273028336589626
best_entropy = 1.273028336589626 best_minus_target = 0.000e+00
local_entropy_histogram_rounded_1e-10 = [(1.2730283366, 122), (1.2730283367, 4), (1.2730283368, 1), (1.2730283369, 2), (1.735126457, 1)]
best_output_spectrum = [0.444444444444, 0.222222222222, 0.222222222222, 0.111111111111, 0.0, 0.0, 0.0, -0.0, -0.0]
best_input_Schmidt_spectrum = [1.0, 0.0, 0.0]
```

The counterexample is therefore blocked in three precise ways.  Product
inputs cannot work by the one-channel minimum, and Proposition 59 prevents
an infinitesimal analytic escape from the canonical product witness.
Collision entropy cannot settle the question because the abstract spectrum
in (297) has entropy below (305), while fixed-spectrum majorization cannot
settle it because Proposition 58 gives an exact violation of its first
partial-sum inequality.  Any counterexample must consequently be a genuinely
nonlocal entangled input, separated from the canonical product basin, whose
higher Weyl cycle sums in (303) realize a low-entropy spectrum despite the
sharp purity cap (293).  The numerical search did not find such an input,
but no inequality currently excludes it **[UNPROVED]**.

## Round 2026-08-21: exact near-one norm reduction for the qutrit pair

The unresolved minimum in (202) can be reduced to a single scalar
maximal-output-norm asymptotic.  The relevant external result is the
Amosov--Holevo near-(p=1) multiplicativity criterion: multiplicativity for
parameters arbitrarily close to (1) implies minimum-output-entropy
additivity.  The source actually opened was
[Amosov--Holevo, *On the multiplicativity hypothesis for quantum
communication channels*](https://www.mathnet.ru/eng/tvp3068).  The
finite-dimensional fixed-pair form needed here is proved below, so that the
reduction includes the exact normalization and does not rely on a global
additivity conjecture.

For (p>1), write

\[
 \nu_p(\Omega)=\max_{\rho\ge0,\ \operatorname {Tr}\rho=1}
                         \|\Omega(\rho)\|_p.                 \tag{324}
\]

### Lemma 60 (the exact one-channel norm curve)

For (s\in\{1,-1\}) and (1<p\le2),

\[
 \nu_p(\Phi_s)^p=\left({2\over3}\right)^p
                         +\left({1\over3}\right)^p.         \tag{325}
\]

**Proof.**  Lemma 54, with a one-dimensional ancillary map, gives

\[
 \operatorname {Tr}\Phi_s(\rho)^2\le {5\over9}             \tag{326}
\]

for every state.  It remains to solve a three-variable scalar problem.  Fix
(1<p<2), and maximize
(f_p(\lambda)=\sum_{j=1}^3\lambda_j^p) subject to

\[
 \lambda_j\ge0,\qquad \sum_j\lambda_j=1,\qquad
 \sum_j\lambda_j^2\le {5\over9}.
\]

If exactly two coordinates are positive, write them as (x,1-x).  The
collision constraint says (1/3\le x\le2/3).  Strict convexity and symmetry
of (x^p+(1-x)^p) put its maximum at an endpoint, giving
((2/3,1/3,0)) up to permutation.

Suppose instead that a maximizer has three positive coordinates.  If the
collision constraint were inactive, the multiplier equation for normalization
would make all three coordinates equal; strict convexity and the feasible
nonuniform vector ((2/3,1/3,0)) exclude that point as a maximum.  Thus the
collision constraint is active.  Its gradient is independent of the
normalization gradient away from the uniform vector, so Lagrange multipliers
give

\[
 p\lambda_j^{p-1}=\alpha+2\beta\lambda_j.                   \tag{327}
\]

The left side minus (2\beta\lambda_j) has strictly decreasing derivative,
and hence a horizontal line meets it in at most two positive points.  Solving
normalization and collision for a nonuniform three-coordinate vector leaves,
up to permutation, only

\[
 (a,b,b),\qquad
 a={3+2\sqrt3\over9},\qquad b={3-\sqrt3\over9}.             \tag{328}
\]

This stationary point is not a local maximum.  Indeed, the tangent vector
(v=(0,1,-1)) annihilates the first variations of both constraints.  Subtracting
(327) at (a) and (b) gives

\[
 2\beta=p\,{a^{p-1}-b^{p-1}\over a-b}.
\]

Since (t\mapsto t^{p-1}) is strictly concave, its secant slope on
([b,a]) is smaller than its derivative at (b).  Therefore the second
variation of the Lagrangian in direction (v) is

\[
 2\left[p(p-1)b^{p-2}-2\beta\right]>0,                      \tag{329}
\]

contrary to the second-order necessary condition for a constrained local
maximum.  Hence the boundary vector is the global maximizer.  At (p=2),
the objective is the collision constraint itself.  Finally, the input
(|0\rangle) gives output spectrum ((2/3,1/3,0)) for either sign (s),
so every bound is attained.  This proves (325). \(\square\)

### Proposition 61 (Amosov--Holevo right-derivative identity)

For any two finite-dimensional channels \(\Omega_1,\Omega_2\),

\[
 \Delta(\Omega_1,\Omega_2)
 =\lim_{p\downarrow1}{1\over p-1}
 \log {\nu_p(\Omega_1\otimes\Omega_2)
              \over\nu_p(\Omega_1)\nu_p(\Omega_2)}.        \tag{330}
\]

In particular, if maximal output (p)-norm multiplicativity holds for a
sequence (p_j\downarrow1), then minimum output entropy is additive for that
pair.

**Proof.**  For a density matrix \(\sigma\), put

\[
 g_\sigma(p)=\log\|\sigma\|_p
 ={1\over p}\log\operatorname {Tr}\sigma^p.
\]

With (0\log0=0), direct differentiation gives

\[
 g_\sigma(1)=0,\qquad g_\sigma'(1)=
 \operatorname {Tr}(\sigma\log\sigma)=-S(\sigma).          \tag{331}
\]

In fixed finite dimension this expansion is uniform over all density
matrices: the scalar functions (t\log t) and (t(\log t)^2), extended by
zero at (t=0), are bounded on ([0,1]).  Since every candidate in the
maximum defining \(\nu_p(\Omega)\) has the common value zero at (p=1),
the uniform expansion yields

\[
 \left.{d\over dp}\log\nu_p(\Omega)\right|_{p=1+}
 =\max_\rho[-S(\Omega(\rho))]=-S_{\min}(\Omega).            \tag{332}
\]

Apply (332) to the two channels and their product and subtract.  This proves
(330).  Product maximizing inputs also show that the ratio inside (330) is
at least one.  If that ratio equals one along (p_j\downarrow1), the existing
right derivative in (330) must vanish, proving the last assertion. \(\square\)

### Corollary 62 (one explicit scalar condition for (202))

Put

\[
 q_p=\left[\left({2\over3}\right)^p
             +\left({1\over3}\right)^p\right]^{1/p},\qquad
 R(p)={\nu_p(\Phi_1\otimes\Phi_{-1})\over q_p^2}.           \tag{333}
\]

Then (R(p)\ge1) and

\[
 2h_2(2/3)-S_{\min}(\Phi_1\otimes\Phi_{-1})
 =\lim_{p\downarrow1}{\log R(p)\over p-1}.                 \tag{334}
\]

Consequently the unresolved equality in (202) is equivalent to the
first-order multiplicativity statement

\[
 \log\nu_p(\Phi_1\otimes\Phi_{-1})
 ={2\over p}\log\left[\left({2\over3}\right)^p
             +\left({1\over3}\right)^p\right]+o(p-1)
 \quad(p\downarrow1).                                      \tag{335}
\]

It is sufficient, by the Amosov--Holevo criterion, to prove the stronger
equality (R(p_j)=1) for any sequence (p_j\downarrow1).  Proposition 55
gives only the isolated equality (R(2)=1), which does not imply (335).
Thus the load-bearing qutrit lemma is now reduced exactly to (335); that
near-one norm estimate remains **[UNPROVED]**.

**Proof.**  Lemma 60 identifies both one-channel norms in Proposition 61
with (q_p).  Substitution in (330) gives (334), and the equivalence with
(335) is immediate.  The product input (|00\rangle) proves (R(p)\ge1).
\(\square\)

The scalar optimization in Lemma 60 and representative values of the
explicit norm curve were checked with `python3` using exact `sympy`
arithmetic before decimal rendering.  The output is verbatim:

```text
stationary_sum = 1
stationary_purity = 5/9
boundary_sum = 1
boundary_purity = 5/9
p = 3/2 boundary_power_sum = 0.73678114368169260999133494343529501676385557945819
p = 3/2 interior_power_sum = 0.71445267482207438878456296402067314439476398531121
boundary_minus_interior = 0.022328468859618221206771979414621872369091594146978
strictly_positive = True
p = 1.1 single_candidate_norm = 0.94423196325873230858491242886739763 product_candidate_norm = 0.89157400043944000032024963729079982
p = 1.5 single_candidate_norm = 0.81575360492382516340496346900893274 product_candidate_norm = 0.66545394394621622988042865520496583
p = 1.9 single_candidate_norm = 0.75539102901144337244361181405195026 product_candidate_norm = 0.57061560671096728277095129615940194
```

This reduction also identifies the missing scale: collision multiplicativity
controls one point of the norm curve, whereas von Neumann additivity is its
right-hand slope at (p=1).  A proof of (335) may therefore use estimates
that lose equality at every fixed (p>1), provided the logarithmic loss is
(o(p-1)).

### Dated formatting correction 2026-08-21

The inline TeX delimiters in the immediately preceding round were stripped
during transcription.  Every plain-parenthesis mathematical expression in
that round is inline mathematics.  In particular,

\[
 \begin{gathered}
 p=1,\quad 1,\quad p>1,\quad s\in\{1,-1\},\quad 1<p\le2,\quad
 1<p<2,\quad f_p(\lambda)=\sum_{j=1}^3\lambda_j^p,\\
 x,\quad 1-x,\quad 1/3\le x\le2/3,\quad x^p+(1-x)^p,\quad
 (2/3,1/3,0),\quad 2\beta\lambda_j,\quad
 v=(0,1,-1),\\
 a,\quad b,\quad t\mapsto t^{p-1},\quad [b,a],\quad p=2,\quad
 |0\rangle,\quad \Omega_1,\Omega_2,\quad p_j\downarrow1,\\
 0\log0=0,\quad t\log t,\quad t(\log t)^2,\quad t=0,\quad
 [0,1],\quad R(p)\ge1,\quad R(2)=1,\quad
 R(p_j)=1,\quad q_p,\quad |00\rangle,\quad o(p-1).
 \end{gathered}
\]

The phrases “near-(p=1),” “maximal output (p)-norm,” and
“right-hand slope at (p=1)” mean, respectively, near-\(p=1\), maximal
output \(p\)-norm, and right-hand slope at \(p=1\).  Equations
(324)--(335), their proofs, the cited reduction, and the computational
output are unchanged.

## Round 2026-08-21: exact minimizer census and cyclic-diagonal exclusion

The numerical search in Proposition 59 repeatedly returned many different
product inputs with the same entropy, but the one-channel minimizing set had
not been classified.  Exhaustive solution of the small algebraic system
reveals two packets of nine rays.  Diagonalizing the one Weyl operator omitted
by the triangle turns that computation into a proof.  A second computation
reveals a three-block decomposition on the maximally correlated two-qutrit
subspace.  Entropy submodularity and a sharp four-Weyl collision estimate then
exclude that entire continuous subspace, and its two cyclic translates, from
the additivity search.

Retain

\[
 \Phi_s(A)={A+ZAZ^*+X^sAX^{-s}\over3},\qquad s\in\{1,-1\},
\]

and let \([x]\) denote the projective ray generated by a nonzero vector
\(x\).

### Proposition 63 (the eighteen one-channel minimizing rays)

Put \(\xi=e^{2\pi i/9}\), and define the unitary

\[
 C={1\over\sqrt3}
 \begin{pmatrix}
 1&\omega&\omega^2\\
 1&1&1\\
 \omega&1&\omega^2
 \end{pmatrix}.
\]

The complete projective minimizing set of \(\Phi_1\) is

\[
 \begin{split}
 \mathcal M_+=\biggl\{\left[{C(1,\xi^r,\xi^t)^T\over\sqrt3}\right]:
 (r,t)\in E_0\cup E_1\biggr\},\qquad\qquad\\
 E_0=\{0,3,6\}^2,\qquad
 E_1=\{1,4,7\}\mathbin\times\{2,5,8\}.                  \tag{336}
 \end{split}
\]

Thus \(|\mathcal M_+|=18\).  If \(Pe_j=e_{-j\pmod3}\), the complete
minimizing set of \(\Phi_{-1}\) is

\[
 \mathcal M_-={[P\overline x]:[x]\in\mathcal M_+\},       \tag{337}
\]

and also has eighteen rays.  The nine rays indexed by \(E_0\) are the
stabilizer eigenstates on the three Weyl lines used by the channel.  On the
nine rays indexed by \(E_1\), the three selected squared Weyl expectations
are all \(1/3\).

**Proof.**  It suffices first to treat \(s=1\).  For a unit vector \(x\),
write \(\rho_x=|x\rangle\langle x|\).  The pure-state mixture formula and
Weyl Parseval identity (199) give

\[
 \begin{split}
 \operatorname {Tr}\Phi_1(\rho_x)^2
 &= {1\over3}+{2\over9}\left(
 |\langle x,Zx\rangle|^2+|\langle x,Xx\rangle|^2
 +|\langle x,XZ^{-1}x\rangle|^2\right)\\
 &= {5\over9}-{2\over9}|\langle x,XZx\rangle|^2.           \tag{338}
 \end{split}
\]

Indeed, one representative from each of the four nonzero projective Weyl
lines has squared expectation summing to one.  The first line in (338) uses
three of those lines, and \(XZ\) represents the omitted one.

Proposition 42 gives \(S_{\min}(\Phi_1)=h_2(2/3)\).  Lemma 20, at output
dimension three and collision cap \(5/9\), says that the unique minimizing
spectrum under that cap is

\[
 (2/3,1/3,0).                                                \tag{339}
\]

Consequently \([x]\) minimizes exactly when equality holds in (338) and the
three orbit vectors \(x,Zx,Xx\) are linearly dependent.  Equivalently,

\[
 \langle x,XZx\rangle=0,qquad
 \det[x,Zx,Xx]=0.                                           \tag{340}
\]

The converse is included here: the first condition gives purity \(5/9\),
and the second gives rank at most two; trace one then forces the spectrum
(339).

Direct multiplication gives

\[
 C^*C=I,qquad C^*XZC=Z,qquad C^*ZC=\omega X^{-1},qquad
 C^*XC=XZ.                                                   \tag{341}
\]

Put \(x=Cy\).  The first condition in (340) becomes
\(\langle y,Zy\rangle=0\).  Since the three numbers \(|y_j|^2\) are
nonnegative and

\[
 |y_0|^2+\omega|y_1|^2+\omega^2|y_2|^2=0,
\]

they are equal.  After normalization and removal of a global phase,

\[
 y={1\over\sqrt3}(1,u,v)^T,qquad |u|=|v|=1.                \tag{342}
\]

Using (341), the determinant condition in (340) is, up to a nonzero scalar,

\[
 \det[(1,u,v)^T,X^{-1}(1,u,v)^T,XZ(1,u,v)^T]
 =-1-\omega u^3-\omega^2v^3=0.                              \tag{343}
\]

Three unit complex numbers having zero sum must be the three cube roots of
unity.  To see this directly, if \(1+a+b=0\) and \(|a|=|b|=1\), then
\(|1+a|=1\), so \(\operatorname {Re}a=-1/2\); hence
\(a\in\{\omega,\omega^2\}\), and \(b\) is the other root.  Applied to
(343), this leaves exactly the two alternatives

\[
 (u^3,v^3)=(1,1),\qquad (u^3,v^3)=(\omega,\omega^2).        \tag{344}
\]

The first alternative gives the nine exponent pairs in \(E_0\), and the
second gives the nine pairs in \(E_1\).  They are distinct rays because the
first coordinate in (342) has been fixed.  This proves (336).  Substitution
in the three selected Weyl expectations gives, respectively, the squared
patterns \((1,0,0)\) up to permutation and \((1/3,1/3,1/3)\), proving the
last assertion.

Finally, Corollary 43 gives

\[
 \Phi_{-1}(A)=P\,\overline{\Phi_1}(PAP)\,P.
\]

Complex conjugation carries a minimizing input of \(\Phi_1\) to one of
\(\overline{\Phi_1}\), and the two conjugations by \(P\) preserve spectra.
This proves (337). \(\square\)

### Corollary 64 (all product minimizers are now explicit)

Among pure product inputs to \(\Phi_1\otimes\Phi_{-1}\), the entropy equals
\(2h_2(2/3)\) exactly on

\[
 \{[x\otimes y]:[x]\in\mathcal M_+, [y]\in\mathcal M_-\}. \tag{345}
\]

There are exactly \(18^2=324\) such product rays.

**Proof.**  On a product input the output is a tensor product, so its entropy
is the sum of the two one-channel output entropies.  Proposition 42 bounds
each summand below by \(h_2(2/3)\), and Proposition 63 characterizes equality
in each summand.  Distinct pairs of projective factors give distinct product
rays. \(\square\)

The next entropy inequality is useful for a continuous entangled sector.
For a unitary \(U\), write

\[
 \mathcal B_U(A)={A+UAU^*\over2}.                            \tag{346}
\]

### Lemma 65 (binary Weyl submodularity and its sharp entropy floor)

If the conjugation actions of two unitaries \(U,V\) commute, then every state
\(\tau\) satisfies

\[
 S(\mathcal B_U(\tau))+S(\mathcal B_V(\tau))
 \ge S(\tau)+S(\mathcal B_U\mathcal B_V(\tau)).             \tag{347}
\]

For the qutrit Weyl pair, the channel

\[
 \Theta=\mathcal B_Z\mathcal B_{X^{-1}}                    \tag{348}
\]

has

\[
 S_{\min}(\Theta)=\log2.                                   \tag{349}
\]

**Proof.**  Introduce two classical bits and the classical-quantum state

\[
 \Gamma_{ABQ}={1\over4}\sum_{r,t=0}^1
 |r,t\rangle\langle r,t|\otimes
 U^rV^t\tau V^{-t}U^{-r}.
\]

Commutation of the conjugation actions gives

\[
 \begin{array}{ll}
 S(AQ)=\log2+S(\mathcal B_V(\tau)),&
 S(BQ)=\log2+S(\mathcal B_U(\tau)),\\
 S(Q)=S(\mathcal B_U\mathcal B_V(\tau)),&
 S(ABQ)=\log4+S(\tau).
 \end{array}
\]

Strong subadditivity in the form
\(S(AQ)+S(BQ)\ge S(Q)+S(ABQ)\) proves (347).

For (349), diagonalize \(\Theta\) on the Weyl basis.  Its multiplier at
\(W_{p,q}=X^pZ^q\) has squared modulus

\[
 \left|{(1+\omega^p)(1+\omega^q)\over4}\right|^2.
\]

This is one at \((p,q)=(0,0)\), is \(1/4\) on the four nonzero coordinate
axes, and is \(1/16\) at the remaining four indices.  If
\(r_{p,q}=\operatorname {Tr}(W_{p,q}^*\tau)\), Weyl Parseval gives

\[
 \sum_{(p,q)\ne(0,0)}|r_{p,q}|^2
 =3\operatorname {Tr}\tau^2-1\le2.
\]

It follows that

\[
 \operatorname {Tr}\Theta(\tau)^2
 \le {1\over3}\left(1+{1\over4}\cdot2\right)={1\over2}.
\]

Hence \(S(\Theta(\tau))\ge-\log\operatorname {Tr}\Theta(\tau)^2
\ge\log2\).  On \(|0\rangle\), the two \(Z\)-conjugates coincide and
the \(X^{-1}\)-conjugate is orthogonal, so the output spectrum is
\((1/2,1/2,0)\).  This proves equality in (349). \(\square\)

### Proposition 66 (no violation on the three cyclic-diagonal planes)

For \(r\in\mathbb F_3\), define

\[
 \mathcal H_r=\operatorname {span}\{|j+r,j\rangle:j\in\mathbb F_3\}
 \subset\mathbb C^3\otimes\mathbb C^3.
\]

Every unit vector \(\psi\in\mathcal H_0\cup\mathcal H_1\cup\mathcal H_2\)
satisfies

\[
 S((\Phi_1\otimes\Phi_{-1})(|\psi\rangle\langle\psi|))
 \ge2h_2(2/3).                                               \tag{350}
\]

Equality holds inside these three planes exactly on the nine computational
product rays \([|j+r,j\rangle]\).

**Proof.**  Weyl covariance of both channel factors makes the three planes
unitarily equivalent for output spectra, so it is enough to use

\[
 \psi_a=\sum_{j=0}^2a_j|j,j\rangle,qquad \|a\|=1.
\]

Put \(\rho_a=|a\rangle\langle a|\) and
\(\sigma_a=\mathcal B_Z(\rho_a)\).  Grouping the nine random-unitary
errors according to the difference of the two output coordinates gives three
orthogonal blocks.  Under the natural identifications of those blocks with
\(\mathbb C^3\), the exact decomposition is

\[
 (\Phi_1\otimes\Phi_{-1})(|\psi_a\rangle\langle\psi_a|)
 \simeq {4\over9}\mathcal B_Z(\sigma_a)
 \oplus {4\over9}\mathcal B_{X^{-1}}(\sigma_a)
 \oplus {1\over9}X^{-1}\rho_aX.                             \tag{351}
\]

Indeed, the four errors with no shift give coefficient vectors
\(a,Za,Za,Z^2a\); the four errors with exactly one shift give
\(a,Za,X^{-1}a,X^{-1}Za\); and the error with both shifts gives one pure
vector in the remaining block.  This proves (351), including the block
weights \((4/9,4/9,1/9)\).

The entropy of a block-diagonal state is the Shannon entropy of its block
weights plus the weighted internal entropies.  Lemma 65 therefore gives

\[
 \begin{split}
 S((\Phi_1\otimes\Phi_{-1})(|\psi_a\rangle\langle\psi_a|))
 &=H(4/9,4/9,1/9)\\
 &\quad+{4\over9}\left[S(\mathcal B_Z(\sigma_a))
               +S(\mathcal B_{X^{-1}}(\sigma_a))\right]\\
 &\ge H(4/9,4/9,1/9)
       +{4\over9}\left[S(\sigma_a)+S(\Theta(\sigma_a))\right]\\
 &\ge 2\log3-{16\over9}\log2+{4\over9}\log2\\
 &=2\log3-{4\over3}\log2=2h_2(2/3),                       \tag{352}
 \end{split}
\]

which proves (350).  Equality in (352) forces \(S(\sigma_a)=0\).  The
average
\(\sigma_a=(\rho_a+Z\rho_aZ^*)/2\) is pure only when \(a\) is a
\(Z\)-eigenvector, hence a computational basis vector.  Conversely, each
such vector gives output spectrum
\((4/9,2/9,2/9,1/9,0,0,0,0,0)\), so equality holds.  Weyl covariance
transports these three rays to the asserted nine rays in the three planes.
\(\square\)

The symbolic diagonalization, the eighteen-ray census, and the block formula
were checked independently.  The lattice search used every nonzero vector in
\((\{0,\pm1,\pm i,\pm1\pm i\})^3\); it is only a finite falsification test
for (350), whose proof is (347)--(352).  Here is the verbatim `python3`
output:

```text
symbolic_C_identities = [True, True, True, True]
orbit_determinant = -I*(sqrt(3)*u**3 + I*u**3 - sqrt(3)*v**3 + I*v**3 - 2*I)/2
equivalent_zero_condition = 1 + omega*u^3 + omega^2*v^3 = 0
phase_exponent_branches = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)] [(1, 2), (1, 5), (1, 8), (4, 2), (4, 5), (4, 8), (7, 2), (7, 5), (7, 8)]
branch_sizes_total_product_pairs = 9 9 18 324
output_spectrum_histogram = {(0.0, 0.333333333333, 0.666666666667): 18}
selected_overlap_histogram = {(0.0, 0.0, 1.0): 9, (0.333333333333, 0.333333333333, 0.333333333333): 9}
largest_omitted_overlap_squared = 2.914e-31
max_block_reconstruction_error_1000_random = 1.441e-16
last_block_traces = [0.444444444444, 0.444444444444, 0.111111111111]
gaussian_integer_grid_vectors_min_target_hits = 728 1.273028336589626 1.273028336589626 24
Theta_squared_multiplier_histogram = {1.0: 1, 0.25: 4, 0.0625: 4}
basis_output_spectrum = [0.444444444444, 0.222222222222, 0.222222222222, 0.111111111111, 0.0, 0.0, 0.0, 0.0, 0.0]
```

The product basin left implicit after Proposition 59 is therefore finite and
explicit: it consists of 324 rays.  Beyond those product rays, (350) removes
three projective two-dimensional families of entangled inputs.  The remaining
possibility in (202) must lie outside all cyclic-diagonal planes and outside
the product set (345); whether such an input lowers the entropy remains
**[UNPROVED]**.

## Round 2026-08-21: a real blow-up makes the local entropy wall uniform

Proposition 59 excludes every analytic descent curve through the canonical
product witness, but a direction-by-direction assertion does not by itself
give one neighborhood on which all directions are controlled simultaneously.
This round imports the real blow-up viewpoint from geometric singular
perturbation theory: a singular point is replaced by its sphere of directions,
and a second chart resolves the directions on which the leading term
degenerates.  The source actually opened for this construction was
[Jardón-Kojakhmetov--Kuehn, *A survey on the blow-up method for fast-slow
systems*, Section 2.1](https://arxiv.org/html/1901.01402v5).  No dynamical
systems theorem from that source is assumed; the two charts and all estimates
needed here are proved below.

Retain

\[
 \Lambda=\Phi_1\otimes\Phi_{-1},\qquad
 F(\psi)=S(\Lambda(|\psi\rangle\langle\psi|)),\qquad
 \psi_0=|00\rangle,
\]

and let (H_*) be as in (305).  A projective neighborhood of
([\psi_0]) has the affine chart

\[
 \psi(\delta)={\psi_0+\delta\over\sqrt{1+\|\delta\|^2}},
 \qquad \langle\psi_0,\delta\rangle=0.                      \tag{353}
\]

The first real blow-up is the polar substitution
(\delta=r\vartheta), where (r\ge0) and (\|\vartheta\|=1).
The exceptional divisor (r=0) is the tangent sphere.  Proposition 59
shows that its only degenerate directions form the complex plane

\[
 \mathcal T=\operatorname {span}\{|02\rangle,|10\rangle\}.  \tag{354}
\]

The transition chart near this exceptional plane is the orthogonal splitting

\[
 \delta=t+u,\qquad t\in\mathcal T,\quad
 u\in\mathcal T^\perp,\quad r=\|\delta\|.                    \tag{355}
\]

### Proposition 67 (the canonical product witnesses are strict local minima)

There is an open projective neighborhood (mathcal U) of ([|00\rangle])
such that

\[
 F(\psi)>H_*\qquad
 ([\psi]\in\mathcal U,\ [\psi]\ne[|00\rangle]).           \tag{356}
\]

By Weyl covariance, the same assertion holds at each of the nine
computational product rays ([|j,k\rangle]).  Consequently, an entropy
counterexample to (202), if one exists, stays a positive projective distance
from each of these nine rays.

**Proof.**  Use the nine-column matrix (V_\psi) in (314).  At
(\psi_0), let (P_+) project onto the four-dimensional range of
(V_{\psi_0}), put (P_-=I-P_+), and let (Q_0) project onto
(\ker V_{\psi_0}).  The tangent-leakage map is

\[
 \mathcal Q(\delta)=P_-V_\delta Q_0.                         \tag{357}
\]

Equations (317) and (319) give, with the splitting (355),

\[
 \mathcal Q(t)=0,\qquad
 \|\mathcal Q(u)\|_2^2\ge {1\over3}\|u\|^2.               \tag{358}
\]

We first make the singular-value expansion in Proposition 59 uniform in
the direction.  Decompose the rows of (V_{\psi(\delta)}) by
(P_+\oplus P_-) and its columns by
(Q_0^\perp\oplus Q_0).  The upper-left block is invertible between its
four-dimensional domain and range at (\delta=0).  Multiplying on the
left and right by uniformly bounded invertible block-triangular matrices
eliminates the two off-diagonal blocks.  The remaining lower-right Schur
block is

\[
 B(\delta)=\mathcal Q(u)+O(r^2),                             \tag{359}
\]

uniformly for (\delta/r) on the tangent sphere.  This follows because
both off-diagonal blocks are (O(r)), their Schur-complement product is
(O(r^2)), and the normalization in (353) changes (V) only by
(1+O(r^2)).  Bounded invertible row and column multipliers distort
singular values by bounded factors.  Hence, if
(\lambda_1(\delta),\ldots,\lambda_5(\delta)) are the five output
eigenvalues that vanish at (\delta=0), there are constants
(c_0,C_0,C_1>0) such that, for all sufficiently small (r),

\[
 \begin{split}
 0\le\lambda_j(\delta)&\le C_0r^2,\\
 q(\delta):=\sum_{j=1}^5\lambda_j(\delta)
 &\ge c_0\|u\|^2-C_1r^4.                                  \tag{360}
 \end{split}
\]

For completeness, the second line can also be read directly from (359):
the sum of the five small squared singular values is comparable to
(\|B(\delta)\|_2^2), and
(\|\mathcal Q(u)+O(r^2)\|_2^2
 \ge\frac16\|u\|^2-Cr^4) by (358) and Young's inequality.

Separate the entropy into the four eigenvalues continuing the nonzero
spectrum in (306) and the five small eigenvalues.  The former contribution,
denoted (F_{\rm old}(\delta)), is real analytic: a fixed contour separates
the four positive eigenvalues from zero, its Riesz spectral projection is
analytic, and (-x\log x) is analytic on that positive spectral cluster.
The proof of Proposition 59 shows that its first derivative at zero vanishes.
On the exceptional plane (u=0), equation (313) and the fact that the five
small eigenvalues contribute (o(\|t\|^2)) give

\[
 F_{\rm old}(t)-H_*={\log2\over3}\|t\|^2+o(\|t\|^2).       \tag{361}
\]

Taylor expansion and polarization of this positive quadratic restriction
therefore yield constants (a,C_2>0) such that

\[
 F_{\rm old}(t+u)-H_*
 \ge a\|t\|^2-C_2(\|t\|\|u\|+\|u\|^2)-C_2r^3,             \tag{362}
\]

where (a) may be any fixed number smaller than (log2/3) after the
neighborhood is reduced.

The small-eigenvalue contribution is nonnegative.  More is true away from
the second exceptional chart.  Choose (M) so large that (359) implies

\[
 \|u\|\ge Mr^2\quad\Longrightarrow\quad
 q(\delta)\ge c_3\|u\|^2                                  \tag{363}
\]

for some (c_3>0).  From the first line of (360),

\[
 \begin{split}
 -\sum_{j=1}^5\lambda_j(\delta)\log\lambda_j(\delta)
 &\ge q(\delta)\log {1\over C_0r^2}\\
 &\ge c_3\|u\|^2\log {1\over C_0r^2}.                    \tag{364}
 \end{split}
\]

We now close the two blow-up charts.  If (|u|<Mr^2), then
(|t|^2=r^2+O(r^4)); (362) is positive for small nonzero (r), and
the small-eigenvalue entropy is nonnegative.  If (|u|\ge Mr^2), use
Young's inequality in (362):

\[
 C_2\|t\|\|u\|\le {a\over2}\|t\|^2+C_4\|u\|^2.
\]

The (r^3) term is absorbed either by the remaining (t)-quadratic term
when (|t|\ge r/2), or by the (u)-term in (364) when
(|t|<r/2).  Since the logarithm in (364) diverges as (r\downarrow0),
after one uniform reduction of the neighborhood the sum of (362) and (364)
is strictly positive.  This proves (356).

Finally, Lemma 53 shows Weyl covariance of each factor.  Local Weyl shifts
act transitively on the nine computational basis rays and conjugate the
corresponding outputs unitarily.  Transporting (mathcal U) proves the
last two assertions. \(\square\)

The finite datum that makes the transition chart quantitative is the
spectral gap in (358).  The following exact `python3`/`sympy` computation
reconstructed (P_-), (Q_0), and the full complex-linear map (357), rather
than inserting the eigenvalues from (319).  The tangent basis is the standard
basis with (|00\rangle) omitted, so coordinate indices (2,3) mean
(|02\rangle,|10\rangle).  Here is the verbatim output:

```text
occupied_output_indices = [0, 0, 2, 0, 0, 2, 3, 3, 5]
column_groups = [(0, 1, 3, 4), (2, 5), (6, 7), (8,)]
Q_map_shape = (81, 8)
QstarQ_rank = 6
QstarQ_eigenvalues = [(0, 2), (1/3, 1), (1/2, 2), (7/12, 2), (3/4, 1)]
kernel_coordinate_indices_in_tangent_basis = [2, 3]
smallest_positive_eigenvalue = 1/3
exceptional_quadratic_coefficient = log(2)/3
```

Thus the blow-up separates the rank-deficient entropy singularity into two
uniformly controlled mechanisms: transverse directions create new
eigenvalues and the positive (r^2\log(1/r)) term, while the exceptional
plane has the ordinary positive quadratic coefficient (log2/3).  This
upgrades the pathwise assertion in Proposition 59 to an actual local basin.
Proposition 64 contains another (315) product-minimizing rays outside the
computational orbit; carrying out their blow-up charts, or proving that they
are related by further channel symmetries, remains **[UNPROVED]**.

### Dated formatting correction 2026-08-21

The inline TeX delimiters in the immediately preceding round were consumed
during transcription.  Every plain-parenthesis mathematical expression in
that round is inline mathematics.  In particular, the following strings mean

\[
 \begin{gathered}
 H_*,\quad [\psi_0],\quad \delta=r\vartheta,\quad r\ge0,\quad
 \|\vartheta\|=1,\quad r=0,\quad
 \mathcal U,\quad [|00\rangle],\quad [\psi],\quad [|j,k\rangle],\\
 V_\psi,\quad \psi_0,\quad P_+,\quad P_-=I-P_+,\quad Q_0,\quad
 \ker V_{\psi_0},\quad
 P_+\oplus P_-,\quad Q_0^\perp\oplus Q_0,\\
 \delta=0,\quad O(r),\quad O(r^2),\quad 1+O(r^2),\quad
 \lambda_1(\delta),\ldots,\lambda_5(\delta),\quad
 c_0,C_0,C_1>0,\\
 F_{\rm old}(\delta),\quad -x\log x,\quad u=0,\quad
 o(\|t\|^2),\quad a,C_2>0,\quad a<\log2/3,\quad
 M,\quad c_3>0.
 \end{gathered}
\]

The same restoration applies to every other such expression.  In the
two-chart conclusion, the malformed norm strings are, explicitly,

\[
 \|u\|<Mr^2,\qquad \|t\|^2=r^2+O(r^4),\qquad
 \|u\|\ge Mr^2,\qquad \|t\|\ge r/2,\qquad \|t\|<r/2,
\]

and the remaining plain-parenthesis expressions there mean
\(r\), \(r^3\), \(t\), \(u\), \(r\downarrow0\),
\(P_-\), \(Q_0\), \(|00\rangle\), \(|02\rangle\),
\(|10\rangle\), \(2,3\), \(r^2\log(1/r)\), \(\log2/3\), and
\(315\), as dictated by equations (353)--(364).

The last line of the finite output,
**exceptional_quadratic_coefficient = log(2)/3**, records the already-proved
coefficient (313).  The independently reconstructed finite matrix supplies
the preceding eigenvalue list and, in particular, the spectral gap \(1/3\)
used in (358).  No mathematical assertion in Proposition 67 is changed.

## Round 2026-08-21: common-scale localization improves the quadratic exponent constant

The quadratic input-qubit estimate (220) normalized the Haar tail separately
by the limiting norm of every coefficient polynomial.  The localization
problem, however, asks only for the common upper target \(K_{N,k}\).  A cutoff
at that common scale replaces the pointwise radius in (243) by

\[
 {N^k\over K_{N,k}}.
\]

This does not remove the remaining power of \(k\), but it gives a strictly
smaller leading constant in the best quantitative input-dimension bound.
No new external result is used: the retained-radius argument (240), in its
fixed-tolerance form (246)--(249), is applied with a larger cutoff interval.

### Lemma 68 (fixed-target tensor-Haar tail)

Let \(P\) be a nonzero self-adjoint polynomial of degree at most \(q_0\) in
\(L\) disjoint tensor copies of Haar-unitary variables, with matrix
coefficients of size \(s\).  Suppose

\[
 \rho=\|P(u)\|\le B,
 \qquad K=\|P\|_{M_s\otimes C^*(\mathbb F_{Lr})},
 \qquad R_B=\max\{1,K/B\},                                  \tag{365}
\]

where \(B>0\).  Fix \(0<\varepsilon\le1/2\), and put
\(\widetilde q_0=q_0(1+\log q_0)\).  There are positive constants
\(c_\varepsilon,C_\varepsilon\), independent of the coefficients of \(P\),
such that, whenever \(n\) satisfies threshold conditions depending only on
\(R_B,q_0,s,\varepsilon\),

\[
 \mathbb P\{\|P(U^{(\cdot,n)})\|>(1+\varepsilon)B\}
 \le C_\varepsilon R_Bs n^L
 \exp\!\left[-{c_\varepsilon n\over
 R_B^6\widetilde q_0^{\,2}\log^2 n}\right].                 \tag{366}
\]

The same assertion holds for a non-self-adjoint polynomial after its
standard \(2\)-by-\(2\) self-adjoint dilation.

**Proof.**  In the proof leading to (240), replace the cutoff around
\([ -\rho,\rho]\) by a smooth function that vanishes on the
\(\varepsilon B/2\)-neighborhood of \([-B,B]\) and equals one outside its
\(\varepsilon B\)-neighborhood.  This cutoff still vanishes on the limiting
spectrum because \(\rho\le B\).  In the substitution
\(f(\vartheta)=h(K\cos\vartheta)\), every derivative ratio is now bounded by

\[
 {K\over\varepsilon B}\le {R_B\over\varepsilon},            \tag{367}
\]

rather than by (230).  The calculation giving (240), with the fixed powers
of \(\varepsilon^{-1}\) absorbed into constants, therefore gives

\[
 \begin{split}
 &\mathbb P\{\|P(U^{(\cdot,n)})\|>(1+\varepsilon)B\}\\
 &\quad\le C_\varepsilon R_Bs n^L
 \left[
 \left({C_\varepsilon R_B^3\widetilde q_0m^{1+2u}
               \over un}\right)^m
 +\left({C_\varepsilon R_B^6\widetilde q_0^{\,2}m^{1+4u}
               \over u^2n}\right)^m
 \right].                                                    \tag{368}
 \end{split}
\]

Choose

\[
 m=\left\lfloor {c_0n\over
 R_B^6\widetilde q_0^{\,2}\log^2n}\right\rfloor,
 \qquad u={1\over1+\log m},                                 \tag{369}
\]

with \(c_0=c_0(\varepsilon)>0\) sufficiently small.  As in (234),
\(m^{4u}\le e^4\), while \(u^{-2}\le C\log^2n\).  Substitution of
(369) makes the second base in (368) at most \(e^{-2}\).  The square of
the first base is bounded by a constant times \(m/n\) times the second
base, so decreasing \(c_0\) controls it as well.  Requiring \(m\ge2\),
\(s\le e^m\), and the fixed-tolerance Haar threshold gives conditions
depending only on the quantities displayed in the statement.  The two
geometric terms in (368), the floor in (369), and the prefactor are absorbed
by changing \(c_\varepsilon,C_\varepsilon\), which proves (366).

The self-adjoint dilation has coefficient size \(2s\) and preserves its
degree and all three norms in (365), so the last assertion follows.
\(\square\)

### Proposition 69 (an explicit improved quadratic coefficient)

Fix \(N\ge4\) and \(0<\varepsilon\le1/2\), and define

\[
 \beta_N=2\log N+3\log{N^2\over N+9}
         =8\log N-3\log(N+9).                               \tag{370}
\]

The localized tuples in Proposition 46 can be chosen with total input
dimension \(d_k\) satisfying

\[
 \log d_k\le
 \beta_Nk^2+8k\log(k+1)+O_{N,\varepsilon}(k),               \tag{371}
\]

while retaining the norm estimate (219).  In particular,

\[
 \limsup_{k\to\infty}{\log d_k\over k^2}\le\beta_N.        \tag{372}
\]

**Proof.**  Put \(D=N^k\) and \(B=K_{N,k}\).  For every
\(b\in\mathbb S_D\), the full norm of the polynomial (212) satisfies the
coefficient-independent estimate

\[
 \|P_b\|_{C^*(\mathbb F_{Nk})}
 \le\sum_{v,w}|b_{vw}|
 \le D\|b\|_2=D.                                            \tag{373}
\]

The first inequality uses only that every group word is unitary, and the
second is Cauchy--Schwarz over the \(D^2\) entries.  The same bound holds
after self-adjoint dilation.  Also, (11) gives \(\|P_b(u)\|\le B\).
Lemma 68 therefore applies simultaneously to the entire net with

\[
 R_B\le {D\over K_{N,k}},
 \qquad
 \left({D\over K_{N,k}}\right)^6
 ={N^{6k}\over[(N+9)^k-N^k]^3}.                             \tag{374}
\]

Since

\[
 (N+9)^k-N^k
 =(N+9)^k\left[1-\left({N\over N+9}\right)^k\right]
 \ge {9\over N+9}(N+9)^k,
\]

(374) implies

\[
 R_B^6\le \left({N+9\over9}\right)^3
 \exp\!\left(3k\log{N^2\over N+9}\right).                 \tag{375}
\]

Use the net in Proposition 46 with

\[
 \delta={\varepsilon B\over D}.
\]

Equations (374)--(375) imply
\(\log(1+2/\delta)=O_{N,\varepsilon}(k)\), and hence

\[
 \log|\mathcal M|\le C_{N,\varepsilon}kN^{2k}.             \tag{376}
\]

Choose the common local Haar size

\[
 n_k=\left\lceil e^{\beta_Nk}(k+1)^8\right\rceil.           \tag{377}
\]

For \(q_0=2k\), equations (370), (375), and (377) give

\[
 {n_k\over R_B^6[2k(1+\log(2k))]^2\log^2n_k}
 \ge c_{N,\varepsilon}N^{2k}{(k+1)^4\over\log^2(k+1)}       \tag{378}
\]

for all sufficiently large \(k\).  The right side of (378) dominates
(376).  The logarithm of the prefactor in (366), even after multiplication
by the net size, contributes in addition only
\(O_{N,\varepsilon}(k^2)+\log|\mathcal M|\).  Thus the union of all bad
events has probability less than one for all sufficiently large \(k\).
There is consequently a realization for which

\[
 \|P_b(U)\|\le(1+\varepsilon)K_{N,k}
 \qquad(b\in\mathcal M).                                   \tag{379}
\]

For arbitrary \(a\in\mathbb S_D\), choose \(b\in\mathcal M\) with
\(\|a-b\|_2\le\delta\).  The \(D\)-Lipschitz estimate (16) and (379)
give

\[
 \|P_a(U)\|
 \le(1+\varepsilon)K_{N,k}+D\delta
 =(1+2\varepsilon)K_{N,k}.                                  \tag{380}
\]

This is (219).  The input space is
\((\mathbb C^{n_k})^{\otimes k}\), so (377) yields

\[
 \log d_k=k\log n_k
 \le\beta_Nk^2+8k\log(k+1)+k\log2.                         \tag{381}
\]

The finitely many values of \(k\) preceding the common threshold are
handled by Proposition 46; enlarging the linear term in (371) covers their
finite dimensions.  Equations (371)--(372) follow. \(\square\)

The radius in the preceding proof of Proposition 46 was bounded by (243).
Keeping its exponential constant in the same union bound would give

\[
 \beta_N^{\rm old}=2\log N+3\log(N^2-N+1).                  \tag{382}
\]

The new coefficient is strictly smaller, because

\[
 \beta_N^{\rm old}-\beta_N
 =3\log\!\left({(N^2-N+1)(N+9)\over N^2}\right)>0.          \tag{383}
\]

Thus (371) is a genuine constant improvement of the strongest proved
quantitative dimension bound, rather than a change in lower-order terms.

### Corollary 70 (the gap rate at the improved dimension constant)

For every fixed \(N\ge4\) and \(0<\varepsilon\le1/2\), there are
finite-dimensional conjugate channels whose complementary output dimension
is \(N^k\), whose input dimension satisfies (371), and for which

\[
 \Delta(\Phi_k,\overline\Phi_k)
 \ge {k\log N\over N}
 -2\log\!\left(1+(1+2\varepsilon)^2
       [(1+9/N)^k-1]\right).                                \tag{384}
\]

Consequently their normalized gaps still satisfy

\[
 \liminf_{k\to\infty}{1\over k}
 \Delta(\Phi_k,\overline\Phi_k)\ge c_N.                   \tag{385}
\]

**Proof.**  Proposition 69 supplies exactly the localized norm estimate
(219) used in Corollary 47.  Applying Lemma 10, the orthogonal collision
calculation (38), and the Bell witness (23) gives (384).  Division by \(k\)
and the same limit as in (226) gives (385). \(\square\)

The constants and the finite-radius improvement were checked with
`python3`; rational quantities in the \(N=5,k=3\) check were computed with
`fractions.Fraction`.  The output is verbatim:

```text
N=4
beta_new=3.395506816574514
beta_old_support_route=10.467436794624392
improvement=7.071929978049878
new_strictly_smaller=True
N=5
beta_new=4.958331310627027
beta_old_support_route=12.352443138038470
improvement=7.394111827411443
new_strictly_smaller=True
N=18
beta_new=13.235463465156329
beta_old_support_route=22.961286758553918
improvement=9.725823293397589
new_strictly_smaller=True
N=72
beta_new=21.029981488111126
beta_old_support_route=34.171957023272107
improvement=13.141975535160981
new_strictly_smaller=True
N=178482139
beta_new=94.999995311488448
beta_old_support_route=151.999992723614156
improvement=56.999997412125708
new_strictly_smaller=True
N=5 k=3 D=125 K_squared=2619
new_common_radius_squared=15625/2619 = 5.966017563955709
old_pointwise_radius_squared=9260
new_radius_strictly_smaller=True
new_sixth_power=3814697265625/17964142659
old_sixth_power=794022776000
sixth_power_improvement_factor=3.739205873843359e+09
exact_ratio_comparison_verified_for_4<=N<=100=True
```

The strict inequality in (383) is analytic for every \(N\ge4\); the last
line is only a redundant finite check.  At the optimized one-bit alphabet
of Proposition 15, the leading quadratic coefficient drops from about
\(151.9999927\) to \(94.9999953\).  The exponent is still quadratic in
the block number, so the qubit-linear condition (24) remains open.

### Proof supplement 2026-08-21

Two elementary edge cases in the application of Lemma 68 are made explicit.
First, for \(N\ge4\),

\[
 K_{N,k}^2=(N+9)^k-N^k<N^{2k}=D^2,
\]

because \(N+9<N^2\).  Hence \(D/K_{N,k}>1\), so the maximum with one in
(365) is indeed bounded by the right side of (374).  Second, if a net
polynomial has \(P_b(u)=0\), orthonormality in (217) forces every grouped
coefficient \(c_s\) to vanish.  Equation (215) then shows that the polynomial
vanishes under every unitary evaluation, so it contributes no bad event.
For all other net points, the proof of Lemma 68 may use the common upper
radius \(D/K_{N,k}\) in place of the smaller individual radius; the choices
in (369) and all threshold conditions are then uniform over the net.

## Round 2026-08-21: the threshold quantifier in the common-scale localization

The strongest quantitative assertion above is the coefficient
\(\beta_N\) in Proposition 69.  Its weakest step is the passage from Lemma
68, whose statement contains unspecified threshold conditions, to the
particular prescribed size (377).  Dependence of a threshold only on
\(R_B,q_0,s,\varepsilon\) is not by itself enough: these parameters vary
with \(k\), so an uncontrolled threshold could be larger than (377).  This
round resolves that quantifier directly from the raw estimate (368).

The source actually reopened for this audit was
[Chen--Garza-Vargas--van Handel, *A new approach to strong convergence II.
The classical ensembles*, Theorem 7.8 and the proof in Section 7.6]
(https://arxiv.org/html/2412.00593v3).  Theorem 7.8 states its smooth
expansion for every matrix size and every moment order.  In Section 7.6 the
restrictions introduced when the moment order is selected are precisely the
lower bound on that order, the coefficient-dimension bound, and the Haar
condition \(\varepsilon\ge2/\sqrt n\).  The tensor-Haar adaptation and the
retained-radius substitution have already been isolated in (368).  Thus the
argument below does not invoke a further asymptotic threshold hidden in the
phrase “sufficiently large.”

### Lemma 71 (the prescribed Haar size clears every explicit threshold)

Fix \(N\ge4\) and \(0<\varepsilon\le1/2\).  Put

\[
 a_N=\log {N^2\over N+9},\qquad
 \beta_N=2\log N+3a_N,
\]

and, for \(k\ge1\), define

\[
 \begin{split}
 D_k&=N^k,& B_k&=K_{N,k},& R_k&={D_k\over B_k},\\
 Q_k&=2k(1+\log(2k)),&
 n_k&=\left\lceil e^{\beta_Nk}(k+1)^8\right\rceil .
 \end{split}                                                   \tag{386}
\]

Let \(c_0=c_0(\varepsilon)>0\) be the fixed constant used in (369), and
set

\[
 m_k=\left\lfloor {c_0n_k\over
             R_k^6Q_k^2\log^2 n_k}\right\rfloor,
 \qquad u_k={1\over1+\log m_k}.                              \tag{387}
\]

Then, for all sufficiently large \(k\),

\[
 m_k\ge2,\qquad {1\over m_k}\le u_k\le1,\qquad
 2\le e^{m_k},\qquad \varepsilon\ge {2\over\sqrt{n_k}}.     \tag{388}
\]

Moreover, there is a constant \(c_{N,\varepsilon}>0\) such that

\[
 {c_0n_k\over R_k^6Q_k^2\log^2n_k}
 \ge c_{N,\varepsilon}N^{2k}
             {(k+1)^4\over\log^2(k+1)}                     \tag{389}
\]

for all sufficiently large \(k\).

**Proof.**  The identity \(B_k^2=(N+9)^k-N^k\) and the elementary
estimate used in (375) give

\[
 R_k^6={N^{6k}\over[(N+9)^k-N^k]^3}
 \le \left({N+9\over9}\right)^3e^{3a_Nk}.                 \tag{390}
\]

Since \(n_k\ge e^{\beta_Nk}(k+1)^8\) and
\(\beta_N-3a_N=2\log N\), it follows that

\[
 {n_k\over R_k^6}
 \ge c_NN^{2k}(k+1)^8.                                     \tag{391}
\]

For fixed \(N\), equation (386) also gives

\[
 Q_k^2\le C k^2\log^2(k+1),\qquad
 \log^2n_k\le C_Nk^2                                      \tag{392}
\]

for all sufficiently large \(k\).  Equations (391)--(392) prove (389).
In particular, the quantity before the floor in (387) tends to infinity,
so \(m_k\ge2\).  For every \(m\ge2\), \(m\ge1+\log m\); hence
\(1/m\le1/(1+\log m)\le1\), proving the middle condition in (388).
The coefficient size after self-adjoint dilation is \(s=2\), so
\(s\le e^{m_k}\).  Finally \(n_k\to\infty\), and therefore
\(n_k\ge4/\varepsilon^2\), which is the last condition in (388).
\(\square\)

### Proposition 72 (the coefficient in Proposition 69 survives the threshold audit)

For the \(n_k\) in (386), the union bound in Proposition 69 is valid for
all sufficiently large \(k\).  Consequently (371)--(372), and hence
(384)--(385), remain proved with the displayed coefficient \(\beta_N\).

**Proof.**  The net radius is \(\delta=\varepsilon/R_k\).  From (390),
\(\log(1+2R_k/\varepsilon)=O_{N,\varepsilon}(k)\).  Thus the volumetric
net obeys

\[
 \log|\mathcal M|
 \le2(D_k^2-1)\log(1+2R_k/\varepsilon)
 \le C_{N,\varepsilon}kN^{2k}.                              \tag{393}
\]

Lemma 71 verifies every explicit admissibility condition for the raw tail
(368), with \(L=k,q_0=2k,s=2,B=B_k\).  After the choices (387), its
negative logarithmic term is bounded below, by (389), as

\[
 E_k\ge c_{N,\varepsilon}N^{2k}
                {(k+1)^4\over\log^2(k+1)}.                  \tag{394}
\]

After multiplying by the net size, the logarithm of every positive
prefactor in (368) is at most

\[
 \log|\mathcal M|+O_{N,\varepsilon}(k^2),                  \tag{395}
\]

because \(\log R_k=O_N(k)\) and
\(k\log n_k=O_N(k^2)\).  Dividing (394) by the leading bound in (393)
gives a lower bound of order
\(k^3/\log^2(k+1)\), which tends to infinity.  Hence the logarithm of
the full union bound is negative for all sufficiently large \(k\).  This
proves the simultaneous good realization at the prescribed size (386).

For the finitely many smaller \(k\), Proposition 46 supplies finite
dimensions.  If those dimensions are \(d_k\), the maximum over that finite
set of

\[
 {\log d_k-\beta_Nk^2-8k\log(k+1)\over k}
\]

is finite, so enlarging only the \(O_{N,\varepsilon}(k)\) term in (371)
covers them.  This proves the proposition. \(\square\)

The finite arithmetic behind (390), and the scale separation in
(393)--(394), were checked with python3.  The radius comparisons use
fractions.Fraction; the scale audit uses 80-decimal mpmath arithmetic
with \(\varepsilon=1/4\).  The latter omits only the fixed positive
universal constant in the tail exponent and is not used in the asymptotic
proof.  Here is the verbatim output:

~~~text
exact_radius_bound N=4 k=1 verified=True ratio=1
exact_radius_bound N=4 k=3 verified=True ratio=2.75794070161
exact_radius_bound N=4 k=7 verified=True ratio=3.01135734042
exact_radius_bound N=5 k=1 verified=True ratio=1
exact_radius_bound N=5 k=3 verified=True ratio=3.27273433582
exact_radius_bound N=5 k=7 verified=True ratio=3.75569759525
exact_radius_bound N=18 k=1 verified=True ratio=1
exact_radius_bound N=18 k=3 verified=True ratio=9.40877914952
exact_radius_bound N=18 k=7 verified=True ratio=22.531310622
scale audit uses epsilon=1/4 and omits only the positive universal tail constant
N=4 k=10 log10(exponent_scale/net_log)=0.27421674397763 admissibility_scale=1.3069665e+13
N=4 k=25 log10(exponent_scale/net_log)=1.4773852970737 admissibility_scale=3.5649367e+32
N=4 k=50 log10(exponent_scale/net_log)=2.3933671997404 admissibility_scale=5.78093e+63
N=4 k=100 log10(exponent_scale/net_log)=3.2860000643891 admissibility_scale=1.2433564e+125
N=5 k=10 log10(exponent_scale/net_log)=-0.14763978317046 admissibility_scale=6.7684823e+14
N=5 k=25 log10(exponent_scale/net_log)=0.9162258224819 admissibility_scale=1.3661872e+37
N=5 k=50 log10(exponent_scale/net_log)=1.7505396100589 admissibility_scale=1.4723839e+73
N=5 k=100 log10(exponent_scale/net_log)=2.5876319552396 admissibility_scale=1.4962673e+144
N=18 k=10 log10(exponent_scale/net_log)=-1.3207242802305 admissibility_scale=1.7680913e+25
N=18 k=25 log10(exponent_scale/net_log)=-0.38733659751898 admissibility_scale=1.576455e+64
N=18 k=50 log10(exponent_scale/net_log)=0.373052604032 admissibility_scale=1.0206631e+128
N=18 k=100 log10(exponent_scale/net_log)=1.1641671701004 admissibility_scale=4.1801004e+254
~~~

The numerical ratios need not exceed one at small \(k\), because the proof
is asymptotic and the omitted tail constant is not normalized.  Their growth
is consistent with the proved factor \(k^3/\log^2 k\).  The essential
point is now quantifier-level rather than numerical: the moment order in
(387) both satisfies every condition used to obtain (368) and overwhelms
the full net cardinality at the exact scale (377).  Thus no uncontrolled
threshold remains in the leading coefficient of (371).

### Dated notation correction 2026-08-21

The symbol \(c_N\) in (391) conflicts with the previously defined entropy
rate \(c_N\), which may be negative for small \(N\).  In (391) it denotes
only a positive \(N\)-dependent constant.  Strike that occurrence and read
(391) as

\[
 \text{~~\(n_k/R_k^6\ge c_NN^{2k}(k+1)^8\)~~},\qquad
 {n_k\over R_k^6}
 \ge \kappa_NN^{2k}(k+1)^8,\qquad
 \kappa_N=\left({9\over N+9}\right)^3>0.                    \tag{396}
\]

Indeed, (396) follows immediately by inverting (390) and using the lower
bound on \(n_k\).  Equations (389) and (394) already use a separately named
positive constant \(c_{N,\varepsilon}\), so no assertion or later estimate
 changes.

## Round 2026-08-21: the stabilizer product basin is one symmetry orbit

Proposition 67 proves strict local minimality at the nine computational
product rays, while Corollary 64 gives (324) product-minimizing rays in
all.  The smallest untreated part of that finite set is the collection in
which both one-qutrit factors belong to the nine-ray stabilizer packet in
Proposition 63.  This round settles exactly that subcase.  An affine
Clifford three-cycle of each Weyl triangle shows that all (81) such product
rays lie in one local-symmetry orbit.  No assertion is made here about a
product ray having a factor in the nonstabilizer (E_1) packet.

Put

\[
 e_x=(1,0),\qquad e_z=(0,1),\qquad
 T_s=\{0,e_z,se_x\}\subset\mathbb F_3^2,
 \qquad s\in\{1,-1\}.
\]

Thus (T_s) is the phase-space support of the random-unitary tuple defining

\[
 \Phi_s(A)={A+ZAZ^*+X^sAX^{-s}\over3}.
\]

### Lemma 73 (an affine Clifford three-cycle of each Weyl triangle)

For (s\in\{1,-1\}\), with its value interpreted in \(\mathbb F_3\), define

\[
 A_s=\begin{pmatrix}0&s\\2s&2\end{pmatrix},\qquad
 f_s(e)=A_se+e_z.                                           \tag{397}
\]

Then \(\det A_s=1\), and (f_s) cyclically permutes the three vertices by

\[
 0\longmapsto e_z\longmapsto se_x\longmapsto0.             \tag{398}
\]

There are unitaries (U_s,V_s\in U(3)\) such that

\[
 U_sW_eU_s^*=\chi_s(e)W_{A_se},\qquad |\chi_s(e)|=1,
 \qquad V_s=ZU_s,                                           \tag{399}
\]

and, for every qutrit state \(\rho\),

\[
 \Phi_s(U_s\rho U_s^*)=V_s\Phi_s(\rho)V_s^*.              \tag{400}
\]

In addition, every Weyl unitary gives the covariance

\[
 \Phi_s(W_g\rho W_g^*)=W_g\Phi_s(\rho)W_g^*.
                                                                    \tag{401}
\]

**Proof.**  The determinant and the vertex cycle follow directly from

\[
 A_se_z=se_x-e_z,\qquad A_s(se_x)=-e_z.                     \tag{402}
\]

Here is an explicit Clifford lift.  Define

\[
 He_j={1\over\sqrt3}\sum_{k=0}^2\omega^{jk}e_k,
 \qquad
 De_j=\omega^{j(j-1)/2}e_j,
 \qquad \omega=e^{2\pi i/3}.                               \tag{403}
\]

Direct multiplication gives

\[
 HXH^*=Z,\qquad HZH^*=X^{-1},\qquad
 DXD^*=XZ,\qquad DZD^*=Z.                                  \tag{404}
\]

Thus the induced matrices on Weyl indices are

\[
 S=\begin{pmatrix}0&2\\1&0\end{pmatrix},\qquad
 T=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

The choices

\[
 U_+=HDHD,\qquad U_-=DH                                   \tag{405}
\]

induce, respectively,

\[
 STST=\begin{pmatrix}0&1\\2&2\end{pmatrix}=A_+,
 \qquad
 TS=\begin{pmatrix}0&2\\1&2\end{pmatrix}=A_-.
\]

This proves (399), including the irrelevant Weyl multiplication phases.
For (e\in T_s\), equation (399) gives

\[
 V_sW_e=ZU_sW_e
       =\widetilde\chi_s(e)W_{e_z+A_se}U_s
       =\widetilde\chi_s(e)W_{f_s(e)}U_s.                  \tag{406}
\]

Conjugate each summand in \(\Phi_s(\rho)\) by (V_s), use that (f_s)
permutes (T_s), and relabel the three terms.  The result is (400).
Finally, two qutrit Weyl operators commute up to a scalar phase.  Moving
(W_g) through each of the three errors in (T_s) makes those phases cancel
against their adjoints, proving (401). \(\square\)

### Lemma 74 (transitivity on the nine stabilizer minimizers)

Let

\[
 \mathscr L_s=
 \{\langle e_z\rangle,\langle se_x\rangle,
                         \langle se_x-e_z\rangle\}          \tag{407}
\]

be the three projective edge directions of (T_s), and let
\(\mathscr S_s\) be the set of eigenrays of the nonidentity Weyl operators
on these three lines.  The input unitaries generated by (U_s) and all
Weyl unitaries act transitively on \(\mathscr S_s\).  Moreover,

\[
 |\mathscr S_s|=9,                                          \tag{408}
\]

and \(\mathscr S_s\) is exactly the nine-ray stabilizer packet of the
one-channel minimizing set in Proposition 63.

**Proof.**  Equation (402) and linearity give

\[
 A_se_z=se_x-e_z,\qquad
 A_s(se_x)=-e_z,\qquad
 A_s(se_x-e_z)=-se_x.                                      \tag{409}
\]

Hence (A_s) cycles the three projective lines in (407).  By (399), (U_s)
therefore cycles their Weyl eigenbases.

Fix a nonzero Weyl index \(\ell\).  Nondegeneracy of the symplectic form on
\(\mathbb F_3^2\) gives an index (g) for which the commutation phase of
\(W_g\) and (W_\ell\) is a nontrivial cube root of unity.  Conjugation by
\(W_g\) consequently cycles the three eigenspaces of (W_\ell).  Their
dimensions are equal and sum to three, so they are one-dimensional and the
Weyl action is transitive on their three rays.  Together with (409), this
proves transitivity on all three eigenbases.

Eigenbases belonging to two distinct lines in (407) share no ray: a common
eigenvector would make two Weyl operators with a nontrivial commutation phase
commute on a nonzero vector.  Thus there are exactly (3\cdot3=9) rays.
The last identification is the stabilizer description of the (E_0) packet
in Proposition 63, transported from (s=1) to (s=-1) by (337).
\(\square\)

### Proposition 75 (all stabilizer--stabilizer product minimizers are strict local minima)

Define the (81)-ray set

\[
 \mathscr P_{\rm st}
 =\{[x\otimes y]:[x]\in\mathscr S_+,
                         [y]\in\mathscr S_-\}.             \tag{410}
\]

For every \([x\otimes y]\in\mathscr P_{\rm st}\), there is an open
projective neighborhood \(\mathcal U_{x,y}\) such that

\[
 S((\Phi_1\otimes\Phi_{-1})(|\psi\rangle\langle\psi|))
 >2h_2(2/3)                                                  \tag{411}
\]

for every \([\psi]\in\mathcal U_{x,y}\) distinct from \([x\otimes y]\).
Consequently every stabilizer--stabilizer product minimizer is a strict
local minimum of the unrestricted two-qutrit pure-state entropy problem.

**Proof.**  Equations (400)--(401) show that every generator used in
Lemma 74 is an input symmetry of \(\Phi_s\) up to an output unitary.
Composition preserves this property.  By Lemma 74, choose such input
symmetries (G_+,G_-) with

\[
 G_+|0\rangle\sim x,\qquad G_-|0\rangle\sim y,             \tag{412}
\]

where \(\sim\) denotes equality up to phase.  There are output unitaries
\(Q_+,Q_-\) for which

\[
 \Phi_s(G_s\rho G_s^*)=Q_s\Phi_s(\rho)Q_s^*.
\]

It follows that the output entropy of \(\Phi_1\otimes\Phi_{-1}\) is
unchanged when its pure input is acted on by (G_+\otimes G_-).
Proposition 67 supplies an open projective neighborhood of \([|00\rangle]\)
on which that entropy is strictly larger than (2h_2(2/3)), except at the
central ray.  Its image under (G_+\otimes G_-) is the required
\(\mathcal U_{x,y}\), and (412) identifies its central ray. \(\square\)

The finite Clifford and phase-space claims above were checked with exact
\(`sympy`\) arithmetic inside \(`python3`\).  The matrices (H,D,U_s) were
checked directly, including all nine Weyl indices for each sign.  Here is
the verbatim output:

```text
H_unitary = True
D_unitary = True
H_X_Hstar_eq_Z = True
H_Z_Hstar_eq_Xminus = True
D_X_Dstar_eq_XZ = True
D_Z_Dstar_eq_Z = True
A_plus = [[0, 1], [2, 2]]
A_minus = [[0, 2], [1, 2]]
s = 1: det(A_s) mod 3 = 1; exact Weyl conjugations = 9/9
 affine_cycle_images = [(0, 1), (1, 0), (0, 0)]
 projective_direction_images = [(1, 2), (0, 1), (1, 0)]
s = -1: det(A_s) mod 3 = 1; exact Weyl conjugations = 9/9
 affine_cycle_images = [(0, 1), (2, 0), (0, 0)]
 projective_direction_images = [(1, 1), (0, 1), (1, 0)]
single_factor_stabilizer_orbit_size = 9
two_factor_stabilizer_product_rays = 81
new_rays_beyond_computational_orbit = 72
product_minimizers_still_outside = 243
```

Thus Proposition 67 extends from its nine computational product rays to all
(81) stabilizer--stabilizer product minimizers, settling (72) previously
untreated rays.  By Corollary 64, the remaining (324-81=243) product
minimizers are exactly those with at least one factor in the nonstabilizer
(E_1) packet.  Their local status remains **[UNPROVED]**.

### Dated formatting correction 2026-08-21

The inline TeX delimiters in the immediately preceding round were consumed
during transcription.  Every plain-parenthesis mathematical expression in
that round is inline mathematics.  In particular, the affected expressions
in order of appearance include

\[
 \begin{gathered}
 324,\quad 81,\quad E_1,\quad T_s,\quad
 s\in\{1,-1\},\quad f_s,\quad U_s,V_s\in U(3),\quad
 e\in T_s,\quad V_s,\quad f_s,\\
 W_g,\quad A_s,\quad U_s,\quad g,\quad W_\ell,\quad
 3\cdot3=9,\quad E_0,\quad s=1,\quad s=-1,\quad
 81,\quad G_+,G_-,\\
 G_+\otimes G_-,\quad 2h_2(2/3),\quad H,D,U_s,\quad
 72,\quad 324-81=243.
 \end{gathered}
\]

The malformed literal strings consisting of a backslash-parenthesis pair
around the names sympy and python3 mean simply those two code names.  All
displayed equations (397)--(412), the proofs, and the exact computational
output are unchanged.

## Round 2026-08-21: the Gibbs dual and stabilizer Fourier separation

The unresolved qutrit problem has so far been phrased as a minimization over
pure input states.  There is an exact dual representation in which the
variable is instead a Hermitian output Hamiltonian.  On a stabilizer maximal
abelian algebra this dual becomes an elementary log-partition problem for a
classical convolution channel.  Solving all forty such sectors strengthens
the finite stabilizer census in Proposition 51: it excludes an entire
continuous family of dual witnesses for each stabilizer basis.  Pinching and
the Weyl multiplier spectrum then force every hypothetical witness below the
product value to carry a definite amount of noncommutative Fourier energy.

Retain

\[
 \Lambda=\Phi_1\otimes\Phi_{-1},\qquad
 H_*=2h_2(2/3)=2\log3-{4\over3}\log2.
\]

### Proposition 76 (exact Gibbs dual of minimum output entropy)

For every finite-dimensional channel
\(\Omega:M_d\to M_D\),

\[
 S_{\min}(\Omega)
 =\inf_{H=H^*}\left\{\log\operatorname {Tr}e^H
                 -\lambda_{\max}(\Omega^*(H))\right\}.     \tag{413}
\]

The infimum need not be attained when a minimizing output is singular.

**Proof.**  For a state \(\sigma\) and a Hermitian \(H\), positivity of
relative entropy against the Gibbs state gives

\[
 D\!\left(\sigma\middle\|{e^H\over\operatorname {Tr}e^H}\right)
 =-S(\sigma)-\operatorname {Tr}(\sigma H)
       +\log\operatorname {Tr}e^H\ge0.
\]

Equality holds at \(H=\log\sigma\) when \(\sigma\) is invertible.  If it
is singular, put the value \(-t\) on its kernel and let \(t\to\infty\).
Consequently,

\[
 S(\sigma)=\inf_{H=H^*}
 \left\{\log\operatorname {Tr}e^H-\operatorname {Tr}(\sigma H)\right\}.
                                                                    \tag{414}
\]

Taking the infimum jointly over input states \(\rho\) and Hamiltonians
\(H\), and then taking the \(\rho\)-infimum first, gives

\[
 \begin{split}
 S_{\min}(\Omega)
 &=\inf_{H=H^*}\left\{\log\operatorname {Tr}e^H
       +\min_\rho[-\operatorname {Tr}(\rho\Omega^*(H))]\right\}\\
 &=\inf_{H=H^*}\left\{\log\operatorname {Tr}e^H
                 -\lambda_{\max}(\Omega^*(H))\right\}.
 \end{split}
\]

This is (413). \(\square\)

Write

\[
 \mathcal F_\Omega(H)=\log\operatorname {Tr}e^H
                 -\lambda_{\max}(\Omega^*(H)).             \tag{415}
\]

Thus the remaining equality in (202) is equivalent to
\(\mathcal F_\Lambda(H)\ge H_*\) for every Hermitian \(H\).

Let \(V=\mathbb F_3^2\oplus\mathbb F_3^2\), with the symplectic form in
(250), and put

\[
 K_{(a,b)}=W_a\otimes W_b,qquad
 E=T_+\times T_-,qquad
 T_+=\{0,(0,1),(1,0)\},\quad
 T_-=\{0,(0,1),(2,0)\}.
\]

For a Lagrangian plane \(L\subset V\), let \(\mathfrak A_L\) be the
nine-dimensional maximal abelian algebra spanned by
\(\{K_\ell:\ell\in L\}\).  If \(C\in V/L\), define

\[
 n_C=|E\cap C|,qquad p_L=(n_C/9:C\in V/L).                 \tag{416}
\]

Zero entries in \(p_L\) are retained or omitted without affecting its
entropy.

### Proposition 77 (exact stabilizer-MASA dual values)

For every Lagrangian plane \(L\subset V\),

\[
 \inf_{H=H^*\in\mathfrak A_L}\mathcal F_\Lambda(H)
 =H(p_L).                                                    \tag{417}
\]

As \(L\) ranges over all forty planes, these restricted dual values are as
follows.

\[
\begin{array}{c|c|c|c|c}
(n_C:n_C>0)&\#\text{ product}&\#\text{ entangled}
 &H(p_L)&H(p_L)-H_*\\
\hline
(4,2,2,1)&9&0&H_*&0\\
(2,2,2,1,1,1)&6&3&2\log3-\frac23\log2&\frac23\log2\\
(1,1,1,1,1,1,1,1,1)&1&0&2\log3&\frac43\log2\\
(2,2,1,1,1,1,1)&0&18&2\log3-\frac49\log2&\frac89\log2\\
(3,1,1,1,1,1,1)&0&3&\frac53\log3&\frac13\log(16/3).
\end{array}                                                  \tag{418}
\]

In particular, every entangled stabilizer MASA has restricted dual value at
least

\[
 H_*+\delta_0,qquad \delta_0={2\over3}\log2.              \tag{419}
\]

**Proof.**  Choose a joint eigenbasis of the commuting Weyl operators in
\(L\).  Its nine basis rays are indexed by the characters of \(L\), which
may be identified with \(V/L\) through the nondegenerate symplectic pairing.
Conjugation by \(K_e\) translates a character by the class of \(e\), and
two errors give the same translation exactly when they lie in the same
coset of \(L\).  Hence the restriction of \(\Lambda\) to the diagonal
algebra \(\mathfrak A_L\) is a classical translation channel whose rows
are the translates of the probability vector \(p_L\).

If the diagonal entries of \(H\in\mathfrak A_L\) form the real vector
\(h\), then \(\Lambda^*(H)\) is diagonal in the same basis and

\[
 \mathcal F_\Lambda(H)
 =\log\sum_j e^{h_j}-\max_x p_{L,x}\mathbin\cdot h,
\]

where the \(p_{L,x}\) are the translated rows.  Therefore

\[
 \begin{split}
 \inf_h\left(\log\sum_j e^{h_j}-\max_xp_{L,x}\mathbin\cdot h\right)
 &=\inf_{h,x}\left(\log\sum_j e^{h_j}-p_{L,x}\mathbin\cdot h\right)\\
 &=\min_x H(p_{L,x})=H(p_L).                                \tag{420}
 \end{split}
\]

The scalar conjugacy used in the second line is (414) applied to a diagonal
state; entries of zero probability are handled by sending the corresponding
\(h_j\) to \(-\infty\).

Proposition 51 gives the five histograms and their multiplicities.  For a
histogram \(n=(n_j)\),

\[
 H(n/9)=2\log3-{1\over9}\sum_jn_j\log n_j,                 \tag{421}
\]

which gives every entry in (418).  Among the three entangled rows, the
smallest gap is \(2\log2/3\): it is plainly smaller than
\(8\log2/9\), and

\[
 {1\over3}\log(16/3)-{2\over3}\log2
 ={1\over3}\log(4/3)>0.
\]

This proves (419). \(\square\)

Thus Proposition 51 did more than test the forty stabilizer input bases.
For each basis it also solves the dual entropy problem on the full
nine-real-dimensional algebra of all Hamiltonians diagonal in that basis.
In particular, no Hamiltonian in an entangled stabilizer MASA can witness an
entropy even as low as \(H_*\).

The separation persists quantitatively away from those algebras.  Define the
stabilizer pinching

\[
 \mathcal P_L(H)={1\over9}\sum_{\ell\in L}K_\ell H K_\ell^*.
                                                                    \tag{422}
\]

Its range is \(\mathfrak A_L\).

### Lemma 78 (pinching lower bound in the Gibbs dual)

For every Hermitian \(H\) and every Lagrangian plane \(L\),

\[
 \mathcal F_\Lambda(H)
 \ge H(p_L)-\|\Lambda^*(H-\mathcal P_LH)\|_\infty.         \tag{423}
\]

Moreover,

\[
 \|\Lambda^*(H-\mathcal P_LH)\|_\infty
 \le {1\over\sqrt3}\|H-\mathcal P_LH\|_2.                \tag{424}
\]

**Proof.**  The log-partition function is convex.  One direct proof is the
variational identity

\[
 \log\operatorname {Tr}e^H
 =\sup_\sigma\{\operatorname {Tr}(\sigma H)+S(\sigma)\},
\]

which follows from the same relative-entropy calculation as (414); it is a
supremum of affine functions of \(H\).  Since (422) is an average of unitary
conjugations, convexity and unitary invariance give

\[
 \log\operatorname {Tr}e^{\mathcal P_LH}
 \le\log\operatorname {Tr}e^H.                             \tag{425}
\]

The maximal-eigenvalue triangle inequality gives

\[
 \lambda_{\max}(\Lambda^*H)
 \le\lambda_{\max}(\Lambda^*\mathcal P_LH)
       +\|\Lambda^*(H-\mathcal P_LH)\|_\infty.
\]

Combining this with (425) and then applying (417) to
\(\mathcal P_LH\in\mathfrak A_L\) proves (423).

For (424), use the orthonormal Hilbert--Schmidt Weyl basis
\(\{K_v/3:v\in V\}\).  Pinching retains exactly the modes in \(L\), so
\(R=H-\mathcal P_LH\) has no identity mode.  Equations (284)--(286) give

\[
 \Lambda^*(K_{(a,b)})
 =\overline{\varphi_1(a)\varphi_{-1}(b)}K_{(a,b)}.
\]

For every nonidentity mode, the squared modulus of this multiplier is at
most \(1/3\).  Parseval and \(\|X\|_\infty\le\|X\|_2\) therefore give

\[
 \|\Lambda^*R\|_\infty^2
 \le\|\Lambda^*R\|_2^2\le {1\over3}\|R\|_2^2,
\]

which is (424). \(\square\)

### Proposition 79 (simultaneous noncommutative Fourier-energy obstruction)

Suppose a Hermitian Hamiltonian \(H\) satisfies

\[
 \mathcal F_\Lambda(H)<H_*.                                \tag{426}
\]

Then, for every one of the twenty-four entangled Lagrangian planes \(L\),

\[
 \begin{split}
 \|\Lambda^*(H-\mathcal P_LH)\|_\infty&>\delta_0,\\
 \|H-\mathcal P_LH\|_2&>\sqrt3\,\delta_0
 ={2\log2\over\sqrt3}.                                   \tag{427}
 \end{split}
\]

There is also a basis-independent Fourier version.  Expand

\[
 H=\sum_{v\in V}h_v{K_v\over3}.
\]

Let \(\mathcal A_{\rm loc}\) consist of the active nonidentity modes for
which exactly one of the two phase-space components is zero, and let
\(\mathcal A_{\rm nl}\) consist of the active modes for which both
components are nonzero.  Here active means that the multiplier of
\(\Lambda^*\) is nonzero.  Then

\[
 {1\over3}\sum_{v\in\mathcal A_{\rm loc}}|h_v|^2
 +{7\over72}\sum_{v\in\mathcal A_{\rm nl}}|h_v|^2
 >\delta_0^2={4\over9}(\log2)^2.                            \tag{428}
\]

**Proof.**  For an entangled \(L\), equations (419), (423), and (426)
imply the first strict inequality in (427).  Equation (424) then implies
the second.

For the Fourier statement, write
\(\mu_v=\varphi_1(a)\varphi_{-1}(b)\) for \(v=(a,b)\).  Parseval gives,
for each entangled \(L\),

\[
 \|\Lambda^*(H-\mathcal P_LH)\|_2^2
 =\sum_{v\notin L}|\mu_v|^2|h_v|^2>\delta_0^2.             \tag{429}
\]

There are six active nonidentity modes in either one-qutrit phase space.
Thus \(|\mathcal A_{\rm loc}|=12\), every such mode has
\(|\mu_v|^2=1/3\), while \(|\mathcal A_{\rm nl}|=36\), and every such
mode has \(|\mu_v|^2=1/9\).

It remains to average membership in \(L\).  Every entangled Lagrangian is
the graph of a linear map \(A:\mathbb F_3^2\to\mathbb F_3^2\) with
\(\det A=-1\), as in (255), so no nonzero local mode belongs to it.  A
fixed nonlocal vector \((x,y)\), with \(x,y\ne0\), belongs to exactly
three such graphs.  Indeed, the condition \(Ax=y\) fixes one column after
a basis containing \(x\) is chosen, and the determinant condition is one
nonzero affine-linear equation for the other column, with exactly three
solutions over \(\mathbb F_3\).  Therefore a local mode lies outside all
twenty-four entangled planes, while a nonlocal mode lies outside twenty-one
of them.  Averaging the left side of (429) over those planes gives exactly

\[
 {1\over3}\sum_{v\in\mathcal A_{\rm loc}}|h_v|^2
 +{21\over24}\,{1\over9}
      \sum_{v\in\mathcal A_{\rm nl}}|h_v|^2,
\]

which is (428). \(\square\)

Combining Proposition 76 with Proposition 79 gives a dual localization of
any putative qutrit counterexample.  If
\(S_{\min}(\Lambda)<H_*\), then some Hamiltonian satisfies (426), and that
Hamiltonian is more than \(2\log2/\sqrt3\) in Hilbert--Schmidt distance
from every entangled stabilizer MASA.  More invariantly, its active local
and nonlocal Weyl coefficients must satisfy the simultaneous energy barrier
(428).  Thus neither a diagonal Hamiltonian in any stabilizer basis nor a
small noncommutative perturbation of one can produce the unresolved entropy
descent.  The surviving dual search is confined to Hamiltonians with
substantial Fourier mass spread outside every entangled Lagrangian plane.

The finite-field incidence counts, the five classical dual values, and the
weighted averaging identity in (428) were checked by exact enumeration.
All finite-field operations and the test weights were exact; only displayed
entropy values were rendered as decimals.  Here is the verbatim
`python3` output:

```text
arithmetic = exact F_3 and Fraction except displayed entropy decimals
lagrangian_planes = 40 product = 16 entangled = 24
all_histograms = [((1, 1, 1, 1, 1, 1, 1, 1, 1), 1), ((2, 2, 1, 1, 1, 1, 1), 18), ((2, 2, 2, 1, 1, 1), 9), ((3, 1, 1, 1, 1, 1, 1), 3), ((4, 2, 2, 1), 9)]
product_histograms = [((1, 1, 1, 1, 1, 1, 1, 1, 1), 1), ((2, 2, 2, 1, 1, 1), 6), ((4, 2, 2, 1), 9)]
entangled_histograms = [((2, 2, 1, 1, 1, 1, 1), 18), ((2, 2, 2, 1, 1, 1), 3), ((3, 1, 1, 1, 1, 1, 1), 3)]
H_star = 1.273028336589626
histogram (1, 1, 1, 1, 1, 1, 1, 1, 1) count 1 dual_value=2.197224577336220 gap=0.924196240746594
histogram (2, 2, 1, 1, 1, 1, 1) count 18 dual_value=1.889159163754022 gap=0.616130827164396
histogram (2, 2, 2, 1, 1, 1) count 9 dual_value=1.735126456962923 gap=0.462098120373297
histogram (3, 1, 1, 1, 1, 1, 1) count 3 dual_value=1.831020481113516 gap=0.557992144523890
histogram (4, 2, 2, 1) count 9 dual_value=1.273028336589626 gap=-0.000000000000000
nonzero_modes = 80 active_local = 12 active_nonlocal = 36
entangled_MASA_incidence_all = {0: 16, 3: 64}
local_mode_incidence = {0: 16}
nonlocal_mode_incidence = {3: 64}
weighted_average_lhs = 220
weighted_average_rhs = 220
weighted_average_identity = True
smallest_entangled_dual_margin = (2/3)log(2) = 0.462098120373297
HS_distance_threshold = sqrt(3)*(2/3)log(2) = 0.800377422568629
active_energy_threshold = ((2/3)log(2))^2 = 0.213534672852534
```

The Gibbs dual is exact, but the Fourier-energy barrier is only necessary.
The log-partition term couples all noncommuting modes, and (428) supplies no
upper bound on their admissible energy after the scalar-shift invariance of
\(\mathcal F_\Lambda\) is taken into account.  A completion along this
representation would require a noncommutative log-partition inequality that
turns the simultaneous separation from the twenty-four entangled MASAs into
\(\mathcal F_\Lambda(H)\ge H_*\); such an inequality is **[UNPROVED]**.

### Dated scope correction 2026-08-21

The sentence above saying that neither a diagonal Hamiltonian in any
stabilizer basis ~~nor a small noncommutative perturbation of one~~ can
produce the unresolved descent is too broad in its second clause.  The
uniform perturbative separation (427) is proved only around the twenty-four
**entangled** stabilizer MASAs.  The corrected conclusion is: no diagonal
Hamiltonian in any stabilizer MASA witnesses a value below \(H_*\), and no
Hamiltonian within Hilbert--Schmidt distance \(2\log2/\sqrt3\) of an
entangled stabilizer MASA does so.  The nine product edge--edge MASAs have
restricted value exactly \(H_*\), so (423) supplies no positive-radius
neighborhood around them.  Equations (413)--(429) and Proposition 79 are
unchanged.

## Round 2026-08-21: all product minimizers are isolated entropy basins

This round tried to produce a qutrit counterexample by leaving one of the
product minimizers not covered by Proposition 75.  Corollary 64 gives 324
such rays, of which 243 have at least one factor in the nonstabilizer packet.
The tangent calculation below closes all of them: every product minimizer is
a strict local minimum even against unrestricted entangled perturbations.
Thus a counterexample to (202), if one exists, is separated from the entire
product-minimizing set.  No external result is used in this round.

For \(s\in\{1,-1\}\), let \(\mathscr S_s\) be the nine stabilizer
minimizers from Lemma 74 and put

\[
 \mathscr N_s=\mathcal M_s\setminus\mathscr S_s.             \tag{430}
\]

Thus \(\mathscr N_s\) is the nine-ray nonstabilizer packet in Proposition
63.

### Lemma 80 (the four product symmetry types)

The input symmetries generated by the qutrit Weyl unitaries and the Clifford
unitary \(U_s\) in Lemma 73 act transitively on each of
\(\mathscr S_s\) and \(\mathscr N_s\).  Consequently the 324 product
minimizers in (345) split into the four product-symmetry orbits

\[
 \mathscr S_+\mathbin\times\mathscr S_-,\quad
 \mathscr S_+\mathbin\times\mathscr N_-,\quad
 \mathscr N_+\mathbin\times\mathscr S_-,\quad
 \mathscr N_+\mathbin\times\mathscr N_-,                 \tag{431}
\]

each containing 81 rays.

**Proof.**  Transitivity on \(\mathscr S_s\) is Lemma 74.  Every generator
is a channel symmetry by (400)--(401), so it preserves the full minimizing
set.  It also preserves the stabilizer packet: Weyl unitaries and the
Clifford \(U_s\) map Weyl eigenrays to Weyl eigenrays.  Hence its complement
\(\mathscr N_s\) is invariant.

Fix \([x]\in\mathscr N_s\).  Its orbit under the nine Weyl unitaries has
nine distinct rays.  Indeed, if a nonidentity Weyl unitary fixed \([x]\),
then \([x]\) would be one of its eigenrays and hence a stabilizer ray, a
contradiction.  Since \(|\mathscr N_s|=9\), this Weyl orbit is all of
\(\mathscr N_s\).  Independent symmetries in the two channel factors now
give the four orbits in (431), each of size \(9^2\). \(\square\)

We next record the finite tangent calculation used at one representative of
each orbit.  Let

\[
 x_{\rm st}=e_0,\qquad
 x_{\rm ns}={1\over\sqrt3}C(1,\xi,\xi^2)^T,
 \qquad y_t=P\overline{x_t}\quad(t\in\{\mathrm{st},\mathrm{ns}\}),
                                                                    \tag{432}
\]

where \(C,\xi,P\) are as in (336)--(337).  For a unit vector \(x\), define

\[
 V_{s,x}:\mathbb C^3\longrightarrow\mathbb C^3,\qquad
 V_{s,x}e_i={U_i^{(s)}x\over\sqrt3},\qquad
 (U_1^{(s)},U_2^{(s)},U_3^{(s)})=(I,Z,X^s).                 \tag{433}
\]

When \(x\) is a minimizer, \(V_{s,x}\) has rank two.  Let \(c_{s,x}\)
span its kernel, let \(R_{s,x}=\operatorname {ran}V_{s,x}\), and define
the one-channel tangent leakage

\[
 \ell_{s,x}(a)=P_{R_{s,x}^{\perp}}V_{s,a}c_{s,x},
 \qquad a\in x^\perp.                                      \tag{434}
\]

The phase and normalization of \(c_{s,x}\) will be chosen so that it is a
unit vector; neither affects its kernel.

### Lemma 81 (exact four-representative tangent data)

For \(x=x_{\rm st},x_{\rm ns}\) and the corresponding representatives for
either sign \(s\),

\[
 \operatorname {spec}(V_{s,x}V_{s,x}^*)=(2/3,1/3,0),
 \qquad
 \operatorname {spec}(\ell_{s,x}^*\ell_{s,x})=(1/2,0).
                                                                    \tag{435}
\]

Let \(a_{s,x}\) be a unit vector spanning \(\ker\ell_{s,x}\).  The Weyl
operator

\[
 W_s=X^sZ                                                     \tag{436}
\]

represents the one projective Weyl line omitted by the three pairwise
overlaps of \(I,Z,X^s\).  Directly at all four one-channel representatives,

\[
 \langle x,W_sx\rangle=0,\qquad
 \left|{d\over dt}\bigg|_{t=0}
 \left\langle {x+ta_{s,x}\over\sqrt{1+t^2}},
 W_s{x+ta_{s,x}\over\sqrt{1+t^2}}\right\rangle\right|=1.  \tag{437}
\]

For \(\psi_{r,t}=x_r\otimes y_t\), let \(\mathcal Q_{r,t}\) be the
product tangent-leakage map defined as in (316), with \(V_{\psi_{r,t}}\)
formed from the nine errors of \(\Phi_1\otimes\Phi_{-1}\).  Then

\[
 \ker\mathcal Q_{r,t}
 =\operatorname {span}\{a_{1,x_r}\otimes y_t,
                          x_r\otimes a_{-1,y_t}\}           \tag{438}
\]

inside \(\psi_{r,t}^{\perp}\).  In particular the kernel is always
two-dimensional.  The complete squared singular-value lists are

\[
\begin{array}{c|c}
(r,t)&\operatorname {spec}(\mathcal Q_{r,t}^*\mathcal Q_{r,t})\\
\hline
(\mathrm{st},\mathrm{st}),\ (\mathrm{ns},\mathrm{ns})
 &0,0,\frac13,\frac12,\frac12,\frac7{12},\frac7{12},\frac34\\
(\mathrm{st},\mathrm{ns}),\ (\mathrm{ns},\mathrm{st})
 &0,0,\frac{13}{36},\frac12,\frac12,
       \frac59,\frac59,\frac79.
\end{array}                                                   \tag{439}
\]

Finally, along the exceptional one-channel direction,

\[
 S\!\left(\Phi_s\left(
 { |x+ta_{s,x}\rangle\langle x+ta_{s,x}|\over1+t^2}
 \right)\right)
 =h_2(2/3)+{\log2\over3}t^2+o(t^2).                        \tag{440}
\]

**Proof.**  Everything through (439) is a finite calculation in the
cyclotomic field \(\mathbb Q(\xi)\).  Substitution of (432) into (433),
using

\[
 \xi^3=\omega,\qquad \xi^6+\xi^3+1=0,
\]

gives (435) and (437).  For the product map, the characteristic polynomials
of \(\mathcal Q^*\mathcal Q\) reduce respectively to

\[
 \lambda^2(\lambda-1/3)(\lambda-1/2)^2
       (\lambda-7/12)^2(\lambda-3/4)
\]

and

\[
 \lambda^2(\lambda-13/36)(\lambda-1/2)^2
       (\lambda-5/9)^2(\lambda-7/9),
\]

which proves (439).  There is also a structural check on its two zero
directions.  Since
\(V_{\psi_{r,t}}=V_{1,x_r}\otimes V_{-1,y_t}\), its coefficient-space
kernel is the sum of

\[
 (\ker V_{1,x_r})\otimes\mathbb C^3,
 \qquad
 \mathbb C^3\otimes(\ker V_{-1,y_t}).                      \tag{441}
\]

Equation (434) shows that each vector on the right of (438) maps (441) into
\(R_{1,x_r}\otimes R_{-1,y_t}\), so both belong to
\(\ker\mathcal Q_{r,t}\).  They are orthogonal.  The nullity two in
(439) proves that they exhaust the tangent kernel, giving (438).

It remains to derive the entropy coefficient.  The Weyl Parseval calculation
used in (338), now for either sign, gives for every unit vector \(z\)

\[
 \operatorname {Tr}\Phi_s(|z\rangle\langle z|)^2
 ={5\over9}-{2\over9}|\langle z,W_sz\rangle|^2.             \tag{442}
\]

Because \(a_{s,x}\) has zero leakage in (434), the eigenvalue issuing from
zero is \(O(t^4)\).  Equations (437)--(442), together with trace one, then
force the other two eigenvalues to be

\[
 {2\over3}-{t^2\over3}+o(t^2),\qquad
 {1\over3}+{t^2\over3}+o(t^2).                             \tag{443}
\]

Applying \(-u\log u\) to (443) proves (440). \(\square\)

### Proposition 82 (all 324 product minimizers are strict local minima)

For every \([x]\in\mathcal M_+\) and \([y]\in\mathcal M_-\), there is
an open projective neighborhood \(\mathcal U_{x,y}\) of \([x\otimes y]\)
such that

\[
 S((\Phi_1\otimes\Phi_{-1})(|\psi\rangle\langle\psi|))>H_* \tag{444}
\]

for every \([\psi]\in\mathcal U_{x,y}\) distinct from
\([x\otimes y]\).  Hence a hypothetical entropy counterexample has a
positive projective distance from the finite set of all 324 product
minimizers.

**Proof.**  By Lemma 80 it suffices to treat the four representatives in
(432).  Use the affine chart (353) at
\(\psi_0=\psi_{r,t}\), and split its tangent variable as

\[
 \delta=v+u,\qquad v\in\ker\mathcal Q_{r,t},\quad
 u\perp\ker\mathcal Q_{r,t}.                               \tag{445}
\]

The positive eigenvalues in (439) give a constant \(c>0\) such that
\(\|\mathcal Q_{r,t}(u)\|_2^2\ge c\|u\|^2\).  The Schur-complement
argument in (359)--(360) therefore applies without change: the total mass
\(q(\delta)\) of the five output eigenvalues issuing from zero obeys

\[
 q(\delta)\ge c_1\|u\|^2-c_2\|\delta\|^4,                 \tag{446}
\]

and every such eigenvalue is \(O(\|\delta\|^2)\), uniformly in direction.

On the exceptional plane, (438) writes

\[
 v=\alpha a_{1,x_r}\otimes y_t
       +\beta x_r\otimes a_{-1,y_t}.                       \tag{447}
\]

Take the product of the two normalized one-channel curves with tangents
\(\alpha a_{1,x_r}\) and \(\beta a_{-1,y_t}\).  Entropy is additive on
this product curve, so (440) gives

\[
 H_*+{\log2\over3}(|\alpha|^2+|\beta|^2)t^2+o(t^2)
 =H_*+{\log2\over3}\|v\|^2t^2+o(t^2).                    \tag{448}
\]

The four positive output eigenvalues form an analytic spectral cluster.
Its entropy has zero first variation at \(\psi_0\).  To see this directly,
one-channel first-order optimality says that the adjoint of the supported
output logarithm maps each minimizing vector to a scalar multiple of itself.
On the product support the logarithm is
\(\log\sigma_x\otimes I+I\otimes\log\sigma_y\); its adjoint therefore
maps \(x\otimes y\) to a scalar multiple of \(x\otimes y\), and pairs to
zero with every projective tangent.  Consequently the quadratic restriction
depends only on the tangent, not on the second-order completion of the
curve.  Equation (448) is therefore the quadratic restriction of the old
spectral-cluster entropy in the affine chart (445).

The two-chart argument in the proof of Proposition 67 now applies verbatim.
When \(\|u\|=O(\|\delta\|^2)\), the positive quadratic form (448) controls
the entropy.  Otherwise (446) contributes

\[
 c_3\|u\|^2\log {1\over C\|\delta\|^2},                   \tag{449}
\]

which absorbs the mixed and cubic Taylor remainders of the old cluster.
After one uniform reduction of the neighborhood, (444) follows at each of
the four representatives.  The input symmetries in Lemma 80 transport these
neighborhoods to all 324 product minimizers.  Since that set is finite, the
neighborhoods may be shrunk to contain metric balls with one common positive
radius.  This proves the distance assertion. \(\square\)

The finite tangent ranks were checked in two independent ways.  First,
floating matrix construction gave the spectra in (435) and (439):

```text
st st rankV= 4 QstarQ= [0.0, 2.5930849268899457e-17, 0.33333333333333304, 0.4999999999999997, 0.5000000000000002, 0.5833333333333331, 0.5833333333333334, 0.7499999999999999]
st ns rankV= 4 QstarQ= [8.281405608609407e-18, 8.416204589997485e-17, 0.3611111111111112, 0.49999999999999983, 0.4999999999999999, 0.5555555555555552, 0.5555555555555559, 0.7777777777777777]
ns st rankV= 4 QstarQ= [0.0, 6.431769209088793e-17, 0.361111111111111, 0.49999999999999983, 0.5000000000000002, 0.555555555555555, 0.5555555555555556, 0.777777777777777]
ns ns rankV= 4 QstarQ= [0.0, 1.2881968172993996e-17, 0.3333333333333332, 0.4999999999999999, 0.5000000000000002, 0.5833333333333327, 0.5833333333333334, 0.7499999999999998]
1 st rank_leak= 1 nonzero_sq= 0.5 omitted_derivative_sq= 1.0
1 ns rank_leak= 1 nonzero_sq= 0.5 omitted_derivative_sq= 1.0
-1 st rank_leak= 1 nonzero_sq= 0.5 omitted_derivative_sq= 1.0
-1 ns rank_leak= 1 nonzero_sq= 0.5 omitted_derivative_sq= 1.0
```

Second, the condition \(\mathcal Q(\eta)=0\) was written without
orthogonal projections: \(V_\eta\) must map \(\ker V_{\psi_0}\) into
\(\operatorname {ran}V_{\psi_0}\).  The resulting 25-by-9 linear system
has coefficients in \(\mathbb Q(\xi)\).  Reducing it at three primes that
contain a primitive ninth root gives rank six each time.  The three-dimensional
full kernel consists of the radial vector and the two directions in (438),
so these modular lower bounds, together with the explicit upper bound, also
certify the characteristic-zero rank.  Here is the verbatim `python3`
output:

```text
prime 19 zeta9 4
st st (4, 4, 5, 5, 6, 3)
st ns (4, 4, 5, 5, 6, 3)
ns st (4, 4, 5, 5, 6, 3)
ns ns (4, 4, 5, 5, 6, 3)
prime 37 zeta9 7
st st (7, 4, 5, 5, 6, 3)
st ns (7, 4, 5, 5, 6, 3)
ns st (7, 4, 5, 5, 6, 3)
ns ns (7, 4, 5, 5, 6, 3)
prime 73 zeta9 2
st st (2, 4, 5, 5, 6, 3)
st ns (2, 4, 5, 5, 6, 3)
ns st (2, 4, 5, 5, 6, 3)
ns ns (2, 4, 5, 5, 6, 3)
```

After the prime and the chosen ninth root, each tuple reports, in order,
the rank of \(V_{\psi_0}\), its right nullity, its left nullity, the rank
of the leakage equations, and their full-space nullity.

The orbit count in Lemma 80 was also checked directly:

```text
s = 1 nonstabilizer_Weyl_orbit_size = 9
s = -1 nonstabilizer_Weyl_orbit_size = 9
product_orbit_types = [('st', 'st', 81), ('st', 'ns', 81), ('ns', 'st', 81), ('ns', 'ns', 81)]
total_product_minimizers = 324
```

### Entanglement-constrained falsification attempt

To look beyond the now-excluded local basins, the entropy was minimized over
all complex vectors in \(\mathbb C^9\) subject to a lower bound on the input
linear entanglement

\[
 E(\psi)=1-\operatorname {Tr}(\psi_A^2).                    \tag{450}
\]

For each displayed floor, eight independent complex Gaussian starts were
optimized with the exact inequality constraint \(E(\psi)\ge E_0\).  No
run descended below \(H_*\); every best point saturated the imposed
entanglement floor.  This is a finite numerical search, not a proof of a
global constrained minimum.  The output is verbatim from `python3`/`scipy`:

```text
floor=0.01 starts=8 converged=8 best_entropy=1.286940990566 margin=0.013912653976 achieved_linear_entropy=0.010000000008
floor=0.05 starts=8 converged=8 best_entropy=1.330527043262 margin=0.057498706673 achieved_linear_entropy=0.050000000001
floor=0.10 starts=8 converged=8 best_entropy=1.378665322724 margin=0.105636986134 achieved_linear_entropy=0.100000000002
floor=0.20 starts=8 converged=8 best_entropy=1.460977075015 margin=0.187948738425 achieved_linear_entropy=0.199999999999
floor=0.40 starts=8 converged=8 best_entropy=1.590253001824 margin=0.317224665234 achieved_linear_entropy=0.399999999999
floor=0.60 starts=8 converged=8 best_entropy=1.717201210992 margin=0.444172874403 achieved_linear_entropy=0.599999999999
```

The obstruction to a counterexample is now exact locally and still open
globally.  Product inputs cannot violate (202), and Proposition 82 gives a
uniform punctured neighborhood of all 324 equality rays on which no
entangled descent is possible.  The constrained search supplies evidence
that increasing Schmidt entanglement raises rather than lowers the entropy,
but it has no global certificate.  A surviving counterexample must therefore
lie in a disconnected entangled basin, a positive distance from every
product minimizer, and must exploit the higher Weyl cycles in (303) despite
the sharp collision identity (293).  No proved inequality excludes such a
basin **[UNPROVED]**.

## Round 2026-08-21: named Brascamp--Lieb reduction of the qutrit lemma

The single load-bearing statement in the qutrit branch is the global half of
(202), namely

\[
 S_{\min}(\Lambda)\ge H_*,\qquad
 \Lambda=\Phi _1\otimes\Phi _{-1},\qquad
 H_*=2\log3-{4\over3}\log2.                                \tag{451}
\]

It has an exact one-variable formulation supplied by a named external
theorem.  The result used here is Corollary 3.7 (``Minimum output entropy'')
of Berta--Sutter--Walter, which is an application of their Theorem 2.1
(``Quantum Brascamp--Lieb duality''):
[M. Berta, D. Sutter, and M. Walter, *Quantum Brascamp--Lieb
Dualities*, Commun. Math. Phys. 401 (2023), Corollary
3.7](https://link.springer.com/article/10.1007/s00220-023-04678-w#Sec11).
The cited corollary applies to every finite-dimensional trace-preserving
completely positive map \(\Omega\) and states

\[
 S_{\min}(\Omega)
 =-\sup_{\tau\in\mathcal D_{++}}
       \lambda_{\max}\!\left(\Omega^*(\log\tau)\right),    \tag{452}
\]

where restricting the supremum to full-support output states is harmless;
singular states are obtained by a full-support limit.  This is also the
external theorem underlying the internally proved Gibbs formula (413), but
(452) identifies the exact single spectral inequality to which (451)
reduces.

### Proposition 83 (precise external-theorem reduction)

For \(\tau\in\mathcal D_{++}(\mathbb C^9)\), put

\[
 b(\tau)=\lambda_{\max}\!\left(\Lambda^*(\log\tau)\right).
                                                                    \tag{453}
\]

Then (451), and hence equality in (202), is equivalent to the single
uniform inequality

\[
 b(\tau)\le -H_*\qquad
       \text{for every }\tau\in\mathcal D_{++}(\mathbb C^9).       \tag{454}
\]

The constant in (454) is sharp: \(\sup_\tau b(\tau)\ge-H_*\).
Thus no attainment assertion is hidden in the reduction, and the sole
remaining direction is the upper bound in (454) **[UNPROVED]**.

**Proof.**  The channel \(\Lambda\) is an average of nine unitary
conjugations and is therefore trace preserving and completely positive, so
all hypotheses of the cited Berta--Sutter--Walter corollary hold.  Formula
(452) gives

\[
 S_{\min}(\Lambda)=-\sup_{\tau\in\mathcal D_{++}}b(\tau),          \tag{455}
\]

which proves the equivalence of (451) and (454).

It remains to verify sharpness rather than assume that the supremum in
(455) is attained.  Let

\[
 \sigma_*:=\Lambda(|00\rangle\langle00|),\qquad
 \tau_\varepsilon={\sigma_*+\varepsilon I_9\over1+9\varepsilon}
 \quad(\varepsilon>0).
\]

The nonzero spectrum of \(\sigma_*\) is
\((4/9,2/9,2/9,1/9)\).  By adjointness and the Rayleigh principle,

\[
 \begin{split}
 b(\tau_\varepsilon)
 &\ge \langle00|\Lambda^*(\log\tau_\varepsilon)|00\rangle\\
 &=\operatorname {Tr}(\sigma_*\log\tau_\varepsilon)
 \longrightarrow \operatorname {Tr}(\sigma_*\log\sigma_*)=-H_*.
 \end{split}                                                     \tag{456}
\]

Hence \(\sup_\tau b(\tau)\ge-H_*\), as claimed. \(\square\)

The reduction is completely explicit in the Weyl basis.  For
\(W_{p,q}=X^pZ^q\), put

\[
 \varphi_s(p,q)={1+\omega^p+\omega^{-sq}\over3},
 \qquad p,q\in\mathbb F_3.
\]

Direct conjugation gives

\[
 \Phi_s^*(W_{p,q})=\overline{\varphi_s(p,q)}W_{p,q},
\]

and therefore

\[
 \Lambda^*(W_{p,q}\otimes W_{r,t})
 =\overline{\varphi_1(p,q)\varphi_{-1}(r,t)}
      (W_{p,q}\otimes W_{r,t}).                              \tag{457}
\]

If \(H=H^*\in M_9\), write

\[
 H=\sum_{p,q,r,t}\widehat H_{p,q,r,t}
                  W_{p,q}\otimes W_{r,t},\qquad
 \widehat H_{p,q,r,t}={1\over9}\operatorname {Tr}
 [(W_{p,q}\otimes W_{r,t})^*H].
\]

Taking \(\tau=e^H/\operatorname {Tr}e^H\) in (454), using unitality of
\(\Lambda^*\), and substituting (457) shows that the remaining statement is
exactly the following Young-type matrix-exponential inequality:

\[
 \lambda_{\max}\!\left(
 \sum_{p,q,r,t}
 \overline{\varphi_1(p,q)\varphi_{-1}(r,t)}
 \widehat H_{p,q,r,t}W_{p,q}\otimes W_{r,t}
 \right)
 \le \log\operatorname {Tr}e^H-H_*                         \tag{458}
\]

for every Hermitian \(H\in M_9\).  Conversely, every full-support
\(\tau\) occurs from \(H=\log\tau\), so (458) loses no cases.  In the
terminology of the cited paper, (458) is precisely the analytic
Brascamp--Lieb form of the entropy assertion, specialized to the two
qutrit Weyl triangles.  It is stronger than all stabilizer-MASA restrictions
proved in Proposition 77 and is not implied by the collision multiplier
histogram alone.

The finite Weyl bookkeeping and the adjoint convention in (457) were checked
with exact cyclotomic arithmetic.  Here is the verbatim `python3` output:

```text
s = 1 single_abs_multiplier_squared_histogram = {'0': 2, '1': 1, '1/3': 6}
s = 1 zero_modes = [(1, 1), (2, 2)]
s = -1 single_abs_multiplier_squared_histogram = {'0': 2, '1': 1, '1/3': 6}
s = -1 zero_modes = [(1, 2), (2, 1)]
product_abs_multiplier_squared_histogram = {'0': 32, '1': 1, '1/3': 12, '1/9': 36}
adjoint_multiplier_identity_all_18_modes = True
product_modes_count = 81
exp_minus_Hstar = 2^(4/3)/9
product_witness_entropy_symbolic = 2*log(3)-4*log(2)/3
```

Thus the earlier descriptions in terms of a disconnected entangled basin or
uncontrolled higher Weyl cycles are now subsumed by one sharp statement:
prove (458), equivalently (454).  The named quantum Brascamp--Lieb theorem
proves that this matrix inequality is neither merely sufficient nor a
relaxation; it is exactly the unresolved global lemma.

## Round W (web, 2026-08-21) — appended from web session [chat 6a88bba9, 6m33s]
Qutrit branch: uniform protection of every binary-spectrum Hamiltonian. Lemma 84 (collision cap ⇒ projector
mass window), Lemma 85 (exact binary conjugate E_r), Proposition 86 (F(H) > H* + 1/100 for ALL ≤2-level H,
exact-fraction certification with 61-term atanh enclosures; r=3 the close call at margin 0.0135), Corollary 87
(2-Lipschitz ⇒ 1/200 operator-norm tube protected). Consequence: any counterexample to (458) is genuinely
≥3-level and ≥1/200 from every binary-spectrum Hamiltonian; the collision optimizer's 3+1+5 flag family is
the next target [UNPROVED]. Full capture: webtransfer/rounds/additivity-gap_W1_capture.md

## Round W2 (web, 2026-08-21) — appended from web session [chat 6a88bba9, 6m2s]
3+1+5 flag family. Lemma 88: exact joint collision ellipse + support function. Lemma 89: two-variable Gibbs
conjugate. Proposition 90 (negative result, load-bearing): the collision-only relaxation bottoms out at
H_9(25/81)=1.22320 < H*=1.27303 with minimizer exactly the 3+1+5 collision-optimizer spectrum (q5*=0) — the
generic relaxation is insufficient in the most literal way. Proposition 91: all forty stabilizer-MASA flags
uniformly protected, δ_st=(1/9)log(3888/3125)>1/50, sharp at the product edge–edge histogram; the 3+1
multiplicity split removes Prop 77's zero-margin degeneracy. A flag counterexample must be non-stabilizer and
exploit channel data beyond the collision ellipse; that case remains [UNPROVED]. Full capture:
webtransfer/rounds/additivity-gap_W2_capture.md

## Round W3 (web, 2026-08-21) — appended from web session [chat 6a88bba9, 20m59s]
Third moment exhausted; no perturbative escape. Prop 92: exact one-qutrit third moment 10/27 (Weyl/Gram +
Newton identities, explicit attainer). Prop 93: two-qutrit M₃ bracketed in [100/729, 19/243+112√2/2187];
equality at the product value [UNPROVED]. Prop 94 (load-bearing negative): the 3+1+5 collision optimizer's
third moment lies strictly below 100/729 ≤ M₃, so the exact third-moment cap leaves the relaxed minimum
unchanged — two-moment information cannot settle the flag family. Lemma 95 + Prop 96: at the worst stabilizer
flag the full 46-dimensional second variation is eventually positive definite (Q₀ PSD with 10-dim kernel,
exactly factored; kernel lifted with generalized eigenvalues 2/3,(4±2√2)/9; limiting λ_min = log(12/5)(4−2√2)/9
≈ 0.11396) — no infinitesimal non-stabilizer escape; nonlinear hunts find no descent. Open: global (458) on
finite-distance non-stabilizer flags. Full capture: webtransfer/rounds/additivity-gap_W3_capture.md

## Round W4 (web, 2026-08-21) — appended from web session [chat 6a88bba9, 8m5s]
Certified-covering attempt on the non-stabilizer 3+1+5 flags: global brute-force certification is
INFEASIBLE this round (fundamental-domain grid 77⁶ ≈ 2.1×10¹¹ points; even after quotienting, the required
uniform cover needs ≈1.43×10⁸ oracle calls > 10⁷ budget). Delivered instead the sharpest partial covering
theorem: explicit certified tubes — operator-norm radius 1/820 around the product edge–edge stabilizer orbit
and 1/100 around all other stabilizer 3+1+5 orbits — with separation check and exact 121-term atanh Fraction
arithmetic throughout. The surviving set is explicit: 𝔉_rem = 𝔉 \ [{d(P,𝔖_ee) ≤ 1/820} ∪ {d(P,𝔖_other) ≤ 1/100}].
Every counterexample to (458), if one exists, lies in 𝔉_rem. The exact per-cell oracle (554)–(566) gives an
adaptive-certification route, but confining its low-margin cells to a computationally manageable submanifold
(or finding one certified low-oracle cell in 𝔉_rem) remains [UNPROVED]. Full capture:
webtransfer/rounds/additivity-gap_W4_capture.md

## Round W5 (web, 2026-08-21) — appended from web session [chat 6a88bba9, 10m28s]
KKT collapse of the flag search. Lemma 103 (exact critical-flag equations): [H,σ]=0 with
H=aP₃+bP₁, minimizing input = top eigenvector of Λ*(H), density ordering must match output
eigenvalue ordering. Prop 104: the 46 flag coordinates DISAPPEAR — at any counterexample
minimizer the flag consists of contiguous spectral blocks of its own output state σ_x; search
drops 62 → 16 real dims (ℂP⁸), six possible orderings. Prop 105 (exact scalar sectors): five of
six orders excluded with certified margins (collision endpoints; d₅-largest killed by
majorization E≥log5=H*+0.336); ONLY d₃>d₁>d₅ survives. Prop 106 (2-dim mass window): any
counterexample needs 93/100<q₃≤1/3+4√2/9<481/500, 0≤q₅<1/50, 9/500<q₁<7/100 (exact-fraction
enclosures, 161-term atanh). Prop 107: interior case confined to explicit algebraic
self-consistency locus (I−|x⟩⟨x|)B(x)x=0 on ℂP⁸ (8 complex equations, dim-0 [UNPROVED]).
Prop 108: boundary case q₅=0 on determinantal variety Z₄ (5×5 minors of Weyl orbit matrix);
local components through product reps have complex dim ≤2; remote component [UNPROVED].
Corollary 109 (NEW single-inequality target): Ky-Fan ν₍₃₎(Λ)≤8/9 would close the ENTIRE 3+1+5
family (counterexample needs q₃>93/100>8/9); 150 BFGS starts hit exactly 8/9 with product
maximizers, 120 more starts on the forced spectral functional never entered the window. Honest
refusal to quote a "coverage fraction" (fibers of unknown dimension). Next target: eq (651)
ν₍₃₎(Λ)=8/9 [UNPROVED]. Full capture: webtransfer/rounds/additivity-gap_W5_capture.md

## Round W6 (web, 2026-08-21) — appended from web session [chat 6a88bba9, 47m15s]
Ky-Fan campaign: target 93/100 NOT reached, but two exact new theorems. Prop 110 (exact SDP dual):
ν₍₃₎(Λ)=max_{rank-3 P} λ_max(Λ*(P)); target ⟺ Λ*(P)≤(93/100)I uniformly. **Prop 112 (sharp
separable theorem): max over separable ρ of κ₃(Λ(ρ)) = 8/9** — proof by exact classification of
the four 3-edge patterns in the 3×3 product-spectrum grid; hardest (L-shape) killed by an exact
SOS identity with positive-definite quartic form R (Sylvester minors 1,3/4,1/2,1/4); equality
forces spectra (2/3,1/3,0)² = product input |00⟩. So any violation must come from input
entanglement. Prop 114: entanglement-dependent collision certificate Tr Λ(ρ)²≤13/81+4p/27 ⇒
κ₃≤A(p)=1/3+2√(6p+2)/9 (recovers old bound at p=1). Lemmas 115–116 + Prop 117: Schmidt-dephasing
splits ρ=ρ₀+Δ with |Δ|₂²=1−p and Δ purely nonlocal-Weyl; projector nonlocal energy N(P)≤18 trades
off against product capture D(N); stability bound κ₃≤8/9+C₀√(1−p), C₀=(5+√21)/24. **Theorem 118:
certified global constant ν₍₃₎(Λ) ≤ c_W6 = 0.95531475083791116... (unique root of an explicit
quartic in (93/100,239/250), root location certified by exact sign evaluations); bracket
8/9 ≤ ν₍₃₎ ≤ c_W6 < 239/250.** Prop 119 (route closure): second+third-moment caps rigorously
CANNOT go below the old collision relaxation (explicit fake spectrum whose third moment is below
the attained 100/729). Exact remaining gap: uncontrolled inputs have Schmidt purity
p>208369/240000≈0.868; minimal missing lemma = quadratic stability κ₃≤8/9+C₂(1−p) with
C₂≤29600/94893≈0.3119 (eq 717) [UNPROVED] — or the sharper Λ*(P)≤(8/9)I. Either closes the whole
(3+1+5) family. Full capture: webtransfer/rounds/additivity-gap_W6_capture.md

## Round W7 (web, 2026-08-21) — appended from web session [chat 6a88bba9]
Stability lemma (718) NOT proved, but the certified constant takes a huge step: **ν₍₃₎(Λ) ≤ c₇ =
0.93411276499640…** (unique root of 2187c⁴−1458c³−621c²+1440c−1280, rational sign certificates)
— gap to 93/100 now just 0.00411. Two new exact tools: **Lemma 120** exact omitted-Weyl identity
Tr Λ(ρ)² = (13+12p−W(ψ))/81 with W ≥ 3(1−p) via the explicit decomposition W−3(1−p) =
15R+9C−8+6D (killed-line bases, pinching + Cauchy-Schwarz); ⇒ **Cor 121** improved collision cap
(10+15p)/81, κ₃ ≤ 1/3+√(30p+2)/9. **Prop 123** maximizer Schmidt-overlap inequality q·λ₁ ≤ 8/9
(effect B=A/q ≥ |ψ⟩⟨ψ| at the global maximizer + separable 8/9 theorem). Intersecting the two
monotone bounds ⇒ Theorem 124 (c₇). **Cor 125**: any violation of 93/100 has λ₁ ∈
(0.94416, 0.95579) and p ∈ (0.89456, 0.91550) — NOT asymptotically product, so infinitesimal
stability alone can never finish. **Prop 122**: full Hessian at |00⟩ strictly negative definite
(eigenvalues −3/2, −32/27, −7/6, −2/3, −1/9 with multiplicities 2,2,4,4,4); entangling-direction
ratio limsup (K−8/9)/(1−p) ≤ −7/24 — the √(1−p) loss is an artifact; certified radius missing.
Exact remaining target: Fourier-energy estimate **W(ψ) ≥ 3(1−p)+15(p−p₀), p₀=268369/300000
(774)** on the band — the gain must come from 15R+9C−8 or the Cauchy deficit D (775). Full
capture: webtransfer/rounds/additivity-gap_W7_capture.md

## Round W8 (web, 2026-08-21/22) — appended from web session [chat 6a88bba9, 30m58s]
双向收获:**Prop 126 精确证伪了上一轮提出的带上 Fourier 估计 (774)**(带内反例:Schmidt 谱
(19/20,1/40,1/40)、R=C=1/3 的均匀展布矩阵,W=0.3554 < 0.4266)——该路线死。改走投影稳定性:
**Lemma 127** 三边积投影的对偶范数一致界 λ_max(Λ*(Q)) ≤ β=(11+8√3)/27=0.92061(L 形经
e+f−ef≤2α−α²);**Lemma 128** 近积等式 ⇒ 谱隙 λ₃−λ₄>1/12 + 投影对齐 ‖Λ*(P−Q)‖∞ ≤ √(8δ);
**Theorem 129 自举**:q>c₈ ⇒ λ₁>0.95157 ⇒ δ<2.28e−5 ⇒ q ≤ β+√(8δ₀) < c₈ 矛盾,
**c₈ = 0.93410411**(全有理证书),改进 c₇−c₈ ≈ 8.65e−6——诚实标注"认证但微小"。带上数值侦察:
经验最大 κ₃ = 0.8654(远低于 0.93),支配积分量恰在 8/9 等式几何。剩余瓶颈被精确定位:平方根
对齐损失 (823);充分替代 = **线性稳定性 (824) [UNPROVED]**:λ_max(Λ*(P)) ≤ β +
C[κ₃(τ)−Tr(Pτ)],C ≤ 0.8683(精确阈 0.8683468984)——即积等式几何处的二阶投影稳定性,一条
证出即封全族。Full capture: webtransfer/rounds/additivity-gap_W8_capture.md

## Round W9 (web, 2026-08-22) — appended from web session [chat 6a88bba9, ~2h (最长一轮)]
(827) 线性投影稳定性仍 [UNPROVED],但无穷小层面完全打通 + 第三矩武器化。**Prop 130(等式积
投影处的精确 Grassmann Hessian)**:切空间实维 36(纠正提示里的 24);广义谱对
(H, D)(alignment-loss 归一)全负——本征值 −1(×20), −7/8(×4), −6/7(×2), −3/4(×2),
−3/8±√105/40(×4,×4);最大 (√105−15)/40 ≈ −0.1188 < 0:每个无穷小投影旋转都使
λ_max(Λ*(P)) 相对对齐损失下降——比所要的 0.8683 系数强得多(符号相反)。**Cor 131**:规范等式
点显式有限盆 ‖P−Q₀‖₂ ≤ 1/20 内 λ_max < β(有理证书 453²−3·260²=2409>0)——局部无余项问题。
**Lemma 132**:一 qutrit 三阶矩强化每个 rank-one 效应:‖Φ_s*(R)‖∞ ≤ α₃ < 0.7143592
(81x³+81x²−81x−13 的根)⇒ 强化三边界 ⇒ **c₉ = 46705053/50000000 = 0.93410106**
(c₈−c₉ = 61/2e7 ≈ 3.05e−6——增量已趋饱和:c₇ 0.93411276 → c₈ 0.93410411 → c₉ 0.93410106)。
精确定位剩余缺口:小对齐区 d≤1/7200 与大对齐区都已覆盖,**中间有限环带未认证**;所需为
"L 形积投影的一致有限半径稳定性定理"——把等式轨道处的严格负 Hessian 沿可分亏损
8/9−κ₃(τ) 控制的半径传播到整个 κ₃(τ)>7/8 区域(同时控制 λ_max、谱隙、二阶导 (885))。
非稳定等式型的 Hessian 数值侦察(≤ −1/9)未入证明,统一 cyclotomic 认证 [UNPROVED]。
Full capture (含画布累积文档 W7-W9): webtransfer/rounds/additivity-gap_W9_capture.md

## Round W10 (web, 2026-08-22) — appended from web session [chat 6a88bba9, 19m36s]
一致连续化 [UNPROVED],但三项严格推进 + 一个关键"负面"发现。**Prop 135**:四个等式型 Hessian
全部 cyclotomic 精确认证(ℚ(ξ),ξ=e^{2πi/9};(st,st) 最大 (√105−15)/40,其余三型恰 −1/9)。
**Lemma 136**:κ₃>7/8 全区域一致谱隙 λ₃−λ₄ > 1/12(L 形被迫;x₂+y₂<1/24 论证)。**Prop 137**:
线性估计 (824)(C=0.8683)在两端都已成立——小对齐 d≤6.04e−7、大对齐 d≥0.01554——**只剩紧致
中环带 (906)**。**Prop 138-140**:四等式轨道周围一致有限半径延拓(H_U ≤ −D_U/20,显式三阶导
Taylor),但半径极小(酉半径 ~1e−5,输入盆 1/8e6——诚实记录"generic 算子范数延拓极其局部");
**Prop 141** 给出精确阻塞常数(三次方程 947 的根 δ* ≈ 4.0e−5)——是方法的障碍,非命题的障碍。
**关键侦察 [NUMERICAL ONLY]**:在 x=e₀, y=(5,1,0)/√26(κ₃=0.878)处广义 Hessian 最大本征值
**+0.0248 为正**——等式处的全负 Hessian 在 κ₃=7/8 前真实变号:环带上的证明必须把基线余量
β−λ_max(Λ*(Q)) 与曲率联合使用,不能要求一致负曲率。c₉ = 0.93410106 维持。缺失命题进一步收窄:
仅需在紧致环带 (950) 上证 (824)。Full capture: webtransfer/rounds/additivity-gap_W10_capture.md

## Round W11 (web, 2026-08-22) — appended from web session [chat 6a88bba9, ~4h 最长轮]
环带未闭,但结构再进两步 + 一个诚实的定量否定。**Lemma 142**:精化三边常数 β̂ = 0.9184093288
⇒ 一致基线余量 M ≥ m* = β−β̂ > 0(纠正 prompt 预设:等式处 λ_max Λ*(Q_eq) = 8/9 < β,余量
处处非零),线性版 c_M = 72m* ≈ 0.1583。**Prop 143(漂亮的精确重构)**:整个投影稳定性估计
等价于单条"倾斜 Ky-Fan"不等式 max_ρ κ₃(Λ(ρ)+Cτ) ≤ β+Cκ——Grassmann 参数彻底消失。
**Prop 145(定量否定)**:基线斜率桥接环带需 c_M ≈ 24.4,证得 0.158,差 154 倍;结论明确:
**曲率机制必须在 √d 松弛之前使用**。**Prop 146**:缺失步骤 = 有限一 qutrit 极小集(18 条射线)
的定量逆稳定性定理(R-形式控谱不控本征基)。**Theorem 147**:c₁₁ = 0.9341010588(+1.2e−9,
"数值上可忽略但精确")。侦察(30000 积输入):比率 (8/9−f_Q)/(8/9−κ₃) 从未低于 0.2545 ⇒
猜想 (997):λ_max Λ*(Q) ≤ 8/9 − δ_sep/4 [UNPROVED]——它将把插值起点从松的 β 换成正确的 8/9。
Full capture: webtransfer/rounds/additivity-gap_W11_capture.md

## Round W12 (web, 2026-08-22) — appended from web session [chat 6a88bba9, 11m8s]
一破一立。**Prop 148:目标 A (997) 精确证伪**——显式代数积输出(√(443/500)e₁+ω²√(57/500)e₂ ⊗ e₀,
Sturm 根隔离 + 高斯整数见证矢量 + 外向舍入 Fraction 区间)给出认证违反 0.00037,且比率 0.2234 <
9/40:任何 ≥0.225 的一致线性斜率不可能(W11 侦察 0.2545 漏掉了这条单参数边界族)。
**Prop 150:目标 B 证毕**——18 极小射线的定量逆稳定性,√ε 阶且阶数锐(精确 Jacobian 奇异值²
=(5±√13)/2 各二重,charpoly (z²−5z+3)²;相位稳定性引理 + 粗定位 + Taylor);
**Cor 151**:显式 δ₁ = 1/104000000² ≈ 9.25e−17 ⇒ W10 等式盆成立——诚实注记:半径太小,
不能独自桥接环带。结论方向:成功的余量+曲率论证必须保留 δ_sep 之外的一 qutrit 取向数据,
或直接攻倾斜 Ky-Fan 形式 (966)。c₁₁ = 0.9341010588 维持。
Full capture: webtransfer/rounds/additivity-gap_W12_capture.md

## Round W13 (web, 2026-08-22) — appended from web session [chat 6a88bba9, ~100min]
倾斜路线未闭但骨架建全:可分输入上的倾斜问题**带严格余量解决**(Prop 152);倾斜 KKT + 精确
Schmidt 带(p∈(0.8645,0.9335), λ₁∈(0.9269,0.9655));**Lemma 155 HS 刚性**(Tr A²≤5/3,第二
本征值仿射压制);**Prop 156 新取向限制**:任何倾斜违反者与锚积输入重叠 >3/5、与自身支配
Schmidt 积重叠 >1/2——这正是标量松弛缺失的取向信息;Prop 157 精确取向依赖倾斜碰撞界
(μ(τ) 乘性);**Prop 158 定量否定**:碰撞证书在等式锚处差 0.094、相干支需 p≥0.9937 而违反带
p<0.9335——两支之间留真实中间区。Cor 159 汇总紧致临界区 (1107)(四重限制)。侦察(246918 试验):
倾斜残差最大 0.888094 < 8/9,倾斜极大点本质为积态(1−λ₁≤3.9e−4)——**不进入**严格违反带;
猜想 (1108):倾斜积最优性 max ≤ 8/9 [UNPROVED](比所需更强)。c₁₁ 维持。
Full capture: webtransfer/rounds/additivity-gap_W13_capture.md
