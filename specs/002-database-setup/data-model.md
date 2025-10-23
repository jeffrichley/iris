# Data Model: Database Setup

**Feature**: Database Setup
**Date**: 2024-12-19
**Phase**: 1 - Design & Contracts

## Entity Definitions

### Project Entity

**Table**: `projects`
**Purpose**: Represents individual projects in the Iris system

**Fields**:
- `id` (INTEGER PRIMARY KEY) - Unique identifier
- `name` (VARCHAR NOT NULL) - Project name
- `description` (TEXT) - Project description
- `status` (VARCHAR NOT NULL) - Project status ('active', 'completed', 'paused')
- `created_at` (TIMESTAMP NOT NULL) - Creation timestamp
- `updated_at` (TIMESTAMP NOT NULL) - Last update timestamp

**Validation Rules**:
- `name` must be non-empty and unique
- `status` must be one of: 'active', 'completed', 'paused'
- `created_at` and `updated_at` are automatically set
- `updated_at` is automatically updated on record changes

**Relationships**:
- One-to-many with `tasks`
- One-to-many with `notes`
- One-to-many with `reminders`
- One-to-many with `ideas`

### Task Entity

**Table**: `tasks`
**Purpose**: Work items belonging to projects

**Fields**:
- `id` (INTEGER PRIMARY KEY) - Unique identifier
- `project_id` (INTEGER NOT NULL, FOREIGN KEY → projects.id) - Parent project
- `title` (VARCHAR NOT NULL) - Task title
- `priority` (VARCHAR NOT NULL) - Task priority ('low', 'medium', 'high', 'urgent')
- `due_date` (DATE) - Task due date
- `completed` (BOOLEAN NOT NULL DEFAULT FALSE) - Completion status
- `notes` (TEXT) - Task notes
- `created_at` (TIMESTAMP NOT NULL) - Creation timestamp
- `updated_at` (TIMESTAMP NOT NULL) - Last update timestamp

**Validation Rules**:
- `title` must be non-empty
- `priority` must be one of: 'low', 'medium', 'high', 'urgent'
- `project_id` must reference existing project
- `due_date` must be valid date if provided
- `completed` defaults to FALSE

**Relationships**:
- Many-to-one with `projects`
- One-to-many with `reminders`

### Idea Entity

**Table**: `ideas`
**Purpose**: Spontaneous ideas that may become projects

**Fields**:
- `id` (INTEGER PRIMARY KEY) - Unique identifier
- `project_id` (INTEGER, FOREIGN KEY → projects.id, nullable) - Associated project
- `title` (VARCHAR NOT NULL) - Idea title
- `description` (TEXT) - Idea description
- `promoted_to_project` (BOOLEAN NOT NULL DEFAULT FALSE) - Promotion status
- `created_at` (TIMESTAMP NOT NULL) - Creation timestamp

**Validation Rules**:
- `title` must be non-empty
- `project_id` must reference existing project if provided
- `promoted_to_project` defaults to FALSE

**Relationships**:
- Many-to-one with `projects` (optional)

### Reminder Entity

**Table**: `reminders`
**Purpose**: Notifications for tasks or projects

**Fields**:
- `id` (INTEGER PRIMARY KEY) - Unique identifier
- `project_id` (INTEGER, FOREIGN KEY → projects.id, nullable) - Associated project
- `task_id` (INTEGER, FOREIGN KEY → tasks.id, nullable) - Associated task
- `message` (TEXT NOT NULL) - Reminder message
- `due_time` (TIMESTAMP NOT NULL) - Reminder time
- `created_at` (TIMESTAMP NOT NULL) - Creation timestamp

**Validation Rules**:
- `message` must be non-empty
- `due_time` must be valid timestamp
- Either `project_id` or `task_id` must be provided (not both)
- `project_id` must reference existing project if provided
- `task_id` must reference existing task if provided

**Relationships**:
- Many-to-one with `projects` (optional)
- Many-to-one with `tasks` (optional)

### Note Entity

**Table**: `notes`
**Purpose**: Free-form notes tied to projects

**Fields**:
- `id` (INTEGER PRIMARY KEY) - Unique identifier
- `project_id` (INTEGER, FOREIGN KEY → projects.id, nullable) - Associated project
- `content` (TEXT NOT NULL) - Note content
- `created_at` (TIMESTAMP NOT NULL) - Creation timestamp
- `updated_at` (TIMESTAMP NOT NULL) - Last update timestamp

**Validation Rules**:
- `content` must be non-empty
- `project_id` must reference existing project if provided
- `created_at` and `updated_at` are automatically set
- `updated_at` is automatically updated on record changes

**Relationships**:
- Many-to-one with `projects` (optional)

## Database Constraints

### Primary Keys
- All tables have `id` as INTEGER PRIMARY KEY
- Auto-incrementing for new records

### Foreign Keys
- `tasks.project_id` → `projects.id` (NOT NULL)
- `ideas.project_id` → `projects.id` (nullable)
- `reminders.project_id` → `projects.id` (nullable)
- `reminders.task_id` → `tasks.id` (nullable)
- `notes.project_id` → `projects.id` (nullable)

### Check Constraints
- `projects.status` IN ('active', 'completed', 'paused')
- `tasks.priority` IN ('low', 'medium', 'high', 'urgent')
- `tasks.completed` IN (TRUE, FALSE)
- `ideas.promoted_to_project` IN (TRUE, FALSE)

### Unique Constraints
- `projects.name` (unique project names)

### Not Null Constraints
- All `id` fields
- All `created_at` and `updated_at` fields
- `projects.name` and `status`
- `tasks.project_id`, `title`, `priority`, `completed`
- `ideas.title`
- `reminders.message` and `due_time`
- `notes.content`

## Indexes

### Performance Indexes
- `projects.name` (unique index)
- `tasks.project_id` (foreign key index)
- `tasks.completed` (for filtering completed tasks)
- `tasks.due_date` (for date-based queries)
- `ideas.project_id` (foreign key index)
- `reminders.due_time` (for time-based queries)
- `reminders.project_id` (foreign key index)
- `reminders.task_id` (foreign key index)
- `notes.project_id` (foreign key index)

### Composite Indexes
- `tasks(project_id, completed)` (for project task queries)
- `reminders(due_time, project_id)` (for project reminders)

## Data Validation

### Application-Level Validation
- String length limits (configurable)
- Date range validation
- Email format validation (if applicable)
- HTML sanitization for text fields

### Database-Level Validation
- Foreign key constraints
- Check constraints for enumerated values
- Not null constraints
- Unique constraints

## State Transitions

### Project Status Transitions
- `active` → `completed` (project finished)
- `active` → `paused` (project suspended)
- `paused` → `active` (project resumed)
- `completed` → `active` (project reopened)

### Task Completion Transitions
- `completed: FALSE` → `completed: TRUE` (task finished)
- `completed: TRUE` → `completed: FALSE` (task reopened)

### Idea Promotion Transitions
- `promoted_to_project: FALSE` → `promoted_to_project: TRUE` (idea becomes project)

## Data Relationships Summary

```
projects (1) ←→ (many) tasks
projects (1) ←→ (many) notes
projects (1) ←→ (many) reminders
projects (1) ←→ (many) ideas
tasks (1) ←→ (many) reminders
```

## Migration Strategy

### Initial Schema
- Create all tables with proper constraints
- Add all indexes for performance
- Set up foreign key relationships
- Configure auto-incrementing primary keys

### Future Extensions
- Add new fields with DEFAULT values
- Create new tables with foreign keys
- Add new indexes as needed
- Modify constraints with proper migration scripts

## Data Integrity Rules

### Referential Integrity
- All foreign keys must reference existing records
- Cascade deletes for project deletion (tasks, notes, reminders, ideas)
- Restrict deletes for task deletion (reminders)

### Business Rules
- Project names must be unique
- Task priorities must be valid enumerated values
- Reminder times must be in the future
- Completed tasks cannot have future due dates
- Ideas can only be promoted once

### Data Consistency
- Timestamps are automatically managed
- Status changes are validated
- Required fields are enforced
- Data types are strictly enforced
