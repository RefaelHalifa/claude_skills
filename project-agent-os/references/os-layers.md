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

### Insight Trigger Rule
When the agent learns any personally or logistically significant detail during a session
(a date, an event, a deadline, a life change, a commitment), it should pause and offer
relevant help — never act automatically. Examples:
- Personal date learned → offer to add to Google Calendar
- Deadline mentioned → offer to block working days in calendar
- New tool or technology mentioned → offer to note in DECISIONS.md
- Life event mentioned → offer to adjust the plan around it
Keep the offer short (1–2 lines) and let the user decide.

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
| `WORK_STATE.md` | Agent produces artifacts across sessions that the next session must not duplicate or contradict — works for code files, legal drafts, event bookings, design components, or any domain |

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
- WORK_STATE: one entry per file/artifact, updated in place never deleted, includes last modified date

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
6. Update WORK_STATE: update in-place any file/artifact touched this session, add new entries for new files, mark removed files as REMOVED — never delete existing lines
7. Insight trigger: if any personally or logistically significant detail was shared this session, offer relevant help before signing off (calendar event, plan adjustment, memory note) — one offer, 1–2 lines, let user decide
8. Tell user: what was completed + what's next (1–2 sentences only)

### Auto-Capture Rule (include if agent has DECISIONS or PREFERENCES file)
The agent silently watches for and immediately logs:
- Any decision made → DECISIONS.md
- Any preference observed → PREFERENCES.md
- Any struggle or quick grasp → PREFERENCES.md LEARNING section
- Any pattern repeated → update existing entry, don't duplicate
- Any file/artifact created or significantly changed → WORK_STATE.md immediately
Rules: observed only (no assumptions), one-liners only, silent (no interruption)

### "Manage Memories" Command (include if agent has 3+ memory files)
Triggered by user saying "manage memories":

1. Collect using a tiered approach:
   - Tier 1: Read all memory files
   - Tier 2: Deep scan last 3–5 sessions — extract file names, imports, functions,
     decisions, preferences mentioned in chat but never saved to memory files
   - Tier 3: Light scan older sessions only if gaps remain after Tier 2 —
     search for the specific missing information only, not everything
   - Sync Google Calendar via MCP for date context
2. Audit: check each file for accuracy, completeness, contradictions
3. Rebuild: reconstruct all files cleanly — pay special attention to WORK_STATE,
   rebuilding one entry per file with full current state + last modified date,
   never deleting existing entries
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
2. Adjust today's task from the shifted plan
3. Update BUILD_PLAN.md: shift ALL future PENDING days to their new real dates
4. Sync to Google Calendar via MCP: update or create events for every shifted day
5. Update CALENDAR_SYNC.md with the new state
6. Show user: shifted day list (old date → new date, one line each) + today's task
7. Never ask user to explain — recalculate, shift, sync, move forward
