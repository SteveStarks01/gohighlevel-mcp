"""Products management client for GoHighLevel API v2"""

from typing import Optional

from .base import BaseGoHighLevelClient
from ..models.product import (
    Product, ProductCreate, ProductUpdate, ProductList,
    ProductPrice, ProductPriceCreate, ProductPriceUpdate, ProductPriceList
)


class ProductsClient(BaseGoHighLevelClient):
    """Client for product-related endpoints"""

    async def get_products(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> ProductList:
        """Get all products for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            ProductList containing products and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", "/products/", params=params, location_id=location_id
        )
        data = response.json()
        
        products_data = data.get("products", [])
        return ProductList(
            products=[Product(**product) for product in products_data],
            count=len(products_data),
            total=data.get("total", len(products_data)),
        )

    async def get_product(self, product_id: str, location_id: str) -> Product:
        """Get a specific product
        
        Args:
            product_id: The product ID
            location_id: The location ID
            
        Returns:
            Product object
        """
        response = await self._request(
            "GET", f"/products/{product_id}", location_id=location_id
        )
        return Product(**response.json())

    async def create_product(self, product: ProductCreate) -> Product:
        """Create a new product
        
        Args:
            product: Product creation data
            
        Returns:
            Created Product object
        """
        response = await self._request(
            "POST",
            "/products/",
            json=product.model_dump(exclude_none=True),
            location_id=product.locationId,
        )
        return Product(**response.json())

    async def update_product(
        self, product_id: str, updates: ProductUpdate, location_id: str
    ) -> Product:
        """Update an existing product
        
        Args:
            product_id: The product ID to update
            updates: Product update data
            location_id: The location ID
            
        Returns:
            Updated Product object
        """
        response = await self._request(
            "PUT",
            f"/products/{product_id}",
            json=updates.model_dump(exclude_none=True),
            location_id=location_id,
        )
        return Product(**response.json())

    async def delete_product(self, product_id: str, location_id: str) -> bool:
        """Delete a product
        
        Args:
            product_id: The product ID to delete
            location_id: The location ID
            
        Returns:
            True if deletion was successful
        """
        response = await self._request(
            "DELETE", f"/products/{product_id}", location_id=location_id
        )
        return response.status_code == 200

    # Product Price Methods

    async def get_product_prices(
        self, product_id: str, location_id: str, limit: int = 100, skip: int = 0
    ) -> ProductPriceList:
        """Get all prices for a product

        Args:
            product_id: The product ID
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip

        Returns:
            ProductPriceList containing prices and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip

        response = await self._request(
            "GET", f"/products/{product_id}/price/", params=params, location_id=location_id
        )
        data = response.json()

        prices_data = data.get("prices", [])
        return ProductPriceList(
            prices=[ProductPrice(**price) for price in prices_data],
            count=len(prices_data),
            total=data.get("total", len(prices_data)),
        )

    async def get_product_price(
        self, product_id: str, price_id: str, location_id: str
    ) -> ProductPrice:
        """Get a specific product price

        Args:
            product_id: The product ID
            price_id: The price ID
            location_id: The location ID

        Returns:
            ProductPrice object
        """
        response = await self._request(
            "GET", f"/products/{product_id}/price/{price_id}", location_id=location_id
        )
        return ProductPrice(**response.json())

    async def create_product_price(
        self, product_id: str, price: ProductPriceCreate, location_id: str
    ) -> ProductPrice:
        """Create a new product price

        Args:
            product_id: The product ID
            price: Product price creation data
            location_id: The location ID

        Returns:
            Created ProductPrice object
        """
        response = await self._request(
            "POST",
            f"/products/{product_id}/price/",
            json=price.model_dump(exclude_none=True),
            location_id=location_id,
        )
        return ProductPrice(**response.json())

    async def update_product_price(
        self, product_id: str, price_id: str, updates: ProductPriceUpdate, location_id: str
    ) -> ProductPrice:
        """Update an existing product price

        Args:
            product_id: The product ID
            price_id: The price ID to update
            updates: Product price update data
            location_id: The location ID

        Returns:
            Updated ProductPrice object
        """
        response = await self._request(
            "PUT",
            f"/products/{product_id}/price/{price_id}",
            json=updates.model_dump(exclude_none=True),
            location_id=location_id,
        )
        return ProductPrice(**response.json())

    async def delete_product_price(
        self, product_id: str, price_id: str, location_id: str
    ) -> bool:
        """Delete a product price

        Args:
            product_id: The product ID
            price_id: The price ID to delete
            location_id: The location ID

        Returns:
            True if deletion was successful
        """
        response = await self._request(
            "DELETE", f"/products/{product_id}/price/{price_id}", location_id=location_id
        )
        return response.status_code == 200
