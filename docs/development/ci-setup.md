# CI/CD Setup and Architecture

## Overview

The Iris project uses a three-tiered GitHub Actions CI/CD pipeline that provides fast feedback during development and comprehensive validation before merging to production.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Developer Workflow                        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Local: Pre-commit Hooks (< 10 seconds)                     │
│  ✓ Ruff format/lint  ✓ Mypy  ✓ ESLint  ✓ Prettier          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Workflow A: Feature Branch (3-5 minutes)                    │
│  ✓ 3 OS platforms  ✓ Python 3.12  ✓ Quick validation        │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Workflow B: PR to Main (10-15 minutes)                      │
│  ✓ 6 OS × 2 Python = 12 jobs  ✓ Security  ✓ Coverage 80%    │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Workflow C: Post-Merge (1-2 minutes)                        │
│  ✓ Version bump  ✓ GitHub Release  ✓ Tags                   │
└─────────────────────────────────────────────────────────────┘
```

## Workflows

### Workflow A: Feature Branch Fast Feedback

**File**: `.github/workflows/ci-feature-branch.yml`

**Trigger**:
```yaml
on:
  push:
    branches-ignore:
      - main
```

**Matrix Configuration**:
```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    python-version: ['3.12']
    node-version: ['20.x']
  fail-fast: false
```

**Jobs**: 3 (one per OS family)

**Steps**:
1. Checkout code
2. Setup Python 3.12 + Node.js 20.x
3. Cache dependencies (uv, pip, npm)
4. Install dependencies
5. Run linting (ruff, eslint)
6. Run type checking (mypy, tsc)
7. Run basic tests (pytest)

**Expected Time**: 3-5 minutes with caching

**Purpose**: Catch common issues quickly without running expensive comprehensive validation

---

### Workflow B: PR to Main Comprehensive Validation

**File**: `.github/workflows/ci-pr-main.yml`

**Trigger**:
```yaml
on:
  pull_request:
    branches:
      - main
```

**Matrix Configuration**:
```yaml
strategy:
  matrix:
    os: 
      - ubuntu-latest    # ubuntu-24.04
      - ubuntu-22.04
      - windows-latest   # windows-2025
      - windows-2022
      - macos-latest     # macos-15 (Apple Silicon)
      - macos-14         # Apple Silicon
    python-version: ['3.12', '3.13']
    node-version: ['20.x']
  fail-fast: false
```

**Jobs**: 12 matrix test jobs + 1 security scan job = 13 jobs total

**Matrix Test Job Steps**:
1. Checkout code
2. Setup Python (3.12 or 3.13) + Node.js 20.x
3. Cache dependencies
4. Install dependencies
5. Run full linting
6. Run full type checking
7. Run tests with coverage
8. Enforce 80% coverage threshold
9. Upload coverage to Codecov (ubuntu-latest + Python 3.12 only)

**Security Scan Job Steps**:
1. Bandit security scan (Python code)
2. Safety dependency scan (Python packages)
3. Risk-based policy enforcement (scripts/safety-policy-check.py)
4. npm audit (frontend dependencies)
5. Upload security reports

**Expected Time**: 10-15 minutes (jobs run in parallel)

**Purpose**: Production-ready validation across all supported platforms and versions

---

### Workflow C: Post-Merge Release Automation

**File**: `.github/workflows/ci-post-merge.yml`

**Trigger**:
```yaml
on:
  push:
    branches:
      - main
```

**Conditions**: Skips if commit message starts with `chore:` or `docs:`

**Steps**:
1. Checkout with full history
2. Setup Python 3.12
3. Install commitizen
4. Bump version automatically:
   - `feat:` → MINOR version bump
   - `fix:` / `perf:` → PATCH version bump
5. Update pyproject.toml version
6. Create git tag
7. Push version changes and tags
8. Create GitHub Release with changelog

**Expected Time**: 1-2 minutes

**Purpose**: Automated semantic versioning and release creation

---

### CodeQL Security Analysis

**File**: `.github/workflows/codeql.yml`

**Triggers**:
- Pull requests to main
- Weekly schedule (Mondays at 00:00 UTC)
- Manual workflow dispatch

**Languages**: Python, JavaScript/TypeScript

**Queries**: `security-extended`, `security-and-quality`

**Purpose**: Continuous security monitoring and vulnerability detection

---

## Matrix Build Strategy

### Why Latest + Previous?

- **Latest**: Ensures compatibility with newest OS features
- **Previous**: Ensures compatibility with users not yet upgraded
- **Coverage**: Balances thoroughness with CI cost/time

### Platform Details

| OS Label | Actual Version | Architecture | Why Included |
|----------|----------------|--------------|--------------|
| ubuntu-latest | Ubuntu 24.04 | x86_64 | Current LTS |
| ubuntu-22.04 | Ubuntu 22.04 | x86_64 | Previous LTS, most Linux users |
| windows-latest | Windows Server 2025 | x86_64 | Newest Windows |
| windows-2022 | Windows Server 2022 | x86_64 | Most Windows users |
| macos-latest | macOS 15 Sequoia | ARM64 (Apple Silicon) | Future of Mac |
| macos-14 | macOS 14 Sonoma | ARM64 (Apple Silicon) | Current Mac users |

**Architecture Coverage**:
- x86_64: Ubuntu, Windows
- ARM64: macOS (Apple Silicon is the future, Intel becoming legacy)

**Python Versions**:
- 3.12: Current stable, production-ready
- 3.13: Latest release, early adopters

**Node.js Version**:
- 20.x LTS: Active LTS, stable for production

---

## Caching Strategy

### Cache Paths

**Linux/macOS**:
```yaml
- ~/.cache/uv
- ~/.cache/pip
- ~/Library/Caches/uv  # macOS specific
```

**Windows**:
```yaml
- ~/AppData/Local/uv/cache
```

**Frontend**:
```yaml
- frontend/node_modules
```

### Cache Keys

Primary key:
```
${{ runner.os }}-deps-py${{ matrix.python-version }}-node${{ matrix.node-version }}-${{ hashFiles('**/pyproject.toml', '**/package-lock.json') }}
```

Fallback keys:
```
${{ runner.os }}-deps-py${{ matrix.python-version }}-node${{ matrix.node-version }}-
${{ runner.os }}-deps-
```

### Cache Performance

| Scenario | First Run | Cached Run | Improvement |
|----------|-----------|------------|-------------|
| Feature Branch | 8-10 min | 3-5 min | ~50% faster |
| PR to Main | 12-18 min | 10-15 min | ~30% faster |

**Cache Invalidation**: Automatic when `pyproject.toml` or `package-lock.json` changes

---

## Security Policy

### Risk-Based Vulnerability Assessment

Implemented in `scripts/safety-policy-check.py`:

| Dependency Type | Severity | Action |
|-----------------|----------|--------|
| Production | CRITICAL/HIGH | ❌ Block merge |
| Production | MEDIUM/LOW | ⚠️ Warn |
| Development | CRITICAL/HIGH | ❌ Block merge |
| Development | MEDIUM/LOW | ⚠️ Warn (can address later) |

### Security Tools

1. **Bandit**: Static code analysis for Python security issues
   - SQL injection, hardcoded secrets, insecure functions
   - Severity threshold: MEDIUM

2. **Safety**: Dependency vulnerability scanning
   - Checks against CVE database
   - Risk-based policy enforcement
   - JSON reports for tracking

3. **CodeQL**: Semantic code analysis
   - Python and JavaScript/TypeScript
   - Security-extended queries
   - GitHub Security tab integration

4. **npm audit**: Frontend dependency vulnerabilities
   - Audit level: moderate
   - Checks Node.js packages

---

## Branch Protection

### Required Checks (15 total)

**Matrix Tests (12 checks)**:
- `comprehensive-validation (ubuntu-latest, 3.12)`
- `comprehensive-validation (ubuntu-latest, 3.13)`
- `comprehensive-validation (ubuntu-22.04, 3.12)`
- `comprehensive-validation (ubuntu-22.04, 3.13)`
- `comprehensive-validation (windows-latest, 3.12)`
- `comprehensive-validation (windows-latest, 3.13)`
- `comprehensive-validation (windows-2022, 3.12)`
- `comprehensive-validation (windows-2022, 3.13)`
- `comprehensive-validation (macos-latest, 3.12)`
- `comprehensive-validation (macos-latest, 3.13)`
- `comprehensive-validation (macos-14, 3.12)`
- `comprehensive-validation (macos-14, 3.13)`

**Security & Quality (3 checks)**:
- `security-scan`
- `CodeQL Analysis (python)`
- `CodeQL Analysis (javascript)`

**Additional Requirements**:
- 1 code review approval
- All conversations resolved
- Branch up to date with main

**Setup**: See [branch-protection-setup.md](./branch-protection-setup.md)

---

## Troubleshooting

### Workflow A Failures

**Linting errors**:
```bash
# Fix locally
just lint
# Or auto-fix
just format
# Commit and push
```

**Type errors**:
```bash
# See errors
just type-check
# Fix code manually (no auto-fix for types)
# Commit and push
```

**Test failures**:
```bash
# Run tests locally
just test
# Fix failing tests
# Commit and push
```

### Workflow B Failures

**Platform-specific test failure**:
- Check which OS/Python combination failed
- Likely causes: Path separators, line endings, locale
- Test locally on that platform or use Docker
- Fix and push

**Coverage below 80%**:
```bash
# Generate HTML coverage report
just test
open htmlcov/index.html  # macOS
start htmlcov/index.html  # Windows
# Add tests for uncovered lines
```

**Security scan blocking**:
- Review bandit-report.json or safety-report.json in artifacts
- Fix code issues (Bandit) or update dependencies (Safety)
- HIGH/CRITICAL must be fixed before merge

### Workflow C Issues

**Version bump failed**:
- Check commit message follows Conventional Commits
- Verify pyproject.toml has correct version field
- Check git tags for conflicts

**Release creation failed**:
- Verify GITHUB_TOKEN has permissions
- Check if tag already exists
- Review workflow logs for details

---

## Performance Optimization

### Current Performance

**Workflow A** (Feature Branch):
- Without cache: ~8-10 minutes
- With cache: ~3-5 minutes
- **Improvement needed if**: Exceeds 5 minutes regularly

**Workflow B** (PR to Main):
- Without cache: ~15-20 minutes
- With cache: ~10-15 minutes
- **Improvement needed if**: Exceeds 15 minutes regularly

### Optimization Techniques

1. **Improve Cache Hit Rate**:
   - Lock file consistency (pyproject.toml, package-lock.json)
   - Avoid unnecessary dependency changes
   - Use deterministic package resolution

2. **Reduce Test Time**:
   - Parallelize tests within pytest
   - Use markers to run subsets: `pytest -m unit`
   - Optimize slow tests

3. **Optimize Dependencies**:
   - Remove unused dev dependencies
   - Use optional dependency groups
   - Pin versions for reproducibility

4. **Matrix Optimization**:
   - Consider reducing to 4 OS (drop one Ubuntu or Windows version)
   - Only test Python 3.13 on latest OS
   - Balance coverage vs cost

### Monitoring

Track workflow performance:
```bash
# Get workflow run times
gh run list --workflow=ci-feature-branch.yml --limit=10

# View specific run
gh run view <run-id> --log
```

---

## CI Minutes Budget

### Free Tier (Public Repos)

- **Included**: 2,000 minutes/month
- **macOS Multiplier**: 10x (1 min macOS = 10 counted minutes)
- **Windows Multiplier**: 2x
- **Linux Multiplier**: 1x

### Current Usage Estimates

**Per Feature Push** (Workflow A):
- 3 jobs × 5 minutes = 15 minutes
- 1 Linux + 1 Windows + 1 macOS = ~15 counted minutes

**Per PR to Main** (Workflow B):
- 12 matrix jobs × 12 minutes = 144 wall-clock minutes
- Breakdown:
  - 4 Ubuntu jobs × 12 min × 1x = 48 minutes
  - 4 Windows jobs × 12 min × 2x = 96 minutes
  - 4 macOS jobs × 12 min × 10x = 480 minutes
- **Total**: ~624 counted minutes per PR

**Monthly Estimate** (Active Development):
- 10 feature pushes: ~150 minutes
- 2 PRs to main: ~1,248 minutes
- **Total**: ~1,400 minutes/month
- **Remaining**: ~600 minutes for experiments/retries

**Recommendation**: Current usage is sustainable for single-developer project

---

## Workflow Triggers Reference

| Event | Workflows Triggered | Purpose |
|-------|---------------------|---------|
| Push to feature branch | Workflow A | Fast feedback |
| Create PR to main | Workflow B + CodeQL | Comprehensive validation |
| Push to main (after merge) | Workflow C | Release automation |
| Weekly (Monday 00:00 UTC) | CodeQL | Scheduled security scan |
| Manual trigger | CodeQL | On-demand security analysis |

---

## Quality Gates Summary

### Before Commit (Local)

- ✅ Code auto-formatted (ruff, prettier)
- ✅ Types checked (mypy, tsc)
- ✅ Linting passed (ruff, eslint)
- ✅ Commit message validated (commitizen)

### Before PR Review (Cloud)

- ✅ Tests pass on 3 platforms
- ✅ Linting clean on all platforms
- ✅ Type checking clean

### Before Merge to Main (Comprehensive)

- ✅ Tests pass on 12 platform/version combinations
- ✅ Coverage ≥ 80%
- ✅ Zero linting errors
- ✅ Zero type errors
- ✅ No HIGH/CRITICAL vulnerabilities
- ✅ Security scans passed (Bandit, Safety, CodeQL)
- ✅ Code review approved
- ✅ All conversations resolved

---

## Common Scenarios

### Scenario 1: Starting New Feature

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make changes
# ... edit code ...

# Pre-commit hooks run automatically on commit
git add .
git commit  # or: just commit

# Push triggers Workflow A
git push -u origin feature/my-feature

# Wait 3-5 minutes for CI feedback
# Green check = ready for PR
# Red X = fix issues and push again
```

### Scenario 2: Creating PR

```bash
# Create PR from feature branch
gh pr create --base main --title "feat: my feature" --body "Description"

# Workflow B triggers automatically
# 12 matrix jobs + security scan = 13 jobs
# Wait 10-15 minutes

# If any job fails:
# - Check logs in GitHub Actions tab
# - Fix locally
# - Push to same branch
# - CI re-runs automatically
```

### Scenario 3: Merging to Main

```bash
# After all checks pass and review approved:
gh pr merge --squash

# Workflow C triggers on main
# Version bumped automatically
# GitHub Release created
# Ready for deployment
```

---

## Adding New Checks

To add a new required check to the pipeline:

1. **Add to Workflow**: Update `.github/workflows/ci-pr-main.yml`
   ```yaml
   - name: My New Check
     run: |
       uv run my-tool check
   ```

2. **Update Branch Protection**: Add check name to required status checks
   - Go to GitHub repository settings
   - Edit main branch protection rule
   - Add `comprehensive-validation` (for matrix) or new job name

3. **Document**: Update this file with new check details

4. **Test**: Create test PR to verify check runs and can block merge

---

## References

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Matrix Strategy](https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs)
- [Branch Protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches)
- [CodeQL](https://codeql.github.com/)
- [Codecov](https://docs.codecov.com/)

---

**Last Updated**: October 20, 2025  
**Maintained By**: Iris Development Team

