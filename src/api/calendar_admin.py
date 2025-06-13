"""Calendar administration client for GoHighLevel API v2"""

from typing import List, Optional

from .base import BaseGoHighLevelClient
from ..models.calendar import Calendar, CalendarCreate, CalendarUpdate, CalendarGroup, CalendarGroupList


class CalendarAdminClient(BaseGoHighLevelClient):
    """Client for calendar administration endpoints"""

    async def create_calendar(self, calendar: CalendarCreate) -> Calendar:
        """Create a new calendar
        
        Args:
            calendar: Calendar creation data
            
        Returns:
            Created Calendar object
        """
        response = await self._request(
            "POST",
            "/calendars",
            json=calendar.model_dump(exclude_none=True),
            location_id=calendar.locationId,
        )
        data = response.json()
        return Calendar(**data.get("calendar", data))

    async def update_calendar(
        self, calendar_id: str, updates: CalendarUpdate
    ) -> Calendar:
        """Update an existing calendar
        
        Args:
            calendar_id: The calendar ID to update
            updates: Calendar update data
            
        Returns:
            Updated Calendar object
        """
        response = await self._request(
            "PUT",
            f"/calendars/{calendar_id}",
            json=updates.model_dump(exclude_none=True),
        )
        data = response.json()
        return Calendar(**data.get("calendar", data))

    async def delete_calendar(self, calendar_id: str) -> bool:
        """Delete a calendar
        
        Args:
            calendar_id: The calendar ID to delete
            
        Returns:
            True if deletion was successful
        """
        response = await self._request(
            "DELETE", f"/calendars/{calendar_id}"
        )
        return response.status_code == 200

    async def get_calendar_groups(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> CalendarGroupList:
        """Get calendar groups for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            CalendarGroupList with groups
        """
        params = {"locationId": location_id, "limit": limit}
        if skip > 0:
            params["skip"] = skip

        response = await self._request(
            "GET", "/calendars/groups", params=params, location_id=location_id
        )
        
        data = response.json()
        groups_data = data.get("groups", [])
        return CalendarGroupList(
            groups=[CalendarGroup(**group) for group in groups_data],
            count=len(groups_data),
            total=data.get("total", len(groups_data)),
        )

    # Calendar Events Management Methods

    async def delete_calendar_event(self, event_id: str, location_id: str) -> bool:
        """Delete a calendar event

        Args:
            event_id: The event ID to delete
            location_id: The location ID

        Returns:
            True if deletion was successful
        """
        response = await self._request(
            "DELETE",
            f"/calendars/events/{event_id}",
            location_id=location_id,
        )
        return response.status_code == 200

    async def create_block_slot(self, block_slot_data: dict, location_id: str) -> dict:
        """Create a calendar block slot

        Args:
            block_slot_data: Block slot creation data
            location_id: The location ID

        Returns:
            Created block slot data
        """
        response = await self._request(
            "POST",
            "/calendars/events/block-slots",
            json=block_slot_data,
            location_id=location_id,
        )
        return response.json()

    async def update_block_slot(self, event_id: str, block_slot_data: dict, location_id: str) -> dict:
        """Update a calendar block slot

        Args:
            event_id: The event ID to update
            block_slot_data: Block slot update data
            location_id: The location ID

        Returns:
            Updated block slot data
        """
        response = await self._request(
            "PUT",
            f"/calendars/events/block-slots/{event_id}",
            json=block_slot_data,
            location_id=location_id,
        )
        return response.json()
