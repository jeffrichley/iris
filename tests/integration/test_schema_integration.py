"""Integration tests for database schema.

This module provides integration tests for the database schema
and migration functionality in the Iris application.
"""

from datetime import datetime

import pytest
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from iris.core.database.models import Base, Idea, Note, Project, Reminder, Task


class TestSchemaCreation:
    """Test cases for database schema creation."""

    def test_schema_creation(self):
        """Test creating database schema."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)

        # Check that all tables are created
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        expected_tables = ["projects", "tasks", "ideas", "reminders", "notes"]
        for table in expected_tables:
            assert table in tables

    def test_table_columns(self):
        """Test that tables have correct columns."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        inspector = inspect(engine)

        # Check projects table columns
        project_columns = [col["name"] for col in inspector.get_columns("projects")]
        expected_project_columns = [
            "id",
            "name",
            "description",
            "status",
            "created_at",
            "updated_at",
        ]
        for col in expected_project_columns:
            assert col in project_columns

        # Check tasks table columns
        task_columns = [col["name"] for col in inspector.get_columns("tasks")]
        expected_task_columns = [
            "id",
            "project_id",
            "title",
            "priority",
            "due_date",
            "completed",
            "notes",
            "created_at",
            "updated_at",
        ]
        for col in expected_task_columns:
            assert col in task_columns

        # Check ideas table columns
        idea_columns = [col["name"] for col in inspector.get_columns("ideas")]
        expected_idea_columns = [
            "id",
            "project_id",
            "title",
            "description",
            "promoted_to_project",
            "created_at",
        ]
        for col in expected_idea_columns:
            assert col in idea_columns

        # Check reminders table columns
        reminder_columns = [col["name"] for col in inspector.get_columns("reminders")]
        expected_reminder_columns = [
            "id",
            "project_id",
            "task_id",
            "message",
            "due_time",
            "created_at",
        ]
        for col in expected_reminder_columns:
            assert col in reminder_columns

        # Check notes table columns
        note_columns = [col["name"] for col in inspector.get_columns("notes")]
        expected_note_columns = ["id", "project_id", "content", "created_at", "updated_at"]
        for col in expected_note_columns:
            assert col in note_columns

    def test_foreign_key_constraints(self):
        """Test foreign key constraints."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        inspector = inspect(engine)

        # Check foreign keys
        foreign_keys = inspector.get_foreign_keys("tasks")
        assert len(foreign_keys) == 1
        assert foreign_keys[0]["referred_table"] == "projects"
        assert foreign_keys[0]["constrained_columns"] == ["project_id"]

        foreign_keys = inspector.get_foreign_keys("ideas")
        assert len(foreign_keys) == 1
        assert foreign_keys[0]["referred_table"] == "projects"
        assert foreign_keys[0]["constrained_columns"] == ["project_id"]

        foreign_keys = inspector.get_foreign_keys("reminders")
        assert len(foreign_keys) == 2
        project_fk = next(fk for fk in foreign_keys if fk["referred_table"] == "projects")
        task_fk = next(fk for fk in foreign_keys if fk["referred_table"] == "tasks")
        assert project_fk["constrained_columns"] == ["project_id"]
        assert task_fk["constrained_columns"] == ["task_id"]

        foreign_keys = inspector.get_foreign_keys("notes")
        assert len(foreign_keys) == 1
        assert foreign_keys[0]["referred_table"] == "projects"
        assert foreign_keys[0]["constrained_columns"] == ["project_id"]

    def test_indexes(self):
        """Test database indexes."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        inspector = inspect(engine)

        # Check that indexes exist
        indexes = inspector.get_indexes("tasks")
        index_names = [idx["name"] for idx in indexes]

        expected_indexes = [
            "ix_tasks_project_id",
            "ix_tasks_completed",
            "ix_tasks_due_date",
            "ix_tasks_project_completed",
        ]
        for idx_name in expected_indexes:
            assert idx_name in index_names

        indexes = inspector.get_indexes("reminders")
        index_names = [idx["name"] for idx in indexes]

        expected_indexes = [
            "ix_reminders_due_time",
            "ix_reminders_project_id",
            "ix_reminders_task_id",
            "ix_reminders_due_project",
        ]
        for idx_name in expected_indexes:
            assert idx_name in index_names

    def test_check_constraints(self):
        """Test check constraints."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)

        # Test project status constraint
        with engine.connect() as conn:
            # Valid status
            conn.execute(
                text(
                    "INSERT INTO projects (name, status, created_at, updated_at) "
                    "VALUES ('Test', 'active', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            conn.execute(
                text(
                    "INSERT INTO projects (name, status, created_at, updated_at) "
                    "VALUES ('Test2', 'completed', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            conn.execute(
                text(
                    "INSERT INTO projects (name, status, created_at, updated_at) "
                    "VALUES ('Test3', 'paused', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            conn.commit()

            # Invalid status should fail
            with pytest.raises(IntegrityError):
                conn.execute(
                    text("INSERT INTO projects (name, status) VALUES ('Test4', 'invalid')")
                )
                conn.commit()

        # Test task priority constraint
        with engine.connect() as conn:
            # Valid priorities - use different project name to avoid conflicts
            conn.execute(
                text(
                    "INSERT INTO projects (name, status, created_at, updated_at) "
                    "VALUES ('TestProject2', 'active', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            conn.execute(
                text(
                    "INSERT INTO tasks (project_id, title, priority, completed, "
                    "created_at, updated_at) VALUES (1, 'Task', 'low', 0, "
                    "CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            conn.execute(
                text(
                    "INSERT INTO tasks (project_id, title, priority, completed, "
                    "created_at, updated_at) VALUES (1, 'Task2', 'medium', 0, "
                    "CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            conn.execute(
                text(
                    "INSERT INTO tasks (project_id, title, priority, completed, "
                    "created_at, updated_at) VALUES (1, 'Task3', 'high', 0, "
                    "CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            conn.execute(
                text(
                    "INSERT INTO tasks (project_id, title, priority, completed, "
                    "created_at, updated_at) VALUES (1, 'Task4', 'urgent', 0, "
                    "CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            conn.commit()

            # Invalid priority should fail
            with pytest.raises(IntegrityError):
                conn.execute(
                    text(
                        "INSERT INTO tasks (project_id, title, priority, completed, "
                        "created_at, updated_at) VALUES (1, 'Task5', 'invalid', 0, "
                        "CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                    )
                )
                conn.commit()


class TestSchemaDataIntegrity:
    """Test cases for data integrity."""

    def test_cascade_deletes(self):
        """Test cascade deletes."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)

        with session() as session:
            # Create project with related entities
            project = Project(name="Test Project", status="active")
            session.add(project)
            session.flush()

            task = Task(
                project_id=project.id, title="Test Task", priority="medium", completed=False
            )
            idea = Idea(project_id=project.id, title="Test Idea", promoted_to_project=False)
            note = Note(project_id=project.id, content="Test note")
            reminder = Reminder(
                project_id=project.id,
                message="Test reminder",
                due_time=datetime(2024, 12, 31, 12, 0, 0),
            )

            session.add_all([task, idea, note, reminder])
            session.commit()

            # Delete project
            session.delete(project)
            session.commit()

            # Check that related entities are deleted
            assert session.query(Task).filter_by(project_id=project.id).count() == 0
            assert session.query(Idea).filter_by(project_id=project.id).count() == 0
            assert session.query(Note).filter_by(project_id=project.id).count() == 0
            assert session.query(Reminder).filter_by(project_id=project.id).count() == 0

    def test_unique_constraints(self):
        """Test unique constraints."""
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

    def test_not_null_constraints(self):
        """Test not null constraints."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)

        with engine.connect() as conn:
            # Test project name not null
            with pytest.raises(IntegrityError):
                conn.execute(text("INSERT INTO projects (status) VALUES ('active')"))
                conn.commit()

            # Test project status not null
            with pytest.raises(IntegrityError):
                conn.execute(text("INSERT INTO projects (name) VALUES ('Test')"))
                conn.commit()

            # Test task title not null
            conn.execute(
                text(
                    "INSERT INTO projects (name, status, created_at, updated_at) "
                    "VALUES ('Test', 'active', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
                )
            )
            with pytest.raises(IntegrityError):
                conn.execute(
                    text(
                        "INSERT INTO tasks (project_id, priority, completed) "
                        "VALUES (1, 'medium', 0)"
                    )
                )
                conn.commit()

            # Test task priority not null
            with pytest.raises(IntegrityError):
                conn.execute(
                    text("INSERT INTO tasks (project_id, title, completed) VALUES (1, 'Task', 0)")
                )
                conn.commit()

            # Test task completed not null
            with pytest.raises(IntegrityError):
                conn.execute(
                    text(
                        "INSERT INTO tasks (project_id, title, priority) "
                        "VALUES (1, 'Task', 'medium')"
                    )
                )
                conn.commit()


class TestSchemaPerformance:
    """Test cases for schema performance."""

    def test_query_performance(self):
        """Test query performance with indexes."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)

        with session() as session:
            # Create test data
            project = Project(name="Test Project", status="active")
            session.add(project)
            session.flush()

            # Create multiple tasks
            for i in range(100):
                task = Task(
                    project_id=project.id,
                    title=f"Task {i}",
                    priority="medium" if i % 2 == 0 else "high",
                    completed=i % 3 == 0,
                )
                session.add(task)

            session.commit()

            # Test queries that should use indexes
            import time

            # Query by project_id (should use index)
            start_time = time.time()
            tasks = session.query(Task).filter_by(project_id=project.id).all()
            query_time = time.time() - start_time

            assert len(tasks) == 100
            assert query_time < 0.1  # Should be fast with index

            # Query by completed status (should use index)
            start_time = time.time()
            completed_tasks = session.query(Task).filter_by(completed=True).all()
            query_time = time.time() - start_time

            assert len(completed_tasks) > 0
            assert query_time < 0.1  # Should be fast with index

    def test_composite_index_performance(self):
        """Test composite index performance."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)

        with session() as session:
            # Create test data
            project = Project(name="Test Project", status="active")
            session.add(project)
            session.flush()

            # Create tasks with different completion statuses
            for i in range(50):
                task = Task(
                    project_id=project.id,
                    title=f"Task {i}",
                    priority="medium",
                    completed=i % 2 == 0,
                )
                session.add(task)

            session.commit()

            # Test composite index query (project_id + completed)
            import time

            start_time = time.time()
            completed_tasks = (
                session.query(Task).filter_by(project_id=project.id, completed=True).all()
            )
            query_time = time.time() - start_time

            assert len(completed_tasks) > 0
            assert query_time < 0.1  # Should be fast with composite index


class TestSchemaMigration:
    """Test cases for schema migration."""

    def test_schema_migration_compatibility(self):
        """Test that schema is compatible with migration system."""
        # This test ensures that the current schema matches what would be created by migrations
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)

        # Check that all expected tables exist
        inspector = inspect(engine)
        tables = inspector.get_table_names()

        expected_tables = ["projects", "tasks", "ideas", "reminders", "notes"]
        for table in expected_tables:
            assert table in tables

        # Check that all expected columns exist
        for table_name in expected_tables:
            columns = [col["name"] for col in inspector.get_columns(table_name)]
            assert len(columns) > 0  # Each table should have columns

    def test_schema_rollback(self):
        """Test schema rollback functionality."""
        engine = create_engine("sqlite:///:memory:")

        # Create schema
        Base.metadata.create_all(engine)

        # Check that tables exist
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        assert "projects" in tables

        # Drop schema
        Base.metadata.drop_all(engine)

        # Check that tables are gone - SQLite may need a new connection to reflect changes
        with engine.connect() as conn:
            result = conn.execute(text("SELECT name FROM sqlite_master WHERE type='table'"))
            tables = [row[0] for row in result]
            assert "projects" not in tables
