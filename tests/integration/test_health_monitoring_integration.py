"""Integration tests for health monitoring.

This module provides integration tests for the health monitoring functionality
in the Iris application.
"""

from datetime import datetime
from unittest.mock import Mock

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from iris.core.database.models import Base, Idea, Note, Project, Reminder, Task
from iris.core.database.monitoring import DatabaseMonitor


class TestHealthMonitoringIntegration:
    """Integration tests for health monitoring."""

    @pytest.fixture
    def db_engine(self):
        """Create database engine for testing."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        return engine

    @pytest.fixture
    def db_session(self, db_engine):
        """Create database session for testing."""
        session = sessionmaker(bind=db_engine)
        return session()

    @pytest.fixture
    def monitor(self, db_session):
        """Create database monitor for testing."""
        # Create a mock connection for testing
        mock_connection = Mock()

        # Make test_connection async
        async def async_test_connection():
            return True

        mock_connection.test_connection = async_test_connection

        # Make get_connection_info async
        async def async_get_connection_info():
            return {"pool_size": 5, "checked_out": 2, "checked_in": 3, "overflow": 0, "invalid": 0}

        mock_connection.get_connection_info = async_get_connection_info

        return DatabaseMonitor(db_session, mock_connection)

    @pytest.mark.asyncio
    async def test_health_monitoring_full_cycle(self, monitor, db_session):
        """Test complete health monitoring cycle."""
        # Create test data
        project = Project(name="Test Project", status="active")
        db_session.add(project)
        db_session.commit()

        task = Task(project_id=project.id, title="Test Task", priority="medium", completed=False)
        db_session.add(task)
        db_session.commit()

        idea = Idea(title="Test Idea", promoted_to_project=False)
        db_session.add(idea)
        db_session.commit()

        note = Note(content="Test Note", project_id=project.id)
        db_session.add(note)
        db_session.commit()

        # Test health metrics
        health = await monitor.get_health_metrics()
        assert health.status == "healthy"
        assert health.project_count == 1
        assert health.task_count == 1
        assert health.idea_count == 1
        assert health.note_count == 1

        # Test performance metrics
        perf = monitor.get_performance_metrics()
        assert perf.avg_query_time > 0
        assert perf.total_queries > 0

        # Test connection health
        conn_health = await monitor.check_connection_health()
        assert conn_health["status"] == "healthy"
        assert "pool_size" in conn_health
        assert "active_connections" in conn_health

        # Test diagnostics report
        report = await monitor.get_diagnostics_report()
        assert "health" in report
        assert "performance" in report
        assert "database" in report
        assert "connections" in report
        assert "statistics" in report

        # Test performance summary
        summary = await monitor.get_performance_summary()
        assert "query_performance" in summary
        assert "connection_performance" in summary
        assert "resource_usage" in summary

    @pytest.mark.asyncio
    async def test_health_monitoring_with_large_dataset(self, monitor, db_session):
        """Test health monitoring with large dataset."""
        # Create large dataset
        projects = []
        for i in range(10):
            project = Project(name=f"Project {i}", status="active")
            db_session.add(project)
            projects.append(project)

        db_session.commit()

        for project in projects:
            for j in range(5):
                task = Task(
                    project_id=project.id, title=f"Task {j}", priority="medium", completed=False
                )
                db_session.add(task)

        db_session.commit()

        # Test health metrics
        health = await monitor.get_health_metrics()
        assert health.status == "healthy"
        assert health.project_count == 10
        assert health.task_count == 50

        # Test performance metrics
        perf = monitor.get_performance_metrics()
        assert perf.avg_query_time > 0
        assert perf.total_queries > 0

        # Test diagnostics report
        report = await monitor.get_diagnostics_report()
        assert report["database"]["project_count"] == 10
        assert report["database"]["task_count"] == 50

        # Test performance summary
        summary = await monitor.get_performance_summary()
        assert summary["query_performance"]["total_queries"] > 0

    @pytest.mark.asyncio
    async def test_health_monitoring_with_mixed_statuses(self, monitor, db_session):
        """Test health monitoring with mixed entity statuses."""
        # Create projects with different statuses
        active_project = Project(name="Active Project", status="active")
        completed_project = Project(name="Completed Project", status="completed")
        paused_project = Project(name="Paused Project", status="paused")

        db_session.add_all([active_project, completed_project, paused_project])
        db_session.commit()

        # Create tasks with different statuses
        active_task = Task(
            project_id=active_project.id, title="Active Task", priority="high", completed=False
        )
        completed_task = Task(
            project_id=completed_project.id,
            title="Completed Task",
            priority="medium",
            completed=True,
        )

        db_session.add_all([active_task, completed_task])
        db_session.commit()

        # Create ideas with different promotion statuses
        promoted_idea = Idea(title="Promoted Idea", promoted_to_project=True)
        unpromoted_idea = Idea(title="Unpromoted Idea", promoted_to_project=False)

        db_session.add_all([promoted_idea, unpromoted_idea])
        db_session.commit()

        # Create reminders with different statuses
        now = datetime.now()
        upcoming_reminder = Reminder(
            message="Upcoming Reminder",
            due_time=now.replace(year=now.year + 1),  # Next year
            project_id=active_project.id,
        )
        past_reminder = Reminder(
            message="Past Reminder",
            due_time=now.replace(year=now.year - 1),  # Last year
            project_id=completed_project.id,
        )

        db_session.add_all([upcoming_reminder, past_reminder])
        db_session.commit()

        # Test health metrics
        health = await monitor.get_health_metrics()
        assert health.status == "healthy"
        assert health.project_count == 3
        assert health.task_count == 2
        assert health.idea_count == 2
        assert health.reminder_count == 2

        # Test diagnostics report
        report = await monitor.get_diagnostics_report()
        assert report["database"]["project_count"] == 3
        assert report["database"]["task_count"] == 2
        assert report["database"]["idea_count"] == 2
        assert report["database"]["reminder_count"] == 2

        # Test statistics
        stats = report["statistics"]
        assert stats["projects"]["total"] == 3
        assert stats["projects"]["active"] == 1
        assert stats["projects"]["completed"] == 1
        assert stats["projects"]["paused"] == 1
        assert stats["tasks"]["total"] == 2
        assert stats["tasks"]["completed"] == 1
        assert stats["tasks"]["pending"] == 1
        assert stats["ideas"]["total"] == 2
        assert stats["ideas"]["promoted"] == 1
        assert stats["ideas"]["unpromoted"] == 1
        assert stats["reminders"]["total"] == 2
        assert stats["reminders"]["upcoming"] == 1
        assert stats["reminders"]["past"] == 1

    @pytest.mark.asyncio
    async def test_health_monitoring_connection_pooling(self, monitor, db_session):
        """Test health monitoring with connection pooling."""
        # Test connection health
        conn_health = await monitor.check_connection_health()
        assert conn_health["status"] == "healthy"
        assert "pool_size" in conn_health
        assert "active_connections" in conn_health
        assert "idle_connections" in conn_health
        assert "utilization" in conn_health

        # Test performance metrics
        perf = monitor.get_performance_metrics()
        assert perf.connection_pool_utilization >= 0
        assert perf.connection_pool_utilization <= 1

        # Test diagnostics report
        report = await monitor.get_diagnostics_report()
        assert "connections" in report
        assert "pool_size" in report["connections"]
        assert "active_connections" in report["connections"]
        assert "idle_connections" in report["connections"]

    @pytest.mark.asyncio
    async def test_health_monitoring_error_handling(self, monitor, db_session):
        """Test health monitoring error handling."""
        # Test with invalid session and mock connection
        mock_connection = Mock()

        async def async_test_connection():
            return False

        mock_connection.test_connection = async_test_connection
        invalid_monitor = DatabaseMonitor(None, mock_connection)

        # Test health metrics with invalid session
        health = await invalid_monitor.get_health_metrics()
        assert health.status == "unhealthy"
        assert health.error_message is not None

        # Test performance metrics with invalid session
        perf = invalid_monitor.get_performance_metrics()
        # Performance metrics are hardcoded, not based on connection status
        assert perf.avg_query_time > 0
        assert perf.total_queries > 0

        # Test connection health with invalid session
        conn_health = await invalid_monitor.check_connection_health()
        assert conn_health["status"] == "unhealthy"
        assert "error" in conn_health

        # Test diagnostics report with invalid session
        report = await invalid_monitor.get_diagnostics_report()
        assert "error" in report

        # Test performance summary with invalid session
        summary = await invalid_monitor.get_performance_summary()
        # Performance summary should still work but show unhealthy connection
        assert "connection_performance" in summary
        assert summary["connection_performance"]["status"] == "unhealthy"

    @pytest.mark.asyncio
    async def test_health_monitoring_metrics_consistency(self, monitor, db_session):
        """Test health monitoring metrics consistency."""
        # Create test data
        project = Project(name="Test Project", status="active")
        db_session.add(project)
        db_session.commit()

        task = Task(project_id=project.id, title="Test Task", priority="medium", completed=False)
        db_session.add(task)
        db_session.commit()

        # Get multiple metrics
        health1 = await monitor.get_health_metrics()
        health2 = await monitor.get_health_metrics()

        # Metrics should be consistent
        assert health1.project_count == health2.project_count
        assert health1.task_count == health2.task_count
        assert health1.idea_count == health2.idea_count
        assert health1.reminder_count == health2.reminder_count
        assert health1.note_count == health2.note_count

        # Test performance metrics consistency
        perf1 = monitor.get_performance_metrics()
        perf2 = monitor.get_performance_metrics()

        # Performance metrics should be consistent
        assert perf1.avg_query_time == perf2.avg_query_time
        assert perf1.max_query_time == perf2.max_query_time
        assert perf1.min_query_time == perf2.min_query_time
        assert perf1.total_queries == perf2.total_queries
        assert perf1.slow_queries == perf2.slow_queries
        assert perf1.connection_pool_utilization == perf2.connection_pool_utilization
        assert perf1.memory_usage == perf2.memory_usage
        assert perf1.disk_usage == perf2.disk_usage

    @pytest.mark.asyncio
    async def test_health_monitoring_timestamp_accuracy(self, monitor, db_session):
        """Test health monitoring timestamp accuracy."""
        # Get metrics
        health = await monitor.get_health_metrics()
        perf = monitor.get_performance_metrics()

        # Check timestamps are recent
        now = datetime.now()
        health_time = health.timestamp
        perf_time = perf.timestamp

        # Timestamps should be within last minute
        assert abs((now - health_time).total_seconds()) < 60
        assert abs((now - perf_time).total_seconds()) < 60

        # Test diagnostics report timestamp
        report = await monitor.get_diagnostics_report()
        assert "timestamp" in report
        report_time = datetime.fromisoformat(report["timestamp"])
        assert abs((now - report_time).total_seconds()) < 60

        # Test performance summary timestamp
        summary = await monitor.get_performance_summary()
        assert "timestamp" in summary
        summary_time = datetime.fromisoformat(summary["timestamp"])
        assert abs((now - summary_time).total_seconds()) < 60
