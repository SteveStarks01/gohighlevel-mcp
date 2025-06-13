"""Links management client for GoHighLevel API v2"""

from typing import Optional
from .base import BaseGoHighLevelClient
from ..models.link import Link, LinkCreate, LinkUpdate, LinkList


class LinksClient(BaseGoHighLevelClient):
    """Client for links-related endpoints"""

    async def get_links(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> LinkList:
        """Get all links for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            LinkList containing links and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", "/links/", params=params, location_id=location_id
        )
        data = response.json()
        
        links_data = data.get("links", [])
        return LinkList(
            links=[Link(**link) for link in links_data],
            count=len(links_data),
            total=data.get("total", len(links_data)),
        )

    async def get_link(self, link_id: str, location_id: str) -> Link:
        """Get a specific link by ID
        
        Args:
            link_id: The link ID
            location_id: The location ID
            
        Returns:
            Link object
        """
        response = await self._request(
            "GET", f"/links/{link_id}", location_id=location_id
        )
        data = response.json()
        return Link(**data.get("link", data))

    async def create_link(self, link: LinkCreate, location_id: str) -> Link:
        """Create a new link
        
        Args:
            link: Link creation data
            location_id: The location ID
            
        Returns:
            Created Link object
        """
        response = await self._request(
            "POST", "/links/", json=link.model_dump(exclude_none=True), location_id=location_id
        )
        data = response.json()
        return Link(**data.get("link", data))

    async def update_link(self, link_id: str, link: LinkUpdate, location_id: str) -> Link:
        """Update an existing link
        
        Args:
            link_id: The link ID
            link: Link update data
            location_id: The location ID
            
        Returns:
            Updated Link object
        """
        response = await self._request(
            "PUT", f"/links/{link_id}", json=link.model_dump(exclude_none=True), location_id=location_id
        )
        data = response.json()
        return Link(**data.get("link", data))

    async def delete_link(self, link_id: str, location_id: str) -> dict:
        """Delete a link
        
        Args:
            link_id: The link ID
            location_id: The location ID
            
        Returns:
            Success response
        """
        response = await self._request(
            "DELETE", f"/links/{link_id}", location_id=location_id
        )
        
        if response.status_code == 204:
            return {"success": True, "message": "Link deleted successfully"}
        
        data = response.json()
        return {"success": True, "message": data.get("message", "Link deleted successfully")}
