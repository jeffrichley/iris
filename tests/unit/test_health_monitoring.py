"""Unit tests for health monitoring.

This module provides unit tests for the health monitoring functionality
in the Iris application.
"""

from datetime import datetime
from unittest.mock import Mock, patch

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from iris.core.database.models import Base, Idea, Note, Project, Task
from iris.core.database.monitoring import DatabaseMonitor, HealthMetrics, PerformanceMetrics


class TestHealthMetrics:
    """Test cases for HealthMetrics class."""

    def test_health_metrics_creation(self):
        """Test creating health metrics."""
        metrics = HealthMetrics(
            status="healthy",
            response_time=0.1,
            query_time=0.05,
            connection_count=5,
            active_connections=2,
            idle_connections=3,
            overflow_connections=0,
            invalid_connections=0,
            project_count=10,
            task_count=25,
            idea_count=5,
            reminder_count=3,
            note_count=8,
            timestamp=datetime.now(),
        )

        assert metrics.status == "healthy"
        assert metrics.response_time == 0.1
        assert metrics.query_time == 0.05
        assert metrics.connection_count == 5
        assert metrics.active_connections == 2
        assert metrics.idle_connections == 3
        assert metrics.overflow_connections == 0
        assert metrics.invalid_connections == 0
        assert metrics.project_count == 10
        assert metrics.task_count == 25
        assert metrics.idea_count == 5
        assert metrics.reminder_count == 3
        assert metrics.note_count == 8
        assert metrics.error_message is None

    def test_health_metrics_with_error(self):
        """Test creating health metrics with error."""
        metrics = HealthMetrics(
            status="unhealthy",
            response_time=0.5,
            query_time=0.0,
            connection_count=0,
            active_connections=0,
            idle_connections=0,
            overflow_connections=0,
            invalid_connections=0,
            project_count=0,
            task_count=0,
            idea_count=0,
            reminder_count=0,
            note_count=0,
            timestamp=datetime.now(),
            error_message="Connection failed",
        )

        assert metrics.status == "unhealthy"
        assert metrics.error_message == "Connection failed"


class TestPerformanceMetrics:
    """Test cases for PerformanceMetrics class."""

    def test_performance_metrics_creation(self):
        """Test creating performance metrics."""
        metrics = PerformanceMetrics(
            avg_query_time=0.05,
            max_query_time=0.2,
            min_query_time=0.01,
            total_queries=100,
            slow_queries=5,
            connection_pool_utilization=0.6,
            memory_usage=0.3,
            disk_usage=0.1,
            timestamp=datetime.now(),
        )

        assert metrics.avg_query_time == 0.05
        assert metrics.max_query_time == 0.2
        assert metrics.min_query_time == 0.01
        assert metrics.total_queries == 100
        assert metrics.slow_queries == 5
        assert metrics.connection_pool_utilization == 0.6
        assert metrics.memory_usage == 0.3
        assert metrics.disk_usage == 0.1


class TestDatabaseMonitor:
    """Test cases for DatabaseMonitor class."""

    @pytest.fixture
    def db_session(self):
        """Create database session for testing."""
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
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

    def test_monitor_initialization(self, db_session):
        """Test monitor initialization."""
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

        monitor = DatabaseMonitor(db_session, mock_connection)
        assert monitor.session is db_session
        assert monitor._connection is mock_connection

    @pytest.mark.asyncio
    async def test_get_health_metrics_healthy(self, monitor):
        """Test getting health metrics when database is healthy."""
        with (
            patch.object(monitor._connection, "test_connection") as mock_test,
            patch.object(monitor._connection, "get_connection_info") as mock_info,
        ):
            mock_test.return_value = True
            mock_info.return_value = {
                "pool_size": 5,
                "checked_out": 2,
                "checked_in": 3,
                "overflow": 0,
                "invalid": 0,
            }

            metrics = await monitor.get_health_metrics()

            assert metrics.status == "healthy"
            assert metrics.connection_count == 5
            assert metrics.active_connections == 2
            assert metrics.idle_connections == 3
            assert metrics.overflow_connections == 0
            assert metrics.invalid_connections == 0
            assert metrics.error_message is None

    @pytest.mark.asyncio
    async def test_get_health_metrics_unhealthy(self, monitor):
        """Test getting health metrics when database is unhealthy."""
        with patch.object(monitor._connection, "test_connection") as mock_test:
            mock_test.return_value = False

            metrics = await monitor.get_health_metrics()

            assert metrics.status == "unhealthy"
            assert metrics.error_message == "Connection test failed"

    @pytest.mark.asyncio
    async def test_get_health_metrics_exception(self, monitor):
        """Test getting health metrics when exception occurs."""
        with patch.object(monitor._connection, "test_connection") as mock_test:
            mock_test.side_effect = Exception("Database error")

            metrics = await monitor.get_health_metrics()

            assert metrics.status == "unhealthy"
            assert metrics.error_message == "Database error"

    def test_get_performance_metrics(self, monitor):
        """Test getting performance metrics."""
        metrics = monitor.get_performance_metrics()

        assert isinstance(metrics, PerformanceMetrics)
        assert metrics.avg_query_time > 0
        assert metrics.max_query_time > 0
        assert metrics.min_query_time > 0
        assert metrics.total_queries > 0
        assert 0 <= metrics.connection_pool_utilization <= 1
        assert 0 <= metrics.memory_usage <= 1
        assert 0 <= metrics.disk_usage <= 1

    @pytest.mark.asyncio
    async def test_get_diagnostics_report(self, monitor):
        """Test getting diagnostics report."""
        with (
            patch.object(monitor, "get_health_metrics") as mock_health,
            patch.object(monitor, "get_performance_metrics") as mock_perf,
            patch.object(monitor, "_get_database_statistics") as mock_stats,
            patch.object(monitor._connection, "get_connection_info") as mock_conn,
        ):
            # Mock health metrics
            mock_health.return_value = HealthMetrics(
                status="healthy",
                response_time=0.1,
                query_time=0.05,
                connection_count=5,
                active_connections=2,
                idle_connections=3,
                overflow_connections=0,
                invalid_connections=0,
                project_count=10,
                task_count=25,
                idea_count=5,
                reminder_count=3,
                note_count=8,
                timestamp=datetime.now(),
            )

            # Mock performance metrics
            mock_perf.return_value = PerformanceMetrics(
                avg_query_time=0.05,
                max_query_time=0.2,
                min_query_time=0.01,
                total_queries=100,
                slow_queries=5,
                connection_pool_utilization=0.6,
                memory_usage=0.3,
                disk_usage=0.1,
                timestamp=datetime.now(),
            )

            # Mock database statistics
            mock_stats.return_value = {
                "projects": {"total": 10, "active": 8, "completed": 2, "paused": 0},
                "tasks": {"total": 25, "completed": 15, "pending": 10},
                "ideas": {"total": 5, "promoted": 2, "unpromoted": 3},
                "reminders": {"total": 3, "upcoming": 2, "past": 1},
                "notes": {"total": 8},
            }

            # Mock connection info
            mock_conn.return_value = {
                "pool_size": 5,
                "checked_out": 2,
                "checked_in": 3,
                "overflow": 0,
                "invalid": 0,
            }

            report = await monitor.get_diagnostics_report()

            assert "health" in report
            assert "performance" in report
            assert "database" in report
            assert "connections" in report
            assert "statistics" in report
            assert "timestamp" in report

            assert report["health"]["status"] == "healthy"
            assert report["health"]["response_time"] == 0.1
            assert report["database"]["project_count"] == 10
            assert report["database"]["task_count"] == 25
            assert report["connections"]["pool_size"] == 5

    @pytest.mark.asyncio
    async def test_get_diagnostics_report_exception(self, monitor):
        """Test getting diagnostics report when exception occurs."""
        with patch.object(monitor, "get_health_metrics") as mock_health:
            mock_health.side_effect = Exception("Database error")

            report = await monitor.get_diagnostics_report()

            assert "error" in report
            assert report["error"] == "Database error"

    @pytest.mark.asyncio
    async def test_check_connection_health_healthy(self, monitor):
        """Test checking connection health when healthy."""
        with patch.object(monitor._connection, "get_connection_info") as mock_info:
            mock_info.return_value = {
                "pool_size": 5,
                "checked_out": 2,
                "checked_in": 3,
                "overflow": 0,
                "invalid": 0,
            }

            health = await monitor.check_connection_health()

            assert health["status"] == "healthy"
            assert health["pool_size"] == 5
            assert health["active_connections"] == 2
            assert health["idle_connections"] == 3
            assert health["overflow_connections"] == 0
            assert health["invalid_connections"] == 0
            assert health["utilization"] == 0.4  # 2/5
            assert "timestamp" in health

    @pytest.mark.asyncio
    async def test_check_connection_health_degraded(self, monitor):
        """Test checking connection health when degraded."""
        with patch.object(monitor._connection, "get_connection_info") as mock_info:
            mock_info.return_value = {
                "pool_size": 5,
                "checked_out": 2,
                "checked_in": 3,
                "overflow": 0,
                "invalid": 1,  # Has invalid connections
            }

            health = await monitor.check_connection_health()

            assert health["status"] == "degraded"
            assert health["invalid_connections"] == 1

    @pytest.mark.asyncio
    async def test_check_connection_health_exception(self, monitor):
        """Test checking connection health when exception occurs."""
        with patch.object(monitor._connection, "get_connection_info") as mock_info:
            mock_info.side_effect = Exception("Connection error")

            health = await monitor.check_connection_health()

            assert health["status"] == "unhealthy"
            assert "error" in health
            assert health["error"] == "Connection error"

    @pytest.mark.asyncio
    async def test_get_performance_summary(self, monitor):
        """Test getting performance summary."""
        with (
            patch.object(monitor, "get_performance_metrics") as mock_perf,
            patch.object(monitor, "check_connection_health") as mock_health,
        ):
            # Mock performance metrics
            mock_perf.return_value = PerformanceMetrics(
                avg_query_time=0.05,
                max_query_time=0.2,
                min_query_time=0.01,
                total_queries=100,
                slow_queries=5,
                connection_pool_utilization=0.6,
                memory_usage=0.3,
                disk_usage=0.1,
                timestamp=datetime.now(),
            )

            # Mock connection health
            mock_health.return_value = {
                "status": "healthy",
                "active_connections": 3,
                "pool_size": 5,
            }

            summary = await monitor.get_performance_summary()

            assert "query_performance" in summary
            assert "connection_performance" in summary
            assert "resource_usage" in summary
            assert "timestamp" in summary

            assert summary["query_performance"]["avg_time"] == 0.05
            assert summary["query_performance"]["max_time"] == 0.2
            assert summary["query_performance"]["total_queries"] == 100
            assert summary["connection_performance"]["status"] == "healthy"
            assert summary["resource_usage"]["memory_usage"] == 0.3

    @pytest.mark.asyncio
    async def test_get_performance_summary_exception(self, monitor):
        """Test getting performance summary when exception occurs."""
        with patch.object(monitor, "get_performance_metrics") as mock_perf:
            mock_perf.side_effect = Exception("Performance error")

            summary = await monitor.get_performance_summary()

            assert "error" in summary
            assert summary["error"] == "Performance error"

    def test_get_entity_count(self, monitor, db_session):
        """Test getting entity count."""
        # Create test data
        project = Project(name="Test Project", status="active")
        db_session.add(project)
        db_session.commit()

        # Test counting
        count = monitor._get_entity_count(Project)
        assert count == 1

        # Test with non-existent entity
        count = monitor._get_entity_count(Task)
        assert count == 0

    def test_get_database_statistics(self, monitor, db_session):
        """Test getting database statistics."""
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

        stats = monitor._get_database_statistics()

        assert "projects" in stats
        assert "tasks" in stats
        assert "ideas" in stats
        assert "notes" in stats

        assert stats["projects"]["total"] == 1
        assert stats["projects"]["active"] == 1
        assert stats["tasks"]["total"] == 1
        assert stats["tasks"]["pending"] == 1
        assert stats["ideas"]["total"] == 1
        assert stats["ideas"]["unpromoted"] == 1
        assert stats["notes"]["total"] == 1

    def test_get_database_statistics_exception(self, monitor):
        """Test getting database statistics when exception occurs."""
        # Mock session to raise exception
        with patch.object(monitor.session, "query") as mock_query:
            mock_query.side_effect = Exception("Database error")

            stats = monitor._get_database_statistics()

            assert "error" in stats
            assert stats["error"] == "Database error"
