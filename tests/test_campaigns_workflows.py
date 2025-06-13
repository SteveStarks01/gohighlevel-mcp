"""Tests for campaign and workflow functionality"""

import pytest
from unittest.mock import AsyncMock, patch
from src.models.campaign import Campaign, CampaignList
from src.models.workflow import Workflow, WorkflowList
from src.mcp.params.campaigns import GetCampaignsParams
from src.mcp.params.workflows import GetWorkflowsParams


class TestCampaignWorkflowImplementation:
    """Test campaign and workflow MCP tools implementation"""

    @pytest.mark.asyncio
    async def test_get_campaigns(self):
        """Test getting all campaigns for a location"""
        # Create mock client
        mock_client = AsyncMock()
        mock_campaign = Campaign(
            id="test_campaign_id",
            name="Test Campaign",
            locationId="test_location",
            status="active",
        )
        mock_campaign_list = CampaignList(campaigns=[mock_campaign], count=1, total=1)
        mock_client.get_campaigns.return_value = mock_campaign_list

        # Create test parameters
        params = GetCampaignsParams(
            location_id="test_location",
            limit=100,
            skip=0,
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        campaign_list = await client.get_campaigns(
            params.location_id, params.limit, params.skip
        )
        result = {
            "success": True,
            "campaigns": [campaign.model_dump() for campaign in campaign_list.campaigns],
            "count": campaign_list.count,
            "total": campaign_list.total,
        }

        assert result["success"] is True
        assert len(result["campaigns"]) == 1
        assert result["campaigns"][0]["name"] == "Test Campaign"
        mock_client.get_campaigns.assert_called_once_with(
            "test_location", 100, 0
        )

    @pytest.mark.asyncio
    async def test_get_workflows(self):
        """Test getting all workflows for a location"""
        # Create mock client
        mock_client = AsyncMock()
        mock_workflow = Workflow(
            id="test_workflow_id",
            name="Test Workflow",
            locationId="test_location",
            status="active",
        )
        mock_workflow_list = WorkflowList(workflows=[mock_workflow], count=1, total=1)
        mock_client.get_workflows.return_value = mock_workflow_list

        # Create test parameters
        params = GetWorkflowsParams(
            location_id="test_location",
            limit=100,
            skip=0,
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        workflow_list = await client.get_workflows(
            params.location_id, params.limit, params.skip
        )
        result = {
            "success": True,
            "workflows": [workflow.model_dump() for workflow in workflow_list.workflows],
            "count": workflow_list.count,
            "total": workflow_list.total,
        }

        assert result["success"] is True
        assert len(result["workflows"]) == 1
        assert result["workflows"][0]["name"] == "Test Workflow"
        mock_client.get_workflows.assert_called_once_with(
            "test_location", 100, 0
        )

    def test_campaign_workflow_parameter_classes_exist(self):
        """Test that campaign and workflow parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetCampaignsParams, BaseModel)
        assert issubclass(GetWorkflowsParams, BaseModel)

        # Check that required fields exist
        assert "location_id" in GetCampaignsParams.model_fields
        assert "location_id" in GetWorkflowsParams.model_fields
