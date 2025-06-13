"""Tests for business functionality"""

import pytest
from unittest.mock import AsyncMock, patch
from src.models.business import Business, BusinessList
from src.mcp.params.businesses import (
    GetBusinessesParams,
    GetBusinessParams,
    CreateBusinessParams,
    UpdateBusinessParams,
    DeleteBusinessParams,
)


class TestBusinessImplementation:
    """Test business MCP tools implementation"""

    @pytest.mark.asyncio
    async def test_get_businesses(self):
        """Test getting all businesses for a location"""
        # Create mock client
        mock_client = AsyncMock()
        mock_business = Business(
            id="test_business_id",
            name="Test Business",
            locationId="test_location",
            email="test@business.com",
        )
        mock_business_list = BusinessList(businesses=[mock_business], count=1, total=1)
        mock_client.get_businesses.return_value = mock_business_list

        # Create test parameters
        params = GetBusinessesParams(
            location_id="test_location",
            limit=100,
            skip=0,
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        business_list = await client.get_businesses(
            params.location_id, params.limit, params.skip
        )
        result = {
            "success": True,
            "businesses": [business.model_dump() for business in business_list.businesses],
            "count": business_list.count,
            "total": business_list.total,
        }

        assert result["success"] is True
        assert len(result["businesses"]) == 1
        assert result["businesses"][0]["name"] == "Test Business"
        mock_client.get_businesses.assert_called_once_with(
            "test_location", 100, 0
        )

    @pytest.mark.asyncio
    async def test_create_business(self):
        """Test creating a new business"""
        # Create mock client
        mock_client = AsyncMock()
        mock_business = Business(
            id="new_business_id",
            name="New Business",
            locationId="test_location",
            email="new@business.com",
        )
        mock_client.create_business.return_value = mock_business

        # Create test parameters
        params = CreateBusinessParams(
            location_id="test_location",
            name="New Business",
            email="new@business.com",
        )

        # Test the logic directly
        from src.models.business import BusinessCreate

        client = mock_client
        business_data = BusinessCreate(
            locationId=params.location_id,
            name=params.name,
            description=params.description,
            website=params.website,
            phone=params.phone,
            email=params.email,
            address=None,  # No address fields provided
            logoUrl=params.logo_url,
            industry=params.industry,
            employeeCount=params.employee_count,
            annualRevenue=params.annual_revenue,
            customFields=None,
            tags=params.tags,
        )
        business = await client.create_business(business_data)
        result = {"success": True, "business": business.model_dump()}

        assert result["success"] is True
        assert result["business"]["name"] == "New Business"
        mock_client.create_business.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_business(self):
        """Test deleting a business"""
        # Create mock client
        mock_client = AsyncMock()
        mock_client.delete_business.return_value = True

        # Create test parameters
        params = DeleteBusinessParams(
            business_id="test_business_id",
            location_id="test_location",
        )

        # Test the logic directly
        client = mock_client
        success = await client.delete_business(
            params.business_id, params.location_id
        )
        result = {
            "success": success,
            "message": (
                "Business deleted successfully" if success else "Failed to delete business"
            ),
        }

        assert result["success"] is True
        assert result["message"] == "Business deleted successfully"
        mock_client.delete_business.assert_called_once_with(
            "test_business_id", "test_location"
        )

    def test_business_parameter_classes_exist(self):
        """Test that business parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetBusinessesParams, BaseModel)
        assert issubclass(GetBusinessParams, BaseModel)
        assert issubclass(CreateBusinessParams, BaseModel)
        assert issubclass(UpdateBusinessParams, BaseModel)
        assert issubclass(DeleteBusinessParams, BaseModel)

        # Check that required fields exist
        assert "location_id" in GetBusinessesParams.model_fields
        assert "business_id" in GetBusinessParams.model_fields
        assert "name" in CreateBusinessParams.model_fields
        assert "location_id" in CreateBusinessParams.model_fields
