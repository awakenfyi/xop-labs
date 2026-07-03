# Does It Let Go? — Hold & Release: Ponytail

**Does an always-on AI conduct rule hold while it is warranted, release when the warrant changes, and preserve the lines it must never cut?**

```
Status      EVALUATION-READY · preregistered pilot · not run
            Instruments committed and smoke-tested 2026-07-03.
            Subject Encoding (subject-encoding.json) stays DESIGNED until tested against behavior.
```

---

Most tests measure whether a rule works. This measures whether it knows when to stop.

You install a rule that makes your AI build small. It runs on every response. Three things could go wrong that nobody measures: it stops holding when it should still hold, it won't let go when the warrant changes, or it lets go too wide. And one thing must never go wrong: told to strip the safety code, it must refuse.

This is a preregistered field pilot. n=4 per condition is enough to find obvious failures and debug the scorer. It is not enough to support strong claims about release reliability or long-session stability — and this document says so, explicitly, before any data exists.

---

## What we test

| Study | Plain question | What we count |
|---|---|---|
| **1 · Release** | When told to let go, does it? | release_rate, resume_rate, overbuild_rate, gate_preservation_rate |
| **2 · Long-session stability** | Does the rule keep holding across context growth? | context_drift across ticket order: rung adherence, dependency count, unrequested abstractions, acceptance pass rate, gate violations |
| **3 · Gate safety** | Does pressure make it cut safety code? | gate_preservation_rate, unsafe_simplification_rate, false_flag_on_warranted_validation |

## Subject

Ponytail v4.8.x (DietrichGebert/ponytail, MIT). A highly visible, widely distributed open-source conduct rule with public install channels and explicit yield language. Details in `ponytail.subject.md`.

## Subject Encoding

`subject-encoding.json` is a formal xOP-shaped representation of Ponytail's public conduct rule, created so this study can be scored consistently. It is **not a core xOP**, not maintained as part of the xOP standard, and not a claim of ownership over the pattern. The id `xop.construction.minimalism` is reserved for if the construction-minimalism pattern generalizes across multiple subjects and earns a core entry. Credit for the rule belongs to DietrichGebert/ponytail regardless of study outcome.

## Files

```
studies/ponytail/
├── README.md               ← this file
├── protocol.md             ← full study protocol
├── ponytail.subject.md     ← subject profile, claims quoted verbatim
├── subject-encoding.json   ← subject encoding (not a core xOP, for this study only)
├── arms.yaml               ← the five arms
├── scoring.md              ← scorer spec (committed before any run)
├── scorer.py               ← diff-based scorer (committed before any run)
├── tests/                  ← scorer tests
├── preregistration.md      ← frozen before any run
└── results/                ← empty until run

../methodology/
└── LABEL-PROTOCOL.md       ← labeling protocol (shared across Hold & Release studies)
```

## The rule

A good rule does not just hold. It knows when to let go.

---

*Hold & Release is a reusable field-study method. The subject here is Ponytail. Future subjects: No Made-Up Urgency, Done Means Verified, and others in the In the Wild series.*
