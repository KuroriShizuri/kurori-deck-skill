# Toolchain

The build pipeline of the GCI deck, as it ran in November 2026. Commands
are given so a new deck can repeat them. Paths are relative to the deck
project root unless stated.

## Pipeline

```
content-id.md / content-en.md
        |
        v
check_numbers_final.py        (gate: zero problems)
        |
        v
per-slide HTML + deck.css + deck.json     (authored source)
        |
        v
build_charts_v2.py            (matplotlib charts from verified numbers)
        |
        v
build_deck.py                 (embed fonts, inline images)
        |
        v
assemble_deck.mjs (Bun)       (combine into .src/index.html)
        |
        v
render_audit.mjs --gate       (Playwright + Chromium: PDF + audit)
        |
        v
validate_pdf.sh               (PDF validation, per-page PNGs)
        |
        v
pdfinfo + pdffonts + visual read of every PNG
        |
        v
deck.pdf
```

## Scripts

All seven scripts are copied verbatim into `scripts/`. Three of them were
not authored for the GCI project: `assemble_deck.mjs`,
`render_audit.mjs`, and `validate_pdf.sh` come from the shared artifact
scripts directory and were invoked from there during the original build.
They are copied here unchanged so the skill is self-contained. The other
four (`build_charts_v2.py`, `check_numbers_final.py`,
`check_notebook_vs_deck.py`, `build_deck.py`) were written for the GCI deck.

| Script | Role | Runtime |
|---|---|---|
| `scripts/build_charts_v2.py` | Build all data charts with matplotlib from verified numbers. Palette navy `#14467C`, soft gold `#E8B84A`, ink `#1A2733`, muted `#5A6B7C`, grid `#D9E1E8`, gray `#9AA5B1`. Font Source Sans 3 from the project media dir. Deciles are recomputed from the source CSVs and asserted against the deck values. Outputs PNG files into `.src/media/`. | Python 3, matplotlib, pandas, numpy |
| `scripts/build_deck.py` | Embed fonts and images into the slide source, in place. Appends `@font-face` rules (base64 TTF, Source Sans 3 Regular 400 plus Bold 700) to `deck.css` once, guarded by a marker comment. Replaces `{{IMG:filename}}` placeholders in every slide HTML with a base64 data URI from `.src/media/`. Run after authoring slides, before `assemble_deck.mjs`. | Python 3 (stdlib only) |
| `scripts/assemble_deck.mjs` | Combine the authored per-slide deck into one self-contained document. Inputs: `--slides <abs dir>` (the `.src/slides/` directory) and `--out <abs file>` (normally `.src/index.html`). `deck.json` is the ordering authority. Prints one JSON object with ok, out, count, and slides. Any failure exits non-zero. | Bun |
| `scripts/render_audit.mjs` | Render the combined HTML with Playwright and headless Chromium, then emit a PDF and per-page PNGs plus a deterministic JSON report. Flags include `--html`, `--pdf`, `--png-dir`, `--fonts`, `--require-webfonts`, `--page-selector`. The `--gate` run checks overflow, missing images, and fonts. In the GCI build the gate reported `ok: true`, 15 pages, no overflow, no broken images, vertical fill 98% on every slide. | Bun, Playwright, Chromium |
| `scripts/validate_pdf.sh` | Validate the PDF: `validate_pdf.sh <pdf> <html> <out-dir>` (out-dir must end in `/validate`). Requires `python3`, `pdfinfo`, `pdftoppm`, `awk`. In the GCI build it reported PASS with 15 validation PNGs. | Bash, poppler-utils |
| `scripts/check_numbers_final.py` | Number and style checker over `content-id.md` and `content-en.md`. See `references/number-verification.md`. Adapt the `SHEET` to the new deck. Must report zero problems. | Python 3 (stdlib only) |
| `scripts/check_notebook_vs_deck.py` | Notebook-vs-deck check: compare notebook cell outputs with the deck text (pdftotext of the final PDF plus `content-en.md` for chart-only numbers). Normalizes thousands separators so 17,117 matches 17117. Each `CHECKS` entry is a (label, notebook pattern, deck pattern) substring match. Adapt `BASE`, the notebook path, `DECK_TXT`, `CONTENT_EN`, and the `CHECKS` list to the new deck. Exit 0 means all checks pass, 1 means any mismatch. In the GCI build it reported 51 PASS and 9 FAIL in known harmless categories; see `references/number-verification.md`. | Python 3, pandas |

## Requirements

- Bun (for `assemble_deck.mjs` and `render_audit.mjs`)
- Python 3 with matplotlib, pandas, numpy (for `build_charts_v2.py`)
- Playwright with headless Chromium (for `render_audit.mjs`)
- `pdfinfo`, `pdffonts`, `pdftoppm` (poppler-utils, for validation and
  final checks)
- Source Sans 3 Regular and Bold TTF files in `.src/media/fonts/`

## Gates before shipping

All of these passed on the GCI deck before submission:

- `check_numbers_final.py`: Total masalah: 0
- `check_notebook_vs_deck.py`: 51 PASS, 9 FAIL in known harmless categories
  (see `references/number-verification.md`)
- `render_audit.mjs --gate`: `ok: true`, 15 pages, overflow none,
  broken images none, vertical fill 98% on every slide
- `validate_pdf.sh`: PASS, 15 validation PNGs
- `pdfinfo`: 15 pages, 960 by 540 pt
- `pdffonts`: only `SourceSans3-Roman`, all `emb yes`
- Visual check: all 15 PNGs read one by one. No overflow, numbers match
  `content-en.md`, source footnotes present on every data slide.

Fix overflow by shrinking the chart or the supporting text, then rebuild
and re-run the gate. The GCI build needed three iterations: slide 5
overflow 65 px, slide 8 overflow 14 px, slide 12 overflow 39 px in the
first pass, fixed by resizing charts (deciles 940 to 780 px, ranks
capped at 680 px, impact line 860 to 760 px) and trimming text. Do not
ship with overflow.

## The PPTX alternative, and its limit

A PPTX version can be built from the rendered slides, but only as an
image-based deck: one rendered PNG per slide, with slide titles as
speaker notes. The text is not editable. That is a limitation, not a
feature. The PDF is the main deliverable. If an editable-text PPTX is
required, rebuild the deck slide by slide in a presentation tool; it will
be near-identical, not pixel-exact. There is no supported path that
converts the HTML source into editable PPTX text.

## Known quirks, recorded not hidden

- The render audit may report the font family as "Source Sans 3
  ExtraLight" because the TTF files carry a legacy family name (name ID
  1). The weight class is correct (400/700) and `pdffonts` proves only
  `SourceSans3-Roman` is embedded. It is not the wrong font.
- An assemble warning that `deck.css` carries no embedded `@font-face`
  is a heuristic that only recognizes `data:font/woff2`. TTF data URIs
  embed and render correctly; `pdffonts` is the proof.
- The layout catalog used for slide archetypes (category 08, entries 335
  to 350) has only 16 entries, so some layouts repeat (338 three times,
  349 twice in the GCI deck). Reuse is fine when the archetype fits.
