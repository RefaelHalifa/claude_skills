# Active Style Profile
_Reverse-engineered from Refael's sample (warm-paper editorial style). This is the single source of
truth for every carousel. `/style [new sample]` overwrites this file._

_Last derived: 2026-06-17 — source: "How to Be Recognized Without Being Loud" sample._

## Brand
- **Name / wordmark:** `Refael` (top-right, small, uppercase tracked, ink color). Optional mark next to it.
- **Headshot placeholder:** `{{HEADSHOT}}` — round, thin orange ring. Used on the CTA slide only.
- No third-party logos.

## Color palette
| Token | Hex | Use |
|-------|-----|-----|
| Paper (background) | `#F2F1ED` | Every slide background. Warm off-white, subtle paper grain. |
| Accent (orange) | `#ED4B1F` | Italic accent word, page numbers, CTA, small graphic accents, underlines. |
| Ink (text) | `#1A1A1A` | Headlines and body. |
| Ink-soft (optional) | `#3A3A3A` | Long body paragraphs if pure black feels heavy. |

Accent is used sparingly — one orange element per slide is the default (the accent word OR the page
number is always orange; extra orange only for a deliberate graphic).

## Typography
- **Headline (display serif):** high-contrast Didone feel. Web: `"Playfair Display", Georgia, serif`,
  weight 700–900. Large, tight leading.
- **Accent word (italic script-serif):** the first phrase of a headline, set in *orange italic*. Web:
  `"Playfair Display", Georgia, serif` with `font-style: italic`. (Swap to a scriptier face like
  `"DM Serif Display"` italic if more flourish is wanted.)
- **Body & labels (sans):** clean geometric sans. Web: `"Inter", "Helvetica Neue", Arial, sans-serif`.
  - Body: regular weight, ~1.5 line-height, ink or ink-soft.
  - Labels/kickers: UPPERCASE, weight 600, letter-spacing ~0.12em — often in orange for section kickers.

## Layout furniture
- **Logo/wordmark:** top-right, every slide.
- **Page number:** bottom-left, orange, plain digit (e.g. `2`). Title slide (1) usually has none.
- **Margins:** generous. Content left-aligned, sitting roughly in the left 60–70% of the slide.
- **Whitespace:** high. One idea per slide, lots of breathing room above and below.
- **Accent-word pattern:** headlines often split — first line/phrase in orange italic, rest in black roman.
  Example: *How to Be* (orange italic) / **Recognized Without Being Loud** (black serif).

## Tone (visual + copy)
Editorial, calm, premium. Confident and quiet — "strategically visible," not loud. Short declarative
sentences. Lowercase warmth in body, strong serif authority in headlines. Matches Refael's direct,
no-fluff voice.

## Layout inventory observed in the sample (for variety)
1. Title card — big split headline + subhead + READ MORE arrow.
2. Headline + body paragraph.
3. Kicker + bullet list (max 4, round bullets).
4. Giant two-color statement filling the slide.
5. Kicker + circle-diagram (3 outlined circles with short labels).
6. Statement + small pixel/sticker graphic accent.
7. CTA — question headline + round headshot + "SHARE THIS POST" label.

## Placeholders
- `{{BRAND}}` → `Refael`
- `{{HEADSHOT}}` → user's photo (round, orange ring) on the CTA slide.
