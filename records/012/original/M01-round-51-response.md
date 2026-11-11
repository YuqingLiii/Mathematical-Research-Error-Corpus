# Verdict

The frozen normalization remains

$$
D=941541228773064677=970330474^2+1,\qquad
B^2=\frac1{D(D+2)},\qquad
A_{\rm sp}^2=(D+1)B^2,
$$

with the exact even, symplectic-Fourier \(+1\) baseline and PW10 target fixed as stated.  No exact baseline vector, frozen-edge vector, exclusion of \(x^{(10)}\), physical violator, or phase-uniform PW10 proof is produced here. 

The exact four-ratio recurrence is correct. Its complete formal-support frontier is

$$
\boxed{
K^{(4)}_\theta\le 970330474
\iff
1\le |\theta|\le 300176
\quad\text{or}\quad
|\theta|\in\mathcal X,
}
$$

where

$$
\boxed{
\begin{aligned}
\mathcal X=\{&
300178,300180,300182,300184,300186,300188,\\
&300190,300192,300195,300197,300199,300201,\\
&300203,300205,300220
\}.
\end{aligned}}
\tag{1}
$$

After excluding the universally repeated slopes, the admissible passing set is

$$
\boxed{
\mathcal T_*=
\Bigl(\{2,\ldots,300176\}\setminus\{3,20,490,12090\}\Bigr)
\cup\mathcal X.
}
\tag{2}
$$

Accordingly, within the present proof-development context:

$$
\boxed{
\begin{gathered}
\textbf{ExtendedEta12090FourthRatioExclusion:}\\
\delta=\pm2m_6,\quad
m_j=20m_6,\quad
m_\ell=490m_6,\quad
m_s=12090m_6,\quad
m_t=\theta m_6,\\
|\theta|\in\mathcal T_*,\quad
\text{all twelve slopes distinct}\\
\Longrightarrow
\text{the corresponding twelve-slope span contains no exact baseline.}
\end{gathered}}
\tag{EET4}
$$

The globally first admissible support failure is

$$
\boxed{|\theta|=300177},
$$

where

$$
K^{(4)}_{300177}=970330492,
$$

so after target removal the gap is only

$$
\boxed{
(970330492-1)-970330473=18.
}
\tag{3}
$$

The globally closest passing value is

$$
\boxed{|\theta|=300220},
$$

with

$$
K^{(4)}_{300220}=970330348
$$

and exact target-removed margin

$$
\boxed{
970330473-(970330348-1)=126.
}
\tag{4}
$$

The support stabilizes sharply at

$$
\boxed{|\theta|\ge300302},
$$

with stabilized value

$$
\boxed{K_\infty=970343224.}
\tag{5}
$$

The first-gap attack also gives a new fifth-ratio subclass theorem:

$$
\boxed{
\begin{gathered}
\textbf{Theta300177FifthRatioExclusion:}\\
\delta=\pm2m_6,\quad
m_j=20m_6,\quad
m_\ell=490m_6,\quad
m_s=12090m_6,\\
m_t=300177m_6,\quad
m_r=\rho m_6,\\
2\le|\rho|\le2797343,\quad
|\rho|\notin\{3,20,490,12090,300177\},\\
\text{all twelve slopes distinct}\\
\Longrightarrow
\text{no exact baseline.}
\end{gathered}}
\tag{T300177-5R}
$$

The generic \(\theta=300177\) case with an arbitrary final centered slope remains open.

---

# 1. Audit of the exact four-ratio recurrence

After deleting row \(i\), let

$$
R_i=\{0,1,\ldots,12\}\setminus\{i\}.
$$

Assign the six labeled ordered pairs as follows:

$$
(3m_6,m_6)\mapsto(u,v),
$$

$$
(+20m_6,-20m_6)\mapsto(a,b),
$$

$$
(+490m_6,-490m_6)\mapsto(c,d),
$$

$$
(+12090m_6,-12090m_6)\mapsto(e,f),
$$

$$
(+\theta m_6,-\theta m_6)\mapsto(g,h),
$$

and the remaining centered pair

$$
(+m_r,-m_r)\mapsto(x,y).
$$

All twelve assigned rows are pairwise distinct and exhaust \(R_i\).

Define

$$
T_0
=
3u+v+20(a-b)+490(c-d)+12090(e-f),
$$

$$
d_\theta=g-h,\qquad q=x-y.
$$

After removing the common determinant chirps and cofactor-wide Fourier translations, the parent frequency is an affine translate of

$$
-\frac h4\left[
m_6(T_0+\theta d_\theta)+m_rq
\right].
$$

Thus the exact formal support coordinate is

$$
\boxed{(T_0+\theta d_\theta,q).}
$$

For fixed \(i,q\), define

$$
\boxed{
\mathcal C^{(4)}_{i,q}
=
\left\{
(T_0,d_\theta):
\begin{array}{l}
u,v,a,b,c,d,e,f,g,h,x,y\text{ exhaust }R_i,\\
x-y=q
\end{array}
\right\}.
}
\tag{6}
$$

Then

$$
\boxed{
S_i^{(4)}(\theta)
=
\sum_{q\ne0}
\left|
\left\{
T_0+\theta d:
(T_0,d)\in\mathcal C^{(4)}_{i,q}
\right\}
\right|,
}
\tag{7}
$$

and

$$
\boxed{
K^{(4)}_\theta=\sum_{i=0}^{12}S_i^{(4)}(\theta).
}
\tag{8}
$$

There is no extra multiplicity factor in (7):

* every pair is already labeled by its slope coefficient;
* its orientation is encoded by its ordered endpoints;
* the Boolean set removes duplicate formal coordinates.

Any collision after inserting the final field ratio \(m_r/m_6\), and any determinant-phase cancellation, can only reduce the actual cofactor support.

Swapping \(g,h\) proves

$$
\boxed{K^{(4)}_{-\theta}=K^{(4)}_\theta.}
\tag{9}
$$

---

## 1.1 Reproducible integer recurrence

For each eight-element row set \(S\), precompute

$$
\boxed{
\mathcal T(S)=
\left\{
3u+v+20(a-b)+490(c-d)+12090(e-f):
(u,v,a,b,c,d,e,f)\text{ permutes }S
\right\}.
}
\tag{10}
$$

Then define

$$
\boxed{
\mathcal A_{i,q,d}
=
\bigcup_{\substack{
x,y,g,h\in R_i\ {\rm distinct}\\
x-y=q,\ g-h=d}}
\mathcal T\!\left(R_i\setminus\{x,y,g,h\}\right).
}
\tag{11}
$$

Equation (7) becomes

$$
\boxed{
S_i^{(4)}(\theta)
=
\sum_{q\ne0}
\left|
\bigcup_{d\ne0}
\bigl(\mathcal A_{i,q,d}+\theta d\bigr)
\right|.
}
\tag{12}
$$

Compact integer-only pseudocode is:

```text
for each 8-row mask S:
    T[S] = empty set
    for each ordered permutation (u,v,a,b,c,d,e,f) of S:
        T[S].add(3u+v+20(a-b)+490(c-d)+12090(e-f))

for deleted i:
    for q,d in {-12,...,-1,1,...,12}:
        A[i,q,d] = empty set

    for ordered distinct x,y,g,h in R_i:
        q = x-y
        d = g-h
        A[i,q,d] |= T[R_i \ {x,y,g,h}]

for theta:
    K[theta] = 0
    for i,q:
        U = union over d of {a+theta*d : a in A[i,q,d]}
        K[theta] += |U|
```

Only ordinary integer sets or bitsets are needed.

---

# 2. Audit of the supplied \(\theta=116983\) certificate

The exact per-cofactor table is

$$
\boxed{
\begin{aligned}
(S_i^{(4)}(116983))_{i=0}^{12}={}&(
38501902,45642450,49073650,51909066,\\
&52849566,54110020,53631882,54110020,\\
&52849566,51909066,49073650,45642450,38501902).
\end{aligned}}
\tag{13}
$$

Its checksum is

$$
\boxed{K^{(4)}_{116983}=637805190.}
\tag{14}
$$

At the preceding value,

$$
\boxed{K^{(4)}_{116982}=653612792.}
\tag{15}
$$

The exact target-removed margins are therefore

$$
970330473-(637805190-1)
=
\boxed{332525284},
\tag{16}
$$

and

$$
970330473-(653612792-1)
=
\boxed{316717682}.
\tag{17}
$$

Thus the rectangular failure at \(116983\) was not an exact-support failure.

The additional supplied anchors are also reproduced:

$$
\begin{array}{c|r}
|\theta|&K^{(4)}_\theta\\ \hline
150000&739935564\\
200000&855376712\\
250000&933982600\\
300000&970296048\\
300176&970322512\\
300177&970330492\\
300178&970321472\\
300220&970330348.
\end{array}
\tag{18}
$$

The nonmonotonicity is already visible at \(300177,300178\).

---

# 3. Exact collision reduction for the complete scan

The eight coefficient slots of \(T_0\) are

$$
3,1,20,-20,490,-490,12090,-12090.
$$

Rearrangement gives the global extrema

$$
\boxed{\min T_0=-150127,\qquad \max T_0=150175.}
\tag{19}
$$

Indeed,

$$
\begin{aligned}
150175={}&
-12090\cdot0-490\cdot1-20\cdot2\\
&+1\cdot8+3\cdot9+20\cdot10+490\cdot11+12090\cdot12,
\end{aligned}
$$

while

$$
\begin{aligned}
-150127={}&
12090\cdot0+490\cdot1+20\cdot2+3\cdot3+1\cdot4\\
&-20\cdot10-490\cdot11-12090\cdot12.
\end{aligned}
$$

Thus the largest possible difference between two \(T_0\)-values is

$$
\boxed{300302.}
\tag{20}
$$

The fully unfolded formal support is

$$
\boxed{
K_\infty
=
\sum_{i,q,d}|\mathcal A_{i,q,d}|
=
970343224.
}
\tag{21}
$$

Its per-cofactor table is

$$
\boxed{
\begin{aligned}
(&53624480,67257904,74299580,80379612,82206304,85480832,\\
&83845800,85480832,82206304,80379612,74299580,67257904,53624480).
\end{aligned}}
\tag{22}
$$

A baseline contradiction requires

$$
K^{(4)}_\theta-1\le970330473,
$$

equivalently

$$
K^{(4)}_\theta\le970330474.
$$

Relative to \(K_\infty\), the required collision deficit is therefore

$$
\boxed{
K_\infty-970330474=12750.
}
\tag{23}
$$

---

## 3.1 Two disjoint adjacent-band matchings

For adjacent \(d,d+1\), define

$$
I_{i,q,d}(\theta)
=
\left|
\mathcal A_{i,q,d}
\cap
\bigl(\mathcal A_{i,q,d+1}+\theta\bigr)
\right|.
\tag{24}
$$

This is precisely the overlap of the projected bands because

$$
a+\theta d=b+\theta(d+1)
\iff
a=b+\theta.
$$

Use the two disjoint matchings

$$
\begin{aligned}
\mathscr M_0={}&
\{(-12,-11),(-10,-9),\ldots,(-2,-1)\}\\
&\cup\{(1,2),(3,4),\ldots,(11,12)\},
\end{aligned}
$$

and

$$
\begin{aligned}
\mathscr M_1={}&
\{(-11,-10),(-9,-8),\ldots,(-3,-2)\}\\
&\cup\{(2,3),(4,5),\ldots,(10,11)\}.
\end{aligned}
$$

Put

$$
H_r(\theta)
=
\sum_{i,q}
\sum_{(d,d+1)\in\mathscr M_r}
I_{i,q,d}(\theta).
\tag{25}
$$

Within each \(\mathscr M_r\), no \(d\)-band occurs twice. At each projected value, the number of matched double occurrences is at most the total union deficit there. Hence

$$
\boxed{
K_\infty-K^{(4)}_\theta
\ge
\max\{H_0(\theta),H_1(\theta)\}.
}
\tag{26}
$$

The exact integer-bitset scan gives, for

$$
1\le\theta\le150151,
$$

$$
\boxed{
\min_\theta\max(H_0(\theta),H_1(\theta))
=
118074632,
}
\tag{27}
$$

attained at

$$
\theta=149647,
$$

where

$$
H_0=118074632,\qquad H_1=99754732.
$$

Since \(118074632\gg12750\), every \(\theta\le150151\) passes.

---

## 3.2 Exact formula above the half-width

For

$$
\theta\ge150152,
$$

one has

$$
2\theta>300302.
$$

Therefore bands with \(|d-d'|\ge2\) cannot overlap. In particular:

* the gap between \(d=-1\) and \(d=1\) cannot overlap;
* no projected value can lie in three \(d\)-bands.

Thus every collision is between adjacent \(d\)-bands and

$$
\boxed{
K^{(4)}_\theta
=
K_\infty-H_0(\theta)-H_1(\theta)
\qquad(\theta\ge150152).
}
\tag{28}
$$

This reduces the complete frontier to an exact scan of adjacent-set intersections.

---

## 3.3 Replication checksums

For the low-range collision certificate \(1\le\theta\le150151\):

$$
\begin{array}{c|r|r}
& H_0&H_1\\ \hline
\sum H_r&
31687862306776&
27020159369932\\
\sum \theta H_r&
2058618643449205948&
1754604114323772216\\
\sum \theta^2H_r&
189488938022181601177204&
161400866866551803426992.
\end{array}
\tag{29}
$$

For the exact critical scan

$$
150152\le\theta\le300301,
$$

which contains \(150150\) values:

$$
\boxed{
\sum K^{(4)}_\theta
=
131974409852556,
}
\tag{30}
$$

$$
\boxed{
\sum \theta K^{(4)}_\theta
=
30190751891579666896,
}
\tag{31}
$$

$$
\boxed{
\sum \theta^2K^{(4)}_\theta
=
7149371020340881916998112.
}
\tag{32}
$$

Within this critical scan, \(150040\) values pass and \(110\) fail.

Over the complete raw passing set there are

$$
\boxed{300191}
$$

positive values, with checksums

$$
\boxed{
\sum_{\theta\ {\rm passing}}\theta=45057468476,
}
$$

$$
\boxed{
\sum_{\theta\ {\rm passing}}\theta^2
=
9017246088045214.
}
\tag{33}
$$

---

# 4. Complete frontier

The raw passing set is

$$
\boxed{
\{1,2,\ldots,300176\}\cup\mathcal X,
}
\tag{34}
$$

with \(\mathcal X\) from (1).

The first failure is

$$
\theta=300177,
\qquad
K^{(4)}_\theta=970330492.
$$

The exact first-failure per-cofactor table is

$$
\boxed{
\begin{aligned}
(&53624480,67257904,74298872,80378258,82204740,85478914,\\
&83844156,85478914,82204740,80378258,74298872,67257904,53624480).
\end{aligned}}
\tag{35}
$$

The closest pass is

$$
\theta=300220,
\qquad
K^{(4)}_\theta=970330348.
$$

No value greater than \(300220\) passes.

After enforcing universal distinctness, the exact admissible set is \(\mathcal T_*\) in (2).

This proves `EET4` inside the frozen ansatz program. It remains a finite-slope ansatz exclusion and not a phase-uniform result. 

---

# 5. Sharp stabilization and explicit final collisions

The exact scan finds:

$$
\boxed{\text{last even collision value}=300284,}
$$

$$
\boxed{\text{last odd collision value}=300301.}
$$

Hence

$$
K^{(4)}_\theta=K_\infty
$$

for every even \(\theta\ge300286\), every odd \(\theta\ge300303\), and therefore every integer

$$
\boxed{\theta\ge300302.}
$$

The threshold is sharp.

Write

$$
T_0=
3u+v+20(a_+-a_-)+490(b_+-b_-)+12090(c_+-c_-).
$$

Both final witnesses use deleted row \(i=4\), formal row coordinate \(q=-3\), and adjacent \(d\)-bands \(-2,-1\).

## Last even collision: \(\theta=300284\)

The \(d=-2\) point is

$$
\begin{aligned}
&(u,v;a_+,a_-;b_+,b_-;c_+,c_-\mid x,y;g,h)\\
&\qquad=(10,8;9,2;11,1;12,0\mid3,6;5,7),
\end{aligned}
$$

giving

$$
T_0=150158,\qquad q=3-6=-3,\qquad d=5-7=-2.
$$

The \(d=-1\) point is

$$
(3,5;2,10;1,11;0,12\mid6,9;7,8),
$$

giving

$$
T_0'=-150126,\qquad q=-3,\qquad d'=-1.
$$

Then

$$
150158-2(300284)
=
-150126-300284
=
-450410.
$$

## Last odd collision: \(\theta=300301\)

Replace the first assignment by

$$
(9,8;10,2;11,1;12,0\mid3,6;5,7),
$$

which gives

$$
T_0=150175.
$$

Then

$$
150175-2(300301)
=
-150126-300301
=
-450427.
$$

The exhaustive exact scan finds no even collision beyond \(300284\) and no odd collision beyond \(300301\).

---

# 6. Candidate four-ratio exclusion theorem

The inherited safe-spacing and target estimate give, for the chosen auxiliary spacing,

$$
\sqrt{D+1}|T_1|>970330473\,E,
\qquad E>0.
\tag{36}
$$

For \(|\theta|\in\mathcal T_*\),

$$
K^{(4)}_\theta\le970330474,
$$

so after removing \(C_{ii}(0)\),

$$
\sum_{\rm ordinary}|W_{1;x,y}|
\le
(K^{(4)}_\theta-1)E
\le
970330473\,E.
\tag{37}
$$

Equations (36)–(37) contradict the physical baseline inequality. This proves the candidate theorem `EET4`.

It does not settle the first failure \(\theta=300177\), because its support coefficient exceeds the threshold by \(18\).

---

# 7. First-gap attack: fold the final centered pair

At the first failure, put

$$
\theta_0=300177.
$$

Define

$$
A=T_0+\theta_0d_\theta.
$$

For a fifth integer ratio

$$
m_r=\rho m_6,
$$

the complete formal frequency becomes the single scalar

$$
A+\rho q.
$$

Define the exact fifth-ratio support recurrence

$$
\boxed{
\mathcal C_i^{(5)}
=
\left\{
(A,q):
\begin{array}{l}
A=T_0+300177(g-h),\\
q=x-y,\\
u,v,a,b,c,d,e,f,g,h,x,y\text{ exhaust }R_i
\end{array}
\right\},
}
\tag{38}
$$

$$
\boxed{
S_i^{(5)}(\rho)
=
\left|
\left\{
A+\rho q:(A,q)\in\mathcal C_i^{(5)}
\right\}
\right|,
\qquad
K_\rho^{(5)}=\sum_iS_i^{(5)}(\rho).
}
\tag{39}
$$

This is an exact Boolean recurrence. Field collisions and determinant cancellation again only reduce the actual support.

---

## 7.1 Exact rectangular bound

The exact \(T_0\)-range is

$$
-150127\le T_0\le150175.
$$

Since

$$
-12\le d_\theta\le12,
\qquad d_\theta\ne0,
$$

at \(\theta_0=300177\),

$$
-3752251
=
-150127-12(300177)
\le A
\le
150175+12(300177)
=
3752299.
$$

Thus the inclusive \(A\)-range has length

$$
\boxed{7504551.}
$$

Since

$$
q\in\{-12,\ldots,-1,1,\ldots,12\},
$$

all fifth-ratio support values lie in an interval containing at most

$$
7504551+24|\rho|
$$

integers per deleted row. Therefore

$$
\boxed{
K_\rho^{(5)}
\le
13\bigl(7504551+24|\rho|\bigr).
}
\tag{40}
$$

The criterion \(K_\rho^{(5)}\le970330474\) holds through

$$
\boxed{|\rho|\le2797343.}
\tag{41}
$$

At the endpoint,

$$
13\bigl(7504551+24\cdot2797343\bigr)
=
\boxed{970330179},
$$

so the target-removed margin is

$$
970330473-(970330179-1)
=
\boxed{295}.
\tag{42}
$$

At the next value,

$$
13\bigl(7504551+24\cdot2797344\bigr)
=
970330491,
$$

so this rectangular argument fails by

$$
(970330491-1)-970330473
=
\boxed{17}.
\tag{43}
$$

Using the inherited safe-spacing and target theorem proves `T300177-5R` for every admissible \(\rho\) in the stated range.

This does not settle the generic \(\theta=300177\) case when the final centered pair is not proportional to \(m_6\).

---

# Exact scope

This round produces:

* no exact physical baseline vector;
* no frozen-edge vector;
* no exclusion of \(x^{(10)}\);
* no exact physical vector above \(10\);
* no phase-uniform PW10 proof;
* no general thirteen-slope ansatz theorem.

It produces two candidate finite-slope exclusions:

1. `ExtendedEta12090FourthRatioExclusion` with exact set \(\mathcal T_*\);
2. `Theta300177FifthRatioExclusion` through \(|\rho|=2797343\).

They remain ansatz results pending replication outside this proof-development context.

# VERIFIED

* The exact recurrence (6)–(12).
* The absence of any extra orientation or labeling factor.
* The supplied \(\theta=116983\) row table and checksum.
* The exact values at \(\theta=116982\) and all supplied anchors.
* The exact \(T_0\)-range \([-150127,150175]\).
* The unfolded total \(K_\infty=970343224\).
* The two disjoint adjacent-band collision certificates.
* The exact critical-range formula \(K_\theta=K_\infty-H_0-H_1\).
* All scan checksums in (29)–(33).
* The complete nonmonotone passing set.
* The globally first failure \(300177\).
* The globally closest pass \(300220\).
* Sharp stabilization at \(300302\).
* The explicit final even and odd collision witnesses.
* The fifth-ratio recurrence and rectangular endpoint \(2797343\).

# CORRECTED

* The coarse rectangular endpoint \(116982\) is not the structured frontier.
* The exact four-ratio frontier extends through \(300176\), with fifteen isolated larger passing values.
* The sequence is strongly nonmonotone.
* The globally closest pass is \(300220\), not \(300176\).
* The sharp stabilization threshold is \(300302\), not the crude range endpoint.
* The generic first support gap is \(18\), after target removal.
* The exact fifth-ratio rectangular endpoint is \(2797343\), using the sharp \(T_0\)-range.

# DISPROVED

* Monotonicity of \(K^{(4)}_\theta\).
* Any inference that the coarse failure at \(116983\) reflects the structured support.
* Any inference that support failure at \(300177\) proves that a baseline exists.
* Sharpness of a stabilization threshold based only on the crude \(T_0\)-range.
* Any claim that the fifth-ratio rectangular method stops before \(2797343\).

# NECESSARY-ONLY

* For generic \(\theta=300177\),

  $$
  \sum_{\rm ordinary}|W_{1;x,y}|
  \le970330491\,E.
  $$

* A generic four-ratio exclusion requires an additional reduction of

  $$
  \boxed{18E}.
  $$

* The fifth-ratio bound (40) is an upper bound, not an exact structured count.

* Matching incidence and determinant phases remain unexploited at the generic first gap.

# EQUIVALENT

The exact formal support is equivalently

$$
K^{(4)}_\theta
=
\sum_{i,q}
\left|
\bigcup_{d\ne0}
(\mathcal A_{i,q,d}+\theta d)
\right|.
$$

For \(\theta\ge150152\),

$$
K^{(4)}_\theta
=
K_\infty-H_0(\theta)-H_1(\theta).
$$

The support argument closes exactly when

$$
K^{(4)}_\theta\le970330474.
$$

The fifth-ratio support is equivalently the projection

$$
(A,q)\longmapsto A+\rho q
$$

of \(\mathcal C_i^{(5)}\).

# NUMERICAL-ONLY

* No floating-point optimization or probabilistic sampling is used.
* All support counts, collision counts, and checksums are integer-valued Boolean-bitset computations.
* Any unproved determinant cancellation at \(\theta=300177\) remains numerical-only without an exact certificate.

# CONJECTURED

* Generic exclusion at \(|\theta|=300177\).
* A matching-incidence or determinant identity supplying the missing \(18E\).
* A structured fifth-ratio frontier beyond \(|\rho|=2797343\).
* The full ratio-two one-defect theorem.
* The arbitrary one-defect theorem.
* A general thirteen-slope ansatz theorem.
* Physical liftability or nonliftability of \(x^{(10)}\).

# OPEN

* Generic \(|\theta|=300177\) without a proportional final centered pair.
* The exact determinant/matching-incidence improvement at the \(18E\) gap.
* Fifth-ratio values \(|\rho|\ge2797344\).
* The full \(\delta=\pm2m_6\) class.
* The arbitrary one-defect class.
* Non-centrally-symmetric twelve-slope sets outside the candidate subclasses.
* A general thirteen-slope theorem.
* Dense nonquadratic baseline solutions.
* Existence of an exact baseline pure-edge vector.
* Frozen named-edge retrieval.
* Physical liftability of \(x^{(10)}\).
* An exact physical vector above \(10\).
* PW10.
* The finite \(r=2\), low-\(A\) gate.

The first genuinely new theorem-level claim requiring independent verification is

$$
\boxed{\texttt{ExtendedEta12090FourthRatioExclusion with the exact set }\mathcal T_*.}
$$

The first-gap attack claim requiring independent verification is

$$
\boxed{\texttt{Theta300177FifthRatioExclusion through }|\rho|=2797343.}
$$

The distinction between these finite-slope ansatz statements and the full physical theorem remains essential. 

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$
