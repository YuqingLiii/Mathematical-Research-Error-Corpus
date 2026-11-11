# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/033/original/M02-circdist_lift_claimrepair2_review_20260823.md`

Original SHA-256: `9a0d3378e3fbc655114593cc52417b006fc51d2e5b3f57be43fef4373271cfc7`

Original lines: 194–222.

194	### 4.3 **DEFECT — the stated bound is the wrong constant, and it is false per sector**
195	
196	5.10(2) fixes the search size **and** the window at the **code distance `d`**. That constant comes
197	from the trailing chain of 5.9, "round-span(`F`) `≤ |F| = d_circ ≤ d`", and from 5.10(1)/(1′),
198	"`d_R` … constant for all `R ≥ d`" — which Amendment 1 §3 restates explicitly **"per sector"**, and
199	whose ceiling Amendment 2 §3 sources to the 公共定义: *"The 公共定义 gives `d_R(M) <= d` for every
200	`R`"*.
201	
202	The 公共定义's inequality is `d_eff(M) <= d_circ(C(M)) <= d`, written for the **circuit** `C(M)`.
203	Definition 1.5 of the proof document defines `d_circ(C)` as the **min over the two memory sectors**.
204	But all of §5 is per-sector ("All statements below are for the Z-memory"). Per sector the only
205	available bound is `d_circ^{Z-mem} ≤ d_X`, and `d = min(d_X, d_Z)`. **For a CSS code with
206	`d_Z < d_X` the transposition fails.**
207	
208	I built such an instance and measured it (§4.5): `n = 6`, X-checks `{0,1},{2,3},{4,5}`, Z-checks
209	`{0,1,2,3},{2,3,4,5}`, `k = 1`; `d_X = 3`, `d_Z = 2`, so `d = 2`. Non-interleaved list-scheduled
210	single-ancilla CSS circuit (hence legal and (MC)-automatic), ideal boundaries. **This instance is
211	`graph-like` in the Z-memory sector (Def 1.12 verified on all 91 elementary faults, 0 violations),
212	so it lies inside the repaired claim's own scope.** Measured, by direct multi-round simulation:
213	
214	```
215	  d_eff = 3 ;  d_circ(Z-memory) = 3  at R = 1,2,3,4     while  d = 2
216	  5.10(2) as stated, W = d = 2      ->  returns NOTHING     <-- defect
217	  5.10(2) with W = d_X = 3          ->  returns 3           <-- correct
218	```
219	
220	Both halves of the stated bound fail: the **size** bound `≤ d = 2` excludes every witness, and the
221	**window** `≤ d = 2` rounds excludes the 1 224 of 27 562 minimum-weight witnesses whose span is 3.
222	Contiguity itself is untouched — all 27 562 are contiguous with span `≤ weight = 3`, a third
