"""Location parameter classes for MCP tools"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class GetLocationParams(BaseModel):
    """Parameters for getting a single location"""

    location_id: str = Field(..., description="The location ID to retrieve")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class SearchLocationsParams(BaseModel):
    """Parameters for searching locations"""

    company_id: Optional[str] = Field(None, description="Company ID to filter locations")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    search_query: Optional[str] = Field(None, description="Search query for location names")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateLocationParams(BaseModel):
    """Parameters for creating a location"""

    company_id: str = Field(
        ..., description="The company ID where the location will be created"
    )
    name: str = Field(..., description="Location name")
    
    # Address fields
    address: Optional[str] = Field(None, description="Location address")
    city: Optional[str] = Field(None, description="Location city")
    state: Optional[str] = Field(None, description="Location state")
    country: Optional[str] = Field(default="US", description="Location country")
    postal_code: Optional[str] = Field(None, description="Location postal code")
    
    logo_url: Optional[str] = Field(None, description="Location logo URL")
    website: Optional[str] = Field(None, description="Location website")
    timezone: Optional[str] = Field(None, description="Location timezone")
    email: Optional[str] = Field(None, description="Location email")
    phone: Optional[str] = Field(None, description="Location phone")
    business_type: Optional[str] = Field(None, description="Business type")
    
    # Settings
    allow_duplicate_contact: Optional[bool] = Field(None, description="Allow duplicate contacts")
    allow_duplicate_opportunity: Optional[bool] = Field(None, description="Allow duplicate opportunities")
    allow_facebook_name_merge: Optional[bool] = Field(None, description="Allow Facebook name merge")
    disable_contact_timezone: Optional[bool] = Field(None, description="Disable contact timezone")
    
    stripe_product_id: Optional[str] = Field(None, description="Stripe product ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateLocationParams(BaseModel):
    """Parameters for updating a location"""

    location_id: str = Field(..., description="The location ID to update")
    name: Optional[str] = Field(None, description="Location name")
    
    # Address fields
    address: Optional[str] = Field(None, description="Location address")
    city: Optional[str] = Field(None, description="Location city")
    state: Optional[str] = Field(None, description="Location state")
    country: Optional[str] = Field(None, description="Location country")
    postal_code: Optional[str] = Field(None, description="Location postal code")
    
    logo_url: Optional[str] = Field(None, description="Location logo URL")
    website: Optional[str] = Field(None, description="Location website")
    timezone: Optional[str] = Field(None, description="Location timezone")
    email: Optional[str] = Field(None, description="Location email")
    phone: Optional[str] = Field(None, description="Location phone")
    business_type: Optional[str] = Field(None, description="Business type")
    
    # Settings
    allow_duplicate_contact: Optional[bool] = Field(None, description="Allow duplicate contacts")
    allow_duplicate_opportunity: Optional[bool] = Field(None, description="Allow duplicate opportunities")
    allow_facebook_name_merge: Optional[bool] = Field(None, description="Allow Facebook name merge")
    disable_contact_timezone: Optional[bool] = Field(None, description="Disable contact timezone")
    
    stripe_product_id: Optional[str] = Field(None, description="Stripe product ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteLocationParams(BaseModel):
    """Parameters for deleting a location"""

    location_id: str = Field(..., description="The location ID to delete")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
