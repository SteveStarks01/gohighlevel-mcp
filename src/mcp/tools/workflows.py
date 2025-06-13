"""Workflow tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ..params.workflows import GetWorkflowsParams


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_workflow_tools(mcp_instance, get_client_func):
    """Register all workflow tools with the MCP server"""
    global mcp, get_client
    mcp = mcp_instance
    get_client = get_client_func

    @mcp.tool()
    async def get_workflows(params: GetWorkflowsParams) -> Dict[str, Any]:
        """Get all workflows for a location"""
        client = await get_client(params.access_token)

        workflow_list = await client.get_workflows(
            params.location_id, params.limit, params.skip
        )
        return {
            "success": True,
            "workflows": [workflow.model_dump() for workflow in workflow_list.workflows],
            "count": workflow_list.count,
            "total": workflow_list.total,
        }
