# Prompt Pack — External Codex Peer Review

**Purpose:** Define how OpenAI Codex participates as an independent, external
peer reviewer in Ruben's personal multi-model workflow. Codex reviews the work
produced by `pe-implementer`; it does not plan, implement, or hold editing
authority in this first slice.

---

## What Codex is (and is not)

- **Codex is external.** It is the separate `codex` CLI, **not** a Claude
  subagent and **not** a target of the `pe-orchestrator` delegation allowlist.
  There is no file for Codex under `.claude/agents/`.
- **Codex reviews only after `pe-implementer` yields control.** Never run a
  Codex review while an implementation worker still holds editing authority.
  Codex and Sonnet must not hold simultaneous editing authority.
- **Codex does not edit files in the first slice.** Review only. Do not apply
  Codex's changes automatically.
- **Never use `codex apply`** in this slice.

## Who invokes Codex

In this first slice, **Ruben invokes Codex manually.** The `pe-orchestrator` has
no `Bash` tool and cannot run Codex itself. The orchestrator (or Ruben) requests
the review; Ruben runs the command; the result is returned to the orchestrator
or to Ruben for synthesis.

## Readiness check (non-mutating)

Before the first review, confirm Codex is authenticated using the documented,
non-mutating status command:

```text
codex login status
```

Do not run `codex login` as part of a review. Authentication changes are out of
scope for this slice.

## Review invocation

**Preferred — strict read-only (hard sandbox guarantee):**

```text
codex exec --sandbox read-only "<review prompt>"
```

**Native review-mode alternative (reviews the uncommitted working diff):**

```text
codex review --uncommitted "<review prompt>"
```

> **Sandbox note:** based on the verified local `codex --help` output,
> `codex review` does **not** expose a `--sandbox` flag, so
> `codex review --uncommitted` is **not sandbox-guaranteed** to be non-mutating.
> When a hard read-only guarantee is required, prefer the
> `codex exec --sandbox read-only` form above.

## Required review prompt content

Instruct Codex to inspect the completed uncommitted diff and to review
correctness, architecture compliance, tests, and regressions. Require the
following output shape:

- **Severity-labeled findings**, each labeled with exactly one of:
  - `BLOCKER`
  - `MAJOR`
  - `MINOR`
  - `NOTE`
- **File and line references** for each finding where available
  (`path:line`).
- **A single final verdict**, exactly one of:
  - `APPROVE`
  - `REQUEST CHANGES`
  - `DISCUSS`

## Example review prompt

```text
Review the current uncommitted git diff as an independent peer engineer.
Do not modify any files. Evaluate correctness, architecture/design compliance,
test adequacy, and regression risk. Report each finding on its own line labeled
BLOCKER, MAJOR, MINOR, or NOTE, with a path:line reference where available.
End with exactly one final verdict line: APPROVE, REQUEST CHANGES, or DISCUSS.
```

## After the review

- Return the severity-labeled findings and verdict to the orchestrator or to
  Ruben for synthesis.
- If the verdict is `REQUEST CHANGES` (or a `BLOCKER`/`MAJOR` is present), route
  a bounded correction pass back to `pe-implementer` — a **separate** pass, with
  Codex not editing — then re-review.
- Ruben performs any resulting Git action personally.
