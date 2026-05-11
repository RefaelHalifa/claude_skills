# CV Design Specification
> Confirmed and locked April 2026. Apply to every CV without exception.

---

## Color Palette

| Role | Hex | Description |
|---|---|---|
| Name | `#1A1A2E` | Dark navy blue |
| Section headers | `#2E6DA4` | Medium corporate blue |
| Body text / bullets | `#3A3A3A` | Dark gray |
| Job meta / subtitles | `#555555` | Mid gray |
| Secondary info / bullet dots | `#888888` | Light gray |
| Horizontal rules | `#CCCCCC` | Light gray |
| Links | `#2E6DA4` | Same blue as section headers |

---

## Typography

| Element | Font | Size | Notes |
|---|---|---|---|
| Name | Helvetica-Bold | 22pt | Centered |
| Section headers | Helvetica-Bold | 9pt | UPPERCASE |
| Body / bullets | Helvetica | 8.4pt | |
| Job meta / stack lines | Helvetica-Oblique | 8.2pt | |
| Summary | Helvetica | 8.8pt | leading 13pt |
| Skill values | Helvetica | 8.3pt | leading 11pt |

---

## Page Layout

- **Page size:** A4
- **Margins:** 16mm left/right, 13mm top, 11mm bottom
- **Target bottom margin remaining:** ~10–12mm (content fills the page)
- **Horizontal rule:** 0.6pt, `#CCCCCC`, under every section header
- **ONE page only — non-negotiable**

---

## Links — Plain Underlined Hypertext (PERMANENT)

- Header links: **"LinkedIn  |  GitHub"** — plain blue underlined label text, centred below the contact line
- Use `canvas.linkURL()` to make the full text bounding box a real PDF hyperlink
- Underline: 0.5pt, `#2E6DA4`, 1.2pt below baseline
- Separator: `"   |   "` in `#888888` (light gray), NOT hyperlinked
- **No pills, no backgrounds, no URL text shown** — just the label as clickable blue underlined text

---

## Skills Section — 2-Column Layout with Dynamic Row Heights (PERMANENT)

- Always use a **2-column layout** (categories split evenly left/right)
- Column geometry: `col_gap=8mm`, `col_w=(CONTENT_W - col_gap)/2 ≈ 85mm`, `label_w=26mm`, `val_w ≈ 57mm (161pt)`
- Labels: Helvetica-Bold 8.3pt — plain `drawString` (NOT HTML — use `&` not `&amp;`)
- Values: Helvetica 8.3pt, leading 11pt — drawn as `Paragraph` objects
- **Values must fit on ONE line** at `val_w ≈ 161pt` (~37 chars). Shorten if too long — never let values wrap to 2 lines (causes cascading overlap)
- Row heights: **measured dynamically** using `para_height()` — never use a fixed `row_h` constant
- Row gap between entries: **3pt**
- Extra gap after skills block: **5pt**

---

## Spacing — Exact Values (PERMANENT)

| Context | Value |
|---|---|
| `gap_before` Experience, Projects, Education, Languages | 13pt |
| `gap_before` Skills | 10pt |
| `gap_before` Summary | 5pt |
| Section header → first content line (rule to content) | 17pt |
| Bullet `line_h` | 13pt |
| Title → company gap in exp blocks | 12pt |
| Company → first bullet gap | 12pt |
| Post-block gap (after last bullet) | 8pt |
| Education row height | 12pt |
| Summary `leading` | 13pt |
| Extra gap after summary | 5pt |

---

## Languages Section — Single Horizontal Line (PERMANENT)

- All languages on **one horizontal line**, spread evenly across full content width
- Format per entry: **Bold language name** + gray `— Level` text (5pt gap between)
- Use `CONTENT_W / len(langs)` as segment width, `ML + i * seg_w` as x per entry
- Do NOT stack languages vertically

---

## Education Section

- Two-column: degree bold left (`col_e=73mm`), institution + year gray right
- Row height: 12pt

---

## Y-Position Tracking — Critical Coding Rules (PERMANENT)

- **Never use `y + offset` as a paragraph reference point** — causes overlap bugs
- For all paragraph drawing:
  1. Measure height: `h = para_height(para, width)`
  2. Draw: `para.drawOn(canvas, x, y - h + 1.5)`
  3. Advance: `y -= h + gap`
- The `+ 1.5` corrects for ReportLab's paragraph box descender space so the first line visually aligns with the cursor
- After every section, verify bottom margin: print `(y - MB)` in pt and mm

---

## Generation Method — Pre-Budget Single-Pass (PERMANENT, 2026-05-11)

> **CRITICAL: never use the old "render → measure → trim → re-render" loop.**
> Every margin-chase rebuild costs tokens. Compute the content budget BEFORE rendering, trim to fit, render ONCE.

### Pre-budget algorithm — run this BEFORE any reportlab call

Step 1 — Compute available content height (constant per page geometry):
```python
PAGE_H = 297 * mm                 # A4
MT, MB = 13 * mm, 11 * mm         # margins
TARGET_BOTTOM = 11 * mm           # we want to land near MB, not waste paper
USABLE_H = PAGE_H - MT - MB       # ≈ 273 mm = 774 pt
```

Step 2 — Compute fixed-section height (these never trim):
```python
FIXED = (
    name_block_h +                # 22pt name + padding
    contact_h +                   # contact line + link line + rule
    languages_h +                 # always one line
    section_header_h * 5 +        # Summary, Skills, Experience, Projects, Education headers
    section_gaps_total            # sum from spacing table above
)
```

Step 3 — Estimate variable-section height from content character counts BEFORE rendering:
```python
# Empirically derived constants — leave fixed unless reportlab font/size changes
CHARS_PER_LINE_BODY      = 96    # at 8.4pt Helvetica, 178mm width
CHARS_PER_LINE_SUMMARY   = 88    # at 8.8pt Helvetica
LINE_H_BODY              = 13    # pt — matches bullet line_h
LINE_H_SUMMARY           = 13    # pt

def est_h(text, cpl, line_h):
    lines = max(1, -(-len(text) // cpl))   # ceiling division
    return lines * line_h
```

Step 4 — Compute total budget BEFORE choosing what to include:
```python
budget = USABLE_H - FIXED                  # pt available for variable content
variable_h = (
    est_h(summary, CHARS_PER_LINE_SUMMARY, LINE_H_SUMMARY) +
    sum(est_h(b, CHARS_PER_LINE_BODY, LINE_H_BODY) for b in all_bullets) +
    skills_rows * 14                        # 11pt leading + 3pt gap
)
```

Step 5 — If `variable_h > budget`, trim by priority list BEFORE rendering:
```python
trim_order = [
    "drop_oldest_bullet_from_lowest_priority_role",
    "tighten_summary_to_3_lines",
    "drop_weakest_project",
    "shorten_each_bullet_by_one_phrase",
]
# Trim items in order, recomputing variable_h after each. Stop the moment it fits.
```

Step 6 — Render ONCE with the trimmed content. Bottom-margin verification is a sanity check only — never a trigger for another render.

### Acceptance criteria — no second render allowed

After the single render, accept the result if:
- Page count == 1 ✅
- Bottom margin remaining is anywhere in 3–18mm range ✅ (don't chase exact 10–12mm)

**HARD CAP: maximum 2 renders per CV session.** If the second render still doesn't fit, STOP and ask the user which bullet to drop — do not loop further.

---

## Legacy Generation Method (reference only — DO NOT USE)

Built with **Python + ReportLab canvas** — direct drawing, NO Platypus flowables.
Direct canvas gives pixel-level control over every element.

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

PAGE_W, PAGE_H = A4
ML = 16 * mm   # margin left/right
MT = 13 * mm   # margin top
MB = 11 * mm   # margin bottom
CONTENT_W = PAGE_W - 2 * ML

# Colors
NAVY  = colors.HexColor('#1A1A2E')
BLUE  = colors.HexColor('#2E6DA4')
DARK  = colors.HexColor('#3A3A3A')
MID   = colors.HexColor('#555555')
LIGHT = colors.HexColor('#888888')
RULE  = colors.HexColor('#CCCCCC')

def para_height(para, width):
    w, h = para.wrap(width, 9999)
    return h

# Y-cursor starts here
y = PAGE_H - MT
```

Canonical reference script: `build_redhat_cv_v3.py` (outputs folder).
Always print bottom margin remaining at end of script to verify page fill.

---

## ATS Rules

- No PDF tables used for layout (skills/education use manual column drawing)
- No text boxes, columns, or graphics in the document structure
- Standard section headings only
- Single-column main layout
- Keywords woven naturally into text — never keyword-stuffed
