# BRAND-STORM — the landscape study

**Before you pick a stance, map the stances already taken.** A brand-storm studies 5–7 companies in a space and answers, per company, per channel: how do they **Tell** (the claim), **Show** (how they let you see the product), **Prove** (the receipts), and **Ask** (what they want people to do)? The output is a stance map with white space marked — the input every `/directions` round deserves and almost never gets.

Extends [web-copy-xop](../web-copy-xop/)'s Tell · See · Prove formula with the fourth beat (**Ask** — the CTA architecture) and runs it across three channels instead of one page.

## The study, per company

One file per company. Every cell kind-labeled per [tracking](../tracking/tracking.xop.md); every quote verbatim with URL + date (anchor) — paraphrase is where study-slop begins.

| | **Web** | **Social** | **Press/PR** |
|---|---|---|---|
| **TELL** | The one-sentence claim above the fold; the story underneath (kind: story) | The claim compressed to feed-length; the recurring themes | The headline they pitch; the founder narrative |
| **SHOW** | How the product is *seen*: live demo, screenshot, video, abstraction? How many seconds to first sight of the real thing? | Product-in-use vs. brand-wallpaper ratio | Do journalists get assets or adjectives? |
| **PROVE** | Receipts: logos, numbers, benchmarks, testimonials — each labeled (anchor / consensus / story) | Social proof mechanics: whose voices, what evidence class | Third-party validation vs. self-claims laundered through coverage |
| **ASK** | CTA architecture: primary verb, friction level, what happens in the first 30 seconds after the click | What each post asks (follow / try / share / believe) | The ask behind the story (fund / adopt / hire / regulate) |

Plus per company: **stance fingerprint** (type, color system, graphic structure — the visual posture in three lines) and **the gap** — where their Tell outruns their Prove (overhang, the brand version).

## The synthesis (the part worth money)

- **The stance map:** all 5–7 fingerprints on one page. Which stances are crowded, which are empty.
- **The white space:** unclaimed stances *that the audience evidence supports* — white space with no audience is just empty for a reason.
- **The proof ceiling:** the strongest evidence class anyone in the space actually shows. If everyone proves with logos, the first mover to prove with live numbers owns the beat.
- **The ask conventions:** what every CTA in the space asks, and the untried verb.
- Everything labeled: the map is consensus + anchor quotes; the white-space call is story until a `/directions` round tests it.

## How it runs (the storm harness)

5–7 company agents in parallel (one per company: fetch web/social/press, fill the grid, verbatim quotes only) → one synthesis agent (stance map + white space) → one skeptic (attacks the white-space claim: *is it empty because nobody wants it?*). Same engine as every storm in this lab; ~9 agents, bounded.

## Where studies live

```
in-the-wild/brand-studies/<space>/
├── README.md            the synthesis: stance map, white space, proof ceiling
├── <company-1>.md       the grid, kind-labeled, quotes dated
├── …
└── methodology.md       corpus dates, channels sampled, what was NOT looked at
```

`in-the-wild/` is the field-evidence wing of this repo (the hold-release studies set the pattern: studies + methodology + templates). Brand-storms are field evidence — they describe what *is*, before the kit decides what *ought*.

## Placement note (the map of the whole)

- **design-kit/** (here) — the forge: laws, commands, storm specs. Where rules get made and attacked.
- **packs/design-os/** — the work pack: the shippable bundle (xOPs + guards + skills + boundary). Kit pieces graduate into the pack as they mature past DESIGNED.
- **in-the-wild/brand-studies/** — the field evidence: brand-storm outputs, one space per folder.

Forge → pack → field. Nothing skips a step.
