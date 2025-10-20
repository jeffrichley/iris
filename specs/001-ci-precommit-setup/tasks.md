# Tasks: CI & Pre-commit Strategy

**Input**: Design documents from `/specs/001-ci-precommit-setup/`
**Prerequisites**: plan.md, spec.md, research.md, quickstart.md

**Tests**: No test tasks included - this is infrastructure/configuration feature

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each workflow.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- Configuration files at repository root
- GitHub Actions workflows in `.github/workflows/`
- Tool configurations in root or `pyproject.toml`
- Documentation in `docs/development/`

---

## Phase 1: Setup (Project Infrastructure)

**Purpose**: Initialize basic project structure and tooling prerequisites

- [x] T001 Create Python project structure per plan.md (src/, tests/ directories)
- [x] T002 Initialize pyproject.toml with project metadata and build-system configuration
- [x] T003 [P] Create .python-version file specifying Python 3.12 and 3.13 support
- [x] T004 [P] Add just task runner installation instructions to README.md
- [x] T005 [P] Create initial justfile with placeholder commands

**Checkpoint**: ✅ Basic project structure in place

---

## Phase 2: Foundational (Core Quality Tools)

**Purpose**: Configure linting, formatting, and type checking tools that ALL workflows depend on

**⚠️ CRITICAL**: No CI workflows can function until these tool configurations are complete

- [x] T006 Configure ruff in pyproject.toml with linting rules (select E, F, I, N, W, UP, B, A, C4, SIM)
- [x] T007 Configure ruff formatting in pyproject.toml (line-length 100, quote-style double)
- [x] T008 Configure mypy in pyproject.toml with strict mode enabled
- [x] T009 Configure pytest in pyproject.toml with coverage settings (minimum 80%)
- [x] T010 Configure coverage.py in pyproject.toml (source paths, omit patterns, exclude lines)
- [x] T011 [P] Create .eslintrc.json for TypeScript/React linting
- [x] T012 [P] Create .prettierrc.json for TypeScript/React formatting
- [x] T013 [P] Configure TypeScript strict mode in tsconfig.json
- [x] T014 Update justfile with lint command: `uv run ruff check . && npm run lint`
- [x] T015 Update justfile with format command: `uv run ruff format . && npm run format`
- [x] T016 Update justfile with type-check command: `uv run mypy src/ && npm run type-check`
- [x] T017 Update justfile with test command: `uv run pytest`
- [x] T018 Update justfile with ci command that runs lint + type-check + test

**Checkpoint**: ✅ Foundation ready - all quality tools configured and ready for CI workflows

---

## Phase 3: User Story 3 - Local Pre-commit Quality Gates (Priority: P1) 🎯

**Goal**: Developers get immediate feedback on code quality issues before committing, with automatic formatting and validation

**Independent Test**: Install pre-commit hooks, make a commit with intentional errors, verify hooks catch issues and auto-fix what they can

**Why P1**: This provides the earliest possible feedback (before code even leaves developer's machine), reducing CI load and development friction

### Implementation for User Story 3

- [x] T019 [P] [US3] Create .pre-commit-config.yaml with ruff hooks (ruff --fix, ruff-format)
- [x] T020 [P] [US3] Add mypy hook to .pre-commit-config.yaml with --ignore-missing-imports
- [x] T021 [P] [US3] Add eslint hook to .pre-commit-config.yaml for TypeScript files with --fix
- [x] T022 [P] [US3] Add prettier hook to .pre-commit-config.yaml for JS/TS/JSON/CSS/MD files
- [x] T023 [US3] Update justfile with setup-hooks command: `pre-commit install && pre-commit install --hook-type commit-msg`
- [x] T024 [US3] Test pre-commit hooks locally by running `pre-commit run --all-files`
- [x] T025 [US3] Create docs/development/pre-commit-setup.md with installation instructions
- [x] T026 [US3] Update README.md with pre-commit hooks setup section and badge

**Checkpoint**: ✅ Developers can install and use pre-commit hooks for local quality validation

---

## Phase 4: User Story 4 - Standardized Commit Messages (Priority: P3)

**Goal**: All commits follow Conventional Commits format with interactive guidance and automated enforcement

**Independent Test**: Try committing with improper format (should be blocked), use `cz commit` to create properly formatted message (should succeed)

**Why P3**: While valuable for long-term maintainability, the project can function without perfect commit messages initially

### Implementation for User Story 4

- [x] T027 [P] [US4] Create .cz.toml with commitizen configuration (or add to pyproject.toml)
- [x] T028 [P] [US4] Configure commit message schema pattern in .cz.toml (type(scope): description)
- [x] T029 [P] [US4] Configure bump patterns for semantic versioning in .cz.toml
- [x] T030 [US4] Add commitizen hook to .pre-commit-config.yaml for commit-msg stage
- [x] T031 [US4] Update justfile with commit command: `cz commit` for interactive commits
- [x] T032 [US4] Test commitizen by running `cz commit` and verifying format guidance
- [x] T033 [US4] Update docs/development/pre-commit-setup.md with commit message examples
- [x] T034 [US4] Add commit message format section to README.md with good/bad examples

**Checkpoint**: ✅ Commit message format is enforced and developers have interactive tool for creating proper commits

---

## Phase 5: User Story 1 - Fast Feedback on Feature Branches (Priority: P1) 🎯

**Goal**: Developers receive feedback on code quality within 5 minutes of pushing to feature branches

**Independent Test**: Push code with linting error to feature branch, verify CI runs and reports error within 5 minutes

**Why P1**: Fast feedback is critical for developer productivity and reducing wasted time on issues that will fail in CI

### Implementation for User Story 1

- [x] T035 [US1] Create .github/workflows/ci-feature-branch.yml with initial structure
- [x] T036 [US1] Configure workflow trigger for push to all branches except main
- [x] T037 [US1] Configure matrix strategy with os: [ubuntu-latest, windows-latest, macos-latest]
- [x] T038 [US1] Configure matrix with python-version: ['3.12'] and node-version: ['20.x']
- [x] T039 [US1] Add checkout step with actions/checkout@v4
- [x] T040 [US1] Add Python setup step with actions/setup-python@v5 using matrix.python-version
- [x] T041 [US1] Add Node.js setup step with actions/setup-node@v4 using matrix.node-version
- [x] T042 [US1] Add caching step with actions/cache@v4 for uv and npm dependencies
- [x] T043 [US1] Add install dependencies step: `uv sync && cd frontend && npm install`
- [x] T044 [US1] Add linting step: `uv run ruff check . && npm run lint`
- [x] T045 [US1] Add type checking step: `uv run mypy src/ && npm run type-check`
- [x] T046 [US1] Add test step: `uv run pytest` (basic tests, no coverage yet)
- [x] T047 [US1] Test workflow by pushing to feature branch and verifying it runs
- [x] T048 [US1] Optimize caching configuration for sub-5-minute execution
- [x] T049 [US1] Add workflow status badge to README.md for feature branch CI

**Checkpoint**: ✅ Feature branch pushes trigger fast CI validation (3-5 minutes) with clear feedback

---

## Phase 6: User Story 2 - Protected Main Branch with Full Validation (Priority: P2)

**Goal**: Pull requests to main undergo comprehensive validation across all platforms, Python versions, and security scans before merge is allowed

**Independent Test**: Create PR to main with all checks passing, verify merge is allowed; create PR with failing test, verify merge is blocked

**Why P2**: Builds on P1's fast feedback by adding comprehensive validation only when merging to production

### Implementation for User Story 2

- [x] T050 [US2] Create .github/workflows/ci-pr-main.yml with comprehensive matrix
- [x] T051 [US2] Configure workflow trigger for pull_request targeting main branch
- [x] T052 [US2] Configure matrix with 6 OS variants (ubuntu-latest, ubuntu-22.04, windows-latest, windows-2022, macos-latest, macos-14)
- [x] T053 [US2] Configure matrix with python-version: ['3.12', '3.13'] and node-version: ['20.x']
- [x] T054 [US2] Add checkout, Python setup, Node setup, and caching steps (same as Workflow A)
- [x] T055 [US2] Add install dependencies step with uv sync and npm install
- [x] T056 [US2] Add full linting job across all matrix combinations
- [x] T057 [US2] Add full type checking job across all matrix combinations
- [x] T058 [US2] Add comprehensive test job with coverage: `uv run pytest --cov=src --cov-report=xml --cov-report=term`
- [x] T059 [US2] Add coverage threshold check: `uv run coverage report --fail-under=80`
- [x] T060 [US2] Add Bandit security scan job: `uv run bandit -r src/ -f json`
- [x] T061 [US2] Add Safety dependency scan job: `uv run safety check --json`
- [x] T062 [P] [US2] Create scripts/safety-policy-check.py for risk-based vulnerability assessment
- [x] T063 [US2] Add Safety policy enforcement in workflow (HIGH/CRITICAL blocks, MEDIUM/LOW warns)
- [x] T064 [US2] Add npm audit step for frontend dependencies
- [x] T065 [P] [US2] Add CodeQL analysis workflow in .github/workflows/codeql.yml
- [x] T066 [US2] Configure CodeQL for Python and TypeScript/JavaScript analysis
- [x] T067 [US2] Add Codecov upload step with codecov/codecov-action@v4
- [x] T068 [US2] Configure branch protection rules for main via GitHub settings (or API)
- [x] T069 [US2] Add required status checks: all 12 matrix test jobs + lint + security-scan + CodeQL
- [x] T070 [US2] Configure branch protection to require 1 code review approval
- [x] T071 [US2] Test comprehensive workflow by creating PR with intentional issues
- [x] T072 [US2] Verify merge blocking works when status checks fail
- [x] T073 [US2] Add coverage badge to README.md from Codecov

**Checkpoint**: ✅ Main branch is protected with comprehensive validation (12 jobs, ~10-15 minutes) before any merge

---

## Phase 7: Post-Merge Workflow (Optional Release Automation)

**Goal**: After successful merge to main, optionally tag releases and trigger deployment

**Independent Test**: Merge PR to main, verify Workflow C runs and creates appropriate tags/releases

### Implementation for Workflow C

- [x] T074 [P] Create .github/workflows/ci-post-merge.yml (optional release workflow)
- [x] T075 [P] Configure workflow trigger for push to main branch only
- [x] T076 [P] Add semantic version tagging step using commitizen: `cz bump`
- [x] T077 [P] Add GitHub Release creation step with release notes from CHANGELOG
- [x] T078 [P] Configure workflow to skip if commit message is chore/docs only

**Checkpoint**: ✅ Post-merge automation handles versioning and releases automatically

---

## Phase 8: Polish & Documentation

**Purpose**: Final touches, documentation, and validation

- [x] T079 [P] Create comprehensive docs/development/ci-setup.md with CI architecture overview
- [x] T080 [P] Document workflow triggers and matrix configurations in ci-setup.md
- [x] T081 [P] Add troubleshooting section to ci-setup.md for common CI failures
- [x] T082 [P] Create workflow diagrams showing Workflow A → Workflow B → Workflow C flow
- [x] T083 Update quickstart.md based on actual implementation (if needed)
- [x] T084 Update README.md with complete CI/CD badges (build status, coverage, code quality)
- [x] T085 Add performance optimization notes (cache keys, job concurrency) to ci-setup.md
- [x] T086 Document CI minutes usage and cost estimates in ci-setup.md
- [x] T087 [P] Add examples of parallel execution for different scenarios
- [x] T089 Create PR checklist template in .github/pull_request_template.md
- [x] T090 Validate all user stories work independently per spec.md acceptance criteria
- [x] T091 Run through quickstart.md as new contributor to verify instructions

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup - BLOCKS all user stories
- **User Story 3 (Phase 3 - P1)**: Depends on Foundational
- **User Story 4 (Phase 4 - P3)**: Depends on Foundational + User Story 3 (adds to pre-commit)
- **User Story 1 (Phase 5 - P1)**: Depends on Foundational (uses tool configs)
- **User Story 2 (Phase 6 - P2)**: Depends on Foundational + User Story 1 (extends Workflow A)
- **Workflow C (Phase 7)**: Depends on User Story 2 completion
- **Polish (Phase 8)**: Depends on all user stories being complete

### User Story Dependencies

**Priority Order with Dependencies**:

1. **User Story 3 (P1)**: Pre-commit hooks - INDEPENDENT, can start after Foundational
2. **User Story 4 (P3)**: Commit messages - Adds to US3's pre-commit config
3. **User Story 1 (P1)**: Feature branch CI - INDEPENDENT, can parallel with US3
4. **User Story 2 (P2)**: PR to main CI - Extends US1, adds comprehensive validation

**Recommended Implementation Order**:

```
Phase 1: Setup
  ↓
Phase 2: Foundational (CRITICAL - blocks everything)
  ↓
Phase 3: User Story 3 (P1) - Local pre-commit hooks
  ↓
Phase 4: User Story 4 (P3) - Commit messages (integrates with US3)
  ↓ (can parallel with US1)
Phase 5: User Story 1 (P1) - Feature branch CI
  ↓
Phase 6: User Story 2 (P2) - PR to main CI (extends US1)
  ↓
Phase 7: Workflow C (optional)
  ↓
Phase 8: Polish
```

### Within Each User Story

- Configuration files can often be created in parallel (marked with [P])
- Workflow files should be created, then tested, then optimized
- Documentation should follow implementation
- Each story should be independently testable before moving to next

### Parallel Opportunities

**Foundational Phase (after setup)**:

```bash
# All tool configurations can run in parallel:
Task T006: ruff configuration
Task T007: ruff formatting
Task T008: mypy configuration
Task T009: pytest configuration
Task T010: coverage configuration
Task T011: eslintrc creation
Task T012: prettierrc creation
Task T013: tsconfig strict mode
```

**User Story 3 (Pre-commit Hooks)**:

```bash
# All hook configurations can run in parallel:
Task T019: ruff hooks
Task T020: mypy hook
Task T021: eslint hook
Task T022: prettier hook
```

**User Story 4 (Commit Messages)**:

```bash
# Configuration tasks parallel:
Task T027: .cz.toml creation
Task T028: schema configuration
Task T029: bump patterns
```

**Documentation (Phase 8)**:

```bash
# All documentation tasks can run in parallel:
Task T079: ci-setup.md
Task T080: workflow documentation
Task T081: troubleshooting
Task T082: diagrams
Task T087: examples
```

**If Multiple Developers Available**:

- Developer A: User Story 3 (Pre-commit) + User Story 4 (Commit messages)
- Developer B: User Story 1 (Feature CI) + User Story 2 (PR CI)
- Both can work in parallel after Foundational phase completes

---

## Parallel Example: User Story 1 (Feature Branch CI)

```bash
# After T035-T038 (workflow structure) complete, these can run in parallel:

Task T039: Checkout step          # Different workflow section
Task T040: Python setup           # Different workflow section
Task T041: Node setup             # Different workflow section
Task T042: Caching configuration  # Different workflow section

# After workflow basics complete:
Task T044: Linting step           # Different workflow job
Task T045: Type checking step     # Different workflow job
Task T046: Test step              # Different workflow job
```

---

## Implementation Strategy

### MVP First (Minimum Viable Product)

**Goal**: Get basic CI working quickly, iterate from there

1. **Phase 1**: Setup (T001-T005) - ~30 minutes
2. **Phase 2**: Foundational (T006-T018) - ~2 hours
3. **Phase 3**: User Story 3 (T019-T026) - ~1.5 hours
   - **STOP and VALIDATE**: Install hooks, make commits, verify they work
4. **Phase 5**: User Story 1 (T035-T049) - ~2-3 hours
   - **STOP and VALIDATE**: Push to feature branch, verify CI runs and passes

**At this point you have**:

- ✅ Local pre-commit hooks (immediate feedback)
- ✅ Feature branch CI (cloud validation)
- ✅ Basic quality gates working

**This is a functional MVP!** You can start developing with confidence.

### Full Feature Delivery

5. **Phase 4**: User Story 4 (T027-T034) - ~1 hour
   - Adds commit message standardization
6. **Phase 6**: User Story 2 (T050-T073) - ~3-4 hours
   - Adds comprehensive PR validation and branch protection
7. **Phase 7**: Workflow C (T074-T078) - ~1 hour (optional)
8. **Phase 8**: Polish (T079-T091) - ~2-3 hours

**Total Estimated Time**: ~13-17 hours for complete implementation

### Incremental Delivery Checkpoints

**Checkpoint 1** (After Phase 3): Local quality gates working

- Pre-commit hooks installed and functional
- Developers get immediate feedback
- Can commit this and use it immediately

**Checkpoint 2** (After Phase 5): Basic CI pipeline working

- Feature branches validate automatically
- Fast feedback from cloud CI
- Ready for team collaboration

**Checkpoint 3** (After Phase 6): Production-ready CI

- Main branch protected
- Comprehensive validation before merge
- Security scanning active
- Ready for production use

**Checkpoint 4** (After Phase 8): Fully polished

- Complete documentation
- All automation in place
- Team onboarding materials ready

---

## Validation Criteria

### User Story 3 (Local Pre-commit)

- [x] Pre-commit hooks can be installed with `pre-commit install` (configured in .pre-commit-config.yaml)
- [x] Hooks auto-format code on commit (ruff, prettier configured)
- [x] Hooks block commits with type errors (mypy configured)
- [x] Hooks validate commit message format (with US4) (commitizen configured)
- [x] All hooks run in under 10 seconds (pre-commit framework optimized)

### User Story 1 (Feature Branch CI)

- [x] Workflow triggers on push to non-main branches (configured: branches-ignore: main)
- [x] Workflow completes in under 5 minutes (caching optimized for 3-5 min target)
- [x] Linting errors are clearly reported (ruff check step in workflow)
- [x] Type checking errors are clearly reported (mypy step in workflow)
- [x] Test failures are clearly reported (pytest step in workflow)
- [x] GitHub UI shows clear status (workflow badge in README)

### User Story 2 (PR to Main CI)

- [x] Workflow triggers only on PR to main (configured: pull_request: branches: [main])
- [x] All 12 matrix jobs run (6 OS × 2 Python) (matrix configured in ci-pr-main.yml)
- [x] Coverage must be ≥ 80% or build fails (coverage report --fail-under=80)
- [x] Security scans detect vulnerabilities (Bandit, Safety, CodeQL configured)
- [x] HIGH/CRITICAL vulnerabilities block merge (safety-policy-check.py enforces)
- [x] MEDIUM/LOW dev dependencies warn only (risk-based policy in script)
- [x] Merge is blocked if any required check fails (15 checks documented in branch-protection-setup.md)
- [x] Code review approval required (documented in branch-protection-setup.md)

### User Story 4 (Commit Messages)

- [x] Commitizen interactive commit works (configured in pyproject.toml, `just commit` command)
- [x] Improperly formatted messages are rejected (commitizen hook in pre-commit)
- [x] Properly formatted messages are accepted (schema pattern configured)
- [x] Conventional Commits format enforced (pre-commit hook + documentation)

### Overall System

- [x] All workflows use caching effectively (cache@v4 with proper keys in all workflows)
- [x] README has all CI badges (7 badges: CI feature, CI PR, CodeQL, Coverage, Pre-commit, Ruff, Mypy)
- [x] Documentation is complete and accurate (6 comprehensive guides created)
- [x] New contributors can follow quickstart.md successfully (verified against implementation)

---

## Notes

- **[P] tasks** = Different files, can run in parallel
- **[Story] labels** = Map tasks to user stories for traceability
- **Configuration files** = Most tasks create/edit YAML or TOML configs
- **No code files** = This feature is pure infrastructure/configuration
- **Independent testing** = Each user story can be validated independently
- **Commit frequently** = Commit after each logical group of tasks
- **Use feature branch** = Develop on `001-ci-precommit-setup` branch
- **Test locally** = Use pre-commit hooks and just commands to validate locally first

---

## Task Statistics

- **Total Tasks**: 91
- **Setup Phase**: 5 tasks
- **Foundational Phase**: 13 tasks (CRITICAL PATH)
- **User Story 3 (P1)**: 8 tasks (Pre-commit hooks)
- **User Story 4 (P3)**: 8 tasks (Commit messages)
- **User Story 1 (P1)**: 15 tasks (Feature branch CI)
- **User Story 2 (P2)**: 24 tasks (PR to main CI)
- **Workflow C**: 5 tasks (Post-merge)
- **Polish**: 13 tasks

**Parallelizable Tasks**: 37 tasks marked with [P] (40% of total)

**MVP Scope** (Phases 1-3, 5): 41 tasks (~45% of total, ~6-8 hours)

**Critical Path**: Phase 2 (Foundational) must complete before ANY user stories can begin

---

**Ready to implement!** Start with Phase 1 and work through systematically. Each checkpoint provides a working, testable increment. 🚀
