"""Calendar administration parameter classes for MCP tools"""

from typing import Optional
from pydantic import BaseModel, Field


class CreateCalendarParams(BaseModel):
    """Parameters for creating a calendar"""

    location_id: str = Field(..., description="Location ID where the calendar will be created")
    name: str = Field(..., description="Calendar name")
    description: Optional[str] = Field(None, description="Calendar description")
    calendar_type: Optional[str] = Field(None, description="Calendar type: round_robin, event, personal")
    event_type: Optional[str] = Field(None, description="Event type")
    event_title: Optional[str] = Field(None, description="Default event title template")
    event_color: Optional[str] = Field(None, description="Event color hex code")
    slug: Optional[str] = Field(None, description="Calendar URL slug")
    slot_duration: Optional[int] = Field(None, description="Slot duration in minutes")
    slot_interval: Optional[int] = Field(None, description="Slot interval in minutes")
    is_active: Optional[bool] = Field(default=True, description="Is calendar active")
    auto_confirm: Optional[bool] = Field(None, description="Auto-confirm appointments")
    allow_reschedule: Optional[bool] = Field(None, description="Allow appointment rescheduling")
    allow_cancellation: Optional[bool] = Field(None, description="Allow appointment cancellation")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateCalendarParams(BaseModel):
    """Parameters for updating a calendar"""

    calendar_id: str = Field(..., description="Calendar ID to update")
    name: Optional[str] = Field(None, description="Calendar name")
    description: Optional[str] = Field(None, description="Calendar description")
    calendar_type: Optional[str] = Field(None, description="Calendar type: round_robin, event, personal")
    event_type: Optional[str] = Field(None, description="Event type")
    event_title: Optional[str] = Field(None, description="Default event title template")
    event_color: Optional[str] = Field(None, description="Event color hex code")
    slug: Optional[str] = Field(None, description="Calendar URL slug")
    slot_duration: Optional[int] = Field(None, description="Slot duration in minutes")
    slot_interval: Optional[int] = Field(None, description="Slot interval in minutes")
    is_active: Optional[bool] = Field(None, description="Is calendar active")
    auto_confirm: Optional[bool] = Field(None, description="Auto-confirm appointments")
    allow_reschedule: Optional[bool] = Field(None, description="Allow appointment rescheduling")
    allow_cancellation: Optional[bool] = Field(None, description="Allow appointment cancellation")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteCalendarParams(BaseModel):
    """Parameters for deleting a calendar"""

    calendar_id: str = Field(..., description="Calendar ID to delete")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetCalendarGroupsParams(BaseModel):
    """Parameters for getting calendar groups"""

    location_id: str = Field(..., description="Location ID to get calendar groups for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


# Calendar Events Management Parameters

class DeleteCalendarEventParams(BaseModel):
    """Parameters for deleting a calendar event"""

    event_id: str = Field(..., description="The event ID to delete")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token override"
    )


class CreateBlockSlotParams(BaseModel):
    """Parameters for creating a calendar block slot"""

    location_id: str = Field(..., description="The location ID")
    calendar_id: str = Field(..., description="The calendar ID")
    start_time: str = Field(..., description="Start time in ISO format")
    end_time: str = Field(..., description="End time in ISO format")
    title: Optional[str] = Field(None, description="Block slot title")
    access_token: Optional[str] = Field(
        None, description="Optional access token override"
    )


class UpdateBlockSlotParams(BaseModel):
    """Parameters for updating a calendar block slot"""

    event_id: str = Field(..., description="The event ID to update")
    location_id: str = Field(..., description="The location ID")
    calendar_id: Optional[str] = Field(None, description="The calendar ID")
    start_time: Optional[str] = Field(None, description="Start time in ISO format")
    end_time: Optional[str] = Field(None, description="End time in ISO format")
    title: Optional[str] = Field(None, description="Block slot title")
    access_token: Optional[str] = Field(
        None, description="Optional access token override"
    )
