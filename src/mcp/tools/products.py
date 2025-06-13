"""Product tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.product import ProductCreate, ProductUpdate, ProductPriceCreate, ProductPriceUpdate
from ..params.products import (
    GetProductsParams,
    GetProductParams,
    CreateProductParams,
    UpdateProductParams,
    DeleteProductParams,
    GetProductPricesParams,
    GetProductPriceParams,
    CreateProductPriceParams,
    UpdateProductPriceParams,
    DeleteProductPriceParams,
)


# Import the mcp instance and get_client from main
# This will be set during import in main.py
mcp = None
get_client = None


def _register_product_tools(mcp_instance, get_client_func):
    """Register all product tools with the MCP server"""
    global mcp, get_client
    mcp = mcp_instance
    get_client = get_client_func

    @mcp.tool()
    async def get_products(params: GetProductsParams) -> Dict[str, Any]:
        """Get all products for a location"""
        client = await get_client(params.access_token)

        product_list = await client.get_products(
            params.location_id, params.limit, params.skip
        )
        return {
            "success": True,
            "products": [product.model_dump() for product in product_list.products],
            "count": product_list.count,
            "total": product_list.total,
        }

    @mcp.tool()
    async def get_product(params: GetProductParams) -> Dict[str, Any]:
        """Get a specific product"""
        client = await get_client(params.access_token)

        product = await client.get_product(params.product_id, params.location_id)
        return {"success": True, "product": product.model_dump()}

    @mcp.tool()
    async def create_product(params: CreateProductParams) -> Dict[str, Any]:
        """Create a new product"""
        client = await get_client(params.access_token)

        product_data = ProductCreate(
            locationId=params.location_id,
            name=params.name,
            description=params.description,
            productType=params.product_type,
            availableInStore=params.available_in_store,
            variants=params.variants,
            medias=params.medias,
            image=params.image,
            statementDescriptor=params.statement_descriptor,
        )

        product = await client.create_product(product_data)
        return {"success": True, "product": product.model_dump()}

    @mcp.tool()
    async def update_product(params: UpdateProductParams) -> Dict[str, Any]:
        """Update an existing product"""
        client = await get_client(params.access_token)

        update_data = ProductUpdate(
            name=params.name,
            description=params.description,
            productType=params.product_type,
            availableInStore=params.available_in_store,
            variants=params.variants,
            medias=params.medias,
            image=params.image,
            statementDescriptor=params.statement_descriptor,
        )

        product = await client.update_product(
            params.product_id, update_data, params.location_id
        )
        return {"success": True, "product": product.model_dump()}

    @mcp.tool()
    async def delete_product(params: DeleteProductParams) -> Dict[str, Any]:
        """Delete a product"""
        client = await get_client(params.access_token)

        success = await client.delete_product(params.product_id, params.location_id)
        return {
            "success": success,
            "message": (
                "Product deleted successfully" if success else "Failed to delete product"
            ),
        }

    # Product Price Tools

    @mcp.tool()
    async def get_product_prices(params: GetProductPricesParams) -> Dict[str, Any]:
        """Get all prices for a product"""
        client = await get_client(params.access_token)

        price_list = await client.get_product_prices(
            params.product_id, params.location_id, params.limit, params.skip
        )
        return {
            "success": True,
            "prices": [price.model_dump() for price in price_list.prices],
            "count": price_list.count,
            "total": price_list.total,
        }

    @mcp.tool()
    async def get_product_price(params: GetProductPriceParams) -> Dict[str, Any]:
        """Get a specific product price"""
        client = await get_client(params.access_token)

        price = await client.get_product_price(
            params.product_id, params.price_id, params.location_id
        )
        return {"success": True, "price": price.model_dump()}

    @mcp.tool()
    async def create_product_price(params: CreateProductPriceParams) -> Dict[str, Any]:
        """Create a new product price"""
        client = await get_client(params.access_token)

        price_data = ProductPriceCreate(
            name=params.name,
            type=params.price_type,
            currency=params.currency,
            amount=params.amount,
            membershipOffers=params.membership_offers,
            variantOptionIds=params.variant_option_ids,
            recurring=params.recurring,
            compareAtPrice=params.compare_at_price,
            trackInventory=params.track_inventory,
            availableQuantity=params.available_quantity,
            allowOutOfStockPurchases=params.allow_out_of_stock_purchases,
        )

        price = await client.create_product_price(
            params.product_id, price_data, params.location_id
        )
        return {"success": True, "price": price.model_dump()}

    @mcp.tool()
    async def update_product_price(params: UpdateProductPriceParams) -> Dict[str, Any]:
        """Update an existing product price"""
        client = await get_client(params.access_token)

        update_data = ProductPriceUpdate(
            name=params.name,
            type=params.price_type,
            currency=params.currency,
            amount=params.amount,
            membershipOffers=params.membership_offers,
            variantOptionIds=params.variant_option_ids,
            recurring=params.recurring,
            compareAtPrice=params.compare_at_price,
            trackInventory=params.track_inventory,
            availableQuantity=params.available_quantity,
            allowOutOfStockPurchases=params.allow_out_of_stock_purchases,
        )

        price = await client.update_product_price(
            params.product_id, params.price_id, update_data, params.location_id
        )
        return {"success": True, "price": price.model_dump()}

    @mcp.tool()
    async def delete_product_price(params: DeleteProductPriceParams) -> Dict[str, Any]:
        """Delete a product price"""
        client = await get_client(params.access_token)

        success = await client.delete_product_price(
            params.product_id, params.price_id, params.location_id
        )
        return {
            "success": success,
            "message": (
                "Product price deleted successfully" if success else "Failed to delete product price"
            ),
        }
