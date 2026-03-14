# Repository Bootstrap Pipeline

Standard operating procedure for creating a new project repository under the portfolio-engineering standard.

---

## Overview

This pipeline ensures every new repository is created consistently, validated against the standard structure, and ready for immediate development.

---

## Steps

### Step 1 — Create the Repository

1. Create a new repository on GitHub (or your Git host of choice).
   - Set visibility to **Private** until the project is ready to publish.
   - Do **not** initialize with a README (the scaffold will provide it).
2. Clone the empty repository locally:
   ```bash
   git clone <repo-url>
   cd <repo-name>
   ```

---

### Step 2 — Scaffold the Structure

Apply the standard scaffold using the master initialization prompt.

**Option A — Manual scaffold:**
```bash
mkdir -p src tests docs notebooks data configs scripts .github/workflows
touch src/__init__.py tests/__init__.py docs/index.md data/.gitkeep
touch README.md LICENSE requirements.txt pyproject.toml .gitignore
```

**Option B — From template:**
```bash
# Copy from the portfolio-engineering templates directory
cp -r /path/to/portfolio-engineering/templates/base/. .
```

Refer to `prompts/master-repo-init.md` for required file contents (README, .gitignore, pyproject.toml).

---

### Step 3 — Fill in Project Metadata

Edit the following files with project-specific information:

| File | Fields to update |
|---|---|
| `README.md` | Title, description, setup, usage |
| `pyproject.toml` | `name`, `version`, `description` |
| `LICENSE` | Year, author name |
| `.gitignore` | Add any project-specific ignores |

---

### Step 4 — Validate the Structure

Run the structure validator from the `portfolio-engineering` control repo:

```bash
python /path/to/portfolio-engineering/validators/repo-structure-check.py <path-to-new-repo>
```

Expected output:
```
[PASS] src/
[PASS] docs/
[PASS] tests/
[PASS] README.md
[PASS] LICENSE

Result: All checks passed.
```

Fix any reported failures before proceeding.

---

### Step 5 — Initial Commit

```bash
git add .
git commit -m "chore: initial repository scaffold"
git push -u origin main
```

---

### Step 6 — Configure GitHub Settings

After pushing, apply these settings in the GitHub repository:

- **Branch protection** on `main`: require PR reviews, no direct pushes.
- **Topics/tags**: add relevant tags (e.g., `python`, `ml`, `research`).
- **Description**: fill in the one-line repo description.
- **CI workflow**: add or copy a base workflow from `.github/workflows/` in this control repo.

---

## Checklist

- [ ] Repository created and cloned
- [ ] Directory structure scaffolded
- [ ] README, LICENSE, pyproject.toml populated
- [ ] Validator passes with no failures
- [ ] Initial commit pushed to `main`
- [ ] Branch protection enabled
- [ ] GitHub metadata (description, topics) filled in

---

## Related Files

| File | Purpose |
|---|---|
| `prompts/master-repo-init.md` | AI prompt for scaffolding content |
| `validators/repo-structure-check.py` | Automated structure validation |
| `templates/` | Base file templates |
