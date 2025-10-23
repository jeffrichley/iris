# API Contracts: CI & Pre-commit Strategy

**Feature**: 001-ci-precommit-setup
**Date**: October 20, 2025
**Status**: N/A

## Summary

This feature implements CI/CD infrastructure and pre-commit hooks, which **do not expose APIs or services** that require contract definitions.

## Why No API Contracts?

API contracts are defined for features that:

- Expose REST/GraphQL endpoints
- Provide programmatic interfaces
- Define request/response schemas
- Enable inter-service communication

**This feature provides:**

- GitHub Actions workflows (CI automation)
- Pre-commit Git hooks (local validation)
- Configuration files (tool setup)
- Task runner commands (developer utilities)

None of these require API contract specifications (OpenAPI, GraphQL schema, etc.).

## Interfaces Provided

While not "APIs" in the traditional sense, this feature does provide interfaces:

### 1. Just Commands (CLI Interface)

Developers interact via command-line:

```bash
just lint          # Run linters
just test          # Run tests
just type-check    # Run type checkers
just format        # Format code
just ci            # Run all checks
```

**Contract**: Defined in `justfile` at repository root
**Documentation**: [quickstart.md](../quickstart.md)

### 2. Pre-commit Hooks (Git Interface)

Git automatically triggers hooks:

```bash
git commit         # Triggers pre-commit hooks
# Hooks run: ruff, mypy, eslint, prettier, commitizen
```

**Contract**: Defined in `.pre-commit-config.yaml`
**Documentation**: [quickstart.md](../quickstart.md)

### 3. GitHub Actions (CI Interface)

GitHub triggers workflows on events:

```yaml
on:
  push: # Workflow A (feature branches)
  pull_request: # Workflow B (PR to main)
```

**Contract**: Defined in `.github/workflows/*.yml`
**Documentation**: [research.md](../research.md)

## External Tool Integrations

The feature integrates with external tools/services:

### GitHub Actions API

- **Provider**: GitHub
- **Documentation**: https://docs.github.com/en/actions
- **Usage**: Workflow execution, status checks, caching

### Codecov API

- **Provider**: Codecov
- **Documentation**: https://docs.codecov.com/
- **Usage**: Coverage report upload and tracking

### Safety Database API

- **Provider**: PyUp.io
- **Documentation**: https://pyup.io/safety/
- **Usage**: Vulnerability scanning for Python dependencies

## Next Steps

For implementation details, see:

- [research.md](../research.md) - Tool integrations and configurations
- [quickstart.md](../quickstart.md) - How to use the CI system
- [plan.md](../plan.md) - Overall implementation architecture
