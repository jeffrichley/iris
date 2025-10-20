# Iris Project - Task Runner Commands
# Run `just` to see all available commands

# Set shell based on OS for cross-platform compatibility
# Windows uses PowerShell, Unix-like systems use sh
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]
set shell := ["sh", "-cu"]

# Default recipe - show available commands
default:
    @just --list

# 🚀 Complete development environment setup (run this first!)
dev:
    @echo "=== Setting up development environment ==="
    @echo ""
    @echo "📦 1/4 Installing Python dependencies..."
    uv sync --extra dev
    @echo ""
    @echo "🪝 2/4 Installing pre-commit hooks..."
    uv run pre-commit install
    uv run pre-commit install --hook-type commit-msg
    @echo ""
    @echo "🔐 3/4 Setting up secrets baseline..."
    -uv run detect-secrets scan > .secrets.baseline || echo "Secrets baseline already exists"
    @echo ""
    @echo "✅ 4/4 Verifying installation..."
    uv run ruff --version
    uv run mypy --version
    uv run pytest --version
    @echo ""
    @echo "=== ✨ Development environment ready! ==="
    @echo ""
    @echo "Next steps:"
    @echo "  • Run 'just test' to verify tests pass"
    @echo "  • Run 'just ci' to run all CI checks"
    @echo "  • Run 'just commit' for guided commits"
    @echo "  • Run 'just' to see all available commands"

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

# Clean build artifacts, cache, and temporary files
clean:
    @echo "🧹 Cleaning build artifacts and cache..."
    -rm -rf build dist *.egg-info
    -rm -rf .pytest_cache .mypy_cache .ruff_cache htmlcov .coverage coverage.xml
    -rm -rf src/**/__pycache__ tests/**/__pycache__
    -rm -rf frontend/node_modules frontend/dist frontend/.next
    @echo "✓ Clean complete!"

# Full clean including virtual environment
clean-all: clean
    @echo "🧹 Removing virtual environment..."
    -rm -rf .venv
    @echo "✓ Full clean complete! Run 'just dev' to reinstall."

# Run security scans locally
security:
    @echo "=== Running security scans ==="
    @echo "🔍 1/2 Scanning code with Bandit..."
    uv run bandit -r src/ --severity-level medium
    @echo ""
    @echo "🔐 2/2 Checking for secrets..."
    uv run detect-secrets scan --baseline .secrets.baseline
    @echo ""
    @echo "✓ Security scans complete!"

# Update dependencies and pre-commit hooks
update:
    @echo "=== Updating dependencies ==="
    @echo "📦 Updating Python packages..."
    uv sync --extra dev --upgrade
    @echo "🪝 Updating pre-commit hooks..."
    uv run pre-commit autoupdate
    @echo "✓ Updates complete! Review changes and commit."

# Run pre-commit on all files
pre-commit:
    @echo "Running pre-commit checks on all files..."
    uv run pre-commit run --all-files

# Open coverage report in browser
coverage:
    @echo "Running tests with coverage..."
    uv run pytest --cov=src --cov-report=html
    @echo "Opening coverage report..."
    {{if os() == "windows" { "start htmlcov/index.html" } else if os() == "macos" { "open htmlcov/index.html" } else { "xdg-open htmlcov/index.html" } }}

