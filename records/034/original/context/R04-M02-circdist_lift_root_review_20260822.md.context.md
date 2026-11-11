# Source context 4

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/034/original/M02-circdist_lift_root_review_20260822.md`

Original SHA-256: `a6fbf42e5f1f65c7c3c2731185dcbcd898e74b919bda4fdc85bde39e98a93b7c`

Original lines: 300–326.

300	### 4.2 But a hypothesis is dropped between §2.1 and §6 — **F2**
301	
302	The assembly's own restatement of the certified criterion (§2.1) reads:
303	
304	> "For every legal, measurement-consistent single-ancilla CSS schedule `M`, **and `R ≥ d`**,
305	> `d_circ(C_R(M)) = d_eff(M) ⟺ ∃γ ∈ L_eff` with `|γ| = d_eff(M)` and `repair(γ) = 0`."
306	
307	I checked the source: iff CONJECTURED 5.7 does carry `R ≥ d`. But:
308	
309	* the **root claim** has no `R` quantifier and no `C_R(M)` — it says "characterizes when
310	  `d_circ = d_eff`", unrestricted;
311	* the **`lift.iff` child claim** has no `R` quantifier either;
312	* §6 of the assembly — the section whose entire job is "every caveat carried forward, none may be
313	  dropped by a promotion of the root" — lists C-R1..3, C-M1..6, C-S1..3, C-O1..6 and **`R ≥ d` is
314	  in none of them**. It appears once, in §2.1, and never again.
315	
316	This is exactly the failure mode §0.3 was written to prevent, applied to the assembly itself. I
317	probed for a live counterexample and did not find one at `d = 2`: my enumeration gives
318	`d_circ = 2` for the interleaved witness and `1` for its non-interleaved partner at `R = 1` as
319	well as `R ≥ 2`, so `R ≥ d` is not demonstrably load-bearing *on this instance*. That does not
320	discharge it — a hypothesis of the certified theorem is a hypothesis of anything assembled from
321	it, and `d_R` is only known to be non-increasing and constant for `R ≥ d`.
322	
323	**F2 (required).** Either add `R ≥ d` (equivalently: "`d_circ` means `d_circ(C_R(M))` for
324	`R ≥ d`") to the root claim, or add it to §6 as **C-M7** and to the root's caveats. This is a
325	second **type-audit** finding: `d_circ` has type `(circuit) → ℤ`, the circuit is `C_R(M)`, and the
326	root claim never binds `R`.
