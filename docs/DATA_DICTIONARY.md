# Data dictionary

Canonical file: `data/records.jsonl`. Encoding: UTF-8. Schema: `schemas/record.schema.json`, JSON Schema 2020-12. IDs are **strings**; preserve leading zeros. Every non-null operational file reference is relative to the repository root. Packaged line numbers are 1-based and inclusive; original archive line numbers are separately named.

| Field | Type | Meaning |
|---|---|---|
| schema_version | string | Normalized catalog format, currently 1.0.0; separate from frozen corpus v1.1 and annotation v3. |
| record_id / legacy_id | string | Stable three-digit paper/dossier ID and historical source identifier. No renumbering after exclusions. |
| problem_id / problem | string | Stable P01–P12 ID and frozen problem name. Table/figure aliases resolve through `data/problems.json`. |
| admission | string | Always `included` here. Excluded allegations are a separate file. |
| collection_context | string | Original investigation or follow-up continuation experiment; not an independent-run identifier. |
| summary | string | Frozen scoped error description. |
| original | object | Exact selected excerpt, research context, original locator and source form. |
| original.source_bindings | array | Each explicit quotation fragment and every matching packaged source, SHA-256 and line range. Only whitespace, source-line prefixes and patch-addition markers are normalized for matching. Ellipsis/excerpt-break markers are not invented. |
| witness | object | Explanation, derivation/counterexample, scope, historic endorsement, witness document and fresh-check references. `argument_invalid` does not mean the target theorem is false. |
| witness.fresh_checks | array | Result file, zero-based result index, description, exact scope and check kind. An empty array means no new computation in this audit, not no mathematical evidence. `certificate_bookkeeping` is not a new rank proof. |
| classification | object | Final level-1 v3 labels with source quotations, rationale, boundaries and optional logical subtype. |
| classification.categories | array | Unique record–category assignments: I understanding, II concepts, III arithmetic/algebra, IV reasoning, V others. Multiple labels require separately localized defects. Only 022 has III+IV (coefficient normalization vs polynomial threshold); 64 other records are single-labelled. |
| primary_logic_subtype | object or null | One primary subtype for IV records; null is not applicable. IV-1 theorem application, IV-2 implication, IV-4 strategy, IV-7 regularity. Other codebook subtypes have zero counts. |
| provenance | object | Frozen record identity, every packaged material path/hash, original event metadata and historical source-context record. |
| model_attribution | object | Distinct artifact author and decision model, plus sourced evidence and its limitations. Four targeted recoveries have `fresh_model_identification=true`: exact event/active turn context for 052/060; selected UI label and receipts for 018/039. Other values are historical annotations. Null = unavailable/unconfirmed for this exact role/error; it never means a particular model. No model is inferred from a folder name. |
| task_context | object | Source-grounded task context; not a claim that an entire original prompt is available. |
| time_evidence | object | Original locator and archived event timestamps/roles. Review time, artifact time and reasoning time must not be conflated. No earliest unseen error time is inferred. |
| visible_reasoning | object | Preserved anchors and availability limits. `paper_subset` records membership in the 12-record analysis, not internal thought completeness. |
| paper_mapping | object | Baseline TeX, Table 1 location, classification sections, explicit examples and reasoning audit reference. All 65 records map through problem and category; only selected records are illustrated individually. |
| audit | object | Separate text binding, hashes, classification join, scoped mathematical reading, fresh-check count and unresolved limitations. Full independent mathematical certification is explicitly false. |

Historical layers retain their original schemas. Their relative `source_name` or `[PROJECT]` references are provenance strings, not missing dependencies of the canonical catalog. Use `provenance.materials` to open packaged sources.

The descriptive percentages use **66 assignments**; 45/66=68.2%. Record prevalence uses **65 records**; 45/65=69.2%. Logical-subtype percentages use **45 IV records**. Neither denominator estimates a model failure probability. Records share research episodes and are not independent samples.

`data/excluded.json` gives 12 negative admission decisions. `supplemental/external_five_excluded.json` records five earlier external allegations as out of scope, without endorsing them as newly verified errors. `supplemental/DUPLICATE_MAP.tsv` preserves earlier duplicate-candidate decisions. No external allegation has been inserted to fill a count.
