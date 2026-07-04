# COMMANDS — how the kit runs

The kit is a command grammar, not a manual. One project, start to finish:

```
/brand-storm <space>        study the landscape: 5–7 companies, how they
                            Tell · Show · Prove · Ask across web/social/press
                            → in-the-wild/brand-studies/<space>/

/brief                      the intent gate: audience, job, tone, one reference,
                            one constraint, expression range. Waivers logged.

/directions                 the R1 round: THREE named stances, each rendering
                            the sacred control copy — LOFI ONLY at this stage.
                            Chooser picks; choice logged as taste; graveyard kept.

/baton                      codify the winner: STANCE.md · tokens.json · limits.md
                            · control-copy.md · prompts.md · range.md

/shake                      the handshake: receiver (human or AI) renders the
                            control copy COLD from the baton alone.
                            → GRIP  (handoff complete — hifi unlocks)
                            → SLIP  (named corrections, one more render)
                            → DROP  (fix the baton, not the receiver)

/hifi                       full expression — GATED: no GRIP, no hifi.
                            Runs inside the baton's limits; every artifact
                            carries its min-to-max position.

/track                      anytime: "kind?" — label any design judgment
                            (anchor / consensus / guard / experience / story)
```

**The gate that makes it a system: you shake to hifi.** Lofi is free — sketch, explore, three directions, all greyscale, all cheap. Hifi is earned — it exists only downstream of a GRIP, which means the stance survived a cold transfer first. No baton, no shake, no GRIP → any hifi output is, by definition, an unnamed default doing the work. That single gate is [name-the-stance](name-the-stance.xop.md) enforced at the command line.

```
lofi ──── free territory ────┐
                             ├─ /shake ─→ GRIP ─→ hifi
baton ─── the package ───────┘        ↘ SLIP → retry
                                       ↘ DROP → fix the baton
```

Skills to build, in order: `/brand-storm` (the storm harness exists — see [BRAND-STORM.md](BRAND-STORM.md)), `/directions`, `/shake`. `/lofi` already ships (xop-lofi · lofi-kit · web-to-lofi). `/track` already ships.
