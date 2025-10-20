# Branch Protection Configuration Guide

## Overview

This document provides instructions for configuring branch protection rules on the `main` branch to enforce quality gates and ensure production-ready code.

## Required Settings

### Access Branch Protection

1. Go to: `https://github.com/jeffrichley/iris/settings/branches`
2. Click "Add rule" or edit existing "main" branch rule

### Configuration

```yaml
Branch name pattern: main

☑ Require a pull request before merging
  ☑ Require approvals: 1
  ☑ Dismiss stale pull request approvals when new commits are pushed
  ☐ Require review from Code Owners (not applicable - single developer)
  ☑ Require approval of the most recent reviewable push

☑ Require status checks to pass before merging
  ☑ Require branches to be up to date before merging
  
  Required status checks (15 total):
    # Matrix Test Jobs (12 checks - 6 OS × 2 Python)
    ✓ comprehensive-validation (ubuntu-latest, 3.12)
    ✓ comprehensive-validation (ubuntu-latest, 3.13)
    ✓ comprehensive-validation (ubuntu-22.04, 3.12)
    ✓ comprehensive-validation (ubuntu-22.04, 3.13)
    ✓ comprehensive-validation (windows-latest, 3.12)
    ✓ comprehensive-validation (windows-latest, 3.13)
    ✓ comprehensive-validation (windows-2022, 3.12)
    ✓ comprehensive-validation (windows-2022, 3.13)
    ✓ comprehensive-validation (macos-latest, 3.12)
    ✓ comprehensive-validation (macos-latest, 3.13)
    ✓ comprehensive-validation (macos-14, 3.12)
    ✓ comprehensive-validation (macos-14, 3.13)
    
    # Security and Quality (3 checks)
    ✓ security-scan
    ✓ CodeQL Analysis (python)
    ✓ CodeQL Analysis (javascript)

☑ Require conversation resolution before merging

☐ Require signed commits (optional)

☑ Require linear history (optional - can use squash merge)

☐ Include administrators (recommended: enforce rules for everyone)

☑ Restrict who can dismiss pull request reviews (if team grows)

☐ Allow force pushes: Never

☐ Allow deletions: Never
```

## Applying Configuration

### Option 1: Manual Configuration (Immediate)

1. Navigate to repository settings → Branches
2. Add/edit branch protection rule for `main`
3. Enable all checkboxes above
4. Add all 15 required status checks
5. Save changes

### Option 2: GitHub CLI (Scripted)

```bash
# Create branch protection rule
gh api repos/jeffrichley/iris/branches/main/protection \
  --method PUT \
  --input branch-protection-config.json
```

### Option 3: Terraform (Infrastructure as Code)

```hcl
resource "github_branch_protection" "main" {
  repository_id = "iris"
  pattern       = "main"
  
  required_status_checks {
    strict = true
    contexts = [
      "comprehensive-validation (ubuntu-latest, 3.12)",
      "comprehensive-validation (ubuntu-latest, 3.13)",
      # ... all 15 checks
    ]
  }
  
  required_pull_request_reviews {
    required_approving_review_count = 1
    dismiss_stale_reviews           = true
  }
  
  enforce_admins = true
}
```

## Verification

After applying configuration:

1. **Test Protection**: Try pushing directly to `main`
   ```bash
   git checkout main
   git commit --allow-empty -m "test: verify protection"
   git push
   # Should be rejected
   ```

2. **Test PR Flow**: Create test PR
   ```bash
   git checkout -b test/branch-protection
   git commit --allow-empty -m "test: verify PR flow"
   git push -u origin test/branch-protection
   # Create PR via GitHub UI
   # Verify merge is blocked until all 15 checks pass
   ```

3. **Verify Status Checks**: 
   - Open PR
   - Check that all 15 required checks appear
   - Verify merge button is disabled until checks pass

## Status Check Names Reference

| Check Name | Workflow | Job | Matrix |
|------------|----------|-----|--------|
| `comprehensive-validation (ubuntu-latest, 3.12)` | ci-pr-main.yml | comprehensive-validation | ubuntu-latest, Python 3.12 |
| `comprehensive-validation (ubuntu-latest, 3.13)` | ci-pr-main.yml | comprehensive-validation | ubuntu-latest, Python 3.13 |
| `comprehensive-validation (ubuntu-22.04, 3.12)` | ci-pr-main.yml | comprehensive-validation | ubuntu-22.04, Python 3.12 |
| `comprehensive-validation (ubuntu-22.04, 3.13)` | ci-pr-main.yml | comprehensive-validation | ubuntu-22.04, Python 3.13 |
| `comprehensive-validation (windows-latest, 3.12)` | ci-pr-main.yml | comprehensive-validation | windows-latest, Python 3.12 |
| `comprehensive-validation (windows-latest, 3.13)` | ci-pr-main.yml | comprehensive-validation | windows-latest, Python 3.13 |
| `comprehensive-validation (windows-2022, 3.12)` | ci-pr-main.yml | comprehensive-validation | windows-2022, Python 3.12 |
| `comprehensive-validation (windows-2022, 3.13)` | ci-pr-main.yml | comprehensive-validation | windows-2022, Python 3.13 |
| `comprehensive-validation (macos-latest, 3.12)` | ci-pr-main.yml | comprehensive-validation | macos-latest, Python 3.12 |
| `comprehensive-validation (macos-latest, 3.13)` | ci-pr-main.yml | comprehensive-validation | macos-latest, Python 3.13 |
| `comprehensive-validation (macos-14, 3.12)` | ci-pr-main.yml | comprehensive-validation | macos-14, Python 3.12 |
| `comprehensive-validation (macos-14, 3.13)` | ci-pr-main.yml | comprehensive-validation | macos-14, Python 3.13 |
| `security-scan` | ci-pr-main.yml | security-scan | single job |
| `CodeQL Analysis (python)` | codeql.yml | analyze | Python |
| `CodeQL Analysis (javascript)` | codeql.yml | analyze | JavaScript |

## Important Notes

- **Wait for first PR**: GitHub only shows status checks after they've run at least once
- **Update as needed**: If you add/remove matrix combinations, update required checks
- **Admin bypass**: Consider enabling "Include administrators" to ensure even repo owners follow rules
- **Required reviews**: Single developer project uses 1 approval; increase for teams

## Troubleshooting

**Problem**: Status checks not appearing

**Solution**: 
- Push a commit to trigger workflows first
- GitHub learns available checks from workflow runs
- Then configure branch protection

**Problem**: Too many required checks

**Solution**:
- This is intentional - ensures comprehensive validation
- All 12 matrix jobs must pass
- All 3 security checks must pass

**Problem**: Can't merge even with passing checks

**Solution**:
- Verify all 15 checks are green
- Verify code review approval received
- Check for conversation threads requiring resolution

---

**Last Updated**: October 20, 2025  
**Maintained By**: Iris Development Team

