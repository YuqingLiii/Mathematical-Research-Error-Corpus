# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/069/original/M03-circdist_sat_transfer_proof_20260823.md`

Original SHA-256: `4fce5371edc09fa153b41f6735d521d31500b84b55a0059c8b42dc000651da30`

Original lines: 149–177.

149	**Standing fact 2.2.** `ker H_Z = S_X ⊕ span{χ_{X_L^{(j)}}}` and `ker H_X = S_Z ⊕ span{χ_{Z_L^{(j)}}}`,
150	each quotient of dimension `k = n − rank H_X − rank H_Z`; and for `v ∈ ker H_Z`, `v ∉ S_X` **iff**
151	`|v ∩ supp(Z_L^{(j)})|` is odd for some `j`. *Standard CSS symplectic duality; status: complete.*
152	
153	**Scope clause T0.** `k ≥ 1`. `𝒜` and `ℬ` are the **given generating sets**, not required
154	independent: `leftker(H_X) ≠ 0` is explicitly in scope (this is the case §3 must handle and the
155	case the toric and bivariate-bicycle families exhibit).
156	
157	### 2.2 Schedule
158	
159	**Definition 2.3 (one round).** Each check `g` owns one ancilla `anc(g)`. Per round: every
160	`anc(a)`, `a ∈ 𝒜`, is prepared in `|+⟩`, is the **control** of exactly one CNOT onto each
161	`q ∈ supp(a)`, and is measured in `X`; every `anc(b)`, `b ∈ ℬ`, is prepared in `|0⟩`, is the
162	**target** of exactly one CNOT from each `q ∈ supp(b)`, and is measured in `Z`. No flags, no cat
163	states, no repeated CNOTs, no change of generating set.
164	
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
