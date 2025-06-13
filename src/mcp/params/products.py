"""Product parameter classes for MCP tools"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class GetProductsParams(BaseModel):
    """Parameters for getting products"""

    location_id: str = Field(..., description="The location ID to get products for")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetProductParams(BaseModel):
    """Parameters for getting a single product"""

    product_id: str = Field(..., description="The product ID to retrieve")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateProductParams(BaseModel):
    """Parameters for creating a product"""

    location_id: str = Field(..., description="Location ID where the product will be created")
    name: str = Field(..., description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    product_type: Optional[str] = Field(None, description="Product type (e.g., PHYSICAL, DIGITAL)")
    available_in_store: Optional[bool] = Field(None, description="Whether product is available in store")
    variants: Optional[List[Dict[str, Any]]] = Field(None, description="Product variants")
    medias: Optional[List[Dict[str, Any]]] = Field(None, description="Product media files")
    image: Optional[str] = Field(None, description="Product image URL")
    statement_descriptor: Optional[str] = Field(None, description="Statement descriptor for payments")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateProductParams(BaseModel):
    """Parameters for updating a product"""

    product_id: str = Field(..., description="The product ID to update")
    location_id: str = Field(..., description="The location ID")
    name: Optional[str] = Field(None, description="Product name")
    description: Optional[str] = Field(None, description="Product description")
    product_type: Optional[str] = Field(None, description="Product type (e.g., PHYSICAL, DIGITAL)")
    available_in_store: Optional[bool] = Field(None, description="Whether product is available in store")
    variants: Optional[List[Dict[str, Any]]] = Field(None, description="Product variants")
    medias: Optional[List[Dict[str, Any]]] = Field(None, description="Product media files")
    image: Optional[str] = Field(None, description="Product image URL")
    statement_descriptor: Optional[str] = Field(None, description="Statement descriptor for payments")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteProductParams(BaseModel):
    """Parameters for deleting a product"""

    product_id: str = Field(..., description="The product ID to delete")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


# Product Price Parameters

class GetProductPricesParams(BaseModel):
    """Parameters for getting product prices"""

    product_id: str = Field(..., description="The product ID to get prices for")
    location_id: str = Field(..., description="The location ID")
    limit: int = Field(default=100, description="Number of results to return (max 100)")
    skip: int = Field(default=0, description="Number of results to skip")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class GetProductPriceParams(BaseModel):
    """Parameters for getting a single product price"""

    product_id: str = Field(..., description="The product ID")
    price_id: str = Field(..., description="The price ID to retrieve")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class CreateProductPriceParams(BaseModel):
    """Parameters for creating a product price"""

    product_id: str = Field(..., description="The product ID")
    location_id: str = Field(..., description="The location ID")
    name: str = Field(..., description="Price name")
    price_type: str = Field(..., description="Price type (one_time, recurring)")
    currency: str = Field(..., description="Currency code (USD, EUR, etc.)")
    amount: int = Field(..., description="Amount in cents")
    membership_offers: Optional[List[Dict[str, Any]]] = Field(None, description="Membership offers")
    variant_option_ids: Optional[List[str]] = Field(None, description="Variant option IDs")
    recurring: Optional[Dict[str, Any]] = Field(None, description="Recurring payment details")
    compare_at_price: Optional[int] = Field(None, description="Compare at price in cents")
    track_inventory: Optional[bool] = Field(None, description="Whether to track inventory")
    available_quantity: Optional[int] = Field(None, description="Available quantity")
    allow_out_of_stock_purchases: Optional[bool] = Field(None, description="Allow out of stock purchases")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class UpdateProductPriceParams(BaseModel):
    """Parameters for updating a product price"""

    product_id: str = Field(..., description="The product ID")
    price_id: str = Field(..., description="The price ID to update")
    location_id: str = Field(..., description="The location ID")
    name: Optional[str] = Field(None, description="Price name")
    price_type: Optional[str] = Field(None, description="Price type (one_time, recurring)")
    currency: Optional[str] = Field(None, description="Currency code (USD, EUR, etc.)")
    amount: Optional[int] = Field(None, description="Amount in cents")
    membership_offers: Optional[List[Dict[str, Any]]] = Field(None, description="Membership offers")
    variant_option_ids: Optional[List[str]] = Field(None, description="Variant option IDs")
    recurring: Optional[Dict[str, Any]] = Field(None, description="Recurring payment details")
    compare_at_price: Optional[int] = Field(None, description="Compare at price in cents")
    track_inventory: Optional[bool] = Field(None, description="Whether to track inventory")
    available_quantity: Optional[int] = Field(None, description="Available quantity")
    allow_out_of_stock_purchases: Optional[bool] = Field(None, description="Allow out of stock purchases")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )


class DeleteProductPriceParams(BaseModel):
    """Parameters for deleting a product price"""

    product_id: str = Field(..., description="The product ID")
    price_id: str = Field(..., description="The price ID to delete")
    location_id: str = Field(..., description="The location ID")
    access_token: Optional[str] = Field(
        None, description="Optional access token to use instead of stored token"
    )
