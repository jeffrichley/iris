# Iris Database Schema Documentation

## Overview

The Iris project management system uses a SQLite database with a well-structured schema designed for local-first operation. The database schema is managed using Alembic migrations and follows SQLAlchemy ORM patterns.

## Database Information

- **Database Type**: SQLite
- **Location**: `.iris/iris.db` (configurable via environment)
- **Migration System**: Alembic
- **ORM**: SQLAlchemy 2.0+
- **Connection Pooling**: Yes (configurable)

## Schema Version

- **Current Version**: 0001
- **Migration File**: `alembic/versions/001_initial_schema.py`
- **Last Updated**: 2024-12-19

## Entity Relationship Diagram

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Projects  │    │    Tasks    │    │   Ideas     │
│             │    │             │    │             │
│ id (PK)     │◄───┤ project_id  │    │ id (PK)     │
│ name        │    │ id (PK)     │    │ project_id  │
│ description │    │ title       │    │ title       │
│ status      │    │ priority    │    │ description │
│ created_at  │    │ due_date    │    │ promoted    │
│ updated_at  │    │ completed   │    │ created_at  │
└─────────────┘    │ notes       │    └─────────────┘
       │           │ created_at  │           │
       │           │ updated_at  │           │
       │           └─────────────┘           │
       │                   │                │
       │                   │                │
       ▼                   ▼                ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Reminders  │    │    Notes    │    │ alembic_    │
│             │    │             │    │ version     │
│ id (PK)     │    │ id (PK)     │    │             │
│ project_id  │    │ project_id  │    │ version_num  │
│ task_id     │    │ content    │    └─────────────┘
│ message     │    │ created_at │
│ due_time    │    │ updated_at │
│ created_at  │    └─────────────┘
└─────────────┘
```

## Tables

### Projects Table

The `projects` table stores project information and serves as the main entity in the system.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique project identifier |
| `name` | VARCHAR(255) | NOT NULL, UNIQUE | Project name |
| `description` | TEXT | NULL | Project description |
| `status` | VARCHAR(50) | NOT NULL | Project status (active, completed, paused) |
| `created_at` | DATETIME | NOT NULL | Creation timestamp |
| `updated_at` | DATETIME | NOT NULL | Last update timestamp |

**Indexes:**
- Primary key on `id`
- Unique index on `name`

**Constraints:**
- `ck_projects_status`: Status must be one of 'active', 'completed', 'paused'

### Tasks Table

The `tasks` table stores individual tasks belonging to projects.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique task identifier |
| `project_id` | INTEGER | NOT NULL, FK | Reference to projects.id |
| `title` | VARCHAR(255) | NOT NULL | Task title |
| `priority` | VARCHAR(50) | NOT NULL | Task priority (low, medium, high, urgent) |
| `due_date` | DATE | NULL | Task due date |
| `completed` | BOOLEAN | NOT NULL | Completion status |
| `notes` | TEXT | NULL | Task notes |
| `created_at` | DATETIME | NOT NULL | Creation timestamp |
| `updated_at` | DATETIME | NOT NULL | Last update timestamp |

**Indexes:**
- Primary key on `id`
- Foreign key on `project_id`
- `ix_tasks_project_id`: Index on project_id
- `ix_tasks_completed`: Index on completed status
- `ix_tasks_due_date`: Index on due_date
- `ix_tasks_project_completed`: Composite index on project_id, completed

**Constraints:**
- `ck_tasks_priority`: Priority must be one of 'low', 'medium', 'high', 'urgent'
- `ck_tasks_completed`: Completed must be TRUE or FALSE
- Foreign key constraint: `project_id` references `projects.id`

### Ideas Table

The `ideas` table stores spontaneous ideas that may become projects.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique idea identifier |
| `project_id` | INTEGER | NULL, FK | Reference to projects.id (optional) |
| `title` | VARCHAR(255) | NOT NULL | Idea title |
| `description` | TEXT | NULL | Idea description |
| `promoted_to_project` | BOOLEAN | NOT NULL | Whether idea was promoted to project |
| `created_at` | DATETIME | NOT NULL | Creation timestamp |

**Indexes:**
- Primary key on `id`
- Foreign key on `project_id` (nullable)
- `ix_ideas_project_id`: Index on project_id

**Constraints:**
- `ck_ideas_promoted`: Promoted_to_project must be TRUE or FALSE
- Foreign key constraint: `project_id` references `projects.id` (nullable)

### Reminders Table

The `reminders` table stores notifications for tasks or projects.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique reminder identifier |
| `project_id` | INTEGER | NULL, FK | Reference to projects.id (optional) |
| `task_id` | INTEGER | NULL, FK | Reference to tasks.id (optional) |
| `message` | TEXT | NOT NULL | Reminder message |
| `due_time` | DATETIME | NOT NULL | Reminder due time |
| `created_at` | DATETIME | NOT NULL | Creation timestamp |

**Indexes:**
- Primary key on `id`
- Foreign key on `project_id` (nullable)
- Foreign key on `task_id` (nullable)
- `ix_reminders_due_time`: Index on due_time
- `ix_reminders_project_id`: Index on project_id
- `ix_reminders_task_id`: Index on task_id
- `ix_reminders_due_project`: Composite index on due_time, project_id

**Constraints:**
- At least one of `project_id` or `task_id` must be provided (enforced at application level)
- Foreign key constraint: `project_id` references `projects.id` (nullable)
- Foreign key constraint: `task_id` references `tasks.id` (nullable)

### Notes Table

The `notes` table stores free-form notes tied to projects.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `id` | INTEGER | PRIMARY KEY | Unique note identifier |
| `project_id` | INTEGER | NULL, FK | Reference to projects.id (optional) |
| `content` | TEXT | NOT NULL | Note content |
| `created_at` | DATETIME | NOT NULL | Creation timestamp |
| `updated_at` | DATETIME | NOT NULL | Last update timestamp |

**Indexes:**
- Primary key on `id`
- Foreign key on `project_id` (nullable)
- `ix_notes_project_id`: Index on project_id

**Constraints:**
- Foreign key constraint: `project_id` references `projects.id` (nullable)

### Alembic Version Table

The `alembic_version` table tracks database migration versions.

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `version_num` | VARCHAR(32) | PRIMARY KEY | Current migration version |

## Relationships

### One-to-Many Relationships

1. **Projects → Tasks**: One project can have many tasks
2. **Projects → Ideas**: One project can have many ideas
3. **Projects → Reminders**: One project can have many reminders
4. **Projects → Notes**: One project can have many notes
5. **Tasks → Reminders**: One task can have many reminders

### Many-to-One Relationships

1. **Tasks → Projects**: Many tasks belong to one project
2. **Ideas → Projects**: Many ideas can belong to one project (optional)
3. **Reminders → Projects**: Many reminders can belong to one project (optional)
4. **Reminders → Tasks**: Many reminders can belong to one task (optional)
5. **Notes → Projects**: Many notes can belong to one project (optional)

## Data Types

### Supported Data Types

- **INTEGER**: Auto-incrementing primary keys
- **VARCHAR(n)**: Variable-length strings with length limits
- **TEXT**: Unlimited text content
- **BOOLEAN**: True/False values
- **DATETIME**: Timestamp values
- **DATE**: Date-only values

### Constraints

- **Primary Keys**: All tables have auto-incrementing integer primary keys
- **Foreign Keys**: Proper referential integrity with cascade options
- **Check Constraints**: Data validation at database level
- **Unique Constraints**: Prevent duplicate values where appropriate
- **NOT NULL**: Required fields are marked as NOT NULL

## Indexes

### Performance Indexes

The schema includes several indexes for optimal query performance:

1. **Primary Indexes**: All primary keys are automatically indexed
2. **Foreign Key Indexes**: All foreign keys are indexed for join performance
3. **Status Indexes**: Frequently queried status fields are indexed
4. **Date Indexes**: Date/time fields used in queries are indexed
5. **Composite Indexes**: Multi-column indexes for complex queries

### Index Naming Convention

- `ix_{table}_{column}`: Single column index
- `ix_{table}_{column1}_{column2}`: Composite index

## Migration History

### Version 0001: Initial Schema

**Date**: 2024-12-19
**Description**: Initial database schema creation

**Changes:**
- Created all core tables (projects, tasks, ideas, reminders, notes)
- Added all indexes for performance
- Added all constraints for data integrity
- Set up proper foreign key relationships

## Best Practices

### Data Integrity

1. **Foreign Key Constraints**: All relationships are properly constrained
2. **Check Constraints**: Data validation at database level
3. **Unique Constraints**: Prevent duplicate data where appropriate
4. **NOT NULL Constraints**: Ensure required data is present

### Performance

1. **Indexes**: Strategic indexing for common query patterns
2. **Composite Indexes**: Multi-column indexes for complex queries
3. **Foreign Key Indexes**: All foreign keys are indexed
4. **Status Indexes**: Frequently queried status fields are indexed

### Maintenance

1. **Migration System**: Alembic for schema versioning
2. **Backup Strategy**: Regular database backups recommended
3. **Monitoring**: Database health monitoring available via CLI
4. **Logging**: Comprehensive logging for database operations

## Security Considerations

### Data Protection

1. **Local Storage**: SQLite database files should be protected
2. **Backup Security**: Backup files should be encrypted
3. **Access Control**: Database file permissions should be restricted
4. **Audit Trail**: All changes are logged with timestamps

### Privacy

1. **Personal Data**: User data is stored locally
2. **No External Dependencies**: No data is sent to external services
3. **Data Ownership**: Users have full control over their data
4. **Export Capability**: Data can be exported for portability

## Troubleshooting

### Common Issues

1. **Migration Failures**: Check Alembic version and migration files
2. **Connection Issues**: Verify database file permissions and location
3. **Performance Issues**: Check index usage and query patterns
4. **Data Corruption**: Use database integrity checks

### Recovery

1. **Backup Restoration**: Use CLI backup/restore commands
2. **Migration Rollback**: Use Alembic downgrade commands
3. **Data Recovery**: Use SQLite recovery tools if needed
4. **Schema Repair**: Recreate database from migrations if necessary

## Future Enhancements

### Planned Features

1. **Full-Text Search**: Add FTS capabilities for content search
2. **Data Archiving**: Archive old data to maintain performance
3. **Replication**: Multi-device synchronization
4. **Encryption**: Database-level encryption for sensitive data

### Schema Evolution

1. **Version Control**: All schema changes go through migrations
2. **Backward Compatibility**: Maintain compatibility where possible
3. **Data Migration**: Automatic data migration with schema changes
4. **Rollback Support**: Ability to rollback schema changes
