# Proof-DAG protocol (schema v6)

This protocol defines the public research state used by every proof-oriented project in the
repository. Its purpose is to make claims, alternative proof routes, dependencies, evidence,
reviews, failures, and remaining work auditable without reconstructing them from chat logs.

The protocol is general: it does not prescribe a model, agent role, wall-clock schedule, or
project-specific workflow.

For the current scheduling experiment, the shared DeepSeek/Codex batch interface is documented
in [section 9](#9-batch-interfaces-for-the-scheduling-experiment) and the executable
[batch-interface contract](scheduling-v3/BATCH_INTERFACE.md). That experiment-specific interface
does not replace the mathematical record and review rules below.

## 1. Canonical object

Each project stores one YAML file per node under `research/<project>/proof-dag/nodes/`. A minimal
record has the following form; optional blocks are omitted rather than written as null values.

```yaml
id: PROJECT.unique-id
role: proof                    # optional: proof | obstruction | outcome | tool | constraint
aliases: [short-name]          # optional
claim: >-
  A precise, reviewable proposition or research outcome.

routes:                        # optional: alternative ways to establish the claim
  route-id:
    premises: [PROJECT.B, PROJECT.C]
    assumptions:               # optional; established interfaces only
      cited-result:
        kind: external-theorem # external-theorem | model-fact
        statement: Exact statement and scope.
        source:
          path: path/to/source
          kind: text
    implication: >-
      Explain why all listed premises, under the listed assumptions, imply this node's claim.
    proof:                     # optional until an argument exists
      sketch: Reviewable blueprint or completed argument.
      sources:
        - path: path/to/argument
          kind: text
    assessment:
      level: OPEN
      summary: What is and is not established about this implication.
      basis:                   # optional: evidence | reviews | runs | counterexamples
        evidence:
          - path: path/to/evidence
            kind: text

assessment:
  level: OPEN                  # OPEN | CONJECTURED | NUMERICAL | CERTIFIED* | PROVED | REFUTED
  summary: Current judgment of the node's own claim.
  basis:                       # optional
    routes: [route-id]
        reviews:
          - path: path/to/review
            kind: review
            reviewed_hash: sha256:... # digest of this exact claim or route implication

disposition:                   # optional; operational, not evidential
  state: PARKED                # PARKED | DEAD
  reason: Why work stopped.
  revive: What new evidence would reopen a PARKED node.
  source:
    path: path/to/stopping-evidence
    kind: review

formalization:                 # optional; present only for a real formal mirror
  lean:
    module: Project.Module
    file: path/to/Module.lean
    claim: Claim
    state: stated
    claim_hash: sha256:...
    sync_state: current        # current | stale
    theorems: [TheoremName]

frontier:                      # optional; only unfinished actions
  task-id:
    task: A concrete next action.
    kind: task                 # task | gate | review
    since: YYYY-MM-DD

events:
  created-YYYY-MM-DD:
    date: YYYY-MM-DD
    type: created
    summary: Registered the claim and its initial evidence state.
    sources:
      - path: path/to/creation-record
        kind: text
```

Closed-key validation is deliberate: a field with no protocol semantics is rejected instead of
silently becoming an undocumented second source of truth.

## 2. Nodes and routes

A node is the smallest independently auditable research object. It owns one claim, one assessment,
and the evidence needed to interpret that assessment. The protocol does not distinguish structural
types such as `goal`, `leaf`, or `kind`: a node may acquire or lose routes without changing its
identity.

A route is a directed AND-hyperedge stored in the node it seeks to establish. Its `premises` are
jointly required; the different routes of one node are alternatives. Thus premises are combined by
AND within a route and routes are combined by OR across the node. Reverse dependencies, roots,
indexes, and diagrams are derived views and are never copied into node files.

Every route contains two logically separate obligations:

1. the listed premise claims must be established to the level required by the parent; and
2. the route implication must itself be argued and reviewed.

These obligations may be completed in any order. A level never propagates automatically across a
route. A completed parent requires an assembled, reviewable argument containing every load-bearing
premise and the corresponding route implication.

A direct proof needs no artificial empty-premise route. It is recorded in the node's assessment
basis and linked evidence. An unresolved hypothesis is not an assumption: it becomes its own OPEN
node and is listed as a premise. `assumptions` is reserved for already established external theorems
and explicit model facts, with exact scope and source.

A `basis.evidence` entry may link another node only as a non-load-bearing cross-reference, using
`kind: node-evidence`. If the parent claim mathematically depends on that node, the dependency must
instead appear under `routes.<route-id>.premises`; generic evidence links do not participate in DAG
reachability or completion checks.

## 3. Evidence levels

The level describes the evidence for the object on which it is written. Route levels assess route
implications; node levels assess node claims.

| Level | Meaning |
|---|---|
| `OPEN` | Registered but no reviewable argument yet. |
| `CONJECTURED` | A substantive blueprint or argument sketch exists. |
| `NUMERICAL` | A reproducible computation or mechanized run supports the scoped claim; the node links the command/output record and states what the run established. |
| `CERTIFIED*` | An independently reviewed conditional result with explicit unresolved premises or scope caveats. |
| `PROVED` | A complete argument and all load-bearing inputs passed independent adversarial review. |
| `REFUTED` | A structured counterexample or decisive contradiction refutes the precise claim or implication. |

Higher positive levels require stronger evidence, but the ladder is not an automatic arithmetic on
the graph. The node's level is written only after examining its own assembled dossier. The validator
may block an impossible promotion; it does not promote nodes.

## 4. Failure and disposition

Failure must be scoped to the proposition actually refuted.

- A refuted premise disables every route that requires it; it does not by itself refute the route
  implication or the parent claim.
- A refuted route implication kills that route only.
- Even if every registered route is dead, the parent is `OPEN` or `PARKED` unless the parent claim
  itself has been refuted. Registered routes are not assumed exhaustive.
- `DEAD` and `PARKED` are dispositions, not confidence levels. `DEAD` records a reviewed route with
  no known repair. `PARKED` requires a concrete revival condition.

Failed routes remain public through their assessments and events. They are removed from the active
frontier, not erased from the research record.

## 5. DAG update protocol

Every mutation follows the same sequence.

1. **Read the current state.** Inspect the target node, its routes and premises, relevant source
   artifacts, and the generated dependency view.
2. **Register before relying.** Add a new claim or route before another node depends on it. A new
   node receives a sourced `created` event. A new route includes its premises, implication statement,
   and at least an OPEN assessment.
3. **Make dependencies explicit.** Convert every unresolved load-bearing hypothesis into a node.
   Record only established interfaces under `assumptions`.
4. **Attach evidence locally.** Put evidence, reviews, runs, and counterexamples in the assessment
   of the node or route they support. A filename or chat transcript is not a verdict by itself.
5. **Review before promotion.** Completion-level promotion of either a node or a route requires a
   locatable independent adversarial review of the assembled argument by a reviewer other than its
   author. The review is normally conducted in a fresh review context and must state the reviewer
   or model, independence declaration, materials inspected, scope, verdict, and limitations. A
   linked review's scope describes the work actually checked, not merely the target claim. The
   review link records `reviewed_hash`, the digest of the exact node claim or route implication
   reviewed, and a completion assessment becomes invalid if that statement later changes. The
   structural validator checks that the review is linked, reachable, and hash-bound; whether it is genuinely
   independent and mathematically adequate remains an audit question, not a filename check.
6. **Append an event.** Record status changes, claim rewrites, route retirement, repairs, and
   migrations with dated sources. A level-change event records both `from` and `to`, and identifies
   the route when the route level changed. Existing events are immutable; the append-only checker
   rejects deletion or rewriting and rejects an unlogged level change. A finished frontier task is
   recorded as an event and REMOVED from the frontier in the same update — "discharged" or
   "resolved" annotations never linger in the frontier, which holds only unfinished actionable
   work.
7. **Refresh derived views and validate.** Regenerate the index and graph, then run the repository
   checker before closing the update.

The initial schema migration temporarily preserved completion labels marked `legacy-mirror` and
tied to the immutable migration snapshot. That exception was useful for lossless migration but is
not a valid evidential basis for a canonical release. Every current `CERTIFIED*` or `PROVED` node
and route must now link a review satisfying the rule above; otherwise it must be demoted to the
highest level supported by the recovered evidence. The migration snapshot remains in the event
history even after review links are recovered or a level is corrected.

## 6. Node-level audit protocol

An auditor must be able to start from one node without reading an entire conversation. For every
audited node, check:

1. the claim is precise and does not embed its current status;
2. every route lists all and only its load-bearing unresolved premises;
3. every external assumption states its exact theorem, regime, and source;
4. the implication proves the parent claim actually written, not an older or stronger statement;
5. the assessment level is licensed by the attached basis and caveats;
   a `NUMERICAL` assessment has an explicit run record, a `REFUTED` assessment identifies the
   counterexample or contradiction, and a completion assessment links its independent review;
6. failures are scoped to a premise, implication, route, or claim without over-propagation;
7. formal mirrors quote the current claim hash, or are explicitly marked `stale`; and
8. the frontier contains only unfinished, actionable work.

The audit result is attached to the same node or route assessment. This makes review incremental:
unchanged subgraphs need not be re-audited merely because a different route changed.

## 7. Formalization

Formal proof is a machine-readable mirror of the same public state, not a separate graph. A
`formalization` block is present only when a real module, file, and claim declaration exist.
`claim_hash` binds the formal mirror to the current natural-language claim. Any claim rewrite sets
`sync_state: stale` and creates a frontier gate until the formal statement, imports, proof, and hash
are synchronized.

A successful build is run evidence. It promotes a mathematical claim only to the extent that the
formal theorem contains all required premises and the formal-to-natural-language correspondence has
been reviewed.

## 8. Project manifest and generated views

`proof-dag/PROJECT.yaml` declares `schema_version`, project name, and root node IDs.
`proof-dag/REDIRECTS.yaml` is the only place for retired-ID redirects.
`NODE_INDEX.md` and `GRAPH.mmd` are generated from canonical node files. They may be deleted and
rebuilt without losing research state.

The schema and semantic checks are implemented by `tools/proof_dag_check.py`; source locators can be
verified against both the working tree and immutable git objects. `tools/check_event_append_only.py`
compares a proposed change with its git base and protects the event ledger. Both checks run in the
repository's pull-request workflow. Historical records from earlier schemas remain recoverable
through the migration event's immutable git reference.

## 9. Batch interfaces for the scheduling experiment

The scheduling experiment uses a shared batch interface for DeepSeek API tools and native Codex
local commands. Its detailed request bodies, examples, receipts, and error behavior are defined in
[scheduling-v3/BATCH_INTERFACE.md](scheduling-v3/BATCH_INTERFACE.md); scheduling field meanings are
defined in [scheduling-v3/PROTOCOL.md](scheduling-v3/PROTOCOL.md).

Native Codex normally receives the question directory, target nodes, and task information, then
uses its file tools to read what it needs. It reuses sufficient, unchanged context rather than
rereading the whole DAG and all proofs each round. The API input packet and paged-reader workflow
are not prerequisites for native work. Batch editing is an optional convenience.

The following rules govern use of the shared interface when selected:

1. **Read one question at a time.** Supply its structure, node states, material references, and
   the nodes requiring assessment. Keep full proofs in registered materials and read relevant
   passages on demand. A shortened statement is navigation, not a replacement for its full
   hypotheses. Complete all mandatory statement reads before submitting assessments.
2. **Batch changes from the same question.** When several nodes require assessment, submit
   their updates together. The model supplies changed assessment fields; the host merges them
   into the stored graph. Do not regenerate the entire graph to change two estimates.
3. **Use the same update implementation.** DeepSeek calls
   `update_node_assessments({"updates": [...]})`. Native Codex may write the same updates array to
   a local JSON file and invoke `research/scheduling-v3/cli.py update`. These interface calls pass through
   `AssessmentSession.update` and `DagStore.update_assessments`; the model does not bypass
   their checks. Native work that does not select this interface can use the project's existing
   local editing and validation workflow, preserving field ownership and history.
4. **Bind a batch to the state assessed.** The host fixes the question, targets, snapshot,
   assessment round, and example IDs before evaluation. Reject a stale snapshot or an invalid
   row without writing any part of the batch. Preserve the attempt and actual available usage;
   do not silently rerun a paid call.
5. **Keep mathematical updates distinct.** The assessment interface changes only scheduling
   estimates and next-step prompts. It cannot create a claim, rewrite dependencies, promote an
   evidence level, or award an independent-review verdict. Mathematical changes remain governed
   by sections 2–6; batch submission does not waive source, event, or review requirements.
6. **Refresh according to the calibration phase.** Before convergence, the online arm appends
   each valid settled attempt to its examples in order and refreshes the costs of all eligible
   candidates across all questions whenever a new example arrives, including unchanged nodes.
   Process questions separately with one shared example version, then recompute the queue in code.
   A cost-only refresh preserves applicable prompts and local probabilities; changed mathematical
   inputs require the corresponding full assessment. After the researcher confirms convergence,
   freeze the calibration example set and refresh only affected nodes. If predictions diverge
   again, pause new dispatches before the researcher decides which examples and scope to use.
   Preserve all measured attempts throughout. The zero-shot arm does not acquire examples.
   Re-estimate local q only when its own mathematical basis changes or the estimate is missing;
   propagate aggregate probabilities to affected ancestors in code, retaining their unchanged local q.
   New examples alone never rewrite a prompt or local q. These are distinct update conditions,
   not mandatory separate model calls: the JSON interface's `refresh` mode batches both together.
7. **Keep parent glue actions schedulable.** A live parent remains an action candidate while its
   premises are unresolved. Its action advances the conditional route implication or searches for
   an alternative route; it must not duplicate the registered child obligations. Leaves advance
   their own claims. Consequently a root and its newly exposed children may all appear in the same
   queue.
8. **Settle stagnation in the controller.** The assessment model cannot write `s`. When a Research
   Agent returns, atomically bind its validated postimage and complete execution-tree output usage.
   Reset only the dispatched node's `s` when an existing live-closure node changes formal level or
   a new node enters the root's live dependency closure. Otherwise add the actual output usage to
   that node's `s`; route, evidence, prompt, q, or prediction-only changes do not reset it. Ranking
   uses `beta=1`, `S0=0` in the frozen exponential factor.

**Format boundary.** The implemented scheduling interface currently targets the experiment's
single-question JSON graph, with a `scheduling` block on its nodes. Canonical schema-v6 YAML
records still use the closed-key format in section 1. This section does not authorize adding
unrecognized keys to those YAML files or flattening alternative routes into a single AND route.
Native Codex can already reuse the interface for the JSON experiment; connecting a canonical
YAML research project requires a format-aware adapter and its validator checks.

Batching and material-on-demand access aim to avoid repeated full-graph input and output.
Whether they reduce total token usage must be measured, including material reads and tool
round trips. A shared batch's usage is recorded as shared usage, not guessed per-node usage.
