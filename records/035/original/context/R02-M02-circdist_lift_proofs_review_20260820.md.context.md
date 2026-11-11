# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/035/original/M02-circdist_lift_proofs_review_20260820.md`

Original SHA-256: `fa75f0405a9e233cc45aae2cf01458caef45d65cfef9bc0a44cbca19f0d0189f`

Original lines: 157–179.

157	### 3.1 GAP-AT-5.3 — the iff-doc's `≤` direction rests on a false claim it contradicts itself on
158	
159	iff-doc §5.2, Lemma 5.3, says of the `|γ|` essential faults:
160	
161	> "these are `w = |γ|` distinct circuit locations, since **distinct residuals force distinct
162	> locations**."
163	
164	This is false, and the document proves it false three pages earlier. Its own Proposition 1.13.4
165	reads:
166	
167	> "on a gate `a→q_j` the possible residuals are `∅, S_j, {q_j}, S_{j−1}`"
168	
169	— four distinct residuals at one location. Since Definition 1.8 (and the frozen fault model) puts
170	**one Pauli per location**, two of those cannot be placed as two weight-1 faults; the `X⊗X`
171	composite is a *single* weight-1 fault whose residual is `S_{j−1}`, and whose `π₁` image is the
172	basis vector `[S_{j−1}]`, not `[S_j] + [{q_j}]`.
173	
174	The same conflation is baked into Definition 5.1, which defines
175	`ℓ_R(γ) := min{|F| : F ⊆ 𝔽 × {0,…,R−1}, ∂F = 0, π₁F = γ}` — a minimum over *formal subsets of
176	(fault type) × (round)*, which is not the same as a minimum over realisable fault configurations.
177	The `≥` direction is unaffected (a real configuration has at most one type per location, so it *is*
178	such a subset). Only the `≤` direction, and hence Theorem 5.6(b)'s upper bound and 5.6(c)'s
179	equality, are exposed.
