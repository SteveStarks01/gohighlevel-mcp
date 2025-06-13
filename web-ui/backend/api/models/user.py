"""
User and Authentication Models
"""

from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserContext(BaseModel):
    """User context information"""
    user_id: str
    company_id: Optional[str] = None
    location_id: Optional[str] = None
    role: str
    user_type: str  # "agency", "location", "user"
    user_name: str
    email: EmailStr
    permissions: Optional[list] = None
    created_at: Optional[datetime] = None


class InstallationData(BaseModel):
    """App installation data"""
    client_id: str
    install_type: str  # "agency", "location"
    location_id: Optional[str] = None
    company_id: Optional[str] = None
    installed_at: Optional[datetime] = None
    status: str = "pending"  # "pending", "active", "suspended"


class TokenData(BaseModel):
    """OAuth token data"""
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "Bearer"
    expires_in: Optional[int] = None
    scope: Optional[str] = None
    location_id: Optional[str] = None
    company_id: Optional[str] = None
    user_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class SessionData(BaseModel):
    """User session data"""
    session_id: str
    user_context: UserContext
    token_data: TokenData
    created_at: datetime
    last_activity: datetime
    expires_at: datetime
