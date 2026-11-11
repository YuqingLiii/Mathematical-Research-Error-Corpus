# Record 008 — Channel additivity violations

**Final admission:** included. **Overclaim:** no.

## 1. Original statement and context

> The Fourier \(+1\) property implies the evenness independently because \(\mathscr F^2\) is phase-space reflection.

Context: The transform is the normalized symplectic Fourier transform (Ff)(k)=D^(-1) sum_p f(p) omega^[p,k] on F_D^2, where [p,k] is alternating and omega is a primitive Dth root of unity.

Locator: round-23-response.md, lines 234

## 2. Witness / adjudication

For the alternating symplectic kernel, squaring the transform gives the identity, not reflection.

Compute F^2 f(l)=D^(-2) sum_(p,k) f(p) omega^([p,k]+[k,l]). Since [k,l]=-[l,k], the exponent is [p-l,k]. Character orthogonality makes the inner sum D^2 when p=l and zero otherwise, so F^2 f(l)=f(l). It does not give f(-l). Evenness must be justified separately.

Scope: statement_false

交替辛核中两次变换的指数是 [p-l,k]，字符正交性给 F²f(l)=f(l)，不是 f(-l)。因此所述偶性推导无效，偶性是否另有证明不在此条判定内。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## 3. Evidence and verification

既有source-bound witness + 2026-09-22原文/论证对照；有本轮小检查则另附。

Historical witness execution and current re-execution are separate. This release does not claim every large computation was rerun, all hidden reasoning recovered, or that every target theorem is false.

The full original file inventory and hashes are in [materials.json](materials.json).

- [M01-round-23-response.md](original/M01-round-23-response.md) — inherited_sanitized_source
- [M02-concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md) — inherited_sanitized_source
- [M03-01_r001_r023_physical_gate_CORE.md](original/M03-01_r001_r023_physical_gate_CORE.md) — inherited_sanitized_source
- [M04-MASTER_AUDIT_PROTOCOL.md](original/M04-MASTER_AUDIT_PROTOCOL.md) — inherited_sanitized_source
- [M05-BASELINE.md](original/M05-BASELINE.md) — inherited_sanitized_source
- [M06-round-02-local-audit.md](original/M06-round-02-local-audit.md) — inherited_sanitized_source
- [M07-round-03-local-audit.md](original/M07-round-03-local-audit.md) — inherited_sanitized_source
- [M08-round-06-local-audit.md](original/M08-round-06-local-audit.md) — inherited_sanitized_source
- [M09-round-18-local-audit.md](original/M09-round-18-local-audit.md) — inherited_sanitized_source
- [M10-round-20-local-audit.md](original/M10-round-20-local-audit.md) — inherited_sanitized_source
- [M11-round-21-local-audit.md](original/M11-round-21-local-audit.md) — inherited_sanitized_source
- [M12-round-23-local-audit.md](original/M12-round-23-local-audit.md) — inherited_sanitized_source

## 4. Visible reasoning

Preserved source summaries/excerpts are not complete internal chain of thought. No reasoning has been reconstructed or invented. Source anchors and historical events are in [record.json](record.json).
