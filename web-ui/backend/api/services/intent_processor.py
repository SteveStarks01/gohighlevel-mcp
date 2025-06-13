"""
Intent Processor Service
Processes natural language input and maps to MCP tool intents
"""

import re
import logging
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import json

logger = logging.getLogger(__name__)


class IntentProcessor:
    """Processes user input to identify intents and extract parameters"""
    
    def __init__(self):
        self.intent_patterns = self._load_intent_patterns()
        self.entity_extractors = self._load_entity_extractors()
    
    def _load_intent_patterns(self) -> Dict[str, List[str]]:
        """Load regex patterns for intent recognition"""
        return {
            # Contact Management
            "show_contacts": [
                r"show\s+(me\s+)?(my\s+)?contacts",
                r"list\s+(my\s+)?contacts",
                r"get\s+(my\s+)?contacts",
                r"view\s+(my\s+)?contacts",
                r"contacts\s+list",
                r"all\s+contacts"
            ],
            "create_contact": [
                r"create\s+(a\s+)?(new\s+)?contact",
                r"add\s+(a\s+)?(new\s+)?contact",
                r"new\s+contact",
                r"make\s+(a\s+)?contact"
            ],
            "search_contacts": [
                r"search\s+(for\s+)?contacts",
                r"find\s+contacts?",
                r"look\s+for\s+contacts?",
                r"contacts?\s+with",
                r"contacts?\s+named",
                r"contacts?\s+called"
            ],
            
            # Conversations & Messaging
            "show_conversations": [
                r"show\s+(me\s+)?(my\s+)?conversations",
                r"list\s+(my\s+)?conversations",
                r"get\s+(my\s+)?conversations",
                r"view\s+(my\s+)?conversations",
                r"messages?",
                r"chats?"
            ],
            "send_message": [
                r"send\s+(a\s+)?message",
                r"send\s+(an\s+)?sms",
                r"send\s+(an\s+)?email",
                r"message\s+",
                r"text\s+",
                r"email\s+"
            ],
            
            # Opportunities
            "show_opportunities": [
                r"show\s+(me\s+)?(my\s+)?opportunities",
                r"list\s+(my\s+)?opportunities",
                r"get\s+(my\s+)?opportunities",
                r"view\s+(my\s+)?opportunities",
                r"opportunities",
                r"deals?",
                r"sales?"
            ],
            "create_opportunity": [
                r"create\s+(a\s+)?(new\s+)?opportunity",
                r"add\s+(a\s+)?(new\s+)?opportunity",
                r"new\s+opportunity",
                r"create\s+(a\s+)?(new\s+)?deal"
            ],
            "show_pipeline": [
                r"show\s+(me\s+)?(my\s+)?pipeline",
                r"view\s+(my\s+)?pipeline",
                r"pipeline\s+status",
                r"sales\s+pipeline",
                r"pipeline"
            ],
            
            # Calendar & Appointments
            "show_appointments": [
                r"show\s+(me\s+)?(my\s+)?appointments",
                r"list\s+(my\s+)?appointments",
                r"get\s+(my\s+)?appointments",
                r"view\s+(my\s+)?appointments",
                r"appointments?",
                r"schedule",
                r"calendar",
                r"today'?s?\s+appointments",
                r"tomorrow'?s?\s+appointments"
            ],
            "create_appointment": [
                r"create\s+(a\s+)?(new\s+)?appointment",
                r"schedule\s+(a\s+)?(new\s+)?appointment",
                r"book\s+(a\s+)?(new\s+)?appointment",
                r"add\s+(a\s+)?(new\s+)?appointment",
                r"new\s+appointment"
            ],
            
            # Analytics & Dashboard
            "show_analytics": [
                r"show\s+(me\s+)?(my\s+)?analytics",
                r"dashboard",
                r"overview",
                r"summary",
                r"stats?",
                r"metrics",
                r"kpis?",
                r"performance"
            ],
            
            # Business Management
            "show_businesses": [
                r"show\s+(me\s+)?(my\s+)?businesses",
                r"list\s+(my\s+)?businesses",
                r"businesses",
                r"companies"
            ],
            "show_users": [
                r"show\s+(me\s+)?(my\s+)?users",
                r"list\s+(my\s+)?users",
                r"users",
                r"team\s+members?",
                r"staff"
            ],
            
            # Products & Payments
            "show_products": [
                r"show\s+(me\s+)?(my\s+)?products",
                r"list\s+(my\s+)?products",
                r"products",
                r"catalog"
            ],
            "show_payments": [
                r"show\s+(me\s+)?(my\s+)?payments",
                r"list\s+(my\s+)?payments",
                r"payments?",
                r"transactions?",
                r"orders?"
            ]
        }
    
    def _load_entity_extractors(self) -> Dict[str, str]:
        """Load regex patterns for entity extraction"""
        return {
            "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "phone": r"\b(?:\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})\b",
            "name": r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b",
            "date": r"\b(?:today|tomorrow|yesterday|\d{1,2}[/-]\d{1,2}[/-]\d{2,4})\b",
            "time": r"\b(?:1[0-2]|0?[1-9]):[0-5][0-9]\s*(?:AM|PM|am|pm)\b",
            "money": r"\$\d+(?:,\d{3})*(?:\.\d{2})?",
            "number": r"\b\d+\b"
        }
    
    def process_input(self, user_input: str) -> Tuple[Optional[str], Dict[str, Any]]:
        """
        Process user input to identify intent and extract parameters
        
        Args:
            user_input: Natural language input from user
            
        Returns:
            Tuple of (intent, parameters)
        """
        user_input_lower = user_input.lower().strip()
        
        # Identify intent
        intent = self._identify_intent(user_input_lower)
        
        # Extract parameters
        parameters = self._extract_parameters(user_input, intent)
        
        logger.info(f"Processed input: '{user_input}' -> Intent: {intent}, Parameters: {parameters}")
        
        return intent, parameters
    
    def _identify_intent(self, user_input: str) -> Optional[str]:
        """Identify the intent from user input"""
        
        # Score each intent based on pattern matches
        intent_scores = {}
        
        for intent, patterns in self.intent_patterns.items():
            score = 0
            for pattern in patterns:
                if re.search(pattern, user_input, re.IGNORECASE):
                    score += 1
            
            if score > 0:
                intent_scores[intent] = score
        
        # Return the highest scoring intent
        if intent_scores:
            return max(intent_scores, key=intent_scores.get)
        
        return None
    
    def _extract_parameters(self, user_input: str, intent: Optional[str]) -> Dict[str, Any]:
        """Extract parameters from user input based on intent"""
        parameters = {}
        
        # Extract common entities
        for entity_type, pattern in self.entity_extractors.items():
            matches = re.findall(pattern, user_input, re.IGNORECASE)
            if matches:
                if entity_type == "phone":
                    # Format phone number
                    parameters[entity_type] = "".join(matches[0]) if isinstance(matches[0], tuple) else matches[0]
                else:
                    parameters[entity_type] = matches[0]
        
        # Intent-specific parameter extraction
        if intent:
            if intent in ["create_contact", "search_contacts"]:
                # Extract contact-specific parameters
                parameters.update(self._extract_contact_parameters(user_input))
            
            elif intent in ["send_message"]:
                # Extract message-specific parameters
                parameters.update(self._extract_message_parameters(user_input))
            
            elif intent in ["create_appointment", "show_appointments"]:
                # Extract appointment-specific parameters
                parameters.update(self._extract_appointment_parameters(user_input))
            
            elif intent in ["create_opportunity"]:
                # Extract opportunity-specific parameters
                parameters.update(self._extract_opportunity_parameters(user_input))
        
        return parameters
    
    def _extract_contact_parameters(self, user_input: str) -> Dict[str, Any]:
        """Extract contact-specific parameters"""
        params = {}
        
        # Extract first and last name
        name_match = re.search(r"(?:for|named|called)\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)", user_input, re.IGNORECASE)
        if name_match:
            full_name = name_match.group(1)
            name_parts = full_name.split()
            if len(name_parts) >= 2:
                params["first_name"] = name_parts[0]
                params["last_name"] = " ".join(name_parts[1:])
            else:
                params["first_name"] = full_name
        
        # Extract company
        company_match = re.search(r"(?:company|from)\s+([A-Z][a-zA-Z\s]+)", user_input, re.IGNORECASE)
        if company_match:
            params["company_name"] = company_match.group(1).strip()
        
        return params
    
    def _extract_message_parameters(self, user_input: str) -> Dict[str, Any]:
        """Extract message-specific parameters"""
        params = {}
        
        # Determine message type
        if re.search(r"\bsms\b|\btext\b", user_input, re.IGNORECASE):
            params["message_type"] = "SMS"
        elif re.search(r"\bemail\b", user_input, re.IGNORECASE):
            params["message_type"] = "Email"
        else:
            params["message_type"] = "SMS"  # Default
        
        # Extract message content
        message_match = re.search(r"(?:saying|message|text)[\s:]+[\"']?([^\"']+)[\"']?", user_input, re.IGNORECASE)
        if message_match:
            params["message"] = message_match.group(1).strip()
        
        return params
    
    def _extract_appointment_parameters(self, user_input: str) -> Dict[str, Any]:
        """Extract appointment-specific parameters"""
        params = {}
        
        # Extract date context
        if re.search(r"\btoday\b", user_input, re.IGNORECASE):
            params["date_filter"] = "today"
        elif re.search(r"\btomorrow\b", user_input, re.IGNORECASE):
            params["date_filter"] = "tomorrow"
        elif re.search(r"\bthis\s+week\b", user_input, re.IGNORECASE):
            params["date_filter"] = "this_week"
        
        return params
    
    def _extract_opportunity_parameters(self, user_input: str) -> Dict[str, Any]:
        """Extract opportunity-specific parameters"""
        params = {}
        
        # Extract opportunity name
        name_match = re.search(r"(?:for|named|called)\s+([A-Z][a-zA-Z\s]+)", user_input, re.IGNORECASE)
        if name_match:
            params["name"] = name_match.group(1).strip()
        
        # Extract monetary value
        money_match = re.search(r"\$(\d+(?:,\d{3})*(?:\.\d{2})?)", user_input)
        if money_match:
            params["monetary_value"] = float(money_match.group(1).replace(",", ""))
        
        return params
