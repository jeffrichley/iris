"""Tasks API routes with JWT authentication.

Per contracts/api-spec.yaml: Task CRUD operations.
"""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field as PydanticField

from iris.auth.dependencies import get_current_user_id
from iris.database.supabase import get_supabase
from iris.models.task import TaskPriority

router = APIRouter(prefix="/api/v1/tasks", tags=["tasks"])


class TaskCreate(PydanticBaseModel):
    """Request schema for creating a task."""
    
    project_id: UUID
    title: str = PydanticField(min_length=1, max_length=500)
    priority: TaskPriority = TaskPriority.MEDIUM
    due_date: str | None = None  # ISO datetime string
    notes: str | None = None


class TaskUpdate(PydanticBaseModel):
    """Request schema for updating a task."""
    
    title: str | None = PydanticField(default=None, min_length=1, max_length=500)
    priority: TaskPriority | None = None
    due_date: str | None = None
    completed: bool | None = None
    notes: str | None = None


@router.get("")
async def list_tasks(
    user_id: str = Depends(get_current_user_id),
    project_id: UUID | None = None,
    completed: bool | None = None,
) -> list[dict[str, str]]:
    """List user's tasks with optional filters."""
    db = get_supabase()
    query = db.from_("tasks").select("*")
    
    if project_id:
        query = query.eq("project_id", str(project_id))
    if completed is not None:
        query = query.eq("completed", completed)
    
    response = query.execute()
    return response.data


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Create new task."""
    db = get_supabase()
    data = task_data.model_dump()
    data["user_id"] = user_id
    data["project_id"] = str(data["project_id"])  # Convert UUID to string
    
    response = db.from_("tasks").insert(data).execute()
    return response.data[0]


@router.get("/{task_id}")
async def get_task(
    task_id: UUID,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Get task by ID."""
    db = get_supabase()
    response = db.from_("tasks").select("*").eq("id", str(task_id)).execute()
    
    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    
    return response.data[0]


@router.patch("/{task_id}")
async def update_task(
    task_id: UUID,
    task_data: TaskUpdate,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Update task."""
    db = get_supabase()
    update_data = {k: v for k, v in task_data.model_dump().items() if v is not None}
    
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No fields to update")
    
    response = db.from_("tasks").update(update_data).eq("id", str(task_id)).execute()
    
    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    
    return response.data[0]


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: UUID,
    user_id: str = Depends(get_current_user_id),
) -> None:
    """Delete task."""
    db = get_supabase()
    response = db.from_("tasks").delete().eq("id", str(task_id)).execute()
    
    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")

