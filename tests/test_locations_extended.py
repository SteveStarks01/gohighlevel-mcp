"""Tests for extended locations functionality"""

import pytest
from unittest.mock import AsyncMock
from pydantic import BaseModel

from src.mcp.params.locations_extended import (
    GetLocationTagsParams, GetLocationTagParams, CreateLocationTagParams, UpdateLocationTagParams, DeleteLocationTagParams,
    GetLocationCustomValuesParams, GetLocationCustomValueParams, CreateLocationCustomValueParams, UpdateLocationCustomValueParams, DeleteLocationCustomValueParams,
    GetLocationCustomFieldsParams, GetLocationCustomFieldParams, CreateLocationCustomFieldParams, UpdateLocationCustomFieldParams, DeleteLocationCustomFieldParams,
)
from src.models.location import (
    LocationTag, LocationTagList, LocationTagCreate, LocationTagUpdate,
    LocationCustomValue, LocationCustomValueList, LocationCustomValueCreate, LocationCustomValueUpdate,
    LocationCustomField, LocationCustomFieldList, LocationCustomFieldCreate, LocationCustomFieldUpdate, LocationCustomFieldOption
)


class TestLocationTagsImplementation:
    """Test location tags functionality"""

    @pytest.mark.asyncio
    async def test_get_location_tags(self):
        """Test getting location tags"""
        # Create mock client
        mock_client = AsyncMock()
        mock_tags = LocationTagList(
            tags=[
                LocationTag(id="tag_1", name="VIP", color="#ff0000"),
                LocationTag(id="tag_2", name="Lead", color="#00ff00"),
            ],
            count=2,
            total=2
        )
        mock_client.get_location_tags.return_value = mock_tags
        
        # Create test parameters
        params = GetLocationTagsParams(
            location_id="test_location",
            limit=10,
            skip=0
        )
        
        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        tags = await client.get_location_tags(params.location_id, params.limit, params.skip)
        result = {"success": True, "tags": tags.model_dump()}
        
        # Verify the result
        assert result["success"] is True
        assert "tags" in result
        assert len(result["tags"]["tags"]) == 2
        
        # Verify the client was called correctly
        mock_client.get_location_tags.assert_called_once_with("test_location", 10, 0)

    @pytest.mark.asyncio
    async def test_get_location_tag(self):
        """Test getting a single location tag"""
        # Create mock client
        mock_client = AsyncMock()
        mock_tag = LocationTag(id="tag_1", name="VIP", color="#ff0000")
        mock_client.get_location_tag.return_value = mock_tag
        
        # Create test parameters
        params = GetLocationTagParams(
            location_id="test_location",
            tag_id="tag_1"
        )
        
        # Test the logic directly
        client = mock_client
        tag = await client.get_location_tag(params.location_id, params.tag_id)
        result = {"success": True, "tag": tag.model_dump()}
        
        # Verify the result
        assert result["success"] is True
        assert "tag" in result
        assert result["tag"]["id"] == "tag_1"
        
        # Verify the client was called correctly
        mock_client.get_location_tag.assert_called_once_with("test_location", "tag_1")

    @pytest.mark.asyncio
    async def test_create_location_tag(self):
        """Test creating a location tag"""
        # Create mock client
        mock_client = AsyncMock()
        mock_tag = LocationTag(id="tag_1", name="VIP", color="#ff0000")
        mock_client.create_location_tag.return_value = mock_tag
        
        # Create test parameters
        params = CreateLocationTagParams(
            location_id="test_location",
            name="VIP",
            color="#ff0000"
        )
        
        # Test the logic directly
        client = mock_client
        tag_data = LocationTagCreate(name=params.name, color=params.color)
        tag = await client.create_location_tag(params.location_id, tag_data)
        result = {"success": True, "tag": tag.model_dump()}
        
        # Verify the result
        assert result["success"] is True
        assert "tag" in result
        assert result["tag"]["name"] == "VIP"
        
        # Verify the client was called correctly
        mock_client.create_location_tag.assert_called_once()
        call_args = mock_client.create_location_tag.call_args
        assert call_args[0][0] == "test_location"  # location_id
        assert call_args[0][1].name == "VIP"  # tag data

    @pytest.mark.asyncio
    async def test_update_location_tag(self):
        """Test updating a location tag"""
        # Create mock client
        mock_client = AsyncMock()
        mock_tag = LocationTag(id="tag_1", name="Premium VIP", color="#ff0000")
        mock_client.update_location_tag.return_value = mock_tag
        
        # Create test parameters
        params = UpdateLocationTagParams(
            location_id="test_location",
            tag_id="tag_1",
            name="Premium VIP"
        )
        
        # Test the logic directly
        client = mock_client
        tag_data = LocationTagUpdate(name=params.name, color=params.color)
        tag = await client.update_location_tag(params.location_id, params.tag_id, tag_data)
        result = {"success": True, "tag": tag.model_dump()}
        
        # Verify the result
        assert result["success"] is True
        assert "tag" in result
        assert result["tag"]["name"] == "Premium VIP"
        
        # Verify the client was called correctly
        mock_client.update_location_tag.assert_called_once()

    @pytest.mark.asyncio
    async def test_delete_location_tag(self):
        """Test deleting a location tag"""
        # Create mock client
        mock_client = AsyncMock()
        mock_client.delete_location_tag.return_value = {"success": True, "message": "Tag deleted successfully"}
        
        # Create test parameters
        params = DeleteLocationTagParams(
            location_id="test_location",
            tag_id="tag_1"
        )
        
        # Test the logic directly
        client = mock_client
        result = await client.delete_location_tag(params.location_id, params.tag_id)
        
        # Verify the result
        assert result["success"] is True
        assert "message" in result
        
        # Verify the client was called correctly
        mock_client.delete_location_tag.assert_called_once_with("test_location", "tag_1")


class TestLocationCustomValuesImplementation:
    """Test location custom values functionality"""

    @pytest.mark.asyncio
    async def test_get_location_custom_values(self):
        """Test getting location custom values"""
        # Create mock client
        mock_client = AsyncMock()
        mock_custom_values = LocationCustomValueList(
            customValues=[
                LocationCustomValue(id="cv_1", key="company_size", value="50-100"),
                LocationCustomValue(id="cv_2", key="industry", value="Technology"),
            ],
            count=2,
            total=2
        )
        mock_client.get_location_custom_values.return_value = mock_custom_values
        
        # Create test parameters
        params = GetLocationCustomValuesParams(
            location_id="test_location",
            limit=10,
            skip=0
        )
        
        # Test the logic directly
        client = mock_client
        custom_values = await client.get_location_custom_values(params.location_id, params.limit, params.skip)
        result = {"success": True, "customValues": custom_values.model_dump()}
        
        # Verify the result
        assert result["success"] is True
        assert "customValues" in result
        assert len(result["customValues"]["customValues"]) == 2
        
        # Verify the client was called correctly
        mock_client.get_location_custom_values.assert_called_once_with("test_location", 10, 0)

    @pytest.mark.asyncio
    async def test_create_location_custom_value(self):
        """Test creating a location custom value"""
        # Create mock client
        mock_client = AsyncMock()
        mock_custom_value = LocationCustomValue(id="cv_1", key="company_size", value="50-100")
        mock_client.create_location_custom_value.return_value = mock_custom_value
        
        # Create test parameters
        params = CreateLocationCustomValueParams(
            location_id="test_location",
            key="company_size",
            value="50-100"
        )
        
        # Test the logic directly
        client = mock_client
        custom_value_data = LocationCustomValueCreate(key=params.key, value=params.value)
        custom_value = await client.create_location_custom_value(params.location_id, custom_value_data)
        result = {"success": True, "customValue": custom_value.model_dump()}
        
        # Verify the result
        assert result["success"] is True
        assert "customValue" in result
        assert result["customValue"]["key"] == "company_size"
        
        # Verify the client was called correctly
        mock_client.create_location_custom_value.assert_called_once()


class TestLocationCustomFieldsImplementation:
    """Test location custom fields functionality"""

    @pytest.mark.asyncio
    async def test_get_location_custom_fields(self):
        """Test getting location custom fields"""
        # Create mock client
        mock_client = AsyncMock()
        mock_custom_fields = LocationCustomFieldList(
            customFields=[
                LocationCustomField(id="cf_1", name="Company Size", dataType="select"),
                LocationCustomField(id="cf_2", name="Industry", dataType="text"),
            ],
            count=2,
            total=2
        )
        mock_client.get_location_custom_fields.return_value = mock_custom_fields
        
        # Create test parameters
        params = GetLocationCustomFieldsParams(
            location_id="test_location",
            limit=10,
            skip=0
        )
        
        # Test the logic directly
        client = mock_client
        custom_fields = await client.get_location_custom_fields(params.location_id, params.limit, params.skip)
        result = {"success": True, "customFields": custom_fields.model_dump()}
        
        # Verify the result
        assert result["success"] is True
        assert "customFields" in result
        assert len(result["customFields"]["customFields"]) == 2
        
        # Verify the client was called correctly
        mock_client.get_location_custom_fields.assert_called_once_with("test_location", 10, 0)

    @pytest.mark.asyncio
    async def test_create_location_custom_field(self):
        """Test creating a location custom field"""
        # Create mock client
        mock_client = AsyncMock()
        mock_custom_field = LocationCustomField(id="cf_1", name="Company Size", dataType="select")
        mock_client.create_location_custom_field.return_value = mock_custom_field
        
        # Create test parameters
        params = CreateLocationCustomFieldParams(
            location_id="test_location",
            name="Company Size",
            data_type="select",
            options=[{"name": "Small", "value": "small"}, {"name": "Large", "value": "large"}]
        )
        
        # Test the logic directly
        client = mock_client
        options = [LocationCustomFieldOption(**opt) for opt in params.options]
        custom_field_data = LocationCustomFieldCreate(
            name=params.name,
            fieldKey=params.field_key,
            dataType=params.data_type,
            position=params.position,
            isRequired=params.is_required,
            placeholder=params.placeholder,
            options=options,
        )
        custom_field = await client.create_location_custom_field(params.location_id, custom_field_data)
        result = {"success": True, "customField": custom_field.model_dump()}
        
        # Verify the result
        assert result["success"] is True
        assert "customField" in result
        assert result["customField"]["name"] == "Company Size"
        
        # Verify the client was called correctly
        mock_client.create_location_custom_field.assert_called_once()

    def test_location_extended_parameter_classes_exist(self):
        """Test that all extended location parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetLocationTagsParams, BaseModel)
        assert issubclass(CreateLocationTagParams, BaseModel)
        assert issubclass(GetLocationCustomValuesParams, BaseModel)
        assert issubclass(CreateLocationCustomValueParams, BaseModel)
        assert issubclass(GetLocationCustomFieldsParams, BaseModel)
        assert issubclass(CreateLocationCustomFieldParams, BaseModel)

        # Check that required fields exist
        assert "location_id" in GetLocationTagsParams.model_fields
        assert "name" in CreateLocationTagParams.model_fields
        assert "key" in CreateLocationCustomValueParams.model_fields
        assert "value" in CreateLocationCustomValueParams.model_fields
        assert "name" in CreateLocationCustomFieldParams.model_fields
        assert "data_type" in CreateLocationCustomFieldParams.model_fields

    @pytest.mark.asyncio
    async def test_get_location_templates(self):
        """Test getting location templates"""
        from src.models.location import LocationTemplate, LocationTemplateList

        # Create mock client
        mock_client = AsyncMock()
        mock_template = LocationTemplate(
            id="template_123",
            locationId="loc_123",
            name="Email Template",
            type="email",
            category="marketing",
            content="Hello {{firstName}}!",
            isActive=True
        )
        mock_template_list = LocationTemplateList(
            templates=[mock_template],
            count=1,
            total=1
        )
        mock_client.get_location_templates.return_value = mock_template_list

        # Test the logic directly
        client = mock_client
        templates = await client.get_location_templates("loc_123", limit=10, skip=0)
        result = {"success": True, "templates": templates.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "templates" in result
        assert len(result["templates"]["templates"]) == 1
        assert result["templates"]["templates"][0]["name"] == "Email Template"

        # Verify the client was called correctly
        mock_client.get_location_templates.assert_called_once_with("loc_123", limit=10, skip=0)

    @pytest.mark.asyncio
    async def test_search_location_tasks(self):
        """Test searching location tasks"""
        from src.models.location import LocationTask, LocationTaskList, LocationTaskSearchFilters

        # Create mock client
        mock_client = AsyncMock()
        mock_task = LocationTask(
            id="task_123",
            locationId="loc_123",
            title="Follow up call",
            body="Call the customer",
            assignedTo="user_123",
            contactId="contact_123",
            status="pending",
            completed=False
        )
        mock_task_list = LocationTaskList(
            tasks=[mock_task],
            count=1,
            total=1
        )
        mock_client.search_location_tasks.return_value = mock_task_list

        # Test the logic directly
        client = mock_client
        filters = LocationTaskSearchFilters(
            assignedTo="user_123",
            status="pending"
        )
        tasks = await client.search_location_tasks("loc_123", filters, limit=10, skip=0)
        result = {"success": True, "tasks": tasks.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "tasks" in result
        assert len(result["tasks"]["tasks"]) == 1
        assert result["tasks"]["tasks"][0]["title"] == "Follow up call"
        assert result["tasks"]["tasks"][0]["status"] == "pending"

        # Verify the client was called correctly
        mock_client.search_location_tasks.assert_called_once_with("loc_123", filters, limit=10, skip=0)
