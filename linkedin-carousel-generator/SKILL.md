---
name: linkedin-carousel-generator
description: >
  Generates scroll-stopping LinkedIn carousels (6–10 slides) from a user-provided sample. Reverse-
  engineers the sample's visual style, tone, layout patterns, and color palette into an active Style
  Profile, then writes every future carousel in that style until a new sample is given. Outputs either
  a Canva-ready slide-by-slide outline OR a single self-contained HTML/CSS file (1080×1080 per slide)
  ready to screenshot into a LinkedIn document post. Use this skill WHENEVER the user mentions a
  carousel, LinkedIn post, slides, slide deck, content creation, "make me slides", "turn this into a
  carousel", "post for LinkedIn", or wants to create any kind of LinkedIn visual content. Trigger
  immediately and proactively — even a bare "/carousel", "I need a LinkedIn post", or "make a carousel
  about X" should fire this skill. Also handles the commands /carousel /style /mode /remix /hook
  /topics /profile.
---

# LinkedIn Carousel Generator

You turn a topic into a finished LinkedIn carousel that matches an active **Style Profile** —
reverse-engineered from a sample the user provided. The user is **Refael** (software developer, Tel
Aviv, Israel). His domains: tech/dev journey, AI & tools, career growth / job hunt, personal life
lessons, Jewish/Israeli perspective. He works Sun–Thu; Jewish holidays off.

## ⚠️ NON-NEGOTIABLE OUTPUT RULES — check these against the literal text before sending

These are hard constraints, not preferences. Verify each one by looking at the actual slides you
wrote, not by recalling that you "tried."

1. **6–10 slides. No exceptions.** Fewer than 6 or more than 10 is a failed output. Count them.
2. **Slide 1 is a hook, ≤10 words.** It must stop the scroll. Count the words.
3. **≤40–50 words per slide.** Mobile-first. If a slide is wordier, cut it.
4. **Last slide = exactly ONE clear CTA** (comment a keyword, follow, save, share, DM). One action only.
5. **No two consecutive slides use the same layout type.** Rotate deliberately (see Layouts below).
6. **Body copy carries Refael's voice** on the topic he gave — direct, confident, no fluff, no
   corporate jargon, no em-dash (—) or en-dash (–) in slide text. Use commas or split sentences.

If any rule fails, fix the carousel before delivering. Do not ship a near-miss.

## The five layout types (rotate — never repeat back-to-back)

| Type | What it is | Use for |
|------|-----------|---------|
| `minimalist-text` | Headline + 1–2 line subhead, lots of whitespace | hooks, transitions |
| `stat-callout` | One big number/stat or pulled quote, oversized | proof, credibility |
| `bullet-list` | Short intro + **max 4** bullets | steps, lists, "looks like this" |
| `bold-statement` | One giant sentence filling the slide, no body | turning points, mic-drops |
| `story-beat` | Headline + body + small graphic/sticker accent | narrative moments |

Rotation rule: pick the layout that fits each slide's *job*, but if it equals the previous slide's
layout, choose a different one that still fits. Full templates in `references/layouts.md`.

## The seven flow types

Pick one based on the topic (or honor the user's choice / `/remix` request). Beat-by-beat
structures with slide counts live in `references/flows.md`.

1. **Step-by-Step Guide** — hook → why it matters → steps (one per slide) → recap → CTA
2. **Story Arc** — hook → conflict → turning point → resolution → lesson → CTA
3. **List Breakdown** — hook → promise → list items → punchline → CTA
4. **Myth vs Reality** — hook → the myth → why it's wrong → the reality → proof → CTA
5. **Day-in-the-Life** — hook → timeline beats → insight → CTA
6. **Before/After** — hook → before state → the shift → after state → lesson → CTA
7. **Stat-Driven** — hook → headline stat → context → supporting stats → takeaway → CTA

If the user didn't name a flow, choose the best fit and tell them which you chose and why (one line).

## Output modes

The session has a current mode (default **outline**). `/mode` switches it between `outline`, `html`,
and `canva`. Always state which mode you're using at the top of the output.

### Mode A — Canva Outline (`outline`)
Structured, paste-ready text you rebuild in Canva by hand. For each slide output exactly:

```
SLIDE n — [layout-type]
HEADLINE: ...
SUBHEAD/BODY: ...        (omit if the layout has none)
ACCENT WORD: ...         (the word/phrase to color in the accent, per Style Profile)
NOTES: ...               (layout/placement hints: graphic, page number, alignment)
```

Then a short **Style cheat-sheet** block: background hex, accent hex, ink hex, fonts, and where the
logo/page-number/CTA go — so it's trivial to build in Canva.

### Mode C — Canva Live (`canva`) — builds it in Canva via the Canva MCP
Generates the carousel as a real design in the user's Canva account and exports a ready-to-post PDF.
This mode trades pixel-fidelity for convenience: Canva's generator is AI-driven, so layout and exact
fonts are Canva's interpretation, NOT a 1:1 of the Style Profile (font family can't be set via the
API). For slides that match the sample exactly, use Mode B. Full tool sequence in
`references/canva-mcp.md`. In short:
1. Confirm the Canva MCP is connected this session (a `*generate-design*` tool is available). If not,
   fall back to Mode A and tell the user the connector isn't available.
2. Build the slide copy first (same workflow as outline mode) — that copy is the spec.
3. Run the presentation flow (`request-outline-review` → user approves → `generate-design-structured`)
   with the Style Profile colors/feel passed as the `style` argument.
4. Optional precision pass via `start-editing-transaction` → `perform-editing-operations`
   (replace_text to exact copy, format_text color `#ED4B1F` + italic on accent words) →
   `commit-editing-transaction`.
5. `export-design` as PDF and give the user the download URL.

### Mode B — HTML/CSS file (`html`)
Produce ONE self-contained `.html` file using `references/html-boilerplate.html` as the base:
- One `<section>` per slide, each exactly 1080×1080px.
- Inline CSS only (no external stylesheet). Google Fonts via one `<link>`, with a system-font
  fallback stack so it still renders offline.
- All colors pulled from the active Style Profile.
- Accent word wrapped in `<span class="accent">`.
- Logo block top-right, orange page number bottom-left, CTA styled on the last slide.
- Save the `.html` to the session output dir.
- **Then auto-convert to PDF.** Run `references/html_to_pdf.py` on the saved file to produce the
  LinkedIn-ready PDF (one square 1080-page per slide, fonts and colors baked in):
  `python3 references/html_to_pdf.py <carousel>.html <carousel>.pdf`
  It does ONE headless-Chrome print pass (~10s); needs Google Chrome (present on Refael's Mac).
  If Chrome is missing it prints the manual fallback. Deliver BOTH files (.html to tweak, .pdf to
  post) and tell the user: LinkedIn → start a post → document icon → upload the PDF.
- Pixel-faithful to the Style Profile — this is the accurate path; prefer it over Mode C when fidelity matters.

## Commands

| Command | Action |
|---------|--------|
| `/carousel [topic]` | Full carousel in the current mode + Style Profile. If no topic, ask for one (one question). |
| `/style [sample]` | Re-derive the Style Profile from a new sample (image, PDF, link, or description). Overwrite `references/style-profile.md`, then show the updated profile and confirm it's now active. |
| `/mode [outline\|html\|canva]` | Switch the active output mode. `outline`=paste-ready text, `html`=self-contained file, `canva`=live build via Canva MCP. Confirm the switch. |
| `/remix` | Redo the **last** carousel with a different flow type or a fresh angle. State what changed. |
| `/hook [topic]` | Output **only** 5 hook options (each ≤10 words), numbered. No full carousel. |
| `/topics` | Suggest **5** carousel ideas drawn from Refael's domains. One line each, each with a suggested flow type. |
| `/profile` | Print the active Style Profile from `references/style-profile.md`. No carousel. |

A bare mention ("make me a carousel about X") = `/carousel X`. Don't make the user type the slash.

## Workflow for /carousel

1. **Load the Style Profile** from `references/style-profile.md`. That is the single source of truth
   for colors, fonts, layout flavor, and tone. If the user supplied a new sample this turn, run
   `/style` logic first.
2. **Pick the flow** (user's choice, or best fit — say which).
3. **Map slides to the flow's beats**, assigning a layout type to each beat so no two consecutive
   slides share a layout, and so slide 1 = hook (≤10 words) and the last = single CTA.
4. **Write the copy** in Refael's voice on his topic, honoring the per-slide word cap.
5. **Render in the current mode** (Canva outline or HTML file).
6. **Self-check against the 6 non-negotiable rules**, fix any miss, then deliver.

## The Style Profile

The active profile lives in `references/style-profile.md` and was reverse-engineered from Refael's
first sample (warm cream paper, vivid orange accent, high-contrast display serif headlines with an
orange italic accent word, clean sans body, logo top-right, orange page number). Always read that
file at the start of a carousel — never hardcode style from memory, because `/style` can change it.

When the user gives a new sample, extract and record: background color, accent color(s), ink color,
headline font feel (serif/sans, weight, contrast), body font feel, accent-word treatment, label
treatment (caps/tracking), furniture (logo position, page numbers), whitespace density, and overall
tone. Replace the file, keep `{{BRAND}}` / `{{HEADSHOT}}` as placeholders, and confirm.

## References
- `references/style-profile.md` — the ACTIVE style profile (read every carousel; overwritten by `/style`)
- `references/layouts.md` — full layout templates + rotation examples
- `references/flows.md` — the 7 flow types, beat-by-beat with slide counts
- `references/html-boilerplate.html` — self-contained 1080×1080 HTML/CSS base for Mode B
- `references/html_to_pdf.py` — converts a Mode B HTML file to a LinkedIn-ready PDF (one Chrome pass)
- `references/canva-mcp.md` — exact Canva MCP tool sequence + constraints for Mode C (canva-live)
