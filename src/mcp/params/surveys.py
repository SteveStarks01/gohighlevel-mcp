"""Parameter models for surveys MCP tools"""

from typing import Optional
from pydantic import BaseModel, Field


class GetSurveysParams(BaseModel):
    """Parameters for getting surveys"""

    location_id: str = Field(..., description="The location ID to get surveys for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetSurveyParams(BaseModel):
    """Parameters for getting a single survey"""

    location_id: str = Field(..., description="The location ID")
    survey_id: str = Field(..., description="The survey ID to retrieve")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetSurveySubmissionsParams(BaseModel):
    """Parameters for getting survey submissions"""

    location_id: str = Field(..., description="The location ID to get submissions for")
    survey_id: Optional[str] = Field(None, description="Optional survey ID to filter submissions")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
