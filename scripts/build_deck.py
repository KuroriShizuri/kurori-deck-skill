#!/usr/bin/env python3
"""Deck v2 build step: embed fonts + images into .src/slides/ in place.

1. Appends @font-face rules (base64 TTF, Source Sans 3 Regular 400 + Bold 700)
   to .src/slides/deck.css (once; guarded by a marker comment).
2. Replaces {{IMG:filename}} placeholders in every slide HTML with a base64
   data URI from .src/media/filename (once; guarded by placeholder presence).
Run after authoring slides, before assemble_deck.mjs.
"""
import base64
import mimetypes
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SLIDES = os.path.join(HERE, "slides")
MEDIA = os.path.join(HERE, "media")
FONTS = os.path.join(MEDIA, "fonts")
MARKER = "/* fonts-embedded-v2 */"


def embed_fonts():
    css_path = os.path.join(SLIDES, "deck.css")
    css = open(css_path, encoding="utf-8").read()
    if MARKER in css:
        print("fonts already embedded, skipping")
        return
    parts = [css.rstrip(), "", MARKER]
    for fname, weight in [("SourceSans3-Regular.ttf", 400),
                          ("SourceSans3-Bold.ttf", 700)]:
        raw = open(os.path.join(FONTS, fname), "rb").read()
        b64 = base64.b64encode(raw).decode("ascii")
        parts.append(
            "@font-face {\n"
            "  font-family: 'Source Sans 3';\n"
            "  font-style: normal;\n"
            f"  font-weight: {weight};\n"
            "  font-display: swap;\n"
            f"  src: url(\"data:font/ttf;base64,{b64}\") format(\"truetype\");\n"
            "}"
        )
    open(css_path, "w", encoding="utf-8").write("\n".join(parts) + "\n")
    print("embedded fonts into deck.css")


def inline_images():
    for name in sorted(os.listdir(SLIDES)):
        if not name.endswith(".html"):
            continue
        path = os.path.join(SLIDES, name)
        html = open(path, encoding="utf-8").read()
        if "{{IMG:" not in html:
            continue
        for fname in set(p[6:-2] for p in
                         __import__("re").findall(r"\{\{IMG:[^}]+\}\}", html)):
            fpath = os.path.join(MEDIA, fname)
            if not os.path.exists(fpath):
                print(f"ERROR: missing image {fname} for {name}")
                sys.exit(1)
            mime = mimetypes.guess_type(fname)[0] or "image/png"
            b64 = base64.b64encode(open(fpath, "rb").read()).decode("ascii")
            html = html.replace("{{IMG:%s}}" % fname,
                                f"data:{mime};base64,{b64}")
        open(path, "w", encoding="utf-8").write(html)
        print("inlined images in", name)


if __name__ == "__main__":
    embed_fonts()
    inline_images()
    print("BUILD OK")
