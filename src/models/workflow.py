"""Workflow models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class Workflow(BaseModel):
    """GoHighLevel Workflow model"""

    id: Optional[str] = None
    locationId: Optional[str] = None
    name: str
    status: Optional[str] = None
    version: Optional[int] = None
    description: Optional[str] = None
    createdBy: Optional[str] = None
    dateAdded: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None

    model_config = {"populate_by_name": True}


class WorkflowList(BaseModel):
    """List of workflows with metadata"""

    workflows: List[Workflow] = Field(default_factory=list, description="List of workflows")
    count: int = Field(default=0, description="Number of workflows in this response")
    total: int = Field(default=0, description="Total number of workflows available")

    model_config = {"populate_by_name": True}
