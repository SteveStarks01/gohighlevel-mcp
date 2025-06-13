"""Location models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class LocationAddress(BaseModel):
    """Address for a location"""

    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = Field(default="US")
    postalCode: Optional[str] = None

    model_config = {"populate_by_name": True}


class LocationSettings(BaseModel):
    """Location settings"""

    allowDuplicateContact: Optional[bool] = None
    allowDuplicateOpportunity: Optional[bool] = None
    allowFacebookNameMerge: Optional[bool] = None
    disableContactTimezone: Optional[bool] = None

    model_config = {"populate_by_name": True}


class Location(BaseModel):
    """GoHighLevel Location model"""

    id: Optional[str] = None
    companyId: Optional[str] = None
    name: str
    address: Optional[LocationAddress] = None
    logoUrl: Optional[str] = None
    website: Optional[str] = None
    timezone: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    businessType: Optional[str] = None
    settings: Optional[LocationSettings] = None
    stripeProductId: Optional[str] = None
    dateAdded: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None

    model_config = {"populate_by_name": True}


class LocationCreate(BaseModel):
    """Model for creating a location"""

    companyId: str = Field(..., description="Company ID where the location will be created")
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

    model_config = {"populate_by_name": True}


class LocationUpdate(BaseModel):
    """Model for updating a location"""

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

    model_config = {"populate_by_name": True}


class LocationList(BaseModel):
    """List of locations with metadata"""

    locations: List[Location] = Field(default_factory=list, description="List of locations")
    count: int = Field(default=0, description="Number of locations in this response")
    total: int = Field(default=0, description="Total number of locations available")

    model_config = {"populate_by_name": True}


# Location Tags Models
class LocationTag(BaseModel):
    """Location tag model"""

    id: str = Field(..., description="Tag ID", alias="_id")
    locationId: Optional[str] = Field(None, description="Location ID")
    name: str = Field(..., description="Tag name")
    color: Optional[str] = Field(None, description="Tag color")
    isSystem: Optional[bool] = Field(None, description="Whether this is a system tag")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")

    model_config = {"populate_by_name": True}


class LocationTagCreate(BaseModel):
    """Model for creating a location tag"""

    name: str = Field(..., description="Tag name")
    color: Optional[str] = Field(None, description="Tag color (hex code)")


class LocationTagUpdate(BaseModel):
    """Model for updating a location tag"""

    name: Optional[str] = Field(None, description="Tag name")
    color: Optional[str] = Field(None, description="Tag color (hex code)")


class LocationTagList(BaseModel):
    """List of location tags"""

    tags: List[LocationTag] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}


# Location Custom Values Models
class LocationCustomValue(BaseModel):
    """Location custom value model"""

    id: str = Field(..., description="Custom value ID", alias="_id")
    locationId: Optional[str] = Field(None, description="Location ID")
    key: str = Field(..., description="Custom value key")
    value: Optional[str] = Field(None, description="Custom value")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")

    model_config = {"populate_by_name": True}


class LocationCustomValueCreate(BaseModel):
    """Model for creating a location custom value"""

    key: str = Field(..., description="Custom value key")
    value: str = Field(..., description="Custom value")


class LocationCustomValueUpdate(BaseModel):
    """Model for updating a location custom value"""

    key: Optional[str] = Field(None, description="Custom value key")
    value: Optional[str] = Field(None, description="Custom value")


class LocationCustomValueList(BaseModel):
    """List of location custom values"""

    customValues: List[LocationCustomValue] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}


# Location Custom Fields Models
class LocationCustomFieldOption(BaseModel):
    """Custom field option model"""

    id: Optional[str] = Field(None, description="Option ID")
    name: str = Field(..., description="Option name")
    value: str = Field(..., description="Option value")

    model_config = {"populate_by_name": True}


class LocationCustomField(BaseModel):
    """Location custom field model"""

    id: str = Field(..., description="Custom field ID", alias="_id")
    locationId: Optional[str] = Field(None, description="Location ID")
    name: str = Field(..., description="Field name")
    fieldKey: Optional[str] = Field(None, description="Field key")
    dataType: Optional[str] = Field(None, description="Data type (text, number, date, etc.)")
    position: Optional[int] = Field(None, description="Field position")
    isRequired: Optional[bool] = Field(None, description="Whether field is required")
    placeholder: Optional[str] = Field(None, description="Field placeholder text")
    options: Optional[List[LocationCustomFieldOption]] = Field(None, description="Field options for select/radio")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")

    model_config = {"populate_by_name": True}


class LocationCustomFieldCreate(BaseModel):
    """Model for creating a location custom field"""

    name: str = Field(..., description="Field name")
    fieldKey: Optional[str] = Field(None, description="Field key")
    dataType: str = Field(..., description="Data type (text, number, date, select, radio, checkbox)")
    position: Optional[int] = Field(None, description="Field position")
    isRequired: Optional[bool] = Field(False, description="Whether field is required")
    placeholder: Optional[str] = Field(None, description="Field placeholder text")
    options: Optional[List[LocationCustomFieldOption]] = Field(None, description="Field options for select/radio")


class LocationCustomFieldUpdate(BaseModel):
    """Model for updating a location custom field"""

    name: Optional[str] = Field(None, description="Field name")
    fieldKey: Optional[str] = Field(None, description="Field key")
    dataType: Optional[str] = Field(None, description="Data type")
    position: Optional[int] = Field(None, description="Field position")
    isRequired: Optional[bool] = Field(None, description="Whether field is required")
    placeholder: Optional[str] = Field(None, description="Field placeholder text")
    options: Optional[List[LocationCustomFieldOption]] = Field(None, description="Field options")


class LocationCustomFieldList(BaseModel):
    """List of location custom fields"""

    customFields: List[LocationCustomField] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}


class LocationTemplate(BaseModel):
    """GoHighLevel Location Template model"""

    id: str = Field(..., description="Template ID")
    locationId: str = Field(..., description="Location ID")
    name: str = Field(..., description="Template name")
    type: Optional[str] = Field(None, description="Template type")
    category: Optional[str] = Field(None, description="Template category")
    content: Optional[str] = Field(None, description="Template content")
    isActive: Optional[bool] = Field(True, description="Whether template is active")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")
    createdBy: Optional[str] = Field(None, description="User who created the template")

    model_config = {"populate_by_name": True}


class LocationTemplateList(BaseModel):
    """List of location templates"""

    templates: List[LocationTemplate] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}


class LocationTaskSearchFilters(BaseModel):
    """Search filters for location tasks"""

    assignedTo: Optional[str] = Field(None, description="User ID assigned to")
    contactId: Optional[str] = Field(None, description="Contact ID")
    status: Optional[str] = Field(None, description="Task status")
    dueDate: Optional[str] = Field(None, description="Due date filter")
    dateAdded: Optional[str] = Field(None, description="Date added filter")

    model_config = {"populate_by_name": True}


class LocationTask(BaseModel):
    """GoHighLevel Location Task model"""

    id: str = Field(..., description="Task ID")
    locationId: str = Field(..., description="Location ID")
    title: str = Field(..., description="Task title")
    body: Optional[str] = Field(None, description="Task description")
    assignedTo: Optional[str] = Field(None, description="User ID assigned to")
    contactId: Optional[str] = Field(None, description="Contact ID")
    status: Optional[str] = Field(None, description="Task status")
    dueDate: Optional[datetime] = Field(None, description="Due date")
    dateAdded: Optional[datetime] = Field(None, description="Date added")
    dateUpdated: Optional[datetime] = Field(None, description="Date updated")
    completed: Optional[bool] = Field(False, description="Whether task is completed")

    model_config = {"populate_by_name": True}


class LocationTaskList(BaseModel):
    """List of location tasks"""

    tasks: List[LocationTask] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}
