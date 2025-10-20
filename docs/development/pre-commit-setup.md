# Pre-commit Hooks Setup Guide

## Overview

Pre-commit hooks provide immediate feedback on code quality before commits reach version control. This saves time by catching issues early and reduces CI failures.

## Quick Setup

### 1. Install Pre-commit Framework

```bash
# Using pip (included in dev dependencies)
uv sync --dev

# Or install separately
pip install pre-commit
```

### 2. Install Hooks

```bash
# Using just (recommended)
just setup-hooks

# Or manually
pre-commit install
pre-commit install --hook-type commit-msg
```

### 3. Verify Installation

```bash
# Run hooks on all files
pre-commit run --all-files
```

## What Gets Checked

### Python Code

**Ruff (Linter & Formatter)**:
- Automatically fixes import sorting
- Enforces code style (100 char line length)
- Catches common errors (unused imports, undefined variables)
- Auto-formats code to match project standards

**Mypy (Type Checker)**:
- Enforces strict type checking
- Catches type errors before runtime
- Ensures type hints are present and correct

### TypeScript/React Code

**ESLint**:
- Enforces TypeScript best practices
- Validates React hooks usage
- Checks accessibility (a11y) compliance
- Auto-fixes many issues

**Prettier**:
- Consistent code formatting
- Handles JS, TS, JSON, CSS, Markdown
- Auto-formats on commit

### Secret Detection

**detect-secrets**:
- Scans for API keys, tokens, passwords, and credentials
- Prevents accidental commit of sensitive data
- Uses baseline file (.secrets.baseline) for false positive management
- Detects: AWS keys, GitHub tokens, API keys, private keys, JWT tokens, and more

**What it catches**:
- API keys and tokens (AWS, Azure, GitHub, Slack, Stripe, etc.)
- Private SSH/PGP keys
- Basic auth credentials
- High-entropy strings (potential secrets)
- JWT tokens
- Database connection strings

### Commit Messages

**Commitizen (Conventional Commits)**:
- Enforces commit message format: `type(scope): description`
- Blocks improperly formatted messages
- Interactive mode guides you through creating proper commits

**Valid commit types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style (formatting, no logic change)
- `refactor`: Code restructuring (no behavior change)
- `perf`: Performance improvement
- `test`: Adding/updating tests
- `chore`: Build process, dependencies
- `ci`: CI configuration changes
- `build`: Build system changes
- `revert`: Revert previous commit

**Examples**:
```bash
# Good commit messages
feat(auth): add OAuth2 support
fix(sync): resolve conflict resolution edge case
docs(api): update authentication guide
test(tasks): add edge case coverage
chore(deps): update ruff to 0.2.0

# Bad commit messages (will be rejected)
"Added stuff"
"Fixed bug"
"WIP"
```

### General Checks

- **Secret detection**: Comprehensive scan for API keys, tokens, credentials (detect-secrets + detect-private-key)
- Removes trailing whitespace
- Ensures files end with newline
- Validates YAML, JSON, TOML syntax
- Prevents committing large files (>1MB)
- Detects merge conflicts
- Checks for TODO/FIXME comments (optional)

## How It Works

### On Every Commit

1. You run `git commit`
2. Pre-commit hooks run automatically
3. If issues found:
   - **Auto-fixable**: Code is fixed, re-stage and commit again
   - **Manual fix needed**: Commit is blocked with error message
4. If all checks pass: Commit proceeds

### Example Workflow

```bash
# Make changes
echo "def hello( ):\n    print('world')" > src/hello.py

# Attempt commit
git add src/hello.py
git commit -m "feat: add hello function"

# Hooks run automatically:
# ✓ ruff: Fixed import sorting
# ✓ ruff-format: Formatted code
# ✗ mypy: Missing type hints
# Commit blocked!

# Fix the issue
echo "def hello() -> None:\n    print('world')" > src/hello.py

# Re-stage and commit
git add src/hello.py
git commit -m "feat: add hello function"
# ✓ All hooks passed - commit successful!
```

### Interactive Commit (Recommended)

Use `just commit` or `cz commit` for guided commit message creation:

```bash
# Stage your changes
git add .

# Use interactive commit
just commit

# You'll be prompted:
? Select the type of change you are committing: 
  ❯ feat: A new feature
    fix: A bug fix
    docs: Documentation only changes
    ...

? What is the scope of this change? (press enter to skip): auth

? Write a short, imperative description of the change: add OAuth2 support

? Provide additional contextual information (press enter to skip): 

? Are there any breaking changes? (Y/n): n

# Result: "feat(auth): add OAuth2 support"
# Commit created automatically!
```

## Bypassing Hooks (Not Recommended)

If you absolutely must bypass hooks (rarely needed):

```bash
git commit --no-verify -m "message"
```

**Warning**: This skips all quality checks. CI will still catch issues.

## Troubleshooting

### Hook Takes Too Long

**Problem**: Pre-commit runs on many files

**Solution**: Only commit specific files
```bash
git add specific_file.py
git commit
```

### Hook Fails with Mysterious Error

**Problem**: Pre-commit cache corruption

**Solution**: Clean and reinstall
```bash
pre-commit clean
pre-commit install --install-hooks
pre-commit run --all-files
```

### Mypy Complains About Missing Imports

**Problem**: Pre-commit runs in isolated environment

**Solution**: Already handled - we use `--ignore-missing-imports`

### ESLint/Prettier Not Running

**Problem**: Frontend not yet set up

**Solution**: Hooks gracefully skip if frontend directory doesn't exist

## Configuration Files

- `.pre-commit-config.yaml` - Hook definitions
- `pyproject.toml` - Python tool configurations (ruff, mypy, pytest)
- `.eslintrc.json` - ESLint rules
- `.prettierrc.json` - Prettier formatting options
- `tsconfig.json` - TypeScript compiler settings

## Updating Hooks

Hooks are version-pinned for reproducibility. To update:

```bash
# Update to latest versions
pre-commit autoupdate

# Test updated hooks
pre-commit run --all-files

# Commit the updated config
git add .pre-commit-config.yaml
git commit -m "chore: update pre-commit hooks"
```

## Best Practices

### Do

✅ Install hooks on every new clone  
✅ Run `pre-commit run --all-files` after updating hooks  
✅ Commit frequently with small changesets  
✅ Fix issues highlighted by hooks  
✅ Keep hooks updated quarterly

### Don't

❌ Bypass hooks without good reason  
❌ Commit large changesets (hooks run on all changed files)  
❌ Ignore type errors (they'll fail in CI anyway)  
❌ Disable specific hooks without team discussion

## Integration with CI

Pre-commit hooks run **locally**. CI runs the same checks **in the cloud**:

| Check | Local (Pre-commit) | CI (GitHub Actions) |
|-------|-------------------|---------------------|
| Ruff lint/format | ✅ Auto-fix | ✅ Verify (fail if unfixed) |
| Mypy type check | ✅ Block commit | ✅ Fail build |
| ESLint | ✅ Auto-fix | ✅ Verify |
| Prettier | ✅ Auto-format | ✅ Verify |
| Tests | ❌ Not in pre-commit | ✅ Full suite + coverage |
| Security scans | ❌ Not in pre-commit | ✅ Bandit, Safety, CodeQL |

**Philosophy**: Hooks catch **quick** issues locally. CI runs **comprehensive** validation.

## Getting Help

- **Pre-commit issues**: https://pre-commit.com/
- **Tool-specific docs**: See configuration file comments
- **Project issues**: Create GitHub issue with error output

---

**Last Updated**: October 20, 2025  
**Maintained By**: Iris Development Team

