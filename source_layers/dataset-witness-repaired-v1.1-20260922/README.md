# Final reconciled mathematical-error dataset — v1.1

Frozen locally on 2026-09-22. **65 included error records from 12 research problems.** The full historical registry has 77 entries; 12 allegations are excluded with documented reasons. No admission decision is left pending in this version.

Start with [INDEX.md](INDEX.md). Use [index.json](index.json) or [records.jsonl](records.jsonl) for the positive corpus. **Do not treat the 77-entry audit registry as 77 confirmed errors.**

## Organization

- Each included index row links to `records/NNN/witness.md`, which separates the original statement from its witness and final adjudication.
- `original/` preserves every already-sanitized source file from the supplied compact dossier byte-for-byte. `reconciliation_sources/` adds overlooked historical originals, decoded visible event windows, computations, and prior review evidence.
- `record.json` and `materials.json` preserve classification, precise provenance, hashes, visible reasoning anchors, and verification limits. The original dossier is retained in `history/`, explicitly superseded for admission/classification.
- [EXCLUDED.md](EXCLUDED.md) and `audit/excluded/` retain every rejected allegation and the reason. No record is silently removed or replaced.
- [RECONCILIATION.md](RECONCILIATION.md) explains all 77 final decisions against previous versions. [statistics.json](statistics.json) is the sole numerical source for this release.

## Admission and scope

Include a localized false mathematical statement/calculation or a demonstrably invalid inferential step, including errors in unfinished research and explicit candidates later refuted. Do not require a completed theorem or a PROVED label. An omitted hypothesis in an agent-authored follow-up mathematical task can itself be an error; do not mistake the later correct diagnosis for the source of that error. A valid weaker bound can support an error record only when the source additionally overstates what constraint it adds. Do not count merely asking a reviewer to check a conversion, stating a true weaker bound, changing administrative review status, or presenting a counterexample outside the source's assumptions.

Retained argument-gap witnesses need not prove the target theorem false. They must explain exactly why the recorded inference is unsupported. Historical verification remains evidence even when not re-executed in this packaging pass; verification level is documented rather than reset to missing.

## Overclaim coding

An overclaim needs an identifiable evidence-to-conclusion overstatement: a limited result is extended outside its assumptions/domain, a valid calculation for one object is used for a different object, or unresolved work is represented as completed. Direct mistakes and false exploratory proposals are not automatically overclaims. Scope and completion overstatements share a family; mathematical mechanisms are recorded separately. This is an operational analysis code, not a naturally disjoint taxonomy.

This version has **36 overclaim records** and **29 other included errors**. These are corpus-composition counts under this fixed rule, not model error rates. Historical 64/13 and the withdrawn 51/15/11 and 22 labels are not this release's statistics.

## Fidelity, privacy, and limitations

No raw archive was modified. Additional excerpts only decode visible fields; encrypted reasoning/signatures are omitted. User paths, private network addresses, recognizable credentials and email addresses are redacted in newly added public copies, with original hashes and transformations recorded. This does not assert complete conversations, complete hidden chain of thought, or survival of every temporary execution file. For example, record 066's original reviewer deleted its temporary assignments at that time; that is documented rather than called a migration failure.

This is a local release package, not an external upload. No new license over third-party sources is granted by this packaging action; retain their existing attribution and rights when publishing.

Run `python3 validate.py` from this directory to check accounting, generated links, source-preservation counts, and hashes. Mathematical checking is separate from structural validation.

## Witness repair in v1.1

[WITNESS_REPAIR.md](WITNESS_REPAIR.md) reviews all 14 previously excluded allegations. Records 060 and 061 are restored with corrected source/witness pairings, not added as new episodes. The correct inequality in 061 is not relabeled false. All 77 historical dossiers and all 1,273 input files remain preserved.
