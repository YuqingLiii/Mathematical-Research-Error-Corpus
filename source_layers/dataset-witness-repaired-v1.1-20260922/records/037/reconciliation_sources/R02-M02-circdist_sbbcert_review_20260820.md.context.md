# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/037/original/M02-circdist_sbbcert_review_20260820.md`

Original SHA-256: `6847fb574afd312f3419bc14fc2ef8f8b9dd75ccbc7b5862fc78c46da506d397`

Original lines: 290–330.

290	overlap in time". And its left–right circuit staggers explicitly: "the X ancilla is prepared at
291	time step 1 and measured at time step `t₁+t₂+2`, while the Z ancilla is prepared at time step
292	`t₁+3` and measured at time step `t₁+2`" — i.e. the Z-ancilla window **straddles the period
293	boundary**. For the gross code `L_X = A`, `R_X = B`, `L_Z = Bᵀ`, `R_Z = Aᵀ` all have degree 3, so
294	`t₁ = t₂ = 3` and `t = 3+3+2 = 8`: **depth 8 means six CNOT layers per period**, exactly the case
295	the target declares impossible.
296	
297	### 5.3 The counterexample, built and checked
298	
299	`lrc6.py` builds SBB's staggered LRC literally: block 1 (layers 0,1,2) runs `L_X ∥ R_Z`, block 2
300	(layers 3,4,5) runs `R_X ∥ L_Z`; the X ancilla of period `p` lives inside period `p`; the Z ancilla
301	instance `p` is prepared before layer 3 of period `p` and measured after layer 2 of period `p+1`.
302	Every layer is asserted to be a matching (6 CNOT layers per period, 864 CNOTs per period). The
303	within-check orders are then left-block-then-right-block for both types.
304	
305	Evaluating the target's own (MC) parity on **absolute** times, for both staggered pairings:
306	
307	```
308	overlapping (X,Z) pairs            : 648
309	odd-parity pairs, X_p vs Z_p       : 0
310	odd-parity pairs, X_p vs Z_{p-1}   : 0
311	```
312	
313	and handing the circuit to `stim` 1.16.0:
314	
315	```
316	stim, X-memory : 288 qubits, 504 detectors, 6 CNOT layers per period
317	                 DEM BUILT OK -> all detectors deterministic. 14472 error mechanisms
318	                 noiseless detector firings: 0 / 504
319	stim, Z-memory : 288 qubits, 576 detectors, 6 CNOT layers per period
320	                 DEM BUILT OK -> all detectors deterministic. 19656 error mechanisms
321	                 noiseless detector firings: 0 / 576
322	```
323	
324	The reason is a one-line computation the target's model cannot express. With shared qubits split
325	one-left/one-right, for `X_p` versus `Z_p` both shared CNOTs of `Z` come *after* both of `X`
326	(`c = 0`); for `X_p` versus `Z_{p−1}` both come *before* (`c = 2`). Even in both cases. The
327	target's §7(7) correction — "with the shared pair split one-per-half, that pattern gives `c_ab = 1`
328	for all 648 overlapping pairs — maximally measurement-inconsistent" — is the *unstaggered* pairing
329	only, and staggering is precisely what removes it.
330	
