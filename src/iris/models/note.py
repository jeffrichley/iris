"""Note entity model.

Per FR-009: Notes table for project-attached text content.
"""

from uuid import UUID

from sqlmodel import Field

from iris.models.base import BaseModel


class Note(BaseModel, table=True):
    """Note entity for project-attached text content.
    
    Free-form text notes attached to projects.
    
    Fields:
        id: UUID primary key (inherited)
        user_id: Owner UUID (inherited, denormalized for RLS)
        project_id: Parent project UUID
        content: Note text (required, non-empty)
        created_at: Creation timestamp (inherited)
        updated_at: Last update timestamp (inherited)
    
    Relationships:
        - Many notes → one project
    
    Business Rules:
        - Deleting project cascades to delete notes
        - Notes support updates (mutable)
        - Future: Full-text search on content
    """
    
    __tablename__ = "notes"
    
    project_id: UUID = Field(
        foreign_key="projects.id",
        nullable=False,
        index=True,
        description="Parent project UUID"
    )
    
    content: str = Field(
        min_length=1,
        nullable=False,
        description="Note text content (non-empty)"
    )

