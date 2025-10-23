"""Logging configuration for Iris project management system.

This module provides centralized logging configuration and setup
for the Iris application across all environments.
"""

import os
from pathlib import Path
from typing import Any

from iris.core.utils.logging import setup_logging


class IrisLoggingConfig:
    """Iris-specific logging configuration manager."""

    def __init__(self, environment: str = "development"):
        """Initialize logging configuration.

        Args:
            environment: Application environment (development, staging, production)
        """
        self.environment = environment
        self.config = self._get_config_for_environment()

    def _get_config_for_environment(self) -> dict[str, Any]:
        """Get logging configuration for specific environment.

        Returns:
            Logging configuration dictionary
        """
        base_config = {
            "enable_console": True,
            "enable_file": True,
            "max_file_size": 10 * 1024 * 1024,  # 10MB
            "backup_count": 5,
            "enable_syslog": False,
        }

        if self.environment == "development":
            return {
                **base_config,
                "level": "DEBUG",
                "log_file": "logs/iris.log",
                "structured": False,
                "enable_console": True,
            }
        elif self.environment == "staging":
            return {
                **base_config,
                "level": "INFO",
                "log_file": "/var/log/iris/iris.log",
                "structured": True,
                "enable_console": False,
                "enable_syslog": True,
                "syslog_address": ("localhost", 514),
            }
        elif self.environment == "production":
            return {
                **base_config,
                "level": "WARNING",
                "log_file": "/var/log/iris/iris.log",
                "structured": True,
                "enable_console": False,
                "enable_syslog": True,
                "syslog_address": ("localhost", 514),
            }
        else:
            return {
                **base_config,
                "level": "INFO",
                "log_file": "logs/iris.log",
                "structured": False,
            }

    def setup_application_logging(self) -> None:
        """Setup application logging with environment-specific configuration."""
        # Create log directory if it doesn't exist
        if self.config.get("log_file"):
            log_path = Path(self.config["log_file"])
            log_path.parent.mkdir(parents=True, exist_ok=True)

        # Setup logging
        setup_logging(
            level=self.config["level"],
            log_file=self.config.get("log_file"),
            structured=self.config.get("structured", False),
            enable_console=self.config.get("enable_console", True),
            enable_file=self.config.get("enable_file", True),
        )

    def get_module_config(self, module_name: str) -> dict[str, Any]:
        """Get module-specific logging configuration.

        Args:
            module_name: Module name

        Returns:
            Module-specific configuration
        """
        module_configs = {
            "database": {
                "level": "DEBUG" if self.environment == "development" else "INFO",
                "enable_sql_logging": self.environment == "development",
            },
            "cli": {"level": "INFO", "enable_progress_logging": True},
            "api": {"level": "INFO", "enable_request_logging": True},
            "core": {"level": "INFO", "enable_performance_logging": True},
        }

        return module_configs.get(module_name, {"level": "INFO"})  # type: ignore

    def configure_module_logging(self, module_name: str) -> None:
        """Configure logging for specific module.

        Args:
            module_name: Module name to configure
        """
        module_config = self.get_module_config(module_name)

        # Set module-specific log level
        import logging

        module_logger = logging.getLogger(f"iris.{module_name}")
        module_logger.setLevel(getattr(logging, module_config["level"].upper()))

        # Configure additional module-specific settings
        if module_name == "database" and module_config.get("enable_sql_logging"):
            # Enable SQLAlchemy SQL logging
            logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
            logging.getLogger("sqlalchemy.pool").setLevel(logging.INFO)

        if module_name == "api" and module_config.get("enable_request_logging"):
            # Enable request logging
            logging.getLogger("iris.api.requests").setLevel(logging.INFO)


def initialize_logging(environment: str | None = None) -> None:
    """Initialize application logging.

    Args:
        environment: Application environment (defaults to IRIS_ENV env var)
    """
    if environment is None:
        environment = os.getenv("IRIS_ENV", "development")

    config = IrisLoggingConfig(environment)
    config.setup_application_logging()

    # Configure module-specific logging
    for module in ["database", "cli", "api", "core"]:
        config.configure_module_logging(module)

    # Logging is now configured globally


def get_logging_config() -> IrisLoggingConfig:
    """Get current logging configuration.

    Returns:
        Current logging configuration instance
    """
    environment = os.getenv("IRIS_ENV", "development")
    return IrisLoggingConfig(environment)
