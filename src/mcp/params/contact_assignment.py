"""Contact campaign/workflow assignment parameter classes for MCP tools"""

from typing import Optional
from pydantic import BaseModel, Field


class AddContactToCampaignParams(BaseModel):
    """Parameters for adding a contact to a campaign"""

    contact_id: str = Field(..., description="The contact ID")
    campaign_id: str = Field(..., description="The campaign ID")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token override"
    )


class RemoveContactFromCampaignParams(BaseModel):
    """Parameters for removing a contact from a specific campaign"""

    contact_id: str = Field(..., description="The contact ID")
    campaign_id: str = Field(..., description="The campaign ID")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token override"
    )


class RemoveContactFromAllCampaignsParams(BaseModel):
    """Parameters for removing a contact from all campaigns"""

    contact_id: str = Field(..., description="The contact ID")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token override"
    )


class AddContactToWorkflowParams(BaseModel):
    """Parameters for adding a contact to a workflow"""

    contact_id: str = Field(..., description="The contact ID")
    workflow_id: str = Field(..., description="The workflow ID")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token override"
    )


class RemoveContactFromWorkflowParams(BaseModel):
    """Parameters for removing a contact from a workflow"""

    contact_id: str = Field(..., description="The contact ID")
    workflow_id: str = Field(..., description="The workflow ID")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token override"
    )
