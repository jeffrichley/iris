Here is the detailed **CI & Pre-commit Strategy** document for your AI agent. It’s written with *specific versions, actions, tools, and workflows* (no “or” options) to achieve world-class quality.

---

# CI & Pre-commit Strategy for Project Iris

### Version 1.0 — October 2025

---

## 1. Objectives

* Ensure code quality, cross-platform correctness, security compliance, and a pristine `main` branch at all times.
* Provide fast feedback on feature/topic branches.
* Maintain separate workflows for development and release merges.
* Enforce standardized commit message practices for traceability.

---

## 2. Branch & Workflow Policy

**Branches:**

* Development work happens on feature/topic branches (e.g., `feature/add-task`, `bugfix/login`).
* The `main` branch is protected: no direct commits, merges only via pull requests after all CI jobs pass.

**Workflows:**

* Workflow **A**: Triggered on `push` to any branch *except* `main`. Runs a subset of CI jobs (basic lint + tests) for fast feedback.
* Workflow **B**: Triggered on `pull_request` targeting `main`. Runs full CI jobs including lint + tests + static analysis + security scans.
* Workflow **C**: Triggered on `push` to `main` after merge. Runs final release / tagging jobs (optional).
* Merge protection rule: On `main`, require success of Workflow B, at least one code review approval, and zero failing checks before allowing merge.

---

## 3. Matrix Build Configuration

**Operating Systems:**

* `ubuntu-latest`
* `windows-latest`
* `macos-latest`

**Backend (Python):**

* Python versions: `3.12`, `3.13` (tested on all OS runners)
* Use GitHub Action `actions/setup-python@v6` with `python-version: ${{ matrix.python-version }}` ([GitHub][1])

**Frontend (Node.js):**

* Node.js version: latest LTS (for example, `20.x`)
* Use `actions/setup-node@v5` or latest stable.
* Run on the same OS matrix as backend jobs for unified visibility.

**Matrix sample snippet in workflow YAML:**

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    python-version: [3.12, 3.13]
    node-version: [20.x]
  fail-fast: false
```

---

## 4. Tooling: Linting, Testing, Static Analysis & Security

**Backend (Python):**

* Use `ruff` for linting, formatting, and auto-fix capabilities (no `black`).
* Use `mypy` for static type checking.
* Use `bandit` for security auditing of Python code.
* Use `safety` (or equivalent) for dependency vulnerability scanning.

**Frontend (TypeScript + React + Tauri):**

* Use `eslint` and `prettier` for code style and linting.
* Use `typescript` compiler with `strict` mode enabled.
* Use `npm audit` or GitHub’s dependency scanning for vulnerabilities.

**Global:**

* Enable GitHub CodeQL scanning for the full repository for security & code-analysis coverage.

---

## 5. Pre-commit Hook Configuration

Use `pre-commit` framework with a `.pre-commit-config.yaml` file.

**Hooks for Python files:**

* `ruff --fix` stage `pre-commit`
* `ruff --check` stage `pre-commit`
* `isort` stage `pre-commit`
* `mypy --ignore-missing-imports` stage `pre-commit`
* `commitizen commit` stage `prepare-commit-msg` or `commit-msg`

**Hooks for TypeScript/Frontend files:**

* `eslint --fix` stage `pre-commit`
* `prettier --write` stage `pre-commit`
* `npm audit` stage `pre-push` (optional)

**Commit message practice:**

* Install `commitizen` and enforce Conventional Commits format (e.g., `feat(scope): description`). ([Conventional Commits][2])
* Use `commitlint` or `commitizen check` in `commit-msg` hook to block bad messages. ([GitHub][3])

---

## 6. Gating & Metrics for Merges to Main

Requirements before `main` merge:

* Lint errors: **0** on backend and frontend.
* Type checking errors: **0** by `mypy` and `tsc`.
* Test suite: must pass entirely with no failures; code coverage minimum: **80%** (backend + frontend).
* Security scan: no critical vulnerabilities allowed; dependency audit must pass.
* Commit message convention: enforced by `commitizen`/`commitlint`.
* All matrix jobs must pass (OS × Python × Node combos).

---

## 7. Implementation Steps for AI Agent

1. Generate `.github/workflows/ci.yml` file incorporating matrix OS + Python + Node versions.
2. Generate `.pre-commit-config.yaml` file with specified hooks and stages.
3. Install `commitizen` configuration (`.cz.toml` or `pyproject.toml` section) enforcing Conventional Commits.
4. Configure GitHub branch protection rules for `main` with required status checks (Workflow B) and review approval.
5. Add `README.md` badges for build status, lint status, coverage status.
6. Add `justfile` or equivalent task runner entries for local dev commands: `just lint`, `just test`, `just type-check`, `just format`.
7. Ensure caching in workflows for pip and npm dependencies to optimize build times.

---

## 8. Next Steps

* Agent executes scaffolding and commits base CI + pre-commit config.
* Developers run local `pre-commit install` and validate commit message flow.
* Feature branches start with normal commits; enforce commit message format and local linting.
* Pull requests into `main` trigger full CI; agent monitors and blocks if any job fails.

---

If you confirm, I’ll provide the **exact YAML snippet and configuration files** (for `.pre-commit-config.yaml`, `.cz.toml`, and `ci.yml`) that the AI agent should use verbatim.

[1]: https://github.com/actions/setup-python?utm_source=chatgpt.com "Set up your GitHub Actions workflow with a specific version of Python"
[2]: https://www.conventionalcommits.org/en/v1.0.0/?utm_source=chatgpt.com "Conventional Commits"
[3]: https://github.com/conventional-changelog/commitlint?utm_source=chatgpt.com "conventional-changelog/commitlint: Lint commit messages - GitHub"
