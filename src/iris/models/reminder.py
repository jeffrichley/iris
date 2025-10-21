"""Reminder entity model.

Per FR-008: Reminders table for time-based notifications.
"""

from datetime import datetime
from uuid import UUID

from sqlmodel import Field

from iris.models.base import BaseModel


class Reminder(BaseModel, table=True):
    """Reminder entity for time-based notifications.
    
    Reminders can be standalone or linked to a task.
    
    Fields:
        id: UUID primary key (inherited)
        user_id: Owner UUID (inherited)
        task_id: Optional task link
        message: Reminder content (required, non-empty)
        due_time: When to trigger notification (required)
        created_at: Creation timestamp (inherited)
    
    Relationships:
        - Many reminders → optional one task
    
    Business Rules:
        - Reminders can exist without task_id (standalone)
        - Deleting task cascades to delete linked reminders
        - Past reminders retained for history
    """
    
    __tablename__ = "reminders"
    
    task_id: UUID | None = Field(
        default=None,
        foreign_key="tasks.id",
        description="Optional task link"
    )
    
    message: str = Field(
        min_length=1,
        nullable=False,
        description="Reminder message (non-empty)"
    )
    
    due_time: datetime = Field(
        nullable=False,
        description="When to trigger notification"
    )
    
    # Override to remove updated_at (reminders are immutable)
    class Config:
        """SQLModel configuration for reminders."""
        table = True

