"""Location management client for GoHighLevel API v2"""

from typing import List, Optional

from .base import BaseGoHighLevelClient
from ..models.location import Location, LocationCreate, LocationUpdate, LocationList


class LocationsClient(BaseGoHighLevelClient):
    """Client for location-related endpoints"""

    async def get_location(self, location_id: str) -> Location:
        """Get a specific location by ID
        
        Args:
            location_id: The location ID
            
        Returns:
            Location object
        """
        response = await self._request(
            "GET", f"/locations/{location_id}"
        )
        data = response.json()
        return Location(**data.get("location", data))

    async def search_locations(
        self, 
        company_id: Optional[str] = None,
        limit: int = 100, 
        skip: int = 0,
        search_query: Optional[str] = None
    ) -> LocationList:
        """Search locations with filters
        
        Args:
            company_id: Optional company ID to filter locations
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            search_query: Optional search query for location names
            
        Returns:
            LocationList with locations
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
        if company_id:
            params["companyId"] = company_id
        if search_query:
            params["query"] = search_query

        response = await self._request(
            "GET", "/locations/search", params=params
        )
        
        data = response.json()
        locations_data = data.get("locations", [])
        return LocationList(
            locations=[Location(**location) for location in locations_data],
            count=len(locations_data),
            total=data.get("total", len(locations_data)),
        )

    async def create_location(self, location: LocationCreate) -> Location:
        """Create a new location
        
        Args:
            location: Location creation data
            
        Returns:
            Created Location object
        """
        response = await self._request(
            "POST",
            "/locations",
            json=location.model_dump(exclude_none=True),
        )
        data = response.json()
        return Location(**data.get("location", data))

    async def update_location(
        self, location_id: str, updates: LocationUpdate
    ) -> Location:
        """Update an existing location
        
        Args:
            location_id: The location ID to update
            updates: Location update data
            
        Returns:
            Updated Location object
        """
        response = await self._request(
            "PUT",
            f"/locations/{location_id}",
            json=updates.model_dump(exclude_none=True),
        )
        data = response.json()
        return Location(**data.get("location", data))

    async def delete_location(self, location_id: str) -> bool:
        """Delete a location
        
        Args:
            location_id: The location ID to delete
            
        Returns:
            True if deletion was successful
        """
        response = await self._request(
            "DELETE", f"/locations/{location_id}"
        )
        return response.status_code == 200
