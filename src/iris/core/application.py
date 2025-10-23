"""Main application initialization for Iris project management system.

This module provides the main application initialization and configuration
for the Iris application.
"""

import os
from typing import Any

from iris.core.config.logging_config import initialize_logging
from iris.core.config.settings import Settings, initialize_settings
from iris.core.database.connection import DatabaseConnection, initialize_database
from iris.core.utils.error_handler import ErrorHandler


class IrisApplication:
    """Main Iris application class."""

    def __init__(self, environment: str | None = None):
        """Initialize Iris application.

        Args:
            environment: Application environment (defaults to IRIS_ENV env var)
        """
        self.environment = environment or os.getenv("IRIS_ENV", "development")
        self.settings: Settings | None = None
        self.logging_config: Any = None
        self.db_connection: DatabaseConnection | None = None
        self.error_handler: ErrorHandler | None = None
        self._initialized = False

    def initialize(self, env_file: str | None = None) -> "IrisApplication":
        """Initialize the application with all required components.

        Args:
            env_file: Path to environment file (.env)

        Returns:
            Initialized application instance
        """
        if self._initialized:
            return self

        try:
            # Initialize logging first
            initialize_logging(self.environment)
            self.logging_config = None  # Logging is configured globally

            # Initialize settings
            self.settings = initialize_settings(env_file)

            # Initialize error handling
            self.error_handler = ErrorHandler()

            # Initialize database connection
            self.db_connection = initialize_database(
                self.settings.get_database_url(), **self.settings.get_connection_pool_config()
            )

            self._initialized = True

        except Exception as e:
            # If initialization fails, we still want to log the error
            if self.logging_config:
                import logging

                logger = logging.getLogger("iris")
                logger.error(f"Application initialization failed: {e}")
            raise

        return self

    def get_settings(self) -> Settings:
        """Get application settings.

        Returns:
            Application settings instance
        """
        if not self._initialized:
            raise RuntimeError("Application not initialized. Call initialize() first.")
        if self.settings is None:
            raise RuntimeError("Application settings not properly initialized.")
        return self.settings

    def get_database_connection(self) -> DatabaseConnection:
        """Get database connection.

        Returns:
            Database connection instance
        """
        if not self._initialized:
            raise RuntimeError("Application not initialized. Call initialize() first.")
        if self.db_connection is None:
            raise RuntimeError("Database connection not properly initialized.")
        return self.db_connection

    def get_error_handler(self) -> ErrorHandler:
        """Get error handler.

        Returns:
            Error handler instance
        """
        if not self._initialized:
            raise RuntimeError("Application not initialized. Call initialize() first.")
        if self.error_handler is None:
            raise RuntimeError("Error handler not properly initialized.")
        return self.error_handler

    def shutdown(self) -> None:
        """Shutdown the application and cleanup resources."""
        if self.db_connection:
            self.db_connection.close()

        self._initialized = False


# Global application instance
_app: IrisApplication | None = None


def get_application() -> IrisApplication:
    """Get global application instance.

    Returns:
        Global application instance
    """
    global _app
    if _app is None:
        _app = IrisApplication()
    return _app


def initialize_application(
    environment: str | None = None, env_file: str | None = None
) -> IrisApplication:
    """Initialize the global application instance.

    Args:
        environment: Application environment
        env_file: Path to environment file

    Returns:
        Initialized application instance
    """
    global _app
    _app = IrisApplication(environment)
    _app.initialize(env_file)
    return _app


def shutdown_application() -> None:
    """Shutdown the global application instance."""
    global _app
    if _app:
        _app.shutdown()
        _app = None


def ensure_application_initialized() -> IrisApplication:
    """Ensure application is initialized, initialize if not.

    Returns:
        Initialized application instance
    """
    app = get_application()
    if not app._initialized:
        app.initialize()
    return app
