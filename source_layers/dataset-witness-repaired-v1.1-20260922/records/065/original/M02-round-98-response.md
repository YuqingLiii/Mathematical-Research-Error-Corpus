# Round 98 audit verdict

$$
\boxed{\texttt{GenericTheta300236Exclusion survives as the finite-slope candidate.}}
$$

For

$$
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300236)m_6,
$$

with the fifth centered pair \(\{\pm m_r\}\) arbitrary and all twelve slopes distinct, the independently regenerated determinant census and the **coupled global-packet certificate** exclude an exact baseline within this displayed centrally symmetric twelve-slope ansatz.

The frozen normalization is

$$
D=941541228773064677=970330474^2+1,\qquad
B^2=\frac1{D(D+2)},\qquad
A_{\rm sp}^2=(D+1)B^2.
$$

These are the exact boundary data fixed by the Round 98 brief. fileciteturn37file0L5-L17

The result remains **CONJECTURED** pending replication outside this proof-development context. It is not PW10.

---

## 1. Target and mismatch report

The audited target is

$$
\boxed{\theta=300236},\qquad
\boxed{K=970338792},\qquad
\boxed{H=(K-1)-970330473=8318}.
$$

The thirteen formal-support totals are

$$
\begin{aligned}
(S_i)=(&53624480,67257904,74299412,80379186,82205750,85480144,\\
&83845040,85480144,82205750,80379186,74299412,67257904,53624480).
\end{aligned}
$$

These target values and the determinant/Laurent coordinates are those prescribed by the brief. fileciteturn37file0L62-L100

### One exact discrepancy

The brief’s displayed raw-size-four vector contains two transcription errors:

$$
H_{4,3}=H_{4,9}=14{,}928{,}318
\quad\text{in the brief,}
$$

but the independently regenerated exact values are

$$
\boxed{H_{4,3}=H_{4,9}=14{,}926{,}862.}
$$

This was confirmed by:

1. the main determinant/Laurent enumerator in three complete executions; and  
2. a separately written count-only `next_permutation` enumerator for deleted rows \(3\) and \(9\).

The corrected raw-size-four vector is

$$
\begin{aligned}
(&8437248,11517728,12835576,14926862,15308304,16650864,\\
&15684084,16650864,15308304,14926862,12835576,11517728,8437248).
\end{aligned}
$$

Its sum is

$$
\boxed{175037248},
$$

which is exactly the global total printed in the brief. Thus the **two row entries**, rather than the global total, were wrong. The corrected census does not alter \(K\), the size-two packet stream, or any load-bearing support-loss inequality.

No other supplied mathematical value required correction.

### Receipt-boundary difference

The brief says that no local Round 97 ZIP receipt exists. In this runtime, that ZIP is present and has SHA-256

```text
1eed3cbfcf576f9369c2e55c81dcfcb2ebb96d95496ed47fc7c8786b36f5a364
```

matching the hash declared in Round 97. It was used only as a code template, never as mathematical evidence for \(\theta=300236\). The included `round97_response.md` is a mathematical reconstruction, not the authenticated browser/API byte stream cited by the brief.

---

## 2. Exact determinant reconstruction

Use the ten fixed special relative slopes

$$
(3,1,20,-20,490,-490,12090,-12090,300236,-300236).
$$

For deleted row \(i\), let

$$
R_i=\{0,\ldots,12\}\setminus\{i\}.
$$

An ordered assignment

$$
\pi=(u,v,a_0,b_0,c,d,e,f,g,h_0,x,y)
$$

defines

$$
\begin{aligned}
t(\pi)
={}&3u+v+20(a_0-b_0)+490(c-d)\\
&+12090(e-f)+300236(g-h_0),
\end{aligned}
$$

$$
q(\pi)=x-y,
$$

$$
\begin{aligned}
Q_6(\pi)
={}&3u^2+v^2+20(a_0^2-b_0^2)+490(c^2-d^2)\\
&+12090(e^2-f^2)+300236(g^2-h_0^2),
\end{aligned}
$$

and

$$
Q_r(\pi)=x^2-y^2.
$$

The exact collected Laurent coefficient is

$$
P_{i;t,q}(Z,W)=
\sum_{\substack{\pi:t(\pi)=t\\q(\pi)=q}}
\varepsilon_i(\pi)Z^{Q_6(\pi)}W^{Q_r(\pi)},
$$

where the same physical phase variables occur in all thirteen cofactors:

$$
Z=\omega^{-m_6h^2/8},\qquad
W=\omega^{-m_rh^2/8}.
$$

An overall maximal-minor sign change in one deleted row multiplies every term in that cofactor by a common sign. It does not change the relative sign used to classify any size-two binomial.

---

## 3. Exact range and complete census

All

$$
\binom{13}{10}=286
$$

ten-row subsets were checked independently by rearrangement. The exact range is

$$
\boxed{-3727755\le t\le3727803}.
$$

The minimizing row set is

$$
\{0,1,2,3,4,5,9,10,11,12\},
$$

and the maximizing set is

$$
\{0,1,2,3,7,8,9,10,11,12\}.
$$

The exploratory buffer \([-3753400,3753450]\) has margins \(25645\) and \(25647\); the runtime buffer \([-3800000,3800000]\) has margins \(72245\) and \(72197\). No determinant assignment was truncated.

### Thirteen-row low-fiber table

| \(i\) | \(S_i\) | singleton \(U_i\) | raw size 2 | raw size 3 | raw size 4 | rowwise matches |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 53,624,480 | 2,611,200 | 8,170,368 | 2,127,360 | 8,437,248 | 8,984 |
| 1 | 67,257,904 | 5,487,296 | 13,221,080 | 3,505,232 | 11,517,728 | 39,080 |
| 2 | 74,299,412 | 6,766,312 | 15,472,552 | 4,554,316 | 12,835,576 | 56,144 |
| 3 | 80,379,186 | 7,100,124 | 17,578,362 | 4,984,304 | **14,926,862** | 57,386 |
| 4 | 82,205,750 | 7,596,718 | 19,216,666 | 5,435,786 | 15,308,304 | 36,880 |
| 5 | 85,480,144 | 8,125,408 | 20,092,532 | 5,746,954 | 16,650,864 | 68,522 |
| 6 | 83,845,040 | 7,619,224 | 18,914,176 | 6,161,992 | 15,684,084 | 65,484 |
| 7 | 85,480,144 | 8,125,408 | 20,092,532 | 5,746,954 | 16,650,864 | 68,522 |
| 8 | 82,205,750 | 7,596,718 | 19,216,666 | 5,435,786 | 15,308,304 | 36,880 |
| 9 | 80,379,186 | 7,100,124 | 17,578,362 | 4,984,304 | **14,926,862** | 57,386 |
| 10 | 74,299,412 | 6,766,312 | 15,472,552 | 4,554,316 | 12,835,576 | 56,144 |
| 11 | 67,257,904 | 5,487,296 | 13,221,080 | 3,505,232 | 11,517,728 | 39,080 |
| 12 | 53,624,480 | 2,611,200 | 8,170,368 | 2,127,360 | 8,437,248 | 8,984 |

The exact totals are

$$
\boxed{\sum_iS_i=970338792},
$$

$$
\boxed{\sum_iU_i=82993340},\qquad
\boxed{\sum_iH_{2,i}=206417296},
$$

$$
\boxed{\sum_iH_{3,i}=58869896},\qquad
\boxed{\sum_iH_{4,i}=175037248}.
$$

Every raw size-two fiber collected to a genuine two-monomial binomial:

$$
\boxed{
\begin{aligned}
\#\{\text{genuine size-two binomials}\}&=206417296,\\
\#\{\text{collected }\pm2\text{ monomials}\}&=0,\\
\#\{\text{zero size-two Laurent polynomials}\}&=0.
\end{aligned}}
$$

At raw size three, rows \(4\) and \(8\) each have exactly \(16\) collected binomials; this is not load-bearing.

The brief required reconstruction of every row count and all four totals, together with the exact packet merge and support-loss certificates. fileciteturn38file0L199-L226

### Seven moment checksums

$$
\boxed{
\begin{aligned}
\sum t&=4954015104,&
\sum\Delta Q_6&=751569369932568,&
\sum\Delta Q_r&=3333280,\\
\sum\sigma&=136798912,&
\sum t^2&=879681805756836044348,\\
\sum(\Delta Q_6)^2&=7185153485045057558160,&
\sum(\Delta Q_r)^2&=79580374736.
\end{aligned}}
$$

---

## 4. Global canonical-key merge

For a collected size-two binomial, order its monomials lexicographically:

$$
c_0Z^AW^B+c_1Z^{A+d_6}W^{B+d_r},
\qquad c_0,c_1\in\{\pm1\}.
$$

Define

$$
\kappa=(d_6,d_r),\qquad \sigma=c_0c_1.
$$

After removing the leading unit monomial, its magnitude is

$$
\left|1+\sigma Z^{d_6}W^{d_r}\right|.
$$

Because every cofactor uses the same \(Z,W\), equal keys across different rows share

$$
\zeta_\kappa=Z^{d_6}W^{d_r}.
$$

Opposite signs at one key therefore form the exact packet

$$
|1+\zeta_\kappa|,\qquad |1-\zeta_\kappa|.
$$

The C++ streaming merge, direct merged-binary verifier, and independent concatenate-sort-reduce verifier agree exactly:

$$
\boxed{
\begin{aligned}
\#\text{records}&=206417296,\\
\#(+)&=171608104,\\
\#(-)&=34809192,\\
\#\text{global keys}&=8007270,\\
\#\text{keys carrying both signs}&=172923,\\
M_{\rm global}&=1270316,\\
\max_\kappa\min(p_\kappa,n_\kappa)&=1152.
\end{aligned}}
$$

The rowwise match total is \(599476\), giving cross-row gain

$$
\boxed{1270316-599476=670840}.
$$

The per-row census contains

$$
18148962
$$

unique combined-sign keys and

$$
18316897
$$

sign-expanded records, a difference of \(167935\).

The two global merge checksums are

$$
\boxed{19634280408065343339642080},
$$

$$
\boxed{1656756186934360}.
$$

The key ranges are

$$
\boxed{0\le\Delta Q_6\le22479356},\qquad
\boxed{-72\le\Delta Q_r\le72}.
$$

These values reproduce the packet targets and checksums supplied in the brief. fileciteturn38file0L9-L69

Three complete executions produced byte-identical canonical row streams and global streams, as well as identical normalized deterministic logs.

---

## 5. Near-ray and support-loss audit

Assume for contradiction that the total nonnegative four-slack sum is less than \(HE\), where \(H=8318\). Then

$$
\Delta_{\rm ray}<HE,\qquad
\Delta_{\rm flat}<HE.
$$

Put

$$
w_i=\sqrt{S_i},\qquad
\alpha=\frac{w\cdot e}{K}.
$$

Then

$$
\|e-\alpha w\|_2^2
=\frac{\Delta_{\rm ray}}K<\frac{HE}{K},
$$

and

$$
\alpha^2>\frac{K-H}{K^2}E.
$$

The exact consecutive-denominator tests are

$$
\boxed{(K-H)S_{\min}-H\,80^2K=377287436525120>0},
$$

$$
\boxed{(K-H)S_{\min}-H\,81^2K=-922188333043696<0}.
$$

Thus \(80\) is maximal and, inside the contradiction branch,

$$
\boxed{e_i>\frac{79}{80}\alpha\sqrt{S_i}}.
$$

### Separate-row relaxation: failed

For

$$
m_i=S_i-|\operatorname{supp}A_i|,
\qquad
D_i=S_ie_i^2-L_i^2,
$$

support Cauchy gives \(D_i\ge m_ie_i^2\), while the exact flatness expansion gives \(\Delta_{\rm flat}\ge\sum_iD_i\).

The strict separate-row ceilings are

$$
(154350,123063,111400,102974,100686,96829,98717,
96829,100686,102974,111400,123063,154350).
$$

Their doubled sum is

$$
\boxed{B_{\rm row}\le2954642>M_{\rm global}=1270316}.
$$

Therefore the separate-row route certifies no surviving packet and is **not** a proof at \(\theta=300236\).

### Coupled route: load-bearing

Keeping the row weights gives

$$
\sum_i m_iS_i
<
\frac{H\,80^2K^2}{79^2(K-H)}.
$$

Write

$$
N_0=H\,80^2K^2
=50123994970501377522892800,
$$

$$
Q_{\rm base}=79^2(K-H)=6055832488234,
$$

$$
Q_0=Q_{\rm base}S_{\min}
=324740868148654368320.
$$

Exact adjacent-integer rounding gives

$$
\boxed{N_0-154350Q_0
=241971756575772700800>0},
$$

$$
\boxed{N_0-154351Q_0
=-82769111572881667520<0}.
$$

Hence

$$
\boxed{\sum_i m_i\le154350},
\qquad
\boxed{B_{\rm coupled}\le308700}.
$$

The surviving packet and anchor counts are

$$
\boxed{N=1270316-308700=961616},
$$

$$
\boxed{G=82993340-308700=82684640}.
$$

Thus

$$
\boxed{Q=G+4N=86531104},
$$

$$
\boxed{R=K-G-2N=885730920}.
$$

These are exactly the coupled values specified in the brief. fileciteturn38file0L71-L180

---

## 6. Packet inequality and exact contradiction

For each surviving packet,

$$
r_+=|1+\zeta|,\qquad r_-=|1-\zeta|,
$$

with

$$
r_+^2+r_-^2=4,\qquad
r_++r_-\le2\sqrt2.
$$

Concatenating the thirteen padded magnitude arrays gives total length \(K\), squared norm \(E\), and \(\ell_1\)-mass \(L\). The selected anchors and packets have energy

$$
Q=G+4N
$$

and total magnitude at most

$$
A=G+2\sqrt2\,N.
$$

The remaining \(R=K-G-2N\) coordinates carry energy \(E-Q\). Therefore

$$
L\le A+\sqrt{R(E-Q)}
$$

and

$$
L^2\le
\left(R+\frac{A^2}{Q}\right)E.
$$

Since

$$
\Delta_{\rm ray}+\Delta_{\rm flat}=KE-L^2,
$$

we obtain

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
\ge
(6-4\sqrt2)\frac{GN}{G+4N}E.
}
$$

The Pell identity

$$
577^2-2\cdot408^2=1
$$

certifies

$$
6-4\sqrt2>\frac{35}{102}.
$$

The exact cleared comparison is

$$
\boxed{
35GN-8318\cdot102(G+4N)
=2709464443485056>0.
}
$$

Therefore, **inside the contradiction branch**,

$$
\Delta_{\rm ray}+\Delta_{\rm flat}>8318E,
$$

contradicting the hypothesis that the total four-slack sum was below \(8318E\). Hence, unconditionally,

$$
\boxed{
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}
\ge8318E.
}
$$

The exact slack identity gives

$$
M_{\rm ord}
\le(K-1-8318)E
=970330473E.
$$

The inherited baseline target is strict:

$$
\sqrt{D+1}|T_1|>970330473E.
$$

Every exact baseline requires

$$
\sqrt{D+1}|T_1|\le M_{\rm ord}.
$$

Contradiction. Therefore

$$
\boxed{
\begin{gathered}
\texttt{GenericTheta300236Exclusion:}\\
\delta=\pm2m_6,\qquad
(m_j,m_\ell,m_s,m_t)=(20,490,12090,300236)m_6,\\
\text{the fifth centered pair arbitrary and all twelve slopes distinct}\\
\Longrightarrow\text{no exact baseline exists.}
\end{gathered}}
$$

For \(\delta=-2m_6\), exchange the two defect endpoints and reverse the common \(m_6\)-orientation. The census and packet inequality are unchanged.

This is precisely the finite-slope conclusion authorized by the brief, which also requires that it remain `CONJECTURED` and not be promoted to PW10. fileciteturn38file0L218-L236

---

# Reproducibility package

The complete ZIP passes `unzip -t` with no errors.

```text
Round 98 bundle SHA-256
faaeee33399b894e8ef85dbc13aa8103f4b582f125969153d9c74723ce6b1787
```

- [Complete Round 98 audit bundle](sandbox:/mnt/data/round98_theta300236_audit_bundle.zip)
- [Bundle SHA-256 receipt](sandbox:/mnt/data/round98_bundle_sha256.txt)
- [Self-contained Round 98 public derivation](sandbox:/mnt/data/round98_artifacts/round98_public_derivation.md)
- [Round 98 brief](sandbox:/mnt/data/round98_artifacts/round98_brief.md)
- [Brief correction certificate](sandbox:/mnt/data/round98_artifacts/round98_brief_corrections.txt)
- [Round 97 mathematical reconstruction](sandbox:/mnt/data/round98_artifacts/round97_response.md)
- [Exact determinant enumerator](sandbox:/mnt/data/round98_artifacts/round98_aggregate.cpp)
- [Global canonical-key merger](sandbox:/mnt/data/round98_artifacts/round98_size2_merge_audit.cpp)
- [Independent concatenate-sort-reduce verifier](sandbox:/mnt/data/round98_artifacts/round98_verify_rows_sort.cpp)
- [Independent count-only correction verifier](sandbox:/mnt/data/round98_artifacts/round98_countonly_h4.cpp)
- [One-command reproduction script](sandbox:/mnt/data/round98_artifacts/round98_reproduce.sh)
- [Complete low-fiber summary](sandbox:/mnt/data/round98_artifacts/round98_lowfiber_summary.csv)
- [Complete raw-fiber histogram](sandbox:/mnt/data/round98_artifacts/round98_raw_fiber_histogram.csv)
- [Global packet summary](sandbox:/mnt/data/round98_artifacts/round98_global_size2_summary.csv)
- [Global merge details](sandbox:/mnt/data/round98_artifacts/round98_global_size2_detail.txt)
- [Exact support-loss arithmetic certificate](sandbox:/mnt/data/round98_artifacts/round98_exact_inequality_checks.txt)
- [Exact range certificate](sandbox:/mnt/data/round98_artifacts/round98_range_check.txt)
- [Direct global-binary verification](sandbox:/mnt/data/round98_artifacts/round98_global_verify.txt)
- [Independent all-row verification](sandbox:/mnt/data/round98_artifacts/round98_rows_sort_verify.txt)
- [Three-execution comparison](sandbox:/mnt/data/round98_artifacts/round98_three_reproductions.txt)
- [Canonical-stream digest manifest](sandbox:/mnt/data/round98_artifacts/round98_stream_sha256.txt)
- [Normalized exhaustive master log](sandbox:/mnt/data/round98_artifacts/round98_master.log)
- [Source and verifier receipts](sandbox:/mnt/data/round98_artifacts/round98_receipts.txt)
- [Receipt self-check](sandbox:/mnt/data/round98_artifacts/round98_receipt_selfcheck.txt)
- [Complete artifact digest](sandbox:/mnt/data/round98_artifacts/round98_digest.txt)

## Core fresh runtime hashes

```text
Round 98 brief
3ff85ab484db1fc135688b573143ce8702274f0d53fcf6836b5c8d0d7c792cc4

determinant enumerator source
f5c877ae178ecfef876aa01e08550fc053812fd1db255a63d0689f4e54965ebd

determinant enumerator binary
db268d7b31c9423818d6b8b693bf2d394eef99d02f0926ca04481b53351b98aa

normalized exhaustive master log
0414be4dae7fdcbddd2ce548b8de79802cd7a708422d758ff8fa5c414a67f945

global merged stream
b53835079c11794e563c9864861b170df5f563c4464043e5379ed42ca4362752

global merged stream size
192174480 bytes

three-execution comparison
0bd1139fa7c435f2f15fa85cf74c6f49376fd5d62f5b298e8fc369c3f3d20906

exact arithmetic output
fec6fd61542b996067340f485b96670fe6b6c550f560952d040e934a8e834837

range output
71521e03dcc1e2d2dff5027611e5c7f3cbc5385b0ef51b8dbadf999ecbcd8c49

public derivation
d14d190647f654d6b3ce8661ca07973fac225891f5f3f5b4edee7f864a95cbcc

count-only correction source
ec8b02d174dea772cb3868b75b8e4d3c1bf5958ec4712e2a60bbe8eff0a5a942
```

# VERIFIED

- \(\theta=300236\), \(K=970338792\), and \(H=8318\).
- Exact range \([-3727755,3727803]\) and buffer adequacy.
- All thirteen formal-support, singleton, size-two, size-three, **corrected** size-four, and rowwise-match counts.
- Global low-fiber totals
  $$
  82993340,\quad206417296,\quad58869896,\quad175037248.
  $$
- Every raw size-two fiber is a genuine binomial.
- No collected size-two \(\pm2\) monomial and no zero size-two Laurent polynomial.
- All seven moment checksums.
- Rowwise matching total \(599476\).
- Global match count
  $$
  M_{\rm global}=1270316.
  $$
- Cross-row gain \(670840\).
- Both global merge checksums, both row-key conventions, and exact key ranges.
- Direct merged-binary and independent concatenate-sort-reduce verification.
- Three byte-identical complete canonical-stream executions.
- Maximal denominator \(80\), with \(81\) failing.
- All strict separate-row ceilings and the failed budget
  $$
  B_{\rm row}=2954642.
  $$
- Coupled bounds
  $$
  \sum_i m_i\le154350,\qquad
  B_{\rm coupled}\le308700.
  $$
- Survivor tuple
  $$
  (N,G,Q,R)=(961616,82684640,86531104,885730920).
  $$
- Exact positive margin
  $$
  2709464443485056.
  $$
- `GenericTheta300236Exclusion` within the displayed finite-slope ansatz.

# CORRECTED

- The brief’s raw-size-four values for rows \(3\) and \(9\) are corrected from \(14{,}928{,}318\) to \(14{,}926{,}862\).
- The brief’s global raw-size-four total \(175{,}037{,}248\) was already correct.
- A separate count-only enumerator independently verifies the corrected entries.
- The brief’s statement that the Round 97 ZIP is unavailable differs from this runtime; the ZIP is present with the declared hash and was used only as a template.
- The strict packet inequality is asserted only inside the contradiction branch.
- The included prior response is a mathematical reconstruction, not an authenticated browser/API byte receipt.

# DISPROVED

- The two erroneous raw-size-four row entries in the brief.
- Adequacy of the thirteen separate-row ceilings at \(\theta=300236\).
- The claim that rowwise matching exhausts the cross-cofactor packet structure.
- The possibility that the regenerated coupled packet coefficient is at most \(8318\).
- The status “generic \(\theta=300236\) remains open” within this exact finite-slope ansatz.

# NECESSARY-ONLY

- Replication outside this proof-development context remains necessary.
- The result applies only to the displayed centrally symmetric twelve-slope family.
- It does not settle general baseline existence.
- It does not exclude \(x^{(10)}\).
- It does not construct an exact physical vector above \(10\).
- It does not prove a general thirteen-slope theorem.
- It does not prove PW10.
- It does not prove the complete finite \(r=2\), low-\(A\) gate.

# EQUIVALENT

Within the audited Wiener chain,

$$
\Delta_{\rm ray}+\Delta_{\rm flat}
+\Delta_{\rm Young}+\Delta_{\rm group}
\ge8318E
$$

is equivalent, through the exact slack identity, to

$$
M_{\rm ord}\le970330473E.
$$

For each globally matched key, the paired magnitudes are exactly

$$
|1+\zeta|,\qquad |1-\zeta|.
$$

For the certified \((G,N)\), the packet coefficient is exactly

$$
(6-4\sqrt2)\frac{GN}{G+4N}.
$$

# NUMERICAL-ONLY

- No floating-point phase sampling was used.
- No heuristic cancellation was used.
- No numerical optimizer, SDP, or interval search was used.
- Determinant enumeration, Laurent-fiber collection, key merging, support-loss rounding, and the cleared comparison are exact integer computations.
- Runtime measurements have no mathematical evidentiary role.

# CONJECTURED

- External replication of `GenericTheta300236Exclusion`.
- Extension of the coupled packet method to later unresolved finite-slope values.
- A general thirteen-slope ansatz theorem.
- Physical liftability or nonliftability of \(x^{(10)}\).

# OPEN

- The full ratio-two class.
- The arbitrary one-defect class.
- Non-centrally-symmetric twelve-slope families outside the finite-slope candidate exclusions.
- A general thirteen-slope theorem.
- Dense nonquadratic baseline solutions.
- Exact baseline existence outside the excluded finite-slope ansätze.
- Frozen named-edge retrieval.
- Physical liftability of \(x^{(10)}\).
- An exact physical vector above \(10\).
- PW10.
- The complete finite \(r=2\), low-\(A\) gate.

No exact baseline vector, exact frozen-edge vector, exclusion of \(x^{(10)}\), exact physical vector above \(10\), phase-uniform PW10 proof, general thirteen-slope theorem, or full-size proof was produced.

The first genuinely new claim requiring outside verification is

$$
\boxed{M_{\rm global}=1270316},
$$

together with

$$
\boxed{
\sum_i m_i\le154350,\qquad
B_{\rm coupled}\le308700,\qquad
N=961616,\qquad G=82684640,
}
$$

and

$$
\boxed{
35GN-8318\cdot102(G+4N)
=2709464443485056>0.
}
$$

$$
\boxed{\text{PW10 for the exact frozen tuple remains OPEN WITH EARLIEST GAP.}}
$$
