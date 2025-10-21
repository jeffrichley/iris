"""Authentication and authorization for Iris.

OAuth2 via Supabase GoTrue with JWT token validation.
"""

from iris.auth.dependencies import get_current_user_id
from iris.auth.jwt import validate_jwt

__all__ = ["validate_jwt", "get_current_user_id"]

