"""Product models for GoHighLevel MCP integration"""

from typing import Optional, List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field


class ProductVariantOption(BaseModel):
    """Product variant option model"""
    
    id: Optional[str] = None
    name: str
    
    model_config = {"populate_by_name": True}


class ProductVariant(BaseModel):
    """Product variant model"""
    
    id: Optional[str] = None
    name: str
    options: Optional[List[ProductVariantOption]] = None
    
    model_config = {"populate_by_name": True}


class ProductMedia(BaseModel):
    """Product media model"""
    
    id: Optional[str] = None
    title: Optional[str] = None
    url: str
    type: str  # e.g., "image"
    isFeatured: Optional[bool] = None
    
    model_config = {"populate_by_name": True}


class Product(BaseModel):
    """GoHighLevel Product model"""
    
    id: Optional[str] = Field(None, alias="_id")
    locationId: Optional[str] = None
    name: str
    description: Optional[str] = None
    productType: Optional[str] = None  # e.g., "PHYSICAL"
    availableInStore: Optional[bool] = None
    userId: Optional[str] = None
    variants: Optional[List[ProductVariant]] = None
    medias: Optional[List[ProductMedia]] = None
    image: Optional[str] = None
    statementDescriptor: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
    model_config = {"populate_by_name": True}


class ProductCreate(BaseModel):
    """Model for creating a product"""
    
    locationId: str = Field(..., description="Location ID where the product will be created")
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    productType: Optional[str] = Field(None, description="Product type (e.g., PHYSICAL, DIGITAL)")
    availableInStore: Optional[bool] = Field(None, description="Whether product is available in store")
    variants: Optional[List[Dict[str, Any]]] = Field(None, description="Product variants")
    medias: Optional[List[Dict[str, Any]]] = Field(None, description="Product media files")
    image: Optional[str] = Field(None, description="Product image URL")
    statementDescriptor: Optional[str] = Field(None, description="Statement descriptor for payments")


class ProductUpdate(BaseModel):
    """Model for updating a product"""
    
    name: Optional[str] = Field(None, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    productType: Optional[str] = Field(None, description="Product type (e.g., PHYSICAL, DIGITAL)")
    availableInStore: Optional[bool] = Field(None, description="Whether product is available in store")
    variants: Optional[List[Dict[str, Any]]] = Field(None, description="Product variants")
    medias: Optional[List[Dict[str, Any]]] = Field(None, description="Product media files")
    image: Optional[str] = Field(None, description="Product image URL")
    statementDescriptor: Optional[str] = Field(None, description="Statement descriptor for payments")


class ProductList(BaseModel):
    """Model for product list response"""

    products: List[Product]
    count: int
    total: Optional[int] = None

    model_config = {"populate_by_name": True}


# Product Price Models

class ProductPriceMembershipOffer(BaseModel):
    """Product price membership offer model"""

    id: Optional[str] = Field(None, alias="_id")
    label: str
    value: str

    model_config = {"populate_by_name": True}


class ProductPriceRecurring(BaseModel):
    """Product price recurring model"""

    interval: str  # e.g., "day", "week", "month", "year"
    intervalCount: int

    model_config = {"populate_by_name": True}


class ProductPrice(BaseModel):
    """GoHighLevel Product Price model"""

    id: Optional[str] = Field(None, alias="_id")
    locationId: Optional[str] = None
    product: str  # Product ID
    userId: Optional[str] = None
    name: str
    type: str  # e.g., "one_time", "recurring"
    currency: str  # e.g., "USD", "INR"
    amount: int  # Amount in cents
    membershipOffers: Optional[List[ProductPriceMembershipOffer]] = None
    variantOptionIds: Optional[List[str]] = None
    recurring: Optional[ProductPriceRecurring] = None
    compareAtPrice: Optional[int] = None
    trackInventory: Optional[bool] = None
    availableQuantity: Optional[int] = None
    allowOutOfStockPurchases: Optional[bool] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

    model_config = {"populate_by_name": True}


class ProductPriceCreate(BaseModel):
    """Model for creating a product price"""

    name: str = Field(..., description="Price name")
    type: str = Field(..., description="Price type (one_time, recurring)")
    currency: str = Field(..., description="Currency code (USD, EUR, etc.)")
    amount: int = Field(..., description="Amount in cents")
    membershipOffers: Optional[List[Dict[str, Any]]] = Field(None, description="Membership offers")
    variantOptionIds: Optional[List[str]] = Field(None, description="Variant option IDs")
    recurring: Optional[Dict[str, Any]] = Field(None, description="Recurring payment details")
    compareAtPrice: Optional[int] = Field(None, description="Compare at price in cents")
    trackInventory: Optional[bool] = Field(None, description="Whether to track inventory")
    availableQuantity: Optional[int] = Field(None, description="Available quantity")
    allowOutOfStockPurchases: Optional[bool] = Field(None, description="Allow out of stock purchases")


class ProductPriceUpdate(BaseModel):
    """Model for updating a product price"""

    name: Optional[str] = Field(None, description="Price name")
    type: Optional[str] = Field(None, description="Price type (one_time, recurring)")
    currency: Optional[str] = Field(None, description="Currency code (USD, EUR, etc.)")
    amount: Optional[int] = Field(None, description="Amount in cents")
    membershipOffers: Optional[List[Dict[str, Any]]] = Field(None, description="Membership offers")
    variantOptionIds: Optional[List[str]] = Field(None, description="Variant option IDs")
    recurring: Optional[Dict[str, Any]] = Field(None, description="Recurring payment details")
    compareAtPrice: Optional[int] = Field(None, description="Compare at price in cents")
    trackInventory: Optional[bool] = Field(None, description="Whether to track inventory")
    availableQuantity: Optional[int] = Field(None, description="Available quantity")
    allowOutOfStockPurchases: Optional[bool] = Field(None, description="Allow out of stock purchases")


class ProductPriceList(BaseModel):
    """Model for product price list response"""

    prices: List[ProductPrice]
    count: int
    total: Optional[int] = None

    model_config = {"populate_by_name": True}
