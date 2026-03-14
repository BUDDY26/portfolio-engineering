#!/usr/bin/env python3
"""
repo-structure-check.py

Validates that a repository contains the required structure for the
portfolio-engineering standard. Exits with code 0 on success, 1 on failure.

Usage:
    python validators/repo-structure-check.py <path-to-repo>
    python validators/repo-structure-check.py .
"""

import sys
from pathlib import Path

REQUIRED_DIRS = ["src", "docs", "tests"]
REQUIRED_FILES = ["README.md", "LICENSE"]


def check_repo(repo_path: Path) -> tuple[list[str], list[str]]:
    """Return (missing_dirs, missing_files) for the given repo path."""
    missing_dirs = [d for d in REQUIRED_DIRS if not (repo_path / d).is_dir()]
    missing_files = [f for f in REQUIRED_FILES if not (repo_path / f).is_file()]
    return missing_dirs, missing_files


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: repo-structure-check.py <path-to-repo>")
        return 1

    repo_path = Path(sys.argv[1]).resolve()

    if not repo_path.exists():
        print(f"ERROR: Path does not exist: {repo_path}")
        return 1

    if not repo_path.is_dir():
        print(f"ERROR: Path is not a directory: {repo_path}")
        return 1

    print(f"Checking repository: {repo_path}\n")

    missing_dirs, missing_files = check_repo(repo_path)

    passed = True

    print("Required directories:")
    for d in REQUIRED_DIRS:
        status = "PASS" if d not in missing_dirs else "FAIL"
        print(f"  [{status}] {d}/")
        if status == "FAIL":
            passed = False

    print("\nRequired files:")
    for f in REQUIRED_FILES:
        status = "PASS" if f not in missing_files else "FAIL"
        print(f"  [{status}] {f}")
        if status == "FAIL":
            passed = False

    print()
    if passed:
        print("Result: All checks passed.")
        return 0
    else:
        all_missing = missing_dirs + missing_files
        print(f"Result: {len(all_missing)} check(s) failed: {', '.join(all_missing)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
