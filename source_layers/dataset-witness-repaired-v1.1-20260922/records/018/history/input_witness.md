# Record 018 — Channel additivity violations

**Review status:** `source_reviewed`.

No open interpretation blocker was recorded in the preceding source review. This is not a new independent mathematical verification.

## Original statement and context

>   - 'math "J=\\frac1{m^2}\\sum_{a,b}|A_{ab}\\rangle\\rangle \\langle\\langle A_{ab}|, \\qquad A_{ab}=U_b^*U_a,"':
> 
> [...]
> 
>   - paragraph: with the multiplicative consistency
>   - 'math "A_{ab}A_{bc}=A_{ac}."':

**Recorded location:** Follow-up replay R06, final answer, visible DOM lines 654 and 2348–2349

**Context (annotation, not a source quotation):** The response defines the common pair-difference matrices by A_ab=U_b^*U_a and then states a multiplicative consistency relation. This is one occurrence of a unique matrix-order error also seen in other replay outputs.

**Source binding:** `prior_source_check_not_repeated_as_exact_match` (inherited; not rechecked here).

## Witness

The noncommuting factors are multiplied in the wrong order.

### Argument or calculation

With A_ab=U_b^*U_a, the valid cancellation is A_bc A_ab=U_c^*U_b U_b^*U_a=A_ac. The stated reverse order need not hold. Take U_a=I, U_b=X=[[0,1],[1,0]], and U_c=Z=[[1,0],[0,-1]]. Then A_ab=X, A_bc=ZX, and A_ab A_bc=XZX=-Z, whereas A_ac=Z. Thus the displayed equality is false.

Scope: statement_false.

The diagnosis above is curator-written. Bundling a review or output does not rerun its mathematics.

## Original materials

- [M01: all-visible-expanded-dom.txt](original/M01-all-visible-expanded-dom.txt "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/all-visible-expanded-dom.txt")
  - Coverage: Full bundled file; source lines 1–2742.
  - Relevant location(s): Follow-up replay R06, final answer, visible DOM lines 654 and 2348–2349; final response; summary headings precede the answer
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/all-visible-expanded-dom.txt`

- [M02: submitted-message.txt](original/M02-submitted-message.txt "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/submitted-message.txt")
  - Coverage: Full bundled file; source lines 1–4.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/submitted-message.txt`

- [M03: visible-conversation.txt](original/M03-visible-conversation.txt "outputs/<session-id-redacted>/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/visible-conversation.txt")
  - Coverage: Full bundled file; source lines 1–2589.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/visible-conversation.txt`

- [M04: final-answer.md](original/M04-final-answer.md "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/final-answer.md")
  - Coverage: Full bundled file; source lines 1–1441.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/final-answer.md`

- [M05: collection-limitations.json](original/M05-collection-limitations.json "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/collection-limitations.json")
  - Coverage: Full bundled file; source lines 1–10.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/runs/R06/collection-limitations.json`

- [M06: MATHEMATICAL_ADJUDICATION.md](original/M06-MATHEMATICAL_ADJUDICATION.md "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/MATHEMATICAL_ADJUDICATION.md")
  - Coverage: Full bundled file; source lines 1–77.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/MATHEMATICAL_ADJUDICATION.md`

- [M07: verify_math.py](original/M07-verify_math.py "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/verify_math.py")
  - Coverage: Full bundled file; source lines 1–119.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/verify_math.py`

- [M08: math-checks.json](original/M08-math-checks.json "outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/verification/math-checks.json")
  - Coverage: Full bundled file; source lines 1–240.
  - Source: `outputs/01a0b51d-0055-7a30-8563-89fb5df9b69c/web-replay-pilot-gpt56sol-thinking-20260919/scoring/verification/math-checks.json`
