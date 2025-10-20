# Iris Project - Task Runner Commands
# Run `just` to see all available commands

# Set shell based on OS for cross-platform compatibility
# Windows uses PowerShell, Unix-like systems use sh
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]
set shell := ["sh", "-cu"]

# Default recipe - show available commands
default:
    @just --list

# Run linting
lint:
    @echo "Running Python linting..."
    uv run ruff check .
    @echo "Running TypeScript linting..."
    -cd frontend 2>nul && npm run lint || echo "Frontend not yet set up"

# Format code
format:
    @echo "Formatting Python code..."
    uv run ruff format .
    @echo "Formatting TypeScript code..."
    -cd frontend 2>nul && npm run format || echo "Frontend not yet set up"

# Run type checking
type-check:
    @echo "Running Python type checking..."
    uv run mypy src/
    @echo "Running TypeScript type checking..."
    -cd frontend 2>nul && npm run type-check || echo "Frontend not yet set up"

# Run tests
test:
    @echo "Running tests with coverage..."
    uv run pytest

# Run all CI checks (lint + type-check + test)
ci:
    @echo "=== Running CI Checks ==="
    @just lint
    @just type-check
    @just test
    @echo "=== All CI Checks Passed ==="

# Install pre-commit hooks
setup-hooks:
    @echo "Installing pre-commit hooks..."
    pre-commit install
    pre-commit install --hook-type commit-msg
    @echo "✓ Pre-commit hooks installed successfully!"
    @echo "Run 'pre-commit run --all-files' to test"

# Interactive commit with Conventional Commits guidance
commit:
    @echo "Starting interactive commit (Conventional Commits)..."
    uv run cz commit

