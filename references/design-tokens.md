# Design tokens

The visual system of the GCI deck, as built. Tokens are taken from
`.src/slides/deck.json` in the original project (theme id
`client_midnight_jade`) and from the final review. Change the values for a
new deck, keep the rules.

## Tokens

| Token | Value | Use |
|---|---|---|
| Navy (primary) | `#14467C` | Structure: titles, headers, charts, full-bleed panels |
| White (background) | `#FFFFFF` | Slide background, always pure white |
| Soft gold (accent) | `#E8B84A` | The single accent: the number to remember |
| Slate teal (secondary) | `#2F6F6E` | Sparing secondary, only where a box is truly needed |
| Ink (text) | `#1A2733` | Body text |
| Track | `#D9E1E8` | Chart tracks and light rules |
| Gray | `#9AA5B1` | Secondary labels |
| Chart muted | `#5A6B7C` | Muted chart text (matplotlib only) |

## Type

- Font: Source Sans 3 only, Regular 400 and Bold 700, for display and
  body alike. The final PDF embeds only `SourceSans3-Roman` (Regular
  plus Bold). Static TTF files are embedded as base64 data URIs by
  `build_deck.py`.
- Do not use Inter, Space Grotesk, Poppins, Montserrat, Playfair Display,
  Georgia, Bebas Neue, Anton, Caveat, Pacifico, Calibri, or Arial as a
  display choice. Inter in particular reads as default AI output.
- Sizes on the 1280 by 720 canvas: body text at least 20 px, tables at
  least 18 px, citations at least 13 px.
- Numbers use the same locale everywhere in charts and text ("49,6%" in
  the Indonesian text, "49.6%" in the English text, never mixed).
- Slide titles are full conclusion sentences with a number, at most two
  lines. Titles longer than 150 characters are flagged by the checker.

## Canvas and output

- Canvas: 1280 by 720. PDF: 960 by 540 pt, 15 pages, fonts embedded.
- One idea per slide, one exhibit per results slide. Slide layouts in
  the GCI deck came from a 350-composition catalog (category 08,
  entries 335 to 350), reused where the catalog had no exact match
  (338 used three times, 349 used twice). The catalog is a layout
  reference, not a rule: keep the archetype (title slide, two content,
  timeline, big number, data chart, matrix, comparison, image with
  caption, process flow), adapt the content.

## The accent rules (eight rules, from the final review)

Soft gold is the one accent. It marks the number to remember, nothing
else.

1. One accent focus per slide. The accent is a number the reader must
   remember.
2. A block on a white slide is fill `#E8B84A` with navy Bold text, at
   least 20 px, no border.
3. An annotation on a navy slide prefers a block of fill `#E8B84A` with
   navy text. Accent text directly on navy is allowed only in Bold at
   least 20 px.
4. In the Marimekko chart, the P1 column is accent fill with a navy Bold
   label inside, separated from P2 by a navy line.
5. Marks without text on white (break-even marker, rank dots, chart
   bars) use a 2 px navy outline, minimum 14 px.
6. Forbidden: accent text on white, thin accent lines on white (use
   navy instead).
7. Forbidden: accent for decoration (bullets, dividers, slide numbers,
   logos), accent tints, accent opacity, accent gradients.
8. Background stays pure white. No off-white or cream surfaces.

## History: amber was replaced by soft gold

The first palette used amber `#F2A900`. It was replaced after review:
amber on white has contrast near 2:1, too low for text, and cream
failed outright (1.15:1 against white). Soft gold keeps the same warm hue
(41.8 degrees against 41.9 for amber) with lower saturation, navy text on
it reads 5.18:1 (better than 4.76:1 on amber), and it stays visible on
white without a border. When a palette color fails contrast, replace the
color, not the rule.

## Slate teal rules

- Teal is a secondary, never a second accent. Use it sparingly, only
  where a box is truly needed, and keep it to a few percent of the deck.
  In the GCI deck it appears on slides 10 and 11 only.
- Never set teal text on navy. Never let teal touch navy as a text
  pairing.
- Gold stays the only focus accent. Teal must not compete with it.

## Photos

- Photos are real photos, recolored to navy duotone. No AI-generated
  imagery is used anywhere in the deck.
- The cover uses a small duotone tab on the left, not a full-bleed photo.
  A large natural-color cover photo was tried and rejected by the author:
  it fights the title for attention.
- GCI photos (Pexels, all recolored navy): cover tower 9073180 (Vaino
  Parjanen), two hands passing a phone 9786072 (Ron Lach, slide 9),
  woman with a phone at a cafe 7550823 (Hanna Pad, slide 10), customer
  at a phone-shop counter 12968298 (Sami Abdullah, slide 11).
- Cite each photo on the references slide with photographer, title,
  source, and date.

## Anti-slop visual checklist

From the "20 reasons why your app looks vibecoded" checklist, applied to
this deck during the build:

- No purple-to-blue gradient, no gradient hero text, no glassmorphism,
  no grain texture, no fade-in animation.
- No emoji in headings. No badge above the headline. No three generic
  icon benefit boxes in a row. No Lucide-everywhere icon set.
- No Inter everywhere. No Space Grotesk plus Instrument Serif pairing.
  The deck pairing (Source Sans 3 for display and body) is one family
  used consistently, not a slop combo.
- No em-dash everywhere. No serif italic accents. No generic buzzword
  copy: every slide carries one specific claim plus a number plus a
  source plus a decision.
- Consistent spacing and grid on every slide. One accent color, used for
  exactly one element per slide.
