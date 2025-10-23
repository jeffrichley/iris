"""Unit tests for configuration management.

This module provides unit tests for the configuration management
in the Iris application.
"""

import os
import tempfile

import pytest

from iris.core.config.settings import (
    ApplicationSettings,
    DatabaseSettings,
    LoggingSettings,
    Settings,
    get_settings,
    initialize_settings,
)


class TestDatabaseSettings:
    """Test cases for DatabaseSettings class."""

    def test_default_database_settings(self):
        """Test default database settings."""
        settings = DatabaseSettings()

        assert settings.database_url == "sqlite:///./.iris/iris.db"
        assert settings.db_host == "localhost"
        assert settings.db_port == 5432
        assert settings.db_name == "iris"
        assert settings.db_user == "iris_user"
        assert settings.db_password == ""
        assert settings.db_pool_size == 5
        assert settings.db_pool_timeout == 300
        assert settings.db_echo is False
        assert settings.db_pool_recycle == 3600

    def test_database_url_validation(self):
        """Test database URL validation."""
        # Test SQLite URL
        settings = DatabaseSettings(database_url="sqlite:///test.db")
        assert settings.database_url == "sqlite:///test.db"

        # Test PostgreSQL URL
        settings = DatabaseSettings(database_url="postgresql://user:pass@localhost:5432/db")
        assert settings.database_url == "postgresql://user:pass@localhost:5432/db"

        # Test URL building from components
        settings = DatabaseSettings(
            db_host="example.com",
            db_port=3306,
            db_name="testdb",
            db_user="testuser",
            db_password="testpass",
        )
        assert settings.database_url == "postgresql://testuser:testpass@example.com:3306/testdb"

    def test_connection_pool_settings(self):
        """Test connection pool settings."""
        settings = DatabaseSettings(db_pool_size=10, db_pool_timeout=600, db_pool_recycle=7200)

        assert settings.db_pool_size == 10
        assert settings.db_pool_timeout == 600
        assert settings.db_pool_recycle == 7200

    def test_database_echo_setting(self):
        """Test database echo setting."""
        settings = DatabaseSettings(db_echo=True)
        assert settings.db_echo is True

        settings = DatabaseSettings(db_echo=False)
        assert settings.db_echo is False


class TestLoggingSettings:
    """Test cases for LoggingSettings class."""

    def test_default_logging_settings(self):
        """Test default logging settings."""
        settings = LoggingSettings()

        assert settings.log_level == "INFO"
        assert settings.log_format == "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        assert settings.log_file is None
        assert settings.log_max_size == 10485760  # 10MB
        assert settings.log_backup_count == 5

    def test_log_level_validation(self):
        """Test log level validation."""
        # Test valid log levels
        for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            settings = LoggingSettings(log_level=level)
            assert settings.log_level == level

        # Test case insensitive
        settings = LoggingSettings(log_level="debug")
        assert settings.log_level == "DEBUG"

        # Test invalid log level
        with pytest.raises(ValueError, match="Invalid log level"):
            LoggingSettings(log_level="INVALID")

    def test_log_file_setting(self):
        """Test log file setting."""
        settings = LoggingSettings(log_file="/tmp/test.log")
        assert settings.log_file == "/tmp/test.log"

        settings = LoggingSettings(log_file=None)
        assert settings.log_file is None

    def test_log_rotation_settings(self):
        """Test log rotation settings."""
        settings = LoggingSettings(
            log_max_size=20971520,  # 20MB
            log_backup_count=10,
        )

        assert settings.log_max_size == 20971520
        assert settings.log_backup_count == 10


class TestApplicationSettings:
    """Test cases for ApplicationSettings class."""

    def test_default_application_settings(self):
        """Test default application settings."""
        settings = ApplicationSettings()

        assert settings.environment == "development"
        assert settings.debug is False
        assert settings.app_name == "Iris"
        assert settings.app_version == "0.1.0"
        assert settings.api_host == "127.0.0.1"
        assert settings.api_port == 8000
        assert settings.api_workers == 1
        assert settings.cli_timeout == 30
        assert settings.cli_verbose is False

    def test_environment_validation(self):
        """Test environment validation."""
        # Test valid environments
        for env in ["development", "testing", "production"]:
            settings = ApplicationSettings(environment=env)
            assert settings.environment == env

        # Test case insensitive
        settings = ApplicationSettings(environment="DEVELOPMENT")
        assert settings.environment == "development"

        # Test invalid environment
        with pytest.raises(ValueError, match="Invalid environment"):
            ApplicationSettings(environment="invalid")

    def test_debug_setting(self):
        """Test debug setting."""
        settings = ApplicationSettings(debug=True)
        assert settings.debug is True

        settings = ApplicationSettings(debug=False)
        assert settings.debug is False

    def test_api_settings(self):
        """Test API settings."""
        settings = ApplicationSettings(api_host="0.0.0.0", api_port=9000, api_workers=4)

        assert settings.api_host == "0.0.0.0"
        assert settings.api_port == 9000
        assert settings.api_workers == 4

    def test_cli_settings(self):
        """Test CLI settings."""
        settings = ApplicationSettings(cli_timeout=60, cli_verbose=True)

        assert settings.cli_timeout == 60
        assert settings.cli_verbose is True


class TestSettings:
    """Test cases for Settings class."""

    def test_default_settings(self):
        """Test default settings initialization."""
        settings = Settings()

        assert settings.database is not None
        assert settings.logging is not None
        assert settings.application is not None

        # Test database settings
        assert settings.database.database_url == "sqlite:///./.iris/iris.db"
        assert settings.database.db_pool_size == 5

        # Test logging settings
        assert settings.logging.log_level == "INFO"

        # Test application settings
        assert settings.application.environment == "development"
        assert settings.application.debug is False

    def test_environment_file_loading(self):
        """Test environment file loading."""
        env_content = """
DATABASE_URL=postgresql://user:pass@localhost:5432/testdb
DB_PASSWORD=secure_password
DB_POOL_SIZE=10
LOG_LEVEL=DEBUG
ENVIRONMENT=production
DEBUG=true
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(env_content)
            env_file = f.name

        try:
            settings = Settings(env_file=env_file)

            assert settings.database.database_url == "postgresql://user:pass@localhost:5432/testdb"
            assert settings.database.db_pool_size == 10
            assert settings.logging.log_level == "DEBUG"
            assert settings.application.environment == "production"
            assert settings.application.debug is True
        finally:
            os.unlink(env_file)

    def test_environment_file_not_found(self):
        """Test behavior when environment file is not found."""
        # Should not raise an error, just use defaults
        settings = Settings(env_file="nonexistent.env")

        assert settings.database.database_url == "sqlite:///./.iris/iris.db"
        assert settings.logging.log_level == "INFO"
        assert settings.application.environment == "development"

    def test_auto_detect_env_file(self):
        """Test automatic .env file detection."""
        env_content = """
DATABASE_URL=sqlite:///auto_detected.db
LOG_LEVEL=WARNING
ENVIRONMENT=development
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(env_content)
            env_file = f.name

        try:
            # Copy to current directory as .env
            import shutil

            shutil.copy(env_file, ".env")

            settings = Settings()

            assert settings.database.database_url == "sqlite:///auto_detected.db"
            assert settings.logging.log_level == "WARNING"
        finally:
            os.unlink(env_file)
            if os.path.exists(".env"):
                os.unlink(".env")

    def test_configuration_validation(self):
        """Test configuration validation."""
        # Test valid configuration
        settings = Settings()
        settings._validate_configuration()  # Should not raise

        # Test production configuration validation
        settings.application.environment = "production"
        settings.database.database_url = "postgresql://user:pass@localhost:5432/db"
        settings.database.db_password = "secure_password"
        settings._validate_configuration()  # Should not raise

        # Test invalid production configuration
        settings.database.database_url = "sqlite:///./.iris/iris.db"
        with pytest.raises(ValueError, match="SQLite is not recommended for production"):
            settings._validate_configuration()

        settings.database.database_url = "postgresql://user:pass@localhost:5432/db"
        settings.database.db_password = ""
        with pytest.raises(ValueError, match="Database password is required for production"):
            settings._validate_configuration()

    def test_get_database_url(self):
        """Test getting database URL."""
        settings = Settings()
        url = settings.get_database_url()

        assert url == "sqlite:///./.iris/iris.db"

        settings.database.database_url = "postgresql://user:pass@localhost:5432/db"
        url = settings.get_database_url()
        assert url == "postgresql://user:pass@localhost:5432/db"

    def test_get_connection_pool_config(self):
        """Test getting connection pool configuration."""
        settings = Settings()
        config = settings.get_connection_pool_config()

        assert "pool_size" in config
        assert "pool_timeout" in config
        assert "pool_recycle" in config
        assert "echo" in config

        assert config["pool_size"] == 5
        assert config["pool_timeout"] == 300
        assert config["pool_recycle"] == 3600
        assert config["echo"] is False

    def test_get_logging_config(self):
        """Test getting logging configuration."""
        settings = Settings()
        config = settings.get_logging_config()

        assert "level" in config
        assert "format" in config
        assert "file" in config
        assert "max_size" in config
        assert "backup_count" in config

        assert config["level"] == "INFO"
        assert config["file"] is None

    def test_environment_checks(self):
        """Test environment check methods."""
        settings = Settings()

        # Test development environment
        settings.application.environment = "development"
        assert settings.is_development() is True
        assert settings.is_production() is False
        assert settings.is_testing() is False

        # Test production environment
        settings.application.environment = "production"
        assert settings.is_development() is False
        assert settings.is_production() is True
        assert settings.is_testing() is False

        # Test testing environment
        settings.application.environment = "testing"
        assert settings.is_development() is False
        assert settings.is_production() is False
        assert settings.is_testing() is True


class TestGlobalSettings:
    """Test cases for global settings management."""

    def test_get_settings(self):
        """Test getting global settings."""
        # Reset global settings
        import src.iris.core.config.settings as settings_module

        settings_module._settings = None

        settings = get_settings()
        assert settings is not None
        assert isinstance(settings, Settings)

        # Should return same instance
        settings2 = get_settings()
        assert settings is settings2

    def test_initialize_settings(self):
        """Test initializing global settings."""
        # Reset global settings
        import src.iris.core.config.settings as settings_module

        settings_module._settings = None

        settings = initialize_settings()
        assert settings is not None
        assert isinstance(settings, Settings)

        # Should be the global instance
        global_settings = get_settings()
        assert settings is global_settings

    def test_initialize_settings_with_env_file(self):
        """Test initializing settings with environment file."""
        env_content = """
DATABASE_URL=sqlite:///test.db
LOG_LEVEL=DEBUG
ENVIRONMENT=testing
"""

        with tempfile.NamedTemporaryFile(mode="w", suffix=".env", delete=False) as f:
            f.write(env_content)
            env_file = f.name

        try:
            # Reset global settings
            import src.iris.core.config.settings as settings_module

            settings_module._settings = None

            settings = initialize_settings(env_file)

            assert settings.database.database_url == "sqlite:///test.db"
            assert settings.logging.log_level == "DEBUG"
            assert settings.application.environment == "testing"
        finally:
            os.unlink(env_file)


class TestSettingsIntegration:
    """Integration tests for settings."""

    def test_settings_consistency(self):
        """Test settings consistency across different initialization methods."""
        settings1 = Settings()
        settings2 = Settings()

        # Should have same default values
        assert settings1.database.database_url == settings2.database.database_url
        assert settings1.logging.log_level == settings2.logging.log_level
        assert settings1.application.environment == settings2.application.environment

    def test_settings_immutability(self):
        """Test that settings are properly isolated."""
        settings1 = Settings()
        settings2 = Settings()

        # Modify settings1
        settings1.database.db_pool_size = 10

        # settings2 should not be affected
        assert settings2.database.db_pool_size == 5

    def test_settings_validation_integration(self):
        """Test settings validation in integration context."""
        # Test valid configuration
        settings = Settings()
        settings._validate_configuration()

        # Test invalid configuration
        settings.database.database_url = ""
        with pytest.raises(ValueError, match="Database URL is required"):
            settings._validate_configuration()

    def test_environment_specific_configuration(self):
        """Test environment-specific configuration."""
        # Test development configuration
        settings = Settings()
        settings.application.environment = "development"
        assert settings.is_development() is True

        # Test production configuration
        settings.application.environment = "production"
        settings.database.database_url = "postgresql://user:pass@localhost:5432/db"
        settings.database.db_password = "secure_password"
        assert settings.is_production() is True

        # Test testing configuration
        settings.application.environment = "testing"
        assert settings.is_testing() is True
