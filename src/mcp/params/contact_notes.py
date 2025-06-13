"""Contact note parameter classes for MCP tools"""

from typing import Optional
from pydantic import BaseModel, Field


class GetContactNotesParams(BaseModel):
    """Parameters for getting contact notes"""

    contact_id: str = Field(..., description="The contact ID to get notes for")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetContactNoteParams(BaseModel):
    """Parameters for getting a single contact note"""

    contact_id: str = Field(..., description="The contact ID")
    note_id: str = Field(..., description="The note ID to retrieve")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateContactNoteParams(BaseModel):
    """Parameters for creating a contact note"""

    contact_id: str = Field(..., description="The contact ID to create note for")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    body: str = Field(..., description="Note content/body")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateContactNoteParams(BaseModel):
    """Parameters for updating a contact note"""

    contact_id: str = Field(..., description="The contact ID")
    note_id: str = Field(..., description="The note ID to update")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    body: str = Field(..., description="Note content/body")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteContactNoteParams(BaseModel):
    """Parameters for deleting a contact note"""

    contact_id: str = Field(..., description="The contact ID")
    note_id: str = Field(..., description="The note ID to delete")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
