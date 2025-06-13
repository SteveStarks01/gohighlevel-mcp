"""Business tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.business import BusinessCreate, BusinessUpdate, BusinessAddress
from ..params.businesses import (
    GetBusinessesParams,
    GetBusinessParams,
    CreateBusinessParams,
    UpdateBusinessParams,
    DeleteBusinessParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_business_tools(mcp_instance, get_client_func):
    """Register all business tools with the MCP server"""
    global mcp, get_client
    mcp = mcp_instance
    get_client = get_client_func

    @mcp.tool()
    async def get_businesses(params: GetBusinessesParams) -> Dict[str, Any]:
        """Get all businesses for a location"""
        client = await get_client(params.access_token)

        business_list = await client.get_businesses(
            params.location_id, params.limit, params.skip
        )
        return {
            "success": True,
            "businesses": [business.model_dump() for business in business_list.businesses],
            "count": business_list.count,
            "total": business_list.total,
        }

    @mcp.tool()
    async def get_business(params: GetBusinessParams) -> Dict[str, Any]:
        """Get a single business by ID"""
        client = await get_client(params.access_token)

        business = await client.get_business(params.business_id, params.location_id)
        return {"success": True, "business": business.model_dump()}

    @mcp.tool()
    async def create_business(params: CreateBusinessParams) -> Dict[str, Any]:
        """Create a new business in GoHighLevel"""
        client = await get_client(params.access_token)

        # Build address if any address fields are provided
        address = None
        if any([
            params.address1, params.address2, params.city, 
            params.state, params.country, params.postal_code
        ]):
            address = BusinessAddress(
                address1=params.address1,
                address2=params.address2,
                city=params.city,
                state=params.state,
                country=params.country,
                postalCode=params.postal_code,
            )

        business_data = BusinessCreate(
            locationId=params.location_id,
            name=params.name,
            description=params.description,
            website=params.website,
            phone=params.phone,
            email=params.email,
            address=address,
            logoUrl=params.logo_url,
            industry=params.industry,
            employeeCount=params.employee_count,
            annualRevenue=params.annual_revenue,
            customFields=[
                {"key": k, "value": v} for k, v in (params.custom_fields or {}).items()
            ] if params.custom_fields else None,
            tags=params.tags,
        )

        business = await client.create_business(business_data)
        return {"success": True, "business": business.model_dump()}

    @mcp.tool()
    async def update_business(params: UpdateBusinessParams) -> Dict[str, Any]:
        """Update an existing business in GoHighLevel"""
        client = await get_client(params.access_token)

        # Build address if any address fields are provided
        address = None
        if any([
            params.address1, params.address2, params.city, 
            params.state, params.country, params.postal_code
        ]):
            address = BusinessAddress(
                address1=params.address1,
                address2=params.address2,
                city=params.city,
                state=params.state,
                country=params.country,
                postalCode=params.postal_code,
            )

        update_data = BusinessUpdate(
            name=params.name,
            description=params.description,
            website=params.website,
            phone=params.phone,
            email=params.email,
            address=address,
            logoUrl=params.logo_url,
            industry=params.industry,
            employeeCount=params.employee_count,
            annualRevenue=params.annual_revenue,
            customFields=[
                {"key": k, "value": v} for k, v in (params.custom_fields or {}).items()
            ] if params.custom_fields else None,
            tags=params.tags,
        )

        business = await client.update_business(
            params.business_id, update_data, params.location_id
        )
        return {"success": True, "business": business.model_dump()}

    @mcp.tool()
    async def delete_business(params: DeleteBusinessParams) -> Dict[str, Any]:
        """Delete a business from GoHighLevel"""
        client = await get_client(params.access_token)

        success = await client.delete_business(params.business_id, params.location_id)
        return {
            "success": success,
            "message": (
                "Business deleted successfully"
                if success
                else "Failed to delete business"
            ),
        }
