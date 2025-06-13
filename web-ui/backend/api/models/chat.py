"""
Chat and Conversation Models
"""

from typing import Optional, Dict, Any, List
from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class MessageRole(str, Enum):
    """Message role enumeration"""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"


class MessageType(str, Enum):
    """Message type enumeration"""
    TEXT = "text"
    DATA = "data"
    ERROR = "error"
    SYSTEM = "system"


class ChatMessage(BaseModel):
    """Individual chat message"""
    id: Optional[str] = None
    conversation_id: str
    role: MessageRole
    content: str
    message_type: MessageType = MessageType.TEXT
    intent: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    mcp_data: Optional[Dict[str, Any]] = None
    timestamp: datetime
    user_id: Optional[str] = None


class Conversation(BaseModel):
    """Chat conversation"""
    id: str
    user_id: str
    title: str
    created_at: datetime
    updated_at: datetime
    message_count: int = 0
    last_message: Optional[str] = None
    last_message_at: Optional[datetime] = None
    metadata: Optional[Dict[str, Any]] = None


class ConversationSummary(BaseModel):
    """Conversation summary for listing"""
    id: str
    title: str
    last_message: Optional[str] = None
    last_message_at: Optional[datetime] = None
    message_count: int = 0
    created_at: datetime


class ChatSession(BaseModel):
    """Active chat session"""
    session_id: str
    conversation_id: str
    user_id: str
    websocket_id: Optional[str] = None
    created_at: datetime
    last_activity: datetime
    is_active: bool = True


class IntentResult(BaseModel):
    """Result of intent processing"""
    intent: Optional[str] = None
    confidence: float = 0.0
    parameters: Dict[str, Any] = {}
    suggested_actions: List[str] = []


class MCPExecutionResult(BaseModel):
    """Result of MCP tool execution"""
    success: bool
    intent: Optional[str] = None
    tool: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    execution_time: Optional[float] = None
    timestamp: datetime
