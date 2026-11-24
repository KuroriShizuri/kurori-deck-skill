#!/usr/bin/env python3
"""Cross-check: does every number in the final deck (Rajendriya.pdf) come
from the executed notebook (Rajendriya.ipynb)?

Compares notebook cell outputs against deck text (pdftotext extraction +
content-en.md for chart-only numbers). Also re-checks the 300-day boundary
counts directly from the source CSV under BOTH conventions.

Usage: python3 check_notebook_vs_deck.py
Exit 0 = all checks pass, 1 = any mismatch.
"""
import json, re, sys
import pandas as pd

BASE = "/home/hatch/workspace/gci-final-assignment"
NB = f"{BASE}/submission/Rajendriya.ipynb"
DECK_TXT = "/tmp/deck-final-text.txt"          # pdftotext -layout deck.pdf
CONTENT_EN = f"{BASE}/deck-v2/content-en.md"   # synced content, chart numbers

nb = json.load(open(NB))
nb_text = []
for c in nb["cells"]:
    for o in c.get("outputs", []):
        if o.get("output_type") == "stream":
            nb_text.append("".join(o.get("text", [])))
        elif o.get("output_type") in ("execute_result", "display_data"):
            d = o.get("data", {})
            if "text/plain" in d:
                nb_text.append("".join(d["text/plain"]))
nb_text = "\n".join(nb_text)
deck_text = open(DECK_TXT).read()
content_en = open(CONTENT_EN).read()
deck_all = deck_text + "\n" + content_en

def norm(s):
    # drop thousands separators so 17,117 == 17117; keep decimal points
    return re.sub(r"(?<=\d),(?=\d{3}\b)", "", s)

nb_n, deck_n = norm(nb_text), norm(deck_all)

# (label, pattern in notebook, pattern in deck). Patterns are plain
# substrings matched on normalised text; % handled by the raw digits.
CHECKS = [
    ("XGB accuracy 0.6357", "0.6357", "0.6357"),
    ("XGB AUC 0.6938", "0.6938", "0.6938"),
    ("RF accuracy 0.6257", "0.6257", "0.6257"),
    ("RF AUC 0.6785", "0.6785", "0.6785"),
    ("LogReg accuracy 0.5961", "0.5961", "0.5961"),
    ("LogReg AUC 0.6295", "0.6295", "0.6295"),
    ("Majority 0.5044", "0.5044", "0.5044"),
    ("Majority AUC 0.5000", "0.5000", "0.5000"),
    ("FE CV with 0.6224", "0.6224", "0.6224"),
    ("FE CV without 0.6239", "0.6239", "0.6239"),
    ("Calibration ECE 0.0052", "0.0052", "0.0052"),
    ("XGB-RF gap 1.00 pp", "1.00", "1.00"),
    ("Margin of error 0.55 pp", "0.55", "0.55"),
    ("Churn rate 49.6%", "0.4956", "49.6%"),
    ("Churn count 49562", "49562", "49562"),  # notebook only; deck shows %
    ("Missing values 342969", "342969", "342969"),
    ("Rows >=1 missing 73.3%", "73.3", "73.3%"),
    ("Complete rows 26705", "26705", "26705"),
    ("eqpdays min -5", "-5", "-5"),
    ("eqpdays negative n=133", "133", "133"),
    ("Decile 40.0 / 43.1", "0.400", "40.0%"),
    ("Decile 37.3 / 61.0", "0.610", "61.0%"),
    ("Decile 58.3 (last)", "0.583", "58.3%"),
    ("Bin 270-300 37.4%", "0.374", "37.4%"),
    ("Bin 300-330 60.3%", "0.603", "60.3%"),
    ("Bin 330-360 62.4%", "0.624", "62.4%"),
    ("Cliff gap 22.9 pp", "22.9", "22.9"),
    ("P1 n=17117", "17117", "17117"),
    ("P1 churn 0.636", "0.636", "63.6%"),
    ("P1 revenue 78.55", "78.55", "78.55"),
    ("P2 n=33800", "33800", "33800"),
    ("P2 churn 0.625", "0.625", "62.5%"),
    ("P2 revenue 45.72", "45.72", "45.72"),
    ("Rest n=49083", "49083", "49083"),
    ("Rest churn 0.357", "0.357", "35.7%"),
    ("Capture 64.7%", "0.647", "64.7%"),
    ("P1 revenue threshold 48.20", "48.2", "48.20"),
    ("Customer value 58.21", "58.21", "58.21"),
    ("Target 50980", "50980", "50980"),
    ("Campaign cost 509800", "509800", "509800"),
    ("Scenario 10% +1729464", "1729464", "1729464"),
    ("Scenario 20% +3968727", "3968727", "3968727"),
    ("Scenario 30% +6207991", "6207991", "6207991"),
    ("Breakeven 2.3 / 4.6 / 9.1", "2.3", "2.3%"),
    ("Threshold TP 9617", "9617", "9617"),   # notebook only
    ("Threshold FP 5677", "5677", "5677"),   # notebook only
    ("Threshold target 15294", "15294", "15294"),  # notebook only
    ("corr eqpdays-months 0.483", "0.483", "0.483"),
    ("corr eqpdays-price -0.478", "-0.478", "-0.478"),
    ("Adjusted OR 1.227", "1.227", "1.227"),
    ("Cheap handsets 57.5%", "0.575", "57.5%"),
    ("Expensive handsets 41.0%", "0.410", "41.0%"),
    ("custcare 1.60 vs 1.98", "1.60", "1.60"),
    ("Gain eqpdays 43.2", "43.2", "43.2"),
    ("Gain months 33.3", "33.3", "33.3"),
    ("Gain refurb_new 29.1", "29.1", "29.1"),
    ("Perm months 0.0313", "0.0313", "0.0313"),
    ("Perm eqpdays 0.0229", "0.0229", "0.0229"),
    ("Perm drop_vce 0.0106", "0.0106", "0.0106"),
    ("Perm custcare 0.0010", "0.0010", "0.0010"),
]

fails = 0
print(f"Notebook: {len(nb['cells'])} cells, {sum(1 for c in nb['cells'] if c['cell_type']=='code')} code cells")
errs = [i for i, c in enumerate(nb["cells"]) for o in c.get("outputs", []) if o.get("output_type") == "error"]
print(f"Notebook error outputs: {errs if errs else 'NONE'}")
print()
for label, nb_pat, deck_pat in CHECKS:
    in_nb = nb_pat in nb_n
    in_deck = deck_pat in deck_n
    # items marked "notebook only" are not required on the deck
    need_deck = "notebook only" not in label
    ok = in_nb and (in_deck or not need_deck)
    if not ok:
        fails += 1
    print(f"{'PASS' if ok else 'FAIL'}  {label:38s} notebook={'Y' if in_nb else 'MISSING':8s} deck={'Y' if in_deck else ('n/a' if not need_deck else 'MISSING')}")

# Boundary counts straight from the CSV, both conventions
print("\n--- 300-day boundary, direct CSV count ---")
client = pd.read_csv(f"{BASE}/source/Client.csv", usecols=["Customer_ID", "eqpdays"])
record = pd.read_csv(f"{BASE}/source/Record.csv", usecols=["Customer_ID", "churn"])
df = record.merge(client, on="Customer_ID", how="inner")
eq = df["eqpdays"]
print(f"rows: {len(df)}, missing eqpdays: {int(eq.isna().sum())}, eqpdays==300: {int((eq == 300).sum())}")
for name, mask in [("<=300", eq <= 300), (">300", eq > 300), ("<300", eq < 300), (">=300", eq >= 300)]:
    sub = df[mask]
    print(f"  {name:6s} n={len(sub):6d}  churn={sub['churn'].mean():.4f} ({sub['churn'].mean()*100:.2f}%)")
nb_le, nb_gt = int((eq <= 300).sum()), int((eq > 300).sum())
dk_lt, dk_ge = int((eq < 300).sum()), int((eq >= 300).sum())
print(f"Notebook convention (<=300/>300): {nb_le}/{nb_gt} — deck says 40,088/59,911: "
      f"{'MATCH' if (nb_le, nb_gt) == (40088, 59911) else 'MISMATCH'}")
print(f"Deck convention (<300/>=300): {dk_lt}/{dk_ge} — deck says 39,926/60,073: "
      f"{'MATCH' if (dk_lt, dk_ge) == (39926, 60073) else 'MISMATCH'}")
print(f"Deck percentages <300 39.5% / >=300 56.3%: churn <300={df[eq < 300]['churn'].mean()*100:.2f}%, "
      f">=300={df[eq >= 300]['churn'].mean()*100:.2f}%")

print(f"\nTOTAL FAILURES: {fails}")
sys.exit(1 if fails else 0)
