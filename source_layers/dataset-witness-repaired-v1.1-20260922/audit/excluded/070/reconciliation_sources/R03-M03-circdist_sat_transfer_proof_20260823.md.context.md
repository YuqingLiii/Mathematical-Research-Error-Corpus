# Source context 3

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/070/original/M03-circdist_sat_transfer_proof_20260823.md`

Original SHA-256: `4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30`

Original lines: 198–223.

198	
199	**Definition 2.8 (locations and configurations).** The **locations** of round `r` are: each CNOT of
200	that round (carrying any of the 15 non-identity two-qubit Paulis immediately after it); each
201	(qubit, time step) at which that qubit is not in a two-qubit gate, plus each ancilla immediately
202	after preparation (carrying any of the 3 non-identity single-qubit Paulis); and each recorded
203	outcome of that round (carrying a classical flip). A **fault configuration** `F` assigns to each
204	location an element of the group attached to it, with `|F| := #{locations assigned a non-identity
205	element}`. An **elementary fault** is a configuration of weight `1`. Data initialisation and the
206	terminal readout are ideal and carry no locations. Propagation is `F₂`-symplectic,
207	`CNOT(c,t) : x_t ← x_t + x_c`, `z_c ← z_c + z_t`; ancilla Pauli frames are zeroed after each
208	round's measurement.
209	
210	**Lemma 2.9 (collision handling — one location, one Pauli).** The record-flip vector and observable
211	flip of a configuration are `F₂`-linear in the assignments. Consequently, for any target effect `e`,
212	```
213	      min{ |S| : S a multiset of elementary faults with total effect e }
214	    = min{ |F| : F a fault configuration with effect e } .
215	```
216	*Derivation.* `≤` is trivial (a configuration is such a multiset). For `≥`, take a minimising
217	multiset `S`; if two of its members share a location `ℓ`, replace them by the single element of
218	`ℓ`'s group equal to their product. By linearity the effect is unchanged; the weight drops by `1`
219	if the product is non-identity and by `2` if it is the identity. Iterating terminates and yields a
220	configuration of weight `≤ |S|`. ∎ *Status: complete. This is the lemma that makes "weight" additive
221	under the union of per-round pieces, because Definition 2.8's location set is **partitioned by
222	round** (T2): distinct rounds cannot collide, so `|⊔_r S_r| = Σ_r |S_r|` exactly, while within a
223	round the collision-permissive minimum already equals the collision-free one.*
