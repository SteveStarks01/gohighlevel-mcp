"""Link models for GoHighLevel MCP integration"""

from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field


class Link(BaseModel):
    """GoHighLevel Link model"""

    id: str = Field(..., description="Link ID")
    locationId: str = Field(..., description="Location ID")
    name: str = Field(..., description="Link name")
    url: str = Field(..., description="Target URL")
    shortUrl: Optional[str] = Field(None, description="Shortened URL")
    description: Optional[str] = Field(None, description="Link description")
    isActive: Optional[bool] = Field(True, description="Whether link is active")
    clickCount: Optional[int] = Field(0, description="Number of clicks")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")
    createdBy: Optional[str] = Field(None, description="User who created the link")

    model_config = {"populate_by_name": True}


class LinkCreate(BaseModel):
    """Model for creating a link"""

    name: str = Field(..., description="Link name")
    url: str = Field(..., description="Target URL")
    description: Optional[str] = Field(None, description="Link description")
    isActive: Optional[bool] = Field(True, description="Whether link is active")


class LinkUpdate(BaseModel):
    """Model for updating a link"""

    name: Optional[str] = Field(None, description="Link name")
    url: Optional[str] = Field(None, description="Target URL")
    description: Optional[str] = Field(None, description="Link description")
    isActive: Optional[bool] = Field(None, description="Whether link is active")


class LinkList(BaseModel):
    """List of links"""

    links: List[Link] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}
