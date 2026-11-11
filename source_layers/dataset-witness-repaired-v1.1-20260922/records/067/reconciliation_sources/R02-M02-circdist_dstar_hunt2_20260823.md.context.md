# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/067/original/M02-circdist_dstar_hunt2_20260823.md`

Original SHA-256: `01f9e79226495ad837ecb8fa08066b4d96a2d7078e385d5831d827ddb6ba82da`

Original lines: 65–93.

65	`a`, `C_a` = their XOR, `D = ⊕_a C_a`, `T = V Δ D` the singletons. Then
66	
67	```
68	cost = K + |V Δ D| = |V| + Σ_a (n_a − ρ_a) + loss_in + gain_out ,   ρ_a = |C_a ∩ V| ,
69	loss_in = 2·#{q ∈ V : cov(q) ∈ {2,3}} ≥ 0 ,   gain_out = #{q ∉ V : cov(q) odd} ≥ 0 .
70	```
71	
72	* **Reduction R1 (proved).** A 6-suffix is `supp(a) ∈ rowspace(H_X)`. Deleting it and replacing `V`
73	  by `V Δ supp(a)` (same nontrivial class) leaves `T` untouched and lowers the count by exactly 1.
74	  So no optimal configuration contains a 6-suffix.
75	* **Reduction R2 (proved).** A 1-suffix has the same support as a singleton, and
76	  `U(1-suffix) ⊆ U(singleton)`, so the singleton dominates it for both `d_ext` and `repair`.
77	* **Drop lemma (proved).** Removing check `a` changes the cost by at most `+(|C_a| − n_a)`, so
78	  every contributing check may be assumed to have `|C_a| − n_a >= 1`. Enumerating subsets of
79	  `{2,3,4,5}` leaves exactly **7 options per check**.
80	* **Bound 1 (proved, and the useful one).** For every nontrivial logical `V` and every check `a`,
81	  `V Δ supp(a)` lies in the same nontrivial class, so `|V| + 6 − 2|V ∩ supp(a)| >= d = 12`, i.e.
82	  **`|V ∩ supp(a)| <= (|V| − 6)/2`** — in particular `<= 3` at `|V| = 12`. (Wave 37 recorded the
83	  `<= 3` fact as a measurement; it is a two-line consequence of `d = 12`.) Verified: max over the
84	  complete pool is exactly 3 in both sectors.
85	
86	**Scope of the exhaustion, stated exactly.** The stratum decided is `|V| = 12` (the complete
87	1884-element weight-12 nontrivial-logical pool per sector, re-expanded and re-validated here from
88	the seed files; completeness of that pool is inherited from the wave-36 exhaustive enumeration),
89	with at most `j <= 4` distinct contributing hook checks, drawn from checks meeting `V`. Within
90	that stratum the search is exhaustive by construction (7 options per check, an admissible
91	`γ`-sorted pruning bound `Σγ >= 12 − W`, `γ_a = ρ_a − n_a <= 2`). Strata `|V| >= 14` are **not**
92	decided; that is the campaign's `|E| ∈ {14,…,30}` cell family and it needs the SAT pipeline.
93	
