# Source context 1

Source: `[RESEARCH_GRAPH]/grothendieck-group-orbit/reviews/spectral-classification-review-20260907.md`

Original SHA-256: `7e21414c47cf8deab81b494ff31ba74fecbb02177c0b1fbc7f9abd2a9ec66941`

Original lines: 147–166.

147	The defect is confined to the final sentence in the exact node claim:
148	
149	> the minimum real vector dimension among such strategies is the minimum rank of a feasible H.
150	
151	The claim quantifies over arbitrary nonzero `A`. Such strategies and feasible
152	weights need not exist. For the already registered `A=diag(2,1)`, `r=1` and
153	`U=V=(1,0)^T`. Every scalar weight has diagonal `(h,0)`, which cannot equal
154	`(1,1)`. Thus the spectrahedron is empty and there is no minimum real vector
155	dimension or minimum feasible rank under the usual meaning of minimum.
156	GOC-T3 correctly supplies the phrase “Whenever it does” before discussing
157	strategies, but that restriction was lost in the node claim. The report does
158	not interpret this imprecision as refuting the equality parametrization.
159	
160	Minimal repair: replace the final clause with “if the feasible set is
161	nonempty, the minimum real vector dimension among such strategies is the
162	minimum rank of a feasible H.” An alternative is to define both quantities
163	as `+infinity` when the feasible set is empty, but that convention must be
164	explicit. This is a FAIL for unconditional completion of the exact reviewed
165	claim, with PASS for its equality-iff part and its conditional dimension
166	formula. No revised statement hash is certified by this report.
