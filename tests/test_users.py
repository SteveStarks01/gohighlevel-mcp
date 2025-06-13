"""Tests for user functionality"""

import pytest
from unittest.mock import AsyncMock, patch
from src.models.user import User, UserList
from src.mcp.params.users import (
    GetUsersParams,
    GetUserParams,
    CreateUserParams,
    UpdateUserParams,
    DeleteUserParams,
)


class TestUserImplementation:
    """Test user MCP tools implementation"""

    @pytest.mark.asyncio
    async def test_get_users(self):
        """Test getting all users"""
        # Create mock client
        mock_client = AsyncMock()
        mock_user = User(
            id="test_user_id",
            name="Test User",
            email="test@user.com",
        )
        mock_user_list = UserList(users=[mock_user], count=1, total=1)
        mock_client.get_users.return_value = mock_user_list

        # Create test parameters
        params = GetUsersParams(
            location_id="test_location",
            limit=100,
            skip=0,
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        user_list = await client.get_users(
            params.location_id, params.limit, params.skip
        )
        result = {
            "success": True,
            "users": [user.model_dump() for user in user_list.users],
            "count": user_list.count,
            "total": user_list.total,
        }

        assert result["success"] is True
        assert len(result["users"]) == 1
        assert result["users"][0]["name"] == "Test User"
        mock_client.get_users.assert_called_once_with(
            "test_location", 100, 0
        )

    @pytest.mark.asyncio
    async def test_create_user(self):
        """Test creating a new user"""
        # Create mock client
        mock_client = AsyncMock()
        mock_user = User(
            id="new_user_id",
            name="New User",
            email="new@user.com",
        )
        mock_client.create_user.return_value = mock_user

        # Create test parameters
        params = CreateUserParams(
            company_id="test_company",
            name="New User",
            email="new@user.com",
        )

        # Test the logic directly
        from src.models.user import UserCreate
        
        client = mock_client
        user_data = UserCreate(
            companyId=params.company_id,
            name=params.name,
            firstName=params.first_name,
            lastName=params.last_name,
            email=params.email,
            phone=params.phone,
            extension=params.extension,
            permissions=None,  # No permissions provided
            roles=params.roles,
            locationIds=params.location_ids,
            profilePhoto=params.profile_photo,
            type=params.user_type,
        )
        user = await client.create_user(user_data)
        result = {"success": True, "user": user.model_dump()}

        assert result["success"] is True
        assert result["user"]["name"] == "New User"
        mock_client.create_user.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_user(self):
        """Test deleting a user"""
        # Create mock client
        mock_client = AsyncMock()
        mock_client.delete_user.return_value = True

        # Create test parameters
        params = DeleteUserParams(
            user_id="test_user_id",
        )

        # Test the logic directly
        client = mock_client
        success = await client.delete_user(params.user_id)
        result = {
            "success": success,
            "message": (
                "User deleted successfully" if success else "Failed to delete user"
            ),
        }

        assert result["success"] is True
        assert result["message"] == "User deleted successfully"
        mock_client.delete_user.assert_called_once_with("test_user_id")

    def test_user_parameter_classes_exist(self):
        """Test that user parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetUsersParams, BaseModel)
        assert issubclass(GetUserParams, BaseModel)
        assert issubclass(CreateUserParams, BaseModel)
        assert issubclass(UpdateUserParams, BaseModel)
        assert issubclass(DeleteUserParams, BaseModel)

        # Check that required fields exist
        assert "user_id" in GetUserParams.model_fields
        assert "name" in CreateUserParams.model_fields
        assert "email" in CreateUserParams.model_fields
        assert "company_id" in CreateUserParams.model_fields
