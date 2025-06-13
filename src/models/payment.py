"""Payment models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class PaymentOrderContactSnapshot(BaseModel):
    """Payment order contact snapshot model"""
    
    id: Optional[str] = None
    locationId: Optional[str] = None
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    country: Optional[str] = None
    companyName: Optional[str] = None
    source: Optional[str] = None
    dateAdded: Optional[datetime] = None
    dateOfBirth: Optional[str] = None
    dnd: Optional[bool] = None
    tags: Optional[List[str]] = None
    website: Optional[str] = None
    attachments: Optional[List[Any]] = None
    assignedTo: Optional[str] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderAmountSummary(BaseModel):
    """Payment order amount summary model"""
    
    subtotal: Optional[float] = None
    discount: Optional[float] = None
    tax: Optional[float] = None
    shipping: Optional[float] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderTaxSummary(BaseModel):
    """Payment order tax summary model"""
    
    id: Optional[str] = Field(None, alias="_id")
    name: str
    calculation: str  # e.g., "exclusive"
    rate: float
    amount: float
    
    model_config = {"populate_by_name": True}


class PaymentOrderSource(BaseModel):
    """Payment order source model"""
    
    id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None  # e.g., "website"
    subType: Optional[str] = None  # e.g., "store"
    meta: Optional[Dict[str, Any]] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderItemPrice(BaseModel):
    """Payment order item price model"""
    
    id: Optional[str] = Field(None, alias="_id")
    name: Optional[str] = None
    type: Optional[str] = None  # e.g., "one_time"
    currency: Optional[str] = None
    amount: Optional[float] = None
    variantOptionIds: Optional[List[str]] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderItemProduct(BaseModel):
    """Payment order item product model"""
    
    id: Optional[str] = Field(None, alias="_id")
    name: str
    description: Optional[str] = None
    availableInStore: Optional[bool] = None
    taxes: Optional[List[Dict[str, Any]]] = None
    variants: Optional[List[Dict[str, Any]]] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderItem(BaseModel):
    """Payment order item model"""
    
    name: str
    qty: int
    product: Optional[PaymentOrderItemProduct] = None
    price: Optional[PaymentOrderItemPrice] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrder(BaseModel):
    """GoHighLevel Payment Order model"""
    
    id: Optional[str] = Field(None, alias="_id")
    type: Optional[str] = None
    altId: Optional[str] = None
    altType: Optional[str] = None
    contactId: Optional[str] = None
    contactSnapshot: Optional[PaymentOrderContactSnapshot] = None
    status: Optional[str] = None  # e.g., "completed", "pending"
    fulfillmentStatus: Optional[str] = None  # e.g., "unfulfilled", "fulfilled"
    currency: Optional[str] = None
    amount: Optional[float] = None
    liveMode: Optional[bool] = None
    items: Optional[List[PaymentOrderItem]] = None
    amountSummary: Optional[PaymentOrderAmountSummary] = None
    taxSummary: Optional[List[PaymentOrderTaxSummary]] = None
    source: Optional[PaymentOrderSource] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderList(BaseModel):
    """Model for payment order list response"""
    
    orders: List[PaymentOrder]
    count: int
    total: Optional[int] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderFulfillment(BaseModel):
    """Payment order fulfillment model"""
    
    id: Optional[str] = Field(None, alias="_id")
    orderId: Optional[str] = None
    trackingNumber: Optional[str] = None
    trackingUrl: Optional[str] = None
    carrier: Optional[str] = None
    status: Optional[str] = None
    items: Optional[List[Dict[str, Any]]] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderFulfillmentList(BaseModel):
    """Model for payment order fulfillment list response"""
    
    fulfillments: List[PaymentOrderFulfillment]
    count: int
    total: Optional[int] = None
    
    model_config = {"populate_by_name": True}


class PaymentOrderFulfillmentCreate(BaseModel):
    """Model for creating a payment order fulfillment"""

    trackingNumber: Optional[str] = Field(None, description="Tracking number for the fulfillment")
    trackingUrl: Optional[str] = Field(None, description="Tracking URL for the fulfillment")
    carrier: Optional[str] = Field(None, description="Shipping carrier")
    items: Optional[List[Dict[str, Any]]] = Field(None, description="Items being fulfilled")
    notify: Optional[bool] = Field(None, description="Whether to notify the customer")


class PaymentSubscription(BaseModel):
    """Payment subscription model"""

    id: str = Field(..., description="Subscription ID", alias="_id")
    locationId: Optional[str] = Field(None, description="Location ID")
    contactId: Optional[str] = Field(None, description="Contact ID")
    productId: Optional[str] = Field(None, description="Product ID")
    priceId: Optional[str] = Field(None, description="Price ID")
    status: Optional[str] = Field(None, description="Subscription status")
    currency: Optional[str] = Field(None, description="Currency code")
    amount: Optional[float] = Field(None, description="Subscription amount")
    interval: Optional[str] = Field(None, description="Billing interval")
    intervalCount: Optional[int] = Field(None, description="Interval count")
    trialPeriodDays: Optional[int] = Field(None, description="Trial period in days")
    currentPeriodStart: Optional[str] = Field(None, description="Current period start date")
    currentPeriodEnd: Optional[str] = Field(None, description="Current period end date")
    canceledAt: Optional[str] = Field(None, description="Cancellation date")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")

    model_config = {"populate_by_name": True}


class PaymentSubscriptionList(BaseModel):
    """List of payment subscriptions"""

    subscriptions: List[PaymentSubscription] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}


class PaymentTransaction(BaseModel):
    """Payment transaction model"""

    id: str = Field(..., description="Transaction ID", alias="_id")
    locationId: Optional[str] = Field(None, description="Location ID")
    contactId: Optional[str] = Field(None, description="Contact ID")
    orderId: Optional[str] = Field(None, description="Order ID")
    subscriptionId: Optional[str] = Field(None, description="Subscription ID")
    type: Optional[str] = Field(None, description="Transaction type")
    status: Optional[str] = Field(None, description="Transaction status")
    currency: Optional[str] = Field(None, description="Currency code")
    amount: Optional[float] = Field(None, description="Transaction amount")
    fee: Optional[float] = Field(None, description="Transaction fee")
    netAmount: Optional[float] = Field(None, description="Net amount after fees")
    paymentMethod: Optional[str] = Field(None, description="Payment method")
    gateway: Optional[str] = Field(None, description="Payment gateway")
    gatewayTransactionId: Optional[str] = Field(None, description="Gateway transaction ID")
    description: Optional[str] = Field(None, description="Transaction description")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")

    model_config = {"populate_by_name": True}


class PaymentTransactionList(BaseModel):
    """List of payment transactions"""

    transactions: List[PaymentTransaction] = Field(default_factory=list)
    count: int = Field(default=0)
    total: int = Field(default=0)

    model_config = {"populate_by_name": True}


class PaymentIntegration(BaseModel):
    """Payment integration model"""

    id: Optional[str] = Field(None, description="Integration ID", alias="_id")
    locationId: Optional[str] = Field(None, description="Location ID")
    provider: Optional[str] = Field(None, description="Payment provider")
    type: Optional[str] = Field(None, description="Integration type")
    status: Optional[str] = Field(None, description="Integration status")
    isActive: Optional[bool] = Field(None, description="Whether integration is active")
    configuration: Optional[Dict[str, Any]] = Field(None, description="Integration configuration")
    credentials: Optional[Dict[str, Any]] = Field(None, description="Integration credentials")
    webhookUrl: Optional[str] = Field(None, description="Webhook URL")
    supportedMethods: Optional[List[str]] = Field(None, description="Supported payment methods")
    createdAt: Optional[datetime] = Field(None, description="Creation date")
    updatedAt: Optional[datetime] = Field(None, description="Last update date")

    model_config = {"populate_by_name": True}


class PaymentIntegrationCreate(BaseModel):
    """Model for creating a payment integration"""

    provider: str = Field(..., description="Payment provider name")
    configuration: Dict[str, Any] = Field(..., description="Integration configuration")
    credentials: Optional[Dict[str, Any]] = Field(None, description="Integration credentials")
    webhookUrl: Optional[str] = Field(None, description="Webhook URL")
    isActive: Optional[bool] = Field(True, description="Whether integration should be active")
