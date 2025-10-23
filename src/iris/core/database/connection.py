"""Database connection management for Iris project management system.

This module provides database connection management, connection pooling,
and transaction management for the Iris application.
"""

import asyncio
import time
from collections.abc import AsyncGenerator, Generator
from contextlib import asynccontextmanager, contextmanager
from datetime import datetime
from typing import Any

from sqlalchemy import Engine, create_engine, text
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from sqlalchemy.exc import TimeoutError as SQLTimeoutError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from iris.core.utils.error_handler import handle_async_errors, handle_errors
from iris.core.utils.exceptions import IrisConnectionError
from iris.core.utils.logging import get_module_logger

logger = get_module_logger("database")


class DatabaseConnection:
    """Manages database connections and connection pooling.

    This class provides database connection management with connection pooling,
    retry logic, and health checking capabilities.
    """

    def __init__(
        self,
        database_url: str,
        pool_size: int = 5,
        pool_timeout: int = 300,
        pool_recycle: int = 3600,
        echo: bool = False,
        retry_attempts: int = 3,
    ) -> None:
        """Initialize database connection.

        Args:
            database_url: Database connection URL
            pool_size: Maximum number of connections in pool
            pool_timeout: Connection pool timeout in seconds
            pool_recycle: Connection pool recycle time in seconds
            echo: Enable SQL echo for debugging
            retry_attempts: Number of retry attempts for failed connections
        """
        self.database_url = database_url
        self.pool_size = pool_size
        self.pool_timeout = pool_timeout
        self.pool_recycle = pool_recycle
        self.echo = echo
        self.retry_attempts = retry_attempts
        self._engine: Engine | None = None
        self._async_engine: AsyncEngine | None = None
        self._session_factory: sessionmaker[Any] | None = None
        self._connection_start_time: datetime | None = None
        self._last_health_check: datetime | None = None

    @handle_errors(reraise=True, context={"operation": "create_engine"})
    def create_engine(self) -> Engine | None:
        """Create SQLAlchemy engine with connection pooling.

        Returns:
            SQLAlchemy engine instance

        Raises:
            ConnectionError: If engine creation fails
        """
        if self._engine is None:
            try:
                self._engine = create_engine(
                    self.database_url,
                    poolclass=QueuePool,
                    pool_size=self.pool_size,
                    pool_timeout=self.pool_timeout,
                    pool_recycle=self.pool_recycle,
                    echo=self.echo,
                    connect_args={"check_same_thread": False}
                    if "sqlite" in self.database_url
                    else {},
                )
                self._connection_start_time = datetime.now()
                logger.info(f"Created database engine with pool_size={self.pool_size}")
            except Exception as e:
                raise IrisConnectionError(
                    message=f"Failed to create database engine: {str(e)}",
                    database_url=self.database_url,
                    original_exception=e,
                ) from e

        return self._engine

    def create_async_engine(self) -> AsyncEngine | None:
        """Create async SQLAlchemy engine with connection pooling.

        Returns:
            Async SQLAlchemy engine instance
        """
        if self._async_engine is None:
            self._async_engine = create_async_engine(
                self.database_url,
                pool_size=self.pool_size,
                pool_timeout=self.pool_timeout,
                pool_recycle=3600,
                echo=False,
            )
            logger.info(f"Created async database engine with pool_size={self.pool_size}")

        return self._async_engine

    def get_session_factory(self) -> sessionmaker[Any] | None:
        """Get session factory for database sessions.

        Returns:
            SQLAlchemy session factory
        """
        if self._session_factory is None:
            engine = self.create_engine()
            self._session_factory = sessionmaker(bind=engine)
            logger.info("Created database session factory")

        return self._session_factory

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[Any, None]:
        """Get database session with automatic cleanup.

        Yields:
            Database session
        """
        session_factory = self.get_session_factory()
        if session_factory is None:
            raise RuntimeError("Session factory not initialized")
        session = session_factory()
        try:
            yield session
            await session.commit()
        except Exception as e:
            await session.rollback()
            logger.error(f"Database session error: {e}")
            raise
        finally:
            session.close()

    @handle_async_errors(reraise=True, context={"operation": "test_connection"})
    async def test_connection(self) -> bool | None:
        """Test database connection with retry logic.

        Returns:
            True if connection is successful, False otherwise

        Raises:
            ConnectionError: If connection test fails after retries
        """
        for attempt in range(self.retry_attempts):
            try:
                start_time = time.time()
                engine = self.create_engine()
                with engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                    duration = time.time() - start_time
                    logger.info(f"Database connection test successful ({duration:.3f}s)")
                    self._last_health_check = datetime.now()
                    return True
            except (SQLAlchemyError, OperationalError, SQLTimeoutError) as e:
                logger.warning(f"Database connection test attempt {attempt + 1} failed: {e}")
                if attempt < self.retry_attempts - 1:
                    await asyncio.sleep(1)  # Wait before retry
                else:
                    logger.error(
                        f"Database connection test failed after {self.retry_attempts} attempts"
                    )
                    raise IrisConnectionError(
                        message=(
                            f"Database connection test failed after {self.retry_attempts} "
                            f"attempts: {str(e)}"
                        ),
                        database_url=self.database_url,
                        timeout=self.pool_timeout,
                        original_exception=e,
                    ) from e
        return False

    async def get_connection_info(self) -> dict[str, Any] | None:
        """Get database connection information.

        Returns:
            Dictionary with connection information
        """
        try:
            engine = self.create_engine()
            pool = engine.pool
            return {
                "database_url": self.database_url,
                "pool_size": pool.size(),
                "checked_in": pool.checkedin(),
                "checked_out": pool.checkedout(),
                "overflow": pool.overflow(),
            }
        except Exception as e:
            logger.error(f"Failed to get connection info: {e}")
            return {}

    @contextmanager
    def transaction(self) -> Generator[Any, None, None]:
        """Context manager for database transactions.

        Yields:
            Database session with transaction
        """
        session_factory = self.get_session_factory()
        if session_factory is None:
            raise RuntimeError("Session factory not initialized")
        session = session_factory()
        try:
            logger.debug("Starting database transaction")
            yield session
            session.commit()
            logger.debug("Database transaction committed")
        except Exception as e:
            session.rollback()
            logger.error(f"Database transaction rolled back: {e}")
            raise
        finally:
            session.close()

    async def health_check(self) -> dict[str, Any]:
        """Perform comprehensive database health check.

        Returns:
            Dictionary with health check results
        """
        start_time = time.time()
        try:
            # Test basic connectivity
            connection_ok = await self.test_connection()
            if not connection_ok:
                return {
                    "status": "unhealthy",
                    "error": "Connection test failed",
                    "response_time": None,
                    "timestamp": datetime.now().isoformat(),
                }

            # Get connection pool info
            pool_info = await self.get_connection_info()

            # Test query performance
            engine = self.create_engine()
            with engine.connect() as conn:
                start_query = time.time()
                try:
                    result = conn.execute(text("SELECT COUNT(*) FROM projects"))
                    query_time = time.time() - start_query
                    project_count = result.scalar()
                except Exception as e:
                    # If tables don't exist yet, that's okay for health check
                    if "no such table" in str(e).lower():
                        query_time = time.time() - start_query
                        project_count = 0
                    else:
                        raise

            total_time = time.time() - start_time

            return {
                "status": "healthy",
                "response_time": total_time,
                "query_time": query_time,
                "project_count": project_count,
                "pool_info": pool_info,
                "timestamp": datetime.now().isoformat(),
            }

        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return {
                "status": "unhealthy",
                "error": str(e),
                "response_time": time.time() - start_time,
                "timestamp": datetime.now().isoformat(),
            }

    def close(self) -> None:
        """Close database connections and cleanup resources."""
        if self._engine:
            self._engine.dispose()
            logger.info("Closed database engine")
        if self._async_engine:
            asyncio.create_task(self._async_engine.dispose())
            logger.info("Closed async database engine")


# Global database connection instance
_db_connection: DatabaseConnection | None = None


def get_database_connection() -> DatabaseConnection:
    """Get global database connection instance.

    Returns:
        Database connection instance
    """
    global _db_connection
    if _db_connection is None:
        raise RuntimeError("Database connection not initialized. Call initialize_database() first.")
    return _db_connection


def initialize_database(
    database_url: str,
    pool_size: int = 5,
    pool_timeout: int = 300,
    pool_recycle: int = 3600,
    echo: bool = False,
    retry_attempts: int = 3,
) -> DatabaseConnection:
    """Initialize global database connection.

    Args:
        database_url: Database connection URL
        pool_size: Maximum number of connections in pool
        pool_timeout: Connection pool timeout in seconds
        pool_recycle: Connection pool recycle time in seconds
        echo: Enable SQL echo for debugging

    Returns:
        Database connection instance
    """
    global _db_connection
    _db_connection = DatabaseConnection(
        database_url, pool_size, pool_timeout, pool_recycle, echo, retry_attempts
    )
    logger.info(f"Initialized database connection: {database_url}")
    return _db_connection
