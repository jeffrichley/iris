# Implementation Plan: CI & Pre-commit Strategy

**Branch**: `001-ci-precommit-setup` | **Date**: October 20, 2025 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-ci-precommit-setup/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Establish a comprehensive CI/CD pipeline and pre-commit hook system that enforces code quality, security, and cross-platform compatibility across the Iris project. The system provides three-tiered validation: local pre-commit hooks for immediate feedback, feature branch CI for fast validation, and comprehensive PR-to-main validation including security scans and matrix builds across all supported platforms and Python versions.

## Technical Context

**Language/Version**: Python 3.12, 3.13 + TypeScript (strict mode) + Node.js 20.x LTS
**Primary Dependencies**: GitHub Actions, ruff, mypy, bandit, safety, eslint, prettier, pre-commit framework, commitizen, just (task runner)
**Storage**: N/A (configuration files only - no data storage)
**Testing**: This feature establishes the testing infrastructure itself (pytest for backend, standard test frameworks for frontend)
**Target Platform**: GitHub Actions runners (ubuntu-latest, windows-latest, macos-latest)
**Project Type**: Infrastructure/Configuration (CI/CD and quality tooling setup)
**Performance Goals**: Feature branch CI feedback < 5 minutes, PR-to-main CI < 15 minutes, pre-commit hooks < 10 seconds
**Constraints**: Zero tolerance for linting/type errors before merge, 80% minimum test coverage, cross-platform validation required
**Scale/Scope**: Matrix builds (3 OS × 2 Python versions × 1 Node version = 6 backend combinations), multiple quality tools coordinated, ~10-15 configuration files

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

### Alignment with Constitution Principles

✅ **Principle 1: Type Safety First**

- **Alignment**: This feature ENFORCES type safety through mypy (Python) and tsc strict mode (TypeScript)
- **Implementation**: FR-014, FR-017, FR-018, FR-025 mandate zero type checking errors
- **Status**: FULLY COMPLIANT - This feature implements the principle

✅ **Principle 2: Explicit Over Implicit**

- **Alignment**: CI workflows are explicit, documented, and visible
- **Implementation**: Three distinct workflows (A, B, C) with clear purposes, FR-044 requires clear error messages
- **Status**: FULLY COMPLIANT

✅ **Principle 6: Test Pyramid**

- **Alignment**: This feature ENFORCES test pyramid through coverage requirements
- **Implementation**: FR-019, FR-026 mandate 80% minimum coverage
- **Status**: FULLY COMPLIANT - This feature implements the principle

✅ **Principle 7: Test Quality**

- **Alignment**: Enforces test quality standards from constitution
- **Implementation**: Uses `just test` (FR-043), no warnings disabled (constitution requirement)
- **Status**: FULLY COMPLIANT

✅ **Principle 17: Version Control**

- **Alignment**: Enforces Conventional Commits as required by constitution
- **Implementation**: FR-038, FR-039, FR-040, FR-041 mandate Conventional Commits format
- **Status**: FULLY COMPLIANT - This feature implements the principle

✅ **Principle 18: Code Review**

- **Alignment**: Enforces PR requirements, CI must pass, coverage must not decrease
- **Implementation**: FR-009-FR-012 establish branch protection matching constitution requirements
- **Status**: FULLY COMPLIANT - This feature implements the principle

✅ **Principle 19: Tooling Compliance**

- **Alignment**: Uses `just` commands as required, uses `uv` for Python (already in project)
- **Implementation**: FR-043 mandates `just lint`, `just test`, `just type-check`, `just format`
- **Status**: FULLY COMPLIANT

✅ **Performance Requirements (Principle 13)**

- **Alignment**: Fast feedback aligns with performance-first mindset
- **Implementation**: SC-001 (5min feedback), optimized with caching (FR-008)
- **Status**: COMPLIANT

### Gate Decision: ✅ PASS

**Rationale**: This feature is foundational infrastructure that IMPLEMENTS many constitution principles rather than violating them. It establishes the enforcement mechanisms for type safety, testing standards, code review processes, and tooling compliance. Zero violations detected.

**Post-Design Re-check Required**: YES (after Phase 1 to verify implementation approach maintains compliance)

---

## Post-Design Constitution Re-check

_Re-evaluated after Phase 1 design completion_

✅ **Type Safety First (Principle 1)**

- **Implementation**: Configured mypy with strict mode, TypeScript strict mode enabled
- **Files**: `pyproject.toml` (mypy config), `tsconfig.json` (TypeScript config)
- **Verification**: FR-017, FR-018, FR-025 ensure zero type errors before merge
- **Status**: COMPLIANT - Strict enforcement configured

✅ **Explicit Over Implicit (Principle 2)**

- **Implementation**: All workflows explicitly documented, clear error messages required (FR-044)
- **Files**: `.github/workflows/*.yml` with detailed comments
- **Status**: COMPLIANT - All automation is transparent and documented

✅ **Error Handling (Principle 4)**

- **Implementation**: Will use rich library for logging (constitution requirement already exists)
- **Note**: CI error messages must be clear and actionable (FR-044)
- **Status**: COMPLIANT - Aligned with existing error handling standards

✅ **Test Pyramid & Quality (Principles 6-7)**

- **Implementation**:
  - Coverage minimum 80% enforced (FR-019, FR-026)
  - Uses `just test` command (constitution requirement)
  - Explicit test markers required (constitution requirement preserved)
  - No warnings disabled (constitution requirement preserved)
- **Files**: `pyproject.toml` (pytest config), `.github/workflows/*.yml` (CI config)
- **Status**: COMPLIANT - Enforces constitution's test standards

✅ **Test Execution (Principle 8)**

- **Implementation**: `just test` command standardized (FR-043)
- **Files**: `justfile` with test commands
- **Status**: COMPLIANT - Matches constitution requirement exactly

✅ **Version Control (Principle 17)**

- **Implementation**:
  - Conventional Commits enforced via commitizen (FR-038-042)
  - Feature branches required (workflow design)
  - PR required for main (FR-009)
  - Squash merge supported
- **Files**: `.cz.toml`, `.pre-commit-config.yaml`, branch protection rules
- **Status**: COMPLIANT - Full implementation of constitution requirements

✅ **Code Review (Principle 18)**

- **Implementation**:
  - All PRs require review (FR-011)
  - CI must pass (FR-010)
  - Coverage cannot decrease (80% minimum enforced)
- **Files**: Branch protection rules, `.github/workflows/ci-pr-main.yml`
- **Status**: COMPLIANT - All review requirements enforced

✅ **Tooling Compliance (Principle 19)**

- **Implementation**:
  - Uses `just` for all commands (FR-043)
  - Uses `uv` for Python (already in project, workflows will use it)
  - Pre-commit hooks installed properly
- **Files**: `justfile`, `.github/workflows/*.yml` (uses `uv run`)
- **Status**: COMPLIANT - Matches tooling requirements

✅ **Performance Requirements (Principle 13)**

- **Implementation**:
  - Feature branch CI < 5 minutes (SC-001)
  - PR validation < 15 minutes (SC-009)
  - Caching strategy implemented (FR-008)
- **Status**: COMPLIANT - Meets performance standards

✅ **Release Standards (Principle 20)**

- **Implementation**:
  - Pre-release checklist enforced via CI (all tests, coverage, security)
  - Workflow C for optional release automation
  - Semantic versioning supported via commitizen
- **Status**: COMPLIANT - Supports release process

### Post-Design Gate Decision: ✅ PASS

**Final Assessment**: Complete design review confirms zero constitutional violations. This feature strengthens constitution compliance by automating enforcement of existing principles. All tooling choices align with constitution requirements.

**Ready for Phase 2**: YES

## Project Structure

### Documentation (this feature)

```
specs/001-ci-precommit-setup/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command) - N/A for this feature
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command) - N/A for this feature
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```
# Configuration/Infrastructure Layout
.github/
└── workflows/
    ├── ci-feature-branch.yml       # Workflow A: Fast feedback on feature branches
    ├── ci-pr-main.yml              # Workflow B: Full validation for PRs to main
    └── ci-post-merge.yml           # Workflow C: Post-merge to main (optional release/tagging)

.pre-commit-config.yaml             # Pre-commit hooks configuration

.commitlintrc.json                  # Commit message linting config (or in pyproject.toml)

.cz.toml                            # Commitizen configuration (or in pyproject.toml)

justfile                            # Task runner commands (lint, test, type-check, format)

# Tool-specific configs (may already exist, will be updated)
pyproject.toml                      # Python project config (ruff, mypy, pytest, coverage sections)
.eslintrc.json                      # ESLint configuration for TypeScript/React
.prettierrc.json                    # Prettier configuration
tsconfig.json                       # TypeScript compiler config with strict mode

# Documentation
README.md                           # Updated with CI badges
docs/
└── development/
    └── ci-setup.md                 # Developer guide for CI and pre-commit hooks
```

**Structure Decision**: This feature creates configuration/infrastructure files at repository root level rather than in `src/` or domain-specific directories. The GitHub Actions workflows go in `.github/workflows/`, pre-commit configuration at root, and tool configurations either at root or in existing config files like `pyproject.toml`. This follows standard practices for CI/CD and quality tooling.

## Complexity Tracking

_Fill ONLY if Constitution Check has violations that must be justified_

**N/A** - No constitutional violations. This feature implements and enforces constitution principles.
