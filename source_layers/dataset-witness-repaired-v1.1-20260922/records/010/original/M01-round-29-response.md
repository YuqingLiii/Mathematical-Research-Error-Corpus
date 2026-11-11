# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

All three proposed audits have definite outcomes:

1. **Candidate theorem A is correct**, but substantially weaker than what the same Gram argument actually proves. There is an unconditional no-go for every effective symmetric Gauss mixture with at most

$$
\boxed{31150}
$$

distinct cores—no Sidon hypothesis is needed.

2. **Candidate theorem B is correct.** The displayed \(L_{m,\varepsilon}\) are precisely the nonvertical affine ruling lines of the parameter quadric, and no arbitrary-rank mixture supported on

$$
L_{m,+}\cup L_{m,-}
$$

can produce a baseline lift.

3. **GlobalDensity is correct:**

$$
\boxed{
|\{(y,z):y\ne0,\ E_{y,z}\ne0\}|
\ge604841398940.
}
$$

The arithmetic correction is also correct:

$$
\boxed{
777716^2+777716+1=604842954373.
}
$$

The first unresolved Gauss-mixture rank is now \(31151\). At that rank, any possible solution must have at least

$$
970330475
$$

active grouped quadratic-difference phases out of at most

$$
970353651,
$$

so its grouped difference support may miss at most \(23176\) of the maximal number. This is an exact near-Sidon requirement.

For two or more ruling slopes, I derive the complete grouped autocorrelation equations and their exact Fourier-dual Gauss system. Every individual exponential sum in that system is explicitly evaluable by quadratic Gauss sums; the remaining obstruction is a large nonlinear cancellation system, not an unknown scalar Weil bound.

No exact baseline lift or contradiction is obtained.

---

# 1. Arithmetic correction

For

$$
r_1=777716,
$$

one has

$$
r_1^2=604842176656,
$$

and therefore

$$
\boxed{
r_1^2+r_1+1
=
604842954373.
}
$$

The previously recorded value \(970353651\) was unrelated to this deformation-dictionary count. It happens instead to be

$$
31151\cdot31150+1=970353651,
$$

which will occur naturally in the Gauss-mixture rank threshold below.

None of the Round 28 deformation thresholds changes.

---

# 2. The parameter quadric

A symmetric quadratic core

$$
H_{y,z}
=
\gamma\omega^{a(y^2+z^2)+byz},
\qquad a\ne0,
$$

has row inverse transform

$$
\begin{aligned}
V(x,y)
&=
\sum_zH_{y,z}\omega^{-zx}\\
&=
\gamma G(a)
\omega^{ay^2-(by-x)^2/(4a)}.
\end{aligned}
$$

Writing

$$
\rho=\gamma G(a),
$$

the resulting two-variable quadratic phase is

$$
V(x,y)
=
\rho\,
\omega^{\kappa x^2+cxy+dy^2},
$$

with

$$
\kappa=-\frac1{4a},
\qquad
c=\frac b{2a},
\qquad
d=a-\frac{b^2}{4a}.
$$

A direct calculation gives

$$
4\kappa d-c^2
=
-\frac da-c^2
=
-1.
$$

Thus valid Gauss-core phase parameters lie on

$$
\boxed{\mathcal Q:\ 4\kappa d-c^2=-1,\qquad \kappa\ne0.}
\tag{2.1}
$$

Conversely, from a point \((\kappa,c,d)\in\mathcal Q\) with \(\kappa\ne0\),

$$
a=-\frac1{4\kappa},
\qquad
b=-\frac c{2\kappa},
$$

recover a unique original quadratic core.

---

# 3. Audit of the vector-valued determinant step

Let

$$
\Theta=\{\theta_1,\ldots,\theta_r\}
\subset\mathbb F_D^3
$$

be distinct parameter points.

Suppose every represented nonzero ordered difference

$$
\theta_i-\theta_j,\qquad i\ne j,
$$

has at least two ordered representations.

For every equality

$$
\theta_i-\theta_j=\theta_k-\theta_\ell
$$

between distinct ordered pairs, introduce

$$
r_{i,j,k,\ell}
=
e_i-e_j-e_k+e_\ell
\in\mathbb Z^r.
$$

Every such vector:

* has coordinate sum zero;
* has Euclidean norm at most \(\sqrt6\).

The norm \(\sqrt6\) occurs only in a three-index relation such as

$$
2e_i-e_j-e_k.
$$

Let \(\mathcal R\) be their rational span.

## 3.1 Full relation rank

If

$$
\dim_{\mathbb Q}\mathcal R=r-1,
$$

choose \(r-1\) independent relation rows. Delete one column so that the resulting integer matrix \(B\) is nonsingular.

Translate the deleted parameter point to zero. For each of the three parameter coordinates, the remaining coordinate vector lies in the modular kernel of \(B\). Since the parameter points are not all equal, \(B\) cannot be invertible modulo \(D\). Hence

$$
D\mid\det B.
$$

Hadamard gives

$$
|\det B|
\le
(\sqrt6)^{r-1}.
$$

Therefore

$$
D\le6^{(r-1)/2},
$$

or

$$
\boxed{D^2\le6^{r-1}.}
\tag{3.1}
$$

## 3.2 Deficient relation rank

Suppose

$$
\dim_{\mathbb Q}\mathcal R\le r-2.
$$

If no vector \(e_i-e_j\) belongs to \(\mathcal R\), choose

$$
x\in\mathcal R^\perp
$$

with all \(x_i\) distinct. This is possible because over \(\mathbb R\), a finite union of proper hyperplanes cannot cover \(\mathcal R^\perp\).

Choose \(i\) and \(j\) where \(x_i\) is maximal and \(x_j\) minimal. The difference \(\theta_i-\theta_j\) has another representation, so for some distinct ordered pair \((k,\ell)\),

$$
e_i-e_j-e_k+e_\ell\in\mathcal R.
$$

Pairing with \(x\),

$$
x_i-x_j=x_k-x_\ell.
$$

But \(x_i-x_j\) is the unique maximal ordered difference among distinct real numbers. Hence

$$
(k,\ell)=(i,j),
$$

contradicting the requirement of a second representation.

Thus some \(e_i-e_j\in\mathcal R\). Choosing a maximal nonsingular relation minor and applying Cramer’s rule gives

$$
(\det B)(e_i-e_j)
$$

as an integer combination of relation rows. Evaluation on the parameter coordinates gives

$$
D\mid\det B,
$$

and once again

$$
D^2\le6^{r-1}.
$$

Therefore the candidate vector-valued determinant assertion is correct:

$$
\boxed{
\text{If every nonzero parameter difference is multiply represented, then }
D^2\le6^{r-1}.
}
\tag{3.2}
$$

Since

$$
6^{46}
=
623673825204293256669089197883129856
<
D^2
=
886499885479492515209635706825114329,
$$

every parameter set with \(r\le47\) has a lonely ordered difference.

---

# 4. Restricted-domain quadratic-phase Gram bound

Let

$$
\Omega=\mathbb F_D\times\mathbb F_D^\times.
$$

For a quadratic parameter

$$
\Delta=(A,B,C)\in\mathbb F_D^3,
$$

write

$$
\phi_\Delta(x,y)
=
\omega^{Ax^2+Bxy+Cy^2}.
$$

The diagonal Gram entry is

$$
\|\phi_\Delta\|_{\ell_2(\Omega)}^2
=
D(D-1).
$$

For distinct \(\Delta,\Delta'\), their Gram inner product is

$$
\mathfrak G(\Delta-\Delta')
=
\sum_{x\in\mathbb F_D}
\sum_{y\ne0}
\omega^{Ax^2+Bxy+Cy^2}
$$

for a nonzero quadratic form.

The full sum over all \((x,y)\in\mathbb F_D^2\) has magnitude:

* \(D\) if the quadratic form has rank two;
* \(D^{3/2}\) if it has rank one.

Removing the \(y=0\) row changes it by at most \(D\). Therefore

$$
\boxed{
|\mathfrak G(A,B,C)|
\le
D^{3/2}+D
\qquad
(A,B,C)\ne0.
}
\tag{4.1}
$$

Consequently, any set of \(L\) distinct restricted quadratic phases is linearly independent whenever

$$
D(D-1)>(L-1)(D^{3/2}+D).
$$

Divide by \(D\):

$$
D-1>(L-1)(\sqrt D+1).
$$

Because

$$
D=970330474^2+1,
$$

put

$$
R=970330474.
$$

Then

$$
R<\sqrt D<R+1,
$$

and for every

$$
L\le R
$$

one has

$$
L-1\le R-1<\sqrt D-1.
$$

Therefore

$$
(L-1)(\sqrt D+1)
<
(\sqrt D-1)(\sqrt D+1)
=
D-1.
$$

Thus:

$$
\boxed{
\text{Every collection of at most }970330474
\text{ distinct restricted quadratic phases is linearly independent.}
}
\tag{4.2}
$$

This is the key strengthening beyond candidate theorem A.

---

# 5. Candidate theorem A and its stronger form

Consider an effective mixture of \(r\) distinct quadratic cores,

$$
V(x,y)
=
\sum_{\nu=1}^r
\rho_\nu
\omega^{q_{\theta_\nu}(x,y)},
\qquad
\rho_\nu\ne0.
$$

Group its squared modulus by parameter differences:

$$
K_\Delta
=
\sum_{\substack{\nu,\mu\\
\theta_\nu-\theta_\mu=\Delta}}
\rho_\nu\overline{\rho_\mu}.
\tag{5.1}
$$

The number of possible grouped parameters is at most

$$
r(r-1)+1.
$$

For a baseline vector,

$$
|V(x,y)|^2=B^2
\qquad(y\ne0).
$$

Hence on \(\Omega\),

$$
\left(K_0-B^2\right)
+
\sum_{\Delta\ne0}
K_\Delta\phi_\Delta(x,y)
=
0.
\tag{5.2}
$$

The coefficient vector in (5.2) cannot be identically zero. If it were, then

$$
|V(x,y)|^2=B^2
$$

would hold for every \((x,y)\), including \(y=0\), contradicting the two exceptional baseline values at \(x=\pm1\).

## 5.1 The proposed 47-core theorem

For \(r\le47\),

$$
r(r-1)+1\le2163.
$$

The determinant lemma supplies a lonely parameter difference, whose grouped coefficient is a single nonzero product

$$
\rho_\nu\overline{\rho_\mu}\ne0.
$$

The corresponding phase family is linearly independent by (4.2), so (5.2) is impossible.

Thus candidate theorem A is correct.

## 5.2 Unconditional \(31150\)-core no-go

The lonely-difference lemma is unnecessary for a much stronger range.

For

$$
r=31150,
$$

$$
r(r-1)+1
=
970291351
<
970330474.
$$

Therefore all possible grouped phases in (5.2) are linearly independent, regardless of repeated parameter differences and regardless of cancellations within individual \(K_\Delta\).

Hence:

$$
\boxed{
\text{No effective symmetric quadratic Gauss mixture with }
1\le r\le31150
\text{ can be a baseline lift.}
}
\tag{Mixture31150NoGo}
$$

This removes the ordered-difference-Sidon hypothesis from the Round 28 bound.

The first rank not covered is

$$
r=31151,
$$

for which

$$
r(r-1)+1
=
970353651.
$$

---

## 5.3 Near-Sidon requirement at the first open rank

For any possible baseline mixture, let

$$
\mathcal D_{\rm act}
=
\{\Delta:K_\Delta\ne0\}
$$

together with \(\Delta=0\) if \(K_0-B^2\ne0\).

Equation (5.2) and (4.2) imply

$$
\boxed{
|\mathcal D_{\rm act}|
\ge970330475.
}
\tag{5.3}
$$

At \(r=31151\), the maximal number of grouped difference phases is

$$
970353651.
$$

Thus at most

$$
\boxed{
970353651-970330475=23176
}
$$

potential classes may be absent or cancel.

In particular, the ordinary difference set must satisfy

$$
\boxed{
|\Theta-\Theta|\ge970330475.
}
\tag{5.4}
$$

Its maximal possible size is \(970353651\). Therefore the first undecided rank is forced to be extremely close to ordered-difference Sidon.

This is stronger than the candidate unconditional 47-core theorem.

---

# 6. Audit of the quadric rulings

The parameter quadric is

$$
4\kappa d-c^2=-1.
$$

Consider an affine line on this quadric whose \(\kappa\)-coordinate is nonconstant. Since the line projects bijectively onto \(\mathbb F_D\), use

$$
t=\kappa
$$

as its affine parameter. Write

$$
c=mt+\varepsilon.
$$

At \(t=0\), the quadric equation gives

$$
\varepsilon^2=1,
\qquad
\varepsilon\in\{+1,-1\}.
$$

The remaining coordinate is forced:

$$
d
=
\frac{c^2-1}{4t}
=
\frac{m^2}{4}t+\frac{m\varepsilon}{2}.
$$

Thus every nonvertical affine ruling line has the form

$$
\boxed{
L_{m,\varepsilon}:
\quad
(\kappa,c,d)
=
\left(
t,\,
mt+\varepsilon,\,
\frac{m^2}{4}t+\frac{m\varepsilon}{2}
\right).
}
\tag{Ruling}
$$

Conversely, substitution proves that every such line lies on the quadric.

The two remaining affine ruling lines are

$$
\kappa=0,\qquad c=\pm1,
$$

with \(d\) arbitrary. They contain no valid Gauss core because valid cores require \(\kappa\ne0\).

Therefore the candidate classification is correct.

Every valid quadric point lies on exactly two nonvertical rulings:

$$
L_{(c-1)/\kappa,+}
\quad\text{and}\quad
L_{(c+1)/\kappa,-}.
$$

---

# 7. One-ruling arbitrary-rank no-go

For a point on \(L_{m,\varepsilon}\), its quadratic phase factors as

$$
\begin{aligned}
q_t(x,y)
&=
tx^2+(mt+\varepsilon)xy
+
\left(
\frac{m^2}{4}t+\frac{m\varepsilon}{2}
\right)y^2\\
&=
tX_m^2+\varepsilon yX_m,
\end{aligned}
$$

where

$$
X_m=x+\frac m2y.
$$

An arbitrary-rank mixture on this ruling is

$$
V(x,y)
=
\omega^{\varepsilon yX_m}
g_{m,\varepsilon}(X_m^2),
$$

with

$$
g_{m,\varepsilon}(s)
=
\sum_{t\ne0}A_t\omega^{ts}.
$$

For every \(y\ne0\), \(x\mapsto X_m\) is a bijection. Constant off-axis modulus therefore gives

$$
|g_{m,\varepsilon}(s)|=B
$$

for every square \(s\), including \(s=0\).

At \(y=0\),

$$
X_m=x,
$$

so

$$
|V(x,0)|=|g_{m,\varepsilon}(x^2)|=B
$$

for every \(x\). This cannot produce the two exceptional values at \(x=\pm1\).

Hence no arbitrary-rank single-ruling mixture is a baseline lift.

---

# 8. Paired-ruling arbitrary-rank no-go

Now allow both rulings of one slope:

$$
V(x,y)
=
\omega^{yX_m}g_{m,+}(X_m^2)
+
\omega^{-yX_m}g_{m,-}(X_m^2).
$$

Fix \(X_m\ne0\). As \(y\) ranges over \(\mathbb F_D^\times\),

$$
r=yX_m
$$

ranges over all nonzero field elements.

Put

$$
A=g_{m,+}(X_m^2),
\qquad
B_-=g_{m,-}(X_m^2).
$$

Then

$$
|V|^2
=
|A|^2+|B_-|^2
+
2\operatorname{Re}
\left(
A\overline{B_-}\omega^{2r}
\right).
$$

For \(D\ge5\), the values \(\omega^{2r}\), \(r\ne0\), include at least three distinct points on the unit circle.

If

$$
A\overline{B_-}\ne0,
$$

constant real part would force at least three points of the unit circle to lie on one line, impossible. Therefore

$$
\boxed{
A\overline{B_-}=0,
\qquad
|A|^2+|B_-|^2=B^2.
}
\tag{8.1}
$$

This holds for every nonzero square \(X_m^2\).

At \(y=0\) and \(x\ne0\),

$$
V(x,0)
=
g_{m,+}(x^2)+g_{m,-}(x^2).
$$

By (8.1),

$$
|V(x,0)|^2=B^2.
$$

In particular, the values at \(x=\pm1\) are \(B\), not \(A_{\rm sp}\).

Thus:

$$
\boxed{
\text{No arbitrary-rank mixture supported on }
L_{m,+}\cup L_{m,-}
\text{ is a baseline lift.}
}
\tag{RulingNoGo}
$$

Candidate theorem B is correct.

It applies to exactly one ruling slope and its two signs. It is not a theorem for multiple slopes.

---

# 9. Global support propagation

Let

$$
H=Q+E
$$

be a symmetric, centrally even deformation of one quadratic core.

A baseline deformation must modify at least one nonzero row. Otherwise, symmetry gives

$$
E_{0,y}=E_{y,0}=0
\quad(y\ne0),
$$

so only \(E_{0,0}\) could change; the bordered-core circle argument then rules out the two spikes.

Choose a modified nonzero row \(y\). The audited MUB-deformation theorem gives

$$
|\operatorname{supp}E_{y,\cdot}|
\ge777716.
$$

At most one changed coordinate can be the zero column. Hence at least

$$
777715
$$

changed columns are nonzero.

By symmetry,

$$
E_{y,z}=E_{z,y},
$$

so every such nonzero column \(z\) is itself a modified nonzero row.

Each of these rows has at least \(777716\) changed entries. Counting ordered matrix positions by row gives

$$
\boxed{
|\{(y,z):y\ne0,\ E_{y,z}\ne0\}|
\ge
777715\cdot777716.
}
$$

The product is

$$
\boxed{
777715\cdot777716
=
604841398940.
}
\tag{GlobalDensity}
$$

The candidate global-density conclusion is correct.

It is a necessary complexity bound, not a contradiction.

---

# 10. Exact two-slope parameter-difference bookkeeping

The first open ruling configuration uses at least two distinct slopes.

For one line write

$$
\theta_{m,\varepsilon}(t)
=
\left(
t,\,
mt+\varepsilon,\,
\frac{m^2}{4}t+\frac{m\varepsilon}{2}
\right),
\qquad t\ne0.
$$

Suppose the effective parameter set is contained in the four lines

$$
L_{m,+},\ L_{m,-},\ L_{n,+},\ L_{n,-},
\qquad m\ne n.
$$

Repeated physical cores at intersections are combined first.

For amplitudes \(\rho_{\sigma,t}\), define the grouped autocorrelation

$$
\boxed{
K_\Delta
=
\sum_{\substack{\sigma,\tau,t,s\\
\theta_\sigma(t)-\theta_\tau(s)=\Delta}}
\rho_{\sigma,t}
\overline{\rho_{\tau,s}}.
}
\tag{10.1}
$$

## 10.1 Same-line differences

On one exact ruling,

$$
\theta_{m,\varepsilon}(t)
-
\theta_{m,\varepsilon}(s)
=
\left(
r,\,
mr,\,
\frac{m^2}{4}r
\right),
\qquad r=t-s.
\tag{10.2}
$$

Thus these terms are ordinary one-dimensional autocorrelations in \(t\).

## 10.2 Paired signs of one slope

For the ordered pair \(+\to-\),

$$
\theta_{m,+}(t)-\theta_{m,-}(s)
=
\left(
r,\,
mr+2,\,
\frac{m^2}{4}r+m
\right).
\tag{10.3}
$$

For the reverse order,

$$
\theta_{m,-}(t)-\theta_{m,+}(s)
=
\left(
r,\,
mr-2,\,
\frac{m^2}{4}r-m
\right).
\tag{10.4}
$$

## 10.3 Distinct slopes

Fix an ordered line pair

$$
(m,\varepsilon)\to(n,\eta),
\qquad m\ne n.
$$

If

$$
\Delta=(A,B,C)
=
\theta_{m,\varepsilon}(t)
-
\theta_{n,\eta}(s),
$$

then

$$
A=t-s
$$

and

$$
B=mt-ns+\varepsilon-\eta.
$$

Therefore

$$
\boxed{
t=
\frac{B-nA-\varepsilon+\eta}{m-n},
\qquad
s=t-A.
}
\tag{10.5}
$$

Thus for each fixed ordered pair of ruling lines, a full parameter difference has at most one contributing ordered pair of cores.

All multiple representations arise from collisions among the finitely many ordered ruling-line types and from the same-line autocorrelations (10.2).

This is the exact grouped two-slope coefficient system.

---

# 11. Full Fourier-dual Gauss system

Let

$$
\psi_\Delta(x,y)
=
\omega^{Ax^2+Bxy+Cy^2},
\qquad
\Delta=(A,B,C).
$$

For a baseline vector,

$$
|V(x,y)|^2
=
B^2
+
DB^2\mathbf1_{\{y=0\}}
\left(
\mathbf1_{\{x=1\}}
+
\mathbf1_{\{x=-1\}}
\right).
$$

Since

$$
DB^2=\frac1{D+2},
$$

define

$$
c_0=K_0-B^2,
\qquad
c_\Delta=K_\Delta\quad(\Delta\ne0).
$$

Then the exact full-domain identity is

$$
\boxed{
\sum_\Delta c_\Delta\psi_\Delta(x,y)
=
\frac1{D+2}
\mathbf1_{\{y=0\}}
\left(
\mathbf1_{\{x=1\}}
+
\mathbf1_{\{x=-1\}}
\right).
}
\tag{11.1}
$$

Use the unnormalized ordinary Fourier transform

$$
\widehat f(\xi,\eta)
=
\sum_{x,y}
f(x,y)\omega^{-\xi x-\eta y}.
$$

Equation (11.1) becomes

$$
\boxed{
\sum_\Delta
c_\Delta\,
\widehat\psi_\Delta(\xi,\eta)
=
\frac{\omega^\xi+\omega^{-\xi}}{D+2}
\qquad
\forall\,\xi,\eta.
}
\tag{TwoSlopeDualGauss}
$$

The right side is independent of \(\eta\).

---

## 11.1 Exact transforms

Let

$$
\mathfrak g
=
\sum_{t\in\mathbb F_D}\omega^{t^2},
\qquad
|\mathfrak g|=\sqrt D.
$$

Since \(D\equiv1\pmod4\), \(\mathfrak g\) is real and
\(\mathfrak g^2=D\).

Put

$$
\Delta_q=4AC-B^2.
$$

### Nondegenerate case

If \(\Delta_q\ne0\),

$$
\boxed{
\widehat\psi_\Delta(\xi,\eta)
=
\chi(\Delta_q)D\,
\omega^{
-\frac{C\xi^2-B\xi\eta+A\eta^2}{\Delta_q}
}.
}
\tag{11.2}
$$

### Rank-one case with \(A\ne0\)

If

$$
\Delta_q=0,\qquad A\ne0,
$$

then

$$
\boxed{
\widehat\psi_\Delta(\xi,\eta)
=
D\,\chi(A)\mathfrak g\,
\omega^{-\xi^2/(4A)}
\mathbf1_{\{\eta=B\xi/(2A)\}}.
}
\tag{11.3}
$$

### Rank-one case with \(A=B=0\)

If

$$
A=B=0,\qquad C\ne0,
$$

then

$$
\boxed{
\widehat\psi_\Delta(\xi,\eta)
=
D\,\chi(C)\mathfrak g\,
\omega^{-\eta^2/(4C)}
\mathbf1_{\{\xi=0\}}.
}
\tag{11.4}
$$

### Zero phase

For \(\Delta=0\),

$$
\widehat\psi_0(\xi,\eta)
=
D^2\mathbf1_{\{(\xi,\eta)=(0,0)\}}.
$$

Thus every individual transform in `TwoSlopeDualGauss` is explicit. There is no unevaluated scalar Weil or Kloosterman sum at this stage.

The open issue is the simultaneous nonlinear cancellation of these explicit dual chirps by coefficients \(c_\Delta\) which themselves must be grouped autocorrelations of the ruling amplitudes.

---

# 12. Exact multi-slope complexity threshold

The relation obtained by restricting (11.1) to \(y\ne0\) is nonzero as a formal grouped coefficient relation, because otherwise the row \(y=0\) would also be flat and the two spikes would disappear.

Section 4 therefore gives:

$$
\boxed{
|\operatorname{supp}c|
\ge970330475.
}
\tag{12.1}
$$

This applies to every multi-slope Gauss mixture, including arbitrary-rank two-slope mixtures.

Consequently:

$$
\boxed{
r\ge31151
}
\tag{12.2}
$$

for the number \(r\) of effective distinct Gauss cores.

Together with `RulingNoGo`, every possible Gauss-mixture baseline lift must satisfy all three requirements:

$$
\boxed{
\begin{aligned}
&\text{at least two distinct ruling slopes},\\
&\text{at least }31151\text{ effective cores},\\
&\text{at least }970330475\text{ active grouped difference phases}.
\end{aligned}
}
\tag{12.3}
$$

At the first possible rank \(31151\), its grouped autocorrelation support must be within \(23176\) classes of the maximum possible size.

This is the strongest exact multi-slope consequence obtained here.

---

# 13. First genuinely open cancellation system

For exactly two slopes \(m\ne n\), combine:

1. the line-pair recovery formulas (10.2)–(10.5);
2. the nonlinear grouped products (10.1);
3. the exact dual equations `TwoSlopeDualGauss`.

The unknowns are the effective amplitudes

$$
\rho_{\sigma,t}
$$

on the four ruling lines. The grouped coefficients must satisfy

$$
K_{-\Delta}=\overline{K_\Delta},
\qquad
K_0=\sum_{\sigma,t}|\rho_{\sigma,t}|^2,
$$

and the equations

$$
\sum_\Delta
c_\Delta
\widehat\psi_\Delta(\xi,\eta)
=
\frac{\omega^\xi+\omega^{-\xi}}{D+2}
$$

for every \((\xi,\eta)\).

Every matrix entry is an explicit quadratic Gauss value. What is not known is whether the nonlinear autocorrelation variety defined by (10.1) intersects this explicit affine Fourier system.

This is the first unresolved two-slope system.

It is strictly smaller and more structured than the original \(D^2\) baseline phase problem:

* parameters lie on four explicit ruling lines;
* each distinct-slope line-pair contributes at most one product to each \(K_\Delta\);
* rank-one differences are confined to the two ruling directions;
* every other contribution is a fully explicit nondegenerate dual chirp.

No exact solution or contradiction is obtained.

---

# 14. Scope of the results

The following families are now excluded exactly:

* every effective Gauss mixture with at most \(31150\) distinct cores;
* every arbitrary-rank mixture supported on one ruling slope, even allowing both signs;
* every deformation of one core with fewer than \(777716\) changed coefficients in each modified nonzero row;
* the bordered-core family;
* every genuine two-core mixture.

The following remain open:

* rank \(31151\) and above;
* arbitrary-rank mixtures on two distinct slopes;
* mixtures on more slopes with large grouped-difference support;
* dense genuinely nonquadratic baseline solutions.

The small-prime continuation evidence remains numerical only and is consistent with the new theorem: the numerically observed solutions use all nontrivial shear characters and are not bounded-complexity Gauss mixtures.

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

* The corrected dictionary count

  $$
  604842954373.
  $$
* `ParameterQuadric`.
* The vector-valued determinantal repeated-difference lemma.
* Candidate theorem A.
* The restricted-domain Gauss bound

  $$
  |\mathfrak G|\le D^{3/2}+D.
  $$
* Linear independence of every set of at most

  $$
  970330474
  $$

  restricted quadratic phases.
* The unconditional no-go through \(31150\) effective cores.
* The near-Sidon requirement at rank \(31151\).
* The exact classification of nonvertical affine ruling lines.
* The single-ruling and paired-ruling arbitrary-rank no-go.
* Candidate theorem B.
* `GlobalDensity`.
* The exact grouped two-slope difference formulas.
* The exact Fourier-dual Gauss system.

# CORRECTED

* Candidate theorem A is valid but not sharp: \(47\) improves to \(31150\) without any Sidon assumption.
* The Round 28 ordered-difference-Sidon hypothesis is unnecessary below rank \(31151\).
* The first open rank is \(31151\), where at least \(970330475\) grouped phase classes must remain active.
* RulingNoGo applies to one slope with its two signs, not to several slopes.
* There is no unknown individual Weil/Kloosterman sum in the first two-slope dual system; every individual kernel entry is an explicit quadratic Gauss sum. The difficulty is simultaneous nonlinear cancellation.

# DISPROVED

* Existence of any effective baseline Gauss mixture with at most \(31150\) distinct cores.
* Existence of any arbitrary-rank baseline mixture supported on

  $$
  L_{m,+}\cup L_{m,-}
  $$

  for one slope \(m\).
* Existence of a baseline deformation whose modified nonzero rows are all sparser than \(777716\).
* Sufficiency of the candidate 47-core threshold as the best available bounded-rank result.

# NECESSARY-ONLY

* At least \(31151\) effective Gauss cores.
* At least two ruling slopes.
* At least \(970330475\) active grouped parameter-difference classes.
* The near-Sidon condition at the first open rank.
* `GlobalDensity`.
* The full nonlinear `TwoSlopeDualGauss` system.

# EQUIVALENT

Within a fixed Gauss-mixture ansatz, the baseline magnitude equations are equivalent to:

1. the grouped autocorrelation definition (10.1); and
2. the full Fourier-dual system `TwoSlopeDualGauss`.

On the off-axis domain alone, they are equivalent to the vanishing restricted quadratic-phase relation (5.2).

# NUMERICAL-ONLY

* Machine-precision baseline lifts at

  $$
  D=3,5,7,11,13,17,19.
  $$
* Their observed full-character occupancy.
* Their generic-looking coefficient singular values.
* Any extrapolation to the frozen prime.

# CONJECTURED

* Existence of a dense full-character baseline lift at the frozen prime.
* Persistence of the small-prime continuation branch.
* Solvability of the two-slope nonlinear Gauss system at high rank.

# OPEN

* The exact two-slope system at rank \(31151\) and above.
* Multi-slope mixtures with at least \(970330475\) active difference classes.
* Dense nonquadratic baseline solutions.
* Existence of any exact baseline pure-edge vector.
* Pure retrieval for the frozen named edges.
* Physical liftability of \(x^{(10)}\).
* An exact physical vector with objective above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the unconditional bounded-rank theorem

$$
\boxed{
r\le31150
\quad\Longrightarrow\quad
\text{no effective symmetric Gauss mixture can be a baseline lift},
}
$$

together with its exact first-open-rank consequence

$$
\boxed{
r=31151
\quad\Longrightarrow\quad
|\operatorname{supp}c|
\ge970330475.
}
$$
