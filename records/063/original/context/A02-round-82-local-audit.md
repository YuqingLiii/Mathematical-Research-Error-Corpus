# Round 82 local audit

## Outcome

The Round 82 public response's load-bearing finite-slope claim is independently reproduced:

```text
GenericTheta300219Exclusion
sum_i m_i <= 133,183
B_coupled <= 266,366
M_global = 1,278,684
N = 1,012,318
G = 82,725,646
35*G*N - 7,190*102*(G+4*N)
  = 2,867,424,128,397,140 > 0
```

The coupled weighted support-loss and globally matched-packet lemma therefore gives `Delta_ray + Delta_flat > 7,190 E` inside the contrary branch for the stated centrally symmetric twelve-slope ansatz. Together with the audited four-slack identity and strict target estimate, this excludes an exact baseline in that ansatz at `theta=300219`.

The independent separate-row relaxation fails: its bad-coordinate budget is `2,549,446>M_global`, so it certifies no surviving packet and has cleared comparison `-58,994,969,053,080<0`. The coupled estimate is load-bearing.

The unconditional conclusion is that the total four-slack sum is at least `7,190 E`; the strict two-slack inequality is used only inside the contradiction branch. The result is not PW10, a phase-uniform theorem, a general baseline exclusion, or a result for the arbitrary one-defect/full ratio-two classes. `GenericTheta300219Exclusion` remains `CONJECTURED` pending replication outside this proof-development context.

## Public receipt and bundle boundary

- Conversation URL: `<private-chat-link-removed>`
- Visible model and tier: `5.6 Pro`
- Exact browser-copied response: `artifacts/web-gpt56sol-pro/round-82-response.md`
- Response SHA-256: `dd9829e71b5f78953a741f544b6e03135404eeb4dda02c49c7a320e654fae0f8`
- Response size: 25,171 bytes; 1,118 newline characters
- Exact URL receipt SHA-256: `fb0d85b666ee7a02c0fa3b61709f652ccec07669eb3b3c4318ce334a5cf115e3`
- Exact sent prompt SHA-256: `85ea8df0321a23ac6fd8aef914646fa6dff14b571e2f5a7eaa155c0524ddb97d`
- Response-declared bundle SHA-256: `c7f1cc5c3b6546c2e935141f971b00d9237ecf0f025dd297cb4543fe8dfc4f7c`
- Post-receipt verifier: `work/verify_round82_response.py`
- Post-receipt verifier SHA-256: `0abc124a3e55306ca66a61073caf2ecc3600375d652fb2166c705859cf6842ba`

The response text was copied directly from the controlled browser and independently hashed; the clipboard bytes and saved file compare exactly. The response-declared ZIP is represented only by sandbox attachment links and no local ZIP receipt was captured. Its digest and the response's runtime-generated source receipts are public-response claims; the conclusion below relies on the independent local regeneration.

The response says that the exact Round 81 browser byte stream was unavailable in its own runtime and labels its bundled Round 81 file as a reconstruction. This is an accurate boundary on that browser runtime's evidence. The separate local Round 81 byte receipt remains archived outside that bundle and is not needed for the Round 82 mathematical conclusion.

## Independent exhaustive replication

- Source: `work/explore_round82_global.cpp`
- Source SHA-256: `43d190771896e6a9f62096b254b08aace475e91c7f47e8aeac0129f54db2f224`
- Exhaustive log: `work/round82-exploratory-global.log`
- Log SHA-256: `f74ede02ecd6289798f180fedddd014df68e0fab2f9abeed89c505a3e8ecfd45`
- Arithmetic verifier: `work/verify_round82_global_budget.py`
- Verifier SHA-256: `19b035ae9e60ffbe521123607ff424becd106a22e590ff396b9796f9c8394de4`
- Arithmetic log: `work/round82-global-budget.log`
- Log SHA-256: `9dfd137cdfcf7e3332d735ab80d00604155af5305fd9d2a319889e214b725b67`

Three complete C++ executions emitted the same exhaustive log. A fresh exact-arithmetic execution agrees byte-for-byte with the saved arithmetic log. The post-receipt verifier also passes. The exhaustive run reproduces all thirteen formal supports and low-fiber histograms, `206,416,968` genuine size-two Laurent binomials, `171,607,544` positive and `34,809,424` negative relative signs, zero collected size-two `+/-2` monomials, zero zero Laurent polynomials, and all seven moment checksums.

The global merge reproduces `8,003,524` canonical keys, `174,962` keys carrying both signs, `1,278,684` opposite-sign matches, maximum per-key match `1,152`, key checksum `19618180552045238370105676`, and multiplicity checksum `1655672247452000`. The singleton total is `82,992,012`. Rowwise matching alone gives `601,184`, so the cross-row gain is `677,500`.

## Exact range and support-loss checks

Rearrangement over all 286 ten-row subsets gives

```text
-3,727,551 <= t <= 3,727,599
```

with minimizing rows `{0,1,2,3,4,5,9,10,11,12}` and maximizing rows `{0,1,2,3,7,8,9,10,11,12}`.

For `K=970,337,664`, `H=7,190`, and `S_min=53,624,480`, denominator `86` is valid and `87` fails:

```text
(K-H)*S_min - H*86^2*K = 433,588,256,836,160 > 0
(K-H)*S_min - H*87^2*K = -773,385,653,283,520 < 0.
```

Strict separate-row rounding gives `B_row<=2,549,446`, which is larger than `M_global=1,278,684`; this route fails.

The coupled weighted inequality has numerator `50,069,305,895,868,822,873,047,040` and denominator after multiplying by `S_min` `375,941,799,771,515,432,000`. Adjacent-integer tests give `sum_i m_i<=133,183` and `B_coupled<=266,366`. This yields `(N,G,Q,R)=(1,012,318,82,725,646,86,774,918,885,587,382)` and margin `2,867,424,128,397,140>0`.

## Response correction

No supplied `theta=300219` mathematical value required correction. The browser response's exact counts, checksums, inequalities, and stated evidence boundary agree with the local audit.

## Next exact gap

`theta=300220` is not an unresolved support failure. Round 51 already independently reproduced

```text
K(300220) = 970,330,348
970,330,473 - (K(300220)-1) = 126,
```

so the formal-support upper bound already covers that value inside the finite-slope ansatz. The earliest not-yet-covered admissible value is therefore `theta=300221`, not `theta=300220`.

A fresh local `theta=300221` exhaustive census gives `K=970,338,504`, `H=8,030`, `M_global=1,349,404`, and singleton total `82,992,952`. The separate-row budget `2,851,442` fails, while the coupled inequality gives `sum_i m_i<=148,959`, `B_coupled<=297,918`, `(N,G,Q,R)=(1,051,486,82,695,034,86,900,978,885,540,498)`, and exact positive margin `2,972,166,353,177,660`. This next candidate requires independent browser-side reconstruction before promotion.

## Status boundary

Round 82 establishes a new independently regenerated strict finite-slope lemma at `theta=300219`. The exact baseline, frozen-edge vector, physical liftability of `x^(10)`, and PW10 remain open. No canonical proof state is changed.
