# Research file-structure protocol

This is the single shared rule for where research material lives and how agents maintain the
directory structure. It governs **placement, naming, linking, moving, and archiving**. Mathematical
status and AND/OR propagation are governed separately by [`DAG_PROTOCOL.md`](DAG_PROTOCOL.md).

The goal is simple: an agent should find existing local work before searching the web, and should be
able to reach every piece of work on a proof obligation from that obligation's canonical node file.

## 1. Canonical hierarchy

```text
research/
  RESEARCH_STRUCTURE_PROTOCOL.md   # this file: placement and maintenance rules
  DAG_PROTOCOL.md                  # proof-state and review rules
  literature/                      # shared, cross-problem literature library and reviews
  <problem>/
    README.md                      # problem entry point
    proof-dag/
      README.md                    # DAG-local usage and validation
      NODE_INDEX.md                # alias/id/file lookup table
      nodes/
        <stable-node-id>.md        # exactly one canonical record per DAG node
    notes/                         # long-form synthesis, handoffs, full-DAG view, proof notes
    paper/                         # manuscript sources and manuscript-only assets, when present
    data/                          # reusable problem data, when present
    logs/                          # problem-local run logs, when present
```

Repository-level `tools/`, `artifacts/`, `logs/`, `results/`, `publish/`, and `paper/` are retained
for existing shared workflows. This protocol does not authorize moving old cited material merely to
make the tree prettier.

## 2. Ownership and source of truth

Each type of information has one canonical owner:

| Information | Canonical owner |
|---|---|
| Where a file belongs | this protocol |
| Proof status, review gate, AND/OR propagation | `DAG_PROTOCOL.md` |
| One node's claim, edges, work log, evidence, reviews, obligations, history | its canonical node file |
| Alias → stable id → node file lookup | the problem's `proof-dag/NODE_INDEX.md` |
| Whole-graph visualization and legacy detailed ledger | the problem's `*_PROOF_DAG.md` |
| Cross-problem bibliography and literature synthesis | `research/literature/` |
| Large proof, certificate, program output, or review body | its linked artifact file |

Do not create a second “authoritative” copy. Summaries may repeat information for navigation, but
they must link to the canonical owner.

## 3. One node, one file

Every Mermaid/DAG node MUST have exactly one file:

```text
research/<problem>/proof-dag/nodes/<stable-node-id>.md
```

The filename is determined by the stable id and is never chosen independently. The file MUST contain:

- stable id, aliases, kind, role, status, disposition, and canonical `node_file` path;
- status-propagating `parents` and `children`;
- non-propagating `related` links;
- Claim, Current status, Work record, Evidence, Adversarial reviews, Open obligations, and
  append-only Status history sections.

Large derivations and logs are linked, not pasted wholesale. “All work is reachable from the node”
is mandatory; “all work is physically inside the node file” is not.

Stable ids are permanent references. Do not rename or reuse an id because the claim evolved. If the
mathematical claim changes materially, create a new node and relate or supersede the old one.

## 4. Where new material goes

Before creating a file, classify it:

1. **Cross-problem paper or literature review** → `research/literature/`.
2. **Node-specific work record or status event** → append to the canonical node file.
3. **Long proof, synthesis note, handoff, or commission prompt** → `research/<problem>/notes/`, then
   link it from every affected node.
4. **Independent adversarial review** → a separate immutable review artifact; link it from the
   reviewed node's `Adversarial reviews` section.
5. **Machine log or generated certificate** → the existing problem-local or repository-level
   log/artifact area used by that workflow; link the exact file from the node.
6. **Manuscript source or manuscript-only figure/table** → `research/<problem>/paper/`.
7. **Disposable experiment** → `tmp/`; it cannot support a status transition until promoted to a
   stable linked location.

For a load-bearing external paper, create `research/literature/papers/<paper-id>/proof-dag/` only
when the local project needs to understand, reproduce, port, repair, or challenge its proof. This is
a proof-idea dependency graph, not a structural table of contents: include only indispensable
lemmas, conceptual steps, parameter checks, alternative routes, and genuine gaps.

When choosing between local and web research: search the node files, `NODE_INDEX.md`, notes, and
`research/literature/` first. Search the web only when the local corpus does not answer the question,
then ingest durable results into the literature library or the relevant node.

## 5. Naming rules

- Directories use stable lowercase names.
- Node files are named exactly `<stable-node-id>.md`.
- Dates in filenames and work logs use `YYYYMMDD` or `YYYY-MM-DD`.
- New artifacts should begin with the problem and a recognizable node/purpose slug, for example
  `se_phi_legal_review_20260718.md`.
- Use descriptive names; do not create ambiguous `final.md`, `new.md`, `latest.md`, `v2-final.md`, or
  agent-name-only files.
- A revision belongs in the existing file's append-only history when possible. Create a second file
  only when provenance or independent review requires a separate immutable record.

## 6. Atomic update rule

A node-related research update is incomplete until all applicable parts of this transaction are done:

1. Read the target node file and its propagating dependencies.
2. Write the proof attempt, log, certificate, or review to its stable location.
3. Append a dated entry and direct link in the target node file.
4. Apply the status/review rules in `DAG_PROTOCOL.md`; never infer a promotion from a filename.
5. If graph structure or status changed, synchronize `NODE_INDEX.md`, Mermaid, nested outline, and
   affected ancestor nodes in the same change.
6. If the active frontier changed, update the problem's prover prompt/handoff.
7. Run the structural validator and check local links before stopping.

Creating an artifact without linking it from a node leaves orphaned research and does not count as a
completed update.

## 7. Move, delete, and archive rules

- Do not move or rename a cited file merely for tidiness.
- Before an unavoidable move, search all references, update them atomically, and leave a short
  forwarding stub when external or historical references may exist.
- Never delete a proof attempt, falsifier, negative result, completed review, or status history.
  Archive obsolete material and link the successor.
- DEAD and REFUTED nodes remain indexed and readable.
- Generated caches and genuinely disposable temporary outputs may be removed only when no node,
  note, paper, or review cites them.
- Do not mass-normalize legacy paths as part of unrelated mathematical work.

## 8. Migration and legacy files

Existing cited files outside the canonical hierarchy are grandfathered. Their current location is
valid until there is a substantive reason to move them. Node files marked `migration_status: mirror`
may initially point to the legacy full DAG for detailed history; all **new** node-specific work must
be recorded directly in the node file.

Structural cleanup never changes a mathematical status. Ambiguous legacy edges or statuses must be
listed in `NODE_INDEX.md` and adjudicated as mathematical work under `DAG_PROTOCOL.md`.

## 9. Required closeout checks

From the repository root:

```powershell
python tools/proof_dag_check.py --problem all
python tools/literature_check.py
git diff --check
```

Before closing a session, confirm:

- every touched DAG node has exactly one canonical file and one index row;
- every new stable artifact is linked from at least one node or literature record;
- all local links resolve;
- no status was changed without the required independent review;
- no cited history was overwritten, moved, or deleted.

## 10. Root-level field folders (2026-07-28 lead directive)

Four broad field folders live at the repository ROOT (not under `research/`), by lead directive of
2026-07-28: `entanglement-distillation/`, `state-geometry/`, `channel-capacity/`, `bosonic-cv/`.
A field folder is a thin container: `README.md` (scope + problem list) + `literature/` (a field
literature library with the same shape as `research/literature/` — `catalog.json`, schema v1, plus
`papers/<author-year-topic>/README.md` pages with the local arXiv PDF alongside, and `reviews/`
where present) + one folder per PROBLEM. Each problem folder is STRICTLY aligned with
`research/se/`: `README.md` + `notes/<PROBLEM>_PROOF_DAG.md` (DAG + the eight rules inlined) +
`proof-dag/` (`README.md`, `NODE_INDEX.md`, `nodes/`). No field-level `proof-dag/` or `notes/`.
`tools/proof_dag_check.py` resolves problems through its `PROBLEM_DIRS` registry (se, ksum, and the
twelve field problems); `tools/literature_check.py` validates all five literature libraries.
All §2–§9 rules apply unchanged; `DAG_PROTOCOL.md` governs statuses and reviews.
