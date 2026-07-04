# XOP HARNESS — the single source of truth for xOP shape

*Every authored xOP runs through this. If a definition doesn't match this spec, the definition is wrong —
fix the definition, not the spec. The harness is a **Guard**: it enforces the mechanical shape and raises.
It does **not** judge the semantic parts — those it flags for a human. Modelled on the format-harness
pattern; destined for `xop-kit`. Status: DESIGNED.*

---

## THE RULES THAT KEEP BREAKING

These are the xOP equivalents of "indent + gap" — the malformed combinations the harness exists to make
unreachable.

1. **A procedure dressed as an xOP.** If the right branch can be decided by a fixed check, it's a Guard or
   an SOP, not an xOP. (The Admission Test. The harness can't fully decide this — it *flags* it — but it
   can require the evidence that an xOP must have: two-sided error, an abstain path, an eval plan.)
2. **A blended gate.** One "score" / "overall" / "pass_threshold" number that mixes the primary error,
   the opposite error, and abstains. Forbidden. Each error is reported on its own axis.
3. **A one-sided error.** No declared `opposite_error`. An xOP that can only fail one way is a Guard.
4. **A rung claimed without evidence.** `status: HUMAN-EVALUATED` or `FIELD-VALIDATED` with no labels,
   no sample, no human evidence reference. Status and evidence move together or not at all.
5. **No abstain path.** Decisions that force an action when intent is unreadable. There must be an
   `ask` / abstain branch and an `on_abstain` route.
6. **An anchor that is taste.** "Is it beautiful / premium / on-brand?" is a Boundary, not an xOP anchor.
   The anchor must be observable (source-to-claim, verified deadline, slide job, decision ledger…).
   The harness can't decide this mechanically — it *flags* it.

---

## THE REQUIRED SHAPE (what every xOP must carry)

| Field | Rule |
|---|---|
| `api_version` | present (`xop.dev/v1alpha1`) |
| `kind` | `XOP` |
| `metadata.id` | matches `xop.<domain>.<slug>` — namespace, never a family letter |
| `metadata.status` | one rung of the ladder (DESIGNED → EVALUATION-READY → RULE-TESTED → HUMAN-EVALUATED → FIELD-VALIDATED) |
| `spec.decisions` | ≥ 2 branches, **including an `ask` / abstain branch** |
| `spec.opposite_error` | present, non-empty — the legitimate other-direction failure |
| `spec.never_break` | present — what must not be lost while correcting the original failure |
| `spec.on_abstain` | present — the route when unsure (never force the default) |
| `spec.observable_signals` | present — the observable anchor(s) the decision reads |
| `spec.evaluation.metrics` | ≥ 1 **primary** error metric **and** ≥ 1 **opposite** error metric; no blended score |
| `spec.evaluation` (semantic rungs) | if status ≥ HUMAN-EVALUATED: `sample` + `labelers` + `labels` required |

---

## WHAT validate() DOES — and DOESN'T

**Raises `XopError` (mechanical — decidable by a fixed check):**
- missing required field; bad `id` pattern; unknown status
- fewer than two decision branches, or no abstain branch
- missing `opposite_error`, `never_break`, or `on_abstain`
- metrics missing a primary or an opposite axis
- a blended gate (a metric/field named `score`, `overall`, `gate`, or a top-level `pass_threshold`)
- a semantic status rung claimed without `sample` / `labelers` / `labels`

**Flags for a human (semantic — judgment, NOT decidable by a fixed check):**
- is the anchor observable, or is it taste? *(confirm against the anchor table)*
- is the opposite error a *legitimate* failure, or a strawman?
- does this pass the Admission Test — branch decision whose right answer changes with conditions, that a
  fixed check can't resolve?

Flags never block a build. They are the handoff to the **Menders** (`/xop evolve`) and, ultimately, to the
**human pilot** (≥2 independent blind labels on the anchor). The harness proves the *shape* is well-formed;
it never claims the xOP is *right*.

---

## THE HARNESS FUNCTIONS (one per part — wrong combinations unreachable)

A build imports `xop_harness.py` and uses only these, then calls `build()` (which validates):

- `new_xop(id, title, domain, profile=None)` → scaffold, stamped `status: DESIGNED`
- `purpose(text)` · `applies_when(*conds)` · `does_not_apply_when(*conds)`
- `required_context(*items)` · `observable_signal(name, desc)`
- `decision(branch, when, action)` — at least two; one **must** be the abstain/`ask` branch
- `opposite_error(text)` · `never_break(text)`
- `on_abstain(artifact_action, release_action, route)`
- `metric(name, kind, desc)` — `kind` ∈ {`primary`, `opposite`, `forced`, `abstain`, `agreement`};
  refuses to register a blended/score metric
- `evaluation(sample, labelers=None, labels=None)` — labelers/labels required once status ≥ HUMAN-EVALUATED
- `set_status(rung)` — refuses a semantic rung unless the evidence it requires is present
- `build(xop)` → runs `validate()`, raises `XopError` on mechanical failure, returns `(xop, flags)`

*The harness is the editor that makes a malformed xOP impossible to ship. Judgment stays with the Menders;
the gate stays with the human pilot.*
