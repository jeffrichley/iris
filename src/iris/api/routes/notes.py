"""Notes API routes with JWT authentication."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel as PydanticBaseModel
from pydantic import Field as PydanticField

from iris.auth.dependencies import get_current_user_id
from iris.database.supabase import get_supabase

router = APIRouter(prefix="/api/v1/notes", tags=["notes"])


class NoteCreate(PydanticBaseModel):
    """Request schema for creating a note."""
    
    project_id: UUID
    content: str = PydanticField(min_length=1)


class NoteUpdate(PydanticBaseModel):
    """Request schema for updating a note."""
    
    content: str = PydanticField(min_length=1)


@router.get("")
async def list_notes(
    user_id: str = Depends(get_current_user_id),
    project_id: UUID | None = None,
) -> list[dict[str, str]]:
    """List user's notes with optional project filter."""
    db = get_supabase()
    query = db.from_("notes").select("*")
    
    if project_id:
        query = query.eq("project_id", str(project_id))
    
    response = query.execute()
    return response.data


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_note(
    note_data: NoteCreate,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Create new note."""
    db = get_supabase()
    data = note_data.model_dump()
    data["user_id"] = user_id
    data["project_id"] = str(data["project_id"])
    
    response = db.from_("notes").insert(data).execute()
    return response.data[0]


@router.get("/{note_id}")
async def get_note(
    note_id: UUID,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Get note by ID."""
    db = get_supabase()
    response = db.from_("notes").select("*").eq("id", str(note_id)).execute()
    
    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    
    return response.data[0]


@router.patch("/{note_id}")
async def update_note(
    note_id: UUID,
    note_data: NoteUpdate,
    user_id: str = Depends(get_current_user_id),
) -> dict[str, str]:
    """Update note content."""
    db = get_supabase()
    
    response = db.from_("notes") \
        .update({"content": note_data.content}) \
        .eq("id", str(note_id)) \
        .execute()
    
    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")
    
    return response.data[0]


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(
    note_id: UUID,
    user_id: str = Depends(get_current_user_id),
) -> None:
    """Delete note."""
    db = get_supabase()
    response = db.from_("notes").delete().eq("id", str(note_id)).execute()
    
    if not response.data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource not found")

