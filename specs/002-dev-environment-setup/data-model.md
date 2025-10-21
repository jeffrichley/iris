# Data Model: Cloud-First Database Schema

**Feature**: Cloud-First Development Environment Setup  
**Phase**: 1 (Design & Contracts)  
**Date**: October 20, 2025  
**Database**: Supabase PostgreSQL with Row Level Security

## Overview

This document defines the database schema for Iris's 5 core entities (projects, tasks, ideas, reminders, notes) with user isolation via Row Level Security (RLS) policies.

**Key Design Principles**:
- User-scoped data (all tables include `user_id` foreign key to `auth.users`)
- UUID primary keys for distributed compatibility
- Timestamps (created_at, updated_at) with timezone support
- RLS policies enforce data isolation at database level
- Foreign keys with CASCADE for data integrity

---

## Entity Relationship Diagram

```
auth.users (Supabase managed)
    ↓ (1:N)
    ├── projects
    │       ↓ (1:N)
    │       ├── tasks
    │       │       ↓ (1:N optional)
    │       │       └── reminders
    │       └── notes
    └── ideas
            ↓ (N:1 optional)
            └── projects (promoted_to_project_id)
```

---

## Tables

### 1. projects

**Purpose**: User's organizational containers for tasks and notes

```sql
CREATE TABLE projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    name TEXT NOT NULL CHECK (LENGTH(name) > 0 AND LENGTH(name) <= 255),
    description TEXT,
    status TEXT NOT NULL CHECK (status IN ('active', 'archived', 'completed')) DEFAULT 'active',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX idx_projects_user_id ON projects(user_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_created_at ON projects(created_at DESC);

-- Trigger for updated_at
CREATE TRIGGER update_projects_updated_at
    BEFORE UPDATE ON projects
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
```

**Fields**:
- `id` (UUID): Primary key, auto-generated
- `user_id` (UUID): Owner reference, indexed for RLS
- `name` (TEXT): Project name, required, max 255 chars
- `description` (TEXT): Optional project details
- `status` (ENUM): active | archived | completed, default active
- `created_at` (TIMESTAMPTZ): Auto-set on insert
- `updated_at` (TIMESTAMPTZ): Auto-updated on modification

**Validation Rules**:
- Name must be 1-255 characters
- Status must be valid enum value
- User_id must exist in auth.users

**State Transitions**:
```
active → archived
active → completed
archived → active
completed → (no transitions, final state)
```

---

### 2. tasks

**Purpose**: Work items belonging to projects with priority and completion tracking

```sql
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    title TEXT NOT NULL CHECK (LENGTH(title) > 0 AND LENGTH(title) <= 500),
    priority TEXT NOT NULL CHECK (priority IN ('high', 'medium', 'low')) DEFAULT 'medium',
    due_date TIMESTAMPTZ,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    completed_at TIMESTAMPTZ,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_project_id ON tasks(project_id);
CREATE INDEX idx_tasks_due_date ON tasks(due_date) WHERE due_date IS NOT NULL;
CREATE INDEX idx_tasks_completed ON tasks(completed) WHERE completed = FALSE;

-- Trigger for updated_at
CREATE TRIGGER update_tasks_updated_at
    BEFORE UPDATE ON tasks
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- Trigger to set completed_at
CREATE TRIGGER set_completed_at
    BEFORE UPDATE ON tasks
    FOR EACH ROW
    WHEN (NEW.completed = TRUE AND OLD.completed = FALSE)
    EXECUTE FUNCTION set_completed_timestamp();
```

**Fields**:
- `id` (UUID): Primary key
- `user_id` (UUID): Owner reference (denormalized for RLS)
- `project_id` (UUID): Parent project reference
- `title` (TEXT): Task description, required, max 500 chars
- `priority` (ENUM): high | medium | low, default medium
- `due_date` (TIMESTAMPTZ): Optional deadline
- `completed` (BOOLEAN): Completion status, default false
- `completed_at` (TIMESTAMPTZ): Auto-set when completed = true
- `notes` (TEXT): Optional task details
- `created_at`, `updated_at` (TIMESTAMPTZ)

**Validation Rules**:
- Title must be 1-500 characters
- Priority must be valid enum value
- Project_id must belong to same user (enforced by RLS + FK)
- If completed = true, completed_at auto-set

**Business Rules**:
- Deleting project cascades to delete all tasks
- Marking task complete sets completed_at timestamp
- Cannot un-complete a task (completed_at persists)

---

### 3. ideas

**Purpose**: Captured spontaneous ideas with optional promotion to projects

```sql
CREATE TABLE ideas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    title TEXT NOT NULL CHECK (LENGTH(title) > 0 AND LENGTH(title) <= 255),
    description TEXT,
    promoted_to_project_id UUID REFERENCES projects(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_ideas_user_id ON ideas(user_id);
CREATE INDEX idx_ideas_promoted ON ideas(promoted_to_project_id) WHERE promoted_to_project_id IS NOT NULL;
CREATE INDEX idx_ideas_created_at ON ideas(created_at DESC);
```

**Fields**:
- `id` (UUID): Primary key
- `user_id` (UUID): Owner reference
- `title` (TEXT): Idea summary, required, max 255 chars
- `description` (TEXT): Optional detailed description
- `promoted_to_project_id` (UUID): Optional link to created project
- `created_at` (TIMESTAMPTZ): Capture timestamp

**Validation Rules**:
- Title must be 1-255 characters
- If promoted, project_id must belong to same user

**Business Rules**:
- Ideas are immutable after creation (no update needed)
- Promoting idea sets promoted_to_project_id
- Deleting promoted project sets promoted_to_project_id = NULL

---

### 4. reminders

**Purpose**: Time-based notifications optionally linked to tasks

```sql
CREATE TABLE reminders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    task_id UUID REFERENCES tasks(id) ON DELETE CASCADE,
    message TEXT NOT NULL CHECK (LENGTH(message) > 0),
    due_time TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_reminders_user_id ON reminders(user_id);
CREATE INDEX idx_reminders_task_id ON reminders(task_id) WHERE task_id IS NOT NULL;
CREATE INDEX idx_reminders_due_time ON reminders(due_time) WHERE due_time > NOW();
```

**Fields**:
- `id` (UUID): Primary key
- `user_id` (UUID): Owner reference
- `task_id` (UUID): Optional task link (standalone or task-bound)
- `message` (TEXT): Reminder content, required
- `due_time` (TIMESTAMPTZ): When to trigger notification, required
- `created_at` (TIMESTAMPTZ): Creation timestamp

**Validation Rules**:
- Message must not be empty
- Due_time must be set
- If task_id set, task must belong to same user

**Business Rules**:
- Reminders can exist without task_id (standalone reminders)
- Deleting task cascades to delete linked reminders
- Past reminders (due_time < NOW()) retained for history

---

### 5. notes

**Purpose**: Free-form text content attached to projects

```sql
CREATE TABLE notes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    content TEXT NOT NULL CHECK (LENGTH(content) > 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_notes_user_id ON notes(user_id);
CREATE INDEX idx_notes_project_id ON notes(project_id);
CREATE INDEX idx_notes_created_at ON notes(created_at DESC);

-- Trigger for updated_at
CREATE TRIGGER update_notes_updated_at
    BEFORE UPDATE ON notes
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();
```

**Fields**:
- `id` (UUID): Primary key
- `user_id` (UUID): Owner reference (denormalized for RLS)
- `project_id` (UUID): Parent project reference
- `content` (TEXT): Note text, required, no max length
- `created_at`, `updated_at` (TIMESTAMPTZ)

**Validation Rules**:
- Content must not be empty
- Project_id must belong to same user

**Business Rules**:
- Deleting project cascades to delete all notes
- Notes support full-text search (future: GIN index on content)

---

## Row Level Security (RLS) Policies

### Pattern for All Tables

```sql
-- Enable RLS
ALTER TABLE {table_name} ENABLE ROW LEVEL SECURITY;

-- SELECT policy: Users read only their own data
CREATE POLICY "users_read_own_{table}"
ON {table_name} FOR SELECT
USING (auth.uid() = user_id);

-- INSERT policy: Users can only insert with their user_id
CREATE POLICY "users_insert_own_{table}"
ON {table_name} FOR INSERT
WITH CHECK (auth.uid() = user_id);

-- UPDATE policy: Users can only update their own data
CREATE POLICY "users_update_own_{table}"
ON {table_name} FOR UPDATE
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

-- DELETE policy: Users can only delete their own data
CREATE POLICY "users_delete_own_{table}"
ON {table_name} FOR DELETE
USING (auth.uid() = user_id);
```

### Applied to All Tables

- ✅ projects
- ✅ tasks
- ✅ ideas
- ✅ reminders
- ✅ notes

**RLS Enforcement**:
- Supabase automatically injects `auth.uid()` from JWT in request
- FastAPI doesn't need to manually filter by user_id (RLS handles it)
- Defense-in-depth: Even if application code has bugs, RLS prevents cross-user data access

---

## Utility Functions

### update_updated_at_column()

```sql
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

**Used by**: projects, tasks, notes

### set_completed_timestamp()

```sql
CREATE OR REPLACE FUNCTION set_completed_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.completed = TRUE AND OLD.completed = FALSE THEN
        NEW.completed_at = NOW();
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

**Used by**: tasks (auto-set completed_at when completed = true)

---

## Constraints Summary

| Table | Constraints |
|-------|-------------|
| projects | name length (1-255), status enum, user_id FK |
| tasks | title length (1-500), priority enum, user_id/project_id FK, due_date optional |
| ideas | title length (1-255), user_id FK, promoted_to_project_id nullable FK |
| reminders | message not empty, due_time required, user_id/task_id FK |
| notes | content not empty, user_id/project_id FK |

**All tables**:
- UUID primary keys
- user_id foreign key to auth.users (ON DELETE CASCADE)
- created_at timestamptz default NOW()
- Indexed on user_id for RLS performance

---

## Migration Order

1. Create utility functions (update_updated_at_column, set_completed_timestamp)
2. Create projects table + indexes + RLS + triggers
3. Create tasks table (depends on projects) + indexes + RLS + triggers
4. Create ideas table (depends on projects) + indexes + RLS
5. Create reminders table (depends on tasks) + indexes + RLS
6. Create notes table (depends on projects) + indexes + RLS + triggers

**File**: `src/iris/database/migrations/001_initial_schema.sql`

---

## Performance Considerations

**Indexes**:
- All user_id columns indexed for RLS queries
- Foreign keys indexed for JOIN performance
- created_at indexed DESC for recent-first queries
- Partial indexes on filtered queries (e.g., incomplete tasks)

**Query Patterns**:
```sql
-- Efficient: Uses idx_tasks_user_id + idx_tasks_completed
SELECT * FROM tasks WHERE user_id = $1 AND completed = FALSE;

-- Efficient: Uses idx_tasks_project_id
SELECT * FROM tasks WHERE project_id = $1;

-- Efficient: Uses idx_reminders_due_time
SELECT * FROM reminders WHERE due_time > NOW() AND due_time < NOW() + INTERVAL '24 hours';
```

**RLS Performance**:
- RLS policies use indexed user_id columns
- auth.uid() function cached per request
- Supabase automatically optimizes RLS query plans

---

## Data Integrity

**Foreign Key Cascade Behavior**:

| Parent | Child | ON DELETE |
|--------|-------|-----------|
| auth.users | All tables | CASCADE (delete user → delete all data) |
| projects | tasks | CASCADE (delete project → delete tasks) |
| projects | notes | CASCADE (delete project → delete notes) |
| projects | ideas | SET NULL (delete promoted project → clear link) |
| tasks | reminders | CASCADE (delete task → delete reminders) |

**Denormalized user_id**:
- Tasks and notes include user_id (also available via project)
- Enables RLS policies without JOINs
- Trade-off: Extra 16 bytes per row for query performance

---

## Future Enhancements

- **Full-text search**: GIN index on notes.content, ideas.description
- **Audit logging**: Trigger-based change tracking
- **Soft deletes**: Add deleted_at column, modify RLS to exclude deleted
- **Version history**: Track changes to projects/tasks for undo/redo
- **Tags/labels**: Many-to-many relationship for task/project tagging

---

## Testing Considerations

**Unit Tests** (SQLModel validation):
- UUID generation
- Enum validation (status, priority)
- Constraint violations (name length, empty strings)

**Integration Tests** (Database):
- Foreign key constraints enforced
- CASCADE deletes work correctly
- Triggers fire on update (updated_at, completed_at)
- Indexes exist and are used (EXPLAIN ANALYZE)

**RLS Tests**:
- User A cannot read User B's data
- User A cannot modify User B's data
- Service role can bypass RLS for admin operations

---

**Phase 1 Data Model Complete. Next: API Contracts.**

