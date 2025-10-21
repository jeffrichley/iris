"""Reminders API routes with JWT authentication."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel as PydanticBaseModel

from iris.auth.dependencies import get_current_user_id
from iris.database.supabase import get_supabase

router = APIRouter(prefix="/api/v1/reminders", tags=["reminders"])


class ReminderCreate(PydanticBaseModel):
    """Request schema for creating a reminder."""
    
    task_id: UUID | None = None
    message: str
    due_time: str  # ISO datetime string


@router.get("")
async def list_reminders(
    user_id: str = Depends(get_current_user_id),
) -> list[dict[str, str]]:
    """List user's reminders."""
    db = get_supabase()
    response = db.from_("reminders").select("*").execute()
    return response.data


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_reminder(
    reminder_data: ReminderCreate,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Create new reminder."""
    db = get_supabase()
    data = reminder_data.model_dump()
    data["user_id"] = user_id
    if data["task_id"]:
        data["task_id"] = str(data["task_id"])
    
    response = db.from_("reminders").insert(data).execute()
    return response.data[0]


@router.delete("/{reminder_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_reminder(
    reminder_id: UUID,
    user_id: str = Depends(get_current_user_id),
) -> None:
    """Delete reminder."""
    db = get_supabase()
    response = db.from_("reminders").delete().eq("id", str(reminder_id)).execute()
    
    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")

