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
