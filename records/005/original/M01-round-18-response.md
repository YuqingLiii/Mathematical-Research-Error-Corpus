# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The one-dimensional chapter is closed:

$$
\boxed{
\text{the named line and every one of the }D+1\text{ frozen line shadows admit a strictly positive factor.}
}
$$

The complete stabilizer-projector layer is therefore feasible. It is also unconditionally insufficient for physicality: there is a compatible stabilizer-positive field with cubic \(C<3.571\times10^{-9}\).

The proposed six-permutation identity and both line-shift Parseval formulas are correct. They give the exact bound

$$
\boxed{
\left(\mathbb E_\kappa|C_{\mathrm{ind}}(\kappa)|^2\right)^{1/2}
<
2.682\times10^{-27}.
}
$$

This is only an average bound. An explicit degree-three character polynomial with the same \(D^{-3/2}\) RMS scale and supremum \(1\) proves that the line-shift moment cannot, by itself, be uniformized into a phase-independent cubic gap.

The first exact cross-line layer can nevertheless be compressed substantially. Stabilizer positivity together with a family of \(2\times2\) cross-basis Cauchy inequalities is **equivalent** to physical rank-one lifting. Equivalently, the structured stabilizer residuals

$$
\delta_{L,k}
=
\operatorname{Tr}\!\left[P_{L,k}(R_\alpha^2-R_\alpha)\right]
$$

obey the exact sum-of-squares identity

$$
\boxed{
\sum_{L,k}\delta_{L,k}^2
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
}
$$

For the stabilizer-positive nonphysical field already constructed, this sum is strictly positive and forces a definite cross-line \(2\times2\) violation. What remains open is whether some other choice of phases for the same magnitudes \(x^{(10)}\) makes every one of these cross-line residuals vanish.

---

# 1. Audit of the line-factor theorem

Fix a projective line \(L=\langle v_L\rangle\), and define

$$
S_L(t)
=
\sum_{j=0}^{m-1}\omega^{[a_j,tv_L]}.
$$

For \(t\neq0\),

$$
\lambda_{tv_L}=|S_L(t)|^2-m.
$$

From the exact definition of \(x^{(10)}\),

$$
x^{(10)}_{tv_L}
=
\gamma+\zeta_L(t),
$$

where

$$
\gamma
=
\frac{D(m-11)-10m}
{D(D+1)(m-1)}
$$

and

$$
\boxed{
\zeta_L(t)
=
\frac{10}{MD}|S_L(t)|^2
+
\frac{10}{M}\mathbf 1_{\Gamma\cap L}(tv_L).
}
\tag{1.1}
$$

Thus the stated quadrature form is

$$
\widehat p_L(t)
=
\rho+i\varepsilon_t\sqrt{\zeta_L(t)},
\qquad
\rho=\sqrt\gamma,
$$

on one representative of each inverse pair, with conjugate values at \(-t\) and \(\widehat p_L(0)=1\).

## 1.1 Parseval bookkeeping on a line

Let

$$
\ell_L=|\Gamma\cap L|\in\{0,2\}.
$$

The projection multiplicities satisfy

$$
\sum_r\nu_L(r)^2=m+\ell_L.
$$

Therefore finite Fourier Parseval gives

$$
\sum_{t\in\mathbb F_D}|S_L(t)|^2
=
D(m+\ell_L).
$$

Since \(S_L(0)=m\), and the nonzero terms occur in inverse pairs,

$$
\sum_{t\in H_L}|S_L(t)|^2
=
\frac{D(m+\ell_L)-m^2}{2}.
$$

Also,

$$
\sum_{t\in H_L}
\mathbf 1_{\Gamma\cap L}(tv_L)
=
\frac{\ell_L}{2}.
$$

Consequently,

$$
\begin{aligned}
Z_L
&:=
\sum_{t\in H_L}\zeta_L(t)\\
&=
\frac{5[D(m+\ell_L)-m^2]}{MD}
+
\frac{5\ell_L}{M}\\
&=
\boxed{
\frac{5(D-m)}{D(m-1)}
+
\frac{10\ell_L}{M}.
}
\end{aligned}
\tag{1.2}
$$

The full excess energy is therefore

$$
\boxed{
\mathcal E_L=2Z_L
=
\frac{10(D-m)}{D(m-1)}
+
\frac{20\ell_L}{M},
}
$$

which is exactly `LineExcess`.

Using \(\ell_L\le2\),

$$
\mathcal E_L
<
\frac{10}{m-1}
+
\frac{40}{m(m-1)}
<
\frac{11}{m-1}
<
\frac1{960}.
$$

All factors and normalizations in the first bookkeeping version are correct.

---

# 2. Audit of the linewise sign balancing

For \(k\neq0\), the inverse Fourier transform is

$$
p_{L,k}
=
\mu+
\frac2D
\sum_{t\in H_L}
\varepsilon_t\sqrt{\zeta_L(t)}
\sin\frac{2\pi kt}{D},
\qquad
\mu=\frac{1-\rho}{D}.
$$

For fixed \(k\), the random summand indexed by \(t\) ranges over an interval of length at most

$$
\frac{4\sqrt{\zeta_L(t)}}{D}.
$$

Hence the sum of squared range lengths is bounded by

$$
\frac{16}{D^2}Z_L
=
\frac{8}{D^2}\mathcal E_L.
$$

The one-sided Hoeffding estimate is therefore

$$
\boxed{
\Pr\{p_{L,k}\le0\}
\le
\exp\left[
-\frac{(1-\rho)^2}{4\mathcal E_L}
\right].
}
\tag{2.1}
$$

Since

$$
\gamma<\frac1{D+1}<\frac14,
\qquad
\rho<\frac12,
$$

and \(\mathcal E_L<11/(m-1)\),

$$
\frac{(1-\rho)^2}{4\mathcal E_L}
>
\frac{m-1}{176}
>60.
$$

Thus

$$
\Pr\{\exists k\neq0:p_{L,k}\le0\}
<
De^{-60}.
$$

The exact frozen comparison

$$
2^{60}-D
=
211380275833782299>0
$$

and \(e>2\) give

$$
De^{-60}<D2^{-60}<1.
$$

So every line admits a strictly positive factor.

This confirms the first union bound.

---

# 3. Audit of the simultaneous all-line variant

From (1.1),

$$
Z_L
<
\frac{5m+20}{M}.
$$

Indeed,

$$
\frac{5(D-m)}{D(m-1)}<\frac5{m-1}=\frac{5m}{M},
\qquad
\frac{10\ell_L}{M}\le\frac{20}{M}.
$$

The exact comparison

$$
M-10000(5m+20)
=
235361008664553220>0
$$

gives

$$
\boxed{Z_L<\frac1{10000}.}
\tag{3.1}
$$

Working directly with \(Z_L\), the one-sided exponent is

$$
\frac{(1-\rho)^2}{8Z_L}
>
\frac{1}{32Z_L}
>
312.5.
$$

There are exactly

$$
(D+1)(D-1)=D^2-1
$$

nonzero line marginals. Since \(D<2^{60}\),

$$
D^2-1<2^{120}.
$$

Thus the global failure probability is bounded by

$$
(D^2-1)e^{-312.5}
<
2^{120}e^{-312.5}
<
e^{-192.5}<1.
$$

The stronger simultaneous bookkeeping is therefore correct.

## 3.1 Greedy derandomization

Order all line-sign variables. For one event \((L,k)\), write its fluctuating coefficients as \(a_{j,L,k}\), and put

$$
\tau_L
=
\frac{D(1-\rho)}{4Z_L}
=
\frac{D(1-\rho)}{2\mathcal E_L}.
$$

After fixing the first \(r\) signs, use the potential

$$
\begin{aligned}
\Phi_r
=
\sum_{L,k\neq0}
&
\exp\left[
-\tau_L\left(
\mu+
\sum_{j\le r}\varepsilon_ja_{j,L,k}
\right)
\right]\\
&\times
\prod_{j>r}
\cosh(\tau_La_{j,L,k}).
\end{aligned}
$$

The average of the two possible next values is the current value, so one sign choice does not increase \(\Phi_r\). The initial bound is strictly below one by the preceding exponential estimate. At the final stage, any nonpositive marginal would contribute at least one to the potential. Hence the greedy rule returns strictly positive factors.

The probabilistic and greedy versions are both valid finite existence proofs.

---

# 4. Complete stabilizer feasibility and nonphysicality

Because distinct projective lines share only the zero label, the line factors assemble into a single Hermitian coefficient field with magnitudes \(x^{(10)}\) and

$$
p_{L,k}>0
\quad\text{for every }L,k.
$$

Thus:

$$
\boxed{
\text{the named line and the all-line spectral-factor gates are closed.}
}
$$

Independent line-character shifts

$$
\alpha_{tv_L}
\longmapsto
\alpha_{tv_L}\omega^{\kappa_Lt}
$$

cyclically permute each positive line marginal and preserve its positivity.

The same-line cubic is

$$
C_{\rm dep}
=
\sum_L\sum_kp_{L,k}^3-\frac1D.
$$

Because

$$
\sum_L\sum_kp_{L,k}^2=2
$$

and each line purity is smaller than \(3/D\),

$$
C_{\rm dep}
<
2\sqrt{\frac3D}-\frac1D.
$$

At the exact frozen \(D\),

$$
2\sqrt{\frac3D}-\frac1D
=
3.5700224891701977\ldots\times10^{-9}.
$$

Every linearly independent cubic term uses three distinct lines. Averaging independent line-character shifts annihilates each such term. Therefore some shift choice satisfies

$$
\boxed{
C(\alpha)
\le C_{\rm dep}
<
3.571\times10^{-9}<1.
}
\tag{4.1}
$$

This verifies `StabilizerNotPhysical` unconditionally.

It proves insufficiency of the complete stabilizer layer, not impossibility of a different phase choice with \(C=1\).

---

# 5. Six-permutation identity

Let

$$
u+v+w=0
$$

with \(u,v,w\) nonzero and on three distinct lines. Put

$$
\zeta=\omega^{2^{-1}[u,v]},
$$

where \(2^{-1}\) is the field inverse of \(2\). No replacement by an ordinary half-angle representative is being made.

The six ordered pairs give:

$$
\begin{array}{c|c}
\text{ordered pair} & \text{Weyl phase}\\ \hline
(u,v)&\zeta\\
(v,u)&\overline\zeta\\
(u,w)&\overline\zeta\\
(w,u)&\zeta\\
(v,w)&\zeta\\
(w,v)&\overline\zeta.
\end{array}
$$

Therefore

$$
\boxed{
\sum_{\text{six orders}}
\omega^{2^{-1}[\cdot,\cdot]}
=
3(\zeta+\overline\zeta)
=
6\operatorname{Re}\zeta.
}
\tag{SixPerm}
$$

The proposed factor is correct.

---

# 6. Character indexing under line shifts

Choose a generator \(v_L\) for each projective line. Every nonzero label has a unique form

$$
z=t_zv_{L_z},
\qquad
t_z\in\mathbb F_D^\times.
$$

For an unordered zero-sum triple

$$
T=\{u,v,w\},
$$

define its character of the line-shift group by

$$
\chi_T(\kappa)
=
\omega^{
\kappa_{L_u}t_u+
\kappa_{L_v}t_v+
\kappa_{L_w}t_w
}.
$$

Distinct unordered triples give distinct characters:

* the support of the character identifies the three lines;
* its three nonzero coefficients identify \(u,v,w\) on those lines.

Moreover, \(T\) and \(-T\) give inverse, distinct characters. They cannot coincide because \(D\) is odd and a nonzero three-element triple cannot equal its negative without containing zero.

Let \(\mathcal T\) contain all unordered nonzero zero-sum triples on three distinct lines, with \(T\) and \(-T\) both retained. For any ordering of \(T\), set

$$
r_T=\operatorname{Re}\omega^{2^{-1}[u,v]}.
$$

This is independent of the ordering up to conjugation, hence has the same real value.

The linearly independent cubic is exactly

$$
\boxed{
C_{\rm ind}(\kappa)
=
\frac6{D^2}
\sum_{T\in\mathcal T}
r_T\,
\alpha_u\alpha_v\alpha_w\,
\chi_T(\kappa).
}
\tag{6.1}
$$

---

# 7. Exact shift Parseval identities

Character orthogonality gives

$$
\begin{aligned}
\mathbb E_\kappa|C_{\rm ind}(\kappa)|^2
&=
\frac{36}{D^4}
\sum_{T\in\mathcal T}
r_T^2
|\alpha_u|^2|\alpha_v|^2|\alpha_w|^2\\
&=
\boxed{
\frac{36}{D^4}
\sum_T
\left(\operatorname{Re}
\omega^{2^{-1}[u,v]}\right)^2
x_u^{(10)}x_v^{(10)}x_w^{(10)}.
}
\end{aligned}
\tag{ShiftParseval-T}
$$

Each unordered triple contributes exactly six ordered independent pairs. Therefore

$$
\sum_{\substack{u,v\\\text{linearly independent}}}
r_{u,v}^2x_ux_vx_{-u-v}
=
6\sum_{T\in\mathcal T}r_T^2x_ux_vx_w.
$$

Consequently,

$$
\boxed{
\mathbb E_\kappa|C_{\rm ind}(\kappa)|^2
=
\frac6{D^4}
\sum_{\substack{u,v\\\text{linearly independent}}}
\left(\operatorname{Re}
\omega^{2^{-1}[u,v]}\right)^2
x_u^{(10)}x_v^{(10)}x_{-u-v}^{(10)}.
}
\tag{ShiftParseval-ord}
$$

Both proposed formulas, including the factors \(36\) and \(6\), are correct.

---

# 8. Exact RMS bound from \(x^{(10)}\)

Because \(x^{(10)}\) is self-Fourier,

$$
x_k
=
\frac1D\sum_zx_z\omega^{[k,z]}.
$$

It follows that

$$
\boxed{
\sum_{u,v}
x_ux_vx_{-u-v}
=
D\sum_zx_z^3.
}
\tag{8.1}
$$

Indeed, substitute the self-Fourier formula for \(x_{-u-v}\) and perform the two character sums.

Dropping the independent-pair restriction and using \(r_T^2\le1\),

$$
\mathbb E_\kappa|C_{\rm ind}|^2
\le
\frac6{D^4}
\sum_{u,v}x_ux_vx_{-u-v}
=
\frac6{D^3}\sum_zx_z^3.
$$

Now

$$
x_0=1,\qquad
0<x_z<U\quad(z\neq0),
\qquad
\sum_{z\neq0}x_z=D-1.
$$

Therefore

$$
\sum_zx_z^3
\le
1+U^2(D-1).
$$

Hence the exact bound is

$$
\boxed{
\mathbb E_\kappa|C_{\rm ind}|^2
\le
\frac6{D^3}
\left[1+(D-1)U^2\right].
}
\tag{8.2}
$$

Using the audited inequality

$$
U<\frac1{135873434^2}
$$

and the exact integer comparison

$$
135873434^4-10^{14}D
=
246676184922887428794697973950736>0,
$$

one obtains

$$
(D-1)U^2<10^{-14}.
$$

Thus

$$
\boxed{
\left(\mathbb E_\kappa|C_{\rm ind}|^2\right)^{1/2}
<
\frac{\sqrt{6(1+10^{-14})}}{D^{3/2}}
<
2.682\times10^{-27}.
}
\tag{8.3}
$$

This is an average/RMS statement. It is not a uniform phase bound.

In particular, some line shift satisfies

$$
|C_{\rm ind}(\kappa)|
<
2.682\times10^{-27},
$$

which sharpens the earlier existence of a shift with merely
\(C_{\rm ind}\le0\). It does not constrain the maximum.

---

# 9. Why the RMS cannot be uniformized by degree alone

Define on \(\mathbb F_D\)

$$
h(s)=\mathbf1_{\{0\}}(s)-\frac1D
=
\frac1D\sum_{t\neq0}\omega^{ts}.
$$

On three line-shift coordinates put

$$
F(\kappa_1,\kappa_2,\kappa_3)
=
\frac{
h(\kappa_1)h(\kappa_2)h(\kappa_3)
}{
(1-1/D)^3
}.
$$

Then:

* \(F(0,0,0)=1\);
* \(F\) has mean zero;
* every Fourier character uses a nonzero frequency on exactly three distinct coordinates;
* \(|F|\le1\);
* and

  $$
  \boxed{
  \mathbb E|F|^2=\frac1{(D-1)^3}.
  }
  $$

Thus a degree-three line-character polynomial can have supremum \(1\) while its RMS is of order \(D^{-3/2}\), exactly the scale in (8.3).

This is not a frozen cubic and not a physical counterexample. It proves that ShiftParseval plus degree-three support cannot, without further coefficient-specific structure, yield a uniform bound.

---

# 10. First and second variations on the line-shift torus

Choose one representative from each pair \(\{T,-T\}\). Write

$$
A_T
=
\frac6{D^2}
\left(\operatorname{Re}
\omega^{2^{-1}[u,v]}\right)
\alpha_u\alpha_v\alpha_w.
$$

Choose balanced integer representatives of the three field coefficients \(t_u,t_v,t_w\), and let \(q_T\) be the corresponding vector in the real line-coordinate space. A continuous fixed-magnitude line-phase variation has

$$
C_{\rm ind}(\theta)
=
2\sum_T
\operatorname{Re}
\left(
A_Te^{i\langle q_T,\theta\rangle}
\right).
$$

If \(C=1\), then the coefficient field is physical and gives a global maximum of \(C\) on the entire phase torus. Hence

$$
\boxed{
\sum_Tq_T\,\operatorname{Im}A_T=0,
}
\tag{10.1}
$$

and

$$
\boxed{
\sum_T
(\operatorname{Re}A_T)\,
q_Tq_T^{\mathsf T}
\succeq0.
}
\tag{10.2}
$$

These are the exact stationarity and Hessian conditions.

They are not phase-free: the signs of \(\operatorname{Re}A_T\) and
\(\operatorname{Im}A_T\) are not determined by \(x^{(10)}\). The model in Section 9 has a unit spike, the same \(D^{-3/2}\) RMS scale, vanishing gradient, and a negative-semidefinite Hessian at its maximum. Therefore neither the RMS nor the abstract Hessian sign yields a bounded principal-minor contradiction for the frozen data.

No phase-uniform cubic gap follows from this route.

---

# 11. A stronger exact cross-line sum-of-squares layer

Let

$$
H_\alpha:=R_\alpha^2-R_\alpha.
$$

For every stabilizer projector \(P_{L,k}\), define

$$
\boxed{
\delta_{L,k}
=
\operatorname{Tr}(P_{L,k}H_\alpha).
}
\tag{11.1}
$$

The complete set of stabilizer projectors satisfies the exact two-design identity

$$
\boxed{
\sum_{L,k}
P_{L,k}\otimes P_{L,k}
=
I+F,
}
\tag{11.2}
$$

where \(F\) is swap.

To verify it, expand

$$
P_{L,k}
=
\frac1D\sum_t\omega^{kt}W_{tv}.
$$

Summing over \(k\) forces the two line parameters to add to zero. Summing over all \(D+1\) lines counts every nonzero Weyl label exactly once and the zero label \(D+1\) times. Using

$$
F=\frac1D\sum_zW_z\otimes W_z^*
$$

gives (11.2).

Since

$$
\operatorname{Tr}H_\alpha
=
\operatorname{Tr}R_\alpha^2-\operatorname{Tr}R_\alpha
=0,
$$

equation (11.2) yields

$$
\begin{aligned}
\sum_{L,k}\delta_{L,k}^2
&=
\operatorname{Tr}
\left[
(H_\alpha\otimes H_\alpha)(I+F)
\right]\\
&=
(\operatorname{Tr}H_\alpha)^2
+
\operatorname{Tr}H_\alpha^2.
\end{aligned}
$$

Therefore

$$
\boxed{
\sum_{L,k}\delta_{L,k}^2
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
}
\tag{11.3}
$$

This is an exact structured global SOS certificate with \(D(D+1)\) scalar residuals.

Moreover,

$$
\delta_{L,k}
=
\frac1D
\sum_t
\bigl(Q_{tv}-\alpha_{tv}\bigr)\omega^{-kt},
$$

where

$$
Q_z
=
\frac1D
\sum_u
\alpha_u\alpha_{z-u}\omega^{[u,z]/2}
$$

is the twisted-convolution coefficient of \(R_\alpha^2\). Thus the line residuals are precisely the linewise Fourier transforms of the global idempotence residual.

Because the stabilizer projectors span \(M_D\),

$$
\boxed{
\delta_{L,k}=0\ \forall L,k
\iff
R_\alpha^2=R_\alpha.
}
\tag{11.4}
$$

Under the standing Hermiticity and trace-one assumptions, this is equivalent to a rank-one physical state.

---

# 12. Cross-basis \(2\times2\) Cauchy constraints

Let

$$
P=|\phi\rangle\langle\phi|,
\qquad
Q=|\chi\rangle\langle\chi|
$$

be stabilizer projectors from two distinct stabilizer bases. Positivity of \(R_\alpha\) implies

$$
\boxed{
\operatorname{Tr}(PR_\alpha QR_\alpha)
\le
\operatorname{Tr}(PR_\alpha)\,
\operatorname{Tr}(QR_\alpha).
}
\tag{12.1}
$$

This is simply

$$
|\langle\phi|R_\alpha|\chi\rangle|^2
\le
\langle\phi|R_\alpha|\phi\rangle
\langle\chi|R_\alpha|\chi\rangle.
$$

It is the positivity of a \(2\times2\) \(R_\alpha\)-Gram matrix.

Choose any fixed-point-free partner map \(L\mapsto\tau(L)\) on the \(D+1\) stabilizer bases. Suppose:

1. every stabilizer marginal is nonnegative; and
2. (12.1) holds for every \(P_{L,k}\) and every
   \(P_{\tau(L),j}\).

For fixed \(L,k\), summing (12.1) over \(j\) gives

$$
\operatorname{Tr}(P_{L,k}R_\alpha^2)
\le
\operatorname{Tr}(P_{L,k}R_\alpha).
$$

Hence

$$
\delta_{L,k}\le0.
$$

But for each \(L\),

$$
\sum_k\delta_{L,k}
=
\operatorname{Tr}(R_\alpha^2-R_\alpha)=0.
$$

Therefore every \(\delta_{L,k}=0\), and (11.4) gives a rank-one projector.

Conversely, a physical rank-one projector makes every inequality in (12.1) an equality.

Thus:

$$
\boxed{
\begin{aligned}
&\text{stabilizer positivity plus the designated cross-basis}\\
&2\times2\text{ Cauchy inequalities}\\
&\iff
\text{physical pure-state lifting}.
\end{aligned}
}
\tag{12.2}
$$

This uses local \(2\times2\) constraints but has global indexing cost

$$
\boxed{
(D+1)D^2
=
834676191481542500102529837710713256761115423061571062
}
$$

quadratic inequalities. It is still substantially smaller than imposing positivity of the full \(D^2\times D^2\) orbit matrix entry by entry.

---

# 13. Quantitative detection of the known nonphysical field

For any Hermitian trace-one, purity-one \(R_\alpha\),

$$
1-C(\alpha)
\le
\sqrt{
\operatorname{Tr}(R_\alpha^2-R_\alpha)^2
}.
$$

Therefore the stabilizer-positive field from Section 4, with

$$
C(\alpha)\le
c_0:=
2\sqrt{\frac3D}-\frac1D,
$$

satisfies

$$
\sum_{L,k}\delta_{L,k}^2
\ge
(1-c_0)^2.
\tag{13.1}
$$

Choose a line with

$$
\sum_k\delta_{L,k}^2
\ge
\frac{(1-c_0)^2}{D+1}.
$$

For \(D\) real numbers of sum zero, if their largest positive entry is \(p\), then

$$
\sum_k\delta_k^2\le D(D-1)p^2.
$$

Hence some \(k\) obeys

$$
\delta_{L,k}
\ge
\frac{1-c_0}
{\sqrt{D(D^2-1)}}.
\tag{13.2}
$$

Now fix the designated partner basis \(\tau(L)\), and define

$$
e_j
=
\operatorname{Tr}
\left(
P_{L,k}R_\alpha
P_{\tau(L),j}R_\alpha
\right)
-
p_{L,k}p_{\tau(L),j}.
$$

Summing over \(j\) gives

$$
\sum_je_j=\delta_{L,k}.
$$

Thus at least one \(j\) satisfies

$$
\boxed{
e_j
\ge
\frac{1-c_0}
{D\sqrt{D(D^2-1)}}.
}
\tag{13.3}
$$

Numerically, the right side is larger than

$$
1.1625\times10^{-45}.
$$

So the already constructed stabilizer-positive field necessarily violates a concrete cross-line \(2\times2\) Cauchy inequality by a strictly positive amount.

This is the first exact cross-line SOS layer that detects what all linewise tests miss.

It does not prove that every phase assignment with magnitudes \(x^{(10)}\) violates such an inequality.

---

# 14. Remaining physical-lift gate

For the fixed magnitude profile \(x^{(10)}\), physical lifting is now equivalently the feasibility of either of the following structured systems:

$$
\delta_{L,k}=0
\quad
\text{for all }D(D+1)\text{ stabilizer projectors},
$$

or, after stabilizer positivity,

$$
\operatorname{Tr}(P_{L,k}R_\alpha
P_{\tau(L),j}R_\alpha)
\le
p_{L,k}p_{\tau(L),j}
$$

for the designated \(D^2(D+1)\) cross-basis pairs.

No compatible phase assignment satisfying these conditions is constructed.

No phase-uniform positive lower bound on the SOS in (11.3) is proved for all compatible phase fields of \(x^{(10)}\).

Therefore:

* the line-shift RMS is far too small to be useful as a uniform bound;
* the Hessian conditions remain phase-dependent;
* the new cross-line SOS system is exact and strictly stronger than the complete stabilizer layer;
* but its feasibility for \(x^{(10)}\) remains open.

A physical lift of \(x^{(10)}\) would disprove PW10 because its frozen objective is strictly larger than \(10\). Excluding this one magnitude profile would still not prove PW10 for every pure state.

---

# VERIFIED

* `LineExcess`, including every factor of \(2\).
* The quadrature factor construction.
* The per-line sign-balancing exponent.
* The stronger all-line bookkeeping:

  $$
  \sum_{t\in H_L}\zeta_L(t)
  <
  \frac{5m+20}{M}
  <
  \frac1{10000}.
  $$
* The simultaneous union bound over all \(D^2-1\) nonzero marginals.
* The greedy conditional-expectation derandomization.
* Strictly positive factors for the named line and every frozen line.
* Feasibility of all \(D(D+1)\) stabilizer inequalities.
* `StabilizerNotPhysical`.
* `SixPerm`.
* `ShiftParseval-T`.
* `ShiftParseval-ord`.
* Distinctness of the line-shift characters attached to distinct unordered triples.
* The exact RMS upper bound

  $$
  \mathbb E|C_{\rm ind}|^2
  \le
  \frac6{D^3}[1+(D-1)U^2].
  $$
* The numerical enclosure

  $$
  \operatorname{RMS}(C_{\rm ind})
  <2.682\times10^{-27}.
  $$
* The exact degree-three spike showing that this RMS scale does not control the supremum.
* The line-shift first- and second-variation formulas.
* The stabilizer two-design identity.
* The global residual SOS

  $$
  \sum_{L,k}\delta_{L,k}^2
  =
  \operatorname{Tr}(R_\alpha^2-R_\alpha)^2.
  $$
* The cross-basis \(2\times2\) Cauchy characterization.
* The quantitative cross-line violation for the known stabilizer-positive nonphysical field.

# CORRECTED

* The line-shift RMS is much smaller than the previous same-line cubic scale, but it is only an average and cannot be promoted to a uniform cubic bound.
* The complete stabilizer layer is no longer a bottleneck.
* The first unresolved obstruction is not a one-dimensional factor problem; it is the simultaneous vanishing of cross-line idempotence residuals.
* A bounded local matrix size does not make the global cross-line system small: the exact \(2\times2\) characterization still contains \(D^2(D+1)\) indexed inequalities.

# DISPROVED

* Any claim that the line-factor problem remains open.
* Any claim that the complete stabilizer layer might itself enforce physicality.
* Any inference from the tiny line-shift RMS to a phase-uniform bound.
* Sufficiency of line-shift stationarity or Hessian negativity without coefficient-specific phase information.

# NECESSARY-ONLY

* The line-shift stationarity equations.
* The line-shift Hessian semidefiniteness condition.
* Every individual cross-basis Cauchy inequality.
* Vanishing of every stabilizer residual \(\delta_{L,k}\).
* Positivity of all stabilizer marginals.

# SUFFICIENT-ONLY

* Stabilizer positivity together with all designated cross-basis Cauchy inequalities is sufficient for physical lifting; in fact, under the standing trace and purity hypotheses it is also necessary.
* Vanishing of all stabilizer residuals is sufficient for physical lifting; again it is also necessary.

# OPEN

* Whether \(x^{(10)}\) admits compatible phases with

  $$
  C(\alpha)=1.
  $$
* Whether all compatible phases for \(x^{(10)}\) have a uniform positive residual

  $$
  \sum_{L,k}\delta_{L,k}^2\ge\eta>0.
  $$
* Whether the exact cross-basis \(2\times2\) system is feasible for
  \(x^{(10)}\).
* Whether another objective-above-\(10\) magnitude profile has a physical lift.
* PW10 for the frozen tuple.
* The finite \(r=2\) low-\(A\) gate.

The first new claim requiring independent verification is the exact cross-line equivalence:

$$
\boxed{
\text{stabilizer positivity}
+
\text{designated cross-basis }2\times2\text{ Cauchy inequalities}
\iff
R_\alpha\text{ is a rank-one projector},
}
$$

together with the quantitative violation bound in (13.3).
