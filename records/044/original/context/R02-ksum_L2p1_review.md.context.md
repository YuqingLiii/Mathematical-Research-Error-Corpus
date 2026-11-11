# Source context 2

Source: `[PROJECT]/artifacts/ksum_L2p1_review.md`

Original SHA-256: `762104d2b1cd81ae0280dcbf48f25c4f789628775ea26d3e4ae0f2e7df0dc6b0`

Original lines: 128–134.

128	### P4 statement and proof plan
129	
130	**The statement is syntactically well quantified but mathematically false as written.** Fixed constants (\eta,c_0,\delta), all (3\le q\le N), all targets, and one witness per ((N,q,t)) give a meaningful family and make “pure high degree (\Omega(\sqrt Nq^\eta))” precise up to integer rounding. The missing restriction (0<\delta<2/3) is minor because correlation is at most one.
131	
132	The fatal cap contradiction is immediate. At (q=N), the demanded degree is (\Omega(N^{1/2+\eta})), strictly larger than (N^{2/3}) for every (\eta>1/6). The range-independent Johnson/Tani walk gives (Q=O(N^{2/3})), and every (T)-query algorithm yields a degree-(2T) approximant after choosing a fixed error convention. This conflicts with the reviewed walk cap, independently of U1. For the target (\eta=1/4), the uncapped formula is compatible only through (q\le N^{2/3}). A corrected uniform statement must include (\min\{\sqrt Nq^\eta,N^{2/3}\}), or explicitly restrict (q\le N^{1/(6\eta)}).
133	
134	The proof plan is coherent as a list of the right obstacles—pair-lattice kernel, conditioning, fixed-point factor, norm/correlation control, full-basis lift—but it is not yet a constructive argument. Conditioning on total occupancy is exactly where low-degree cancellation can fail, and no kernel or Christoffel estimate is supplied. After the cap repair it is a plausible research program, not an argument sketch strong enough for CONJECTURED.
