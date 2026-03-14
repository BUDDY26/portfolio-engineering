# Prompt Pack — Implementation Roadmap

**Purpose:** Use this prompt after the repository architect phase is complete and documentation has been approved. It instructs Claude Code to produce a structured, phased implementation roadmap derived from the project's governing documents — without beginning to write code.

---

## Prompt

You are producing the **first implementation roadmap** for this project. Your output will guide all future development sessions. You are not writing code in this session. You are creating the plan that governs when and how code gets written.

Follow these steps in order.

---

### Step 1 — Read Governing Documents

Before producing anything, read the following files in full:
- `docs/architecture.md`
- `docs/implementation-plan.md` (if present)
- `README.md`
- `CLAUDE.md`

If `docs/architecture.md` is missing or contains only placeholder content, stop and report: **"Architecture document is not ready. Complete docs/architecture.md before generating the roadmap."**

If `docs/implementation-plan.md` is missing, note that it will be created as an output of this session.

---

### Step 2 — Identify Scope and Constraints

From the governing documents, extract and summarize:

- **Core objective:** What this project must accomplish at completion
- **Known constraints:** Technology choices, integration requirements, timeline pressures, research scope
- **Out of scope:** What has been explicitly excluded or deferred
- **Dependencies:** External systems, datasets, APIs, or libraries the project relies on

Present this as a **Scope Summary** before proceeding.

---

### Step 3 — Break Work into Phases

Design a phased roadmap. Each phase must follow this structure:

```
## Phase N — <Phase Name>

**Goal:** One sentence describing what this phase achieves.

**Inputs:** What must exist before this phase begins.

**Deliverables:**
- [ ] <concrete output 1>
- [ ] <concrete output 2>

**Files to create or modify:**
- `path/to/file.py` — purpose
- `path/to/file.md` — purpose

**Approval point:** What the human must review and confirm before Phase N+1 begins.

**Success criteria:** How to verify this phase is complete.
```

Recommended phase structure for most portfolio projects:

- **Phase 0 — Foundation:** Environment, configuration, CI, base structure verification
- **Phase 1 — Core Domain:** Primary logic, data models, or algorithmic core
- **Phase 2 — Integration:** Connecting components, external APIs, or data pipelines
- **Phase 3 — Evaluation / Testing:** Benchmarks, test coverage, validation results
- **Phase 4 — Documentation and Polish:** Final README, usage examples, demo artifacts

Adjust phases to fit the specific project. Do not force phases that are not applicable.

---

### Step 4 — Identify First Files to Implement

For Phase 0 and Phase 1 only, list the exact files that will be created or modified first, in the order they should be addressed. For each file state:

- File path
- What it contains
- Why it comes before other files
- Whether it requires human input or decisions before it can be written

Do not write these files. List them as a queue.

---

### Step 5 — Define Approval Points

List every point in the roadmap where work must pause for human review before continuing. For each approval point state:

- What phase it follows
- What artifacts are being reviewed
- What question the human must answer to proceed
- What happens if the answer is "revise" rather than "approve"

---

### Step 6 — Produce the Implementation Plan Document

Draft the full content of `docs/implementation-plan.md` based on the roadmap you have just designed.

Present the draft in full. Then ask: **"Shall I write this to docs/implementation-plan.md?"**

Do not write the file until confirmed.

---

### Step 7 — Hold on Code

Confirm: **"Implementation roadmap complete. No source code has been written. Awaiting approval to proceed to Phase 0."**

---

## When to Use This Prompt

- After `repository-architect.md` has been run and documentation has been approved
- When `docs/architecture.md` is complete but no implementation plan exists
- When resuming a project and re-establishing a plan from the current architecture
- When scope has changed significantly and the roadmap needs to be rebuilt
