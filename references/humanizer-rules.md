# Humanizer rules

The language pipeline of the GCI deck, condensed from two skills. The
skills themselves are separate projects and are not bundled here. Install
them from their own repos when you want the full pipeline. This file
summarizes their rules tightly enough to follow the pipeline by hand, and
records the two cautions the GCI build learned.

## The pipeline

```
Indonesian draft (content-id.md)
        |
        v
humanizer-indonesia  (v1.7.2)   remove AI tells + translationese
        |
        v
English translation (content-en.md)
        |
        v
academic-humanizer   (v0.3.3)   remove AI tells, keep scholarly voice
        |
        v
check_numbers_final.py          (numbers unchanged by either pass)
```

Rules that hold for both passes: never change a number, a result, or a
citation. Never invent evidence. Human editing after the pass stays
mandatory. The skill output is a draft for a human to edit, not finished
prose.

## English pass: academic-humanizer (AIScientists-Dev, MIT, v0.3.3)

From NSF CAREER and NIH R01 funded researchers. Six layers, audit first
then rewrite. Apply to English academic prose and to deck prose. Never
use it to evade AI-use disclosure.

### Layer 1: general AI-tell catalog

Remove inflated significance ("marking a pivotal moment"), superficial
"-ing" tails ("..., highlighting..."), promotional or figurative language
("rich", "vibrant", "groundbreaking"), vague attributions ("experts
argue" with no cite), AI vocabulary (delve, underscore, intricate,
tapestry, testament, landscape in the abstract sense, pivotal, showcase,
foster, leverage as filler, realm, seamless), copula avoidance ("serves
as" becomes "is"), negative parallelisms ("not just X, but Y"), rule of
three padding, elegant variation (cycling synonyms for one referent),
filler ("it is worth noting that", "in order to"), overlong
clause-stacked sentences (split them), and em-dashes (remove entirely;
recast with commas, colons, parentheses, or separate sentences).

### Layer 2: academic AI tells

- Over-claiming verbs: empirical work shows and provides evidence; it
  does not prove or demonstrate universal truths. Watch demonstrate,
  prove, establish, confirm, guarantee, and "significantly" with no
  test or number.
- Significance hype: paves the way for, a crucial step toward, has the
  potential to revolutionize, opens new avenues, sheds light on, of
  paramount importance, bridges the gap.
- Empty intensifiers: extensive, comprehensive, thorough experiments, a
  wide range of, numerous, various. Replace with the counted thing.
- Novelty padding: "novel" more than once per section, "to the best of
  our knowledge", "for the first time".
- Formulaic openers: "In recent years, X has attracted increasing
  attention", "With the rapid development of...", "Despite recent
  advances,...".
- Connective overuse: do not start consecutive sentences with Moreover,
  Furthermore, Additionally, In particular. Let logic carry.
- Contribution-list cliches: each contribution names a specific result,
  not a restatement of the abstract.
- Citation dumping: cite the one or two works that matter and say why,
  not a bracketed list.
- Hedging by vagueness: somewhat, relatively, fairly, to some extent,
  quite. Quantify or cut.
- Boilerplate emphasis: "It is worth noting that", "It should be
  emphasized that", "Notably,", "Importantly,". If it matters, the
  sentence shows it.
- Overlong sentences: split sentences past about 30 words or with three
  or more subordinate clauses. One idea per sentence.

### Layer 3: preserve these, do not over-correct

- Evidence-tied hedging is correct and required. Keep "suggests", "is
  consistent with", "we hypothesize that", "may indicate", "appears to"
  when the claim is genuinely uncertain.
- Passive voice is fine when the actor is irrelevant.
- First-person plural "we" is standard.
- Semicolons and an occasional triple are fine in moderation. Em-dashes
  are the exception: remove them entirely.
- Formal definitions, named methods and metrics, technical terms,
  equations, and symbols stay verbatim.
- Never invent, drop, or alter a number, equation, or citation.

### Layer 4: claim-evidence discipline

For every empirical claim, check that it is backed by a number, figure,
table, or citation in the text, and that the verb matches the strength
of that evidence. An unbacked claim gets an evidence pointer or gets
softened. A verb stronger than the evidence gets downgraded. A vague
magnitude gets a number or a range, attributed. Prefer ranges over single
averaged values unless the averaging method is stated. When comparing,
lead with the comparison against the strongest competitor, not the
trivial baseline.

### Layer 5: voice and venue matching

Read an author sample first when one exists and match sentence rhythm,
connective habits, hedging level and placement, section openings,
notation, and recurring phrasings. Match the venue register too. With no
sample, default to clean, precise, venue-appropriate prose.

### Layer 6: funding-proposal mode

For NSF and NIH proposals only, not for decks. Vision language that the
paper layers would trim is appropriate there, provided a credible plan
and evidence back it. The discipline becomes claim to feasibility: every
bold claim needs preliminary data, a prior result, a classical theorem,
or a collaborator. Never invent preliminary results, funding, partners,
or letters.

### Output of the pass

The cleaned text plus a short change report: patterns removed by type,
claims softened or given evidence pointers, voice notes. Confirm that no
number, equation, or citation was altered.

## Indonesian pass: humanizer-indonesia (v1.7.2)

Edits Indonesian text so it reads as human writing, not model output or
translation. Framework: draft, audit, then final revision. The skill
produces a draft for a human to edit. Measured evidence in the skill:
a policy essay scored AI 89% without the skill and AI 32% with it, on
the same facts; the human score still stayed below the author band, so
hand editing remains the last step. The author voice wins over the
detector score whenever they conflict.

### Six rules that must never be broken

1. Rewrite, do not cut. If the original has five paragraphs, the result
   has five paragraphs.
2. Keep meaning and numbers. All numbers, units, figure references,
   equation references, program references, and citations stay intact.
   Never replace a number with a vague adjective, and never drop a
   cross-reference because the sentence holding it is being shortened.
3. Follow the register. A journal still sounds like a journal. The goal
   is to remove padding, not to make a paper sound like a blog.
4. Zero em-dash and en-dash in prose. En-dash is allowed only as a
   number range in the bibliography and in specifications. This rule does
   not apply to the hyphen: reduplicated words must keep it
   (rata-rata, benar-benar, masing-masing).
5. Do not compress tighter than the author. Author prose carries slack:
   akan, untuk, dapat, suatu, phrases that are not as tight as possible.
   That slack is part of the voice, not a defect.
6. Language is edited, substance is reported. Technical errors, claims
   without references, mismatched numbers, and certainty that does not
   fit the data are not fixed silently. Record them as confirmation
   points and let the author decide.

### Workflow (eight steps)

1. Check feasibility: text in Indonesian, document type not excluded
   (patents, contracts, regulations, direct quotations, validated
   research instruments are never edited), target register (akademik,
   ajar, semiformal).
2. Measure the input with `scripts/metrik.py` (seven thresholded metrics
   plus diagnostics). Note which lines need review.
3. Read the tell catalog (`references/id-ai-tells.md`) including false
   positives that must be left alone.
4. Calibrate voice from an author sample or a voice preset
   (`references/voice-*.md`) when one exists. With no sample, say so
   plainly and use a neutral voice for the register.
5. Draft the revision. Vary sentence rhythm. Build cohesion through
   keyword repetition and the `-nya` clitic, not through a connector on
   every sentence. Keep old information at the start of a sentence and
   new information at the end. Pair every claim with a number or a
   reference. Count the items in every list: an exact three-item list is
   a model habit and is flagged by detectors.
6. Step 5b (mandatory): test kalke and diction. For each paragraph ask
   what English sentence sits behind it. If the source sentence can be
   reconstructed clause by clause, the sentence is translated, not
   written in Indonesian. Rewrite the idea, not the order. Watch
   mistranslated collocations, English verbs forced into me- forms,
   dead coinages, preserved English word order, raw participle clauses
   at sentence start, word-for-word technical terms, and translated
   idioms.
7. Step 5c (mandatory): test personification, register, and sentence
   openings. Dead things have no character: a model is not lazy, brave,
   or chatty. Replace colloquial phrases with standard university
   register. Break monotonous sentence openers. Remove anticipatory
   denial ("X, bukan berarti Y"). Merge topic-announcing openers with
   the first fact of the paragraph.
8. Step 5d: fuse fragmented sentences. A run of short one-clause
   sentences is as much a tell as long nominal sentences. Join two or
   three short sentences with a conjunction that names the relation
   (karena, sehingga, sedangkan, sebab, sebagaimana, meskipun, apabila).
   Keep one short sentence as the paragraph closer, and make the closer
   carry a fact, a finding, or an admitted limit, not a punchline.
9. Audit: ask what still reads as AI or translation, rerun the metric
   script, compare with step 2. Passing every metric does not prove the
   text flows.
10. Final revision and handover: the revised draft, a short audit list, a
    list of diction decisions (which terms changed and why), the final
    revision, a before and after metric table, and confirmation points
    for substance issues.

### Indonesian deck metrics (GCI build)

Measured on `content-id.md` with the academic preset (272 sentences,
3,912 words): mean sentence length 14.4 (target 14 to 20), standard
deviation 8.8 (minimum 6.4), sentences of 28 words or more 8.8%
(maximum 20), coordination on long sentences 0.54 (maximum 1.5),
connectors 0.00 per 100 words (maximum 0.4), light verbs 0.00 per 100
words (maximum 0.4), enumeration 0.26 per 1,000 words (maximum 1),
"merupakan" 0.00 per 1,000 words (maximum 4), em-dash and en-dash 0
(maximum 0). Two post-metric fixes: "antar jenis" became "antarjenis",
"bila" became "jika" (two occurrences), after which "bila" was 0. The
number checker still reported zero problems after the humanizer pass:
no number changed.

## Two cautions the GCI build learned

### 1. Keep the epistemic hedge

The humanizer audit proposed removing "To the best of our knowledge"
from a novelty sentence. An independent review rejected the fix: the
phrase is an epistemic hedge, and removing it turns the sentence into a
factual novelty claim. When a sentence makes a novelty claim, keep the
hedge that marks it as a claim, not a fact.

### 2. A style fix can become a new empirical claim

The audit proposed replacing the vague phrase "helps only in limited
settings" with a specific exclusive list: "only on standard Credit
Default (F1@0.5) and standard HIGGS (accuracy and AUC)". Checking the
results table showed the exclusivity was false: post-ReLU correction
also helped on regularized Credit Default, regularized HIGGS,
regularized Bank Marketing, and standard Adult Income AUC, among
others. The fix would have introduced a false claim, so it was reverted
and the original wording kept. Rule: any humanizer fix that names
specific settings, or adds the word "only", is a new empirical claim.
Verify it against the table before keeping it. When in doubt, revert
to the original wording.

## What the humanizer never touches

Short titles, numbers, model names, citations, formulas, figure and
table numbers, and cross-references. Compare numbers before and after
the humanizer pass. If a number moved, the pass is wrong, not the
number.
