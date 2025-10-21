"""Health check endpoint.

Per FR-020: Unprotected endpoint for service health verification.
"""

from datetime import datetime

from fastapi import APIRouter

from iris.database.supabase import get_supabase
from iris.utils.exceptions import DatabaseError

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check() -> dict[str, str | bool]:
    """Health check endpoint (unprotected).
    
    Per FR-020: Returns service status and Supabase connection health.
    This endpoint does NOT require authentication (public endpoint).
    
    Returns:
        dict: Health status with Supabase connection check
        
    Example Response:
        {
            "status": "healthy",
            "supabase_connected": true,
            "timestamp": "2025-10-20T14:30:00.000Z"
        }
    """
    # Check Supabase connection
    supabase_connected = False
    try:
        db = get_supabase()
        # Attempt a simple query to verify connection
        # Use a table that should exist after schema init
        db.from_("projects").select("id").limit(1).execute()
        supabase_connected = True
    except (DatabaseError, Exception):
        # Connection failed, but don't crash health check
        supabase_connected = False
    
    return {
        "status": "healthy",
        "supabase_connected": supabase_connected,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

