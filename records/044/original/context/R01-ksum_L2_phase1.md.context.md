# Source context 1

Source: `[PROJECT]/artifacts/ksum_L2_phase1.md`

Original SHA-256: `8436994bee0c4f9c125cd2a276d0b04048f65ebcd6ca111f1e18647c9e0e4cc3`

Original lines: 183–211.

183	## 5. P4 — first asymptotic lemma now owed
184	
185	**Conjectured joint-histogram witness lemma.** There exist constants
186	\(\eta>1/6\), \(c_0>0\), and \(\delta>0\) such that, uniformly for
187	\(3\le q\le N\) and \(t\in\mathbb Z_q\), there is an
188	\(S_N\times C(\sigma)\)-invariant signed measure
189	\(\mu_{N,q,t}\) on \((\mathbb Z_q)^N\) satisfying
190	\[
191	 \|\mu_{N,q,t}\|_1=1,\qquad
192	 \langle\mu_{N,q,t},F_{N,q,t}\rangle\ge\frac13+\delta,
193	\]
194	and
195	\[
196	 \langle\mu_{N,q,t},p\rangle=0
197	 \quad\text{for every query polynomial }p
198	 \text{ of degree }<c_0\sqrt N\,q^\eta.
199	\]
200	The target value is \(\eta=1/4\). Any fixed \(\eta>1/6\) is already the route's required advance.
201	
202	### Proof plan only
203	
204	1. Work in the falling-factorial generators \(P_{u,v},Q_s\), keeping the filtration equal to query degree by the exact symmetrization map (1).
205	2. Construct a signed finite-band kernel on the pair-count lattice \((i,j)\), then symmetrize it over two-cycles and condition on total occupancy \(N\). The local kernel must distinguish the NO boundary \(ij=0\) from the YES interior \(ij>0\); a scalar total \(i+j\) cannot do this.
206	3. Use discrete orthogonal polynomials on occupancy slices to annihilate all generator products below degree \(D\). Prove that conditioning on \(\sum_a n_a=N\) preserves the required moment cancellations rather than reintroducing low-degree leakage.
207	4. Treat fixed points as a separate \(Q_s\) factor and obtain constants uniform in the cycle type \(\tau\); the \(\tau=0\) and \(\tau>0\) cases cannot be identified by target relabeling.
208	5. Bound the class-weight \(\ell_1\) norm and the signed mass on the YES/NO boundary by a discrete Christoffel-function or extremal-polynomial estimate, aiming for \(D=\Omega(\sqrt N\,q^\eta)\).
209	6. Lift class weights uniformly to inputs and verify pure high degree against the full one-hot query basis, not only against a chosen generator list.
210	
211	This lemma is the node's next obligation. No step above has been proved here.
