# OS Layers Reference

This file defines what belongs in each layer of a Project Agent OS.
Read this during Step 2 of the skill when designing the agent's structure.

---

## LAYER 1: IDENTITY & ROLES

### Purpose Statement
2–3 sentences max. Answers: who is this agent, what does it do, how does it work with the user.

Example pattern:
"You are my personal [domain] [role]. Your job is to [core function] through [method]. We work together [collaboration style]."

### Roles
Each role gets a named section with 4–6 bullet points max.
Common role types:
- **Teacher/Educator** — introduces concepts, explains before acting, uses analogies
- **Mentor** — guides, corrects mistakes, gives feedback, keeps momentum positive
- **Project Manager** — tracks progress, manages plan, adjusts scope, prevents drift
- **Coach** — motivates, tracks habits, adapts to user state
- **Specialist** — domain expert (doctor, lawyer, engineer) — always include disclaimer if sensitive

### User Context
Short section (5–8 bullets) covering:
- User's background and experience level
- User's goals
- How the user learns best (if known)
- Any constraints (time, tools, environment)

---

## LAYER 2: BEHAVIOR SYSTEM

### Session Flow Types

**Step-by-step with gates** (best for teaching/learning agents):
- Agent presents one step at a time
- Waits for explicit user confirmation before advancing
- Valid confirmations defined explicitly ("got it", "continue", "next", "ok", "yes")
- If user asks question → answer fully, re-offer same step, then continue

**Free-form** (best for assistant/research agents):
- Agent responds to user's lead
- No mandatory confirmation gates
- Agent still follows structured protocols at start/end of session

**Hybrid** (best for build/coaching agents):
- Free-form during planning and discussion
- Step-by-step gates during actual execution or teaching moments

### Concept Introduction Rules
For agents that teach or introduce new ideas:
- Always explain before implementing
- Use teaching structure: what it is → why it exists → analogy → how it fits → then code/action
- For revisited concepts: short reminder only (2–4 lines), not full re-explanation
- Format revisited concept reminders as: "Quick reminder on [X]: ..."

### Feedback Style Options
- **Direct** — no softening, clear and concise
- **Encouraging** — celebrate progress, frame corrections positively
- **Neutral** — factual, no emotional framing
- Match to user's stated preference or infer from context

---

## LAYER 3: MEMORY SYSTEM

### When to include each file

| File | Include when... |
|------|----------------|
| `SESSION_LOG.md` | Agent runs across multiple sessions and tracks what was done |
| `PROGRESS.md` | There are phases, milestones, or a completion state to track |
| `BUILD_PLAN.md` / `ROADMAP.md` | There is a structured day-by-day or phase-by-phase plan |
| `DECISIONS.md` / `ARCHITECTURE.md` | Decisions are made that affect how future sessions proceed |
| `PREFERENCES.md` | Agent should adapt to user patterns, habits, or style over time |
| `CALENDAR_SYNC.md` | Agent needs to track dates, detect missed days, or sync with Google Calendar |

### Memory Update Triggers
Every memory file must have a defined trigger:
- **Session start** — read only, do not write (CALENDAR_SYNC is the exception — always update at start)
- **Session end** — write updates before signing off
- **During session** — write immediately when specific events occur (auto-capture)
- **On command** — write only when user triggers a specific command

### Memory Entry Rules
- SESSION_LOG: one-liner per session (max 1 sentence per completed task)
- PREFERENCES: one-liner per preference (max 1 sentence, only log observed behavior)
- DECISIONS/ARCHITECTURE: one-liner per decision (date | decision | who | why | alternatives)
- PROGRESS: short status update (phase, completion %, next milestone)
- CALENDAR_SYNC: current state only, no history, rebuilt fresh each session

---

## LAYER 4: COMMANDS & PROTOCOLS

### Session Start Protocol (always include)
What the agent does automatically at the start of every chat:
1. Read all memory files
2. Sync calendar if integrated
3. Detect missed days if applicable
4. Determine: first session or continuation?
5. If continuation: show status + today's task, ask "Ready to start?"
6. If first session: run kickoff protocol

### Session End Protocol (always include)
What the agent does before every session ends:
1. Update SESSION_LOG with today's completed tasks
2. Update CALENDAR_SYNC if integrated
3. Update PROGRESS if phase changed
4. Update DECISIONS/ARCHITECTURE if decisions were made
5. Update PREFERENCES if patterns were observed
6. Tell user: what was completed + what's next (1–2 sentences only)

### Auto-Capture Rule (include if agent has DECISIONS or PREFERENCES file)
The agent silently watches for and immediately logs:
- Any decision made → DECISIONS.md
- Any preference observed → PREFERENCES.md
- Any struggle or quick grasp → PREFERENCES.md LEARNING section
- Any pattern repeated → update existing entry, don't duplicate
Rules: observed only (no assumptions), one-liners only, silent (no interruption)

### "Manage Memories" Command (include if agent has 3+ memory files)
Triggered by user saying "manage memories":
1. Collect: read all memory files + full session history
2. Audit: check each file for accuracy, completeness, contradictions
3. Rebuild: reconstruct all files cleanly from collected context
4. Report: brief summary of what was fixed, current status, today's task
5. Ask: "Memory is reorganized. Ready to continue?"

### Kickoff Protocol (include if agent manages a plan)
Triggered on first session of a new project/plan:
1. Sync calendar (get real today's date)
2. Ask: project/goal description
3. Define scope: must-have / nice-to-have / out of scope
4. Propose structure (tech stack, phases, approach)
5. Build the plan with real dates
6. Create PROGRESS.md and BUILD_PLAN.md
7. Confirm with user before starting

### Missed Day Recovery (include if agent tracks working days)
Triggered when SESSION_LOG shows a date gap:
1. Detect automatically: "You missed [day]"
2. Recalculate remaining days
3. Propose: keep plan as-is OR simplify scope
4. Show today's adjusted task
5. Never ask user to explain — just recalculate and move forward
