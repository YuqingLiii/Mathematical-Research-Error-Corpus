# Current classification (2026-09-23)

The manuscript currently uses [Yoshida first-level annotation v2](annotations-yoshida65-level1-v2-20260923/README.md).

- Frozen corpus: `dataset-witness-repaired-v1.1-20260922/records.jsonl`, 65 records; no admission or source/witness changes.
- Record-category counts: problem understanding 2; mathematical concept knowledge 3; arithmetic and algebraic manipulation 15; logical and reasoning 45; others 2.
- Total: 67 labels across 65 records; the existing two double-labelled records are unchanged.
- Targeted revision: 032, 036 and 055 move from concept knowledge to logical/reasoning, based on explicit derivations or theorem applications. Only the six former concept-category records were re-examined in this pass.
- [Six-record source audit](annotations-yoshida65-level1-v2-20260923/CONCEPT_ORIGIN_AUDIT.md) includes the original quotes, source locations, boundaries and §4.6 alignment correction (11 reasoning-visible errors; 1 qualification/output discrepancy among 12 aligned records).
- Main manuscript and Figures 1(c) and 2 use the revised counts. Historical annotation v1 and frozen release ZIPs are retained unchanged.

Validation: `release_work/reclassify_concept_origins_20260923.py --check`.
