"""Unit tests for data validation.

This module provides unit tests for data validation
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
from iris.core.utils.exceptions import BusinessLogicError, ValidationError


class TestDataValidation:
    """Test cases for data validation."""

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
    def idea_service(self, db_session):
        """Create idea service for testing."""
        return IdeaService(db_session)

    @pytest.fixture
    def reminder_service(self, db_session):
        """Create reminder service for testing."""
        return ReminderService(db_session)

    @pytest.fixture
    def note_service(self, db_session):
        """Create note service for testing."""
        return NoteService(db_session)

    def test_project_name_validation(self, project_service):
        """Test project name validation."""
        # Test empty name
        with pytest.raises(ValidationError, match="Project name cannot be empty"):
            project_service.create("")

        # Test whitespace-only name
        with pytest.raises(ValidationError, match="Project name cannot be empty"):
            project_service.create("   ")

        # Test name with leading/trailing whitespace (should be trimmed)
        project = project_service.create("  Test Project  ")
        assert project.name == "Test Project"

    def test_project_status_validation(self, project_service):
        """Test project status validation."""
        # Test valid statuses
        for i, status in enumerate(["active", "completed", "paused"]):
            project = project_service.create(f"Test Project {i}", status=status)
            assert project.status == status

        # Test invalid status
        with pytest.raises(ValidationError, match="Invalid project status"):
            project_service.create("Test Project Invalid", status="invalid")

        # Test case sensitivity
        with pytest.raises(ValidationError, match="Invalid project status"):
            project_service.create("Test Project", status="ACTIVE")

    def test_project_unique_name_constraint(self, project_service):
        """Test project unique name constraint."""
        # Create first project
        project1 = project_service.create("Unique Project", status="active")
        assert project1.id is not None

        # Try to create second project with same name
        with pytest.raises(BusinessLogicError):
            project_service.create("Unique Project", status="active")
            project_service.session.commit()

    def test_task_title_validation(self, project_service, task_service):
        """Test task title validation."""
        project = project_service.create("Test Project", status="active")

        # Test empty title
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            task_service.create(project.id, "")

        # Test whitespace-only title
        with pytest.raises(ValueError, match="Task title cannot be empty"):
            task_service.create(project.id, "   ")

        # Test title with leading/trailing whitespace (should be trimmed)
        task = task_service.create(project.id, "  Test Task  ")
        assert task.title == "Test Task"

    def test_task_priority_validation(self, project_service, task_service):
        """Test task priority validation."""
        project = project_service.create("Test Project", status="active")

        # Test valid priorities
        for priority in ["low", "medium", "high", "urgent"]:
            task = task_service.create(project.id, "Test Task", priority=priority)
            assert task.priority == priority

        # Test invalid priority
        with pytest.raises(ValueError, match="Invalid task priority"):
            task_service.create(project.id, "Test Task", priority="invalid")

        # Test case sensitivity
        with pytest.raises(ValueError, match="Invalid task priority"):
            task_service.create(project.id, "Test Task", priority="HIGH")

    def test_task_foreign_key_validation(self, task_service):
        """Test task foreign key validation."""
        # Test non-existent project
        with pytest.raises(ValueError, match="Project with ID 999 not found"):
            task_service.create(999, "Test Task")

    def test_task_due_date_validation(self, project_service, task_service):
        """Test task due date validation."""
        project = project_service.create("Test Project", status="active")

        # Test valid due date
        due_date = date.today() + timedelta(days=7)
        task = task_service.create(project.id, "Test Task", due_date=due_date)
        assert task.due_date == due_date

        # Test past due date (should be allowed)
        past_date = date.today() - timedelta(days=1)
        task = task_service.create(project.id, "Past Task", due_date=past_date)
        assert task.due_date == past_date

        # Test None due date (should be allowed)
        task = task_service.create(project.id, "No Due Date Task")
        assert task.due_date is None

    def test_idea_title_validation(self, idea_service):
        """Test idea title validation."""
        # Test empty title
        with pytest.raises(ValueError, match="Idea title cannot be empty"):
            idea_service.create("")

        # Test whitespace-only title
        with pytest.raises(ValueError, match="Idea title cannot be empty"):
            idea_service.create("   ")

        # Test title with leading/trailing whitespace (should be trimmed)
        idea = idea_service.create("  Test Idea  ")
        assert idea.title == "Test Idea"

    def test_idea_foreign_key_validation(self, idea_service):
        """Test idea foreign key validation."""
        # Test non-existent project
        with pytest.raises(ValueError, match="Project with ID 999 not found"):
            idea_service.create("Test Idea", project_id=999)

    def test_reminder_message_validation(self, project_service, reminder_service):
        """Test reminder message validation."""
        project = project_service.create("Test Project", status="active")
        due_time = datetime.now() + timedelta(hours=1)

        # Test empty message
        with pytest.raises(ValueError, match="Reminder message cannot be empty"):
            reminder_service.create("", due_time, project_id=project.id)

        # Test whitespace-only message
        with pytest.raises(ValueError, match="Reminder message cannot be empty"):
            reminder_service.create("   ", due_time, project_id=project.id)

        # Test message with leading/trailing whitespace (should be trimmed)
        reminder = reminder_service.create("  Test Reminder  ", due_time, project_id=project.id)
        assert reminder.message == "Test Reminder"

    def test_reminder_foreign_key_validation(self, project_service, task_service, reminder_service):
        """Test reminder foreign key validation."""
        project = project_service.create("Test Project", status="active")
        task_service.create(project.id, "Test Task", priority="medium")
        due_time = datetime.now() + timedelta(hours=1)

        # Test non-existent project
        with pytest.raises(ValueError, match="Project with ID 999 not found"):
            reminder_service.create("Test Reminder", due_time, project_id=999)

        # Test non-existent task
        with pytest.raises(ValueError, match="Task with ID 999 not found"):
            reminder_service.create("Test Reminder", due_time, task_id=999)

    def test_reminder_project_task_exclusivity(
        self, project_service, task_service, reminder_service
    ):
        """Test reminder project/task exclusivity."""
        project = project_service.create("Test Project", status="active")
        task = task_service.create(project.id, "Test Task", priority="medium")
        due_time = datetime.now() + timedelta(hours=1)

        # Test neither project_id nor task_id
        with pytest.raises(ValueError, match="Either project_id or task_id must be provided"):
            reminder_service.create("Test Reminder", due_time)

        # Test both project_id and task_id
        with pytest.raises(ValueError, match="Cannot specify both project_id and task_id"):
            reminder_service.create(
                "Test Reminder", due_time, project_id=project.id, task_id=task.id
            )

    def test_note_content_validation(self, note_service):
        """Test note content validation."""
        # Test empty content
        with pytest.raises(ValueError, match="Note content cannot be empty"):
            note_service.create("")

        # Test whitespace-only content
        with pytest.raises(ValueError, match="Note content cannot be empty"):
            note_service.create("   ")

        # Test content with leading/trailing whitespace (should be trimmed)
        note = note_service.create("  Test Note Content  ")
        assert note.content == "Test Note Content"

    def test_note_foreign_key_validation(self, note_service):
        """Test note foreign key validation."""
        # Test non-existent project
        with pytest.raises(ValueError, match="Project with ID 999 not found"):
            note_service.create("Test Note", project_id=999)

    def test_string_length_validation(
        self, project_service, task_service, idea_service, note_service
    ):
        """Test string length validation."""
        project = project_service.create("Test Project", status="active")

        # Test very long strings (should be handled by database constraints)
        long_string = "x" * 1000

        # These should work (database will enforce length limits)
        try:
            task = task_service.create(project.id, long_string[:255], priority="medium")
            assert len(task.title) <= 255

            idea = idea_service.create(long_string[:255])
            assert len(idea.title) <= 255

            note = note_service.create(long_string)
            assert len(note.content) == len(long_string)
        except Exception as e:
            # If database enforces length limits, that's also valid
            assert "too long" in str(e).lower() or "length" in str(e).lower()

    def test_date_validation(self, project_service, task_service):
        """Test date validation."""
        project = project_service.create("Test Project", status="active")

        # Test valid date
        valid_date = date.today() + timedelta(days=30)
        task = task_service.create(project.id, "Test Task", due_date=valid_date)
        assert task.due_date == valid_date

        # Test edge case dates
        today = date.today()
        task = task_service.create(project.id, "Today Task", due_date=today)
        assert task.due_date == today

        # Test far future date
        future_date = date.today() + timedelta(days=365)
        task = task_service.create(project.id, "Future Task", due_date=future_date)
        assert task.due_date == future_date

    def test_datetime_validation(self, project_service, reminder_service):
        """Test datetime validation."""
        project = project_service.create("Test Project", status="active")

        # Test valid datetime
        valid_datetime = datetime.now() + timedelta(hours=1)
        reminder = reminder_service.create("Test Reminder", valid_datetime, project_id=project.id)
        assert reminder.due_time == valid_datetime

        # Test past datetime (should be allowed)
        past_datetime = datetime.now() - timedelta(hours=1)
        reminder = reminder_service.create("Past Reminder", past_datetime, project_id=project.id)
        assert reminder.due_time == past_datetime

        # Test far future datetime
        future_datetime = datetime.now() + timedelta(days=365)
        reminder = reminder_service.create(
            "Future Reminder", future_datetime, project_id=project.id
        )
        assert reminder.due_time == future_datetime

    def test_boolean_validation(self, project_service, task_service, idea_service):
        """Test boolean validation."""
        project = project_service.create("Test Project", status="active")

        # Test task completion
        task = task_service.create(project.id, "Test Task", priority="medium", completed=False)
        assert task.completed is False

        task = task_service.create(project.id, "Completed Task", priority="medium", completed=True)
        assert task.completed is True

        # Test idea promotion
        idea = idea_service.create("Test Idea", promoted_to_project=False)
        assert idea.promoted_to_project is False

        idea = idea_service.create("Promoted Idea", promoted_to_project=True)
        assert idea.promoted_to_project is True

    def test_nullable_field_validation(
        self, project_service, task_service, idea_service, note_service
    ):
        """Test nullable field validation."""
        project = project_service.create("Test Project", status="active")

        # Test optional fields
        task = task_service.create(project.id, "Test Task", priority="medium")
        assert task.due_date is None
        assert task.notes is None

        idea = idea_service.create("Test Idea")
        assert idea.description is None
        assert idea.project_id is None

        note = note_service.create("Test Note")
        assert note.project_id is None

        # Test with optional fields
        task = task_service.create(
            project.id, "Task with Notes", priority="medium", notes="Some notes"
        )
        assert task.notes == "Some notes"

        idea = idea_service.create("Idea with Description", description="Some description")
        assert idea.description == "Some description"

        note = note_service.create("Note with Project", project_id=project.id)
        assert note.project_id == project.id

    def test_relationship_validation(
        self, project_service, task_service, idea_service, reminder_service, note_service
    ):
        """Test relationship validation."""
        project = project_service.create("Test Project", status="active")
        task = task_service.create(project.id, "Test Task", priority="medium")

        # Test valid relationships
        idea = idea_service.create("Test Idea", project_id=project.id)
        assert idea.project_id == project.id

        reminder = reminder_service.create(
            "Test Reminder", datetime.now() + timedelta(hours=1), project_id=project.id
        )
        assert reminder.project_id == project.id

        task_reminder = reminder_service.create(
            "Task Reminder", datetime.now() + timedelta(hours=1), task_id=task.id
        )
        assert task_reminder.task_id == task.id

        note = note_service.create("Test Note", project_id=project.id)
        assert note.project_id == project.id

        # Test cascade relationships
        project_notes = note_service.get_by_project(project.id)
        assert len(project_notes) == 1
        assert project_notes[0].content == "Test Note"

        project_ideas = idea_service.get_all(project_id=project.id)
        assert len(project_ideas) == 1
        assert project_ideas[0].title == "Test Idea"
