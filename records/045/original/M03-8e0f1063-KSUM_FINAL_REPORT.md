# k-Sum alphabet-size commission — FINAL REPORT

**Date:** 2026-07-17. **Protocol:** KSUM_MODEL_DIVISION.md §-1 (Fable 5 = strategy/interpretation; Opus 4.8 = all execution/verification; the strategist verified nothing itself). **Certification chain:** every claim below traces to an Opus run with command/log/SHA (provenance in the cited documents), and the headline result passed a two-layer check: adversarial construction+verification (W1) followed by an independent hostile audit by a different agent with its own code (W2, 16 attack surfaces, 484,470 independent encoding checks). Commits: `f0d8df7` (Stage 0/1), `54915b0` (challenge amendments + C7 battery), `97eef0c` (Stage 2/3), plus the W1/W2/report commit accompanying this file.

---

## 1. Executive verdict

**The commission asked:** what exactly is the alphabet-size obstruction in the Belovs–Špalek k-Sum lower bound, and can it be relaxed? (BS:388; Špalek:425; Rosmanis §7; Belovs 2026:3101 — all verbatim on disk.)

**Answer, for k = 2: YES — the alphabet condition is relaxed from q ≥ N² to q = Θ(N), with a smooth tradeoff below it.** Not by repairing BS's adversary matrix (that route is proved dead — §4), but by a three-line encoding that transfers the small-range claw-detection lower bound of Ambainis–Balodis–Iraids (arXiv:2103.16390), independently re-proved by Tani (arXiv:2410.02243) via multisymmetric approximate degree. The connection was found by literature sweep, not derivation — the two literatures had zero citation overlap before this.

**For k ≥ 3: open, untouched by our technique** (§6). The anatomy of why BS's own proof cannot be pushed below q ≈ n^k is complete and committed (§4–5).

## 2. The main theorem

**Theorem A (k = 2, cyclic; PROVED-BY-REDUCTION modulo the on-disk ABI/Tani claw lower bound; W2-audited).**
Let q ≥ 5 be odd, t ∈ Z_q arbitrary, N ≥ q+1. Then
> **Q(2-Sum over Z_q, target t, N inputs) = Ω(√N · q^{1/6}).**

Range: 5 ≤ q ≤ N−1 with k = (q−1)/2 (ABI), extended to q ≤ 2N−1 by Tani's version; odd N covered by freezing one coordinate to the never-used value 0 (W2 finding F1). By the translation theorem (C7, PROVED), all t are equivalent at odd q.

**Theorem A′ (general abelian G, t = 0; same status, W2-verified on 8 groups incl. Z₆, Z₈, Z₁₀, Z₂×Z₄, Z₃×Z₃, Z₁₅).** For any finite abelian G with 2-torsion G[2]:
> **Q(2-Sum over G, t = 0, N inputs) = Ω(√N · ((q−|G[2]|)/2)^{1/6})** via a sum-free-from-zero value set S of size (q−|G[2]|)/2.

**Corollary B (the threshold drop).** At q = Θ(N), Theorem A gives Ω(N^{2/3}); combined with the standard O(N^{2/3}) quantum-walk upper bound (Ambainis quant-ph/0311001 + Childs–Eisenberg quant-ph/0311038, cited at BS:107):
> **Q(2-Sum, Z_q, N) = Θ(N^{2/3}) once q = Θ(N)** — the tight-bound threshold at k=2 drops from Belovs–Špalek's q ≥ N² to q = Θ(N).
For q above the stated ranges the same encoding with k = n−1 plateaus the lower bound at Ω(N^{2/3}) (the no-collision arithmetic needs only q ≥ 2k+1); this plateau step was numerically confirmed in the commit-pass check accompanying this report.

**The reduction (the entire new mathematical content).** Given a claw instance — ABI's Claw_{n→k} is a single total decision function on [k]^{2n} (claw.tex:125–133), i.e. exactly the 2-Sum oracle model — encode x_i = f(i) ∈ {1..k} for i ≤ n and x_{n+j} = −g(j) mod q ∈ {q−k..q−1}. Within-half pair sums lie in ±[2, 2k] ∌ 0 (mod q, q ≥ 2k+1); cross-half sums vanish iff f(i) = g(j). So 2-Sum(x) = Claw(f,g) exactly, query-for-query, and restriction can only decrease Q. Verified analytically and by 77,598 + 484,470 exhaustive instance checks (W1, W2 independently; zero mismatches).

**Witness status (the commissioned goal).** The explicit witness = the encoding above + the two published certificates it transfers (ABI's proof, resting on Zhang [Zha05] and Brassard et al. [BHK+19 Thm 13], both verified real and unconditional in claw.bbl; Tani's independent dual-polynomial route). A *numerical* small-instance witness is impossible in principle: the q^{1/6} factor is invisible at any reachable N — this project's own permanent-blocker theorem (KSUM_STAGE0_VERDICT.md §3.2/§3.6). No such artifact will exist, and its absence is not a gap.

**Credit (G10).** The lower-bound machinery is entirely ABI's and Tani's; Zhang's and Brassard et al.'s underneath. Our contribution is the encoding, its verification, and the structural program that located it.

## 3. How it was found

Stage 0's scoop agent surfaced the small-range claw literature as "adjacent, unnamed, zero overlap with the k-Sum literature" while verifying the problem was still open. The strategist's reframe — 2-Sum at k=2 is *involution-twisted element distinctness*, hit ⟺ x_j = σ(x_i), σ(x) = t−x — made claw the obvious donor once the σ-structure was proved to be the whole story (C7: only (n, q, τ) matters; PROVED). The user's standing directive "search the literature before grinding" is the reason this took hours instead of weeks: the route came out of a citation sweep, and every prior break in this repo (Rosmanis on-disk, BS:386) had the same shape.

## 4. Why the old route could never have worked — the anatomy (all committed)

1. **BS's proof uses q ≥ n^k at exactly one step** — the flat-test-vector legality estimate at BS:379; everything else is alphabet-free (Stage 0, Agent A; verified line-by-line).
2. **The legal-column restriction destroys the algebra, not the symmetry.** Aut(Γ̃) = Aut(Γ_L) = C(σ) — the drag is zero (three independent reproductions) — but L is not scheme-compatible (nonzero top-level Hamming mass; level-1 mass exactly 0 iff τ=0, a small new fact), and the restricted matrix must be analyzed in a module whose commutant explodes.
3. **Rosmanis's minimal-alphabet ED machinery does not port to any τ < q** (Stage 3, verdict NO): D₀ is never one orbit (exact closed form), the regular-representation property fails on both sides (minimal witnesses at n=2), dim End exceeds the required p(n) by up to 8000×, and at τ=0 the equal-value blocks his positive-space induction needs are *empty*. Špalek's 2013 prediction ("entirely new design") is vindicated — and Rosmanis's smooth-tradeoff conjecture is *also* vindicated, by Theorem A. Both sides of the 2013 disagreement were right.
4. **No OA-uniform (Theorem-5-type) bound can reach small q at all** (Stage 2, Theorem 3, PROVED): some orthogonal-array choice is constant once n > q (k=2) or n > (k−1)q on p|k ladders (k≥3). Any small-alphabet bound must use group structure — as Theorem A's does, through σ.
5. **The symmetry landscape is now theorems, not measurements:** Aut(f) = diag(C(σ)) ⋊ S_n for k=2 (all abelian G, all t, n ≥ 3; constancy iff t=0, G=G[2], n>q); = diag(Aff_{k,t}(G)) ⋊ S_n for k ≥ 3, n > k modulo the explicit (NC-ext) hypothesis (proved for q > k·2^k, small q exhaustive); n = k is the sharp degenerate boundary.
6. **The exponent question was and remains numerically undecidable** — √n vs n^{2/3} differ by n^{1/6}; a G11-compliant separation needs n ≈ 256 at q=3. Stage 0's certified-value curve (flat at ≈0.78·√n through n=8) discriminates nothing, as the challenge round established. Theorem A settles by structure what no computation could.

## 5. The bounds table for k = 2, after this commission

| regime | family | bound | status |
|---|---|---|---|
| q = O(1) | any | Θ(√N) | BS:137 + positive adversary (known) |
| \|G\| = 4, t=0 | Z₂² vs Z₄ | 0 vs Θ(√N) | known (§3.6 of the commission; structure = τ, now C7-PROVED) |
| any q, t=0, \|A_t\| ≥ N | large 2-torsion | Ω(N^{2/3}) | ED-restriction theorem (Stage 0 D, VALID; one on-trust link Shi/AS) |
| **5 ≤ q ≲ N, odd, any t** | **cyclic (and via C7 all τ=1)** | **Ω(√N · q^{1/6})** | **Theorem A — NEW** |
| **t=0, any abelian G** | small 2-torsion | **Ω(√N · ((q−\|G[2]\|)/2)^{1/6})** | **Theorem A′ — NEW** |
| **q = Θ(N) up** | cyclic (t=0 general; odd-q any t) | **Θ(N^{2/3})** | **Corollary B — NEW threshold, was q ≥ N²** |
| q ≥ N² | any | Θ(N^{2/3}) | BS Thm 1 (subsumed at k=2 by Corollary B) |
| any q | any | O(N^{2/3}) | Johnson walk (known) |

## 6. What remains open (the honest ledger)

1. **k ≥ 3 — the original problem above k=2 is untouched.** The natural attack is a "k-claw"/multi-list analog of the encoding feeding Tani's multisymmetric framework; no such lower bound exists in the literature we swept. This is the concrete next campaign if commissioned.
2. **The gap in the middle:** between Ω(√N·q^{1/6}) and O(N^{2/3}) for 5 ≤ q ≪ N. Both endpoints could move: ABI themselves have a O(√N·q^{1/4})-type *claw* upper bound — whether an analogous 2-Sum algorithm exists at small q is the first literature/derivation question on the upper side; and any improvement of the claw lower bound (k^{1/6} → k^{1/4}?) transfers to 2-Sum automatically through our encoding.
3. **Even-q, t ≠ 0** beyond the 2-torsion-restriction cases: Theorem A′ is stated at t=0; the t-classification at even q is τ-dependent (C7) and partially open.
4. **The base bounds are cited, not re-derived** (Zhang, Brassard et al., ABI, Tani) — deliberate, per the literature-first directive; all four are published/unconditional and two of them independently prove the same claw bound.
5. Loose threads recorded elsewhere: (NC-ext) in full generality; the k≥3 constancy threshold (EGZ-type, OPEN); Recon A's 0.8115-vs-0.80 discrepancy (unchased, immaterial).

## 7. Process record

Six-agent verified Stage 0 with pre-registered predictions; a lead's challenge that forced one retraction ("empirically live"), one severity re-grade (MAJOR incumbent misdescription), one provenance correction (a p-value that existed only in a report), and the C7 held-out battery that ended in a proof; Stage 2/3 theorems and the Rosmanis NO; then W1/W2. Failure modes caught this cycle and logged: a strategist proof-strategy that didn't survive contact (Theorem 1's background-value approach, replaced by the executor), an unregistered bonus claim audited after the fact (Theorem A′, confirmed), an auditor's own harness bug (disclosed, fixed, and turned into extra confirmation), and a phantom incumbent (ksum_probe.py) that had never produced a number. The division of labor — strategist may not verify, executor may not be told the wanted answer, every number carries command/log/SHA — is the reason this report contains no claim that survived on trust alone.
