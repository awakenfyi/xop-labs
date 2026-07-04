---
name: basis-thinking
title: "Basis Thinking — Tell · See · Prove · Do"
status: DESIGNED
lab: marketing
kind: skill            # a method, not a single xOP (see "What this is" below)
contains_xop: xop.marketing.benchmark-fit     # "Steal or Invent" — the one real judgment inside
invokes_xops:
  - xop.claim.evidence-bound        # read live, cite the source — observed, not assumed
  - xop.decision.ledger             # don't silently drift the approved positioning
  - xop.comms.audience-fit          # the read serves a named audience
  - xop.design.layout-fit           # module sequence follows the page's job
---

# Basis Thinking — Tell · See · Prove · Do

**BASIS® (Tell · See · Prove · Do)** is Morgan Sage Norman's narrative marketing framework — a method
practiced for decades, here turned into a Skill an AI can run. It reads any website as a sequence of
four module types and produces a **lo-fi, black-and-white read-out**: how a site tells its story, how
competitors do it, where your own site has gaps.

## What this is (honestly)
Basis Thinking is a **Skill** — a production-and-audit method, not a single xOP. By the Admission Test it
is a sequence, not one conditional judgment, so it isn't an xOP on its own. But it **contains one real
xOP** — **Steal or Invent** (`xop.marketing.benchmark-fit`): in the *See* step, adopt a best-in-class
pattern or hold a distinct one. And it **invokes** rules that already exist: read live and cite it
(Claims Need Receipts), don't drift the approved positioning (Decisions Stay Decided), serve a named
audience (Audience & Channel Fit), let the module sequence follow the page's job (Layout Follows the Job).
Naming the parts honestly is what keeps "Basis Thinking" a method instead of a label on everything.

## The four modules
A page is a sequence of these. Most pages run them in order; some repeat or interleave.

- **TELL** — the story and vision. The broad claim, the category, the hero. *"This is what we can do for
  you."* (Hero images, campaigns, the H1.)
- **SEE** — show the product. Features, UI, how it works. *"This is our product."* (Mockups, GIFs,
  product illustration.)
- **PROVE** — the evidence for why you're different. *"Our product delivers results."* (Customer stories,
  ROI, logos, awards, quotes, comparison.)
- **+DO** — the action you want taken. (Sign up, buy, book a demo, talk to sales.) DO can attach to any
  module, not only the end.

Premise from the framework: **most websites already follow this pattern**, which is why any site can be
pressure-tested against it — pick a site, any site, and read its modules.

## What the Skill produces — three stages
Basis runs in order. Each stage has its own artifact; you don't write copy until the brief is set.

**Stage 1 · Audit read-out** — `templates/basis-readout.html` (lo-fi, black and white).
Given a target site and a set of competitors/analogs:

1. **The site, read** — each section classified Tell / See / Prove / Do, quoted, with the date read.
2. **Benchmark** — per module, what competitors and analogs do, what is strong, and which patterns are
   table-stakes versus a wedge.
3. **Your site, audited** — your Tell / See / Prove / Do against the benchmark.
4. **Gaps & opportunities** — where you're thin, where to adopt (Steal), where to hold distinct (Invent),
   each tied to a module and an observed source.

**Stage 2 · Page briefs** — `templates/basis-page-brief.html` (one per page type).
The content strategy *before* copy. Each page type gets a one-page brief: a vertical **module stack**,
top to bottom, where every module declares four things — its **intent** (WHAT / WHY / HOW), a short
**descriptor** (what the module does), the **user questions** it answers, and its **register**
(Aspirational / Educational / Functional). A one-line **strategy statement** sets the page's job. This is
the step the PolyAI deck sits just past — the brief is the skeleton, the copy comes next.

**Stage 3 · Copy** — full draft H1 / sub / body / CTA per module, page by page (the PolyAI deck format).
Only after the briefs are agreed.

## Page briefs — the module stack
Each module band carries three parallel lenses on the same row, so the brief reads in any vocabulary:

| Intent (Golden Circle) | Tell·See·Prove·Do | Register | Typical module |
|---|---|---|---|
| WHY — why it matters | **Tell** | Aspirational | hero / why-it-makes-sense |
| WHAT — what it is | **See** | Educational | product features / overview |
| WHAT + WHY — value of the whole | **See → Prove** | Educational | offerings overview |
| WHY — reasons to believe | **Prove** | Aspirational | validation / who-uses-it |
| HOW — the next action | **+Do** | Functional | CTA (persistent + closing) |

Register is the emotional/functional tone, color-coded on the rail: **Aspirational** (orange),
**Educational** (purple), **Functional** (black) — the only color on an otherwise black-and-white page.

## Page types & standard module stacks
One brief per page type. Standard stacks (adjust per audit):

- **Home / Customer welcome** — WHAT (what is it) · HOW (CTA persistent) · WHAT+WHY (offerings overview) ·
  WHY (reasons to believe) · HOW (what's next). *Job: establish they're in the right place, balance
  emotional appeal with real solutions.*
- **POP — Product Overview** — WHAT (overview) · HOW (CTA persistent) · WHY (value of the services used
  together) · HOW (CTA: demo / upsell / routing). *Job: get the demo request; arm them to share it.*
- **PDP — Product Detail** — WHAT (what it is) · WHAT+WHY (features) · WHY (validation) · HOW (CTA). *Job:
  prove the specific product does the job.*
- **Industry (POP / PDP)** — WHY (why it makes sense) · HOW (CTA persistent) · WHAT+WHY (product features) ·
  WHY (validation) · HOW (CTA: demo / upsell / routing). *Job: connect relevance to the industry first,
  then to businesses of any size.*
- **Pricing** — WHAT (the tiers) · WHY (which is right for me) · WHY (validation) · HOW (CTA: start / talk
  to sales). *Job: let each buyer self-place without gating mid-funnel.*
- **Customer / Resources** — by template; usually WHAT (the story/asset) · WHY (proof) · HOW (next step).

The same five module types rearrange across every page type and across the customer lifecycle.

## Procedure
1. **Define who to audit.** Direct competitors + analogs (adjacent categories with the same job). From
   the framework's own example: competitors *and* analogs both earn a slot.
2. **Read live — observed, not assumed.** Open each page. Quote the actual H1, module, and CTA. Record
   the site and the date. Never assert a pattern you did not read. *(Claims Need Receipts.)*
3. **Classify into Tell / See / Prove / Do.** Mark each section by module and by the page-type template
   it sits in (Home, Product Overview, Product Detail, Industry, Customer, Resources).
4. **Benchmark per module.** For each of Tell / See / Prove / Do: how do they do it, what's strong, is it
   table-stakes or a wedge? Note trends across the set.
5. **Audit your own site** the same way — your modules, same four lenses.
6. **Call the gaps.** For each gap, decide with **Steal or Invent** (`xop.marketing.benchmark-fit`):
   adopt the pattern (cite the source), hold distinct (name the differentiator it protects), or ask.
   Keep the approved positioning intact unless the owner reopens it. *(Decisions Stay Decided.)*
7. **Emit the read-out** (Stage 1) in the template.
8. **Write the page briefs** (Stage 2) — one per page type. For each, set the strategy statement, then
   stack the modules: intent (WHAT/WHY/HOW), descriptor, the user questions answered, and the register
   (Aspirational/Educational/Functional). Use the standard stacks above as the starting point and adjust
   to the gaps the audit found.
9. **Only then, write copy** (Stage 3) — full H1 / sub / body / CTA per module, page by page.

## Audit questions (from the framework)
How do competitors handle Tell, See, Prove, Do — and what do they do better? Which similar, related, or
analog companies should we read? Are there trends? What's the value messaging, the journeys, the entry
and exit points? What does the product do, what problems does it solve, and how do we compare? Where are
the openings?

## Page-type templates the modules fill
Home · Product Overview (POP) · Product Detail (PDP) · Industry Overview/Detail · Customer Overview/Detail
· Resources. Each is a different arrangement of the same four modules across the customer lifecycle.

## Guardrails
- **Observed, not assumed.** Every benchmark line quotes a real, dated read. No invented competitor
  behavior. *(Claims Need Receipts.)*
- **A gap is a gap only if it's real and it matters** — they have it, you don't, and it changes the
  page's job. Don't pad the list. *(Materiality.)*
- **Steal or Invent is a judgment, not a default.** Adopting a rival's wedge or contradicting your
  positioning needs authority, not a copy-paste. *(xop.marketing.benchmark-fit · Decisions Stay Decided.)*
- **Lo-fi means lo-fi.** Black and white, hairline rules, mono labels — a read-out, not a styled deck.
- Status: **DESIGNED.** The embedded xOP hasn't cleared its pilot. The read-out is a working draft to
  audit and edit, not a finished site.

*BASIS® and Tell · See · Prove · Do are Morgan Sage Norman's framework.*
