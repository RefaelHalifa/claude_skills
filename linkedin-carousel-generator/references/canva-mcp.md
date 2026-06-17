# Mode C — Canva Live (via the Canva MCP)

Builds the carousel as a real design in the user's Canva account and exports a ready-to-post PDF.
**Honest constraints — tell the user up front:**
- Canva's generator is AI-driven. Layout, spacing, and exact fonts are Canva's interpretation, NOT a
  pixel match of the Style Profile. **Font family cannot be set via the API** (you can change color,
  size, italic, weight, alignment after generation, but not the typeface).
- Multi-slide designs come through the **presentation** flow, which requires the user to approve an
  outline in a popup widget. Presentations default to 16:9; resize to a square/portrait carousel if
  desired with `resize-design`.
- For slides that exactly match the sample, use Mode B (HTML). Use Mode C when the user wants it to
  land directly in their Canva account with minimal manual work.

Tool names below omit the server prefix; the live tools are `mcp__<canva-server>__<name>`.

## Preconditions
1. Check a Canva tool is available this session (search for `generate-design` / `create-design-from-candidate`).
   If none, STOP this mode: fall back to Mode A and tell the user the Canva connector isn't connected.
2. Optional brand: ask if they want an on-brand result; if yes, `list-brand-kits` → pass `brand_kit_id`.

## Step sequence
1. **Write the slide copy first** using the normal `/carousel` workflow (flow + layout rotation +
   the 6 hard rules). This copy is the source of truth; Canva only renders it.

2. **Outline review** — call `request-outline-review` with one outline entry per slide:
   - `title` = the slide headline.
   - `description` = the body/sub copy PLUS a style cue, e.g. "layout: bullet-list, max 4 bullets;
     accent word 'X' in orange italic; page number 3 bottom-left."
   Wait for the user to approve the outline in the widget. If they edit it, re-call
   `request-outline-review` with the updated outline; do not skip ahead.

3. **Generate** — after approval, call `generate-design-structured`:
   - `design_type`: `presentation`
   - `topic`: the carousel subject (≤150 chars)
   - `audience`: e.g. "LinkedIn — developers, recruiters, founders"
   - `length`: the slide count (e.g. "7 slides")
   - `style`: paste the Style Profile feel —
     "Warm off-white paper background (#F2F1ED), vivid orange accent (#ED4B1F), black ink text.
      High-contrast serif headlines with the first phrase in orange italic. Clean sans body. Minimal,
      editorial, lots of whitespace. Wordmark 'Refael' top-right, orange page number bottom-left."
   - `presentation_outlines`: the same array from step 2.
   - `brand_kit_id`: only if the user chose one.

4. **Create the editable design** — `generate-design-structured` returns design *candidates* (each
   with a `candidate_id` + the job `id`), NOT a finished design. Show the user the candidate preview
   URLs, then call `create-design-from-candidate` with the chosen `candidate_id` + `job_id` to get the
   real `design_id`. Then `get-design` / `get-design-pages` for page and element IDs if editing.

5. **(Optional) Precision pass** — if the generated copy drifted or accent words aren't styled:
   - `start-editing-transaction` (returns `transaction_id` + `pages`).
   - `perform-editing-operations`:
     - `replace_text` / `find_and_replace_text` to set each slide's copy to the exact spec.
     - `format_text` with `{ "color": "#ED4B1F", "font_style": "italic" }` on each accent word, and
       `{ "color": "#ED4B1F" }` on page numbers.
   - `commit-editing-transaction` (MANDATORY — uncommitted edits are lost). Never tell the user it's
     saved before committing.

6. **(Optional) Square/portrait** — if they want 1:1 or 4:5 instead of 16:9, `resize-design`.

7. **Export** — `get-export-formats` then `export-design` `{ "type": "pdf" }`. Give the user the
   returned download URL and tell them: LinkedIn → start a post → document → upload this PDF.

## Fallback
Any failure (connector missing, generation error twice, export unsupported) → produce Mode A outline
instead and tell the user why, so they always leave with something usable.
