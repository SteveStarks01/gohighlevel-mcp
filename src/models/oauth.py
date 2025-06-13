"""OAuth and SaaS models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class InstalledLocation(BaseModel):
    """OAuth Installed Location model"""

    locationId: str = Field(..., description="Location ID")
    locationName: str = Field(..., description="Location name")
    companyId: str = Field(..., description="Company ID")
    companyName: str = Field(..., description="Company name")
    installedAt: Optional[datetime] = Field(None, description="Installation date")
    isActive: Optional[bool] = Field(True, description="Whether installation is active")
    permissions: Optional[List[str]] = Field(None, description="Granted permissions")

    model_config = {"populate_by_name": True}


class InstalledLocationList(BaseModel):
    """List of installed locations"""

    locations: List[InstalledLocation] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}


class LocationToken(BaseModel):
    """Location Token model"""

    locationId: str = Field(..., description="Location ID")
    accessToken: str = Field(..., description="Access token")
    tokenType: Optional[str] = Field("Bearer", description="Token type")
    expiresIn: Optional[int] = Field(None, description="Token expiration in seconds")
    scope: Optional[str] = Field(None, description="Token scope")
    createdAt: Optional[datetime] = Field(None, description="Token creation date")

    model_config = {"populate_by_name": True}


class LocationTokenRequest(BaseModel):
    """Location Token Request model"""

    locationId: str = Field(..., description="Location ID")
    scope: Optional[str] = Field(None, description="Requested scope")


class SaasSubscription(BaseModel):
    """SaaS Subscription model"""

    locationId: str = Field(..., description="Location ID")
    planId: str = Field(..., description="Plan ID")
    status: str = Field(..., description="Subscription status")
    billingCycle: Optional[str] = Field(None, description="Billing cycle")
    amount: Optional[float] = Field(None, description="Subscription amount")
    currency: Optional[str] = Field("USD", description="Currency")
    startDate: Optional[datetime] = Field(None, description="Subscription start date")
    endDate: Optional[datetime] = Field(None, description="Subscription end date")
    trialEndDate: Optional[datetime] = Field(None, description="Trial end date")
    isActive: Optional[bool] = Field(True, description="Whether subscription is active")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")

    model_config = {"populate_by_name": True}


class SaasSubscriptionUpdate(BaseModel):
    """SaaS Subscription Update model"""

    planId: Optional[str] = Field(None, description="Plan ID")
    status: Optional[str] = Field(None, description="Subscription status")
    billingCycle: Optional[str] = Field(None, description="Billing cycle")
    amount: Optional[float] = Field(None, description="Subscription amount")
    currency: Optional[str] = Field(None, description="Currency")
    startDate: Optional[datetime] = Field(None, description="Subscription start date")
    endDate: Optional[datetime] = Field(None, description="Subscription end date")
    trialEndDate: Optional[datetime] = Field(None, description="Trial end date")
    isActive: Optional[bool] = Field(None, description="Whether subscription is active")
