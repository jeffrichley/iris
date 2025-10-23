# Iris Database API Documentation

## Overview

The Iris database API provides a comprehensive interface for database operations through SQLAlchemy ORM models and service classes. The API is designed for type safety, performance, and ease of use.

## Architecture

### Core Components

1. **Models**: SQLAlchemy ORM models defining database entities
2. **Services**: Business logic layer for CRUD operations
3. **Connection**: Database connection management with pooling
4. **Monitoring**: Health monitoring and performance metrics
5. **Error Handling**: Comprehensive error handling and recovery

### Design Patterns

- **Repository Pattern**: Service classes encapsulate data access
- **Unit of Work**: Transaction management through sessions
- **Connection Pooling**: Efficient connection reuse
- **Error Handling**: Centralized exception management

## Models

### Project Model

```python
from src.iris.core.database.models import Project

# Create a new project
project = Project(
    name="My Project",
    description="Project description",
    status="active"
)

# Access project properties
print(project.id)           # Auto-generated ID
print(project.name)         # Project name
print(project.status)       # Project status
print(project.created_at)   # Creation timestamp
print(project.updated_at)  # Last update timestamp
```

**Properties:**
- `id`: Integer primary key
- `name`: String (255 chars, unique)
- `description`: Text (optional)
- `status`: String (active, completed, paused)
- `created_at`: DateTime
- `updated_at`: DateTime

**Relationships:**
- `tasks`: List of associated tasks
- `notes`: List of associated notes
- `reminders`: List of associated reminders
- `ideas`: List of associated ideas

### Task Model

```python
from src.iris.core.database.models import Task

# Create a new task
task = Task(
    project_id=1,
    title="Complete feature",
    priority="high",
    due_date=date(2024, 12, 31),
    completed=False,
    notes="Important task notes"
)

# Access task properties
print(task.id)              # Auto-generated ID
print(task.project_id)      # Parent project ID
print(task.title)           # Task title
print(task.priority)        # Task priority
print(task.completed)       # Completion status
```

**Properties:**
- `id`: Integer primary key
- `project_id`: Integer foreign key
- `title`: String (255 chars)
- `priority`: String (low, medium, high, urgent)
- `due_date`: Date (optional)
- `completed`: Boolean
- `notes`: Text (optional)
- `created_at`: DateTime
- `updated_at`: DateTime

**Relationships:**
- `project`: Parent project
- `reminders`: List of associated reminders

### Idea Model

```python
from src.iris.core.database.models import Idea

# Create a new idea
idea = Idea(
    project_id=1,  # Optional
    title="Great idea",
    description="Detailed idea description",
    promoted_to_project=False
)

# Access idea properties
print(idea.id)                    # Auto-generated ID
print(idea.project_id)            # Associated project (optional)
print(idea.title)                 # Idea title
print(idea.promoted_to_project)   # Promotion status
```

**Properties:**
- `id`: Integer primary key
- `project_id`: Integer foreign key (optional)
- `title`: String (255 chars)
- `description`: Text (optional)
- `promoted_to_project`: Boolean
- `created_at`: DateTime

**Relationships:**
- `project`: Associated project (optional)

### Reminder Model

```python
from src.iris.core.database.models import Reminder

# Create a new reminder
reminder = Reminder(
    project_id=1,  # Optional
    task_id=1,     # Optional
    message="Don't forget to review the code",
    due_time=datetime(2024, 12, 25, 10, 0, 0)
)

# Access reminder properties
print(reminder.id)        # Auto-generated ID
print(reminder.message)   # Reminder message
print(reminder.due_time)  # Due time
```

**Properties:**
- `id`: Integer primary key
- `project_id`: Integer foreign key (optional)
- `task_id`: Integer foreign key (optional)
- `message`: Text
- `due_time`: DateTime
- `created_at`: DateTime

**Relationships:**
- `project`: Associated project (optional)
- `task`: Associated task (optional)

### Note Model

```python
from src.iris.core.database.models import Note

# Create a new note
note = Note(
    project_id=1,  # Optional
    content="Important project notes"
)

# Access note properties
print(note.id)           # Auto-generated ID
print(note.content)      # Note content
print(note.created_at)   # Creation timestamp
```

**Properties:**
- `id`: Integer primary key
- `project_id`: Integer foreign key (optional)
- `content`: Text
- `created_at`: DateTime
- `updated_at`: DateTime

**Relationships:**
- `project`: Associated project (optional)

## Services

### ProjectService

```python
from src.iris.core.database.services import ProjectService
from src.iris.core.database.connection import get_database_connection

# Get database connection
db_connection = get_database_connection()
session = db_connection.get_session()

# Create service
project_service = ProjectService(session)

# Create a new project
project = project_service.create(
    name="My New Project",
    description="Project description",
    status="active"
)

# Get project by ID
project = project_service.get_by_id(1)

# Get all projects
projects = project_service.get_all()

# Get projects by status
active_projects = project_service.get_by_status("active")

# Update project
project_service.update(1, name="Updated Project Name")

# Delete project
project_service.delete(1)

# Get project statistics
stats = project_service.get_statistics()
```

**Methods:**
- `create(name, description=None, status="active")`: Create new project
- `get_by_id(project_id)`: Get project by ID
- `get_all()`: Get all projects
- `get_by_status(status)`: Get projects by status
- `update(project_id, **kwargs)`: Update project
- `delete(project_id)`: Delete project
- `get_statistics()`: Get project statistics

### TaskService

```python
from src.iris.core.database.services import TaskService

# Create service
task_service = TaskService(session)

# Create a new task
task = task_service.create(
    project_id=1,
    title="Complete feature",
    priority="high",
    due_date=date(2024, 12, 31),
    notes="Important task"
)

# Get task by ID
task = task_service.get_by_id(1)

# Get tasks by project
project_tasks = task_service.get_by_project(1)

# Get tasks by status
completed_tasks = task_service.get_by_status(completed=True)

# Update task
task_service.update(1, completed=True)

# Delete task
task_service.delete(1)
```

**Methods:**
- `create(project_id, title, priority="medium", due_date=None, notes=None, completed=False)`: Create new task
- `get_by_id(task_id)`: Get task by ID
- `get_by_project(project_id)`: Get tasks by project
- `get_by_status(completed)`: Get tasks by completion status
- `update(task_id, **kwargs)`: Update task
- `delete(task_id)`: Delete task

### IdeaService

```python
from src.iris.core.database.services import IdeaService

# Create service
idea_service = IdeaService(session)

# Create a new idea
idea = idea_service.create(
    title="Great idea",
    description="Detailed description",
    project_id=1  # Optional
)

# Get idea by ID
idea = idea_service.get_by_id(1)

# Get all ideas
ideas = idea_service.get_all()

# Get ideas by project
project_ideas = idea_service.get_by_project(1)

# Promote idea to project
idea_service.promote_to_project(1)

# Delete idea
idea_service.delete(1)
```

**Methods:**
- `create(title, description=None, project_id=None)`: Create new idea
- `get_by_id(idea_id)`: Get idea by ID
- `get_all()`: Get all ideas
- `get_by_project(project_id)`: Get ideas by project
- `promote_to_project(idea_id)`: Promote idea to project
- `delete(idea_id)`: Delete idea

### ReminderService

```python
from src.iris.core.database.services import ReminderService

# Create service
reminder_service = ReminderService(session)

# Create a new reminder
reminder = reminder_service.create(
    project_id=1,  # Optional
    task_id=1,     # Optional
    message="Don't forget!",
    due_time=datetime(2024, 12, 25, 10, 0, 0)
)

# Get reminder by ID
reminder = reminder_service.get_by_id(1)

# Get reminders by project
project_reminders = reminder_service.get_by_project(1)

# Get reminders by task
task_reminders = reminder_service.get_by_task(1)

# Get upcoming reminders
upcoming = reminder_service.get_upcoming(days=7)

# Delete reminder
reminder_service.delete(1)
```

**Methods:**
- `create(project_id=None, task_id=None, message, due_time)`: Create new reminder
- `get_by_id(reminder_id)`: Get reminder by ID
- `get_by_project(project_id)`: Get reminders by project
- `get_by_task(task_id)`: Get reminders by task
- `get_upcoming(days=7)`: Get upcoming reminders
- `delete(reminder_id)`: Delete reminder

### NoteService

```python
from src.iris.core.database.services import NoteService

# Create service
note_service = NoteService(session)

# Create a new note
note = note_service.create(
    project_id=1,  # Optional
    content="Important notes"
)

# Get note by ID
note = note_service.get_by_id(1)

# Get notes by project
project_notes = note_service.get_by_project(1)

# Update note
note_service.update(1, content="Updated content")

# Delete note
note_service.delete(1)
```

**Methods:**
- `create(project_id=None, content)`: Create new note
- `get_by_id(note_id)`: Get note by ID
- `get_by_project(project_id)`: Get notes by project
- `update(note_id, **kwargs)`: Update note
- `delete(note_id)`: Delete note

## Connection Management

### Database Connection

```python
from src.iris.core.database.connection import initialize_database, get_database_connection

# Initialize database connection
db_connection = initialize_database(
    database_url="sqlite:///iris.db",
    pool_size=5,
    pool_timeout=300,
    pool_recycle=3600,
    echo=False
)

# Get existing connection
db_connection = get_database_connection()

# Test connection
is_connected = await db_connection.test_connection()

# Get connection info
info = await db_connection.get_connection_info()

# Health check
health = await db_connection.health_check()
```

### Session Management

```python
from src.iris.core.database.connection import get_database_connection

# Get database connection
db_connection = get_database_connection()

# Get session factory
session_factory = db_connection.get_session_factory()

# Create session
session = session_factory()

try:
    # Use session for database operations
    project = session.query(Project).filter_by(id=1).first()
    session.commit()
except Exception as e:
    session.rollback()
    raise
finally:
    session.close()
```

### Async Session Management

```python
# Async session context manager
async with db_connection.get_session() as session:
    # Use session for database operations
    project = await session.get(Project, 1)
    await session.commit()
```

## Error Handling

### Exception Types

```python
from src.iris.core.utils.exceptions import (
    DatabaseError, ConnectionError, ValidationError,
    BusinessLogicError, SystemError
)

try:
    # Database operations
    project = project_service.create("My Project")
except ValidationError as e:
    print(f"Validation error: {e.message}")
    print(f"Field: {e.details.get('field')}")
    print(f"Suggestions: {e.suggestions}")
except DatabaseError as e:
    print(f"Database error: {e.message}")
    print(f"Error code: {e.error_code}")
except ConnectionError as e:
    print(f"Connection error: {e.message}")
    print(f"Database URL: {e.details.get('database_url')}")
```

### Error Recovery

```python
from src.iris.core.utils.error_handler import retry_on_error

@retry_on_error(max_retries=3, retry_delay=1.0)
async def create_project_with_retry(name: str):
    return project_service.create(name)
```

## Performance Optimization

### Query Optimization

```python
# Use indexes for filtering
projects = session.query(Project).filter_by(status="active").all()

# Use composite indexes
tasks = session.query(Task).filter_by(project_id=1, completed=False).all()

# Use date indexes
upcoming_tasks = session.query(Task).filter(
    Task.due_date >= date.today()
).all()
```

### Connection Pooling

```python
# Configure connection pool
db_connection = initialize_database(
    database_url="sqlite:///iris.db",
    pool_size=10,        # Maximum connections
    pool_timeout=300,   # Connection timeout
    pool_recycle=3600   # Connection recycle time
)
```

### Batch Operations

```python
# Batch insert
projects = [
    Project(name=f"Project {i}", status="active")
    for i in range(100)
]
session.add_all(projects)
session.commit()

# Batch update
session.query(Task).filter_by(completed=False).update({
    "completed": True
})
session.commit()
```

## Monitoring and Health Checks

### Health Monitoring

```python
from src.iris.core.database.monitoring import DatabaseMonitor

# Create monitor
monitor = DatabaseMonitor(db_connection)

# Get health metrics
health = await monitor.get_health_metrics()
print(f"Status: {health.status}")
print(f"Response time: {health.response_time}ms")
print(f"Connection count: {health.connection_count}")

# Get performance metrics
performance = await monitor.get_performance_metrics()
print(f"Query count: {performance.query_count}")
print(f"Average query time: {performance.avg_query_time}ms")
```

### Diagnostics

```python
# Get diagnostics
diagnostics = await monitor.get_diagnostics()
print(f"Database size: {diagnostics.database_size}MB")
print(f"Table counts: {diagnostics.table_counts}")
print(f"Index usage: {diagnostics.index_usage}")
```

## Best Practices

### Transaction Management

```python
# Always use transactions for multiple operations
session = session_factory()
try:
    # Create project
    project = Project(name="My Project")
    session.add(project)
    session.flush()  # Get the ID

    # Create tasks
    task1 = Task(project_id=project.id, title="Task 1")
    task2 = Task(project_id=project.id, title="Task 2")
    session.add_all([task1, task2])

    session.commit()
except Exception as e:
    session.rollback()
    raise
finally:
    session.close()
```

### Error Handling

```python
# Always handle exceptions properly
try:
    project = project_service.create("My Project")
except ValidationError as e:
    # Handle validation errors
    logger.error(f"Validation failed: {e.message}")
    raise
except DatabaseError as e:
    # Handle database errors
    logger.error(f"Database error: {e.message}")
    raise
except Exception as e:
    # Handle unexpected errors
    logger.error(f"Unexpected error: {e}")
    raise
```

### Performance Considerations

```python
# Use appropriate indexes
projects = session.query(Project).filter_by(status="active").all()

# Avoid N+1 queries
projects = session.query(Project).options(
    joinedload(Project.tasks)
).all()

# Use pagination for large datasets
projects = session.query(Project).offset(0).limit(20).all()
```

## Migration Management

### Running Migrations

```python
# Run migrations programmatically
from alembic import command
from alembic.config import Config

# Configure Alembic
config = Config("alembic.ini")

# Run migrations
command.upgrade(config, "head")

# Check current version
command.current(config)

# Generate new migration
command.revision(config, autogenerate=True, message="Add new field")
```

### Migration Best Practices

1. **Always backup before migrations**
2. **Test migrations on development data**
3. **Use descriptive migration messages**
4. **Review generated migrations before applying**
5. **Test rollback procedures**

## Security Considerations

### Data Protection

1. **Use parameterized queries** (SQLAlchemy ORM handles this)
2. **Validate input data** before database operations
3. **Use appropriate data types** for sensitive information
4. **Implement access controls** at the application level

### Backup and Recovery

1. **Regular backups** of database files
2. **Test restore procedures** regularly
3. **Version control** for migration files
4. **Document recovery procedures**

## Troubleshooting

### Common Issues

1. **Connection timeouts**: Check pool configuration
2. **Lock timeouts**: Check for long-running transactions
3. **Disk space**: Monitor database file size
4. **Performance**: Check index usage and query patterns

### Debugging

```python
# Enable SQL logging
import logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

# Use database monitoring
monitor = DatabaseMonitor(db_connection)
health = await monitor.get_health_metrics()
performance = await monitor.get_performance_metrics()
```
