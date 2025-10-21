-- Migration: 001_initial_schema
-- Description: Create core tables with Row Level Security policies
-- Date: 2025-10-20
-- Per data-model.md and FR-005 through FR-013, FR-047 through FR-051

BEGIN;

-- ============================================================================
-- UTILITY FUNCTIONS
-- ============================================================================

-- Function to automatically update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Function to set completed_at when task is marked complete
CREATE OR REPLACE FUNCTION set_completed_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    IF NEW.completed = TRUE AND OLD.completed = FALSE THEN
        NEW.completed_at = NOW();
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- ============================================================================
-- TABLE: projects (FR-005)
-- ============================================================================

CREATE TABLE IF NOT EXISTS projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    name TEXT NOT NULL CHECK (LENGTH(name) > 0 AND LENGTH(name) <= 255),
    description TEXT,
    status TEXT NOT NULL CHECK (status IN ('active', 'archived', 'completed')) DEFAULT 'active',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes for performance (FR-012)
CREATE INDEX idx_projects_user_id ON projects(user_id);
CREATE INDEX idx_projects_status ON projects(status);
CREATE INDEX idx_projects_created_at ON projects(created_at DESC);

-- Trigger for updated_at
CREATE TRIGGER update_projects_updated_at
    BEFORE UPDATE ON projects
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- TABLE: tasks (FR-006)
-- ============================================================================

CREATE TABLE IF NOT EXISTS tasks (
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

-- Indexes (FR-012)
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_project_id ON tasks(project_id);
CREATE INDEX idx_tasks_due_date ON tasks(due_date) WHERE due_date IS NOT NULL;
CREATE INDEX idx_tasks_completed ON tasks(completed) WHERE completed = FALSE;
CREATE INDEX idx_tasks_created_at ON tasks(created_at DESC);

-- Triggers
CREATE TRIGGER update_tasks_updated_at
    BEFORE UPDATE ON tasks
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER set_task_completed_at
    BEFORE UPDATE ON tasks
    FOR EACH ROW
    WHEN (NEW.completed = TRUE AND OLD.completed = FALSE)
    EXECUTE FUNCTION set_completed_timestamp();

-- ============================================================================
-- TABLE: ideas (FR-007)
-- ============================================================================

CREATE TABLE IF NOT EXISTS ideas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    title TEXT NOT NULL CHECK (LENGTH(title) > 0 AND LENGTH(title) <= 255),
    description TEXT,
    promoted_to_project_id UUID REFERENCES projects(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes (FR-012)
CREATE INDEX idx_ideas_user_id ON ideas(user_id);
CREATE INDEX idx_ideas_promoted ON ideas(promoted_to_project_id) WHERE promoted_to_project_id IS NOT NULL;
CREATE INDEX idx_ideas_created_at ON ideas(created_at DESC);

-- ============================================================================
-- TABLE: reminders (FR-008)
-- ============================================================================

CREATE TABLE IF NOT EXISTS reminders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    task_id UUID REFERENCES tasks(id) ON DELETE CASCADE,
    message TEXT NOT NULL CHECK (LENGTH(message) > 0),
    due_time TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes (FR-012)
CREATE INDEX idx_reminders_user_id ON reminders(user_id);
CREATE INDEX idx_reminders_task_id ON reminders(task_id) WHERE task_id IS NOT NULL;
CREATE INDEX idx_reminders_due_time ON reminders(due_time) WHERE due_time > NOW();
CREATE INDEX idx_reminders_created_at ON reminders(created_at DESC);

-- ============================================================================
-- TABLE: notes (FR-009)
-- ============================================================================

CREATE TABLE IF NOT EXISTS notes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    project_id UUID NOT NULL REFERENCES projects(id) ON DELETE CASCADE,
    content TEXT NOT NULL CHECK (LENGTH(content) > 0),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Indexes (FR-012)
CREATE INDEX idx_notes_user_id ON notes(user_id);
CREATE INDEX idx_notes_project_id ON notes(project_id);
CREATE INDEX idx_notes_created_at ON notes(created_at DESC);

-- Trigger for updated_at
CREATE TRIGGER update_notes_updated_at
    BEFORE UPDATE ON notes
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- ============================================================================
-- ROW LEVEL SECURITY (RLS) POLICIES
-- Per FR-013, FR-047, FR-048, FR-049, FR-050
-- ============================================================================

-- Enable RLS on all tables
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;
ALTER TABLE ideas ENABLE ROW LEVEL SECURITY;
ALTER TABLE reminders ENABLE ROW LEVEL SECURITY;
ALTER TABLE notes ENABLE ROW LEVEL SECURITY;

-- ============================================================================
-- RLS POLICIES: projects
-- ============================================================================

-- SELECT: Users can only read their own projects (FR-048)
CREATE POLICY "users_read_own_projects"
ON projects FOR SELECT
USING (auth.uid() = user_id);

-- INSERT: Users can only insert with their user_id (FR-049)
CREATE POLICY "users_insert_own_projects"
ON projects FOR INSERT
WITH CHECK (auth.uid() = user_id);

-- UPDATE: Users can only update their own projects
CREATE POLICY "users_update_own_projects"
ON projects FOR UPDATE
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

-- DELETE: Users can only delete their own projects
CREATE POLICY "users_delete_own_projects"
ON projects FOR DELETE
USING (auth.uid() = user_id);

-- ============================================================================
-- RLS POLICIES: tasks
-- ============================================================================

CREATE POLICY "users_read_own_tasks"
ON tasks FOR SELECT
USING (auth.uid() = user_id);

CREATE POLICY "users_insert_own_tasks"
ON tasks FOR INSERT
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "users_update_own_tasks"
ON tasks FOR UPDATE
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "users_delete_own_tasks"
ON tasks FOR DELETE
USING (auth.uid() = user_id);

-- ============================================================================
-- RLS POLICIES: ideas
-- ============================================================================

CREATE POLICY "users_read_own_ideas"
ON ideas FOR SELECT
USING (auth.uid() = user_id);

CREATE POLICY "users_insert_own_ideas"
ON ideas FOR INSERT
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "users_update_own_ideas"
ON ideas FOR UPDATE
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "users_delete_own_ideas"
ON ideas FOR DELETE
USING (auth.uid() = user_id);

-- ============================================================================
-- RLS POLICIES: reminders
-- ============================================================================

CREATE POLICY "users_read_own_reminders"
ON reminders FOR SELECT
USING (auth.uid() = user_id);

CREATE POLICY "users_insert_own_reminders"
ON reminders FOR INSERT
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "users_update_own_reminders"
ON reminders FOR UPDATE
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "users_delete_own_reminders"
ON reminders FOR DELETE
USING (auth.uid() = user_id);

-- ============================================================================
-- RLS POLICIES: notes
-- ============================================================================

CREATE POLICY "users_read_own_notes"
ON notes FOR SELECT
USING (auth.uid() = user_id);

CREATE POLICY "users_insert_own_notes"
ON notes FOR INSERT
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "users_update_own_notes"
ON notes FOR UPDATE
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

CREATE POLICY "users_delete_own_notes"
ON notes FOR DELETE
USING (auth.uid() = user_id);

COMMIT;

-- Migration complete!
-- All 5 tables created with RLS policies
-- Tables: projects, tasks, ideas, reminders, notes
-- Total RLS policies: 20 (4 per table × 5 tables)

