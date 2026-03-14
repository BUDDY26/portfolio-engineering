# Master Repository Initialization Prompt

Use this prompt to initialize any new project repository under the portfolio-engineering standard structure.

---

## Prompt

You are initializing a new project repository. Your task is to scaffold the repository with a consistent, professional structure suitable for AI/ML research and engineering projects.

### Instructions

Create the following directory and file structure:

```
<repo-name>/
├── src/                  # Source code
│   └── __init__.py
├── tests/                # Unit and integration tests
│   └── __init__.py
├── docs/                 # Documentation and design notes
│   └── index.md
├── notebooks/            # Jupyter notebooks (if applicable)
├── data/                 # Data files (gitignored by default)
│   └── .gitkeep
├── configs/              # Configuration files (YAML, TOML, etc.)
├── scripts/              # Utility and automation scripts
├── .github/
│   └── workflows/        # CI/CD pipelines
├── README.md             # Project overview and usage instructions
├── LICENSE               # License file (MIT by default)
├── .gitignore            # Standard Python/ML gitignore
├── requirements.txt      # Python dependencies
└── pyproject.toml        # Project metadata and tooling config
```

### README.md Template

Populate `README.md` with the following sections:
- **Project Title** and one-line description
- **Overview** — what the project does and why it exists
- **Setup** — how to install dependencies and run the project
- **Usage** — example commands or API calls
- **Project Structure** — brief description of key directories
- **Contributing** — link to contributing guidelines or a brief note
- **License** — license type and link

### .gitignore Contents

Include ignores for:
- Python artifacts (`__pycache__`, `*.pyc`, `.venv`, `dist/`, `build/`)
- Data directories (`data/`, `*.csv`, `*.parquet`, `*.h5`)
- Secrets and credentials (`.env`, `*.key`, `secrets/`)
- IDE files (`.vscode/`, `.idea/`)
- Jupyter checkpoints (`.ipynb_checkpoints/`)
- OS files (`.DS_Store`, `Thumbs.db`)

### pyproject.toml Template

```toml
[project]
name = "<repo-name>"
version = "0.1.0"
description = "<short description>"
requires-python = ">=3.10"

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.ruff]
line-length = 88
```

### Validation

After scaffolding, confirm the following are present:
- [ ] `src/` directory with `__init__.py`
- [ ] `tests/` directory with `__init__.py`
- [ ] `docs/` directory with at least `index.md`
- [ ] `README.md` with all required sections
- [ ] `LICENSE` file
- [ ] `.gitignore` covering Python and ML artifacts

---

## Usage

Replace `<repo-name>` and `<short description>` with the actual project name and description before running this prompt against a new repository context.
