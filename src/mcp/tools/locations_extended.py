"""Extended locations MCP tools for GoHighLevel integration"""

from typing import Dict, Any

from ...models.location import (
    LocationTagCreate, LocationTagUpdate,
    LocationCustomValueCreate, LocationCustomValueUpdate,
    LocationCustomFieldCreate, LocationCustomFieldUpdate, LocationCustomFieldOption,
    LocationTaskSearchFilters
)
from ..params.locations_extended import (
    GetLocationTagsParams, GetLocationTagParams, CreateLocationTagParams, UpdateLocationTagParams, DeleteLocationTagParams,
    GetLocationCustomValuesParams, GetLocationCustomValueParams, CreateLocationCustomValueParams, UpdateLocationCustomValueParams, DeleteLocationCustomValueParams,
    GetLocationCustomFieldsParams, GetLocationCustomFieldParams, CreateLocationCustomFieldParams, UpdateLocationCustomFieldParams, DeleteLocationCustomFieldParams,
    GetLocationTemplatesParams, SearchLocationTasksParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_locations_extended_tools(_mcp, _get_client):
    """Register all extended locations MCP tools"""
    global mcp, get_client
    mcp = _mcp
    get_client = _get_client

    # Location Tags Tools
    @mcp.tool()
    async def get_location_tags(params: GetLocationTagsParams) -> Dict[str, Any]:
        """Get all tags for a location"""
        client = await get_client(params.access_token)

        tags = await client.get_location_tags(params.location_id, params.limit, params.skip)
        return {"success": True, "tags": tags.model_dump()}

    @mcp.tool()
    async def get_location_tag(params: GetLocationTagParams) -> Dict[str, Any]:
        """Get a specific location tag"""
        client = await get_client(params.access_token)

        tag = await client.get_location_tag(params.location_id, params.tag_id)
        return {"success": True, "tag": tag.model_dump()}

    @mcp.tool()
    async def create_location_tag(params: CreateLocationTagParams) -> Dict[str, Any]:
        """Create a new location tag"""
        client = await get_client(params.access_token)

        tag_data = LocationTagCreate(
            name=params.name,
            color=params.color,
        )

        tag = await client.create_location_tag(params.location_id, tag_data)
        return {"success": True, "tag": tag.model_dump()}

    @mcp.tool()
    async def update_location_tag(params: UpdateLocationTagParams) -> Dict[str, Any]:
        """Update a location tag"""
        client = await get_client(params.access_token)

        tag_data = LocationTagUpdate(
            name=params.name,
            color=params.color,
        )

        tag = await client.update_location_tag(params.location_id, params.tag_id, tag_data)
        return {"success": True, "tag": tag.model_dump()}

    @mcp.tool()
    async def delete_location_tag(params: DeleteLocationTagParams) -> Dict[str, Any]:
        """Delete a location tag"""
        client = await get_client(params.access_token)

        result = await client.delete_location_tag(params.location_id, params.tag_id)
        return result

    # Location Custom Values Tools
    @mcp.tool()
    async def get_location_custom_values(params: GetLocationCustomValuesParams) -> Dict[str, Any]:
        """Get all custom values for a location"""
        client = await get_client(params.access_token)

        custom_values = await client.get_location_custom_values(params.location_id, params.limit, params.skip)
        return {"success": True, "customValues": custom_values.model_dump()}

    @mcp.tool()
    async def get_location_custom_value(params: GetLocationCustomValueParams) -> Dict[str, Any]:
        """Get a specific location custom value"""
        client = await get_client(params.access_token)

        custom_value = await client.get_location_custom_value(params.location_id, params.custom_value_id)
        return {"success": True, "customValue": custom_value.model_dump()}

    @mcp.tool()
    async def create_location_custom_value(params: CreateLocationCustomValueParams) -> Dict[str, Any]:
        """Create a new location custom value"""
        client = await get_client(params.access_token)

        custom_value_data = LocationCustomValueCreate(
            key=params.key,
            value=params.value,
        )

        custom_value = await client.create_location_custom_value(params.location_id, custom_value_data)
        return {"success": True, "customValue": custom_value.model_dump()}

    @mcp.tool()
    async def update_location_custom_value(params: UpdateLocationCustomValueParams) -> Dict[str, Any]:
        """Update a location custom value"""
        client = await get_client(params.access_token)

        custom_value_data = LocationCustomValueUpdate(
            key=params.key,
            value=params.value,
        )

        custom_value = await client.update_location_custom_value(params.location_id, params.custom_value_id, custom_value_data)
        return {"success": True, "customValue": custom_value.model_dump()}

    @mcp.tool()
    async def delete_location_custom_value(params: DeleteLocationCustomValueParams) -> Dict[str, Any]:
        """Delete a location custom value"""
        client = await get_client(params.access_token)

        result = await client.delete_location_custom_value(params.location_id, params.custom_value_id)
        return result

    # Location Custom Fields Tools
    @mcp.tool()
    async def get_location_custom_fields(params: GetLocationCustomFieldsParams) -> Dict[str, Any]:
        """Get all custom fields for a location"""
        client = await get_client(params.access_token)

        custom_fields = await client.get_location_custom_fields(params.location_id, params.limit, params.skip)
        return {"success": True, "customFields": custom_fields.model_dump()}

    @mcp.tool()
    async def get_location_custom_field(params: GetLocationCustomFieldParams) -> Dict[str, Any]:
        """Get a specific location custom field"""
        client = await get_client(params.access_token)

        custom_field = await client.get_location_custom_field(params.location_id, params.custom_field_id)
        return {"success": True, "customField": custom_field.model_dump()}

    @mcp.tool()
    async def create_location_custom_field(params: CreateLocationCustomFieldParams) -> Dict[str, Any]:
        """Create a new location custom field"""
        client = await get_client(params.access_token)

        # Convert options if provided
        options = None
        if params.options:
            options = [LocationCustomFieldOption(**opt) for opt in params.options]

        custom_field_data = LocationCustomFieldCreate(
            name=params.name,
            fieldKey=params.field_key,
            dataType=params.data_type,
            position=params.position,
            isRequired=params.is_required,
            placeholder=params.placeholder,
            options=options,
        )

        custom_field = await client.create_location_custom_field(params.location_id, custom_field_data)
        return {"success": True, "customField": custom_field.model_dump()}

    @mcp.tool()
    async def update_location_custom_field(params: UpdateLocationCustomFieldParams) -> Dict[str, Any]:
        """Update a location custom field"""
        client = await get_client(params.access_token)

        # Convert options if provided
        options = None
        if params.options:
            options = [LocationCustomFieldOption(**opt) for opt in params.options]

        custom_field_data = LocationCustomFieldUpdate(
            name=params.name,
            fieldKey=params.field_key,
            dataType=params.data_type,
            position=params.position,
            isRequired=params.is_required,
            placeholder=params.placeholder,
            options=options,
        )

        custom_field = await client.update_location_custom_field(params.location_id, params.custom_field_id, custom_field_data)
        return {"success": True, "customField": custom_field.model_dump()}

    @mcp.tool()
    async def delete_location_custom_field(params: DeleteLocationCustomFieldParams) -> Dict[str, Any]:
        """Delete a location custom field"""
        client = await get_client(params.access_token)

        result = await client.delete_location_custom_field(params.location_id, params.custom_field_id)
        return result

    # Location Templates Tools
    @mcp.tool()
    async def get_location_templates(params: GetLocationTemplatesParams) -> Dict[str, Any]:
        """Get all templates for a location"""
        client = await get_client(params.access_token)

        templates = await client.get_location_templates(params.location_id, params.limit, params.skip)
        return {"success": True, "templates": templates.model_dump()}

    # Location Tasks Tools
    @mcp.tool()
    async def search_location_tasks(params: SearchLocationTasksParams) -> Dict[str, Any]:
        """Search tasks for a location"""
        client = await get_client(params.access_token)

        # Create search filters if any are provided
        filters = None
        if any([params.assigned_to, params.contact_id, params.status, params.due_date, params.date_added]):
            filters = LocationTaskSearchFilters(
                assignedTo=params.assigned_to,
                contactId=params.contact_id,
                status=params.status,
                dueDate=params.due_date,
                dateAdded=params.date_added,
            )

        tasks = await client.search_location_tasks(params.location_id, filters, params.limit, params.skip)
        return {"success": True, "tasks": tasks.model_dump()}
