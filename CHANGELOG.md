# Changelog - kurori-deck-skill

Additive-only: each version adds to the previous one. Old methods stay
recorded; nothing is deleted silently. When a rule changes, this file
says what changed and why.

## v2.0.0 - 25 Nov 2026

The FREEZE opens. Design v2 (router-design-v2-2026-11-24.md) plus the
MieLestari case test (v10 FINAL, scored 9) land in the skill.

### Added

- **Method router** (design v2 sections 1-5). Nine methods (4 flows:
  Pyramid, H-P-S-I-T-C, SCR, Data-story; 5 supporting layers: BLUF, One
  slide one message, Data Slide Formula, "so what?" test, Storyboard),
  ranked per brief on five dimensions (purpose, audience, data
  availability, slide budget, style). Past user preference is recorded
  as evidence under dimensions 1 and 5, not as a sixth dimension.
  Walk-down moves between the 4 flows. Candidate orders per deck type:
  professional and data (Data-story first, proven by the Company A
  test), pitch (H-P-S-I-T-C first, confirmed by the KopiRumah pitch
  test), case competition (Pyramid first, prior with supporting
  evidence), academic (Data-story first). Two modes: general (router
  picks) and focused (user gives the method; follow it and advise).
  SCR stands alone in the pool AND nests inside H-P-S-I-T-C.
- **Slide budget as a sweet spot** (design v2 section 8). Target 15,
  no hard floor any more; the agent decides more or fewer from the
  findings. Cap 15 applies only when the assignment limits it.
  Case-competition main deck 10-12 slides; appendix not counted.
- **Palette library** (`references/palette-library.md`, 51 named
  palettes) plus the visual picker
  (`references/palette-picker-2026-11-24.html`). The agent reasons
  about the palette from data, audience, and context, proposes 3-4
  options with one line of reasoning each, and the user locks one in.
  "Bebas" means the agent uses its own #1 and records it. Only verified
  hex becomes a build token.
- **15-step workflow with a Frozen Spec** (design v2 section 9 and the
  15-step table). Brief converges first (step 7 gate, consolidated
  confirmation, always shown even when the material looks complete),
  decisions freeze into a Frozen Spec (step 10), the full HTML preview
  is the iteration gate (step 9), and the validate-refine loop stops
  when the data check passes AND the user approves the preview
  (step 14). The humanizer passes are a checklist item in step 11
  (Indonesian text, humanizer-id, translate to English,
  academic-humanizer), not a memory. The brief for a test deck must
  include the reference list. The asset-permission question ("may the
  agent search the internet for images and assets?") is a standard
  step-5 question; default when unanswered is ALLOWED from verified
  free-license sources only, never AI-generated images.
- **Case-Competition Mode** (`references/case-competition-mode.md`).
  Two layers in one file: a 10-12 slide narrative main deck (answer
  first, question kickers, sentence titles with numbers) plus a dense
  appendix (one analysis per slide, self-contained, sources ON the
  slide). Traceable backbone, named frameworks as a rubric, show the
  work, a touchable artifact (QR or model link), close with the decision
  asked for, and an honesty ceiling: a fictional case without primary
  data caps at a win-worthiness score of 9. Never promise a 10. Worked
  example: the MieLestari deck (v10 FINAL, 43 slides, scored 9).
- **Design rules, 19 total** (design v2 section 10 plus the symmetry
  rule). Rules 1-14 from the Company A test, rules 15-18 from the "10
  Niche Design Hacks" reel (concentric corners, alpha borders, OKLCH
  color, icon weight matched to text weight), rule 19 symmetry from the
  user's 25 Nov 2026 critique (panel content distributed vertically,
  never top-stacked with more than 40 px of dead space below the text).
- **Verification discipline.** Canonical numbers file as the single
  source of truth, one checker per version, rendered pages read by eye
  (not only an overflow check), and a geometry assertion: every
  element's bottom edge at least 8 px above the insight bar.
- **Research and build tools** the user asked for: Statista (free
  statistics only, cite the source), Google Trends (free consumer
  insight), Canva / Google Slides (build time).
- **Workflow flowchart** (`references/alur-kerja-v2-flowchart-2026-11-24.html`
  and `.pdf`).
- **Pitch test result.** The pitch candidate order is CONFIRMED by the
  KopiRumah pitch test (24 Nov 2026, H-P-S-I-T-C #1, 11-slide deck v7
  FINAL, user verdict "dah mantep banget"). The checklist listed the
  pitch test as still open; the design document marks it done, and this
  changelog follows the design document.

### Changed

- **Hard rule 1 (slide count).** Was: "15 slides maximum, including the
  title slide and the references slide." Now: the slide budget follows
  the assignment; 15 is the sweet spot, not a hard floor; the cap of 15
  applies only when the assignment limits it. Hard rules 2-10 are
  unchanged.
- **Workflow steps.** The v1 ten steps are folded into the v2 fifteen
  steps. The v1 content (assignment rules, plan, analysis and titles
  from numbers, market framing, Indonesian-first draft, two humanizer
  passes, checker, build pipeline, submit) is kept inside steps 1-15.
  Nothing was dropped.
- **Roadmap.** The pitch-deck frameworks (H-P-S-I-T-C, SCR, Pyramid,
  One slide One message, BLUF, Data Slide Formula, Storyboard, "so
  what?" test) are ADOPTED in v2 as the router pool. The roadmap file
  now records what is still open instead of listing them as candidates.
- **Step 15 deliverable.** The workflow table said "pptx (editable
  text) plus PDF". The editable-text PPTX path is NOT adopted, so step
  15 now says: PDF plus deck source; PPTX is image-based only. See
  "Still open" below.

### Still open (not adopted, not rules)

- Editable-text PPTX path (python-pptx or another route).
- Density switch for professional vs pitch (kept as a preset; note the
  user's taste is bold display typography even for professional decks).
- Full automatic palette extraction from a reference image.
- Free-asset source list (researched Nov 2026, must be re-verified
  before adoption).
- Processing fluency citation (Reber et al. 2004, paper NOT verified,
  do not cite).
- "Two modes general/focused plus router mode" from early v2 research
  is covered in v2 as general mode (router picks) and focused mode
  (user gives the method). No separate definition was needed.

## v1.0.0 - 24 Nov 2026

Initial release as `gci-deck-skill`, renamed to `rajen-deck-skill` and
then to `kurori-deck-skill` (same day; the skill face never contained
the old program name). Method: Company A telecom churn deck, 15 slides,
Indonesian draft first, two humanizer passes, number checker with zero
problems, one HTML file per slide, PDF rendered with a repeatable
pipeline. Ten hard rules. Humanizer source links added to
`references/humanizer-rules.md` (academic-humanizer, humanizer-indonesia).
