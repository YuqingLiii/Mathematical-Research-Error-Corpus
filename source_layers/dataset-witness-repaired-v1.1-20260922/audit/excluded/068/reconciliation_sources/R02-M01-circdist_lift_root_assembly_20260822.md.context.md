# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/068/original/M01-circdist_lift_root_assembly_20260822.md`

Original SHA-256: `275a8c2cdce003277abe9e0e6dfed057f4f91cd00238fc9805ff360c58a8aa46`

Original lines: 241–264.

241	### 2.3 C3 — "zero time-direction voltage/monodromy"
242	
243	Discharged by the same child clause, with one wording correction that the assembly must not paper
244	over.
245	
246	The certified realisation of "zero voltage" is `repair(γ) = 0`, which by (LIFT′) reads:
247	
248	> there exist a round assignment `r_1,…,r_w` and unit-weight voltage representatives
249	> `u_i ∈ U(E_i)` such that in **every** round and on **every** Z-check, the in-round measurement
250	> flips equal the parity of the syndrome accumulated by all earlier rounds:
251	> `U_b(r) = c_b(r−1)` for all `b, r`.
252	
253	This is `F₂`-valued (so the recon's `F₂`-versus-`Z` orientation crux does not arise), it is
254	computed from one round's `(E, s, u, λ)` data plus a round assignment, and no multi-round circuit
255	is ever built. The recon's earlier `Σ_i u_i = 0` is the same-round special case.
256	
257	**The correction.** The root says "*zero* time-direction voltage/monodromy", which reads as the
258	vanishing of a single well-defined quantity attached to `γ`. It is not one. Because a residual `E`
259	admits a *set* `U(E)` of unit-weight voltages, the voltage of `γ` is a set, and the liftability
260	condition is a **minimum over that set and over round assignments** being zero, not the vanishing
261	of a scalar. §7 R2 proposes the minimal rewording. Substantively the clause is discharged; verbally
262	it overstates the sharpness of the object.
263	
264	**Scope of the equal-weight statement.** The biconditional `ℓ(γ) = |γ| ⟺ repair(γ) = 0` holds in
