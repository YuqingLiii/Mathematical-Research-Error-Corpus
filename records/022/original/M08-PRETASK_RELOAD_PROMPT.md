> **Schema-v6 refresh, 2026-08-17.** Three consecutive sessions reported that this template still
> spoke schema v5 (a "§2 status ladder", "the eight hard rules", `artifacts.work_record`, a
> Windows-only python path). Corrected here so the fourth session does not have to report it again.
> The DISK still wins over this file if they ever disagree.

# Pre-task rules reload — standalone prompt (run FIRST, before ANY commission)

Fill the two placeholders when dispatching: {PROBLEM_DIR} (e.g. `channel-capacity/werner-holevo-gap`)
and {NODE_ID} (e.g. `WHGAP.antideg-boundary`), plus the ROLE you are assigned (executor | reviewer).

---

You are about to work in this repository under its proving protocol. Before doing ANYTHING else —
no math, no code, no file edits — read the following files from disk, completely, in this order.
The DISK is authoritative: if anything you were told elsewhere (including your commission prompt)
conflicts with these files on rules, structure, statuses, or review, the disk wins and you must
REPORT the conflict instead of resolving it silently.

1. `research/DAG_PROTOCOL.md` — the whole file. Pay particular attention to:
   - §3, the six-level evidence table: which LEVEL each kind of evidence licenses, and who may write it
     (self-authored work never carries a completion tier — §5.5);
   - §1-§2, the canonical object and the node/route model; §5, the DAG update protocol; §6, the
     node-level audit protocol; §7, formalization. (There is no numbered "hard rules" list in v6 —
     that was schema v5. Historical note for readers of old commissions: v5 rule 2 (you may never
     stamp your own work PROVED, nor
     kill a branch to REFUTED alone), rule 6 (completion-tier statuses CERTIFIED*/PROVED/REFUTED
     open ONLY after an INDEPENDENT reviewer — a fresh instance that did not author the work and
     was not told the wanted answer — has COMPLETED a review, archived on disk and cited on the
     node; until then the cap is NUMERICAL with a `pending-review:` marker, or OPEN/CONJECTURED),
     rule 7 (a review counts only if it demonstrably executed the 7a–7g quality checklist), and
     rule 8 (ideas become nodes BEFORE commissions; outcomes are recorded before new work —
     including 8e: children may be registered only together with a composition blueprint in the
     parent's node file, and that blueprint must be completed into a reviewed prose or Lean
     composition proof once the children complete);
   - §4–§6, the READ/WRITE protocols and the session-close checklist.
2. `research/FILE_PROTOCOL.md` — where every kind of file belongs (§4), naming (§5),
   the atomic update rule (§6), move/archive rules (§7), closeout checks (§9), and §10 (root-level
   field folders).
3. `{PROBLEM_DIR}/README.md` — the problem entry.
4. The problem DAG in `{PROBLEM_DIR}/notes/` (`*_PROOF_DAG.md`) — the DAG plus the eight rules inlined.
5. `{PROBLEM_DIR}/proof-dag/NODE_INDEX.md`, then the target node file listed there and its child
   node files. KSUM and SE use `{NODE_ID}.yaml`; legacy problem trees may still use `{NODE_ID}.md`.

When done, output a PRE-ACTION REPORT (top of your working log) before any work:

- target node id and its current status as read from disk;
- your ROLE (executor or reviewer); if reviewer, an independence statement: you did not author the
  reviewed work and were given no desired outcome;
- the highest LEVEL your planned evidence could license per §3, and who would be allowed to write it;
- the gates and deliverables of your commission, in one line each;
- any conflict found between your commission text and the disk protocols (or "none").

Only after this report may you begin the commissioned work.

---

## Folder and DAG maintenance obligations (bind you DURING and AFTER the work)

While working, and before you stop, you maintain the tree per the protocols you just read:

1. **Placement (§4 of the file protocol).** Every new file goes to its canonical home:
   scripts under `tools/`; run artifacts and logs under `artifacts/` (with a dated, problem-slugged
   name and a `SHA256SUMS.txt`); long-form notes and commission prompts under
   `{PROBLEM_DIR}/notes/`; review reports as separate immutable artifacts; disposable experiments
   only under `tmp/` (they cannot support any status). Naming per §5 — no `final.md`/`new.md`.
2. **Atomic update (§6).** No orphaned research: every artifact you produce is linked from the
   node in the same session — append a dated entry under `events:` (append-only; verify with
   `python3 tools/check_event_append_only.py --base-ref HEAD`), and cite it from `assessment.basis`,
   `artifacts.evidence`, or `artifacts.reviews` in the canonical node file the moment a result is
   read (rule 8c).
3. **Level writes only per the §3 evidence table** — at your role's permission level, with a disk cite;
   every status is hand-written per the single-status model (DAG_PROTOCOL §1, 2026-08-08): no
   bottom-up recomputation exists; a mother with a live decomposition sits at ≥ CONJECTURED, and
   LINT-COMPLETION polices completion tiers against sub-completion load-bearing children; REFUTED
   requires reason + DEAD/PARKED tag and only direct evidence against the node's own claim;
   nothing of your own authorship gets a completion tier (rule 6).
4. **Keep all views in sync in the same change:** the canonical node file, `NODE_INDEX.md`, the
   Mermaid diagram, the nested outline, and the DAG doc's "Most recent change" header must
   describe the SAME graph before you stop.
5. **Never delete or move cited history** (§7): failures are append-only; archive, do not erase.
6. **Closeout (§9 + DAG protocol §6 checklist):** run
   `python3 tools/proof_dag_check.py --problem <problem>` and `python3 tools/literature_check.py`
   (both MUST exit 0), plus `python3 tools/check_event_append_only.py --base-ref HEAD`. Regenerate
   derived views with `--write-generated`; NODE_INDEX.md and GRAPH.mmd are generated, never
   hand-edited. Do NOT require `tools/lean_dag_check.py` to exit 0 — it has a v6 loader as of
   2026-08-17 but still reports pre-existing declared deviations,
   walk the session-close checklist, then print your FINAL line. A session that leaves the tree
   out of sync, a result unrecorded, or a validator red is an INCOMPLETE session regardless of the
   mathematics.
