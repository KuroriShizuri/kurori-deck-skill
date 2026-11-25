---
name: kurori-deck-skill
version: 2.0.0
description: |
  Build a business proposal deck backed by data analysis, the way the worked example decks were built: pick the method with the router, draft in Indonesian first, run humanizer
  passes, verify numbers against the executed notebook, write one HTML file per
  slide, and render the PDF with a repeatable pipeline. Sweet spot 15 slides;
  every number is cited on the slide where it appears. Includes a
  case-competition mode for decks judged cold, without a presenter.
license: MIT
compatibility: claude-code codex muse opencode
---

# Kurori Deck Skill

Build a short business proposal deck from a data analysis, with a source for
every number. This skill records the method used for the worked example decks:
the Company A telecom churn deck (November 2026, 15 slides, English, built
from an Indonesian draft) and the MieLestari case-competition deck (November
2026, 43 slides, Indonesian, scored 9 for win-worthiness by an external
reviewer). Every number was checked against the executed analysis and cited
on the slide where it appears. The finished packages were delivered to their
author. The deck PDFs themselves are not included here. This skill includes
the method, the rules, the toolchain, and the deck texts as worked examples
(`examples/`, `references/worked-example.md`,
`references/case-competition-mode.md`).

## What changed in v2.0.0

Version 1 recorded one fixed workflow for one assignment. Version 2 adds
what three test programs proved after v1 shipped:

- **Method router.** Nine methods (4 flows, 5 supporting layers), ranked
  per brief on five dimensions, with a walk-down when the user rejects the
  top pick. See "Method router".
- **Slide budget as a sweet spot.** 15 is the target, not a hard floor and
  not a universal cap. The cap of 15 applies only when the assignment
  limits it. Case-competition main decks run 10-12 slides plus an appendix
  that is not counted. See "Slide budget".
- **Palette library.** 51 named palettes in `references/palette-library.md`
  with a visual picker (`references/palette-picker-2026-11-24.html`). The
  agent reasons about the palette from data, audience, and context, then
  proposes 3-4 options with one line of reasoning each. The user locks one
  in. See "Palette".
- **15-step workflow with a Frozen Spec.** The brief converges first
  (step 7 gate), the decisions freeze into a Frozen Spec (step 10), the
  build follows, and the validate-refine loop has a stop rule. The
  humanizer passes are a checklist item in step 11, not a memory. See
  "Workflow".
- **Case-Competition Mode.** A two-layer mode for decks judged cold,
  without a presenter: a 10-12 slide narrative main deck plus a dense
  appendix, one analysis per slide. Full spec in
  `references/case-competition-mode.md`.
- **Design rules.** 19 empirical visual rules from the Company A test
  (rules 1-14), the "10 Niche Design Hacks" reel (rules 15-18), and
  the MieLestari test (rule 19), including the symmetry rule. See
  "Design rules".
- **Verification discipline.** Canonical numbers file as the single source
  of truth, one checker per version, and rendered pages read by eye, not
  only by an overflow check. See "Verification discipline".

The v1 method is kept intact inside the v2 workflow: the ten hard rules
still apply (rule 1 revised as above), the Indonesian-first draft with two
humanizer passes is still the language pipeline, and the number checker
still has to report zero problems before the build. Nothing in v1 was
deleted; v2 adds choice and a second mode around it. The full record is
in `CHANGELOG.md`.

## When to use

Use this skill when the user asks for a presentation deck that must defend
a business proposal with data: a course final assignment, a churn or
retention proposal, a pitch deck, a case-competition entry, or any
executive deck where a model supports a recommendation. It fits when the
deck must stay tight, every number must carry its source, and the text
must not read like generic AI output.

When the deck will be judged cold, without a presenter (a business case,
case competition, or any deck handed in as a document), use
Case-Competition Mode. When the user names a pitch deck, the router picks
H-P-S-I-T-C first.

## When not to use

Do not use it for a free-form creative deck, a lecture slide set, or a deck
with no data behind it. The verification steps assume there is an analysis
notebook (or equivalent) that produces the numbers on the slides. If there is no notebook or equivalent analysis output, the number steps do
not apply. Skip the notebook checks in the workflow, run the remaining
steps, and say plainly that the numbers were not verified against an executed
analysis.

## Hard rules

These rules are never broken. The original deck passed its build and number
checks because it followed them, and the MieLestari deck kept its score of
9 because it followed them too.

1. **Slide budget follows the assignment; 15 is the sweet spot, not a
   hard floor.** Confirm the real limit for each new assignment (Workflow
   step 1). When the assignment caps the deck at 15 slides, 15 is a hard
   cap and every slide counts, including title and references. When the
   assignment sets no cap, target 15 and let the agent decide more or
   fewer from the findings; the "so what?" gate and one-slide-one-message
   bound the growth, not a number. In Case-Competition Mode the main deck
   runs 10-12 slides and the appendix is not counted.
2. **At least one ML or statistical model, with its name, its evaluation
   metric, and its score written explicitly in slide text.** A chart alone
   does not count. Compare several models when you can.
3. **Direct quotation stays below 40% of the deck text, as a guide.** Write the
   argument in your own sentences.
4. **Every number on a slide carries its source on the same slide.** Add a
   footnote (at least 13 px) with organization, document title, and date. No
   number without a source, no exceptions.
5. **Use market data only after its source is proven openable and
   searchable.** Open the page yourself and find the figure on it before the
   number enters any slide. If you cannot open the source, do not use the
   figure.
6. **Model scores must match the executed notebook.** The notebook as
   executed and submitted is the authority, not a local run and not the
   tutorial text. See `references/number-verification.md`.
7. **AI chat history is never published.** If the assignment asks for AI use
   disclosure, cite the session URL only. Never attach or paste a transcript.
   The worked examples cite Kiro session URLs, which are login-gated and do not
   make the transcript public.
8. **No em-dash and no en-dash in slide text, no emoji, no AI-style
   wording.** The checker rejects both dashes everywhere, so write number
   ranges such as 270-300 with a plain hyphen. Banned words: delve,
   furthermore, moreover, leverage, leveraging, cutting-edge, robust,
   seamless, pivotal, utilize, and gradient. Model names are exempt from the
   word ban: the ban covers wording, not the name of a model such as Gradient
   Boosting. Do not use a spaced hyphen as a dash. See
   `references/humanizer-rules.md`.
9. **Numbers are never invented, rounded into a new claim, or copied from
   memory.** If a number is not in the verified sheet (the `SHEET` in
   `check_numbers_final.py`, see Workflow step 12), it does not go on a slide. In
   drafts, write TBD or drop the claim instead of guessing. No TBD may remain
   in the submitted deck.
10. **The last slide is the full reference list with URLs.** The same list
    goes into the submission platform's References field, unchanged.

## Method router

Do not pick a method by habit. Route it per brief.

### Mechanism

1. **User gives no method prompt.** The agent reasons from context,
   purpose, and data, ranks all nine methods, shows the ranked list with
   one line of reasoning per method, and builds on #1.
2. **User gives a method.** Follow it, and say in the brief why another
   method could work better. Advice only, unless the method clashes with
   a hard bound (slide budget, deck purpose, or a skill rule); then mark
   it as a CONFLICT and ask before building.
3. **Walk-down.** The user rejects #1, the agent moves to #2, then #3,
   until the list runs out. When it runs out, listen again: what does the
   user want, from a reference or from imagination.

### The five ranking dimensions

Rank on these five dimensions only. Do not add a sixth. Past user
preference is not a separate dimension; record it as supporting evidence
under dimension 1 (fit to purpose) and dimension 5 (fit to style). A
separate dimension would double-count and lock in habits, and the user
may want a different flow for a different deck type.

1. **Fit to purpose.** Inform, persuade, decide, or report.
2. **Fit to audience.** Executives want the conclusion first; investors
   want a story; academics want the method first.
3. **Data availability.** A data-story flow needs model results;
   H-P-S-I-T-C needs a clear problem and solution.
4. **Slide budget.** Sweet spot 15; H-P-S-I-T-C runs long, SCR runs
   short.
5. **Fit to style.** Professional by default; pitch only when the user
   says pitch.

### The pool: nine methods

Four flows can structure a whole deck. Five supporting layers are always
on, in priority order, and are not walk-down alternatives.

**Flows:**

1. **Pyramid.** Conclusion first, held up by a tiered tree of arguments.
2. **H-P-S-I-T-C.** A full pitch flow: Hook, Problem, Solution, Impact,
   Traction, Call to action.
3. **SCR.** Situation, Complication, Resolution; a short problem-based
   flow. SCR also nests inside H-P-S-I-T-C: the Problem phase of an
   H-P-S-I-T-C template follows SCR structure. The pool lists SCR once;
   the H-P-S-I-T-C template refers to it.
4. **Data-story.** Problem, Data, Model, Results, Recommendation. The
   flow of the user's own Company A deck; proven to work in their hands.

**Supporting layers (always on):**

5. **BLUF.** Conclusion first at every level; slide titles are
   conclusion sentences. This is already hard rule 8's title practice in
   v1. BLUF is a principle that is always on; Pyramid is a flow. Both
   live, at different levels.
6. **One slide one message.** One slide, one message.
7. **Data Slide Formula.** A data-slide template: finding, so what,
   evidence. Applies only to slides whose main point is one data finding
   (in the Company A test: slides 5, 6, 7, 8). Hook, problem definition,
   process, and decision slides use other structures.
8. **The "so what?" test.** A gate per slide; a slide with no answer is
   cut or merged. The skill judges it while building; the user confirms
   it at the HTML preview.
9. **Storyboard.** One line per slide (message plus visual) before any
   slide is built; sits in the research step.

### Candidate order per deck type

These orders are priors. The router still re-ranks per case; the order
below is only the starting point, never a verdict.

- **Professional / data: Data-story > SCR > Pyramid > H-P-S-I-T-C.**
  Proven by the Company A test: Data-story #1, SCR #2, Pyramid #3,
  H-P-S-I-T-C #4. H-P-S-I-T-C last because a pitch flow does not fit a
  data and decision deck.
- **Pitch: H-P-S-I-T-C > Pyramid > Data-story > SCR.** Confirmed by the
  KopiRumah pitch test (24 Nov 2026): H-P-S-I-T-C #1, SCR nested in the
  Problem slide works.
- **Case competition (business case, judged as a document): Pyramid >
  SCR > Data-story > H-P-S-I-T-C.** Prior with supporting evidence: the
  MieLestari test deck used Pyramid first and scored 9 for
  win-worthiness. The methods were not ranked against each other in
  that test, so the order stays a prior, not a confirmed ranking. Full
  mode in `references/case-competition-mode.md`.
- **Academic: Data-story > Pyramid > SCR > H-P-S-I-T-C.** Evidence: the
  user's own Company A deck uses Data-story (Problem, Data, Model,
  Results, Recommendation) and worked; Pyramid second because each
  section opens with a conclusion.

### Rules when the user gives a method

- **Explicit** ("use Pyramid"): follow it; advice is advisory, the
  requested method wins unless the user moves.
- **Implicit** ("make a pitch deck", which implies H-P-S-I-T-C): count
  it as given but weak; follow it, and advise.
- **Hard conflict vs soft advice.** When the requested method clashes
  with a hard bound (slide budget, deck purpose, or a skill rule), mark
  it as a CONFLICT and ask before building. Do not just advise.
- **Method outside the pool, or unknown:** ask for a short definition,
  or treat the input as a reference or imagination (the "list ran out"
  path). Never pretend to understand it.

### Walk-down mechanics

- Rank the list ONCE per brief; rejections move down in order.
- Moving #1 to #2 means the brief is re-derived (storyboard and slide
  order change with the flow), not just a label swap.
- When the user changes the brief (new data, audience, or purpose),
  rank again from zero.
- When the list runs out, take the reference or imagination path (a
  reference deck or image leads to a research step).

### Two modes: general and focused

- **General mode:** the router picks the method, as above.
- **Focused mode:** the user gives the method. The flow is the same, but
  the first thinking step uses the given method (follow it and advise)
  instead of the router.

## Slide budget

The agent estimates the slide count and offers it in the brief, before
building.

- **Structural slides:** about 5 (title, problem and context, method,
  recommendation, references).
- **Finding slides:** one slide per key finding or interpretation from
  the data (one chart plus "so what" per slide); a complex, multi-facet
  finding gets 2 slides.
- **Sweet spot 15.** Target 15 slides. More or fewer is the agent's call
  from what the deck needs (a pitch deck of 10-12 slides is normal) when
  the user asks for no specific number. When the user asks for a number,
  follow it. There is no hard floor of 15 any more. Growth is bounded by
  the "so what?" gate and one-slide-one-message, not by a number.
- **Cap 15 only when the assignment limits it.** In the Company A
  assignment the grader ignores slides past the limit, so an extra slide
  counts as missing. Confirm the limit and its consequence for each new
  assignment (Workflow step 1).
- **Case-Competition Mode:** main deck 10-12 slides; appendix slides are
  not counted toward the budget.

The Company A test proved the estimate: 15 slides estimated, 15 built.

## Palette

Never ask the user "what palette" as bare text. Never use one palette
for every deck.

1. **The library is the source.** `references/palette-library.md` holds
   51 named palettes: 22 from reference reels, 13 draft combinations
   that passed an external review, 16 added by that review. Contrast
   ratios were checked with the WCAG formula. A palette already used in
   one deck is recorded so the next deck does not repeat it by accident.
2. **The agent reasons first.** Reason about the palette from the data,
   the audience, and the deck context (a serious data or finance deck
   takes a calm professional palette; a pitch or investor deck takes a
   bold pitch palette; an academic deck takes a calm academic palette),
   then propose 3-4 options that fit, with one line of reasoning per
   option.
3. **Always visual.** Every palette proposal comes with the visual
   picker (`references/palette-picker-2026-11-24.html`, one file with
   all 51 palettes: name, colors, fit label). Never ask about a palette
   in text alone.
4. **The user locks one in.** The user's lock wins. When the user answers
   "bebas" or does not choose, the agent uses its own #1 option and
   records that in the brief.
5. **Only verified hex becomes a build token.** Hex values marked with ~
   in the picker are preview estimates, not build tokens. Verify a hex
   from a full-resolution frame before it becomes a token. The default
   tokens in "Design tokens" below are only the fallback when the user
   picks nothing and there is no reference.
6. **The library is alive.** Each new reference from the user is added
   as a named palette. Full automatic palette extraction from a
   reference image is NOT adopted yet (see "Still not adopted"); the
   proven mechanism is "show 3-4 options from the library, user locks
   one in".

## Workflow

Fifteen steps. Converge first (an agreed plan), then build, then refine.
The user gate sits where it belongs. The full flowchart is in
`references/alur-kerja-v2-flowchart-2026-11-24.html` (and
`.pdf`).

### Step 1. Prompt

The user gives the prompt: the deck request, material, data, references
(a reference deck or image). The brief for a test deck MUST include the
reference list: a brief without it makes the agent report false "gaps".

### Step 2. Agent reads material and prompt

Research step: read the material, verify sources (they must be openable
and findable), extract the palette from a reference image. Output:
verified sources, palette, first mapping. Read the assignment README and
tutorial files directly from disk. Do not rely on a browser summary or a
chat answer about the format. The worked example showed why: an early
browser report invented a 16:9 requirement, a white background, a group
presentation, and a Google Classroom deadline. None of these were in the
official documents. (The final deck still uses a 16:9 canvas and a white
background, as design choices, not as requirements.) For a new
assignment, confirm its real rules before writing anything, including the
slide budget and what happens past the limit. Record them in a new rules
file formatted like `references/deck-rules.md`, and do this before the
build starts.

### Step 3. Agent thinking

Router: rank the 9 methods on the 5 dimensions, estimate the slide count
(structural about 5 plus 1 per key finding; sweet spot 15), and draft a
storyboard (one line per slide: message plus visual).

### Step 4. Prototyping, the plan

Assemble the plan prototype, which is the brief: method #1 with its
reason, slide estimate, storyboard, palette, density. Two prototypes
exist in this workflow and they are different kinds: #1 is a plan
prototype (this brief); #2 is a deck prototype (the HTML preview in
step 9).

### Step 5. Ask the user what the agent needs

The agent asks 3-5 taste questions: what is still unclear from the
material or prompt. One of the standard questions, asked with the taste
questions: "may the agent search the internet for images and assets?"
Record the answer in the brief (step 6-7) and freeze it in the Frozen
Spec (step 10), so the build (step 11) does not have to ask again.
When the user answers "only my material" and the material has no usable
image, mark that as a GAP in the brief; do not silently build an empty
deck. Default when the user does not answer: ALLOWED, but only from the
verified free-license source list, never AI-generated images (the user
prefers real photos, not AI images). The brief always shows the asset
plan, so the user can veto it at the step 7 gate. Every image and asset
carries its source (on the slide or in the references); use only sources
proven openable and findable.

### Step 6. Agent thinking

Work through the user's answers, revise the brief.

### Step 7. Ask confirmation, or give a recommendation (GATE)

The agent asks for confirmation of the brief, or gives a
recommendation; the user agrees or changes it. Ask for ALL missing
details at once, in one confirmation message (about what, for whom,
purpose, missing data), not one question at a time, so the user handles
everything in one answer. **Confirm even when the material looks
complete:** always show a consolidated confirmation before building,
with what the agent understood from the material (about what, for whom,
purpose) plus the 3-4 palette options with the visual picker, so the
user can correct and lock everything in one answer. This is the brief
approval gate. No build before the brief and the palette are confirmed.
When the user answers "bebas" or "lanjut", the agent uses its own
reasoning and records that in the brief. In Case-Competition Mode the
confirmation covers the scope of the main deck and the appendix both.

### Step 8. LOOP: thinking and user feedback

Repeat steps 6-7 until the brief converges. Output: final brief.

### Step 9. Prototyping, the deck

Build the full HTML deck preview. The preview is the iteration gate:
the user reviews the whole deck in the browser before anything is
rendered to PDF.

### Step 10. Get condition: the Frozen Spec

Collect every agreed decision (method, slide count, palette, content,
asset permission, density) as the final specification before the build.
Write it down as a checklist. Once frozen, the build follows it; a
change after freezing reopens step 7, it does not silently edit the
build. The humanizer checklist (step 11) is an item in the Frozen Spec.

### Step 11. Take action: build

Build: one HTML file per slide, plus charts. Write the text in
Indonesian first, then run the language pipeline as a CHECKLIST, in this
order: Indonesian text, `humanizer-indonesia` pass, translate to
English, `academic-humanizer` pass on the English prose only. This step
is easy to skip by accident; it is a checklist item in the Frozen Spec,
not a memory. Then assemble. See "Language pipeline" below and
`references/humanizer-rules.md`.

### Step 12. Agent validation: data and looks

Validate the data (numbers match the notebook or source) and the looks
(design tokens, layout, no overflow). Output: a findings list. Two
validation lessons, both from real builds:

- **Validate files from the agent that was tested.** A long code block
  transcribed from a page view can mix in draft lines (a folded Thought
  block). Ask for a re-send in chunks. The agent's own correction about
  its file is authoritative. Visual verification is mandatory before
  claiming done.
- **Read the rendered pages, not only the overflow check.** An overflow
  check that only flags elements crossing the slide edge misses content
  clipped by an inner bar. In the MieLestari build, slide S2 of v9 was
  clipped 16 px by the insight bar and passed a 113/113 check. Read the
  rendered pages, above all the slides whose content grew in that round.

### Step 13. Refine

Fix the validation findings.

### Step 14. LOOP: validation and refine (GATE)

Repeat steps 12-13 until the data check passes AND the user approves the
preview. When stuck, escalate to the user; do not loop alone. Stop rule:
stop when the data check passes and the user approves the preview.

### Step 15. Deliver to the user

Hand over the final package: PDF plus the deck source. A PPTX version
can be built from the rendered slides, but only as an image-based deck:
one rendered PNG per slide, with slide titles as speaker notes. The text
is not editable. That is a limitation, not a feature. An editable-text
PPTX path is NOT adopted yet (see "Still not adopted"). The PDF is the
main deliverable.

### Language pipeline (step 11, in detail)

1. Draft the deck text in Indonesian first (`content-id.md` in the
   worked example). One section per slide: Title, Composition, Exhibit,
   Content, Footnote. `examples/content-id.md` shows the format of each
   section. Write numbers in the notation that
   `scripts/check_numbers_final.py` expects, so the Indonesian and
   English numbers match exactly. Keep the slide order identical in
   both languages.
2. Run the Indonesian humanizer pass. Apply the `humanizer-indonesia`
   rules to the Indonesian draft. Use the installed skill when it is
   available. The condensed rules are in
   `references/humanizer-rules.md`. The pass removes AI tells and
   translationese (kalke, i.e. calques) without changing any number,
   citation, or cross-reference. Run that skill's metric script if it
   is available, and fix what it flags. The Indonesian draft in the
   worked example measured: mean sentence length 14.4 words, standard
   deviation 8.8, 0 em/en dashes. The humanizer produces a draft for a
   human to edit, so edit the result by hand afterwards.
3. Translate to English, then run the English humanizer pass. Translate
   the Indonesian draft into English (`content-en.md`). Then apply the
   `academic-humanizer` rules to the English prose only. Use the
   installed skill when it is available. Never apply the humanizer to
   titles, numbers, model names, citations, or formulas. Titles are full
   sentences that carry numbers, so rewrite a weak title by hand instead
   of running it through the humanizer.

Two lessons from the original build, both caught by an independent review:

- Keep an epistemic hedge such as "to the best of our knowledge" when the
  sentence makes a novelty claim.
- Never let a style fix turn a vague magnitude into a specific exclusive
  claim. A fix that names specific settings ("only on ...") is a new
  empirical claim. Check it against the results table before keeping it.

See `references/humanizer-rules.md`.

### Analysis before the build

The Frozen Spec freezes the method, the slide count, the palette, and
the content plan. The analysis runs after the freeze and before the
text is written in step 11. Titles stay working hypotheses until the
analysis produces numbers.

- **Run the analysis, then write slide titles from the numbers.**
  Titles are full conclusion sentences that carry a number, at most two
  lines long. Example from the worked example: "Churn jumps from 37.4%
  for handsets aged 270-300 days to 60.3% for handsets aged 300-330
  days, a gap of 22.9 percentage points." Never write a title before the
  number behind it exists. Add every number used in a title to the
  verified sheet, including derived ones such as the 22.9-point gap.
  Compare models on the same train/test split and report accuracy, AUC,
  precision, and recall. Report the margin of error next to the scores
  when the split is large enough to compute it. Test feature engineering
  and report the result even when it does not help. In the worked
  example it did not help (cross-validated accuracy 0.6224 with the new
  features against 0.6239 without), so the features were left out and
  the slide says so.
- **Settle the market framing and its boundary sentence.** When the
  company in the case is anonymous, say so on the slides, and say which
  real market is used only as a reference. Write the boundary sentence
  early and repeat it wherever a reader could mistake the reference
  market for the company itself. Example: "Company A is anonymous.
  Indonesia is only a reference market, and the model results are not
  claimed to represent Indonesian customers." Verify each market source
  by opening it (hard rule 5) before any market figure enters the deck.

### Verification discipline

- **One canonical numbers file is the single source of truth.** Keep
  every number the deck shows in one canonical file (JSON in the
  MieLestari build), computed from the model or the executed notebook.
  The deck only displays; it never invents a number by hand. A new
  version of the deck gets a new canonical file; the old file is kept.
- **One checker per version.** Adapt `scripts/check_numbers_final.py`
  to the deck by replacing its verified sheet (the `SHEET`) with the
  new deck's numbers, taken from the executed notebook. Run it. It
  checks three things: numbers are identical between the Indonesian
  and English text, slide by slide; every number appears in the
  verified sheet, as the value, the value times 100, or the value
  divided by 100; the style bans hold (no banned numbers as defined in
  the script, no em/en dash, no emoji, no banned words, no spaced
  hyphen). It must report zero problems. Then run the notebook-vs-deck
  check with `scripts/check_notebook_vs_deck.py` (adapt its paths and
  its `CHECKS` list to the new deck). In the original build it reported
  51 PASS and 9 FAIL. On review, all 9 fell in categories judged
  harmless: notebook-only values, a derived arithmetic gap, and rank
  values shown as ranks by design. See
  `references/number-verification.md`. Record harmless categories in
  writing. A FAIL with no written reason is an open defect.
- **Fix the text, not the checker.** When a check fails, change the deck
  text or the model, never the check.
- **A geometry assertion in the checker.** The checker must also assert
  layout geometry: the bottom edge of every element sits at least 8 px
  above the top of the insight bar, on every slide. The MieLestari v9
  build passed 113/113 checks while a slide was clipped 16 px by its
  insight bar, because the check only flagged elements crossing the
  slide edge.
- **Read the rendered pages.** After the render, read every rendered
  page image by eye. Look for overflow, numbers that differ from the
  English text, and data slides missing a source footnote. Do not ship
  with overflow.

### Build the deck

Author one standalone HTML file per slide, plus `deck.css` and `deck.json`
(the manifest decides slide order). Then run the pipeline:

1. Build charts from the verified numbers with Python and matplotlib.
   `scripts/build_charts_v2.py` is the worked example.
2. Embed fonts and inline images with `scripts/build_deck.py`.
3. Combine the slides with `scripts/assemble_deck.mjs` (run with Bun).
4. Render to PDF and audit with `scripts/render_audit.mjs` (Playwright
   with headless Chromium; run it with `--gate`).
5. Validate with `scripts/validate_pdf.sh`.

Then check the PDF:

- Run `pdfinfo`. Expect the page count from the slide budget at 960 by
  540 pt. This equals the 1280 by 720 px canvas at 96 px per inch.
- Run `pdffonts`. Every font listed must be Source Sans 3 (Regular or
  Bold) and show `yes` in the `emb` column.
- Read every rendered PNG (in `.src/validate/`). Look for overflow,
  numbers that differ from the English text, and data slides missing a
  source footnote.

Command arguments, the full pipeline, and the gates are in
`references/toolchain.md`. Print CSS trap, learned in the KopiRumah
pitch test: kill JS zoom in print CSS (`.frame{zoom:1!important}`,
`@page{size:1280px 720px}`); always check the slide SIZE in the
rendered PDF pages, not only the page count. Five more HTML/CSS build
traps from the test decks (flex `<br>`, stretch, flex-shrink, font
fallback width, SVG marker units) are in `references/toolchain.md`.

### Submit the package

Submit the PDF, the notebook, and the reference list through the course
platform. The reference list on the last slide and the list pasted into
the platform's References field must be the same list. If the assignment
requires AI use disclosure, the list includes the AI session URL. Never
attach the AI chat transcript. Rename `deck.pdf` to follow the platform's
file-name rule. In the worked example the files were `[AccountName].pdf`
and `[AccountName].ipynb`, with account name Rajendriya.

## Case-Competition Mode

Use this mode when the deck is a business case judged cold, without a
presenter. The full spec is in `references/case-competition-mode.md`;
the shape is:

- **Two layers in one file.** A main deck (narrative, 10-12 slides,
  pitch density: one claim per slide, at most 6 lines, one chart per
  slide, slide 1 is a cover and the answer sits on slide 2) plus
  an appendix (document density, one analysis per slide, self-contained,
  sources ON the slide). A divider slide ("Lampiran / Appendix") stands
  between them. Appendix slides are not counted in the slide budget.
- **Answer first.** The recommendation and the key numbers sit on slide
  2, not at the end. Each main slide opens with a question kicker
  ("| Q: ...") and a sentence title that carries a number.
- **A traceable backbone.** Gap, root cause, solution arm, KPI, and
  financial line share one ID chain across the whole deck, so a judge
  can trace one number from the recommendation to its assumption
  without asking.
- **Named frameworks as a rubric.** MAUT, Monte Carlo, tornado,
  break-even, FMEA, Gate 0 with kill criteria. The judge can tick off
  analytic rigor without thinking.
- **Show the work.** Assumptions up front, calibration, sensitivity,
  downside scenarios, and admitted limits. A probability of 100% with
  no visible input lowers credibility, so show the distribution.
- **Something the judge can touch.** A QR code or a link to the working
  model (spreadsheet, repo), not a promise.
- **Close with the decision asked for.** The implementation slide
  carries the decision requested, stages with stop criteria, and
  trigger metrics.
- **Honesty ceiling.** A fictional case without primary data caps at a
  win-worthiness score of 9. Never promise a 10. Assumptions are
  labeled, limits are stated as Phase 2, numbers are never invented.

The worked example is the MieLestari deck (v10 FINAL, 43 slides, scored
9). See `references/case-competition-mode.md`.

## Design rules

Nineteen empirical rules, from the Company A test (rules 1-14), the
"10 Niche Design Hacks" reel (rules 15-18), and the MieLestari test
(rule 19). When the rules and a good look conflict, the look wins; log
the change.

1. **Bold on type scale and boxes.** Titles 36 px over two lines (a
   bold claim plus a light 26 px continuation); key numbers become
   48 px display figures in the title; hero numbers 104-200 px. A
   safe, conservative router output is a defect, not a feature. The
   skill pushes a bold hierarchy as part of the build.
2. **An exhibit must fill the slide height.** A thin one-element
   exhibit floats in empty space. Enlarge it and center it vertically
   until it fills the slide.
3. **A title is a display element, not a text block.** Pull the key
   number out of the title and enlarge it as a display figure.
4. **Display figures stay in tune.** Same color and same voice as the
   title (navy, no text shadow or outline); hierarchy comes only from
   size plus weight. A contrasting color plus outline reads as trying
   too hard to stand apart.
5. **A display number must never sit trapped inside small parentheses.**
6. **Place information creatively.** Diagonal or stepped (rising steps,
   staggered cards, shifted rows), not stiff parallel boxes. Rising
   steps (first step lowest) read as progress; the step shape itself
   shows direction. Do not force an arrow into a narrow 14 px gap.
7. **A background shape must be bold and deliberate, or absent.**
   A small half-hearted accent reads as noise and must go. A background
   shape must not enter the content area; accents live only in the
   padding zone or behind cards (cards on white). A big circle or oval
   behind a chart or table collides with information and hurts the eyes,
   even when the color fits.
8. **A square card must not pierce a slanted shape behind it.** Work
   out the fit (inset plus trapezoid size adjusted).
9. **A comparison line (dashed) sits above the bars, or is deleted.**
   When the bar length alone already shows the best or worst, delete
   the line.
10. **Small shapes at the edge** (a small triangle or trapezoid) that are
    neither bold nor invisible are a distraction. Remove them.
11. **A callout box needs an explaining label** (a small title) so the
    reader knows what the number is for.
12. **A title panel** (tint plus a 6 px coral top line) is the tested
    maximum that passed. Keep it as the standard title treatment on the
    bold variant.
13. **Assets are part of the build, not an option.** Free-license photos
    or illustrations are used from the start (slide 1 vertical photo
    panel, credit in the footer and the references). Hotlinks can fail
    in a headless render, so embed as a base64 data URI and keep the
    file self-contained. **Pitch decks are asset-rich on every slide:**
    each slide carries an image or visual asset relevant to its content,
    not only 2-3 photos on the cover, solution, or ask; sources are
    free-license only (Wikimedia Commons CC0 or public domain, Pexels),
    never AI-generated; verify the license before use. **Big-space
    principle:** an environmental or area photo is used ONLY when it
    gets a big space (a full panel, full-bleed, or a substantial
    full-width band) so the audience understands what the picture
    shows; when a slide cannot give a big space, the photo is DELETED,
    not shrunk or moved to a corner. A photo that does not illustrate
    its slide is deleted even when space exists.
14. **Contrast.** Coral on blue at about 2.2:1 does not read. Text on
    coral or tint uses dark ink (#023A6B); a coral accent on blue uses
    white (about 4.7:1).
15. **Nested corners must be concentric.** Inner radius equals outer
    radius minus padding (a card inside a card or panel). Corners that
    do not match look wrong even when the gap is small.
16. **Borders use alpha, not solid hex.** A solid border looks bad on a
    different background; an alpha color blends with any background.
    This matters because the decks use many colored backgrounds.
17. **Color in OKLCH, not HSL.** The eye does not perceive lightness
    evenly. Build palettes and gradients in OKLCH so equal lightness
    looks equal and gradients do not go gray in the middle (gradients
    use "in oklch").
18. **Match icon weight to text weight.** A thin icon next to bold text
    looks careless; match the icon stroke to the font weight beside it.
19. **Symmetry: distribute panel content vertically.** Panel content
    must be spread vertically (flex space-between or center), never
    stacked at the top with more than 40 px of dead space below the
    text. Case-competition decks carry almost no empty space; layouts
    must be BOLD and not boxy.

## Design tokens

- Navy `#14467C` is the structure color.
- White is the background.
- Soft gold `#E8B84A` is the single accent.
- Slate teal `#2F6F6E` is a sparing secondary color. Use it only where a box
  is truly needed. Never set teal text on a navy background.
- Font: Source Sans 3 only, Regular and Bold.
- Canvas: 1280 by 720 px.
- Minimum sizes: body text 20 px, tables 18 px, citations 13 px.
- Photos are recolored to a navy duotone. The cover uses a small duotone tab,
  not a full-bleed photo.

These are the v1 default tokens. They are the fallback when the user
picks no palette and there is no reference. A deck that locks a palette
from `references/palette-library.md` uses that palette's tokens instead;
the MieLestari deck, for example, uses navy `#0B2E6E` and `#12264A`,
blue `#1F4E9C`, gold `#E8A33D` and `#F5B544`, with Poppins and
Montserrat. Full tokens, contrast figures, the eight accent rules, and
the checklist for avoiding generic-looking visuals are in
`references/design-tokens.md`.

## File layout of a deck project

```
deck/
  content-id.md            Indonesian draft, one section per slide
  content-en.md            English final text, same slide order
  check_numbers_final.py   number and style checker (adapt the SHEET)
  canonical-numbers.json   canonical numbers, single source of truth
  frozen-spec.md           Frozen Spec checklist (Workflow step 10)
  .src/
    slides/                one HTML file per slide, deck.css, deck.json
    media/                 charts (PNG), photos, fonts, build_charts_v2.py
    index.html             assembled document (generated)
    validate/              per-page PNGs from the final PDF (generated)
  deck.pdf                 final output
```

## Dependencies

- `academic-humanizer` (English humanizer; MIT; AIScientists-Dev; v0.3.3):
  six layers, audit then rewrite, preserves numbers and citations, never
  invents evidence. Source: https://github.com/AIScientists-Dev/academic-humanizer.
  Condensed in `references/humanizer-rules.md`.
- `humanizer-indonesia` (Indonesian humanizer; MIT; adhiprib; v1.7.2):
  draft, audit, then final revision. Removes AI tells and translationese.
  Source: https://github.com/adhiprib/humanizer-indonesia. Condensed in
  `references/humanizer-rules.md`.
- The `documents` skill presentation guide (one HTML file per slide plus
  `deck.css` plus `deck.json`, assembled the same way on every run): the layout
  pattern this skill follows.
- The scripts in `scripts/`: `assemble_deck.mjs`, `render_audit.mjs`,
  `validate_pdf.sh`, `build_charts_v2.py`, `check_numbers_final.py`,
  `check_notebook_vs_deck.py`, `build_deck.py`. See `references/toolchain.md`
  for what each one does and where it came from.
- Research and build tools the user asked for: **Statista** for market
  research (market size, industry data, consumer behavior; most content
  sits behind a paywall, so use its free statistics and cite the source,
  and never claim a number that cannot be verified); **Google Trends**
  for consumer insight (free, real-time market trends and changing
  consumer interest, supporting evidence for problem and trend slides and
  appendix); **Canva / Google Slides** for deck design at build time
  (free base tier). These are general tools the user recommended, not
  quotes from third-party material, and no third-party material is copied
  into this repo.
- Tools the build commands need: Python with matplotlib, Bun, Playwright with
  headless Chromium, `pdfinfo` and `pdffonts` (from poppler-utils), and the
  Source Sans 3 font files. Versions are not recorded in this skill.

## Still not adopted

These items are open decisions, not rules. Do not teach them as rules
until they are tested and adopted in a new version.

- **Editable-text PPTX path** (python-pptx or another route). The
  supported PPTX today is image-based only (one rendered PNG per
  slide). See `references/toolchain.md`.
- **Density switch for professional vs pitch.** Kept as a preset. Note:
  the user's taste is bold display typography even for professional
  decks, so "bold" is not pitch-only.
- **Full automatic palette extraction** from a reference image. The
  proven mechanism is "show 3-4 options from the library, user locks
  one in".
- **Free-asset source list.** A list of free-license sources; the
  licenses were verified in October 2026 and the list was researched
  again in November 2026; it must be re-verified before it is adopted
  into this skill.
- **Processing fluency citation.** A paper (Reber et al. 2004) was
  proposed as support for carousel design; the paper is NOT verified,
  so do not cite it.

## Reference files

| File | What it holds |
|---|---|
| `references/deck-rules.md` | Assignment rules and the 15-slide plan |
| `references/number-verification.md` | Number discipline, the checker, real cases |
| `references/design-tokens.md` | Colors, fonts, sizes, photo and accent rules |
| `references/toolchain.md` | Build pipeline, scripts, gates, PPTX limits |
| `references/humanizer-rules.md` | Both humanizer skills, condensed, with cautions |
| `references/worked-example.md` | The Company A churn deck, numbers and slide map |
| `references/case-competition-mode.md` | Case-Competition Mode spec and the MieLestari worked example |
| `references/palette-library.md` | 51 named palettes with fit labels |
| `references/palette-picker-2026-11-24.html` | Visual palette picker, all 51 palettes |
| `references/alur-kerja-v2-flowchart-2026-11-24.html` | Workflow flowchart (HTML) |
| `references/alur-kerja-v2-flowchart-2026-11-24.pdf` | Workflow flowchart (PDF) |
| `references/roadmap.md` | Ideas for a future version; nothing here is a rule |
| `CHANGELOG.md` | Version history, what changed, what is still open |
| `examples/content-en.md` | Final English deck text (worked example) |
| `examples/content-id.md` | Indonesian draft text (worked example) |
| `scripts/` | Toolchain scripts, copied verbatim |
