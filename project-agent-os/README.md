# project-agent-os

A Claude skill that builds complete, ready-to-use Claude Project agents from scratch.

Describe what your agent should do — it produces a fully structured system prompt, memory files, and a knowledge base reference file, all optimized for token efficiency and multi-session consistency.

---

## What It Builds

For every agent, the skill produces:

| Output | Description |
|--------|-------------|
| `INSTRUCTIONS.md` | Complete system prompt, ready to paste into Claude Project |
| Memory file schemas | Structure definitions for all persistent memory files |
| `AGENT_REFERENCE.md` | Token-saving knowledge base file for the project |
| Setup checklist | Numbered steps for exactly what to create and where |

---

## What the Agent OS Includes

Every agent built with this skill gets four layers:

**Identity & Roles** — Who the agent is, what roles it plays (teacher, mentor, manager, coach), and how it relates to the user.

**Behavior System** — How the agent behaves during sessions: step-by-step flow with confirmation gates, concept introduction rules, revisited concept reminders, feedback style.

**Memory System** — Automatic persistent memory across sessions using Claude Project knowledge base files. Supported file types:

- `SESSION_LOG.md` — What was done each session, one-liner format
- `PROGRESS.md` — Phase, status, milestones, expected completion
- `BUILD_PLAN.md` / `ROADMAP.md` — Day-by-day or phase-by-phase plan, created once at kickoff
- `ARCHITECTURE.md` / `DECISIONS.md` — Key decisions made by agent or user, with reasoning
- `PREFERENCES.md` — User learning patterns and work habits, auto-observed over time
- `CALENDAR_SYNC.md` — Live calendar state, rebuilt every session via Google Calendar MCP

**Commands & Protocols** — Automatic session start/end protocols, auto-capture rule, and optional commands:

- `manage memories` — Full memory audit and rebuild from session history
- `sync calendar` — Force Google Calendar MCP sync
- Kickoff protocol — First session onboarding and plan creation
- Missed day recovery — Automatic detection and plan adjustment

---

## File Structure

```
project-agent-os/
├── SKILL.md                          # Main skill — 5-step build process
└── references/
    ├── os-layers.md                  # Design guide for all four OS layers
    ├── memory-templates.md           # Ready-to-use schemas for every memory file type
    └── token-rules.md                # What goes in instructions vs. knowledge base
```

---

## How to Use

Install this skill into your Claude environment, then trigger it by saying things like:

- "Build me an agent for [purpose]"
- "Create a Claude Project for [domain]"
- "I want an agent that helps me with [goal]"
- "Design a system prompt for a project agent"
- "Add memory and calendar awareness to this existing prompt"

The skill will interview you, design the full OS, and produce all output files ready to copy-paste.

---

## Design Principles

**Memory over re-explanation** — The agent never asks for context it can find in memory files.

**Token efficiency by design** — Static content lives in the knowledge base, not in instructions. Target: under 400 lines / 1500 tokens per system prompt.

**One-liners in memory** — All log entries, preferences, and decisions are maximum one sentence.

**Calendar truth** — Dates always come from Google Calendar MCP, never from assumption.

**Silent memory updates** — The agent never interrupts a session to announce it saved something.

**First session vs. continuation** — Kickoff runs once only. Every subsequent session picks up exactly where the last one left off.

---

## Token Savings

A well-built agent using this skill targets:

| | Without skill | With skill |
|--|---------------|------------|
| Instructions size | ~1,800 tokens | ~1,150 tokens |
| Savings per session | — | ~650 tokens (~35%) |
| Savings per 10-session project | — | ~6,500 tokens |

---

## Built From

This skill was designed based on a real backend engineering mentor agent, iteratively improved across sessions to solve:
- Plan being rebuilt every session instead of persisted
- Calendar date mistakes and missed day blindness
- No architectural or preference memory
- Token waste from examples and static content in instructions
- Teaching dumps (all steps at once) instead of step-by-step gated flow

---

## Version

`v1.0.0` — Initial release
