# Source context 3

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/067/original/M02-circdist_dstar_hunt2_20260823.md`

Original SHA-256: `01f9e79226495ad837ecb8fa08066b4d96a2d7078e385d5831d827ddb6ba82da`

Original lines: 103–148.

103	`V ∈ ker H_Z`, `V ∉ rowspace(H_X)`, `|V| = 12`, `⊕(residual supports) = V`, and counts the faults
104	one by one: **144 / 144 assertions pass.** The smallest witness, in full:
105	
106	```
107	Z-memory, |V| = 12, 10 faults
108	  V          = {1, 3, 7, 11, 12, 14, 72, 73, 74, 77, 78, 80}
109	  hook       check 66, 4-suffix, qubits {78, 12, 141, 72}   times (9, 11, 12, 32)
110	             (check 66 full CNOT order 68,67,78,12,141,72 at times 5,8,9,11,12,32)
111	  hook       check  2, 2-suffix, qubits {77, 80}            times (12, 32)
112	  singletons {1, 3, 7, 11, 14, 73, 74, 141}                 (8 of them)
113	```
114	
115	`|V ∩ D| = 5`, `|D \ V| = 1`, so `cost = 2 + (12−5) + 1 = 10`. The X-memory witness has the same
116	shape (check 18's 4-suffix + check 26's 2-suffix + 8 singletons).
117	
118	### 1.3 The witnesses are not an artefact of the residual presentation
119	
120	The campaign's certified machinery uses the **360-column** extended code with [SBB26]'s three
121	residuals per check `{i1,i2} / {i4,i5,i6} / {i5,i6}`, not "all suffixes". The two presentations are
122	the same column set modulo `supp(a)`: `{i1,i2} = supp(a) Δ 4-suffix`, `{i2..i6} = supp(a) Δ {i1}`
123	(a singleton). `src/v1_model_and_repair.py` §C **rewrites all 144 witnesses into the 360-column
124	model** and re-asserts them: same fault count, and the target is still a **weight-12** nontrivial
125	logical, hence still inside the campaign's `|E| = 12` cell. `144 / 144` pass. The kill therefore
126	holds in the campaign's own model, not only in wave 37's phrasing of it.
127	
128	### 1.4 What exactly wave 37 missed
129	
130	At `|V| = 12`, with `ρ_a <= 3`, the effective gain of an option is `2ρ_a − |C_a| − n_a`, and the
131	complete list of gain-positive shapes is:
132	
133	| shape | residuals | gain | tested by wave 37? |
134	|---|---|---|---|
135	| `{i4,i5,i6} ⊆ V` (3-suffix) | 1 | 2 | **yes** |
136	| `{i5,i6} ⊆ V` (2-suffix) | 1 | 1 | **yes** |
137	| 4-suffix `{i3,i4,i5,i6}` with exactly 3 in `V` ≡ `{i1,i2} ⊆ V Δ supp(a)` (**2-prefix**) | 1 | 1 | **NO** |
138	| `{i2,i3,i4} ⊆ V` (2-suffix ⊕ 5-suffix) | 2 | 1 | **NO** |
139	
140	`d_eff <= 10` in this stratum iff some `V` carries total gain `>= 2`. Wave 37's `hunt.dext_le10`
141	implemented only rows 1–2 — its own comment, *"no longer suffix can fit"*, is true but irrelevant:
142	the missing shapes do not need the suffix to fit inside `V`. Measured on the candidate:
143	
144	| sector | 3-suffix-in-`V` | 2-suffix-in-`V` | **2-prefix-in-`V`** | disjoint gain-1 pairs |
145	|---|---|---|---|---|
146	| Z-memory | 0 | 144 | **888** | **132** |
147	| X-memory | 0 | 360 | **456** | **84** |
148	| `M_cand` (either sector) | 0 | 360 | 360 | **0** |
