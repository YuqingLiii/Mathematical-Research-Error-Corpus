# Independent QEC release QA — 2026-09-22

Scope: records 028–039 and 066–070 (17 records). Review is source/provenance and packaging QA, not a new mathematical rerun.

## Governing reconciliation

- 14 retained: 028–039, 066, 067.
- 3 excluded: 068, 069, 070.
- No open admission decision in this subset.
- Expected overclaim flags: yes for 028, 029, 031, 032, 033, 034, 037, 038, 066, 067; no for 030, 035, 036, 039; not applicable for the three exclusions.

## Build-script inspection

The script loads `reconciliation_qec.json` as governing admission and overclaim decisions. It preserves the old witness separately in `history/`, exports the reconciliation source windows, and explicitly states that deleted temporary assignments for 066 are not surviving fixtures. Those design choices faithfully preserve the reconciliation.

Issues sent to the release owner before the build:

1. `record.mechanism` was inherited from the withdrawn reaudit. For 028 it read “简写定理的继承前提不明”, contradicting the resolved positive verdict. Replace with “安装声明遗漏测量一致性前提”. For 034 the more precise wording is “根组装遗漏轮数前提”.
2. Excluded `record.json` entries still carried the old witness object with `scope=argument_invalid`. The Markdown correctly declined endorsement. Add explicit historical/not-endorsed metadata for the JSON witness too, to prevent machine consumers treating the allegation as a positive witness.
3. The 067 filename `tiled_gapcand_32.json` is historical. Its actual payload has 36 distinct slots, 0–35. Do not infer a 32-slot schedule from its filename. Current adjudication and recorded exact checks correctly concern the 36-slot schedule.

## Mathematical source-fidelity checks

- 028 is the independently installed claim missing MC, not the MC-qualified theorem body. Original legality and the four-qubit witness are both bundled.
- 034 is the old assembly's omitted `R≥d`; the later C-M7 caveat is a repair witness, not evidence that the old assembly already had the condition.
- 068's scalar-voltage allegation is excluded because the same assembly defines the existential/minimum-over-representatives interpretation.
- 069's `k=0` example does not refute the displayed extended-valued min-plus equality. Exclusion must not be described as a missing source.
- 070's full-group condition appears in the same historical YAML's caveats, lines 47–54. The non-group example is outside that condition.
- 066 is retained on its original coverage claim, exact archived audit, and scoped retraction. The archived review explicitly says temporary implementations and outputs were deleted at the time (line 92). No assertion that its exact historical 416,062-literal countermodel assignment is bundled is permitted.
- 067's selected witness is ten faults with XOR support of size twelve, zero syndrome, and nontrivial logical class on the actual frozen schedule. The current fresh check covers this selected witness, not all 144 historical witnesses.

## Artifact inspection — completed

Read the actual generated `dataset-final-v1-20260922` files after the release owner built them.

- All 17 `record.json` admission decisions and overclaim flags match the governing QEC reconciliation exactly.
- All 17 final `witness.md` files contain the governing rationale; all their local Markdown targets resolve.
- Checked all **545 manifest-listed files** in this subset: all are present, all SHA-256 values match, and inherited originals are byte-identical to the compact source archive's local extraction.
- Checked the presence of **46 reconciliation source windows**. Their quoted source selections are those independently reviewed in this task; original/source and auditor roles remain separate.
- The two pre-build metadata issues are fixed: 028/034 now have resolved mathematical mechanisms, and excluded witness objects have `endorsement=historical_allegation_not_endorsed`.
- No retained record's governing `mechanism` or `summary` carries an unresolved/pending classification.
- 068/069/070 are under `audit/excluded/`, not the positive `records/` index, and explicitly say the old allegation is not endorsed.
- 066's final record explicitly says the temporary model assignment was deleted by the original reviewer and is not a surviving assignment fixture.
- 067 retains the actual 36-slot input and distinguishes the one newly checked ten-fault witness from the 144 historical witness checks.

The release owner is adding root-level `checks/witness_checks.json` and runnable checks separately. At this inspection checkpoint, `computational_checks.file` correctly pointed to that planned root-relative location, but the `checks/` directory had not yet been written. This is a packaging completion item, not an evidence/admission uncertainty. The owner has been notified.
