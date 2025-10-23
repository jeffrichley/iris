"""Pytest configuration and fixtures for Iris test suite."""

import pytest
from rich.console import Console


@pytest.fixture
def sample_fixture():
    """Sample fixture for testing."""
    return "test_data"


@pytest.fixture
def console():
    """Rich console fixture for testing."""
    return Console()


@pytest.fixture(autouse=True)
def reset_global_settings():
    """Reset global settings between tests to prevent test interference."""
    import os

    import src.iris.core.config.settings as settings_module

    # Store original state
    original_settings = settings_module._settings

    # Store original environment variables that might be set by tests
    env_vars_to_clear = [
        "DATABASE_URL",
        "DB_HOST",
        "DB_PORT",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
        "DB_POOL_SIZE",
        "DB_POOL_TIMEOUT",
        "DB_ECHO",
        "DB_POOL_RECYCLE",
        "LOG_LEVEL",
        "LOG_FILE",
        "LOG_MAX_SIZE",
        "LOG_BACKUP_COUNT",
        "ENVIRONMENT",
        "DEBUG",
        "APP_NAME",
        "APP_VERSION",
        "API_HOST",
        "API_PORT",
        "API_WORKERS",
        "CLI_TIMEOUT",
        "CLI_VERBOSE",
    ]

    original_env = {}
    for var in env_vars_to_clear:
        original_env[var] = os.environ.get(var)
        if var in os.environ:
            del os.environ[var]

    # Reset to None before each test
    settings_module._settings = None

    yield

    # Restore original state after each test
    settings_module._settings = original_settings

    # Restore original environment variables
    for var, value in original_env.items():
        if value is not None:
            os.environ[var] = value
        elif var in os.environ:
            del os.environ[var]


@pytest.fixture(autouse=True)
def reset_database_connections():
    """Reset database connections between tests to prevent test interference."""
    import src.iris.core.database.connection as connection_module

    # Store original state
    original_connection = connection_module._db_connection

    # Reset to None before each test
    connection_module._db_connection = None

    yield

    # Restore original state after each test
    connection_module._db_connection = original_connection
