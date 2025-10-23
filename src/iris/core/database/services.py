"""Database service layer for Iris project management system.

This module provides CRUD operations and business logic for all database entities
in the Iris application.
"""

from datetime import date, datetime
from typing import Any

from sqlalchemy import and_, asc, desc
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from iris.core.database.models import Idea, Note, Project, Reminder, Task
from iris.core.utils.error_handler import handle_errors
from iris.core.utils.exceptions import BusinessLogicError, DatabaseError, ValidationError


class ProjectService:
    """Service class for Project entity CRUD operations."""

    def __init__(self, session: Session):
        """Initialize project service.

        Args:
            session: Database session
        """
        self.session = session

    @handle_errors(reraise=True, context={"operation": "create_project"})
    def create(self, name: str, description: str | None = None, status: str = "active") -> Project:
        """Create a new project.

        Args:
            name: Project name
            description: Project description
            status: Project status

        Returns:
            Created project instance

        Raises:
            ValidationError: If project name is empty or invalid
            BusinessLogicError: If project already exists
            DatabaseError: If database operation fails
        """
        if not name or not name.strip():
            raise ValidationError(message="Project name cannot be empty", field="name", value=name)

        if status not in ["active", "completed", "paused"]:
            raise ValidationError(
                message=f"Invalid project status: {status}",
                field="status",
                value=status,
                expected_type="active, completed, or paused",
            )

        # Check if project already exists
        existing_project = self.session.query(Project).filter_by(name=name.strip()).first()
        if existing_project:
            raise BusinessLogicError(
                message=f"Project with name '{name}' already exists",
                operation="create_project",
                entity_id=str(existing_project.id),
            )

        try:
            project = Project(
                name=name.strip(),
                description=description.strip() if description else None,
                status=status,
            )

            self.session.add(project)
            self.session.flush()
            return project
        except SQLAlchemyError as e:
            raise DatabaseError(
                message=f"Failed to create project: {str(e)}",
                error_code="PROJECT_CREATE_ERROR",
                original_exception=e,
            ) from e

    def get_by_id(self, project_id: int) -> Project | None:
        """Get project by ID.

        Args:
            project_id: Project ID

        Returns:
            Project instance or None if not found
        """
        return self.session.query(Project).filter_by(id=project_id).first()

    def get_by_name(self, name: str) -> Project | None:
        """Get project by name.

        Args:
            name: Project name

        Returns:
            Project instance or None if not found
        """
        return self.session.query(Project).filter_by(name=name).first()

    def get_all(self, status: str | None = None) -> list[Project]:
        """Get all projects.

        Args:
            status: Filter by status (optional)

        Returns:
            List of project instances
        """
        query = self.session.query(Project)
        if status:
            query = query.filter_by(status=status)
        return query.order_by(asc(Project.created_at)).all()

    def update(self, project_id: int, **kwargs: Any) -> Project | None:
        """Update project.

        Args:
            project_id: Project ID
            **kwargs: Fields to update

        Returns:
            Updated project instance or None if not found

        Raises:
            ValueError: If invalid field values
        """
        project = self.get_by_id(project_id)
        if not project:
            return None

        # Validate status if provided
        if "status" in kwargs and kwargs["status"] not in ["active", "completed", "paused"]:
            raise ValueError(f"Invalid project status: {kwargs['status']}")

        # Update fields
        for field, value in kwargs.items():
            if hasattr(project, field):
                setattr(project, field, value)

        self.session.flush()
        return project

    def delete(self, project_id: int) -> bool:
        """Delete project.

        Args:
            project_id: Project ID

        Returns:
            True if deleted, False if not found
        """
        project = self.get_by_id(project_id)
        if not project:
            return False

        self.session.delete(project)
        self.session.flush()
        return True

    def get_statistics(self) -> dict[str, Any]:
        """Get project statistics.

        Returns:
            Dictionary with project statistics
        """
        total = self.session.query(Project).count()
        active = self.session.query(Project).filter_by(status="active").count()
        completed = self.session.query(Project).filter_by(status="completed").count()
        paused = self.session.query(Project).filter_by(status="paused").count()

        return {"total": total, "active": active, "completed": completed, "paused": paused}


class TaskService:
    """Service class for Task entity CRUD operations."""

    def __init__(self, session: Session):
        """Initialize task service.

        Args:
            session: Database session
        """
        self.session = session

    def create(
        self,
        project_id: int,
        title: str,
        priority: str = "medium",
        due_date: date | None = None,
        notes: str | None = None,
        completed: bool = False,
    ) -> Task:
        """Create a new task.

        Args:
            project_id: Parent project ID
            title: Task title
            priority: Task priority
            due_date: Task due date
            notes: Task notes

        Returns:
            Created task instance

        Raises:
            ValueError: If invalid parameters
            SQLAlchemyError: If database operation fails
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        if priority not in ["low", "medium", "high", "urgent"]:
            raise ValueError(f"Invalid task priority: {priority}")

        # Verify project exists
        project = self.session.query(Project).filter_by(id=project_id).first()
        if not project:
            raise ValueError(f"Project with ID {project_id} not found")

        task = Task(
            project_id=project_id,
            title=title.strip(),
            priority=priority,
            due_date=due_date,
            notes=notes.strip() if notes else None,
            completed=completed,
        )

        self.session.add(task)
        self.session.flush()
        return task

    def get_by_id(self, task_id: int) -> Task | None:
        """Get task by ID.

        Args:
            task_id: Task ID

        Returns:
            Task instance or None if not found
        """
        return self.session.query(Task).filter_by(id=task_id).first()

    def get_by_project(self, project_id: int, completed: bool | None = None) -> list[Task]:
        """Get tasks by project.

        Args:
            project_id: Project ID
            completed: Filter by completion status (optional)

        Returns:
            List of task instances
        """
        query = self.session.query(Task).filter_by(project_id=project_id)
        if completed is not None:
            query = query.filter_by(completed=completed)
        return query.order_by(asc(Task.created_at)).all()

    def get_by_priority(self, priority: str) -> list[Task]:
        """Get tasks by priority.

        Args:
            priority: Task priority

        Returns:
            List of task instances
        """
        return (
            self.session.query(Task)
            .filter_by(priority=priority)
            .order_by(asc(Task.created_at))
            .all()
        )

    def get_overdue(self) -> list[Task]:
        """Get overdue tasks.

        Returns:
            List of overdue task instances
        """
        today = date.today()
        return (
            self.session.query(Task)
            .filter(and_(Task.due_date < today, ~Task.completed))
            .order_by(asc(Task.due_date))
            .all()
        )

    def update(self, task_id: int, **kwargs: Any) -> Task | None:
        """Update task.

        Args:
            task_id: Task ID
            **kwargs: Fields to update

        Returns:
            Updated task instance or None if not found

        Raises:
            ValueError: If invalid field values
        """
        task = self.get_by_id(task_id)
        if not task:
            return None

        # Validate priority if provided
        if "priority" in kwargs and kwargs["priority"] not in ["low", "medium", "high", "urgent"]:
            raise ValueError(f"Invalid task priority: {kwargs['priority']}")

        # Update fields
        for field, value in kwargs.items():
            if hasattr(task, field):
                setattr(task, field, value)

        self.session.flush()
        return task

    def complete(self, task_id: int) -> Task | None:
        """Mark task as completed.

        Args:
            task_id: Task ID

        Returns:
            Updated task instance or None if not found
        """
        return self.update(task_id, completed=True)

    def uncomplete(self, task_id: int) -> Task | None:
        """Mark task as not completed.

        Args:
            task_id: Task ID

        Returns:
            Updated task instance or None if not found
        """
        return self.update(task_id, completed=False)

    def delete(self, task_id: int) -> bool:
        """Delete task.

        Args:
            task_id: Task ID

        Returns:
            True if deleted, False if not found
        """
        task = self.get_by_id(task_id)
        if not task:
            return False

        self.session.delete(task)
        self.session.flush()
        return True

    def get_statistics(self) -> dict[str, Any]:
        """Get task statistics.

        Returns:
            Dictionary with task statistics
        """
        total = self.session.query(Task).count()
        completed = self.session.query(Task).filter_by(completed=True).count()
        pending = total - completed

        by_priority = {}
        for priority in ["low", "medium", "high", "urgent"]:
            by_priority[priority] = self.session.query(Task).filter_by(priority=priority).count()

        return {
            "total": total,
            "completed": completed,
            "pending": pending,
            "by_priority": by_priority,
        }


class IdeaService:
    """Service class for Idea entity CRUD operations."""

    def __init__(self, session: Session):
        """Initialize idea service.

        Args:
            session: Database session
        """
        self.session = session

    def create(
        self,
        title: str,
        description: str | None = None,
        project_id: int | None = None,
        promoted_to_project: bool = False,
    ) -> Idea:
        """Create a new idea.

        Args:
            title: Idea title
            description: Idea description
            project_id: Associated project ID (optional)

        Returns:
            Created idea instance

        Raises:
            ValueError: If invalid parameters
            SQLAlchemyError: If database operation fails
        """
        if not title or not title.strip():
            raise ValueError("Idea title cannot be empty")

        # Verify project exists if provided
        if project_id:
            project = self.session.query(Project).filter_by(id=project_id).first()
            if not project:
                raise ValueError(f"Project with ID {project_id} not found")

        idea = Idea(
            title=title.strip(),
            description=description.strip() if description else None,
            project_id=project_id,
            promoted_to_project=promoted_to_project,
        )

        self.session.add(idea)
        self.session.flush()
        return idea

    def get_by_id(self, idea_id: int) -> Idea | None:
        """Get idea by ID.

        Args:
            idea_id: Idea ID

        Returns:
            Idea instance or None if not found
        """
        return self.session.query(Idea).filter_by(id=idea_id).first()

    def get_all(
        self,
        project_id: int | None = None,
        promoted: bool | None = None,
        promoted_to_project: bool | None = None,
    ) -> list[Idea]:
        """Get all ideas.

        Args:
            project_id: Filter by project ID (optional)
            promoted: Filter by promotion status (optional, deprecated)
            promoted_to_project: Filter by promotion status (optional)

        Returns:
            List of idea instances
        """
        query = self.session.query(Idea)
        if project_id:
            query = query.filter_by(project_id=project_id)
        # Support both parameter names for backward compatibility
        promotion_filter = promoted_to_project if promoted_to_project is not None else promoted
        if promotion_filter is not None:
            query = query.filter_by(promoted_to_project=promotion_filter)
        return query.order_by(desc(Idea.created_at)).all()

    def promote_to_project(
        self, idea_id: int, project_name: str, project_description: str | None = None
    ) -> Project | None:
        """Promote idea to project.

        Args:
            idea_id: Idea ID
            project_name: Name for the new project
            project_description: Description for the new project

        Returns:
            Created project instance or None if idea not found
        """
        idea = self.get_by_id(idea_id)
        if not idea:
            return None

        # Create project
        project_service = ProjectService(self.session)
        project: Project = project_service.create(
            name=project_name, description=project_description, status="active"
        )

        # Update idea
        idea.project_id = project.id
        idea.promoted_to_project = True

        self.session.flush()
        return project

    def delete(self, idea_id: int) -> bool:
        """Delete idea.

        Args:
            idea_id: Idea ID

        Returns:
            True if deleted, False if not found
        """
        idea = self.get_by_id(idea_id)
        if not idea:
            return False

        self.session.delete(idea)
        self.session.flush()
        return True


class ReminderService:
    """Service class for Reminder entity CRUD operations."""

    def __init__(self, session: Session):
        """Initialize reminder service.

        Args:
            session: Database session
        """
        self.session = session

    def create(
        self,
        message: str,
        due_time: datetime,
        project_id: int | None = None,
        task_id: int | None = None,
    ) -> Reminder:
        """Create a new reminder.

        Args:
            message: Reminder message
            due_time: Reminder due time
            project_id: Associated project ID (optional)
            task_id: Associated task ID (optional)

        Returns:
            Created reminder instance

        Raises:
            ValueError: If invalid parameters
            SQLAlchemyError: If database operation fails
        """
        if not message or not message.strip():
            raise ValueError("Reminder message cannot be empty")

        if not project_id and not task_id:
            raise ValueError("Either project_id or task_id must be provided")

        if project_id and task_id:
            raise ValueError("Cannot specify both project_id and task_id")

        # Verify project exists if provided
        if project_id:
            project = self.session.query(Project).filter_by(id=project_id).first()
            if not project:
                raise ValueError(f"Project with ID {project_id} not found")

        # Verify task exists if provided
        if task_id:
            task = self.session.query(Task).filter_by(id=task_id).first()
            if not task:
                raise ValueError(f"Task with ID {task_id} not found")

        reminder = Reminder(
            message=message.strip(), due_time=due_time, project_id=project_id, task_id=task_id
        )

        self.session.add(reminder)
        self.session.flush()
        return reminder

    def get_by_id(self, reminder_id: int) -> Reminder | None:
        """Get reminder by ID.

        Args:
            reminder_id: Reminder ID

        Returns:
            Reminder instance or None if not found
        """
        return self.session.query(Reminder).filter_by(id=reminder_id).first()

    def get_by_project(self, project_id: int) -> list[Reminder]:
        """Get reminders by project.

        Args:
            project_id: Project ID

        Returns:
            List of reminder instances
        """
        return (
            self.session.query(Reminder)
            .filter_by(project_id=project_id)
            .order_by(asc(Reminder.due_time))
            .all()
        )

    def get_by_task(self, task_id: int) -> list[Reminder]:
        """Get reminders by task.

        Args:
            task_id: Task ID

        Returns:
            List of reminder instances
        """
        return (
            self.session.query(Reminder)
            .filter_by(task_id=task_id)
            .order_by(asc(Reminder.due_time))
            .all()
        )

    def get_upcoming(self, hours: int = 24) -> list[Reminder]:
        """Get upcoming reminders.

        Args:
            hours: Hours ahead to look for reminders

        Returns:
            List of upcoming reminder instances
        """
        from datetime import timedelta

        now = datetime.now()
        cutoff_time = now + timedelta(hours=hours)

        return (
            self.session.query(Reminder)
            .filter(Reminder.due_time > now, Reminder.due_time <= cutoff_time)
            .order_by(asc(Reminder.due_time))
            .all()
        )

    def delete(self, reminder_id: int) -> bool:
        """Delete reminder.

        Args:
            reminder_id: Reminder ID

        Returns:
            True if deleted, False if not found
        """
        reminder = self.get_by_id(reminder_id)
        if not reminder:
            return False

        self.session.delete(reminder)
        self.session.flush()
        return True


class NoteService:
    """Service class for Note entity CRUD operations."""

    def __init__(self, session: Session):
        """Initialize note service.

        Args:
            session: Database session
        """
        self.session = session

    def create(self, content: str, project_id: int | None = None) -> Note:
        """Create a new note.

        Args:
            content: Note content
            project_id: Associated project ID (optional)

        Returns:
            Created note instance

        Raises:
            ValueError: If invalid parameters
            SQLAlchemyError: If database operation fails
        """
        if not content or not content.strip():
            raise ValueError("Note content cannot be empty")

        # Verify project exists if provided
        if project_id:
            project = self.session.query(Project).filter_by(id=project_id).first()
            if not project:
                raise ValueError(f"Project with ID {project_id} not found")

        note = Note(content=content.strip(), project_id=project_id)

        self.session.add(note)
        self.session.flush()
        return note

    def get_by_id(self, note_id: int) -> Note | None:
        """Get note by ID.

        Args:
            note_id: Note ID

        Returns:
            Note instance or None if not found
        """
        return self.session.query(Note).filter_by(id=note_id).first()

    def get_by_project(self, project_id: int) -> list[Note]:
        """Get notes by project.

        Args:
            project_id: Project ID

        Returns:
            List of note instances
        """
        return (
            self.session.query(Note)
            .filter_by(project_id=project_id)
            .order_by(desc(Note.created_at))
            .all()
        )

    def get_all(self) -> list[Note]:
        """Get all notes.

        Returns:
            List of note instances
        """
        return self.session.query(Note).order_by(desc(Note.created_at)).all()

    def update(self, note_id: int, content: str) -> Note | None:
        """Update note content.

        Args:
            note_id: Note ID
            content: New note content

        Returns:
            Updated note instance or None if not found

        Raises:
            ValueError: If content is empty
        """
        if not content or not content.strip():
            raise ValueError("Note content cannot be empty")

        note = self.get_by_id(note_id)
        if not note:
            return None

        note.content = content.strip()
        self.session.flush()
        return note

    def delete(self, note_id: int) -> bool:
        """Delete note.

        Args:
            note_id: Note ID

        Returns:
            True if deleted, False if not found
        """
        note = self.get_by_id(note_id)
        if not note:
            return False

        self.session.delete(note)
        self.session.flush()
        return True
