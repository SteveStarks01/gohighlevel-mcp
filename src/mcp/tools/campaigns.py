"""Campaign tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ..params.campaigns import GetCampaignsParams


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_campaign_tools(mcp_instance, get_client_func):
    """Register all campaign tools with the MCP server"""
    global mcp, get_client
    mcp = mcp_instance
    get_client = get_client_func

    @mcp.tool()
    async def get_campaigns(params: GetCampaignsParams) -> Dict[str, Any]:
        """Get all campaigns for a location"""
        client = await get_client(params.access_token)

        campaign_list = await client.get_campaigns(
            params.location_id, params.limit, params.skip
        )
        return {
            "success": True,
            "campaigns": [campaign.model_dump() for campaign in campaign_list.campaigns],
            "count": campaign_list.count,
            "total": campaign_list.total,
        }
