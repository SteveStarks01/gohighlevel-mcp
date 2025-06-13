"""OAuth management tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.oauth import LocationTokenRequest, SaasSubscriptionUpdate
from ..params.oauth_management import (
    GetInstalledLocationsParams,
    GenerateLocationTokenParams,
    UpdateSaasSubscriptionParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_oauth_management_tools(_mcp, _get_client):
    """Register OAuth management tools with the MCP instance"""
    global mcp, get_client
    mcp = _mcp
    get_client = _get_client

    @mcp.tool()
    async def get_installed_locations(params: GetInstalledLocationsParams) -> Dict[str, Any]:
        """Get all locations where the OAuth application is installed"""
        client = await get_client(params.access_token)

        locations = await client.get_installed_locations(params.limit, params.skip)
        return {"success": True, "locations": locations.model_dump()}

    @mcp.tool()
    async def generate_location_token(params: GenerateLocationTokenParams) -> Dict[str, Any]:
        """Generate an OAuth token for a specific location"""
        client = await get_client(params.access_token)

        request_data = LocationTokenRequest(
            locationId=params.location_id,
            scope=params.scope,
        )

        token = await client.generate_location_token(request_data)
        return {"success": True, "token": token.model_dump()}

    @mcp.tool()
    async def update_saas_subscription(params: UpdateSaasSubscriptionParams) -> Dict[str, Any]:
        """Update the SaaS subscription details for a specific location"""
        client = await get_client(params.access_token)

        subscription_data = SaasSubscriptionUpdate(
            planId=params.plan_id,
            status=params.status,
            billingCycle=params.billing_cycle,
            amount=params.amount,
            currency=params.currency,
            isActive=params.is_active,
        )

        subscription = await client.update_saas_subscription(params.location_id, subscription_data)
        return {"success": True, "subscription": subscription.model_dump()}
