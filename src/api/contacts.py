"""Contact management client for GoHighLevel API v2"""

from typing import List, Optional

from .base import BaseGoHighLevelClient
from ..models.contact import Contact, ContactCreate, ContactUpdate, ContactList
from ..models.task import Task, TaskCreate, TaskUpdate, TaskList
from ..models.note import Note, NoteCreate, NoteUpdate, NoteList


class ContactsClient(BaseGoHighLevelClient):
    """Client for contact-related endpoints"""

    async def get_contacts(
        self,
        location_id: str,
        limit: int = 100,
        skip: int = 0,
        query: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> ContactList:
        """Get contacts for a location"""
        params = {"locationId": location_id, "limit": limit}

        # Only add skip if it's greater than 0
        if skip > 0:
            params["skip"] = skip

        if query:
            params["query"] = query
        if email:
            params["email"] = email
        if phone:
            params["phone"] = phone
        if tags:
            params["tags"] = ",".join(tags)

        response = await self._request(
            "GET", "/contacts", params=params, location_id=location_id
        )
        data = response.json()
        return ContactList(
            contacts=[Contact(**c) for c in data.get("contacts", [])],
            count=len(data.get("contacts", [])),
            total=data.get("meta", {}).get("total") or data.get("total"),
            meta=data.get("meta"),
            traceId=data.get("traceId"),
        )

    async def get_contact(self, contact_id: str, location_id: str) -> Contact:
        """Get a specific contact"""
        response = await self._request(
            "GET", f"/contacts/{contact_id}", location_id=location_id
        )
        data = response.json()
        return Contact(**data.get("contact", data))

    async def create_contact(self, contact: ContactCreate) -> Contact:
        """Create a new contact"""
        response = await self._request(
            "POST",
            "/contacts",
            json=contact.model_dump(exclude_none=True),
            location_id=contact.locationId,
        )
        data = response.json()
        return Contact(**data.get("contact", data))

    async def update_contact(
        self, contact_id: str, updates: ContactUpdate, location_id: str
    ) -> Contact:
        """Update an existing contact"""
        response = await self._request(
            "PUT",
            f"/contacts/{contact_id}",
            json=updates.model_dump(exclude_none=True),
            location_id=location_id,
        )
        data = response.json()
        return Contact(**data.get("contact", data))

    async def delete_contact(self, contact_id: str, location_id: str) -> bool:
        """Delete a contact"""
        response = await self._request(
            "DELETE", f"/contacts/{contact_id}", location_id=location_id
        )
        return response.status_code == 200

    async def add_contact_tags(
        self, contact_id: str, tags: List[str], location_id: str
    ) -> Contact:
        """Add tags to a contact"""
        await self._request(
            "POST",
            f"/contacts/{contact_id}/tags",
            json={"tags": tags},
            location_id=location_id,
        )
        # Tags endpoint returns {tags: [...], tagsAdded: [...]}
        # Need to fetch the updated contact
        return await self.get_contact(contact_id, location_id)

    async def remove_contact_tags(
        self, contact_id: str, tags: List[str], location_id: str
    ) -> Contact:
        """Remove tags from a contact"""
        await self._request(
            "DELETE",
            f"/contacts/{contact_id}/tags",
            json={"tags": tags},
            location_id=location_id,
        )
        # Tags endpoint returns {tags: [...], tagsRemoved: [...]}
        # Need to fetch the updated contact
        return await self.get_contact(contact_id, location_id)

    # Contact Tasks Methods

    async def get_contact_tasks(self, contact_id: str, location_id: str) -> TaskList:
        """Get all tasks for a contact"""
        response = await self._request(
            "GET", f"/contacts/{contact_id}/tasks", location_id=location_id
        )
        data = response.json()
        tasks_data = data.get("tasks", [])
        return TaskList(
            tasks=[Task(**task) for task in tasks_data],
            count=len(tasks_data),
            total=data.get("total", len(tasks_data)),
        )

    async def get_contact_task(
        self, contact_id: str, task_id: str, location_id: str
    ) -> Task:
        """Get a specific task for a contact"""
        response = await self._request(
            "GET", f"/contacts/{contact_id}/tasks/{task_id}", location_id=location_id
        )
        data = response.json()
        return Task(**data.get("task", data))

    async def create_contact_task(
        self, contact_id: str, task: TaskCreate, location_id: str
    ) -> Task:
        """Create a new task for a contact"""
        response = await self._request(
            "POST",
            f"/contacts/{contact_id}/tasks",
            json=task.model_dump(exclude_none=True),
            location_id=location_id,
        )
        data = response.json()
        return Task(**data.get("task", data))

    async def update_contact_task(
        self, contact_id: str, task_id: str, updates: TaskUpdate, location_id: str
    ) -> Task:
        """Update an existing task for a contact"""
        response = await self._request(
            "PUT",
            f"/contacts/{contact_id}/tasks/{task_id}",
            json=updates.model_dump(exclude_none=True),
            location_id=location_id,
        )
        data = response.json()
        return Task(**data.get("task", data))

    async def delete_contact_task(
        self, contact_id: str, task_id: str, location_id: str
    ) -> bool:
        """Delete a task for a contact"""
        response = await self._request(
            "DELETE", f"/contacts/{contact_id}/tasks/{task_id}", location_id=location_id
        )
        return response.status_code == 200

    async def complete_contact_task(
        self, contact_id: str, task_id: str, completed: bool, location_id: str
    ) -> Task:
        """Mark a contact task as completed or incomplete"""
        response = await self._request(
            "PUT",
            f"/contacts/{contact_id}/tasks/{task_id}/completed",
            json={"completed": completed},
            location_id=location_id,
        )
        data = response.json()
        return Task(**data.get("task", data))

    # Contact Notes Methods

    async def get_contact_notes(self, contact_id: str, location_id: str) -> NoteList:
        """Get all notes for a contact"""
        response = await self._request(
            "GET", f"/contacts/{contact_id}/notes", location_id=location_id
        )
        data = response.json()
        notes_data = data.get("notes", [])
        return NoteList(
            notes=[Note(**note) for note in notes_data],
            count=len(notes_data),
            total=data.get("total", len(notes_data)),
        )

    async def get_contact_note(
        self, contact_id: str, note_id: str, location_id: str
    ) -> Note:
        """Get a specific note for a contact"""
        response = await self._request(
            "GET", f"/contacts/{contact_id}/notes/{note_id}", location_id=location_id
        )
        data = response.json()
        return Note(**data.get("note", data))

    async def create_contact_note(
        self, contact_id: str, note: NoteCreate, location_id: str
    ) -> Note:
        """Create a new note for a contact"""
        response = await self._request(
            "POST",
            f"/contacts/{contact_id}/notes",
            json=note.model_dump(exclude_none=True),
            location_id=location_id,
        )
        data = response.json()
        return Note(**data.get("note", data))

    async def update_contact_note(
        self, contact_id: str, note_id: str, updates: NoteUpdate, location_id: str
    ) -> Note:
        """Update an existing note for a contact"""
        response = await self._request(
            "PUT",
            f"/contacts/{contact_id}/notes/{note_id}",
            json=updates.model_dump(exclude_none=True),
            location_id=location_id,
        )
        data = response.json()
        return Note(**data.get("note", data))

    async def delete_contact_note(
        self, contact_id: str, note_id: str, location_id: str
    ) -> bool:
        """Delete a note for a contact"""
        response = await self._request(
            "DELETE", f"/contacts/{contact_id}/notes/{note_id}", location_id=location_id
        )
        return response.status_code == 200

    # Contact Campaign/Workflow Assignment Methods

    async def add_contact_to_campaign(
        self, contact_id: str, campaign_id: str, location_id: str
    ) -> bool:
        """Add a contact to a campaign"""
        response = await self._request(
            "POST",
            f"/contacts/{contact_id}/campaigns/{campaign_id}",
            location_id=location_id,
        )
        return response.status_code in [200, 201]

    async def remove_contact_from_campaign(
        self, contact_id: str, campaign_id: str, location_id: str
    ) -> bool:
        """Remove a contact from a specific campaign"""
        response = await self._request(
            "DELETE",
            f"/contacts/{contact_id}/campaigns/{campaign_id}",
            location_id=location_id,
        )
        return response.status_code == 200

    async def remove_contact_from_all_campaigns(
        self, contact_id: str, location_id: str
    ) -> bool:
        """Remove a contact from all campaigns"""
        response = await self._request(
            "DELETE",
            f"/contacts/{contact_id}/campaigns/removeAll",
            location_id=location_id,
        )
        return response.status_code == 200

    async def add_contact_to_workflow(
        self, contact_id: str, workflow_id: str, location_id: str
    ) -> bool:
        """Add a contact to a workflow"""
        response = await self._request(
            "POST",
            f"/contacts/{contact_id}/workflow/{workflow_id}",
            location_id=location_id,
        )
        return response.status_code in [200, 201]

    async def remove_contact_from_workflow(
        self, contact_id: str, workflow_id: str, location_id: str
    ) -> bool:
        """Remove a contact from a workflow"""
        response = await self._request(
            "DELETE",
            f"/contacts/{contact_id}/workflow/{workflow_id}",
            location_id=location_id,
        )
        return response.status_code == 200
