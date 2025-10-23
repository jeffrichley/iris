"""SQLAlchemy models for Iris project management system.

This module provides SQLAlchemy models for all database entities
in the Iris application.
"""

from datetime import date, datetime
from typing import Any, Optional

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    event,
)
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.sql import func

Base = declarative_base()


# Type alias for Base class to help mypy
BaseType = type[Base]  # type: ignore[valid-type]


class Project(Base):  # type: ignore[valid-type,misc]
    """Project entity representing individual projects in the Iris system."""

    __tablename__ = "projects"

    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Basic fields
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), nullable=False)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    # Relationships
    tasks: Mapped[list["Task"]] = relationship(
        "Task", back_populates="project", cascade="all, delete-orphan"
    )
    notes: Mapped[list["Note"]] = relationship(
        "Note", back_populates="project", cascade="all, delete-orphan"
    )
    reminders: Mapped[list["Reminder"]] = relationship(
        "Reminder", back_populates="project", cascade="all, delete-orphan"
    )
    ideas: Mapped[list["Idea"]] = relationship(
        "Idea", back_populates="project", cascade="all, delete-orphan"
    )

    # Constraints
    __table_args__ = (
        CheckConstraint("status IN ('active', 'completed', 'paused')", name="ck_projects_status"),
    )

    def __repr__(self) -> str:
        return f"<Project(id={self.id}, name='{self.name}', status='{self.status}')>"


class Task(Base):  # type: ignore[valid-type,misc]
    """Task entity representing work items belonging to projects."""

    __tablename__ = "tasks"

    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Foreign key
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("projects.id"), nullable=False)

    # Basic fields
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    priority: Mapped[str] = mapped_column(String(50), nullable=False)
    due_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    # Relationships
    project: Mapped["Project"] = relationship("Project", back_populates="tasks")
    reminders: Mapped[list["Reminder"]] = relationship(
        "Reminder", back_populates="task", cascade="all, delete-orphan"
    )

    # Constraints
    __table_args__ = (
        CheckConstraint(
            "priority IN ('low', 'medium', 'high', 'urgent')", name="ck_tasks_priority"
        ),
        CheckConstraint("completed IN (TRUE, FALSE)", name="ck_tasks_completed"),
        Index("ix_tasks_project_id", "project_id"),
        Index("ix_tasks_completed", "completed"),
        Index("ix_tasks_due_date", "due_date"),
        Index("ix_tasks_project_completed", "project_id", "completed"),
    )

    def __repr__(self) -> str:
        return (
            f"<Task(id={self.id}, title='{self.title}', priority='{self.priority}', "
            f"completed={self.completed})>"
        )


class Idea(Base):  # type: ignore[valid-type,misc]
    """Idea entity representing spontaneous ideas that may become projects."""

    __tablename__ = "ideas"

    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Foreign key (optional)
    project_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("projects.id"), nullable=True
    )

    # Basic fields
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    promoted_to_project: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())

    # Relationships
    project: Mapped[Optional["Project"]] = relationship("Project", back_populates="ideas")

    # Constraints
    __table_args__ = (
        CheckConstraint("promoted_to_project IN (TRUE, FALSE)", name="ck_ideas_promoted"),
        Index("ix_ideas_project_id", "project_id"),
    )

    def __repr__(self) -> str:
        return f"<Idea(id={self.id}, title='{self.title}', promoted={self.promoted_to_project})>"


class Reminder(Base):  # type: ignore[valid-type,misc]
    """Reminder entity representing notifications for tasks or projects."""

    __tablename__ = "reminders"

    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Foreign keys (one must be provided)
    project_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("projects.id"), nullable=True
    )
    task_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("tasks.id"), nullable=True)

    # Basic fields
    message: Mapped[str] = mapped_column(Text, nullable=False)
    due_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())

    # Relationships
    project: Mapped[Optional["Project"]] = relationship("Project", back_populates="reminders")
    task: Mapped[Optional["Task"]] = relationship("Task", back_populates="reminders")

    # Constraints
    __table_args__ = (
        Index("ix_reminders_due_time", "due_time"),
        Index("ix_reminders_project_id", "project_id"),
        Index("ix_reminders_task_id", "task_id"),
        Index("ix_reminders_due_project", "due_time", "project_id"),
    )

    def __repr__(self) -> str:
        message_preview = self.message[:50] + "..." if len(self.message) > 50 else self.message
        return f"<Reminder(id={self.id}, message='{message_preview}', due_time={self.due_time})>"


class Note(Base):  # type: ignore[valid-type,misc]
    """Note entity representing free-form notes tied to projects."""

    __tablename__ = "notes"

    # Primary key
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # Foreign key (optional)
    project_id: Mapped[int | None] = mapped_column(
        Integer, ForeignKey("projects.id"), nullable=True
    )

    # Basic fields
    content: Mapped[str] = mapped_column(Text, nullable=False)

    # Timestamps
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=func.now(), onupdate=func.now()
    )

    # Relationships
    project: Mapped[Optional["Project"]] = relationship("Project", back_populates="notes")

    # Constraints
    __table_args__ = (Index("ix_notes_project_id", "project_id"),)

    def __repr__(self) -> str:
        content_preview = self.content[:50] + "..." if len(self.content) > 50 else self.content
        return f"<Note(id={self.id}, content='{content_preview}', project_id={self.project_id})>"


# Event listeners for automatic timestamp updates
@event.listens_for(Project, "before_update")
@event.listens_for(Task, "before_update")
@event.listens_for(Note, "before_update")
def update_timestamp(mapper: Any, connection: Any, target: Any) -> None:
    """Update the updated_at timestamp before any update operation."""
    target.updated_at = datetime.now()
