# Iris Database Migrations Guide

## Overview

Iris uses Alembic for database schema migrations, providing version control for database changes. This guide covers migration management, best practices, and troubleshooting.

## Migration System

### Alembic Configuration

The migration system is configured in `alembic.ini`:

```ini
[alembic]
script_location = alembic
sqlalchemy.url = sqlite:///./.iris/iris.db
version_num_format = %%04d
```

### Environment Setup

The `alembic/env.py` file configures the migration environment:

```python
from src.iris.core.database.models import Base
from src.iris.core.config.settings import get_settings

# Set target metadata
target_metadata = Base.metadata

# Get database URL from settings
settings = get_settings()
database_url = settings.get_database_url()
config.set_main_option("sqlalchemy.url", database_url)
```

## Migration Commands

### Basic Commands

```bash
# Check current migration status
python -m alembic current

# View migration history
python -m alembic history

# Show pending migrations
python -m alembic show head

# Run migrations to latest version
python -m alembic upgrade head

# Run migrations to specific version
python -m alembic upgrade 0001

# Rollback to previous version
python -m alembic downgrade -1

# Rollback to specific version
python -m alembic downgrade base
```

### Migration Generation

```bash
# Generate migration from model changes
python -m alembic revision --autogenerate -m "Description of changes"

# Generate empty migration
python -m alembic revision -m "Description of changes"

# Generate migration with specific revision ID
python -m alembic revision --rev-id 0002 -m "Description of changes"
```

### Migration Validation

```bash
# Check migration syntax
python -m alembic check

# Validate migration chain
python -m alembic branches

# Show migration differences
python -m alembic show <revision>
```

## Migration Files

### File Structure

Migration files are located in `alembic/versions/` and follow the naming pattern:
`{revision_id}_{description}.py`

Example: `001_initial_schema.py`

### Migration File Template

```python
"""Description of changes

Revision ID: 0001
Revises:
Create Date: 2024-12-19 16:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers
revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Apply migration changes."""
    # Migration code here
    pass

def downgrade() -> None:
    """Rollback migration changes."""
    # Rollback code here
    pass
```

### Initial Schema Migration

The initial schema migration (`001_initial_schema.py`) creates all core tables:

```python
def upgrade() -> None:
    """Create initial database schema."""

    # Create projects table
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('status', sa.String(length=50), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    # Create tasks table
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(length=255), nullable=False),
        sa.Column('priority', sa.String(length=50), nullable=False),
        sa.Column('due_date', sa.Date(), nullable=True),
        sa.Column('completed', sa.Boolean(), nullable=False),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id']),
        sa.PrimaryKeyConstraint('id')
    )

    # Create indexes
    op.create_index('ix_tasks_project_id', 'tasks', ['project_id'])
    op.create_index('ix_tasks_completed', 'tasks', ['completed'])
    op.create_index('ix_tasks_due_date', 'tasks', ['due_date'])
```

## Migration Workflow

### Development Workflow

1. **Make model changes** in `src/iris/core/database/models.py`
2. **Generate migration** using `alembic revision --autogenerate`
3. **Review generated migration** for accuracy
4. **Test migration** on development database
5. **Commit migration** to version control

### Production Workflow

1. **Backup database** before migration
2. **Test migration** on staging environment
3. **Schedule maintenance window** if needed
4. **Run migration** using `alembic upgrade head`
5. **Verify migration** success
6. **Monitor application** for issues

### Rollback Workflow

1. **Identify target version** for rollback
2. **Backup current database** state
3. **Run rollback** using `alembic downgrade`
4. **Verify rollback** success
5. **Test application** functionality

## Best Practices

### Migration Design

1. **Keep migrations small** and focused
2. **Use descriptive names** for migrations
3. **Include both upgrade and downgrade** functions
4. **Test rollback procedures** regularly
5. **Document breaking changes** clearly

### Data Safety

1. **Always backup** before migrations
2. **Test migrations** on development data
3. **Use transactions** for data migrations
4. **Validate data** after migrations
5. **Monitor performance** impact

### Code Organization

1. **Group related changes** in single migration
2. **Use separate migrations** for different features
3. **Order operations** logically (create, modify, drop)
4. **Handle dependencies** between tables
5. **Consider performance** implications

## Common Migration Patterns

### Adding New Table

```python
def upgrade() -> None:
    op.create_table(
        'new_table',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('new_table')
```

### Adding New Column

```python
def upgrade() -> None:
    op.add_column('existing_table',
        sa.Column('new_column', sa.String(255), nullable=True)
    )

def downgrade() -> None:
    op.drop_column('existing_table', 'new_column')
```

### Modifying Column

```python
def upgrade() -> None:
    op.alter_column('existing_table', 'column_name',
        existing_type=sa.String(100),
        type_=sa.String(255),
        nullable=False
    )

def downgrade() -> None:
    op.alter_column('existing_table', 'column_name',
        existing_type=sa.String(255),
        type_=sa.String(100),
        nullable=True
    )
```

### Adding Index

```python
def upgrade() -> None:
    op.create_index('ix_table_column', 'table_name', ['column_name'])

def downgrade() -> None:
    op.drop_index('ix_table_column', 'table_name')
```

### Data Migration

```python
def upgrade() -> None:
    # Add new column
    op.add_column('projects',
        sa.Column('new_field', sa.String(255), nullable=True)
    )

    # Migrate data
    connection = op.get_bind()
    connection.execute(
        "UPDATE projects SET new_field = 'default_value' WHERE new_field IS NULL"
    )

    # Make column non-nullable
    op.alter_column('projects', 'new_field', nullable=False)

def downgrade() -> None:
    op.drop_column('projects', 'new_field')
```

## Troubleshooting

### Common Issues

#### Migration Conflicts

```bash
# Check for conflicts
python -m alembic branches

# Resolve conflicts by merging
python -m alembic merge -m "Merge conflicts" <revision1> <revision2>
```

#### Failed Migrations

```bash
# Check migration status
python -m alembic current

# Show migration history
python -m alembic history

# Rollback to previous version
python -m alembic downgrade -1

# Retry migration
python -m alembic upgrade head
```

#### Database Lock Issues

```bash
# Check for active connections
# Close all database connections
# Retry migration
python -m alembic upgrade head
```

### Debugging Migrations

#### Enable Verbose Logging

```python
# In alembic/env.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Check Migration SQL

```bash
# Show SQL for migration
python -m alembic upgrade head --sql

# Show SQL for specific revision
python -m alembic upgrade <revision> --sql
```

#### Validate Migration Files

```bash
# Check migration syntax
python -m alembic check

# Validate migration chain
python -m alembic branches
```

## Advanced Topics

### Custom Migration Operations

```python
def upgrade() -> None:
    # Custom operation
    op.execute("CREATE INDEX CONCURRENTLY idx_name ON table_name (column_name)")

def downgrade() -> None:
    op.execute("DROP INDEX CONCURRENTLY idx_name")
```

### Conditional Migrations

```python
def upgrade() -> None:
    # Check if column exists
    connection = op.get_bind()
    inspector = sa.inspect(connection)
    columns = [col['name'] for col in inspector.get_columns('table_name')]

    if 'new_column' not in columns:
        op.add_column('table_name',
            sa.Column('new_column', sa.String(255), nullable=True)
        )
```

### Multi-Database Migrations

```python
def upgrade() -> None:
    # Different operations for different databases
    if op.get_bind().dialect.name == 'postgresql':
        op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm")
    elif op.get_bind().dialect.name == 'sqlite':
        op.execute("PRAGMA foreign_keys = ON")
```

## Migration Testing

### Unit Testing Migrations

```python
import pytest
from alembic import command
from alembic.config import Config

def test_migration_upgrade():
    config = Config("alembic.ini")
    # Test upgrade
    command.upgrade(config, "head")

def test_migration_downgrade():
    config = Config("alembic.ini")
    # Test downgrade
    command.downgrade(config, "base")
```

### Integration Testing

```python
def test_migration_with_data():
    # Setup test data
    # Run migration
    # Verify data integrity
    # Test rollback
    pass
```

## Production Considerations

### Zero-Downtime Migrations

1. **Add columns** as nullable first
2. **Populate data** in background
3. **Make columns** non-nullable
4. **Drop old columns** in separate migration

### Large Table Migrations

1. **Use batch operations** for large tables
2. **Add indexes** concurrently
3. **Monitor performance** during migration
4. **Consider maintenance windows**

### Backup and Recovery

1. **Full database backup** before migration
2. **Test restore procedures** regularly
3. **Document recovery steps** clearly
4. **Keep migration backups** for rollback

## Monitoring and Alerting

### Migration Monitoring

```python
# Log migration events
import logging
logger = logging.getLogger('alembic')

def log_migration_start():
    logger.info("Migration started")

def log_migration_complete():
    logger.info("Migration completed successfully")

def log_migration_failure(error):
    logger.error(f"Migration failed: {error}")
```

### Health Checks

```python
# Check migration status
def check_migration_status():
    from alembic import command
    from alembic.config import Config

    config = Config("alembic.ini")
    current = command.current(config)
    head = command.heads(config)

    return current == head
```

## Migration Documentation

### Documenting Changes

1. **Include detailed descriptions** in migration messages
2. **Document breaking changes** clearly
3. **Provide rollback instructions** when needed
4. **Update API documentation** for schema changes

### Version Control

1. **Commit migration files** to version control
2. **Tag releases** with migration versions
3. **Maintain migration history** in documentation
4. **Track migration dependencies** between features

## Security Considerations

### Migration Security

1. **Validate migration files** before execution
2. **Use parameterized queries** in migrations
3. **Avoid sensitive data** in migration files
4. **Implement access controls** for migration execution

### Data Protection

1. **Encrypt sensitive data** during migration
2. **Use secure connections** for database access
3. **Implement audit logging** for migration events
4. **Follow data retention** policies during migrations
