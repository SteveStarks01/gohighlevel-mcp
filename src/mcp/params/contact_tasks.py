"""Contact task parameter classes for MCP tools"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class GetContactTasksParams(BaseModel):
    """Parameters for getting contact tasks"""

    contact_id: str = Field(..., description="The contact ID to get tasks for")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetContactTaskParams(BaseModel):
    """Parameters for getting a single contact task"""

    contact_id: str = Field(..., description="The contact ID")
    task_id: str = Field(..., description="The task ID to retrieve")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateContactTaskParams(BaseModel):
    """Parameters for creating a contact task"""

    contact_id: str = Field(..., description="The contact ID to create task for")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    title: str = Field(..., description="Task title")
    body: Optional[str] = Field(None, description="Task description/body")
    due_date: Optional[datetime] = Field(None, description="Task due date")
    assigned_to: Optional[str] = Field(None, description="User ID to assign the task to")
    completed: bool = Field(False, description="Whether the task is completed")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateContactTaskParams(BaseModel):
    """Parameters for updating a contact task"""

    contact_id: str = Field(..., description="The contact ID")
    task_id: str = Field(..., description="The task ID to update")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    title: Optional[str] = Field(None, description="Task title")
    body: Optional[str] = Field(None, description="Task description/body")
    due_date: Optional[datetime] = Field(None, description="Task due date")
    assigned_to: Optional[str] = Field(None, description="User ID to assign the task to")
    completed: Optional[bool] = Field(None, description="Whether the task is completed")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteContactTaskParams(BaseModel):
    """Parameters for deleting a contact task"""

    contact_id: str = Field(..., description="The contact ID")
    task_id: str = Field(..., description="The task ID to delete")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CompleteContactTaskParams(BaseModel):
    """Parameters for completing a contact task"""

    contact_id: str = Field(..., description="The contact ID")
    task_id: str = Field(..., description="The task ID to complete")
    location_id: str = Field(
        ..., description="The location ID where the contact exists"
    )
    completed: bool = Field(True, description="Whether to mark the task as completed")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
