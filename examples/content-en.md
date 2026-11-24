# Deck v2: GCI World 2026 Final Assignment (Company A, telecom churn)

Short blueprint (workflow steps 1 to 3)
- Goal: convince Company A executives that a targeted retention program deserves a pilot with a control group.
- Audience: executives without an ML background. One idea per slide, one exhibit per results slide.
- Key message: churn jumps sharply once a handset reaches 300 days of age, the model is good enough to prioritize customers, the program breaks even at a low save rate, but the save rate is unproven.
- Story flow: hook (1-2), problem (3-4), insight (5-8), solution (9-12), cost (13), conclusions (14), references (15).

### Slide 1
Title: Customers leave sharply once handsets reach 300 days, and a retention offer breaks even if it keeps 2.3% of those who would leave (12-month stay assumption)
Composition: Layout catalog (350), category 08, number 335 (title slide). Archetype: a small navy-duotone telecom tower photo tab on the left, navy panel behind, text column shifted right, one soft gold block in the text column. Reason: a calm opening that states both thesis numbers at once, and the soft gold block marks the one number to remember.
Exhibit: none. A title slide carries no chart. A telecom tower photo, cropped and recolored to navy duotone, sits as a small tab on the left. Photo: Väinö Parjanen / Pexels [13].
Content:
- A data-driven proposal for Company A, an anonymous telecom operator.
- Churn means that a customer leaves 31-60 days after the observation date. Save rate means the share of customers who would have left and are kept by the offer.
- Reference market: Indonesia, used only as a market backdrop. The model results are not claimed to represent Indonesian customers.
- GCI World 2026 Final Assignment | Rajendriya
- Soft gold block: Breaks even at a 2.3% save rate (12-month stay assumption)
Footnote: none. The reference-market sentence moved to the body.

### Slide 2
Title: The Indonesian reference market has about 297 million active subscribers, and about 97% of them are prepaid, so customers can switch easily
Composition: Layout catalog (350), category 08, number 338 (two content). Archetype: 35/65 vertical split, a navy panel with three figures, a white side with the chart. Reason: the market context reads at a glance through three figures, and the operator chart supports them.
Exhibit: Navy panel with three figures: 297 million active subscribers (Q3 2026, Komdigi [2]), 97% prepaid (PwC [1]), USD 17-18 billion telecom revenue in 2025 (PwC [1]). Horizontal bar chart of subscribers per operator: Telkomsel 157.6 million (Sep 2025) [7], Indosat 91.5 million (Q3 2026) [4], XLSmart 70 million (Q3 2026) [5]. Each bar carries its own date and citation marker. Annotation: Largest operators, using the subscriber counts each one reports. Operator figures use different dates and definitions, so they do not add up to the 297 million Komdigi figure.
Content:
- Telecom revenue in 2025 was about USD 17-18 billion (PwC) [1].
- Active mobile subscribers in Q3 2026 were about 297 million according to Komdigi (Indonesia's digital ministry) [2], and about 97% are prepaid [1].
- ARPU (average monthly revenue per user) in Q3 2026 was Rp46,000 at Indosat [4] and Rp47,500 at XLSmart [5], in Indonesian rupiah.
- Globally, people keep a handset for about 3.5 years on average, much longer than the 300 days at which churn jumps in our data [6].
- Boundary: Company A is anonymous. Indonesia is only a reference market, and the model results are not claimed to represent Indonesian customers.
Footnote: [1] PwC Indonesia, Jun 2026. [2] Kompas, 13 Nov 2026 (Komdigi statement). [3] Biometric Update, Nov 2026. [4] Counterpoint, Nov 2026 (Indosat). [5] Investing.com, Nov 2026 (XLSmart). [6] GSMA, Jun 2026. [7] PT Telkom Indonesia, Nine Months of 2025 Results (Unaudited), 2025. Full URLs on slide 15. Boundary: Company A is anonymous. Indonesia is only a reference market, and the model results are not claimed to represent Indonesian customers.

### Slide 3
Title: We predict which customers will churn 31-60 days after the observation date, so the business has time to act before day 31
Composition: Layout catalog (350), category 08, number 346 (timeline page). Archetype: full-bleed navy, one question in the center, a timeline below. Reason: the problem-definition slide should make the audience read one business question before seeing any data.
Exhibit: Horizontal timeline: day 0 (observation date, the date we look at each customer; the model scores each customer's risk on day 0), action window (days 0-30: the business acts), day 31 (the churn window opens), churn window days 31-60 (the target is 1 if the customer leaves here). Only the churn window gets a soft gold block. Two figures below the timeline: 30,000 test customers for accuracy and AUC (customers the model had not seen), 100,000 Company A customers in the data.
Content:
- Business question: which customers will churn, and which factors can the business change before that happens?
- About 97% of subscribers are prepaid (PwC [1]), so customers can switch easily.
- For each customer, the model answers yes or no: will this customer leave 31-60 days after the observation date?
- 30,000 test customers for accuracy and AUC (customers the model had not seen).
- 100,000 Company A customers in the data.
Footnote: Churn definition: Company A Dataset Overview [8]. AUC is explained on slide 7. Business value is computed separately on slide 12.

### Slide 4
Title: Two limits on the data: 49.6% churn applies only to this dataset, and only 26,705 of 100,000 rows are complete
Composition: Layout catalog (350), category 08, number 344 (big number page). Archetype: the very large figure 49.6% as the focus, a band of four figures above, two limit groups below. Reason: the two numeric facts most often misread sit in one composition with the largest visual weight.
Exhibit: Typographic figure 49.6% on a soft gold panel with navy text, captioned 'Churn in the 31-60 day window, in this dataset only.' Two groups below: Limit 1: the 49.6% figure (right) and Limit 2: incomplete data (left, under the gold panel). Band of four figures above: 100,000 customers, 342,969 missing values, 73.3% of rows with at least one missing value, 26,705 complete rows.
Content:
- Two files are joined on Customer_ID: Client.csv (account, device, demographics) and Record.csv (usage, billing, call quality, churn target).
- 342,969 values are missing: 73.3% of rows have at least one missing value.
- Handset age (eqpdays) is negative for 133 customers, down to -5 days: we treat it as a data error.
- 49.6% of customers in the dataset churn in the 31-60 day window after observation. This figure applies only to this dataset, and we do not use it as the basis for impact calculations.
- Customers who leave and customers who stay are nearly balanced. A model that always guesses 'stays' reaches 0.5044 accuracy (AUC 0.5000, a coin flip). That is the yardstick for the models on slide 7.
- Komdigi reports churn fell from about 20% to 2.8% in Q3 2026 [3], but its definition is unpublished, so we do not compare it with the 49.6% in our data.
- Financial impact is computed from the number of customers offered and the save rate (slide 12).
Footnote: Author analysis of Client.csv and Record.csv [8][9].

### Slide 5
Title: Churn jumps from 37.4% for handsets aged 270-300 days to 60.3% for handsets aged 300-330 days, a gap of 22.9 percentage points
Composition: Layout catalog (350), category 08, number 349 (data chart page). Archetype: full-bleed navy, a chart with inverted colors (white bars), a soft gold block as the annotation. Reason: this is the main finding, so it gets the densest background and one large chart.
Exhibit: Bars for 10 equal-sized customer groups by handset age (eqpdays), bar height is the churn rate: 40.0%, 43.1%, 37.5%, 37.3%, 61.0%, 58.1%, 52.7%, 53.3%, 54.4%, 58.3%. A vertical line between deciles 4 and 5. Soft gold callout: Zoom on 30-day age bands. 270-300 days: 37.4%. 300-330 days: 60.3%. Gap: 22.9 percentage points. Axis label: 10 equal-sized customer groups, youngest to oldest handsets.
Content:
- Handsets younger than 300 days: 39.5% churn (39,926 customers). Handsets 300 days old or older: 56.3% (60,073 customers).
- The shape is a step, which we call the 300-day cliff. After the jump, churn stays between 52.7% and 61.0% across customer groups 5 to 10. In narrower 30-day age bands, the 330-360 day band shows 62.4%.
- We do not yet know why. A jump this sharp looks more like a business rule (for example contract end or upgrade eligibility) than gradual device aging. This is a hypothesis we have not tested.
Footnote: One customer has no handset-age record, so the two groups add to 99,999, not 100,000 [9].

### Slide 6
Title: Two risk segments hold 64.7% of the customers who leave, and P1 is the higher-value one (USD 78.55 a month)
Composition: Layout catalog (350), category 08, number 348 (matrix page). Archetype: a Marimekko chart at 65% width and a definition rail at 35% on the right. Reason: column width shows segment size and height shows churn, so two dimensions read at once.
Exhibit: Marimekko. Column width is customer count (P1 17,117, P2 33,800, Rest 49,083). Height is churn rate (63.6%, 62.5%, 35.7%). P1 soft gold, P2 navy, Rest gray. Monthly revenue is written in the columns (USD 78.55 and USD 45.72). Annotation: P1 churn is almost the same as P2 (63.6% vs 62.5%). Legend: column width = number of customers. Column height = share who churn.
Content:
- P1: high risk (model score of 0.5 or more), handset 300 days old or older, revenue of USD 48.20 a month or more (currency assumed to be USD). It has 17,117 customers (17.1%), churn 63.6%, and revenue of USD 78.55 per month.
- P2: high risk, not in P1. It has 33,800 customers (33.8%), churn 62.5%, and revenue of USD 45.72 per month.
- All other customers (49,083), churn 35.7%.
- P1 and P2 together are about half of all customers, yet hold nearly two-thirds of the customers who leave (64.7% in the test data). P1 starts exactly at the 300-day cliff, so the segment and the churn jump line up. Customer counts use all 100,000 customers. The 64.7% is measured on the 30,000 test customers.
Footnote: Author analysis [9].

### Slide 7
Title: Our best model (XGBoost) is right for about 6 of 10 customers and beats Random Forest by 1.00 percentage points
Composition: Layout catalog (350), category 08, number 339 (comparison page). Archetype: a dot plot on the left and a how-to-read card on the right. Reason: executives need to know what accuracy means, and a dot plot shows uncertainty that a table hides.
Exhibit: Dot plot of accuracy for four models with a margin-of-error band of about ±0.55 percentage points, plus an AUC column as numbers. Reference line at 0.5044. Annotation: XGBoost vs Random Forest, a gap of 1.00 percentage points. Soft gold chip: Useful for ranking customers, not for certainty. A text line under the chart lists all accuracy (AUC) scores, followed by a short note on why each model was chosen.
Content:
- Accuracy (AUC): majority guess 0.5044 (0.5000), Logistic Regression 0.5961 (0.6295), Random Forest 0.6257 (0.6785), XGBoost 0.6357 (0.6938).
- About the models: Logistic Regression is a simple, explainable baseline. XGBoost and Random Forest combine many decision trees and can capture step-like patterns such as the jump at 300 days. All three were trained on the same 70,000 customers and tested on the same 30,000.
- Main model: XGBoost (accuracy 0.6357, AUC 0.6938). Soft gold chip: Useful for ranking customers, not for certainty. About 6 of 10 customers are predicted correctly.
- How to read AUC: AUC measures how well the model ranks likely leavers above likely stayers. A score of 0.5000 is a coin flip.
- The margin of error on accuracy is about ±0.55 percentage points. The gap to Random Forest is 1.00 percentage points.
- Scores are well calibrated (calibration error ECE 0.0052).
- The extra features we built did not help. Accuracy in internal cross-checks was 0.6224 with them and 0.6239 without, so we left them out.
Footnote: All models use the same 30,000 test customers. Accuracy from internal cross-checks is not directly comparable with test accuracy [9].

### Slide 8
Title: Handset age and tenure rank first and second on both importance measures, while customer care ranks 53 and 45
Composition: Layout catalog (350), category 08, number 342 (content with caption). Archetype: a rank chart at 60% on the left, four stacked evidence cards on the right, separated by thin navy rules. Reason: importance alone misleads, so ranks and directional evidence sit side by side.
Exhibit: Rank dot plot (1 is top): for each feature one dot for gain rank and one dot for permutation rank. Handset age (gain 1, permutation 2), tenure (gain 2, permutation 1), refurbished or new handset (gain 3, permutation 62), dropped voice calls (permutation 6, gain 18), customer care calls (gain 53, permutation 45). Features the business can change (handset age, dropped voice calls) are soft gold.
Content:
- Gain: how much the model relies on a feature. Permutation: how much accuracy drops when the feature is scrambled.
- Gain: handset age (43.2) ranks 1, tenure ranks 2, and refurbished or new handset (29.1) ranks 3, but refurbished or new handset ranks 62 on permutation (0.0004).
- Permutation: tenure ranks 1, handset age ranks 2, and dropped voice calls (0.0106) rank 6, but dropped voice calls rank 18 on gain.
- Handset age moves together with tenure (correlation 0.483) and handset price (-0.478), so we also tested it with related factors held fixed. It stays the strongest predictor, and each typical step up multiplies the odds of churn by 1.227.
- Price also matters: the cheapest quarter of handsets churns at 57.5% and the most expensive quarter at 41.0%.
- Customer care calls show almost no link to churn in our model: rank 53 (gain) and 45 (permutation). Customers who leave call customer care less often (1.60 calls on average vs 1.98 for customers who stay).
- What the business can change: handset age and call quality (dropped voice calls). The business cannot change tenure.
- Importance values use their own units and are not comparable across types, and importance does not prove cause and effect.
Footnote: Author analysis [9].

### Slide 9
Title: Proposal 1 offers a new handset to the 17,117 high-value customers whose handsets have reached the 300-day cliff, where churn is 63.6%
Composition: Layout catalog (350), category 08, number 343 (image with caption). Archetype: a horizontal ruler in the top third, four text blocks below, and a tall side photo on the right. Reason: the ruler shows that the P1 threshold falls exactly on the 300-day cliff, so the trigger and the segment boundary are the same.
Exhibit: Handset age ruler with markers at 270, 300, 330, and 360 days. Ruler annotation: P1 is 17,117 of the 60,073 customers 300 days old or older (those who also have risk of 0.5 or more and revenue of USD 48.20 or more). A navy line at 300 days. A soft gold block at 300 days: P1 starts here. A tall side photo on the right shows two hands passing a phone from one to the other, recolored to navy. Photo: Ron Lach / Pexels [10].
Content:
- Target: Segment P1 (handset age of 300 days or more, model risk score of 0.5 or more, revenue of USD 48.20 or more). The segment has 17,117 customers with revenue of USD 78.55 per month.
- Action: offer handset replacement, through subsidy or trade-in, matched to customer value.
- Evidence: handset age is still the strongest predictor after accounting for related factors such as tenure, handset price, revenue, and usage. Churn rises 22.9 percentage points past 300 days.
- Limits: correlation is not cause, so replacing handsets may not remove the jump. The subsidy cost per handset is not estimated. Handset price also matters: the cheapest quarter of handsets churns at 57.5%, the most expensive quarter at 41.0%.
Footnote: Author analysis [9].

### Slide 10
Title: Proposal 2 sends a USD 10 retention offer to the 50,980 customers with an even or higher chance of leaving
Composition: Layout catalog (350), category 08, number 338 (two content). Archetype: a 40% navy panel on the left with the cost equation, four white text blocks on the right, and a photo inside the bottom of the navy panel. Reason: the cost follows directly from the customer count, so it gets its own panel.
Exhibit: Cost equation: 50,980 customers x USD 10 per offer = USD 509,800. The total sits in a soft gold block with navy text. The cost follows directly from the count: 50,980 customers x USD 10 per offer = USD 509,800. The USD 10 per offer is an assumed campaign cost. A photo inside the navy panel shows a woman using a smartphone at a cafe, recolored to navy. Photo: Hanna Pad / Pexels [11]. A two-row reach-versus-capture chart fills the bottom-right void: row 1 'Customers who get the offer', 50,980 of 100,000 (slate teal bar); row 2 'Leavers in that group (test data)', 64.7% of leavers (navy bar). Caption: About half of customers hold nearly two-thirds of those who leave.
Content:
- Target: all 50,980 customers with a score of 0.5 or more. This group covers Segment P1 and Segment P2 (P2: 33,800 customers, churn 62.5%, revenue USD 45.72).
- Action: send each customer a retention offer worth USD 10. This value is an assumed campaign cost.
- Evidence: the model's scores match real churn rates closely (calibration error ECE 0.0052). P1 and P2 hold 64.7% of the customers who leave in the test data.
- Limits: the save rate cannot be estimated from this data. Some customers who get the offer would have stayed anyway. The cost of those offers is included in the total.
- P1 and P2 add up to 50,917, which differs from 50,980 by about 0.1%. This does not change any result.
Footnote: The USD 10 per offer cost is a labeled assumption [9].

### Slide 11
Title: Every customer is scored, the 50,980 who score 0.5 or more get an offer, and a pilot with a control group measures the save rate
Composition: Layout catalog (350), category 08, number 347 (process flow page). Archetype: a horizontal four-step flow with a stepped baseline. Reason: the order of decisions is the content of this slide, and the steps descending to the right show the filtering.
Exhibit: Flow diagram: (1) XGBoost risk score for 100,000 customers, (2) a 0.5 cut-off selects 50,980 customers, (3) every selected customer gets the USD 10 retention offer and P1 customers also get the handset replacement offer, (4) a pilot with a control group measures the save rate. A soft gold block only on step 4: the save rate is unknown. Below the flow, the four columns continue: a funnel under steps 1-2 (100,000 scored, 50,980 selected at cut-off 0.5, 17,117 also get the handset offer), the calibration sentence, and the cut-off card; a near-square photo tile under step 3 shows a customer at a phone-shop counter, recolored to navy; a pilot diagram under step 4 splits the selected customers into an offered group and a control group (slate teal), and comparing churn in the two groups gives the save rate. Photo: Sami Abdullah / Pexels [12].
Content:
- Step 1: the model gives every customer a risk score. 100,000 customers scored.
- Step 2: customers with a score of 0.5 or more enter the offer list. 50,980 selected.
- Step 3: every selected customer gets the USD 10 retention offer. P1 customers (17,117) also get the handset replacement offer.
- Step 4: a pilot with a control group measures the save rate, a figure we cannot estimate from this data. The save rate is not yet known.
- We start at 0.5 as a cautious cut-off (threshold). Under the slide 12 assumptions, a lower cut-off could earn more if the save rate is the same for all customers. We set the final cut-off after the pilot.
- Scores are well calibrated (ECE 0.0052), so a score can be read as the chance of churn.
Footnote: Calibration is computed on test data [9].

### Slide 12
Title: If the offer keeps 10% of those who would leave, the program nets USD 1,729,464 in 12 months (before handset and service-fee costs)
Composition: Layout catalog (350), category 08, number 349 (data chart page). Archetype: a page-wide line chart with a navy assumptions band along the bottom. Reason: assumptions must always be visible next to results, so the band is attached to the chart.
Exhibit: Line chart: x axis save rate, y axis net result (USD), for a 12-month stay period. Three labeled scenario points: 10% (+USD 1,729,464), 20% (+USD 3,968,727), 30% (+USD 6,207,991). A soft gold diamond with a navy outline marks the 2.3% break-even point on the chart. A break-even panel beside the chart lists the break-even save rate by stay period: 2.3% (12 months), 4.6% (6 months), 9.1% (3 months), with a navy 10% reference line and the formula: net result = customers saved x USD 58.21 a month x months of stay, minus USD 509,800.
Content:
- Assumptions: customer value of USD 58.21 per month, 50,980 customers offered, a cost of USD 10 per offer (USD 509,800 in total), and a 12-month stay period.
- A 10% save rate gives a net result of +USD 1,729,464, 20% gives +USD 3,968,727, and 30% gives +USD 6,207,991.
- Break-even is a 2.3% save rate with a 12-month stay. It rises to 4.6% with a 6-month stay and to 9.1% with a 3-month stay.
- Our data has no group that received the offer and no comparison group that did not, so the save rate cannot be estimated from this data. The 10%, 20%, and 30% figures are scenarios. These results exclude the handset replacement cost and the USD 144,000 service fee.
- Company A's customer value (USD 58.21 a month) is about 23 times Indosat's revenue per customer (about USD 2.54 a month [4]), so the dollar figures do not transfer directly to the Indonesian market.
Footnote: All dollar figures are labeled assumptions [9]. The 49.6% dataset figure is not used in this calculation.

### Slide 13
Title: The indicative first-year service fee is USD 144,000: 140 person-days at USD 600 a day, plus support of USD 5,000 a month
Composition: Layout catalog (350), category 08, number 336 (title and content). Archetype: full-bleed navy with a cost table, the total in a soft gold block on the right. Reason: a quotation is a commercial document, so a plain table fits better than an illustration.
Exhibit: Four-row table: day rate USD 600 per day, implementation 140 person-days (USD 84,000), support USD 5,000 per month for 12 months (USD 60,000), first-year total USD 144,000 (soft gold block). Below it a list of the proposed scope.
Content:
- Day rate: USD 600 per day.
- Implementation: 140 person-days (USD 84,000).
- Support: USD 5,000 per month for 12 months (USD 60,000).
- First-year total: USD 144,000.
- Proposed scope: risk scoring pipeline, pilot design with a control group, save rate measurement, operational support.
- For comparison, the 10% save rate scenario nets USD 1,729,464 before the service fee.
- Indicative quote: rates and days are planning assumptions until the scope is agreed.
Footnote: none. The indicative-quote sentence is in the body.

### Slide 14
Title: Handset age of 300 days or more is the strongest churn signal the business can act on, and a pilot decides whether to scale up
Composition: Layout catalog (350), category 08, number 337 (section title page). Archetype: full-bleed navy with three numbered findings and one soft gold block holding the recommendation. Reason: the skill rule asks the deck to end on conclusions.
Exhibit: none.
Content:
- Finding 1: churn rises 22.9 percentage points once a handset reaches 300 days.
- Finding 2: the model is good enough to rank customers by risk (accuracy 0.6357, AUC 0.6938), but not to be certain about any one customer.
- Finding 3: the program breaks even at a 2.3% save rate (12-month stay period), but the save rate is unproven.
- Soft gold block: Decision requested: approve a pilot with a control group to measure the save rate, then set the final cut-off.
Footnote: All financial impact is an assumption-based scenario (slide 12).

### Slide 15
Title: Market figures come from the public sources below, and all model figures come from our analysis of Company A data
Composition: Layout catalog (350), category 08, number 338 (two content). Archetype: a two-column list in small type, no soft gold. Reason: a references slide should be tidy and readable, with no element competing with the content.
Exhibit: none.
Content:
- [1] PwC Indonesia, Indonesia telecommunications sector overview and market update, Jun 2026. https://www.pwc.com/id/en/pwc-publications/industries-publications/tmt/indonesia-telecom-market-outlook.html
- [2] Kompas, Exceeding Target, 41.49 Million Users Have Registered for Biometric SIM Cards, 13 Nov 2026. https://go.kompas.com/read/2026/11/13/132446674/exceeding-target-4149-million-users-have-registered-for-biometric-sim-cards
- [3] Biometric Update, Indonesia surpasses 2026 biometric SIM target with 41M registrations, Nov 2026. https://www.biometricupdate.com/202611/indonesia-surpasses-2026-biometric-sim-target-with-41m-registrations
- [4] Counterpoint Research, Indosat Q3 2026 Revenue Grows 11.1%, Nov 2026. https://counterpointresearch.com/en/insights/indosat-q3-2026-revenue-grows
- [5] Investing.com, XLSMART Q3 2026 slides: record ARPU, integration nears completion, Nov 2026. https://www.investing.com/news/company-news/xlsmart-q3-2026-slides-record-arpu-integration-nears-completion-93CH-5034927
- [6] GSMA, Mobile Device Circularity Key Facts and Figures, Jun 2026. https://www.gsma.com/solutions-and-impact/connectivity-for-good/external-affairs/wp-content/uploads/2026/06/Mobile-Device-Circularity-Factsheet.pdf
- [7] PT Telkom Indonesia, Nine Months of 2025 Results (Unaudited), 2025. https://aro.telkom.co.id/minio/show/data/lampiran/1761838522183_original_TLKM-9M25-Info-Memo.pdf
- [8] GCI World 2026, Company A Dataset Overview and tutorial notebook.
- [9] Author analysis of Client.csv and Record.csv (attached notebook).
- [10] Ron Lach, Two people exchanging a green mobile phone against a solid green background, Pexels, 4 Oct 2021. https://www.pexels.com/photo/9786072/. Photo of two hands passing a phone from one to the other, recolored to navy, slide 9.
- [11] Hanna Pad, Woman Using Mobile Phone, Pexels, 18 Apr 2021. https://www.pexels.com/photo/woman-using-mobile-phone-7550823/. Photo of a woman using a smartphone at a cafe, recolored to navy, slide 10.
- [12] Sami Abdullah, A customer examines smartphones in a modern Istanbul gadget store, Pexels, 24 Jul 2022. https://www.pexels.com/photo/12968298/. Photo of a customer at a phone-shop counter, recolored to navy, slide 11.
- [13] Väinö Parjanen, Antenna Tower Under the Blue Sky, Pexels, 5 Aug 2021. https://www.pexels.com/photo/9073180/. Cover photo, cropped and recolored to navy duotone (#14467C to white).
- Generative AI tools were used for discussion and drafting. Chat history URL: https://app.kiro.dev/session/dff20d50-6c54-498c-aabe-d83d6b1b1d6b.
Footnote: Direct quotation makes up less than 40% of the slide text.
