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
