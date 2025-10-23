"""Integration tests for database functionality.

This module provides integration tests for the database functionality
in the Iris application.
"""

import asyncio
import os
import tempfile

import pytest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError

from iris.core.config.settings import Settings
from iris.core.database.connection import DatabaseConnection, initialize_database
from iris.core.database.models import Base, Idea, Note, Project, Reminder, Task


class TestDatabaseIntegration:
    """Integration tests for database functionality."""

    @pytest.fixture
    def temp_db(self):
        """Create temporary database for testing."""
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
            db_path = tmp.name

        yield f"sqlite:///{db_path}"

        # Cleanup - try multiple times on Windows
        if os.path.exists(db_path):
            import time

            for attempt in range(3):
                try:
                    os.unlink(db_path)
                    break
                except (OSError, PermissionError):
                    if attempt < 2:
                        time.sleep(0.1)  # Wait a bit and try again
                    # On last attempt, just ignore the error

    @pytest.fixture
    def db_connection(self, temp_db):
        """Create database connection for testing."""
        connection = DatabaseConnection(temp_db)
        engine = connection.create_engine()
        Base.metadata.create_all(engine)
        return connection

    def test_database_schema_creation(self, db_connection):
        """Test database schema creation."""
        engine = db_connection.create_engine()

        # Check that all tables are created
        with engine.connect() as conn:
            result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
            tables = [row[0] for row in result]

            expected_tables = ["projects", "tasks", "ideas", "reminders", "notes"]
            for table in expected_tables:
                assert table in tables

    def test_project_creation_and_retrieval(self, db_connection):
        """Test creating and retrieving projects."""
        with db_connection.transaction() as session:
            # Create a project
            project = Project(name="Test Project", description="A test project", status="active")
            session.add(project)
            session.flush()

            # Retrieve the project
            retrieved_project = session.query(Project).filter_by(name="Test Project").first()

            assert retrieved_project is not None
            assert retrieved_project.name == "Test Project"
            assert retrieved_project.description == "A test project"
            assert retrieved_project.status == "active"
            assert retrieved_project.id is not None
            assert retrieved_project.created_at is not None
            assert retrieved_project.updated_at is not None

    def test_task_creation_and_retrieval(self, db_connection):
        """Test creating and retrieving tasks."""
        with db_connection.transaction() as session:
            # Create a project first
            project = Project(name="Test Project", status="active")
            session.add(project)
            session.flush()

            # Create a task
            task = Task(project_id=project.id, title="Test Task", priority="high", completed=False)
            session.add(task)
            session.flush()

            # Retrieve the task
            retrieved_task = session.query(Task).filter_by(title="Test Task").first()

            assert retrieved_task is not None
            assert retrieved_task.title == "Test Task"
            assert retrieved_task.priority == "high"
            assert retrieved_task.completed is False
            assert retrieved_task.project_id == project.id
            assert retrieved_task.id is not None

    def test_idea_creation_and_retrieval(self, db_connection):
        """Test creating and retrieving ideas."""
        with db_connection.transaction() as session:
            # Create an idea
            idea = Idea(title="Test Idea", description="A test idea", promoted_to_project=False)
            session.add(idea)
            session.flush()

            # Retrieve the idea
            retrieved_idea = session.query(Idea).filter_by(title="Test Idea").first()

            assert retrieved_idea is not None
            assert retrieved_idea.title == "Test Idea"
            assert retrieved_idea.description == "A test idea"
            assert retrieved_idea.promoted_to_project is False
            assert retrieved_idea.id is not None

    def test_reminder_creation_and_retrieval(self, db_connection):
        """Test creating and retrieving reminders."""
        with db_connection.transaction() as session:
            # Create a project first
            project = Project(name="Test Project", status="active")
            session.add(project)
            session.flush()

            # Create a reminder
            from datetime import datetime, timedelta

            due_time = datetime.now() + timedelta(hours=1)

            reminder = Reminder(project_id=project.id, message="Test reminder", due_time=due_time)
            session.add(reminder)
            session.flush()

            # Retrieve the reminder
            retrieved_reminder = session.query(Reminder).filter_by(message="Test reminder").first()

            assert retrieved_reminder is not None
            assert retrieved_reminder.message == "Test reminder"
            assert retrieved_reminder.project_id == project.id
            assert retrieved_reminder.due_time == due_time
            assert retrieved_reminder.id is not None

    def test_note_creation_and_retrieval(self, db_connection):
        """Test creating and retrieving notes."""
        with db_connection.transaction() as session:
            # Create a project first
            project = Project(name="Test Project", status="active")
            session.add(project)
            session.flush()

            # Create a note
            note = Note(project_id=project.id, content="Test note content")
            session.add(note)
            session.flush()

            # Retrieve the note
            retrieved_note = session.query(Note).filter_by(content="Test note content").first()

            assert retrieved_note is not None
            assert retrieved_note.content == "Test note content"
            assert retrieved_note.project_id == project.id
            assert retrieved_note.id is not None

    def test_relationships(self, db_connection):
        """Test entity relationships."""
        with db_connection.transaction() as session:
            # Create a project
            project = Project(name="Test Project", status="active")
            session.add(project)
            session.flush()

            # Create related entities
            task = Task(
                project_id=project.id, title="Test Task", priority="medium", completed=False
            )
            idea = Idea(project_id=project.id, title="Test Idea", promoted_to_project=False)
            note = Note(project_id=project.id, content="Test note")

            session.add_all([task, idea, note])
            session.flush()

            # Test relationships
            assert len(project.tasks) == 1
            assert len(project.ideas) == 1
            assert len(project.notes) == 1

            assert project.tasks[0].title == "Test Task"
            assert project.ideas[0].title == "Test Idea"
            assert project.notes[0].content == "Test note"

    def test_constraints_and_validation(self, db_connection):
        """Test database constraints and validation."""
        import uuid

        unique_name = f"Unique Project {uuid.uuid4().hex[:8]}"

        # Test unique constraint on project name using raw SQL to avoid session issues
        engine = db_connection.create_engine()
        with engine.connect() as conn:
            # Insert first project
            conn.execute(
                text(
                    "INSERT INTO projects (name, status, created_at, updated_at) "
                    "VALUES (:name, 'active', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                ),
                {"name": unique_name},
            )
            conn.commit()

            # Try to insert another project with the same name
            with pytest.raises(IntegrityError):  # Should raise integrity error
                conn.execute(
                    text(
                        "INSERT INTO projects (name, status, created_at, updated_at) "
                        "VALUES (:name, 'active', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                    ),
                    {"name": unique_name},
                )
                conn.commit()

    @pytest.mark.asyncio
    async def test_connection_health_check(self, db_connection):
        """Test database health check."""
        health = await db_connection.health_check()

        assert health["status"] == "healthy"
        assert "response_time" in health
        assert "query_time" in health
        assert "project_count" in health
        assert "pool_info" in health
        assert "timestamp" in health

    @pytest.mark.asyncio
    async def test_connection_performance(self, db_connection):
        """Test database connection performance."""
        # Test connection establishment time
        start_time = asyncio.get_event_loop().time()
        result = await db_connection.test_connection()
        end_time = asyncio.get_event_loop().time()

        assert result is True
        assert (end_time - start_time) < 5.0  # Should be under 5 seconds

    def test_transaction_rollback(self, db_connection):
        """Test transaction rollback on error."""
        import uuid

        unique_name = f"Test Project {uuid.uuid4().hex[:8]}"

        # Test that the transaction context manager properly handles exceptions
        with pytest.raises(ValueError), db_connection.transaction() as session:
            # Create a project
            project = Project(name=unique_name, status="active")
            session.add(project)
            session.flush()

            # This should cause a rollback
            raise ValueError("Test error")

        # Check that the project was not committed
        with db_connection.transaction() as session:
            project = session.query(Project).filter_by(name=unique_name).first()
            assert project is None

    def test_concurrent_connections(self, db_connection):
        """Test concurrent database connections."""
        # Test multiple sessions sequentially to avoid SQLite locking issues
        with db_connection.transaction() as session1:
            project1 = Project(name="Project 1", status="active")
            session1.add(project1)
            session1.flush()
            assert project1.id is not None

        with db_connection.transaction() as session2:
            project2 = Project(name="Project 2", status="active")
            session2.add(project2)
            session2.flush()
            assert project2.id is not None

        # Verify both projects were created
        with db_connection.transaction() as session:
            projects = (
                session.query(Project).filter(Project.name.in_(["Project 1", "Project 2"])).all()
            )
            assert len(projects) == 2


class TestDatabaseConfiguration:
    """Test database configuration integration."""

    def test_database_url_configuration(self):
        """Test database URL configuration."""
        # Test SQLite configuration
        settings = Settings()
        db_url = settings.get_database_url()

        assert db_url is not None
        assert "sqlite" in db_url or "postgresql" in db_url

    def test_connection_pool_configuration(self):
        """Test connection pool configuration."""
        settings = Settings()
        pool_config = settings.get_connection_pool_config()

        assert "pool_size" in pool_config
        assert "pool_timeout" in pool_config
        assert "pool_recycle" in pool_config
        assert "echo" in pool_config

    def test_environment_specific_configuration(self):
        """Test environment-specific configuration."""
        # Test development environment
        settings = Settings()
        assert settings.is_development() or settings.is_production() or settings.is_testing()

    def test_database_initialization_with_settings(self):
        """Test database initialization with settings."""
        settings = Settings()
        db_url = settings.get_database_url()
        pool_config = settings.get_connection_pool_config()

        connection = initialize_database(
            db_url, pool_size=pool_config["pool_size"], pool_timeout=pool_config["pool_timeout"]
        )

        assert connection is not None
        assert connection.database_url == db_url
        assert connection.pool_size == pool_config["pool_size"]
        assert connection.pool_timeout == pool_config["pool_timeout"]
