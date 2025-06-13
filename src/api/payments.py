"""Payments management client for GoHighLevel API v2"""

from typing import Optional

from .base import BaseGoHighLevelClient
from ..models.payment import (
    PaymentOrder, PaymentOrderList,
    PaymentOrderFulfillment, PaymentOrderFulfillmentList, PaymentOrderFulfillmentCreate,
    PaymentSubscription, PaymentSubscriptionList,
    PaymentTransaction, PaymentTransactionList,
    PaymentIntegration, PaymentIntegrationCreate
)


class PaymentsClient(BaseGoHighLevelClient):
    """Client for payment-related endpoints"""

    async def get_payment_orders(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> PaymentOrderList:
        """Get all payment orders for a location
        
        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            PaymentOrderList containing orders and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", "/payments/orders/", params=params, location_id=location_id
        )
        data = response.json()
        
        orders_data = data.get("orders", [])
        return PaymentOrderList(
            orders=[PaymentOrder(**order) for order in orders_data],
            count=len(orders_data),
            total=data.get("total", len(orders_data)),
        )

    async def get_payment_order(self, order_id: str, location_id: str) -> PaymentOrder:
        """Get a specific payment order
        
        Args:
            order_id: The payment order ID
            location_id: The location ID
            
        Returns:
            PaymentOrder object
        """
        response = await self._request(
            "GET", f"/payments/orders/{order_id}", location_id=location_id
        )
        return PaymentOrder(**response.json())

    async def get_order_fulfillments(
        self, order_id: str, location_id: str, limit: int = 100, skip: int = 0
    ) -> PaymentOrderFulfillmentList:
        """Get all fulfillments for a payment order
        
        Args:
            order_id: The payment order ID
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip
            
        Returns:
            PaymentOrderFulfillmentList containing fulfillments and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip
            
        response = await self._request(
            "GET", f"/payments/orders/{order_id}/fulfillments", 
            params=params, location_id=location_id
        )
        data = response.json()
        
        fulfillments_data = data.get("fulfillments", [])
        return PaymentOrderFulfillmentList(
            fulfillments=[PaymentOrderFulfillment(**fulfillment) for fulfillment in fulfillments_data],
            count=len(fulfillments_data),
            total=data.get("total", len(fulfillments_data)),
        )

    async def create_order_fulfillment(
        self, order_id: str, fulfillment: PaymentOrderFulfillmentCreate, location_id: str
    ) -> PaymentOrderFulfillment:
        """Create a new fulfillment for a payment order
        
        Args:
            order_id: The payment order ID
            fulfillment: Fulfillment creation data
            location_id: The location ID
            
        Returns:
            Created PaymentOrderFulfillment object
        """
        response = await self._request(
            "POST",
            f"/payments/orders/{order_id}/fulfillments",
            json=fulfillment.model_dump(exclude_none=True),
            location_id=location_id,
        )
        return PaymentOrderFulfillment(**response.json())

    async def get_payment_subscriptions(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> PaymentSubscriptionList:
        """Get all payment subscriptions for a location

        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip

        Returns:
            PaymentSubscriptionList containing subscriptions and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip

        response = await self._request(
            "GET", "/payments/subscriptions/", params=params, location_id=location_id
        )
        data = response.json()

        subscriptions_data = data.get("subscriptions", [])
        return PaymentSubscriptionList(
            subscriptions=[PaymentSubscription(**subscription) for subscription in subscriptions_data],
            count=len(subscriptions_data),
            total=data.get("total", len(subscriptions_data)),
        )

    async def get_payment_subscription(self, subscription_id: str, location_id: str) -> PaymentSubscription:
        """Get a specific payment subscription

        Args:
            subscription_id: The payment subscription ID
            location_id: The location ID

        Returns:
            PaymentSubscription object
        """
        response = await self._request(
            "GET", f"/payments/subscriptions/{subscription_id}", location_id=location_id
        )
        return PaymentSubscription(**response.json())

    async def get_payment_transactions(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> PaymentTransactionList:
        """Get all payment transactions for a location

        Args:
            location_id: The location ID
            limit: Number of results to return (max 100)
            skip: Number of results to skip

        Returns:
            PaymentTransactionList containing transactions and metadata
        """
        params = {"limit": limit}
        if skip > 0:
            params["skip"] = skip

        response = await self._request(
            "GET", "/payments/transactions/", params=params, location_id=location_id
        )
        data = response.json()

        transactions_data = data.get("transactions", [])
        return PaymentTransactionList(
            transactions=[PaymentTransaction(**transaction) for transaction in transactions_data],
            count=len(transactions_data),
            total=data.get("total", len(transactions_data)),
        )

    async def get_payment_transaction(self, transaction_id: str, location_id: str) -> PaymentTransaction:
        """Get a specific payment transaction

        Args:
            transaction_id: The payment transaction ID
            location_id: The location ID

        Returns:
            PaymentTransaction object
        """
        response = await self._request(
            "GET", f"/payments/transactions/{transaction_id}", location_id=location_id
        )
        return PaymentTransaction(**response.json())

    async def get_payment_integration(self, location_id: str) -> PaymentIntegration:
        """Get the whitelabel payment integration for a location

        Args:
            location_id: The location ID

        Returns:
            PaymentIntegration object
        """
        response = await self._request(
            "GET", "/payments/integrations/provider/whitelabel", location_id=location_id
        )
        return PaymentIntegration(**response.json())

    async def create_payment_integration(
        self, integration: PaymentIntegrationCreate, location_id: str
    ) -> PaymentIntegration:
        """Create or configure a whitelabel payment integration

        Args:
            integration: Integration creation data
            location_id: The location ID

        Returns:
            Created PaymentIntegration object
        """
        response = await self._request(
            "POST",
            "/payments/integrations/provider/whitelabel",
            json=integration.model_dump(exclude_none=True),
            location_id=location_id,
        )
        return PaymentIntegration(**response.json())
