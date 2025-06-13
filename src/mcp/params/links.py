"""Parameter models for links MCP tools"""

from typing import Optional
from pydantic import BaseModel, Field


class GetLinksParams(BaseModel):
    """Parameters for getting links"""

    location_id: str = Field(..., description="The location ID to get links for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetLinkParams(BaseModel):
    """Parameters for getting a single link"""

    location_id: str = Field(..., description="The location ID")
    link_id: str = Field(..., description="The link ID to retrieve")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateLinkParams(BaseModel):
    """Parameters for creating a link"""

    location_id: str = Field(..., description="The location ID")
    name: str = Field(..., description="Link name")
    url: str = Field(..., description="Target URL")
    description: Optional[str] = Field(None, description="Link description")
    is_active: Optional[bool] = Field(True, description="Whether link is active")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateLinkParams(BaseModel):
    """Parameters for updating a link"""

    location_id: str = Field(..., description="The location ID")
    link_id: str = Field(..., description="The link ID to update")
    name: Optional[str] = Field(None, description="Link name")
    url: Optional[str] = Field(None, description="Target URL")
    description: Optional[str] = Field(None, description="Link description")
    is_active: Optional[bool] = Field(None, description="Whether link is active")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteLinkParams(BaseModel):
    """Parameters for deleting a link"""

    location_id: str = Field(..., description="The location ID")
    link_id: str = Field(..., description="The link ID to delete")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
