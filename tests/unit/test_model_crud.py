"""Unit tests for model CRUD operations.

This module provides unit tests for the CRUD operations
in the Iris application.
"""

from datetime import date, datetime, timedelta

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from iris.core.database.models import Base
from iris.core.database.services import (
    IdeaService,
    NoteService,
    ProjectService,
    ReminderService,
    TaskService,
)
from iris.core.utils.exceptions import ValidationError


class TestProjectService:
    """Test cases for ProjectService CRUD operations."""

    @pytest.fixture
    def db_session(self):
        """Create database session for testing."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        return session()

    @pytest.fixture
    def project_service(self, db_session):
        """Create project service for testing."""
        return ProjectService(db_session)

    def test_create_project(self, project_service):
        """Test creating a project."""
        project = project_service.create(
            name="Test Project", description="A test project", status="active"
        )

        assert project.name == "Test Project"
        assert project.description == "A test project"
        assert project.status == "active"
        assert project.id is not None
        assert project.created_at is not None
        assert project.updated_at is not None

    def test_create_project_validation(self, project_service):
        """Test project creation validation."""
        # Test empty name
        with pytest.raises(ValidationError, match="Project name cannot be empty"):
            project_service.create("")

        # Test invalid status
        with pytest.raises(ValidationError, match="Invalid project status"):
            project_service.create("Test", status="invalid")

    def test_get_project_by_id(self, project_service):
        """Test getting project by ID."""
        project = project_service.create("Test Project", status="active")
        project_id = project.id

        retrieved = project_service.get_by_id(project_id)
        assert retrieved is not None
        assert retrieved.name == "Test Project"
        assert retrieved.id == project_id

        # Test non-existent project
        assert project_service.get_by_id(999) is None

    def test_get_project_by_name(self, project_service):
        """Test getting project by name."""
        project_service.create("Test Project", status="active")

        retrieved = project_service.get_by_name("Test Project")
        assert retrieved is not None
        assert retrieved.name == "Test Project"

        # Test non-existent project
        assert project_service.get_by_name("Non-existent") is None

    def test_get_all_projects(self, project_service):
        """Test getting all projects."""
        # Create multiple projects
        project_service.create("Project 1", status="active")
        project_service.create("Project 2", status="completed")
        project_service.create("Project 3", status="paused")

        # Get all projects
        all_projects = project_service.get_all()
        assert len(all_projects) == 3

        # Get projects by status
        active_projects = project_service.get_all(status="active")
        assert len(active_projects) == 1
        assert active_projects[0].name == "Project 1"

        completed_projects = project_service.get_all(status="completed")
        assert len(completed_projects) == 1
        assert completed_projects[0].name == "Project 2"

    def test_update_project(self, project_service):
        """Test updating project."""
        project = project_service.create("Test Project", status="active")
        project_id = project.id

        # Update project
        updated = project_service.update(
            project_id, description="Updated description", status="completed"
        )

        assert updated is not None
        assert updated.description == "Updated description"
        assert updated.status == "completed"
        assert updated.name == "Test Project"  # Unchanged

        # Test invalid status update
        with pytest.raises(ValueError, match="Invalid project status"):
            project_service.update(project_id, status="invalid")

        # Test non-existent project
        assert project_service.update(999, status="active") is None

    def test_delete_project(self, project_service):
        """Test deleting project."""
        project = project_service.create("Test Project", status="active")
        project_id = project.id

        # Delete project
        result = project_service.delete(project_id)
        assert result is True

        # Verify project is deleted
        assert project_service.get_by_id(project_id) is None

        # Test deleting non-existent project
        assert project_service.delete(999) is False

    def test_project_statistics(self, project_service):
        """Test project statistics."""
        # Create projects with different statuses
        project_service.create("Project 1", status="active")
        project_service.create("Project 2", status="completed")
        project_service.create("Project 3", status="paused")
        project_service.create("Project 4", status="active")

        stats = project_service.get_statistics()

        assert stats["total"] == 4
        assert stats["active"] == 2
        assert stats["completed"] == 1
        assert stats["paused"] == 1


class TestTaskService:
    """Test cases for TaskService CRUD operations."""

    @pytest.fixture
    def db_session(self):
        """Create database session for testing."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        return session()

    @pytest.fixture
    def project_service(self, db_session):
        """Create project service for testing."""
        return ProjectService(db_session)

    @pytest.fixture
    def task_service(self, db_session):
        """Create task service for testing."""
        return TaskService(db_session)

    def test_create_task(self, project_service, task_service):
        """Test creating a task."""
        # Create project first
        project = project_service.create("Test Project", status="active")

        task = task_service.create(
            project_id=project.id,
            title="Test Task",
            priority="high",
            due_date=date.today() + timedelta(days=7),
            notes="Test notes",
        )

        assert task.title == "Test Task"
        assert task.priority == "high"
        assert task.completed is False
        assert task.project_id == project.id
        assert task.id is not None

    def test_create_task_validation(self, project_service, task_service):
        """Test task creation validation."""
        # Create project first
        project = project_service.create("Test Project", status="active")

        # Test empty title
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            task_service.create(project.id, "")

        # Test invalid priority
        with pytest.raises(ValueError, match="Invalid task priority"):
            task_service.create(project.id, "Test Task", priority="invalid")

        # Test non-existent project
        with pytest.raises(ValueError, match="Project with ID 999 not found"):
            task_service.create(999, "Test Task")

    def test_get_task_by_id(self, project_service, task_service):
        """Test getting task by ID."""
        project = project_service.create("Test Project", status="active")
        task = task_service.create(project.id, "Test Task", priority="medium")
        task_id = task.id

        retrieved = task_service.get_by_id(task_id)
        assert retrieved is not None
        assert retrieved.title == "Test Task"
        assert retrieved.id == task_id

        # Test non-existent task
        assert task_service.get_by_id(999) is None

    def test_get_tasks_by_project(self, project_service, task_service):
        """Test getting tasks by project."""
        project = project_service.create("Test Project", status="active")

        # Create multiple tasks
        task_service.create(project.id, "Task 1", priority="high", completed=False)
        task_service.create(project.id, "Task 2", priority="medium", completed=True)
        task_service.create(project.id, "Task 3", priority="low", completed=False)

        # Get all tasks
        all_tasks = task_service.get_by_project(project.id)
        assert len(all_tasks) == 3

        # Get completed tasks
        completed_tasks = task_service.get_by_project(project.id, completed=True)
        assert len(completed_tasks) == 1
        assert completed_tasks[0].title == "Task 2"

        # Get pending tasks
        pending_tasks = task_service.get_by_project(project.id, completed=False)
        assert len(pending_tasks) == 2

    def test_get_tasks_by_priority(self, project_service, task_service):
        """Test getting tasks by priority."""
        project = project_service.create("Test Project", status="active")

        # Create tasks with different priorities
        task_service.create(project.id, "High Task", priority="high")
        task_service.create(project.id, "Medium Task", priority="medium")
        task_service.create(project.id, "Another High Task", priority="high")

        # Get high priority tasks
        high_tasks = task_service.get_by_priority("high")
        assert len(high_tasks) == 2

        # Get medium priority tasks
        medium_tasks = task_service.get_by_priority("medium")
        assert len(medium_tasks) == 1

    def test_get_overdue_tasks(self, project_service, task_service):
        """Test getting overdue tasks."""
        project = project_service.create("Test Project", status="active")

        # Create overdue task
        overdue_date = date.today() - timedelta(days=1)
        task_service.create(project.id, "Overdue Task", priority="high", due_date=overdue_date)

        # Create future task
        future_date = date.today() + timedelta(days=1)
        task_service.create(project.id, "Future Task", priority="medium", due_date=future_date)

        # Get overdue tasks
        overdue_tasks = task_service.get_overdue()
        assert len(overdue_tasks) == 1
        assert overdue_tasks[0].title == "Overdue Task"

    def test_update_task(self, project_service, task_service):
        """Test updating task."""
        project = project_service.create("Test Project", status="active")
        task = task_service.create(project.id, "Test Task", priority="medium")
        task_id = task.id

        # Update task
        updated = task_service.update(
            task_id, title="Updated Task", priority="high", completed=True
        )

        assert updated is not None
        assert updated.title == "Updated Task"
        assert updated.priority == "high"
        assert updated.completed is True

        # Test invalid priority update
        with pytest.raises(ValueError, match="Invalid task priority"):
            task_service.update(task_id, priority="invalid")

        # Test non-existent task
        assert task_service.update(999, title="Test") is None

    def test_complete_task(self, project_service, task_service):
        """Test completing task."""
        project = project_service.create("Test Project", status="active")
        task = task_service.create(project.id, "Test Task", priority="medium")

        # Complete task
        completed = task_service.complete(task.id)
        assert completed is not None
        assert completed.completed is True

        # Uncomplete task
        uncompleted = task_service.uncomplete(task.id)
        assert uncompleted is not None
        assert uncompleted.completed is False

    def test_delete_task(self, project_service, task_service):
        """Test deleting task."""
        project = project_service.create("Test Project", status="active")
        task = task_service.create(project.id, "Test Task", priority="medium")
        task_id = task.id

        # Delete task
        result = task_service.delete(task_id)
        assert result is True

        # Verify task is deleted
        assert task_service.get_by_id(task_id) is None

        # Test deleting non-existent task
        assert task_service.delete(999) is False

    def test_task_statistics(self, project_service, task_service):
        """Test task statistics."""
        project = project_service.create("Test Project", status="active")

        # Create tasks with different priorities and completion status
        task_service.create(project.id, "High Task", priority="high", completed=True)
        task_service.create(project.id, "Medium Task", priority="medium", completed=False)
        task_service.create(project.id, "Low Task", priority="low", completed=True)
        task_service.create(project.id, "Urgent Task", priority="urgent", completed=False)

        stats = task_service.get_statistics()

        assert stats["total"] == 4
        assert stats["completed"] == 2
        assert stats["pending"] == 2
        assert stats["by_priority"]["high"] == 1
        assert stats["by_priority"]["medium"] == 1
        assert stats["by_priority"]["low"] == 1
        assert stats["by_priority"]["urgent"] == 1


class TestIdeaService:
    """Test cases for IdeaService CRUD operations."""

    @pytest.fixture
    def db_session(self):
        """Create database session for testing."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        return session()

    @pytest.fixture
    def project_service(self, db_session):
        """Create project service for testing."""
        return ProjectService(db_session)

    @pytest.fixture
    def idea_service(self, db_session):
        """Create idea service for testing."""
        return IdeaService(db_session)

    def test_create_idea(self, idea_service):
        """Test creating an idea."""
        idea = idea_service.create(title="Test Idea", description="A test idea")

        assert idea.title == "Test Idea"
        assert idea.description == "A test idea"
        assert idea.promoted_to_project is False
        assert idea.project_id is None
        assert idea.id is not None

    def test_create_idea_with_project(self, project_service, idea_service):
        """Test creating an idea with project."""
        project = project_service.create("Test Project", status="active")

        idea = idea_service.create(
            title="Test Idea", description="A test idea", project_id=project.id
        )

        assert idea.title == "Test Idea"
        assert idea.project_id == project.id
        assert idea.promoted_to_project is False

    def test_create_idea_validation(self, project_service, idea_service):
        """Test idea creation validation."""
        # Test empty title
        with pytest.raises(ValueError, match="Idea title cannot be empty"):
            idea_service.create("")

        # Test non-existent project
        with pytest.raises(ValueError, match="Project with ID 999 not found"):
            idea_service.create("Test Idea", project_id=999)

    def test_get_idea_by_id(self, idea_service):
        """Test getting idea by ID."""
        idea = idea_service.create("Test Idea", "A test idea")
        idea_id = idea.id

        retrieved = idea_service.get_by_id(idea_id)
        assert retrieved is not None
        assert retrieved.title == "Test Idea"
        assert retrieved.id == idea_id

        # Test non-existent idea
        assert idea_service.get_by_id(999) is None

    def test_get_all_ideas(self, project_service, idea_service):
        """Test getting all ideas."""
        project = project_service.create("Test Project", status="active")

        # Create ideas
        idea_service.create("Idea 1", project_id=project.id)
        idea_service.create("Idea 2", promoted_to_project=True)
        idea_service.create("Idea 3", project_id=project.id)

        # Get all ideas
        all_ideas = idea_service.get_all()
        assert len(all_ideas) == 3

        # Get ideas by project
        project_ideas = idea_service.get_all(project_id=project.id)
        assert len(project_ideas) == 2

        # Get promoted ideas
        promoted_ideas = idea_service.get_all(promoted_to_project=True)
        assert len(promoted_ideas) == 1

    def test_promote_idea_to_project(self, project_service, idea_service):
        """Test promoting idea to project."""
        idea = idea_service.create("Test Idea", "A test idea")
        idea_id = idea.id

        # Promote idea to project
        project = idea_service.promote_to_project(idea_id, "New Project", "Project description")

        assert project is not None
        assert project.name == "New Project"
        assert project.description == "Project description"
        assert project.status == "active"

        # Check that idea is updated
        updated_idea = idea_service.get_by_id(idea_id)
        assert updated_idea.project_id == project.id
        assert updated_idea.promoted_to_project is True

        # Test promoting non-existent idea
        assert idea_service.promote_to_project(999, "Test") is None

    def test_delete_idea(self, idea_service):
        """Test deleting idea."""
        idea = idea_service.create("Test Idea", "A test idea")
        idea_id = idea.id

        # Delete idea
        result = idea_service.delete(idea_id)
        assert result is True

        # Verify idea is deleted
        assert idea_service.get_by_id(idea_id) is None

        # Test deleting non-existent idea
        assert idea_service.delete(999) is False


class TestReminderService:
    """Test cases for ReminderService CRUD operations."""

    @pytest.fixture
    def db_session(self):
        """Create database session for testing."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        return session()

    @pytest.fixture
    def project_service(self, db_session):
        """Create project service for testing."""
        return ProjectService(db_session)

    @pytest.fixture
    def task_service(self, db_session):
        """Create task service for testing."""
        return TaskService(db_session)

    @pytest.fixture
    def reminder_service(self, db_session):
        """Create reminder service for testing."""
        return ReminderService(db_session)

    def test_create_reminder_with_project(self, project_service, reminder_service):
        """Test creating reminder with project."""
        project = project_service.create("Test Project", status="active")
        due_time = datetime.now() + timedelta(hours=1)

        reminder = reminder_service.create(
            message="Test reminder", due_time=due_time, project_id=project.id
        )

        assert reminder.message == "Test reminder"
        assert reminder.due_time == due_time
        assert reminder.project_id == project.id
        assert reminder.task_id is None
        assert reminder.id is not None

    def test_create_reminder_with_task(self, project_service, task_service, reminder_service):
        """Test creating reminder with task."""
        project = project_service.create("Test Project", status="active")
        task = task_service.create(project.id, "Test Task", priority="medium")
        due_time = datetime.now() + timedelta(hours=1)

        reminder = reminder_service.create(
            message="Test reminder", due_time=due_time, task_id=task.id
        )

        assert reminder.message == "Test reminder"
        assert reminder.due_time == due_time
        assert reminder.task_id == task.id
        assert reminder.project_id is None
        assert reminder.id is not None

    def test_create_reminder_validation(self, project_service, reminder_service):
        """Test reminder creation validation."""
        project = project_service.create("Test Project", status="active")
        due_time = datetime.now() + timedelta(hours=1)

        # Test empty message
        with pytest.raises(ValueError, match="Reminder message cannot be empty"):
            reminder_service.create("", due_time, project_id=project.id)

        # Test neither project_id nor task_id
        with pytest.raises(ValueError, match="Either project_id or task_id must be provided"):
            reminder_service.create("Test", due_time)

        # Test both project_id and task_id
        with pytest.raises(ValueError, match="Cannot specify both project_id and task_id"):
            reminder_service.create("Test", due_time, project_id=project.id, task_id=1)

        # Test non-existent project
        with pytest.raises(ValueError, match="Project with ID 999 not found"):
            reminder_service.create("Test", due_time, project_id=999)

    def test_get_reminder_by_id(self, project_service, reminder_service):
        """Test getting reminder by ID."""
        project = project_service.create("Test Project", status="active")
        due_time = datetime.now() + timedelta(hours=1)

        reminder = reminder_service.create("Test reminder", due_time, project_id=project.id)
        reminder_id = reminder.id

        retrieved = reminder_service.get_by_id(reminder_id)
        assert retrieved is not None
        assert retrieved.message == "Test reminder"
        assert retrieved.id == reminder_id

        # Test non-existent reminder
        assert reminder_service.get_by_id(999) is None

    def test_get_reminders_by_project(self, project_service, reminder_service):
        """Test getting reminders by project."""
        project = project_service.create("Test Project", status="active")
        due_time = datetime.now() + timedelta(hours=1)

        # Create multiple reminders
        reminder_service.create("Reminder 1", due_time, project_id=project.id)
        reminder_service.create("Reminder 2", due_time + timedelta(hours=1), project_id=project.id)

        reminders = reminder_service.get_by_project(project.id)
        assert len(reminders) == 2
        assert reminders[0].message == "Reminder 1"
        assert reminders[1].message == "Reminder 2"

    def test_get_upcoming_reminders(self, project_service, reminder_service):
        """Test getting upcoming reminders."""
        project = project_service.create("Test Project", status="active")

        # Create reminders with different due times
        reminder_service.create(
            "Past reminder", datetime.now() - timedelta(hours=1), project_id=project.id
        )

        reminder_service.create(
            "Upcoming reminder", datetime.now() + timedelta(hours=1), project_id=project.id
        )

        reminder_service.create(
            "Future reminder", datetime.now() + timedelta(hours=25), project_id=project.id
        )

        # Get upcoming reminders (next 24 hours)
        upcoming = reminder_service.get_upcoming(24)
        assert len(upcoming) == 1
        assert upcoming[0].message == "Upcoming reminder"

    def test_delete_reminder(self, project_service, reminder_service):
        """Test deleting reminder."""
        project = project_service.create("Test Project", status="active")
        due_time = datetime.now() + timedelta(hours=1)

        reminder = reminder_service.create("Test reminder", due_time, project_id=project.id)
        reminder_id = reminder.id

        # Delete reminder
        result = reminder_service.delete(reminder_id)
        assert result is True

        # Verify reminder is deleted
        assert reminder_service.get_by_id(reminder_id) is None

        # Test deleting non-existent reminder
        assert reminder_service.delete(999) is False


class TestNoteService:
    """Test cases for NoteService CRUD operations."""

    @pytest.fixture
    def db_session(self):
        """Create database session for testing."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        return session()

    @pytest.fixture
    def project_service(self, db_session):
        """Create project service for testing."""
        return ProjectService(db_session)

    @pytest.fixture
    def note_service(self, db_session):
        """Create note service for testing."""
        return NoteService(db_session)

    def test_create_note(self, note_service):
        """Test creating a note."""
        note = note_service.create("Test note content")

        assert note.content == "Test note content"
        assert note.project_id is None
        assert note.id is not None
        assert note.created_at is not None
        assert note.updated_at is not None

    def test_create_note_with_project(self, project_service, note_service):
        """Test creating note with project."""
        project = project_service.create("Test Project", status="active")

        note = note_service.create("Test note content", project_id=project.id)

        assert note.content == "Test note content"
        assert note.project_id == project.id

    def test_create_note_validation(self, project_service, note_service):
        """Test note creation validation."""
        # Test empty content
        with pytest.raises(ValueError, match="Note content cannot be empty"):
            note_service.create("")

        # Test non-existent project
        with pytest.raises(ValueError, match="Project with ID 999 not found"):
            note_service.create("Test note", project_id=999)

    def test_get_note_by_id(self, note_service):
        """Test getting note by ID."""
        note = note_service.create("Test note content")
        note_id = note.id

        retrieved = note_service.get_by_id(note_id)
        assert retrieved is not None
        assert retrieved.content == "Test note content"
        assert retrieved.id == note_id

        # Test non-existent note
        assert note_service.get_by_id(999) is None

    def test_get_notes_by_project(self, project_service, note_service):
        """Test getting notes by project."""
        project = project_service.create("Test Project", status="active")

        # Create multiple notes
        note_service.create("Note 1", project_id=project.id)
        note_service.create("Note 2", project_id=project.id)
        note_service.create("Note 3")  # No project

        # Get notes by project
        project_notes = note_service.get_by_project(project.id)
        assert len(project_notes) == 2
        # Check that we get both notes (order may vary due to same timestamp)
        note_contents = [note.content for note in project_notes]
        assert "Note 1" in note_contents
        assert "Note 2" in note_contents

    def test_get_all_notes(self, note_service):
        """Test getting all notes."""
        # Create multiple notes
        note_service.create("Note 1")
        note_service.create("Note 2")
        note_service.create("Note 3")

        all_notes = note_service.get_all()
        assert len(all_notes) == 3
        # Check that we get all three notes (order may vary due to same timestamp)
        note_contents = [note.content for note in all_notes]
        assert "Note 1" in note_contents
        assert "Note 2" in note_contents
        assert "Note 3" in note_contents

    def test_update_note(self, note_service):
        """Test updating note."""
        note = note_service.create("Original content")
        note_id = note.id

        # Update note
        updated = note_service.update(note_id, "Updated content")
        assert updated is not None
        assert updated.content == "Updated content"

        # Test empty content update
        with pytest.raises(ValueError, match="Note content cannot be empty"):
            note_service.update(note_id, "")

        # Test non-existent note
        assert note_service.update(999, "Test") is None

    def test_delete_note(self, note_service):
        """Test deleting note."""
        note = note_service.create("Test note content")
        note_id = note.id

        # Delete note
        result = note_service.delete(note_id)
        assert result is True

        # Verify note is deleted
        assert note_service.get_by_id(note_id) is None

        # Test deleting non-existent note
        assert note_service.delete(999) is False
