# KSUM STAGE 3 — Module anatomy of the σ-twist: does Rosmanis's ED adversary adapt to 2-Sum?

**Date:** 2026-07-16. **Executor/verifier:** Opus 4.8 (all computation, all cross-checks). **Strategist:** Fable 5 (registered predictions only; refuting them is a valued outcome — see the scorecard in §7). **Protocol:** `KSUM_SMALL_G_COMMISSION.md` §6 Stage 3; context `KSUM_STAGE0_VERDICT.md`. **Every number below carries a provenance triplet** (command, log, script SHA‑256) in §9, and every claim is labelled **PROVED / NUMERICAL / CONJECTURED / OPEN**.

---

## 0. The one thing that makes the whole computation cheap (stated so it can be checked)

For 2‑Sum over an abelian group `G`, `|G|=q`, target `t`, the collision relation at `k=2` is `x_j = σ(x_i)` with `σ(x)=t−x`, an **involution** on `G` with `τ = #{x:2x=t}` fixed points and `m=(q−τ)/2` transpositions. Both `D_0` (legal strings) and the symmetry group `Γ = S_n × C`, `C = C_{Sym(G)}(σ)`, depend on `G` **only through the graph of σ**, i.e. only through σ's cycle type `1^τ 2^m`. The group operation never enters `D_0`'s definition (`no i≠j with x_j=σ(x_i)`) or `Γ`'s action. Hence **every T1–T4/T6 quantity is a function of `(n, τ, m)` alone** (this is exactly the C7 covariance proved at `k=2` in `KSUM_STAGE0_VERDICT.md §3.3`). I therefore realise σ abstractly (fixed points `0..τ−1`, then transpositions `(τ,τ+1),…`) and confirm `|C| = τ!·2^m·m!` at every cell. **PROVED** (the covariance is the C7 theorem; `|C|` matches the formula at all 10 groups touched, `T1`/`T3` logs).

The grid cells `(q,τ)` map to `(τ,m)`: (3,1)→τ1m1, (4,0)→τ0m2, (4,2)→τ2m1, (5,1)→τ1m2, (8,0)→τ0m4, (8,2)→τ2m3, (8,4)→τ4m2.

---

## 1. VERDICT (T5) — the deliverable, first

> **NO. Rosmanis's ED analysis does not adapt from `σ = id` to `σ = negation` (any `τ < q`). It breaks at the very first structural hypothesis — the regular‑representation property of `V = C[D_0]` (his Claim 2) — and the break is not repairable by bookkeeping. Špalek arXiv:1304.0845:425 ("an entirely new design") is vindicated. Per the commission's stopping rule, I report the obstruction precisely and STOP.**

**Which hypothesis fails, and where it is in Rosmanis.** Claim 2 (`rosmanis_small_range_ed.txt:283‑285`) asserts

> "V decomposes into irreps of S[N] × SΣ as V ≅ ⊕_{λ⊢N} λ×λ,"

and its proof (`:286‑291`) rests entirely on one sentence:

> "As a representation of S[N] and SΣ, respectively, V is isomorphic to the **regular** representation… For every `y ∈ D0` and every `π ∈ S[N]`, there is a **unique** `τ ∈ SΣ` such that `yπ = yτ`."

That sentence is **three separate structural facts, and 2‑Sum fails all three, in order:**

1. **`V` is not even transitive, let alone regular.** The regular representation is a single free orbit. For 2‑Sum, `D_0` splits into **≥ 2 `Γ`‑orbits** for every `τ<q`, `n≥2` (T1). The regular‑rep premise is false at step 0.
2. **The "unique `τ`" (here: unique `c∈C`) bijection fails on both sides** (T2b): *existence* fails and *uniqueness* fails, each with a two‑character witness (§5).
3. **Multiplicity‑freeness is destroyed** (T2/T3): `dim End_Γ(C[D_0]) ≫ p(n)`; the `⊕λ×λ` "each once" pattern is replaced by multiplicities up to 5 already at `n≤3` and by `~10^5` distinct isotypic components at `(8,0) n=8`.

**The first broken structure is #1: `D_0` is not a single free orbit.** Everything else is downstream. Concretely the regular representation needs `|D_0| = |Γ|/1` with trivial stabilisers and a single orbit; 2‑Sum gives multiple orbits **and** generically non‑trivial `C`‑stabilisers.

**Smallest witness of the obstruction** (both failure modes; verified explicitly, §5):
- *Non‑transitivity / existence failure:* `q=3, τ=1, n=2`, `σ=(0)(1 2)`, `C={id,(1 2)}`. Take `y=(0,1)` and `π` = the swap. Then `y^π=(1,0)`, but **no `c∈C` sends `y→y^π`** (it would need `c(0)=1`, moving the fixed point `0` off the fixed‑point set — impossible in `C`). So the `S_n`‑orbit of `y` is not inside its `C`‑orbit: `V` is not the regular rep.
- *Uniqueness failure:* `q=4, τ=0, n=2`, `σ=(0 1)(2 3)`. Take `y=(0,0)`, `π=id`. Then `{c∈C : c(y)=y}={id,(2 3)}` has size 2 — the flip of the **unused** pair `{2,3}` stabilises `y`. Two solutions, not one.

**Adaptation appendix (the one allowed paragraph).** An honest adaptation cannot reuse Rosmanis's `⊕λ×λ` transporter basis (`:332‑348`). It would have to carry the **measured** multiplicity structure: `V` decomposes with high multiplicities into `S_n×C` irreps `λ×μ` (μ an irrep of `C=S_τ×(C_2≀S_m)`), and the row space `U` decomposes over collisions of **two inequivalent kinds** — fixed‑point collisions (`x_i=x_j=a`, `2a=t`; the ED type) and 2‑cycle collisions (`x_i=a, x_j=t−a`, `a≠t−a`; **absent in ED**), which carry different `C`‑stabilisers (§4). Because the multiplicities are `>1`, Schur's lemma no longer pins each transporter block to a scalar; one gets a matrix of free parameters per isotypic component, i.e. exactly the "matrix orthogonal polynomial / recoupling‑with‑multiplicity" regime the corpus flags — **not** Rosmanis's scalar‑β construction. That is a different design, which is the point. I do **not** attempt it (stopping rule).

**ED‑limit consistency (whole‑computation sanity check): PASSES.** As `τ→q` (`σ→id`) the structure continuously returns to ED: orbit count `→ 1`, and at the bijection corner `q=n∈{2,4,8}` (elementary‑abelian‑2 groups, `t=0`) `dim End = p(n)` exactly (2, 5, 22). See §6.

---

## 2. T1 — Γ‑orbits on `D_0` (exact)

**Parametrisation (PROVED — complete invariant, verified 3 ways).** A `Γ`‑orbit on `D_0` is exactly
`( f , {μ_1,…,μ_r} )` where `f ∈ {0,…,τ}` is the number of fixed‑point values used (each appears exactly once, forced by legality) and `{μ_i}` is a multiset of `r ≤ m` positive integers — one multiplicity per used 2‑cycle (which side is used is quotiented away by the `C_2` flip; which cycle by `S_m`) — with `f + Σμ_i = n`. Soundness: `Γ` preserves `(f,{μ_i})`. Completeness: given equal invariants, `S_τ` matches used fixed points, `S_m`+flips match 2‑cycles by multiplicity, `S_n` matches the arrangement.

**Closed form (PROVED).** Orbit count
`N(n;τ,m) = Σ_{f=0}^{min(τ,n)} p_{≤m}(n−f)`,  `p_{≤m}(s)` = partitions of `s` into ≤ `m` parts.
**Generating function:** `Σ_n N(n) z^n = (1+z+⋯+z^τ)·∏_{i=1}^{m} 1/(1−z^i)`.
Growth in `n` at fixed `(q,τ)` is polynomial of degree **`m−1 = (q−τ)/2 − 1`** — in particular **constant when `m=1`**.

**Verification (NUMERICAL, exhaustive).** Closed form `=` exhaustive invariant‑count over all of `D_0` at **every** grid cell `n=2..8`, and `=` a genuine union‑find orbit count under `S_n×C` generators at every cell with `|D_0|≤4000`. All agree (`T1_orbits.log`).

| (q,τ) | m | n=2 | 3 | 4 | 5 | 6 | 7 | 8 | law in n |
|---|---|---|---|---|---|---|---|---|---|
| (3,1) | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | const `τ+1=2` |
| (4,0) | 2 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | `⌊n/2⌋+1` |
| (4,2) | 1 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | const `τ+1=3` |
| (5,1) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | linear |
| (8,0) | 4 | 2 | 3 | 5 | 6 | 9 | 11 | 15 | cubic |
| (8,2) | 3 | 4 | 6 | 9 | 12 | 16 | 20 | 25 | quadratic |
| (8,4) | 2 | 4 | 6 | 9 | 11 | 14 | 16 | 19 | quadratic |

(`|D_0|` ranges from 6 up to 844 760 at `(8,0) n=8`; full column in the log.) **ED endpoints** `σ=id` (`τ=q`, `q=2,4,8`): orbit count `=1` for all `n≤q` (single orbit = injective strings), `=0` for `n>q`. **This is the Rosmanis regime and the contrast that drives the verdict.**

---

## 3. T2 — `dim End_Γ(C[D_0]) = #orbitals`, and the ED benchmark `p(n)`

**Method (NUMERICAL, cross‑validated 3 ways).** Burnside over `Γ = S_n × C` conjugacy classes: `#orbits = |G|^{-1}Σ_g|Fix(g)|`, `dim End = #orbitals = |G|^{-1}Σ_g|Fix(g)|²`. **The Burnside `#orbits` reproduces the T1 closed form at every cell** (validates the fixed‑point counter, hence the squared sum). Independently confirmed by direct union‑find on `D_0×D_0` at every cell with `|D_0|≤1500` (all "OK", `T2_orbitals.log`), and by the T3 character machinery (`Σ mult² = dim End`, §4).

`p(n)` computed independently (partition function): `p(2..8) = 2,3,5,7,11,15,22`.

**`dim End` (each entry ≫ `p(n)`):**

| (q,τ) | n=2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| (3,1) | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| (4,0) | 13 | 27 | 56 | 91 | 147 | 211 | 302 |
| (4,2) | 22 | 38 | 40 | 40 | 40 | 40 | 40 |
| (5,1) | 33 | 109 | 260 | 504 | 863 | 1355 | 2002 |
| (8,0) | 20 | 121 | 711 | 3458 | 14718 | 54020 | 176588 |
| (8,2) | 57 | 393 | 2273 | 10222 | 37052 | 112118 | 295207 |
| (8,4) | 54 | 302 | 1412 | 5090 | 14212 | 31702 | 60638 |
| **ED `p(n)`** | **2** | **3** | **5** | **7** | **11** | **15** | **22** |

**Reading:** Rosmanis's `dim End = p(n)` (his `V` is multiplicity‑free, so `Σ mult² = Σ1 = p(n)`). Here `dim End` overshoots by factors from `5×` (at `(3,1)`) to `8000×` (at `(8,0) n=8`) and **grows in `n`** wherever `m≥2`. Multiplicity‑freeness is not marginally violated; it is obliterated.

---

## 4. T2b + T3 — the regularity test and the multiplicity structure

### 4.1 The Rosmanis "unique `c`" property (T2b)

For each legal `y` and each `π∈S_n`, the solution set `{c∈C : c(y)=y^π}` is empty or a coset of `Stab_C(y)`, so it has size `0` (existence fails) or `|Stab_C(y)|` (unique iff `=1`). Property‑at‑`y` (Rosmanis needs it ∀π) `⟺ Stab_C(y)=1` **and** `S_n·y ⊆ C·y`.

**Derived characterisation (PROVED by exhaustive check, `charOK=True` at every cell):**
`Stab_C(y)=1  ⟺  (f ≥ τ−1)  and  (r = m)` — i.e. uniqueness holds **only** for `y` that use ≥ `τ−1` of the `τ` fixed points **and** at least one value from **every** one of the `m` two‑cycles. Since a legal string uses ≤ one side per pair, this is the maximal‑support case; it is *impossible* below `n = (τ−1)+m`, so for `n < (τ−1)+m` uniqueness fails for **all** `y`. This is the sharp form of the strategist's "non‑surjective ⇒ uniqueness fails" (the relevant surjectivity is onto the `m` pair‑classes plus the fixed points).

**Fractions (per `(y,π)`), selected (full grid `n≤6/7` in `T2b_rosmanis.log`):**

| (q,τ) n | unique | exist‑fail | uniq‑fail | frac‑`y` with full property |
|---|---|---|---|---|
| (3,1) 2 | 0.667 | 0.333 | 0.000 | 0.333 |
| (3,1) 5 | 0.333 | 0.667 | 0.000 | 0.167 |
| (4,0) 2 | 0.667 | 0.000 | 0.333 | 0.667 |
| (4,0) 6 | 0.095 | 0.889 | 0.016 | 0.000 |
| (4,2) 2 | 0.333 | 0.333 | 0.333 | 0.000 |
| (5,1) 2 | 0.400 | 0.200 | 0.400 | 0.400 |
| (8,0) 2 | 0.000 | 0.000 | 1.000 | 0.000 |
| (8,2) 2 | 0.000 | 0.214 | 0.786 | 0.000 |
| (8,4) 4 | 0.000 | 0.813 | 0.187 | 0.000 |

The full‑property fraction `→ 0` as `n` grows in every column (and is `0` outright once `n ≥ 2` in the multi‑pair cells). Both failure modes are generic. **The property never holds for all `y` in any cell with `τ<q`.**

### 4.2 What replaces `⊕λ×λ` (T3)

**`S_n`‑marginal multiplicities** (`mult_{S_n}(λ)` in `C[D_0]|_{S_n}`, Murnaghan–Nakayama; validated on S₃/S₄): already not "each once". E.g. `(3,1)` all `n`: `mult((n))=4, mult((n−1,1))=2`, rest 0 → the trivial `S_n`‑rep alone appears **4×**. `(8,0) n=6`: max multiplicity **1240**. Full vectors in `T3_multiplicity.log`.

**Full joint `mult(λ×μ)`** at small cells via a Dixon–Schneider character table of `C` (validated: orthonormal rows, integer dims, `Σdim²=|C|`; e.g. `C_2≀S_4`→dims summing to 384). **Independent cross‑check:** the joint `Σmult²` reproduces the Burnside `dim End`, and `mult(triv×triv)` reproduces the T1 orbit count, at every small cell (e.g. `(4,0)n=4`: `Σmult²=56`, `mult(triv×triv)=3`; `(5,1)n=3`: `109` and `4`; `(8,0)n=2`: `20` and `2`). Two disjoint machineries agree.

Concrete smallest example, `(3,1) n=2` (`C=C_2`, irreps μ₀=triv, μ₁=sgn):
`V = 2·((2)×μ₀) ⊕ 2·((2)×μ₁) ⊕ 1·((1,1)×μ₀) ⊕ 1·((1,1)×μ₁)`.
Contrast Rosmanis, where the analogous `V` would be `⊕_{λ⊢2} λ×λ` = each of two blocks **once**. Here the trivial `S_n` rep already carries multiplicity 2 and pairs with **both** `C`‑characters — there is no diagonal `λ↔μ` matching. `mult(triv×triv)=2=#orbits`, `Σmult²=10=dim End`.

**Consistency identities (hold at every checked cell):** `mult(triv_{S_n} × triv_C) = #orbits` (T1); `Σ_{λ,μ} mult(λ×μ)² = #orbitals = dim End` (T2).

---

## 5. Smallest failure witnesses (explicit, re‑verified)

Verified directly against the enumerated `C` (`t3` witness recomputation, echoed in this report's driver):

- **Existence / non‑transitivity:** `(q,τ,n)=(3,1,2)`, `σ=[0,2,1]`, `C=[[0,1,2],[0,2,1]]`. `y=(0,1)`, `π`=swap ⇒ `y^π=(1,0)`; `{c: c(y)=y^π} = ∅`. *(Cause: `π` swaps a fixed‑point‑valued position with a 2‑cycle‑valued position; `C` preserves the fixed/non‑fixed partition of values, so cannot realise the swap.)*
- **Uniqueness:** `(q,τ,n)=(4,0,2)`, `σ=[1,0,3,2]`. `y=(0,0)`, `π=id`; `Stab_C(y)={id,(2 3)}`, size 2. *(Cause: the unused pair `{2,3}` contributes a free flip.)*

---

## 6. ED‑limit consistency check (does `τ→q` recover ED?)

**PASSES, cleanly at the corner and continuously along the ladder.**

- **Orbit count → 1:** at `σ=id` (`τ=q`) the orbit count is `1` for all `n≤q` (T1 ED rows). ✔
- **`dim End → p(n)`:** exactly at the **bijection corner** `q=n` (`Z_2^k, t=0`, `n=2,4,8`): `dim End = 2, 5, 22 = p(2),p(4),p(8)`. ✔ For `q>n` (ED with `|Σ|>n`, injective‑but‑not‑surjective strings) `dim End > p(n)` (e.g. ED `q=8,n=4 → 20`), which is the correct ED‑at‑`|Σ|>n` value — `p(n)` is specifically the `|Σ|=n` (surjective) number, matching Rosmanis's `|Σ|=N` hypothesis.
- **τ‑ladder** at fixed `q=8` (`dim End`, `n=4`): `τ=0:711, 2:2273, 4:1412, 6:293, 8:20`; orbit counts `5,9,9,5,1`. The approach to the ED endpoint is monotone near `τ=q` but **non‑monotone in the interior** (the `τ=2` bump exceeds `τ=0`) — reported honestly; the limit itself is clean. (`T2_orbitals.log`.)

---

## 7. Registered‑prediction scorecard (strategist's falsifiable claims vs. measurement)

| # | Registered prediction | Outcome |
|---|---|---|
| P1 | `q−τ≥2 ⇒ orbit count ≥ 2 ∀ n≥2` | **CONFIRMED** (min is 2, every such cell) |
| P2 | orbit count **grows with n** at fixed `(q,τ)`, degree `~(q−τ)/2 + [τ>0]` | **REFUTED in two respects.** (a) **constant** for all `m=1` cells `(3,1),(4,2)` — no growth; (b) where it does grow the degree is **`m−1=(q−τ)/2−1`**, not `(q−τ)/2+[τ>0]`. The exact law is `Σ_f p_{≤m}(n−f)` (§2). |
| P3 | ED (`σ=id`, `|Σ|≥n`) has `D_0` = one orbit | **CONFIRMED** (=1 at all ED endpoints) |
| P4 | uniqueness fails for non‑surjective / repeated‑value `y` | **CONFIRMED & SHARPENED** to the exact iff `Stab_C(y)=1 ⟺ f≥τ−1 ∧ r=m` |
| P5 | existence fails when `y` has two positions with values in different `C`‑orbits swapped | **CONFIRMED** (smallest witness is exactly a fixed↔2‑cycle swap) |
| P6 | `dim End ≠ p(n)` | **CONFIRMED** (`≫ p(n)`, §3) |
| P7 (T6) | nonzero Hamming mass at **every** level incl. `m=n` | **REFUTED literally / CONFIRMED in intent.** `m=n` mass is nonzero everywhere (not low‑degree ✔), but level `m=1` is **exactly 0** for all `τ=0` cells and all `n=2` cells; odd levels are strongly suppressed at `τ=0`. |

Two registered predictions (P2, P7) are refuted in detail — recorded here as the protocol requires.

---

## 8. T6 — Hamming‑level profile of `1_{D_0}`

Mass `= ‖proj_{E_m} 1_{D_0}‖²` per weight level `m`, in the Hamming scheme of `G^n` (`P_0=J/q`, `P_1=I−P_0` per coordinate). `Σ_m mass_m = |D_0|` holds to `<10^{-6}` at every cell (consistency). Fractions `mass_m/|D_0|`:

| (q,τ) n | m=0 | 1 | 2 | 3 | 4 | 5 | 6 | `m=n` nonzero? |
|---|---|---|---|---|---|---|---|---|
| (3,1) 2 | .667 | .000 | .333 | | | | | yes (2.0) |
| (3,1) 6 | .019 | .019 | .332 | .110 | .297 | .111 | .113 | yes |
| (4,0) 2 | .750 | .000 | .250 | | | | | yes (3.0) |
| (4,0) 6 | .062 | **.000** | .447 | .002 | .451 | .006 | .033 | yes (8.2) |
| (4,2) 6 | .021 | .025 | .305 | .085 | .256 | .172 | .136 | yes |

**Findings.** (i) The top level `m=n` has nonzero mass in **every** cell ⇒ `1_{D_0}` is **not low‑degree**; `L=D_0` is **not scheme‑compatible** (not a union of a few Hamming classes). This is the operative content and it holds. (ii) But the literal "every level" claim is false: for **fixed‑point‑free `σ` (`τ=0`) the level‑1 mass is exactly 0 at all `n`** (the indicator has no linear Fourier part — a genuine, previously‑unregistered structural fact: single‑coordinate marginals of `D_0` are constant when there are no fixed points), and level‑1 is 0 for all `n=2`. (NUMERICAL, cells `(3,1),(4,0),(4,2)`, `n≤6`.)

---

## 9. Provenance

Interpreter `C:[USER_HOME]/AppData/Local/Microsoft/WindowsApps/python.exe` (Python 3.11.9, numpy 1.26.4, scipy 1.14.1). All commands run with cwd `tools/`; logs in `artifacts/logs_ksum_stage3_20260716/`. No git commits made.

| Task | Command (prefix `<python> `) | Log | Script SHA‑256 |
|---|---|---|---|
| T1 | `ksum_stage3_t1_orbits.py ../artifacts/logs_ksum_stage3_20260716/t1_results.json` | `T1_orbits.log` | t1 `e9697d0c…157` |
| T2 | `ksum_stage3_t2_orbitals.py …/t2_results.json` | `T2_orbitals.log` | t2 `2e445a4b…a2` |
| T2b | `ksum_stage3_t2b_rosmanis.py …/t2b_results.json` | `T2b_rosmanis.log` | t2b `b6eac8b3…f6` |
| T3 | `ksum_stage3_t3_mult.py …/t3_results.json` | `T3_multiplicity.log` | t3 `654c2f0e…5c` |
| T4 | `ksum_stage3_t4_rows.py …/t4_results.json` | `T4_rows.log` | t4 `07b4f539…29` |
| T6 | `ksum_stage3_t6_hamming.py …/t6_results.json` | `T6_hamming.log` | t6 `736db034…25` |

Full SHA‑256 (all in `tools/`):
```
16f19f0b729fdca246b5dfbf4ee7b5b8703964d60a8471970d7bf282c378092b  ksum_stage3_core.py
e9697d0ce29bb6cbb8d9595349a0a42f2273c19f9c323d7a23b985850fb11157  ksum_stage3_t1_orbits.py
2e445a4b77398f73063c35800bd292cf363483ad5838ea2dc282e24c0be446a2  ksum_stage3_t2_orbitals.py
b6eac8b36e465d61f9fac44323b2bd48626272b51c94ba96cb53135b66e2adf6  ksum_stage3_t2b_rosmanis.py
654c2f0e44bea2a5eaac6a715e1d09c6f17f8f4c52a69511f2f369b3fab8625c  ksum_stage3_t3_mult.py
07b4f539765d206f771b34d1f54cdd8a05dca238fdafbac5cd62ed846b6d4829  ksum_stage3_t4_rows.py
736db03434cac4eaf751664e2f328ccc25f41511fd2eda138d29aafba8a55f25  ksum_stage3_t6_hamming.py
```
Reference: `artifacts/references/rosmanis_small_range_ed.txt` (Claim 2 at `:283‑291`; `D_1` stabiliser `:292‑306`).

A separate reader (`T_crosscheck.log`) re‑opens the on‑disk JSON result files and re‑verifies, with **zero mismatches**: Burnside `#orbits == T1` closed form (49 cells); T3 `Σmult² == dim End` and `mult(triv²) == #orbits` (13 joint cells); ED bijection `dim End == p(n)` (q=n=2,4,8); and `p(n)` recomputed.

**Validation architecture (why the numbers are trustworthy).** `fix_count` is validated by a 4‑way agreement at small cells: Burnside `#orbits` `=` T1 closed form `=` exhaustive invariant count `=` union‑find. `dim End` is validated by Burnside `=` direct pair union‑find (small cells) `=` T3 `Σmult²` (disjoint char‑theory code). The `C` character table (Dixon) is validated by orthonormality/integer‑dims/`Σdim²=|C|` and by reproducing `#orbits`/`#orbitals`. Murnaghan–Nakayama validated on known S₃/S₄ tables. Row‑side `fix_count_on_R` validated by Burnside `#orbits` `=` union‑find on an explicit `R` at every cell with `|R|≤40000`.

---

## 10. T4 — the row side (`R = {({i,j},x) : x_i+x_j=t}`) and the `:292‑306` analogue

Burnside `#orbits`/`#orbitals` on `R` under `Γ`, cross‑checked by union‑find on explicit `R` (`|R|≤40000`, all "OK", `T4_rows.log`). Selected `#orbits` / `#orbitals`:

| (q,τ) n | \|R\| | orbits | orbitals | 2‑cycle‑collision frac |
|---|---|---|---|---|
| (4,0) 2 | 4 | 1 | 3 | 1.000 |
| (4,0) 6 | 15360 | 14 | 48044 | 1.000 |
| (8,0) 7 | 5505024 | 47 | 19 764 593 | 1.000 |
| (4,2) 4 | 384 | 12 | 1816 | 0.500 |
| (8,2) 7 | 5505024 | 177 | 81 487 264 | 0.750 |

**The structural point (Rosmanis `:292‑306`).** Rosmanis decomposes the positive space over collisions where **`x_i=x_j`** (a value repeated), then over the freed/doubled value pair `{s,t}` with stabiliser `S^{s,t}_{i,j}=(S_{i,j}×S_{[N]∖{i,j}})×(S_{s,t}×S_{Σ∖{s,t}})`. For 2‑Sum a marked collision is a **σ‑pair `{a, t−a}`**, and it comes in **two inequivalent kinds**:
- **fixed‑point collision** `a=σ(a)` (`x_i=x_j=a`, `2a=t`) — the ED type; exists only if `τ≥1`; occurs in fraction `τ/q` of rows;
- **2‑cycle collision** `a≠σ(a)` (`x_i=a`, `x_j=t−a`, **two distinct values**) — occurs in fraction `(q−τ)/q`; **has no ED analogue at all**.

For every `τ=0` cell (`(4,0),(8,0)`) the fixed‑point type is **entirely absent — 100% of collisions are 2‑cycle** — so Rosmanis's "`x_i=x_j`" set `D_{i,j}` on which his whole `:292‑330` induction is built is **empty**. The two kinds carry different `C`‑stabilisers (a fixed‑point pair: `S_{τ−1}×(C_2≀S_m)` fixing the value; a 2‑cycle pair: `C_2 × S_τ × (C_2≀S_{m−1})` stabilising the pair setwise, the `C_2` being the flip). This inequivalence is the row‑side face of the same obstruction. **This confirms the branch to STOP: even the positive‑space decomposition Rosmanis uses does not port.**

---

## 11. WHAT I DID NOT CHECK (self‑disclosure — required, and NOT a certification)

- **Orbital direct‑cross‑checks at large cells.** `dim End` and row `#orbitals` at cells beyond the union‑find caps (`|D_0|>1500`, `|R|>40000`) rest on Burnside alone (its `fix_count` validated by the `#orbits` match and, for `D_0`, additionally by T3's `Σmult²` at small cells — but the *large*‑cell orbital numbers themselves are single‑method).
- **Full joint `mult(λ×μ)` beyond small cells.** Computed only at the 13 small cells listed; the `S_n`‑marginal is broad but the full joint at e.g. `(8,0) n≥3` is **OPEN** (heavy `C`‑table × M‑N sum). The consistency identities are checked where the joint was computed.
- **T6 only for `(3,1),(4,0),(4,2)`, `n≤6`** (as commissioned); the `τ=0` level‑1 nullity is observed, not proved in general (a short character argument would settle it — not attempted).
- **The Rosmanis property scan skips `n≥7` at large cells** (`n!` blow‑up); fractions there are extrapolated from the monotone trend, not measured.
- **No SDP / adversary‑value computation.** This bundle is pure representation/orbit combinatorics; I did **not** build or bound any adversary matrix (the stopping rule forbids it once regularity fails), and I make **no** claim about `Q(2‑Sum)` itself here.
- **Non‑abelian or non‑cyclic realisations** were not separately run; they are covered *by the `(n,τ,m)`‑only reduction* (§0), which is proved, but I did not exhaustively re‑verify a group‑realised σ against the abstract one beyond `|C|`‑order checks.
- **Numerical Dixon** uses float eigen‑decomposition with integer/orthonormality validation to `1e‑6`; I did not do exact rational arithmetic (the validation gates make a wrong table detectable, but this is a float method).
- I did **not** independently re‑derive Rosmanis's `⊕λ×λ` for ED from scratch beyond reproducing `dim End=p(n)` at the bijection corner.
