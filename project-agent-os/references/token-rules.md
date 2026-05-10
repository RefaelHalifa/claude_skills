# Token Optimization Rules

Every Claude Project system prompt loads every session and costs tokens every time.
These rules ensure maximum behavior quality at minimum token cost.

---

## THE CORE SPLIT

**Instructions (system prompt):** Behavior rules only.
What the agent does, how it behaves, what it tracks, what commands it responds to.

**Knowledge Base (AGENT_REFERENCE.md):** Reference content only.
Examples, formats, standards, static rules the agent looks up occasionally.

If content tells the agent HOW TO BEHAVE → instructions.
If content shows WHAT SOMETHING LOOKS LIKE → knowledge base.

---

## WHAT GOES IN INSTRUCTIONS

✅ Identity and role definitions
✅ Behavior flow rules (step-by-step gates, confirmation rules)
✅ Insight trigger rule (when to offer proactive help based on learned details)
✅ Memory file structure definitions (schema only — field names, format, update trigger)
✅ WORK_STATE.md schema definition (what it tracks, update trigger, in-place update rule)
✅ Session start protocol
✅ Session end protocol
✅ Auto-capture rule
✅ Custom commands ("manage memories", "sync calendar", etc.)
✅ Kickoff protocol
✅ Calendar sync rules (when to sync, what to do with results, fallback behavior)
✅ Missed day detection and recovery logic
✅ General rules (one-liners, max 10–15 bullets)
✅ Domain-specific command rules (e.g. always end git sequences with git push)
✅ Kickoff message (last 3–5 lines of instructions)

---

## WHAT GOES IN AGENT_REFERENCE.MD (knowledge base)

✅ Format examples for every memory file (what the actual content looks like)
✅ Code/content snippet format examples
✅ Output standards (resume polish, report format, documentation standards)
✅ Working days and schedule rules (static reference)
✅ Domain-specific reference content (naming conventions, preferred libraries, etc.)
✅ Missed day shift format example
✅ Anything the agent only needs to look at 1–2 times per project

---

## NEVER PUT IN EITHER (cut entirely)

❌ Redundant restatements of the same rule in two places
❌ Motivational filler — keep only if it serves a functional purpose
❌ Long prose explanations of rules that can be bullet points
❌ Examples inside instructions (all examples go to knowledge base)

---

## TARGET SIZES

| File | Target | Hard Max |
|------|--------|----------|
| Instructions | Under 350 lines / 1500 tokens | 500 lines / 2500 tokens |
| AGENT_REFERENCE.md | Any size (knowledge base, not auto-loaded) | No limit |
| Each memory .md file | Current state only, no bloat | 50–100 lines |

---

## ONE-LINER RULE

Every rule that can be expressed in one line should be one line.
Every memory entry should be one sentence max.
Every session log entry should be one sentence max.
Every preference entry should be one sentence max.

The goal: the agent should be able to read all memory files in under 500 tokens total.

---

## MEMORY FILE SIZE MANAGEMENT

Memory files grow over time. If a file exceeds its max, the agent should:
- SESSION_LOG: Archive older entries (keep last 10 sessions active, move older to ARCHIVE section at bottom)
- PREFERENCES: Merge duplicate or redundant entries, keep only the clearest version
- DECISIONS/ARCHITECTURE: Keep all entries but trim Why/Alternatives to shortest clear form
- PROGRESS: Replace previous status entirely — no history needed (history lives in SESSION_LOG)
- CALENDAR_SYNC: Always current state only — never accumulates
- WORK_STATE: Replace entries per file when updated — never delete lines, mark removed files as REMOVED. If file exceeds 60 lines, trim entries to one-liners only.

---

## KNOWLEDGE BASE FILE LOADING

The agent loads knowledge base files ONLY when needed:
- AGENT_REFERENCE.md → only when needing a format example or reference standard
- Memory files (SESSION_LOG, PROGRESS, etc.) → at session start and session end only
- Never load AGENT_REFERENCE.md in the middle of a teaching or building step unless a format question arises

The agent should state in the general rules: "Read AGENT_REFERENCE.md only when needed — not every message."

---

## QUICK CHECKLIST BEFORE FINALIZING

- [ ] Instructions under 400 lines?
- [ ] Zero format examples inside instructions?
- [ ] Every memory file has schema (not example) in instructions?
- [ ] Every memory file's example is in AGENT_REFERENCE.md?
- [ ] WORK_STATE schema includes: in-place update rule, last modified date, REMOVED marker?
- [ ] Session start reads all memory files?
- [ ] Session end updates all relevant files including WORK_STATE?
- [ ] Insight trigger rule is present?
- [ ] Domain-specific command rules added to general rules?
- [ ] No rule is stated more than once across all files?
- [ ] All one-liner rules are actually one line?
