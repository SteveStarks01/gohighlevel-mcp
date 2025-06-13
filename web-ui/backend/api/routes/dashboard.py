"""
Dashboard Routes
Provides data for the dashboard interface
"""

import logging
from typing import Dict, Any
from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime, timedelta

from ..services.mcp_bridge import MCPBridge
from ..models.user import UserContext

logger = logging.getLogger(__name__)

router = APIRouter()


async def get_user_context() -> Dict[str, Any]:
    """Get current user context (mock for now)"""
    # TODO: Get from session/database
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


@router.get("/overview")
async def get_dashboard_overview(
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """
    Get dashboard overview with key metrics
    
    Returns KPIs and summary data for the dashboard
    """
    try:
        # TODO: Get MCP bridge from dependency injection
        # For now, return mock data
        
        mock_data = {
            "success": True,
            "data": {
                "kpis": {
                    "total_contacts": 1247,
                    "total_opportunities": 89,
                    "total_opportunity_value": 245000,
                    "appointments_today": 12,
                    "active_campaigns": 5,
                    "conversion_rate": 23.5
                },
                "recent_activity": [
                    {
                        "type": "contact_created",
                        "description": "New contact: John Smith",
                        "timestamp": datetime.utcnow().isoformat(),
                        "icon": "user-plus"
                    },
                    {
                        "type": "opportunity_updated",
                        "description": "Opportunity moved to 'Proposal' stage",
                        "timestamp": (datetime.utcnow() - timedelta(minutes=15)).isoformat(),
                        "icon": "trending-up"
                    },
                    {
                        "type": "appointment_scheduled",
                        "description": "Appointment scheduled for tomorrow",
                        "timestamp": (datetime.utcnow() - timedelta(minutes=30)).isoformat(),
                        "icon": "calendar"
                    }
                ],
                "pipeline_summary": {
                    "stages": [
                        {"name": "Lead", "count": 25, "value": 50000},
                        {"name": "Qualified", "count": 18, "value": 75000},
                        {"name": "Proposal", "count": 12, "value": 85000},
                        {"name": "Closed Won", "count": 8, "value": 35000}
                    ]
                },
                "upcoming_appointments": [
                    {
                        "id": "apt_1",
                        "title": "Sales Call with ABC Corp",
                        "contact": "Jane Doe",
                        "time": "2024-01-15T10:00:00Z",
                        "duration": 60
                    },
                    {
                        "id": "apt_2",
                        "title": "Product Demo",
                        "contact": "Mike Johnson",
                        "time": "2024-01-15T14:30:00Z",
                        "duration": 30
                    }
                ]
            },
            "timestamp": datetime.utcnow().isoformat()
        }
        
        return mock_data
        
    except Exception as e:
        logger.error(f"Error getting dashboard overview: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get dashboard data")


@router.get("/contacts/summary")
async def get_contacts_summary(
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """Get contacts summary data"""
    try:
        # Mock data for contacts summary
        return {
            "success": True,
            "data": {
                "total_contacts": 1247,
                "new_this_week": 23,
                "new_this_month": 89,
                "by_source": [
                    {"source": "Website", "count": 456},
                    {"source": "Referral", "count": 234},
                    {"source": "Social Media", "count": 189},
                    {"source": "Direct", "count": 368}
                ],
                "recent_contacts": [
                    {
                        "id": "contact_1",
                        "name": "John Smith",
                        "email": "john@example.com",
                        "phone": "+1-555-0123",
                        "created_at": datetime.utcnow().isoformat(),
                        "source": "Website"
                    },
                    {
                        "id": "contact_2",
                        "name": "Sarah Johnson",
                        "email": "sarah@example.com",
                        "phone": "+1-555-0124",
                        "created_at": (datetime.utcnow() - timedelta(hours=2)).isoformat(),
                        "source": "Referral"
                    }
                ]
            }
        }
        
    except Exception as e:
        logger.error(f"Error getting contacts summary: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get contacts summary")


@router.get("/opportunities/summary")
async def get_opportunities_summary(
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """Get opportunities summary data"""
    try:
        # Mock data for opportunities summary
        return {
            "success": True,
            "data": {
                "total_opportunities": 89,
                "total_value": 245000,
                "won_this_month": 12,
                "won_value_this_month": 45000,
                "pipeline_health": {
                    "conversion_rate": 23.5,
                    "average_deal_size": 2753,
                    "average_sales_cycle": 45
                },
                "by_stage": [
                    {"stage": "Lead", "count": 25, "value": 50000},
                    {"stage": "Qualified", "count": 18, "value": 75000},
                    {"stage": "Proposal", "count": 12, "value": 85000},
                    {"stage": "Negotiation", "count": 6, "value": 35000}
                ]
            }
        }
        
    except Exception as e:
        logger.error(f"Error getting opportunities summary: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get opportunities summary")


@router.get("/calendar/summary")
async def get_calendar_summary(
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """Get calendar summary data"""
    try:
        # Mock data for calendar summary
        return {
            "success": True,
            "data": {
                "appointments_today": 12,
                "appointments_this_week": 45,
                "appointments_next_week": 38,
                "total_scheduled": 156,
                "upcoming_appointments": [
                    {
                        "id": "apt_1",
                        "title": "Sales Call",
                        "contact": "John Smith",
                        "time": "2024-01-15T10:00:00Z",
                        "duration": 60,
                        "type": "sales_call"
                    },
                    {
                        "id": "apt_2",
                        "title": "Product Demo",
                        "contact": "Sarah Johnson",
                        "time": "2024-01-15T14:30:00Z",
                        "duration": 30,
                        "type": "demo"
                    }
                ],
                "calendar_utilization": {
                    "this_week": 78,
                    "next_week": 65,
                    "average": 72
                }
            }
        }
        
    except Exception as e:
        logger.error(f"Error getting calendar summary: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get calendar summary")


@router.get("/analytics/chart-data")
async def get_chart_data(
    chart_type: str,
    period: str = "30d",
    user_context: Dict[str, Any] = Depends(get_user_context)
):
    """Get chart data for dashboard visualizations"""
    try:
        # Mock chart data based on type
        if chart_type == "contacts_growth":
            return {
                "success": True,
                "data": {
                    "labels": ["Week 1", "Week 2", "Week 3", "Week 4"],
                    "datasets": [{
                        "label": "New Contacts",
                        "data": [23, 31, 28, 35],
                        "borderColor": "rgb(59, 130, 246)",
                        "backgroundColor": "rgba(59, 130, 246, 0.1)"
                    }]
                }
            }
        elif chart_type == "pipeline_value":
            return {
                "success": True,
                "data": {
                    "labels": ["Lead", "Qualified", "Proposal", "Negotiation", "Closed Won"],
                    "datasets": [{
                        "label": "Pipeline Value",
                        "data": [50000, 75000, 85000, 35000, 45000],
                        "backgroundColor": [
                            "rgba(239, 68, 68, 0.8)",
                            "rgba(245, 158, 11, 0.8)",
                            "rgba(59, 130, 246, 0.8)",
                            "rgba(16, 185, 129, 0.8)",
                            "rgba(34, 197, 94, 0.8)"
                        ]
                    }]
                }
            }
        else:
            return {
                "success": False,
                "error": f"Unknown chart type: {chart_type}"
            }
            
    except Exception as e:
        logger.error(f"Error getting chart data: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to get chart data")
