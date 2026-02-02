# ⚠️ Manual Setup Required

## Overview

The CI/CD implementation is complete, but **branch protection rules** must be configured manually in GitHub. This cannot be done via files alone.

## Required Action: Configure Branch Protection

### Why Manual Setup?

Branch protection rules are **GitHub repository settings** that require:

- Repository admin permissions
- Access to GitHub web UI or API
- Cannot be committed as files in the repository

### Step-by-Step Instructions

Follow the complete guide: **[branch-protection-setup.md](./branch-protection-setup.md)**

### Quick Setup (5 minutes)

1. **Navigate to Branch Protection Settings**:

   ```
   https://github.com/jeffrichley/iris/settings/branches
   ```

2. **Add/Edit Rule for `main` branch**

3. **Enable These Settings**:

   ✅ **Require pull request before merging**
   - Require 1 approval
   - Dismiss stale reviews when new commits pushed

   ✅ **Require status checks to pass**
   - Require branches to be up to date
   - Add all 15 required checks (see below)

   ✅ **Require conversation resolution**

   ❌ **Do NOT allow**:
   - Force pushes
   - Deletions
   - Bypassing (even for admins)

4. **Add Required Status Checks** (15 total):

   **After first PR runs**, add these checks:

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

   **Security (3 checks)**:
   - `security-scan`
   - `CodeQL Analysis (python)`
   - `CodeQL Analysis (javascript)`

5. **Save Changes**

### ⚠️ Important Notes

**Timing**: You must push this branch and create a PR FIRST before status checks appear in GitHub's dropdown. GitHub learns about available checks from actual workflow runs.

**Recommended Flow**:

1. ✅ Push this feature branch → Workflow A runs
2. ✅ Create PR to main → Workflow B + CodeQL run
3. ✅ Wait for all workflows to complete
4. ✅ THEN configure branch protection (checks will be visible)
5. ✅ Close/reopen the PR to trigger protection rules

---

## Verification

After setup, test that protection works:

```bash
# This should FAIL (direct push to main blocked):
git checkout main
git commit --allow-empty -m "test: verify protection"
git push
# Expected: "protected branch hook declined"

# This should WORK (via PR):
git checkout -b test/protection
git commit --allow-empty -m "test: verify protection"
git push -u origin test/protection
gh pr create --base main
# Expected: PR created, must wait for CI + approval before merge
```

---

## What Happens Without Branch Protection?

❌ **Without branch protection**:

- Developers can push directly to `main` (bypassing CI)
- Code can be merged without review
- Broken code can reach production
- Quality gates are recommendations, not enforcement

✅ **With branch protection**:

- All changes MUST go through PR process
- CI MUST pass before merge
- Code review MUST be approved
- Quality is enforced, not suggested

---

## Alternative: Automated Setup (Advanced)

### Using GitHub CLI

```bash
# Note: This is a complex command - see branch-protection-setup.md for full details
gh api repos/jeffrichley/iris/branches/main/protection \
  --method PUT \
  --field required_pull_request_reviews[required_approving_review_count]=1 \
  --field required_status_checks[strict]=true \
  # ... additional fields ...
```

### Using Terraform

See **[branch-protection-setup.md](./branch-protection-setup.md)** for complete Terraform example.

---

## Summary

**What's Automated**: ✅

- Pre-commit hooks
- GitHub Actions workflows
- Security scanning
- Coverage enforcement
- Documentation

**What's Manual**: ⚠️

- Branch protection rules (5 minutes, one-time setup)
- Initial secrets baseline scan (if you have existing code with secrets)

**Time Required**: ~5-10 minutes for first-time setup

**When to Do It**: After pushing this branch and creating your first PR (so GitHub knows about the status checks)

---

**See**: [branch-protection-setup.md](./branch-protection-setup.md) for complete instructions
