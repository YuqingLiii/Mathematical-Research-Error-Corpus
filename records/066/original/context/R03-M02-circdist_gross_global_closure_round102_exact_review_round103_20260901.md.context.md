# Source context 3

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/066/original/M02-circdist_gross_global_closure_round102_exact_review_round103_20260901.md`

Original SHA-256: `4ddb4f4bc966a5c930066409cb267aea30d3b3bb68a45529e1174052ccd7e361`

Original lines: 349–379.

349	## 8. Scientific retraction and adversarial counter-scenario
350	
351	Let `B_185` be the first outer base with 330 selectors and the untranslated 14,484 block registry. Its exact CNF has 416,062 variables, 1,417,374 clauses, and SHA-256 `ddd40740b42854b74de7d64e3899f017a58a56223b3fa560d15845a9f7cae6c9`. Let `L` be the conjunction of the 71 translation lex leaders.
352	
353	I independently launched a fresh CaDiCaL solve of `B_185`, outside the proposer ledger. It returned `rc=10/SAT` in about 3.42 seconds with empty stderr. I parsed exactly 416,062 assignment literals, checked the exact variable domain, and satisfied all 1,417,374 clauses. The decoded legal raw schedule has SHA-256 `50e84c565d1ff4191a3fa48c22f0d4509ec072645540cb791e7acc3c33e8f148`; rank compression gives SHA-256 `1b68d1beb7c2205d7def84e5f1560340523d095be60ae348d27b58523f3df513`, 144 layers.
354	
355	I then enumerated all 72 translated raw schedules and evaluated every original block and selector directly:
356	
357	* exactly one translate survives `B_185`, the identity `(0,0)`;
358	* the orbit’s lexicographically least raw vector occurs at `(1,5)`;
359	* that least translate has raw schedule SHA-256 `01ced0f703ea1bf21c6c9a07d963f7514eaa85bbfd16ab4373a2635340c51087`;
360	* it hits 75 installed block cuts and zero selectors; and
361	* its first hit in registry order is `r69-Xerr-2-8-19`.
362	
363	Therefore this base orbit contains no member satisfying both the original base and all lex leaders: its only base survivor is not least, and its least member is not a base model. The failed proof step is
364	
365	\[
366	B_{185}(S)\Longrightarrow B_{185}(\delta S),
367	\]
368	
369	which is false because the registry was not invariant. This is a concrete refutation of the orbit-canonicalization claim. It does not assert that `B_185 ∧ L` is UNSAT; the package’s different exploratory assignment proves it SAT. It establishes that the quotient has no licensed orbit-wise coverage or UNSAT lifting theorem.
370	
371	I also checked the three package schedules against the old registry over all translations:
372	
373	| orbit | old-base-surviving translates / 72 | least-translate old cut hits |
374	|---|---:|---:|
375	| iteration-184 schedule after its two cuts | 0 | 159 blocks / 0 selectors |
376	| exploratory schedule | 1 | 0 / 0 |
377	| corrected schedule | 72 | 0 / 0 |
378	
379	The exploratory quotient encoding itself is internally exact: its raw quotient SHA-256 is `496ca65f5e9a6b6c24fc1050123f1f0850ecbbfb2219fb09e9606ec7055800d6` (physical compressed-bit artifact SHA-256 `c0af79e4110f54a2388502a201973833c7c470ef15db9cbce302cecc10602871`), with 1,029,502 variables and 6,324,965 clauses. Its complete assignment satisfies all clauses; its decoded schedule has raw SHA-256 `5b4f340bb40e25d84d49db2f19df2a172632b316b7e8e39e97ba3ac910d8915e`, compressed SHA-256 `2c8ce90954f7439947a6988d5a536533a44aeb6c3eda1ff5627a029790c8e958`, 548 layers, orbit size 72, and stabilizer size 1. Those are point facts, not coverage facts.
