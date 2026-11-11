# Mathematical research error corpus (anonymous review copy)

This repository contains the 65 accepted records of naturally occurring mathematical errors that
the paper studies, grouped into 12 research problems. Each record keeps its stable ID, the original
erroneous statement with context, a scoped witness showing why the statement fails, its category
label(s), and relative pointers to the source material it was taken from.

We are progressively conducting comparative audits of these naturally occurring errors across representations and aim to complete the planned comparison before the end of the rebuttal period.

## Start here

- [`index.json`](index.json): one entry per record (ID, problem, summary, witness document).
- [`data/records.jsonl`](data/records.jsonl): the 65 records, one JSON object per line
  ([data dictionary](docs/DATA_DICTIONARY.md), [schema](schemas/record.schema.json)).
- [`data/problems.json`](data/problems.json): the 12 problems and the record IDs mapped to each.
- [`data/statistics.json`](data/statistics.json) and [`data/excluded.json`](data/excluded.json):
  label counts and the 12 allegations that were not accepted as records.
- Witnesses: `source_layers/dataset-witness-repaired-v1.1-20260922/records/<id>/witness.md`, with the
  record's source material under `original/` and `reconciliation_sources/` in the same folder.
- Category annotations: `source_layers/annotations-yoshida65-level1-v3-20260923/` (current level-1
  labels, following the first-level categories of Yoshida et al., arXiv:2609.15145) and
  `source_layers/annotations-yoshida45-subtypes-20260923/` (logical subtypes); v1 and v2 are history.
- [`docs/RECORD_AUDIT.md`](docs/RECORD_AUDIT.md): per-record binding and witness status as recorded
  when the corpus was assembled.

## Verification scripts

- `source_layers/dataset-witness-repaired-v1.1-20260922/checks/check_witnesses.py` with
  `checks/witness_checks.json`: the frozen scoped witness checks.
- `scripts/run_witnesses.py` and `scripts/additional_witnesses.py`: re-run those scoped checks and the
  additional checks without writing into the frozen layer (`pip install -r requirements.txt`).
  Recorded outputs are in `audit/witness_execution.json` and `audit/additional_witness_execution.json`.
- `scripts/check_anonymous_copy.py`: structural and link check for this copy (record and problem
  counts, ID accounting, index consistency, schema, and that every referenced file is either present
  or listed as omitted). It does not check mathematics.

`scripts/validate.py` is the corpus's full validator. It also needs material that is not part of this
copy (the manuscript, reasoning-alignment inputs, raw session extracts and the private file
manifest), so it does not pass here; `check_anonymous_copy.py` is the check intended for this copy.
No mathematical check was re-run to prepare this copy.

## What this copy omits

Omitted files are listed with reasons in
[`provenance/ANONYMOUS_COPY_EXCLUSIONS.tsv`](provenance/ANONYMOUS_COPY_EXCLUSIONS.tsv): raw session
event files and session-derived extracts, the manuscript and manuscript excerpts, reasoning-alignment
records, repository-hosting and local-provenance records, and the private file manifest.
Within JSON records, fields holding internal reasoning, analysis or thinking text (for example the
quoted text of `visible_reasoning` anchors) and raw event payloads were removed; pointers such as
source names, line numbers and hashes remain. Identifying strings (local paths, account names,
private chat links, session identifiers) were replaced by placeholders. Changed files are listed in
[`provenance/ANONYMOUS_COPY_MODIFIED_FILES.tsv`](provenance/ANONYMOUS_COPY_MODIFIED_FILES.tsv);
recorded hashes of changed or omitted files therefore no longer resolve in this copy.

Quoted research material and third-party content keep their original terms.
