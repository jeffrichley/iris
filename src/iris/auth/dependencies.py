"""FastAPI dependencies for authentication and authorization.

Per research.md RES-008: Use FastAPI Depends() for user_id injection.
Compliant with FR-023, FR-064: Extract user_id from JWT, never from request.
"""

from fastapi import Header

from iris.auth.jwt import validate_jwt


async def get_current_user_id(authorization: str = Header(...)) -> str:
    """FastAPI dependency to inject authenticated user_id.
    
    Automatically extracts and validates JWT from Authorization header,
    returning the authenticated user_id for use in route handlers.
    
    This dependency enforces FR-064: user_id comes ONLY from validated JWT,
    never from request body or query parameters.
    
    Args:
        authorization: Authorization header (injected by FastAPI)
        
    Returns:
        user_id: Validated user UUID from JWT 'sub' claim
        
    Raises:
        HTTPException: 401 if token validation fails
        
    Usage in routes:
        @router.get("/projects")
        async def list_projects(
            user_id: str = Depends(get_current_user_id)
        ):
            # user_id automatically validated and injected
            return get_user_projects(user_id)
            
    Example:
        >>> # FastAPI automatically calls this dependency
        >>> # Header: Authorization: Bearer eyJhbGci...
        >>> # Returns: "550e8400-e29b-41d4-a716-446655440000"
    """
    return validate_jwt(authorization)


# Alias for clarity in route signatures
async def require_auth(authorization: str = Header(...)) -> str:
    """Alias for get_current_user_id - clearer in some contexts."""
    return await get_current_user_id(authorization)

