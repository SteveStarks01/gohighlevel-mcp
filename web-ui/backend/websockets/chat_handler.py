"""
WebSocket Chat Handler
Handles real-time chat communication via WebSocket
"""

import json
import logging
from typing import Dict, Any, List
from fastapi import WebSocket, WebSocketDisconnect
from datetime import datetime

from ..services.openrouter_client import OpenRouterClient, ChatMessage
from ..services.mcp_bridge import MCPBridge
from ..services.intent_processor import IntentProcessor

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections"""
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.user_connections: Dict[str, WebSocket] = {}
    
    async def connect(self, websocket: WebSocket, user_id: str = None):
        """Accept a new WebSocket connection"""
        await websocket.accept()
        self.active_connections.append(websocket)
        if user_id:
            self.user_connections[user_id] = websocket
        logger.info(f"WebSocket connected. Total connections: {len(self.active_connections)}")
    
    def disconnect(self, websocket: WebSocket, user_id: str = None):
        """Remove a WebSocket connection"""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
        if user_id and user_id in self.user_connections:
            del self.user_connections[user_id]
        logger.info(f"WebSocket disconnected. Total connections: {len(self.active_connections)}")
    
    async def send_personal_message(self, message: str, websocket: WebSocket):
        """Send a message to a specific WebSocket"""
        await websocket.send_text(message)
    
    async def send_to_user(self, message: str, user_id: str):
        """Send a message to a specific user"""
        if user_id in self.user_connections:
            await self.user_connections[user_id].send_text(message)


class ChatWebSocketHandler:
    """Handles WebSocket chat functionality"""
    
    def __init__(self, mcp_bridge: MCPBridge, openrouter_client: OpenRouterClient):
        self.mcp_bridge = mcp_bridge
        self.openrouter_client = openrouter_client
        self.intent_processor = IntentProcessor()
        self.connection_manager = ConnectionManager()
        self.conversation_history: Dict[str, List[ChatMessage]] = {}
    
    async def handle_connection(self, websocket: WebSocket):
        """Handle a new WebSocket connection"""
        user_id = None  # TODO: Extract from authentication
        
        await self.connection_manager.connect(websocket, user_id)
        
        try:
            # Send welcome message
            welcome_message = {
                "type": "system",
                "message": "Connected to GoHighLevel AI Assistant. How can I help you today?",
                "timestamp": datetime.utcnow().isoformat(),
                "suggestions": [
                    "Show me today's appointments",
                    "What's my pipeline looking like?",
                    "Create a new contact",
                    "Show recent conversations"
                ]
            }
            await websocket.send_text(json.dumps(welcome_message))
            
            # Handle incoming messages
            while True:
                data = await websocket.receive_text()
                message_data = json.loads(data)
                
                await self.handle_message(websocket, message_data, user_id)
                
        except WebSocketDisconnect:
            self.connection_manager.disconnect(websocket, user_id)
        except Exception as e:
            logger.error(f"WebSocket error: {str(e)}")
            self.connection_manager.disconnect(websocket, user_id)
    
    async def handle_message(self, websocket: WebSocket, message_data: Dict[str, Any], user_id: str = None):
        """Handle an incoming chat message"""
        try:
            message_type = message_data.get("type", "chat")
            
            if message_type == "chat":
                await self.handle_chat_message(websocket, message_data, user_id)
            elif message_type == "typing":
                await self.handle_typing_indicator(websocket, message_data, user_id)
            else:
                logger.warning(f"Unknown message type: {message_type}")
        
        except Exception as e:
            logger.error(f"Error handling message: {str(e)}")
            error_response = {
                "type": "error",
                "message": "Sorry, I encountered an error processing your message. Please try again.",
                "timestamp": datetime.utcnow().isoformat()
            }
            await websocket.send_text(json.dumps(error_response))
    
    async def handle_chat_message(self, websocket: WebSocket, message_data: Dict[str, Any], user_id: str = None):
        """Handle a chat message"""
        user_message = message_data.get("message", "")
        conversation_id = message_data.get("conversation_id", f"conv_{user_id or 'anonymous'}")
        
        logger.info(f"Processing chat message: {user_message}")
        
        # Send typing indicator
        typing_response = {
            "type": "typing",
            "is_typing": True,
            "timestamp": datetime.utcnow().isoformat()
        }
        await websocket.send_text(json.dumps(typing_response))
        
        try:
            # Get or create conversation history
            if conversation_id not in self.conversation_history:
                self.conversation_history[conversation_id] = []
            
            conversation = self.conversation_history[conversation_id]
            
            # Add user message to history
            user_chat_message = ChatMessage(role="user", content=user_message)
            conversation.append(user_chat_message)
            
            # Process intent
            intent, parameters = self.intent_processor.process_input(user_message)
            
            # Mock user context for now
            user_context = {
                "userId": user_id or "mock_user",
                "locationId": "mock_location",
                "companyId": "mock_company",
                "userName": "Demo User",
                "type": "location",
                "access_token": "mock_token"
            }
            
            # Execute MCP tools if intent identified
            mcp_data = None
            if intent:
                logger.info(f"Executing intent: {intent} with parameters: {parameters}")
                # mcp_data = await self.mcp_bridge.execute_intent(intent, parameters, user_context)
                
                # Mock execution for now
                mcp_data = await self.mock_mcp_execution(intent, parameters)
            
            # Generate AI response
            system_prompt = self.openrouter_client.get_system_prompt(user_context)
            
            # Add MCP data context if available
            if mcp_data and mcp_data.get("success"):
                context_message = ChatMessage(
                    role="system",
                    content=f"Tool execution result: {json.dumps(mcp_data.get('data', {}))}"
                )
                conversation.append(context_message)
            
            # Get AI response
            ai_response = await self.openrouter_client.chat_completion(
                messages=conversation[-10:],  # Keep last 10 messages for context
                system_prompt=system_prompt,
                temperature=0.7
            )
            
            # Add AI response to conversation
            ai_chat_message = ChatMessage(role="assistant", content=ai_response.content)
            conversation.append(ai_chat_message)
            
            # Send response
            response = {
                "type": "message",
                "message": ai_response.content,
                "intent": intent,
                "data": mcp_data,
                "conversation_id": conversation_id,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            # Stop typing indicator
            typing_response["is_typing"] = False
            await websocket.send_text(json.dumps(typing_response))
            
            # Send actual response
            await websocket.send_text(json.dumps(response))
            
        except Exception as e:
            logger.error(f"Error processing chat message: {str(e)}")
            
            # Stop typing indicator
            typing_response["is_typing"] = False
            await websocket.send_text(json.dumps(typing_response))
            
            # Send error response
            error_response = {
                "type": "error",
                "message": "I'm sorry, I encountered an error processing your request. Please try again.",
                "timestamp": datetime.utcnow().isoformat()
            }
            await websocket.send_text(json.dumps(error_response))
    
    async def handle_typing_indicator(self, websocket: WebSocket, message_data: Dict[str, Any], user_id: str = None):
        """Handle typing indicator"""
        # For now, just acknowledge the typing indicator
        # In a multi-user chat, this would broadcast to other users
        pass
    
    async def mock_mcp_execution(self, intent: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Mock MCP execution for development"""
        
        mock_responses = {
            "show_contacts": {
                "success": True,
                "data": {
                    "contacts": [
                        {"id": "1", "name": "John Smith", "email": "john@example.com", "phone": "+1-555-0123"},
                        {"id": "2", "name": "Sarah Johnson", "email": "sarah@example.com", "phone": "+1-555-0124"},
                        {"id": "3", "name": "Mike Davis", "email": "mike@example.com", "phone": "+1-555-0125"}
                    ],
                    "count": 3,
                    "total": 1247
                }
            },
            "show_appointments": {
                "success": True,
                "data": {
                    "appointments": [
                        {
                            "id": "1",
                            "title": "Sales Call with ABC Corp",
                            "contact": "John Smith",
                            "time": "10:00 AM",
                            "duration": "1 hour"
                        },
                        {
                            "id": "2",
                            "title": "Product Demo",
                            "contact": "Sarah Johnson",
                            "time": "2:30 PM",
                            "duration": "30 minutes"
                        }
                    ],
                    "count": 2
                }
            },
            "show_opportunities": {
                "success": True,
                "data": {
                    "opportunities": [
                        {"id": "1", "name": "ABC Corp Deal", "value": 15000, "stage": "Proposal"},
                        {"id": "2", "name": "XYZ Inc Project", "value": 25000, "stage": "Qualified"},
                        {"id": "3", "name": "Tech Solutions Contract", "value": 35000, "stage": "Negotiation"}
                    ],
                    "total_value": 75000,
                    "count": 3
                }
            },
            "show_analytics": {
                "success": True,
                "data": {
                    "kpis": {
                        "total_contacts": 1247,
                        "total_opportunities": 89,
                        "total_value": 245000,
                        "conversion_rate": 23.5
                    }
                }
            }
        }
        
        return mock_responses.get(intent, {
            "success": False,
            "error": f"No mock data available for intent: {intent}"
        })
