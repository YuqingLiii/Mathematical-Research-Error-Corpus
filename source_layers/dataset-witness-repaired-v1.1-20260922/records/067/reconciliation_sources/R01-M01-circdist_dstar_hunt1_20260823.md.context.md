# Source context 1

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/067/original/M01-circdist_dstar_hunt1_20260823.md`

Original SHA-256: `d6d104c20d28c3fe29a3dd2cf53cfe50f3cc3cadc852e46c6ea00fc5ff4f4671`

Original lines: 173–188.

173	* legal = True; **(MC) violations 0 / 648**; globally interleaved; **384 / 648** pairs interleaved
174	  on the overlap; 648 / 648 interleaved as whole checks.
175	* hook classification of the 2-suffixes: **72/72 diagonal, 0 horizontal, 0 vertical** in *both*
176	  sectors (0 vertical is Theorem 1 discharging itself).
177	* weight-≤10 configurations from the weight-12 pool: **0** in both sectors.
178	* Z-memory: **0 / 144** canonical `gamma` have `repair = 0`. X-memory: **0 / 360**.
179	* the 3-representative shortcut is exact: `0/6 × 24 = 0/144` and `0/15 × 24 = 0/360`.
180	* the audit also ran the **multi-round** (LIFT′) certificate test, 2 round-groups, on **all 504**
181	  canonical `gamma`: **0** admit `repair = 0`. (3-group untested.)
182	
183	### 6.2 What is missing before this is a witness — stated precisely
184	
185	1. **`d_eff = 11` is not certified.** Only the weight-12-pool disqualifier is clean. Uncovered:
186	   `|gamma| <= 10` arising from weight-14 logicals, or from overlapping residual configurations
187	   (`Σ|E_i| = |V| + 2m`, `m >= 1`). Weight-13 is now **provably empty** (§2, even weight). Closing
188	   this is exactly the campaign's 990-slot SAT machinery, per sector.
