# Repository Initialization Procedure

**Scope:** This document is the canonical reference for starting any new project repository within this portfolio engineering system. Follow this procedure every time a new repository is created from `portfolio-base-template`. It does not change between projects.

---

## Required Startup Order

The steps below must be followed in sequence. Do not skip steps. Do not open Claude Code before the structure validator passes.

---

### Step 1 — Create the Repository from Template

On GitHub:

1. Navigate to the `portfolio-base-template` repository
2. Click **Use this template** → **Create a new repository**
3. Name the repository in kebab-case (e.g., `dqn-reconstruction`, `sportschatplus-v2`, `narrvoca`)
4. Set visibility to **Private** until the project is ready for public portfolio use
5. Do not include all branches — default branch only
6. Click **Create repository**

---

### Step 2 — Clone Locally

```bash
git clone git@github.com:<your-username>/<repo-name>.git
cd <repo-name>
```

Confirm that the expected template files are present before proceeding:

```bash
ls -la
```

Expected: `README.md`, `CLAUDE.md`, `docs/`, `src/`, `tests/`, `scripts/`, `.github/`, `LICENSE`

If any of these are absent, do not proceed. Restore from the template before continuing.

---

### Step 3 — Run the Bootstrap Script

```bash
bash scripts/bootstrap.sh
```

This script handles initial local setup: virtual environment creation, base dependency installation, and directory confirmation. If the script does not exist, flag it as a template gap — do not skip this step silently.

---

### Step 4 — Run the Structure Validator in Strict Mode

```bash
bash scripts/validate-structure.sh --strict
```

This step must exit with code 0 before Claude Code is opened. If any checks fail:

- Do not proceed to Step 5
- Fix the reported gaps (missing files or directories)
- Re-run the validator until it passes cleanly

The validator is the machine-readable gate. Claude Code sessions begin only on a structurally valid repository.

---

### Step 5 — Open Claude Code

Navigate to the repository root and start Claude Code:

```bash
claude
```

Confirm Claude Code is operating inside the correct repository directory before continuing.

---

### Step 6 — Run the Entry Protocol

In the Claude Code session, say:

> "Run the entry protocol"

This invokes `.claude/skills/entry-protocol.md` — a nine-phase read-only scan that reads CLAUDE.md, checks bootstrap status, validates structure, inventories source and test files, reviews documentation, identifies unfilled placeholders, builds a session summary, and proposes prioritized work items.

**Do not modify any files during this step.** The entry protocol is read-only. It ensures Claude Code has full context before any documentation or implementation work begins.

The step is complete when Claude confirms: *"Entry protocol complete. Await user instruction."*

---

### Step 7 — Run the Repository Architect Prompt

Open and paste the following prompt into the Claude Code session:

```
portfolio-engineering/prompt-packs/repository-architect.md
```

Copy the full contents of the **Prompt** section and paste it as the first message.

This session covers:
- Repository inspection and placeholder identification
- Explanation of key template files
- Project identity collection (name, description, stack, audience)
- Documentation drafts for README.md, CLAUDE.md, and docs/architecture.md

**Do not approve any code changes.** This session produces only documentation drafts. Apply drafts only after reviewing them. The session ends when Claude confirms: *"Repository architecture review complete."*

---

### Step 8 — Run the Implementation Roadmap Prompt

Open and paste the following prompt into a new Claude Code session:

```
portfolio-engineering/prompt-packs/implementation-roadmap.md
```

Copy the full contents of the **Prompt** section and paste it as the first message.

This session covers:
- Reading and validating docs/architecture.md
- Extracting scope and constraints
- Designing a phased implementation roadmap
- Producing a draft of docs/implementation-plan.md

**Do not approve any source code.** The only output is a completed `docs/implementation-plan.md`. Apply it only after reviewing the draft in full. The session ends when Claude confirms: *"Implementation roadmap complete. No source code has been written."*

---

### Step 9 — Run the Pre-Implementation Validation Prompt

Open and paste the following prompt into a new Claude Code session:

```
portfolio-engineering/prompt-packs/pre-implementation-validation.md
```

Copy the full contents of the **Prompt** section and paste it as the first message.

This session runs 7 named checks:

| Check | Required |
|---|---|
| README.md customized | Blocking |
| CLAUDE.md customized | Blocking |
| docs/architecture.md present and substantive | Blocking |
| docs/implementation-plan.md present with Phase 0 and Phase 1 | Blocking |
| Testing strategy defined | Blocking |
| `bash scripts/validate-structure.sh --strict` passes | Blocking |
| CI workflow present under `.github/workflows/` | Blocking |

All checks must PASS. Any failure blocks the next step. If any check fails, address the remediation steps Claude identifies and re-run this prompt before proceeding.

The session ends when Claude reports: *"Repository is cleared for implementation. Proceed to Phase 0."*

---

### Step 10 — Begin Project-Specific Implementation

Only after Step 9 produces a clean pass may implementation begin. Open a new Claude Code session and follow `docs/implementation-plan.md` starting from Phase 0.

Implementation sessions are project-specific. The process above (Steps 1–9) is complete and does not repeat.

---

## Summary Table

| Step | Action | Gate Condition |
|---|---|---|
| 1 | Create repo from portfolio-base-template | Template files present on GitHub |
| 2 | Clone locally | All expected files visible |
| 3 | `bash scripts/bootstrap.sh` | Script exits cleanly |
| 4 | `bash scripts/validate-structure.sh --strict` | Exit code 0 — required before Claude |
| 5 | Open Claude Code | Validator passed |
| 6 | Run entry protocol (`.claude/skills/entry-protocol.md`) | Read-only scan complete |
| 7 | Run `repository-architect.md` prompt | Docs drafted and approved |
| 8 | Run `implementation-roadmap.md` prompt | `docs/implementation-plan.md` written |
| 9 | Run `pre-implementation-validation.md` prompt | All 7 checks PASS |
| 10 | Begin implementation | Phase 0 of implementation plan |

---

## Related Files in This Repository

| File | Role |
|---|---|
| `prompt-packs/repository-architect.md` | Prompt for Step 7 — inspection and identity setup |
| `prompt-packs/implementation-roadmap.md` | Prompt for Step 8 — phased roadmap generation |
| `prompt-packs/pre-implementation-validation.md` | Prompt for Step 9 — final gate check |
| `repo-factory/one-command-repo-generator.md` | Alternative: single-session condensed init prompt |
| `repo-factory/repo-generator-sequence.md` | Human workflow guide for the one-command generator |
| `pipelines/repo-bootstrap.md` | Broader pipeline context and CI configuration notes |
| `validators/repo-structure-check.py` | Python CI validator used in GitHub Actions |
| `.github/workflows/structure-check.yml` | CI workflow that enforces structure on push and PR |

---

## Notes

- This procedure applies unchanged to all portfolio repositories: `dqn-reconstruction`, `sportschatplus-v2`, `narrvoca`, and any future projects created from `portfolio-base-template`.
- The one-command repo generator (`repo-factory/one-command-repo-generator.md`) is a condensed alternative to Steps 7–9 for operators who prefer a single session. Bootstrap (Step 3) and structure validation (Step 4) are still required before it.
- This document is the authoritative reference. If a process question arises about how to start a new repo, the answer is here.
