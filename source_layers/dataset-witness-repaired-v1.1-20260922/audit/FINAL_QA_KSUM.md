# Final package QA — query complexity and set equality

Date: 2026-09-22. Read-only QA of `dataset-final-v1-20260922`; no release files edited.

Scope: records 040–048, 074–076; top-level INDEX, README, EXCLUDED, statistics and records.jsonl. This QA checks the already completed source reconciliation, not another reset of the mathematical admission review.

## Substantive findings

### P1 — computational-check references did not resolve — FIXED

Every inspected `record.json` has `computational_checks.file = "checks/witness_checks.json"`, but this path does not exist relative to any inspected record directory. At the time of QA, the release root also has no `checks/` directory. Example: `records/074/record.json:93–97`.

Fix before release: point to an existing package-relative file (using the correct number of `../` segments), or set the field explicitly absent if no machine-readable check is bundled. Do not merely copy the old check file into place: its old 074 test uses q=6 and is not the accepted domain-correct q=42 witness. If the old checks are retained as history, label them as such and supply the q=42 calculation separately or explicitly describe the final derivation as the accepted check.

### P2 — record 074 current reasoning-anchor metadata bound the repaired version — FIXED

`records/074/record.json:34` correctly states that the inherited thinking concerns the repaired construction and must not be used as formation evidence for the bad common-shift argument. Nevertheless:

- line39 labels that anchor `role: generation` inside the current `visible_reasoning.anchors`;
- lines55,69,83 label the same old-version events `original_claim_or_computation` inside `historical_events`.

The historical-events container itself is appropriately named; the risk is the current reasoning-anchor list. A consumer counting direct error-forming summary anchors could count this as one despite the prose warning. Move this anchor to historical/context-only evidence, or attach an explicit `binding_status: context_only_not_error_forming` and make the release's reasoning-count logic respect that field. The corrected 074 error and witness themselves are sound.

### Minor clarity — excluded 076 context retains tentative-inclusion wording

`audit/excluded/076/record.json.original.context` and its rendered witness say the item can only be recorded as a proposed unfinished conversion. Admission, endorsement, witness_scope, EXCLUDED and adjudication all clearly exclude it, so this is not a counting error. For maximum clarity the context can instead say it is a review question preserved for audit accountability, not a confirmed mathematical error. The source quote must remain unchanged.

## Checks passed

- All 12 inspected `record.json` original excerpts exactly match the quoted original section in their `witness.md`.
- For all 11 included records, the JSON witness explanation and evidence match `witness.md`.
- 040–048 remain consistent with the reconciled scoped judgments. 044 explicitly remains a false conjectured candidate, not a falsely claimed completed theorem. 046 distinguishes the valid embedding from the missing source norm bridge and corrects the historical withdrawal chronology. 047 is a T_b proof gap, whereas 048 has exact T_a violations; neither overstates the other.
- 074 uses k=4,K=2,q=42, satisfies the original threshold, computes C0=14 and |δ|≤5, and exhibits only even reachable targets. It explicitly distinguishes the repaired per-coordinate construction. The q=6 wording appears only as superseded history, not in the accepted witness.
- 075 uses the earlier universal item1 and the Z2,t=1,n=2 single-orbit counterexample. It explicitly explains the source/witness pairing correction and does not pretend the valid regularity-failure examples are refutations. Later q≥3 repairs are preserved.
- 076 is absent from the positive `records/` tree and present under `audit/excluded/`. Its admission is excluded, overclaim is null, endorsement is historical_allegation_not_endorsed, and scope is not_a_refutation_of_original. The rendered dossier explicitly says not a positive record. Root EXCLUDED explains why the original LP table and the request to check normalization are not errors.
- `records.jsonl` contains 63 unique included IDs and exactly35 `overclaim=true`, matching statistics.json and README. The positive INDEX has63 rows. The14 excluded IDs include076. The root documents clearly distinguish the77-entry historical registry from63 included errors; no old64/13 or withdrawn51/15/11 count is presented as current.

## Outcome

**FINAL PASS after rebuilding.** No additional mathematical-admission bug found in this assigned subset. Both identified packaging/provenance issues have been fixed and rechecked in the actual final directory:

- All12 inspected records now declare `computational_checks.path_base = release_root`; their referenced `checks/witness_checks.json` resolves from that root.
- The root contains both `checks/check_witnesses.py` and `checks/witness_checks.json`. The latter contains41 passed checks. The single074 check explicitly uses k=4,K=2,q=42 and the source threshold42; no q=6 check is endorsed for074.
- Record074 has an empty current `visible_reasoning.anchors` list. Its repaired-version excerpt is under `context_only_anchors`, with an explicit description that it is not error-forming reasoning. Every inherited event has `roles=[version_context]` and `binding_status=corrected_version_context_only`; its former roles are preserved only under `historical_roles`.

The final verification inspected the files and machine-readable results; it did not launch an additional large computation. The earlier mathematical and count QA remains valid.
