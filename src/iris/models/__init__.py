"""Data models for Iris using SQLModel.

All models extend BaseModel which provides common fields:
- id (UUID primary key)
- user_id (UUID foreign key for RLS)
- created_at, updated_at (timestamps)
"""

from iris.models.base import BaseModel
from iris.models.idea import Idea
from iris.models.note import Note
from iris.models.project import Project, ProjectStatus
from iris.models.reminder import Reminder
from iris.models.task import Task, TaskPriority

__all__ = [
    "BaseModel",
    "Project",
    "ProjectStatus",
    "Task",
    "TaskPriority",
    "Idea",
    "Reminder",
    "Note",
]

