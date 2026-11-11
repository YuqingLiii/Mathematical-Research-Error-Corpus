# Verdict

$$
\boxed{\texttt{GenericTheta300179Exclusion is PROVED within the present finite-slope audit context.}}
$$

For

$$
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300179)m_6,
$$

with the fifth centered pair \(\{\pm m_r\}\) arbitrary and all twelve slopes distinct, the exact determinant-specific size-two census forces

$$
\boxed{
\Delta_{\rm flat}>1074E.
}
$$

Consequently,

$$
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}\ge1074E,
$$

and therefore

$$
M_{\rm ord}\le (K-1-1074)E=970330473E.
$$

This contradicts the inherited strict target estimate

$$
\sqrt{D+1}|T_1|>970330473E.
$$

Thus no exact baseline exists in this finite-slope ansatz.

The inherited Laurent framework and slack decomposition are the same ones isolated in the uploaded source, where the earlier \(18E\) version remained open.  The exact determinant/Laurent coefficient conventions used here are those recorded in the source. 

This is **not** PW10. The source explicitly distinguishes finite-slope ansatz exclusions from a phase-uniform PW10 theorem.    

---

# 1. Exact first-gap setup

Set

$$
H:=1074,
\qquad
K:=970331548.
$$

The formal-support table is

$$
\boxed{
\begin{aligned}
(S_i)_{i=0}^{12}
={}&(
53624480,67257904,74299020,80378492,82204810,85479020,\\
&83844096,85479020,82204810,80378492,74299020,67257904,53624480).
\end{aligned}}
$$

Its sum is

$$
\sum_iS_i=K.
$$

At a safe spacing,

$$
C_{ii}(0)=e_i^2,\qquad C_{ii}(2)=0,
$$

and the exact slack identity is

$$
(K-1)E-M_{\rm ord}
=
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}.
\tag{1.1}
$$

The supplied source records the same telescoping identity in the earlier \(K=970330492\) case. 

Assume, toward contradiction,

$$
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}<HE.
\tag{1.2}
$$

Because every slack is nonnegative,

$$
\Delta_{\rm ray}<HE,\qquad
\Delta_{\rm flat}<HE.
\tag{1.3}
$$

Put

$$
w_i=\sqrt{S_i},\qquad
\alpha=\frac{w\cdot e}{K},\qquad
s=\sqrt{\frac EK}.
$$

Then

$$
\|e-\alpha w\|_2^2
=\frac{\Delta_{\rm ray}}K
<Hs^2,
\tag{1.4}
$$

and

$$
\alpha^2>
\left(1-\frac HK\right)s^2.
\tag{1.5}
$$

---

# 2. New exact support-loss budgets

From (1.4)–(1.5),

$$
\frac{|e_i-\alpha\sqrt{S_i}|}
{\alpha\sqrt{S_i}}
<
\sqrt{\frac{HK}{(K-H)S_i}}.
$$

The proposed uniform \(1/200\) enclosure is valid because

$$
\boxed{
(K-H)S_{\min}-H\cdot200^2K
=
10348023794323520>0,
}
$$

where

$$
S_{\min}=53624480.
$$

Hence

$$
\boxed{
e_i>\frac{199}{200}\alpha\sqrt{S_i}
\qquad\forall i.
}
\tag{2.1}
$$

Let

$$
n_i=|\operatorname{supp}A_i|,
\qquad
m_i=S_i-n_i.
$$

Since

$$
D_i:=S_ie_i^2-L_i^2\ge m_ie_i^2
$$

and

$$
D_i\le\Delta_{\rm flat}<HE,
$$

equation (2.1) gives

$$
m_i<
\frac{H\,200^2K^2}
{199^2(K-H)S_i}.
$$

Therefore the exact integer ceilings are

$$
\boxed{
\begin{aligned}
(m_i)=(&19629,15650,14167,13096,12805,12314,12554,\\
       &12314,12805,13096,14167,15650,19629).
\end{aligned}}
\tag{2.2}
$$

Equivalently,

$$
m_i\le
\left\lfloor
\frac{H\,200^2K^2-1}
{199^2(K-H)S_i}
\right\rfloor.
$$

The corresponding bad-coordinate budgets

$$
B_i:=2m_i
$$

are

$$
\boxed{
\begin{aligned}
(B_i)=(&39258,31300,28334,26192,25610,24628,25108,\\
       &24628,25610,26192,28334,31300,39258).
\end{aligned}}
\tag{2.3}
$$

Indeed, if \(z_i\) formal coefficients vanish and actual-frequency collision groups have sizes \(r_{i,j}\ge2\), then

$$
m_i\ge z_i+\sum_j(r_{i,j}-1),
$$

while the number of formal coordinates affected is at most

$$
z_i+\sum_jr_{i,j}
\le2m_i=B_i.
\tag{2.4}
$$

---

# 3. Complete new low-fiber census

The \(300179\) run was regenerated from scratch using the special-column order

$$
(3,1,20,-20,490,-490,12090,-12090,300179,-300179).
$$

No Round‑54 size-two count was reused.

## 3.1 Raw-fiber histogram

| \(i\) |    \(S_i\) | raw size 1 \(U_i\) | raw size 2 | raw size 3 | raw size 4 | maximum |
| ----: | ---------: | -----------------: | ---------: | ---------: | ---------: | ------: |
|     0 | 53,624,480 |          2,611,200 |  8,170,368 |  2,127,360 |  8,437,248 |     480 |
|     1 | 67,257,904 |          5,487,296 | 13,221,080 |  3,505,232 | 11,517,728 |     240 |
|     2 | 74,299,020 |          6,766,012 | 15,472,264 |  4,554,384 | 12,835,624 |     360 |
|     3 | 80,378,492 |          7,099,514 | 17,577,832 |  4,984,594 | 14,926,928 |     360 |
|     4 | 82,204,810 |          7,595,714 | 19,216,316 |  5,436,030 | 15,308,304 |     360 |
|     5 | 85,479,020 |          8,124,302 | 20,091,844 |  5,747,358 | 16,651,026 |     360 |
|     6 | 83,844,096 |          7,618,408 | 18,913,468 |  6,162,308 | 15,684,232 |     360 |
|     7 | 85,479,020 |          8,124,302 | 20,091,844 |  5,747,358 | 16,651,026 |     360 |
|     8 | 82,204,810 |          7,595,714 | 19,216,316 |  5,436,030 | 15,308,304 |     360 |
|     9 | 80,378,492 |          7,099,514 | 17,577,832 |  4,984,594 | 14,926,928 |     360 |
|    10 | 74,299,020 |          6,766,012 | 15,472,264 |  4,554,384 | 12,835,624 |     360 |
|    11 | 67,257,904 |          5,487,296 | 13,221,080 |  3,505,232 | 11,517,728 |     240 |
|    12 | 53,624,480 |          2,611,200 |  8,170,368 |  2,127,360 |  8,437,248 |     480 |

Globally,

$$
\boxed{
\begin{aligned}
\#\{\text{raw size 1}\}&=82986484,\\
\#\{\text{raw size 2}\}&=206412876.
\end{aligned}}
\tag{3.1}
$$

Every raw size-two fiber is a genuine binomial:

$$
\boxed{
\begin{aligned}
\#\{\text{genuine binomials}\}&=206412876,\\
\#\{\text{collected }\pm2\text{ monomials}\}&=0,\\
\#\{\text{collected zero polynomials}\}&=0.
\end{aligned}}
\tag{3.2}
$$

The exponent-difference ranges are

$$
\boxed{
0\le\Delta Q_6\le22475252,\qquad
-72\le\Delta Q_r\le72.
}
\tag{3.3}
$$

---

## 3.2 Signed-difference matching census

For each deleted row and signed exponent-difference key, write

$$
n_i^\sigma(d_6,d_r)
=
\#\{\text{size-two records with key }(d_6,d_r)
\text{ and sign }\sigma\}.
$$

Define

$$
M_i
=
\sum_{d_6,d_r}
\min\{n_i^+(d_6,d_r),n_i^-(d_6,d_r)\}.
\tag{3.4}
$$

The complete census is:

| \(i\) | distinct exponent differences | \(\sigma=+1\) | \(\sigma=-1\) | \(M_i\) | \(B_i\) | \(G_i:=U_i-B_i\) | \(N_i:=\max(0,M_i-B_i)\) |
| ----: | ----------------------------: | ------------: | ------------: | ------: | ------: | ---------------: | -----------------------: |
|     0 |                       357,170 |     6,701,184 |     1,469,184 |   9,020 |  39,258 |        2,571,942 |                        0 |
|     1 |                       922,377 |    10,841,064 |     2,380,016 |  39,298 |  31,300 |        5,455,996 |                    7,998 |
|     2 |                     1,366,982 |    12,879,268 |     2,592,996 |  56,382 |  28,334 |        6,737,678 |                   28,048 |
|     3 |                     1,772,341 |    14,743,906 |     2,833,926 |  58,032 |  26,192 |        7,073,322 |                   31,840 |
|     4 |                     2,141,504 |    15,760,752 |     3,455,564 |  37,358 |  25,610 |        7,570,104 |                   11,748 |
|     5 |                     1,975,040 |    16,961,220 |     3,130,624 |  68,998 |  24,628 |        8,099,674 |                   44,370 |
|     6 |                     1,075,004 |    15,828,996 |     3,084,472 |  65,744 |  25,108 |        7,593,300 |                   40,636 |
|     7 |                     1,975,040 |    16,961,220 |     3,130,624 |  68,998 |  24,628 |        8,099,674 |                   44,370 |
|     8 |                     2,141,504 |    15,760,752 |     3,455,564 |  37,358 |  25,610 |        7,570,104 |                   11,748 |
|     9 |                     1,772,341 |    14,743,906 |     2,833,926 |  58,032 |  26,192 |        7,073,322 |                   31,840 |
|    10 |                     1,366,982 |    12,879,268 |     2,592,996 |  56,382 |  28,334 |        6,737,678 |                   28,048 |
|    11 |                       922,377 |    10,841,064 |     2,380,016 |  39,298 |  31,300 |        5,455,996 |                    7,998 |
|    12 |                       357,170 |     6,701,184 |     1,469,184 |   9,020 |  39,258 |        2,571,942 |                        0 |

Totals:

$$
\boxed{
\begin{aligned}
\sum_iM_i&=603920,\\
\sum_iB_i&=375752,\\
\sum_iG_i&=82610732,\\
\sum_iN_i&=288644.
\end{aligned}}
\tag{3.5}
$$

Because singleton fibers and raw size-two fibers are disjoint formal-coordinate classes, the same bad set may be charged conservatively against both populations without double counting in the variance lower bound.

---

# 4. Collision-robust surviving anchors and pairs

At most \(B_i\) formal coordinates in cofactor \(i\) are bad.

Therefore:

* at least

  $$
  G_i=U_i-B_i
  $$

  singleton monomials remain physically isolated, nonzero, and of modulus exactly \(1\);
* from a fixed disjoint pairing of the \(M_i\) opposite-sign records, at most \(B_i\) pairs are destroyed.

Thus at least

$$
N_i=\max(0,M_i-B_i)
$$

complete opposite-sign pairs survive.

For one surviving matched pair, the two Laurent coefficients have a common leading monomial and opposite relative signs:

$$
1+\zeta,\qquad1-\zeta,
\qquad |\zeta|=1.
$$

If \(1-\zeta=0\), that formal coordinate is a zero and belongs to the charged bad set. A surviving complete pair is therefore physically nonzero and isolated.

Its two magnitudes satisfy

$$
\boxed{
r_+^2+r_-^2=4,
\qquad
r_++r_-\le2\sqrt2.
}
\tag{4.1}
$$

No continuous-phase relaxation is used; \(\zeta\) is the actual \(D\)-th root

$$
\zeta=\omega^{a\Delta Q_6+b\Delta Q_r}.
$$

---

# 5. New exact scale bound

The anchored-variance comparison requires an upper bound on \(E/K\). This must be recomputed because \(H=1074\).

Let

$$
\bar a_0=\frac{L_0}{S_0},
\qquad
s=\sqrt{\frac EK}.
$$

Using row \(i=0\),

$$
|1-s|
\le
|1-\bar a_0|
+
\left|\bar a_0-\frac{e_0}{\sqrt{S_0}}\right|
+
\left|\frac{e_0}{\sqrt{S_0}}-\alpha\right|
+
|s-\alpha|.
\tag{5.1}
$$

The four terms satisfy

$$
|1-\bar a_0|
<
s\sqrt{\frac{HK}{S_0G_0}},
$$

$$
\left|\bar a_0-\frac{e_0}{\sqrt{S_0}}\right|
<
s\,\frac{\sqrt{HK}}{S_0},
$$

$$
\left|\frac{e_0}{\sqrt{S_0}}-\alpha\right|
<
s\sqrt{\frac H{S_0}},
$$

and

$$
0\le s-\alpha
<
s\left(1-\sqrt{1-\frac HK}\right).
$$

The following rational enclosures are proved by exact integer arithmetic:

$$
\sqrt{\frac{HK}{S_0G_0}}<\frac{87}{1000},
$$

because

$$
7569S_0G_0-10^6HK
=
1773224610671040>0;
$$

$$
\frac{\sqrt{HK}}{S_0}<\frac{191}{10000},
$$

because

$$
191^2S_0^2-10^8HK
=
690602849919462400>0;
$$

$$
\sqrt{\frac H{S_0}}<\frac9{2000},
$$

because

$$
81S_0-4\cdot10^6H
=
47582880>0;
$$

and

$$
1-\sqrt{1-\frac HK}
<
\frac{H}{2K-H}
<
\frac3{5000000},
$$

because

$$
3(2K-H)-5\cdot10^6H
=
451986066>0.
$$

Their sum is

$$
\frac{553003}{5000000},
$$

and

$$
\frac19-\frac{553003}{5000000}
=
\frac{22973}{45000000}>0.
$$

Consequently,

$$
|1-s|<\frac{s}{9},
$$

and hence

$$
\boxed{
s<\frac98,
\qquad
E<K\left(\frac98\right)^2.
}
\tag{5.2}
$$

---

# 6. Anchored variance from the surviving pairs

For cofactor \(i\), pad the magnitude array with zeros to length \(S_i\), and let

$$
\bar a_i=\frac{L_i}{S_i}.
$$

Then

$$
\frac{D_i}{S_i}
=
\sum_{\xi=1}^{S_i}
\bigl(|A_i(\xi)|-\bar a_i\bigr)^2,
\qquad
D_i=S_ie_i^2-L_i^2.
\tag{6.1}
$$

Restrict this sum to:

* the \(G_i\) surviving unit anchors;
* the \(N_i\) surviving complete opposite-sign pairs.

For arbitrary \(\mu\in\mathbb R\),

$$
\frac{D_i}{S_i}
\ge
G_i(1-\mu)^2
+
\sum_{p=1}^{N_i}
\left[
(r_{p,+}-\mu)^2+(r_{p,-}-\mu)^2
\right].
\tag{6.2}
$$

Minimizing the right-hand side gives

$$
\min_\mu
=
G_i+4N_i
-
\frac{
\left(G_i+\sum_p(r_{p,+}+r_{p,-})\right)^2
}{
G_i+2N_i
}.
$$

Using (4.1),

$$
\min_\mu
\ge
(6-4\sqrt2)\,
\frac{G_iN_i}{G_i+2N_i}.
\tag{6.3}
$$

Now

$$
\sqrt2<\frac{17}{12},
$$

so

$$
6-4\sqrt2>\frac13.
$$

Also,

$$
G_i>2N_i
$$

for every row; the smallest value of \(G_i-2N_i\) is

$$
2571942>0.
$$

Therefore, whenever \(N_i>0\),

$$
\boxed{
\frac{D_i}{S_i}>\frac{N_i}{6}.
}
\tag{6.4}
$$

Rows \(0\) and \(12\) have \(N_i=0\) and simply contribute the valid lower bound \(D_i\ge0\).

Thus

$$
\Delta_{\rm flat}
\ge
\sum_iD_i
>
\frac16\sum_iS_iN_i.
\tag{6.5}
$$

The exact weighted count is

$$
\boxed{
\sum_iS_iN_i
=
23286218764480.
}
\tag{6.6}
$$

Hence

$$
\boxed{
\Delta_{\rm flat}
>
3881036460746+\frac23.
}
\tag{6.7}
$$

---

# 7. Exact final comparison

From (5.2),

$$
HE
<
HK\frac{81}{64}.
$$

Equation (6.5) beats that quantity because

$$
\boxed{
64\sum_iS_iN_i-486HK
=
983839864806448>0.
}
\tag{7.1}
$$

Equivalently,

$$
\frac16\sum_iS_iN_i
>
HK\frac{81}{64}
>
HE.
$$

Therefore

$$
\boxed{
\Delta_{\rm flat}>1074E.
}
\tag{7.2}
$$

This contradicts the assumption that the sum of all four nonnegative slacks is below \(1074E\).

Thus the exact physical inequality holds:

$$
\boxed{
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}
\ge1074E.
}
\tag{7.3}
$$

`EnergyRay1074` is neither needed nor claimed.

---

# 8. Consequence for the baseline

Using (1.1) and \(K=970331548\),

$$
\begin{aligned}
M_{\rm ord}
&\le
(K-1)E-1074E\\
&=
970330473E.
\end{aligned}
\tag{8.1}
$$

But the inherited target estimate is strict:

$$
\sqrt{D+1}|T_1|>970330473E.
\tag{8.2}
$$

This contradicts the physical baseline inequality

$$
\sqrt{D+1}|T_1|\le M_{\rm ord}.
$$

Hence:

$$
\boxed{
\begin{gathered}
\texttt{GenericTheta300179Exclusion:}\\
\delta=\pm2m_6,\quad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300179)m_6,\\
\text{the fifth centered pair arbitrary and all twelve slopes distinct}\\
\Longrightarrow
\text{no exact baseline exists.}
\end{gathered}}
\tag{8.3}
$$

This remains a finite-slope candidate theorem pending independent replication of the new \(300179\) low-fiber census.

---

# 9. Explicit structural examples

Use the special-column order

$$
(3,1,20,-20,490,-490,12090,-12090,300179,-300179).
$$

## 9.1 Type I: one arbitrary-pair placement

The matched difference key is

$$
(\Delta Q_6,\Delta Q_r)=(2820,0).
$$

A \(\sigma=+1\) record is

$$
i=0,\quad t=-2787752,\quad q=-11,\quad(x,y)=(1,12),
$$

with assignments

$$
(4,7,5,8,6,9,3,10,2,11),
$$

$$
(4,7,6,9,5,8,3,10,2,11),
$$

exponents

$$
Q_6=-36243866,\quad -36241046,
$$

and determinant signs \(-1,-1\).

A matched \(\sigma=-1\) record is

$$
i=0,\quad t=-1509589,\quad q=-9,\quad(x,y)=(2,11),
$$

with assignments

$$
(12,10,3,7,8,1,5,6,4,9),
$$

$$
(1,3,8,10,12,5,6,7,4,9),
$$

exponents

$$
Q_6=-19614023,\quad -19611203,
$$

and signs \(+1,-1\).

---

## 9.2 Type II: two arbitrary-pair placements

The matched key is

$$
(\Delta Q_6,\Delta Q_r)=(8824,-16).
$$

A \(\sigma=+1\) record is

$$
i=0,\quad t=-3363833,\quad q=-8,
$$

with

$$
(x,y)=(2,10),\quad
Q_r=-96,
$$

assignment

$$
(11,3,7,6,5,8,4,9,1,12),
$$

and

$$
(x,y)=(3,11),\quad
Q_r=-112,
$$

assignment

$$
(10,6,8,7,2,5,4,9,1,12).
$$

Both determinant signs are \(-1\).

A matched \(\sigma=-1\) record is

$$
i=0,\quad t=-2085048,\quad q=-4,
$$

with placements

$$
(x,y)=(4,8),\qquad(x,y)=(6,10),
$$

assignments

$$
(2,9,10,1,11,3,7,6,5,12),
$$

$$
(4,3,11,2,9,1,8,7,5,12),
$$

and determinant signs \(-1,+1\).

These are the two structural size-two types: the terms either share one arbitrary-pair placement, giving \(\Delta Q_r=0\), or use two placements, giving \(\Delta Q_r\ne0\).

---

# 10. Deterministic checksums and reproducer

The canonical stream record is 16 bytes:

```text
int32  t
int32  DeltaQ6
int16  DeltaQr
int8   q
int8   sigma
uint32 zero_padding
```

Ordering:

1. deleted row \(i=0,\ldots,12\);
2. \(q=-12,\ldots,-1,1,\ldots,12\);
3. increasing \(t\).

Exact stream digest:

```text
9188e2a05d8880a91e1a717b2f19619ff19f7482cff6791a4aaa4845d484ef9c
```

Exact aggregate-text digest:

```text
e6edb047e591b32127e9f9fea50cac41b661f0475feb266619a681b9090011d8
```

Integer checksums:

$$
\begin{aligned}
\#\text{records}&=206412876,\\
\sum t&=4953909024,\\
\sum\Delta Q_6&=751418613554112,\\
\sum\Delta Q_r&=3333280,\\
\sum\sigma&=136794692,\\
\sum t^2&=879344995479279201900,\\
\sum(\Delta Q_6)^2&=7182382339465020225280,\\
\sum(\Delta Q_r)^2&=79579910944.
\end{aligned}
$$

The index-weighted checksum is

$$
1319386502367145814134320,
$$

and the stream FNV-64 checksum is

```text
37120cd3e31b6e9f
```

## Reproducibility files

* [Raw-fiber histogram](sandbox:/mnt/data/round55_raw_fiber_histogram.csv)
* [Size-two matching summary](sandbox:/mnt/data/round55_size2_summary.csv)
* [Digest and checksums](sandbox:/mnt/data/round55_digest.txt)
* [Explicit matched-pair assignments](sandbox:/mnt/data/round55_pair_examples.txt)
* [Exact inequality checks](sandbox:/mnt/data/round55_exact_inequality_checks.txt)
* [Integer-only C++20 reproducer](sandbox:/mnt/data/round55_lowfiber_reproducer.cpp)
* [Budget and checksum postprocessor](sandbox:/mnt/data/round55_finalize.py)

---

# VERIFIED

* The new support table \(S_i\) and \(K=970331548\).
* The \(H=1074\) coordinatewise \(1/200\) energy enclosure.
* The exact support-loss ceilings \(m_i\).
* The bad-coordinate budgets \(B_i=2m_i\).
* The complete raw-fiber histogram.
* The exact total of \(206412876\) raw size-two fibers.
* Every raw size-two fiber is a genuine binomial.
* Zero collected \(\pm2\) monomials.
* Zero collected size-two Laurent cancellations.
* The sign totals and distinct exponent-difference counts.
* The opposite-sign matching counts \(M_i\).
* The deletion-robust counts \(G_i\) and \(N_i\).
* The exact scale bound \(E<K(9/8)^2\).
* The anchored-variance lower bound.
* The final exact comparison (7.1).
* `GenericTheta300179Exclusion` within this finite-slope ansatz.

# CORRECTED

* No Round‑54 singleton, size-two, matching, or deletion count was reused.
* Rows \(0\) and \(12\) have \(M_i<B_i\), so they contribute no deletion-robust matched pair:

  $$
  N_0=N_{12}=0.
  $$
* The correct total matched count is

  $$
  \sum_iM_i=603920.
  $$
* The correct deletion-robust count is

  $$
  \sum_iN_i=288644.
  $$
* The \(300179\) coefficient scale requires the new \(9/8\) bound; the earlier \(70/69\) estimate was not reused.

# DISPROVED

* The possibility that the complete new size-two anchored relaxation remains below \(1074E\).
* The need to add size-three or size-four fibers at \(\theta=300179\).
* The possibility of an admissible phase/deletion pattern violating the size-two certificate.
* The status “generic \(\theta=300179\) remains open” within this exact finite-slope ansatz.

# NECESSARY-ONLY

* Independent replication of the new \(300179\) low-fiber census is still required before broader promotion of the candidate ansatz theorem.
* The theorem does not cover arbitrary twelve-slope sets.
* It does not establish the physical lift or nonliftability of \(x^{(10)}\).
* It does not prove PW10.

# EQUIVALENT

Within the audited Wiener route,

$$
\Delta_{\rm ray}
+\Delta_{\rm flat}
+\Delta_{\rm Young}
+\Delta_{\rm group}
\ge1074E
$$

is equivalent to

$$
M_{\rm ord}\le970330473E.
$$

For a matched signed exponent-difference key, the two surviving binomials are exactly

$$
1+\zeta,\qquad1-\zeta.
$$

The candidate finite-slope exclusion is equivalent to the contradiction between (8.1) and (8.2).

# NUMERICAL-ONLY

* No floating-point phase search is used.
* No sampled phase plot is used.
* No interval branch-and-bound is needed.
* The exhaustive census is integer-only.
* The theorem uses exact counts and elementary rational/radical inequalities.

# CONJECTURED

* Independent replication of `GenericTheta300179Exclusion`.
* Extension of the low-fiber method to subsequent unresolved four-ratio values.
* A general thirteen-slope ansatz theorem.
* Physical liftability or nonliftability of \(x^{(10)}\).

# OPEN

* The full ratio-two and arbitrary one-defect classes.
* Non-centrally-symmetric twelve-slope families outside the candidate exclusions.
* A general thirteen-slope theorem.
* Dense nonquadratic baseline solutions.
* Existence of an exact baseline vector outside the excluded ansatz families.
* Frozen named-edge retrieval.
* Physical liftability of \(x^{(10)}\).
* An exact physical vector above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new claim requiring independent verification is the exact \(300179\) opposite-sign matching census

$$
\boxed{
(M_i)=
(9020,39298,56382,58032,37358,68998,65744,
68998,37358,58032,56382,39298,9020),
}
$$

together with its determinant-specific implication

$$
\boxed{\Delta_{\rm flat}>1074E.}
$$

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$
