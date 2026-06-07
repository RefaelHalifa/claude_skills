# Platform Targets Reference

Read this during **STEP 0** once you know which platform the agent will run on.
It defines **how** Layer 3 (Memory) and Layer 4 (Commands & Protocols) get implemented —
Layers 1 (Identity & Roles) and 2 (Behavior System) stay identical across every platform.

The four OS layers and the memory *concepts* (session log, progress, decisions, preferences,
work state, calendar state) never change. What changes is the **mechanism**: a real file, a
memory-tool entry, a frontmattered topic file, or a filesystem path. Design the conceptual
memory table first (Step 2), then translate it through the matching profile below.

---

## Profile A — Claude Project (file-based knowledge base)

This is the skill's original, most fully-specified target. Default to this profile if the
platform is unclear — and tell the user you're defaulting.

- **Persistence:** `.md` files created in the Project's Knowledge Base. No real filesystem —
  the agent produces file content as text, the user pastes/uploads it once at setup, and the
  agent edits these files by re-presenting their full updated content for the user to re-save
  (unless the platform exposes a file-write tool, in which case use it directly).
- **Recall:** agent re-reads the KB files at session start — full file content loads into context.
- **`INSTRUCTIONS.md` memory section says:** "maintain these named KB files; here is each one's
  schema, format, and update trigger" (this is the skill's existing default wording — keep it).
- **Commands/protocols:** standard Layer 4 set. "Manage memories" Tier 1 (read files) always
  works; Tiers 2–3 (scan past sessions) are **not reliably available** — claude.ai does not
  expose cross-conversation transcript search to the agent. Treat history-search as absent
  unless the user confirms the Project has it.
- **Calendar fallback:** Google Calendar MCP if connected → else ask the user for today's date
  at session start (do not assume a system clock — claude.ai does not expose one to the agent).
  Log which source was used.
- **Output artifacts:** `INSTRUCTIONS.md` + empty named KB files (one per memory concept) +
  `AGENT_REFERENCE.md` + setup checklist. Unchanged from the skill's original design.

---

## Profile B — claude.ai chat / Project using built-in memory

No addressable files exist here at all — do not generate "create these KB files" instructions.

- **Persistence:** Anthropic's built-in memory tool (the agent writes/queries discrete memory
  entries through tool calls, not files).
- **Recall:** query-driven and associative — the agent issues memory-tool lookups for relevant
  entries; it cannot "read all memory files" the way Profile A can. Session start becomes
  "query memory for: last session summary, current progress, open decisions, preferences" —
  not "open and read N files."
- **`INSTRUCTIONS.md` memory section says:** describe *what* to remember and *when* to write or
  query a memory-tool entry — translate each conceptual memory file into an entry type/tag
  (e.g., "session-log entry: one per session, one sentence" instead of "append a line to
  SESSION_LOG.md"). No file schemas, no file paths.
- **Commands/protocols:** "manage memories" becomes "review and consolidate memory-tool
  entries" — merge duplicates, drop stale ones. Tiers 2–3 (deep-scan session history) are
  **unavailable** — there is no transcript search. Skip them entirely; rely solely on what's
  in memory-tool entries, and tell the user plainly that anything mentioned in chat but never
  written to memory may be lost.
- **Calendar fallback:** Google Calendar MCP if connected → else ask the user to confirm
  today's date each session and store it as a single current-state memory entry (no rebuilt
  CALENDAR_SYNC file — there's nothing to rebuild it into). See `memory-templates.md` note on
  CALENDAR_SYNC collapsing for this profile.
- **Output artifacts:** `INSTRUCTIONS.md` (memory-tool-flavored, no file schemas) + memory-tool
  entry-type templates (replacing file schemas) + `AGENT_REFERENCE.md` + a setup checklist that
  walks through enabling/configuring the memory tool rather than creating KB files.

---

## Profile C — Cowork (managed auto-memory directory)

Cowork agents already run inside a managed memory convention — adopt it rather than imposing
the skill's generic file names on top of it.

> **Check for existing infrastructure first.** Cowork projects almost always already have a
> managed memory directory with its own `MEMORY.md` index, frontmatter conventions, and
> possibly a `consolidate-memory`-style skill in place. Read the index and a sample topic file
> before proposing anything — map the new agent's memory needs onto *that* convention (names,
> `metadata.type` values, linking style), don't introduce a second, parallel system. If real
> infrastructure is found, follow `SKILL.md` Step 1B's audit → gap-list → additive-patch flow
> even if the user just asked to "build an agent."

- **Persistence:** a managed directory (e.g. `.../memory/`) with `MEMORY.md` as a one-line-per-entry
  index, and per-topic `.md` files carrying frontmatter (`name`, `description`,
  `metadata.type`: one of `user` / `feedback` / `project` / `reference`), cross-linked with
  `[[name]]` references.
- **Recall:** agent reads `MEMORY.md` first, then opens only the linked topic files relevant to
  the current task — not a full read of everything every session.
- **`INSTRUCTIONS.md` memory section says:** map each conceptual memory file onto this
  convention instead of inventing parallel files:
  - SESSION_LOG / PROGRESS / WORK_STATE → `metadata.type: project` topic file(s), indexed in `MEMORY.md`
  - PREFERENCES → `metadata.type: user` and/or `feedback` topic file(s)
  - DECISIONS / ARCHITECTURE → `metadata.type: reference` topic file(s)
  - Link related entries with `[[name]]` per Cowork convention
- **Commands/protocols:** "manage memories" maps directly onto the existing `consolidate-memory`
  pattern — merge duplicates, fix stale facts, prune the index. Tiers 2–3 (deep-scan session
  history) **are available** here (session transcripts are searchable) — keep them, phrased to
  match Cowork's consolidation flow.
- **Calendar fallback:** the session/runtime context already supplies the current date — use it
  directly as the primary source; Google Calendar MCP (if connected) only for richer sync
  (events, conflicts), not for "what day is it."
- **Output artifacts:** updated `MEMORY.md` index entries + new per-topic files with correct
  frontmatter + `INSTRUCTIONS.md` written in terms of `[[links]]` and topic-file types +
  `AGENT_REFERENCE.md` (may itself be one of the topic files rather than a separate KB file) +
  a setup checklist describing the directory location and frontmatter format.

---

## Profile D — Claude Code / filesystem-backed agent

The richest profile — full read/write filesystem access plus shell tools.

> **Check for existing infrastructure first.** Never assume a blank slate — `ls`/`find`/`Read`
> for a `CLAUDE.md`, a `memory/` (or similarly named) directory, an index file, hooks, or
> skills that already manage instructions/persistence before designing anything new. If one
> exists, this becomes a retrofit, not a fresh build: audit it against the four OS layers
> (`SKILL.md` Step 1B), reuse its existing file names/conventions/index structure for the new
> agent's memory needs, and propose additive changes — never a parallel structure that
> duplicates or conflicts with what's already maintaining the project.

- **Persistence:** real `.md` files anywhere in the project/repo, optionally a `CLAUDE.md`,
  hooks, custom skills, or slash commands.
- **Recall:** agent uses Read/Grep/Bash directly — no re-presentation needed, no context-budget
  concern from "loading everything"; it can grep for exactly what it needs.
- **`INSTRUCTIONS.md` memory section says:** close to Profile A's file-schema wording, but
  framed as direct filesystem read/write with real paths — and may additionally propose
  `CLAUDE.md` placement or a small custom skill/command for repeated protocols.
- **Commands/protocols:** full Layer 4 set including "manage memories" Tiers 1–3 — deep-scan is
  genuinely possible (grep git log, session transcripts, file history). This is the only
  profile where the full three-tier design works exactly as originally written.
- **Calendar fallback:** system date via `date`/Bash as the primary, reliable source (a real
  clock exists here, unlike A/B); Google Calendar MCP as enrichment if connected.
- **Output artifacts:** same shape as Profile A (instructions + memory files + reference file +
  checklist) but with real file paths, and optionally a proposal to scaffold a hook or custom
  skill for automated protocol steps.

---

## Comparison table

| | A — Claude Project | B — claude.ai memory | C — Cowork | D — Claude Code |
|---|---|---|---|---|
| Persistence | KB `.md` files | memory-tool entries | `MEMORY.md` index + frontmatter topic files | real filesystem files |
| Recall | re-read full files | query memory tool | read index → follow links | Read/Grep on demand |
| Calendar fallback | GCal MCP → ask user | GCal MCP → ask user, store as 1 entry | session context date → GCal MCP enrichment | system date (Bash) → GCal MCP enrichment |
| History/transcript search available? | No | No | Yes | Yes |
| "Manage memories" Tiers 2–3 | Skip | Skip | Keep (consolidate-memory pattern) | Keep (full deep scan) |
| Output artifacts | INSTRUCTIONS + empty KB files + AGENT_REFERENCE + checklist | INSTRUCTIONS (tool-flavored) + entry templates + AGENT_REFERENCE + checklist | MEMORY.md index updates + frontmatter topic files + INSTRUCTIONS + checklist | INSTRUCTIONS + real files + AGENT_REFERENCE + checklist (+ optional hook/skill scaffold) |
