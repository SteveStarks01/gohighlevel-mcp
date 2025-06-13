"""Tests for surveys functionality"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from src.api.surveys import SurveysClient
from src.models.survey import Survey, SurveySubmission, SurveyList, SurveySubmissionList
from src.services.oauth import OAuthService


@pytest.fixture
def oauth_service():
    """Create a mock OAuth service"""
    service = MagicMock(spec=OAuthService)
    service.get_access_token = AsyncMock(return_value="test_token")
    return service


@pytest.fixture
def surveys_client(oauth_service):
    """Create a SurveysClient instance"""
    return SurveysClient(oauth_service)


@pytest.mark.asyncio
async def test_get_surveys(surveys_client):
    """Test getting surveys"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "surveys": [
            {
                "id": "survey_123",
                "locationId": "loc_123",
                "name": "Customer Feedback",
                "description": "Survey for customer feedback",
                "isActive": True,
                "questions": [
                    {"id": "q1", "type": "text", "question": "How was your experience?"}
                ]
            }
        ],
        "total": 1
    }
    
    surveys_client._request = AsyncMock(return_value=mock_response)
    
    # Test the method
    result = await surveys_client.get_surveys("loc_123", limit=10, skip=0)
    
    # Assertions
    assert isinstance(result, SurveyList)
    assert len(result.surveys) == 1
    assert result.surveys[0].id == "survey_123"
    assert result.surveys[0].name == "Customer Feedback"
    assert result.total == 1
    
    # Verify the request was made correctly
    surveys_client._request.assert_called_once_with(
        "GET", "/surveys/", params={"limit": 10}, location_id="loc_123"
    )


@pytest.mark.asyncio
async def test_get_survey(surveys_client):
    """Test getting a single survey"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "survey": {
            "id": "survey_123",
            "locationId": "loc_123",
            "name": "Customer Feedback",
            "description": "Survey for customer feedback",
            "isActive": True,
            "questions": [
                {"id": "q1", "type": "text", "question": "How was your experience?"}
            ]
        }
    }
    
    surveys_client._request = AsyncMock(return_value=mock_response)
    
    # Test the method
    result = await surveys_client.get_survey("survey_123", "loc_123")
    
    # Assertions
    assert isinstance(result, Survey)
    assert result.id == "survey_123"
    assert result.name == "Customer Feedback"
    assert result.isActive == True
    
    # Verify the request was made correctly
    surveys_client._request.assert_called_once_with(
        "GET", "/surveys/survey_123", location_id="loc_123"
    )


@pytest.mark.asyncio
async def test_get_survey_submissions(surveys_client):
    """Test getting survey submissions"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "submissions": [
            {
                "id": "sub_123",
                "surveyId": "survey_123",
                "locationId": "loc_123",
                "contactId": "contact_123",
                "responses": {
                    "q1": "Great experience!"
                },
                "submittedAt": "2024-01-01T12:00:00Z"
            }
        ],
        "total": 1
    }
    
    surveys_client._request = AsyncMock(return_value=mock_response)
    
    # Test the method
    result = await surveys_client.get_survey_submissions("loc_123", survey_id="survey_123", limit=10, skip=0)
    
    # Assertions
    assert isinstance(result, SurveySubmissionList)
    assert len(result.submissions) == 1
    assert result.submissions[0].id == "sub_123"
    assert result.submissions[0].surveyId == "survey_123"
    assert result.submissions[0].responses["q1"] == "Great experience!"
    assert result.total == 1
    
    # Verify the request was made correctly
    surveys_client._request.assert_called_once_with(
        "GET", "/surveys/submissions", 
        params={"limit": 10, "surveyId": "survey_123"}, 
        location_id="loc_123"
    )


@pytest.mark.asyncio
async def test_get_survey_submissions_no_filter(surveys_client):
    """Test getting survey submissions without survey filter"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "submissions": [
            {
                "id": "sub_123",
                "surveyId": "survey_123",
                "locationId": "loc_123",
                "contactId": "contact_123",
                "responses": {
                    "q1": "Great experience!"
                }
            },
            {
                "id": "sub_124",
                "surveyId": "survey_124",
                "locationId": "loc_123",
                "contactId": "contact_124",
                "responses": {
                    "q1": "Good experience!"
                }
            }
        ],
        "total": 2
    }
    
    surveys_client._request = AsyncMock(return_value=mock_response)
    
    # Test the method without survey_id filter
    result = await surveys_client.get_survey_submissions("loc_123", limit=10, skip=0)
    
    # Assertions
    assert isinstance(result, SurveySubmissionList)
    assert len(result.submissions) == 2
    assert result.submissions[0].id == "sub_123"
    assert result.submissions[1].id == "sub_124"
    assert result.total == 2
    
    # Verify the request was made correctly (no surveyId in params)
    surveys_client._request.assert_called_once_with(
        "GET", "/surveys/submissions", 
        params={"limit": 10}, 
        location_id="loc_123"
    )
