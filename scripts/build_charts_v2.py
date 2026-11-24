#!/usr/bin/env python3
"""Build all data charts for deck v2 (GCI Final Assignment) from verified numbers.

Palette: navy #14467C, white, soft gold #E8B84A, ink #1A2733, muted #5A6B7C,
grid #D9E1E8, gray #9AA5B1. Font: Source Sans 3 (deck's own media dir).
All numbers come from content-en.md / the verified recompute (recompute_p1_300.log).
Deciles are recomputed from source CSVs and asserted against the deck values.
Outputs: deck-v2/.src/media/*.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
GCI = os.path.join(os.path.expanduser("~"), "workspace", "gci-final-assignment")

for f in ["SourceSans3-Regular.ttf", "SourceSans3-Bold.ttf"]:
    font_manager.fontManager.addfont(os.path.join(HERE, "fonts", f))
plt.rcParams["font.family"] = "Source Sans 3"

NAVY = "#14467C"
GOLD = "#E8B84A"
INK = "#1A2733"
MUTED = "#5A6B7C"
GRID = "#D9E1E8"
GRAY = "#9AA5B1"

def save(fig, name):
    out = os.path.join(HERE, name)
    fig.savefig(out, dpi=200, facecolor=fig.get_facecolor())
    print("wrote", out)
    plt.close(fig)

# ---------------------------------------------------------------- deciles: verify
c = pd.read_csv(os.path.join(GCI, "source", "Client.csv"), usecols=["Customer_ID", "eqpdays"])
r = pd.read_csv(os.path.join(GCI, "source", "Record.csv"), usecols=["Customer_ID", "churn"])
df = c.merge(r, on="Customer_ID").dropna(subset=["eqpdays"])
df["decile"] = pd.qcut(df["eqpdays"], 10, labels=False) + 1
dec = df.groupby("decile")["churn"].mean().values * 100
expected = np.array([40.0, 43.1, 37.5, 37.3, 61.0, 58.1, 52.7, 53.3, 54.4, 58.3])
diff = np.abs(dec - expected)
print("deciles recomputed:", np.round(dec, 1).tolist())
print("deciles max abs diff vs deck: %.2f pp" % diff.max())
assert diff.max() < 0.15, "decile mismatch"
bnd = df.groupby("decile")["eqpdays"].max().values
print("decile upper bounds (days):", bnd.tolist())
print("boundary D4/D5 at ~%d days (cliff is 300)" % bnd[3])

# ---------------------------------------------------------------- 1. operators (slide 2)
fig, ax = plt.subplots(figsize=(7.6, 3.2))
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
ops = [("Telkomsel", 157.6, "Sep 2025", "[7]"), ("Indosat", 91.5, "Q3 2026", "[4]"), ("XLSmart", 70.0, "Q3 2026", "[5]")]
y = np.arange(len(ops))[::-1]
ax.barh(y, [o[1] for o in ops], height=0.55, color=NAVY, zorder=3)
for yi, (name, val, date, ref) in zip(y, ops):
    ax.text(val + 4, yi, f"{val:.1f}M  ({date}) {ref}", va="center", ha="left",
            fontsize=13, color=INK)
ax.set_yticks(y, [o[0] for o in ops], fontsize=13, color=INK)
ax.set_xlim(0, 240)  # 240, not 205: the "[7]" marker makes the Telkomsel label longer (23 Nov 2026)
ax.set_xlabel("Subscribers (million)", fontsize=12, color=INK)
ax.tick_params(axis="x", labelsize=11, colors=INK)
ax.xaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
save(fig, "operators.png")

# ---------------------------------------------------------------- 2. deciles (slide 5, navy)
fig, ax = plt.subplots(figsize=(11.0, 4.9))
fig.patch.set_facecolor(NAVY); ax.set_facecolor(NAVY)
x = np.arange(1, 11)
ax.bar(x, dec, width=0.72, color="white", zorder=3)
ax.axvline(4.5, color="white", linestyle=(0, (4, 3)), linewidth=1.6, zorder=4)
for xi, v in zip(x, dec):
    ax.text(xi, v + 1.8, f"{v:.1f}%", ha="center", va="bottom",
            fontsize=12, color="white")
ax.set_xlim(0.3, 10.7)
ax.set_ylim(0, 74)
ax.set_xticks(x, [f"D{i}" for i in x], fontsize=12, color="white")
ax.set_yticks([0, 20, 40, 60], ["0%", "20%", "40%", "60%"], fontsize=12, color="white")
ax.set_xlabel("10 equal-sized customer groups, youngest to oldest handsets", fontsize=13, color="white")
ax.set_ylabel("Churn rate", fontsize=13, color="white")
ax.tick_params(axis="x", colors="white", length=0)
ax.tick_params(axis="y", colors="white", length=0)
ax.yaxis.grid(True, color="white", alpha=0.25, linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left", "bottom"]:
    ax.spines[s].set_visible(False)
plt.tight_layout()
save(fig, "deciles.png")

# ---------------------------------------------------------------- 3. Marimekko (slide 6)
fig, ax = plt.subplots(figsize=(7.6, 4.6))
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
segs = [("P1", 17117, 63.6, 78.55, GOLD, NAVY),
        ("P2", 33800, 62.5, 45.72, NAVY, "white"),
        ("Rest", 49083, 35.7, None, GRAY, "white")]
assert sum(s[1] for s in segs) == 100000
left = 0
for name, n, churn, rev, color, tcol in segs:
    w = n / 1000.0
    ax.bar(left + w / 2, churn, width=w, color=color, edgecolor="white",
           linewidth=1.2, zorder=3)
    cx = left + w / 2
    ax.text(cx, churn - 4, f"{name}", ha="center", va="top", fontsize=15,
            fontweight="bold", color=tcol)
    ax.text(cx, churn - 13, f"n={n:,}", ha="center", va="top", fontsize=12,
            fontweight="bold", color=tcol)
    ax.text(cx, churn - 21, f"{churn:.1f}% churn", ha="center", va="top",
            fontsize=12, fontweight="bold", color=tcol)
    if rev is not None:
        ax.text(cx, churn - 29, f"${rev:.2f}/mo", ha="center", va="top",
                fontsize=12, fontweight="bold", color=tcol)
    left += w
# Navy rule between the P1 (soft gold) and P2 columns (palette rule 4).
ax.plot([17.117, 17.117], [0, 63.6], color=NAVY, linewidth=2.0, zorder=6)
ax.annotate("P1 churn almost the same as P2\n(63.6% vs 62.5%)",
            xy=(17.117 / 2, 63.6), xytext=(55, 78),
            fontsize=12, color=INK, ha="center", va="center",
            arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
ax.set_xlim(0, 100)
ax.set_ylim(0, 88)
ax.set_xticks([17117 / 2000, 17117 / 1000 + 33800 / 2000, 50917 / 1000 + 49083 / 2000],
              ["P1\n17,117", "P2\n33,800", "Rest\n49,083"], fontsize=12, color=INK)
ax.set_yticks([0, 20, 40, 60], ["0%", "20%", "40%", "60%"], fontsize=12, color=INK)
ax.set_ylabel("Churn rate", fontsize=13, color=INK)
ax.tick_params(axis="x", length=0)
ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
save(fig, "marimekko.png")

# ---------------------------------------------------------------- 4. model dots (slide 7)
fig, ax = plt.subplots(figsize=(7.4, 4.4))
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
models = [("XGBoost", 0.6357, 0.6938, GOLD),
          ("Random Forest", 0.6257, 0.6785, NAVY),
          ("Logistic Regression", 0.5961, 0.6295, NAVY),
          ("Majority guess", 0.5044, 0.5000, NAVY)]
y = np.arange(len(models))[::-1]
acc = [m[1] for m in models]
ax.errorbar(acc, y, xerr=0.0055, fmt="o", ms=11, color=NAVY,
            ecolor=NAVY, elinewidth=1.6, capsize=5, zorder=4)
for yi, m in zip(y, models):
    edge = NAVY if m[3] == GOLD else "white"
    ax.plot([m[1]], [yi], "o", ms=11, color=m[3], zorder=5,
            markeredgecolor=edge, markeredgewidth=2.0 if m[3] == GOLD else 1.0)
    ax.text(0.665, yi, f"AUC {m[2]:.4f}", va="center", ha="left",
            fontsize=12, color=INK)
    ax.text(m[1], yi + 0.28, f"{m[1]:.4f}", va="bottom", ha="center",
            fontsize=11, color=MUTED)
ax.axvline(0.5044, color=MUTED, linestyle=(0, (4, 3)), linewidth=1.4, zorder=2)
ax.text(0.512, 3.75, "majority guess 0.5044", ha="left", va="bottom",
        fontsize=11, color=MUTED)
ax.text(0.665, 3.75, "AUC", ha="left", va="bottom", fontsize=11,
        fontweight="bold", color=INK)
ax.set_yticks(y, [m[0] for m in models], fontsize=13, color=INK)
ax.set_xlim(0.48, 0.74)
ax.set_ylim(-0.6, 4.1)
ax.set_xticks([0.50, 0.55, 0.60, 0.65],
              ["0.50", "0.55", "0.60", "0.65"], fontsize=12, color=INK)
ax.set_xlabel("Accuracy (error bars: margin of error about 0.55 pp)", fontsize=12, color=INK)
ax.tick_params(axis="y", length=0)
ax.xaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
save(fig, "model-dots.png")

# ---------------------------------------------------------------- 5. rank dots (slide 8)
fig, ax = plt.subplots(figsize=(7.4, 4.6))
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
feats = [("eqpdays", 1, 2, True),
         ("months", 2, 1, False),
         ("refurb_new", 3, 62, False),
         ("drop_vce_Mean", 18, 6, True),
         ("custcare_Mean", 53, 45, False)]
y = np.arange(len(feats))[::-1]
label_pos = {  # (x, y, ha, va) per (feature, kind); chosen to avoid collisions
    ("eqpdays", "g"): (0.55, 4.0, "right", "center"),
    ("eqpdays", "p"): (2.45, 4.0, "left", "center"),
    ("months", "g"): (2.45, 3.0, "left", "center"),
    ("months", "p"): (0.55, 3.0, "right", "center"),
    ("refurb_new", "g"): (3, 2.32, "center", "bottom"),
    ("refurb_new", "p"): (62, 1.68, "center", "top"),
    ("drop_vce_Mean", "g"): (18, 1.32, "center", "bottom"),
    ("drop_vce_Mean", "p"): (6, 0.68, "center", "top"),
    ("custcare_Mean", "g"): (53, 0.32, "center", "bottom"),
    ("custcare_Mean", "p"): (45, -0.32, "center", "top"),
}
for yi, (name, g, p, actionable) in zip(y, feats):
    col = GOLD if actionable else NAVY
    ax.plot([g], [yi], "o", ms=11, color=col, zorder=5,
            markeredgecolor=NAVY if actionable else "white",
            markeredgewidth=2.0 if actionable else 1.0)
    ax.plot([p], [yi], "D", ms=10, markerfacecolor="white",
            markeredgecolor=NAVY, markeredgewidth=2.0, zorder=5)
    for kind, val in (("g", g), ("p", p)):
        # Ranks 1 and 2 are not labeled on the chart: the two markers sit
        # one unit apart and any label would sit on a marker. The caption
        # below the chart states those ranks in words.
        if val <= 2:
            continue
        lx, ly, ha, va = label_pos[(name, kind)]
        ax.text(lx, ly, str(val), ha=ha, va=va, fontsize=10, color=MUTED, zorder=6)
ax.plot([], [], "o", ms=9, color=NAVY, label="gain rank")
ax.plot([], [], "D", ms=8, markerfacecolor="white", markeredgecolor=NAVY,
        markeredgewidth=1.6, label="permutation rank")
ax.plot([], [], "o", ms=9, color=GOLD, markeredgecolor=NAVY,
        markeredgewidth=2.0, label="business can change")
ax.legend(loc="upper right", fontsize=11, frameon=False)
labels = ["Handset age\n(eqpdays)", "Tenure\n(months)",
          "Refurbished or new handset\n(refurb_new)",
          "Dropped voice calls\n(drop_vce_Mean)",
          "Customer care calls\n(custcare_Mean)"]
ax.set_yticks(y, labels, fontsize=13, color=INK)
ax.set_xlim(0, 66)
ax.set_ylim(-0.7, 4.7)
ax.set_xticks([1, 10, 20, 30, 40, 50, 60], ["1", "10", "20", "30", "40", "50", "60"], fontsize=12, color=INK)
ax.set_xlabel("Rank (1 is top)", fontsize=12, color=INK)
ax.tick_params(axis="y", length=0)
ax.xaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for s in ["top", "right", "left"]:
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
save(fig, "ranks.png")

# ---------------------------------------------------------------- 6. impact line (slide 12)
# Net(s) = s * 22,392,640 - 509,800  (12-month stay period; verified by the three
# scenario points: 10% -> 1,729,464; 20% -> 3,968,727; 30% -> 6,207,991)
# Narrower figure (9.5 x 3.27, was 11.0 x 4.6) so the chart fits slide 12
# at 696 px display width (aspect 2.91) next to the break-even panel.
# Rapiin round 23 Nov 2026: 4.6% and 9.1% break-even markers removed from the
# chart (they now live in the side panel); only the gold 2.3% marker stays.
fig, ax = plt.subplots(figsize=(9.5, 3.27))
fig.patch.set_facecolor("white"); ax.set_facecolor("white")
s = np.linspace(0, 0.35, 200)
net = s * 22392640 - 509800
ax.axhline(0, color=MUTED, linewidth=1.2, zorder=2)
ax.plot(s * 100, net / 1e6, color=NAVY, linewidth=2.4, zorder=4)
scen = [(10, 1729464), (20, 3968727), (30, 6207991)]
for pct, val in scen:
    ax.plot([pct], [val / 1e6], "o", ms=10, color=NAVY, zorder=5,
            markeredgecolor="white", markeredgewidth=1.0)
    ax.text(pct, val / 1e6 + 0.35, f"{pct}%  +${val:,}", ha="center", va="bottom",
            fontsize=12, fontweight="bold", color=INK)
for pct, lab, col, ly in [(2.3, "break-even 2.3% (12-month stay)", GOLD, -1.3)]:
    ax.plot([pct], [0], "D" if col == GOLD else "o", ms=11 if col == GOLD else 8,
            color=col, zorder=5,
            markeredgecolor=NAVY if col == GOLD else "white",
            markeredgewidth=2.0 if col == GOLD else 1.0)
    ax.plot([pct, pct], [0, -0.85], color=NAVY, linewidth=1.0,
            linestyle=(0, (3, 3)), zorder=3)
    ax.text(pct, ly, lab, ha="left", va="top",
            fontsize=11, fontweight="bold" if col == GOLD else "normal",
            color=INK)
ax.set_xlim(0, 35)
ax.set_ylim(-4.2, 7.4)
ax.set_xticks([0, 5, 10, 15, 20, 25, 30, 35],
              ["0%", "5%", "10%", "15%", "20%", "25%", "30%", "35%"],
              fontsize=12, color=INK)
ax.set_yticks([-1, 0, 2, 4, 6],
              ["-$1M", "$0", "$2M", "$4M", "$6M"], fontsize=12, color=INK)
ax.set_xlabel("Save rate", fontsize=13, color=INK)
ax.set_ylabel("Net result (USD, 12-month stay period)", fontsize=13, color=INK)
ax.yaxis.grid(True, color=GRID, linewidth=0.8, zorder=0)
ax.set_axisbelow(True)
for s_ in ["top", "right", "left"]:
    ax.spines[s_].set_visible(False)
ax.spines["bottom"].set_color(MUTED)
plt.tight_layout()
save(fig, "impact-line.png")

print("ALL CHARTS DONE")
