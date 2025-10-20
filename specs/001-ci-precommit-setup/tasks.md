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

- [ ] T001 Create Python project structure per plan.md (src/, tests/ directories)
- [ ] T002 Initialize pyproject.toml with project metadata and build-system configuration
- [ ] T003 [P] Create .python-version file specifying Python 3.12 and 3.13 support
- [ ] T004 [P] Add just task runner installation instructions to README.md
- [ ] T005 [P] Create initial justfile with placeholder commands

**Checkpoint**: Basic project structure in place

---

## Phase 2: Foundational (Core Quality Tools)

**Purpose**: Configure linting, formatting, and type checking tools that ALL workflows depend on

**⚠️ CRITICAL**: No CI workflows can function until these tool configurations are complete

- [ ] T006 Configure ruff in pyproject.toml with linting rules (select E, F, I, N, W, UP, B, A, C4, SIM)
- [ ] T007 Configure ruff formatting in pyproject.toml (line-length 100, quote-style double)
- [ ] T008 Configure mypy in pyproject.toml with strict mode enabled
- [ ] T009 Configure pytest in pyproject.toml with coverage settings (minimum 80%)
- [ ] T010 Configure coverage.py in pyproject.toml (source paths, omit patterns, exclude lines)
- [ ] T011 [P] Create .eslintrc.json for TypeScript/React linting
- [ ] T012 [P] Create .prettierrc.json for TypeScript/React formatting
- [ ] T013 [P] Configure TypeScript strict mode in tsconfig.json
- [ ] T014 Update justfile with lint command: `uv run ruff check . && npm run lint`
- [ ] T015 Update justfile with format command: `uv run ruff format . && npm run format`
- [ ] T016 Update justfile with type-check command: `uv run mypy src/ && npm run type-check`
- [ ] T017 Update justfile with test command: `uv run pytest`
- [ ] T018 Update justfile with ci command that runs lint + type-check + test

**Checkpoint**: Foundation ready - all quality tools configured and ready for CI workflows

---

## Phase 3: User Story 3 - Local Pre-commit Quality Gates (Priority: P1) 🎯

**Goal**: Developers get immediate feedback on code quality issues before committing, with automatic formatting and validation

**Independent Test**: Install pre-commit hooks, make a commit with intentional errors, verify hooks catch issues and auto-fix what they can

**Why P1**: This provides the earliest possible feedback (before code even leaves developer's machine), reducing CI load and development friction

### Implementation for User Story 3

- [ ] T019 [P] [US3] Create .pre-commit-config.yaml with ruff hooks (ruff --fix, ruff-format)
- [ ] T020 [P] [US3] Add mypy hook to .pre-commit-config.yaml with --ignore-missing-imports
- [ ] T021 [P] [US3] Add eslint hook to .pre-commit-config.yaml for TypeScript files with --fix
- [ ] T022 [P] [US3] Add prettier hook to .pre-commit-config.yaml for JS/TS/JSON/CSS/MD files
- [ ] T023 [US3] Update justfile with setup-hooks command: `pre-commit install && pre-commit install --hook-type commit-msg`
- [ ] T024 [US3] Test pre-commit hooks locally by running `pre-commit run --all-files`
- [ ] T025 [US3] Create docs/development/pre-commit-setup.md with installation instructions
- [ ] T026 [US3] Update README.md with pre-commit hooks setup section and badge

**Checkpoint**: Developers can install and use pre-commit hooks for local quality validation

---

## Phase 4: User Story 4 - Standardized Commit Messages (Priority: P3)

**Goal**: All commits follow Conventional Commits format with interactive guidance and automated enforcement

**Independent Test**: Try committing with improper format (should be blocked), use `cz commit` to create properly formatted message (should succeed)

**Why P3**: While valuable for long-term maintainability, the project can function without perfect commit messages initially

### Implementation for User Story 4

- [ ] T027 [P] [US4] Create .cz.toml with commitizen configuration (or add to pyproject.toml)
- [ ] T028 [P] [US4] Configure commit message schema pattern in .cz.toml (type(scope): description)
- [ ] T029 [P] [US4] Configure bump patterns for semantic versioning in .cz.toml
- [ ] T030 [US4] Add commitizen hook to .pre-commit-config.yaml for commit-msg stage
- [ ] T031 [US4] Update justfile with commit command: `cz commit` for interactive commits
- [ ] T032 [US4] Test commitizen by running `cz commit` and verifying format guidance
- [ ] T033 [US4] Update docs/development/pre-commit-setup.md with commit message examples
- [ ] T034 [US4] Add commit message format section to README.md with good/bad examples

**Checkpoint**: Commit message format is enforced and developers have interactive tool for creating proper commits

---

## Phase 5: User Story 1 - Fast Feedback on Feature Branches (Priority: P1) 🎯

**Goal**: Developers receive feedback on code quality within 5 minutes of pushing to feature branches

**Independent Test**: Push code with linting error to feature branch, verify CI runs and reports error within 5 minutes

**Why P1**: Fast feedback is critical for developer productivity and reducing wasted time on issues that will fail in CI

### Implementation for User Story 1

- [ ] T035 [US1] Create .github/workflows/ci-feature-branch.yml with initial structure
- [ ] T036 [US1] Configure workflow trigger for push to all branches except main
- [ ] T037 [US1] Configure matrix strategy with os: [ubuntu-latest, windows-latest, macos-latest]
- [ ] T038 [US1] Configure matrix with python-version: ['3.12'] and node-version: ['20.x']
- [ ] T039 [US1] Add checkout step with actions/checkout@v4
- [ ] T040 [US1] Add Python setup step with actions/setup-python@v5 using matrix.python-version
- [ ] T041 [US1] Add Node.js setup step with actions/setup-node@v4 using matrix.node-version
- [ ] T042 [US1] Add caching step with actions/cache@v4 for uv and npm dependencies
- [ ] T043 [US1] Add install dependencies step: `uv sync && cd frontend && npm install`
- [ ] T044 [US1] Add linting step: `uv run ruff check . && npm run lint`
- [ ] T045 [US1] Add type checking step: `uv run mypy src/ && npm run type-check`
- [ ] T046 [US1] Add test step: `uv run pytest` (basic tests, no coverage yet)
- [ ] T047 [US1] Test workflow by pushing to feature branch and verifying it runs
- [ ] T048 [US1] Optimize caching configuration for sub-5-minute execution
- [ ] T049 [US1] Add workflow status badge to README.md for feature branch CI

**Checkpoint**: Feature branch pushes trigger fast CI validation (3-5 minutes) with clear feedback

---

## Phase 6: User Story 2 - Protected Main Branch with Full Validation (Priority: P2)

**Goal**: Pull requests to main undergo comprehensive validation across all platforms, Python versions, and security scans before merge is allowed

**Independent Test**: Create PR to main with all checks passing, verify merge is allowed; create PR with failing test, verify merge is blocked

**Why P2**: Builds on P1's fast feedback by adding comprehensive validation only when merging to production

### Implementation for User Story 2

- [ ] T050 [US2] Create .github/workflows/ci-pr-main.yml with comprehensive matrix
- [ ] T051 [US2] Configure workflow trigger for pull_request targeting main branch
- [ ] T052 [US2] Configure matrix with 6 OS variants (ubuntu-latest, ubuntu-22.04, windows-latest, windows-2022, macos-latest, macos-14)
- [ ] T053 [US2] Configure matrix with python-version: ['3.12', '3.13'] and node-version: ['20.x']
- [ ] T054 [US2] Add checkout, Python setup, Node setup, and caching steps (same as Workflow A)
- [ ] T055 [US2] Add install dependencies step with uv sync and npm install
- [ ] T056 [US2] Add full linting job across all matrix combinations
- [ ] T057 [US2] Add full type checking job across all matrix combinations
- [ ] T058 [US2] Add comprehensive test job with coverage: `uv run pytest --cov=src --cov-report=xml --cov-report=term`
- [ ] T059 [US2] Add coverage threshold check: `uv run coverage report --fail-under=80`
- [ ] T060 [US2] Add Bandit security scan job: `uv run bandit -r src/ -f json`
- [ ] T061 [US2] Add Safety dependency scan job: `uv run safety check --json`
- [ ] T062 [P] [US2] Create scripts/safety-policy-check.py for risk-based vulnerability assessment
- [ ] T063 [US2] Add Safety policy enforcement in workflow (HIGH/CRITICAL blocks, MEDIUM/LOW warns)
- [ ] T064 [US2] Add npm audit step for frontend dependencies
- [ ] T065 [P] [US2] Add CodeQL analysis workflow in .github/workflows/codeql.yml
- [ ] T066 [US2] Configure CodeQL for Python and TypeScript/JavaScript analysis
- [ ] T067 [US2] Add Codecov upload step with codecov/codecov-action@v4
- [ ] T068 [US2] Configure branch protection rules for main via GitHub settings (or API)
- [ ] T069 [US2] Add required status checks: all 12 matrix test jobs + lint + security-scan + CodeQL
- [ ] T070 [US2] Configure branch protection to require 1 code review approval
- [ ] T071 [US2] Test comprehensive workflow by creating PR with intentional issues
- [ ] T072 [US2] Verify merge blocking works when status checks fail
- [ ] T073 [US2] Add coverage badge to README.md from Codecov

**Checkpoint**: Main branch is protected with comprehensive validation (12 jobs, ~10-15 minutes) before any merge

---

## Phase 7: Post-Merge Workflow (Optional Release Automation)

**Goal**: After successful merge to main, optionally tag releases and trigger deployment

**Independent Test**: Merge PR to main, verify Workflow C runs and creates appropriate tags/releases

### Implementation for Workflow C

- [ ] T074 [P] Create .github/workflows/ci-post-merge.yml (optional release workflow)
- [ ] T075 [P] Configure workflow trigger for push to main branch only
- [ ] T076 [P] Add semantic version tagging step using commitizen: `cz bump`
- [ ] T077 [P] Add GitHub Release creation step with release notes from CHANGELOG
- [ ] T078 [P] Configure workflow to skip if commit message is chore/docs only

**Checkpoint**: Post-merge automation handles versioning and releases automatically

---

## Phase 8: Polish & Documentation

**Purpose**: Final touches, documentation, and validation

- [ ] T079 [P] Create comprehensive docs/development/ci-setup.md with CI architecture overview
- [ ] T080 [P] Document workflow triggers and matrix configurations in ci-setup.md
- [ ] T081 [P] Add troubleshooting section to ci-setup.md for common CI failures
- [ ] T082 [P] Create workflow diagrams showing Workflow A → Workflow B → Workflow C flow
- [ ] T083 Update quickstart.md based on actual implementation (if needed)
- [ ] T084 Update README.md with complete CI/CD badges (build status, coverage, code quality)
- [ ] T085 Add performance optimization notes (cache keys, job concurrency) to ci-setup.md
- [ ] T086 Document CI minutes usage and cost estimates in ci-setup.md
- [ ] T087 [P] Add examples of parallel execution for different scenarios
- [ ] T088 Create PR checklist template in .github/pull_request_template.md
- [ ] T089 Test complete workflow end-to-end: feature branch → PR → merge → release
- [ ] T090 Validate all user stories work independently per spec.md acceptance criteria
- [ ] T091 Run through quickstart.md as new contributor to verify instructions

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
- [ ] Pre-commit hooks can be installed with `pre-commit install`
- [ ] Hooks auto-format code on commit
- [ ] Hooks block commits with type errors
- [ ] Hooks validate commit message format (with US4)
- [ ] All hooks run in under 10 seconds

### User Story 1 (Feature Branch CI)
- [ ] Workflow triggers on push to non-main branches
- [ ] Workflow completes in under 5 minutes
- [ ] Linting errors are clearly reported
- [ ] Type checking errors are clearly reported
- [ ] Test failures are clearly reported
- [ ] GitHub UI shows clear status

### User Story 2 (PR to Main CI)
- [ ] Workflow triggers only on PR to main
- [ ] All 12 matrix jobs run (6 OS × 2 Python)
- [ ] Coverage must be ≥ 80% or build fails
- [ ] Security scans detect vulnerabilities
- [ ] HIGH/CRITICAL vulnerabilities block merge
- [ ] MEDIUM/LOW dev dependencies warn only
- [ ] Merge is blocked if any required check fails
- [ ] Code review approval required

### User Story 4 (Commit Messages)
- [ ] Commitizen interactive commit works
- [ ] Improperly formatted messages are rejected
- [ ] Properly formatted messages are accepted
- [ ] Conventional Commits format enforced

### Overall System
- [ ] All workflows use caching effectively
- [ ] README has all CI badges
- [ ] Documentation is complete and accurate
- [ ] New contributors can follow quickstart.md successfully

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

