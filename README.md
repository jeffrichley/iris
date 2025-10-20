# 🌸 Iris - Personal Project Management Assistant

[![CI - Feature Branch](https://github.com/jeffrichley/iris/actions/workflows/ci-feature-branch.yml/badge.svg)](https://github.com/jeffrichley/iris/actions/workflows/ci-feature-branch.yml)
[![CI - PR to Main](https://github.com/jeffrichley/iris/actions/workflows/ci-pr-main.yml/badge.svg)](https://github.com/jeffrichley/iris/actions/workflows/ci-pr-main.yml)
[![CodeQL](https://github.com/jeffrichley/iris/actions/workflows/codeql.yml/badge.svg)](https://github.com/jeffrichley/iris/actions/workflows/codeql.yml)
[![codecov](https://codecov.io/gh/jeffrichley/iris/branch/main/graph/badge.svg)](https://codecov.io/gh/jeffrichley/iris)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue)](https://mypy-lang.org/)

A local-first personal project management assistant powered by AI.

## Quick Start

### Prerequisites

- Python 3.12 or 3.13
- Node.js 20.x LTS (for frontend)
- [uv](https://github.com/astral-sh/uv) - Fast Python package installer
- [just](https://github.com/casey/just) - Command runner

### Install just (Task Runner)

**macOS/Linux**:
```bash
# Using Homebrew
brew install just

# Using cargo
cargo install just
```

**Windows**:
```powershell
# Using Scoop
scoop install just

# Using Cargo
cargo install just

# Or download from https://github.com/casey/just/releases
```

### Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jeffrichley/iris.git
   cd iris
   ```

2. **Install dependencies**:
   ```bash
   uv sync --dev
   ```

3. **Install pre-commit hooks** (recommended):
   ```bash
   just setup-hooks
   ```

   **What are pre-commit hooks?**  
   Automated checks that run before each commit to catch issues early:
   - ✅ Auto-format Python (ruff) and TypeScript (prettier)
   - ✅ Check types (mypy for Python, TypeScript compiler)
   - ✅ Lint code (ruff for Python, ESLint for TypeScript)
   - ✅ Detect secrets (API keys, tokens, credentials)
   - ✅ Prevent common mistakes (trailing whitespace, large files, merge conflicts)

   See [Pre-commit Setup Guide](docs/development/pre-commit-setup.md) for details.

4. **Verify setup**:
   ```bash
   just ci
   ```

## Available Commands

Run `just` to see all available commands:

```bash
just lint          # Run linting
just test          # Run tests  
just type-check    # Run type checking
just format        # Format code
just ci            # Run all checks (lint + type-check + test)
just commit        # Interactive commit with Conventional Commits guidance
just setup-hooks   # Install pre-commit hooks
```

## Commit Message Format

This project uses [Conventional Commits](https://www.conventionalcommits.org/) for clear, consistent commit history.

### Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

| Type | Use For | Example |
|------|---------|---------|
| `feat` | New features | `feat(auth): add OAuth2 support` |
| `fix` | Bug fixes | `fix(sync): resolve conflict resolution` |
| `docs` | Documentation | `docs(api): update authentication guide` |
| `style` | Code style (no logic change) | `style(ui): adjust button spacing` |
| `refactor` | Code restructuring | `refactor(db): simplify query builder` |
| `perf` | Performance improvements | `perf(search): add index on task title` |
| `test` | Tests | `test(tasks): add edge case coverage` |
| `chore` | Build, tooling, dependencies | `chore(deps): update ruff to 0.2.0` |
| `ci` | CI configuration | `ci: optimize cache strategy` |

### Interactive Commit (Recommended)

```bash
git add .
just commit  # Interactive prompts guide you through creating a proper commit
```

### Manual Commit

If writing manually, the commit message hook will validate the format:

```bash
# ✅ Good
git commit -m "feat(tasks): add priority levels"

# ❌ Bad (will be rejected)
git commit -m "Added stuff"
```

## Project Structure

```
iris/
├── src/           # Python source code
├── tests/         # Test files
├── frontend/      # React/TypeScript frontend (coming soon)
├── docs/          # Documentation
└── specs/         # Feature specifications
```

## Contributing

This is a personal project, but suggestions and feedback are welcome! Please:

1. Check existing issues or create a new one
2. Follow the code style (enforced by pre-commit hooks)
3. Write tests for new features
4. Ensure all CI checks pass

## License

MIT License - See LICENSE file for details

---

**Status**: 🚧 Early Development

# Fix pre-commit.ci queue
