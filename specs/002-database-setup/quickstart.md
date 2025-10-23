# Quickstart: Database Setup

**Feature**: Database Setup
**Date**: 2024-12-19
**Phase**: 1 - Design & Contracts

## Overview

This quickstart guide will help you set up the database infrastructure for the Iris project management system. The setup includes database connections, schema management, data models, and CLI tools.

## Prerequisites

- Python 3.11+
- SQLite 3.30+ (included with Python)
- PostgreSQL 12+ (optional, for production)

## Installation

### 1. Install Dependencies

```bash
# Install required packages
pip install sqlalchemy alembic rich typer pydantic python-dotenv

# Or using uv (recommended)
uv add sqlalchemy alembic rich typer pydantic python-dotenv
```

### 2. Environment Configuration

Create a `.env` file in your project root:

```bash
# Database Configuration
DATABASE_URL=sqlite:///./.iris/iris.db
# For PostgreSQL: postgresql://user:password@localhost:5432/iris  # pragma: allowlist secret

# Connection Settings
DB_HOST=localhost
DB_PORT=5432
DB_NAME=iris
DB_USER=iris_user
DB_PASSWORD=your_password

# Connection Pool Settings
DB_POOL_SIZE=5
DB_POOL_TIMEOUT=300

# Environment
ENVIRONMENT=development
```

## Database Setup

### 1. Initialize Database

```bash
# Create database and run migrations
iris-dev db migrate

# Test database connection
iris-dev db test-connection

# Check database health
iris-dev db health-check
```

### 2. Verify Setup

```bash
# Check database tables
sqlite3 .iris/iris.db ".tables"

# Expected output:
# alembic_version  ideas        projects     reminders    tasks
# notes
```

## CLI Usage

### Database Commands

```bash
# Test database connectivity
iris-dev db test-connection

# Run database migrations
iris-dev db migrate

# Check database health
iris-dev db health-check
```

### Command Options

```bash
# Verbose output
iris-dev db migrate --verbose

# Force migration (skip confirmation)
iris-dev db migrate --force

# Health check with details
iris-dev db health-check --detailed
```

## CLI Database Management

### Health Check

```bash
# Check database health via CLI
iris-dev db health-check

# Output
✅ Database Health Check
┌─────────────────┬─────────────┐
│ Status          │ Healthy     │
│ Response Time    │ 15.2ms     │
│ Active Conn      │ 2/5         │
│ Idle Conn        │ 3/5         │
│ Last Check       │ 10:30:00    │
└─────────────────┴─────────────┘
```

### Migration Management

```bash
# Run migrations via CLI
iris-dev db migrate

# Output
🔄 Running Database Migrations
┌─────────────────────────────────┬─────────────┐
│ Migration                       │ Status      │
├─────────────────────────────────┼─────────────┤
│ 001_initial_schema              │ ✅ Applied  │
│ 002_add_user_preferences        │ ✅ Applied  │
│ 003_add_project_tags            │ ⏳ Running  │
└─────────────────────────────────┴─────────────┘
⏱️  Total time: 1.25s
```

## Development Workflow

### 1. Database Changes

```bash
# Create new migration
alembic revision --autogenerate -m "Add new field"

# Review generated migration
cat alembic/versions/xxx_add_new_field.py

# Apply migration
iris-dev db migrate
```

### 2. Testing

```bash
# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/

# Run all tests
pytest
```

### 3. Development Database

```bash
# Use test database
export DATABASE_URL=sqlite:///./test_iris.db

# Run tests
pytest

# Clean up test database
rm test_iris.db
```

## Production Setup

### 1. PostgreSQL Configuration

```bash
# Install PostgreSQL
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# macOS
brew install postgresql

# Start PostgreSQL
sudo systemctl start postgresql  # Linux
brew services start postgresql   # macOS
```

### 2. Database Creation

```sql
-- Connect to PostgreSQL
psql -U postgres

-- Create database and user
CREATE DATABASE iris;
CREATE USER iris_user WITH PASSWORD 'your_password';  -- pragma: allowlist secret
GRANT ALL PRIVILEGES ON DATABASE iris TO iris_user;
```

### 3. Environment Configuration

```bash
# Production .env
DATABASE_URL=postgresql://iris_user:your_password@localhost:5432/iris  # pragma: allowlist secret
ENVIRONMENT=production
DB_POOL_SIZE=10
DB_POOL_TIMEOUT=600
```

## Troubleshooting

### Common Issues

#### Connection Refused
```bash
# Check database service
sudo systemctl status postgresql

# Check connection
iris-dev db test-connection
```

#### Migration Failures
```bash
# Check migration status
alembic current

# Check migration history
alembic history

# Rollback migration
alembic downgrade -1
```

#### Permission Issues
```bash
# Check database permissions
psql -U postgres -c "\l"

# Grant permissions
GRANT ALL PRIVILEGES ON DATABASE iris TO iris_user;
```

### Debug Mode

```bash
# Enable debug logging
export LOG_LEVEL=DEBUG

# Run with verbose output
iris-dev db migrate --verbose

# Check logs
tail -f logs/iris.log
```

## Next Steps

1. **Create your first project**: Use the TUI to create a new project
2. **Add tasks**: Create tasks for your project
3. **Set reminders**: Add reminders for important deadlines
4. **Take notes**: Add project notes and ideas

## Support

- **Documentation**: [Iris Documentation](https://docs.iris.example.com)
- **Issues**: [GitHub Issues](https://github.com/iris/iris/issues)
- **Discord**: [Iris Community](https://discord.gg/iris)

## Related Features

- **TUI Interface**: Interactive terminal interface
- **API Endpoints**: REST API for database operations
- **Data Models**: SQLAlchemy models for data access
- **CLI Tools**: Command-line interface for database management
