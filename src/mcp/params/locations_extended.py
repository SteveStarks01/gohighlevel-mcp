"""Parameter models for extended locations MCP tools"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


# Location Tags Parameters
class GetLocationTagsParams(BaseModel):
    """Parameters for getting location tags"""

    location_id: str = Field(..., description="The location ID to get tags for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetLocationTagParams(BaseModel):
    """Parameters for getting a single location tag"""

    location_id: str = Field(..., description="The location ID")
    tag_id: str = Field(..., description="The tag ID to retrieve")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateLocationTagParams(BaseModel):
    """Parameters for creating a location tag"""

    location_id: str = Field(..., description="The location ID")
    name: str = Field(..., description="Tag name")
    color: Optional[str] = Field(None, description="Tag color (hex code)")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateLocationTagParams(BaseModel):
    """Parameters for updating a location tag"""

    location_id: str = Field(..., description="The location ID")
    tag_id: str = Field(..., description="The tag ID to update")
    name: Optional[str] = Field(None, description="Tag name")
    color: Optional[str] = Field(None, description="Tag color (hex code)")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteLocationTagParams(BaseModel):
    """Parameters for deleting a location tag"""

    location_id: str = Field(..., description="The location ID")
    tag_id: str = Field(..., description="The tag ID to delete")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


# Location Custom Values Parameters
class GetLocationCustomValuesParams(BaseModel):
    """Parameters for getting location custom values"""

    location_id: str = Field(..., description="The location ID to get custom values for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetLocationCustomValueParams(BaseModel):
    """Parameters for getting a single location custom value"""

    location_id: str = Field(..., description="The location ID")
    custom_value_id: str = Field(..., description="The custom value ID to retrieve")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateLocationCustomValueParams(BaseModel):
    """Parameters for creating a location custom value"""

    location_id: str = Field(..., description="The location ID")
    key: str = Field(..., description="Custom value key")
    value: str = Field(..., description="Custom value")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateLocationCustomValueParams(BaseModel):
    """Parameters for updating a location custom value"""

    location_id: str = Field(..., description="The location ID")
    custom_value_id: str = Field(..., description="The custom value ID to update")
    key: Optional[str] = Field(None, description="Custom value key")
    value: Optional[str] = Field(None, description="Custom value")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteLocationCustomValueParams(BaseModel):
    """Parameters for deleting a location custom value"""

    location_id: str = Field(..., description="The location ID")
    custom_value_id: str = Field(..., description="The custom value ID to delete")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


# Location Custom Fields Parameters
class GetLocationCustomFieldsParams(BaseModel):
    """Parameters for getting location custom fields"""

    location_id: str = Field(..., description="The location ID to get custom fields for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetLocationCustomFieldParams(BaseModel):
    """Parameters for getting a single location custom field"""

    location_id: str = Field(..., description="The location ID")
    custom_field_id: str = Field(..., description="The custom field ID to retrieve")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateLocationCustomFieldParams(BaseModel):
    """Parameters for creating a location custom field"""

    location_id: str = Field(..., description="The location ID")
    name: str = Field(..., description="Field name")
    field_key: Optional[str] = Field(None, description="Field key")
    data_type: str = Field(..., description="Data type (text, number, date, select, radio, checkbox)")
    position: Optional[int] = Field(None, description="Field position")
    is_required: Optional[bool] = Field(False, description="Whether field is required")
    placeholder: Optional[str] = Field(None, description="Field placeholder text")
    options: Optional[List[Dict[str, str]]] = Field(None, description="Field options for select/radio")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateLocationCustomFieldParams(BaseModel):
    """Parameters for updating a location custom field"""

    location_id: str = Field(..., description="The location ID")
    custom_field_id: str = Field(..., description="The custom field ID to update")
    name: Optional[str] = Field(None, description="Field name")
    field_key: Optional[str] = Field(None, description="Field key")
    data_type: Optional[str] = Field(None, description="Data type")
    position: Optional[int] = Field(None, description="Field position")
    is_required: Optional[bool] = Field(None, description="Whether field is required")
    placeholder: Optional[str] = Field(None, description="Field placeholder text")
    options: Optional[List[Dict[str, str]]] = Field(None, description="Field options")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteLocationCustomFieldParams(BaseModel):
    """Parameters for deleting a location custom field"""

    location_id: str = Field(..., description="The location ID")
    custom_field_id: str = Field(..., description="The custom field ID to delete")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


# Location Templates Parameters

class GetLocationTemplatesParams(BaseModel):
    """Parameters for getting location templates"""

    location_id: str = Field(..., description="The location ID to get templates for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


# Location Tasks Parameters

class SearchLocationTasksParams(BaseModel):
    """Parameters for searching location tasks"""

    location_id: str = Field(..., description="The location ID to search tasks for")
    assigned_to: Optional[str] = Field(None, description="User ID assigned to")
    contact_id: Optional[str] = Field(None, description="Contact ID")
    status: Optional[str] = Field(None, description="Task status")
    due_date: Optional[str] = Field(None, description="Due date filter")
    date_added: Optional[str] = Field(None, description="Date added filter")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
