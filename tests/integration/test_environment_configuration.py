"""Integration tests for environment configuration.

This module provides integration tests for environment-specific
configuration in the Iris application.
"""

import os
import tempfile
from unittest.mock import patch

import pytest

from iris.core.config.settings import Settings
from iris.core.database.connection import initialize_database


class TestEnvironmentConfiguration:
    """Test cases for environment-specific configuration."""

    def test_development_environment(self):
        """Test development environment configuration."""
        with patch.dict(
            os.environ,
            {
                "ENVIRONMENT": "development",
                "DATABASE_URL": "sqlite:///./dev_iris.db",
                "LOG_LEVEL": "DEBUG",
                "DEBUG": "true",
            },
        ):
            settings = Settings()

            assert settings.application.environment == "development"
            assert settings.application.debug is True
            assert settings.logging.log_level == "DEBUG"
            assert settings.database.database_url == "sqlite:///./dev_iris.db"
            assert settings.is_development() is True
            assert settings.is_production() is False
            assert settings.is_testing() is False

    def test_production_environment(self):
        """Test production environment configuration."""
        with patch.dict(
            os.environ,
            {
                "ENVIRONMENT": "production",
                "DATABASE_URL": "postgresql://user:pass@localhost:5432/iris_prod",
                "DB_PASSWORD": "secure_password",
                "LOG_LEVEL": "WARNING",
                "DEBUG": "false",
            },
        ):
            settings = Settings()

            assert settings.application.environment == "production"
            assert settings.application.debug is False
            assert settings.logging.log_level == "WARNING"
            assert (
                settings.database.database_url == "postgresql://user:pass@localhost:5432/iris_prod"
            )
            assert settings.database.db_password == "secure_password"
            assert settings.is_development() is False
            assert settings.is_production() is True
            assert settings.is_testing() is False

    def test_testing_environment(self):
        """Test testing environment configuration."""
        with patch.dict(
            os.environ,
            {
                "ENVIRONMENT": "testing",
                "DATABASE_URL": "sqlite:///:memory:",
                "LOG_LEVEL": "ERROR",
                "DEBUG": "false",
            },
        ):
            settings = Settings()

            assert settings.application.environment == "testing"
            assert settings.application.debug is False
            assert settings.logging.log_level == "ERROR"
            assert settings.database.database_url == "sqlite:///:memory:"
            assert settings.is_development() is False
            assert settings.is_production() is False
            assert settings.is_testing() is True

    def test_environment_file_loading(self):
        """Test loading configuration from environment file."""
        env_content = """
# Development Environment
ENVIRONMENT=development
DATABASE_URL=sqlite:///./iris_dev.db
DB_POOL_SIZE=3
LOG_LEVEL=DEBUG
DEBUG=true
API_HOST=127.0.0.1
API_PORT=8000
CLI_VERBOSE=true
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(env_content)
            env_file = f.name

        try:
            settings = Settings(env_file=env_file)

            assert settings.application.environment == "development"
            assert settings.application.debug is True
            assert settings.database.database_url == "sqlite:///./iris_dev.db"
            assert settings.database.db_pool_size == 3
            assert settings.logging.log_level == "DEBUG"
            assert settings.application.api_host == "127.0.0.1"
            assert settings.application.api_port == 8000
            assert settings.application.cli_verbose is True
        finally:
            os.unlink(env_file)

    def test_environment_file_override(self):
        """Test environment variables override file settings."""
        env_content = """
DATABASE_URL=sqlite:///./file_iris.db
LOG_LEVEL=INFO
ENVIRONMENT=development
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(env_content)
            env_file = f.name

        try:
            with patch.dict(
                os.environ, {"DATABASE_URL": "sqlite:///./env_iris.db", "LOG_LEVEL": "DEBUG"}
            ):
                settings = Settings(env_file=env_file)

                # Environment variables should override file settings
                assert settings.database.database_url == "sqlite:///./env_iris.db"
                assert settings.logging.log_level == "DEBUG"
                # File setting should still be used for non-overridden values
                assert settings.application.environment == "development"
        finally:
            os.unlink(env_file)

    def test_database_connection_with_environment(self):
        """Test database connection with environment-specific configuration."""
        with patch.dict(
            os.environ,
            {
                "DATABASE_URL": "sqlite:///./test_iris.db",
                "DB_POOL_SIZE": "3",
                "DB_POOL_TIMEOUT": "60",
            },
        ):
            settings = Settings()

            # Initialize database with environment settings
            connection = initialize_database(
                settings.get_database_url(),
                pool_size=settings.get_connection_pool_config()["pool_size"],
                pool_timeout=settings.get_connection_pool_config()["pool_timeout"],
            )

            assert connection.database_url == "sqlite:///./test_iris.db"
            assert connection.pool_size == 3
            assert connection.pool_timeout == 60

    def test_logging_configuration_with_environment(self):
        """Test logging configuration with environment-specific settings."""
        with patch.dict(
            os.environ,
            {
                "LOG_LEVEL": "WARNING",
                "LOG_FILE": "/tmp/iris.log",
                "LOG_MAX_SIZE": "5242880",
                "LOG_BACKUP_COUNT": "3",
            },
        ):
            settings = Settings()
            config = settings.get_logging_config()

            assert config["level"] == "WARNING"
            assert config["file"] == "/tmp/iris.log"
            assert config["max_size"] == 5242880
            assert config["backup_count"] == 3

    def test_api_configuration_with_environment(self):
        """Test API configuration with environment-specific settings."""
        with patch.dict(
            os.environ, {"API_HOST": "0.0.0.0", "API_PORT": "9000", "API_WORKERS": "4"}
        ):
            settings = Settings()

            assert settings.application.api_host == "0.0.0.0"
            assert settings.application.api_port == 9000
            assert settings.application.api_workers == 4

    def test_cli_configuration_with_environment(self):
        """Test CLI configuration with environment-specific settings."""
        with patch.dict(os.environ, {"CLI_TIMEOUT": "60", "CLI_VERBOSE": "true"}):
            settings = Settings()

            assert settings.application.cli_timeout == 60
            assert settings.application.cli_verbose is True

    def test_production_validation(self):
        """Test production environment validation."""
        with (
            patch.dict(
                os.environ,
                {
                    "ENVIRONMENT": "production",
                    "DATABASE_URL": "sqlite:///./.iris/iris.db",
                    "DB_PASSWORD": "",
                },
            ),
            pytest.raises(ValueError, match="SQLite is not recommended for production"),
        ):
            # Should raise validation error for production with SQLite during initialization
            settings = Settings()

        with patch.dict(
            os.environ,
            {
                "ENVIRONMENT": "production",
                "DATABASE_URL": "postgresql://user:pass@localhost:5432/iris",
                "DB_PASSWORD": "password123",  # pragma: allowlist secret
            },
        ):
            settings = Settings()

            # Should not raise validation error for production with PostgreSQL and password
            settings._validate_configuration()

    def test_development_validation(self):
        """Test development environment validation."""
        with patch.dict(
            os.environ, {"ENVIRONMENT": "development", "DATABASE_URL": "sqlite:///./.iris/iris.db"}
        ):
            settings = Settings()

            # Should not raise validation error for development
            settings._validate_configuration()

    def test_testing_validation(self):
        """Test testing environment validation."""
        with patch.dict(
            os.environ, {"ENVIRONMENT": "testing", "DATABASE_URL": "sqlite:///:memory:"}
        ):
            settings = Settings()

            # Should not raise validation error for testing
            settings._validate_configuration()

    def test_environment_specific_database_urls(self):
        """Test environment-specific database URL generation."""
        # Development environment
        with patch.dict(
            os.environ,
            {
                "ENVIRONMENT": "development",
                "DB_HOST": "localhost",
                "DB_PORT": "5432",
                "DB_NAME": "iris",  # Use 'iris' to trigger SQLite logic
                "DB_USER": "dev_user",
                "DB_PASSWORD": "dev_pass",
            },
        ):
            settings = Settings()
            # Should use SQLite for local development
            assert settings.database.database_url == "sqlite:///./.iris/iris.db"

        # Production environment
        with patch.dict(
            os.environ,
            {
                "ENVIRONMENT": "production",
                "DB_HOST": "prod-db.example.com",
                "DB_PORT": "5432",
                "DB_NAME": "iris_prod",
                "DB_USER": "prod_user",
                "DB_PASSWORD": "prod_pass",
            },
        ):
            settings = Settings()
            # Should use PostgreSQL for production
            expected_url = "postgresql://prod_user:prod_pass@prod-db.example.com:5432/iris_prod"
            assert settings.database.database_url == expected_url

    def test_connection_pool_environment_configuration(self):
        """Test connection pool configuration with environment variables."""
        with patch.dict(
            os.environ,
            {
                "DB_POOL_SIZE": "10",
                "DB_POOL_TIMEOUT": "600",
                "DB_POOL_RECYCLE": "7200",
                "DB_ECHO": "true",
            },
        ):
            settings = Settings()
            config = settings.get_connection_pool_config()

            assert config["pool_size"] == 10
            assert config["pool_timeout"] == 600
            assert config["pool_recycle"] == 7200
            assert config["echo"] is True

    def test_application_info_environment_configuration(self):
        """Test application info configuration with environment variables."""
        with patch.dict(os.environ, {"APP_NAME": "Iris Production", "APP_VERSION": "1.0.0"}):
            settings = Settings()

            assert settings.application.app_name == "Iris Production"
            assert settings.application.app_version == "1.0.0"

    def test_environment_configuration_integration(self):
        """Test complete environment configuration integration."""
        env_content = """
# Complete Environment Configuration
ENVIRONMENT=production
DATABASE_URL=postgresql://user:pass@localhost:5432/iris_prod
DB_PASSWORD=secure_password  # pragma: allowlist secret
DB_POOL_SIZE=20
DB_POOL_TIMEOUT=900
LOG_LEVEL=WARNING
LOG_FILE=/var/log/iris/iris.log
LOG_MAX_SIZE=20971520
LOG_BACKUP_COUNT=10
DEBUG=false
APP_NAME=Iris Production
APP_VERSION=1.0.0
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=4
CLI_TIMEOUT=60
CLI_VERBOSE=false
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(env_content)
            env_file = f.name

        try:
            settings = Settings(env_file=env_file)

            # Validate all settings
            assert settings.application.environment == "production"
            assert (
                settings.database.database_url == "postgresql://user:pass@localhost:5432/iris_prod"
            )
            assert settings.database.db_password == "secure_password"
            assert settings.database.db_pool_size == 20
            assert settings.database.db_pool_timeout == 900
            assert settings.logging.log_level == "WARNING"
            assert settings.logging.log_file == "/var/log/iris/iris.log"
            assert settings.logging.log_max_size == 20971520
            assert settings.logging.log_backup_count == 10
            assert settings.application.debug is False
            assert settings.application.app_name == "Iris Production"
            assert settings.application.app_version == "1.0.0"
            assert settings.application.api_host == "0.0.0.0"
            assert settings.application.api_port == 8000
            assert settings.application.api_workers == 4
            assert settings.application.cli_timeout == 60
            assert settings.application.cli_verbose is False

            # Validate configuration
            settings._validate_configuration()  # Should not raise

            # Test environment checks
            assert settings.is_production() is True
            assert settings.is_development() is False
            assert settings.is_testing() is False
        finally:
            os.unlink(env_file)
