"""Initial database schema

Revision ID: 0001
Revises:
Create Date: 2024-12-19 16:00:00.000000

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create initial database schema."""

    # Create projects table
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("status", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )

    # Create tasks table
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("priority", sa.String(length=50), nullable=False),
        sa.Column("due_date", sa.Date(), nullable=True),
        sa.Column("completed", sa.Boolean(), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # Create ideas table
    op.create_table(
        "ideas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("promoted_to_project", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # Create reminders table
    op.create_table(
        "reminders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.Column("task_id", sa.Integer(), nullable=True),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("due_time", sa.DateTime(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["tasks.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # Create notes table
    op.create_table(
        "notes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["projects.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # Create indexes for performance
    op.create_index("ix_tasks_project_id", "tasks", ["project_id"])
    op.create_index("ix_tasks_completed", "tasks", ["completed"])
    op.create_index("ix_tasks_due_date", "tasks", ["due_date"])
    op.create_index("ix_ideas_project_id", "ideas", ["project_id"])
    op.create_index("ix_reminders_due_time", "reminders", ["due_time"])
    op.create_index("ix_reminders_project_id", "reminders", ["project_id"])
    op.create_index("ix_reminders_task_id", "reminders", ["task_id"])
    op.create_index("ix_notes_project_id", "notes", ["project_id"])

    # Create composite indexes
    op.create_index("ix_tasks_project_completed", "tasks", ["project_id", "completed"])
    op.create_index("ix_reminders_due_project", "reminders", ["due_time", "project_id"])


def downgrade() -> None:
    """Drop initial database schema."""

    # Drop indexes
    op.drop_index("ix_reminders_due_project", table_name="reminders")
    op.drop_index("ix_tasks_project_completed", table_name="tasks")
    op.drop_index("ix_notes_project_id", table_name="notes")
    op.drop_index("ix_reminders_task_id", table_name="reminders")
    op.drop_index("ix_reminders_project_id", table_name="reminders")
    op.drop_index("ix_reminders_due_time", table_name="reminders")
    op.drop_index("ix_ideas_project_id", table_name="ideas")
    op.drop_index("ix_tasks_due_date", table_name="tasks")
    op.drop_index("ix_tasks_completed", table_name="tasks")
    op.drop_index("ix_tasks_project_id", table_name="tasks")

    # Drop tables
    op.drop_table("notes")
    op.drop_table("reminders")
    op.drop_table("ideas")
    op.drop_table("tasks")
    op.drop_table("projects")
