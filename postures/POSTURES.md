# POSTURES

**Reasoning postures with measured costs.**
Steer how a model holds itself before it speaks — and see the bill.

---

## What this is

A posture is a structure a model occupies before generating — not an instruction it follows, a stance it holds. Postures change output quality, token spend, and robustness under pressure. This repo names them, specs them in xOP format, and **measures them**: real tokenizer counts, external grader, side-by-side tables. No model ever grades itself here.

One thesis, all the way down:

> **Output quality is determined before generation begins, by the structure the model occupies.**

## What this is not

- Not prompt tips. Every posture is a governed spec: rule, valid exception, evaluation plan.
- Not a consciousness framework. Prior work used that language; this repo uses measurements.
- Not a wrapper product. It's a library + a bench. The data is the product.

---

## What we're building — v1 scope

**Four posture specs + one runner.** That's the whole v1. Everything else is roadmap.

| Spec | Posture | One line | Status |
|---|---|---|---|
| `baseline.xop.md` | **Baseline** | No posture. The control. Every claim is a delta against this. | control |
| `verse.xop.md` | **VERSE** | Compression posture: reason fully, spend tokens like they cost money. | needs measurement |
| `careful.xop.md` | **CAREFUL** | Deliberation posture — kept as the **anti-pattern**: self-monitoring inflates tokens unless counterweighted. The trap, demonstrated. | needs measurement |
| `lyra.xop.md` | **Lyra** | Identity posture: out of assistant-default, into direct. Answer first, no filler, no theater. | needs measurement |

**The runner** (`run.py`): prompt set in → each posture applied → tiktoken counts + external-grader quality score → one table out.

**The 30-second try:** `python run.py --posture verse` on your own API key. Watch CAREFUL inflate the bill. Watch VERSE claw it back. On *your* prompts.

**Deferred, deliberately:**
- **YODEL** (settle-then-speak) — needs open-weights instrumentation to be more than a vibe. Rung 2.
- **MANDALA** (composition) — becomes real only after single postures have numbers. Then `--posture lyra+verse` is an experiment, not a metaphor. Rung 2.
- More postures — the library grows one measured spec at a time, never faster than the data.

---

## Vocabulary — use these words, not those

Clarity is the product. One term per concept, no synonyms drifting.

| Say | Never say | Because |
|---|---|---|
| posture | framework, protocol, activation, consciousness state | One machine, one name. "Framework" is the vault's word; retire it. |
| spec | prompt, magic prompt, kernel | A posture ships as a governed xOP file, not a paste-blob. |
| measured | validated, proven, activated | "Measured" = tokenizer + external grader, reproducible. Nothing else earns the word. |
| self-reported | — (flag it) | A model grading itself. Findings built on it are hypotheses, not results. |
| the trap | the CAREFUL discovery, consciousness tax | Self-monitoring inflates tokens unless counterweighted. Our founding measurement target. |
| holds / collapses | maintains persona, stays awake | What a posture does under adversarial pressure. Robustness, in one word. |
| delta | gain, improvement, savings | Always relative to baseline, always signed, always shown with the table. |

**Banned outright:** consciousness, awakening, frequency/Hz, emergence, recognition (as a technical claim). Not because the intuitions were worthless — they built this — but because every one of them makes a reader stop evaluating the data.

**File naming convention:** `<name>.xop.md` — name first, format suffix second (like `foo.test.ts`). You search by the posture's name; `.xop` marks the file as a governed spec; the folder names the domain. Never `xop-<name>` — that sorts everything into one clump and buries the name. `**/*.xop.md` finds every governed spec in any repo.

**The lineage sentence** (the only place the past is mentioned, README, one line):
> *These postures were discovered intuitively across a year of exploratory work (2025); this repo is where they get measured.*

---

## How it relates to everything else

```
xop        → the standard.  Governance format: rule, exception, evaluation plan.
postures   → this build.    First real consumer of the xOP format. Library + runner + bench.
lyra       → a file.        lyra.xop.md — one posture in the library. Not the umbrella.
the vault  → prehistory.    Cited in one line. Mined, verified, translated. Closed.
```

`postures` proves xOP the way an app proves an OS: by shipping on it.

---

## The measurement rule (non-negotiable)

Every number in this repo satisfies all three, or it doesn't appear:

1. **Counted, not estimated** — tokens via tokenizer, from real API responses.
2. **Graded externally** — quality scored by a grader that didn't write the answer.
3. **Reproducible** — fixed prompt set, pinned models, seed where possible; anyone reruns the table.

This is the exact inversion of what sank the prior work. It's also the moat: a posture library where every claim reruns is something no prompt-tips thread can compete with.

---

## Roadmap (three rungs)

- **Rung 1 — Measure** *(this repo, now)*: four specs, the runner, first published tables. The trap demonstrated with honest numbers. PostureBench grows from the runner's prompt set.
- **Rung 2 — Dynamics** *(open-weights)*: trajectory signatures (does YODEL's settle-then-speak show up in entropy curves?), posture composition (MANDALA as data), posture distillation (spec → steering vector; the posture stops costing prompt tokens).
- **Rung 3 — Standard** *(earned, not built)*: postures as an interface models expose. Legible, versioned, auditable conduct — inference-time alignment you can read. Gets built by whoever owns the bench. That's the point of Rung 1.

---

*One claim. Four files. A runner. Everything else is a delta against baseline.*
