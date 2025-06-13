"""Payment parameter classes for MCP tools"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class GetPaymentOrdersParams(BaseModel):
    """Parameters for getting payment orders"""

    location_id: str = Field(..., description="The location ID to get payment orders for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetPaymentOrderParams(BaseModel):
    """Parameters for getting a single payment order"""

    order_id: str = Field(..., description="The payment order ID to retrieve")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetOrderFulfillmentsParams(BaseModel):
    """Parameters for getting order fulfillments"""

    order_id: str = Field(..., description="The payment order ID to get fulfillments for")
    location_id: str = Field(..., description="The location ID")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateOrderFulfillmentParams(BaseModel):
    """Parameters for creating an order fulfillment"""

    order_id: str = Field(..., description="The payment order ID to create fulfillment for")
    location_id: str = Field(..., description="The location ID")
    tracking_number: Optional[str] = Field(None, description="Tracking number for the fulfillment")
    tracking_url: Optional[str] = Field(None, description="Tracking URL for the fulfillment")
    carrier: Optional[str] = Field(None, description="Shipping carrier")
    items: Optional[List[Dict[str, Any]]] = Field(None, description="Items being fulfilled")
    notify: Optional[bool] = Field(None, description="Whether to notify the customer")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetPaymentSubscriptionsParams(BaseModel):
    """Parameters for getting payment subscriptions"""

    location_id: str = Field(..., description="The location ID to get payment subscriptions for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetPaymentSubscriptionParams(BaseModel):
    """Parameters for getting a single payment subscription"""

    subscription_id: str = Field(..., description="The payment subscription ID to retrieve")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetPaymentTransactionsParams(BaseModel):
    """Parameters for getting payment transactions"""

    location_id: str = Field(..., description="The location ID to get payment transactions for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetPaymentTransactionParams(BaseModel):
    """Parameters for getting a single payment transaction"""

    transaction_id: str = Field(..., description="The payment transaction ID to retrieve")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetPaymentIntegrationParams(BaseModel):
    """Parameters for getting payment integration"""

    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreatePaymentIntegrationParams(BaseModel):
    """Parameters for creating a payment integration"""

    location_id: str = Field(..., description="The location ID")
    provider: str = Field(..., description="Payment provider name")
    configuration: Dict[str, Any] = Field(..., description="Integration configuration")
    credentials: Optional[Dict[str, Any]] = Field(None, description="Integration credentials")
    webhook_url: Optional[str] = Field(None, description="Webhook URL")
    is_active: Optional[bool] = Field(True, description="Whether integration should be active")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
