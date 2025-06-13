"""Campaign management client for GoHighLevel API v2"""

from typing import List, Optional

from .base import BaseGoHighLevelClient
from ..models.campaign import Campaign, CampaignList


class CampaignsClient(BaseGoHighLevelClient):
    """Client for campaign-related endpoints"""

    async def get_campaigns(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> CampaignList:
        """Get all campaigns for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            CampaignList with campaigns
        """
        params = {"locationId": location_id, "limit": limit}
        if skip > 0:
            params["skip"] = skip

        response = await self._request(
            "GET", "/campaigns", params=params, location_id=location_id
        )
        
        data = response.json()
        campaigns_data = data.get("campaigns", [])
        return CampaignList(
            campaigns=[Campaign(**campaign) for campaign in campaigns_data],
            count=len(campaigns_data),
            total=data.get("total", len(campaigns_data)),
        )
