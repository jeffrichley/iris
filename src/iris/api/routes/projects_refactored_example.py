"""Projects API routes - REFACTORED to use Service Layer.

THIN CONTROLLER PATTERN:
- Routes handle HTTP concerns only (request parsing, response formatting)
- Business logic delegated to ProjectService
- Service methods reusable for MCP tools, CLI, background jobs

Compare with original projects.py to see the difference!
"""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field as PydanticField

from iris.auth.dependencies import get_current_user_id
from iris.database.supabase import get_supabase
from iris.models.project import ProjectStatus
from iris.services.project_service import ProjectService
from iris.utils.exceptions import AuthorizationError, DatabaseError, ValidationError

router = APIRouter(prefix="/api/v1/projects", tags=["projects"])


# Request Schemas (HTTP-specific)


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


# FastAPI Dependency


def get_project_service() -> ProjectService:
    """Get ProjectService instance (FastAPI dependency)."""
    return ProjectService(db=get_supabase())


# CRUD Endpoints (THIN - just delegate to service)


@router.get("")
async def list_projects(
    user_id: str = Depends(get_current_user_id),
    status_filter: ProjectStatus | None = None,
    service: ProjectService = Depends(get_project_service),
) -> list[dict[str, str]]:
    """List projects - delegates to service."""
    return service.list_projects(user_id=user_id, status_filter=status_filter)


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_project(
    project_data: ProjectCreate,
    user_id: str = Depends(get_current_user_id),
    service: ProjectService = Depends(get_project_service),
) -> dict[str, str]:
    """Create project - delegates to service."""
    try:
        return service.create_project(
            user_id=user_id,
            name=project_data.name,
            description=project_data.description,
            status=project_data.status
        )
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message
        )


@router.get("/{project_id}")
async def get_project(
    project_id: UUID,
    user_id: str = Depends(get_current_user_id),
    service: ProjectService = Depends(get_project_service),
) -> dict[str, str]:
    """Get project - delegates to service."""
    try:
        return service.get_project(user_id=user_id, project_id=project_id)
    except AuthorizationError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    except DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message
        )


@router.patch("/{project_id}")
async def update_project(
    project_id: UUID,
    project_data: ProjectUpdate,
    user_id: str = Depends(get_current_user_id),
    service: ProjectService = Depends(get_project_service),
) -> dict[str, str]:
    """Update project - delegates to service."""
    try:
        return service.update_project(
            user_id=user_id,
            project_id=project_id,
            name=project_data.name,
            description=project_data.description,
            status=project_data.status
        )
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e.message)
    except AuthorizationError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    except DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message
        )


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: UUID,
    user_id: str = Depends(get_current_user_id),
    service: ProjectService = Depends(get_project_service),
) -> None:
    """Delete project - delegates to service."""
    try:
        service.delete_project(user_id=user_id, project_id=project_id)
    except AuthorizationError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    except DatabaseError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message
        )

