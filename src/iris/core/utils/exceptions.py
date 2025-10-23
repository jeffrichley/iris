"""Custom exceptions for Iris project management system.

This module provides custom exception classes for different types of errors
that can occur in the Iris application.
"""

from enum import Enum
from typing import Any


class ErrorSeverity(Enum):
    """Error severity levels."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ErrorCategory(Enum):
    """Error categories for classification."""

    DATABASE = "database"
    CONFIGURATION = "configuration"
    VALIDATION = "validation"
    NETWORK = "network"
    PERMISSION = "permission"
    BUSINESS_LOGIC = "business_logic"
    SYSTEM = "system"


class IrisBaseError(Exception):
    """Base exception class for all Iris-specific exceptions."""

    def __init__(
        self,
        message: str,
        severity: ErrorSeverity = ErrorSeverity.MEDIUM,
        category: ErrorCategory = ErrorCategory.SYSTEM,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
        suggestions: list[str] | None = None,
        original_exception: Exception | None = None,
    ):
        """Initialize Iris exception.

        Args:
            message: Human-readable error message
            severity: Error severity level
            category: Error category for classification
            error_code: Unique error code for identification
            details: Additional error details
            suggestions: List of suggested fixes
            original_exception: Original exception that caused this error
        """
        super().__init__(message)
        self.message = message
        self.severity = severity
        self.category = category
        self.error_code = error_code
        self.details = details or {}
        self.suggestions = suggestions or []
        self.original_exception = original_exception

    def to_dict(self) -> dict[str, Any]:
        """Convert exception to dictionary representation."""
        return {
            "message": self.message,
            "severity": self.severity.value,
            "category": self.category.value,
            "error_code": self.error_code,
            "details": self.details,
            "suggestions": self.suggestions,
            "original_exception": str(self.original_exception) if self.original_exception else None,
        }


class DatabaseError(IrisBaseError):
    """Database-related errors."""

    def __init__(
        self,
        message: str,
        error_code: str | None = None,
        details: dict[str, Any] | None = None,
        suggestions: list[str] | None = None,
        original_exception: Exception | None = None,
    ):
        super().__init__(
            message=message,
            severity=ErrorSeverity.HIGH,
            category=ErrorCategory.DATABASE,
            error_code=error_code,
            details=details,
            suggestions=suggestions,
            original_exception=original_exception,
        )


class IrisConnectionError(DatabaseError):
    """Database connection errors."""

    def __init__(
        self,
        message: str,
        database_url: str | None = None,
        timeout: int | None = None,
        original_exception: Exception | None = None,
    ):
        suggestions = [
            "Check database server is running",
            "Verify connection parameters",
            "Check network connectivity",
            "Verify database credentials",
        ]

        details = {}
        if database_url:
            details["database_url"] = database_url
        if timeout:
            details["timeout"] = str(timeout)

        super().__init__(
            message=message,
            error_code="DB_CONNECTION_ERROR",
            details=details,
            suggestions=suggestions,
            original_exception=original_exception,
        )


class MigrationError(DatabaseError):
    """Database migration errors."""

    def __init__(
        self,
        message: str,
        migration_file: str | None = None,
        current_version: str | None = None,
        target_version: str | None = None,
        original_exception: Exception | None = None,
    ):
        suggestions = [
            "Check migration files are valid",
            "Verify database schema is consistent",
            "Check database permissions",
            "Review migration history",
        ]

        details = {}
        if migration_file:
            details["migration_file"] = migration_file
        if current_version:
            details["current_version"] = current_version
        if target_version:
            details["target_version"] = target_version

        super().__init__(
            message=message,
            error_code="DB_MIGRATION_ERROR",
            details=details,
            suggestions=suggestions,
            original_exception=original_exception,
        )


class ValidationError(IrisBaseError):
    """Data validation errors."""

    def __init__(
        self,
        message: str,
        field: str | None = None,
        value: Any | None = None,
        expected_type: str | None = None,
        original_exception: Exception | None = None,
    ):
        suggestions = [
            "Check input data format",
            "Verify required fields are provided",
            "Check data type constraints",
            "Review validation rules",
        ]

        details = {}
        if field:
            details["field"] = field
        if value is not None:
            details["value"] = str(value)
        if expected_type:
            details["expected_type"] = expected_type

        super().__init__(
            message=message,
            severity=ErrorSeverity.MEDIUM,
            category=ErrorCategory.VALIDATION,
            error_code="VALIDATION_ERROR",
            details=details,
            suggestions=suggestions,
            original_exception=original_exception,
        )


class ConfigurationError(IrisBaseError):
    """Configuration-related errors."""

    def __init__(
        self,
        message: str,
        config_key: str | None = None,
        config_file: str | None = None,
        original_exception: Exception | None = None,
    ):
        suggestions = [
            "Check configuration file format",
            "Verify required configuration keys",
            "Check environment variables",
            "Review configuration documentation",
        ]

        details = {}
        if config_key:
            details["config_key"] = config_key
        if config_file:
            details["config_file"] = config_file

        super().__init__(
            message=message,
            severity=ErrorSeverity.HIGH,
            category=ErrorCategory.CONFIGURATION,
            error_code="CONFIG_ERROR",
            details=details,
            suggestions=suggestions,
            original_exception=original_exception,
        )


class BusinessLogicError(IrisBaseError):
    """Business logic errors."""

    def __init__(
        self,
        message: str,
        operation: str | None = None,
        entity_id: str | None = None,
        original_exception: Exception | None = None,
    ):
        suggestions = [
            "Check business rules and constraints",
            "Verify entity state and relationships",
            "Review operation prerequisites",
            "Check user permissions",
        ]

        details = {}
        if operation:
            details["operation"] = operation
        if entity_id:
            details["entity_id"] = entity_id

        super().__init__(
            message=message,
            severity=ErrorSeverity.MEDIUM,
            category=ErrorCategory.BUSINESS_LOGIC,
            error_code="BUSINESS_LOGIC_ERROR",
            details=details,
            suggestions=suggestions,
            original_exception=original_exception,
        )


class IrisPermissionError(IrisBaseError):
    """Permission-related errors."""

    def __init__(
        self,
        message: str,
        resource: str | None = None,
        action: str | None = None,
        user_id: str | None = None,
        original_exception: Exception | None = None,
    ):
        suggestions = [
            "Check user permissions",
            "Verify resource access rights",
            "Contact system administrator",
            "Review security policies",
        ]

        details = {}
        if resource:
            details["resource"] = resource
        if action:
            details["action"] = action
        if user_id:
            details["user_id"] = user_id

        super().__init__(
            message=message,
            severity=ErrorSeverity.HIGH,
            category=ErrorCategory.PERMISSION,
            error_code="PERMISSION_ERROR",
            details=details,
            suggestions=suggestions,
            original_exception=original_exception,
        )


class IrisSystemError(IrisBaseError):
    """System-level errors."""

    def __init__(
        self,
        message: str,
        component: str | None = None,
        original_exception: Exception | None = None,
    ):
        suggestions = [
            "Check system resources",
            "Verify system configuration",
            "Review system logs",
            "Contact system administrator",
        ]

        details = {}
        if component:
            details["component"] = component

        super().__init__(
            message=message,
            severity=ErrorSeverity.CRITICAL,
            category=ErrorCategory.SYSTEM,
            error_code="SYSTEM_ERROR",
            details=details,
            suggestions=suggestions,
            original_exception=original_exception,
        )
