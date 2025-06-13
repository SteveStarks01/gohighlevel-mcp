"""Contact tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.contact import ContactCreate, ContactUpdate
from ...models.task import TaskCreate, TaskUpdate
from ...models.note import NoteCreate, NoteUpdate
from ..params.contacts import (
    CreateContactParams,
    UpdateContactParams,
    DeleteContactParams,
    GetContactParams,
    SearchContactsParams,
    ManageTagsParams,
)
from ..params.contact_tasks import (
    GetContactTasksParams,
    GetContactTaskParams,
    CreateContactTaskParams,
    UpdateContactTaskParams,
    DeleteContactTaskParams,
    CompleteContactTaskParams,
)
from ..params.contact_notes import (
    GetContactNotesParams,
    GetContactNoteParams,
    CreateContactNoteParams,
    UpdateContactNoteParams,
    DeleteContactNoteParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_contact_tools(_mcp, _get_client):
    """Register contact tools with the MCP instance"""
    global mcp, get_client
    mcp = _mcp
    get_client = _get_client

    @mcp.tool()
    async def create_contact(params: CreateContactParams) -> Dict[str, Any]:
        """Create a new contact in GoHighLevel"""
        client = await get_client(params.access_token)

        contact_data = ContactCreate(
            locationId=params.location_id,
            firstName=params.first_name,
            lastName=params.last_name,
            email=params.email,
            phone=params.phone,
            tags=params.tags,
            source=params.source,
            companyName=params.company_name,
            address1=params.address,
            city=params.city,
            state=params.state,
            postalCode=params.postal_code,
            customFields=[
                {"key": k, "value": v} for k, v in (params.custom_fields or {}).items()
            ],
        )

        contact = await client.create_contact(contact_data)
        return {"success": True, "contact": contact.model_dump()}

    @mcp.tool()
    async def update_contact(params: UpdateContactParams) -> Dict[str, Any]:
        """Update an existing contact in GoHighLevel"""
        client = await get_client(params.access_token)

        update_data = ContactUpdate(
            firstName=params.first_name,
            lastName=params.last_name,
            email=params.email,
            phone=params.phone,
            tags=params.tags,
            companyName=params.company_name,
            address1=params.address,
            city=params.city,
            state=params.state,
            postalCode=params.postal_code,
            customFields=(
                [
                    {"key": k, "value": v}
                    for k, v in (params.custom_fields or {}).items()
                ]
                if params.custom_fields
                else None
            ),
        )

        contact = await client.update_contact(
            params.contact_id, update_data, params.location_id
        )
        return {"success": True, "contact": contact.model_dump()}

    @mcp.tool()
    async def delete_contact(params: DeleteContactParams) -> Dict[str, Any]:
        """Delete a contact from GoHighLevel"""
        client = await get_client(params.access_token)

        success = await client.delete_contact(params.contact_id, params.location_id)
        return {
            "success": success,
            "message": (
                "Contact deleted successfully"
                if success
                else "Failed to delete contact"
            ),
        }

    @mcp.tool()
    async def get_contact(params: GetContactParams) -> Dict[str, Any]:
        """Get a single contact by ID"""
        client = await get_client(params.access_token)

        contact = await client.get_contact(params.contact_id, params.location_id)
        return {"success": True, "contact": contact.model_dump()}

    @mcp.tool()
    async def search_contacts(params: SearchContactsParams) -> Dict[str, Any]:
        """Search contacts in a location"""
        client = await get_client(params.access_token)

        result = await client.get_contacts(
            location_id=params.location_id,
            limit=params.limit,
            skip=params.skip,
            query=params.query,
            email=params.email,
            phone=params.phone,
            tags=params.tags,
        )

        return {
            "success": True,
            "contacts": [c.model_dump() for c in result.contacts],
            "count": result.count,
            "total": result.total,
        }

    @mcp.tool()
    async def add_contact_tags(params: ManageTagsParams) -> Dict[str, Any]:
        """Add tags to a contact"""
        client = await get_client(params.access_token)

        contact = await client.add_contact_tags(
            params.contact_id, params.tags, params.location_id
        )
        return {"success": True, "contact": contact.model_dump()}

    @mcp.tool()
    async def remove_contact_tags(params: ManageTagsParams) -> Dict[str, Any]:
        """Remove tags from a contact"""
        client = await get_client(params.access_token)

        contact = await client.remove_contact_tags(
            params.contact_id, params.tags, params.location_id
        )
        return {"success": True, "contact": contact.model_dump()}

    # Contact Tasks Tools

    @mcp.tool()
    async def get_contact_tasks(params: GetContactTasksParams) -> Dict[str, Any]:
        """Get all tasks for a contact"""
        client = await get_client(params.access_token)

        task_list = await client.get_contact_tasks(
            params.contact_id, params.location_id
        )
        return {
            "success": True,
            "tasks": [task.model_dump() for task in task_list.tasks],
            "count": task_list.count,
            "total": task_list.total,
        }

    @mcp.tool()
    async def get_contact_task(params: GetContactTaskParams) -> Dict[str, Any]:
        """Get a specific task for a contact"""
        client = await get_client(params.access_token)

        task = await client.get_contact_task(
            params.contact_id, params.task_id, params.location_id
        )
        return {"success": True, "task": task.model_dump()}

    @mcp.tool()
    async def create_contact_task(params: CreateContactTaskParams) -> Dict[str, Any]:
        """Create a new task for a contact"""
        client = await get_client(params.access_token)

        task_data = TaskCreate(
            title=params.title,
            body=params.body,
            dueDate=params.due_date,
            assignedTo=params.assigned_to,
            completed=params.completed,
        )

        task = await client.create_contact_task(
            params.contact_id, task_data, params.location_id
        )
        return {"success": True, "task": task.model_dump()}

    @mcp.tool()
    async def update_contact_task(params: UpdateContactTaskParams) -> Dict[str, Any]:
        """Update an existing task for a contact"""
        client = await get_client(params.access_token)

        update_data = TaskUpdate(
            title=params.title,
            body=params.body,
            dueDate=params.due_date,
            assignedTo=params.assigned_to,
            completed=params.completed,
        )

        task = await client.update_contact_task(
            params.contact_id, params.task_id, update_data, params.location_id
        )
        return {"success": True, "task": task.model_dump()}

    @mcp.tool()
    async def delete_contact_task(params: DeleteContactTaskParams) -> Dict[str, Any]:
        """Delete a task for a contact"""
        client = await get_client(params.access_token)

        success = await client.delete_contact_task(
            params.contact_id, params.task_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Task deleted successfully" if success else "Failed to delete task"
            ),
        }

    @mcp.tool()
    async def complete_contact_task(params: CompleteContactTaskParams) -> Dict[str, Any]:
        """Mark a contact task as completed or incomplete"""
        client = await get_client(params.access_token)

        task = await client.complete_contact_task(
            params.contact_id, params.task_id, params.completed, params.location_id
        )
        return {"success": True, "task": task.model_dump()}

    # Contact Notes Tools

    @mcp.tool()
    async def get_contact_notes(params: GetContactNotesParams) -> Dict[str, Any]:
        """Get all notes for a contact"""
        client = await get_client(params.access_token)

        note_list = await client.get_contact_notes(
            params.contact_id, params.location_id
        )
        return {
            "success": True,
            "notes": [note.model_dump() for note in note_list.notes],
            "count": note_list.count,
            "total": note_list.total,
        }

    @mcp.tool()
    async def get_contact_note(params: GetContactNoteParams) -> Dict[str, Any]:
        """Get a single note for a contact"""
        client = await get_client(params.access_token)

        note = await client.get_contact_note(
            params.contact_id, params.note_id, params.location_id
        )
        return {"success": True, "note": note.model_dump()}

    @mcp.tool()
    async def create_contact_note(params: CreateContactNoteParams) -> Dict[str, Any]:
        """Create a new note for a contact"""
        client = await get_client(params.access_token)

        note_data = NoteCreate(body=params.body)

        note = await client.create_contact_note(
            params.contact_id, note_data, params.location_id
        )
        return {"success": True, "note": note.model_dump()}

    @mcp.tool()
    async def update_contact_note(params: UpdateContactNoteParams) -> Dict[str, Any]:
        """Update an existing note for a contact"""
        client = await get_client(params.access_token)

        update_data = NoteUpdate(body=params.body)

        note = await client.update_contact_note(
            params.contact_id, params.note_id, update_data, params.location_id
        )
        return {"success": True, "note": note.model_dump()}

    @mcp.tool()
    async def delete_contact_note(params: DeleteContactNoteParams) -> Dict[str, Any]:
        """Delete a note for a contact"""
        client = await get_client(params.access_token)

        success = await client.delete_contact_note(
            params.contact_id, params.note_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Note deleted successfully" if success else "Failed to delete note"
            ),
        }
