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
