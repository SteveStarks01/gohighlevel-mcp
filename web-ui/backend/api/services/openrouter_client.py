"""
OpenRouter API Client
Handles communication with OpenRouter for AI functionality
"""

import os
import json
import logging
from typing import Dict, List, Any, Optional, AsyncGenerator
import httpx
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class ChatMessage(BaseModel):
    """Chat message model"""
    role: str  # "user", "assistant", "system"
    content: str


class OpenRouterResponse(BaseModel):
    """OpenRouter API response model"""
    content: str
    usage: Optional[Dict[str, Any]] = None
    model: Optional[str] = None


class OpenRouterClient:
    """Client for OpenRouter API integration"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = os.getenv("OPENROUTER_MODEL", "anthropic/claude-3-sonnet")
        self.max_tokens = int(os.getenv("OPENROUTER_MAX_TOKENS", "4000"))
        
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY environment variable is required")
        
        self.client = httpx.AsyncClient(
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": os.getenv("OPENROUTER_REFERER", "https://ghl-mcp-app.com"),
                "X-Title": "GoHighLevel MCP Assistant"
            },
            timeout=60.0
        )
    
    async def chat_completion(
        self,
        messages: List[ChatMessage],
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        stream: bool = False
    ) -> OpenRouterResponse:
        """
        Send chat completion request to OpenRouter
        
        Args:
            messages: List of chat messages
            system_prompt: Optional system prompt
            temperature: Response randomness (0.0 to 1.0)
            stream: Whether to stream the response
            
        Returns:
            OpenRouterResponse with the AI response
        """
        try:
            # Prepare messages
            formatted_messages = []
            
            # Add system prompt if provided
            if system_prompt:
                formatted_messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            
            # Add conversation messages
            for msg in messages:
                formatted_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
            
            # Prepare request payload
            payload = {
                "model": self.model,
                "messages": formatted_messages,
                "max_tokens": self.max_tokens,
                "temperature": temperature,
                "stream": stream
            }
            
            logger.info(f"Sending request to OpenRouter with model: {self.model}")
            
            # Send request
            response = await self.client.post(
                f"{self.base_url}/chat/completions",
                json=payload
            )
            
            response.raise_for_status()
            result = response.json()
            
            # Extract response content
            if "choices" in result and len(result["choices"]) > 0:
                content = result["choices"][0]["message"]["content"]
                usage = result.get("usage", {})
                
                return OpenRouterResponse(
                    content=content,
                    usage=usage,
                    model=result.get("model", self.model)
                )
            else:
                raise ValueError("Invalid response format from OpenRouter")
                
        except httpx.HTTPStatusError as e:
            logger.error(f"OpenRouter API error: {e.response.status_code} - {e.response.text}")
            raise Exception(f"OpenRouter API error: {e.response.status_code}")
        except Exception as e:
            logger.error(f"Error in OpenRouter chat completion: {str(e)}")
            raise
    
    async def chat_completion_stream(
        self,
        messages: List[ChatMessage],
        system_prompt: Optional[str] = None,
        temperature: float = 0.7
    ) -> AsyncGenerator[str, None]:
        """
        Stream chat completion from OpenRouter
        
        Args:
            messages: List of chat messages
            system_prompt: Optional system prompt
            temperature: Response randomness
            
        Yields:
            Chunks of the AI response as they arrive
        """
        try:
            # Prepare messages (same as above)
            formatted_messages = []
            
            if system_prompt:
                formatted_messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            
            for msg in messages:
                formatted_messages.append({
                    "role": msg.role,
                    "content": msg.content
                })
            
            payload = {
                "model": self.model,
                "messages": formatted_messages,
                "max_tokens": self.max_tokens,
                "temperature": temperature,
                "stream": True
            }
            
            # Stream request
            async with self.client.stream(
                "POST",
                f"{self.base_url}/chat/completions",
                json=payload
            ) as response:
                response.raise_for_status()
                
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        data = line[6:]  # Remove "data: " prefix
                        
                        if data == "[DONE]":
                            break
                        
                        try:
                            chunk = json.loads(data)
                            if "choices" in chunk and len(chunk["choices"]) > 0:
                                delta = chunk["choices"][0].get("delta", {})
                                if "content" in delta:
                                    yield delta["content"]
                        except json.JSONDecodeError:
                            continue
                            
        except Exception as e:
            logger.error(f"Error in OpenRouter streaming: {str(e)}")
            raise
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()
    
    def get_system_prompt(self, user_context: Dict[str, Any]) -> str:
        """
        Generate system prompt based on user context
        
        Args:
            user_context: User information and context
            
        Returns:
            System prompt for the AI assistant
        """
        location_id = user_context.get("locationId", "")
        company_id = user_context.get("companyId", "")
        user_name = user_context.get("userName", "User")
        user_type = user_context.get("type", "location")
        
        return f"""You are an AI assistant for GoHighLevel CRM. You help users manage their CRM data through natural language conversations.

User Context:
- Name: {user_name}
- Type: {user_type}
- Company ID: {company_id}
- Location ID: {location_id}

You have access to 115 comprehensive tools that cover 100% of GoHighLevel API v2 endpoints including:
- Contact management (create, update, search, tasks, notes)
- Conversations and messaging (SMS, email, WhatsApp)
- Opportunities and sales pipeline management
- Calendar and appointment scheduling
- Business and user management
- Campaign and workflow operations
- Product and payment processing
- Location management and settings

Guidelines:
1. Be conversational and helpful
2. When users ask for data, execute the appropriate tools and present results clearly
3. When users want to create or update data, confirm details before executing
4. Provide actionable insights based on the data
5. Suggest relevant follow-up actions
6. If you need more information to complete a task, ask clarifying questions
7. Format responses with clear structure (lists, tables when appropriate)
8. Always maintain user context throughout the conversation

Remember: You can execute actions in the background using the available tools. Always explain what you're doing and provide clear, useful responses."""
