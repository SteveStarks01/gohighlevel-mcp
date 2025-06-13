"""Links tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.link import LinkCreate, LinkUpdate
from ..params.links import (
    GetLinksParams,
    GetLinkParams,
    CreateLinkParams,
    UpdateLinkParams,
    DeleteLinkParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_links_tools(_mcp, _get_client):
    """Register links tools with the MCP instance"""
    global mcp, get_client
    mcp = _mcp
    get_client = _get_client

    @mcp.tool()
    async def get_links(params: GetLinksParams) -> Dict[str, Any]:
        """Get all links for a location"""
        client = await get_client(params.access_token)

        links = await client.get_links(params.location_id, params.limit, params.skip)
        return {"success": True, "links": links.model_dump()}

    @mcp.tool()
    async def get_link(params: GetLinkParams) -> Dict[str, Any]:
        """Get a specific link"""
        client = await get_client(params.access_token)

        link = await client.get_link(params.link_id, params.location_id)
        return {"success": True, "link": link.model_dump()}

    @mcp.tool()
    async def create_link(params: CreateLinkParams) -> Dict[str, Any]:
        """Create a new link"""
        client = await get_client(params.access_token)

        link_data = LinkCreate(
            name=params.name,
            url=params.url,
            description=params.description,
            isActive=params.is_active,
        )

        link = await client.create_link(link_data, params.location_id)
        return {"success": True, "link": link.model_dump()}

    @mcp.tool()
    async def update_link(params: UpdateLinkParams) -> Dict[str, Any]:
        """Update an existing link"""
        client = await get_client(params.access_token)

        update_data = LinkUpdate(
            name=params.name,
            url=params.url,
            description=params.description,
            isActive=params.is_active,
        )

        link = await client.update_link(params.link_id, update_data, params.location_id)
        return {"success": True, "link": link.model_dump()}

    @mcp.tool()
    async def delete_link(params: DeleteLinkParams) -> Dict[str, Any]:
        """Delete a link"""
        client = await get_client(params.access_token)

        result = await client.delete_link(params.link_id, params.location_id)
        return result
