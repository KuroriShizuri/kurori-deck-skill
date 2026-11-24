# Worked example: Company A telecom churn

The deck this skill was built from. All numbers below come from
`examples/content-en.md`, the final English deck text. Exact slide wording
is in that file; this page summarizes the case and the numbers so a new
deck can see what a finished example looks like.

## The case

Company A is a mobile operator with 99,999 customers in two source files
(`Client.csv`, `Record.csv`, dated 2022) from the course tutorial. The
dataset is anonymized and published for teaching. Company A itself is
anonymous. Indonesia is used only as a reference market, and the model
results are not claimed to represent Indonesian customers. The business
question, in one sentence: "Which customers are about to leave Company A,
and what should we do about it before they do?"

The dataset covers 25 features and 99,999 customers. Churn is 49,562
customers, 49.6%. The model answers one question: will this customer
leave? The answer drives one action: offer a handset upgrade and
retention offer to the customers the model flags.

## The numbers that drive the deck

### Dataset limits (slide 4)

- 342,969 missing values across 12 of 25 features. 73.3% of rows have at
  least one missing value. Only 26,705 rows are complete.
- Handset age (eqpdays) is negative for 133 customers (down to -5 days),
  a data defect that was kept and flagged, not silently fixed.
- Missing values were not imputed with the mean and were not deleted.
  Rows were not dropped. The pipeline uses built-in missing handling and
  native categorical encoding.
- The 49.6% churn rate applies only to this dataset. It must not be
  compared with operator churn rates from market sources.

### The 300-day churn cliff (slide 5)

Churn by 30-day handset-age bands: 40.0%, 43.1%, 37.5%, 37.3%, 61.0%,
58.1%, 52.7%, 53.3%, 54.4%, 58.3% (bands from 180-210 days to 450-480
days). The cliff sits between 270-300 days (37.4%) and 300-330 days
(60.3%): a gap of 22.9 percentage points. Below 300 days: n=39,926,
churn 39.5%. At or above 300 days: n=60,073, churn 56.3%. The same
cliff appears when handset age is measured in months: 37.4% for 9 months
versus 60.3% for 10 months. Device age correlates with contract length
(0.483) and with price (-0.478), so the cliff is not a pure handset
effect. The deck says this plainly.

### Risk segments (slide 6)

- P1 (renewal plus high risk): handset 10 months or older, n=17,117,
  churn 0.636, revenue USD 78.55 a month.
- P2 (retention only): handset under 10 months, n=33,800, churn 0.625,
  revenue USD 45.72 a month.
- Rest: n=49,083, churn 0.357.
- P1 plus P2 is 50,917 customers, 50.9% of the dataset, and captures
  64.7% of churners in the test data. The price quartile pattern: the
  cheapest quartile churns 57.5%, the most expensive 41.0%. The offer
  target on the proposal slides is 50,980 customers (test-scaled), 63
  more than the direct count of 50,917; the footnote explains the 0.1%
  difference.

### Model comparison (slide 7)

All models on the same split: 69,999 train, 30,000 test. Accuracy and
AUC, plus precision and recall for the chosen model:

| Model | Accuracy | AUC |
|---|---|---|
| XGBoost | 0.6357 | 0.6938 |
| Random Forest | 0.6257 | 0.6785 |
| Logistic Regression | 0.5961 | 0.6295 |
| Majority class | 0.5044 | 0.5000 |

XGBoost precision 0.6288, recall 0.6468. Calibration error (ECE)
0.0052. Margin of error on accuracy is about plus or minus 0.55
percentage points on 30,000 test customers. The gap between XGBoost and
Random Forest is 1.00 points. Feature engineering did not help:
cross-validated accuracy 0.6224 with the new features against 0.6239
without them, so the features were left out and the slide says so.

### What drives churn (slide 8)

XGBoost gain rank and permutation rank differ, and the slide shows both.
Handset age: gain rank 1 (43.2), permutation rank 2 (0.0229). Months
with company: gain rank 2 (33.3), permutation rank 1 (0.0313).
Refurbished or new handset: gain rank 3 (29.1), permutation rank 62
(0.0004). The slide's point: what the model uses to score is not what a
business can change. Only two levers are intervenable: handset renewal
(renewal cuts churn 13.5 points, odds ratio 1.227 per standard-deviation
step) and network experience (dropped calls and customer-care calls,
which the data show but cannot price).

### The proposal (slides 9 to 12)

- Proposal 1, handset renewal program: upgrade 19,000 customers on
  handsets aged 10 months or more, free new handset, trade in the old
  one, 12-month contract.
- Proposal 2, targeted retention offer: 32,000 customers on handsets
  under 10 months get a one-off retention offer; three options are
  offered so the customer chooses, and the offer runs before the 300-day
  cliff.
- How it works: score weekly with XGBoost, target with the rules above,
  act through the retention team, monitor weekly and review monthly.
- Expected impact at a customer value of USD 58.21 a month, 50,980
  customers offered, USD 10 per offer (USD 509,800 total), 12-month
  stay: save 10% gives plus USD 1,729,464; save 20% gives plus USD
  3,968,727; save 30% gives plus USD 6,207,991. Break-evens: 2.3% for a
  12-month stay, 4.6% for 6 months, 9.1% for 3 months. The save rate
  cannot be estimated from the data (no treated group, no control
  group), so it is shown as scenarios, never as one number.

### Quotation (slide 13)

First-year service fee USD 144,000: 140 person-days at USD 600 a day
(USD 84,000) plus support at USD 5,000 a month for 12 months (USD
60,000). The client keeps the data and the models; the fee covers one
year of maintenance and support only.

### Reference market (slide 2)

Indonesia, three operators, verified by opening each source:

- PwC: operator revenue USD 17 to 18 billion in 2025, about 97%
  prepaid.
- Komdigi: about 297 million active subscribers, Q3 2026. Churn
  reported falling from about 20% to 2.8% in Q3 2026; the definition is
  unpublished, so it is never compared with the 49.6% dataset figure.
- Indosat: 91.5 million subscribers, Q3 2026, ARPU Rp46,000.
- XLSmart: 70 million subscribers, Q3 2026, ARPU Rp47,500.
- Telkomsel: 157.6 million subscribers, September 2025.
- GSMA: global handset holding about 3.5 years.

## Slide map

| # | Topic | Key figure |
|---|---|---|
| 1 | Cover | 22.9 point churn cliff, plus USD 6.2 million at 30% saved |
| 2 | Reference market | USD 17 to 18 billion, 297 million subscribers, 97% prepaid |
| 3 | Business question | 49.6% churn in this dataset |
| 4 | Dataset limits | 73.3% of rows have at least one missing value |
| 5 | The 300-day cliff | 37.4% to 60.3%, gap 22.9 points |
| 6 | Risk segments | P1 plus P2 capture 64.7% of test churners |
| 7 | Model comparison | XGBoost 0.6357 accuracy, 0.6938 AUC |
| 8 | What drives churn | Handset age gain 43.2, renewal odds ratio 1.227 |
| 9 | Proposal 1 | Renew 19,000 handsets aged 10 months or more |
| 10 | Proposal 2 | Offer 32,000 customers before the cliff |
| 11 | How it works | Score weekly, target, act, monitor |
| 12 | Expected impact | Plus USD 1,729,464 to plus USD 6,207,991 |
| 13 | Quotation | USD 144,000 first-year service fee |
| 14 | Conclusions | Three findings and the decision requested |
| 15 | References | 13 sources plus the AI session URL |

## Verification record of this deck

- Checker (`check_numbers_final.py`): zero problems.
- Notebook versus deck check: 51 PASS, 9 FAIL, all 9 in known harmless
  categories (notebook-only values, the derived 22.9 point arithmetic
  gap, rank values shown as ranks on slide 8 by design).
- Render gate: 15 pages, no overflow, no broken images, vertical fill
  98% on every slide.
- PDF validation: PASS, 15 pages, 960 by 540 pt, only Source Sans 3
  embedded.
- The final PDF: 1,787,465 bytes, 15 pages, md5
  `c6a329fa456a3876792223774dcb3d30`.
- The finished package (PDF, notebook, references) was delivered to the
  author on 23 November 2026. Upload to Omnicampus was the author's
  action, due 28 November 2026 18:30 WIB.
