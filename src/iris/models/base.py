"""Base SQLModel with common fields for all entities.

Compliant with Constitution Principle 1: Type Safety First
All code uses type hints, no Any allowed.

Per FR-010: All tables MUST include user_id for Row Level Security.
"""

from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class BaseModel(SQLModel):
    """Base model with common fields for all entities.
    
    Provides:
    - UUID primary key (auto-generated)
    - user_id for Row Level Security (FR-010)
    - created_at timestamp (auto-set)
    - updated_at timestamp (auto-updated)
    
    All entities must extend this base model to ensure consistent
    user isolation and timestamp tracking.
    """

    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False,
        description="Unique identifier (UUID v4)"
    )

    user_id: UUID = Field(
        foreign_key="auth.users.id",
        nullable=False,
        index=True,  # Indexed for RLS performance (FR-012)
        description="Owner user ID (foreign key to auth.users)"
    )

    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": "NOW()"},
        description="Record creation timestamp (UTC)"
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": "NOW()",
            "onupdate": "NOW()"
        },
        description="Record last update timestamp (UTC)"
    )

    class Config:
        """SQLModel configuration."""
        
        # Use PostgreSQL column types
        arbitrary_types_allowed = True
        # Validate on assignment
        validate_assignment = True

