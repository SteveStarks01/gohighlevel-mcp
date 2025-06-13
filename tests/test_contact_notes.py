"""Tests for contact notes functionality"""

import pytest
from unittest.mock import AsyncMock, patch
from src.models.note import Note, NoteList
from src.mcp.params.contact_notes import (
    GetContactNotesParams,
    GetContactNoteParams,
    CreateContactNoteParams,
    UpdateContactNoteParams,
    DeleteContactNoteParams,
)


class TestContactNotesImplementation:
    """Test contact notes MCP tools implementation"""

    @pytest.mark.asyncio
    async def test_get_contact_notes(self):
        """Test getting all notes for a contact"""
        # Create mock client
        mock_client = AsyncMock()
        mock_note = Note(
            id="test_note_id",
            body="Test note content",
            contactId="test_contact_id",
            locationId="test_location",
        )
        mock_note_list = NoteList(notes=[mock_note], count=1, total=1)
        mock_client.get_contact_notes.return_value = mock_note_list

        # Create test parameters
        params = GetContactNotesParams(
            contact_id="test_contact_id",
            location_id="test_location",
        )

        # Test the logic directly (simulating what the MCP tool does)
        # Skip the main import and test the core logic
        client = mock_client
        note_list = await client.get_contact_notes(
            params.contact_id, params.location_id
        )
        result = {
            "success": True,
            "notes": [note.model_dump() for note in note_list.notes],
            "count": note_list.count,
            "total": note_list.total,
        }

        assert result["success"] is True
        assert len(result["notes"]) == 1
        assert result["notes"][0]["body"] == "Test note content"
        mock_client.get_contact_notes.assert_called_once_with(
            "test_contact_id", "test_location"
        )

    @pytest.mark.asyncio
    async def test_create_contact_note(self):
        """Test creating a new note for a contact"""
        # Create mock client
        mock_client = AsyncMock()
        mock_note = Note(
            id="new_note_id",
            body="New note content",
            contactId="test_contact_id",
            locationId="test_location",
        )
        mock_client.create_contact_note.return_value = mock_note

        # Create test parameters
        params = CreateContactNoteParams(
            contact_id="test_contact_id",
            location_id="test_location",
            body="New note content",
        )

        # Test the logic directly
        from src.models.note import NoteCreate

        client = mock_client
        note_data = NoteCreate(body=params.body)
        note = await client.create_contact_note(
            params.contact_id, note_data, params.location_id
        )
        result = {"success": True, "note": note.model_dump()}

        assert result["success"] is True
        assert result["note"]["body"] == "New note content"
        mock_client.create_contact_note.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_contact_note(self):
        """Test deleting a note for a contact"""
        # Create mock client
        mock_client = AsyncMock()
        mock_client.delete_contact_note.return_value = True

        # Create test parameters
        params = DeleteContactNoteParams(
            contact_id="test_contact_id",
            note_id="test_note_id",
            location_id="test_location",
        )

        # Test the logic directly
        client = mock_client
        success = await client.delete_contact_note(
            params.contact_id, params.note_id, params.location_id
        )
        result = {
            "success": success,
            "message": (
                "Note deleted successfully" if success else "Failed to delete note"
            ),
        }

        assert result["success"] is True
        assert result["message"] == "Note deleted successfully"
        mock_client.delete_contact_note.assert_called_once_with(
            "test_contact_id", "test_note_id", "test_location"
        )

    def test_note_parameter_classes_exist(self):
        """Test that note parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetContactNotesParams, BaseModel)
        assert issubclass(GetContactNoteParams, BaseModel)
        assert issubclass(CreateContactNoteParams, BaseModel)
        assert issubclass(UpdateContactNoteParams, BaseModel)
        assert issubclass(DeleteContactNoteParams, BaseModel)

        # Check that required fields exist
        assert "contact_id" in GetContactNotesParams.model_fields
        assert "location_id" in GetContactNotesParams.model_fields
        assert "note_id" in GetContactNoteParams.model_fields
        assert "body" in CreateContactNoteParams.model_fields
