"""Idea entity model.

Per FR-007: Ideas table for spontaneous idea capture.
"""

from uuid import UUID

from sqlmodel import Field

from iris.models.base import BaseModel


class Idea(BaseModel, table=True):
    """Idea entity for capturing spontaneous thoughts.
    
    Ideas can be promoted to projects via promoted_to_project_id link.
    
    Fields:
        id: UUID primary key (inherited)
        user_id: Owner UUID (inherited)
        title: Idea summary (1-255 chars)
        description: Optional detailed description
        promoted_to_project_id: Optional link to created project
        created_at: Capture timestamp (inherited)
    
    Relationships:
        - Many ideas → optional one project (when promoted)
    
    Business Rules:
        - Ideas are immutable after creation (no updated_at)
        - Promoting sets promoted_to_project_id
        - Deleting promoted project sets link to NULL
    """
    
    __tablename__ = "ideas"
    
    title: str = Field(
        max_length=255,
        min_length=1,
        nullable=False,
        description="Idea summary (1-255 characters)"
    )
    
    description: str | None = Field(
        default=None,
        description="Optional idea details"
    )
    
    promoted_to_project_id: UUID | None = Field(
        default=None,
        foreign_key="projects.id",
        description="Project UUID if idea was promoted"
    )
    
    # Override to remove updated_at (ideas are immutable)
    class Config:
        """SQLModel configuration for ideas."""
        table = True

