# Prompt Pack — Pre-Implementation Validation

**Purpose:** Use this prompt as the final gate before any implementation code is written. It instructs Claude Code to run a comprehensive checklist verifying the repository is properly initialized, documented, and structurally sound.

---

## Prompt

You are performing a **pre-implementation validation** of this repository. This is a gate check. If any required condition is not met, implementation must not begin. Your output is a pass/fail report with actionable remediation steps for every failure.

Do not write any implementation code during this session. Your only outputs are a validation report and, if needed, targeted remediation for documentation or configuration gaps.

---

### Validation Checklist

Run each check in order. Report PASS or FAIL for each item. Collect all failures before presenting the final report — do not stop at the first failure.

---

#### 1. README.md — Customized

**Check:** `README.md` exists and has been meaningfully customized beyond the template default.

A PASS requires all of the following to be true:
- The project title is not a placeholder (no `{{`, `<`, or generic template text)
- The overview section describes this specific project
- The setup instructions reflect the actual stack
- There is no remaining placeholder text such as `TODO`, `TBD`, `{{PROJECT_NAME}}`, or `<replace this>`

**Fail remediation:** List the specific lines or sections that remain as placeholders.

---

#### 2. CLAUDE.md — Customized

**Check:** `CLAUDE.md` exists and contains project-specific behavior instructions for Claude Code.

A PASS requires:
- The file exists
- It contains at least one project-specific instruction (not just the template default)
- It does not contain unresolved placeholder text

**Fail remediation:** State what project-specific content needs to be added.

---

#### 3. docs/architecture.md — Present and Substantive

**Check:** `docs/architecture.md` exists and contains meaningful architectural content.

A PASS requires:
- The file exists
- It describes the system's components, data flow, or design decisions in project-specific terms
- It is not a blank stub or unchanged template

**Fail remediation:** List missing sections. Reference `implementation-roadmap.md` prompt for how to proceed.

---

#### 4. docs/implementation-plan.md — Present if Development is Beginning

**Check:** If implementation is about to begin, `docs/implementation-plan.md` must exist and contain at least Phase 0 and Phase 1 definitions.

A PASS requires:
- The file exists
- It defines at minimum two phases with goals, deliverables, and success criteria
- Phase 0 deliverables are all checked or explicitly deferred with justification

If the project is still in the documentation phase and implementation has not been approved, this check is advisory rather than blocking.

**Fail remediation:** Run the `implementation-roadmap.md` prompt to produce this document.

---

#### 5. Testing Strategy — Defined

**Check:** A testing strategy is documented somewhere in the repository.

A PASS requires at least one of:
- A `Testing` or `Test Strategy` section in `docs/architecture.md` or `docs/implementation-plan.md`
- A `tests/` directory exists with at least a placeholder or `__init__.py`
- `CLAUDE.md` contains instructions about how tests should be written

**Fail remediation:** Add a brief testing strategy section to `docs/architecture.md` before proceeding.

---

#### 6. Structure Validator — Passes Strict Mode

**Check:** Run the local structure validator if it exists.

```bash
bash scripts/validate-structure.sh --strict
```

A PASS requires:
- The script exists at `scripts/validate-structure.sh`
- It exits with code 0

If the script does not exist, report FAIL and note that it should be present per the `portfolio-base-template` standard.

**Fail remediation:** Report the exact validator output and list each failed check.

---

#### 7. CI Workflow — Present

**Check:** At least one GitHub Actions workflow file exists under `.github/workflows/`.

A PASS requires:
- The directory `.github/workflows/` exists
- At least one `.yml` file is present
- The workflow file is syntactically valid YAML (check for obvious formatting errors)

**Fail remediation:** Copy or restore the standard structure-check workflow from `portfolio-engineering/.github/workflows/structure-check.yml`.

---

### Final Report Format

Present the report as follows:

```
## Pre-Implementation Validation Report

| Check | Status | Notes |
|---|---|---|
| README.md customized | PASS / FAIL | ... |
| CLAUDE.md customized | PASS / FAIL | ... |
| docs/architecture.md present | PASS / FAIL | ... |
| docs/implementation-plan.md present | PASS / FAIL | ... |
| Testing strategy defined | PASS / FAIL | ... |
| validate-structure.sh --strict | PASS / FAIL | ... |
| CI workflow present | PASS / FAIL | ... |

**Overall: READY TO PROCEED / NOT READY**

### Failures Requiring Remediation
<list each FAIL with specific remediation action>

### Advisory Items
<any PASS items that have minor gaps worth noting>
```

---

### Gate Decision

- **All checks PASS:** State "Repository is cleared for implementation. Proceed to Phase 0."
- **Any check FAILS:** State "Implementation is blocked. Resolve all failures listed above before proceeding." Do not offer to begin implementation code as a workaround.

---

## When to Use This Prompt

- After running `repository-architect.md` and `implementation-roadmap.md`
- Before the first implementation session in any new project repo
- After a significant documentation or structural change to re-verify readiness
- When returning to a stalled project before resuming development
