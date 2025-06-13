"""Surveys management client for GoHighLevel API v2"""

from typing import Optional
from .base import BaseGoHighLevelClient
from ..models.survey import Survey, SurveySubmission, SurveyList, SurveySubmissionList


class SurveysClient(BaseGoHighLevelClient):
    """Client for surveys-related endpoints"""

    async def get_surveys(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> SurveyList:
        """Get all surveys for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            SurveyList containing surveys and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", "/surveys/", params=params, location_id=location_id
        )
        data = response.json()
        
        surveys_data = data.get("surveys", [])
        return SurveyList(
            surveys=[Survey(**survey) for survey in surveys_data],
            count=len(surveys_data),
            total=data.get("total", len(surveys_data)),
        )

    async def get_survey(self, survey_id: str, location_id: str) -> Survey:
        """Get a specific survey by ID
        
        Args:
            survey_id: The survey ID
            location_id: The location ID
            
        Returns:
            Survey object
        """
        response = await self._request(
            "GET", f"/surveys/{survey_id}", location_id=location_id
        )
        data = response.json()
        return Survey(**data.get("survey", data))

    async def get_survey_submissions(
        self, 
        location_id: str, 
        survey_id: Optional[str] = None,
        limit: int = 100, 
        skip: int = 0
    ) -> SurveySubmissionList:
        """Get survey submissions for a location
        
        Args:
            location_id: The location ID
            survey_id: Optional survey ID to filter submissions
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            SurveySubmissionList containing submissions and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
        if survey_id:
            params["surveyId"] = survey_id
            
        response = await self._request(
            "GET", "/surveys/submissions", params=params, location_id=location_id
        )
        data = response.json()
        
        submissions_data = data.get("submissions", [])
        return SurveySubmissionList(
            submissions=[SurveySubmission(**submission) for submission in submissions_data],
            count=len(submissions_data),
            total=data.get("total", len(submissions_data)),
        )
