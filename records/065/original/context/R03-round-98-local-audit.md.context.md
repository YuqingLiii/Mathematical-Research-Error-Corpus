# Source context 3

Source: `[HOLEVO_PROJECT]/outputs/round-98-local-audit.md`

Original SHA-256: `94ba0af84ffaa6676503fcff1428548ba3b2781fa330e28610f55bf082568d0c`

Original lines: 60–67.

60	Strict separate-row rounding gives `B_row<=2,954,642>M_global`, so that relaxation does not certify a packet survivor. The load-bearing coupled inequality gives `sum_i m_i<=154,350`, `B_coupled<=308,700`, `(N,G,Q,R)=(961,616,82,684,640,86,531,104,885,730,920)`, and exact positive margin `2,709,464,443,485,056`.
61	
62	## Response correction
63	
64	The frozen Round 98 prompt contains two erroneous non-load-bearing raw-size-four entries: rows `3` and `9` were sent as `14,928,318`, while the correct exact values are `14,926,862`. The displayed global size-four total `175,037,248` was already correct. The error arose when a bare textual replacement of `6862` by `8318` unintentionally changed digits inside `14926862`.
65	
66	The public response identified the discrepancy, regenerated both affected rows with a separate count-only enumerator, and used the corrected vector. The correction does not alter `K`, the formal supports, the size-two packet stream, `M_global`, or either load-bearing support-loss bound. No other supplied mathematical value required correction.
67	
