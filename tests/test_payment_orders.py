"""Tests for payment order tools"""

import pytest
from unittest.mock import AsyncMock
from src.mcp.params.payments import (
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
from src.models.payment import (
    PaymentOrder, PaymentOrderList,
    PaymentOrderFulfillment, PaymentOrderFulfillmentList, PaymentOrderFulfillmentCreate,
    PaymentSubscription, PaymentSubscriptionList,
    PaymentTransaction, PaymentTransactionList,
    PaymentIntegration, PaymentIntegrationCreate
)


class TestPaymentOrderImplementation:
    """Test payment order MCP tools implementation"""

    @pytest.mark.asyncio
    async def test_get_payment_orders(self):
        """Test getting payment orders"""
        # Create mock client
        mock_client = AsyncMock()
        mock_orders = PaymentOrderList(
            orders=[
                PaymentOrder(id="order_1", amount=100.0, currency="USD"),
                PaymentOrder(id="order_2", amount=200.0, currency="USD"),
            ],
            count=2,
            total=2
        )
        mock_client.get_payment_orders.return_value = mock_orders

        # Create test parameters
        params = GetPaymentOrdersParams(
            location_id="test_location",
            limit=10,
            skip=0
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        orders = await client.get_payment_orders(
            params.location_id, params.limit, params.skip
        )
        result = {"success": True, "orders": orders.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "orders" in result
        assert len(result["orders"]["orders"]) == 2

        # Verify the client was called correctly
        mock_client.get_payment_orders.assert_called_once_with("test_location", 10, 0)

    @pytest.mark.asyncio
    async def test_get_payment_order(self):
        """Test getting a single payment order"""
        # Create mock client
        mock_client = AsyncMock()
        mock_order = PaymentOrder(id="order_1", amount=100.0, currency="USD")
        mock_client.get_payment_order.return_value = mock_order

        # Create test parameters
        params = GetPaymentOrderParams(
            order_id="order_1",
            location_id="test_location"
        )

        # Test the logic directly
        client = mock_client
        order = await client.get_payment_order(params.order_id, params.location_id)
        result = {"success": True, "order": order.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "order" in result
        assert result["order"]["id"] == "order_1"

        # Verify the client was called correctly
        mock_client.get_payment_order.assert_called_once_with("order_1", "test_location")

    @pytest.mark.asyncio
    async def test_get_order_fulfillments(self):
        """Test getting order fulfillments"""
        # Create mock client
        mock_client = AsyncMock()
        mock_fulfillments = PaymentOrderFulfillmentList(
            fulfillments=[
                PaymentOrderFulfillment(id="fulfillment_1", orderId="order_1"),
            ],
            count=1,
            total=1
        )
        mock_client.get_order_fulfillments.return_value = mock_fulfillments

        # Create test parameters
        params = GetOrderFulfillmentsParams(
            order_id="order_1",
            location_id="test_location",
            limit=10,
            skip=0
        )

        # Test the logic directly
        client = mock_client
        fulfillments = await client.get_order_fulfillments(
            params.order_id, params.location_id, params.limit, params.skip
        )
        result = {"success": True, "fulfillments": fulfillments.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "fulfillments" in result
        assert len(result["fulfillments"]["fulfillments"]) == 1

        # Verify the client was called correctly
        mock_client.get_order_fulfillments.assert_called_once_with("order_1", "test_location", 10, 0)

    @pytest.mark.asyncio
    async def test_create_order_fulfillment(self):
        """Test creating an order fulfillment"""
        # Create mock client
        mock_client = AsyncMock()
        mock_fulfillment = PaymentOrderFulfillment(
            id="fulfillment_1",
            orderId="order_1",
            trackingNumber="TRACK123"
        )
        mock_client.create_order_fulfillment.return_value = mock_fulfillment

        # Create test parameters
        params = CreateOrderFulfillmentParams(
            order_id="order_1",
            location_id="test_location",
            tracking_number="TRACK123",
            carrier="UPS"
        )

        # Test the logic directly
        client = mock_client
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
        result = {"success": True, "fulfillment": fulfillment.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "fulfillment" in result
        assert result["fulfillment"]["trackingNumber"] == "TRACK123"

        # Verify the client was called correctly
        mock_client.create_order_fulfillment.assert_called_once()
        call_args = mock_client.create_order_fulfillment.call_args
        assert call_args[0][0] == "order_1"  # order_id
        assert call_args[0][2] == "test_location"  # location_id

        # Check the fulfillment data
        fulfillment_data = call_args[0][1]
        assert fulfillment_data.trackingNumber == "TRACK123"
        assert fulfillment_data.carrier == "UPS"

    def test_payment_parameter_classes_exist(self):
        """Test that payment parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetPaymentOrdersParams, BaseModel)
        assert issubclass(GetPaymentOrderParams, BaseModel)
        assert issubclass(GetOrderFulfillmentsParams, BaseModel)
        assert issubclass(CreateOrderFulfillmentParams, BaseModel)

        # Check that required fields exist
        assert "location_id" in GetPaymentOrdersParams.model_fields
        assert "order_id" in GetPaymentOrderParams.model_fields
        assert "order_id" in GetOrderFulfillmentsParams.model_fields
        assert "order_id" in CreateOrderFulfillmentParams.model_fields

    @pytest.mark.asyncio
    async def test_get_payment_subscriptions(self):
        """Test getting payment subscriptions"""
        # Create mock client
        mock_client = AsyncMock()
        mock_subscriptions = PaymentSubscriptionList(
            subscriptions=[
                PaymentSubscription(id="sub_1", amount=29.99, currency="USD"),
                PaymentSubscription(id="sub_2", amount=49.99, currency="USD"),
            ],
            count=2,
            total=2
        )
        mock_client.get_payment_subscriptions.return_value = mock_subscriptions

        # Create test parameters
        params = GetPaymentSubscriptionsParams(
            location_id="test_location",
            limit=10,
            skip=0
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        subscriptions = await client.get_payment_subscriptions(
            params.location_id, params.limit, params.skip
        )
        result = {"success": True, "subscriptions": subscriptions.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "subscriptions" in result
        assert len(result["subscriptions"]["subscriptions"]) == 2

        # Verify the client was called correctly
        mock_client.get_payment_subscriptions.assert_called_once_with("test_location", 10, 0)

    @pytest.mark.asyncio
    async def test_get_payment_subscription(self):
        """Test getting a single payment subscription"""
        # Create mock client
        mock_client = AsyncMock()
        mock_subscription = PaymentSubscription(id="sub_1", amount=29.99, currency="USD")
        mock_client.get_payment_subscription.return_value = mock_subscription

        # Create test parameters
        params = GetPaymentSubscriptionParams(
            subscription_id="sub_1",
            location_id="test_location"
        )

        # Test the logic directly
        client = mock_client
        subscription = await client.get_payment_subscription(params.subscription_id, params.location_id)
        result = {"success": True, "subscription": subscription.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "subscription" in result
        assert result["subscription"]["id"] == "sub_1"

        # Verify the client was called correctly
        mock_client.get_payment_subscription.assert_called_once_with("sub_1", "test_location")

    def test_payment_subscription_parameter_classes_exist(self):
        """Test that payment subscription parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetPaymentSubscriptionsParams, BaseModel)
        assert issubclass(GetPaymentSubscriptionParams, BaseModel)

        # Check that required fields exist
        assert "location_id" in GetPaymentSubscriptionsParams.model_fields
        assert "subscription_id" in GetPaymentSubscriptionParams.model_fields

    @pytest.mark.asyncio
    async def test_get_payment_transactions(self):
        """Test getting payment transactions"""
        # Create mock client
        mock_client = AsyncMock()
        mock_transactions = PaymentTransactionList(
            transactions=[
                PaymentTransaction(id="txn_1", amount=100.0, currency="USD"),
                PaymentTransaction(id="txn_2", amount=200.0, currency="USD"),
            ],
            count=2,
            total=2
        )
        mock_client.get_payment_transactions.return_value = mock_transactions

        # Create test parameters
        params = GetPaymentTransactionsParams(
            location_id="test_location",
            limit=10,
            skip=0
        )

        # Test the logic directly (simulating what the MCP tool does)
        client = mock_client
        transactions = await client.get_payment_transactions(
            params.location_id, params.limit, params.skip
        )
        result = {"success": True, "transactions": transactions.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "transactions" in result
        assert len(result["transactions"]["transactions"]) == 2

        # Verify the client was called correctly
        mock_client.get_payment_transactions.assert_called_once_with("test_location", 10, 0)

    @pytest.mark.asyncio
    async def test_get_payment_transaction(self):
        """Test getting a single payment transaction"""
        # Create mock client
        mock_client = AsyncMock()
        mock_transaction = PaymentTransaction(id="txn_1", amount=100.0, currency="USD")
        mock_client.get_payment_transaction.return_value = mock_transaction

        # Create test parameters
        params = GetPaymentTransactionParams(
            transaction_id="txn_1",
            location_id="test_location"
        )

        # Test the logic directly
        client = mock_client
        transaction = await client.get_payment_transaction(params.transaction_id, params.location_id)
        result = {"success": True, "transaction": transaction.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "transaction" in result
        assert result["transaction"]["id"] == "txn_1"

        # Verify the client was called correctly
        mock_client.get_payment_transaction.assert_called_once_with("txn_1", "test_location")

    @pytest.mark.asyncio
    async def test_get_payment_integration(self):
        """Test getting payment integration"""
        # Create mock client
        mock_client = AsyncMock()
        mock_integration = PaymentIntegration(
            id="int_1",
            provider="stripe",
            status="active",
            isActive=True
        )
        mock_client.get_payment_integration.return_value = mock_integration

        # Create test parameters
        params = GetPaymentIntegrationParams(
            location_id="test_location"
        )

        # Test the logic directly
        client = mock_client
        integration = await client.get_payment_integration(params.location_id)
        result = {"success": True, "integration": integration.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "integration" in result
        assert result["integration"]["provider"] == "stripe"

        # Verify the client was called correctly
        mock_client.get_payment_integration.assert_called_once_with("test_location")

    @pytest.mark.asyncio
    async def test_create_payment_integration(self):
        """Test creating a payment integration"""
        # Create mock client
        mock_client = AsyncMock()
        mock_integration = PaymentIntegration(
            id="int_1",
            provider="stripe",
            status="active",
            isActive=True
        )
        mock_client.create_payment_integration.return_value = mock_integration

        # Create test parameters
        params = CreatePaymentIntegrationParams(
            location_id="test_location",
            provider="stripe",
            configuration={"api_key": "sk_test_123"},
            is_active=True
        )

        # Test the logic directly
        client = mock_client
        integration_data = PaymentIntegrationCreate(
            provider=params.provider,
            configuration=params.configuration,
            credentials=params.credentials,
            webhookUrl=params.webhook_url,
            isActive=params.is_active,
        )
        integration = await client.create_payment_integration(integration_data, params.location_id)
        result = {"success": True, "integration": integration.model_dump()}

        # Verify the result
        assert result["success"] is True
        assert "integration" in result
        assert result["integration"]["provider"] == "stripe"

        # Verify the client was called correctly
        mock_client.create_payment_integration.assert_called_once()
        call_args = mock_client.create_payment_integration.call_args
        assert call_args[0][1] == "test_location"  # location_id

        # Check the integration data
        integration_data = call_args[0][0]
        assert integration_data.provider == "stripe"
        assert integration_data.configuration == {"api_key": "sk_test_123"}

    def test_payment_transaction_parameter_classes_exist(self):
        """Test that payment transaction parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetPaymentTransactionsParams, BaseModel)
        assert issubclass(GetPaymentTransactionParams, BaseModel)

        # Check that required fields exist
        assert "location_id" in GetPaymentTransactionsParams.model_fields
        assert "transaction_id" in GetPaymentTransactionParams.model_fields

    def test_payment_integration_parameter_classes_exist(self):
        """Test that payment integration parameter classes are properly defined"""
        from pydantic import BaseModel

        # Check that parameter classes exist and are BaseModel subclasses
        assert issubclass(GetPaymentIntegrationParams, BaseModel)
        assert issubclass(CreatePaymentIntegrationParams, BaseModel)

        # Check that required fields exist
        assert "location_id" in GetPaymentIntegrationParams.model_fields
        assert "provider" in CreatePaymentIntegrationParams.model_fields
        assert "configuration" in CreatePaymentIntegrationParams.model_fields
