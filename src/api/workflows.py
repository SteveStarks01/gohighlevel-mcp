"""Workflow management client for GoHighLevel API v2"""

from typing import List, Optional

from .base import BaseGoHighLevelClient
from ..models.workflow import Workflow, WorkflowList


class WorkflowsClient(BaseGoHighLevelClient):
    """Client for workflow-related endpoints"""

    async def get_workflows(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> WorkflowList:
        """Get all workflows for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            WorkflowList with workflows
        """
        params = {"locationId": location_id, "limit": limit}
        if skip > 0:
            params["skip"] = skip

        response = await self._request(
            "GET", "/workflows", params=params, location_id=location_id
        )
        
        data = response.json()
        workflows_data = data.get("workflows", [])
        return WorkflowList(
            workflows=[Workflow(**workflow) for workflow in workflows_data],
            count=len(workflows_data),
            total=data.get("total", len(workflows_data)),
        )
