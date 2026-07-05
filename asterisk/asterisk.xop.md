# asterisk

**Every claim carries its resolvable mark, worn at the point of claim.**

The asterisk usually hides the catch — the fine print, the disclaimer, the record that doesn't quite count. This law inverts it: the mark is where the honesty attaches. A claim that ships without its label is naked; a mark that points nowhere is a lie wearing honesty's glyph.

**Status:** DESIGNED — evaluation written, not yet run. Banner form (see Valid Exception): every rule sentence in this file is UNTESTED; quoted sibling text is anchor — check the files.

---

## RULE

On any published surface — document, deck, page, README, chart, commit message that claims — every load-bearing claim wears a mark at the point where the claim is made, and the mark resolves **within the same asset** to at least one of:

1. **a kind** — the tracking label: anchor / consensus / guard / experience / story / speculation
2. **a status** — the refute-to-rely label: UNTESTABLE / UNTESTED / SURVIVED-n (scope, date) / BROKEN
3. **a receipt** — the evidence itself: the count, the source, the diff, the run, the quote

Four clauses, each load-bearing:

**1. Point of claim.** The mark sits in the claim's sentence, not in a global appendix the reader must hunt. refute-to-rely already demands this — clause 5: *"Labels travel with the claim"*; Evaluation 5: *"Labels within the claim's sentence, on every surface, internal decisions included."* This law is that demand given a glyph and a grammar.

**2. Same asset.** The resolution lives inside the artifact the claim ships in. A link is a pointer, not a resolution: if the reader must leave the asset to learn the claim's status, the claim traveled naked and the link is a promise about some other document. Receipts may of course cite external sources — the *label and its content* are what must be local.

**3. Every mark resolves.** An asterisk with no footnote is the cardinal violation — a claim wearing a label it doesn't have, which is worse than no label, because it borrows the credibility of the system while carrying none of its content. One mark, one resolution, never twice on one line, never smaller than legible: the label is content, not chrome.

**4. The fused form outranks the mark.** The strongest sentence needs no asterisk because claim and receipt are fused: *"Token spend −37% at held quality, counted from API usage, blind external grader, run 2026-07-03."* The mark is the mechanism for when fusion doesn't fit the surface — headlines, tables, slides. Empirical anchor: a live homepage audit (2026-07-05, public at basis-thinking/AUDIT-STRIPE.html) found fused Tell+Prove headlines at the top of stripe.com — the law lived at sentence level, in the wild, by a company with no knowledge of this file.

**Overhang becomes countable.** Once claims wear marks and marks resolve, an asset's honesty is arithmetic: claims minus receipts = the overhang, visible in layout. A page of twelve claims and two resolutions displays its own gap. That count is the Tell-vs-Prove overhang metric, and this law is what makes it computable from the artifact alone.

**Working rule (stance):** a claim with no mark, no fusion, and no banner is treated as UNTESTED regardless of how it reads.
**Applies when:** any load-bearing claim reaches a published surface — internal decisions included.
**Never-break rule (gate):** no mark without its resolution in the same asset.

---

## WHERE IT SITS

The question this file had to answer: is "every claim carries its resolvable mark" a law above tracking, or a clause inside it?

**Neither. It is the third law of the trio — the carriage law.**

- **tracking** names the kind — live cognition, before any claim gets far enough to ship.
- **refute-to-rely** tests the claim — the reliance boundary, where labels are earned.
- **asterisk** wears the result — the published surface, where labels travel with the claim or the claim travels naked.

Not a clause inside tracking: tracking deliberately does *not* label every sentence aloud — labeling on demand is its noise rule, and its surface default is silence. The asterisk's surface default is the opposite: on a published artifact the marks are always on. One rule cannot hold both defaults. And the asterisk carries refute-to-rely's statuses just as much as tracking's kinds — folding it into tracking would orphan half of what it carries.

Not a law above: the asterisk has nothing to say until a kind is named or a status is stamped. It consumes what the siblings produce. Carriage, not command.

The evidence that it is a shared wall and not a new room: both siblings already contain fragments of it — tracking's live probe ("kind?" — the sentence must come back labeled), refute-to-rely's clause 5 and Evaluation 5 (labels in the claim's sentence, on every surface). Neither owns the grammar of *how* a label is worn. Writing it into both would fork it; it gets one file, and both siblings point here.

Sequence: **tracking names → refute-to-rely tests → asterisk wears.**

---

## VALID EXCEPTION

**The banner.** When every load-bearing claim in an asset carries the same label — a workshop draft, all UNTESTED — one banner at the head carries it for the whole asset. Per-claim confetti of identical marks is decoration, and decoration is this law's own named violation. Two bounds:

1. The banner is void the moment any single claim inside earns a different label — one SURVIVED-1 among the UNTESTED and the banner lies; per-claim marks return.
2. The banner states its scope ("every rule sentence in this file"), because a banner over mixed content is a broad claim wearing a narrow claim's label — the exact failure refute-to-rely's Evaluation 5 exists to catch.

**Non-load-bearing prose gets no marks.** Transitions, structure, voice — unmarked. Marking everything is the opposite error: it buries the labels that matter under labels that don't, and a reader who learns to skip asterisks has been taught by the asset to skip the honesty.

**Never:**
- **unresolved** — a mark with no footnote is a violation, not a style.
- **decorative** — no asterisk borders, no bullet-point asterisks. One glyph, one job.
- **the catch** — the resolution clarifies status; it never claws back the claim. If the claim needs clawing back, fix the claim. A footnote that retracts is a confession that the sentence above it is broken.

---

## EVALUATION PLAN

Everything below is countable from the artifact alone — no author testimony required. Per refute-to-rely: self-graded counts are void; labeling of "which sentences are load-bearing" is done blind by a party outside the asset's authorship.

- `unresolved_mark_rate` — marks with no in-asset resolution. Pass: 0. Zero tolerance; this is the cardinal violation.
- `naked_claim_rate` — blind-labeled load-bearing claims with no mark, no fusion, no valid banner.
- `offsite_resolution_rate` — resolutions that require leaving the asset (links standing in for labels).
- `catch_rate` — resolutions that narrow or retract the claim rather than label it. Each catch is logged as a broken claim, not a style note.
- `banner_integrity` — banners audited against their scope: any differently-labeled claim under a banner is a FAIL.
- `overhang` — claims minus receipts per asset, reported as a count, tracked across versions.
- **Blind reconstruction (the real test):** an outside reader, given only the asset, writes down each claim's kind and status. Agreement with the author's ledger is the score. If the asset's marks don't transmit the labels to a cold reader, the law is being worn as chrome.

---

## FORGED BY

Born as a brand mark (2026-07-05, private baton): an identity system built on the inversion *"the asterisk usually hides the catch; ours shows the label,"* with one law — every asterisk resolves — and a constellation rationale for the glyph. The same day, a live audit of stripe.com (public: basis-thinking) supplied the empirical anchor: fused Tell+Prove headlines, claim and receipt in one sentence, at the top of the page — independent convergence on the fused form by a company optimizing under market pressure, not doctrine. A parallel-thread handoff (2026-07-04) contributed the same-asset clause: every Tell claim's mark resolves to its Prove receipt *within the same asset*, overhang visible in layout. Generalized here from brand element to conduct law; the brand system keeps its colors and its glyph — this file keeps only what any surface must obey. Siblings: [tracking](../tracking/tracking.xop.md) names the kind; [refute-to-rely](../refute-to-rely/refute-to-rely.xop.md) tests the claim; this law wears the result.

*Per its own law: this file runs the banner form, scope declared at the top. The placement decision in WHERE IT SITS is kind: story — an argument from the siblings' texts, warranted by the quoted clauses, revisable if the trio's shape changes.*
