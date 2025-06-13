"""
Chat Routes
Handles chat API endpoints for the AI assistant
"""

import logging
from typing import Dict, Any, List
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from datetime import datetime

from ..services.openrouter_client import OpenRouterClient, ChatMessage
from ..services.mcp_bridge import MCPBridge
from ..services.intent_processor import IntentProcessor

logger = logging.getLogger(__name__)

router = APIRouter()


class ChatRequest(BaseModel):
    """Chat request model"""
    message: str
    conversation_id: str = None


class ChatResponse(BaseModel):
    """Chat response model"""
    response: str
    conversation_id: str
    intent: str = None
    data: Dict[str, Any] = None
    timestamp: str


async def get_user_context() -> Dict[str, Any]:
    """Get current user context (mock for now)"""
    return {
        "userId": "mock_user_id",
        "companyId": "mock_company_id",
        "locationId": "mock_location_id",
        "role": "admin",
        "type": "location",
        "userName": "Demo User",
        "email": "demo@example.com",
        "access_token": "mock_access_token"
    }


@router.post("/message", response_model=ChatResponse)
async def send_chat_message(
    request: ChatRequest,
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """
    Send a message to the AI assistant
    
    This endpoint processes user messages, identifies intents,
    executes MCP tools, and returns AI-generated responses.
    """
    try:
        logger.info(f"Chat message received: {request.message}")
        
        # Initialize services (in production, use dependency injection)
        openrouter_client = OpenRouterClient()
        intent_processor = IntentProcessor()
        # mcp_bridge = MCPBridge(ghl_client)  # TODO: Get from DI
        
        # Process user input to identify intent
        intent, parameters = intent_processor.process_input(request.message)
        
        # Prepare conversation context
        conversation_history = []  # TODO: Load from database
        
        # Add user message to history
        user_message = ChatMessage(role="user", content=request.message)
        conversation_history.append(user_message)
        
        # Execute MCP tools if intent is identified
        mcp_data = None
        if intent:
            logger.info(f"Identified intent: {intent} with parameters: {parameters}")
            
            # Mock MCP execution for now
            mcp_data = await mock_mcp_execution(intent, parameters, user_context)
        
        # Generate AI response
        system_prompt = openrouter_client.get_system_prompt(user_context)
        
        # Add context about executed tools to the conversation
        if mcp_data and mcp_data.get("success"):
            context_message = f"I executed the '{intent}' action and retrieved the following data: {mcp_data.get('data', {})}"
            conversation_history.append(ChatMessage(role="system", content=context_message))
        
        # Get AI response
        ai_response = await openrouter_client.chat_completion(
            messages=conversation_history,
            system_prompt=system_prompt,
            temperature=0.7
        )
        
        # Create response
        response = ChatResponse(
            response=ai_response.content,
            conversation_id=request.conversation_id or f"conv_{datetime.utcnow().timestamp()}",
            intent=intent,
            data=mcp_data,
            timestamp=datetime.utcnow().isoformat()
        )
        
        # TODO: Save conversation to database
        
        return response
        
    except Exception as e:
        logger.error(f"Error processing chat message: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to process message")


@router.get("/conversations")
async def get_conversations(
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """Get user's conversation history"""
    try:
        # TODO: Get from database
        mock_conversations = [
            {
                "id": "conv_1",
                "title": "Contact Management",
                "last_message": "Show me today's contacts",
                "timestamp": datetime.utcnow().isoformat(),
                "message_count": 5
            },
            {
                "id": "conv_2",
                "title": "Pipeline Review",
                "last_message": "What's my pipeline looking like?",
                "timestamp": (datetime.utcnow()).isoformat(),
                "message_count": 8
            }
        ]
        
        return {
            "success": True,
            "conversations": mock_conversations
        }
        
    except Exception as e:
        logger.error(f"Error getting conversations: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get conversations")


@router.get("/conversations/{conversation_id}/messages")
async def get_conversation_messages(
    conversation_id: str,
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """Get messages from a specific conversation"""
    try:
        # TODO: Get from database
        mock_messages = [
            {
                "id": "msg_1",
                "role": "user",
                "content": "Show me today's contacts",
                "timestamp": datetime.utcnow().isoformat()
            },
            {
                "id": "msg_2",
                "role": "assistant",
                "content": "I found 12 contacts created today. Here are the most recent ones: John Smith, Sarah Johnson, Mike Davis...",
                "timestamp": datetime.utcnow().isoformat(),
                "data": {
                    "intent": "show_contacts",
                    "contacts_count": 12
                }
            }
        ]
        
        return {
            "success": True,
            "messages": mock_messages
        }
        
    except Exception as e:
        logger.error(f"Error getting conversation messages: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get messages")


@router.get("/suggestions")
async def get_chat_suggestions(
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """Get suggested prompts for the user"""
    try:
        suggestions = [
            {
                "text": "Show me today's appointments",
                "category": "calendar",
                "icon": "calendar"
            },
            {
                "text": "Create a new contact for John Doe",
                "category": "contacts",
                "icon": "user-plus"
            },
            {
                "text": "What's my pipeline looking like?",
                "category": "opportunities",
                "icon": "trending-up"
            },
            {
                "text": "Send a follow-up message to recent leads",
                "category": "messaging",
                "icon": "message-circle"
            },
            {
                "text": "Show me this week's performance",
                "category": "analytics",
                "icon": "bar-chart"
            }
        ]
        
        return {
            "success": True,
            "suggestions": suggestions
        }
        
    except Exception as e:
        logger.error(f"Error getting suggestions: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get suggestions")


async def mock_mcp_execution(intent: str, parameters: Dict[str, Any], user_context: Dict[str, Any]) -> Dict[str, Any]:
    """Mock MCP tool execution for development"""
    
    mock_responses = {
        "show_contacts": {
            "success": True,
            "data": {
                "contacts": [
                    {"id": "1", "name": "John Smith", "email": "john@example.com"},
                    {"id": "2", "name": "Sarah Johnson", "email": "sarah@example.com"}
                ],
                "count": 2,
                "total": 1247
            }
        },
        "show_appointments": {
            "success": True,
            "data": {
                "appointments": [
                    {"id": "1", "title": "Sales Call", "contact": "John Smith", "time": "10:00 AM"},
                    {"id": "2", "title": "Demo", "contact": "Sarah Johnson", "time": "2:30 PM"}
                ],
                "count": 2
            }
        },
        "show_opportunities": {
            "success": True,
            "data": {
                "opportunities": [
                    {"id": "1", "name": "ABC Corp Deal", "value": 15000, "stage": "Proposal"},
                    {"id": "2", "name": "XYZ Inc Project", "value": 25000, "stage": "Qualified"}
                ],
                "total_value": 40000,
                "count": 2
            }
        }
    }
    
    return mock_responses.get(intent, {
        "success": False,
        "error": f"No mock data for intent: {intent}"
    })
