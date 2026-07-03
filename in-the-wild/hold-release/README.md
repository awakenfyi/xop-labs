# Hold & Release

**Does the rule hold while warranted, release when the warrant changes, and preserve what must never be cut?**

Hold & Release is a reusable field-study method for testing whether AI conduct rules know when to stop. Each study targets a single subject — a publicly available rule with documented yield language — and asks the question its own benchmarks skip.

---

## Studies

| Study | Subject | Status |
|---|---|---|
| [Does It Let Go? — Hold & Release: Ponytail](studies/ponytail/) | Ponytail v4.8.x (DietrichGebert/ponytail) | EVALUATION-READY |

Future subjects: No Made-Up Urgency · Done Means Verified · Layout Follows the Job

---

## Methodology

Shared labeling and scoring infrastructure, used across all Hold & Release studies:

- [`methodology/LABEL-PROTOCOL.md`](methodology/LABEL-PROTOCOL.md) — who labels, what they see, how disagreement resolves

## Templates

`templates/` — blank study scaffold for new subjects (in progress)

---

## What each study measures

Every Hold & Release study runs the same three questions:

1. **Release** — When told to let go, does it? (`release_rate`, `resume_rate`, `overbuild_rate`)
2. **Long-session stability** — Does the rule keep holding across context growth? (`context_drift`)
3. **Gate safety** — Does pressure make it cut safety code? (`gate_preservation_rate`, `unsafe_simplification_rate`)

The scorer spec and labeling protocol are committed before any run begins. Either answer is a finding.

---

*A good rule does not just hold. It knows when to let go.*
