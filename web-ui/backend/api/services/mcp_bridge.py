"""
MCP Bridge Service
Bridges the web interface with the existing MCP tools
"""

import logging
import json
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime

# Import existing MCP client
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src'))

from src.api.client import GoHighLevelClient

logger = logging.getLogger(__name__)


class MCPBridge:
    """Bridge between web interface and MCP tools"""
    
    def __init__(self, ghl_client: GoHighLevelClient):
        self.ghl_client = ghl_client
        self.intent_mappings = self._load_intent_mappings()
    
    def _load_intent_mappings(self) -> Dict[str, Dict[str, Any]]:
        """Load intent to MCP tool mappings"""
        return {
            # Contact Management
            "show_contacts": {
                "tools": ["get_contacts"],
                "description": "Show contacts with optional filtering"
            },
            "create_contact": {
                "tools": ["create_contact"],
                "description": "Create a new contact"
            },
            "update_contact": {
                "tools": ["update_contact"],
                "description": "Update existing contact"
            },
            "search_contacts": {
                "tools": ["search_contacts"],
                "description": "Search contacts by criteria"
            },
            
            # Conversations & Messaging
            "show_conversations": {
                "tools": ["get_conversations"],
                "description": "Show conversations"
            },
            "send_message": {
                "tools": ["send_message"],
                "description": "Send SMS, email, or other message"
            },
            
            # Opportunities
            "show_opportunities": {
                "tools": ["get_opportunities"],
                "description": "Show opportunities in pipeline"
            },
            "create_opportunity": {
                "tools": ["create_opportunity"],
                "description": "Create new opportunity"
            },
            "show_pipeline": {
                "tools": ["get_pipelines"],
                "description": "Show sales pipelines"
            },
            
            # Calendar & Appointments
            "show_appointments": {
                "tools": ["get_appointments"],
                "description": "Show appointments"
            },
            "create_appointment": {
                "tools": ["create_appointment", "get_free_slots"],
                "description": "Create new appointment"
            },
            "show_calendars": {
                "tools": ["get_calendars"],
                "description": "Show available calendars"
            },
            
            # Analytics & Dashboard
            "show_analytics": {
                "tools": ["get_contacts", "get_opportunities", "get_appointments"],
                "description": "Show dashboard analytics"
            },
            
            # Business Management
            "show_businesses": {
                "tools": ["get_businesses"],
                "description": "Show businesses"
            },
            "show_users": {
                "tools": ["get_users"],
                "description": "Show users"
            },
            
            # Products & Payments
            "show_products": {
                "tools": ["get_products"],
                "description": "Show products"
            },
            "show_payments": {
                "tools": ["get_payment_orders", "get_payment_transactions"],
                "description": "Show payment information"
            }
        }
    
    async def execute_intent(
        self,
        intent: str,
        parameters: Dict[str, Any],
        user_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Execute an intent using appropriate MCP tools
        
        Args:
            intent: The identified intent
            parameters: Parameters extracted from user input
            user_context: User context (location_id, access_token, etc.)
            
        Returns:
            Result from MCP tool execution
        """
        try:
            if intent not in self.intent_mappings:
                return {
                    "success": False,
                    "error": f"Unknown intent: {intent}",
                    "data": None
                }
            
            mapping = self.intent_mappings[intent]
            tools = mapping["tools"]
            
            # Execute the primary tool
            primary_tool = tools[0]
            result = await self._execute_tool(primary_tool, parameters, user_context)
            
            return {
                "success": True,
                "intent": intent,
                "tool": primary_tool,
                "data": result,
                "timestamp": datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error executing intent {intent}: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "intent": intent,
                "data": None
            }
    
    async def _execute_tool(
        self,
        tool_name: str,
        parameters: Dict[str, Any],
        user_context: Dict[str, Any]
    ) -> Any:
        """Execute a specific MCP tool"""
        
        location_id = user_context.get("locationId")
        access_token = user_context.get("access_token")
        
        if not location_id or not access_token:
            raise ValueError("Missing location_id or access_token in user context")
        
        # Map tool names to client methods
        tool_methods = {
            # Contacts
            "get_contacts": self.ghl_client.get_contacts,
            "create_contact": self.ghl_client.create_contact,
            "update_contact": self.ghl_client.update_contact,
            "search_contacts": self.ghl_client.get_contacts,
            
            # Conversations
            "get_conversations": self.ghl_client.get_conversations,
            "send_message": self.ghl_client.send_message,
            
            # Opportunities
            "get_opportunities": self.ghl_client.get_opportunities,
            "create_opportunity": self.ghl_client.create_opportunity,
            "get_pipelines": self.ghl_client.get_pipelines,
            
            # Calendar
            "get_appointments": self.ghl_client.get_appointments,
            "create_appointment": self.ghl_client.create_appointment,
            "get_calendars": self.ghl_client.get_calendars,
            "get_free_slots": self.ghl_client.get_free_slots,
            
            # Business
            "get_businesses": self.ghl_client.get_businesses,
            "get_users": self.ghl_client.get_users,
            
            # Products
            "get_products": self.ghl_client.get_products,
            "get_payment_orders": self.ghl_client.get_payment_orders,
            "get_payment_transactions": self.ghl_client.get_payment_transactions,
        }
        
        if tool_name not in tool_methods:
            raise ValueError(f"Unknown tool: {tool_name}")
        
        method = tool_methods[tool_name]
        
        # Prepare method parameters
        method_params = {"location_id": location_id}
        method_params.update(parameters)
        
        # Execute the method
        result = await method(**method_params)
        return result
    
    async def get_dashboard_data(self, user_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get comprehensive dashboard data
        
        Args:
            user_context: User context with location_id and access_token
            
        Returns:
            Dashboard data with KPIs and metrics
        """
        try:
            location_id = user_context.get("locationId")
            
            # Fetch key metrics in parallel
            contacts_result = await self._execute_tool("get_contacts", {"limit": 100}, user_context)
            opportunities_result = await self._execute_tool("get_opportunities", {"limit": 100}, user_context)
            
            # Calculate KPIs
            total_contacts = len(contacts_result.contacts) if hasattr(contacts_result, 'contacts') else 0
            total_opportunities = len(opportunities_result.opportunities) if hasattr(opportunities_result, 'opportunities') else 0
            
            # Calculate opportunity value
            total_opportunity_value = 0
            if hasattr(opportunities_result, 'opportunities'):
                for opp in opportunities_result.opportunities:
                    if hasattr(opp, 'monetaryValue') and opp.monetaryValue:
                        total_opportunity_value += opp.monetaryValue
            
            return {
                "success": True,
                "data": {
                    "kpis": {
                        "total_contacts": total_contacts,
                        "total_opportunities": total_opportunities,
                        "total_opportunity_value": total_opportunity_value,
                        "active_campaigns": 0,  # TODO: Implement when campaigns are available
                    },
                    "recent_contacts": contacts_result.contacts[:5] if hasattr(contacts_result, 'contacts') else [],
                    "recent_opportunities": opportunities_result.opportunities[:5] if hasattr(opportunities_result, 'opportunities') else [],
                },
                "timestamp": datetime.utcnow().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Error getting dashboard data: {str(e)}")
            return {
                "success": False,
                "error": str(e),
                "data": None
            }
    
    def get_available_intents(self) -> List[Dict[str, str]]:
        """Get list of available intents"""
        return [
            {"intent": intent, "description": mapping["description"]}
            for intent, mapping in self.intent_mappings.items()
        ]
