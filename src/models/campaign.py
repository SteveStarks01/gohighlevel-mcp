"""Campaign models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class Campaign(BaseModel):
    """GoHighLevel Campaign model"""

    id: Optional[str] = None
    locationId: Optional[str] = None
    name: str
    status: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    createdBy: Optional[str] = None
    dateAdded: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None

    model_config = {"populate_by_name": True}


class CampaignList(BaseModel):
    """List of campaigns with metadata"""

    campaigns: List[Campaign] = Field(default_factory=list, description="List of campaigns")
    count: int = Field(default=0, description="Number of campaigns in this response")
    total: int = Field(default=0, description="Total number of campaigns available")

    model_config = {"populate_by_name": True}
