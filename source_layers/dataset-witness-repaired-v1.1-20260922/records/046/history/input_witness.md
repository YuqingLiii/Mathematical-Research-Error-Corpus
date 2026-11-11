# Record 046 — Set equality and collision

**Review status:** `source_reviewed`.

Correction: do not say knowingly reused an already-withdrawn certificate, or that the zero-padding reduction was wrong.

## Original statement and context

> 证明完成了。核心比预想的简单：**SE 是 Collision 的一个固定承诺子问题**，所以 SE 的显式矩阵可以原封不动嵌入 Collision。

**Recorded location:** Assistant message, 2026-07-16T10:55:28.849Z; mathematical follow-up, 13:49:09.641Z.

**Context (annotation, not a source quotation):** The proposed explicit collision lower bound imported a set-equality adversary matrix. The completion statement was made before the formal upstream withdrawal; the zero-padding embedding itself was correct.

**Source binding:** `automatic_text_match` (inherited; not rechecked here).

## Witness

Preserving the numerator and masked matrix norms transfers only the bound already established for the source matrix; it cannot establish an unproved source norm bound.

### Argument or calculation

For the coordinate isometry J, Gamma_Col=J Gamma_SE gives ||Gamma_Col||=||Gamma_SE|| and ||Gamma_Col o Delta_i||=||Gamma_SE o Delta_i||. The inherited denominator still needs ||K_N* G K_N|| <= C^2/j. Its proposed derivation lacked the identity j U(K_N* G K_N)U*=M/[B_theta(q)^2 omega] in a common normalization. Thus the displayed Omega(N^(1/3)) certificate remains conditional on that identity. Finite checks at N=2,4,6 establish the embedding, not the uniform bound.

Scope: argument_invalid.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl](original/M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.readable.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/gold2_se_terra/rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl") · [event data](original/M01-rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl.visible.json)
  - Coverage: Selected visible events; source lines 10757–10773, 10783–10798, 11017–11030, 11291–11306.
  - Relevant location(s): agent_message 2026-07-16T10:54:18Z、10:55:28Z、13:35:31Z、13:49:09Z；gold3 fork 09-25-58 于 13:41:35Z
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/gold2_se_terra/rollout-2026-07-11T12-59-37-<session-id-redacted>.jsonl`

- [M02: GOLD3_collision_reclaim.md](original/M02-GOLD3_collision_reclaim.md "tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/GOLD3_collision_reclaim.md")
  - Coverage: Full bundled file; source lines 1–13.
  - Relevant location(s): #primary inherited-certificate failure
  - Source: `tracking/ai-proof-records-20260912/recovered-marathon-20260821/webreview/GOLD3_collision_reclaim.md`
