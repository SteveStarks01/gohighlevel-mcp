"""Tests for OAuth management functionality"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from src.api.oauth_management import OAuthManagementClient
from src.models.oauth import (
    InstalledLocation, InstalledLocationList, LocationToken, LocationTokenRequest,
    SaasSubscription, SaasSubscriptionUpdate
)
from src.services.oauth import OAuthService


@pytest.fixture
def oauth_service():
    """Create a mock OAuth service"""
    service = MagicMock(spec=OAuthService)
    service.get_access_token = AsyncMock(return_value="test_token")
    return service


@pytest.fixture
def oauth_client(oauth_service):
    """Create an OAuthManagementClient instance"""
    return OAuthManagementClient(oauth_service)


@pytest.mark.asyncio
async def test_get_installed_locations(oauth_client):
    """Test getting installed locations"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "locations": [
            {
                "locationId": "loc_123",
                "locationName": "Test Location",
                "companyId": "comp_123",
                "companyName": "Test Company",
                "installedAt": "2024-01-01T12:00:00Z",
                "isActive": True,
                "permissions": ["contacts.readonly", "contacts.write"]
            }
        ],
        "total": 1
    }
    
    oauth_client._request = AsyncMock(return_value=mock_response)
    
    # Test the method
    result = await oauth_client.get_installed_locations(limit=10, skip=0)
    
    # Assertions
    assert isinstance(result, InstalledLocationList)
    assert len(result.locations) == 1
    assert result.locations[0].locationId == "loc_123"
    assert result.locations[0].locationName == "Test Location"
    assert result.locations[0].isActive == True
    assert result.total == 1
    
    # Verify the request was made correctly
    oauth_client._request.assert_called_once_with(
        "GET", "/oauth/installedLocations", params={"limit": 10}
    )


@pytest.mark.asyncio
async def test_generate_location_token(oauth_client):
    """Test generating a location token"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "token": {
            "locationId": "loc_123",
            "accessToken": "new_access_token_123",
            "tokenType": "Bearer",
            "expiresIn": 3600,
            "scope": "contacts.readonly contacts.write",
            "createdAt": "2024-01-01T12:00:00Z"
        }
    }
    
    oauth_client._request = AsyncMock(return_value=mock_response)
    
    # Create request data
    request_data = LocationTokenRequest(
        locationId="loc_123",
        scope="contacts.readonly contacts.write"
    )
    
    # Test the method
    result = await oauth_client.generate_location_token(request_data)
    
    # Assertions
    assert isinstance(result, LocationToken)
    assert result.locationId == "loc_123"
    assert result.accessToken == "new_access_token_123"
    assert result.tokenType == "Bearer"
    assert result.expiresIn == 3600
    
    # Verify the request was made correctly
    oauth_client._request.assert_called_once_with(
        "POST", "/oauth/locationToken", 
        json={
            "locationId": "loc_123",
            "scope": "contacts.readonly contacts.write"
        }
    )


@pytest.mark.asyncio
async def test_update_saas_subscription(oauth_client):
    """Test updating SaaS subscription"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "subscription": {
            "locationId": "loc_123",
            "planId": "premium_plan",
            "status": "active",
            "billingCycle": "monthly",
            "amount": 99.99,
            "currency": "USD",
            "startDate": "2024-01-01T00:00:00Z",
            "endDate": "2024-02-01T00:00:00Z",
            "isActive": True,
            "updatedAt": "2024-01-01T12:00:00Z"
        }
    }
    
    oauth_client._request = AsyncMock(return_value=mock_response)
    
    # Create subscription update data
    subscription_data = SaasSubscriptionUpdate(
        planId="premium_plan",
        status="active",
        billingCycle="monthly",
        amount=99.99,
        currency="USD",
        isActive=True
    )
    
    # Test the method
    result = await oauth_client.update_saas_subscription("loc_123", subscription_data)
    
    # Assertions
    assert isinstance(result, SaasSubscription)
    assert result.locationId == "loc_123"
    assert result.planId == "premium_plan"
    assert result.status == "active"
    assert result.amount == 99.99
    assert result.isActive == True
    
    # Verify the request was made correctly
    oauth_client._request.assert_called_once_with(
        "PUT", "/update-saas-subscription/loc_123", 
        json={
            "planId": "premium_plan",
            "status": "active",
            "billingCycle": "monthly",
            "amount": 99.99,
            "currency": "USD",
            "isActive": True
        }
    )


@pytest.mark.asyncio
async def test_generate_location_token_minimal(oauth_client):
    """Test generating a location token with minimal data"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "locationId": "loc_123",
        "accessToken": "new_access_token_123",
        "tokenType": "Bearer"
    }
    
    oauth_client._request = AsyncMock(return_value=mock_response)
    
    # Create minimal request data
    request_data = LocationTokenRequest(locationId="loc_123")
    
    # Test the method
    result = await oauth_client.generate_location_token(request_data)
    
    # Assertions
    assert isinstance(result, LocationToken)
    assert result.locationId == "loc_123"
    assert result.accessToken == "new_access_token_123"
    assert result.tokenType == "Bearer"
    
    # Verify the request was made correctly
    oauth_client._request.assert_called_once_with(
        "POST", "/oauth/locationToken", 
        json={"locationId": "loc_123"}
    )
