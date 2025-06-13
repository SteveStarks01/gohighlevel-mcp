"""Payment tools for GoHighLevel MCP integration"""

from typing import Dict, Any

from ...models.payment import PaymentOrderFulfillmentCreate, PaymentIntegrationCreate
from ..params.payments import (
    GetPaymentOrdersParams,
    GetPaymentOrderParams,
    GetOrderFulfillmentsParams,
    CreateOrderFulfillmentParams,
    GetPaymentSubscriptionsParams,
    GetPaymentSubscriptionParams,
    GetPaymentTransactionsParams,
    GetPaymentTransactionParams,
    GetPaymentIntegrationParams,
    CreatePaymentIntegrationParams,
)


def _register_payment_tools(mcp, get_client):
    """Register payment-related MCP tools"""

    @mcp.tool()
    async def get_payment_orders(params: GetPaymentOrdersParams) -> Dict[str, Any]:
        """Get all payment orders for a location"""
        client = await get_client(params.access_token)

        orders = await client.get_payment_orders(
            params.location_id, params.limit, params.skip
        )
        return {"success": True, "orders": orders.model_dump()}

    @mcp.tool()
    async def get_payment_order(params: GetPaymentOrderParams) -> Dict[str, Any]:
        """Get a specific payment order"""
        client = await get_client(params.access_token)

        order = await client.get_payment_order(params.order_id, params.location_id)
        return {"success": True, "order": order.model_dump()}

    @mcp.tool()
    async def get_order_fulfillments(params: GetOrderFulfillmentsParams) -> Dict[str, Any]:
        """Get all fulfillments for a payment order"""
        client = await get_client(params.access_token)

        fulfillments = await client.get_order_fulfillments(
            params.order_id, params.location_id, params.limit, params.skip
        )
        return {"success": True, "fulfillments": fulfillments.model_dump()}

    @mcp.tool()
    async def create_order_fulfillment(params: CreateOrderFulfillmentParams) -> Dict[str, Any]:
        """Create a new fulfillment for a payment order"""
        client = await get_client(params.access_token)

        fulfillment_data = PaymentOrderFulfillmentCreate(
            trackingNumber=params.tracking_number,
            trackingUrl=params.tracking_url,
            carrier=params.carrier,
            items=params.items,
            notify=params.notify,
        )

        fulfillment = await client.create_order_fulfillment(
            params.order_id, fulfillment_data, params.location_id
        )
        return {"success": True, "fulfillment": fulfillment.model_dump()}

    @mcp.tool()
    async def get_payment_subscriptions(params: GetPaymentSubscriptionsParams) -> Dict[str, Any]:
        """Get all payment subscriptions for a location"""
        client = await get_client(params.access_token)

        subscriptions = await client.get_payment_subscriptions(
            params.location_id, params.limit, params.skip
        )
        return {"success": True, "subscriptions": subscriptions.model_dump()}

    @mcp.tool()
    async def get_payment_subscription(params: GetPaymentSubscriptionParams) -> Dict[str, Any]:
        """Get a specific payment subscription"""
        client = await get_client(params.access_token)

        subscription = await client.get_payment_subscription(params.subscription_id, params.location_id)
        return {"success": True, "subscription": subscription.model_dump()}

    @mcp.tool()
    async def get_payment_transactions(params: GetPaymentTransactionsParams) -> Dict[str, Any]:
        """Get all payment transactions for a location"""
        client = await get_client(params.access_token)

        transactions = await client.get_payment_transactions(
            params.location_id, params.limit, params.skip
        )
        return {"success": True, "transactions": transactions.model_dump()}

    @mcp.tool()
    async def get_payment_transaction(params: GetPaymentTransactionParams) -> Dict[str, Any]:
        """Get a specific payment transaction"""
        client = await get_client(params.access_token)

        transaction = await client.get_payment_transaction(params.transaction_id, params.location_id)
        return {"success": True, "transaction": transaction.model_dump()}

    @mcp.tool()
    async def get_payment_integration(params: GetPaymentIntegrationParams) -> Dict[str, Any]:
        """Get the whitelabel payment integration for a location"""
        client = await get_client(params.access_token)

        integration = await client.get_payment_integration(params.location_id)
        return {"success": True, "integration": integration.model_dump()}

    @mcp.tool()
    async def create_payment_integration(params: CreatePaymentIntegrationParams) -> Dict[str, Any]:
        """Create or configure a whitelabel payment integration"""
        client = await get_client(params.access_token)

        integration_data = PaymentIntegrationCreate(
            provider=params.provider,
            configuration=params.configuration,
            credentials=params.credentials,
            webhookUrl=params.webhook_url,
            isActive=params.is_active,
        )

        integration = await client.create_payment_integration(integration_data, params.location_id)
        return {"success": True, "integration": integration.model_dump()}
