# Memory File Templates

Ready-to-use schemas for every memory file type.
Copy and adapt these when building the memory system in Step 3.
These schemas go into the INSTRUCTIONS as structure definitions.
The examples go into AGENT_REFERENCE.md — not into instructions.
Works for any domain: code, legal, events, design, or any project type.

---

## SESSION_LOG.md

### Schema (goes in instructions)
**`SESSION_LOG.md`**
- Updated after EVERY session
- One-liner per completed task (max 1 sentence)
- Format: YYYY-MM-DD | Day Name | Status | Tasks Completed | Next Up
- Status options: COMPLETE / PARTIAL / SKIPPED

### Example (goes in AGENT_REFERENCE.md only)
## SESSION LOG
2025-01-12 | Sunday | COMPLETE | Set up project, created DB schema | Next: User model
2025-01-13 | Monday | PARTIAL | Started user model, blocked on migration | Next: Finish migration
2025-01-14 | Tuesday | SKIPPED
2025-01-15 | Wednesday | COMPLETE | User model + migrations done | Next: Auth routes

---

## PROGRESS.md

### Schema (goes in instructions)
**`PROGRESS.md`**
- Updated when phase changes or milestone is reached
- Tracks: project name, current phase, completion status, expected end date
- Format: key-value pairs, one per line
- Fields: Project | Description | Phase | Status | Started | Expected End | Completed Days | Remaining Days
- Status options: NOT_STARTED / IN_PROGRESS / COMPLETED / ON_HOLD

### Example (goes in AGENT_REFERENCE.md only)
Project: User Auth API
Description: RESTful API with JWT auth and user management
Phase: Week 1 — Core Build
Status: IN_PROGRESS
Started: 2025-01-12
Expected End: 2025-01-24
Completed Days: 3
Remaining Days: 7

---

## BUILD_PLAN.md / ROADMAP.md

### Schema (goes in instructions)
**`BUILD_PLAN.md`**
- Created ONCE at kickoff — never regenerated unless scope changes
- Format: numbered day sections, each with PRIMARY and SECONDARY tasks
- Each day entry: Day number | Date | Day name | Tasks | Status
- Status per day: PENDING / IN_PROGRESS / DONE / SKIPPED

### Example (goes in AGENT_REFERENCE.md only)
## Day 1 (Sun, Jan 12) — DONE
- PRIMARY: Project setup, DB schema design
- SECONDARY: Environment variables, README skeleton

## Day 2 (Mon, Jan 13) — DONE
- PRIMARY: User model + migrations
- SECONDARY: Database connection test

## Day 3 (Tue, Jan 14) — SKIPPED

## Day 4 (Wed, Jan 15) — IN_PROGRESS
- PRIMARY: Auth routes + JWT logic
- SECONDARY: Token refresh endpoint

---

## ARCHITECTURE.md / DECISIONS.md

### Schema (goes in instructions)
**`ARCHITECTURE.md`**
- Updated whenever an architectural or key decision is made — by user OR agent
- One entry per decision
- Format: YYYY-MM-DD | Decision | Decided By | Why | Alternatives Rejected
- Decided By options: Agent / User / Both
- If decision is revised: add new entry marked REVISION, do not delete original

### Example (goes in AGENT_REFERENCE.md only)
## DECISIONS
2025-01-12 | Use FastAPI over Flask | Agent | Better async + auto docs | Flask (too minimal), Django (too heavy)
2025-01-12 | PostgreSQL for DB | Agent | Relational fit, production-ready | SQLite (not scalable), MongoDB (no relations)
2025-01-13 | JWT in httpOnly cookie | User | More secure than localStorage | localStorage (XSS risk)
2025-01-15 | Split routers by domain | Agent | Cleaner separation, easier to scale | Single router file

---

## PREFERENCES.md

### Schema (goes in instructions)
**`PREFERENCES.md`**
- Updated when agent observes clear patterns in how user learns, works, or communicates
- Never assume — only log what is clearly observed
- Organized into four fixed sections, never free-form
- One-liner per entry (max 1 sentence)
- If pattern already logged: update existing entry, do not duplicate

Sections:
- LEARNING PREFERENCES — concepts grasped quickly, concepts needing more time, effective explanation styles
- WORK PATTERNS — session pace, feedback preference, how user signals confusion or readiness
- CODE/OUTPUT PREFERENCES — style, formatting, things user has pushed back on
- PROJECT PATTERNS — recurring gaps, recurring strengths, habits to watch for

### Example (goes in AGENT_REFERENCE.md only)
## LEARNING PREFERENCES
- Struggles with async/await — needs extra analogies and slower pace
- Grasps relational DB concepts quickly — can skip basics
- Python analogies land well every time — always use them

## WORK PATTERNS
- Goes quiet when lost — check in if no response after complex step
- Prefers direct feedback, not softened
- Signals readiness with short confirmations ("ok", "got it", "next")

## CODE/OUTPUT PREFERENCES
- Prefers explicit variable names over abbreviations
- Dislikes inline comments on obvious lines
- Prefers full files over fragmented snippets

## PROJECT PATTERNS
- Tends to underestimate time for testing steps — build in buffer
- Strong at planning phase, sometimes loses momentum mid-build

---

## CALENDAR_SYNC.md

### Schema (goes in instructions)
**`CALENDAR_SYNC.md`**
- Rebuilt fresh at EVERY session start using Google Calendar MCP (or system date fallback)
- Current state only — no history kept in this file
- Fields: Today | Day Name | Working Days Completed | Working Days Missed | Days Remaining This Week | Days Remaining Overall | Expected Completion | Upcoming Conflicts

### Example (goes in AGENT_REFERENCE.md only)
## CALENDAR STATE
Today: 2025-01-15 (Wednesday)
Working Days Completed: 3 (Sun Jan 12, Mon Jan 13, Wed Jan 15)
Working Days Missed: 1 (Tue Jan 14)
Remaining This Week: 2 (Thu Jan 16)
Remaining Overall: 7
Expected Completion: 2025-01-24
Upcoming Conflicts: None in next 14 days
Last Sync: Google Calendar MCP — success

---

## WORK_STATE.md

### Schema (goes in instructions)
**`WORK_STATE.md`**
- Updated at the END of every session, and immediately when a significant artifact is created or changed
- Snapshots what currently EXISTS — not what was done, but what is there right now
- Current state only — previous entries for the same item are replaced, not appended
- Format: Item/File/Module → what exists inside it (comma-separated, one-liners)
- Domain examples:
  - Code: file path → imports, functions, routes, models present
  - Legal: document name → sections drafted, clauses included, status
  - Event: category → vendors booked, decisions confirmed, items completed
  - Design: component/page → elements built, states handled, assets created

### Example — Code project (goes in AGENT_REFERENCE.md only)
## WORK STATE
app/main.py → FastAPI app init, CORS middleware, router includes (users, auth)
app/models/user.py → User model, UserCreate schema, UserResponse schema
app/routes/auth.py → /register, /login, /refresh endpoints
app/routes/users.py → /me GET endpoint
app/db/session.py → engine, SessionLocal, get_db dependency
requirements.txt → fastapi, uvicorn, sqlalchemy, pydantic, python-jose, passlib

### Example — Legal project (goes in AGENT_REFERENCE.md only)
## WORK STATE
Contract Draft v3 → Parties clause ✓, Scope of work ✓, Payment terms ✓, IP ownership (in progress), Termination clause (pending)
Filed Documents → NDA signed 2025-01-10, Incorporation cert filed 2025-01-12
Pending → Shareholder agreement, Operating agreement

### Example — Event planning project (goes in AGENT_REFERENCE.md only)
## WORK STATE
Venue → The Grand Hall confirmed, deposit paid, capacity 200
Catering → Three quotes received, Bella Cucina selected, menu pending final approval
Entertainment → DJ booked, photographer shortlisted (2 options remaining)
Invitations → Guest list finalized (87 people), invites not yet sent
Pending → Florist, transportation, accommodation block

---

## MISSED DAY SHIFT FORMAT

### Schema (goes in instructions)
Not needed — the missed day recovery protocol in instructions covers the behavior.

### Example (goes in AGENT_REFERENCE.md only)
## MISSED DAY SHIFT FORMAT
When days are missed and the plan is shifted, report to user like this:

Shifted Days:
- [New Date] (was [Old Date]) → [Task]
- [New Date] (was [Old Date]) → [Task]

Today: [New Date] — [Task]

Example:
Shifted Days:
- Sun Jan 19 (was Thu Jan 16) → Auth routes + JWT logic
- Mon Jan 20 (was Sun Jan 19) → Password reset endpoint
- Tue Jan 21 (was Mon Jan 20) → Email verification flow

Today: Sun Jan 19 — Auth routes + JWT logic

---

## AGENT_REFERENCE.md — Master Template

This is the token-saving knowledge base file. It contains all examples and static reference content
that the agent needs occasionally but not every session.

### Header to always include:
# AGENT REFERENCE FILE
Read this file only when you need format examples or reference standards.
Do not load this entire file every message — jump to the relevant section when needed.

### Sections to include (add only what applies to this agent):
- Memory File Format Examples (one section per memory file)
- Output/Delivery Standards (resume polish, report format, etc.)
- Working Days & Schedule Rules
- Code/Content Format Examples
- Domain-Specific Reference (tech stack choices, naming conventions, etc.)
- Missed Day Shift Format (include if agent tracks working days and calendar)
