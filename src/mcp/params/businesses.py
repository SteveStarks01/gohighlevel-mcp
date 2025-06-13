"""Business parameter classes for MCP tools"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from ...models.business import BusinessAddress


class GetBusinessesParams(BaseModel):
    """Parameters for getting businesses"""

    location_id: str = Field(..., description="The location ID to get businesses for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetBusinessParams(BaseModel):
    """Parameters for getting a single business"""

    business_id: str = Field(..., description="The business ID to retrieve")
    location_id: str = Field(
        ..., description="The location ID where the business exists"
    )
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateBusinessParams(BaseModel):
    """Parameters for creating a business"""

    location_id: str = Field(
        ..., description="The location ID where the business will be created"
    )
    name: str = Field(..., description="Business name")
    description: Optional[str] = Field(None, description="Business description")
    website: Optional[str] = Field(None, description="Business website URL")
    phone: Optional[str] = Field(None, description="Business phone number")
    email: Optional[str] = Field(None, description="Business email address")
    
    # Address fields
    address1: Optional[str] = Field(None, description="Business address line 1")
    address2: Optional[str] = Field(None, description="Business address line 2")
    city: Optional[str] = Field(None, description="Business city")
    state: Optional[str] = Field(None, description="Business state")
    country: Optional[str] = Field(default="US", description="Business country")
    postal_code: Optional[str] = Field(None, description="Business postal code")
    
    logo_url: Optional[str] = Field(None, description="Business logo URL")
    industry: Optional[str] = Field(None, description="Business industry")
    employee_count: Optional[int] = Field(None, description="Number of employees")
    annual_revenue: Optional[float] = Field(None, description="Annual revenue")
    custom_fields: Optional[Dict[str, Any]] = Field(None, description="Custom fields")
    tags: Optional[List[str]] = Field(None, description="Business tags")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateBusinessParams(BaseModel):
    """Parameters for updating a business"""

    business_id: str = Field(..., description="The business ID to update")
    location_id: str = Field(
        ..., description="The location ID where the business exists"
    )
    name: Optional[str] = Field(None, description="Business name")
    description: Optional[str] = Field(None, description="Business description")
    website: Optional[str] = Field(None, description="Business website URL")
    phone: Optional[str] = Field(None, description="Business phone number")
    email: Optional[str] = Field(None, description="Business email address")
    
    # Address fields
    address1: Optional[str] = Field(None, description="Business address line 1")
    address2: Optional[str] = Field(None, description="Business address line 2")
    city: Optional[str] = Field(None, description="Business city")
    state: Optional[str] = Field(None, description="Business state")
    country: Optional[str] = Field(None, description="Business country")
    postal_code: Optional[str] = Field(None, description="Business postal code")
    
    logo_url: Optional[str] = Field(None, description="Business logo URL")
    industry: Optional[str] = Field(None, description="Business industry")
    employee_count: Optional[int] = Field(None, description="Number of employees")
    annual_revenue: Optional[float] = Field(None, description="Annual revenue")
    custom_fields: Optional[Dict[str, Any]] = Field(None, description="Custom fields")
    tags: Optional[List[str]] = Field(None, description="Business tags")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteBusinessParams(BaseModel):
    """Parameters for deleting a business"""

    business_id: str = Field(..., description="The business ID to delete")
    location_id: str = Field(
        ..., description="The location ID where the business exists"
    )
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
