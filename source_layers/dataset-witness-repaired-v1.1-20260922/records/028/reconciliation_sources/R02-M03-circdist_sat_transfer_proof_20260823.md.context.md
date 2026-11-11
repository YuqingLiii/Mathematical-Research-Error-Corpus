# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/028/original/M03-circdist_sat_transfer_proof_20260823.md`

Original SHA-256: `4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30`

Original lines: 165–177.

165	**Definition 2.4 (legality).** `M` assigns a time step in `{0,…,T−1}` to every CNOT (`t(a→q)`,
166	`t(q→b)`); it is **legal** if at every step each physical qubit is in at most one two-qubit gate.
167	
168	**Definition 2.5 (measurement consistency, (MC)).** With
169	`c_{ab}(M) := #{q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q)} mod 2`, `M` is measurement-consistent iff
170	`c_{ab} = 0` for all `(a,b)`. Writing `c'_{ab} := #{q : t(a→q) < t(q→b)}`, (CSS) gives
171	`c_{ab} + c'_{ab} ≡ 0`, hence `c'_{ab} = c_{ab}`, so **(MC) is mirror-symmetric** and selects the
172	same schedule class in both sectors. *Status: complete; this is the window amendment's Repair 3,
173	re-derived here in one line because §3 consumes both `c` and `c'`.*
174	
175	**Scope clause T1.** Every statement below quantifies over **all** `(Q,M)` with `Q` CSS, `k ≥ 1`,
176	and `M` legal **and** measurement-consistent in the class of Definitions 2.3–2.4 — any depth,
177	interleaved or not, any check weights, graph-like or not, generating sets dependent or not.
