# Parallel Execution Guide

## Overview

This guide demonstrates how different CI tasks and development workflows can run in parallel to maximize efficiency.

## Parallel Opportunities in CI

### Workflow A (Feature Branch)

**3 jobs run in parallel**:

```
Time: 0 min                                      5 min
|─────────────────────────────────────────────────|
│                                                 │
├─ [ubuntu-latest, Python 3.12] ─────────────────┤
│                                                 │
├─ [windows-latest, Python 3.12] ────────────────┤
│                                                 │
└─ [macos-latest, Python 3.12] ──────────────────┘

Wall-clock time: ~5 minutes (all jobs run simultaneously)
Total CI minutes consumed: ~15 minutes
```

### Workflow B (PR to Main)

**13 jobs run in parallel**:

```
Matrix Jobs (12 jobs in parallel):
├─ ubuntu-latest × Python 3.12
├─ ubuntu-latest × Python 3.13
├─ ubuntu-22.04 × Python 3.12
├─ ubuntu-22.04 × Python 3.13
├─ windows-latest × Python 3.12
├─ windows-latest × Python 3.13
├─ windows-2022 × Python 3.12
├─ windows-2022 × Python 3.13
├─ macos-latest × Python 3.12
├─ macos-latest × Python 3.13
├─ macos-14 × Python 3.12
└─ macos-14 × Python 3.13

Security Job (runs in parallel with matrix):
└─ security-scan (Ubuntu, Python 3.12)

CodeQL Jobs (runs in parallel):
├─ CodeQL: Python
└─ CodeQL: JavaScript

Wall-clock time: ~12-15 minutes (limited by slowest job)
Total CI minutes consumed: ~624 minutes (macOS 10x multiplier)
```

## Parallel Development Tasks

### Phase 2: Foundational (Tool Configuration)

**Can run in parallel** (different files):

```bash
# Developer A:
Task T006: pyproject.toml (ruff linting)
Task T007: pyproject.toml (ruff formatting)
Task T008: pyproject.toml (mypy)
Task T009: pyproject.toml (pytest)
Task T010: pyproject.toml (coverage)

# Developer B:
Task T011: .eslintrc.json
Task T012: .prettierrc.json
Task T013: tsconfig.json

# Merge after both complete
```

**Cannot run in parallel** (same file):
- T006-T010 all edit pyproject.toml → must be sequential OR coordinated merge
- T014-T018 all edit justfile → must be sequential

### Phase 3: User Story 3 (Pre-commit Hooks)

**Can run in parallel**:

```bash
# Developer A:
Task T019: .pre-commit-config.yaml (ruff hooks)
Task T020: .pre-commit-config.yaml (mypy hook)

# Developer B:
Task T021: .pre-commit-config.yaml (eslint hook)
Task T022: .pre-commit-config.yaml (prettier hook)

# Developer C:
Task T025: docs/development/pre-commit-setup.md

# Note: T019-T022 edit same file, need merge or coordination
```

### Phase 4: User Story 4 (Commit Messages)

**Can run in parallel**:

```bash
# Developer A:
Task T027-T029: pyproject.toml (commitizen config)

# Developer B:
Task T033: docs/development/pre-commit-setup.md (commit examples)

# Developer C:
Task T034: README.md (commit format section)
```

### Phase 6: User Story 2 (PR to Main CI)

**Can run in parallel**:

```bash
# Team A: Workflow file
Task T050-T067: .github/workflows/ci-pr-main.yml

# Team B: Security script
Task T062: scripts/safety-policy-check.py

# Team C: CodeQL
Task T065-T066: .github/workflows/codeql.yml

# Team D: Documentation
Task T068-T072: docs/development/branch-protection-setup.md
```

### Phase 8: Polish (Documentation)

**All parallel** (different files):

```bash
Developer A: T079-T081 (ci-setup.md)
Developer B: T082 (workflow diagrams)
Developer C: T087 (parallel examples - this file)
Developer D: T089 (PR checklist)
```

## Local Development Parallelization

### Running Multiple Quality Checks

**Sequential** (traditional):
```bash
just lint       # 30 seconds
just type-check # 45 seconds
just test       # 2 minutes
# Total: ~3 minutes
```

**Parallel** (faster):
```bash
# Run all in background
just lint & just type-check & just test &
wait
# Total: ~2 minutes (time of slowest task)
```

**Using just ci** (automated):
```bash
just ci  # Runs sequentially but optimized
```

### Pre-commit Hooks (Automatic Parallelization)

Pre-commit framework automatically parallelizes hooks when possible:

```
pre-commit run --all-files

Parallel execution:
├─ ruff (on Python files) ───────┐
├─ mypy (on Python files) ───────┼─→ Completes in ~5-8 sec
├─ eslint (on TS files) ─────────┤
└─ prettier (on all files) ──────┘

# Instead of: 4 × 3 sec = 12 sec sequential
# Actual: ~5-8 sec parallel
```

## Team Collaboration Strategies

### Strategy 1: Feature-Based Parallelism

After Foundational phase completes:

```
Developer A → User Story 1 (Feature Branch CI)
Developer B → User Story 3 (Pre-commit Hooks)
Developer C → User Story 4 (Commit Messages)

All three can work simultaneously!
```

### Strategy 2: Layer-Based Parallelism

Within a single user story:

```
Phase start:
├─ Dev A: Configuration files
├─ Dev B: Workflow files
└─ Dev C: Documentation

Phase integrate:
└─ All: Test and verify together
```

### Strategy 3: Component-Based Parallelism

For Workflow B (largest phase):

```
Team 1: Core workflow (T050-T059)
Team 2: Security (T060-T064)
Team 3: CodeQL (T065-T066)
Team 4: Coverage (T067)
Team 5: Documentation (T068-T073)

Integration: All teams merge at end
```

## GitHub Actions Concurrency

### Default Behavior

GitHub Actions runs jobs in parallel up to concurrency limits:

- **Public repos**: ~20 concurrent jobs
- **Private repos (free)**: ~5 concurrent jobs
- **Private repos (paid)**: Configurable

### Our Workflows

**Workflow A**: 3 jobs → All run in parallel simultaneously  
**Workflow B**: 13 jobs → All run in parallel (within limits)  
**CodeQL**: 2 jobs (Python, JS) → Run in parallel

**Optimization**: No need for manual job orchestration; GitHub handles it automatically

## Bottlenecks and Solutions

### Bottleneck 1: Same File Edits

**Problem**: Multiple tasks edit pyproject.toml (T006-T010)

**Solutions**:
- **Sequential**: Complete T006-T010 in order
- **Coordinated**: Use git branches, merge carefully
- **Single session**: One developer does all pyproject.toml edits

### Bottleneck 2: macOS Job Cost

**Problem**: macOS jobs count as 10× CI minutes

**Solutions**:
- **Accepted**: macOS testing is valuable for cross-platform app
- **Future optimization**: Drop macos-14 if budget tight (keep latest only)
- **Cost-benefit**: 4 macOS jobs × 10× = worth it for reliability

### Bottleneck 3: Foundational Phase (Critical Path)

**Problem**: Phase 2 (T006-T018) blocks ALL user stories

**Solutions**:
- **Prioritize**: Complete Phase 2 first (2 hours)
- **Team effort**: All developers help with foundational tasks
- **Cannot avoid**: Foundation must be solid before building user stories

## Best Practices

### DO

✅ Run lint, format, type-check in parallel during development  
✅ Let GitHub Actions handle job parallelization automatically  
✅ Use pre-commit hooks (they parallelize automatically)  
✅ Assign different user stories to different developers  
✅ Create configuration files in parallel if different files

### DON'T

❌ Edit same file from multiple branches without coordination  
❌ Skip pre-commit hooks to "save time" (creates more work later)  
❌ Try to manually control GitHub Actions job order  
❌ Start user story work before Foundational phase completes

## Monitoring Parallel Execution

### GitHub Actions UI

View job parallelization:
1. Go to Actions tab
2. Click on workflow run
3. See all jobs running simultaneously
4. Monitor progress in real-time

### Local Commands

```bash
# See all pre-commit hooks
pre-commit run --all-files --verbose

# See which hooks run in parallel
# (pre-commit framework handles this automatically)
```

---

**Last Updated**: October 20, 2025  
**Maintained By**: Iris Development Team

