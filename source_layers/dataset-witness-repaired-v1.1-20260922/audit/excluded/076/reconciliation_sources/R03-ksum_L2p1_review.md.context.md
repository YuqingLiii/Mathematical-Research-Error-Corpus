# Source context 3

Source: `[PROJECT]/artifacts/ksum_L2p1_review.md`

Original SHA-256: `762104d2b1cd81ae0280dcbf48f25c4f789628775ea26d3e4ae0f2e7df0dc6b0`

Original lines: 102–112.

102	### Error convention and corrected finite interpretation
103	
104	For sign approximate degree, the submitted test “correlation (>1/3)” correctly certifies (\widetilde{\deg}_{1/3}(F)\ge d). It does **not** directly imply (Q_{1/3}(F)\ge d/2). A (T)-query algorithm with output error (e) has a degree-(2T) expected-sign polynomial of uniform error (2e), so direct error-(1/3) exclusion requires correlation (>2/3). At that threshold the logged table re-grades to:
105	
106	| Case | single degree certified for direct error-1/3 polynomial test | joint degree certified |
107	|---|---:|---:|
108	| (3,3,0) | 0 | 2 |
109	| (4,3,0) | 0 | 2 |
110	| (5,4,1) | 2 | 3 |
111	
112	Degree zero means only that this LP supplies no positive-degree certificate at the strict (>2/3) threshold; it is not a claim that the function has degree zero. The original degrees 3,4,4 still yield an asymptotic quantum lower bound up to a larger constant by first amplifying a (1/3)-error algorithm to error below (1/6); they do not carry the claimed direct factor (1/2).
