"""Campaign parameter classes for MCP tools"""

from typing import Optional
from pydantic import BaseModel, Field


class GetCampaignsParams(BaseModel):
    """Parameters for getting campaigns"""

    location_id: str = Field(..., description="The location ID to get campaigns for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
