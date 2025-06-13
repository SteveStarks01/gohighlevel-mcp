"""User models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class UserPermissions(BaseModel):
    """User permissions model"""

    campaignsEnabled: Optional[bool] = None
    campaignsReadOnly: Optional[bool] = None
    contactsEnabled: Optional[bool] = None
    workflowsEnabled: Optional[bool] = None
    workflowsReadOnly: Optional[bool] = None
    triggersEnabled: Optional[bool] = None
    funnelsEnabled: Optional[bool] = None
    websitesEnabled: Optional[bool] = None
    opportunitiesEnabled: Optional[bool] = None
    dashboardStatsEnabled: Optional[bool] = None
    bulkRequestsEnabled: Optional[bool] = None
    appointmentsEnabled: Optional[bool] = None
    reviewsEnabled: Optional[bool] = None
    onlineListingsEnabled: Optional[bool] = None
    phoneCallEnabled: Optional[bool] = None
    conversationsEnabled: Optional[bool] = None
    assignedDataOnly: Optional[bool] = None
    adwordsReportingEnabled: Optional[bool] = None
    membershipEnabled: Optional[bool] = None
    facebookAdsReportingEnabled: Optional[bool] = None
    attributionsReportingEnabled: Optional[bool] = None
    settingsEnabled: Optional[bool] = None
    tagsEnabled: Optional[bool] = None
    leadValueEnabled: Optional[bool] = None
    marketingEnabled: Optional[bool] = None
    agentReportingEnabled: Optional[bool] = None
    botService: Optional[bool] = None
    socialPlanner: Optional[bool] = None
    bloggingEnabled: Optional[bool] = None
    invoiceEnabled: Optional[bool] = None
    affiliateManagerEnabled: Optional[bool] = None
    contentAiEnabled: Optional[bool] = None
    refundsEnabled: Optional[bool] = None
    recordPaymentEnabled: Optional[bool] = None
    paymentsEnabled: Optional[bool] = None
    communitiesEnabled: Optional[bool] = None
    exportPaymentsEnabled: Optional[bool] = None

    model_config = {"populate_by_name": True}


class User(BaseModel):
    """GoHighLevel User model"""

    id: Optional[str] = None
    name: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    email: str
    phone: Optional[str] = None
    extension: Optional[str] = None
    permissions: Optional[UserPermissions] = None
    roles: Optional[List[str]] = None
    locationIds: Optional[List[str]] = None
    profilePhoto: Optional[str] = None
    deleted: Optional[bool] = None
    type: Optional[str] = None
    dateAdded: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None

    model_config = {"populate_by_name": True}


class UserCreate(BaseModel):
    """Model for creating a user"""

    companyId: str = Field(..., description="Company ID where the user will be created")
    name: str = Field(..., description="User's full name")
    firstName: Optional[str] = Field(None, description="User's first name")
    lastName: Optional[str] = Field(None, description="User's last name")
    email: str = Field(..., description="User's email address")
    phone: Optional[str] = Field(None, description="User's phone number")
    extension: Optional[str] = Field(None, description="User's phone extension")
    permissions: Optional[UserPermissions] = Field(None, description="User permissions")
    roles: Optional[List[str]] = Field(None, description="User roles")
    locationIds: Optional[List[str]] = Field(None, description="Location IDs user has access to")
    profilePhoto: Optional[str] = Field(None, description="User's profile photo URL")
    type: Optional[str] = Field(None, description="User type")

    model_config = {"populate_by_name": True}


class UserUpdate(BaseModel):
    """Model for updating a user"""

    name: Optional[str] = Field(None, description="User's full name")
    firstName: Optional[str] = Field(None, description="User's first name")
    lastName: Optional[str] = Field(None, description="User's last name")
    email: Optional[str] = Field(None, description="User's email address")
    phone: Optional[str] = Field(None, description="User's phone number")
    extension: Optional[str] = Field(None, description="User's phone extension")
    permissions: Optional[UserPermissions] = Field(None, description="User permissions")
    roles: Optional[List[str]] = Field(None, description="User roles")
    locationIds: Optional[List[str]] = Field(None, description="Location IDs user has access to")
    profilePhoto: Optional[str] = Field(None, description="User's profile photo URL")
    type: Optional[str] = Field(None, description="User type")

    model_config = {"populate_by_name": True}


class UserList(BaseModel):
    """List of users with metadata"""

    users: List[User] = Field(default_factory=list, description="List of users")
    count: int = Field(default=0, description="Number of users in this response")
    total: int = Field(default=0, description="Total number of users available")

    model_config = {"populate_by_name": True}
