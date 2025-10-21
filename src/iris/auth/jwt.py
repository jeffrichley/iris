"""JWT token validation for Supabase-issued tokens.

Per research.md RES-003: Use python-jose with Supabase JWT_SECRET.
Compliant with FR-019, FR-041 through FR-046.

Security Features:
- Algorithm restriction (HS256 only) - FR-042
- Comprehensive claim validation - FR-043
- Tampering detection - FR-041
- Clock skew protection - FR-044
- Provider validation - FR-045
- Security event logging - FR-046
"""

from typing import Any

from fastapi import Header, HTTPException, status
from jose import JWTError, jwt

from iris.config.settings import get_settings
from iris.utils.logging import log_security_event


def validate_jwt(authorization: str = Header(...)) -> str:
    """Validate JWT token and extract user_id.
    
    Validates Supabase-issued JWT token from Authorization header.
    Enforces security requirements per FR-041 through FR-046.
    
    Args:
        authorization: Authorization header value (Bearer <token>)
        
    Returns:
        user_id: UUID string from 'sub' claim
        
    Raises:
        HTTPException: 401 if token invalid/expired/missing/tampered
        
    Security:
        - Validates signature using SUPABASE_JWT_SECRET (FR-041)
        - Restricts algorithm to HS256 only (FR-042)
        - Validates all required claims (FR-043)
        - Rejects future iat timestamps (FR-044)
        - Validates provider claim is "google" (FR-045)
        - Logs security events on validation failure (FR-046)
        
    Example:
        >>> user_id = validate_jwt("Bearer eyJhbGciOiJIUzI1NiIs...")
        >>> # Returns: "550e8400-e29b-41d4-a716-446655440000"
    """
    settings = get_settings()
    
    # Check Authorization header format (FR-022)
    if not authorization.startswith("Bearer "):
        log_security_event(
            event_type="invalid_jwt_format",
            details="Authorization header missing 'Bearer ' prefix"
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="invalid_token"  # Minimal info per FR-061
        )
    
    token = authorization.replace("Bearer ", "")
    
    try:
        # Decode and validate JWT (FR-041, FR-042, FR-043)
        payload: dict[str, Any] = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=["HS256"],  # FR-042: Restrict to HS256 only
            audience="authenticated",  # FR-043: Validate audience
            options={
                "verify_signature": True,  # FR-041: Verify signature
                "verify_exp": True,        # FR-043: Verify expiration
                "verify_aud": True,        # FR-043: Verify audience
            }
        )
        
        # Validate required claims exist (FR-043)
        user_id = payload.get("sub")
        email = payload.get("email")
        role = payload.get("role")
        iat = payload.get("iat")
        exp = payload.get("exp")
        
        if not all([user_id, email, role, iat, exp]):
            log_security_event(
                event_type="jwt_missing_claims",
                details=f"Missing required claims. Has: {list(payload.keys())}"
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid_token"
            )
        
        # Validate provider claim is "google" (FR-045)
        app_metadata = payload.get("app_metadata", {})
        provider = app_metadata.get("provider")
        
        if provider != "google":
            log_security_event(
                event_type="jwt_invalid_provider",
                details=f"Expected provider='google', got '{provider}'"
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid_token"
            )
        
        # Check for clock skew attacks (FR-044)
        import time
        current_time = int(time.time())
        if isinstance(iat, (int, float)) and iat > current_time + 60:  # Allow 60s grace
            log_security_event(
                event_type="jwt_future_iat",
                details=f"Token iat is in the future: {iat} > {current_time}"
            )
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="invalid_token"
            )
        
        return str(user_id)
        
    except JWTError as e:
        # Log security event (FR-046)
        error_type = type(e).__name__
        log_security_event(
            event_type=f"jwt_validation_failed_{error_type.lower()}",
            details=f"JWT validation error: {error_type}"
        )
        
        # Return minimal error info (FR-061)
        if "expired" in str(e).lower():
            detail = "expired_token"
        elif "signature" in str(e).lower():
            detail = "invalid_token"  # Don't reveal it's signature issue
        else:
            detail = "invalid_token"
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail
        )

