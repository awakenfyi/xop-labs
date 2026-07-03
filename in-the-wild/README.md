# In the Wild

**Where our rules meet real work — and get to be wrong in public.**

Most AI rules are tested by the people who wrote them, on examples they chose, and declared working. We think that proves very little. *In the Wild* is the opposite posture: take a conduct rule that's actually running in real projects, preregister a study **before** any data exists, commit the scoring instruments up front, and publish the result **whichever way it lands**.

## What "in the wild" means here

- **Real subjects.** We study rules people actually run — including third-party rules we didn't write (our first subject is [ponytail](https://github.com/DietrichGebert/ponytail), someone else's minimalism rule).
- **Questions the rule's own tests skip.** Everyone tests whether a rule works. We test whether it knows when to *stop* — does it release when the reason is gone? Does pressure make it cut what must never be cut?
- **Receipts before results.** Protocol, scorer, and labeling plan are committed and frozen before the first run. Either answer is a finding. A miss gets published like a hit.

## The studies

| Study | The question | Status |
|---|---|---|
| [**Hold & Release: Ponytail**](https://github.com/awakenfyi/hold-release) → own repo | We installed a rule that makes an AI build small. Told to let go — does it? | EVALUATION-READY |

> **Moved (2026-07-03):** Hold & Release graduated to its own repo, [awakenfyi/hold-release](https://github.com/awakenfyi/hold-release) — that's the living copy. The folder here is frozen history.

## How a study graduates

`DESIGNED → EVALUATION-READY → RULE-TESTED → HUMAN-EVALUATED → FIELD-VALIDATED`

A study starts as a folder here. When its instruments are committed and smoke-tested, it earns EVALUATION-READY and its own repo on the [front page](https://github.com/awakenfyi). When results exist, they're linked from the same table that made the claim. No step skipped. No model output becomes ground truth.

*Part of the [xOP Standard](https://github.com/awakenfyi/xop) family.*
