# portfolio-engineering

Control repository for project initialization, documentation, and repository governance across the portfolio system.

---

## Overview

`portfolio-engineering` is the control repository for a structured portfolio engineering system. It contains the procedures, prompts, and validation tools used to initialize, document, and gate every new project repository in the portfolio.

All active project repositories are created from `portfolio-base-template` and initialized using the procedures defined here. The canonical reference is `docs/repo-initialization-procedure.md`.

---

## Purpose

This repository defines how a new project repository is created, documented, and cleared for implementation.

It provides:

- A canonical 10-step initialization procedure governing every new repository
- Prompt packs that instruct Claude Code through each initialization phase
- A condensed single-session initialization alternative
- A Python-based structure validator enforced by CI
- Explicit documentation of which older files are deprecated and what supersedes them

---

## System Role

`portfolio-engineering` sits between two other components in the portfolio system:

| Component | Role |
|---|---|
| `portfolio-base-template` | GitHub template repository. Every new project repository is created from this template. It provides the standard directory structure, base files, and CI scaffold. |
| `portfolio-engineering` (this repo) | Control repository. Provides the procedures, prompts, and validators used after a repo is created from the template. |
| Active project repos | Destination. Each project repository is the output — initialized using `portfolio-base-template` and the procedures in this repository. |

`portfolio-engineering` does not modify `portfolio-base-template` or any active project repository directly. It provides the tools and instructions that a human (with Claude Code) follows to bring a new repository from template to implementation-ready.

---

## Repository Structure

```text
portfolio-engineering/
├── .github/
│   └── workflows/
│       └── structure-check.yml           # CI: validates repo structure on push and PR
├── docs/
│   └── repo-initialization-procedure.md  # Canonical 10-step initialization procedure
├── pipelines/
│   └── repo-bootstrap.md                 # DEPRECATED — see docs/repo-initialization-procedure.md
├── prompt-packs/
│   ├── repository-architect.md           # Step 7: repo inspection and documentation setup
│   ├── implementation-roadmap.md         # Step 8: phased roadmap generation
│   └── pre-implementation-validation.md  # Step 9: 7-check gate before implementation
├── prompts/
│   └── master-repo-init.md               # DEPRECATED — see docs/repo-initialization-procedure.md
├── repo-factory/
│   ├── one-command-repo-generator.md     # Alternative: single-session initialization prompt
│   └── repo-generator-sequence.md        # DEPRECATED — see docs/repo-initialization-procedure.md
├── validators/
│   └── repo-structure-check.py           # Python validator: checks required dirs and files
├── src/                                  # Placeholder — reserved for future tooling
├── tests/                                # Placeholder — reserved for future tests
└── LICENSE
```

---

## Canonical Workflow

The authoritative reference for initializing any new project repository is:

```
docs/repo-initialization-procedure.md
```

The procedure consists of 10 sequential steps. Steps 1–4 are terminal commands run before Claude Code opens. Steps 5–10 are Claude Code sessions. Each step has an explicit gate condition that must be satisfied before proceeding.

| Step | Action | Gate Condition |
|---|---|---|
| 1 | Create repository from `portfolio-base-template` on GitHub | Template files present |
| 2 | Clone locally | All expected files visible |
| 3 | `bash scripts/bootstrap.sh` | Script exits cleanly |
| 4 | `bash scripts/validate-structure.sh --strict` | Exit code 0 — required before opening Claude Code |
| 5 | Open Claude Code | Validator passed |
| 6 | Run entry protocol (`.claude/skills/entry-protocol.md`) | Read-only scan complete |
| 7 | Run `repository-architect.md` prompt | Documentation drafted and approved |
| 8 | Run `implementation-roadmap.md` prompt | `docs/implementation-plan.md` written |
| 9 | Run `pre-implementation-validation.md` prompt | All 7 checks pass |
| 10 | Begin project-specific implementation | Phase 0 of implementation plan |

Each step must be completed and validated before proceeding to the next.

---

## Key Components

### Prompt Packs (`prompt-packs/`)

Three prompts are used in sequence during Steps 7–9 of the initialization procedure. Each is used as the initial prompt in a structured initialization session.

**`repository-architect.md`** (Step 7)
Instructs Claude Code to inspect the new repository, identify unfilled template placeholders, and produce drafts for `README.md`, `CLAUDE.md`, and `docs/architecture.md`. No files are written without explicit approval. Session ends when Claude confirms: *"Repository architecture review complete. Awaiting documentation approval before implementation begins."*

**`implementation-roadmap.md`** (Step 8)
Instructs Claude Code to read `docs/architecture.md` and produce a phased `docs/implementation-plan.md`. Phases follow a standard structure (Phase 0 — Foundation, Phase 1 — Core Domain, and so on). No source code is written. Session ends when Claude confirms: *"Implementation roadmap complete. No source code has been written."*

**`pre-implementation-validation.md`** (Step 9)
Instructs Claude Code to run 7 blocking checks: README.md customized, CLAUDE.md customized, `docs/architecture.md` substantive, `docs/implementation-plan.md` present with Phase 0 and Phase 1 defined, testing strategy documented, `bash scripts/validate-structure.sh --strict` exits 0, CI workflow present. All 7 checks must pass. Session ends when Claude confirms: *"Repository is cleared for implementation. Proceed to Phase 0."*

### Repo Factory (`repo-factory/`)

**`one-command-repo-generator.md`**
A single master prompt that condenses the documentation and planning phases (equivalent to Steps 7–9) into one Claude Code session. Suitable when a single-session initialization is preferred over the three-prompt sequence. Bootstrap (`bash scripts/bootstrap.sh`) and structure validation (`bash scripts/validate-structure.sh --strict`) must still be completed locally before this prompt is used. The session runs a 10-step internal sequence covering repository inspection, project identity collection, README and CLAUDE.md customization, architecture document preparation, implementation plan creation, ADR setup, validator confirmation, and a final initialization report.

### Validator (`validators/`)

**`repo-structure-check.py`**
Python script that validates a repository contains the required structure. Checks for:

- Required directories: `src/`, `docs/`, `tests/`
- Required files: `README.md`, `LICENSE`

```bash
python validators/repo-structure-check.py <path-to-repo>
```

Exits with code 0 on pass, code 1 on failure. Output format:

```
[PASS] src/
[PASS] docs/
[PASS] tests/
[PASS] README.md
[PASS] LICENSE

Result: All checks passed
```

### CI Workflow (`.github/workflows/structure-check.yml`)

Runs `validators/repo-structure-check.py` against this repository on every push and pull request using Python 3.12. Enforces structural integrity automatically.

---

## Deprecated Components

The following files are retained for reference only. They describe earlier initialization patterns that predate `docs/repo-initialization-procedure.md`. Do not use them for new repositories.

| File | Superseded By |
|---|---|
| `pipelines/repo-bootstrap.md` | `docs/repo-initialization-procedure.md` |
| `prompts/master-repo-init.md` | `docs/repo-initialization-procedure.md` |
| `repo-factory/repo-generator-sequence.md` | `docs/repo-initialization-procedure.md` |

Each deprecated file contains a `⚠️ Deprecated` header identifying the superseding document.

---

## Usage

### Starting a New Project Repository

1. Review docs/repo-initialization-procedure.md before beginning.
2. Create the new repository from `portfolio-base-template` on GitHub.
3. Clone locally and complete Steps 3–4 (bootstrap and structure validation).
4. Open Claude Code and follow Steps 5–10 using the prompt packs in `prompt-packs/`, or use the condensed alternative in `repo-factory/one-command-repo-generator.md`.

### Validating an Existing Repository

Run the structure validator against any repository to check for required files and directories:

```bash
python validators/repo-structure-check.py /path/to/project-repo
```

### Using the Prompt Packs

Prompt packs are plain Markdown files. To use one: open the file, locate the `## Prompt` section, copy its full contents, and paste into a Claude Code session as the opening message.

---

## Constraints

- `src/` and `tests/` are placeholders reserved for potential future tooling.
- This repository does not initialize or modify `portfolio-base-template`. Changes to the base template are managed in that repository.
- This repository does not track the status of active project repositories. Project-specific documentation lives in each project repo.
- The structure validator (`repo-structure-check.py`) checks for the presence of required directories and files only. It does not validate file contents.
- The one-command repo generator does not replace the bootstrap and structure validation steps. These must be completed locally before any Claude Code session begins.
