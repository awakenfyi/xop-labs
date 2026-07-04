# xOP: baseline

**Family:** posture
**Status:** control
**Version:** 1.0

## Rule

No posture. The model receives the task prompt with no system-level stance. This is the control condition — every measured claim in this repo is a delta against baseline.

## Valid exception

None. The control is never modified. If a baseline run looks wrong, fix the prompt set or the pinned model — never the control.

## Evaluation plan

- Baseline runs on every prompt in the set, every time, even when testing a single posture.
- Its token counts come from API response `usage`; its quality score from the external grader.
- Baseline results are reported in every table. A posture with no baseline column is not a result.

## Posture prompt

*(none — the runner sends no system prompt for baseline)*
