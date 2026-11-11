# Source context 1

Source: `[PROJECT]/paper/evidence_to_overclaim_iclr2027/dataset-clean/records/038/original/M01-circdist_cplx_islandv_20260820.md`

Original SHA-256: `c62e0d2c83f348a4bc8aa90f4807819a7c40834d30aea4298077b948f63be78e`

Original lines: 236–249.

236	**Proposition 5 (prescribability, CONJECTURED).** Fix a line `L = {0,u_1,u_2,u_3} ≤ S` and a set of
237	checks on it — necessarily disjoint cosets `B_i + L` of the qubit-column set. Write
238	`φ_r(i) ∈ Log` for the class label of check `i` at `u_r` relative to a reference section chosen with
239	`z(u_3) = z(u_1)+z(u_2)`. Then
240	
241	1. **`φ_1(i) + φ_2(i) + φ_3(i) = 0` is forced** — not a design choice. *Proof:* the three "cross"
242	   4-sets `W^r_{ij} = {B_i, B_i+u_r, B_j, B_j+u_r}` satisfy `W^1_{ij}+W^2_{ij}+W^3_{ij} = χ_{c_i} +
243	   χ_{c_j} ∈ S_X`, so the three class-differences sum to `0`; the same for the labels. ∎
244	2. **The only relations that can be imposed are `φ_r(i) = φ_r(j)`**, and each is imposed by
245	   declaring the single weight-4 X-check `W^r_{ij}` (a legal coset 4-set) to be a stabiliser — a
246	   *connector*. Any consistent system of such relations is realisable, and everything not forced is
247	   generically independent in `Log`.
248	3. Consequently the realisable label systems on a line are exactly the triples of partitions
249	   `(Π_1,Π_2,Π_3)` of the checks with `Π_a ∧ Π_b = Π_1∧Π_2∧Π_3` for all `a ≠ b`.
