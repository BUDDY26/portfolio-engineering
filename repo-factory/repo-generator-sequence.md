# ⚠️ Deprecated

This document is superseded by:
`portfolio-engineering/docs/repo-initialization-procedure.md`

Do not use this flow for new repositories.
Retained for reference only.

---

# Repo Generator Sequence

**Purpose:** The human workflow for creating and initializing a new project repository using the `portfolio-base-template` and the one-command repo generator. Follow this sequence every time a new project repository is started.

---

## Prerequisites

Before starting, confirm:
- You have access to the `portfolio-base-template` repository on GitHub
- You have `git`, `bash`, and Python 3.10+ installed locally
- Claude Code is installed and available in the terminal
- The `portfolio-engineering` repository is cloned locally (for reference)

---

## Sequence

### 1 — Create the Repository from Template

On GitHub:

1. Navigate to the `portfolio-base-template` repository
2. Click **"Use this template"** → **"Create a new repository"**
3. Set the repository name (use kebab-case, e.g., `dqn-reconstruction`, `sportschatplus-v2`, `narrvoca`)
4. Set visibility to **Private** until the project is ready for public portfolio use
5. Do not check "Include all branches" — only the default branch is needed
6. Click **"Create repository"**

---

### 2 — Clone the Repository Locally

```bash
git clone git@github.com:<your-username>/<repo-name>.git
cd <repo-name>
```

Verify the template files are present:

```bash
ls -la
```

Expected output includes: `README.md`, `CLAUDE.md`, `docs/`, `src/`, `tests/`, `scripts/`, `.github/`

---

### 3 — Run the Bootstrap Script

```bash
bash scripts/bootstrap.sh
```

This script performs initial local setup such as:
- Creating a Python virtual environment (if applicable)
- Installing base dependencies
- Confirming the directory structure is intact

If `scripts/bootstrap.sh` does not exist in the template, note the gap and proceed. The absence of this script should be reported as a template issue.

---

### 4 — Run the Structure Validator in Strict Mode

```bash
bash scripts/validate-structure.sh --strict
```

Expected output: all checks pass with exit code 0.

If any checks fail:
- Do not proceed to Step 5
- Fix the structural issue (missing files or directories) before continuing
- Re-run the validator until it passes cleanly

This step must pass before Claude Code is opened.

---

### 5 — Open Claude Code

Navigate into the repository root and start Claude Code:

```bash
claude
```

Confirm that Claude Code is operating inside the correct repository by checking the working directory at the start of the session.

---

### 6 — Paste the Master Initialization Prompt

Open the one-command repo generator prompt:

```
portfolio-engineering/repo-factory/one-command-repo-generator.md
```

Copy the full contents of the **Master Prompt** section (everything under `## Master Prompt`).

Paste it as your first message in the Claude Code session.

Claude will begin the initialization sequence (Steps 1–10 of the master prompt). Follow Claude's prompts:
- Answer the project identity questions in Step 3 fully and precisely
- Review every draft before confirming it should be applied
- Do not rush past approval points

The session ends when Claude produces the **Final Initialization Report** (Step 9) and confirms no implementation code has been written.

---

### 7 — Review the Initialization Report

After the session completes, review the initialization report Claude produced.

Confirm:
- All required files were customized (README.md, CLAUDE.md, docs/architecture.md)
- `docs/implementation-plan.md` was created and reviewed
- No template gaps were left unresolved
- The "Implementation Status" field reads: **NOT STARTED**

If any items are marked **Pending** (draft produced but not yet applied), apply them now or schedule them for the next session.

---

### 8 — Begin Implementation Planning

The repository is now initialized. The next step is implementation — but only through the defined prompt pack sequence:

| Session | Prompt to Use | Location |
|---|---|---|
| Session 1 (complete) | One-command repo generator | `repo-factory/one-command-repo-generator.md` |
| Session 2 | Pre-implementation validation | `prompt-packs/pre-implementation-validation.md` |
| Session 3+ | Implementation (Phase 0 first) | Follow `docs/implementation-plan.md` |

Do not skip the pre-implementation validation. It is the final gate before code is written.

---

## Quick Reference Card

```
1.  GitHub → Use template → Create repo (Private)
2.  git clone → cd <repo-name>
3.  bash scripts/bootstrap.sh
4.  bash scripts/validate-structure.sh --strict  ← must pass
5.  claude
6.  Paste: repo-factory/one-command-repo-generator.md → Master Prompt
7.  Follow prompts, answer Step 3 identity questions, approve drafts
8.  Review initialization report
9.  Next session: pre-implementation-validation.md
10. Then: Phase 0 of docs/implementation-plan.md
```

---

## Known Future Projects Using This Sequence

This sequence is designed for reuse across all portfolio repositories, including:

| Project | Description |
|---|---|
| `dqn-reconstruction` | Deep Q-Network reconstruction and analysis |
| `sportschatplus-v2` | Sports analytics and conversational AI platform |
| `narrvoca` | Narrative vocabulary analysis tool |
| Future AI/ML repos | Any new project created from `portfolio-base-template` |

No changes to this sequence are needed between projects. Project-specific content is collected during Step 3 of the master prompt.

---

## Related Files

| File | Role |
|---|---|
| `repo-factory/one-command-repo-generator.md` | Master initialization prompt |
| `prompt-packs/repository-architect.md` | Deep architectural review prompt |
| `prompt-packs/implementation-roadmap.md` | Roadmap generation prompt |
| `prompt-packs/pre-implementation-validation.md` | Gate check before coding begins |
| `pipelines/repo-bootstrap.md` | Broader pipeline context and CI notes |
| `validators/repo-structure-check.py` | Python-based CI structure validator |
