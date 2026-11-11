# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/032/original/M02-circdist_lift_proofs_review_20260820.md`

Original SHA-256: `fa75f0405a9e233cc45aae2cf01458caef45d65cfef9bc0a44cbca19f0d0189f`

Original lines: 219–247.

219	### 3.3 REFUTE as stated — `R_sat(M) ≤ d`
220	
221	iff-doc §5.10(1): "`d_R(M)` is non-increasing in `R` and **constant for all `R ≥ d`**; i.e.
222	`R_sat(M) ≤ d` in the sense of `CIRCDIST.sat`, for this model." Repeated without qualification in
223	§8 item 4: "`R_sat(M) ≤ d` for every single-ancilla CSS schedule with ideal boundaries, per sector."
224	
225	The frozen definition (公共定义, 课题四) is
226	
227	```
228	   R_sat(M) = min{ R_0 : d_R(M) = d  for all R ≥ R_0 },     = ∞ if no such R_0.
229	```
230	
231	Saturation is at the **code distance `d`**, not at `lim_R d_R`. Contiguity gives the latter. When
232	`d_∞(M) < d` — the generic hook-damaged case — `R_sat(M) = ∞`, not `≤ d`.
233	
234	**Explicit counterexample, computed this session.** Steane `[[7,1,3]]`, natural within-check orders
235	`X_i = Z_i = supp` in index order, non-interleaved (either block order), legal, `MC = ∅`:
236	`d_eff = 2 < 3 = d`, and my exhaustive weight-`≤3` search gives `d_R = 2` for `R = 1,2,3,4`. Hence
237	`R_sat = ∞`. The claim `R_sat ≤ d = 3` is false here. (Twelve further non-interleaved
238	configurations in §4.4 with `d_eff < d` are additional witnesses.)
239	
240	**The sibling document gets this right and the two contradict each other.** nonint Corollary 7.3:
241	"`R_sat(M) = 1` if `d_eff(M) = d`, `R_sat(M) = ∞` if `d_eff(M) < d`." That is correct. The
242	iff-doc's §5.10(1) should be restated as: *`d_R` is constant for `R ≥ d`, with limiting value
243	`d_∞`; consequently `R_sat ≤ d` when `d_∞ = d` and `R_sat = ∞` otherwise, and in either case
244	`R_sat` is decided by finitely many `R`.* The finite-window content (`B(r,d) = d`) is untouched by
245	this correction and is a real `CIRCDIST.sat` deliverable — the error is only in the identification
246	with `R_sat`. A `CIRCDIST.sat` session adopting §8 item 4 verbatim would adopt a false statement,
247	which is why I am recording this as REFUTE-as-stated rather than as a wording nit.
