"""Business models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class BusinessAddress(BaseModel):
    """Address for a business"""

    address1: Optional[str] = None
    address2: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = Field(default="US")
    postalCode: Optional[str] = None

    model_config = {"populate_by_name": True}


class Business(BaseModel):
    """GoHighLevel Business model"""

    id: Optional[str] = None
    locationId: Optional[str] = None
    name: str
    description: Optional[str] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[BusinessAddress] = None
    logoUrl: Optional[str] = None
    industry: Optional[str] = None
    employeeCount: Optional[int] = None
    annualRevenue: Optional[float] = None
    customFields: Optional[List[Dict[str, Any]]] = None
    tags: Optional[List[str]] = None
    dateAdded: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None

    model_config = {"populate_by_name": True}


class BusinessCreate(BaseModel):
    """Model for creating a business"""

    locationId: str = Field(..., description="Location ID where the business will be created")
    name: str = Field(..., description="Business name")
    description: Optional[str] = Field(None, description="Business description")
    website: Optional[str] = Field(None, description="Business website URL")
    phone: Optional[str] = Field(None, description="Business phone number")
    email: Optional[str] = Field(None, description="Business email address")
    address: Optional[BusinessAddress] = Field(None, description="Business address")
    logoUrl: Optional[str] = Field(None, description="Business logo URL")
    industry: Optional[str] = Field(None, description="Business industry")
    employeeCount: Optional[int] = Field(None, description="Number of employees")
    annualRevenue: Optional[float] = Field(None, description="Annual revenue")
    customFields: Optional[List[Dict[str, Any]]] = Field(None, description="Custom fields")
    tags: Optional[List[str]] = Field(None, description="Business tags")

    model_config = {"populate_by_name": True}


class BusinessUpdate(BaseModel):
    """Model for updating a business"""

    name: Optional[str] = Field(None, description="Business name")
    description: Optional[str] = Field(None, description="Business description")
    website: Optional[str] = Field(None, description="Business website URL")
    phone: Optional[str] = Field(None, description="Business phone number")
    email: Optional[str] = Field(None, description="Business email address")
    address: Optional[BusinessAddress] = Field(None, description="Business address")
    logoUrl: Optional[str] = Field(None, description="Business logo URL")
    industry: Optional[str] = Field(None, description="Business industry")
    employeeCount: Optional[int] = Field(None, description="Number of employees")
    annualRevenue: Optional[float] = Field(None, description="Annual revenue")
    customFields: Optional[List[Dict[str, Any]]] = Field(None, description="Custom fields")
    tags: Optional[List[str]] = Field(None, description="Business tags")

    model_config = {"populate_by_name": True}


class BusinessList(BaseModel):
    """List of businesses with metadata"""

    businesses: List[Business] = Field(default_factory=list, description="List of businesses")
    count: int = Field(default=0, description="Number of businesses in this response")
    total: int = Field(default=0, description="Total number of businesses available")

    model_config = {"populate_by_name": True}
