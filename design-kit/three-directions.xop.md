# three-directions

**Never present one answer to a perspectival question. Present three named stances rendering the same content — then pass the winner as a baton, sealed with a handshake.**

Child of [name-the-stance](name-the-stance.xop.md). This xOP governs the *directions round* — the moment taste enters a project — and the *handoff* — the moment taste leaves one pair of hands for another (human→human, human→AI, AI→AI).

Codified from the professional agency Round-1 practice (studied from real brand builds, privately) and the show-don't-tell preview mechanic proven in slide tooling. **Status: DESIGNED.**

---

## RULE

### Part I — The round (three directions)

**1. Three, not one, not five.** One direction is a default wearing a presentation. Two is a false binary. Five is a menu that outsources the thinking. Three named stances is the smallest set that proves the space was explored and the largest a chooser can genuinely hold. *(kind: consensus — agency practice across decades; revisable.)*

**2. Each direction is a complete stance, small.** The anatomy:
- **A name and a number** — D1/D2/D3, plus a real name (a direction with no name is a mood, not a stance)
- **One sentence of stance** — what this direction believes
- **Type pairing** — headline + body, named faces
- **Color system with tint scale** — named colors, each at 100/50/25% — the scale *is* part of the system
- **Graphic structure** — the layout grammar: grids, badges, devices
- **Its own limits** — balance proportions, approved variations, incorrect usage. A direction that can't say what it *isn't* isn't a direction.

**3. The control copy is sacred.** All three directions render **the same test content** — one line, chosen once, in-voice, before any direction exists. Constant content × varied stance = a controlled comparison; vary both and the round is theater. Pick a stress string: numbers, symbols, an ampersand, attitude — e.g. *"Table for 2 @ 9? We ordered the whole left side & zero regrets."* — so the stance has to survive punctuation, digits, and tone at once. *(This is the postures-runner mechanic in agency form: fixed prompt set, varied stance, comparable outputs.)*

**4. Lofi before hifi, per direction.** Each direction is shown as structure first — greyscale, hierarchy-from-value (the lofi-kit pass) — then as full expression. A chooser who sees hifi first chooses the color, not the stance. The ladder: **strategy sentence → lofi structure → hifi expression → min-to-max range.**

**5. The choice is an experience-report, logged as one.** "We pick D2" is taste — sovereign, kind: experience/consensus, never dressed as measurement. What gets logged: who chose, against which brief, what each direction's strongest render was, and *why* in one sentence per rejected direction. Rejected directions are archived, not deleted — they are the round's graveyard, and a round with no graveyard never had three real directions.

### Part II — The baton (the handoff)

**6. Taste travels as a baton: a package another system can run without you.** When a direction wins, it is codified into a machine-and-human-consumable kit:

```
baton/
├── STANCE.md          the one-sentence belief + the story (kind: story, labeled)
├── tokens.json        colors + tints, type pairing, spacing scale, radii  (kind: anchor)
├── limits.md          balance proportions, approved variations, incorrect usage,
│                      minimum sizes, clear space — the DON'TS, each with its
│                      two-direction test                                   (kind: guard)
├── control-copy.md    the sacred test content + its reference renders     (the calibration set)
├── prompts.md         system prompts for AI renderers: how to hold the stance,
│                      how to know the limits, when to HOLD and ask
└── range.md           min-to-max expression per artifact class            (the dial)
```

`prompts.md` is what "how it knows the limits" means operationally: any downstream system — a coding agent, an image model, a deck skill — receives the stance as conduct (*hold this; these are your walls; here is what out-of-bounds looks like; when uncertain, HOLD and show the nearest in-bounds option*), never as vibes.

**7. No handoff without a handshake.** A baton *sent* is not a baton *received*. The handshake: the receiver — human or AI — **renders the control copy in the stance, cold, from the baton alone.** The sender compares against the reference renders and returns one of: **GRIP** (handoff complete — receiver holds the stance), **SLIP** (close; named corrections, one more render), or **DROP** (the baton is incomplete — fix the *baton*, not the receiver; a stance that can't survive transfer was never codified, only felt). The handshake result is logged with the baton. *(This is refute-to-rely applied to taste transfer: reproduction is the only proof a handoff happened. Same law, warmer room.)*

## VALID EXCEPTION

**The follow-on.** Inside an already-GRIP'd stance, new artifacts don't re-run the round — the baton governs. The round re-opens only when the *brief* changes class (new audience, new register, rebrand) — and a client who asks for "just one quick direction" gets the round anyway at lofi depth: three greyscale structures cost hours, not weeks, and choosing among three is faster than round-tripping one.

## EVALUATION PLAN

- **Round integrity:** three directions materially distinct? Test: swap the control copy between any two directions' renders — if the result is plausible, they were one direction twice. `distinctness` judged by a grader outside the round.
- **Handshake validity:** does GRIP predict downstream conformance? Track guard-violation rate of post-GRIP artifacts vs. post-SLIP-forced ones. If GRIP doesn't predict, the handshake is theater — revise what the baton carries.
- **Baton completeness (machine):** an AI receiver given only the baton renders the control copy; deterministic checks (tokens conformance, limit violations) score it. A baton no AI can run is documentation, not a baton.
- **Opposite error:** rounds where three directions were secretly one taste in three costumes — measured by the swap test above; and follow-ons wrongly forced through new rounds (`round_churn`).

---

*Lineage: the agency Round-1 tradition (studied from real brand builds, kept private) · show-don't-tell preview tooling · the postures lab (fixed content × varied stance = the measurement) · the vault's handoff letters (a stance that survives transfer, written down — finally with a harness). This file wears DESIGNED.*
