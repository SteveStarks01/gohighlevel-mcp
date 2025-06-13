"""
Authentication Routes
Handles OAuth 2.0 flow for GoHighLevel marketplace app
"""

import os
import logging
from typing import Dict, Any
from fastapi import APIRouter, HTTPException, Request, Depends, Query
from fastapi.responses import RedirectResponse
import httpx
from cryptography.fernet import Fernet
import json
import base64

from ..models.user import UserContext, InstallationData
from ..services.openrouter_client import OpenRouterClient

logger = logging.getLogger(__name__)

router = APIRouter()

# Environment variables
GHL_CLIENT_ID = os.getenv("GHL_CLIENT_ID")
GHL_CLIENT_SECRET = os.getenv("GHL_CLIENT_SECRET")
GHL_SHARED_SECRET = os.getenv("GHL_SHARED_SECRET")
GHL_REDIRECT_URI = os.getenv("GHL_REDIRECT_URI")

if not all([GHL_CLIENT_ID, GHL_CLIENT_SECRET, GHL_SHARED_SECRET]):
    raise ValueError("Missing required GoHighLevel environment variables")


@router.get("/install")
async def handle_app_install(
    clientId: str = Query(...),
    installType: str = Query(...),
    locationId: str = Query(None),
    companyId: str = Query(None)
):
    """
    Handle app installation from GoHighLevel marketplace
    
    This endpoint is called when a user installs the app from the marketplace.
    It receives installation parameters and initiates the OAuth flow.
    """
    try:
        logger.info(f"App installation request: clientId={clientId}, installType={installType}, locationId={locationId}, companyId={companyId}")
        
        # Validate client ID
        if clientId != GHL_CLIENT_ID:
            raise HTTPException(status_code=400, detail="Invalid client ID")
        
        # Store installation data (in production, use a database)
        installation_data = InstallationData(
            client_id=clientId,
            install_type=installType,
            location_id=locationId,
            company_id=companyId
        )
        
        # TODO: Store installation_data in database
        
        # Redirect to OAuth authorization
        oauth_url = f"https://marketplace.gohighlevel.com/oauth/chooselocation"
        oauth_params = {
            "response_type": "code",
            "redirect_uri": GHL_REDIRECT_URI,
            "client_id": GHL_CLIENT_ID,
            "scope": " ".join([
                "contacts.readonly", "contacts.write",
                "conversations.readonly", "conversations.write",
                "opportunities.readonly", "opportunities.write",
                "calendars.readonly", "calendars.write",
                "businesses.readonly", "businesses.write",
                "users.readonly", "users.write",
                "campaigns.readonly", "workflows.readonly",
                "locations.readonly", "locations.write",
                "products.readonly", "products.write",
                "payments/orders.readonly",
                "oauth.readonly", "oauth.write"
            ])
        }
        
        # Build OAuth URL
        oauth_query = "&".join([f"{k}={v}" for k, v in oauth_params.items()])
        full_oauth_url = f"{oauth_url}?{oauth_query}"
        
        return RedirectResponse(url=full_oauth_url)
        
    except Exception as e:
        logger.error(f"Error handling app installation: {str(e)}")
        raise HTTPException(status_code=500, detail="Installation failed")


@router.get("/callback")
async def oauth_callback(
    code: str = Query(...),
    state: str = Query(None)
):
    """
    Handle OAuth callback from GoHighLevel
    
    This endpoint receives the authorization code and exchanges it for tokens.
    """
    try:
        logger.info(f"OAuth callback received: code={code[:10]}..., state={state}")
        
        # Exchange code for tokens
        token_url = "https://services.leadconnectorhq.com/oauth/token"
        token_data = {
            "client_id": GHL_CLIENT_ID,
            "client_secret": GHL_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": GHL_REDIRECT_URI
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(token_url, data=token_data)
            response.raise_for_status()
            tokens = response.json()
        
        # TODO: Store tokens in database associated with installation
        
        logger.info("OAuth flow completed successfully")
        
        # Redirect to the app dashboard
        return RedirectResponse(url="/dashboard")
        
    except httpx.HTTPStatusError as e:
        logger.error(f"OAuth token exchange failed: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=400, detail="OAuth authentication failed")
    except Exception as e:
        logger.error(f"Error in OAuth callback: {str(e)}")
        raise HTTPException(status_code=500, detail="Authentication failed")


@router.post("/decrypt-user-data")
async def decrypt_user_data(request: Request):
    """
    Decrypt user session data from GoHighLevel
    
    This endpoint receives encrypted user data from the frontend and decrypts it
    using the shared secret key.
    """
    try:
        body = await request.json()
        encrypted_data = body.get("encryptedData")
        
        if not encrypted_data:
            raise HTTPException(status_code=400, detail="Missing encrypted data")
        
        # Decrypt using shared secret
        cipher = Fernet(base64.urlsafe_b64encode(GHL_SHARED_SECRET.encode()[:32].ljust(32, b'0')))
        decrypted_bytes = cipher.decrypt(encrypted_data.encode())
        user_data = json.loads(decrypted_bytes.decode())
        
        # Create user context
        user_context = UserContext(
            user_id=user_data.get("userId"),
            company_id=user_data.get("companyId"),
            location_id=user_data.get("activeLocation"),
            role=user_data.get("role"),
            user_type=user_data.get("type"),
            user_name=user_data.get("userName"),
            email=user_data.get("email")
        )
        
        return {
            "success": True,
            "user_context": user_context.model_dump()
        }
        
    except Exception as e:
        logger.error(f"Error decrypting user data: {str(e)}")
        raise HTTPException(status_code=400, detail="Failed to decrypt user data")


@router.get("/user-context")
async def get_user_context(request: Request):
    """
    Get current user context from session
    
    This endpoint returns the current user's context information.
    """
    try:
        # TODO: Get user context from session/database
        # For now, return a mock response
        
        return {
            "success": True,
            "user_context": {
                "user_id": "mock_user_id",
                "company_id": "mock_company_id",
                "location_id": "mock_location_id",
                "role": "admin",
                "user_type": "location",
                "user_name": "Demo User",
                "email": "demo@example.com"
            }
        }
        
    except Exception as e:
        logger.error(f"Error getting user context: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get user context")


@router.post("/logout")
async def logout(request: Request):
    """
    Logout user and clear session
    """
    try:
        # TODO: Clear user session
        
        return {
            "success": True,
            "message": "Logged out successfully"
        }
        
    except Exception as e:
        logger.error(f"Error during logout: {str(e)}")
        raise HTTPException(status_code=500, detail="Logout failed")
