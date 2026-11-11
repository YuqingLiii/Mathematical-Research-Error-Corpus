# Concentrated adversarial audit 1/5 — Rounds 1–23

## 1. Audit receipt

**Package.** `01_r001_r023_physical_gate`.

**Attachments received.**

- `/mnt/data/01_r001_r023_physical_gate_CORE.md`
- `/mnt/data/01_r001_r023_physical_gate_EVIDENCE.zip`

**Archive integrity.** I expanded the ZIP to `/mnt/data/audit01`. `MANIFEST.tsv` contains 229 payload entries; I recomputed every listed byte count and SHA-256. Result: **229/229 present, 229/229 byte counts match, 229/229 SHA-256 values match**. This authenticates the archived bytes only; it does not validate the mathematics.

**Files actually opened/read as mathematical evidence.**

- `audit/01_r001_r023_physical_gate_CORE.md`: traversed by round/section headings and read at the load-bearing reduction, correction, status-ledger, and Round-23-gap locations. I did **not** treat the 45,581-line file as self-authenticating and did not manually reread every non-load-bearing prose paragraph.
- `audit/MASTER_AUDIT_PROTOCOL.md`, `audit/BASELINE.md`, `audit/01_r001_r023_physical_gate_ROUND_INDEX.tsv`, and `MANIFEST.tsv`.
- The local audits for **Rounds 1–23** (Rounds 1–6 through the CORE plus direct source checks where needed; Rounds 7–23 from `evidence/outputs/round-XX-local-audit.md`).
- Targeted response/source sections, especially `round-13-response.md` for `x^(10)`, plus response text exercised by the verifier scripts.
- Targeted independent derivations and checker source around the Round 18–23 Hessian/residual/two-line/edge-Fourier chain.

**Code actually run.**

- All **46** archived `evidence/work/verify_round*.py` programs (Rounds 9–23) were bytecode-compiled and executed from the correct archive root. **46/46 exited 0.** The first attempt from the wrong working directory produced path-only `FileNotFoundError`s for several receipt checkers; rerunning from `evidence/` resolved those and is the run counted here.
- Custom independent checker `/mnt/data/audit01/independent_audit_checks.py`, written for this audit, recomputed on fresh random small-dimensional matrices: the vectorization/partial-trace transpose convention, the two-copy orbit-block identity, the frame quotient, a positive-equal-diagonal reverse witness check, the Weyl multiplication convention, the `PureFourier` identity, and the antisymmetric symplectic-Fourier involution. It printed `PASS`; representative errors were `8.3e-17` (OB), `6.7e-16` (FR), and `2.0e-15` (`F^2=I`). These numerical checks support, but do not replace, the exact derivations below.

**Coverage limits.**

- I did **not** independently verify the external Collins–Youn, Bordenave–Collins, Fukuda, or other imported literature from primary-source copies, because those sources are not supplied as checkable source documents in this package. Those dependencies are `NOT_CHECKED` here even where historical local audits say they were web-checked.
- I did not perform an exhaustive enumeration at the frozen dimension `D=941541228773064677`; the archive itself does not do so either. Large frozen claims are exact-integer/rational calculations or analytic bounds; finite exhaustive programs are confined to explicitly small objects (e.g. the 24 orderings or primes `D=3,5,7`).
- Semantic coverage is concentrated on the proof-critical chain requested in the audit prompt; hash coverage is complete, semantic coverage of ancillary prose is not.

## 2. Executive verdict

1. **MATERIAL ERROR FOUND.** The earliest material defect is Round 2's omission of the positive-gap hypothesis from `(E1)`; the resulting `A=m, D=1` proof is literally valid but irrelevant to the full-size gate.
2. The Round 1 load-bearing algebra checked here—centered hierarchy, positive equal-diagonal duality, correlation-matrix normalization, orbit-block identity, and frame/partial-trace identities—survives.
3. `(OL1)` is only a sufficient conditional-ratio gate; it is neither the actual two-copy target nor maximum-output 2-norm multiplicativity.
4. Round 3's advertised “new” Haar scalar obstruction is valid but **REDUNDANT**; it is dominated by the rank-one Haar average.
5. Round 18 contains the first later genuinely false analytic step: the continuous `C_ind`-only Hessian omits variation of the same-line cubic and is invalid as stated.
6. Round 20's full-average no-go is underived; Round 21's `<4DM` simplification is unsupported; Round 23's claim `F^2=reflection` is false (`F^2=I`).
7. `x^(10)` is a **magnitude pseudo-candidate** only. No magnitude feasibility, linewise factorization, PSD marginal witness, or finite residual test supplies a complex physical phase lift.
8. **PW10, the all-copy gate, a positive fixed-pair regularized defect, and the full-size theorem all remain OPEN.**

## 3. Claim ledger

| ID | Source / locator | Exact material claim | Dependency | Audit action | Status | Consequence |
|---|---|---|---|---|---|---|
| C-001 | R1 response/local audit; CORE §§2–4, orbit-block section | Centered expansion of `C^⊗r` and `(P) <=> (H_r)` | `C=D0+E`, trace-annihilation | Re-derived HS orthogonality and powers of `q` | `VERIFIED` | No missing factor; lower marginals do not control the fully centered `r=3` term. |
| C-002 | R1, `(D+)` | `sup_rho ||N_r(rho)||_2 = sup_{Y in K_{q,r}} ||N_r^*(Y)||_∞` | output PSD + constant diagonal | Checked both inequalities, including maximizing-output normalized witness | `VERIFIED` | Indefinite Hermitian coefficients are unnecessary for the physical gate. |
| C-003 | R1, `(CM_r)` | Correlation-matrix form has RHS `(Aq)^(r/2)||G||_2` | C-002 and `Y=G/||G||_2` | Recomputed scaling | `VERIFIED` | Still an all-`r`, growing-cone problem; no uniformization follows. |
| C-004 | R1/R2, `(OB)` | `P_T=d_T/m + m^-2 sum_{v!=w}||C(X_vw)||_2^2` with `X_vw=T(U_w^*U_v)^T T^*` | column vectorization | Exact derivation + independent matrix test | `VERIFIED` | Transpose/adjoint/normalization are correct. |
| C-005 | R1 orbit-block positivity/rank | `[X_vw]` is PSD, equal-diagonal, rank `<=D` (or input `d`) and generated by one common `T` | physical Stinespring output | Checked as a reduced pure Stinespring state | `VERIFIED` | Cannot replace this family by an arbitrary operator-valued cone. |
| C-006 | R1 `(Rec)/(Prod)` | Uniform bounds on `kappa_s` imply `(P)`/`(WK)` | C-004 + pure-state maximizer | Checked convexity and induction | `VERIFIED` | A sufficient reduction only; the uniform bounds remain unproved. |
| C-007 | R2/R3 | Purity maximization may be restricted to pure inputs | convexity of squared HS norm | Re-derived `||tX+(1-t)Y||_2^2 <= ...` | `VERIFIED` | No illicit pure-state reduction found. |
| C-008 | R2, ratio relation | `P_T=d_T(1+R_T)/m` | C-004 | Re-derived | `VERIFIED` | Keeps the actual marginal purity `d_T`; replacing it by `p` changes the condition. |
| C-009 | R2/R3 | `(OL1): R_T<=A-1` implies actual two-copy target `(OB2)` | `d_T<=A/m` | Re-derived | `VERIFIED` | `(OL1)` is stronger than the target. |
| C-010 | R2/R3 | max-output 2-norm multiplicativity implies `(OB2)` | `p<=A/m` | Re-derived | `VERIFIED` | Multiplicativity is a different sufficient route. |
| C-011 | R2 Weyl example | Multiplicativity and `(OB2)` do not imply `(OL1)` | full Weyl example outside low-`A` regime | Checked algebra against local audit | `VERIFIED` | Prevents treating the ratio gate as equivalent to the physical target. |
| C-012 | R2 literal `(E1)` | There exists a tuple with one-copy and ratio bounds | missing Gap | Checked `A=m,D=1` witness | `VERIFIED` **only literally** | No relevance to positive defect. |
| C-013 | R2 local audit, CORE 3217–3247 | `(E1)` omitted `A^2<m^(1/m)`; corrected `(E1_gap)` is open | C-012 | Direct logical audit | `CORRECTED` / `OPEN` | Earliest material missing-hypothesis defect. |
| C-014 | R3 | Haar full-Schmidt-rank lower bound | Haar second moment | Rechecked formula | `VERIFIED` | Witness can be full rank. |
| C-015 | R3 local audit, CORE 5059–5060 | Haar-LB/HC is a new scalar obstruction | PureAvg comparison | Factored difference `((α-D)(D²-α))/(...)` | `DISPROVED` as novelty / `REDUNDANT` mathematically | Does not narrow low-`A` feasible scalar region beyond one-copy average. |
| C-016 | R3–R5 | FR/LF/PT, double-centered `Gamma_U`, Pair-energy, Comm-defect | vectorization + same tuple | Re-derived representative formulas; checked source derivations | `VERIFIED` | Correct route-specific reductions, not closure. |
| C-017 | R5 | MM and Align-Q | Gram positivity / Choi–Liouville C-S | Rechecked normalized variables | `VERIFIED` | Strictly stronger than generic `C_U<=I_U`, still insufficient. |
| C-018 | R6 | RD, centered alignment, B-rank, contraction, Unitary-Q | same-map blocks | Rechecked exact identities and reran checkers | `VERIFIED` | Scalar relaxation remains feasible. |
| C-019 | R6 Section 9 | displayed scalar system was the “strongest” centered C-S system | centered C-S | Added missing lower endpoint | `CORRECTED` | Survivor remains feasible; no theorem conclusion changes. |
| C-020 | R6 decoupled model | separate `P` and `J~` model disproves sufficiency of listed decoupled properties | intentionally omits realignment/cocycle | Checked explicit limitation | `VERIFIED` **within relaxation** | It is not an actual unitary tuple and cannot disprove `(E1_gap)`. |
| C-021 | R7 | parabolic Weyl–Sidon ordered differences are injective | odd prime `D`, selected `t_a` | Re-derived difference/sum recovery | `VERIFIED` | Gives actual one-tuple Choi frame. |
| C-022 | R7 | multiplier/additive-energy formulas and `PureFourier` | Weyl character convention | Re-derived + custom small-`D` test | `VERIFIED` | Same-map Choi/Liouville coupling is restored. |
| C-023 | R7, CORE 14185–14214 | for `q=10`, one-copy gate is equivalent to PW10 | orbit Gram identity | Re-derived `||C(rho)||_2²=(m+F_Gamma)/m²` | `VERIFIED` | PW10 is neither merely a stabilizer test nor a numerical heuristic. |
| C-024 | R7 stabilizer line | line formula `||L(rho_l)||_2²=(m+N_l)/m²` | stabilizer characteristic support | Re-derived convention | `VERIFIED`, `NECESSARY-ONLY` | Passing every line cannot establish PW10. |
| C-025 | R7 freeze wording | “fully frozen” tuple without tie-break | existential prime choices | Checked quantifiers | `CORRECTED` | Canonical least-prime tie-break repairs it without altering existence. |
| C-026 | R8 | WR10 Hermitian Weyl-polynomial estimate is equivalent to PW10 | HS projection duality | Checked both directions | `VERIFIED` | It is a coordinate reformulation, not a logically smaller theorem. |
| C-027 | R8/R9 | Bell weights / horizontal fibers alone certify PW10 | physical rank-one constraints omitted | Rechecked relaxation | `DISPROVED` / `NECESSARY-ONLY` | Relaxed high-eigenvalue or fiber configurations are not physical states. |
| C-028 | R9 | phase-blind constant-10 absolute-moment sufficient condition holds for frozen tuple | discarded Weyl phases | reran exact checker | `DISPROVED` | Failure does not disprove PW10. |
| C-029 | R10 | subresultant route produces a usable certificate | degree-`m` Bezout identity | inspected local audit | `SUFFICIENT-ONLY`, `OPEN` | Only a certificate schema was given; no certificate produced. |
| C-030 | R10 | Perron-Schur route is a smaller verification problem | matrix domination | scope audit | `CORRECTED / OVERSTATED` | Sufficiency is valid, but frozen verification is not made small. |
| C-031 | R11 | LC plus magnitude-only TriGram suffices | magnitude relaxation | exact half-point | `DISPROVED` | Necessitates stronger/global constraints. |
| C-032 | R11 | SF/ConvMag exclude the specific half-point | self-Fourier magnitude identity | checked | `VERIFIED`, `NECESSARY-ONLY` | Does not prove PW10. |
| C-033 | R12 | strengthened magnitude relaxation admits objective `>10` | `x*` construction | exact rational checker | `VERIFIED` **as relaxation feasibility** | Explicitly no phase lift. |
| C-034 | R13, CORE 25584–25623 | `x^(10)=b+(10/M)d` satisfies frozen magnitude constraints and objective `>10` | magnitude-only SF/LC/TriGram/ConvMag | reran exact checkers | `VERIFIED` | `x^(10)` is a pseudo-candidate, not a physical state. |
| C-035 | R13 | under Hermiticity/trace/purity hypotheses, physical phase lift `<=> C(alpha)=1 <=> rank-one projector | Weyl expansion | Re-derived spectral defect logic | `VERIFIED` | Correct exact phase-lift gate. |
| C-036 | R13 | real nonnegative phase of `x^(10)` is physical | parity witness | checked | `DISPROVED` | Only that phase is excluded; complex phases remain. |
| C-037 | R14 | character orbit/sign-phase examples exclude all phases | finite/measure subsets only | scope audit | `DISPROVED` as global inference; stated response does not make it | No phase-uniform gap. |
| C-038 | R14 | residual Parseval/SOS normalization | Weyl coefficients | checker + derivation | `VERIFIED` | A residual for one phase assignment does not bound all phases. |
| C-039 | R15 | stabilizer line/projector and Radon formulas | projective line decomposition | reran checkers | `VERIFIED`, `NECESSARY-ONLY` | Strict line-shadow positivity is not spectral factorization. |
| C-040 | R15 | linewise feasibility would imply physicality | cross-line phases omitted | explicit `Z/5Z`/later constructions | `DISPROVED` | Cross-line compatibility is load-bearing. |
| C-041 | R16 | all frozen line shadows lie in convex hull of nonnegative autocorrelations | line convex-hull theorem | reran checker | `VERIFIED` | Eliminates circulant copositive linear-separator route but does not construct factors. |
| C-042 | R17 | every frozen line has a strictly positive cyclic probability factor | Fourier-floor/random-sign argument | exact checker rerun | `VERIFIED` | Closes one-dimensional line-factor gate only. |
| C-043 | R17 | complete stabilizer-projector layer suffices for physicality | independent line phases | constructed stabilizer-positive nonphysical field | `DISPROVED` | Strong direct evidence that linewise feasibility cannot be promoted. |
| C-044 | R18 | complete-MUB residual SOS / designated cross-basis 2x2 system characterizes physicality under standing hypotheses | complete stabilizer MUB | checked formulas | `VERIFIED` **as equivalence/repackaging** | Not a phase-free lower bound. |
| C-045 | R18, CORE 35068–35075, 35261–35294 | continuous `C_ind`-only Hessian gives necessary conditions | assumes `C_dep` invariant on continuous path | explicit same-line triple | `DISPROVED` / `CORRECTED` | First later false analytic step; replace with discrete finite differences/full Hessian. |
| C-046 | R19 | corrected full Hessian and discrete line-shift fourth-moment decomposition | includes same-line terms | reran checkers | `VERIFIED` | Same-line fourth moments remain phase-sensitive. |
| C-047 | R19 | average residual near one gives pointwise gap | mean only | checked quantifiers | `DISPROVED` | No phase-uniform residual gap. |
| C-048 | R20 | `SingleLineSOS` positive gap | assumes an unshifted physical lift | rechecked exact formula | `VERIFIED`, `CONDITIONAL` | Does not exclude the lift itself. |
| C-049 | R20, CORE 39192 | full two-line shift average necessarily retains uncancellable phase data | only one component averaged in response | source audit | `NOT_PROVED` / `CORRECTED` | Underived no-go cannot be used. |
| C-050 | R20 | DifferenceFrame identity and product-vector PW10 form | Sidon difference frame | checker rerun | `VERIFIED` | Unrestricted operator norm would be too large a cone. |
| C-051 | R21 | full two-line average, rank-two displacement, global quartic contraction, anti-projector symmetry | physical projector algebra | reran four checkers | `VERIFIED`, `NECESSARY-ONLY` | Does not select physical branch or prove PW10. |
| C-052 | R21 | `sqrt(8) D sqrt(lambda_z^2+M^2+6M) < 4DM` from `|lambda_z|<=M` | envelope only | direct substitution | `DISPROVED` / `CORRECTED` | Correct envelope is `4DM sqrt(1+3/M)>4DM`; still far too weak to matter. |
| C-053 | R22 | centered idempotence, orbit/external split, diagonal/swap/genuine-cycle energy decomposition | exact Weyl bookkeeping | checker rerun | `VERIFIED` | Leaves external cubic phases and genuine 4-phase cycles unrestricted. |
| C-054 | R22 | those decompositions independently certify PW10 | they are contractions/components of idempotence | scope audit | `DISPROVED` as promotion / response correctly avoids promotion | No threshold bound is produced. |
| C-055 | R23 | edge identity strengthens to `F d_h=d_h` | centered idempotence + Hermiticity | derived and small-prime checked | `VERIFIED` | Strong necessary edge constraint. |
| C-056 | R23, CORE 45512–45530 | antisymmetric symplectic `F^2` is phase-space reflection | Fourier kernel antisymmetric | exact double-sum | `CORRECTED`: `F^2=I` | Evenness must come from Hermiticity, not Fourier squaring. |
| C-057 | R23 | analytic `K^(h)` solves edge phase problem | rank-relaxed two-basis marginals | rank/support audit | `NECESSARY-ONLY / TOO WEAK` | Mixed PSD witness is not a pure `+1`-eigenvector. |
| C-058 | R23 | separate edge solutions imply global phase field | rank-one cross-edge cycles omitted | reconstructed `Y_{a,b}` | `OPEN` | Cross-edge consistency is an additional load-bearing condition. |
| C-059 | R23, CORE 45548–45561 | existence of prescribed-magnitude even `+1` Fourier edge vector; then common cross-edge assembly | C-055 | no construction/exclusion found | `OPEN / earliest gap` | Earliest sharpened Round-23 branch gap. |
| C-060 | R7–R23 | PW10 for exact frozen tuple | C-023 plus physical characteristic constraints | audited all relaxations | `OPEN` | No physical violating state and no uniform upper bound. |
| C-061 | R3–R23 | finite `r=2` low-`A` `(E1_gap)` | PW10 plus later all-`T` ratio work | chain audit | `OPEN` | PW10 alone would only settle one-copy part for the candidate. |
| C-062 | R1 | one frozen tuple satisfies `(P)` or admissible `(WK)` for every copy and entangled input | all-copy same-tuple quantifier | no proof/counterexample | `OPEN` | No fixed regularized defect follows. |
| C-063 | R1 downstream | `(P)/(WK)` implies positive fixed-pair regularized MOE defect | entropy `S>=S2`, complementarity, Bell witness | algebra checked; imported existence not supplied | `CONDITIONAL` | Antecedent remains open. |
| C-064 | R1 imported transfer/strong-convergence literature | stated Collins–Youn / Bordenave–Collins / Fukuda hypotheses and source claims | external literature | source documents absent | `NOT_CHECKED` | Not used to promote any open target in this audit. |
| C-065 | global target | fixed regularized defect / all-copy gate / full-size MOE-Holevo theorem | C-061–C-064 | dependency audit | `OPEN` | No later finite-slope or ansatz result changes baseline status. |

## 4. Detailed findings

### F-001 — HIGH — Round 2 omitted the positive-gap hypothesis

**Source locator.** CORE 3217–3247; `outputs/round-02-local-audit.md` §Verdict / §Corrected next gate.

**Finding.** `(E1)` was stated without the inherited condition

\[
A^2<m^{1/m}\quad\Longleftrightarrow\quad \frac{\log_2m}{m}>2\log_2 A.
\]

The response chooses

\[
A=m,\qquad D=1,
\]

so the universal channel-purity bound `p_1<=1=A/m` and universal frame bound `kappa_1<=m-1=A-1` make literal `(E1)` true. But for `m>1`,

\[
A^2=m^2>m^{1/m},
\]

so the witness is maximally outside the positive-defect regime.

**Minimal correction.** Replace `(E1)` by `(E1_gap)` with `A^2<m^(1/m)` included in the same existential quantifier block. This is exactly what Round 3 does.

**Consequence.** Round 2's literal `PROVED` result is not progress on the intended finite physical gate. Rounds 3–23 are not invalidated because they explicitly use the repaired low-`A` condition.

### F-002 — MEDIUM — Round 3's Haar-LB novelty was overstated

**Source locator.** CORE 5034–5060 and 5174–5218; `outputs/round-03-local-audit.md` §Redundancy check.

Let

\[
q_{\rm pure}=\frac{\alpha+D}{D(D+1)},\qquad
q_{\rm full}=\frac{\alpha^2+D^2}{D^2(\alpha+1)}.
\]

Direct common-denominator subtraction gives

\[
q_{\rm pure}-q_{\rm full}
=\frac{(\alpha-D)(D^2-\alpha)}{D^2(D+1)(\alpha+1)}.
\]

In the feasible low-`A` regime, `D<alpha<D^2`, so this is nonnegative. Therefore the rank-one Haar-average consequence of `p<=A/m`, namely `m q_pure<=A`, already implies the Round-3 full-rank quadratic condition `m q_full<=A`.

**Minimal correction.** Keep Haar-LB as a valid full-Schmidt-rank witness statement, but mark its scalar obstruction `REDUNDANT` and retract “new necessary scalar obstruction.” Round 4 does so.

### F-003 — LOW/MEDIUM — Round 6's “strongest scalar system” omitted one side of centered Cauchy–Schwarz

**Source locator.** CORE 12053–12067; `outputs/round-06-local-audit.md` §Scalar-survivor audit.

For centered positive blocks `B,P` on the `n`-dimensional traceless space,

\[
\left|x-\frac{uv}{n}\right|
\le
\sqrt{\left(a-\frac{v^2}{n}\right)
      \left(b-\frac{u^2}{n}\right)}.
\]

Round 6 retained the upper endpoint but omitted

\[
x\ge \frac{uv}{n}-
\sqrt{\left(a-\frac{v^2}{n}\right)
      \left(b-\frac{u^2}{n}\right)}.
\]

**Minimal correction.** Include the companion lower bound. For the displayed scalar survivor its lower endpoint is negative, so `x=0` still satisfies the corrected system. Thus the “strongest” descriptor was false, but the survivor and OPEN verdict survive.

### F-004 — HIGH (route-local) — Round 18's continuous `C_ind`-only Hessian is invalid

**Source locator.** CORE 35068–35075 and 35261–35294; `outputs/round-18-local-audit.md` §Rejected continuous Hessian step.

The response differentiated a continuous balanced-representative line phase while treating the same-line cubic `C_dep` as invariant. That invariance holds for the finite field-character shifts, not for the proposed continuous deformation.

A concrete same-line zero-sum triple uses balanced representatives

\[
t=(D-1)/2,
\qquad (t,t,1),
\]

whose integer sum is `D`. Under the continuous line phase its monomial gains `e^{iD theta_L}`, so `C_dep` changes. Hence stationarity of total `C=C_dep+C_ind` does **not** imply stationarity/Hessian conditions for `C_ind` alone.

**Minimal correction.** Replace the continuous `C_ind` Hessian by the discrete maximum/finite-difference conditions, or use the Round-19 full fixed-magnitude Hessian including same-line terms.

**Consequence.** Any Round-18 conclusion depending on equations (10.1)–(10.2) as necessary conditions is invalid. Round 19 explicitly repairs this, so later corrected identities are not invalidated.

### F-005 — MEDIUM — Round 20's “full average still retains phase dependence” no-go was underived

**Source locator.** CORE 39170–39192; `outputs/round-20-local-audit.md` §Two-line plaquette.

The exact two-line plaquette expansion is correct, but the response averaged only one component and asserted that the remaining higher terms behave similarly. That does not exclude cancellation after the **complete** double cyclic average.

**Minimal correction.** Keep the exact plaquette formula; delete the no-cancellation/no-go conclusion until the full average is computed. Round 21 performs the complete average and correctly leaves explicit KD/Bargmann data without claiming an impossibility theorem.

### F-006 — MEDIUM — Round 21's `<4DM` simplification is false from the stated envelope

**Source locator.** CORE 41470–41494; `outputs/round-21-local-audit.md` §Weighted coefficient extraction.

From only `|lambda_z|<=M`,

\[
\sqrt 8\,D\sqrt{\lambda_z^2+M^2+6M}
\le 4DM\sqrt{1+3/M},
\]

and the factor `sqrt(1+3/M)` is strictly greater than one. Thus `<4DM` does not follow.

**Minimal correction.** Use the valid slightly larger envelope, or prove a sharper bound for the particular `lambda_{z_*}`. The corrected envelope remains astronomically larger than the desired right side, so no qualitative result changes.

### F-007 — LOW — Round 23's Fourier-square statement is wrong

**Source locator.** CORE 45512–45530; `outputs/round-23-local-audit.md` §CORRECTED.

For

\[
(\mathscr Ff)(k)=D^{-1}\sum_p f(p)\omega^{[p,k]},
\]

antisymmetry gives

\[
\begin{aligned}
(\mathscr F^2f)(\ell)
&=D^{-2}\sum_{p,k}f(p)\omega^{[p,k]+[k,\ell]}\\
&=D^{-2}\sum_{p,k}f(p)\omega^{[p-\ell,k]}\\
&=f(\ell).
\end{aligned}
\]

So `mathscr F^2=I`, not reflection. The custom checker and archived Round-23 PSD checker both reproduce this at `D=3,5,7`.

**Minimal correction.** Derive evenness of `d_h` directly from Hermiticity `alpha_{-z}=conj(alpha_z)`. The valid eigenvector identity `F d_h=d_h` remains intact.

### F-008 — CRITICAL BOUNDARY — `x^(10)` is magnitude-feasible, not physically liftable by construction

**Source locator.** CORE 25584–25623 and 25740–25749; R13 response §1/§phase-lift criterion; R20 local audit 39110–39112.

The frozen point

\[
x^{(10)}=b+\frac{10}{M}d
\]

is verified to be real, even, self-Fourier, normalized with `x_0=1`, positive on nonzero labels, feasible for the audited magnitude relaxation, and to have the frozen objective strictly above `10`.

Those facts determine `|alpha_z|`, not a globally compatible phase field. Under the exact Hermiticity/trace/purity normalization, a phase field is physical iff

\[
C(\alpha)=\operatorname{Tr}R_\alpha^3=1,
\]

because

\[
1-C(\alpha)=\sum_j \mu_j^2(1-\mu_j)\ge0
\]

for the Hermitian `R_alpha` with `Tr R=Tr R^2=1`; equality forces a rank-one projector. The real nonnegative phase, all affine-character phases, and several sign/line constructions are nonphysical, but that does not exclude all complex phases.

**Minimal correction.** Always label `x^(10)` a **pseudo-candidate of unresolved physical liftability**. No statement about its magnitude feasibility may be promoted to a PW10 counterexample.

### F-009 — CRITICAL BOUNDARY — linewise feasibility does not imply cross-line phase compatibility

**Source locator.** R15–R17 local audits; CORE 33366–33397.

Round 17 proves each frozen projective-line shadow has a strictly positive cyclic probability factor, even simultaneously enough to pass every stabilizer-projector inequality. The same round also constructs a field with the exact magnitudes `x^(10)` that passes that full stabilizer layer but has `C(alpha)<1`.

Therefore line-by-line spectral factorization/stabilizer positivity is **not sufficient** for global physicality. This is an explicit logical separation, not just lack of proof.

**Minimal correction.** Any use of linewise feasibility must add cross-line rank-one/idempotence compatibility. This blocks any promotion from Rounds 15–17 to PW10.

### F-010 — HIGH BOUNDARY — residual SOS and cross-basis tests are equivalences/repackagings, not phase-free certificates

**Source locator.** R18/R19 local audits; CORE 35151–35230, 37550–37570.

The complete MUB residual identity

\[
\sum_{L,k}\delta_{L,k}^2=\operatorname{Tr}(R_\alpha^2-R_\alpha)^2
\]

and the designated cross-basis `2x2` conditions correctly characterize physicality under the stated standing hypotheses. But an equivalence to the original idempotence gate does not itself supply a positive lower bound uniformly over the phase torus with fixed `x^(10)`.

**Minimal correction.** Classify these as `VERIFIED` equivalent repackagings; keep the phase-uniform residual gap `OPEN`.

### F-011 — HIGH BOUNDARY — Round 23 edge marginals remain a rank relaxation

**Source locator.** CORE 45460–45508 and 45538–45561.

For each nonzero edge `h`, the analytic matrix

\[
K^{(h)}=\operatorname{Diag}(q_h)+F^*\operatorname{Diag}(q_h)F-N^{-1}I
\]

is correctly shown PSD with the requested two basis marginals. This proves feasibility of a **mixed** two-basis marginal relaxation. It does not prove existence of a vector `d_h` that is simultaneously

1. in the `+1` eigenspace of the symplectic Fourier transform,
2. even/Hermitian-compatible, and
3. has the prescribed squared magnitudes.

Even separate pure edge vectors must then satisfy the common rank-one cross-edge cycle

\[
Y_{a,b}Y_{b,c}=x_bY_{a,c}
\]

and centered idempotence.

**Minimal correction.** Keep the PSD witness `NECESSARY-ONLY / TOO WEAK`; do not promote separate edge feasibility to a global phase lift.

### F-012 — HIGH BOUNDARY — ratio, multiplicativity, and the actual two-copy target are distinct

**Source locator.** R2/R3; CORE 2237–2415 and local audit 3236–3247.

For a pure two-copy input encoded by `T`, let

\[
d_T=\|C(TT^*)\|_2^2,\qquad P_T=\|(C\otimes C)(\Psi_T)\|_2^2.
\]

Then exactly

\[
P_T=\frac{d_T}{m}(1+R_U(T)).
\]

Thus:

- ratio gate `(OL1)`: `R_U(T)<=A-1`;
- max-output multiplicativity: `R_U(T)<=mp^2/d_T-1`;
- actual target `(OB2)`: `R_U(T)<=A^2/(m d_T)-1`.

With `d_T<=p<=A/m`, both `(OL1)` and multiplicativity imply `(OB2)`, but they are not equivalent. The Weyl example gives multiplicativity and `(OB2)` with failure of `(OL1)`. When `p=A/m`, `(OL1)` implies multiplicativity; for strict slack that implication was not proved.

**Minimal correction.** Never replace the denominator `d_T` by `p` inside an equivalence and never call a failure of `(OL1)` a failure of `(OB2)`.

### F-013 — HIGH BOUNDARY — positive equal-diagonal duality is exact, but it does not solve same-tuple/all-copy control

**Source locator.** R1 `(D+)` and `(CM_r)`; CORE 523–658.

Every physical output `X=N_r(rho)` is PSD, trace one, and has constant diagonal `1/n`. For

\[
\alpha_r=\sup_\rho\|N_r(\rho)\|_2,
\]

Cauchy–Schwarz gives, for every positive equal-diagonal `Y` with `||Y||_2=1`,

\[
\|N_r^*(Y)\|_\infty\le\alpha_r.
\]

Conversely, if `rho_*` maximizes output norm, then

\[
Y_*=N_r(\rho_*)/\alpha_r
\]

belongs to the same cone and

\[
\|N_r^*(Y_*)\|_\infty\ge
\operatorname{Tr}(Y_*N_r(\rho_*))=\alpha_r.
\]

Both directions are exact. Writing `Y=G/||G||_2` gives the stated correlation-matrix inequality with RHS `(Aq)^{r/2}||G||_2`.

**Consequence.** The reduction legitimately removes indefinite coefficients, but the cone still grows with `r` and all copies use the same frozen tuple. No finite-net/fixed-`r` result supplies the required `exists U forall r forall rho` quantifier.

### F-014 — `NOT_CHECKED` — imported theorem dependencies are not source-verified in this package audit

**Source locator.** R1 external references and historical local-audit “primary-source checks.”

The package quotes claims attributed to Collins–Youn, Bordenave–Collins, and Fukuda, but it does not include the primary source texts as checkable evidence. Under the master protocol, these dependencies are `NOT_CHECKED` here. In particular I do not use historical claims of web verification to promote a theorem.

**Consequence.** This does not weaken the negative/open verdict: the full-size theorem already fails to close at the internal PW10 / `r=2` / all-copy gates before those transfers could matter.

## 5. Dependency/invalidation map

| Finding / checked interface | Immediate dependency | Downstream effect |
|---|---|---|
| F-001 Round-2 missing Gap | literal `(E1)` only | Invalidates only the claimed relevance of Round 2's `PROVED` witness. Rounds 3–23 use repaired `(E1_gap)`. |
| F-002 Haar-LB redundancy | Round-3 “new obstruction” narrative | Removes novelty/strength claim; does not invalidate the formula or later work. |
| F-003 missing lower centered-C-S bound | Round-6 “strongest scalar system” label | Corrected system still has the displayed survivor; no downstream closure is lost. |
| F-004 false continuous Hessian | Round-18 equations (10.1)–(10.2) and any `C_ind`-only stationarity consequence | Those consequences are invalid. Round 19's full Hessian/discrete conditions supersede them. |
| F-005 underived full-average no-go | one Round-20 no-cancellation sentence | Round-20 exact plaquette survives; Round 21 recomputes the full average. |
| F-006 false `<4DM` simplification | one Round-21 coefficient envelope | Replace constant by `4DM sqrt(1+3/M)`; still no obstruction, so final status unchanged. |
| F-007 `F^2` correction | Round-23 evenness justification | `F d_h=d_h` survives; evenness comes from Hermiticity. |
| C-004/C-013 orbit-block and D+ reductions | Rounds 1–6 physical-gate route | **If either failed**, the physical two-copy/all-copy reductions and all later attempts to solve them through these coordinates would lose their claimed connection. They were independently checked here. |
| C-023 PW10 equivalence | Rounds 7–23 | **If this failed**, all R8–R23 PW10 work would cease to address the one-copy gate. It was independently checked. |
| C-035 phase-lift equivalence | Rounds 13–23 `x^(10)` branch | **If this failed**, cubic/residual/phase-lift conclusions would be invalid. Its spectral derivation checks. |
| F-009 linewise insufficiency | Rounds 15–17 | Prevents any promotion from single-line or complete stabilizer feasibility to physical lift/PW10. |
| F-010 residual-SOS equivalence without gap | Rounds 18–22 | Prevents treating a reformulation of idempotence as an independent phase-uniform certificate. |
| F-011 edge rank relaxation | Round 23 | Prevents rank-relaxed marginal feasibility from becoming a pure edge solution or global lift. |
| PW10 remains OPEN | one-copy gate of exact R7 tuple | All later finite `r=2` ratio work requiring that one-copy bound remains conditional. |
| finite `r=2` `(E1_gap)` remains OPEN | fixed finite physical gate | No finite same-tuple two-copy ratio theorem is obtained. |
| all-copy `(P)/(WK)` remains OPEN | fixed-pair regularized defect | No positive regularized defect for a fixed finite pair is established. |
| fixed regularized defect remains OPEN | full-size outer-power construction | Full-size extensive MOE theorem does not follow. |
| MOE-to-Holevo imports `NOT_CHECKED` | final transfer | Cannot be used here as an independently verified final promotion even if upstream gates were solved. |

**Later themes invalid if an earlier reduction failed.** Specifically: failure of the orbit-block/D+ layer would invalidate the R2–R6 physical-ratio program; failure of the Weyl–Sidon/PureFourier equivalence would invalidate R8–R23 as work on the one-copy gate; failure of the R13 phase-lift theorem would invalidate the use of `C(alpha)=1`, idempotence residuals, line/projector tests, MUB SOS, and edge equations as physical-lift criteria; failure of the stabilizer/MUB identities would invalidate R15–R23 line/residual decompositions. None of those checked interfaces failed in this audit.

## 6. Computational audit

### 6.1 Reproducibility and receipts

- Archive manifest: **229/229 exact byte-size and SHA-256 matches**.
- Archived verifier programs: **46/46** `verify_round*.py` files from Rounds 9–23 compiled and executed successfully from the correct working directory.
- Several checkers intentionally report limitations while exiting successfully. In particular:
  - Round 20 checker reports: `full-average no-go is underived; candidate wording overclaims`.
  - Round 21 checkers report: the generic `<4DM` simplification is unsupported.
  - Round 23 checker reports: `symplectic Fourier square is identity, not reflection`.
  Their success means the checker detected the documented correction; it is not evidence that the historical response was error-free.

### 6.2 Arithmetic / overflow

The frozen large-integer checkers use Python arbitrary-precision integers, `fractions.Fraction`, or high-precision `Decimal` for load-bearing inequalities. I found no 64-bit truncation or wraparound path. Floats are used predominantly in small-prime matrix smoke tests or to print decimal approximations after exact inequalities have already been asserted. No material frozen conclusion in the checked scripts depends on an IEEE-754 comparison at the giant dimension.

### 6.3 Enumeration coverage

- The scripts do **not** enumerate `D^2`, `D^4`, the entire phase torus, all physical states, or all `T`; nor do the prose claims validly say they do.
- Small-prime tests at `D=3,5,7` check signs, transposes, cocycles, and matrix identities only. They are convention checks, not extrapolating proofs.
- The Round-19 “24-ordering” computation genuinely enumerates the finite set of 24 permutations relevant to that local fourth-order contraction; it does not enumerate all phase assignments.
- Round-20/21 quotient checks exhaust explicitly small finite quotient models where stated; they do not enumerate the frozen quotient.
- The Round-17 all-line existence proof is analytic/probabilistic with exact union-bound arithmetic; it is not an enumeration of all signs. The local audit correctly calls it an existence proof rather than an explicit sign list.

### 6.4 Code/object correspondence

The principal object-correspondence checks passed:

- Round 12/13 scripts manipulate the advertised **magnitude relaxation** and do not silently solve phase lifting.
- Round 15–17 scripts manipulate line shadows/autocorrelations and stabilizer projectors; the local audits explicitly separate those from global rank-one physicality.
- Round 18/19 scripts distinguish the invalid continuous `C_ind` Hessian from the corrected full/discrete formulas.
- Round 20/21 scripts retain unresolved KD/Bargmann terms rather than numerically substituting missing phases.
- Round 22 scripts check contractions/components of centered idempotence, not an independent certificate.
- Round 23 scripts check edge Fourier/autocorrelation and a rank-relaxed PSD witness; they do not claim a rank-one edge vector.

### 6.5 Independent reconstruction performed in this audit

The custom checker is supplementary to exact paper derivations. It directly confirmed:

1. `Tr_A[(A⊗I)|psi_T><psi_T|]=T A^T T^*`;
2. `(OB)` with all factors of `m`;
3. the frame quotient `(FR)`;
4. the equal-diagonal normalization of the dual witness `Y=N(rho)/||N(rho)||_2`;
5. the Weyl product convention and `PureFourier` identity for a small parabolic tuple;
6. `mathscr F^2=I` for the antisymmetric symplectic kernel.

These tests were performed on fresh matrices not stored in the evidence archive.

## 7. Corrected status ledger

### `VERIFIED`

- Round-1 centered hierarchy, positive equal-diagonal duality, all-copy correlation-matrix normalization, orbit-block formula, frame formula, and partial traces.
- Pure-state reduction by convexity and the distinction among `(OL1)`, multiplicativity, and `(OB2)`.
- Round-4/5 pair-energy, commutator-defect, Choi/Liouville dictionary, MM, and alignment bounds.
- Round-6 RD/centered-alignment/B-rank/contraction/Unitary-Q identities and existence of a surviving scalar/decoupled relaxation.
- Round-7 Weyl–Sidon tuple, Choi frame, multiplier/additive-energy formulas, `PureFourier`, stabilizer-line formula, and exact equivalence of the one-copy gate to PW10 at `q=10`.
- Round-8 exact WR10/PW10 duality.
- Round-9/10 restricted physical-state/fiber formulas at their stated necessary/sufficient scope.
- Round-12/13 exact magnitude pseudo-candidates and the exact phase-lift criterion.
- Round-14 sign/character witnesses and residual normalization at their stated scope.
- Round-15/16/17 line-shadow/autocorrelation identities, all-line factor existence, and explicit insufficiency of the stabilizer layer.
- Round-18 MUB residual SOS and cross-basis equivalence after removing the false continuous-Hessian step.
- Round-19 corrected full-Hessian/fourth-moment bookkeeping.
- Round-20 conditional single-line gap, exact plaquette, quotient symmetries, and DifferenceFrame identity.
- Round-21 complete two-line average, rank-two identities, quartic contraction, anti-projector symmetry, and corrected coefficient bounds.
- Round-22 centered idempotence and orbit/external plus quartic decompositions.
- Round-23 edge Fourier eigenvector identity, centered edge formula, autocorrelation identity, rank-relaxed PSD witness, and cross-edge rank-one cycle formula.

### `CORRECTED`

- Round 2: add the positive-gap hypothesis to get `(E1_gap)`.
- Round 3: Haar-LB/HC is not a new scalar obstruction; it is dominated by PureAvg.
- Round 6: add the missing lower centered-Cauchy endpoint; do not call the displayed scalar list “strongest.”
- Round 7: canonical tie-breaking is needed before calling the parametric Weyl–Sidon family “fully frozen.”
- Round 10: FiveCarry was not disproved; subresultant was a schema, not a produced certificate; Perron-Schur was not a smaller frozen verification problem.
- Round 14: existential sign field is not an explicit sign vector; collective residual vanishing is equivalent, individual residual equations are merely necessary.
- Round 16: all-line convex-hull theorem supersedes the proposed exceptional copositive-separator search.
- Round 18: reject the continuous `C_ind`-only Hessian; use discrete/full Hessian.
- Round 20: reject the underived full-average no-cancellation claim.
- Round 21: replace `<4DM` by a valid larger envelope unless a sharper `lambda_{z_*}` bound is proved.
- Round 23: `mathscr F^2=I`; derive evenness from Hermiticity.

### `REDUNDANT`

- Round-3 HC as a low-`A` scalar obstruction.
- Round-5/Round-6 weaker scalar relaxations already implied by PureAvg/stronger alignment constraints.
- Round-6 RD-PT2 versus uncentered alignment (`x<=(a+b)/2` is weaker than `x<=sqrt(ab)`).
- Many line/fiber/marginal tests once exact stronger equivalences are introduced; they remain valid necessary tests but do not improve the global status.

### `DISPROVED`

- Sufficiency of the literal Round-2 result for positive defect.
- Sufficiency of LC plus magnitude-only TriGram.
- Phase-blind absolute-moment constant-10 condition for the frozen tuple.
- Sufficiency of linewise/stabilizer positivity for physicality.
- Round-18 `C_ind`-only continuous Hessian as a necessary condition.
- Any inference from average/RMS residual size to a pointwise phase-uniform gap without an additional theorem.
- Round-21 `<4DM` inequality from the stated envelope.
- Round-23 “symplectic Fourier square equals reflection” statement.

### `NECESSARY-ONLY` / `SUFFICIENT-ONLY`

- Stabilizer lines, finite support/fiber tests, line projectors, local Gram minors, parity caps, rank-two displacement contractions, and edge marginal polygon tests are necessary-only unless an explicit equivalence is proved.
- `(OL1)` and the uniform `kappa_s` bounds are sufficient gates stronger than the corresponding physical purity targets.
- The uninstantiated subresultant/Bezout and Perron-Schur conditions are sufficient-only and unproved for the frozen tuple.

### `NOT_CHECKED`

- Primary-source theorem claims attributed to Collins–Youn, Bordenave–Collins, Fukuda, and any external literature not supplied as a source document in this package.

### `OPEN`

- A complex physical phase lift of `x^(10)`; equivalently, whether its phase-uniform defect can vanish.
- A positive phase-uniform residual/cubic gap for `x^(10)` if no lift exists.
- Existence of some other objective-above-10 magnitude profile with a physical lift.
- PW10/WR10 for the exact frozen Weyl–Sidon tuple.
- The full one-copy bound for that tuple insofar as it is equivalent to PW10.
- The uniform all-`T` finite `r=2` low-`A` gate `(E1_gap)`.
- The all-copy physical-output purity gate `(P)` or admissible `(WK)` for one frozen finite tuple.
- A positive regularized MOE defect for one fixed finite pair.
- The Hayden–Penington full-size extensive MOE/Holevo theorem.

## 8. First remaining unknown

There are two levels of “earliest” that must not be conflated.

**Global proof-chain level.** The earliest unresolved statement after the repaired Round-2 specification is still a physical one-copy/two-copy gate. For the concrete Round-7 Weyl–Sidon route, the one-copy part is exactly

\[
\boxed{
\sup_{\rho\ \mathrm{pure}}
\sum_{g\in\Gamma}
|\operatorname{Tr}(W_g^*\rho)|^2\le10
}
\qquad\text{(PW10).}
\]

No Round 8–23 argument proves it or constructs a physical violating state. Even a proof that the single pseudo-profile `x^(10)` has no lift would not prove PW10, because another physical magnitude profile could violate it.

**Earliest sharpened unknown at the end of Round 23, within the `x^(10)` branch.** For a selected nonzero edge `h`, the exact edge equations require an even `+1` symplectic-Fourier eigenvector `d_h` with the prescribed squared magnitudes. It is unknown whether such a vector exists. If separate edge vectors do exist, it is additionally unknown whether they assemble into one Hermitian rank-one coefficient matrix satisfying

\[
Y_{a,b}Y_{b,c}=x_bY_{a,c}
\]

and centered idempotence simultaneously. The analytic PSD matrix `K^(h)` settles only a mixed rank-relaxation and therefore does not answer this question.

That is the first exact Round-23 branch gap. It is **not** a replacement for PW10 and must not be promoted to an equivalent global gate.

## 9. Final audit verdict

**MATERIAL ERROR FOUND**

The package contains material missing-hypothesis/overclaim and analytic errors—most importantly the Round-2 omission of the positive-gap condition and the Round-18 invalid continuous `C_ind`-only Hessian—plus smaller corrected defects in Rounds 6, 20, 21, and 23. The local audits generally identify and quarantine these errors; I found no checked instance where a corrected restricted or magnitude/linewise result validly promotes PW10 or any global target.

Within the checked scope, the principal load-bearing reductions from the physical problem to the orbit-block/frame formulations, the Weyl–Sidon one-copy PW10 formulation, and the magnitude/phase-lift separation survive the independent checks described above. That does **not** prove any open gate.

**The full-size theorem remains OPEN.** This audit has not supplied, and the package does not contain within the checked chain, a complete line-by-line proof of every required global step: PW10 remains open for the frozen tuple, the uniform finite `r=2` physical ratio gate remains open, the same-tuple all-copy gate remains open, and therefore a positive fixed-pair regularized defect and the Hayden–Penington full-size extensive theorem remain open.
