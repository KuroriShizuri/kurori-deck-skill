#!/usr/bin/env python3
"""Pemeriksa angka dan gaya untuk deck v2.

Tiga pemeriksaan:
1. Angka per slide identik antara slides.id.md dan slides.en.md
   (format Indonesia: 1.729.464 dan 0,6357; format Inggris: 1,729,464 dan 0.6357).
2. Setiap angka di slide ada di lembar angka terverifikasi (nilai, nilai x 100, atau nilai / 100).
3. Larangan gaya: angka tutorial yang dibatalkan, em-dash, en-dash, emoji, kata AI-slop.
"""
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
ID_FILE = HERE / "content-id.md"
EN_FILE = HERE / "content-en.md"

# Lembar angka terverifikasi (notasi titik desimal). Sumber: pesan Rajendriya.
SHEET = """
0.5044 0.5 0.6357 0.6938 0.6257 0.6785 0.5961 0.6295 30000 0.55 1.00
0.400 0.431 0.375 0.373 0.610 0.581 0.527 0.533 0.544 0.583 0.374 0.603 0.624
300 270 330 360 39.5 39926 56.3 60073 22.9
0.483 0.478 0.205 1.227 0.575 0.410
530 48.20 5878 5.9 0.626 75.22 45039 45.0 0.629 54.40 49083 0.357 64.7
43.2 29.1 0.0106 53 45 1.60 1.98
0.6224 0.6239 0.0052
58.21 50980 509800 70000 10 12 0.1 0.2 0.3 1729464 3968727 6207991 2.3 4.6 9.1
342969 73.3 26705 21 5 133 100000 49.6
17 18 60 97 297 20 2.8 157.6 91.5 46000 70 47500 3.5 31 144000 600 5000
2025 2026
17117 17.1 0.636 78.55 33800 33.8 0.625 45.72 62 0.0004 18 10000 99999 140 84000 60000 2.54 23 50917
"""
ALLOWED = set()
for t in SHEET.split():
    v = float(t)
    for x in (v, v * 100, v / 100):
        ALLOWED.add(round(x, 6))
ALLOWED.update(float(i) for i in range(0, 16))
ALLOWED.add(100.0)  # batang 100% adalah desain, bukan data  # nomor slide, langkah, bilangan kecil

FORBIDDEN_STRINGS = ["0,6368", "0.6368"]
FORBIDDEN_CHARS = {"\u2014": "em-dash", "\u2013": "en-dash"}
EMOJI = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF]")
BANNED_WORDS = re.compile(
    r"\b(delve|furthermore|moreover|leverage|leveraging|cutting-edge|robust|seamless|"
    r"landscape|pivotal|foster|utilize|gradient|Inter)\b",
    re.IGNORECASE if False else 0,
)
BANNED_WORDS_CI = re.compile(
    r"\b(delve|furthermore|moreover|leverage|leveraging|cutting-edge|robust|seamless|pivotal|utilize|gradient)\b",
    re.IGNORECASE,
)
TOKEN = re.compile(r"\d[\d.,]*\d|\d")
URL = re.compile(r"https?://\S+")


def parse_token(tok: str, lang: str) -> float:
    if lang == "id":
        if re.fullmatch(r"\d{1,3}(\.\d{3})+", tok):
            tok = tok.replace(".", "")
        else:
            tok = tok.replace(",", ".")
    else:
        if re.fullmatch(r"\d{1,3}(,\d{3})+", tok):
            tok = tok.replace(",", "")
    return round(float(tok), 6)


def split_slides(text: str):
    parts = re.split(r"^### ", text, flags=re.MULTILINE)
    out = {"Pembuka": parts[0]}
    for p in parts[1:]:
        head, _, body = p.partition("\n")
        out[head.strip()] = body
    return out


def numbers(body: str, lang: str, skip_refs: bool):
    vals = []
    for line in body.splitlines():
        if skip_refs and re.match(r"^- \[\d+\]", line):
            line = URL.sub("", line)
            # judul rujukan boleh memuat angka dari sumber; dibandingkan, tetapi tidak diperiksa terhadap lembar
        else:
            line = URL.sub("", line)
        for tok in TOKEN.findall(line):
            vals.append((parse_token(tok, lang), tok, line.strip()))
    return vals


def main() -> int:
    id_text = ID_FILE.read_text(encoding="utf-8")
    en_text = EN_FILE.read_text(encoding="utf-8")
    problems = 0

    # 3. Larangan gaya
    for name, text in (("ID", id_text), ("EN", en_text)):
        for s in FORBIDDEN_STRINGS:
            if s in text:
                print(f"[GAYA] {name}: memuat angka terlarang {s}")
                problems += 1
        for ch, label in FORBIDDEN_CHARS.items():
            if ch in text:
                print(f"[GAYA] {name}: memuat {label}")
                problems += 1
        if EMOJI.search(text):
            print(f"[GAYA] {name}: memuat emoji")
            problems += 1
        for m in BANNED_WORDS_CI.finditer(text):
            print(f"[GAYA] {name}: kata terlarang '{m.group(0)}'")
            problems += 1
        for m in re.finditer(r"\bInter\b", text):
            print(f"[GAYA] {name}: menyebut font Inter")
            problems += 1
        for i, line in enumerate(text.splitlines(), 1):
            if re.search(r"\s-\s", line):
                print(f"[GAYA] {name} baris {i}: tanda hubung berspasi (mirip dash): {line[:70]}")
                problems += 1

    id_s = split_slides(id_text)
    en_s = split_slides(en_text)
    if list(id_s) != list(en_s):
        print("[STRUKTUR] Daftar slide ID dan EN berbeda:", list(id_s), list(en_s))
        problems += 1

    # 1 dan 2. Angka
    for key in id_s:
        if key not in en_s:
            continue
        a = numbers(id_s[key], "id", True)
        b = numbers(en_s[key], "en", True)
        ca = Counter(v for v, _, _ in a)
        cb = Counter(v for v, _, _ in b)
        if ca != cb:
            print(f"[BEDA] {key}: ID-EN tidak identik")
            for v in sorted(set(ca) | set(cb)):
                if ca[v] != cb[v]:
                    print(f"        nilai {v}: ID x{ca[v]}, EN x{cb[v]}")
            problems += 1
        for lang, items in (("ID", a), ("EN", b)):
            for v, tok, line in items:
                if re.match(r"^- \[\d+\]", line) or re.match(r"^(Komposisi|Composition):", line):
                    continue
                if v not in ALLOWED:
                    print(f"[ASING] {key} {lang}: angka {tok} (={v}) tidak ada di lembar. Baris: {line[:80]}")
                    problems += 1

    # Judul
    print("\nJudul (ghost-deck test), panjang karakter:")
    for lang, text in (("ID", id_text), ("EN", en_text)):
        print(f"-- {lang}")
        for key, body in split_slides(text).items():
            m = re.search(r"^(Judul|Title): (.+)$", body, flags=re.MULTILINE)
            if m:
                t = m.group(2)
                flag = "  <== panjang" if len(t) > 150 else ""
                print(f"{key}: ({len(t)}) {t}{flag}")

    print(f"\nTotal masalah: {problems}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
