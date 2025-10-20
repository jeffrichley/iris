# CI & Pre-commit Quickstart Guide

**Feature**: 001-ci-precommit-setup  
**Last Updated**: October 20, 2025  
**Audience**: Iris developers

## Overview

This guide helps you set up local pre-commit hooks and understand the CI/CD pipeline for the Iris project. Following these steps ensures your code passes CI checks before you even push to GitHub.

---

## 🚀 Quick Setup (< 5 minutes)

### 1. Install Pre-commit Hooks

From the repository root:

```bash
# Install pre-commit framework (if not already installed)
pip install pre-commit

# Install git hooks
pre-commit install
pre-commit install --hook-type commit-msg

# Verify installation
pre-commit --version
```

**What this does**: Installs Git hooks that run automatically before each commit and when writing commit messages.

### 2. Install Development Tools

The pre-commit hooks will auto-install tools, but you can pre-install them:

```bash
# Install all Python dev dependencies
uv sync --dev

# Install frontend dependencies
cd frontend  # if applicable
npm install
```

### 3. Verify Setup

Test that hooks work:

```bash
# Run hooks on all files (first time)
pre-commit run --all-files

# Try a commit (will validate everything)
git add .
git commit -m "test: verify pre-commit hooks"
```

**Expected**: Hooks auto-format code, check types, and validate commit message.

---

## 🎯 Daily Workflow

### Making Changes

```bash
# 1. Create feature branch
git checkout -b feature/my-awesome-feature

# 2. Make changes to code
# ... edit files ...

# 3. Run checks locally (before committing)
just lint          # Check for linting errors
just type-check    # Check for type errors
just test          # Run tests

# 4. Format code (optional - hooks do this automatically)
just format

# 5. Commit changes (hooks run automatically)
git add .
git commit

# If commit message doesn't follow format, you'll see:
# ❌ commitizen check...........................Failed
# Then use interactive commit instead:
cz commit
```

### Interactive Commit (Recommended)

```bash
# Use Commitizen for guided commit messages
cz commit

# You'll be prompted:
# Select the type of change: (Use arrow keys)
#   ❯ feat: A new feature
#     fix: A bug fix
#     docs: Documentation only changes
#     ...

# Then prompted for scope, description, etc.
# Result: Properly formatted commit message every time!
```

### Push to GitHub

```bash
# Push your branch
git push -u origin feature/my-awesome-feature

# CI Workflow A runs automatically:
# - Fast linting (3-5 minutes)
# - Basic tests on one OS
# - Quick feedback in GitHub UI
```

---

## 🔄 CI Workflows Explained

### Workflow A: Feature Branch Fast Feedback

**Trigger**: Push to any branch except `main`

**What runs**:
- ✅ Ruff linting (Python)
- ✅ mypy type checking (Python)
- ✅ ESLint (TypeScript/React)
- ✅ Prettier format check
- ✅ Basic tests on Ubuntu + Python 3.12

**Duration**: ~3-5 minutes with cache

**Purpose**: Quick feedback to catch obvious issues

**When it fails**: Fix locally, push again

### Workflow B: PR to Main - Comprehensive Validation

**Trigger**: Pull request targeting `main` branch

**What runs**:
- ✅ Full matrix builds (3 OS × 2 Python versions)
- ✅ Complete test suite on all platforms
- ✅ Security scans (Bandit, Safety, CodeQL)
- ✅ Code coverage check (must be ≥ 80%)
- ✅ Dependency audits

**Duration**: ~10-15 minutes with cache

**Purpose**: Ensure code is production-ready before merge

**Merge blocked if**: 
- Any test fails on any platform
- Coverage drops below 80%
- Critical/High security vulnerabilities found
- Type checking errors exist
- Linting errors exist

### Workflow C: Post-Merge to Main

**Trigger**: Push to `main` (after PR merge)

**What runs**:
- 📦 Optional: Version tagging
- 📦 Optional: Release creation
- 📦 Optional: Deployment triggers

**Duration**: ~1-2 minutes

**Purpose**: Release automation

---

## 🛠️ Available Commands

All commands use `just` (task runner):

```bash
# Linting
just lint              # Run all linters (Python + TypeScript)
just lint-py           # Python only
just lint-ts           # TypeScript only

# Type Checking
just type-check        # Run all type checkers
just type-check-py     # mypy (Python)
just type-check-ts     # tsc (TypeScript)

# Testing
just test              # Run all tests
just test-unit         # Unit tests only
just test-integration  # Integration tests only
just test-cov          # Tests with coverage report

# Formatting
just format            # Auto-format all code
just format-py         # Python only (ruff format)
just format-ts         # TypeScript only (prettier)

# Combined
just ci                # Run everything (lint + type-check + test)
just pre-push          # Run before pushing (faster than full ci)

# Setup
just setup-hooks       # Install pre-commit hooks
```

---

## 🚨 Troubleshooting

### Pre-commit Hook Failures

**Problem**: `ruff check` fails

```bash
# Fix automatically
just format

# Or manually
uv run ruff check . --fix
```

**Problem**: `mypy` type errors

```bash
# See detailed errors
just type-check

# Fix code to add type hints or fix type errors
# No auto-fix available - manual code changes required
```

**Problem**: `commitizen` rejects commit message

```bash
# Use interactive commit instead
cz commit

# Or format manually:
# ✅ Good: "feat(auth): add OAuth2 support"
# ❌ Bad:  "added oauth stuff"
```

**Problem**: Hook takes too long

```bash
# Skip hooks temporarily (NOT RECOMMENDED)
git commit --no-verify

# Better: Commit smaller changesets
git add specific_file.py
git commit
```

### CI Failures

**Problem**: Tests pass locally but fail in CI

**Common causes**:
1. Platform-specific issue (Windows vs Linux vs macOS)
2. Missing dependency in `pyproject.toml`
3. Hard-coded paths that differ across OS
4. Timezone or locale differences

**Solution**:
```bash
# Run tests in CI-like environment locally
docker run -v $(pwd):/app -w /app python:3.12 just test

# Or test specific platform
# (Windows) Test on Windows runner
# (macOS) Test on macOS runner
```

**Problem**: Coverage dropped below 80%

```bash
# See coverage report
just test-cov

# Opens HTML report showing uncovered lines
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows

# Add tests for uncovered code
```

**Problem**: Security scan found vulnerabilities

```bash
# See vulnerability details in CI logs
# For Python dependencies:
uv run safety check --detailed

# Fix by updating vulnerable package
uv add package_name@latest

# For dev dependencies (MEDIUM/LOW severity):
# - Can be addressed in follow-up PR
# - Merge not blocked
```

### Git Workflow Issues

**Problem**: Can't push to `main` directly

**Solution**: This is intentional! Use feature branches:

```bash
git checkout -b feature/my-fix
git add .
git commit
git push -u origin feature/my-fix
# Then create PR on GitHub
```

**Problem**: PR blocked by required reviews

**Solution**: Request review from team member or project owner

**Problem**: PR blocked by failing status checks

**Solution**:
1. Check which CI job failed in GitHub PR UI
2. Read error logs
3. Fix issue locally
4. Push fix to same branch
5. CI re-runs automatically

---

## 📋 Commit Message Format

**Required format**: `<type>(<scope>): <description>`

### Types

| Type | When to Use | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(tasks): add task priority levels` |
| `fix` | Bug fix | `fix(sync): resolve conflict resolution edge case` |
| `docs` | Documentation only | `docs(api): update authentication guide` |
| `style` | Code style (formatting, no logic change) | `style(ui): adjust button spacing` |
| `refactor` | Code restructuring (no behavior change) | `refactor(db): simplify query builder` |
| `perf` | Performance improvement | `perf(search): add index on task title` |
| `test` | Adding or updating tests | `test(tasks): add edge case coverage` |
| `chore` | Build, tooling, dependencies | `chore(deps): update ruff to 0.2.0` |

### Scope (Optional but Recommended)

Common scopes for Iris:
- `auth`, `tasks`, `projects`, `sync`, `ui`, `api`, `db`, `cli`, `docs`, `ci`, `deps`

### Examples

✅ **Good**:
```
feat(auth): add OAuth2 integration
fix(sync): prevent data loss during conflict
docs(setup): add Windows installation guide
test(tasks): increase coverage to 90%
chore(ci): optimize cache strategy
```

❌ **Bad**:
```
Added stuff
Fixed bug
WIP
Update README
```

### Using Interactive Commit

```bash
$ cz commit

? Select the type of change you are committing: feat
? What is the scope of this change? (press enter to skip): tasks
? Write a short description: add task priority levels
? Provide a longer description (press enter to skip): 
? Are there any breaking changes? (y/N): N
? Does this change affect any open issues? (y/N): N

[feature/task-priority 1a2b3c4] feat(tasks): add task priority levels
```

---

## 🎓 Best Practices

### 1. Commit Early, Commit Often

Small, focused commits are easier to:
- Review
- Test
- Revert if needed
- Understand in git history

### 2. Run Checks Before Pushing

```bash
# Quick pre-push check
just lint && just test

# Full CI simulation
just ci
```

**Saves time**: Catch issues locally instead of waiting for CI

### 3. Keep Feature Branches Updated

```bash
# Regularly sync with main
git checkout main
git pull
git checkout feature/my-feature
git merge main

# Resolve conflicts, run tests
just test
```

**Avoids**: Merge conflicts and CI surprises

### 4. Use Pre-commit Hooks

Let hooks auto-fix formatting:
- Don't manually format with ruff/prettier
- Commit normally, hooks handle it
- Saves time and ensures consistency

### 5. Understand Coverage Reports

```bash
just test-cov

# Check HTML report to see:
# - Which lines aren't covered
# - Which branches need test cases
# - Overly complex functions (high cyclomatic complexity)
```

---

## 📊 CI Status Badges

Add to README.md:

```markdown
[![CI](https://github.com/jeffrichley/iris/actions/workflows/ci-pr-main.yml/badge.svg)](https://github.com/jeffrichley/iris/actions/workflows/ci-pr-main.yml)
[![Coverage](https://codecov.io/gh/jeffrichley/iris/branch/main/graph/badge.svg)](https://codecov.io/gh/jeffrichley/iris)
[![Code Quality](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
```

---

## 🔗 Additional Resources

### Documentation

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [pre-commit Documentation](https://pre-commit.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Internal Docs

- [Iris Constitution](../../../planning/CONSTITUTION.md) - Project principles and standards
- [Feature Specification](./spec.md) - Detailed requirements for CI system
- [Research Document](./research.md) - Technical decisions and rationale
- [Implementation Plan](./plan.md) - Architecture and structure

### Getting Help

1. **Check CI logs**: Most errors are clearly explained in workflow output
2. **Run locally**: `just ci` simulates CI environment
3. **Ask for help**: Create issue with CI logs and steps to reproduce

---

## ✅ Checklist for New Contributors

Before your first PR:

- [ ] Install pre-commit hooks: `pre-commit install`
- [ ] Install dev dependencies: `uv sync --dev`
- [ ] Verify hooks work: `pre-commit run --all-files`
- [ ] Try interactive commit: `cz commit`
- [ ] Run local CI: `just ci`
- [ ] Read the [Constitution](../../../planning/CONSTITUTION.md)
- [ ] Understand commit message format
- [ ] Know how to check coverage reports

---

**Questions?** Open an issue or check the [research document](./research.md) for technical details.

**Found a bug in CI?** PRs welcome! This system is designed to evolve with the project.

