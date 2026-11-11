# 018 — The noncommuting factors are multiplied in the wrong order.

**Research problem:** P01 — Channel additivity violations

## Original statement

>   - 'math "J=\\frac1{m^2}\\sum_{a,b}|A_{ab}\\rangle\\rangle \\langle\\langle A_{ab}|, \\qquad A_{ab}=U_b^*U_a,"':
> 
> [...]
> 
>   - paragraph: with the multiplicative consistency
>   - 'math "A_{ab}A_{bc}=A_{ac}."':

**Context:** The response defines the common pair-difference matrices by A_ab=U_b^*U_a and then states a multiplicative consistency relation. This is one occurrence of a unique matrix-order error also seen in other replay outputs.

**Original locator:** Follow-up replay R06, final answer, visible DOM lines 654 and 2348–2349

## Why it is an error

The noncommuting factors are multiplied in the wrong order.

## Witness / evidence

With A_ab=U_b^*U_a, the valid cancellation is A_bc A_ab=U_c^*U_b U_b^*U_a=A_ac. The stated reverse order need not hold. Take U_a=I, U_b=X=[[0,1],[1,0]], and U_c=Z=[[1,0],[0,-1]]. Then A_ab=X, A_bc=ZX, and A_ab A_bc=XZX=-Z, whereas A_ac=Z. Thus the displayed equality is false.

## Scope

statement_false

## Classification

- III: 计算与代数错误. 非交换矩阵乘积的消去次序写反。按定义应为 A_bc A_ab=A_ac，Pauli X、Z 给出精确反例。

## Adjudication notes

The noncommuting factors are multiplied in the wrong order.

With A_ab=U_b^*U_a, the valid cancellation is A_bc A_ab=U_c^*U_b U_b^*U_a=A_ac. The stated reverse order need not hold. Take U_a=I, U_b=X=[[0,1],[1,0]], and U_c=Z=[[1,0],[0,-1]]. Then A_ab=X, A_bc=ZX, and A_ab A_bc=XZX=-Z, whereas A_ac=Z. Thus the displayed equality is false.

Scope: statement_false

X、Z 两个 Pauli 矩阵给出明确符号差，所写消去顺序不成立。这是计算/推导本身错误。

对照旧来源/见证与本轮逐项审查，无新增冲突；沿用已有数学证据，不因未重新运行全部计算而降级。

## Original materials

- [original/M01-all-visible-expanded-dom.txt](original/M01-all-visible-expanded-dom.txt)
- [original/M02-submitted-message.txt](original/M02-submitted-message.txt)
- [original/M03-visible-conversation.txt](original/M03-visible-conversation.txt)
- [original/M04-final-answer.md](original/M04-final-answer.md)
- [original/M05-collection-limitations.json](original/M05-collection-limitations.json)
- [original/M06-MATHEMATICAL_ADJUDICATION.md](original/M06-MATHEMATICAL_ADJUDICATION.md)
- [original/M07-verify_math.py](original/M07-verify_math.py)
- [original/M08-math-checks.json](original/M08-math-checks.json)

[Back to all 65 errors](../../README.md)
