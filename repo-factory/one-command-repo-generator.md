# One-Command Repo Generator

**Purpose:** A single master prompt that initializes a new repository — created from `portfolio-base-template` and cloned locally — through a complete, structured sequence. Paste this prompt into Claude Code at the start of the first session inside the new repo.

This prompt assumes:
- The repository has already been created from `portfolio-base-template` on GitHub
- The repository has been cloned to the local machine
- Claude Code is running inside the cloned repository directory
- No implementation code has been written yet

---

## Master Prompt

You are initializing a new project repository that was created from `portfolio-base-template`. Your role is to run a complete, controlled initialization sequence and produce a final initialization report. You will not write implementation code during this session.

Follow every step in the order given. Do not skip steps. Do not proceed past a step that requires human input until that input is received.

---

### Step 1 — Inspect the Repository

List all files and directories at the top level. Then read the following files if they exist:
- `README.md`
- `CLAUDE.md`
- `docs/architecture.md`
- `docs/implementation-plan.md`
- `pyproject.toml` or `package.json` (whichever is present)
- `scripts/validate-structure.sh`
- `.github/workflows/` (list all workflow files)

Report what you find. Flag any of these that are missing.

---

### Step 2 — Confirm Template Files Are Present

Verify the following standard template artifacts exist:

| Expected File / Directory | Present? |
|---|---|
| `README.md` | |
| `CLAUDE.md` | |
| `docs/` | |
| `docs/architecture.md` | |
| `src/` | |
| `tests/` | |
| `scripts/validate-structure.sh` | |
| `.github/workflows/` | |
| `LICENSE` | |

For any item marked absent, flag it as a template gap before proceeding.

---

### Step 3 — Project Identity Setup

Ask the following questions. Do not proceed to Step 4 until you have answers for all of them.

1. **Project name:** What is the repository name and the human-readable project title?
2. **One-line description:** What does this project do, in one sentence?
3. **Problem statement:** What specific problem does this project solve?
4. **Technology stack:** What are the primary languages, frameworks, and tools?
5. **Audience:** Who will read or use this project (portfolio reviewer, research committee, hiring manager, general public)?
6. **Scope boundary:** What is explicitly out of scope for this project?
7. **Known architectural decisions:** Are any major design decisions already made? (e.g., model architecture, database choice, API design)

Present these as a numbered list and wait for the user to provide answers before continuing.

---

### Step 4 — README.md and CLAUDE.md Customization

Using the project identity from Step 3, draft replacements for the placeholder content in both files.

**For README.md, draft:**
- Project title and badge line (if applicable)
- One-line description
- Overview paragraph (3–5 sentences describing the project, its purpose, and its context)
- Setup section header with placeholder commands appropriate to the stack
- Note that remaining sections will be filled in as the project develops

**For CLAUDE.md, draft:**
- Project-specific behavior instructions for Claude Code
- Stack-specific conventions (e.g., "always use type annotations", "follow PEP 8", "tests must be written before implementation")
- Any known constraints on how Claude should operate in this repo
- Reference to governing documents (`docs/architecture.md`, `docs/implementation-plan.md`)

Present both drafts in full. Then ask: **"Shall I apply these to README.md and CLAUDE.md?"**

Do not write to either file until confirmed.

---

### Step 5 — Refine docs/architecture.md

Read the current contents of `docs/architecture.md`.

Identify:
- Which sections are complete and project-specific
- Which sections are still template stubs or placeholders
- Which sections are missing entirely but required for this project type

Propose a revised outline for `docs/architecture.md` that reflects the project identity established in Step 3. For any section that needs to be written, provide a one-paragraph draft.

Ask: **"Shall I apply the architecture document revisions?"** Do not write until confirmed.

---

### Step 6 — Create docs/implementation-plan.md

Based on the project scope and the refined architecture, draft a `docs/implementation-plan.md` if it does not already exist or if the existing one is a template stub.

Structure the plan using this format for each phase:

```
## Phase N — <Phase Name>

**Goal:** <one sentence>

**Inputs:** <what must exist before this phase>

**Deliverables:**
- [ ] <concrete output>

**Files to create or modify:**
- `path/to/file` — purpose

**Approval point:** <what the human reviews before Phase N+1>

**Success criteria:** <how to verify completion>
```

Include at minimum:
- Phase 0 — Foundation (environment, CI, structure validation)
- Phase 1 — Core Domain (primary logic or algorithmic core)

Add further phases as the project scope warrants.

Present the full draft. Ask: **"Shall I write this to docs/implementation-plan.md?"** Do not write until confirmed.

---

### Step 7 — Prepare First ADR if Applicable

If any architectural decisions were identified in Step 3 (question 7), draft the first Architecture Decision Record.

Use this format:

```markdown
# ADR-001 — <Decision Title>

**Date:** <today's date>
**Status:** Accepted

## Context
<Why this decision needed to be made>

## Decision
<What was decided>

## Consequences
<What this decision enables and what it constrains>
```

Save to `docs/decisions/ADR-001-<short-title>.md`.

Ask: **"Shall I create this ADR?"** If no architectural decisions were identified in Step 3, skip this step and note it was skipped.

---

### Step 8 — Verify Validator and CI Presence

Check:
1. Does `scripts/validate-structure.sh` exist?
2. Does `.github/workflows/` contain at least one `.yml` file?

If either is missing, flag it explicitly. Do not attempt to recreate them from scratch — note that they should be restored from `portfolio-base-template` or `portfolio-engineering`.

If both are present, report: **"Validator and CI workflow confirmed present."**

---

### Step 9 — Produce Final Initialization Report

Produce a structured report summarizing the outcome of this entire session.

```
## Repository Initialization Report

**Project:** <name>
**Date:** <today>
**Template:** portfolio-base-template
**Initialized by:** Claude Code (one-command-repo-generator)

### Files Modified or Created This Session
| File | Action | Status |
|---|---|---|
| README.md | Customized | Applied / Pending |
| CLAUDE.md | Customized | Applied / Pending |
| docs/architecture.md | Revised | Applied / Pending |
| docs/implementation-plan.md | Created | Applied / Pending |
| docs/decisions/ADR-001-*.md | Created | Applied / Skipped |

### Template Gaps Identified
<list any missing standard files>

### Open Questions
<any questions from Step 3 that were not fully answered>

### Recommended Next Session
<which prompt pack to run next and why>

### Implementation Status
NOT STARTED — No source code has been written.
```

---

### Step 10 — Hold on Implementation

State clearly:

**"Initialization sequence complete. This repository has not had any implementation code written. The next step is to run the pre-implementation-validation prompt, then begin Phase 0 as defined in docs/implementation-plan.md."**

Do not offer to begin coding. Do not scaffold `src/` contents. Do not write tests. Wait for the next session.

---

## Notes for Reuse

This prompt is designed to work unchanged across all portfolio projects including but not limited to:
- DQN reconstruction projects
- Sports analytics platforms (e.g., SportsChatPlus-V2)
- NLP / narrative analysis tools (e.g., NarrVoca)
- Any future AI/ML or software engineering portfolio repository

The only project-specific content comes from the answers provided during Step 3.
