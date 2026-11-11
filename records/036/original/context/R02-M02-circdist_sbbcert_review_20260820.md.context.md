# Source context 2

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/036/original/M02-circdist_sbbcert_review_20260820.md`

Original SHA-256: `6847fb574afd312f3419bc14fc2ef8f8b9dd75ccbc7b5862fc78c46da506d397`

Original lines: 375–396.

375	`1[t_{LZ}(j) < t_{LX}(i)] = 1[t_{RZ}(i) < t_{RX}(j)]` for all `(i,j) ∈ {0,1,2}²` — nine
376	constraints, not 648. **CONFIRM** (value).
377	
378	**The equivalence is false.** The target's derivation (§2.4(1)) reads: "`c_ab` even means the two
379	shared CNOT pairs agree on their order, i.e. either all of `a`'s CNOTs on the overlap precede all
380	of `b`'s, or vice versa — S5 verbatim." The step after "i.e." is a non-sequitur. With shared times
381	`A₁,A₂` for `a` and `B₁,B₂` for `b`, "agree" is `(B₁<A₁) ⟺ (B₂<A₂)`; "all before all" is
382	`max(A) < min(B)` or `max(B) < min(A)`. `A₁=1 < B₁=2 < A₂=3 < B₂=4` agrees but is interleaved.
383	
384	This is not a hypothetical. Searching legal 12-layer translation-invariant gross schedules I found
385	one in seconds:
386	
387	```
388	LX(left)=[11,10,3]  LX(right)=[7,5,8]  LZ(left)=[6,8,5]  LZ(right)=[2,1,10]
389	legal (all four 6-element unions distinct);  (MC) violations 0 / 648
390	SBB non-interleaving violated on 4 of the 9 monomial classes  = 288 / 648 pairs
391	```
392	
393	So **(MC) ⇏ non-interleaved**. The converse *does* hold (non-interleaved ⇒ each pair separated ⇒
394	`c ∈ {0,2}`), which is the in-house Prop. 3.3 the target also cites.
395	
396	**Consequences.** §5's "single highest-leverage consequence" — "*if (MC) is indeed equivalent to
