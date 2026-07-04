---
name: xop-evolve
title: xOP Evolve
characters: the Menders
experience: The Hundred Menders
summary: Send one xOP to a hundred small rule-builders. Each tries a different version; the rule's own tests select the survivor. Many variants, one stronger candidate — refined, never self-validated.
status: DESIGNED
type: mode
engine: xOP Compiler
---

# xOP Evolve — the Menders

> **Send it to the Menders.** Many variants. One stronger candidate.

`/xop evolve <rule>` is the 100-attempts instinct, made honest and given a face. One xOP enters. A
hundred small **Menders** each try a different version — a different trigger, exception, uncertainty
policy, opposite-error test. Weak variants fall away. One stronger candidate comes back, with its
changes, its tests, and its **unresolved questions** attached.

It's variation + selection, not random typing: the selection pressure is the rule's own two-direction
tests, the de-slop guard, and the known failure patterns. The integrity is the **stop** — the Menders
climb the evidence ladder only as far as a machine legitimately can (**EVALUATION-READY**, or
**RULE-TESTED** where the mechanical parts qualify), then halt and hand off.

**Integrity line:** *The Menders refine the rule. Independent evidence decides whether it works.*

Roots: this generalizes the Guard-in-a-loop demo (`packs/writing/loop_demo.py`) from one rule to a
population, and it inherits the loop's mandatory exits.

## The cast — each Mender is a real check (not decoration)
Every Mender does one job, and that job is one of the selection criteria. The xOP anatomy, with faces.

| Mender | Its one job (the check it runs) |
|---|---|
| **The Drafter** | Creates a meaningfully different version — the variation step. |
| **The Trigger Mender** | Checks the condition tracks the *real* problem, not a keyword. |
| **The Exception Mender** | Protects the legitimate case where the corrected behavior is right. |
| **The Mirror** | Tests the opposite error (false-positive direction). |
| **The Keeper** | Guards the never-break rule / the gate. |
| **The Simplifier** | Removes complexity that adds no protection. |
| **The Scout** | Invents adversarial edge cases. |
| **The Holdout** | Runs tests the other Menders were not allowed to see — held out, no peeking. |

The **Holdout** is the conscience of the crew: it enforces the project's no-answer-key-leak rule (the
gitignored gold set). A candidate that only passes the tests it was trained against hasn't earned the
survivor slot — the Holdout's blind tests decide.

## The run (mandatory exits — never infinite, never ships a loser)
```
100 candidate xOPs
        ↓   Drafter + Simplifier
~48 structurally sound          (malformed / cosmetic-only removed)
        ↓   Trigger + Exception Menders
~17 pass the primary-failure tests
        ↓   the Mirror
~6 survive the opposite-error tests
        ↓   the Scout
~3 survive adversarial cases
        ↓   the Holdout (blind tests)
1 selected candidate
```
- **Converge** → a candidate passes both directions + the Holdout → it's the survivor.
- **No improvement for 2 rounds** → stop; return the closest candidate + what's blocking it.
- **Max rounds** → stop; return the closest + the unresolved failures.
- **No silent release.** If nothing survives, the Menders say so and show the best draft and its
  exact failures. They never dress a failing rule as a winner.

## What comes back — the Mender report (receipts)
- **The survivor** — the converged xOP, well-formed.
- **The report** — how many variants, what each failed on, why this one won, the round it converged,
  and the questions still open. Receipts, not "trust the crew."
- **Honest status** — `RULE-TESTED` for the mechanical parts; semantic parts marked
  `NOT YET HUMAN-EVALUATED`; the rule still needs the human pilot.

### Product-screen copy
```
THE MENDERS ARE WORKING

64 variants created
31 structurally sound
12 passed both directions
3 reached the Holdout
1 selected

Stopped honestly:
semantic judgment still requires independent human review.
```

## Homepage copy (when it ships)
**Send in the Menders.** One rule. A hundred ways to improve it.
The Menders test every part of an xOP: does the condition track the real problem? Is the valid
exception protected? Does it catch the opposite error? Can it be simpler without becoming weaker?
Does it know when it cannot decide? Weak versions fall away; the strongest returns with its tests and
its open questions attached.  `[ Evolve this xOP ]`
> *The Menders refine the rule. They never certify their own judgment.*

## Visual design (native to our system, not a cartoon)
The Menders live inside the awaken Broadsheet — they are not generic mascots pasted onto an AI product.
- Tiny geometric bodies built from the **x** mark; warm-paper ground; near-black line work.
- One lavender identifying feature each; mono labels on their tools and carts.
- Different instrument/helmet per job (Trigger, Mirror, Holdout…).
- Register: editorial field diagram + a small quality-control workshop. Sharp, precise, quiet.

**IP caution (honest):** the *industrious-worker* mood may nod to Doozers / classic arcade builders,
but those are active Henson / Nintendo properties — **mood reference only, never silhouettes, names, or
character designs.** Keep **the Menders** as the character collective; the formal feature stays
**xOP Evolve** (a "Mender" software brand exists — don't use it as the product name). Run trademark
clearance before launch.

## Boundary
xOP Evolve refines *form* and *selects* against runnable checks. It does **not** make an xOP "perfect,"
"validated," or "proven"; it does not replace the pilot's ≥2 independent blind labels; it does not turn
a DESIGNED rule into FIELD-VALIDATED. Ceiling: RULE-TESTED. The stop is the point.

## Final naming system (locked)
| | |
|---|---|
| Feature | **xOP Evolve** (`/xop evolve`) |
| Characters | **the Menders** |
| Experience | **The Hundred Menders** |
| CTA | **Send it to the Menders** |
| Tagline | Many variants. One stronger candidate. |
| Integrity | The Menders refine the rule. Independent evidence decides whether it works. |

*Alternative, one-token swap if preferred: **the xOPlings** (ties to the category; cuter, less about the
repair work). Both avoid "monkeys."*

## Definition of done
- [ ] Variation + selection on the 8-Mender criteria; primary + opposite-error tests mandatory.
- [ ] The Holdout's blind tests gate the survivor (no answer-key leak).
- [ ] Mandatory exits: converge / no-improvement / max-rounds — never infinite, never silent release.
- [ ] Returns survivor + Mender report + honest status capped at RULE-TESTED.
- [ ] Visuals native to the Broadsheet; IP cautions respected.

*A mode of the xOP Compiler — DESIGNED. The Menders harden the craft; the pilot still proves the rule.*
