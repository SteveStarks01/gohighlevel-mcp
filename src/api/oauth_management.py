"""OAuth management client for GoHighLevel API v2"""

from typing import Optional
from .base import BaseGoHighLevelClient
from ..models.oauth import (
    InstalledLocation, InstalledLocationList, 
    LocationToken, LocationTokenRequest,
    SaasSubscription, SaasSubscriptionUpdate
)


class OAuthManagementClient(BaseGoHighLevelClient):
    """Client for OAuth management endpoints"""

    async def get_installed_locations(
        self, limit: int = 100, skip: int = 0
    ) -> InstalledLocationList:
        """Get all locations where the OAuth application is installed
        
        Args:
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            InstalledLocationList containing locations and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", "/oauth/installedLocations", params=params
        )
        data = response.json()
        
        locations_data = data.get("locations", [])
        return InstalledLocationList(
            locations=[InstalledLocation(**location) for location in locations_data],
            count=len(locations_data),
            total=data.get("total", len(locations_data)),
        )

    async def generate_location_token(self, request: LocationTokenRequest) -> LocationToken:
        """Generate an OAuth token for a specific location
        
        Args:
            request: Location token request data
            
        Returns:
            LocationToken object
        """
        response = await self._request(
            "POST", "/oauth/locationToken", json=request.model_dump(exclude_none=True)
        )
        data = response.json()
        return LocationToken(**data.get("token", data))

    async def update_saas_subscription(
        self, location_id: str, subscription: SaasSubscriptionUpdate
    ) -> SaasSubscription:
        """Update the SaaS subscription details for a specific location
        
        Args:
            location_id: The location ID
            subscription: Subscription update data
            
        Returns:
            Updated SaasSubscription object
        """
        response = await self._request(
            "PUT", 
            f"/update-saas-subscription/{location_id}", 
            json=subscription.model_dump(exclude_none=True)
        )
        data = response.json()
        return SaasSubscription(**data.get("subscription", data))
