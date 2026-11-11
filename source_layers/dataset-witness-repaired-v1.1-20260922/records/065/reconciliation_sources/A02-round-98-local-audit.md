# Round 98 local audit

## Outcome

The Round 98 public response independently reconstructs the finite-slope candidate and the local exact checks reproduce its load-bearing certificate. The separate-row relaxation is insufficient, while the coupled support-loss route is strict:

```
GenericTheta300236Exclusion
M_global = 1,270,316

separate-row relaxation:
  B_row <= 2,954,642 > M_global
  status: insufficient

load-bearing coupled certificate:
  sum_i m_i <= 154,350
  B_coupled <= 308,700
  (N,G,Q,R) = (961,616,82,684,640,86,531,104,885,730,920)
  cleared margin = 2,709,464,443,485,056 > 0
```

The globally matched-packet certificate gives `Delta_ray + Delta_flat > 8,318 E` inside the contrary branch for the stated centrally symmetric twelve-slope ansatz. Together with the audited four-slack identity and strict target estimate, this excludes an exact baseline in that ansatz at `theta=300236`.

The unconditional conclusion is that the total four-slack sum is at least `8,318 E`; the strict two-slack inequality is used only inside the contradiction branch. The result is not PW10, a phase-uniform theorem, a general baseline exclusion, or a result for the arbitrary one-defect/full ratio-two classes. `GenericTheta300236Exclusion` remains `CONJECTURED` pending replication outside this proof-development context.

## Public receipt and bundle boundary

- Conversation URL: `<private-chat-link-removed>`
- Visible model and tier: `5.6 Pro`
- Public response normalized from the authenticated conversation API: `artifacts/web-gpt56sol-pro/round-98-response.md`
- Response SHA-256: `ac77ae7c6f36bab52b19527625c2ffdf288ddedf0a020b45ed689ed2c4c0d72a`
- Response size: `20,927` bytes; `855` newline characters
- Authenticated API raw response SHA-256: `c2b3509980f5c2b1d0b9e2bb3aa7430dca17e0c77fed63797faf2f7ad81e6205`
- Exact URL receipt SHA-256: `fb0d85b666ee7a02c0fa3b61709f652ccec07669eb3b3c4318ce334a5cf115e3`
- Exact sent-prompt SHA-256: `3ff85ab484db1fc135688b573143ce8702274f0d53fcf6836b5c8d0d7c792cc4`
- Dispatch receipt SHA-256: `2ca33f30e44e9655695115fc1f4db8c0232df4c0d51be4f89a9fda166e7831f8`
- Response-declared global-stream SHA-256: `b53835079c11794e563c9864861b170df5f563c4464043e5379ed42ca4362752`
- Response-declared bundle SHA-256: `faaeee33399b894e8ef85dbc13aa8103f4b582f125969153d9c74723ce6b1787`
- Post-receipt verifier SHA-256: `ecf1fe754c67e2ae9a764626c229424705dd97b4ea82bd165d0081ca0673d065`

The frozen response bytes are anchored to the authenticated conversation API raw message plus a deterministic conversion of display-math delimiter lines from `\[`/`\]` to `$$`; the verifier proves that normalization exactly. This is not represented as an independently persisted clipboard-byte comparison. The response reports a ZIP inside its own sandbox and a matching digest, but no local Round 98 ZIP receipt was captured here. Its ZIP, stream digest, and runtime-generated source receipts remain public-response claims; the conclusion below relies on the independent local regeneration.

## Independent exhaustive replication

- Source SHA-256: `edce43fdaa63d190e2b53b5b8ce93a7edb1ea180c4da9b344cad4ffc91c1b612`
- Compiled binary SHA-256: `2780b598485edbd5f194f0e6fc3648860d7d1ccb0b839ca0b63ef1a77126024e`
- Exhaustive log SHA-256: `1ab74c3ca3f0d3713388c793e4ec6d9a077ac59cdbf56f91c3ebe2b66f35f782`
- Three-execution record SHA-256: `f0a079b7541fece8c77ded222a33f4088c079caa3d32ef5220732ed7a598e36f`
- Arithmetic verifier SHA-256: `edc12159453bdb44e5da1cf11223434902b6ee5c05f9026044b8880c83fa251b`
- Arithmetic log SHA-256: `1fe61aaf6782ba4ff46cf6f167c901a07b1fde4d6639a8b5c237fd0deb663b5d`

Three complete C++ executions emitted the same exhaustive log. A fresh exact-arithmetic execution agrees byte-for-byte with the saved arithmetic log. The post-receipt verifier passes. The exhaustive run reproduces `206,417,296` genuine size-two Laurent binomials, `171,608,104` positive and `34,809,192` negative relative signs, zero collected size-two `+/-2` monomials, zero zero Laurent polynomials, and all seven moment checksums.

The per-row key census has `18,148,962` unique combined-sign keys and `18,316,897` sign-expanded records. The global merge reproduces `8,007,270` canonical keys, `172,923` keys carrying both signs, `1,270,316` opposite-sign matches, maximum per-key match `1,152`, key checksum `19634280408065343339642080`, and multiplicity checksum `1656756186934360`. The singleton total is `82,993,340`. Rowwise matching alone gives `599,476`, so the cross-row gain is `670,840`.

## Exact range and support-loss checks

Rearrangement over all 286 ten-row subsets gives `-3,727,755 <= t <= 3,727,803` with the same exact minimizing and maximizing ten-row sets. For `K=970,338,792`, `H=8,318`, and `S_min=53,624,480`, denominator `80` is valid and `81` fails.

Strict separate-row rounding gives `B_row<=2,954,642>M_global`, so that relaxation does not certify a packet survivor. The load-bearing coupled inequality gives `sum_i m_i<=154,350`, `B_coupled<=308,700`, `(N,G,Q,R)=(961,616,82,684,640,86,531,104,885,730,920)`, and exact positive margin `2,709,464,443,485,056`.

## Response correction

The frozen Round 98 prompt contains two erroneous non-load-bearing raw-size-four entries: rows `3` and `9` were sent as `14,928,318`, while the correct exact values are `14,926,862`. The displayed global size-four total `175,037,248` was already correct. The error arose when a bare textual replacement of `6862` by `8318` unintentionally changed digits inside `14926862`.

The public response identified the discrepancy, regenerated both affected rows with a separate count-only enumerator, and used the corrected vector. The correction does not alter `K`, the formal supports, the size-two packet stream, `M_global`, or either load-bearing support-loss bound. No other supplied mathematical value required correction.

The frozen prompt, staging artifact, and sent artifact are preserved exactly and are not silently rewritten. Future prompt construction applies complete array blocks rather than bare numeric substitutions, and the pre-send verifier checks every support, singleton, size-two, size-three, and size-four vector.

## Next exact gap

The earliest not-yet-covered admissible value is `theta=300237`. A fresh independent local census gives

```
K = 970,336,236
H = 5,762
M_global = 1,296,616
singleton total = 82,989,972
rowwise match total = 607,100
```

At this value the separate-row relaxation again fails: `B_row<=2,038,098>M_global`. The coupled weighted inequality is load-bearing and gives `sum_i m_i<=106,470`, `B_coupled<=212,940`, `(N,G,Q,R)=(1,083,676,82,777,032,87,111,736,885,391,852)`, and exact positive margin `3,088,424,244,608,256`.

The exact assignment range is `-3,727,767 <= t <= 3,727,815`. The run has `206,416,856` genuine size-two records, `171,607,708` positive and `34,809,148` negative relative signs, `7,994,654` global keys, `179,107` keys carrying both signs, maximum per-key match `1,152`, global key checksum `19584392289209264874621128`, multiplicity checksum `1653160977174684`, and key ranges `0 <= Delta Q_6 <= 22,479,428` and `-72 <= Delta Q_r <= 72`.

The Round 99 source SHA-256 is `f96c65e44427273d1a6065716d068638479a77c9fe394a7a6f775c6fe2c1a20c`; compiled binary SHA-256 is `5d1c8a457db19f0ec782cd620dd0969c498d9627d78484e6277f766f3f51c2a4`; exhaustive-log SHA-256 is `0649ce7878526240f0dd67f71b9ddef1811514083f5f254f43bfacf2aa447108`; three-execution record SHA-256 is `3e5efc127cba93db7a885be6852ebd7e89e9423f75f02a736dd524e47da85d4b`; arithmetic-verifier SHA-256 is `2f7de52114fff5c4d42e797ec0df8e365bfb84ed0ca980f7fec5675ce60ded4b`; arithmetic-log SHA-256 is `d1535b3720e0bce6f66f7a63a8e34f9b6d9e914b7e620757401b38fc976fd255`. This next candidate requires independent browser-side reconstruction before promotion.

## Status boundary

Round 98 establishes a new independently regenerated strict finite-slope lemma at `theta=300236`, with the two non-load-bearing row counts corrected as recorded above. The exact baseline, frozen-edge vector, physical liftability of `x^(10)`, full-size theorem, and PW10 remain open. No canonical proof state is changed.
