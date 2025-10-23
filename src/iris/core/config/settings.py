"""Configuration management for Iris project management system.

This module provides environment-specific configuration management
and settings for the Iris application.
"""

from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """Database configuration settings."""

    model_config = SettingsConfigDict(extra="allow")

    # Database connection
    database_url: str = Field(default="sqlite:///./.iris/iris.db")
    db_host: str = Field(default="localhost")
    db_port: int = Field(default=5432)
    db_name: str = Field(default="iris")
    db_user: str = Field(default="iris_user")
    db_password: str = Field(default="")

    # Connection pool settings
    db_pool_size: int = Field(default=5)
    db_pool_timeout: int = Field(default=300)

    # Database options
    db_echo: bool = Field(default=False)
    db_pool_recycle: int = Field(default=3600)

    @model_validator(mode="before")
    @classmethod
    def build_database_url(cls, data: Any) -> Any:
        """Build database URL from individual components if not provided."""
        if isinstance(data, dict):
            # If a specific URL is provided, use it
            if "database_url" in data and data["database_url"]:
                return data

            # Build URL from components
            host = data.get("db_host", "localhost")
            port = data.get("db_port", 5432)
            name = data.get("db_name", "iris")
            user = data.get("db_user", "iris_user")
            password = data.get("db_password", "")

            if host == "localhost" and name == "iris":
                # Use SQLite for local development
                data["database_url"] = "sqlite:///./.iris/iris.db"
            else:
                # Use PostgreSQL for other configurations
                data["database_url"] = f"postgresql://{user}:{password}@{host}:{port}/{name}"

        return data


class LoggingSettings(BaseSettings):
    """Logging configuration settings."""

    model_config = SettingsConfigDict(extra="allow")

    log_level: str = Field(default="INFO")
    log_format: str = Field(default="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_file: str | None = Field(default=None)
    log_max_size: int = Field(default=10485760)  # 10MB
    log_backup_count: int = Field(default=5)

    @field_validator("log_level")
    @classmethod
    def validate_log_level(cls, v: str) -> str:
        """Validate log level."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if v.upper() not in valid_levels:
            raise ValueError(f"Invalid log level: {v}. Must be one of {valid_levels}")
        return v.upper()


class ApplicationSettings(BaseSettings):
    """Application configuration settings."""

    model_config = SettingsConfigDict(extra="allow")

    # Environment
    environment: str = Field(default="development")
    debug: bool = Field(default=False)

    # Application info
    app_name: str = Field(default="Iris")
    app_version: str = Field(default="0.1.0")

    # API settings
    api_host: str = Field(default="127.0.0.1")
    api_port: int = Field(default=8000)
    api_workers: int = Field(default=1)

    # CLI settings
    cli_timeout: int = Field(default=30)
    cli_verbose: bool = Field(default=False)

    @field_validator("environment")
    @classmethod
    def validate_environment(cls, v: str) -> str:
        """Validate environment setting."""
        valid_envs = ["development", "testing", "production"]
        if v.lower() not in valid_envs:
            raise ValueError(f"Invalid environment: {v}. Must be one of {valid_envs}")
        return v.lower()


class Settings:
    """Main settings class that combines all configuration sections."""

    def __init__(self, env_file: str | None = None):
        """Initialize settings with optional environment file.

        Args:
            env_file: Path to environment file (.env)
        """
        # Load environment file if provided
        if env_file and Path(env_file).exists():
            load_dotenv(env_file)
        elif Path(".env").exists():
            load_dotenv(".env")

        # Initialize configuration sections
        self.database = DatabaseSettings()
        self.logging = LoggingSettings()
        self.application = ApplicationSettings()

        # Validate configuration
        self._validate_configuration()

    def _validate_configuration(self) -> None:
        """Validate configuration settings."""
        # Validate database URL
        if not self.database.database_url:
            raise ValueError("Database URL is required")

        # Validate environment-specific settings
        if self.application.environment == "production":
            if self.database.database_url.startswith("sqlite"):
                raise ValueError("SQLite is not recommended for production")
            if not self.database.db_password:
                raise ValueError("Database password is required for production")

    def get_database_url(self) -> str:
        """Get database URL for current environment.

        Returns:
            Database connection URL
        """
        return self.database.database_url

    def get_connection_pool_config(self) -> dict[str, Any]:
        """Get connection pool configuration.

        Returns:
            Dictionary with pool configuration
        """
        return {
            "pool_size": self.database.db_pool_size,
            "pool_timeout": self.database.db_pool_timeout,
            "pool_recycle": self.database.db_pool_recycle,
            "echo": self.database.db_echo,
        }

    def get_logging_config(self) -> dict[str, Any]:
        """Get logging configuration.

        Returns:
            Dictionary with logging configuration
        """
        return {
            "level": self.logging.log_level,
            "format": self.logging.log_format,
            "file": self.logging.log_file,
            "max_size": self.logging.log_max_size,
            "backup_count": self.logging.log_backup_count,
        }

    def is_development(self) -> bool:
        """Check if running in development environment.

        Returns:
            True if development environment
        """
        return self.application.environment == "development"

    def is_production(self) -> bool:
        """Check if running in production environment.

        Returns:
            True if production environment
        """
        return self.application.environment == "production"

    def is_testing(self) -> bool:
        """Check if running in testing environment.

        Returns:
            True if testing environment
        """
        return self.application.environment == "testing"


# Global settings instance
_settings: Settings | None = None


def get_settings() -> Settings:
    """Get global settings instance.

    Returns:
        Settings instance
    """
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings


def initialize_settings(env_file: str | None = None) -> Settings:
    """Initialize global settings with optional environment file.

    Args:
        env_file: Path to environment file (.env)

    Returns:
        Settings instance
    """
    global _settings
    _settings = Settings(env_file)
    return _settings
