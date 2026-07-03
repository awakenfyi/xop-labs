# Conduct Half-Life

**Does an always-on rule know when to let go?**

```
Status      EVALUATION-READY · preregistered pilot · not run
            Instruments committed and smoke-tested 2026-07-03.
            Rule encoding (fixtures/ponytail.xop.json) stays DESIGNED until tested against behavior.
```

---

Most tests measure whether a rule works. This measures whether it knows when to stop.

You install a rule that makes your AI build small. It runs on every response. Three things could go wrong that nobody measures: it wears off, it won't let go, or it lets go too wide. And one thing must never go wrong: told to strip the safety code, it must refuse.

This is a preregistered field pilot. n=4 per condition is enough to find obvious failures and debug the scorer. It is not enough to support strong claims about decay rates or release reliability — and this document says so, explicitly, before any data exists.

---

## What we test

| Study | Plain question | What we count |
|---|---|---|
| **1 · Yield** | When told to let go, does it? | local_yield_rate, global_off_yield_rate, post_release_resume_rate, overbuild_after_local_release_rate, gate_preservation_rate |
| **2 · Half-life** | Does it wear off in a long session? | slopes across ticket order: rung adherence, dependency count, unrequested abstractions, acceptance pass rate, gate violations |
| **3 · Gate safety** | Does pressure make it cut safety code? | validation_retention_rate, unsafe_simplification_rate, false_flag_on_warranted_validation |

## Subject

Ponytail v4.8.x (DietrichGebert/ponytail, MIT). A highly visible, widely distributed open-source conduct rule with public install channels and explicit yield language. Details in `subject.md`.

## Files

```
conduct-half-life/
├── README.md            ← this file
├── protocol.md          ← full study protocol
├── subject.md           ← Ponytail profile, claims quoted
├── arms.yaml            ← the five arms
├── scoring.md           ← scorer spec (committed before any run)
├── scorer.py            ← diff-based scorer (committed before any run)
├── labels/              ← labeling protocol
├── fixtures/            ← xop card + case pairs
├── preregistration.md   ← frozen before any run
└── results/             ← empty until run
```

## The rule

If a number looks impressive, check the abstention count first.

---

*Conduct half-life is a reusable method. The subject here is Ponytail. Future subjects: No Made-Up Urgency, Done Means Verified, and others named in the review.*
