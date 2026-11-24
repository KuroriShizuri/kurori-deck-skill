# Deck rules

Rules for the assignment and the 15-slide plan. The GCI World 2026 Final
Assignment is the worked example. Rules that came from its official
documents are marked as such. Adapt the values to the new assignment, keep
the structure.

## Assignment rules (GCI World 2026, from README.docx and the tutorial)

- Deliver a PDF slide deck, **15 slides maximum in total**, including the
  title slide and the references slide. A slide past 15 is ignored by the
  grader.
- Submit through the course platform (Omnicampus in the GCI case): (1)
  slides PDF, (2) reference list in the platform References field plus
  citations on the slides, (3) the analysis notebook (`.ipynb`, `.py`,
  or `.zip`) that reproduces the analysis. Resubmission is allowed before
  the deadline; only the last submission is graded, and every resubmission
  must attach all files. No late submission.
- File names follow the platform rule. GCI case: `[AccountName].pdf` and
  `[AccountName].ipynb`, account name Rajendriya.
- Deadline in the GCI case: 28 November 2026, 11:30 UTC (18:30 WIB).
- At least one ML or statistical model. The model name, the evaluation
  metric, and the score must be written explicitly in slide text. A
  visualization alone does not count. Comparing several models is better.
  A model that clearly does not fit the data does not count.
- The proposal must rest on EDA and external market analysis, with clear
  citations. Direct quotation stays below 40% as a guide. The deck must be
  understandable by executives without an ML background. Use many
  visualizations. The logic must stay consistent from analysis to
  proposal.
- Explain why the model was chosen, how it was built, and what insight it
  gave. The model insight must inform the proposal. State the business
  problem, the ML task, the business question in one sentence a non
  technical executive understands, and who acts on the model output and
  what action they take. A model whose output cannot be acted on is not a
  proposal.
- The grading rubric scores the business proposal, not the model. The
  model is one input to the proposal.
- When generative AI is used, include the chat URL in the references.
  Never publish the chat transcript.

## What the official documents do NOT say

Read the rules from the files, not from a summary. In the GCI build, an
early browser report invented a 16:9 requirement, a white background, a
group presentation with Q and A, and a Google Classroom deadline. None of
it was in the official documents. The correction cost a full plan rewrite.
Verify format claims against the README and tutorial files on disk before
believing them.

## The 15-slide plan (GCI case)

Story flow: hook (1 to 2), problem (3 to 4), insight (5 to 8), solution
(9 to 12), cost (13), conclusions (14), references (15). One idea per
slide, one exhibit per results slide. Slide titles are full conclusion
sentences that carry a number.

| # | Part | Slide (GCI case) |
|---|---|---|
| 1 | Title | Cover with thesis numbers and the break-even figure |
| 2 | Intro and market | Reference market in three figures plus operator chart |
| 3 | Problem definition | Business question and churn window timeline |
| 4 | EDA, dataset limits | 49.6% churn applies only to this dataset; missing data |
| 5 | EDA, main finding | The 300-day churn cliff |
| 6 | EDA, segments | Risk segments P1 and P2 |
| 7 | Experiments | Model comparison, scores explicit |
| 8 | Experiments | What drives churn (importance plus intervenability) |
| 9 | Proposal 1 | Handset renewal program |
| 10 | Proposal 2 | Targeted retention offer |
| 11 | Proposal 1 and 2 | How it works (scoring, targeting, action, monitoring) |
| 12 | Proposal impact | Expected impact, three save-rate scenarios |
| 13 | Quotation | First-year service fee |
| 14 | Conclusions | Three findings plus the decision requested |
| 15 | References | Full reference list with URLs |

The GCI plan went through a review by Sonnet 5.5 before the build. The
review changed: proposal titles stay hypotheses until the analysis lands;
slide 5 title was replaced because it overclaimed; slide 8 became one
table with all models on the same split; slide 13 became three save-rate
scenarios instead of one impact number; slides 4 and 5 were merged to free
a slot; the market slide must state its assumptions and cite on the slide.
Get a review of the plan before building, and record what it changes.

## Title rule

A slide title is a full conclusion sentence with a number, at most two
lines. Short verdict titles ("solid", "stop-scroll") were tried and
dropped after review: they carry no evidence. A verdict word may survive
only as a small chip on a comparison slide, never as the title.

## Citation rule

Every number on a slide carries its source on the same slide, as a small
footnote (at least 13 px): organization, document title, date. Example:
"Source: PwC, Indonesia Telecommunications Sector Overview, Jun 2026".
The last slide lists every reference in full, with URLs. The same list
goes into the platform References field, unchanged.

## Submission checklist

- [ ] PDF has 15 pages or fewer, 960 by 540 pt, fonts embedded
- [ ] Notebook runs by clicking Run All, with no setup step
- [ ] Model name, metric, and score are explicit in slide text
- [ ] Every number has a source on its own slide
- [ ] Reference list on slide 15 matches the platform References field
- [ ] AI session URL is cited; no transcript is attached
- [ ] File names follow the platform rule
- [ ] Checker reports zero problems (see `number-verification.md`)
