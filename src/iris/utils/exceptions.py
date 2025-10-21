"""Custom exception classes for Iris.

Compliant with Constitution Principle 4: Error Handling
Errors MUST be specific, never generic.
"""


class IrisException(Exception):
    """Base exception for all Iris-specific errors."""

    def __init__(self, message: str, details: str | None = None) -> None:
        """Initialize exception with message and optional details.
        
        Args:
            message: User-facing error message
            details: Technical details for logging (not shown to user)
        """
        self.message = message
        self.details = details
        super().__init__(message)


class DatabaseError(IrisException):
    """Raised when database operations fail.
    
    Examples:
    - Supabase connection failures
    - Schema initialization errors
    - Query execution failures
    - Foreign key constraint violations
    """

    pass


class AuthenticationError(IrisException):
    """Raised when authentication fails.
    
    Examples:
    - Invalid JWT tokens
    - Expired tokens
    - Missing Authorization header
    - OAuth2 flow failures
    - JWT signature validation failures
    
    Compliant with FR-022, FR-060: Generic messages to avoid information leakage.
    """

    pass


class ValidationError(IrisException):
    """Raised when input validation fails.
    
    Examples:
    - Invalid request body
    - Missing required fields
    - Field type mismatches
    - Business rule violations
    """

    pass


class ConfigurationError(IrisException):
    """Raised when configuration is invalid.
    
    Examples:
    - Missing .env file
    - Invalid Supabase credentials
    - Malformed environment variables
    
    Compliant with FR-055, FR-069.
    """

    pass


class AuthorizationError(IrisException):
    """Raised when authorization check fails.
    
    Examples:
    - User attempting to access another user's data
    - RLS policy violations
    - Insufficient permissions
    
    Compliant with FR-065: Return 404 instead of 403 to hide resource existence.
    """

    pass

