# Number verification

How numbers get onto slides, and how they are checked. This is the
discipline that keeps a deck honest. Every rule below comes from a real
failure or a real catch in the GCI build.

## The authority rule

The executed notebook is the authority for every model number. Not a
local run, not the tutorial text, not memory. In the GCI build the
submitted notebook was executed in Colab, and the deck was checked
against that executed notebook. Local runs of the same code can give
slightly different scores (different library versions), so the deck must
match the notebook the grader receives.

## Real cases from the GCI build

### The tutorial number that must never be written

The tutorial notebook reported XGBoost test accuracy 0.6368. The
reproduced analysis measured XGBoost accuracy 0.6357 with AUC 0.6938.
The deck writes 0.6357, never 0.6368. The checker bans the strings
"0.6368" and "0,6368" outright. Whenever a tutorial or sample reports a
score, reproduce it and use your own measured score.

### The stable score

Random Forest accuracy 0.6257 with AUC 0.6785 was stable across two
separate Colab runs. An earlier local run had printed 0.6245 and 0.6790.
The deck was corrected everywhere to the Colab values, and the gap to
XGBoost became 1.00 percentage points (was 1.12). If a score moves
between runs, find out why before choosing which value to print, and
print the value from the submitted notebook.

### The feature engineering that did not help

Feature engineering was tested and did not help: cross-validated accuracy
was 0.6224 with the new features and 0.6239 without them. The features
were left out, and slide 7 says so in one line. A negative result is
still a result. Never claim a method helped when the numbers say it did
not.

### The margin of error

Accuracy on 30,000 test customers carries a margin of error of about
plus or minus 0.55 percentage points (half the width of the 95%
interval). The deck prints it next to the model scores, and the gap
between XGBoost and Random Forest (1.00 points) is read against it. A
gap smaller than the margin of error is not a meaningful difference.

### The derived arithmetic gap

The deck standard for handsets 300 days or older is 56.3% churn
(n=60,073) against 39.5% for younger handsets (n=39,926), while the
30-day band figures are 37.4% (270 to 300 days) and 60.3% (300 to 330
days). The gap between the band figures is 22.9 points. The band figures
and the group figures come from different cuts of the same data and do
not have to reconcile to the same gap. When two numbers on a slide look
inconsistent, check whether they are different cuts before calling one
of them wrong.

### The rank values shown as ranks

Slide 8 shows permutation importance of refurbished or new handset as
rank 62 with value 0.0004. The rank is the finding, not the value. The
notebook-vs-deck checker flagged such cases; they were reviewed one by
one and kept by design. A checker flag is a prompt to look, not an order
to change.

### The two counts that differ by 0.1%

The offer target is 50,980 customers (scaled from test data) while the
direct count of segments P1 and P2 is 50,917. The difference is 63
customers, 0.1%, and it is sampling variation. The deck uses 50,980 with
a footnote on slide 10. Small mismatches with a known cause get a
footnote, not a silent fix.

## The verified-numbers sheet

Keep one sheet of verified numbers for the deck. In the GCI build it
lives inside `scripts/check_numbers_final.py` as `SHEET`, in dot-decimal
notation. Every number on a slide must appear in the sheet as the value,
times 100, or divided by 100. Numbers that are slide numbers, step
numbers, or small counts (0 to 15, plus 100 for a 100% bar) are allowed
by rule. Add a number to the sheet only after checking it against its
source. The sheet is the single place where a new number is approved.

## The checker: scripts/check_numbers_final.py

Three checks, run on the Indonesian and English deck text:

1. **ID-EN parity.** Numbers per slide must be identical between the two
   languages (Indonesian notation 1.729.464 and 0,6357; English notation
   1,729,464 and 0.6357). A mismatch means a translation dropped or
   changed a number.
2. **Sheet membership.** Every number in the slide body must be in the
   verified sheet. Reference lines are compared but not checked against
   the sheet, because reference titles may carry numbers from their
   sources.
3. **Style bans.** No banned number strings, no em-dash, no en-dash, no
   emoji, no banned AI words (delve, furthermore, moreover, leverage,
   leveraging, cutting-edge, robust, seamless, pivotal, utilize,
   gradient), no mention of the font Inter, no spaced hyphen that looks
   like a dash.

The checker must report **Total masalah: 0** (zero problems). Fix the
text, not the checker. The checker also prints slide title lengths as a
ghost-deck test: flag any title longer than 150 characters.

## The notebook-vs-deck check

When a notebook exists, run a second check that compares the notebook
outputs with the deck text, using `scripts/check_notebook_vs_deck.py`
(adapt its paths and its `CHECKS` list to the new deck). In the GCI build
it reported 51 PASS and 9 FAIL, with all 9 in
known harmless categories: notebook-only values, a derived arithmetic
gap of 22.9 points, and rank values shown as ranks on slide 8 by design.
Record the harmless categories in writing. A FAIL with no written reason
is an open defect.

## Rules for writing numbers on slides

- Write the number, the unit, and the base together ("37.4% for handsets
  aged 270-300 days", not "37.4%").
- State the denominator next to a rate ("n=60,073") at least once per
  exhibit.
- Label every assumption next to the result it feeds. The profit slide
  in the GCI deck carries its assumptions in a band attached to the
  chart: customer value USD 58.21 a month, 50,980 customers offered, USD
  10 per offer (USD 509,800 total), 12-month stay.
- Present an unmeasurable quantity as scenarios, never as one number.
  The save rate cannot be estimated from the GCI data (no treated group,
  no control group), so the deck shows 10%, 20%, and 30% scenarios with
  break-evens at 2.3%, 4.6%, and 9.1% for 12, 6, and 3 month stays.
- Never compare rates with different definitions. Komdigi reported churn
  falling from about 20% to 2.8% in Q3 2026, but its definition is
  unpublished, so the deck does not compare it with the 49.6% dataset
  figure.
