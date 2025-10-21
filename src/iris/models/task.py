"""Task entity model.

Per FR-006: Tasks table with user isolation and project linking.
"""

from datetime import datetime
from enum import Enum
from uuid import UUID

from sqlmodel import Field

from iris.models.base import BaseModel


class TaskPriority(str, Enum):
    """Task priority enumeration."""
    
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class Task(BaseModel, table=True):
    """Task entity with user isolation and project linking.
    
    Represents a work item belonging to a project.
    
    Fields:
        id: UUID primary key (inherited)
        user_id: Owner UUID (inherited, denormalized for RLS performance)
        project_id: Parent project UUID
        title: Task description (1-500 chars)
        priority: Task priority (high/medium/low)
        due_date: Optional deadline
        completed: Completion status (default false)
        completed_at: Auto-set when completed=true (via trigger)
        notes: Optional task details
        created_at: Creation timestamp (inherited)
        updated_at: Last update timestamp (inherited)
    
    Relationships:
        - Many tasks → one project
        - One task → many reminders (optional)
    
    Business Rules:
        - Deleting project cascades to delete tasks
        - Marking complete auto-sets completed_at via database trigger
    """
    
    __tablename__ = "tasks"
    
    project_id: UUID = Field(
        foreign_key="projects.id",
        nullable=False,
        index=True,
        description="Parent project UUID"
    )
    
    title: str = Field(
        max_length=500,
        min_length=1,
        nullable=False,
        description="Task description (1-500 characters)"
    )
    
    priority: TaskPriority = Field(
        default=TaskPriority.MEDIUM,
        description="Task priority level"
    )
    
    due_date: datetime | None = Field(
        default=None,
        description="Optional task deadline"
    )
    
    completed: bool = Field(
        default=False,
        nullable=False,
        description="Task completion status"
    )
    
    completed_at: datetime | None = Field(
        default=None,
        description="Completion timestamp (auto-set by trigger)"
    )
    
    notes: str | None = Field(
        default=None,
        description="Optional task notes"
    )

