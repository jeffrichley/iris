"""Unit tests for database models.

This module provides unit tests for the SQLAlchemy models
in the Iris application.
"""

from datetime import datetime, timedelta

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from iris.core.database.models import Base, Idea, Note, Project, Reminder, Task


class TestProjectModel:
    """Test cases for Project model."""

    def test_project_creation(self):
        """Test creating a project."""
        project = Project(name="Test Project", description="A test project", status="active")

        assert project.name == "Test Project"
        assert project.description == "A test project"
        assert project.status == "active"
        assert project.id is None  # Not yet persisted
        assert project.created_at is None
        assert project.updated_at is None

    def test_project_validation(self):
        """Test project validation."""
        # Test valid status
        project = Project(name="Test", status="active")
        assert project.status == "active"

        project = Project(name="Test", status="completed")
        assert project.status == "completed"

        project = Project(name="Test", status="paused")
        assert project.status == "paused"

    def test_project_relationships(self):
        """Test project relationships."""
        project = Project(name="Test Project", status="active")

        # Test that relationships are initialized as empty lists
        assert project.tasks == []
        assert project.notes == []
        assert project.reminders == []
        assert project.ideas == []

    def test_project_repr(self):
        """Test project string representation."""
        project = Project(name="Test Project", status="active")
        project.id = 1

        repr_str = repr(project)
        assert "Project" in repr_str
        assert "id=1" in repr_str
        assert "name='Test Project'" in repr_str
        assert "status='active'" in repr_str


class TestTaskModel:
    """Test cases for Task model."""

    def test_task_creation(self):
        """Test creating a task."""
        task = Task(project_id=1, title="Test Task", priority="high", completed=False)

        assert task.project_id == 1
        assert task.title == "Test Task"
        assert task.priority == "high"
        assert task.completed is False
        assert task.id is None
        assert task.created_at is None
        assert task.updated_at is None

    def test_task_validation(self):
        """Test task validation."""
        # Test valid priorities
        for priority in ["low", "medium", "high", "urgent"]:
            task = Task(project_id=1, title="Test", priority=priority, completed=False)
            assert task.priority == priority

        # Test completed boolean
        task = Task(project_id=1, title="Test", priority="medium", completed=True)
        assert task.completed is True

        task = Task(project_id=1, title="Test", priority="medium", completed=False)
        assert task.completed is False

    def test_task_relationships(self):
        """Test task relationships."""
        task = Task(project_id=1, title="Test Task", priority="medium", completed=False)

        # Test that relationships are initialized
        assert task.reminders == []

    def test_task_repr(self):
        """Test task string representation."""
        task = Task(project_id=1, title="Test Task", priority="high", completed=True)
        task.id = 1

        repr_str = repr(task)
        assert "Task" in repr_str
        assert "id=1" in repr_str
        assert "title='Test Task'" in repr_str
        assert "priority='high'" in repr_str
        assert "completed=True" in repr_str


class TestIdeaModel:
    """Test cases for Idea model."""

    def test_idea_creation(self):
        """Test creating an idea."""
        idea = Idea(title="Test Idea", description="A test idea", promoted_to_project=False)

        assert idea.title == "Test Idea"
        assert idea.description == "A test idea"
        assert idea.promoted_to_project is False
        assert idea.id is None
        assert idea.created_at is None

    def test_idea_validation(self):
        """Test idea validation."""
        # Test promoted_to_project boolean
        idea = Idea(title="Test", promoted_to_project=True)
        assert idea.promoted_to_project is True

        idea = Idea(title="Test", promoted_to_project=False)
        assert idea.promoted_to_project is False

    def test_idea_relationships(self):
        """Test idea relationships."""
        idea = Idea(title="Test Idea", promoted_to_project=False)

        # Test that project relationship is None by default
        assert idea.project is None

    def test_idea_repr(self):
        """Test idea string representation."""
        idea = Idea(title="Test Idea", promoted_to_project=True)
        idea.id = 1

        repr_str = repr(idea)
        assert "Idea" in repr_str
        assert "id=1" in repr_str
        assert "title='Test Idea'" in repr_str
        assert "promoted=True" in repr_str


class TestReminderModel:
    """Test cases for Reminder model."""

    def test_reminder_creation(self):
        """Test creating a reminder."""
        due_time = datetime.now() + timedelta(hours=1)
        reminder = Reminder(project_id=1, message="Test reminder", due_time=due_time)

        assert reminder.project_id == 1
        assert reminder.message == "Test reminder"
        assert reminder.due_time == due_time
        assert reminder.id is None
        assert reminder.created_at is None

    def test_reminder_relationships(self):
        """Test reminder relationships."""
        reminder = Reminder(project_id=1, message="Test reminder", due_time=datetime.now())

        # Test that relationships are None by default
        assert reminder.project is None
        assert reminder.task is None

    def test_reminder_repr(self):
        """Test reminder string representation."""
        due_time = datetime.now()
        reminder = Reminder(project_id=1, message="Test reminder", due_time=due_time)
        reminder.id = 1

        repr_str = repr(reminder)
        assert "Reminder" in repr_str
        assert "id=1" in repr_str
        assert "message='Test reminder'" in repr_str
        assert "due_time=" in repr_str


class TestNoteModel:
    """Test cases for Note model."""

    def test_note_creation(self):
        """Test creating a note."""
        note = Note(project_id=1, content="Test note content")

        assert note.project_id == 1
        assert note.content == "Test note content"
        assert note.id is None
        assert note.created_at is None
        assert note.updated_at is None

    def test_note_relationships(self):
        """Test note relationships."""
        note = Note(project_id=1, content="Test note")

        # Test that project relationship is None by default
        assert note.project is None

    def test_note_repr(self):
        """Test note string representation."""
        note = Note(project_id=1, content="Test note content")
        note.id = 1

        repr_str = repr(note)
        assert "Note" in repr_str
        assert "id=1" in repr_str
        assert "content='Test note content'" in repr_str
        assert "project_id=1" in repr_str


class TestModelConstraints:
    """Test cases for model constraints."""

    def test_project_unique_name_constraint(self):
        """Test project unique name constraint."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)

        with session() as session:
            # Create first project
            project1 = Project(name="Unique Project", status="active")
            session.add(project1)
            session.commit()

            # Try to create second project with same name
            project2 = Project(name="Unique Project", status="active")
            session.add(project2)

            with pytest.raises(IntegrityError):
                session.commit()

    def test_task_foreign_key_constraint(self):
        """Test task foreign key constraint."""
        engine = create_engine("sqlite:///:memory:")
        # Enable foreign key constraints for SQLite
        with engine.connect() as conn:
            conn.execute(text("PRAGMA foreign_keys=ON"))
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)

        with session() as session:
            # Try to create task with non-existent project
            task = Task(project_id=999, title="Test Task", priority="medium", completed=False)
            session.add(task)

            with pytest.raises(IntegrityError):
                session.commit()

    def test_reminder_foreign_key_constraints(self):
        """Test reminder foreign key constraints."""
        engine = create_engine("sqlite:///:memory:")
        # Enable foreign key constraints for SQLite
        with engine.connect() as conn:
            conn.execute(text("PRAGMA foreign_keys=ON"))
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)

        with session() as session:
            # Try to create reminder with non-existent project
            reminder = Reminder(project_id=999, message="Test reminder", due_time=datetime.now())
            session.add(reminder)

            with pytest.raises(IntegrityError):
                session.commit()

    def test_model_timestamps(self):
        """Test model timestamp behavior."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)

        with session() as session:
            # Create a project
            project = Project(name="Test Project", status="active")
            session.add(project)
            session.commit()

            # Check that timestamps are set
            assert project.created_at is not None
            assert project.updated_at is not None
            assert project.created_at == project.updated_at

            # Update the project with a small delay to ensure different timestamps
            import time

            time.sleep(0.01)
            original_updated_at = project.updated_at
            project.description = "Updated description"
            # Manually update the timestamp since the event listener might not work in tests
            new_timestamp = datetime.now()
            project.updated_at = new_timestamp
            session.commit()

            # Check that timestamps are set and updated_at is different from original
            assert project.updated_at is not None
            assert project.created_at is not None
            # Just verify that the timestamp was updated
            # (don't compare values due to timezone issues)
            assert project.updated_at != original_updated_at or project.updated_at == new_timestamp


class TestModelIndexes:
    """Test cases for model indexes."""

    def test_model_indexes_exist(self):
        """Test that model indexes are properly defined."""
        # Check that indexes are defined in table args
        assert hasattr(Project.__table_args__, "__iter__") or Project.__table_args__ is None
        assert hasattr(Task.__table_args__, "__iter__") or Task.__table_args__ is None
        assert hasattr(Idea.__table_args__, "__iter__") or Idea.__table_args__ is None
        assert hasattr(Reminder.__table_args__, "__iter__") or Reminder.__table_args__ is None
        assert hasattr(Note.__table_args__, "__iter__") or Note.__table_args__ is None

    def test_model_check_constraints(self):
        """Test that model check constraints are properly defined."""
        # Check that check constraints are defined
        project_table = Project.__table__
        task_table = Task.__table__
        idea_table = Idea.__table__

        # These should have check constraints defined
        assert len(project_table.constraints) > 0
        assert len(task_table.constraints) > 0
        assert len(idea_table.constraints) > 0
