# Final release QA — Grothendieck records

Date: 2026-09-22

Target: `paper/evidence_to_overclaim_iclr2027/dataset-final-v1-20260922`

Scope: records 053, 054, 056, 071, 072, 073, and 077 only. This is final-package consistency QA against the completed reconciliation, not a fresh mathematical audit or corpus-wide count determination.

## Verdict: PASS

The corrected final build passes the checks below. One stale mechanism label in 071 was found during QA, reported to the release builder, and corrected before this verdict. No outstanding bug remains within this bounded QA scope.

| Record | Final placement | Materials with verified SHA-256 | Local reconciliation windows | Result |
|---|---|---:|---:|---|
| 053 | `audit/excluded/053/` | 5 | 3 | PASS |
| 054 | `audit/excluded/054/` | 8 | 4 | PASS |
| 056 | `records/056/` | 17 | 4 | PASS |
| 071 | `records/071/` | 9 | 3 | PASS |
| 072 | `records/072/` | 17 | 4 | PASS |
| 073 | `audit/excluded/073/` | 9 | 3 | PASS |
| 077 | `records/077/` | 8 | 4 | PASS |

## Completed checks

1. **Admission and exclusion agree across representations.** The retained records are present in `index.json`, `records.jsonl`, and `records/`; the excluded records appear only in `excluded.json` and `audit/excluded/`. No record in this scope also has a directory in the opposite admission location. Included `records.jsonl` objects exactly match their corresponding `record.json` objects.
2. **All listed materials exist and match their manifest hashes.** Every material listed in the seven `materials.json` files was checked using SHA-256. Each reconciliation window has the exact original line range specified in `reconciliation_groth.json`; original identifiers are sanitized in the release rather than exposing whole conversations.
3. **Original-excerpt overrides were applied.** For 071, 072, and 077, `original.excerpt` exactly equals the corresponding string in `reconciliation_groth_overrides.json`. Each excerpt is present in its designated source window after removing the added line-number prefix where applicable. The rendered `witness.md` contains the same excerpt after normalizing Markdown blockquotes and display whitespace.
4. **Exclusions are explicit, not unfinished.** Records 053, 054, and 073 have `admission: excluded`, null `overclaim`, `mechanism: excluded_allegation`, and `witness.endorsement: historical_allegation_not_endorsed`. Their rendered files explicitly say that the old allegation is not a positive mathematical-error record. Old allegations remain available as history, not as newly accepted witnesses.
5. **No active pending status was found.** Earlier `prior_package_status` and `superseded_20260922_status` values remain inside the historical adjudication fields. They are labeled as prior/superseded rather than used as the current admission. Narrative references to resolving an old pending state do not make a record pending again.
6. **No complete-internal-CoT claim was introduced.** All seven machine-readable records explicitly state that visible reasoning excerpts/summaries are not asserted to be complete internal chain of thought. Their verification limits also distinguish historical execution from current reruns and do not claim that all target theorems are false.

## Sensitive interpretation checks

- **071:** The direct original quote is the preserved, retired `commutant-classification` route under an all-extremizer parent claim. The release explains a coverage error in that route; it does not invent a literal assertion that all optimizers are invariant. The mechanism field has been corrected from the stale all-invariant formulation to **“受限的不变权重参数化被用作全部极值策略分类路线”**. The witness is scoped to the invalid coverage of that registered route, not to invariant averaging or the repaired classification.
- **072:** The unconditional minimum-rank clause is labeled `contemporaneous_review_quotation`. Its context identifies the target claim hash and explicitly states that this is not recovery of the first writing event. The empty-feasible-set witness is limited to the missing condition on the minimum clause; the conditional rank formula is not called false.
- **077:** The original quote is directly decoded from the archived browser capture: “the attached program settles the entire trivial-isotypic block exactly.” The final record preserves the adjacent OPEN-GAP/global-proof limitations. The original execution output and frozen result show `INCONCLUSIVE`; the accepted allegation concerns the claimed complete decision of this block, not a false assertion that the entire SOS theorem had been proved.

## Non-blocking historical content

Excluded index summaries and `history/` files intentionally preserve the rejected allegations. Their exclusion context and non-endorsement are explicit. No historical source file was altered by this QA, and no new mathematical computation or remote recovery was required.
