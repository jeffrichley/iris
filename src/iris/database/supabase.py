"""Supabase client initialization and connection management.

Per research.md RES-001: Use supabase-py with singleton pattern.
Compliant with FR-026: Use supabase-py for Supabase client interactions.
"""

from supabase import Client, create_client

from iris.config.settings import get_settings
from iris.utils.exceptions import DatabaseError
from iris.utils.logging import log_error, log_info

_supabase_client: Client | None = None


def get_supabase() -> Client:
    """Get Supabase client singleton with connection pooling.
    
    Client is initialized once and reused for all operations.
    Uses SUPABASE_ANON_KEY which enforces Row Level Security (FR-056).
    
    Connection pooling handled automatically by httpx backend.
    
    Returns:
        Client: Supabase client instance
        
    Raises:
        DatabaseError: If Supabase connection cannot be established
        
    Example:
        >>> db = get_supabase()
        >>> response = db.from_("projects").select("*").execute()
    """
    global _supabase_client
    
    if _supabase_client is None:
        settings = get_settings()
        
        try:
            _supabase_client = create_client(
                supabase_url=settings.SUPABASE_URL,
                supabase_key=settings.SUPABASE_ANON_KEY  # Uses anon key (RLS enforced)
            )
            
            log_info(
                f"Connected to Supabase at {settings.SUPABASE_URL}",
                title="Database Connected"
            )
            
        except Exception as e:
            log_error(
                "Failed to connect to Supabase. Verify credentials in .env file.",
                title="Database Connection Failed",
                exception=e
            )
            raise DatabaseError(
                message="Cannot connect to Supabase",
                details=str(e)
            ) from e
    
    return _supabase_client


def get_supabase_admin() -> Client:
    """Get Supabase client with admin privileges (bypasses RLS).
    
    WARNING: This client uses SERVICE_KEY which bypasses Row Level Security!
    Only use for admin operations or development debugging (FR-051, FR-056).
    
    Returns:
        Client: Supabase client with admin privileges
        
    Raises:
        DatabaseError: If service key not configured or connection fails
    """
    settings = get_settings()
    
    if not settings.SUPABASE_SERVICE_KEY:
        raise DatabaseError(
            message="SUPABASE_SERVICE_KEY not configured",
            details="Admin operations require service role key in .env"
        )
    
    try:
        return create_client(
            supabase_url=settings.SUPABASE_URL,
            supabase_key=settings.SUPABASE_SERVICE_KEY  # Service key (bypasses RLS)
        )
    except Exception as e:
        raise DatabaseError(
            message="Cannot connect to Supabase with admin key",
            details=str(e)
        ) from e

