"""Note models for GoHighLevel MCP integration"""

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field


class Note(BaseModel):
    """GoHighLevel Note model"""

    id: Optional[str] = None
    locationId: Optional[str] = None
    contactId: Optional[str] = None
    body: str
    dateAdded: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None

    model_config = {"populate_by_name": True}


class NoteCreate(BaseModel):
    """Model for creating a note"""

    body: str = Field(..., description="Note content/body")


class NoteUpdate(BaseModel):
    """Model for updating a note"""

    body: Optional[str] = Field(None, description="Note content/body")


class NoteList(BaseModel):
    """Response model for note list"""

    notes: List[Note]
    count: int
    total: Optional[int] = None
