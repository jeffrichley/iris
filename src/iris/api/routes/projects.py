"""Projects API routes with JWT authentication.

Per FR-024, FR-025: Protected endpoints with user_id filtering.
Per FR-064, FR-065: user_id from JWT only, return 404 for unauthorized access.
Per contracts/api-spec.yaml: OpenAPI specification compliance.
"""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field as PydanticField

from iris.auth.dependencies import get_current_user_id
from iris.database.supabase import get_supabase
from iris.models.project import ProjectStatus
from iris.utils.exceptions import DatabaseError
from iris.utils.logging import log_error

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])


# Request/Response Schemas


class ProjectCreate(PydanticBaseModel):
    """Request schema for creating a project."""
    
    name: str = PydanticField(min_length=1, max_length=255)
    description: str | None = None
    status: ProjectStatus = ProjectStatus.ACTIVE


class ProjectUpdate(PydanticBaseModel):
    """Request schema for updating a project."""
    
    name: str | None = PydanticField(default=None, min_length=1, max_length=255)
    description: str | None = None
    status: ProjectStatus | None = None


# CRUD Endpoints


@router.get("")
async def list_projects(
    user_id: str = Depends(get_current_user_id),
    status_filter: ProjectStatus | None = None,
) -> list[dict[str, str]]:
    """List user's projects (RLS filtered).
    
    Per FR-025: Filters by authenticated user_id automatically via RLS.
    
    Args:
        user_id: Authenticated user UUID (injected from JWT)
        status_filter: Optional filter by project status
        
    Returns:
        List of user's projects
        
    Security:
        - Requires valid JWT (via get_current_user_id dependency)
        - RLS policies automatically filter by user_id
        - Only returns projects owned by authenticated user
    """
    try:
        db = get_supabase()
        
        # Build query (RLS automatically filters by user_id from JWT)
        query = db.from_("projects").select("*")
        
        if status_filter:
            query = query.eq("status", status_filter.value)
        
        response = query.execute()
        return response.data
        
    except Exception as e:
        log_error(f"Failed to list projects: {str(e)}", exception=e)
        raise DatabaseError(message="Failed to retrieve projects") from e


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_project(
    project_data: ProjectCreate,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Create new project for authenticated user.
    
    Per FR-064: user_id injected from JWT, never from request body.
    Per FR-049: RLS WITH CHECK enforces user_id matching.
    
    Args:
        project_data: Project creation data
        user_id: Authenticated user UUID (injected)
        
    Returns:
        Created project with all fields
        
    Raises:
        HTTPException: 400 if validation fails
    """
    try:
        db = get_supabase()
        
        # Inject user_id from JWT (FR-064)
        data = project_data.model_dump()
        data["user_id"] = user_id
        
        # Insert (RLS WITH CHECK ensures user_id matches auth.uid())
        response = db.from_("projects").insert(data).execute()
        
        if not response.data:
            raise DatabaseError(message="Failed to create project")
        
        return response.data[0]
        
    except Exception as e:
        log_error(f"Failed to create project: {str(e)}", exception=e)
        raise


@router.get("/{project_id}")
async def get_project(
    project_id: UUID,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Get project by ID (RLS enforced).
    
    Per FR-065: Returns 404 if project doesn't exist or not owned by user.
    
    Args:
        project_id: Project UUID
        user_id: Authenticated user UUID (injected)
        
    Returns:
        Project details
        
    Raises:
        HTTPException: 404 if not found or not authorized
    """
    try:
        db = get_supabase()
        
        # RLS automatically filters by user_id
        response = db.from_("projects").select("*").eq("id", str(project_id)).execute()
        
        if not response.data:
            # FR-065: Return 404 (not 403) to hide existence
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resource not found"
            )
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        log_error(f"Failed to get project: {str(e)}", exception=e)
        raise DatabaseError(message="Failed to retrieve project") from e


@router.patch("/{project_id}")
async def update_project(
    project_id: UUID,
    project_data: ProjectUpdate,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Update project (RLS enforced).
    
    Args:
        project_id: Project UUID
        project_data: Fields to update
        user_id: Authenticated user UUID (injected)
        
    Returns:
        Updated project
        
    Raises:
        HTTPException: 404 if not found or not authorized
    """
    try:
        db = get_supabase()
        
        # Build update data (only include non-None fields)
        update_data = {
            k: v for k, v in project_data.model_dump().items() 
            if v is not None
        }
        
        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No fields to update"
            )
        
        # Update (RLS ensures only owner can update)
        response = db.from_("projects") \
            .update(update_data) \
            .eq("id", str(project_id)) \
            .execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resource not found"
            )
        
        return response.data[0]
        
    except HTTPException:
        raise
    except Exception as e:
        log_error(f"Failed to update project: {str(e)}", exception=e)
        raise


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: UUID,
    user_id: str = Depends(get_current_user_id),
) -> None:
    """Delete project (cascades to tasks/notes per FR-011).
    
    Args:
        project_id: Project UUID to delete
        user_id: Authenticated user UUID (injected)
        
    Raises:
        HTTPException: 404 if not found or not authorized
    """
    try:
        db = get_supabase()
        
        # Delete (RLS ensures only owner can delete, CASCADE to tasks/notes)
        response = db.from_("projects").delete().eq("id", str(project_id)).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resource not found"
            )
        
    except HTTPException:
        raise
    except Exception as e:
        log_error(f"Failed to delete project: {str(e)}", exception=e)
        raise

