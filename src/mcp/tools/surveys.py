"""Surveys tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ..params.surveys import (
    GetSurveysParams,
    GetSurveyParams,
    GetSurveySubmissionsParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_surveys_tools(_mcp, _get_client):
    """Register surveys tools with the MCP instance"""
    global mcp, get_client
    mcp = _mcp
    get_client = _get_client

    @mcp.tool()
    async def get_surveys(params: GetSurveysParams) -> Dict[str, Any]:
        """Get all surveys for a location"""
        client = await get_client(params.access_token)

        surveys = await client.get_surveys(params.location_id, params.limit, params.skip)
        return {"success": True, "surveys": surveys.model_dump()}

    @mcp.tool()
    async def get_survey(params: GetSurveyParams) -> Dict[str, Any]:
        """Get a specific survey"""
        client = await get_client(params.access_token)

        survey = await client.get_survey(params.survey_id, params.location_id)
        return {"success": True, "survey": survey.model_dump()}

    @mcp.tool()
    async def get_survey_submissions(params: GetSurveySubmissionsParams) -> Dict[str, Any]:
        """Get survey submissions for a location"""
        client = await get_client(params.access_token)

        submissions = await client.get_survey_submissions(
            params.location_id, params.survey_id, params.limit, params.skip
        )
        return {"success": True, "submissions": submissions.model_dump()}
