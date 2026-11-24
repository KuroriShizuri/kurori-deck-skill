---
name: rajen-deck-skill
version: 1.0.0
description: |
  Build a business proposal deck backed by data analysis, the way the GCI World
  2026 Final Assignment deck was built: draft in Indonesian first, run humanizer
  passes, verify numbers against the executed notebook, write one HTML file per
  slide, and render the PDF with a repeatable pipeline. 15 slides maximum;
  every number is cited on the slide where it appears.
license: MIT
compatibility: claude-code codex muse opencode
---

# Rajen Deck Skill

Build a short business proposal deck from a data analysis, with a source for
every number. This skill records the method used for the GCI World 2026 Final
Assignment (Company A telecom churn, November 2026): a 15-slide PDF deck in
English, built from an Indonesian draft. Every number was checked against the
executed analysis notebook and cited on the slide where it appears. The
finished package was delivered to its author. The deck PDF itself is not
included here. This skill includes the method, the rules, the toolchain, and
the deck text as a worked example (`examples/`).

## When to use

Use this skill when the user asks for a presentation deck that must defend a
business proposal with data: a course final assignment, a churn or retention
proposal, or any executive deck where a model supports a recommendation. It
fits when the deck must stay short (15 slides or fewer), every number must
carry its source, and the text must not read like generic AI output.

## When not to use

Do not use it for a free-form creative deck, a lecture slide set, or a deck
with no data behind it. The verification steps assume there is an analysis
notebook (or equivalent) that produces the numbers on the slides. If there is no notebook or equivalent analysis output, the number steps do
not apply. Skip Step 3 and the notebook checks in Step 8, run the remaining
steps, and say plainly that the numbers were not verified against an executed
analysis.

## Hard rules

These rules are never broken. The original deck passed its build and number
checks (Steps 8 and 9) because it followed them.

1. **15 slides maximum, including the title slide and the references slide.**
   Count every slide. In the GCI assignment the grader ignores slides past the
   limit, so an extra slide counts as missing. Confirm the limit and its
   consequence for each new assignment (Step 1).
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
   The GCI case cites the Kiro session URL, which is login-gated and does not
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
   `check_numbers_final.py`, see Step 8), it does not go on a slide. In
   drafts, write TBD or drop the claim instead of guessing. No TBD may remain
   in the submitted deck.
10. **The last slide is the full reference list with URLs.** The same list
    goes into the submission platform's References field, unchanged.

## Workflow

### Step 1. Read the assignment rules from the official documents

Read the assignment README and tutorial files directly from disk. Do not rely
on a browser summary or a chat answer about the format. The GCI case showed
why: an early browser report invented a 16:9 requirement, a white background,
a group presentation, and a Google Classroom deadline. None of these were in
the official documents. (The final deck still uses a 16:9 canvas and a white
background, as design choices, not as requirements.) The real rules were: PDF,
15 slides maximum, submission through Omnicampus, deadline 28 November 2026
11:30 UTC, file names `[AccountName].pdf` and `[AccountName].ipynb`. For a new
assignment, confirm its real rules before writing anything. Record them in a
new rules file formatted like `references/deck-rules.md`, and do this before
the build starts.

### Step 2. Plan the deck before the analysis is finished, but do not fix slide titles yet

Draft a 15-slide plan covering hook, problem, insight, solution, cost,
conclusions, and references. The GCI plan, slide by slide, is in
`references/deck-rules.md`. If the new deck needs fewer slides, 15 is a
ceiling, not a target. Give each slide one idea and each results slide one
exhibit. Keep proposal titles as working hypotheses until the analysis
produces numbers.

### Step 3. Run the analysis, then write slide titles from the numbers

Titles are full conclusion sentences that carry a number, at most two lines
long. Example from the worked example: "Churn jumps from 37.4% for handsets
aged 270-300 days to 60.3% for handsets aged 300-330 days, a gap of 22.9
percentage points." Never write a title before the number behind it exists.
Add every number used in a title to the verified sheet, including derived
ones such as the 22.9-point gap.

Compare models on the same train/test split and report accuracy, AUC,
precision, and recall. Report the margin of error next to the scores when the
split is large enough to compute it. Test feature engineering and report the
result even when it does not help. In the GCI case it did not help
(cross-validated accuracy 0.6224 with the new features against 0.6239
without), so the features were left out and the slide says so.

### Step 4. Settle the market framing and its boundary sentence

When the company in the case is anonymous, say so on the slides, and say which
real market is used only as a reference. Write the boundary sentence early and
repeat it wherever a reader could mistake the reference market for the company
itself. Example: "Company A is anonymous. Indonesia is only a reference
market, and the model results are not claimed to represent Indonesian
customers." Verify each market source by opening it (rule 5) before any market
figure enters the deck.

### Step 5. Draft the deck text in Indonesian first

Write the full slide text in Indonesian (`content-id.md` in the worked
example). Use one section per slide: Title, Composition, Exhibit, Content,
Footnote. `examples/content-id.md` shows the format of each section. Write
numbers in the notation that `scripts/check_numbers_final.py` expects, so the
Indonesian and English numbers match exactly. Keep the slide order identical
in both languages.

### Step 6. Run the Indonesian humanizer pass

Apply the `humanizer-indonesia` rules to the Indonesian draft. Use the
installed skill when it is available. The condensed rules are in
`references/humanizer-rules.md`. The pass removes AI tells and translationese
(kalke, i.e. calques) without changing any number, citation, or
cross-reference. Run that skill's metric script if it is available, and fix
what it flags. The GCI Indonesian draft measured: mean sentence length 14.4
words, standard deviation 8.8, 0 em/en dashes. The humanizer produces a draft
for a human to edit, so edit the result by hand afterwards.

### Step 7. Translate to English, then run the English humanizer pass

Translate the Indonesian draft into English (`content-en.md`). Then apply the
`academic-humanizer` rules to the English prose only. Use the installed skill
when it is available. Never apply the humanizer to titles, numbers, model
names, citations, or formulas. Titles are full sentences that carry numbers,
so rewrite a weak title by hand instead of running it through the humanizer.

Two lessons from the GCI build, both caught by an independent review:

- Keep an epistemic hedge such as "to the best of our knowledge" when the
  sentence makes a novelty claim.
- Never let a style fix turn a vague magnitude into a specific exclusive
  claim. A fix that names specific settings ("only on ...") is a new
  empirical claim. Check it against the results table before keeping it.

See `references/humanizer-rules.md`.

### Step 8. Verify every number with the checker

Copy `scripts/check_numbers_final.py` into the deck project root. Replace its
verified sheet (the `SHEET`) with the new deck's numbers, taken from the
executed notebook. Run it. It checks three things:

1. Numbers are identical between the Indonesian and English text, slide by
   slide.
2. Every number appears in the verified sheet, as the value, the value times
   100, or the value divided by 100.
3. The style bans hold: no banned numbers (as defined in the script), no
   em/en dash, no emoji, no banned words, no spaced hyphen.

It must report zero problems.

Then run the notebook-vs-deck check with `scripts/check_notebook_vs_deck.py`
(adapt its paths and its `CHECKS` list to the new deck; the GCI version is the
worked example). In the GCI build it reported 51 PASS and 9 FAIL. On review,
all 9 fell in categories judged harmless: notebook-only values, a derived
arithmetic gap, and rank values shown as ranks by design. See
`references/number-verification.md`.

### Step 9. Build the deck

Author one standalone HTML file per slide, plus `deck.css` and `deck.json`
(the manifest decides slide order). Then run the pipeline:

1. Build charts from the verified numbers with Python and matplotlib.
   `scripts/build_charts_v2.py` is the worked example.
2. Embed fonts and inline images with `scripts/build_deck.py`.
3. Combine the slides with `scripts/assemble_deck.mjs` (run with Bun).
4. Render to PDF and audit with `scripts/render_audit.mjs` (Playwright with
   headless Chromium; run it with `--gate`).
5. Validate with `scripts/validate_pdf.sh`.

Then check the PDF:

- Run `pdfinfo`. Expect 15 pages for the GCI deck (at most 15 in general) at
  960 by 540 pt. This equals the 1280 by 720 px canvas at 96 px per inch.
- Run `pdffonts`. Every font listed must be Source Sans 3 (Regular or Bold)
  and show `yes` in the `emb` column.
- Read every rendered PNG (in `.src/validate/`). Look for overflow, numbers
  that differ from the English text, and data slides missing a source
  footnote.

Command arguments, the full pipeline, and the gates are in
`references/toolchain.md`.

### Step 10. Submit the package

Submit the PDF, the notebook, and the reference list through the course
platform. The reference list on the last slide and the list pasted into the
platform's References field must be the same list. If the assignment requires
AI use disclosure, the list includes the AI session URL. Never attach the AI
chat transcript. Rename `deck.pdf` to follow the platform's file-name rule. In
the GCI case the files were `[AccountName].pdf` and `[AccountName].ipynb`,
with account name Rajendriya.

## File layout of a deck project

```
deck/
  content-id.md            Indonesian draft, one section per slide
  content-en.md            English final text, same slide order
  check_numbers_final.py   number and style checker (adapt the SHEET)
  .src/
    slides/                one HTML file per slide, deck.css, deck.json
    media/                 charts (PNG), photos, fonts, build_charts_v2.py
    index.html             assembled document (generated)
    validate/              per-page PNGs from the final PDF (generated)
  deck.pdf                 final output
```

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

Full tokens, contrast figures, the eight accent rules, and the checklist for
avoiding generic-looking visuals are in `references/design-tokens.md`.

## Dependencies

- `academic-humanizer` (English humanizer; MIT; AIScientists-Dev; v0.3.3):
  six layers, audit then rewrite, preserves numbers and citations, never
  invents evidence. Source: https://github.com/AIScientists-Dev/academic-humanizer.
  Condensed in `references/humanizer-rules.md`.
- `humanizer-indonesia` (Indonesian humanizer; v1.7.2): draft, audit, then
  final revision. Removes AI tells and translationese. Condensed in
  `references/humanizer-rules.md`.
- The `documents` skill presentation guide (one HTML file per slide plus
  `deck.css` plus `deck.json`, assembled the same way on every run): the layout
  pattern this skill follows.
- The scripts in `scripts/`: `assemble_deck.mjs`, `render_audit.mjs`,
  `validate_pdf.sh`, `build_charts_v2.py`, `check_numbers_final.py`,
  `check_notebook_vs_deck.py`, `build_deck.py`. See `references/toolchain.md`
  for what each one does and where it came from.
- Tools the Step 9 commands need: Python with matplotlib, Bun, Playwright with
  headless Chromium, `pdfinfo` and `pdffonts` (from poppler-utils), and the
  Source Sans 3 font files. Versions are not recorded in this skill.

## Roadmap: NOT adopted, not part of this skill

Pitch-deck frameworks such as H-P-S-I-T-C, the SCR Framework, the Pyramid
Principle, One slide One message, the BLUF method, the Data Slide Formula, the
Storyboard approach, and the "So what?" Test are recorded in
`references/roadmap.md` as candidates for a future improvement. They are NOT
adopted here. Do not teach them as rules of this skill until the skill author
and the person using the skill brainstorm them and adopt them in a new
version.

## Reference files

| File | What it holds |
|---|---|
| `references/deck-rules.md` | Assignment rules and the 15-slide plan |
| `references/number-verification.md` | Number discipline, the checker, real cases |
| `references/design-tokens.md` | Colors, fonts, sizes, photo and accent rules |
| `references/toolchain.md` | Build pipeline, scripts, gates, PPTX limits |
| `references/humanizer-rules.md` | Both humanizer skills, condensed, with cautions |
| `references/worked-example.md` | The Company A churn deck, numbers and slide map |
| `references/roadmap.md` | Pitch-deck frameworks under consideration, not adopted |
| `examples/content-en.md` | Final English deck text (worked example) |
| `examples/content-id.md` | Indonesian draft text (worked example) |
| `scripts/` | Toolchain scripts, copied verbatim |
