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
