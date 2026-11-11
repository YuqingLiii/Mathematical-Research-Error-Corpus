# Historical report — not the governing release statistics

# August session-event recovery

Date: 2026-09-18

## Scope

This package records the read-only recovery of the six publication-corpus rows
whose exact writer/materialization event was previously unresolved:
`GAP-003`, `GAP-004`, `GAP-005`, `GAP-007`, `GAP-008`, and
`GROTH-H4-001`.

The sources were checked against the Mac Studio at `[PRIVATE_NETWORK_ADDRESS]`. Four
source files have full-file SHA-256 identity between the local copy and the
Mac Studio copy. The long Grothendieck session continued locally after the
emergency snapshot, so its full-file hashes differ; all nine selected decisive
JSONL lines were instead checked individually and have identical SHA-256 values
on both machines. `SOURCE_MAP.tsv` records both full-file identities and this
append-only exception. No remote file was modified.

The raw files in `raw/codex/` are exact, newline-preserving slices of the
original JSONL records. `RECOVERED_EVENTS.tsv` binds each slice line back to its
original JSONL line, timestamp, byte count, and line SHA-256.

## Results

| record | bad event (UTC; New York local) | recovered evidence | gate after recovery |
|---|---|---|---|
| GAP-003 | 2026-08-20 23:41:57.547; 19:41:57.547 EDT | Exact `PROOF.md` creation patch says the entire problem is to choose *different* tuples. | P4 byte-bound |
| GAP-004 | 2026-08-21 02:13:44.670; 2026-08-20 22:13:44.670 EDT | Exact patch calls the aggregate expansion a generating function for the orthogonal sectors; 25.689 seconds later the agent says that wording could overstate the result and explicitly disavows a per-subset estimate. | P3 event-linked, deliberately not P4 |
| GAP-005 | 2026-08-20 23:41:57.547; 19:41:57.547 EDT | Same exact creation patch says tensoring a single Hastings counterexample with itself cannot settle the extensive question in the surrounding conjugate-pair route. | P4 byte-bound |
| GAP-007 | 2026-08-21 16:10:22.317; 12:10:22.317 EDT | Exact patch attributes the needed coefficient-sensitive tail to the opened source; the next session corrects that attribution at 16:15:33.756 UTC. | P4 byte-bound |
| GAP-008 | 2026-08-21 16:15:33.756; 12:15:33.756 EDT | Exact patch writes `epsilon^(-4u) <= C`; a failed correction attempt is preserved, followed by the successful counterfamily/correction at 16:17:38.800 UTC. | P4 byte-bound |
| GROTH-H4-001 | 2026-08-30 01:29:22.886; 2026-08-29 21:29:22.886 EDT | Exact DAG creation patch uses a feasible separating moment functional in the wrong weak-duality direction; the exact repair begins at 02:31:16.464 UTC. | P4 byte-bound |

## GAP-004 calibration

An exact search over the relevant August 20--21 Codex sessions and marathon
rollouts found the literal per-subset inequality only in the immediate
clarification that says it is **not** asserted. The pre-clarification artifact
contains the broader sentence that equation (44) is the generating function
for the orthogonal sectors. Therefore this package binds the visible
overstatement episode and its author, but it does not claim byte-level
authorship of the canonicalized literal inequality. This is why the row is P3,
not P4.

## Corpus-level effect

Before this recovery, the 50-row publication curation had 33 P4 rows, 11 P3
rows, and 6 P2 rows. After merging these events it has:

- 38 P4 byte-bound rows;
- 12 P3 visible-event rows;
- 0 P2 writer-unresolved rows;
- 50/50 rows with event-supported focal authorship;
- 50/50 rows with complete mathematical claim-to-failure reconstruction.

These are provenance/process counts, not independent-run counts. No witness was
independently re-proved in this recovery pass, and Codex reasoning remains
summary-only because the encrypted hidden content is unavailable.
