"""Project entity model.

Per FR-005: Projects table with user isolation.
Compliant with Constitution Principle 1: Type Safety (Enums for status).
"""

from enum import Enum

from sqlmodel import Field

from iris.models.base import BaseModel


class ProjectStatus(str, Enum):
    """Project status enumeration.
    
    Compliant with Constitution: Enums for static values, no magic strings.
    """
    
    ACTIVE = "active"
    ARCHIVED = "archived"
    COMPLETED = "completed"


class Project(BaseModel, table=True):
    """Project entity with user isolation via RLS.
    
    Represents a user's organizational container for tasks and notes.
    
    Fields:
        id: UUID primary key (inherited from BaseModel)
        user_id: Owner UUID (inherited from BaseModel, indexed for RLS)
        name: Project name (1-255 chars, required)
        description: Optional project details
        status: Project status (active/archived/completed)
        created_at: Creation timestamp (inherited from BaseModel)
        updated_at: Last update timestamp (inherited from BaseModel)
    
    Relationships:
        - One project → many tasks
        - One project → many notes
        - One project ← optional idea promotion
    
    RLS: Row Level Security enforced via auth.uid() = user_id
    """
    
    __tablename__ = "projects"
    
    name: str = Field(
        max_length=255,
        min_length=1,
        nullable=False,
        description="Project name (1-255 characters)"
    )
    
    description: str | None = Field(
        default=None,
        description="Optional project description"
    )
    
    status: ProjectStatus = Field(
        default=ProjectStatus.ACTIVE,
        description="Project status (active/archived/completed)"
    )

