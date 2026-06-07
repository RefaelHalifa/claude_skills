---
name: project-agent-os
description: >
  Build a complete Claude Project Agent OS — a fully structured system prompt + knowledge base
  files — for any project-based agent. Use this skill whenever a user wants to create a Claude
  Project agent that needs persistent memory, consistent behavior, calendar awareness, structured
  commands, and token efficiency. Trigger this skill when the user says things like "build me an
  agent", "create a Claude Project for", "I want an agent that helps me with", "design a system
  prompt for a project agent", "make an agent that tracks", or any request to set up a Claude
  Project with ongoing sessions, progress tracking, or multi-session continuity. Also trigger when
  a user shows an existing agent prompt and wants to add memory, calendar sync, behavior structure,
  or token optimization to it.
---

# Project Agent OS — Skill

This skill turns a description of what an agent should do into a complete, ready-to-use
Claude Project system: a system prompt (instructions) + knowledge base files, all designed
with memory, behavior consistency, calendar awareness, custom commands, and token efficiency.

---

## WHAT THIS SKILL PRODUCES

For every agent built with this skill, the output is always:

1. **`INSTRUCTIONS.md`** — The full system prompt, ready to paste into Claude Project instructions
2. **Memory file structures** — All `.md` files the agent will maintain in the knowledge base
3. **`AGENT_REFERENCE.md`** — Token-saving reference file for the knowledge base
4. **Setup checklist** — Exactly what to create, where, and in what order

Read `references/os-layers.md` for the full breakdown of what each layer contains and how to design it.
Read `references/memory-templates.md` for ready-to-use memory file templates and formats.
Read `references/token-rules.md` for the rules on what goes in instructions vs. knowledge base.

---

## STEP 0 — IDENTIFY PLATFORM TARGET

Before anything else, work out **where this agent will actually run** — that determines how
memory persists and how commands behave. Ask the user (in plain language, no jargon) or infer
from context which of these fits:

- **A — Claude Project** with a file-based knowledge base (the classic setup: paste instructions, create KB files)
- **B — claude.ai chat/Project using built-in memory** (no files — Anthropic's memory feature)
- **C — Cowork** (its own managed memory directory with an index + linked topic files)
- **D — Claude Code / a filesystem-backed agent** (real files, repo, possibly hooks/skills)

Read `references/platform-targets.md` now — it defines exactly how Layers 3 and 4 get built
in Steps 2–3 and how output artifacts are shaped in Steps 3–4 for each profile.

If the platform is unclear or the user doesn't know, **default to Profile A** and say so
explicitly ("I'll build this for a Claude Project with file-based memory unless you tell me
otherwise") — it's the skill's most mature, fully-specified path.

**Also determine here whether this is a from-scratch build or a retrofit.** If the user has
supplied an existing agent prompt and wants memory, calendar sync, behavior structure, or
token optimization added to it — skip to **STEP 1B — RETROFIT MODE** instead of Step 1.

### Filesystem platforms (Profiles C and D): check before you build

On Cowork and Claude Code — both real-filesystem platforms — **never assume the project is a
blank slate.** A memory/instructions system may already exist (a `CLAUDE.md`, a `memory/`
directory with an index file, hooks, existing skills, established frontmatter or naming
conventions). Building a parallel structure on top of one that already exists creates
duplication and conflicts — exactly what this skill is supposed to prevent.

Before designing anything:
1. **Look first** — `ls`/`find`/`Read` for `CLAUDE.md`, a `memory/` or similarly-named
   directory, an index file (`MEMORY.md`/`INDEX.md`), hooks, or skills that already manage
   persistence or instructions.
2. **If something exists**, treat this like retrofit mode (Step 1B) even if the user didn't
   frame it that way: audit the existing system against the four OS layers, map the new
   agent's needs onto its *existing* file names, frontmatter, and index conventions — don't
   invent new ones — and propose additive integration.
3. **Only design from scratch (Steps 1–5 as written) if nothing exists.**

See the "check for existing infrastructure first" note in `references/platform-targets.md`
Profiles C and D.

---

## STEP 1 — CAPTURE INTENT

Before writing anything, extract from the conversation or ask the user:

### Required
- **Agent purpose:** What does this agent do? (teach, manage, build, track, coach, etc.)
- **Domain:** What subject or field? (backend dev, iOS, language learning, fitness, etc.)
- **User background:** Who is the user? (experience level, goals, relevant context)
- **Session type:** Is this ongoing across many sessions or one-time?

### Memory needs (ask if not obvious)
- Does the agent need to track a **plan** that persists across sessions?
- Does it need a **session log** (what was done, what's next)?
- Does it need to track **decisions** made during sessions?
- Does it need to remember **what already exists** (built, drafted, filed, booked, completed artifacts) so the next session doesn't repeat or contradict it?
- Does it need to track **user preferences** or learning patterns?
- Does it need a **progress tracker** (phases, milestones, completion)?

### Schedule and calendar
- What are the user's **working days**? (default: Sunday–Thursday)
- Are there **rest days or holidays** to respect?
- Does the agent need **Google Calendar MCP** sync?
- Does it need to **detect missed days** and adjust plans?

### Behavior needs
- Does the agent have **multiple roles** (teacher, mentor, manager)?
- Should it follow a **step-by-step flow** with user confirmation between steps?
- Are there **custom commands** the user should be able to trigger? (e.g., "manage memories", "sync calendar", "weekly review")
- Should it **remind the user** of past concepts or decisions?
- Should it **offer proactive help** when it learns personally or logistically significant details? (insight trigger)
- Are there **domain-specific command rules** the agent must always follow? (e.g., always end git sequences with git push, always include error handling, always validate before submitting) → add to general rules in instructions

### External integrations
- Google Calendar (for date sync and holiday detection)?
- Google Drive (for file access)?
- Any other MCP connections?

### Token sensitivity
- Is this a **heavy session agent** (lots of code or content per session)? → More aggressive token optimization needed
- Or a **light session agent** (mostly conversation)? → Standard optimization

If any required field is missing, ask before proceeding. Do not guess.

---

## STEP 1B — RETROFIT MODE

Use this instead of Steps 1–4 when the user supplies an **existing agent prompt** and wants
memory, calendar sync, behavior structure, or token optimization added to it. Goal: improve
the agent without rebuilding it — preserve its voice, roles, and existing custom behavior.

1. **Confirm the destination platform** via Step 0 (the prompt's current home and its future
   home may differ — plan for where it will run, not where it came from).
2. **Audit**: map the existing prompt's content onto the four OS layers (Identity & Roles,
   Behavior System, Memory System, Commands & Protocols). For each layer, mark it
   present / partial / missing — mirror the structure in `references/os-layers.md`.
3. **Gap list**: write out concretely what's missing or weak (e.g., "no session-log
   equivalent," "no calendar fallback chain," "memory updates aren't silent," "no token split
   between instructions and reference content").
4. **Propose additive patches only — never a full rebuild.** Each patch is a small, clearly
   scoped insertion or edit, shown as a before/after or "insert after section X: ..." block,
   that preserves the original prompt's tone, roles, and behavior. Use the same memory file
   templates (`references/memory-templates.md`) and platform mechanics
   (`references/platform-targets.md`) as the from-scratch flow — only the *delivery format*
   changes (patches vs. full files).
5. **Present patches grouped by layer** and let the user approve or reject each independently.
6. Route every approved patch through the same instructions-vs-reference split rules as
   Step 3 (`references/token-rules.md`), so additions don't bloat the original prompt.

---

## STEP 2 — DESIGN THE OS LAYERS

Once you have the answers, design all four layers. Read `references/os-layers.md` for full guidance.

### Layer 1: IDENTITY & ROLES
Define who the agent is and what roles it plays.
- Name and purpose statement (2–3 sentences max)
- Roles (each with clear responsibilities)
- User context section (background, goals, experience level)

### Layer 2: BEHAVIOR SYSTEM
Define how the agent behaves during sessions.
- Session flow (step-by-step or free-form?)
- Confirmation gates (wait for user between steps?)
- Concept introduction rules (always teach before code/action?)
- Revisited concept rules (quick reminder vs. full explanation?)
- Feedback and correction style

### Layer 3: MEMORY SYSTEM
How these are persisted and recalled depends on the platform identified in Step 0 — read the
matching profile in `references/platform-targets.md` before designing concrete file/entry
structures. The list below is the platform-agnostic *concept* inventory; the profile tells you
whether each concept becomes a real file, a memory-tool entry, or a frontmattered topic file.

Choose which memory files this agent needs and design each one.
Always include at minimum:
- `SESSION_LOG.md` — if multi-session
- `PROGRESS.md` — if there is a plan or milestone structure

Add based on agent type:
- `BUILD_PLAN.md` or `ROADMAP.md` — if there is a day-by-day or phase-by-phase plan
- `DECISIONS.md` or `ARCHITECTURE.md` — if decisions are made that affect future sessions
- `PREFERENCES.md` — if the agent should adapt to the user over time
- `CALENDAR_SYNC.md` — if calendar awareness is needed
- `WORK_STATE.md` — if the agent produces artifacts across sessions (code, documents, bookings, designs) that the next session must not duplicate or contradict

Read `references/memory-templates.md` for the exact format of each file.

### Layer 4: COMMANDS & PROTOCOLS
What "read all memory files," "manage memories," and calendar sync actually *mean* in
practice depends on the platform — re-check `references/platform-targets.md` for the matching
profile before writing protocol wording (e.g. "manage memories" deep-scan tiers only exist
where session-history search is possible).

Define special commands and automatic protocols.
Always include:
- Session start protocol (what the agent does automatically at the start of every chat)
- Session end protocol (what the agent saves before signing off)
- Auto-capture rule (what the agent silently logs during sessions)

Add based on needs:
- "manage memories" command (memory audit and rebuild)
- "sync calendar" command
- "weekly review" or "resync" commands
- Kickoff protocol (for first session of a new project/plan)
- Missed day detection and recovery

---

## STEP 3 — BUILD THE OUTPUT FILES

Read `references/token-rules.md` before writing any file.

### Build order:
1. Write `INSTRUCTIONS.md` — the system prompt
2. Write the memory artifacts in the shape the platform actually uses (schemas/concepts only,
   not content — the agent fills them during sessions): real file schemas for Profiles A/D,
   memory-tool entry templates for Profile B, or `MEMORY.md` index entries + frontmattered
   topic files for Profile C. See `references/platform-targets.md` → "Output artifacts" for
   the exact shape per profile.
3. Write `AGENT_REFERENCE.md` — everything moved out of instructions to save tokens (note: on
   some platforms this may itself need to be a topic file or folded artifact rather than a
   standalone KB file — check the matching profile)
4. Write the setup checklist

### Instructions file rules:
- Include: identity, roles, behavior system, memory system (structure only, no examples), all protocols and commands, general rules
- Exclude: format examples, static reference content, resume/output standards → these go in AGENT_REFERENCE.md
- Target: under 400 lines, under 2000 tokens
- One-liner rules wherever possible

### Memory file rules:
- Provide the schema (field names, format, section headers) — not example content
- Include the update trigger (when does this file get written/updated?)
- Include the format line (one-liner? table? sections?)

### AGENT_REFERENCE.md rules:
- Include: format examples for all memory files, output standards, static reference content
- Add a header note: "Read only when needed — not every message"
- Organize by section with clear headers so agent can jump to the right part

---

## STEP 4 — PRESENT THE OUTPUT

Present everything in this order:

1. **Summary card** — Agent name, roles, memory files, commands, integrations (5–10 lines)
2. **`INSTRUCTIONS.md`** — Full system prompt in one copy-paste block
3. **Memory file schemas** — Each file's structure in its own block with its filename
4. **`AGENT_REFERENCE.md`** — Full reference file in one copy-paste block
5. **Setup checklist** — Numbered steps for what to create where

### Setup checklist format:
The shape below is for Profile A (Claude Project / KB files) — adapt it to the platform's
actual setup steps using its "Output artifacts" description in `references/platform-targets.md`.
For example: Profile B replaces "create KB files" with "enable/configure the memory tool";
Profile C replaces it with "place files in the managed memory directory with correct
frontmatter and link them from MEMORY.md"; Profile D uses real repo paths.

```
SETUP CHECKLIST
□ Step 1: Open your Claude Project → Settings → Instructions
          Paste the full INSTRUCTIONS.md content
□ Step 2: In Claude Project → Knowledge Base, create these files:
          - [filename].md (empty — agent will populate)
          - [filename].md (empty — agent will populate)
          - AGENT_REFERENCE.md (paste the full content provided)
□ Step 3: Start your first session and say "[kickoff trigger phrase]"
```

---

## STEP 5 — VALIDATE BEFORE DELIVERING

Before presenting, check:
- [ ] **Dry run**: mentally simulate a session start using the produced INSTRUCTIONS.md plus
      the initial memory artifacts — confirm every file/entry/topic the instructions reference
      actually got created in Step 3, every "read X" instruction has something to read, and the
      wording matches the platform's real recall mechanism (file read / memory-tool query /
      index-and-links / grep) per `references/platform-targets.md`
- [ ] Instructions are under 400 lines
- [ ] No format examples are inside instructions (they're in AGENT_REFERENCE.md)
- [ ] Every memory artifact has: name/path, update trigger, format rule
- [ ] Session start protocol reads/queries ALL memory artifacts (in the platform-appropriate way)
- [ ] Session end protocol updates ALL relevant memory artifacts
- [ ] Auto-capture rule is present if agent tracks decisions or preferences
- [ ] Calendar fallback follows the platform's actual chain (see `platform-targets.md`
      comparison table) — never a blanket "Google Calendar MCP, else system date" assumption;
      the fallback used is logged or surfaced, never silently assumed
- [ ] "manage memories" command is included if agent has 3+ memory artifacts, AND its
      deep-scan tiers (2–3) are present only where the platform actually supports
      session/transcript history search (Claude Code, Cowork) — otherwise they're explicitly
      omitted with a note to the user about the limitation
- [ ] Setup checklist is complete, numbered, and matches the platform's real setup steps

---

## DESIGN PRINCIPLES

These principles apply to every agent built with this skill:

**Memory over re-explanation**
The agent should never ask the user for context it could find in memory files. Memory is checked before any clarifying question is asked.

**Token efficiency by design**
Static content (examples, standards, reference formats) lives in the knowledge base, not in instructions. Instructions contain only behavior rules the agent needs every session.

**One-liners in memory**
All session log entries, preference entries, and decision entries are maximum one sentence. Density over length.

**Calendar truth**
Dates come from the platform's most reliable source first, in the fallback order defined per
profile in `references/platform-targets.md` (e.g. system clock → MCP for Claude Code; MCP →
ask the user for Claude Project/claude.ai; session context → MCP for Cowork). Never assumed
silently — whichever source was used gets logged or surfaced to the user.

**Silent memory updates**
The agent never interrupts a session to announce it saved something. All memory updates happen silently unless the user explicitly asks.

**Sensitive-data hygiene**
Certain categories — compensation/salary figures, contract financial terms, personal ID
numbers, credentials/secrets, raw health or legal specifics — must never be written verbatim
into persistent memory. Summarize or omit instead (e.g. "compensation discussion in progress,"
not the figure). Apply extra caution on platforms where the user doesn't fully control where
memory is stored — see `references/memory-templates.md` for the full rule and
`references/platform-targets.md` for which platforms warrant more care.

**Platform-aware mechanics**
The four-layer model (Identity, Behavior, Memory, Commands) is constant across every platform.
*How* Layers 3 and 4 are actually implemented — files, memory-tool entries, indexed topic
files, or a real filesystem — is decided once in Step 0 and threads through every later step.

**Commands are always available**
Custom commands ("manage memories", "sync calendar", etc.) work at any point in any session without needing setup or context re-establishment.

**First session vs. continuation**
The agent always detects whether this is the first session of a new project or a continuation. It only runs full kickoff/onboarding once — never again unless explicitly reset.
