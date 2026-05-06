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
- Does the agent need to track **decisions** made during sessions?
- Does the agent need to remember **what already exists** (built, drafted, filed, booked, completed artifacts) so the next session doesn't repeat or contradict it?
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

### External integrations
- Google Calendar (for date sync and holiday detection)?
- Google Drive (for file access)?
- Any other MCP connections?

### Token sensitivity
- Is this a **heavy session agent** (lots of code or content per session)? → More aggressive token optimization needed
- Or a **light session agent** (mostly conversation)? → Standard optimization

If any required field is missing, ask before proceeding. Do not guess.

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
Choose which memory files this agent needs and design each one.
Always include at minimum:
- `SESSION_LOG.md` — if multi-session
- `PROGRESS.md` — if there is a plan or milestone structure

Add based on agent type:
- `BUILD_PLAN.md` or `ROADMAP.md` — if there is a day-by-day or phase-by-phase plan
- `DECISIONS.md` or `ARCHITECTURE.md` — if decisions are made that affect future sessions
- `PREFERENCES.md` — if the agent should adapt to the user over time
- `CALENDAR_SYNC.md` — if calendar awareness is needed

Read `references/memory-templates.md` for the exact format of each file.

### Layer 4: COMMANDS & PROTOCOLS
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
2. Write memory file structures (schemas only, not content — agent fills them during sessions)
3. Write `AGENT_REFERENCE.md` — everything moved out of instructions to save tokens
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
- [ ] Instructions are under 400 lines
- [ ] No format examples are inside instructions (they're in AGENT_REFERENCE.md)
- [ ] Every memory file has: filename, update trigger, format rule
- [ ] Session start protocol reads ALL memory files
- [ ] Session end protocol updates ALL relevant memory files
- [ ] Auto-capture rule is present if agent tracks decisions or preferences
- [ ] If Google Calendar MCP is included: sync is triggered at session start AND end
- [ ] "manage memories" command is included if agent has 3+ memory files
- [ ] Setup checklist is complete and numbered

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
Dates always come from Google Calendar MCP (if integrated), never from assumption. If MCP is unavailable, fall back to system date and log the fallback.

**Silent memory updates**
The agent never interrupts a session to announce it saved something. All memory updates happen silently unless the user explicitly asks.

**Commands are always available**
Custom commands ("manage memories", "sync calendar", etc.) work at any point in any session without needing setup or context re-establishment.

**First session vs. continuation**
The agent always detects whether this is the first session of a new project or a continuation. It only runs full kickoff/onboarding once — never again unless explicitly reset.
