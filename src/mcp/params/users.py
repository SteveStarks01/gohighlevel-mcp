"""User parameter classes for MCP tools"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from ...models.user import UserPermissions


class GetUsersParams(BaseModel):
    """Parameters for getting users"""

    location_id: Optional[str] = Field(None, description="The location ID to get users for (optional)")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetUserParams(BaseModel):
    """Parameters for getting a single user"""

    user_id: str = Field(..., description="The user ID to retrieve")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateUserParams(BaseModel):
    """Parameters for creating a user"""

    company_id: str = Field(
        ..., description="The company ID where the user will be created"
    )
    name: str = Field(..., description="User's full name")
    first_name: Optional[str] = Field(None, description="User's first name")
    last_name: Optional[str] = Field(None, description="User's last name")
    email: str = Field(..., description="User's email address")
    phone: Optional[str] = Field(None, description="User's phone number")
    extension: Optional[str] = Field(None, description="User's phone extension")
    
    # Permission fields (simplified for MCP interface)
    campaigns_enabled: Optional[bool] = Field(None, description="Enable campaigns access")
    campaigns_read_only: Optional[bool] = Field(None, description="Campaigns read-only access")
    contacts_enabled: Optional[bool] = Field(None, description="Enable contacts access")
    workflows_enabled: Optional[bool] = Field(None, description="Enable workflows access")
    workflows_read_only: Optional[bool] = Field(None, description="Workflows read-only access")
    opportunities_enabled: Optional[bool] = Field(None, description="Enable opportunities access")
    appointments_enabled: Optional[bool] = Field(None, description="Enable appointments access")
    conversations_enabled: Optional[bool] = Field(None, description="Enable conversations access")
    settings_enabled: Optional[bool] = Field(None, description="Enable settings access")
    
    roles: Optional[List[str]] = Field(None, description="User roles")
    location_ids: Optional[List[str]] = Field(None, description="Location IDs user has access to")
    profile_photo: Optional[str] = Field(None, description="User's profile photo URL")
    user_type: Optional[str] = Field(None, description="User type")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateUserParams(BaseModel):
    """Parameters for updating a user"""

    user_id: str = Field(..., description="The user ID to update")
    name: Optional[str] = Field(None, description="User's full name")
    first_name: Optional[str] = Field(None, description="User's first name")
    last_name: Optional[str] = Field(None, description="User's last name")
    email: Optional[str] = Field(None, description="User's email address")
    phone: Optional[str] = Field(None, description="User's phone number")
    extension: Optional[str] = Field(None, description="User's phone extension")
    
    # Permission fields (simplified for MCP interface)
    campaigns_enabled: Optional[bool] = Field(None, description="Enable campaigns access")
    campaigns_read_only: Optional[bool] = Field(None, description="Campaigns read-only access")
    contacts_enabled: Optional[bool] = Field(None, description="Enable contacts access")
    workflows_enabled: Optional[bool] = Field(None, description="Enable workflows access")
    workflows_read_only: Optional[bool] = Field(None, description="Workflows read-only access")
    opportunities_enabled: Optional[bool] = Field(None, description="Enable opportunities access")
    appointments_enabled: Optional[bool] = Field(None, description="Enable appointments access")
    conversations_enabled: Optional[bool] = Field(None, description="Enable conversations access")
    settings_enabled: Optional[bool] = Field(None, description="Enable settings access")
    
    roles: Optional[List[str]] = Field(None, description="User roles")
    location_ids: Optional[List[str]] = Field(None, description="Location IDs user has access to")
    profile_photo: Optional[str] = Field(None, description="User's profile photo URL")
    user_type: Optional[str] = Field(None, description="User type")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteUserParams(BaseModel):
    """Parameters for deleting a user"""

    user_id: str = Field(..., description="The user ID to delete")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
