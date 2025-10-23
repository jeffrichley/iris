"""Error handling utilities for Iris project management system.

This module provides centralized error handling, logging, and recovery
mechanisms for the Iris application.
"""

import asyncio
import logging
import traceback
from collections.abc import Callable, Generator
from contextlib import contextmanager
from datetime import datetime
from functools import wraps
from typing import Any

import typer

from iris.core.utils.exceptions import (
    ConfigurationError,
    ErrorCategory,
    ErrorSeverity,
    IrisBaseError,
    IrisConnectionError,
    IrisPermissionError,
    IrisSystemError,
    MigrationError,
    ValidationError,
)


class ErrorHandler:
    """Centralized error handling and recovery system."""

    def __init__(self, logger: logging.Logger | None = None):
        """Initialize error handler.

        Args:
            logger: Logger instance for error logging
        """
        self.logger = logger or logging.getLogger(__name__)
        self.error_counts: dict[str, int] = {}
        self.recovery_strategies: dict[str, Callable[..., Any]] = {}

    def handle_error(
        self,
        error: Exception,
        context: dict[str, Any] | None = None,
        severity_override: ErrorSeverity | None = None,
    ) -> IrisBaseError:
        """Handle and process an error.

        Args:
            error: Exception to handle
            context: Additional context information
            severity_override: Override error severity

        Returns:
            Processed Iris exception
        """
        # Convert to Iris exception if needed
        if isinstance(error, IrisBaseError):
            iris_error = error
        else:
            iris_error = self._convert_to_iris_error(error, context)

        # Override severity if specified
        if severity_override:
            iris_error.severity = severity_override

        # Log the error
        self._log_error(iris_error, context)

        # Track error counts
        self._track_error(iris_error)

        # Attempt recovery if strategy exists
        self._attempt_recovery(iris_error, context)

        return iris_error

    def _convert_to_iris_error(
        self, error: Exception, context: dict[str, Any] | None = None
    ) -> IrisBaseError:
        """Convert standard exception to Iris exception.

        Args:
            error: Standard exception
            context: Additional context

        Returns:
            Iris exception
        """
        error_type = type(error).__name__
        message = str(error)

        # Map common exceptions to Iris exceptions
        if "connection" in error_type.lower() or "connect" in message.lower():
            return IrisConnectionError(
                message=f"Database connection failed: {message}", original_exception=error
            )
        elif "migration" in error_type.lower() or "migrate" in message.lower():
            return MigrationError(
                message=f"Database migration failed: {message}", original_exception=error
            )
        elif "validation" in error_type.lower() or "validate" in message.lower():
            return ValidationError(
                message=f"Validation failed: {message}", original_exception=error
            )
        elif "config" in error_type.lower() or "configuration" in message.lower():
            return ConfigurationError(
                message=f"Configuration error: {message}", original_exception=error
            )
        elif "permission" in error_type.lower() or "access" in message.lower():
            return IrisPermissionError(
                message=f"Permission denied: {message}", original_exception=error
            )
        else:
            return IrisSystemError(message=f"System error: {message}", original_exception=error)

    def _log_error(self, error: IrisBaseError, context: dict[str, Any] | None = None) -> None:
        """Log error with appropriate level.

        Args:
            error: Iris exception to log
            context: Additional context
        """
        log_level = self._get_log_level(error.severity)
        log_message = f"[{error.error_code}] {error.message}"

        if context:
            log_message += f" | Context: {context}"

        if error.details:
            log_message += f" | Details: {error.details}"

        if error.suggestions:
            log_message += f" | Suggestions: {error.suggestions}"

        self.logger.log(log_level, log_message)

        # Log stack trace for high severity errors
        if error.severity in [ErrorSeverity.HIGH, ErrorSeverity.CRITICAL]:
            self.logger.debug(f"Stack trace: {traceback.format_exc()}")

    def _get_log_level(self, severity: ErrorSeverity) -> int:
        """Get log level for error severity.

        Args:
            severity: Error severity level

        Returns:
            Logging level
        """
        severity_map = {
            ErrorSeverity.LOW: logging.INFO,
            ErrorSeverity.MEDIUM: logging.WARNING,
            ErrorSeverity.HIGH: logging.ERROR,
            ErrorSeverity.CRITICAL: logging.CRITICAL,
        }
        return severity_map.get(severity, logging.ERROR)

    def _track_error(self, error: IrisBaseError) -> None:
        """Track error counts for monitoring.

        Args:
            error: Iris exception to track
        """
        key = f"{error.category.value}:{error.error_code}"
        self.error_counts[key] = self.error_counts.get(key, 0) + 1

    def _attempt_recovery(
        self, error: IrisBaseError, context: dict[str, Any] | None = None
    ) -> None:
        """Attempt error recovery if strategy exists.

        Args:
            error: Iris exception
            context: Additional context
        """
        recovery_key = f"{error.category.value}:{error.error_code}"
        if recovery_key in self.recovery_strategies:
            try:
                self.recovery_strategies[recovery_key](error, context)
            except Exception as recovery_error:
                self.logger.error(f"Recovery failed for {recovery_key}: {recovery_error}")

    def register_recovery_strategy(
        self,
        category: ErrorCategory,
        error_code: str,
        strategy: Callable[[IrisBaseError, dict[str, Any] | None], None],
    ) -> None:
        """Register error recovery strategy.

        Args:
            category: Error category
            error_code: Error code
            strategy: Recovery function
        """
        key = f"{category.value}:{error_code}"
        self.recovery_strategies[key] = strategy

    def get_error_statistics(self) -> dict[str, Any]:
        """Get error statistics.

        Returns:
            Error statistics dictionary
        """
        return {
            "error_counts": self.error_counts.copy(),
            "total_errors": sum(self.error_counts.values()),
            "timestamp": datetime.now().isoformat(),
        }


def handle_errors(
    error_handler: ErrorHandler | None = None,
    reraise: bool = True,
    context: dict[str, Any] | None = None,
) -> Callable[..., Any]:
    """Decorator for automatic error handling.

    Args:
        error_handler: Error handler instance
        reraise: Whether to reraise the error
        context: Additional context

    Returns:
        Decorator function
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except (SystemExit, KeyboardInterrupt, typer.Exit) as e:
                # Re-raise system exits, keyboard interrupts, and typer exits without handling
                raise e
            except Exception as e:
                handler = error_handler or ErrorHandler()
                iris_error = handler.handle_error(e, context)
                if reraise:
                    raise iris_error from e
                return None

        return wrapper

    return decorator


def handle_async_errors(
    error_handler: ErrorHandler | None = None,
    reraise: bool = True,
    context: dict[str, Any] | None = None,
) -> Callable[..., Any]:
    """Decorator for automatic async error handling.

    Args:
        error_handler: Error handler instance
        reraise: Whether to reraise the error
        context: Additional context

    Returns:
        Decorator function
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return await func(*args, **kwargs)
            except (SystemExit, KeyboardInterrupt, typer.Exit) as e:
                # Re-raise system exits, keyboard interrupts, and typer exits without handling
                raise e
            except Exception as e:
                handler = error_handler or ErrorHandler()
                iris_error = handler.handle_error(e, context)
                if reraise:
                    raise iris_error from e
                return None

        return wrapper

    return decorator


@contextmanager
def error_context(
    error_handler: ErrorHandler | None = None, context: dict[str, Any] | None = None
) -> Generator[ErrorHandler, None, None]:
    """Context manager for error handling.

    Args:
        error_handler: Error handler instance
        context: Additional context

    Yields:
        Error handler instance
    """
    handler = error_handler or ErrorHandler()
    try:
        yield handler
    except Exception as e:
        handler.handle_error(e, context)
        raise


class RetryableError(IrisBaseError):
    """Error that can be retried."""

    def __init__(
        self, message: str, max_retries: int = 3, retry_delay: float = 1.0, **kwargs: Any
    ) -> None:
        super().__init__(message, **kwargs)
        self.max_retries = max_retries
        self.retry_delay = retry_delay


def retry_on_error(
    max_retries: int = 3,
    retry_delay: float = 1.0,
    retryable_errors: list[type[Exception]] | None = None,
) -> Callable[..., Any]:
    """Decorator for retrying operations on error.

    Args:
        max_retries: Maximum number of retries
        retry_delay: Delay between retries in seconds
        retryable_errors: List of exception types that can be retried

    Returns:
        Decorator function
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        async def async_wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error = None
            for attempt in range(max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if retryable_errors and not any(
                        isinstance(e, error_type) for error_type in retryable_errors
                    ):
                        raise e
                    if attempt < max_retries:
                        await asyncio.sleep(retry_delay * (2**attempt))  # Exponential backoff
                        continue
                    raise e
            if last_error:
                raise last_error
            raise RuntimeError("Retry failed but no error was captured")

        @wraps(func)
        def sync_wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    if retryable_errors and not any(
                        isinstance(e, error_type) for error_type in retryable_errors
                    ):
                        raise e
                    if attempt < max_retries:
                        import time

                        time.sleep(retry_delay * (2**attempt))  # Exponential backoff
                        continue
                    raise e
            if last_error:
                raise last_error
            raise RuntimeError("Retry failed but no error was captured")

        # Return appropriate wrapper based on function type
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper

    return decorator


# Global error handler instance
_global_error_handler: ErrorHandler | None = None


def get_global_error_handler() -> ErrorHandler:
    """Get global error handler instance.

    Returns:
        Global error handler
    """
    global _global_error_handler
    if _global_error_handler is None:
        _global_error_handler = ErrorHandler()
    return _global_error_handler


def set_global_error_handler(handler: ErrorHandler) -> None:
    """Set global error handler instance.

    Args:
        handler: Error handler instance
    """
    global _global_error_handler
    _global_error_handler = handler
