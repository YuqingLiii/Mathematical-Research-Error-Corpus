# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

No exact baseline vector, frozen-edge vector, physical vector with objective above \(10\), exclusion of \(x^{(10)}\), or phase-uniform proof of PW10 is obtained.

The strongest new result is an exact bounded-complexity theorem. Relative to any single symmetric quadratic Gauss core, a baseline deformation cannot modify only a bounded number of entries in each row. At the frozen prime:

$$
\boxed{
\text{every modified nonzero row must differ from the core in at least }
777716\text{ coefficients}.}
$$

This is much stronger than the previous 47-shear-character lower bound, although it concerns a different complexity measure: Hamming distance from one quadratic Gauss core.

The two-core mixture is also classified exactly:

$$
\boxed{
\text{a sum of two nonzero symmetric quadratic Gauss cores can have a
constant-modulus nonzero row only if the two cores are identical,}
}
$$

so the mixture collapses to one effective core. More generally, every ordered-difference-Sidon mixture of at most \(31150\) distinct cores is impossible.

---

# 1. Quadratic Gauss preliminaries

Work first over an odd prime field \(\mathbb F_p\), with

$$
\omega=e^{2\pi i/p}.
$$

For \(a\ne0\), define

$$
G(a)=\sum_{z\in\mathbb F_p}\omega^{az^2}.
$$

Completing the square gives

$$
\boxed{
\sum_z\omega^{az^2+\ell z}
=
G(a)\omega^{-\ell^2/(4a)}.
}
\tag{1.1}
$$

Its magnitude is exactly

$$
\boxed{|G(a)|=\sqrt p.}
\tag{1.2}
$$

Indeed, using the bijection

$$
u=x-y,\qquad v=x+y
$$

available because \(p\) is odd,

$$
\begin{aligned}
|G(a)|^2
&=
\sum_{x,y}\omega^{a(x^2-y^2)}\\
&=
\sum_{u,v}\omega^{auv}\\
&=p.
\end{aligned}
$$

We will repeatedly use the following elementary lemma.

## Circle lemma

Let \(R>0\), \(\delta\in\mathbb C\), and let
\(\zeta_1,\zeta_2,\zeta_3\) be three distinct unit complex numbers. If

$$
|R\zeta_1+\delta|
=
|R\zeta_2+\delta|
=
|R\zeta_3+\delta|,
$$

then

$$
\boxed{\delta=0.}
$$

Indeed, after squaring, the three points satisfy

$$
\operatorname{Re}(\overline\delta\,\zeta_j)=\text{constant}.
$$

If \(\delta\ne0\), this is the intersection of the unit circle with one line, which contains at most two points.

---

# 2. Audit of `BorderedGaussNoGo`

Consider

$$
Q_{y,z}
=
\gamma\,
\omega^{a(y^2+z^2)+byz},
\qquad
a\ne0,\quad\gamma\ne0.
$$

This is symmetric and centrally even:

$$
Q_{y,z}=Q_{z,y}=Q_{-y,-z}.
$$

Its inverse Fourier transform in the row coordinate \(z\) is

$$
\begin{aligned}
\mathcal Q_y(x)
&=
\sum_z Q_{y,z}\omega^{-zx}\\
&=
\gamma G(a)
\omega^{ay^2-(by-x)^2/(4a)}.
\end{aligned}
\tag{2.1}
$$

Thus every full quadratic row has constant modulus

$$
\boxed{|\mathcal Q_y(x)|=|\gamma|\sqrt p.}
\tag{2.2}
$$

Now retain the quadratic values for \(yz\ne0\), but allow an arbitrary symmetric first row and column:

$$
H_{y,0}=H_{0,y}=h_y.
$$

For \(y\ne0\), the modified inverse row is

$$
\mathcal H_y(x)
=
\mathcal Q_y(x)+\delta_y,
\qquad
\delta_y=h_y-\gamma\omega^{ay^2}.
\tag{2.3}
$$

As \(x\) varies, the quadratic phase

$$
\omega^{-(by-x)^2/(4a)}
$$

takes \((p+1)/2\) distinct values. For \(p\ge7\), there are at least three. If \(\mathcal H_y\) has constant modulus, the circle lemma gives

$$
\delta_y=0.
$$

Therefore

$$
\boxed{
h_y=\gamma\omega^{ay^2}\quad(y\ne0)
}
\tag{2.4}
$$

and the required off-axis modulus is necessarily

$$
\boxed{B=|\gamma|\sqrt p.}
\tag{2.5}
$$

The zero row is consequently

$$
\mathcal H_0(x)
=
\gamma G(a)\omega^{-x^2/(4a)}
+
(h_0-\gamma).
\tag{2.6}
$$

For a baseline edge, its modulus must equal \(B\) for every
\(x\ne\pm1\). The values of \(x^2\) on
\(\mathbb F_p\setminus\{\pm1\}\) include

$$
\frac{p-1}{2}\ge3
$$

distinct values when \(p\ge7\). The circle lemma therefore forces

$$
h_0=\gamma.
$$

Then the zero row is flat:

$$
|\mathcal H_0(x)|=B\quad\forall x,
$$

which cannot produce the two exceptional amplitudes

$$
A_{\rm sp}=\sqrt{p+1}\,B>B.
$$

Hence:

$$
\boxed{
\text{A single bordered symmetric quadratic Gauss core cannot be a
baseline lift for any prime }p\ge7.
}
\tag{BorderedGaussNoGo}
$$

This covers exactly:

* one global quadratic core with fixed \(a,b,\gamma\);
* an arbitrary symmetric first row and column.

It does **not** cover dense nonquadratic corrections, row-dependent quadratic parameters, multiplicative-character factors, or sums of many cores.

---

# 3. Exact deformation equations

Fix a nonzero row \(y\). Write

$$
H_{y,z}=Q_{y,z}+E_{y,z},
$$

and abbreviate

$$
q_z=Q_{y,z},
\qquad
e_z=E_{y,z}.
$$

Let

$$
T=\operatorname{supp}e,\qquad r=|T|.
$$

Both the full core row and the modified row have constant inverse-Fourier modulus precisely when their nonzero cyclic autocorrelations vanish. Since the core autocorrelation already vanishes, the exact deformation equations are

$$
\boxed{
\sum_z
\left[
e_{z+s}\overline{e_z}
+
e_{z+s}\overline{q_z}
+
q_{z+s}\overline{e_z}
\right]
=0
\quad(s\ne0).
}
\tag{3.1}
$$

Equivalently, in the inverse-Fourier variable \(x\), put

$$
W(x)=\sum_{t\in T}e_t\omega^{-tx}.
$$

From (2.1), write

$$
\mathcal Q_y(x)
=
\rho_y\,
\omega^{\kappa x^2+\ell_yx},
\tag{3.2}
$$

where

$$
\kappa=-\frac1{4a}\ne0,
\qquad
\ell_y=\frac{by}{2a},
$$

and

$$
|\rho_y|=|\gamma|\sqrt p.
$$

If the modified row has constant modulus \(B_y\), then

$$
\boxed{
\begin{aligned}
0={}&
\rho_y
\sum_{t\in T}\overline{e_t}\,
\omega^{\kappa x^2+(\ell_y+t)x}\\
&+
\overline{\rho_y}
\sum_{t\in T}e_t\,
\omega^{-\kappa x^2-(\ell_y+t)x}\\
&+
\sum_{t,u\in T}
e_t\overline{e_u}\omega^{(u-t)x}\\
&+
|\rho_y|^2-B_y^2
\qquad\forall x.
\end{aligned}
}
\tag{3.3}
$$

This is the exact finite phase system used below.

---

# 4. Three mutually unbiased quadratic bases

For \(c,d\in\mathbb F_p\), define the normalized chirps

$$
\phi_{c,d}(x)
=
p^{-1/2}\omega^{cx^2+dx}.
$$

For fixed \(c\), the vectors

$$
\{\phi_{c,d}:d\in\mathbb F_p\}
$$

form an orthonormal basis.

For \(c\ne c'\),

$$
\left|
\langle\phi_{c,d},\phi_{c',d'}\rangle
\right|
=
p^{-1/2}.
\tag{4.1}
$$

This follows from the Gauss-sum calculation in Section 1. Thus different quadratic bases are mutually unbiased.

Equation (3.3) uses columns from exactly three such bases:

$$
\mathcal C_+
=
\{\phi_{\kappa,\ell_y+t}:t\in T\},
$$

$$
\mathcal C_-
=
\{\phi_{-\kappa,-\ell_y-t}:t\in T\},
$$

and

$$
\mathcal C_0
=
\{\phi_{0,s}:s\in T-T\}.
$$

Since \(p\) is odd and \(\kappa\ne0\), the three quadratic parameters

$$
\kappa,\quad-\kappa,\quad0
$$

are distinct.

Put

$$
d_T=|T-T|.
$$

The three block sizes are

$$
r,\quad r,\quad d_T.
$$

---

# 5. A support-sensitive deformation no-go

Let \(G_T\) be the Gram matrix of the selected columns
\(\mathcal C_+\cup\mathcal C_-\cup\mathcal C_0\).

The operator norm of the cross block between the two \(r\)-column chirp families is bounded by its Frobenius norm:

$$
a\le\frac r{\sqrt p}.
$$

The cross block between an \(r\)-column family and the \(d_T\)-column character family satisfies

$$
b\le\sqrt{\frac{r\,d_T}{p}}.
$$

For coefficient-block norms \(x_1,x_2,x_3\), the Gram quadratic form is bounded below by

$$
\begin{pmatrix}x_1&x_2&x_3\end{pmatrix}
\begin{pmatrix}
1&-a&-b\\
-a&1&-b\\
-b&-b&1
\end{pmatrix}
\begin{pmatrix}x_1\\x_2\\x_3\end{pmatrix}.
\tag{5.1}
$$

The antisymmetric eigenvalue of the comparison matrix is \(1+a>0\). On the symmetric two-dimensional block, positivity is equivalent to

$$
1-a-2b^2>0.
$$

Consequently, the selected chirp columns are linearly independent whenever

$$
\boxed{
2r\,|T-T|+r\sqrt p<p.
}
\tag{5.2}
$$

If they are independent, equation (3.3) forces every coefficient in the \(+\kappa\) family to vanish:

$$
\rho_y\overline{e_t}=0
\quad(t\in T).
$$

Since \(\rho_y\ne0\), this gives \(e_t=0\), contradicting \(T=\operatorname{supp}e\).

We have proved:

## Sparse quadratic deformation theorem

$$
\boxed{
\begin{gathered}
\text{If a quadratic Gauss row and a modified row both have constant}\\
\text{inverse-Fourier modulus, and the modification support }T
\text{ satisfies}\\[1mm]
2|T|\,|T-T|+|T|\sqrt p<p,
\end{gathered}
}
$$

then the modification is zero.

The two constant moduli need not be equal.

---

# 6. Exact frozen lower bound: \(777716\) modifications

Now specialize to

$$
p=D=941541228773064677
=
970330474^2+1.
$$

Thus

$$
970330474<\sqrt D<970330475.
$$

For a set \(T\) of size \(r\),

$$
|T-T|\le r(r-1)+1.
$$

Take

$$
r_0=777715.
$$

Then

$$
r_0(r_0-1)+1
=
604839843511,
$$

and exact integer arithmetic gives

$$
\begin{aligned}
&
2r_0\bigl(r_0(r_0-1)+1\bigr)
+
970330475\,r_0\\
&\qquad=
941540678357679355\\
&\qquad<
941541228773064677=D.
\end{aligned}
\tag{6.1}
$$

The margin is

$$
\boxed{550415385322.}
$$

Therefore condition (5.2) holds for every support of size at most \(777715\).

Hence:

$$
\boxed{
\text{Every nonzero modified row must differ from a quadratic core in at
least }777716\text{ positions}.}
\tag{6.2}
$$

This is a growing lower bound of order \(D^{1/3}\).

## 6.1 The first undecided support size is almost Sidon

Set

$$
r_1=777716.
$$

Any surviving support must violate (5.2), so

$$
2r_1|T-T|+r_1\sqrt D\ge D.
$$

Using \(\sqrt D<970330475\),

$$
|T-T|
>
\frac{D-970330475\,r_1}{2r_1}.
$$

The exact Euclidean division is

$$
D-970330475\,r_1
=
2r_1\cdot604839419040
+
1144297,
$$

where

$$
2r_1=1555432.
$$

Therefore

$$
\boxed{|T-T|\ge604839419041.}
\tag{6.3}
$$

But the maximal possible value is

$$
r_1(r_1-1)+1=604841398941.
$$

Thus at the first undecided support size, the difference set may fall short of its maximum by at most

$$
\boxed{1979900.}
$$

So the first unresolved deformation is already forced to have an almost-Sidon support.

---

# 7. Global baseline corollary

Let

$$
H=Q+E
$$

be a symmetric, centrally even deformation of one quadratic Gauss core. Suppose every nonzero row of \(H\) has the required constant baseline modulus.

If a nonzero row is modified, Section 6 implies that its modification support has size at least \(777716\).

If no nonzero row is modified, symmetry implies

$$
E_{0,y}=E_{y,0}=0
\quad(y\ne0).
$$

Only \(E_{0,0}\) could remain. But then the zero row is one quadratic Gauss row translated by one complex constant. The circle argument from Section 2 forces that constant to vanish on the \(D-2\) ordinary baseline positions, after which the two spikes cannot occur.

Therefore:

$$
\boxed{
\begin{gathered}
\text{Any symmetric deformation of one quadratic Gauss core producing a}\\
\text{baseline lift has at least one nonzero row with at least }
777716\\
\text{modified coefficients.}
\end{gathered}
}
\tag{7.1}
$$

This rules out every fixed-complexity deformation and a substantial growing range.

---

# 8. The first undecided deformation system

For a support \(T\), equation (3.3) can be written as one explicit dictionary-kernel equation

$$
\boxed{\Phi_T c(e,B_y)=0,}
\tag{8.1}
$$

where \(\Phi_T\) has columns

$$
\mathcal C_+\cup\mathcal C_-\cup\mathcal C_0,
$$

and the coefficient vector is

$$
c_t^+
=
\rho_y\overline{e_t},
$$

$$
c_t^-
=
\overline{\rho_y}e_t,
$$

$$
c_s^0
=
\sum_{\substack{t,u\in T\\u-t=s}}
e_t\overline{e_u}
+
\mathbf1_{\{s=0\}}
\bigl(|\rho_y|^2-B_y^2\bigr).
\tag{8.2}
$$

Equivalently,

$$
G_Tc(e,B_y)=0,
\qquad
G_T=\Phi_T^*\Phi_T.
\tag{8.3}
$$

For \(|T|\le777715\), \(G_T\) is positive definite by Section 5.

At \(|T|=777716\), this is the first undecided finite determinant/kernel system. The dictionary has at most

$$
r_1^2+r_1+1
=
970353651
$$

columns, but the coefficient vector has the special nonlinear form (8.2). Merely proving \(G_T\) singular would be necessary, not sufficient: its kernel must contain a vector with that exact conjugate-quadratic structure.

---

# 9. Exact classification of a two-core mixture

Consider

$$
H_{y,z}
=
\sum_{\nu=1}^2
\gamma_\nu
\omega^{a_\nu(y^2+z^2)+b_\nu yz},
\qquad
a_\nu\ne0,
\quad
\gamma_\nu\ne0.
$$

For a fixed nonzero row \(y\), its inverse transform is

$$
G_y(x)
=
\sum_{\nu=1}^2
\rho_\nu
\omega^{
\kappa_\nu x^2
+c_\nu yx
+d_\nu y^2
},
\tag{9.1}
$$

where

$$
\rho_\nu=\gamma_\nu G(a_\nu),
$$

$$
\kappa_\nu=-\frac1{4a_\nu},
\qquad
c_\nu=\frac{b_\nu}{2a_\nu},
\qquad
d_\nu=a_\nu-\frac{b_\nu^2}{4a_\nu}.
$$

Its squared modulus is

$$
\begin{aligned}
|G_y(x)|^2
={}&
|\rho_1|^2+|\rho_2|^2\\
&+
2\operatorname{Re}\left[
\rho_1\overline{\rho_2}
\omega^{
(\kappa_1-\kappa_2)x^2
+(c_1-c_2)yx
+(d_1-d_2)y^2
}
\right].
\end{aligned}
\tag{9.2}
$$

If

$$
(\kappa_1-\kappa_2,\ c_1-c_2)\ne(0,0),
$$

the polynomial phase in \(x\) assumes at least three distinct unit values:

* if the quadratic coefficient is zero, it assumes all \(p\) values;
* if it is nonzero, it assumes \((p+1)/2\ge4\) values.

The circle lemma then contradicts constant modulus because

$$
\rho_1\overline{\rho_2}\ne0.
$$

Therefore

$$
\kappa_1=\kappa_2,
\qquad
c_1=c_2.
$$

The first equality gives

$$
a_1=a_2,
$$

and the second then gives

$$
b_1=b_2.
$$

Thus the two cores are identical except for their scalar coefficients:

$$
H_{y,z}
=
(\gamma_1+\gamma_2)
\omega^{a_1(y^2+z^2)+b_1yz}.
$$

Hence:

$$
\boxed{
\text{Every constant-modulus two-core mixture collapses to one effective
quadratic core.}
}
\tag{9.3}
$$

If \(\gamma_1+\gamma_2=0\), the row is zero and cannot be a baseline row.

This classification is exact and does not rely on asymptotics.

---

# 10. General fixed-rank Gauss mixtures

For

$$
H_{y,z}
=
\sum_{\nu=1}^r
\gamma_\nu
\omega^{a_\nu(y^2+z^2)+b_\nu yz},
$$

combine terms having identical \((a_\nu,b_\nu)\), and assume the remaining transformed parameter points

$$
\theta_\nu=(\kappa_\nu,c_\nu)
$$

are distinct.

For fixed \(y\ne0\), constant modulus requires

$$
\boxed{
\sum_{\nu\ne\mu}
\rho_\nu\overline{\rho_\mu}
\omega^{(d_\nu-d_\mu)y^2}
\omega^{
(\kappa_\nu-\kappa_\mu)x^2
+
(c_\nu-c_\mu)yx
}
=\text{constant in }x.
}
\tag{10.1}
$$

Let

$$
\Delta\Theta
=
\{\theta_\nu-\theta_\mu:\nu\ne\mu\}.
$$

If

$$
|\Delta\Theta|<\sqrt p,
$$

the selected quadratic-phase functions together with the constant function are linearly independent by the mutually unbiased-basis Gram estimate. Consequently, every difference class must satisfy

$$
\boxed{
\sum_{\substack{\nu\ne\mu\\
\theta_\nu-\theta_\mu=\Delta}}
\rho_\nu\overline{\rho_\mu}
\omega^{(d_\nu-d_\mu)y^2}
=0
\quad
\forall\,\Delta\ne0.
}
\tag{10.2}
$$

For a baseline, this must hold for every \(y\ne0\).

## 10.1 Difference-Sidon mixtures

Suppose the parameter set \(\{\theta_\nu\}\) is ordered-difference Sidon:

$$
\theta_\nu-\theta_\mu
=
\theta_{\nu'}-\theta_{\mu'},
\quad\nu\ne\mu,\ \nu'\ne\mu'
$$

implies

$$
(\nu,\mu)=(\nu',\mu').
$$

Then each sum in (10.2) contains one nonzero term and cannot vanish.

Hence an ordered-difference-Sidon mixture is impossible whenever

$$
r(r-1)<\sqrt p.
\tag{10.3}
$$

For the frozen prime,

$$
31150\cdot31149
=
970291350
<
970330474
<
\sqrt D.
$$

Therefore:

$$
\boxed{
\text{No ordered-difference-Sidon mixture of }
2\le r\le31150
\text{ distinct quadratic cores can have constant-modulus nonzero rows.}
}
\tag{10.4}
$$

The \(r=2\) classification is unconditional because every two-point parameter set is automatically ordered-difference Sidon.

## 10.2 First uncancelled mixture system

For non-Sidon parameter sets, equation (10.2) is the first exact unresolved system:

$$
\boxed{
\sum_{\theta_\nu-\theta_\mu=\Delta}
\rho_\nu\overline{\rho_\mu}
\omega^{(d_\nu-d_\mu)y^2}
=0
\quad
\text{for every }\Delta\ne0,\ y\ne0.
}
\tag{10.5}
$$

Thus every parameter difference must be multiply represented, with exact coefficient and quadratic-\(y\) cancellation. This is substantially smaller than the original \(D^2\)-entry baseline system when \(r\) is fixed, but it is not solved here.

---

# 11. Scope of the new no-go theorems

The results exclude:

* the bordered single quadratic core;
* every deformation differing from one quadratic core in at most
  \(777715\) entries of each nonzero row;
* every two-core mixture;
* every ordered-difference-Sidon mixture of at most \(31150\) cores.

They do not exclude:

* a dense genuinely nonquadratic deformation;
* a high-rank mixture with heavily repeated parameter differences and exact cancellations;
* the full-character solutions suggested by the small-prime numerical continuation;
* a topological continuation branch.

The numerical continuation at

$$
D=3,5,7,11,13,17,19
$$

remains evidence only. No degree, intersection number, or cobordism invariant is proved to survive to the frozen prime, and singular fibers have not been excluded.

---

# Closing status

No exact baseline vector has been produced.

No exact frozen-edge vector has been produced.

No exact exclusion of \(x^{(10)}\) has been produced.

No exact physical vector with objective above \(10\) has been produced.

No phase-uniform proof of PW10 has been produced.

Therefore

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

# VERIFIED

* The Gauss-sum normalization and completed-square formula.
* The circle lemma.
* `BorderedGaussNoGo` for every prime \(p\ge7\).
* The exact row-deformation autocorrelation equations.
* The three mutually unbiased quadratic bases used by a sparse deformation.
* The support-sensitive no-go condition

  $$
  2|T|\,|T-T|+|T|\sqrt p<p.
  $$
* The exact frozen lower bound of \(777716\) modified entries in any modified nonzero row.
* At the first undecided size \(777716\), the support must satisfy

  $$
  |T-T|\ge604839419041.
  $$
* The exact finite dictionary-kernel system (8.1)–(8.3).
* Exact collapse of every two-core mixture to one core.
* The ordered-difference-Sidon mixture no-go through \(r=31150\).

# CORRECTED

* The bordered argument applies only to one global quadratic core with an arbitrary first row and column.
* Sparse deformations are excluded far beyond the one-coefficient border case, but not when they are dense.
* A low-rank Gauss mixture need not be treated as a generic deformation: its cross terms admit the sharper parameter-difference analysis.
* The first unresolved deformation at size \(777716\) must have an almost-maximal difference set; it is not an arbitrary sparse support.
* The topological continuation route remains unproved because singular fibers and degree preservation are uncontrolled.

# DISPROVED

* Existence of a bordered single-core baseline lift.
* Existence of a baseline deformation changing at most \(777715\) coefficients in every nonzero row.
* Existence of a genuine two-core constant-modulus mixture.
* Existence of an ordered-difference-Sidon mixture with \(2\le r\le31150\).
* Sufficiency of the small-prime continuation observations as a proof at the frozen prime.

# NECESSARY-ONLY

* Dense row modification beyond the \(777715\) threshold.
* The near-Sidon difference-set requirement at the first undecided support size.
* The grouped mixture cancellation equations (10.5).
* Any proposed full-character topological continuation.

# EQUIVALENT

For a fixed deformed quadratic row:

* constant inverse-Fourier modulus;
* vanishing of every nonzero cyclic autocorrelation;
* the exact dictionary equation \(\Phi_Tc(e,B)=0\).

For a fixed-rank Gauss mixture in the linearly independent regime:

* constant row modulus;
* the grouped parameter-difference cancellations (10.2), together with the correct constant term.

# NUMERICAL-ONLY

* Machine-precision baseline lifts at

  $$
  D=3,5,7,11,13,17,19.
  $$
* Numerical full-character occupancy and generic-looking singular values.
* Any extrapolation of those observations to the frozen prime.

# CONJECTURED

* Existence of a dense full-character baseline lift at the frozen prime.
* Persistence of the small-prime continuation branch without singularity.
* No conjecture is promoted to a proved statement.

# OPEN

* The first dense deformation system beginning at support size \(777716\).
* Non-Sidon high-rank Gauss mixtures satisfying the exact cancellations (10.5).
* Existence of any baseline pure-edge vector.
* Pure one-edge retrieval for \(z_\star\) and \(h_\star\).
* Controlled continuation from a baseline solution to a frozen edge.
* Cross-edge rank-one consistency.
* Physical liftability of \(x^{(10)}\).
* An exact physical vector with objective above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the support-sensitive quadratic-deformation theorem

$$
\boxed{
2|T|\,|T-T|+|T|\sqrt D<D
\quad\Longrightarrow\quad
E_{y,\cdot}=0,
}
$$

and its frozen consequence that any modified nonzero row must contain at least

$$
\boxed{777716}
$$

changed coefficients.
