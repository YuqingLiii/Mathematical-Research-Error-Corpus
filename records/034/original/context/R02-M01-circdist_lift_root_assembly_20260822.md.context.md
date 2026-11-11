# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/034/original/M01-circdist_lift_root_assembly_20260822.md`

Original SHA-256: `275a8c2cdce003277abe9e0e6dfed057f4f91cd00238fc9805ff360c58a8aa46`

Original lines: 134–160.

134	| clause | text | kind |
135	|---|---|---|
136	| **(C1)** | in graph-like DEMs with fixed boundaries, a **necessary-and-sufficient structural criterion** (in graph-covering, voltage-graph, or chain-complex form) characterizes when `d_circ = d_eff` | universal, biconditional |
137	| **(C2)** | the criterion is **of the shape** `d_circ = min_{γ ∈ L_eff} ℓ(γ)`, `ℓ(γ)` = length of the shortest closed spacetime lift of `γ` | universal, identity |
138	| **(C3)** | **zero time-direction voltage/monodromy** is the equal-weight liftability condition | definitional content of (C1)/(C2) |
139	| **(C4)** | the criterion **recovers the non-interleaved equality** `d_circ = d_eff` as a corollary | universal, derivational |
140	| **(C5)** | the criterion **is accompanied by an explicit interleaved example** with `d_circ > d_eff` | **existential** |
141	
142	The kind column is what makes §4 necessary: (C1)–(C4) are universally quantified over the model
143	class, and (C5) is existential inside it. Restricting the model class weakens the first four and
144	**strengthens** the fifth. That asymmetry is the whole scope problem.
145	
146	### 1.3 The frozen ambient conventions all five clauses inherit
147	
148	From the 公共定义 (`CIRCDIST_PROBLEMS.md`, §公共定义 and 课题二), unchanged:
149	CSS code `Q = [[n,k,d]]`; single ancilla per stabilizer generator, prepared once and measured once
150	per round, one CNOT per data qubit of the generator's support; `d_eff(M) := d_ext(E(M))`;
151	`d_circ(C) = min{|F| : F` fires no detector and flips a nontrivial logical `}`; standard memory
152	experiment with equal elementary-fault weights and ideal final readout;
153	`d_eff(M) ≤ d_circ(C(M)) ≤ d`.
154	
155	Plus the **measurement-consistency legality constraint (MC)** added across the round-2+ artifacts
156	and now part of the model: for every `(a,b) ∈ 𝒜 × ℬ`,
157	`c_{ab}(M) = #{q ∈ supp(a) ∩ supp(b) : t(q→b) < t(a→q)} ≡ 0 (mod 2)`. A schedule violating (MC)
158	has non-deterministic detectors and therefore **no `d_circ` at all** — so (MC) is a hypothesis of
159	every clause, silently, and any future instance offered against this root must be checked for it
160	first. This is the constraint that invalidated the round-1 recon's original `[[4,2,2]]` witness.
