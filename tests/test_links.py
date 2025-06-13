"""Tests for links functionality"""

import pytest
from unittest.mock import AsyncMock, MagicMock
from src.api.links import LinksClient
from src.models.link import Link, LinkCreate, LinkUpdate, LinkList
from src.services.oauth import OAuthService


@pytest.fixture
def oauth_service():
    """Create a mock OAuth service"""
    service = MagicMock(spec=OAuthService)
    service.get_access_token = AsyncMock(return_value="test_token")
    return service


@pytest.fixture
def links_client(oauth_service):
    """Create a LinksClient instance"""
    return LinksClient(oauth_service)


@pytest.mark.asyncio
async def test_get_links(links_client):
    """Test getting links"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "links": [
            {
                "id": "link_123",
                "locationId": "loc_123",
                "name": "Test Link",
                "url": "https://example.com",
                "shortUrl": "https://short.ly/abc",
                "description": "Test description",
                "isActive": True,
                "clickCount": 10
            }
        ],
        "total": 1
    }
    
    links_client._request = AsyncMock(return_value=mock_response)
    
    # Test the method
    result = await links_client.get_links("loc_123", limit=10, skip=0)
    
    # Assertions
    assert isinstance(result, LinkList)
    assert len(result.links) == 1
    assert result.links[0].id == "link_123"
    assert result.links[0].name == "Test Link"
    assert result.total == 1
    
    # Verify the request was made correctly
    links_client._request.assert_called_once_with(
        "GET", "/links/", params={"limit": 10}, location_id="loc_123"
    )


@pytest.mark.asyncio
async def test_get_link(links_client):
    """Test getting a single link"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "link": {
            "id": "link_123",
            "locationId": "loc_123",
            "name": "Test Link",
            "url": "https://example.com",
            "shortUrl": "https://short.ly/abc",
            "description": "Test description",
            "isActive": True,
            "clickCount": 10
        }
    }
    
    links_client._request = AsyncMock(return_value=mock_response)
    
    # Test the method
    result = await links_client.get_link("link_123", "loc_123")
    
    # Assertions
    assert isinstance(result, Link)
    assert result.id == "link_123"
    assert result.name == "Test Link"
    assert result.url == "https://example.com"
    
    # Verify the request was made correctly
    links_client._request.assert_called_once_with(
        "GET", "/links/link_123", location_id="loc_123"
    )


@pytest.mark.asyncio
async def test_create_link(links_client):
    """Test creating a link"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "link": {
            "id": "link_123",
            "locationId": "loc_123",
            "name": "New Link",
            "url": "https://example.com",
            "description": "New description",
            "isActive": True,
            "clickCount": 0
        }
    }
    
    links_client._request = AsyncMock(return_value=mock_response)
    
    # Create link data
    link_data = LinkCreate(
        name="New Link",
        url="https://example.com",
        description="New description",
        isActive=True
    )
    
    # Test the method
    result = await links_client.create_link(link_data, "loc_123")
    
    # Assertions
    assert isinstance(result, Link)
    assert result.id == "link_123"
    assert result.name == "New Link"
    assert result.url == "https://example.com"
    
    # Verify the request was made correctly
    links_client._request.assert_called_once_with(
        "POST", "/links/", 
        json={
            "name": "New Link",
            "url": "https://example.com",
            "description": "New description",
            "isActive": True
        }, 
        location_id="loc_123"
    )


@pytest.mark.asyncio
async def test_update_link(links_client):
    """Test updating a link"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "link": {
            "id": "link_123",
            "locationId": "loc_123",
            "name": "Updated Link",
            "url": "https://updated.com",
            "description": "Updated description",
            "isActive": False,
            "clickCount": 5
        }
    }
    
    links_client._request = AsyncMock(return_value=mock_response)
    
    # Create update data
    update_data = LinkUpdate(
        name="Updated Link",
        url="https://updated.com",
        description="Updated description",
        isActive=False
    )
    
    # Test the method
    result = await links_client.update_link("link_123", update_data, "loc_123")
    
    # Assertions
    assert isinstance(result, Link)
    assert result.id == "link_123"
    assert result.name == "Updated Link"
    assert result.url == "https://updated.com"
    assert result.isActive == False
    
    # Verify the request was made correctly
    links_client._request.assert_called_once_with(
        "PUT", "/links/link_123", 
        json={
            "name": "Updated Link",
            "url": "https://updated.com",
            "description": "Updated description",
            "isActive": False
        }, 
        location_id="loc_123"
    )


@pytest.mark.asyncio
async def test_delete_link(links_client):
    """Test deleting a link"""
    # Mock the response
    mock_response = MagicMock()
    mock_response.status_code = 204
    
    links_client._request = AsyncMock(return_value=mock_response)
    
    # Test the method
    result = await links_client.delete_link("link_123", "loc_123")
    
    # Assertions
    assert result["success"] == True
    assert "deleted successfully" in result["message"]
    
    # Verify the request was made correctly
    links_client._request.assert_called_once_with(
        "DELETE", "/links/link_123", location_id="loc_123"
    )
