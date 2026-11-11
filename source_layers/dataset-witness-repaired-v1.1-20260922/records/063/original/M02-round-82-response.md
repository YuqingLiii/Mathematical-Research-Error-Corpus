# Round 82 audit verdict

$$
\boxed{\texttt{GenericTheta300219Exclusion is proved within the present finite-slope audit context.}}
$$

For

$$
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300219)m_6,
$$

with the fifth centered pair \(\{\pm m_r\}\) arbitrary and all twelve slopes distinct, the independently regenerated determinant census and the coupled global packet certificate rule out an exact baseline.

The frozen normalization is

$$
D=941541228773064677=970330474^2+1,\qquad
B^2=\frac1{D(D+2)},\qquad
A_{\rm sp}^2=(D+1)B^2.
$$

These are the exact constants fixed by the Round 82 brief.  The audited target is

$$
\theta=300219,\qquad
K=970337664,\qquad
H=(K-1)-970330473=7190,
$$

for the displayed centrally symmetric twelve-slope family, with the final centered pair left arbitrary. 

No mathematical mismatch was found. The result remains **CONJECTURED** pending replication outside this proof-development context. It is a finite-slope ansatz exclusion, not PW10.

---

## 1. Exact determinant reconstruction and range

Use the ten fixed special relative slopes

$$
(3,1,20,-20,490,-490,12090,-12090,300219,-300219).
$$

For deleted row \(i\), let

$$
R_i=\{0,\ldots,12\}\setminus\{i\}.
$$

An ordered assignment

$$
\pi=(u,v,a_0,b_0,c,d,e,f,g,h_0,x,y)
$$

of the twelve columns to \(R_i\) defines

$$
\begin{aligned}
t(\pi)
={}&3u+v+20(a_0-b_0)+490(c-d)\\
&+12090(e-f)+300219(g-h_0),
\end{aligned}
$$

$$
q(\pi)=x-y,
$$

$$
\begin{aligned}
Q_6(\pi)
={}&3u^2+v^2+20(a_0^2-b_0^2)+490(c^2-d^2)\\
&+12090(e^2-f^2)+300219(g^2-h_0^2),
\end{aligned}
$$

and

$$
Q_r(\pi)=x^2-y^2.
$$

The collected Laurent coefficient is

$$
P_{i;t,q}(Z,W)
=
\sum_{\substack{\pi:t(\pi)=t\\q(\pi)=q}}
\varepsilon_i(\pi)Z^{Q_6(\pi)}W^{Q_r(\pi)},
$$

where all thirteen cofactors use the same physical variables

$$
Z=\omega^{-m_6h^2/8},
\qquad
W=\omega^{-m_rh^2/8}.
$$

An overall signed-minor convention change in one cofactor multiplies all terms in that cofactor by the same sign and leaves every relative size-two sign unchanged.

### Rearrangement audit

All

$$
\binom{13}{10}=286
$$

ten-row subsets were checked independently by the rearrangement inequality. The exact range is

$$
\boxed{-3727551\le t\le3727599}.
$$

The minimizing row set is

$$
\{0,1,2,3,4,5,9,10,11,12\},
$$

and the maximizing row set is

$$
\{0,1,2,3,7,8,9,10,11,12\}.
$$

The direct enumerator used

$$
[-3800000,3800000],
$$

leaving exact safety margins \(72449\) and \(72401\). No determinant assignment was truncated. The exact range agrees with the discovery boundary in the brief. 

---

## 2. Complete thirteen-row low-fiber census

All thirteen deleted rows were regenerated directly; reflected rows were not filled by copying.

| \(i\) |    \(S_i\) | singleton \(U_i\) | raw size 2 | raw size 3 | raw size 4 | rowwise matches |
| ----: | ---------: | ----------------: | ---------: | ---------: | ---------: | --------------: |
|     0 | 53,624,480 |         2,611,200 |  8,170,368 |  2,127,360 |  8,437,248 |           8,996 |
|     1 | 67,257,904 |         5,487,296 | 13,221,080 |  3,505,232 | 11,517,728 |          39,252 |
|     2 | 74,299,396 |         6,766,276 | 15,472,576 |  4,554,316 | 12,835,564 |          56,288 |
|     3 | 80,379,126 |         7,100,030 | 17,578,366 |  4,984,338 | 14,926,858 |          57,570 |
|     4 | 82,205,586 |         7,596,522 | 19,216,670 |  5,435,766 | 15,308,312 |          36,924 |
|     5 | 85,479,878 |         8,125,098 | 20,092,420 |  5,747,058 | 16,650,908 |          68,686 |
|     6 | 83,844,924 |         7,619,168 | 18,914,008 |  6,162,040 | 15,684,148 |          65,752 |
|     7 | 85,479,878 |         8,125,098 | 20,092,420 |  5,747,058 | 16,650,908 |          68,686 |
|     8 | 82,205,586 |         7,596,522 | 19,216,670 |  5,435,766 | 15,308,312 |          36,924 |
|     9 | 80,379,126 |         7,100,030 | 17,578,366 |  4,984,338 | 14,926,858 |          57,570 |
|    10 | 74,299,396 |         6,766,276 | 15,472,576 |  4,554,316 | 12,835,564 |          56,288 |
|    11 | 67,257,904 |         5,487,296 | 13,221,080 |  3,505,232 | 11,517,728 |          39,252 |
|    12 | 53,624,480 |         2,611,200 |  8,170,368 |  2,127,360 |  8,437,248 |           8,996 |

The exact totals are

$$
\boxed{\sum_iS_i=970337664},
$$

$$
\boxed{\sum_iU_i=82992012},
$$

$$
\boxed{\sum_iH_{2,i}=206416968},
\qquad
\boxed{\sum_iH_{3,i}=58870180},
\qquad
\boxed{\sum_iH_{4,i}=175037384}.
$$

Every raw size-two fiber collected to a genuine two-monomial binomial:

$$
\boxed{
\begin{aligned}
\#\{\text{genuine size-two binomials}\}&=206416968,\\
\#\{\text{collected }\pm2\text{ monomials}\}&=0,\\
\#\{\text{zero size-two Laurent polynomials}\}&=0.
\end{aligned}}
$$

These reproduce every low-fiber row and all four global totals supplied in the brief. 

### Seven exact moment checksums

The concatenated canonical size-two streams give

$$
\boxed{
\begin{aligned}
\sum t&=4954007232,\\
\sum\Delta Q_6&=751527852930248,\\
\sum\Delta Q_r&=3333296,\\
\sum\sigma&=136798120,\\
\sum t^2&=879582216897143216480,\\
\sum(\Delta Q_6)^2&=7184347031263105435440,\\
\sum(\Delta Q_r)^2&=79580429328.
\end{aligned}}
$$

---

## 3. Global canonical-key merge

Order each collected size-two binomial lexicographically:

$$
c_0Z^AW^B+c_1Z^{A+d_6}W^{B+d_r},
\qquad c_0,c_1\in\{\pm1\}.
$$

Define

$$
\kappa=(d_6,d_r),
\qquad
\sigma=c_0c_1\in\{\pm1\}.
$$

After removing the leading unit sign and monomial, its physical magnitude is

$$
\left|1+\sigma Z^{d_6}W^{d_r}\right|.
$$

Since all cofactors use the same physical \(Z,W\), records from different deleted rows with equal \(\kappa\) share

$$
\zeta_\kappa=Z^{d_6}W^{d_r}.
$$

Opposite-sign records at that key therefore have exact magnitudes

$$
|1+\zeta_\kappa|,
\qquad
|1-\zeta_\kappa|.
$$

An overall signed-minor convention change in one deleted row changes both binomial coefficients by the same sign and does not alter \(\sigma\). Cross-row pairing is therefore convention-independent.

A thirteen-way C++ streaming merge, a separate verifier of the merged binary, and an independently written NumPy concatenate–lexsort–reduce verifier agree exactly on

$$
\boxed{
\begin{aligned}
\#\{\text{row-key records}\}&=18148133,\\
\#\{\text{global keys}\}&=8003524,\\
\#\{+\text{ records}\}&=171607544,\\
\#\{-\text{ records}\}&=34809424,\\
\#\{\text{keys carrying both signs}\}&=174962,\\
M_{\rm global}&=1278684,\\
\max_\kappa\min(p_\kappa,n_\kappa)&=1152.
\end{aligned}}
$$

The rowwise match total is only

$$
601184,
$$

so the exact cross-row gain is

$$
\boxed{1278684-601184=677500}.
$$

The two global merge checksums are

$$
\boxed{19618180552045238370105676}
$$

and

$$
\boxed{1655672247452000}.
$$

These reproduce every global-merge quantity specified by the brief. 

Three complete executions produced byte-identical thirteen-row streams and byte-identical merged global streams. The merged global stream has

```text
SHA-256: 217f3722af84e850acd35d08636149994b4705366d88448b6a02c5929b19da26
size:    192084576 bytes
```

---

## 4. Exact near-ray estimate

Assume for contradiction that the total four-slack sum is below

$$
HE=7190E.
$$

Since all four slacks are nonnegative,

$$
\Delta_{\rm ray}<HE,
\qquad
\Delta_{\rm flat}<HE.
$$

Put

$$
w_i=\sqrt{S_i},
\qquad
\alpha=\frac{w\cdot e}{K}.
$$

Then

$$
\|e-\alpha w\|_2^2
=
\frac{\Delta_{\rm ray}}K
<
\frac{HE}{K},
$$

while

$$
\alpha^2
=
\frac{(w\cdot e)^2}{K^2}
>
\frac{K-H}{K^2}E.
$$

The exact consecutive-denominator tests are

$$
\boxed{
(K-H)S_{\min}-H\cdot86^2K
=433588256836160>0,
}
$$

whereas

$$
\boxed{
(K-H)S_{\min}-H\cdot87^2K
=-773385653283520<0.
}
$$

Thus \(86\) is the largest valid denominator and, inside the contradiction branch,

$$
\boxed{
e_i>\frac{85}{86}\alpha\sqrt{S_i}
\quad\text{for every }i.
}
$$

The denominator and both exact signs agree with the independent discovery calculation. 

---

## 5. Why the separate-row relaxation fails

For row \(i\), define

$$
m_i=S_i-|\operatorname{supp}A_i|,
\qquad
D_i=S_ie_i^2-L_i^2.
$$

The flatness slack expands as

$$
\begin{aligned}
\Delta_{\rm flat}
={}&
\left(\sum_i\sqrt{S_i}e_i\right)^2
-\left(\sum_iL_i\right)^2\\
={}&
\sum_iD_i+
2\sum_{i<j}
\left(\sqrt{S_iS_j}e_ie_j-L_iL_j\right).
\end{aligned}
$$

Since

$$
L_i\le\sqrt{S_i}e_i,
$$

all cross terms are nonnegative, so

$$
\Delta_{\rm flat}\ge\sum_iD_i.
$$

Support Cauchy gives

$$
D_i\ge m_ie_i^2.
$$

Bounding each row separately by \(D_i<HE\) gives the strict integer ceilings

$$
\boxed{
\begin{aligned}
(m_i)=(&133183,106186,96123,88852,86878,83550,85179,\\
       &83550,86878,88852,96123,106186,133183).
\end{aligned}}
$$

The resulting independent-row bad-coordinate budget is

$$
\boxed{
B_{\rm row}\le2\sum_i m_i=2549446.
}
$$

But

$$
2549446>M_{\rm global}=1278684.
$$

Therefore the separate-row route certifies no surviving packet. It does **not** prove the \(\theta=300219\) case. This failure is a limitation of that relaxation, not an admissible physical deletion witness. The brief expressly identifies the coupled route—not these thirteen separate bounds—as load-bearing. 

---

## 6. Load-bearing coupled support-loss certificate

Retain the single weighted inequality before replacing the row weights individually. Inside the contradiction branch,

$$
HE>\Delta_{\rm flat}
\ge\sum_iD_i
\ge\sum_i m_ie_i^2.
$$

Using

$$
e_i^2>
\frac{85^2(K-H)}{86^2K^2}ES_i
$$

gives

$$
\boxed{
\sum_i m_iS_i
<
\frac{H\,86^2K^2}{85^2(K-H)}.
}
$$

The exact numerator is

$$
N_0=H\,86^2K^2
=50069305895868822873047040,
$$

and

$$
Q_{\rm base}=85^2(K-H)
=7010637674650.
$$

With

$$
S_{\min}=53624480,
$$

put

$$
Q_0=Q_{\rm base}S_{\min}
=375941799771515432000.
$$

The adjacent integer comparisons are

$$
\boxed{
N_0-133183Q_0
=249176899083092991040>0,
}
$$

$$
\boxed{
N_0-133184Q_0
=-126764900688422440960<0.
}
$$

The bound is strict and \(\sum_i m_i\) is integral. Therefore

$$
\boxed{\sum_i m_i\le133183}.
$$

A zero formal coefficient consumes one support loss. A nontrivial actual-frequency collision group of size \(r\ge2\) consumes at least \(r-1\) support losses and involves at most \(2(r-1)\) relevant singleton/size-two coordinates. Thus the one coupled bad-coordinate set satisfies

$$
\boxed{
B_{\rm coupled}\le2\sum_i m_i\le266366.
}
$$

This reproduces the load-bearing support-loss certificate in the brief. 

---

## 7. Simultaneous packet and anchor survivors

Choose a fixed coordinate-disjoint family of

$$
M_{\rm global}=1278684
$$

opposite-sign packets.

Every selected size-two coordinate occurs in exactly one selected packet. The singleton and size-two populations are also disjoint. Against the **same** coupled bad set:

* at most \(B_{\rm coupled}\) selected packets are destroyed;
* at most \(B_{\rm coupled}\) singleton anchors are bad.

The deletion budget is not partitioned or counted twice; both are conservative consequences of the same bad-coordinate set.

Hence

$$
\boxed{
N=1278684-266366=1012318,
}
$$

$$
\boxed{
G=82992012-266366=82725646.
}
$$

Consequently,

$$
\boxed{
Q=G+4N=86774918,
}
$$

and

$$
\boxed{
R=K-G-2N=885587382.
}
$$

The exact survivor tuple is therefore

$$
\boxed{
(N,G,Q,R)
=
(1012318,82725646,86774918,885587382).
}
$$

These values agree exactly with the brief. 

---

## 8. Global \(KE-L^2\) packet inequality

Concatenate the thirteen coefficient-magnitude arrays, padding row \(i\) to length \(S_i\). Their total length is \(K\), total squared norm is \(E\), and total \(\ell_1\)-mass is

$$
L=\sum_iL_i.
$$

For one surviving opposite-sign packet, put

$$
r_+=|1+\zeta|,
\qquad
r_-=|1-\zeta|,
\qquad |\zeta|=1.
$$

Exactly,

$$
r_+^2+r_-^2=4,
$$

and

$$
r_++r_-\le2\sqrt2.
$$

Thus the \(G\) singleton anchors and \(N\) packets have exact squared energy

$$
Q=G+4N
$$

and total magnitude at most

$$
A=G+2\sqrt2\,N.
$$

The remaining

$$
R=K-G-2N
$$

coordinates carry squared energy \(E-Q\). Therefore

$$
L\le A+\sqrt{R(E-Q)}.
$$

Writing the right-hand side as

$$
\frac A{\sqrt Q}\sqrt Q+\sqrt R\,\sqrt{E-Q}
$$

and applying Cauchy–Schwarz gives

$$
L^2
\le
\left(R+\frac{A^2}{Q}\right)E.
$$

Since

$$
\Delta_{\rm ray}+\Delta_{\rm flat}=KE-L^2
$$

and \(K-R=G+2N\),

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
\ge
(6-4\sqrt2)\frac{GN}{G+4N}E.
}
$$

The exact Pell identity

$$
577^2-2\cdot408^2=1
$$

certifies

$$
\sqrt2<\frac{577}{408},
\qquad
6-4\sqrt2>\frac{35}{102}.
$$

The cleared comparison is

$$
\boxed{
\begin{aligned}
&35GN-7190\cdot102(G+4N)\\
&\qquad=2867424128397140>0.
\end{aligned}}
$$

Therefore, inside the contradiction branch,

$$
\Delta_{\rm ray}+\Delta_{\rm flat}>7190E.
$$

This contradicts the assumption that the total nonnegative four-slack sum was below \(7190E\). Hence, unconditionally,

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}
\ge7190E.
}
$$

The brief’s exact packet inequality and positive margin are thereby independently reproduced. 

---

## 9. Baseline contradiction

The exact slack identity is

$$
(K-1)E-M_{\rm ord}
=
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}.
$$

Because

$$
K-1-7190=970330473,
$$

the proved total-slack lower bound gives

$$
\boxed{
M_{\rm ord}\le970330473E.
}
$$

The inherited target estimate is strict:

$$
\sqrt{D+1}|T_1|>970330473E.
$$

Every exact baseline would require

$$
\sqrt{D+1}|T_1|\le M_{\rm ord}.
$$

Contradiction. Thus the exact finite-slope conclusion is

$$
\boxed{
\begin{gathered}
\texttt{GenericTheta300219Exclusion:}\\
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300219)m_6,\\
\text{the fifth centered pair arbitrary and all twelve slopes distinct}\\
\Longrightarrow\text{no exact baseline exists.}
\end{gathered}}
$$

For \(\delta=-2m_6\), exchange the two defect endpoints and reverse the common \(m_6\)-orientation. The determinant census, canonical keys, and packet inequality are unchanged.

The requested logical status is exactly the one prescribed by the brief: finite-slope candidate only, **CONJECTURED** pending replication outside this proof context. 

---

# Mismatch and receipt report

## Mathematical mismatches

$$
\boxed{\text{None.}}
$$

Every requested support total, range endpoint, low-fiber count, moment checksum, merge checksum, match count, near-ray sign, support-loss bound, survivor count, and cleared margin agrees exactly.

## Byte-level implementation differences

The discovery implementation quoted in the brief has these hashes:

```text
discovery enumerator source
43d190771896e6a9f62096b254b08aace475e91c7f47e8aeac0129f54db2f224

discovery exhaustive log
f74ede02ecd6289798f180fedddd014df68e0fab2f9abeed89c505a3e8ecfd45

discovery arithmetic verifier
19b035ae9e60ffbe521123607ff424becd106a22e590ff396b9796f9c8394de4

discovery arithmetic output
9dfd137cdfcf7e3332d735ab80d00604155af5305fd9d2a319889e214b725b67
```

Those are the independent receipts recorded by the brief. 

The fresh runtime implementation has different source and log hashes because it is a separately reconstructed implementation:

```text
Round 82 brief
85ea8df0321a23ac6fd8aef914646fa6dff14b571e2f5a7eaa155c0524ddb97d

determinant enumerator source
990f015b4148fc9c1c6d2473e872d09ed5631e4b06d40ca6bf1698532d9f4a9f

global merge source
6d90292bd18072c941ea37e977b918f547a2f0c99b64b8b3619310ac37da0f04

exhaustive master log
e2744343d88804007345539cf35d68be6cf8da96b2e93b932f09450e9b4a67c8

global binary verifier source
375a3f2dc9b64bddd7f38a53c79d7d80000e6c9da4a580d54a927e23fd61d9b6

global binary verifier output
f1f799ae2e0bd1c1f8a74f82d32cd68e30171555e74f3a2da5bde92ef7ee81e6

NumPy all-row verifier source
0e5edc7845785773e2dd80548a2ea25deaebd4b7dd0ca97c8e7a6b42f955d05d

NumPy all-row verifier output
68db79438713d4dca61cd532bb6812abce9940a3187f62a8e403d5db169fc9cd

expected-value verifier source
40c287fa690b54b805c4e11ff2f950825dedeb3a132ea5b394e5b9561b73033f

expected-value verifier output
5a86d33da067cbbad1f875c0baa741928d77236025472e60a48ad8d10524ae8d

exact arithmetic verifier source
851fbfb088cb40d3bc2b04cae393fd05d7f4f4001a90581acb714bb4e0b20a7a

exact arithmetic output
c361c74fec9384833a1489ed8f0c24351979bbab2ff8cebb202114a4feb35e34

range verifier source
22da2f6393929289b3c462a406fdbbff2d35450c00e07d77223ccc09dae14aa1

range output
107b824138b563f5ed5521b0cad235a82973d64e7b8c3ce04baf5a7949335614

global merged stream
217f3722af84e850acd35d08636149994b4705366d88448b6a02c5929b19da26

public derivation
23a77e783350bb5e48b673edca07b72fbb6348fc9d23e0fd0568186152435488

three-run comparison
d9a593af0d50f2c06f88f31e4e66e23f17f581eaec7e01ea4eb72059796d363e
```

The different source and log hashes are explicitly recorded and are not silently treated as identical receipts. The independently computed mathematical outputs agree exactly.

The exact Round 81 browser byte stream was unavailable in this runtime. The bundle therefore contains a self-contained mathematical `round81_response.md` reconstruction and labels it explicitly as **not** a browser-byte or clipboard receipt, as permitted by the Round 82 brief. 

## Final bundle

```text
SHA-256
c7f1cc5c3b6546c2e935141f971b00d9237ecf0f025dd297cb4543fe8dfc4f7c
```

The ZIP passes a complete `unzip -t` integrity check.

* [Complete Round 82 audit bundle](sandbox:/mnt/data/round82_theta300219_audit_bundle.zip)
* [Bundle SHA-256 receipt](sandbox:/mnt/data/round82_bundle_sha256.txt)
* [Self-contained Round 82 public derivation](sandbox:/mnt/data/round82_artifacts/round82_public_derivation.md)
* [Round 82 brief](sandbox:/mnt/data/round82_artifacts/round82_brief.md)
* [Round 81 mathematical reconstruction](sandbox:/mnt/data/round82_artifacts/round81_response.md)
* [Integer-only determinant enumerator](sandbox:/mnt/data/round82_artifacts/round82_aggregate.cpp)
* [Global canonical-key merge source](sandbox:/mnt/data/round82_artifacts/round82_size2_merge_audit.cpp)
* [One-command reproduction script](sandbox:/mnt/data/round82_artifacts/round82_reproduce.sh)
* [Independent global binary verifier](sandbox:/mnt/data/round82_artifacts/round82_verify_global.py)
* [Independent NumPy all-row verifier](sandbox:/mnt/data/round82_artifacts/round82_verify_rows_numpy.py)
* [Expected-value verifier](sandbox:/mnt/data/round82_artifacts/round82_verify_expected.py)
* [Exact arithmetic verifier](sandbox:/mnt/data/round82_artifacts/round82_exact_inequality_checks.py)
* [Exact arithmetic output](sandbox:/mnt/data/round82_artifacts/round82_exact_inequality_checks.txt)
* [Exact rearrangement-range certificate](sandbox:/mnt/data/round82_artifacts/round82_range_check.txt)
* [Complete low-fiber summary](sandbox:/mnt/data/round82_artifacts/round82_lowfiber_summary.csv)
* [Complete raw-fiber histogram](sandbox:/mnt/data/round82_artifacts/round82_raw_fiber_histogram.csv)
* [Global packet summary](sandbox:/mnt/data/round82_artifacts/round82_global_size2_summary.csv)
* [Global merge details](sandbox:/mnt/data/round82_artifacts/round82_global_size2_detail.txt)
* [Three-execution byte-comparison report](sandbox:/mnt/data/round82_artifacts/round82_three_reproductions.txt)
* [Large-stream digest manifest](sandbox:/mnt/data/round82_artifacts/round82_stream_sha256.txt)
* [Exhaustive master log](sandbox:/mnt/data/round82_artifacts/round82_master.log)
* [Source and verifier receipts](sandbox:/mnt/data/round82_artifacts/round82_receipts.txt)
* [Complete artifact digest](sandbox:/mnt/data/round82_artifacts/round82_digest.txt)

# VERIFIED

* The exact target

  $$
  K=970337664,\qquad H=7190.
  $$
* The exact assignment range

  $$
  -3727551\le t\le3727599.
  $$
* Buffer adequacy.
* All thirteen formal-support totals.
* All thirteen singleton, size-two, size-three, size-four, and rowwise-match counts.
* The global low-fiber totals

  $$
  \sum U_i=82992012,\quad
  \sum H_{2,i}=206416968,\quad
  \sum H_{3,i}=58870180,\quad
  \sum H_{4,i}=175037384.
  $$
* Every raw size-two fiber is a genuine binomial.
* Zero collected size-two \(\pm2\) monomials.
* Zero zero-valued size-two Laurent polynomials.
* All seven moment checksums.
* The rowwise matching total

  $$
  601184.
  $$
* The global canonical-key count

  $$
  8003524.
  $$
* The global opposite-sign count

  $$
  M_{\rm global}=1278684.
  $$
* The cross-row gain

  $$
  677500.
  $$
* Both weighted merge checksums.
* Independent merged-binary verification.
* Independent NumPy all-row regeneration.
* Three byte-identical complete executions.
* The largest valid near-ray denominator \(86\), with \(87\) failing.
* Every strict separate-row support-loss ceiling.
* The failed separate-row budget

  $$
  B_{\rm row}=2549446.
  $$
* The load-bearing coupled bounds

  $$
  \sum_i m_i\le133183,\qquad
  B_{\rm coupled}\le266366.
  $$
* The coupled survivor tuple

  $$
  (N,G,Q,R)
  =(1012318,82725646,86774918,885587382).
  $$
* Coordinate-disjoint global packet selection.
* Simultaneous singleton-anchor and packet deletion accounting.
* The exact cleared positive margin

  $$
  2867424128397140.
  $$
* The contradiction proving total slack at least \(7190E\).
* `GenericTheta300219Exclusion` within the displayed finite-slope ansatz.

# CORRECTED

* No supplied \(\theta=300219\) mathematical value required correction.
* The runtime enumerator used the wider interval

  $$
  [-3800000,3800000]
  $$

  rather than merely inheriting the exploratory buffer; the exact range remained the same.
* The separate-row route is not a proof at this value.
* The coupled weighted support-loss inequality is load-bearing.
* Rowwise matching does not exhaust the usable global packet structure.
* The strict inequality

  $$
  \Delta_{\rm ray}+\Delta_{\rm flat}>7190E
  $$

  is derived only inside the contradiction branch; the unconditional conclusion is the total four-slack lower bound.
* Runtime source and log hashes differ from the independent discovery hashes because the implementation was separately reconstructed; all mathematical outputs match.
* `round81_response.md` is a mathematical reconstruction, not a browser-byte receipt.

# DISPROVED

* Adequacy of the thirteen independent separate-row ceilings at \(\theta=300219\).
* The claim that rowwise matching captures all usable opposite-sign packets.
* The possibility that the independently regenerated coupled packet coefficient is at most \(7190\).
* The need for size-three packet data in this case.
* The status “generic \(\theta=300219\) remains open” within this exact finite-slope ansatz.

# NECESSARY-ONLY

* Replication outside this proof-development context remains necessary before broader promotion.
* The result covers only the displayed centrally symmetric twelve-slope family.
* It does not settle general baseline existence.
* It does not exclude \(x^{(10)}\).
* It does not construct an exact physical vector with objective above \(10\).
* It does not prove a general thirteen-slope theorem.
* It does not prove PW10.
* It does not prove the complete finite \(r=2\), low-\(A\) gate.

# EQUIVALENT

Within the audited Wiener chain,

$$
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}
\ge7190E
$$

is equivalent through the exact slack identity to

$$
M_{\rm ord}\le970330473E.
$$

For every globally matched key, the paired magnitudes are exactly

$$
|1+\zeta|,
\qquad
|1-\zeta|.
$$

For the certified survivor pair \((G,N)\), the exact packet coefficient is

$$
(6-4\sqrt2)\frac{GN}{G+4N}.
$$

# NUMERICAL-ONLY

* No floating-point phase sampling was used.
* No heuristic phase cancellation was used.
* No numerical optimizer, SDP, or interval search was used.
* Determinant enumeration, low-fiber collection, global merging, checksums, support-loss rounding, and cleared packet comparison are exact integer computations.
* The only radical estimate is reduced to the exact Pell identity

  $$
  577^2-2\cdot408^2=1.
  $$
* Execution-time measurements have no mathematical evidentiary role.

# CONJECTURED

* External replication of `GenericTheta300219Exclusion`.
* Extension of the coupled support-loss method to later unresolved finite-slope values.
* A general thirteen-slope ansatz theorem.
* Physical liftability or nonliftability of \(x^{(10)}\).

# OPEN

* The full ratio-two class.
* The arbitrary one-defect class.
* Non-centrally-symmetric twelve-slope families outside the candidate exclusions.
* A general thirteen-slope theorem.
* Dense nonquadratic baseline solutions.
* Exact baseline existence outside the excluded finite-slope ansätze.
* Frozen named-edge retrieval.
* Physical liftability of \(x^{(10)}\).
* An exact physical vector above \(10\).
* PW10.
* The complete finite \(r=2\), low-\(A\) gate.

No exact baseline vector, exact frozen-edge vector, exclusion of \(x^{(10)}\), exact physical vector above \(10\), phase-uniform PW10 proof, or full-size proof was produced.

The first genuinely new claim requiring independent verification is the determinant-specific coupled certificate

$$
\boxed{
\sum_i m_i\le133183,\qquad
B_{\rm coupled}\le266366,
}
$$

together with

$$
\boxed{
M_{\rm global}=1278684,\qquad
N=1012318,\qquad
G=82725646,
}
$$

and the exact implication

$$
\boxed{
35GN-7190\cdot102(G+4N)
=2867424128397140>0.
}
$$

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$
