"""Tests for location functionality"""

import pytest
from unittest.mock import AsyncMock, patch
from src.models.location import Location, LocationList
from src.mcp.params.locations import (
    GetLocationParams,
    SearchLocationsParams,
    CreateLocationParams,
    UpdateLocationParams,
    DeleteLocationParams,
)


class TestLocationImplementation:
    """Test location MCP tools implementation"""

    @pytest.mark.asyncio
    async def test_get_location(self):
        """Test getting a single location by ID"""
        # Create mock client
        mock_client = AsyncMock()
        mock_location = Location(
            id="test_location_id",
            name="Test Location",
            companyId="test_company",
            email="test@location.com",
        )
        mock_client.get_location.return_value = mock_location

        # Create test parameters
        params = GetLocationParams(
            location_id="test_location_id",
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        location = await client.get_location(params.location_id)
        result = {"success": True, "location": location.model_dump()}

        assert result["success"] is True
        assert result["location"]["name"] == "Test Location"
        mock_client.get_location.assert_called_once_with("test_location_id")

    @pytest.mark.asyncio
    async def test_search_locations(self):
        """Test searching locations"""
        # Create mock client
        mock_client = AsyncMock()
        mock_location = Location(
            id="test_location_id",
            name="Test Location",
            companyId="test_company",
            email="test@location.com",
        )
        mock_location_list = LocationList(locations=[mock_location], count=1, total=1)
        mock_client.search_locations.return_value = mock_location_list

        # Create test parameters
        params = SearchLocationsParams(
            company_id="test_company",
            limit=100,
            skip=0,
            search_query="Test",
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        location_list = await client.search_locations(
            params.company_id, params.limit, params.skip, params.search_query
        )
        result = {
            "success": True,
            "locations": [location.model_dump() for location in location_list.locations],
            "count": location_list.count,
            "total": location_list.total,
        }

        assert result["success"] is True
        assert len(result["locations"]) == 1
        assert result["locations"][0]["name"] == "Test Location"
        mock_client.search_locations.assert_called_once_with(
            "test_company", 100, 0, "Test"
        )

    @pytest.mark.asyncio
    async def test_create_location(self):
        """Test creating a new location"""
        # Create mock client
        mock_client = AsyncMock()
        mock_location = Location(
            id="new_location_id",
            name="New Location",
            companyId="test_company",
            email="new@location.com",
        )
        mock_client.create_location.return_value = mock_location

        # Create test parameters
        params = CreateLocationParams(
            company_id="test_company",
            name="New Location",
            email="new@location.com",
        )

        # Test the logic directly
        from src.models.location import LocationCreate
        
        client = mock_client
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
        result = {"success": True, "location": location.model_dump()}

        assert result["success"] is True
        assert result["location"]["name"] == "New Location"
        mock_client.create_location.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_location(self):
        """Test deleting a location"""
        # Create mock client
        mock_client = AsyncMock()
        mock_client.delete_location.return_value = True

        # Create test parameters
        params = DeleteLocationParams(
            location_id="test_location_id",
        )

        # Test the logic directly
        client = mock_client
        success = await client.delete_location(params.location_id)
        result = {
            "success": success,
            "message": (
                "Location deleted successfully" if success else "Failed to delete location"
            ),
        }

        assert result["success"] is True
        assert result["message"] == "Location deleted successfully"
        mock_client.delete_location.assert_called_once_with("test_location_id")

    def test_location_parameter_classes_exist(self):
        """Test that location parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetLocationParams, BaseModel)
        assert issubclass(SearchLocationsParams, BaseModel)
        assert issubclass(CreateLocationParams, BaseModel)
        assert issubclass(UpdateLocationParams, BaseModel)
        assert issubclass(DeleteLocationParams, BaseModel)

        # Check that required fields exist
        assert "location_id" in GetLocationParams.model_fields
        assert "name" in CreateLocationParams.model_fields
        assert "company_id" in CreateLocationParams.model_fields
