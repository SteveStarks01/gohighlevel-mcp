"""User management client for GoHighLevel API v2"""

from typing import List, Optional

from .base import BaseGoHighLevelClient
from ..models.user import User, UserCreate, UserUpdate, UserList


class UsersClient(BaseGoHighLevelClient):
    """Client for user-related endpoints"""

    async def get_users(
        self, location_id: Optional[str] = None, limit: int = 100, skip: int = 0
    ) -> UserList:
        """Get all users
        
        Args:
            location_id: Optional location ID to filter users
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            UserList with users
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
        if location_id:
            params["locationId"] = location_id

        response = await self._request(
            "GET", "/users", params=params
        )
        
        data = response.json()
        users_data = data.get("users", [])
        return UserList(
            users=[User(**user) for user in users_data],
            count=len(users_data),
            total=data.get("total", len(users_data)),
        )

    async def get_user(self, user_id: str) -> User:
        """Get a specific user by ID
        
        Args:
            user_id: The user ID
            
        Returns:
            User object
        """
        response = await self._request(
            "GET", f"/users/{user_id}"
        )
        data = response.json()
        return User(**data.get("user", data))

    async def create_user(self, user: UserCreate) -> User:
        """Create a new user
        
        Args:
            user: User creation data
            
        Returns:
            Created User object
        """
        response = await self._request(
            "POST",
            "/users",
            json=user.model_dump(exclude_none=True),
        )
        data = response.json()
        return User(**data.get("user", data))

    async def update_user(
        self, user_id: str, updates: UserUpdate
    ) -> User:
        """Update an existing user
        
        Args:
            user_id: The user ID to update
            updates: User update data
            
        Returns:
            Updated User object
        """
        response = await self._request(
            "PUT",
            f"/users/{user_id}",
            json=updates.model_dump(exclude_none=True),
        )
        data = response.json()
        return User(**data.get("user", data))

    async def delete_user(self, user_id: str) -> bool:
        """Delete a user
        
        Args:
            user_id: The user ID to delete
            
        Returns:
            True if deletion was successful
        """
        response = await self._request(
            "DELETE", f"/users/{user_id}"
        )
        return response.status_code == 200
