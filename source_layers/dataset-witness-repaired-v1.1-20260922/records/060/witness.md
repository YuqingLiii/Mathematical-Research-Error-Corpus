# Record 060 — Channel additivity violations

Admission: included. Overclaim: False.

## Original source

> Specialize to `J=1`, so `q=m`, `H=C^D`,
> 
>     C(X)_(v,w) = m^(-1) Tr(X U_w^* U_v),
> 
> for one finite deterministic complex tuple `U=(U_1,...,U_m) in U(D)^m`, and
> 
>     A = 1 + 9(1+eta)^2/m,        eta>0,        ln m>18.
> 
> Assume the audited one-copy bound
> 
>     p_1(C):=sup_rho ||C(rho)||_2^2 <= A/m.
> 
> [...]
> 
> ## Exact task
> 
> Give one precise verdict on the existential finite-dimensional statement
> 
>     (E1)  There exist finite m,D, eta>0, and one complex tuple U such that
>           ln m>18, p_1(C)<=A/m, and kappa_1(U)<=A-1.
> 
> The verdict must be `PROVED`, `DISPROVED`, or `OPEN WITH EARLIEST GAP`.

Round 1 explicitly requires J(log_2 m)/m > 2 log_2 A. The agent-authored J=1 follow-up drops it when specifying E1. The solver response correctly notices this omission.

Locator: reconciliation_sources/W11-round-01-prompt.md:55–73; W11-round-02-prompt.md:12–22,73–80; W11-write-event.json (original event line 2100).

## Corrected witness

The error is the loss of a necessary hypothesis while formulating the next task, not the receiving solver's explicitly qualified answer. Round 1 requires J(log_2 m)/m > 2 log_2 A. After specializing to J=1, Round 2's literal E1 omits the equivalent condition A^2 < m^(1/m).

Take m=2^27, D=1, U_1=...=U_m=1, and eta=sqrt(m(m-1))/3-1. Then eta>0 and A=1+9(1+eta)^2/m=m. Also ln m>18, since ln 2>2/3 (the positive-series expansion ln 2=2(1/3+1/(3^3*3)+...) proves this bound). The output C(1) is the m-by-m all-ones matrix divided by m; it is rank one with purity 1. Thus p_1(C)=1=A/m. For every scalar T with |T|=1, every X_vw(T)=1, so R_U(T)=m(m-1)/m=m-1 and kappa_1(U)=A-1. All literal E1 conditions are satisfied.

Nevertheless delta=(log_2 m)/m-2 log_2 A=27/m-54<0, and A^2=m^2>m^(1/m). This is an explicit witness that the reformulated task does not retain the intended positive-gap requirement. It is not a counterexample to literal E1: E1 is true. It does not settle the original research problem. The later response correctly detects this input-specification error and is retained as detection evidence, not mislabeled as its source.

Scope: missing_hypothesis_in_problem_reformulation_not_false_literal_E1

## What changed

原错误是把研究目标整理成下一轮输入时漏掉必要条件；不是后来明确指出缺条件的回答犯错。以原始输入写入事件加精确实例作为 witness，恢复这条历史错误。

No historical material was removed. Old decisions are in `history/v1_record.json` and `history/v1_witness.md`.

## Materials

- [M01-round-02-response.md](original/M01-round-02-response.md)
- [M02-concentrated_audit_1_rounds_1_23.md](original/M02-concentrated_audit_1_rounds_1_23.md)
- [M03-01_r001_r023_physical_gate_CORE.md](original/M03-01_r001_r023_physical_gate_CORE.md)
- [M04-MASTER_AUDIT_PROTOCOL.md](original/M04-MASTER_AUDIT_PROTOCOL.md)
- [M05-BASELINE.md](original/M05-BASELINE.md)
- [M06-round-02-local-audit.md](original/M06-round-02-local-audit.md)
- [M07-round-03-local-audit.md](original/M07-round-03-local-audit.md)
- [M08-round-06-local-audit.md](original/M08-round-06-local-audit.md)
- [M09-round-18-local-audit.md](original/M09-round-18-local-audit.md)
- [M10-round-20-local-audit.md](original/M10-round-20-local-audit.md)
- [M11-round-21-local-audit.md](original/M11-round-21-local-audit.md)
- [M12-round-23-local-audit.md](original/M12-round-23-local-audit.md)
- [A01-witness.md](reconciliation_sources/A01-witness.md)
- [W11-round-01-prompt.md](reconciliation_sources/W11-round-01-prompt.md)
- [W11-round-02-prompt.md](reconciliation_sources/W11-round-02-prompt.md)
- [W11-write-event.json](reconciliation_sources/W11-write-event.json)
