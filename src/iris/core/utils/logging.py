"""Logging utilities for Iris project management system.

This module provides shared logging utilities and configuration
for the Iris application.
"""

import logging
import logging.handlers
from datetime import datetime
from typing import Any

from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install

# Install rich traceback handler
install(show_locals=True)


class LoggingConfig:
    """Centralized logging configuration for Iris application."""

    def __init__(
        self,
        level: str = "INFO",
        log_file: str | None = None,
        max_file_size: int = 10 * 1024 * 1024,  # 10MB
        backup_count: int = 5,
        enable_console: bool = True,
        enable_file: bool = True,
        enable_syslog: bool = False,
        syslog_address: str | None = None,
        format_string: str | None = None,
    ):
        """Initialize logging configuration.

        Args:
            level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_file: Log file path
            max_file_size: Maximum log file size in bytes
            backup_count: Number of backup files to keep
            enable_console: Enable console logging
            enable_file: Enable file logging
            enable_syslog: Enable syslog logging
            syslog_address: Syslog server address
            format_string: Custom log format string
        """
        self.level = level.upper()
        self.log_file = log_file
        self.max_file_size = max_file_size
        self.backup_count = backup_count
        self.enable_console = enable_console
        self.enable_file = enable_file
        self.enable_syslog = enable_syslog
        self.syslog_address = syslog_address
        self.format_string = format_string or "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

        # Module-specific log levels
        self.module_levels: dict[str, str] = {
            "iris.database": "DEBUG",
            "iris.cli": "INFO",
            "iris.api": "INFO",
            "iris.core": "INFO",
            "sqlalchemy.engine": "WARNING",
            "sqlalchemy.pool": "WARNING",
            "alembic": "INFO",
        }

    def configure_logging(self) -> None:
        """Configure application logging."""
        # Configure root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(getattr(logging, self.level))

        # Clear existing handlers
        root_logger.handlers.clear()

        # Add console handler
        if self.enable_console:
            self._setup_console_handler(root_logger)

        # Add file handler
        if self.enable_file and self.log_file:
            self._setup_file_handler(root_logger)

        # Add syslog handler
        if self.enable_syslog and self.syslog_address:
            self._setup_syslog_handler(root_logger)

        # Configure module-specific log levels
        self._configure_module_levels()

    def _setup_console_handler(self, logger: logging.Logger) -> None:
        """Setup console handler with Rich formatting."""
        console_handler = RichHandler(
            console=Console(stderr=True),
            show_time=True,
            show_path=True,
            markup=True,
            rich_tracebacks=True,
        )
        console_handler.setLevel(getattr(logging, self.level))
        logger.addHandler(console_handler)

    def _setup_file_handler(self, logger: logging.Logger) -> None:
        """Setup rotating file handler."""
        if self.log_file is None:
            raise ValueError("Log file path is required for file handler setup")
        file_handler = logging.handlers.RotatingFileHandler(
            self.log_file,
            maxBytes=self.max_file_size,
            backupCount=self.backup_count,
            encoding="utf-8",
        )
        file_handler.setLevel(getattr(logging, self.level))

        formatter = logging.Formatter(self.format_string)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    def _setup_syslog_handler(self, logger: logging.Logger) -> None:
        """Setup syslog handler."""
        try:
            syslog_handler = logging.handlers.SysLogHandler(
                address=self.syslog_address or ("localhost", 514)
            )
            syslog_handler.setLevel(getattr(logging, self.level))

            formatter = logging.Formatter(
                "iris[%(process)d]: %(name)s - %(levelname)s - %(message)s"
            )
            syslog_handler.setFormatter(formatter)
            logger.addHandler(syslog_handler)
        except Exception as e:
            logger.warning(f"Failed to setup syslog handler: {e}")

    def _configure_module_levels(self) -> None:
        """Configure module-specific log levels."""
        for module, level in self.module_levels.items():
            module_logger = logging.getLogger(module)
            module_logger.setLevel(getattr(logging, level.upper()))

    def get_logger(self, name: str) -> logging.Logger:
        """Get logger with configured settings.

        Args:
            name: Logger name

        Returns:
            Configured logger instance
        """
        logger = logging.getLogger(name)

        # Set module-specific level if configured
        for module, level in self.module_levels.items():
            if name.startswith(module):
                logger.setLevel(getattr(logging, level.upper()))
                break

        return logger


class IrisLogger:
    """Enhanced logger for Iris application with Rich formatting."""

    def __init__(self, name: str, level: str = "INFO", console: Console | None = None):
        """Initialize Iris logger.

        Args:
            name: Logger name
            level: Log level
            console: Rich console instance
        """
        self.name = name
        self.level = level.upper()
        self.console = console or Console()

        # Create logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(getattr(logging, self.level))

        # Clear existing handlers
        self.logger.handlers.clear()

        # Add Rich handler for console output
        self._setup_rich_handler()

        # Add file handler if configured
        self._setup_file_handler()

    def _setup_rich_handler(self) -> None:
        """Setup Rich console handler."""
        rich_handler = RichHandler(
            console=self.console,
            show_time=True,
            show_path=True,
            markup=True,
            rich_tracebacks=True,
        )
        rich_handler.setLevel(getattr(logging, self.level))

        # Create formatter
        formatter = logging.Formatter(
            fmt="%(message)s",
            datefmt="[%X]",
        )
        rich_handler.setFormatter(formatter)

        self.logger.addHandler(rich_handler)

    def _setup_file_handler(self) -> None:
        """Setup file handler if log file is configured."""
        # This would be configured from settings in a real implementation
        pass

    def debug(self, message: str, **kwargs: Any) -> None:
        """Log debug message."""
        self.logger.debug(message, **kwargs)

    def info(self, message: str, **kwargs: Any) -> None:
        """Log info message."""
        self.logger.info(message, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        """Log warning message."""
        self.logger.warning(message, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        """Log error message."""
        self.logger.error(message, **kwargs)

    def critical(self, message: str, **kwargs: Any) -> None:
        """Log critical message."""
        self.logger.critical(message, **kwargs)

    def exception(self, message: str, **kwargs: Any) -> None:
        """Log exception with traceback."""
        self.logger.exception(message, **kwargs)


class DatabaseLogger:
    """Specialized logger for database operations."""

    def __init__(self, console: Console | None = None):
        """Initialize database logger.

        Args:
            console: Rich console instance
        """
        self.console = console or Console()
        self.logger = IrisLogger("iris.database", console=self.console)

    def connection_established(self, database_url: str, pool_size: int) -> None:
        """Log successful database connection."""
        self.logger.info(f"[SUCCESS] Database connection established: {database_url}")
        self.logger.info(f"[INFO] Connection pool size: {pool_size}")

    def connection_failed(self, database_url: str, error: str) -> None:
        """Log failed database connection."""
        self.logger.error(f"[ERROR] Database connection failed: {database_url}")
        self.logger.error(f"[DETAIL] Error: {error}")

    def migration_started(self, migration_name: str) -> None:
        """Log migration start."""
        self.logger.info(f"[MIGRATE] Starting migration: {migration_name}")

    def migration_completed(self, migration_name: str, duration: float) -> None:
        """Log migration completion."""
        self.logger.info(f"[SUCCESS] Migration completed: {migration_name} ({duration:.2f}s)")

    def migration_failed(self, migration_name: str, error: str) -> None:
        """Log migration failure."""
        self.logger.error(f"[ERROR] Migration failed: {migration_name}")
        self.logger.error(f"[DETAIL] Error: {error}")

    def query_executed(self, query: str, duration: float) -> None:
        """Log query execution."""
        self.logger.debug(f"[QUERY] Query executed ({duration:.3f}s): {query}")

    def transaction_started(self) -> None:
        """Log transaction start."""
        self.logger.debug("[TRANSACTION] Transaction started")

    def transaction_committed(self) -> None:
        """Log transaction commit."""
        self.logger.debug("[SUCCESS] Transaction committed")

    def transaction_rolled_back(self, error: str) -> None:
        """Log transaction rollback."""
        self.logger.warning(f"[WARNING] Transaction rolled back: {error}")


class CLILogger:
    """Specialized logger for CLI operations."""

    def __init__(self, console: Console | None = None):
        """Initialize CLI logger.

        Args:
            console: Rich console instance
        """
        self.console = console or Console()
        self.logger = IrisLogger("iris.cli", console=self.console)

    def command_started(self, command: str, args: dict[str, Any]) -> None:
        """Log command start."""
        self.logger.info(f"[START] Starting command: {command}")
        if args:
            self.logger.debug(f"[DEBUG] Arguments: {args}")

    def command_completed(self, command: str, duration: float) -> None:
        """Log command completion."""
        self.logger.info(f"[SUCCESS] Command completed: {command} ({duration:.2f}s)")

    def command_failed(self, command: str, error: str) -> None:
        """Log command failure."""
        self.logger.error(f"[ERROR] Command failed: {command}")
        self.logger.error(f"[DETAIL] Error: {error}")

    def progress_update(self, message: str, progress: float | None = None) -> None:
        """Log progress update."""
        if progress is not None:
            self.logger.info(f"[PROGRESS] {message} ({progress:.1f}%)")
        else:
            self.logger.info(f"[INFO] {message}")

    def success(self, message: str) -> None:
        """Log success message."""
        self.logger.info(f"[SUCCESS] {message}")

    def warning(self, message: str) -> None:
        """Log warning message."""
        self.logger.warning(f"[WARNING] {message}")

    def error(self, message: str) -> None:
        """Log error message."""
        self.logger.error(f"[ERROR] {message}")


def get_logger(name: str, level: str = "INFO") -> IrisLogger:
    """Get logger instance.

    Args:
        name: Logger name
        level: Log level

    Returns:
        Logger instance
    """
    return IrisLogger(name, level)


def get_database_logger() -> DatabaseLogger:
    """Get database logger instance.

    Returns:
        Database logger instance
    """
    return DatabaseLogger()


def get_cli_logger() -> CLILogger:
    """Get CLI logger instance.

    Returns:
        CLI logger instance
    """
    return CLILogger()


class StructuredFormatter(logging.Formatter):
    """Structured log formatter for JSON-like output."""

    def format(self, record: logging.LogRecord) -> str:
        """Format log record as structured data."""
        log_data = {
            "timestamp": datetime.fromtimestamp(record.created).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "process": record.process,
            "thread": record.thread,
        }

        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)

        # Add extra fields if present
        for key, value in record.__dict__.items():
            if key not in {
                "name",
                "msg",
                "args",
                "levelname",
                "levelno",
                "pathname",
                "filename",
                "module",
                "lineno",
                "funcName",
                "created",
                "msecs",
                "relativeCreated",
                "thread",
                "threadName",
                "processName",
                "process",
                "getMessage",
                "exc_info",
                "exc_text",
                "stack_info",
            }:
                log_data[key] = value

        return str(log_data)


def setup_logging(
    level: str = "INFO",
    log_file: str | None = None,
    structured: bool = False,
    enable_console: bool = True,
    enable_file: bool = True,
) -> None:
    """Setup application logging with comprehensive configuration.

    Args:
        level: Log level
        log_file: Optional log file path
        structured: Enable structured logging
        enable_console: Enable console logging
        enable_file: Enable file logging
    """
    config = LoggingConfig(
        level=level, log_file=log_file, enable_console=enable_console, enable_file=enable_file
    )
    config.configure_logging()

    # Setup structured logging if requested
    if structured:
        _setup_structured_logging(log_file)


def _setup_structured_logging(log_file: str | None = None) -> None:
    """Setup structured logging with JSON-like output."""
    root_logger = logging.getLogger()

    # Update file handler with structured formatter
    for handler in root_logger.handlers:
        if isinstance(handler, logging.handlers.RotatingFileHandler):
            handler.setFormatter(StructuredFormatter())


def get_application_logger() -> logging.Logger:
    """Get application logger with proper configuration.

    Returns:
        Configured application logger
    """
    return logging.getLogger("iris")


def get_module_logger(module_name: str) -> logging.Logger:
    """Get module-specific logger.

    Args:
        module_name: Module name (e.g., 'database', 'cli', 'api')

    Returns:
        Configured module logger
    """
    return logging.getLogger(f"iris.{module_name}")


def log_performance(func_name: str, duration: float, **kwargs: Any) -> None:
    """Log performance metrics.

    Args:
        func_name: Function name
        duration: Execution duration in seconds
        **kwargs: Additional performance data
    """
    logger = get_application_logger()
    logger.info(
        f"Performance: {func_name}",
        extra={"performance": True, "function": func_name, "duration": duration, **kwargs},
    )


def log_security_event(event_type: str, details: dict[str, Any]) -> None:
    """Log security-related events.

    Args:
        event_type: Type of security event
        details: Event details
    """
    logger = get_application_logger()
    logger.warning(
        f"Security event: {event_type}",
        extra={"security": True, "event_type": event_type, **details},
    )
