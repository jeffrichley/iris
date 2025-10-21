"""Ideas API routes with JWT authentication.

Per contracts/api-spec.yaml: Idea CRUD and promotion.
"""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field as PydanticField

from iris.auth.dependencies import get_current_user_id
from iris.database.supabase import get_supabase

router = APIRouter(prefix="/api/v1/ideas", tags=["ideas"])


class IdeaCreate(PydanticBaseModel):
    """Request schema for creating an idea."""
    
    title: str = PydanticField(min_length=1, max_length=255)
    description: str | None = None


class IdeaPromote(PydanticBaseModel):
    """Request schema for promoting idea to project."""
    
    project_name: str = PydanticField(min_length=1, max_length=255)


@router.get("")
async def list_ideas(
    user_id: str = Depends(get_current_user_id),
) -> list[dict[str, str]]:
    """List user's ideas."""
    db = get_supabase()
    response = db.from_("ideas").select("*").execute()
    return response.data


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_idea(
    idea_data: IdeaCreate,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Create new idea."""
    db = get_supabase()
    data = idea_data.model_dump()
    data["user_id"] = user_id
    
    response = db.from_("ideas").insert(data).execute()
    return response.data[0]


@router.post("/{idea_id}/promote")
async def promote_idea(
    idea_id: UUID,
    promote_data: IdeaPromote,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, dict[str, str]]:
    """Promote idea to project.
    
    Creates a new project and links it to the idea.
    """
    db = get_supabase()
    
    # Get the idea
    idea_response = db.from_("ideas").select("*").eq("id", str(idea_id)).execute()
    if not idea_response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Idea not found")
    
    idea = idea_response.data[0]
    
    # Create project from idea
    project_data = {
        "user_id": user_id,
        "name": promote_data.project_name,
        "description": idea.get("description", ""),
        "status": "active"
    }
    
    project_response = db.from_("projects").insert(project_data).execute()
    if not project_response.data:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create project"
        )
    
    project = project_response.data[0]
    
    # Update idea with promoted_to_project_id
    db.from_("ideas") \
        .update({"promoted_to_project_id": project["id"]}) \
        .eq("id", str(idea_id)) \
        .execute()
    
    return {
        "idea": idea,
        "project": project
    }

