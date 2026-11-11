# Verdict: **OPEN WITH EARLIEST GAP**

The low-\(A\) existential statement

$$
(E1_{\rm gap})
$$

is neither proved nor disproved by the available identities.

The earliest unresolved pointwise quantity is the **double-centered same-tuple correlation**

$$
\Gamma_U(T):=
\left\|
\bigl(Q\otimes Q\bigr)
\bigl(|\psi_T\rangle\langle\psi_T|\bigr)
\right\|_2^2,
\qquad
Q:=L-\Delta_D,
$$

where

$$
L(X)=\frac1m\sum_{a=1}^m U_aXU_a^*,
\qquad
\Delta_D(X)=\operatorname{Tr}(X)\frac{I_D}{D}.
$$

The one-copy frame flatness and the exact partial traces determine all scalar, one-sided, and marginal contributions to the target, but do not bound \(\Gamma_U(T)\) uniformly over all physical \(T\).

A new deterministic obstruction is proved below: averaging over **full-Schmidt-rank** inputs gives

$$
\boxed{
\kappa_1(U)\ge
\frac{m\bigl(\alpha_U^2+D^2\bigr)}
     {D^2(\alpha_U+1)}-1,
\qquad
\alpha_U:=\|C(I_D)\|_2^2.
}
\tag{Haar-LB}
$$

Consequently, any solution of \((E1_{\rm gap})\) must obey a new quadratic constraint on \(\alpha_U\), strictly stronger than the one-copy constraint at the maximally mixed input.

No randomness in \(U\) is used in this result.

---

# 1. Vectorization conventions and the frame identity

Use

$$
|X\rangle\rangle
=
\sum_{i=1}^D |i\rangle_A\otimes X|i\rangle_B.
$$

For \(M,N,X\in M_D\),

$$
(M\otimes N)|X\rangle\rangle
=
|N X M^{\mathsf T}\rangle\rangle.
\tag{1.1}
$$

Indeed,

$$
\begin{aligned}
(M\otimes N)|X\rangle\rangle
&=
\sum_{i,j}M_{ji}|j\rangle\otimes NX|i\rangle\\
&=
\sum_j|j\rangle\otimes NXM^{\mathsf T}|j\rangle.
\end{aligned}
$$

The Hilbert–Schmidt inner product agrees with vector inner product:

$$
\langle\langle X|Y\rangle\rangle=\operatorname{Tr}(X^*Y).
\tag{1.2}
$$

For a rank-one operator on \(A\otimes B\),

$$
\boxed{
\operatorname{Tr}_A|X\rangle\rangle\langle\langle X|
=
XX^*,
}
\tag{1.3}
$$

and

$$
\boxed{
\operatorname{Tr}_B|X\rangle\rangle\langle\langle X|
=
(X^*X)^{\mathsf T}.
}
\tag{1.4}
$$

Let

$$
z_{a,v}(T)=U_aTU_v^{\mathsf T},
\qquad
F_{T,v}
=
\sum_{a=1}^m
|z_{a,v}(T)\rangle\rangle
\langle\langle z_{a,v}(T)|,
$$

and

$$
F_T
=
\sum_{a=1}^m
|U_aT\rangle\rangle
\langle\langle U_aT|.
$$

Right multiplication by \(U_v^{\mathsf T}\) acts as \(U_v\) on subsystem \(A\). Thus, with

$$
\mathsf R_v=U_v\otimes I_D,
$$

one has

$$
\boxed{
F_{T,v}=\mathsf R_vF_T\mathsf R_v^*.
}
\tag{1.5}
$$

Define

$$
\mathfrak R_U(F)
=
\frac1m\sum_{v=1}^m
\mathsf R_vF\mathsf R_v^*.
\tag{1.6}
$$

Then

$$
\sum_vF_{T,v}=m\,\mathfrak R_U(F_T).
\tag{1.7}
$$

## 1.1 Frame overlaps and \(C(X_{vw})\)

Set

$$
A_{vw}=U_w^*U_v.
$$

Since

$$
A_{vw}^{\mathsf T}
=
U_v^{\mathsf T}\overline{U_w},
$$

we have

$$
X_{vw}(T)
=
TU_v^{\mathsf T}\overline{U_w}T^*.
$$

Now

$$
\begin{aligned}
\langle\langle z_{b,w}(T)|z_{a,v}(T)\rangle\rangle
&=
\operatorname{Tr}
\left[
(U_bTU_w^{\mathsf T})^*
(U_aTU_v^{\mathsf T})
\right]\\
&=
\operatorname{Tr}
\left[
\overline{U_w}T^*U_b^*U_aTU_v^{\mathsf T}
\right]\\
&=
\operatorname{Tr}
\left[
TU_v^{\mathsf T}\overline{U_w}T^*
U_b^*U_a
\right]\\
&=
\operatorname{Tr}
\left[
X_{vw}(T)U_b^*U_a
\right]\\
&=
m\,C(X_{vw}(T))_{a,b}.
\end{aligned}
\tag{1.8}
$$

Therefore

$$
\begin{aligned}
\operatorname{Tr}(F_{T,v}F_{T,w})
&=
\sum_{a,b}
\left|
\langle\langle z_{b,w}|z_{a,v}\rangle\rangle
\right|^2\\
&=
m^2\|C(X_{vw}(T))\|_2^2.
\end{aligned}
\tag{1.9}
$$

When \(v=w\),

$$
X_{vv}(T)=TT^*=\rho_T.
$$

All \(F_{T,v}\) are unitarily conjugate, so

$$
\boxed{
\operatorname{Tr}(F_T^2)=m^2d_T.
}
\tag{1.10}
$$

Summing (1.9) over all \(v,w\),

$$
\begin{aligned}
1+R_U(T)
&=
\frac{
\sum_{v,w}\|C(X_{vw}(T))\|_2^2
}{
m d_T
}\\
&=
\frac{
m^{-2}\operatorname{Tr}
\left[
\left(\sum_vF_{T,v}\right)^2
\right]
}{
m^{-1}\operatorname{Tr}(F_T^2)
}.
\end{aligned}
$$

Hence

$$
\boxed{
1+R_U(T)
=
\frac{
\operatorname{Tr}\left[
\left(\sum_vF_{T,v}\right)^2
\right]
}{
m\,\operatorname{Tr}(F_T^2)
}
=
m\,
\frac{\|\mathfrak R_U(F_T)\|_2^2}
     {\|F_T\|_2^2}.
}
\tag{FR}
$$

All transposes and normalizations in the proposed identity are correct.

---

# 2. Verification of the left-frame flatness

Define the synthesis map

$$
Z_T:\mathbb C^m\longrightarrow M_D,
\qquad
Z_Te_a=|U_aT\rangle\rangle.
$$

Then

$$
F_T=Z_TZ_T^*,
$$

while

$$
G_T=Z_T^*Z_T
$$

has entries

$$
G_T(a,b)
=
\langle U_aT,U_bT\rangle_{\rm HS}
=
\operatorname{Tr}(T^*U_a^*U_bT).
$$

Thus \(F_T\) and \(G_T\) have identical nonzero eigenvalues. In particular,

$$
\operatorname{Tr}(F_T^2)
=
\operatorname{Tr}(G_T^2)
=
\|G_T\|_2^2.
\tag{2.1}
$$

Every diagonal entry is

$$
G_T(a,a)=\operatorname{Tr}(T^*T)=1.
$$

Also,

$$
\operatorname{Tr}F_T
=
\sum_a\|U_aT\|_2^2
=
m.
\tag{2.2}
$$

Since

$$
\begin{aligned}
C(\rho_T)_{v,w}
&=
\frac1m
\operatorname{Tr}(TT^*U_w^*U_v)\\
&=
\frac1m
\operatorname{Tr}(T^*U_w^*U_vT)\\
&=
\frac1mG_T(w,v),
\end{aligned}
$$

we have

$$
C(\rho_T)=\frac1mG_T^{\mathsf T}.
$$

Therefore

$$
\boxed{
\operatorname{Tr}(F_T^2)
=
\|G_T\|_2^2
=
m^2d_T.
}
\tag{2.3}
$$

The one-copy assumption gives

$$
d_T\le p\le\frac Am,
$$

so

$$
\boxed{
\operatorname{Tr}(F_T^2)\le Am.
}
\tag{2.4}
$$

Removing the \(m\) diagonal terms of the Gram matrix yields

$$
\boxed{
\sum_{a\ne b}|G_T(a,b)|^2
=
\operatorname{Tr}(F_T^2)-m
\le m(A-1).
}
\tag{LF}
$$

Thus every equality and implication in \((LF)\) is correct.

---

# 3. Partial traces

From (1.3),

$$
\begin{aligned}
\operatorname{Tr}_A F_T
&=
\sum_a
(U_aT)(U_aT)^*\\
&=
\sum_aU_aTT^*U_a^*.
\end{aligned}
$$

Hence

$$
\boxed{
\operatorname{Tr}_A F_T
=
\sum_aU_a\rho_TU_a^*
=
mL(\rho_T).
}
\tag{3.1}
$$

From (1.4),

$$
\begin{aligned}
\operatorname{Tr}_B F_T
&=
\sum_a
\left[
(U_aT)^*(U_aT)
\right]^{\mathsf T}\\
&=
\sum_a(T^*T)^{\mathsf T}.
\end{aligned}
$$

Therefore

$$
\boxed{
\operatorname{Tr}_B F_T
=
m(T^*T)^{\mathsf T}.
}
\tag{3.2}
$$

Define

$$
\sigma_T:=(T^*T)^{\mathsf T}.
$$

Both \(\rho_T\) and \(\sigma_T\) are density matrices and have the same eigenvalues, but no complementary-spectrum assertion for a mixed \(\rho_T\) is being used.

Because \(\mathsf R_v=U_v\otimes I\) acts on subsystem \(A\),

$$
\operatorname{Tr}_A\mathfrak R_U(F_T)
=
\operatorname{Tr}_A F_T
=
mL(\rho_T),
\tag{3.3}
$$

whereas

$$
\begin{aligned}
\operatorname{Tr}_B\mathfrak R_U(F_T)
&=
\frac1m\sum_v
U_v
\left[m\sigma_T\right]
U_v^*\\
&=
mL(\sigma_T).
\end{aligned}
\tag{3.4}
$$

Thus the fully corrected partial-trace identities are

$$
\boxed{
\begin{aligned}
\operatorname{Tr}_A F_T&=mL(\rho_T),&
\operatorname{Tr}_B F_T&=m\sigma_T,\\
\operatorname{Tr}_A\mathfrak R_U(F_T)&=mL(\rho_T),&
\operatorname{Tr}_B\mathfrak R_U(F_T)&=mL(\sigma_T).
\end{aligned}
}
\tag{PT}
$$

The subsystem assignment in the prompt is correct: right multiplication by \(U_v^{\mathsf T}\) acts on \(A\).

---

# 4. Exact implication diagram

Let

$$
P_T
=
\left\|
(C\otimes C)
(|\psi_T\rangle\langle\psi_T|)
\right\|_2^2.
$$

The audited identity is

$$
\boxed{
P_T=\frac{d_T}{m}\bigl(1+R_U(T)\bigr).
}
\tag{4.1}
$$

Let

$$
p_2(C):=\sup_TP_T.
$$

Product inputs give

$$
p_2(C)\ge p^2.
\tag{4.2}
$$

Define:

$$
K:\quad \kappa_1(U)\le A-1,
$$

$$
M:\quad p_2(C)=p^2,
$$

$$
G:\quad p_2(C)\le\frac{A^2}{m^2}.
$$

## 4.1 Proven arrows

Under \(K\),

$$
P_T
\le
\frac{A}{m}d_T
\le
\frac{A}{m}p.
$$

Hence

$$
\boxed{
K\Longrightarrow
p_2(C)\le\frac{Ap}{m}
\le\frac{A^2}{m^2}.
}
\tag{4.3}
$$

Therefore

$$
\boxed{K\Longrightarrow G.}
$$

Under \(M\),

$$
p_2(C)=p^2\le\frac{A^2}{m^2},
$$

so

$$
\boxed{M\Longrightarrow G.}
$$

If the one-copy estimate is saturated,

$$
p=\frac Am,
$$

then (4.3) becomes

$$
p_2(C)\le p^2.
$$

Together with (4.2),

$$
\boxed{
p=\frac Am
\quad\Longrightarrow\quad
K\Longrightarrow M.
}
\tag{4.4}
$$

Likewise, if \(p=A/m\), then \(G\) implies

$$
p_2(C)\le\frac{A^2}{m^2}=p^2,
$$

and hence

$$
\boxed{
p=\frac Am
\quad\Longrightarrow\quad
G\Longleftrightarrow M.
}
\tag{4.5}
$$

## 4.2 Reverse arrows

The independently checked full-Weyl example from Round 2 establishes, within this channel class,

$$
\boxed{M\nRightarrow K}
$$

and

$$
\boxed{G\nRightarrow K.}
$$

That example is not used anywhere in the present low-\(A\) analysis.

For \(p<A/m\), the estimate supplied by \(K\),

$$
p_2(C)\le\frac{Ap}{m},
$$

is strictly weaker than \(p_2(C)\le p^2\). This calculation alone is not a counterexample. Therefore:

$$
\boxed{
K\Longrightarrow M
\text{ for }p<A/m
\text{ is not established here,}
}
$$

and no converse non-implication is claimed.

Similarly, no actual channel is supplied here proving \(G\nRightarrow M\) in the strict-slack case \(p<A/m\).

The rigorous diagram is therefore

$$
\begin{array}{ccccc}
K&\longrightarrow&G&\longleftarrow&M,\\[1mm]
&&\nwarrow&&
\end{array}
$$

with \(M\nRightarrow K\) and \(G\nRightarrow K\), while \(K\to M\) is valid under the additional equality \(p=A/m\) and otherwise remains undecided.

---

# 5. Exact isolation of the uncontrolled same-tuple correlation

Let

$$
|\psi_T\rangle
=
\sum_i|i\rangle\otimes T|i\rangle,
\qquad
\Psi_T=|\psi_T\rangle\langle\psi_T|.
$$

From (1.1),

$$
F_T
=
\sum_a
(I\otimes U_a)\Psi_T(I\otimes U_a^*)
=
m(\operatorname{id}\otimes L)(\Psi_T).
\tag{5.1}
$$

Since \(\mathfrak R_U\) applies \(L\) on subsystem \(A\),

$$
\boxed{
\mathfrak R_U(F_T)
=
m(L\otimes L)(\Psi_T).
}
\tag{5.2}
$$

Consequently,

$$
d_T
=
\frac{\|F_T\|_2^2}{m^2}
=
\|(\operatorname{id}\otimes L)(\Psi_T)\|_2^2,
\tag{5.3}
$$

and \((FR)\) becomes

$$
\boxed{
1+R_U(T)
=
m\,
\frac{\|(L\otimes L)(\Psi_T)\|_2^2}
     {\|(\operatorname{id}\otimes L)(\Psi_T)\|_2^2}.
}
\tag{5.4}
$$

Thus the ratio condition is exactly

$$
\boxed{
m\|(L\otimes L)(\Psi_T)\|_2^2
\le
A\,d_T
\qquad
\text{for every }T.
}
\tag{5.5}
$$

## 5.1 Centered orthogonal decomposition

Write

$$
L=\Delta_D+Q,
\qquad
\Delta_D(X)=\operatorname{Tr}(X)\frac{I_D}{D}.
$$

Then

$$
Q(I_D)=0,
\qquad
\operatorname{Tr}Q(X)=0.
$$

The two marginals of \(\Psi_T\) are

$$
\operatorname{Tr}_B\Psi_T=\sigma_T,
\qquad
\operatorname{Tr}_A\Psi_T=\rho_T.
$$

First,

$$
(\operatorname{id}\otimes L)(\Psi_T)
=
\sigma_T\otimes\frac{I_D}{D}
+
(\operatorname{id}\otimes Q)(\Psi_T).
$$

The two terms are Hilbert–Schmidt orthogonal, because the second has zero partial trace over \(B\). Hence

$$
\boxed{
d_T
=
\frac{\operatorname{Tr}(\sigma_T^2)}{D}
+
\left\|
(\operatorname{id}\otimes Q)(\Psi_T)
\right\|_2^2.
}
\tag{5.6}
$$

For the two-sided output,

$$
\begin{aligned}
(L\otimes L)(\Psi_T)
={}&
\frac{I_D\otimes I_D}{D^2}\\
&+
Q(\sigma_T)\otimes\frac{I_D}{D}\\
&+
\frac{I_D}{D}\otimes Q(\rho_T)\\
&+
(Q\otimes Q)(\Psi_T).
\end{aligned}
\tag{5.7}
$$

All four terms are pairwise Hilbert–Schmidt orthogonal. Therefore

$$
\boxed{
\begin{aligned}
\|(L\otimes L)(\Psi_T)\|_2^2
={}&
\frac1{D^2}
+
\frac{\|Q(\sigma_T)\|_2^2}{D}\\
&+
\frac{\|Q(\rho_T)\|_2^2}{D}
+
\Gamma_U(T),
\end{aligned}
}
\tag{5.8}
$$

where

$$
\boxed{
\Gamma_U(T)
=
\|(Q\otimes Q)(\Psi_T)\|_2^2.
}
\tag{5.9}
$$

Substitution into (5.5) gives the exact condition

$$
\boxed{
\begin{aligned}
m\Gamma_U(T)
\le{}&
A d_T-\frac{m}{D^2}\\
&-\frac{m}{D}
\left(
\|Q(\sigma_T)\|_2^2+
\|Q(\rho_T)\|_2^2
\right)
\end{aligned}
}
\tag{DC}
$$

for every Hilbert–Schmidt unit \(T\).

This is the first exact uncontrolled inequality.

The data \((LF)\) determine \(d_T\) and bound it by \(A/m\). The partial traces determine \(L(\rho_T)\) and \(L(\sigma_T)\), hence also \(Q(\rho_T)\) and \(Q(\sigma_T)\). They do not provide a pointwise upper bound for the double-centered term \(\Gamma_U(T)\).

The coupled physical form of \(F_T\) may impose such a bound, but proving or refuting precisely that implication is the remaining finite gate.

---

# 6. New full-Schmidt-rank obstruction

The following lemma goes beyond rank-one inputs, a single Bell input, and the universal \(m-1\) estimate.

## Lemma 6.1

For every finite deterministic tuple \(U\), define

$$
\alpha_U
=
\|C(I_D)\|_2^2
=
\frac1{m^2}
\sum_{v,w}
\left|
\operatorname{Tr}(U_w^*U_v)
\right|^2.
\tag{6.1}
$$

Then there exists a full-rank \(T\in M_D\), \(\|T\|_2=1\), such that

$$
R_U(T)
\ge
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}
-1.
$$

Consequently,

$$
\boxed{
\kappa_1(U)
\ge
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}
-1.
}
\tag{6.2}
$$

### Proof

Let \(|\psi_T\rangle\) be Haar-uniform on the unit sphere of
\(\mathbb C^D\otimes\mathbb C^D\). Under vectorization this is Haar-uniform \(T\) on the Hilbert–Schmidt unit sphere. Such a \(T\) has rank \(D\) almost surely.

For an \(n\)-dimensional Haar-random pure state \(\Psi\),

$$
\mathbb E[\Psi^{\otimes2}]
=
\frac{I+F}{n(n+1)},
\tag{6.3}
$$

where \(F\) is the swap. This follows from unitary invariance: the expectation lies in the span of \(I,F\), and its trace and swap trace are both one.

For a completely positive map \(\Phi:M_n\to M_k\), the swap identity gives

$$
\boxed{
\mathbb E_\Psi
\operatorname{Tr}[\Phi(\Psi)^2]
=
\frac{
\operatorname{Tr}[\Phi(I_n)^2]
+
\|J_\Phi\|_2^2
}{
n(n+1)
}.
}
\tag{6.4}
$$

Indeed,

$$
\operatorname{Tr}[X^2]
=
\operatorname{Tr}[(X\otimes X)F_k],
$$

the \(I\)-term in (6.3) gives \(\operatorname{Tr}\Phi(I)^2\), and the \(F_n\)-term gives

$$
\sum_{i,j}
\operatorname{Tr}
\left[
\Phi(E_{ij})\Phi(E_{ji})
\right]
=
\|J_\Phi\|_2^2.
$$

For the present \(C\),

$$
\begin{aligned}
\|J_C\|_2^2
&=
\sum_{i,j}\|C(E_{ij})\|_2^2\\
&=
\frac1{m^2}
\sum_{v,w}\sum_{i,j}
\left|
(U_w^*U_v)_{j,i}
\right|^2\\
&=
\frac1{m^2}\sum_{v,w}D\\
&=
D.
\end{aligned}
\tag{6.5}
$$

Let

$$
P_T
=
\|(C\otimes C)(\Psi_T)\|_2^2.
$$

Applying (6.4) to \(\Phi=C\otimes C\), whose input dimension is \(D^2\), gives

$$
\boxed{
\mathbb E P_T
=
\frac{\alpha_U^2+D^2}
     {D^2(D^2+1)}.
}
\tag{6.6}
$$

Here

$$
\|(C\otimes C)(I_{D^2})\|_2^2
=
\alpha_U^2,
$$

and

$$
\|J_{C\otimes C}\|_2^2
=
\|J_C\|_2^4
=
D^2.
$$

Now let

$$
\rho_T=\operatorname{Tr}_A\Psi_T.
$$

Tracing (6.3) over the two \(A\)-systems gives

$$
\mathbb E[\rho_T^{\otimes2}]
=
\frac{D I+F}{D(D^2+1)}.
\tag{6.7}
$$

Therefore

$$
\begin{aligned}
\mathbb E d_T
&=
\mathbb E\operatorname{Tr}[C(\rho_T)^2]\\
&=
\frac{D\alpha_U+\|J_C\|_2^2}
       {D(D^2+1)}\\
&=
\boxed{
\frac{\alpha_U+1}{D^2+1}.
}
\end{aligned}
\tag{6.8}
$$

Let

$$
N_T=
\sum_{v\ne w}
\|C(X_{vw}(T))\|_2^2.
$$

From \((OB)\),

$$
N_T=m^2P_T-md_T.
$$

Hence

$$
\begin{aligned}
\frac{\mathbb E N_T}
     {\mathbb E[m d_T]}
&=
m\frac{\mathbb E P_T}{\mathbb E d_T}-1\\
&=
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}
-1.
\end{aligned}
\tag{6.9}
$$

Because \(m d_T>0\),

$$
N_T\le \kappa_1(U)\,m d_T
$$

pointwise. Taking expectations proves (6.2).

Moreover, the rank-deficient matrices form a Haar-null algebraic set. Thus the weighted average in (6.9) is attained or exceeded by at least one full-rank \(T\). ∎

This is not a probabilistic construction of \(U\). Haar averaging is only an exact device for selecting a deterministic entangled input for each already frozen tuple.

---

# 7. Consequences for any putative low-\(A\) solution

Since

$$
\frac{C(I_D)}{D}
=
C\left(\frac{I_D}{D}\right)
$$

is a density matrix on \(\mathbb C^m\),

$$
\frac{\alpha_U}{D^2}
=
\left\|
C\left(\frac{I_D}{D}\right)
\right\|_2^2
\ge\frac1m.
$$

The one-copy hypothesis gives the upper bound

$$
\frac{\alpha_U}{D^2}\le\frac Am.
$$

Thus

$$
\boxed{
\frac{D^2}{m}
\le
\alpha_U
\le
\frac{AD^2}{m}.
}
\tag{7.1}
$$

If \(\kappa_1(U)\le A-1\), Lemma 6.1 requires

$$
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}
\le A.
$$

Equivalently,

$$
\boxed{
m\alpha_U^2
-
AD^2\alpha_U
+
D^2(m-A)
\le0.
}
\tag{HC}
$$

This is a new necessary scalar condition.

## 7.1 Strict maximally mixed slack

At the one-copy upper endpoint

$$
\alpha_U=\frac{AD^2}{m},
$$

the left side of \((HC)\) equals

$$
D^2(m-A)>0.
$$

Here \(m>A\) follows from the low-\(A\) condition and \(m>1\). Therefore:

$$
\boxed{
\left\|
C\left(\frac{I_D}{D}\right)
\right\|_2^2
=
\frac Am
\quad\Longrightarrow\quad
\kappa_1(U)>A-1.
}
\tag{7.2}
$$

So a solution of \((E1_{\rm gap})\) cannot merely satisfy the one-copy inequality at the maximally mixed input with equality. It requires a quantitatively strict slack.

The roots of the quadratic in \((HC)\) are

$$
\boxed{
\alpha_\pm
=
\frac{
AD^2
\pm
D\sqrt{A^2D^2-4m(m-A)}
}{
2m}.
}
\tag{7.3}
$$

Thus a necessary condition is

$$
A^2D^2\ge4m(m-A),
\tag{7.4}
$$

and

$$
\boxed{
\alpha_-\le\alpha_U\le\alpha_+.
}
\tag{7.5}
$$

Moreover,

$$
\alpha_+
<
\frac{AD^2}{m},
$$

with exact gap

$$
\boxed{
\frac{AD^2}{m}-\alpha_+
=
\frac{
2D(m-A)
}{
AD+\sqrt{A^2D^2-4m(m-A)}
}.
}
\tag{7.6}
$$

This obstruction is genuinely entangled: its witness can be chosen full Schmidt rank. It is not a reformulation of the product lower bound

$$
\kappa_1(U)\ge mp-1.
$$

The obstruction still does not disprove \((E1_{\rm gap})\). For sufficiently large finite \(D\), the scalar interval (7.1) can intersect the quadratic interval (7.5). The remaining pointwise double-centered condition \((DC)\) is not settled by this average argument.

---

# 8. Why the proof stops

A proof of \((E1_{\rm gap})\) would require one finite tuple for which

$$
\Gamma_U(T)
\le
\frac{A}{m}d_T
-
\frac1{D^2}
-
\frac{
\|Q(\sigma_T)\|_2^2+
\|Q(\rho_T)\|_2^2
}{D}
\tag{8.1}
$$

holds for every Hilbert–Schmidt unit \(T\).

A disproof would require showing that every tuple satisfying

$$
p\le\frac Am
$$

and the low-\(A\) scalar constraints admits some physical \(T\) violating (8.1).

Neither conclusion follows from:

$$
\operatorname{Tr}(F_T^2)\le Am,
$$

the two partial traces,

$$
\operatorname{Tr}_A\mathfrak R_U(F_T)=mL(\rho_T),
\qquad
\operatorname{Tr}_B\mathfrak R_U(F_T)=mL(\sigma_T),
$$

or the new averaged obstruction \((HC)\).

The exact remaining correlation is the double-traceless component

$$
(Q\otimes Q)(\Psi_T),
$$

where both copies of \(Q\) are formed from the same frozen tuple \(U\).

---

# Audit ledger

| Status                                                        | Statement                                                                                           |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **PROVED**                                                    | The frame identity \((FR)\), including all transposes and normalizations.                           |
| **PROVED**                                                    | \(\operatorname{Tr}F_T=m\), \(\operatorname{Tr}F_T^2=m^2d_T\), and the off-diagonal bound \((LF)\). |
| **PROVED**                                                    | The partial traces \((PT)\), with right multiplication acting on subsystem \(A\).                   |
| **PROVED**                                                    | \(K\Rightarrow G\) and \(M\Rightarrow G\).                                                          |
| **PROVED**                                                    | If \(p=A/m\), then \(K\Rightarrow M\) and \(G\Leftrightarrow M\).                                   |
| **DISPROVED, from the independently checked Round 2 example** | \(M\Rightarrow K\) and \(G\Rightarrow K\).                                                          |
| **PROVED**                                                    | Exact centered reduction \((DC)\); all uncontrolled dependence is isolated in \(\Gamma_U(T)\).      |
| **PROVED**                                                    | Full-Schmidt-rank averaged lower bound \((\mathrm{Haar\text{-}LB})\).                               |
| **PROVED**                                                    | Necessary quadratic constraint \((HC)\) and strict maximally mixed slack (7.2)–(7.6).               |
| **OPEN**                                                      | The existential statement \((E1_{\rm gap})\).                                                       |
| **OPEN**                                                      | Uniform pointwise control of \(\Gamma_U(T)\) over every physical \(T\).                             |
| **OPEN**                                                      | Whether \(K\Rightarrow M\) when \(p<A/m\) in this channel class.                                    |
| **CONJECTURED**                                               | None promoted.                                                                                      |

The first new proved statement requiring independent verification is the full-rank bound

$$
\kappa_1(U)\ge
\frac{m(\alpha_U^2+D^2)}
     {D^2(\alpha_U+1)}-1.
$$

The first unresolved statement is the uniform double-centered inequality \((8.1)\).
