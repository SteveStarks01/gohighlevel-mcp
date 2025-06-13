"""Task models for GoHighLevel MCP integration"""

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field


class Task(BaseModel):
    """GoHighLevel Task model"""

    id: Optional[str] = None
    locationId: Optional[str] = None
    contactId: Optional[str] = None
    assignedTo: Optional[str] = None
    title: str
    body: Optional[str] = None
    dueDate: Optional[datetime] = None
    dateAdded: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None
    completed: bool = False
    completedDate: Optional[datetime] = None

    model_config = {"populate_by_name": True}


class TaskCreate(BaseModel):
    """Model for creating a task"""

    title: str = Field(..., description="Task title")
    body: Optional[str] = Field(None, description="Task description/body")
    dueDate: Optional[datetime] = Field(None, description="Task due date")
    assignedTo: Optional[str] = Field(None, description="User ID to assign the task to")
    completed: bool = Field(False, description="Whether the task is completed")


class TaskUpdate(BaseModel):
    """Model for updating a task"""

    title: Optional[str] = Field(None, description="Task title")
    body: Optional[str] = Field(None, description="Task description/body")
    dueDate: Optional[datetime] = Field(None, description="Task due date")
    assignedTo: Optional[str] = Field(None, description="User ID to assign the task to")
    completed: Optional[bool] = Field(None, description="Whether the task is completed")


class TaskList(BaseModel):
    """Response model for task list"""

    tasks: List[Task]
    count: int
    total: Optional[int] = None
