# Research: CI & Pre-commit Strategy

**Feature**: 001-ci-precommit-setup  
**Date**: October 20, 2025  
**Status**: Complete

## Overview

This document captures research findings and technical decisions for implementing the CI/CD pipeline and pre-commit hook system for the Iris project. All decisions are based on industry best practices, tool maturity, and alignment with project constitution.

---

## 1. Python Linting & Formatting: Ruff

### Decision

Use **ruff** as the sole Python linter and formatter (no black, no flake8, no isort separately).

### Rationale

1. **Performance**: Ruff is 10-100x faster than traditional Python linters, written in Rust
2. **All-in-one**: Replaces black, flake8, isort, pyupgrade, and more in a single tool
3. **Auto-fix**: Supports automatic fixing of many issues, improving developer experience
4. **Active Development**: Backed by Astral (Charlie Marsh), rapidly evolving with strong community
5. **Constitution Alignment**: Simplicity principle - one tool instead of 4-5

### Alternatives Considered

| Tool | Why Rejected |
|------|--------------|
| black + flake8 + isort | Multiple tools = slower CI, more config complexity |
| pylint | Slower, more opinionated, overlaps with mypy for many checks |
| autopep8 | Less comprehensive, doesn't replace all linting needs |

### Configuration

```toml
# pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP", "B", "A", "C4", "SIM"]
ignore = []

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

### References

- [Ruff Official Docs](https://docs.astral.sh/ruff/)
- [Ruff vs Black Performance](https://github.com/astral-sh/ruff#how-does-ruff-compare-to-black-flake8-isort-etc)

---

## 2. Type Checking: mypy

### Decision

Use **mypy** with strict type checking for all Python code.

### Rationale

1. **Industry Standard**: Most widely adopted Python type checker
2. **Gradual Typing**: Can incrementally add types to existing codebase
3. **Constitution Mandate**: Type Safety First principle requires comprehensive type checking
4. **IDE Integration**: Excellent support in VS Code, PyCharm, etc.
5. **Plugin Ecosystem**: Rich ecosystem for frameworks (pydantic, SQLAlchemy, etc.)

### Alternatives Considered

| Tool | Why Rejected |
|------|--------------|
| pyright | Excellent but less mature plugin ecosystem for our stack |
| pyre | Facebook's tool, less community adoption, enterprise-focused |
| pytype | Google's tool, slower, different type inference approach |

### Configuration

```toml
# pyproject.toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_any_unimported = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
check_untyped_defs = true

# Per-module options for gradual adoption if needed
[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false  # Allow untyped test functions
```

### References

- [mypy Documentation](https://mypy.readthedocs.io/)
- [Type Checking Best Practices](https://mypy.readthedocs.io/en/stable/existing_code.html)

---

## 3. Security Scanning: Bandit + Safety + CodeQL

### Decision

Use **three-layered security approach**:
1. **Bandit** for static code security analysis (Python)
2. **Safety** for dependency vulnerability scanning (Python)
3. **GitHub CodeQL** for comprehensive repository-wide analysis

### Rationale

1. **Defense in Depth**: Multiple tools catch different vulnerability classes
2. **Bandit**: Catches common security anti-patterns in code (SQL injection, hardcoded secrets, etc.)
3. **Safety**: Checks dependencies against known CVE database
4. **CodeQL**: GitHub-native, semantic code analysis, supports multiple languages
5. **Constitution Alignment**: Privacy by Design requires security-first approach

### Risk-Based Policy (from Spec Clarification)

- **Production Dependencies**: CRITICAL/HIGH → Block merge
- **Dev Dependencies**: CRITICAL/HIGH → Block merge, MEDIUM/LOW → Warn only
- **Rationale**: Dev tools don't ship to users but can compromise dev environment

### Configuration

```yaml
# .github/workflows/ci-pr-main.yml (excerpt)
- name: Run Bandit Security Scan
  run: |
    uv run bandit -r src/ -f json -o bandit-report.json
    uv run bandit -r src/ --severity-level medium

- name: Run Safety Check
  run: |
    uv run safety check --json --output safety-report.json
    # Custom script to parse and apply risk-based policy
    python scripts/safety-policy-check.py safety-report.json
```

### References

- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Safety Documentation](https://pyup.io/safety/)
- [GitHub CodeQL](https://codeql.github.com/)

---

## 4. Frontend Linting: ESLint + Prettier

### Decision

Use **ESLint** for linting and **Prettier** for formatting in TypeScript/React code.

### Rationale

1. **Industry Standard**: De facto standards for TypeScript/React projects
2. **Separation of Concerns**: ESLint for code quality, Prettier for formatting
3. **Integration**: Work well together with eslint-config-prettier
4. **React Best Practices**: ESLint plugins for React hooks, accessibility, etc.
5. **Constitution Alignment**: Type Safety First enforced via TypeScript strict mode

### Configuration

```json
// .eslintrc.json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react/recommended",
    "plugin:react-hooks/recommended",
    "plugin:jsx-a11y/recommended",
    "prettier"  // Must be last to disable formatting rules
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    }
  },
  "rules": {
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/explicit-function-return-type": "warn"
  }
}

// .prettierrc.json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": false,
  "printWidth": 100,
  "tabWidth": 2,
  "useTabs": false
}
```

### References

- [ESLint Documentation](https://eslint.org/)
- [Prettier Documentation](https://prettier.io/)
- [TypeScript ESLint](https://typescript-eslint.io/)

---

## 5. GitHub Actions Matrix Strategy

### Decision

Use **two-tier matrix strategy** with different coverage for feature branches vs PR to main.

### Rationale

1. **Cross-Platform Validation**: Iris must work on Windows, macOS, and Linux
2. **Python Version Coverage**: Support both 3.12 and 3.13 as per constitution
3. **Fail-Fast False**: See all failures, not just first one (better debugging)
4. **Caching Strategy**: Use `actions/cache` for pip and npm to optimize build time
5. **Parallel Execution**: GitHub Actions runs matrix jobs in parallel (faster feedback)
6. **Two-Tier Approach**: Fast feedback on feature branches, comprehensive validation on PR to main

### Available GitHub-Hosted Runners

Based on [GitHub's official documentation](https://docs.github.com/en/actions/reference/runners/github-hosted-runners):

**Ubuntu Runners:**
- `ubuntu-latest` (currently ubuntu-24.04)
- `ubuntu-24.04` (Noble Numbat LTS)
- `ubuntu-22.04` (Jammy Jellyfish LTS)

**Windows Runners:**
- `windows-latest` (currently windows-2025)
- `windows-2025` (Windows Server 2025 - newest)
- `windows-2022` (Windows Server 2022)

**macOS Runners:**
- `macos-latest` (currently macos-15, Apple Silicon/ARM64)
- `macos-15` (Sequoia, Apple Silicon)
- `macos-14` (Sonoma, Apple Silicon)
- `macos-13` (Ventura, Intel x86_64)
- `macos-15-intel` (Sequoia, Intel x86_64)

### Matrix Configuration: Workflow A (Feature Branch)

**Purpose**: Fast feedback on feature branches

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    python-version: ['3.12']
    node-version: ['20.x']
  fail-fast: false
```

**Jobs**: 3 (one per OS family, Python 3.12 only)  
**Expected Time**: ~3-5 minutes with caching

### Matrix Configuration: Workflow B (PR to Main)

**Purpose**: Comprehensive validation before merge

```yaml
strategy:
  matrix:
    os: 
      - ubuntu-latest    # ubuntu-24.04 (current LTS)
      - ubuntu-22.04     # Previous LTS
      - windows-latest   # windows-2025 (newest)
      - windows-2022     # Previous stable
      - macos-latest     # macos-15 (Apple Silicon, current)
      - macos-14         # Apple Silicon, previous
    python-version: ['3.12', '3.13']
    node-version: ['20.x']
  fail-fast: false
```

**Jobs**: 12 (6 OS × 2 Python versions × 1 Node version)  
**Expected Time**: ~10-15 minutes with caching (jobs run in parallel)

**Rationale for OS Selection**:
- **Ubuntu**: Latest (24.04) + Previous LTS (22.04) covers most Linux users
- **Windows**: Latest (2025) + Previous (2022) covers modern Windows servers
- **macOS**: Latest (15) + Previous (14) both on Apple Silicon (future of Mac)
- **Architecture Coverage**: Primarily ARM64 for macOS (Intel becoming legacy), x86_64 for Linux/Windows

### Caching Strategy

```yaml
- uses: actions/cache@v4
  with:
    path: |
      ~/.cache/uv
      ~/.cache/pip
      node_modules
    key: ${{ runner.os }}-${{ matrix.python-version }}-${{ hashFiles('**/pyproject.toml', '**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-${{ matrix.python-version }}-
```

### Performance Expectations

**Workflow A (Feature Branch - Fast Feedback):**
- **Without Cache**: 8-10 minutes per job
- **With Cache**: 3-5 minutes per job
- **Parallel Execution**: All 3 jobs run simultaneously
- **Wall-Clock Time**: ~3-5 minutes

**Workflow B (PR to Main - Comprehensive):**
- **Without Cache**: 10-15 minutes per job
- **With Cache**: 8-12 minutes per job
- **Parallel Execution**: All 12 jobs run simultaneously
- **Wall-Clock Time**: ~10-15 minutes (limited by slowest job)

**CI Minutes Consumption per PR**:
- Feature branch push: ~15 minutes (3 jobs × 5 min)
- PR to main: ~120 minutes (12 jobs × 10 min avg, but 4 macOS jobs count as 10x = ~400 equivalent minutes)

### References

- [GitHub Actions Matrix Strategy](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)
- [Actions Cache Documentation](https://github.com/actions/cache)

---

## 6. Pre-commit Framework

### Decision

Use **pre-commit framework** with hooks for ruff, mypy, eslint, prettier, and commitizen.

### Rationale

1. **Language Agnostic**: Manages hooks for Python, TypeScript, and any language
2. **Standardized**: Industry standard for managing Git hooks
3. **Isolated Environments**: Each hook runs in its own virtualenv (reproducible)
4. **Fast**: Only runs on changed files by default
5. **CI Integration**: Same hooks can run in CI for consistency

### Hook Configuration

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        args: [--ignore-missing-imports]
        additional_dependencies: [pydantic]

  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v9.0.0
    hooks:
      - id: eslint
        files: \.(js|jsx|ts|tsx)$
        args: [--fix]

  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: v4.0.0
    hooks:
      - id: prettier
        files: \.(js|jsx|ts|tsx|json|css|md)$

  - repo: https://github.com/commitizen-tools/commitizen
    rev: v3.13.0
    hooks:
      - id: commitizen
        stages: [commit-msg]
```

### References

- [pre-commit Documentation](https://pre-commit.com/)
- [pre-commit Hook Catalog](https://pre-commit.com/hooks.html)

---

## 7. Commit Message Standardization: Commitizen

### Decision

Use **Commitizen** for Conventional Commits enforcement and interactive commit creation.

### Rationale

1. **Constitution Mandate**: Principle 17 requires Conventional Commits
2. **Interactive**: Guides developers through creating properly formatted commits
3. **Validation**: Blocks improperly formatted commits automatically
4. **Python Native**: Written in Python, integrates well with our stack
5. **Changelog Generation**: Can auto-generate changelogs from commit history

### Alternatives Considered

| Tool | Why Rejected |
|------|--------------|
| commitlint | JavaScript-based, requires Node.js for Python-only workflows |
| Manual validation | Error-prone, requires custom scripts |

### Configuration

```toml
# pyproject.toml or .cz.toml
[tool.commitizen]
name = "cz_conventional_commits"
version = "0.1.0"
tag_format = "v$version"
version_files = [
    "pyproject.toml:version",
    "src/iris/__init__.py:__version__"
]

[tool.commitizen.customize]
message_template = "{{change_type}}({{scope}}): {{message}}"
example = "feat(auth): add OAuth2 support"
schema = "<type>(<scope>): <subject>"
schema_pattern = "^(feat|fix|docs|style|refactor|perf|test|chore)(\\(\\w+\\))?:\\s.+"

bump_pattern = "^(feat|fix|perf)"
bump_map = {"feat" = "MINOR", "fix" = "PATCH", "perf" = "PATCH"}
```

### Usage

```bash
# Interactive commit (recommended for developers)
cz commit

# Or use git commit normally (will be validated by pre-commit hook)
git commit -m "feat(ci): add GitHub Actions workflow"
```

### References

- [Commitizen Documentation](https://commitizen-tools.github.io/commitizen/)
- [Conventional Commits Specification](https://www.conventionalcommits.org/)

---

## 8. Task Runner: Just

### Decision

Use **just** (command runner) for standardized development commands.

### Rationale

1. **Constitution Mandate**: Principle 19 requires `just test`, `just lint`, etc.
2. **Cross-Platform**: Works on Windows, macOS, Linux
3. **Simple Syntax**: Makefile-like but without Make's complexity
4. **Fast**: Written in Rust, instant startup
5. **Already Adopted**: Project already uses `just` per constitution

### Justfile Commands

```justfile
# justfile

# Run all tests
test:
    uv run pytest

# Run linting
lint:
    uv run ruff check .
    uv run mypy src/
    npm run lint

# Format code
format:
    uv run ruff format .
    npm run format

# Type checking
type-check:
    uv run mypy src/
    npm run type-check

# Run CI locally (matches GitHub Actions)
ci:
    just lint
    just type-check
    just test

# Install pre-commit hooks
setup-hooks:
    pre-commit install
    pre-commit install --hook-type commit-msg
```

### References

- [Just Documentation](https://just.systems/)
- [Just GitHub Repository](https://github.com/casey/just)

---

## 9. Branch Protection & PR Requirements

### Decision

Implement **strict branch protection** on `main` with required status checks and code review.

### Rationale

1. **Constitution Mandate**: Principle 18 requires PR reviews and CI passing
2. **Quality Gate**: Prevents broken code from reaching main
3. **Accountability**: Code review ensures knowledge sharing
4. **Automation**: GitHub enforces rules, no manual oversight needed

### Protection Rules

```yaml
# Applied via GitHub repository settings (can be automated with Terraform/API)
Branch: main
  Require pull request before merging: true
    Required approvals: 1
    Dismiss stale reviews: true
    Require review from Code Owners: false (single developer project)
  
  Require status checks to pass:
    # Ubuntu - 2 OS × 2 Python = 4 jobs
    - CI / test (ubuntu-latest, 3.12)
    - CI / test (ubuntu-latest, 3.13)
    - CI / test (ubuntu-22.04, 3.12)
    - CI / test (ubuntu-22.04, 3.13)
    
    # Windows - 2 OS × 2 Python = 4 jobs
    - CI / test (windows-latest, 3.12)
    - CI / test (windows-latest, 3.13)
    - CI / test (windows-2022, 3.12)
    - CI / test (windows-2022, 3.13)
    
    # macOS - 2 OS × 2 Python = 4 jobs
    - CI / test (macos-latest, 3.12)
    - CI / test (macos-latest, 3.13)
    - CI / test (macos-14, 3.12)
    - CI / test (macos-14, 3.13)
    
    # Quality & Security checks
    - CI / lint
    - CI / security-scan
    - CodeQL
  
  Require branches to be up to date: true
  Require linear history: false (allow merge commits)
  
  Do not allow bypassing: true (even admins must follow rules)
  Allow force pushes: false
  Allow deletions: false
```

### References

- [GitHub Branch Protection Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

---

## 10. Workflow Triggers & Optimization

### Decision

Three distinct workflows with different triggers and scopes:

1. **Workflow A** (Feature Branch): `push` to any branch except `main` - Fast feedback
2. **Workflow B** (PR to Main): `pull_request` targeting `main` - Comprehensive validation
3. **Workflow C** (Post-Merge): `push` to `main` - Optional release/tagging

### Rationale

1. **Fast Feedback Loop**: Developers get quick results on feature branches (lint + tests only)
2. **Comprehensive Gate**: Full validation before merge (security, coverage, all platforms)
3. **Separation of Concerns**: Don't run expensive jobs on every push
4. **CI Cost Optimization**: Avoid redundant work, use appropriate scope for each stage

### Workflow Scope Comparison

| Check | Workflow A (Feature) | Workflow B (PR to Main) | Workflow C (Post-Merge) |
|-------|---------------------|------------------------|-------------------------|
| **OS Coverage** | Latest only (3 OS) | Latest + Previous (6 OS) | ❌ Skip |
| **Python Versions** | 3.12 only | 3.12 + 3.13 | ❌ Skip |
| **Total Jobs** | 3 jobs | 12 jobs | N/A |
| Linting | ✅ Quick validation | ✅ Full validation | ❌ Skip (already validated) |
| Type Check | ✅ Quick validation | ✅ Full validation | ❌ Skip |
| Tests | ✅ Basic (3 platforms) | ✅ Comprehensive (6 OS × 2 Python) | ❌ Skip |
| Security Scan | ❌ Skip | ✅ Full (bandit, safety, CodeQL) | ❌ Skip |
| Coverage Check | ❌ Skip | ✅ Required 80%+ | ❌ Skip |
| Release/Tag | ❌ Skip | ❌ Skip | ✅ Optional |

### Expected Performance

- **Workflow A** (Feature Branch): ~3-5 minutes wall-clock time (3 jobs in parallel)
- **Workflow B** (PR to Main): ~10-15 minutes wall-clock time (12 jobs in parallel)
- **Workflow C** (Post-Merge): ~1-2 minutes (optional release automation)

### References

- [GitHub Actions Triggering Workflows](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow)
- [CI/CD Best Practices](https://docs.github.com/en/actions/guides/about-continuous-integration)

---

## 11. Test Coverage Enforcement

### Decision

Require **minimum 80% test coverage** with coverage reports uploaded to artifacts.

### Rationale

1. **Constitution Mandate**: Principle 6 requires specific coverage targets (85% overall, but we start at 80% minimum)
2. **Quality Assurance**: High coverage reduces bugs
3. **Trend Tracking**: Coverage reports show coverage over time
4. **Blocking Mechanism**: CI fails if coverage drops below threshold

### Implementation

```yaml
# In CI workflow
- name: Run Tests with Coverage
  run: |
    uv run pytest --cov=src --cov-report=xml --cov-report=html --cov-report=term
    
- name: Check Coverage Threshold
  run: |
    uv run coverage report --fail-under=80

- name: Upload Coverage Report
  uses: codecov/codecov-action@v4
  with:
    file: ./coverage.xml
    fail_ci_if_error: true
```

### Configuration

```toml
# pyproject.toml
[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/test_*.py"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
    "if TYPE_CHECKING:",
]
precision = 2
```

### References

- [Coverage.py Documentation](https://coverage.readthedocs.io/)
- [Codecov Documentation](https://docs.codecov.com/)

---

## Summary of Key Decisions

| Decision Area | Choice | Primary Rationale |
|---------------|--------|-------------------|
| Python Linter/Formatter | **ruff** | All-in-one, 10-100x faster, auto-fix |
| Type Checking | **mypy** (strict) | Industry standard, constitution mandate |
| Security Scanning | **Bandit + Safety + CodeQL** | Multi-layered defense, risk-based policy |
| Frontend Linting | **ESLint + Prettier** | Industry standard, separation of concerns |
| Matrix Strategy | **Two-tier: 3 jobs (feature) / 12 jobs (PR)** | Fast feedback + comprehensive validation |
| Pre-commit Framework | **pre-commit** | Language-agnostic, standardized, fast |
| Commit Standards | **Commitizen** | Interactive, Python-native, constitution mandate |
| Task Runner | **just** | Already adopted, cross-platform, simple |
| Branch Protection | **Strict rules on main** | Constitution compliance, quality gate |
| Workflow Strategy | **3 workflows (A/B/C)** | Fast feedback vs comprehensive validation |
| Coverage Threshold | **80% minimum** | Constitution alignment, quality assurance |

---

## Open Questions & Decisions

All research complete. No open questions remain.

---

**Research Status**: ✅ COMPLETE  
**Ready for Phase 1**: YES  
**Next Step**: Generate data-model.md, contracts/, and quickstart.md

