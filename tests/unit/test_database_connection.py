"""Unit tests for database connection management.

This module provides unit tests for the database connection functionality
in the Iris application.
"""

from unittest.mock import patch

import pytest
from sqlalchemy.exc import OperationalError

from iris.core.database.connection import (
    DatabaseConnection,
    get_database_connection,
    initialize_database,
)
from iris.core.database.models import Base
from iris.core.utils.exceptions import IrisConnectionError


class TestDatabaseConnection:
    """Test cases for DatabaseConnection class."""

    def test_initialization(self):
        """Test database connection initialization."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url, pool_size=3, pool_timeout=60)

        assert connection.database_url == db_url
        assert connection.pool_size == 3
        assert connection.pool_timeout == 60
        assert connection.retry_attempts == 3
        assert connection._engine is None
        assert connection._session_factory is None

    def test_create_engine(self):
        """Test engine creation."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        engine = connection.create_engine()

        assert engine is not None
        assert connection._engine is engine
        assert connection._connection_start_time is not None

    def test_get_session_factory(self):
        """Test session factory creation."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        session_factory = connection.get_session_factory()

        assert session_factory is not None
        assert connection._session_factory is session_factory

    @pytest.mark.asyncio
    async def test_test_connection_success(self):
        """Test successful connection test."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        result = await connection.test_connection()

        assert result is True
        assert connection._last_health_check is not None

    @pytest.mark.asyncio
    async def test_test_connection_failure(self):
        """Test connection test failure."""
        db_url = "sqlite:///nonexistent.db"
        connection = DatabaseConnection(db_url, retry_attempts=1)

        with patch("iris.core.database.connection.create_engine") as mock_engine:
            mock_engine.return_value.connect.side_effect = OperationalError(
                "Connection failed", None, None
            )

            with pytest.raises(IrisConnectionError):
                await connection.test_connection()

    @pytest.mark.asyncio
    async def test_test_connection_retry(self):
        """Test connection test with retries."""
        db_url = "sqlite:///nonexistent.db"
        connection = DatabaseConnection(db_url, retry_attempts=3)

        with patch("iris.core.database.connection.create_engine") as mock_engine:
            mock_engine.return_value.connect.side_effect = OperationalError(
                "Connection failed", None, None
            )

            with patch("asyncio.sleep") as mock_sleep:
                with pytest.raises(IrisConnectionError):
                    await connection.test_connection()

                assert mock_sleep.call_count == 2  # 2 retries

    def test_transaction_context_manager(self):
        """Test transaction context manager."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        with connection.transaction() as session:
            assert session is not None
            # Session should be active during transaction
            assert session.is_active

    def test_transaction_rollback(self):
        """Test transaction rollback on error."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        with pytest.raises(ValueError), connection.transaction() as session:
            # Session should be active during transaction
            assert session.is_active
            raise ValueError("Test error")

    @pytest.mark.asyncio
    async def test_health_check_healthy(self):
        """Test health check when database is healthy."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        # Create tables for health check
        engine = connection.create_engine()
        Base.metadata.create_all(engine)

        result = await connection.health_check()

        assert result["status"] == "healthy"
        assert "response_time" in result
        assert "query_time" in result
        assert "project_count" in result
        assert "pool_info" in result
        assert "timestamp" in result

    @pytest.mark.asyncio
    async def test_health_check_unhealthy(self):
        """Test health check when database is unhealthy."""
        db_url = "sqlite:///nonexistent.db"
        connection = DatabaseConnection(db_url, retry_attempts=1)

        with patch("iris.core.database.connection.create_engine") as mock_engine:
            mock_engine.return_value.connect.side_effect = OperationalError(
                "Connection failed", None, None
            )

            result = await connection.health_check()

            assert result["status"] == "unhealthy"
            assert "error" in result
            assert "response_time" in result
            assert "timestamp" in result

    @pytest.mark.asyncio
    async def test_get_connection_info(self):
        """Test getting connection information."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        info = await connection.get_connection_info()

        assert "database_url" in info
        assert "pool_size" in info
        assert "checked_in" in info
        assert "checked_out" in info
        assert "overflow" in info

    def test_close(self):
        """Test closing database connections."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        # Create engine first
        connection.create_engine()

        # Mock the dispose method
        with patch.object(connection._engine, "dispose") as mock_dispose:
            connection.close()
            mock_dispose.assert_called_once()


class TestGlobalDatabaseConnection:
    """Test cases for global database connection management."""

    def test_initialize_database(self):
        """Test database initialization."""
        db_url = "sqlite:///:memory:"
        connection = initialize_database(db_url, pool_size=3)

        assert connection is not None
        assert connection.database_url == db_url
        assert connection.pool_size == 3

    def test_get_database_connection(self):
        """Test getting database connection."""
        db_url = "sqlite:///:memory:"
        initialize_database(db_url)

        connection = get_database_connection()

        assert connection is not None
        assert connection.database_url == db_url

    def test_get_database_connection_not_initialized(self):
        """Test getting database connection when not initialized."""
        # Reset global connection
        import iris.core.database.connection as conn_module

        conn_module._db_connection = None

        with pytest.raises(RuntimeError, match="Database connection not initialized"):
            get_database_connection()


class TestDatabaseConnectionIntegration:
    """Integration tests for database connection."""

    def test_full_connection_lifecycle(self):
        """Test complete connection lifecycle."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        # Create engine
        engine = connection.create_engine()
        assert engine is not None

        # Create session factory
        session_factory = connection.get_session_factory()
        assert session_factory is not None

        # Test session creation
        session = session_factory()
        assert session is not None
        session.close()

        # Test transaction
        with connection.transaction() as session:
            assert session is not None

        # Close connection
        connection.close()

    @pytest.mark.asyncio
    async def test_async_connection_lifecycle(self):
        """Test async connection lifecycle."""
        db_url = "sqlite:///:memory:"
        connection = DatabaseConnection(db_url)

        # Test connection
        result = await connection.test_connection()
        assert result is True

        # Test health check
        health = await connection.health_check()
        assert health["status"] == "healthy"

        # Test connection info
        info = await connection.get_connection_info()
        assert "database_url" in info
