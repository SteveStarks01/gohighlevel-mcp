"""Calendar administration tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.calendar import CalendarCreate, CalendarUpdate
from ..params.calendar_admin import (
    CreateCalendarParams,
    UpdateCalendarParams,
    DeleteCalendarParams,
    GetCalendarGroupsParams,
    DeleteCalendarEventParams,
    CreateBlockSlotParams,
    UpdateBlockSlotParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_calendar_admin_tools(mcp_instance, get_client_func):
    """Register all calendar administration tools with the MCP server"""
    global mcp, get_client
    mcp = mcp_instance
    get_client = get_client_func

    @mcp.tool()
    async def create_calendar(params: CreateCalendarParams) -> Dict[str, Any]:
        """Create a new calendar in GoHighLevel"""
        client = await get_client(params.access_token)

        calendar_data = CalendarCreate(
            locationId=params.location_id,
            name=params.name,
            description=params.description,
            calendarType=params.calendar_type,
            eventType=params.event_type,
            eventTitle=params.event_title,
            eventColor=params.event_color,
            slug=params.slug,
            slotDuration=params.slot_duration,
            slotInterval=params.slot_interval,
            isActive=params.is_active,
            autoConfirm=params.auto_confirm,
            allowReschedule=params.allow_reschedule,
            allowCancellation=params.allow_cancellation,
        )

        calendar = await client.create_calendar(calendar_data)
        return {"success": True, "calendar": calendar.model_dump()}

    @mcp.tool()
    async def update_calendar(params: UpdateCalendarParams) -> Dict[str, Any]:
        """Update an existing calendar in GoHighLevel"""
        client = await get_client(params.access_token)

        update_data = CalendarUpdate(
            name=params.name,
            description=params.description,
            calendarType=params.calendar_type,
            eventType=params.event_type,
            eventTitle=params.event_title,
            eventColor=params.event_color,
            slug=params.slug,
            slotDuration=params.slot_duration,
            slotInterval=params.slot_interval,
            isActive=params.is_active,
            autoConfirm=params.auto_confirm,
            allowReschedule=params.allow_reschedule,
            allowCancellation=params.allow_cancellation,
        )

        calendar = await client.update_calendar(params.calendar_id, update_data)
        return {"success": True, "calendar": calendar.model_dump()}

    @mcp.tool()
    async def delete_calendar(params: DeleteCalendarParams) -> Dict[str, Any]:
        """Delete a calendar from GoHighLevel"""
        client = await get_client(params.access_token)

        success = await client.delete_calendar(params.calendar_id)
        return {
            "success": success,
            "message": (
                "Calendar deleted successfully"
                if success
                else "Failed to delete calendar"
            ),
        }

    @mcp.tool()
    async def get_calendar_groups(params: GetCalendarGroupsParams) -> Dict[str, Any]:
        """Get calendar groups for a location"""
        client = await get_client(params.access_token)

        group_list = await client.get_calendar_groups(
            params.location_id, params.limit, params.skip
        )
        return {
            "success": True,
            "groups": [group.model_dump() for group in group_list.groups],
            "count": group_list.count,
            "total": group_list.total,
        }

    # Calendar Events Management Tools

    @mcp.tool()
    async def delete_calendar_event(params: DeleteCalendarEventParams) -> Dict[str, Any]:
        """Delete a calendar event"""
        client = await get_client(params.access_token)

        success = await client.delete_calendar_event(
            params.event_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Calendar event deleted successfully" if success else "Failed to delete calendar event"
            ),
        }

    @mcp.tool()
    async def create_block_slot(params: CreateBlockSlotParams) -> Dict[str, Any]:
        """Create a calendar block slot"""
        client = await get_client(params.access_token)

        block_slot_data = {
            "calendarId": params.calendar_id,
            "startTime": params.start_time,
            "endTime": params.end_time,
        }
        if params.title:
            block_slot_data["title"] = params.title

        result = await client.create_block_slot(block_slot_data, params.location_id)
        return {"success": True, "block_slot": result}

    @mcp.tool()
    async def update_block_slot(params: UpdateBlockSlotParams) -> Dict[str, Any]:
        """Update a calendar block slot"""
        client = await get_client(params.access_token)

        block_slot_data = {}
        if params.calendar_id:
            block_slot_data["calendarId"] = params.calendar_id
        if params.start_time:
            block_slot_data["startTime"] = params.start_time
        if params.end_time:
            block_slot_data["endTime"] = params.end_time
        if params.title:
            block_slot_data["title"] = params.title

        result = await client.update_block_slot(
            params.event_id, block_slot_data, params.location_id
        )
        return {"success": True, "block_slot": result}
