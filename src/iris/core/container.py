"""Dependency injection container for Iris using dependency-injector.

This module provides a clean dependency injection setup using the
python-dependency-injector framework.
"""

from dependency_injector import containers, providers

from iris.core.config.logging_config import IrisLoggingConfig
from iris.core.config.settings import Settings
from iris.core.database.connection import DatabaseConnection
from iris.core.database.services import IdeaService, ProjectService, TaskService
from iris.core.utils.error_handler import ErrorHandler


class Container(containers.DeclarativeContainer):
    """Main application container with all dependencies."""

    # Configuration
    config = providers.Configuration()

    # Core services
    settings = providers.Singleton(Settings)
    error_handler = providers.Singleton(ErrorHandler)
    logging_config = providers.Singleton(
        IrisLoggingConfig,
        environment=config.environment,
    )

    # Database connection
    database_connection = providers.Singleton(
        DatabaseConnection,
        database_url=settings.provided.database_url,
        pool_size=settings.provided.pool_size,
        pool_timeout=settings.provided.pool_timeout,
        pool_recycle=settings.provided.pool_recycle,
        echo=settings.provided.echo,
        retry_attempts=settings.provided.retry_attempts,
    )

    # Database services (these need session injection)
    project_service = providers.Factory(
        ProjectService,
        session=providers.Dependency(),
    )

    task_service = providers.Factory(
        TaskService,
        session=providers.Dependency(),
    )

    idea_service = providers.Factory(
        IdeaService,
        session=providers.Dependency(),
    )


# Global container instance
container = Container()


def configure_container(environment: str = "development") -> Container:
    """Configure the container for the given environment.

    Args:
        environment: Application environment

    Returns:
        Configured container
    """
    container.config.environment.from_value(environment)
    return container


def get_container() -> Container:
    """Get the global container instance.

    Returns:
        Container instance
    """
    return container
