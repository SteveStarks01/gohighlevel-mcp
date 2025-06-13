"""Contact campaign/workflow assignment tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ..params.contact_assignment import (
    AddContactToCampaignParams,
    RemoveContactFromCampaignParams,
    RemoveContactFromAllCampaignsParams,
    AddContactToWorkflowParams,
    RemoveContactFromWorkflowParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_contact_assignment_tools(mcp_instance, get_client_func):
    """Register all contact assignment tools with the MCP server"""
    global mcp, get_client
    mcp = mcp_instance
    get_client = get_client_func

    @mcp.tool()
    async def add_contact_to_campaign(params: AddContactToCampaignParams) -> Dict[str, Any]:
        """Add a contact to a campaign"""
        client = await get_client(params.access_token)

        success = await client.add_contact_to_campaign(
            params.contact_id, params.campaign_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Contact added to campaign successfully" if success else "Failed to add contact to campaign"
            ),
        }

    @mcp.tool()
    async def remove_contact_from_campaign(params: RemoveContactFromCampaignParams) -> Dict[str, Any]:
        """Remove a contact from a specific campaign"""
        client = await get_client(params.access_token)

        success = await client.remove_contact_from_campaign(
            params.contact_id, params.campaign_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Contact removed from campaign successfully" if success else "Failed to remove contact from campaign"
            ),
        }

    @mcp.tool()
    async def remove_contact_from_all_campaigns(params: RemoveContactFromAllCampaignsParams) -> Dict[str, Any]:
        """Remove a contact from all campaigns"""
        client = await get_client(params.access_token)

        success = await client.remove_contact_from_all_campaigns(
            params.contact_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Contact removed from all campaigns successfully" if success else "Failed to remove contact from all campaigns"
            ),
        }

    @mcp.tool()
    async def add_contact_to_workflow(params: AddContactToWorkflowParams) -> Dict[str, Any]:
        """Add a contact to a workflow"""
        client = await get_client(params.access_token)

        success = await client.add_contact_to_workflow(
            params.contact_id, params.workflow_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Contact added to workflow successfully" if success else "Failed to add contact to workflow"
            ),
        }

    @mcp.tool()
    async def remove_contact_from_workflow(params: RemoveContactFromWorkflowParams) -> Dict[str, Any]:
        """Remove a contact from a workflow"""
        client = await get_client(params.access_token)

        success = await client.remove_contact_from_workflow(
            params.contact_id, params.workflow_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Contact removed from workflow successfully" if success else "Failed to remove contact from workflow"
            ),
        }

    @mcp.tool()
    async def remove_contact_from_all_campaigns(params: RemoveContactFromAllCampaignsParams) -> Dict[str, Any]:
        """Remove a contact from all campaigns"""
        client = await get_client(params.access_token)

        success = await client.remove_contact_from_all_campaigns(
            params.contact_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Contact removed from all campaigns successfully" if success else "Failed to remove contact from all campaigns"
            ),
        }
