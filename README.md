# xOP Labs

**Domain xOPs observed in the wild — before they earn a place in the standard.**

![MIT](https://img.shields.io/badge/license-MIT-blue) ![designed](https://img.shields.io/badge/status-designed-lightgrey)

The experimental arm of [xOP](https://github.com/awakenfyi/xop). Every rule here is `DESIGNED` — it has a coherent shape and an evaluation plan. None has cleared the human pilot (≥2 independent blind labels on its anchor). When a rule graduates, it moves into the standard catalog at [awakenfyi/xop](https://github.com/awakenfyi/xop).

---

## What's here

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

## The discipline

Building a rule is not validating it. The pilot is the gate.

Every xOP in this repo is `DESIGNED` — it has a coherent shape and an evaluation plan. That is
not the same as proven. Status climbs a ladder:

`DESIGNED → EVALUATION-READY → RULE-TESTED → HUMAN-EVALUATED → FIELD-VALIDATED`

No step is skipped. No model output becomes ground truth.

---

## The family

| Repo | One line | Status |
|---|---|---|
| [lyra](https://github.com/awakenfyi/lyra) | the formula + inference core (`L = x − x̂`) | research code |
| [xop](https://github.com/awakenfyi/xop) | the open standard for AI conduct | alpha |
| [xop-kit](https://github.com/awakenfyi/xop-kit) | the reference runtime: Guards, CLI | alpha, `git clone` + `pip install -e .` |
| [xop-labs](https://github.com/awakenfyi/xop-labs) *(this repo)* | domain xOPs observed in the wild | designed |
| [xhat](https://github.com/awakenfyi/xhat) | session-depth warrant ledger: how much did the model carry past revocation? | v0.1, lexical fallback |

---

*Created by [Morgan Sage Norman](https://github.com/morgansage) · [awaken.fyi](https://awaken.fyi) · since 2025 · MIT*
