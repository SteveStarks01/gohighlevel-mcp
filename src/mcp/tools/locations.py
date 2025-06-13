"""Location tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.location import LocationCreate, LocationUpdate, LocationAddress, LocationSettings
from ..params.locations import (
    GetLocationParams,
    SearchLocationsParams,
    CreateLocationParams,
    UpdateLocationParams,
    DeleteLocationParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_location_tools(mcp_instance, get_client_func):
    """Register all location tools with the MCP server"""
    global mcp, get_client
    mcp = mcp_instance
    get_client = get_client_func

    @mcp.tool()
    async def get_location(params: GetLocationParams) -> Dict[str, Any]:
        """Get a single location by ID"""
        client = await get_client(params.access_token)

        location = await client.get_location(params.location_id)
        return {"success": True, "location": location.model_dump()}

    @mcp.tool()
    async def search_locations(params: SearchLocationsParams) -> Dict[str, Any]:
        """Search locations with filters"""
        client = await get_client(params.access_token)

        location_list = await client.search_locations(
            params.company_id, params.limit, params.skip, params.search_query
        )
        return {
            "success": True,
            "locations": [location.model_dump() for location in location_list.locations],
            "count": location_list.count,
            "total": location_list.total,
        }

    @mcp.tool()
    async def create_location(params: CreateLocationParams) -> Dict[str, Any]:
        """Create a new location in GoHighLevel"""
        client = await get_client(params.access_token)

        # Build address if any address fields are provided
        address = None
        if any([params.address, params.city, params.state, params.country, params.postal_code]):
            address = LocationAddress(
                address=params.address,
                city=params.city,
                state=params.state,
                country=params.country,
                postalCode=params.postal_code,
            )

        # Build settings if any setting fields are provided
        settings = None
        if any([
            params.allow_duplicate_contact, params.allow_duplicate_opportunity,
            params.allow_facebook_name_merge, params.disable_contact_timezone
        ]):
            settings = LocationSettings(
                allowDuplicateContact=params.allow_duplicate_contact,
                allowDuplicateOpportunity=params.allow_duplicate_opportunity,
                allowFacebookNameMerge=params.allow_facebook_name_merge,
                disableContactTimezone=params.disable_contact_timezone,
            )

        location_data = LocationCreate(
            companyId=params.company_id,
            name=params.name,
            address=params.address,
            city=params.city,
            state=params.state,
            country=params.country,
            postal_code=params.postal_code,
            logo_url=params.logo_url,
            website=params.website,
            timezone=params.timezone,
            email=params.email,
            phone=params.phone,
            business_type=params.business_type,
            allow_duplicate_contact=params.allow_duplicate_contact,
            allow_duplicate_opportunity=params.allow_duplicate_opportunity,
            allow_facebook_name_merge=params.allow_facebook_name_merge,
            disable_contact_timezone=params.disable_contact_timezone,
            stripe_product_id=params.stripe_product_id,
        )

        location = await client.create_location(location_data)
        return {"success": True, "location": location.model_dump()}

    @mcp.tool()
    async def update_location(params: UpdateLocationParams) -> Dict[str, Any]:
        """Update an existing location in GoHighLevel"""
        client = await get_client(params.access_token)

        update_data = LocationUpdate(
            name=params.name,
            address=params.address,
            city=params.city,
            state=params.state,
            country=params.country,
            postal_code=params.postal_code,
            logo_url=params.logo_url,
            website=params.website,
            timezone=params.timezone,
            email=params.email,
            phone=params.phone,
            business_type=params.business_type,
            allow_duplicate_contact=params.allow_duplicate_contact,
            allow_duplicate_opportunity=params.allow_duplicate_opportunity,
            allow_facebook_name_merge=params.allow_facebook_name_merge,
            disable_contact_timezone=params.disable_contact_timezone,
            stripe_product_id=params.stripe_product_id,
        )

        location = await client.update_location(params.location_id, update_data)
        return {"success": True, "location": location.model_dump()}

    @mcp.tool()
    async def delete_location(params: DeleteLocationParams) -> Dict[str, Any]:
        """Delete a location from GoHighLevel"""
        client = await get_client(params.access_token)

        success = await client.delete_location(params.location_id)
        return {
            "success": success,
            "message": (
                "Location deleted successfully"
                if success
                else "Failed to delete location"
            ),
        }
