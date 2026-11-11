# Verdict

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

The edge-Fourier identity is correct, but it has a stronger consequence than the stated equality of two probability distributions:

$$
\boxed{\mathscr F d_h=d_h\qquad\text{for every }h,}
$$

where \(\mathscr F\) is the normalized symplectic Fourier transform. Thus every physical edge field must be a \(+1\) Fourier eigenvector with prescribed pointwise magnitudes.

For the exact frozen pseudo-magnitude \(x^{(10)}\):

* all one-\(h\) collision, polygon, support, and two-basis mixed-state tests pass;
* for every nonzero \(h\), an explicit analytic positive-semidefinite two-basis witness exists;
* this applies in particular to \(z_\star=(0,1)\) and

  $$
  h_\star=(970330475,1940660948)=a_1-a_0;
  $$
* the remaining one-\(h\) requirement is the **pure Fourier-eigenvector phase retrieval problem**, not merely compatibility of two measurement marginals;
* across different \(h\), the first surviving condition is a rank-one triangle phase cycle.

The centered Fourier identity at the special frequency \(k=h/2\) is exactly the already audited oriented centered-idempotence equation. Thus the full edge-Fourier family contains the global physical-lift problem rather than bypassing it.

No physical lift, no contradiction excluding \(x^{(10)}\), and no phase-uniform proof of PW10 is obtained.

---

# 1. Mandatory Round 21 corrections

The following narrower formulations are retained.

1. `FullTwoLineAverage` is verified and explicitly contains unresolved KD/Bargmann quantities. This does **not** prove that no cancellation or simplification occurs after all physical compatibility equations are imposed.

2. The safe weighted-extraction envelope is

   $$
   \sqrt8D\sqrt{\lambda_z^2+M^2+6M}
   \le
   4DM\sqrt{1+\frac3M},
   $$

   which is slightly larger than \(4DM\). No sharper exact value of the relevant \(\lambda_z\) was evaluated.

3. The anti-projector symmetry proves that the rank-two displacement equations are not a positivity selector when a solution exists. It does not prove consistency of those equations for \(x^{(10)}\).

4. The quantities at \(z_\star=(0,1)\) involving translated frozen sums remain exact but unevaluated cyclotomic expressions. Only rigorous pointwise bounds were supplied.

5. In the shorthand formula for \(G_\Gamma\), the genuine off-diagonal restriction is

   $$
   v\ne u,\qquad v\ne z-u.
   $$

---

# 2. Derivation of the edge-Fourier identity

Let

$$
P=|\psi\rangle\langle\psi|,
\qquad
\alpha_z=\operatorname{Tr}(W_z^*P),
\qquad
\alpha_{-z}=\overline{\alpha_z}.
$$

For

$$
d_h(p)
=
\alpha_{p+h/2}\overline{\alpha_{p-h/2}},
$$

define the unnormalized Fourier transform

$$
\widehat d_h(k)
=
\sum_p d_h(p)\omega^{[p,k]}.
$$

Because \(P\) has rank one,

$$
\operatorname{Tr}(PA)\operatorname{Tr}(PB)
=
\operatorname{Tr}(PAPB).
$$

Apply this with

$$
A=W_{-h/2-k},
\qquad
B=W_{-h/2+k}.
$$

Then

$$
\begin{aligned}
&\alpha_{h/2+k}\alpha_{h/2-k}\\
&\quad=
\operatorname{Tr}
\left(
PW_{-h/2-k}
P
W_{-h/2+k}
\right).
\end{aligned}
$$

Insert

$$
P=\frac1D\sum_r\alpha_rW_r.
$$

Weyl multiplication gives

$$
W_{-h/2-k}W_rW_{-h/2+k}
=
\omega^{[r,k]-[h,k]/2}W_{r-h}.
$$

Since

$$
\operatorname{Tr}(PW_{r-h})=\alpha_{h-r},
$$

we get

$$
\alpha_{h/2+k}\alpha_{h/2-k}
=
\frac1D
\sum_r
\alpha_r\alpha_{h-r}
\omega^{[r,k]-[h,k]/2}.
$$

Set \(r=p+h/2\). Then

$$
\alpha_{h-r}
=
\alpha_{h/2-p}
=
\overline{\alpha_{p-h/2}},
$$

and the phase becomes \(\omega^{[p,k]}\). Therefore

$$
\boxed{
\widehat d_h(k)
=
D\alpha_{h/2+k}\alpha_{h/2-k}.
}
\tag{EdgeFourier}
$$

All half-labels are well defined because \(D\) is odd.

---

# 3. The stronger self-Fourier consequence

Using Hermiticity,

$$
\alpha_{h/2-k}
=
\overline{\alpha_{k-h/2}}.
$$

Consequently,

$$
\alpha_{h/2+k}\alpha_{h/2-k}
=
d_h(k).
$$

Hence EdgeFourier is equivalently

$$
\boxed{\widehat d_h(k)=Dd_h(k).}
\tag{3.1}
$$

Define the normalized Fourier transform on the \(D^2\)-point phase space by

$$
(\mathscr Ff)(k)
=
\frac1D\sum_pf(p)\omega^{[p,k]}.
$$

Then

$$
\boxed{\mathscr Fd_h=d_h.}
\tag{3.2}
$$

This is stronger than merely prescribing the magnitudes in two mutually unbiased bases.

## 3.1 Symmetries

A direct use of \(\alpha_{-z}=\overline{\alpha_z}\) gives

$$
\boxed{d_h(-p)=d_h(p),}
\tag{3.3}
$$

and

$$
\boxed{d_{-h}(p)=\overline{d_h(p)}.}
\tag{3.4}
$$

The Fourier \(+1\) property implies the evenness independently because \(\mathscr F^2\) is phase-space reflection.

## 3.2 Magnitudes

The time-domain magnitude is

$$
\boxed{
|d_h(p)|^2
=
x_{p+h/2}x_{p-h/2}.
}
$$

The Fourier magnitude is

$$
\boxed{
|\widehat d_h(k)|^2
=
D^2x_{h/2+k}x_{h/2-k}.
}
$$

These are the proposed `EdgeFourierMagnitude` identities.

---

# 4. Centered edge identity

Put

$$
\beta=\alpha-\delta_0,
\qquad
\beta_0=0,
$$

and

$$
d_h^\beta(p)
=
\beta_{p+h/2}\overline{\beta_{p-h/2}}.
$$

For \(h\ne0\), the only removed terms occur at \(p=\pm h/2\). Each removed value equals \(\alpha_h\). Thus

$$
\boxed{
\begin{aligned}
\widehat d_h^\beta(k)
={}&
D\alpha_{h/2+k}\alpha_{h/2-k}\\
&-
\alpha_h
\left(
\omega^{[h,k]/2}
+
\omega^{-[h,k]/2}
\right).
\end{aligned}
}
\tag{CenteredEdgeFourier}
$$

For \(h=0\),

$$
d_0^\beta(p)=x_p-\delta_{p,0},
$$

so self-Fourier symmetry of \(x\) gives

$$
\boxed{
\widehat d_0^\beta(k)=Dx_k-1.
}
\tag{4.1}
$$

## 4.1 The diagonal slice is exactly centered idempotence

Set \(k=h/2\). Then

$$
\widehat d_h^\beta(h/2)
=
(D-2)\alpha_h.
\tag{4.2}
$$

On the other hand,

$$
\begin{aligned}
\widehat d_h^\beta(h/2)
&=
\sum_p
\beta_{p+h/2}
\beta_{h/2-p}
\omega^{[p,h]/2}\\
&=
\sum_u
\beta_u\beta_{h-u}
\omega^{[u,h]/2}.
\end{aligned}
$$

Therefore

$$
\boxed{
\sum_u
\beta_u\beta_{h-u}
\omega^{[u,h]/2}
=
(D-2)\beta_h,
}
\tag{4.3}
$$

which is precisely `OrientedCoefficient`.

Thus:

$$
\boxed{
\text{the }k=h/2\text{ slice of centered EdgeFourier is full centered idempotence.}
}
$$

The edge-Fourier route contains the old global lift equation rather than replacing it by an independent weaker structure.

---

# 5. Edge autocorrelation

Let

$$
E_h
=
\sum_p|d_h(p)|^2
=
\sum_p
x_{p+h/2}x_{p-h/2}.
$$

Unnormalized Fourier Parseval on \(D^2\) points gives

$$
\sum_k|\widehat d_h(k)|^2=D^2E_h.
$$

For a displacement \(s\),

$$
\begin{aligned}
&\sum_p
d_h(p)\overline{d_h(p-s)}\\
&\quad=
\frac1{D^2}
\sum_k|\widehat d_h(k)|^2\omega^{-[s,k]}.
\end{aligned}
$$

Substituting EdgeFourierMagnitude yields

$$
\boxed{
\sum_p
d_h(p)\overline{d_h(p-s)}
=
\sum_k
x_{h/2+k}x_{h/2-k}
\omega^{-[s,k]}.
}
\tag{EdgeAutocorrelation}
$$

The Fourier sign is correct for the transform convention used above.

---

# 6. Normalized one-\(h\) phase retrieval

Put

$$
r_h(p)=x_{p+h/2}x_{p-h/2}.
$$

Then

$$
E_h=\sum_pr_h(p).
$$

Define

$$
q_h(p)=\frac{r_h(p)}{E_h},
\qquad
\widetilde q_h(k)=
\frac{x_{h/2+k}x_{h/2-k}}{E_h}.
$$

These are in fact the same numerical function:

$$
\boxed{q_h=\widetilde q_h.}
\tag{6.1}
$$

If

$$
v_h=\frac{d_h}{\sqrt{E_h}},
$$

then \(q_h\) is its standard-basis distribution and \(\widetilde q_h\) is its symplectic-Fourier-basis distribution.

The physical requirement is stronger:

$$
\boxed{\mathscr Fv_h=v_h.}
\tag{6.2}
$$

Thus the true one-\(h\) problem is Fourier-eigenvector phase retrieval.

---

# 7. Frozen pointwise bounds

For every nonzero \(z\), the exact formula for \(x^{(10)}\) gives

$$
\boxed{
\gamma\le x_z^{(10)}\le U,
}
\tag{7.1}
$$

where

$$
\gamma=
\frac{D(m-11)-10m}
{D(D+1)(m-1)}
$$

and

$$
U=
\frac{11}{D+1}+\frac{10}{M}.
$$

At the exact frozen integers,

$$
U<7\times10^{-17},
\tag{7.2}
$$

and

$$
D\gamma>1-3\times10^{-8}.
\tag{7.3}
$$

The value \(x_0=1\) also satisfies \(x_0\ge\gamma\).

---

# 8. A uniform enclosure for every nonzero \(h\)

Write

$$
x^{(10)}=b+\eta.
$$

The exact self-Fourier construction gives

$$
\boxed{
\|\eta\|_2^2
=
\frac{20}{M}
\left(
\mathcal O_{10}-\frac{M}{D+1}
\right).
}
\tag{8.1}
$$

Since \(\mathcal O_{10}\le MU\),

$$
\|\eta\|_2^2
\le
\frac{200}{D+1}+\frac{200}{M}.
$$

Exact cross multiplication yields

$$
\boxed{
\|\eta\|_2^2
<
\frac{49}{4\cdot10^{16}}.
}
\tag{8.2}
$$

Also

$$
\|b\|_2^2=\frac{2D}{D+1}<2.
$$

Define

$$
\varepsilon_x
=
2\|b\|_2\|\eta\|_2+\|\eta\|_2^2.
$$

Then

$$
\boxed{
\varepsilon_x<\frac{53}{5\cdot10^8}
=1.06\times10^{-7}.
}
\tag{8.3}
$$

For \(h\ne0\), the baseline edge energy is

$$
E_h^{\,b}
=
\frac{D(D+2)}{(D+1)^2}<1.
$$

Translation is unitary on \(\ell_2(V)\), so

$$
|E_h-E_h^{\,b}|\le\varepsilon_x.
$$

Therefore

$$
\boxed{
D^2\gamma^2
\le E_h
<
1+1.06\times10^{-7}.
}
\tag{8.4}
$$

Moreover,

$$
2D^2\gamma^2
>
2(1-3\times10^{-8})^2
>
1.99999988.
$$

Hence

$$
\boxed{
\frac{\gamma^2}{E_h}>
\frac1{2D^2}.
}
\tag{8.5}
$$

This lower bound is the key to the exact two-basis PSD witness below.

---

# 9. Two-MUB collision test

Let

$$
N=D^2.
$$

For any pure vector in dimension \(N\), the collision probabilities in two mutually unbiased bases obey

$$
\sum_pq(p)^2+\sum_k\widetilde q(k)^2
\le1+\frac1N.
\tag{9.1}
$$

A self-contained proof is obtained by writing the pure density matrix as

$$
\tau=\frac IN+A
$$

with \(A\) traceless. The two traceless diagonal subspaces associated with mutually unbiased bases are Hilbert–Schmidt orthogonal. The sum of the squared norms of the two diagonal projections of \(A\) is therefore at most

$$
\|A\|_2^2=1-\frac1N.
$$

Adding the two uniform contributions gives (9.1).

Because \(q_h=\widetilde q_h\),

$$
\boxed{
2\sum_pq_h(p)^2
\le1+\frac1{D^2}.
}
\tag{9.2}
$$

## 9.1 Uniform frozen margin for every \(h\ne0\)

There are two values \(p=\pm h/2\) at which one factor in \(r_h(p)\) is \(x_0\); hence

$$
r_h(p)\le U
$$

at those two points. At every other point,

$$
r_h(p)\le U^2.
$$

Therefore

$$
\sum_pr_h(p)^2
\le
2U^2+(D^2-2)U^4.
$$

Using

$$
D<10^{18},
\qquad
U<7\times10^{-17},
\qquad
D\gamma>1-3\times10^{-8},
$$

gives the rigorous enclosure

$$
\boxed{
2\sum_pq_h(p)^2
<
5\times10^{-29}.
}
\tag{9.3}
$$

Thus the two-MUB collision inequality passes with an enormous margin for every nonzero \(h\).

---

# 10. Every polygon inequality from EdgeAutocorrelation passes

For fixed \(h,s\), put

$$
\ell_p
=
|d_h(p)|\,|d_h(p-s)|
=
\sqrt{r_h(p)r_h(p-s)}.
$$

A complex number \(R\) can be a sum of vectors having lengths \(\ell_p\) only if

$$
\boxed{
\max\{0,2\ell_{\max}-L\}
\le |R|\le L,
\qquad
L=\sum_p\ell_p.
}
\tag{10.1}
$$

This is the complete polygon/reverse-triangle condition.

For \(h\ne0\) and \(s\ne0\),

$$
L\ge D^2\gamma^2>0.99999994.
\tag{10.2}
$$

Also \(r_h(p)\le U\), so

$$
\ell_{\max}\le U<7\times10^{-17}.
$$

Hence

$$
2\ell_{\max}-L<0.
$$

The reverse-triangle lower endpoint is therefore zero.

For the upper endpoint, compare with the baseline \(b\). For \(h,s\ne0\),

$$
\left|
\sum_pr_h^{\,b}(p)\omega^{-[s,p]}
\right|
\le
\frac2{D+1}.
$$

The \(\ell_1\)-difference between the frozen and baseline edge products is bounded by \(\varepsilon_x\). Therefore

$$
\boxed{
\left|
\sum_kr_h(k)\omega^{-[s,k]}
\right|
<
1.07\times10^{-7}.
}
\tag{10.3}
$$

Combining (10.2)–(10.3), every polygon condition passes strictly.

For \(s=0\), EdgeAutocorrelation is the identity \(E_h=E_h\).

---

# 11. The three requested values of \(h\)

## 11.1 \(h=0\)

Here

$$
d_0(p)=x_p^{(10)}.
$$

Since \(x^{(10)}\) is self-Fourier,

$$
\mathscr Fd_0=d_0.
$$

Thus the normalized vector

$$
v_0=\frac{x^{(10)}}{\sqrt{E_0}}
$$

is an explicit pure one-\(h\) solution. Its norm is

$$
\boxed{
E_0
=
\frac{2D}{D+1}
+
\frac{20}{M}
\left(
\mathcal O_{10}-\frac{M}{D+1}
\right).
}
\tag{11.1}
$$

This is the old global self-Fourier identity, not a new physical-lift constraint.

## 11.2 \(z_\star=(0,1)\)

This is nonzero, so all uniform bounds in Sections 8–10 apply:

$$
D^2\gamma^2\le E_{z_\star}<1+1.06\times10^{-7},
$$

the collision expression is below \(5\times10^{-29}\), and every polygon inequality passes.

No exact pure edge phase vector is constructed.

## 11.3 \(h_\star=a_1-a_0\)

One has

$$
t_0=0,\qquad t_1=2P_0+1=970330475.
$$

Using

$$
D=4P_0^2+1,
$$

$$
t_1^2
=
(2P_0+1)^2
\equiv4P_0
=
1940660948
\pmod D.
$$

Therefore

$$
\boxed{
h_\star
=
(970330475,1940660948).
}
$$

It is a nonzero element of \(\Gamma\), and the same uniform certified bounds apply.

---

# 12. Exact analytic two-basis PSD witness

The two-basis rank-relaxed problem asks for a density matrix \(K^{(h)}\) such that

$$
K^{(h)}\succeq0,
\qquad
\operatorname{Tr}K^{(h)}=1,
$$

whose standard-basis diagonal and symplectic-Fourier-basis diagonal both equal \(q_h\).

Let \(\mathsf F\) be the normalized \(D^2\times D^2\) symplectic Fourier matrix,

$$
\mathsf F_{k,p}
=
\frac1D\omega^{[p,k]}.
$$

For \(h\ne0\), define

$$
\boxed{
K^{(h)}
=
\operatorname{Diag}(q_h)
+
\mathsf F^*
\operatorname{Diag}(q_h)
\mathsf F
-
\frac1{D^2}I.
}
\tag{12.1}
$$

Because every entry of a Fourier basis vector has squared modulus \(1/D^2\),

$$
\operatorname{diag}
\left(
\mathsf F^*\operatorname{Diag}(q_h)\mathsf F
\right)
=
\frac1{D^2}\mathbf1.
$$

Hence

$$
\operatorname{diag}K^{(h)}=q_h.
$$

Similarly,

$$
\operatorname{diag}
\left(
\mathsf F K^{(h)}\mathsf F^*
\right)=q_h.
$$

Its trace is

$$
1+1-1=1.
$$

## 12.1 Positivity

Let

$$
q_{\min}=\min_pq_h(p).
$$

From (8.5),

$$
q_{\min}>
\frac1{2D^2}.
$$

Write

$$
q_h=q_{\min}\mathbf1+r,
\qquad r\ge0.
$$

Then

$$
\boxed{
\begin{aligned}
K^{(h)}
={}&
\left(
2q_{\min}-\frac1{D^2}
\right)I\\
&+
\operatorname{Diag}(r)
+
\mathsf F^*\operatorname{Diag}(r)\mathsf F.
\end{aligned}
}
\tag{12.2}
$$

Every term on the right is positive semidefinite. Thus

$$
\boxed{K^{(h)}\succeq0.}
$$

This is an exact analytic primal witness for every nonzero \(h\), including \(z_\star\) and \(h_\star\).

For \(h=0\), the rank-one witness

$$
K^{(0)}
=
|v_0\rangle\langle v_0|
$$

works.

Therefore:

$$
\boxed{
\text{the exact two-basis PSD relaxation is feasible for every }h.
}
$$

It cannot exclude the frozen pseudo-magnitude.

It does not solve the pure edge-vector problem because \(K^{(h)}\) need not have rank one or be supported in the \(+1\) Fourier eigenspace.

---

# 13. Cross-\(h\) rank-one consistency

For \(a,b\in V\), define

$$
Y_{a,b}^{\mathrm{time}}
=
d_{a-b}\!\left(\frac{a+b}{2}\right).
$$

Then

$$
Y_{a,b}^{\mathrm{time}}
=
\alpha_a\overline{\alpha_b}.
$$

Also define

$$
Y_{a,b}^{\mathrm{freq}}
=
\frac1D
\widehat d_{a-b}\!\left(\frac{a+b}{2}\right).
$$

EdgeFourier gives

$$
Y_{a,b}^{\mathrm{freq}}
=
\alpha_a\overline{\alpha_b}.
$$

Hence a physical family must satisfy

$$
\boxed{
Y^{\mathrm{time}}=Y^{\mathrm{freq}}
=\alpha\alpha^*.
}
\tag{13.1}
$$

In particular, the full matrix \(Y\) is positive semidefinite of rank one and has diagonal \(x\).

The rank-one minors give

$$
\boxed{
Y_{a,b}Y_{b,c}
=
x_bY_{a,c},
}
\tag{EdgeCycle}
$$

which is the corrected form of the proposed equation.

---

# 14. Contraction over triples from \(A\)

For pairwise distinct \(a,b,c\in A\), summing EdgeCycle gives

$$
\boxed{
\sum_{\substack{a,b,c\in A\\\mathrm{distinct}}}
Y_{a,b}Y_{b,c}
=
\sum_{\substack{a,b,c\in A\\\mathrm{distinct}}}
x_bY_{a,c}.
}
\tag{14.1}
$$

This is true term by term. It is not \(T_A\), \(T_{\rm ext}\), or `GammaOriented`.

Indeed, the orbit-channel Bargmann term is

$$
\boxed{
\operatorname{Tr}(Q_aQ_bQ_c)
=
\omega^{-([a,b]+[b,c]+[c,a])/2}
\alpha_{a-b}\alpha_{b-c}\alpha_{c-a}.
}
\tag{14.2}
$$

Equation (14.1), by contrast, uses

$$
\alpha_a\overline{\alpha_b}
\alpha_b\overline{\alpha_c}
$$

and contains no Weyl cocycle. It is a rank-one consistency identity for the coefficient field restricted to \(A\), not an orbit moment.

Thus contracting EdgeCycle over \(A\) does not generate a new scalar obstruction.

---

# 15. The smallest explicit cross-\(h\) phase cycle

The first nontrivial cross-\(h\) compatibility condition uses three labels.

Take

$$
a_0=(0,0),
$$

$$
a_1=(970330475,1940660948),
$$

and, since \(r_2=4\),

$$
a_2=(1940660952,15525287596).
$$

Define

$$
Y_{rs}
=
\frac1D
\widehat d_{a_r-a_s}
\!\left(
\frac{a_r+a_s}{2}
\right).
$$

Then a physical family must satisfy

$$
\boxed{
Y_{01}Y_{12}Y_{20}
=
x_{a_0}x_{a_1}x_{a_2}
=
x_{a_1}x_{a_2}>0.
}
\tag{15.1}
$$

Equivalently,

$$
\arg Y_{01}+\arg Y_{12}+\arg Y_{20}=0
\pmod{2\pi}.
$$

The magnitude equality is automatic:

$$
|Y_{01}Y_{12}Y_{20}|
=
x_{a_0}x_{a_1}x_{a_2}.
$$

Thus this minimal triangle detects only phase inconsistency. It gives no magnitude contradiction for \(x^{(10)}\).

Separate one-\(h\) phase retrieval problems do not enforce (15.1). It is the first explicit cross-\(h\) condition that they lose.

---

# 16. Relation to centered idempotence

Although the triangle phase cycle is not one of the Round 22 scalar contractions, the full edge-Fourier family is not a new route around idempotence.

For every \(h\ne0\),

$$
\widehat d_h^\beta(h/2)
=
(D-2)\alpha_h
$$

is exactly `OrientedCoefficient`.

Consequently:

* solving the full centered edge equations at \(k=h/2\) for all \(h\ne0\) is equivalent to centered idempotence;
* `GammaOriented` and `GammaEnergy` are contractions of this diagonal slice over \(h\in\Gamma\);
* the remaining edge conditions consist of:

  1. pure \(+1\)-Fourier phase retrieval for each \(d_h\);
  2. rank-one consistency of the resulting edge fields across different \(h\).

The analytic \(K^{(h)}\) witness proves only that the two-basis **mixed-state** relaxation is too weak. It does not address either of these two surviving conditions.

---

# 17. Earliest exact remaining gap

The edge-Fourier attack reduces the frozen lift problem to the following hierarchy.

## One-\(h\) pure constraint

For every \(h\), find a vector \(d_h\) satisfying

$$
|d_h(p)|^2
=
x_{p+h/2}^{(10)}x_{p-h/2}^{(10)},
$$

and

$$
\boxed{\mathscr Fd_h=d_h.}
\tag{17.1}
$$

All phase-free collision, polygon, support, and mixed-state two-basis tests pass. No such pure vector is constructed for \(h=z_\star\), \(h=h_\star\), or all \(h\).

## Cross-\(h\) constraint

The edge fields must satisfy

$$
d_{a-b}\!\left(\frac{a+b}{2}\right)
d_{b-c}\!\left(\frac{b+c}{2}\right)
=
x_b
d_{a-c}\!\left(\frac{a+c}{2}\right)
$$

for all triples \(a,b,c\).

Equivalently, the matrix assembled from the edge fields must be one common rank-one matrix

$$
Y=\alpha\alpha^*.
$$

## Centered orientation constraint

At the diagonal frequency \(k=h/2\), the centered edge equation is the full oriented idempotence equation.

Thus the first unresolved statement is:

> Do there exist \(+1\)-Fourier edge vectors with the frozen prescribed magnitudes which can be assembled into one common rank-one matrix and whose centered diagonal slices satisfy idempotence?

No contradiction or construction is obtained.

---

# Status of the three closing outcomes

No exact unit vector with

$$
\mathcal F_\Gamma>10
$$

has been produced.

No exact contradiction excluding a physical lift of \(x^{(10)}\) has been produced.

No phase-uniform proof of PW10 has been produced.

Therefore

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$

---

# VERIFIED

* `EdgeFourier`, including the half-label and Fourier signs.
* `EdgeFourierMagnitude`.
* The stronger identity

  $$
  \mathscr Fd_h=d_h.
  $$
* \(d_h(-p)=d_h(p)\).
* \(d_{-h}(p)=\overline{d_h(p)}\).
* `EdgeCycle`.
* `CenteredEdgeFourier`, including both endpoint subtractions.
* \(\widehat d_0^\beta(k)=Dx_k-1\).
* `EdgeAutocorrelation`.
* The two-MUB collision inequality.
* The exact values

  $$
  z_\star=(0,1),
  \qquad
  h_\star=(970330475,1940660948).
  $$
* The exact uniform enclosures for every nonzero \(h\).
* Every collision and polygon test for \(z_\star\) and \(h_\star\).
* The analytic two-basis PSD witness \(K^{(h)}\).
* Feasibility of the rank-relaxed two-basis problem for every \(h\).
* The rank-one edge matrix \(Y=\alpha\alpha^*\).
* The minimal three-edge phase cycle.

# CORRECTED

* The new edge relation is not merely equality of time and Fourier probabilities: the edge field itself is a \(+1\) Fourier eigenvector.
* The one-\(h\) PSD relaxation is strictly weaker than the required pure Fourier-eigenvector problem.
* Contracting EdgeCycle over triples in \(A\) is not \(T_A\), \(T_{\rm ext}\), or `GammaOriented`.
* The centered diagonal edge slice is exactly the old oriented centered-idempotence equation.
* The Round 22 shorthand restriction on \(G_\Gamma\) is

  $$
  v\ne u,\qquad v\ne z-u.
  $$

# DISPROVED

* Sufficiency of the two-MUB collision inequality for excluding any nonzero \(h\).
* Sufficiency of all polygon/reverse-triangle autocorrelation inequalities.
* Sufficiency of the rank-relaxed two-basis PSD test.
* Any claim that separate one-\(h\) feasibility automatically supplies one common coefficient field.

# NECESSARY-ONLY

* Pure \(+1\)-Fourier edge phase retrieval for every \(h\).
* The triangle and higher rank-one edge cycles.
* Centered edge idempotence.
* The exact rank-one matrix condition \(Y=\alpha\alpha^*\).

# EQUIVALENT

* `EdgeFourier` and \(\mathscr Fd_h=d_h\).
* The \(k=h/2\) centered edge equation and `OrientedCoefficient`.
* Rank-one cross-\(h\) consistency and vanishing of all \(2\times2\) minors of \(Y\), together with its fixed positive diagonal.

# OPEN

* Pure one-\(h\) Fourier phase retrieval for \(z_\star\).
* Pure one-\(h\) Fourier phase retrieval for \(h_\star\).
* Simultaneous pure edge retrieval for all \(h\).
* Cross-\(h\) rank-one consistency.
* A physical phase lift of \(x^{(10)}\).
* An exact physical vector with objective above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first new claim requiring independent verification is the universal analytic witness

$$
\boxed{
K^{(h)}
=
\operatorname{Diag}(q_h)
+
\mathsf F^*\operatorname{Diag}(q_h)\mathsf F
-\frac1{D^2}I
\succeq0
\qquad(h\ne0),
}
$$

together with the frozen lower bound

$$
\min_pq_h(p)>\frac1{2D^2}.
$$
