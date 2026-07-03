# Personal Multi-Model Orchestration System

This document describes the design of Ruben James Aleman's personal Claude Code
orchestration system: a controlled, multi-model coding workflow with precise
per-model roles, preserved governance, and Ruben as final authority.

This is the **first slice** of that system. It defines canonical agent
definitions and the Codex review contract as Git-tracked files. It does **not**
install anything, change settings, or automate synchronization.

---

## 1. Purpose and ownership

The system gives each model a precise, non-interchangeable role so that
planning, implementation, review, and approval stay separated; scope does not
expand on its own; and evidence and handoffs are recorded. It is built for
Ruben's personal use across his own machines. Ruben remains the final authority
and personally performs every Git write operation (commit, push, merge, tag,
release, reset, restore, rebase, branch deletion).

The canonical definitions are Git-tracked in `portfolio-engineering`. Each
machine later receives **runtime copies** of the three agent files under the
user-level Claude configuration. Generated project repositories do **not**
receive project-scoped copies of these agents.

## 2. Canonical files in `portfolio-engineering`

The source of truth for the first slice is exactly these five files:

- `agents/pe-orchestrator.md` — Fable main-thread coordinator
- `agents/pe-architect.md` — Opus read-only architecture specialist
- `agents/pe-implementer.md` — Sonnet bounded implementation worker
- `prompt-packs/codex-review.md` — external Codex peer-review contract
- `docs/orchestration.md` — this document

These files are edited **only** here, in their canonical location.

## 3. Later runtime-copy locations

After separate review and approval, the three agent files (only) are copied to
the user-level agents directory on each machine:

```
C:\Users\ruben\.claude\agents\pe-orchestrator.md
C:\Users\ruben\.claude\agents\pe-architect.md
C:\Users\ruben\.claude\agents\pe-implementer.md
```

`prompt-packs/codex-review.md` and `docs/orchestration.md` are **not** copied —
they are an invocation reference and documentation. Codex receives **no** file
under `.claude/agents/`. The runtime copies are derivatives; they are never
edited independently — changes are made in the canonical files and re-copied.

## 4. Role boundaries

| Role | Model | Authority | Never |
|---|---|---|---|
| `pe-orchestrator` | Fable (main thread via `--agent`) | Inspect context; delegate to the two workers; synthesize; return decisions to Ruben | Edit files; run Bash/Git; invoke any agent other than the two workers; self-approve scope |
| `pe-architect` | Opus (subagent) | Read-only analysis, design, roadmaps, target-file proposals, acceptance criteria | Edit; run Bash; delegate; authorize implementation |
| `pe-implementer` | Sonnet (subagent) | Edit approved files in ~5-file batches; run tests/validators; `git status`/`git diff` | Expand scope; unapproved refactor; delegate; Git write/destructive commands |
| Codex reviewer | external `codex` CLI | Independent read-only review of the uncommitted diff; severity-labeled findings + verdict | Edit files (first slice); hold editing authority with Sonnet simultaneously; `codex apply` |
| Ruben | — | Final authority; scope approval; **all** Git write operations | — |

## 5. Execution lifecycle

1. **Task intake** — the orchestrator (Fable) frames the task and inspects
   context read-only.
2. **Architecture** — the orchestrator delegates to `pe-architect` (Opus), which
   returns a plan: assumptions, risks, unresolved decisions, proposed target
   files, roadmap, and acceptance criteria.
3. **Ruben's scope approval** — Ruben reviews the plan and approves the scope and
   the specific target files. No implementation begins without this.
4. **Implementation** — the orchestrator delegates approved work to
   `pe-implementer` (Sonnet), which edits only approved files in bounded batches
   and runs tests/validators.
5. **External Codex review** — after the implementer yields, Codex reviews the
   uncommitted diff and returns severity-labeled findings and a verdict.
6. **Correction** — if changes are requested, a separate bounded implementer
   pass addresses the findings (Codex does not edit).
7. **Verification** — tests/validators re-run; Codex re-reviews if needed.
8. **Ruben's Git action** — Ruben personally performs the commit/push/tag/etc.

Only one editing worker holds authority at a time across this lifecycle.

## 6. Native controls versus conventions

**Native (runtime-enforced by agent frontmatter):**

- Orchestrator has no `Write`/`Edit`/`Bash` — cannot edit files or run commands.
- Orchestrator delegation is restricted to `pe-architect` and `pe-implementer`
  via the `Agent(pe-architect, pe-implementer)` allowlist (valid because the
  orchestrator runs as the `--agent` main thread).
- Architect is read-only (`Read`, `Grep`, `Glob` only).
- Neither worker can delegate: `Agent` is omitted from their tools.

**Convention (behavioral, not enforced in this slice):**

- The implementer's prohibition on Git write/destructive commands. `Bash` is
  granted for tests/validators/`git status`/`git diff`; nothing currently
  *blocks* a Git write command at the subcommand level. This is trust-based
  until later hardening.
- Routing rules, batch sizing, read-before-edit, scope discipline,
  one-editor-at-a-time, and conflict escalation.
- The model-identity confirmation and stop rule (see §8).

## 7. Agent allowlisting and nested-delegation restrictions

- **Allowlisting:** `pe-orchestrator` lists `Agent(pe-architect, pe-implementer)`
  in `tools`. Because it runs as the main thread via `claude --agent`, this is a
  runtime-enforced allowlist: spawning any other agent type fails.
- **No nested delegation:** `pe-architect` and `pe-implementer` omit `Agent`
  from their tools entirely, so they cannot spawn any subagents. This is
  runtime-enforced by omission.

## 8. Model fallback risk (roles are not interchangeable)

The Claude Code runtime does **not** guarantee a subagent runs on its intended
model. A policy-excluded or unavailable subagent model **silently falls back to
the inherited model** instead of erroring, and the roles (Fable / Opus /
Sonnet) are **not interchangeable** — a silent fallback could run architecture
reasoning or implementation on the wrong model.

The model and effort values for the three roles are **configured in agent
frontmatter** (`pe-orchestrator`: model `fable`, effort `high`;
`pe-architect`: model `opus`, effort `xhigh`; `pe-implementer`: model
`sonnet`, effort `high`). These values were accepted syntactically because the
agent definitions loaded. However, during verified delegated runs the installed
runtime **did not expose worker model or effort metadata**: the runtime
metadata available to the orchestrator contained only the agent ID, token
usage, tool-use count, and duration.

The orchestrator therefore applies this policy (matching
`agents/pe-orchestrator.md`):

- **A worker's natural-language self-report is never evidence** of its model.
- **If the runtime explicitly exposes a worker model that mismatches the
  configured model, or the worker fails to launch, rejects its frontmatter,
  reports a model-configuration error, or encounters any runtime error**, the
  orchestrator stops and reports to Ruben.
- **If the runtime does not expose a model field**, the delegation is labeled
  `MODEL IDENTITY UNVERIFIED`: the configured model is stated, and it is stated
  that the actual runtime model could not be confirmed. Absence of model
  metadata alone is never described as a confirmed mismatch.
- **Meaningful delegated work under `MODEL IDENTITY UNVERIFIED` requires
  Ruben's explicit approval** before it begins.
- **Effort values are described as configured but runtime-unverified** unless
  the runtime later exposes an authoritative effort field.

This is an honest human-approval fallback, not fail-closed model pinning; there
is no runtime primitive in this slice that pins a subagent to a specific model.

## 9. Session reload requirement

Subagents are loaded at session start. When the three agent files are copied to
`C:\Users\ruben\.claude\agents\` (or later updated on disk), a **new Claude Code
session is required** before the changes load. Files edited directly on disk do
not hot-reload into a running session. (Agents created or edited through the
interactive `/agents` interface take effect immediately, but the canonical
workflow here is file copy + restart.)

## 10. Codex read-only boundary

Codex is an external peer reviewer. In this slice it performs review only and
does not edit files. The strict read-only invocation is
`codex exec --sandbox read-only "<review prompt>"`. The native
`codex review --uncommitted` form reviews the working diff but, per the verified
local help, is **not sandbox-guaranteed** non-mutating. `codex apply` is never
used. Authentication readiness is checked with the non-mutating
`codex login status`. See `prompt-packs/codex-review.md` for the full contract.

## 11. First-slice limitations

This slice deliberately excludes:

- **No command-level Bash guard** — the implementer's Git prohibition is
  convention, not enforcement.
- **No settings enforcement** — no `settings.json` permission `deny` rules are
  added.
- **No MCP** configuration.
- **No plugins** configuration.
- **No automatic synchronization** between canonical files and runtime copies.

## 12. Future hardening (clearly deferred — not part of this slice)

- **Verified permission deny patterns** in settings to fail-close the Git and
  destructive-command prohibitions (exact match-pattern spelling to be confirmed
  against `/permissions` on the target machine).
- **An agent-scoped `PreToolUse` guard** on the implementer's `Bash` tool to
  block write/destructive commands at execution time.
- **Automated installation or hash verification** to copy the three agent files
  and confirm runtime copies match canonical (e.g. SHA-256 comparison).
- **Optional Codex integration** beyond manual invocation (e.g. an MCP bridge),
  only after it is verified.
- **Verify whether a future Claude Code runtime exposes or applies worker
  frontmatter effort values in an observable way.**

## 13. Governance compatibility with `portfolio-base-template`

The roles are designed to respect the governance that repositories created from
`portfolio-base-template` already carry in their `CLAUDE.md`:

- the three-tier permission model (allowed / requires approval / never);
- Ruben's exclusive control of Git operations;
- documentation authority (documentation over code; ADRs and implementation plan
  binding where present);
- the conflict-resolution protocol (report, explain, propose, wait);
- proposal-before-refactor;
- read-before-edit and re-read-after-edit;
- bounded edit batches (~5 files);
- QA separation and the Plan → Code → Audit → Fix → Verify lifecycle;
- release, tag, and push safeguards (Ruben only).

The orchestrator and workers operate **under** the active repository's rules; an
external routing decision about *what* to work on never overrides the
repository's rules about *how* work is performed. No change to
`portfolio-base-template` is made or proposed in this slice.

## 14. Manual installation is a later, separately approved step

Copying the three canonical agent files into `C:\Users\ruben\.claude\agents\` is
a distinct, later action that Ruben approves and performs separately. It is not
part of this file-creation slice. Project-scoped agent copies are **not** used.
