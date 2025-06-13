"""Extended locations API client for GoHighLevel MCP integration"""

from typing import Optional, Dict, Any
from .base import BaseGoHighLevelClient
from ..models.location import (
    LocationTag, LocationTagList, LocationTagCreate, LocationTagUpdate,
    LocationCustomValue, LocationCustomValueList, LocationCustomValueCreate, LocationCustomValueUpdate,
    LocationCustomField, LocationCustomFieldList, LocationCustomFieldCreate, LocationCustomFieldUpdate,
    LocationTemplate, LocationTemplateList, LocationTask, LocationTaskList, LocationTaskSearchFilters
)


class LocationsExtendedClient(BaseGoHighLevelClient):
    """Extended client for location-specific operations (tags, custom values, custom fields)"""

    # Location Tags Methods
    async def get_location_tags(self, location_id: str, limit: int = 100, skip: int = 0) -> LocationTagList:
        """Get all tags for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            LocationTagList containing tags and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", f"/locations/{location_id}/tags", params=params
        )
        data = response.json()
        
        tags_data = data.get("tags", [])
        return LocationTagList(
            tags=[LocationTag(**tag) for tag in tags_data],
            count=len(tags_data),
            total=data.get("total", len(tags_data)),
        )

    async def get_location_tag(self, location_id: str, tag_id: str) -> LocationTag:
        """Get a specific location tag
        
        Args:
            location_id: The location ID
            tag_id: The tag ID
            
        Returns:
            LocationTag object
        """
        response = await self._request(
            "GET", f"/locations/{location_id}/tags/{tag_id}"
        )
        return LocationTag(**response.json())

    async def create_location_tag(self, location_id: str, tag: LocationTagCreate) -> LocationTag:
        """Create a new location tag
        
        Args:
            location_id: The location ID
            tag: Tag creation data
            
        Returns:
            Created LocationTag object
        """
        response = await self._request(
            "POST",
            f"/locations/{location_id}/tags/",
            json=tag.model_dump(exclude_none=True),
        )
        return LocationTag(**response.json())

    async def update_location_tag(self, location_id: str, tag_id: str, tag: LocationTagUpdate) -> LocationTag:
        """Update a location tag
        
        Args:
            location_id: The location ID
            tag_id: The tag ID
            tag: Tag update data
            
        Returns:
            Updated LocationTag object
        """
        response = await self._request(
            "PUT",
            f"/locations/{location_id}/tags/{tag_id}",
            json=tag.model_dump(exclude_none=True),
        )
        return LocationTag(**response.json())

    async def delete_location_tag(self, location_id: str, tag_id: str) -> Dict[str, Any]:
        """Delete a location tag
        
        Args:
            location_id: The location ID
            tag_id: The tag ID
            
        Returns:
            Success confirmation
        """
        response = await self._request(
            "DELETE", f"/locations/{location_id}/tags/{tag_id}"
        )
        return {"success": True, "message": "Tag deleted successfully"}

    # Location Custom Values Methods
    async def get_location_custom_values(self, location_id: str, limit: int = 100, skip: int = 0) -> LocationCustomValueList:
        """Get all custom values for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            LocationCustomValueList containing custom values and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", f"/locations/{location_id}/customValues", params=params
        )
        data = response.json()
        
        custom_values_data = data.get("customValues", [])
        return LocationCustomValueList(
            customValues=[LocationCustomValue(**cv) for cv in custom_values_data],
            count=len(custom_values_data),
            total=data.get("total", len(custom_values_data)),
        )

    async def get_location_custom_value(self, location_id: str, custom_value_id: str) -> LocationCustomValue:
        """Get a specific location custom value
        
        Args:
            location_id: The location ID
            custom_value_id: The custom value ID
            
        Returns:
            LocationCustomValue object
        """
        response = await self._request(
            "GET", f"/locations/{location_id}/customValues/{custom_value_id}"
        )
        return LocationCustomValue(**response.json())

    async def create_location_custom_value(self, location_id: str, custom_value: LocationCustomValueCreate) -> LocationCustomValue:
        """Create a new location custom value
        
        Args:
            location_id: The location ID
            custom_value: Custom value creation data
            
        Returns:
            Created LocationCustomValue object
        """
        response = await self._request(
            "POST",
            f"/locations/{location_id}/customValues",
            json=custom_value.model_dump(exclude_none=True),
        )
        return LocationCustomValue(**response.json())

    async def update_location_custom_value(self, location_id: str, custom_value_id: str, custom_value: LocationCustomValueUpdate) -> LocationCustomValue:
        """Update a location custom value
        
        Args:
            location_id: The location ID
            custom_value_id: The custom value ID
            custom_value: Custom value update data
            
        Returns:
            Updated LocationCustomValue object
        """
        response = await self._request(
            "PUT",
            f"/locations/{location_id}/customValues/{custom_value_id}",
            json=custom_value.model_dump(exclude_none=True),
        )
        return LocationCustomValue(**response.json())

    async def delete_location_custom_value(self, location_id: str, custom_value_id: str) -> Dict[str, Any]:
        """Delete a location custom value
        
        Args:
            location_id: The location ID
            custom_value_id: The custom value ID
            
        Returns:
            Success confirmation
        """
        response = await self._request(
            "DELETE", f"/locations/{location_id}/customValues/{custom_value_id}"
        )
        return {"success": True, "message": "Custom value deleted successfully"}

    # Location Custom Fields Methods
    async def get_location_custom_fields(self, location_id: str, limit: int = 100, skip: int = 0) -> LocationCustomFieldList:
        """Get all custom fields for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            LocationCustomFieldList containing custom fields and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", f"/locations/{location_id}/customFields", params=params
        )
        data = response.json()
        
        custom_fields_data = data.get("customFields", [])
        return LocationCustomFieldList(
            customFields=[LocationCustomField(**cf) for cf in custom_fields_data],
            count=len(custom_fields_data),
            total=data.get("total", len(custom_fields_data)),
        )

    async def get_location_custom_field(self, location_id: str, custom_field_id: str) -> LocationCustomField:
        """Get a specific location custom field
        
        Args:
            location_id: The location ID
            custom_field_id: The custom field ID
            
        Returns:
            LocationCustomField object
        """
        response = await self._request(
            "GET", f"/locations/{location_id}/customFields/{custom_field_id}"
        )
        return LocationCustomField(**response.json())

    async def create_location_custom_field(self, location_id: str, custom_field: LocationCustomFieldCreate) -> LocationCustomField:
        """Create a new location custom field
        
        Args:
            location_id: The location ID
            custom_field: Custom field creation data
            
        Returns:
            Created LocationCustomField object
        """
        response = await self._request(
            "POST",
            f"/locations/{location_id}/customFields",
            json=custom_field.model_dump(exclude_none=True),
        )
        return LocationCustomField(**response.json())

    async def update_location_custom_field(self, location_id: str, custom_field_id: str, custom_field: LocationCustomFieldUpdate) -> LocationCustomField:
        """Update a location custom field
        
        Args:
            location_id: The location ID
            custom_field_id: The custom field ID
            custom_field: Custom field update data
            
        Returns:
            Updated LocationCustomField object
        """
        response = await self._request(
            "PUT",
            f"/locations/{location_id}/customFields/{custom_field_id}",
            json=custom_field.model_dump(exclude_none=True),
        )
        return LocationCustomField(**response.json())

    async def delete_location_custom_field(self, location_id: str, custom_field_id: str) -> Dict[str, Any]:
        """Delete a location custom field
        
        Args:
            location_id: The location ID
            custom_field_id: The custom field ID
            
        Returns:
            Success confirmation
        """
        response = await self._request(
            "DELETE", f"/locations/{location_id}/customFields/{custom_field_id}"
        )
        return {"success": True, "message": "Custom field deleted successfully"}

    # Location Templates Methods
    async def get_location_templates(self, location_id: str, limit: int = 100, skip: int = 0) -> LocationTemplateList:
        """Get all templates for a location

        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip

        Returns:
            LocationTemplateList containing templates and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip

        response = await self._request(
            "GET", f"/locations/{location_id}/templates", params=params
        )
        data = response.json()

        templates_data = data.get("templates", [])
        return LocationTemplateList(
            templates=[LocationTemplate(**template) for template in templates_data],
            count=len(templates_data),
            total=data.get("total", len(templates_data)),
        )

    # Location Tasks Methods
    async def search_location_tasks(
        self,
        location_id: str,
        filters: Optional[LocationTaskSearchFilters] = None,
        limit: int = 100,
        skip: int = 0
    ) -> LocationTaskList:
        """Search tasks for a location

        Args:
            location_id: The location ID
            filters: Optional search filters
            limit: Number of results to return (max 100)
            skip: Number of results to skip

        Returns:
            LocationTaskList containing tasks and metadata
        """
        search_data = {"limit": limit}
        if skip > 0:
            search_data["skip"] = skip

        if filters:
            search_data.update(filters.model_dump(exclude_none=True))

        response = await self._request(
            "POST", f"/locations/{location_id}/tasks/search", json=search_data
        )
        data = response.json()

        tasks_data = data.get("tasks", [])
        return LocationTaskList(
            tasks=[LocationTask(**task) for task in tasks_data],
            count=len(tasks_data),
            total=data.get("total", len(tasks_data)),
        )
