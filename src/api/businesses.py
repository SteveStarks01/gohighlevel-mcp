"""Business management client for GoHighLevel API v2"""

from typing import List, Optional

from .base import BaseGoHighLevelClient
from ..models.business import Business, BusinessCreate, BusinessUpdate, BusinessList


class BusinessesClient(BaseGoHighLevelClient):
    """Client for business-related endpoints"""

    async def get_businesses(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> BusinessList:
        """Get all businesses for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            BusinessList with businesses
        """
        params = {"locationId": location_id, "limit": limit}
        if skip > 0:
            params["skip"] = skip

        response = await self._request(
            "GET", "/businesses", params=params, location_id=location_id
        )
        
        data = response.json()
        businesses_data = data.get("businesses", [])
        return BusinessList(
            businesses=[Business(**business) for business in businesses_data],
            count=len(businesses_data),
            total=data.get("total", len(businesses_data)),
        )

    async def get_business(self, business_id: str, location_id: str) -> Business:
        """Get a specific business by ID
        
        Args:
            business_id: The business ID
            location_id: The location ID
            
        Returns:
            Business object
        """
        response = await self._request(
            "GET", f"/businesses/{business_id}", location_id=location_id
        )
        data = response.json()
        return Business(**data.get("business", data))

    async def create_business(self, business: BusinessCreate) -> Business:
        """Create a new business
        
        Args:
            business: Business creation data
            
        Returns:
            Created Business object
        """
        response = await self._request(
            "POST",
            "/businesses",
            json=business.model_dump(exclude_none=True),
            location_id=business.locationId,
        )
        data = response.json()
        return Business(**data.get("business", data))

    async def update_business(
        self, business_id: str, updates: BusinessUpdate, location_id: str
    ) -> Business:
        """Update an existing business
        
        Args:
            business_id: The business ID to update
            updates: Business update data
            location_id: The location ID
            
        Returns:
            Updated Business object
        """
        response = await self._request(
            "PUT",
            f"/businesses/{business_id}",
            json=updates.model_dump(exclude_none=True),
            location_id=location_id,
        )
        data = response.json()
        return Business(**data.get("business", data))

    async def delete_business(self, business_id: str, location_id: str) -> bool:
        """Delete a business
        
        Args:
            business_id: The business ID to delete
            location_id: The location ID
            
        Returns:
            True if deletion was successful
        """
        response = await self._request(
            "DELETE", f"/businesses/{business_id}", location_id=location_id
        )
        return response.status_code == 200
