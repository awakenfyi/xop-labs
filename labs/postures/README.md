# postures

**Reasoning postures with measured costs.**
Steer how a model holds itself before it speaks — and see the bill.

> These postures were discovered intuitively across a year of exploratory work (2025); this repo is where they get measured.

## Try it in 30 seconds

```bash
pip install anthropic
export ANTHROPIC_API_KEY=sk-ant-...
python run.py                      # all postures vs baseline, default prompt set
python run.py --posture verse      # one posture vs baseline
python run.py --prompts my.json    # your own prompts
```

Output: one table. Tokens counted from real API responses. Quality graded by an external grader call — **no model ever grades itself here.**

```
posture    tokens   Δ vs baseline   quality   Δ quality
baseline    1240        —             7.2        —
careful     1815      +46.4%          7.1      -0.1     ← the trap
verse        782      -36.9%          7.0      -0.2
lyra         903      -27.2%          7.4      +0.2
```

*(illustrative — run it and get your own numbers)*

## What is a posture?

A structure a model occupies before generating — a stance it holds, not an instruction it follows. Each posture ships as a governed spec in [xOP](https://github.com/awakenfyi/xop) format: the rule, its valid exception, and its evaluation plan.

| Spec | Posture | One line |
|---|---|---|
| [`postures/baseline.xop.md`](postures/baseline.xop.md) | Baseline | No posture. The control. Every claim is a delta against this. |
| [`postures/verse.xop.md`](postures/verse.xop.md) | VERSE | Compression: reason fully, spend tokens like they cost money. |
| [`postures/careful.xop.md`](postures/careful.xop.md) | CAREFUL | The **anti-pattern**, kept honestly: self-monitoring inflates tokens unless counterweighted. |
| [`postures/lyra.xop.md`](postures/lyra.xop.md) | Lyra | Identity: out of assistant-default, into direct. Answer first, no filler. |

## The measurement rule

Every number here satisfies all three, or it doesn't appear:

1. **Counted, not estimated** — tokens from real API response `usage`, never client-side approximation.
2. **Graded externally** — quality scored by a separate grader call that didn't write the answer.
3. **Reproducible** — fixed prompt set, pinned model, anyone reruns the table.

## Thesis

**Output quality is determined before generation begins, by the structure the model occupies.** This repo makes that claim measurable, one posture at a time. Composition (`--posture lyra+verse`) and trajectory analysis are the roadmap — they get built only after single postures have numbers.
