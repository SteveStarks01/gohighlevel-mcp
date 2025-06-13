"""Parameter models for OAuth management MCP tools"""

from typing import Optional
from pydantic import BaseModel, Field


class GetInstalledLocationsParams(BaseModel):
    """Parameters for getting installed locations"""

    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GenerateLocationTokenParams(BaseModel):
    """Parameters for generating a location token"""

    location_id: str = Field(..., description="The location ID to generate token for")
    scope: Optional[str] = Field(None, description="Requested scope for the token")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateSaasSubscriptionParams(BaseModel):
    """Parameters for updating SaaS subscription"""

    location_id: str = Field(..., description="The location ID")
    plan_id: Optional[str] = Field(None, description="Plan ID")
    status: Optional[str] = Field(None, description="Subscription status")
    billing_cycle: Optional[str] = Field(None, description="Billing cycle")
    amount: Optional[float] = Field(None, description="Subscription amount")
    currency: Optional[str] = Field(None, description="Currency")
    is_active: Optional[bool] = Field(None, description="Whether subscription is active")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
