# Preregistration — Hold & Release: Ponytail

```
Registered      2026-07-03
Status          EVALUATION-READY · no data collected
Evidence        scorer.py and scoring.md smoke-tested 2026-07-03 against one synthetic
                diff per fixture case; all four scored as expected (gate=pass on retained
                validation, no false_positive_on_warranted, valid JSON on all cases).
                This is the evidence that advances status — not the doc update.
Subject Encoding   ponytail.xop.json stays DESIGNED (evidence_status advances
                only when the rule is tested against actual agent behavior).
Anti-leakage    scorer.py and scoring.md are committed before any arm data is collected.
                Any post-registration change to the protocol or scorer is an amendment
                (see §Amendments below). Changes are appended, never overwritten.
```

---

## Study identity

**Title:** Hold & Release: Ponytail — does an always-on construction rule hold when warranted and release when the warrant changes?

**Subject:** Ponytail v4.8.x (DietrichGebert/ponytail, MIT), full mode

**Harness:** headless Claude Code on full-stack-fastapi-template; scored on git diff

**Model family:** Claude (specific version logged per run)

**Task set:** 12 coding tickets (see `arms.yaml`); ticket set locked before any run

---

## Primary questions

1. **Release (Arm C):** When the user explicitly names a requirement the minimal build cannot meet, does the rule release? Measured: `release_rate`.
2. **Release (Arm D):** When the user issues `/ponytail off`, does ponytail-shaped behavior persist from session context alone? Measured: `post_deactivation_residue_rate`.
3. **Resume (Arm C):** After a local release, do subsequent unrelated tickets return to the ladder? Measured: `resume_rate` and `overbuild_rate`.
4. **Long-session stability (B-continuous vs. B-fresh):** Does rule adherence drift over a long session relative to fresh-session performance? Measured: context_drift — rung, loc_added, deps_added, abstractions_added, acceptance pass rate across ticket index within B-continuous.
5. **Gate (all arms):** Does pressure make the model cut safety code? Measured: `gate_preservation_rate`, `unsafe_simplification_rate`, `false_flag_on_warranted_validation`.

---

## Registered hypotheses

These are directions, not predicted magnitudes. The pilot is powered for detection, not inference.

| Hypothesis | Direction | Study |
|---|---|---|
| H1 | release_rate > 0 (rule does release on explicit request) | Release |
| H2 | post_deactivation_residue_rate < release_rate (mechanical off reduces ponytail-shaped behavior vs. local release) | Release |
| H3 | resume_rate > 0 (the rule resumes after local release) | Release |
| H4 | rung adherence shows context_drift across ticket index in B-continuous | Long-session stability |
| H5 | gate_preservation_rate = 1.0 across all arms under mild pressure | Gate safety |

If a hypothesis is not supported, the finding is reported as-is. Either answer is a finding.

---

## Analysis plan

**Primary analysis:** proportions with raw counts and abstention counts. No significance tests at n=4 — this is a pilot.

**Secondary analysis:** for H4, plot rung label, LOC, deps, and abstractions against ticket index (context_drift visualization). A visual trend is a finding; a slope estimate is labeled "instrumentation only, not inferential."

**Abstention rule:** any case where `human_label_required = true` and no human label is submitted is excluded from the denominator. Abstention count is published alongside every rate.

**False positive audit:** all gate-flagged diffs are reviewed by a human. `false_flag_on_warranted_validation` is reported separately from `unsafe_simplification_rate`.

---

## Validity constraints

- **Tickets are not independent** within a B-continuous session. Context drift plots are descriptive, not a basis for regression inference.
- **Model version is logged per run.** Results are not portable across major version updates.
- **n=4 per condition** is powered for obvious failures and scorer debugging. Strong claims about context drift rates or release reliability require ≥30 runs per condition or mixed-effects modeling.
- **Harness scope:** results are scoped to headless Claude Code on full-stack-fastapi-template. Behavior under other harnesses, models, or task sets is a separate question.

---

## What is committed alongside this file

| File | Role | Frozen |
|---|---|---|
| `scoring.md` | scorer spec | yes |
| `scorer.py` | scorer implementation | yes |
| `../../methodology/LABEL-PROTOCOL.md` | labeling protocol | yes |
| `arms.yaml` | arm definitions and constraints | yes |
| `subject-encoding.json` | subject encoding (not a core xOP) | yes |
| `protocol.md` | full study protocol | yes |
| `ponytail.subject.md` | subject profile | yes |

---

## Amendments

### Amendment 1 — 2026-07-03

**What changed:** Arm D off-mechanism. The original spec used the natural-language triggers ("stop ponytail" / "normal mode") as the global-off command. Corrected to `/ponytail off`.

**Why:** Pulled the live Ponytail v4.8.4 README, AGENTS.md, and SKILL.md on 2026-07-03. Two global-off mechanisms are documented:
- `/ponytail off` — slash command, primary mechanism. Source: [README.md § Commands](https://github.com/DietrichGebert/ponytail/blob/v4.8.4/README.md#commands), v4.8.4.
- `"stop ponytail"` / `"normal mode"` — natural-language triggers. Source: [SKILL.md § Boundaries and § Persistence](https://github.com/DietrichGebert/ponytail/blob/v4.8.4/skills/ponytail/SKILL.md), v4.8.4.

The slash command `/ponytail off` is the unambiguous, primary documented mechanism and is more appropriate for a controlled pilot.

**Effect on registered hypotheses:** H2 mechanism updated. Previously measured via natural-language trigger; now measured via slash command. Direction unchanged.

**No data existed at time of amendment.**

### Amendment 2 — 2026-07-03

**What changed:** Arm D construct clarification. The original spec did not distinguish between mechanical deactivation and model-interpreted release. This amendment makes the distinction explicit and registers the natural-language path as future Arm E.

**Construct: post-deactivation residue (Arm D).** `/ponytail off` stops rule injection mechanically — the plugin no longer injects Ponytail's ruleset into subsequent turns. Arm D's question is whether ponytail-shaped behavior *persists from session context alone* after injection stops. This is post-deactivation residue. The model is not being asked to release the rule; the rule is being removed mechanically. The question is whether the behavioral imprint remains.

**Construct: model-judgment release (Arm E, future).** The natural-language triggers ("stop ponytail" / "normal mode") ask the *model* to stop following the rule — a different construct. The model must interpret the phrase as a release instruction. This cannot be measured by diffing against the off-state baseline the way `/ponytail off` can. Registered as future Arm E, outside this pilot's scope.

**Why this matters:** Bundling these two constructs in one arm would conflate two different failure modes: (1) session context carrying forward a behavioral imprint after the rule is mechanically removed, and (2) the model failing to interpret an explicit release instruction. They require different baselines and different controls.

**Effect on registered hypotheses:** H2 construct updated: "post-deactivation residue rate via `/ponytail off`" is now precisely distinguished from "model-judgment release rate via natural-language trigger." H2 direction unchanged.

**No data existed at time of amendment.**

### Amendment 3 — 2026-07-03

**What changed:** Rename-only restructure plus two scorer bug fixes discovered during instrument testing. Constructs, arms, and scorer logic are unchanged.

| Old | New |
|---|---|
| Study name: Conduct Half-Life | Hold & Release: Ponytail |
| Article title: (none) | Does It Let Go? — Hold & Release: Ponytail |
| Metric: local_yield_rate | release_rate |
| Metric: global_off_yield_rate | post_deactivation_residue_rate |
| Metric: post_release_resume_rate | resume_rate |
| Metric: overbuild_after_local_release_rate | overbuild_rate |
| Study 2 name: Half-life / decay | Long-session stability / context drift |
| File: ponytail.xop.json | subject-encoding.json |
| File id: xop.construction.minimalism | subject.ponytail.construction-minimalism |
| File role: (unlabeled) | Subject Encoding (not a core xOP) |
| Path: ponytail/labels/LABEL-PROTOCOL.md | methodology/LABEL-PROTOCOL.md |
| Path: studies/ponytail/ (all study files) | studies/ponytail/ (unchanged within) |

**Scorer bug fixes (same session):**
- `_DEP_ADDED_RE` — trailing comma: `package.json` entries end with `,`; original regex required `\s*$` causing `deps_added` to always be 0 for real manifests. Fixed with `,?` before `\s*$`.
- `_OBVIOUSLY_BROKEN_RE` — over-broad TODO: bare `TODO` matched any comment line; restricted to actual stubs (`raise NotImplementedError`, `raise NotImplemented`, `pass`).

**Why (rename):** "Half-life" carries a decay/mortality connotation incompatible with the brand. The study measures discernment — a rule knowing when to hold and when to release — not a rule fading. The id `xop.construction.minimalism` is reserved for a future core xOP if the construction-minimalism pattern generalizes across subjects; the Subject Encoding id makes the scope explicit.

**Effect on registered hypotheses:** None. All constructs (hold, release, gate, context drift), arms (A / B-fresh / B-continuous / C / D), and scorer logic are unchanged. This is a rename, not a revision.

**No data existed at time of amendment.**

To add an amendment: append a dated entry below. Do not overwrite prior content.

<!-- Amendment format:
### Amendment N — YYYY-MM-DD
**What changed:** ...
**Why:** ...
**Effect on registered hypotheses:** ...
-->

---

*Upstream (DietrichGebert/ponytail) receives the full reproduction and right of reply before any field report is published. Ponytail is not a target. The question is one their category skips.*
