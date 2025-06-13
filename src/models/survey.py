"""Survey models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class Survey(BaseModel):
    """GoHighLevel Survey model"""

    id: str = Field(..., description="Survey ID")
    locationId: str = Field(..., description="Location ID")
    name: str = Field(..., description="Survey name")
    description: Optional[str] = Field(None, description="Survey description")
    isActive: Optional[bool] = Field(True, description="Whether survey is active")
    questions: Optional[List[Dict[str, Any]]] = Field(None, description="Survey questions")
    settings: Optional[Dict[str, Any]] = Field(None, description="Survey settings")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")
    createdBy: Optional[str] = Field(None, description="User who created the survey")

    model_config = {"populate_by_name": True}


class SurveySubmission(BaseModel):
    """GoHighLevel Survey Submission model"""

    id: str = Field(..., description="Submission ID")
    surveyId: str = Field(..., description="Survey ID")
    locationId: str = Field(..., description="Location ID")
    contactId: Optional[str] = Field(None, description="Contact ID")
    responses: Dict[str, Any] = Field(..., description="Survey responses")
    submittedAt: Optional[datetime] = Field(None, description="Submission date")
    ipAddress: Optional[str] = Field(None, description="Submitter IP address")
    userAgent: Optional[str] = Field(None, description="Submitter user agent")

    model_config = {"populate_by_name": True}


class SurveyList(BaseModel):
    """List of surveys"""

    surveys: List[Survey] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}


class SurveySubmissionList(BaseModel):
    """List of survey submissions"""

    submissions: List[SurveySubmission] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}
