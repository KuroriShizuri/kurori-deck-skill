# rajen-deck-skill

Build a business proposal deck backed by data analysis, the way the GCI
World 2026 Final Assignment deck was built: draft in Indonesian first,
run humanizer passes, verify numbers against the executed notebook,
write one HTML file per slide, and render the PDF with a repeatable
pipeline. 15 slides maximum; every number is cited on the slide where it
appears.

Origin: GCI World 2026 Final Assignment (Company A telecom churn),
November 2026. The finished package was delivered to its author; the deck
PDF itself is not included here. What is included is the method, the
rules, the toolchain, and the deck text as a worked example.

## What is inside

| Path | What it is |
|---|---|
| `SKILL.md` | The skill, in English (start here) |
| `SKILL-id.md` | The skill, in Indonesian (same content, rewritten naturally) |
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

## Install

This skill is harness-neutral: it is a folder of Markdown and scripts, and
it works in any AI host that loads skills from a folder. Copy the whole
`rajen-deck-skill` folder into the skill directory of your host, then point
the host at it the way that host loads a local skill.

- Claude Code: copy into `~/.claude/skills/rajen-deck-skill/`
- Codex: copy into the Codex skills directory for your install
- Muse: copy into `~/workspace/custom-skills/rajen-deck-skill/`
- Other hosts: copy into the directory where that host reads local skills

No build step and no extra install are needed for the skill text itself.
The toolchain scripts need their own runtimes when you run a build
(Bun, Python 3 with matplotlib and pandas, Playwright with Chromium,
`pdfinfo`, `pdffonts`, `pdftoppm`). See `references/toolchain.md`.

The two humanizer skills are separate projects and are not bundled here.
Install them the same way, from their own repos, when you want the full
language pipeline:

- `academic-humanizer` (English): AIScientists-Dev/academic-humanizer,
  https://github.com/AIScientists-Dev/academic-humanizer, MIT, v0.3.3
- `humanizer-indonesia` (Indonesian): the humanizer-indonesia skill,
  v1.7.2

## Use

1. Read `SKILL.md` (or `SKILL-id.md`) first.
2. Read the assignment README and tutorial files directly, and write the
   real rules down before drafting.
3. Follow the ten workflow steps in order. Do not skip the number
   verification step: the checker must report zero problems before the
   deck is built.
4. Adapt `scripts/check_numbers_final.py` to the new deck by replacing
   the verified-numbers sheet (`SHEET`) with the new verified numbers.
   Keep the style bans as they are.
5. Use `examples/content-en.md` and `examples/content-id.md` as the shape
   of the deck text: one section per slide, Title, Composition, Exhibit,
   Content, Footnote.

## Hard rules, in short

15 slides maximum including title and references. At least one model with
name, metric, and score written explicitly in slide text. Direct quotation
below 40% of the deck text, as a guide. Every number carries its source on
the same slide. Market data only after its source is proven openable.
Model scores must match the executed notebook. AI chat history is never
published (session URL only). No em-dash, no en-dash in slide text, no
emoji, no AI-style wording. Model names are exempt from the word ban.
Numbers are never invented or copied from memory.

## What this skill is not

The pitch-deck frameworks listed in `references/roadmap.md`
(H-P-S-I-T-C, SCR Framework, Pyramid Principle, One slide One message,
BLUF method, Data Slide Formula, Storyboard approach, the "So what?"
Test) are candidates for a future improvement. They are not adopted here
and must not be taught as rules of this skill.

## License

MIT. Copyright 2026 Rajendriya Wigar Punagi. See `LICENSE`.
