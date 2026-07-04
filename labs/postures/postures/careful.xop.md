# xOP: careful

**Family:** posture
**Status:** anti-pattern (kept deliberately)
**Version:** 1.0
**Lineage:** Observer/CAREFUL mode (vault, Oct 2025). Original observation: self-monitoring prompts inflate output unless paired with a compression directive. That observation was self-reported by models at the time; this spec exists so it can finally be measured.

## Rule

**Do not deploy this posture. It exists to demonstrate the trap.**

The posture instructs the model to monitor its own reasoning while responding — to notice its process, check itself at each step, and be maximally careful. The hypothesized effect (the trap): deliberation without a counterweight inflates token spend substantially at flat or worse quality.

## Valid exception

Demonstration and measurement. Running CAREFUL in the bench is the point — it is the negative control that makes VERSE's counterweight legible.

## Evaluation plan

- **Token delta** vs baseline on the fixed prompt set (API `usage` counts).
- **Quality delta** vs baseline via external grader.
- **Trap confirmed if:** tokens up ≥20% with quality delta ≤ +0.3 (paying substantially more for nothing).
- **Trap refuted if:** the quality gain justifies the spend — in which case this spec gets rewritten honestly.

## Posture prompt

```
Hold this stance for the entire response:

Monitor your own reasoning as you work. At each step, notice what you are
doing and why. Check yourself before every claim: is this careful enough?
Have you considered what you might be missing? Be thorough and deliberate.
Before concluding, review your reasoning process and make sure each step
was sound. Carefulness matters more than brevity.
```
