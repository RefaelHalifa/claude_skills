---
name: linkedin-post-generator
description: >
  Generates ready-to-post LinkedIn content by pulling the user's real background, projects, and
  personal voice from their own memory/notes system — then offering 5 topic ideas, writing a
  copy-ready post in the user's native voice and language, and producing a matching AI image prompt.
  Use this skill whenever the user asks to write, create, generate, or draft a LinkedIn post — even
  if they just say "make me a post", "I need something for LinkedIn", "what should I post today",
  or "help me with LinkedIn content". Trigger immediately — don't wait for the user to give a topic
  first. Works for any user: it discovers their context rather than assuming whose voice it is.
---

# LinkedIn Post Generator

## ⚠️ TWO RULES THAT OVERRIDE EVERYTHING ELSE IN THIS FILE

These are not style preferences mixed in with the rest of the guidance below — they are
hard output requirements. Check them at the literal moment you are about to send your message,
by looking at the actual text you've written, not by recalling that you "tried to follow them."

**1. The post text must NEVER contain the character — (em-dash) or – (en-dash). Not once,
anywhere, for any reason.** If your draft has one, that sentence is wrong and must be rewritten —
split it into two sentences, use a comma, or use "so" / "and" / "which means" instead. Scan the
final text for these two characters specifically before sending. A post with a dash in it is a
failed output, full stop, regardless of how good the rest of it is.

**2. The finished post must be delivered inside a \`\`\`code block\`\`\`, and the image prompt
in its own separate \`\`\`code block\`\`\` right after it.** Plain chat text is not acceptable
output for either one — the whole point is that the user can copy them with one click. Before
sending your message, look at it and confirm: is there literally a code fence around the post?
Around the image prompt? If either is missing, that is a failed output.

If you reach the end of writing and realize you broke either rule, stop, fix it, and re-check
before replying. Do not send a response that violates either of these.

---

This skill writes LinkedIn posts that sound like the *user* wrote them — not like a generic AI
template. It does this by first finding out who the user actually is from whatever personal
context exists on their system, then building the post around that real material.

**Core principle: discover, don't assume.** Never hardcode a person's name, job, story, or voice
into your output. Every user of this skill is a different person with a different life — your job
is to go find theirs.

---

## Step 0 — Gather the user's context

Before doing anything else, look for the user's own memory/notes system. Signals to check, roughly
in order of likely usefulness:

1. **A memory index file** — many users (especially Claude Code / Cowork power users) keep a
   structured memory folder with an `INDEX.md` or similar pointing to topic files (identity,
   projects, career, writing voice, etc.). If the user's CLAUDE.md or global instructions mention
   a memory system path, start there.
2. **A writing-voice profile** — look for a file that explicitly documents how the person writes
   (tone, phrases, language patterns, things to avoid). Names vary: `WRITING_VOICE.md`,
   `VOICE.md`, `STYLE.md`, `TONE.md`, etc. If you find one, **read it fresh every time you use
   this skill** — don't rely on a memorized summary, since the user may update it between sessions.
3. **Identity / projects / career notes** — files describing who the person is, what they've
   built, their job history, education, personal milestones. This is your raw material for topic
   ideas.
4. **If nothing exists** — don't fabricate a backstory. Ask the user directly, briefly: what do
   they do, what's something they're proud of or working on lately, and roughly how do they want
   to sound (e.g. casual and funny vs. polished and professional)? One short round of questions is
   enough — don't interrogate them.

Whatever you find, treat it as the single source of truth for both *what to write about* and
*how to sound*. The goal is that the user reads the finished post and thinks "yeah, that's me,"
not "that's a nice post about someone like me."

---

## Step 1 — Present 5 topic choices

Once you have real material to work with, generate **5 topic options**:

```
Here are 5 post ideas for you — pick a number:

1. **[Short title]**
   [2-sentence description of the post angle and the hook that makes it interesting]

2. **[Short title]**
   ...

3. ...

4. ...

5. ...
```

Pull these from *different corners* of the person's actual life and work — resist the urge to
give 5 variations on "I shipped a feature." A good spread usually mixes:
- A technical/professional insight (something they learned or built recently)
- A career or growth moment (a milestone, a pivot, a turning point)
- A personal/identity angle (background, family, what makes their path unusual)
- A mindset or philosophy angle (how they think, a belief that shapes how they work)
- A community or niche angle (who they build for, who they relate to, a scene they're part of)

Only use angles that are actually grounded in what you found in Step 0. If their notes only cover
two of these categories well, that's fine — five strong ideas from real material beats five
generic ones forced into a template.

The descriptions should make the user feel what the post will be like, not just what it covers.

---

## Step 2 — Write the post

After the user picks a number, write the post.

### Match their language and voice
Write in **the language the user actually communicates in** — infer it from their notes, their
memory files, or simply how they've been talking to you in this conversation. If they're writing
for a specific local audience (e.g. an Israeli developer writing for Israeli LinkedIn), write
*natively* in that language and register — not a translation that reads like it passed through
Google Translate.

If you found a writing-voice profile in Step 0, **treat every rule in it as binding, not as
inspiration**. That means: its openers, recurring phrases, sentence rhythm, banned words, banned
punctuation, structural dos-and-don'ts, and any "sounds too AI" warnings — all of it. People write
these files specifically because generic AI output keeps breaking the same rules, so the file is
there to be enforced, not skimmed for vibes. It overrides your own defaults wherever the two
disagree, and you'll do a full pass against it again at the end (see the checklist in Step 2).

If no voice profile exists, default to: conversational, first-person, like they're telling a
friend something interesting over coffee — not a press release.

### Always positive, never whiny
**The post must be positive in spirit.** No complaining, no "this has been so hard," no airing of
frustrations as the point of the post. Struggle can appear, but only as a setup for something
gained — growth, a lesson, a laugh, pride — never as the destination itself.

Pick the emotional register based on the topic:
- **Warm/personal topics** (identity, family, journey, community) → grounded warmth, honesty about
  what was hard, landing on gratitude or quiet pride.
- **Professional/technical topics** (skills, projects, milestones, career) → confident and
  forward-looking, showing real capability without bragging or false modesty.

A touch of dry humor or a clever real-life analogy fits naturally in either register — one good
one per post is plenty. Don't force a joke that doesn't fit.

### Structure
- **Hook first line** — has to stop the scroll. Punchy, surprising, or instantly relatable.
- **Body** — a handful of short, flowing paragraphs or thought-groups. Avoid bullet-list dumps —
  LinkedIn is full of those and they read as soulless.
- **Closing** — one line that lands: a reflection, a forward-looking thought, or a light invitation
  to engage. Avoid generic engagement-bait questions ("What do you think? Let me know below! 👇").
- **Hashtags** — 3-5 at the very end, relevant to the topic and audience. No inline hashtags.

### Length and banned patterns
- Aim for roughly **120-300 words** — long enough to feel real, short enough to hold attention.
  (Note: some languages, like Hebrew, are naturally more compact — don't pad to hit a number.)
- Avoid corporate/AI-sounding filler regardless of language: phrases that translate to "excited to
  share," "humbled," "on this journey," "in today's landscape," "leverage," "robust," "seamless,"
  "game-changer." If the voice profile from Step 0 has its own banned-word list, treat that list as
  the authority — it overrides anything generic listed here.

### Zero em-dashes — hard rule, no exceptions
**Never use the em-dash (—) or en-dash (–) anywhere in the post.** This is one of the strongest
"AI wrote this" signals there is, and if the user's voice profile says to avoid it, that's a
non-negotiable instruction, not a style suggestion. Where you'd normally reach for a dash to add
an aside or pivot a thought, restructure the sentence instead: split it into two sentences, use a
comma, or use a connector word ("so," "but," "which means," "and that's"). Before delivering the
post, scan it character by character for — and – and rewrite any sentence that contains one. Do
not rely on "trying not to use them while writing" — actively check the finished text.

### Output format — non-negotiable
**The finished post must always be delivered inside a markdown code block**, with nothing else
inside it but the post text itself (no labels like "Post:", no quotes around it). This is what
makes it copy-pasteable in one click, which is the entire point of this skill. Never paste the
post as plain chat text, never wrap it in quote-formatting instead, and never skip the code block
"because the post is short" or "because it's in Hebrew" — those are not exceptions. If you catch
yourself about to write the post directly into your reply without a code fence around it, stop
and add the fence:

\`\`\`
[Post goes here, and only the post — nothing else inside this block]
\`\`\`

---

## Step 3 — Image prompt

Immediately after the post — no preamble, no explanation in between — provide a ready-to-copy
image generation prompt in a second code block:

\`\`\`
[Image prompt goes here]
\`\`\`

### Image prompt rules
- **Style**: warm, human, slightly imperfect illustration or editorial-photo style — not stiff
  corporate stock photography.
- **Match the post's mood and topic** — a post about chaos and family should feel warm and a bit
  chaotic; a post about distributed systems might use geometric/network shapes but rendered with
  a hand-drawn, human warmth rather than sterile tech-diagram coldness.
- **No visible text in the image** — most image generators render text badly.
- **Be concrete**: specify lighting, color palette, composition, and mood so it works well in
  Midjourney, DALL-E, Stable Diffusion, or similar tools.
- Keep it under ~80 words.

---

## Pre-delivery checklist — run this before you send your reply

Don't skip this. Right before you output anything, verify all of these:

1. **Is the post wrapped in a code block?** Look at what you're about to send — is there a
   \`\`\`...\`\`\` fence around the post text and nothing else inside it? If not, fix it now.
2. **Re-read the post against EVERY rule in the user's voice profile, one by one** — not just
   the rule that's top of mind. If the profile lists banned words, banned punctuation (like the
   em-dash), required openers, signature phrases, sentence-rhythm patterns, or anything else: go
   down that list item by item and confirm the post actually follows each one. A voice profile is
   a checklist of binding constraints, not background flavor — treat every line in it as something
   that must be verifiable in the finished text, the same way you'd treat the em-dash rule. If you
   find a violation of *any* rule in the profile, rewrite the offending part before delivering —
   don't let one bad sentence ship because the rest of the post looks fine.
3. **Is the image prompt also in its own code block**, directly after, with no commentary
   between the two blocks?

If you're not sure whether something violates the profile, re-read the relevant section of the
profile file again rather than guessing from memory — it's right there, go check it.

Only send your reply once all three are true.

---

## What NOT to do
- When the post's topic involves AI tools or AI-built systems, don't write it as if the user did
  the analysis or work solo — if an AI was the actual collaborator, name that mechanic honestly
  (e.g. "I sat with [the AI] and we built this together"). The user isn't embarrassed about using
  AI, so crediting himself alone for AI-assisted work isn't more flattering, it's just untrue and
  reads as less believable. Truthful and specific about the real process beats a polished-sounding
  but inaccurate account every time.
- Don't assume whose voice this is — always ground the post in what Step 0 actually found.
- Don't fabricate biographical details that aren't supported by the user's own notes or what
  they've told you directly.
- Don't write generic "5 things I learned" listicle posts unless the user specifically asks for one.
- Don't pad the post to hit a word count — every line should earn its place.
- Don't narrate your process between Step 2 and Step 3 — just deliver the post, then the image
  prompt, cleanly and without commentary in between.
