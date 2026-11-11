# Source context 3

Source: `[RESEARCH_GRAPH]/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md`

Original SHA-256: `7e21414c47cf8deab81b494ff31ba74fecbb02177c0b1fbc7f9abd2a9ec66941`

Original lines: 187–208.

187	For `A=0`, the value statement also holds and every feasible strategy is
188	optimal. The exact claim nevertheless states, without a nonzero restriction,
189	that the value is “attained by normalized rows of paired top left and right
190	singular bases.” With a rectangular zero matrix the full top left singular
191	space is `R^m` and the full top right singular space is `R^n`. When `m!=n`,
192	these spaces cannot have bases with a common column count, as required by
193	the dossier's definition of paired bases.
194	
195	For example, take `A=0` of size `1 by 2`, with the two-element group acting
196	trivially on the single row and transitively on the two columns. All stated
197	equivariance and transitivity hypotheses hold, but the full zero-singular
198	spaces have dimensions one and two. A thin SVD would select only a subspace
199	on the larger side and would not be the defined pair of full top spaces;
200	an arbitrary such choice can also have a zero row, so normalization is not
201	an automatic repair.
202	
203	Minimal repair: retain the value equality for all `A`; say that for `A!=0`
204	it is attained by normalized rows of paired top singular bases, while for
205	`A=0` every feasible strategy is optimal. The exact reviewed claim fails the
206	well-posed construction requirement. Its optimum-value theorem and its
207	nonzero construction pass. This finding does not claim a counterexample to
208	the optimum-value equality.
