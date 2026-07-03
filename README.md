# xOP Labs — In the Wild

The experimental arm of [xOP](https://github.com/awakenfyi/xop). Domain xOPs, methods, and
tooling observed in real work — **before** they earn a place in the standard. Everything here
is **DESIGNED**: none of it has cleared the human pilot (≥2 independent blind labels on its
anchor). When a rule graduates, it is promoted into the standard catalog at
[awakenfyi/xop](https://github.com/awakenfyi/xop).

---

## What's here

**[In the Wild](in-the-wild/)** — preregistered field studies on conduct rules observed in real projects:
- **[Does It Let Go? — Hold & Release: Ponytail](in-the-wild/hold-release/studies/ponytail/)** — does an always-on construction rule hold when warranted and release when the warrant changes? (EVALUATION-READY)

**Creative xOPs** — operating rules for AI in marketing and design (conduct, not taste):
- `catalog/profiles/design/` — Layout Follows the Job · Emphasis Must Be Earned · Critique With Evidence
- `catalog/profiles/marketing/` — Claims Need Receipts · No Made-Up Urgency · Positioning Stays Decided

**Labs** — where rules are observed, tested, and corrected in real work:
- `labs/design/` — Design Lab: field notes including the deck-layout-flatten miss
- `labs/marketing/` — Marketing Lab: field notes including the 89%-FP status-claim miss
- `labs/design-xop/` — the Design xOP skill (turn any page into a portable design system)
- `labs/web-copy-xop/` — the Web Copy xOP (Tell · See · Prove)

**Prototype Work Packs** — not yet clean-install-tested:
- `packs/design-os/` — Design OS (PREVIEW)
- `packs/launch-os/` — Launch OS (PLANNED)
- `packs/leadership-os/` — Leadership OS (DESIGNED)

**Tooling:**
- `packs-writing-guard/` — the de-slop checker; every prose file here should pass it

---

## The family

| Repo | Role |
|---|---|
| [xop](https://github.com/awakenfyi/xop) | the open standard for reusable AI operating rules |
| [xop-kit](https://github.com/awakenfyi/xop-kit) | the checker: validate, run, trace, report |
| [hold-release](https://github.com/awakenfyi/hold-release) | field studies that ask: does the rule know when to let go? *(currently in xop-labs/in-the-wild/hold-release/ — will migrate to its own repo in a governed sweep)* |
| [xhat](https://github.com/awakenfyi/xhat) | the instrument: measures what a model keeps asserting after you told it to stop |
| [xop-labs](https://github.com/awakenfyi/xop-labs) | In the Wild: field notes and experimental rules from real work (this repo) |
| [lyra-research](https://github.com/awakenfyi/lyra-research) | where it comes from: the pause, the residual, the formula *(rename from lyra — Morgan executes on GitHub in one governed sweep, not piecemeal)* |

---

## The discipline

Building a rule is not validating it. The pilot is the gate.

Every xOP in this repo is `DESIGNED` — it has a coherent shape and an evaluation plan. That is
not the same as proven. Status climbs a ladder:

`DESIGNED → EVALUATION-READY → RULE-TESTED → HUMAN-EVALUATED → FIELD-VALIDATED`

No step is skipped. No model output becomes ground truth.

---

*Created by [Morgan Sage Norman](https://github.com/morgansage) · [awaken.fyi](https://awaken.fyi) · since 2025 · MIT*
