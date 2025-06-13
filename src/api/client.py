"""Main GoHighLevel API v2 client with composition pattern"""

from typing import Any, Dict, Optional, List
from datetime import date

from ..services.oauth import OAuthService
from ..models.contact import Contact, ContactCreate, ContactUpdate, ContactList
from ..models.task import Task, TaskCreate, TaskUpdate, TaskList
from ..models.note import Note, NoteCreate, NoteUpdate, NoteList
from ..models.business import Business, BusinessCreate, BusinessUpdate, BusinessList
from ..models.user import User, UserCreate, UserUpdate, UserList
from ..models.campaign import Campaign, CampaignList
from ..models.workflow import Workflow, WorkflowList
from ..models.location import (
    Location, LocationCreate, LocationUpdate, LocationList,
    LocationTag, LocationTagList, LocationTagCreate, LocationTagUpdate,
    LocationCustomValue, LocationCustomValueList, LocationCustomValueCreate, LocationCustomValueUpdate,
    LocationCustomField, LocationCustomFieldList, LocationCustomFieldCreate, LocationCustomFieldUpdate,
    LocationTemplate, LocationTemplateList, LocationTask, LocationTaskList, LocationTaskSearchFilters
)
from ..models.calendar import CalendarCreate, CalendarUpdate, CalendarGroup, CalendarGroupList
from ..models.product import (
    Product, ProductCreate, ProductUpdate, ProductList,
    ProductPrice, ProductPriceCreate, ProductPriceUpdate, ProductPriceList
)
from ..models.conversation import (
    Conversation,
    ConversationCreate,
    ConversationList,
    Message,
    MessageCreate,
    MessageList,
)
from ..models.opportunity import (
    Opportunity,
    OpportunityCreate,
    OpportunityUpdate,
    OpportunitySearchResult,
    OpportunitySearchFilters,
    Pipeline,
)
from ..models.calendar import (
    Appointment,
    AppointmentCreate,
    AppointmentUpdate,
    AppointmentList,
    Calendar,
    CalendarList,
    FreeSlotsResult,
)
from ..models.form import (
    FormList,
    FormSubmissionList,
    FormFileUploadRequest,
)
from ..models.payment import (
    PaymentOrder, PaymentOrderList,
    PaymentOrderFulfillment, PaymentOrderFulfillmentList, PaymentOrderFulfillmentCreate,
    PaymentSubscription, PaymentSubscriptionList,
    PaymentTransaction, PaymentTransactionList,
    PaymentIntegration, PaymentIntegrationCreate
)
from ..models.link import Link, LinkCreate, LinkUpdate, LinkList
from ..models.survey import Survey, SurveySubmission, SurveyList, SurveySubmissionList
from ..models.oauth import (
    InstalledLocation, InstalledLocationList, LocationToken, LocationTokenRequest,
    SaasSubscription, SaasSubscriptionUpdate
)

from .contacts import ContactsClient
from .conversations import ConversationsClient
from .opportunities import OpportunitiesClient
from .calendars import CalendarsClient
from .forms import FormsClient
from .businesses import BusinessesClient
from .users import UsersClient
from .campaigns import CampaignsClient
from .workflows import WorkflowsClient
from .locations import LocationsClient
from .locations_extended import LocationsExtendedClient
from .calendar_admin import CalendarAdminClient
from .products import ProductsClient
from .payments import PaymentsClient
from .links import LinksClient
from .surveys import SurveysClient
from .oauth_management import OAuthManagementClient


class GoHighLevelClient:
    """Main client for interacting with GoHighLevel API v2

    Uses composition pattern to delegate to specialized endpoint clients
    while maintaining the same public interface for backward compatibility.
    """

    def __init__(self, oauth_service: OAuthService):
        self.oauth_service = oauth_service

        # Initialize specialized clients
        self._contacts = ContactsClient(oauth_service)
        self._conversations = ConversationsClient(oauth_service)
        self._opportunities = OpportunitiesClient(oauth_service)
        self._calendars = CalendarsClient(oauth_service)
        self._forms = FormsClient(oauth_service)
        self._businesses = BusinessesClient(oauth_service)
        self._users = UsersClient(oauth_service)
        self._campaigns = CampaignsClient(oauth_service)
        self._workflows = WorkflowsClient(oauth_service)
        self._locations = LocationsClient(oauth_service)
        self._locations_extended = LocationsExtendedClient(oauth_service)
        self._calendar_admin = CalendarAdminClient(oauth_service)
        self._products = ProductsClient(oauth_service)
        self._payments = PaymentsClient(oauth_service)
        self._links = LinksClient(oauth_service)
        self._surveys = SurveysClient(oauth_service)
        self._oauth_management = OAuthManagementClient(oauth_service)

    async def __aenter__(self):
        # Enter all specialized clients
        await self._contacts.__aenter__()
        await self._conversations.__aenter__()
        await self._opportunities.__aenter__()
        await self._calendars.__aenter__()
        await self._forms.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # Exit all specialized clients
        await self._contacts.__aexit__(exc_type, exc_val, exc_tb)
        await self._conversations.__aexit__(exc_type, exc_val, exc_tb)
        await self._opportunities.__aexit__(exc_type, exc_val, exc_tb)
        await self._calendars.__aexit__(exc_type, exc_val, exc_tb)
        await self._forms.__aexit__(exc_type, exc_val, exc_tb)

    # Location Methods (keeping these in main client for now)

    async def get_locations(self, limit: int = 100, skip: int = 0) -> Dict[str, Any]:
        """Get all locations"""
        # Use the first available client for the request
        response = await self._contacts._request(
            "GET", "/locations/search", params={"limit": limit, "skip": skip}
        )
        return response.json()

    async def get_location(self, location_id: str) -> Dict[str, Any]:
        """Get a specific location"""
        response = await self._contacts._request("GET", f"/locations/{location_id}")
        return response.json()

    # Contact Methods - Delegate to ContactsClient

    async def get_contacts(
        self,
        location_id: str,
        limit: int = 100,
        skip: int = 0,
        query: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> ContactList:
        """Get contacts for a location"""
        return await self._contacts.get_contacts(
            location_id=location_id,
            limit=limit,
            skip=skip,
            query=query,
            email=email,
            phone=phone,
            tags=tags,
        )

    async def get_contact(self, contact_id: str, location_id: str) -> Contact:
        """Get a specific contact"""
        return await self._contacts.get_contact(contact_id, location_id)

    async def create_contact(self, contact: ContactCreate) -> Contact:
        """Create a new contact"""
        return await self._contacts.create_contact(contact)

    async def update_contact(
        self, contact_id: str, updates: ContactUpdate, location_id: str
    ) -> Contact:
        """Update an existing contact"""
        return await self._contacts.update_contact(contact_id, updates, location_id)

    async def delete_contact(self, contact_id: str, location_id: str) -> bool:
        """Delete a contact"""
        return await self._contacts.delete_contact(contact_id, location_id)

    async def add_contact_tags(
        self, contact_id: str, tags: List[str], location_id: str
    ) -> Contact:
        """Add tags to a contact"""
        return await self._contacts.add_contact_tags(contact_id, tags, location_id)

    async def remove_contact_tags(
        self, contact_id: str, tags: List[str], location_id: str
    ) -> Contact:
        """Remove tags from a contact"""
        return await self._contacts.remove_contact_tags(contact_id, tags, location_id)

    # Contact Tasks Methods - Delegate to ContactsClient

    async def get_contact_tasks(self, contact_id: str, location_id: str) -> TaskList:
        """Get all tasks for a contact"""
        return await self._contacts.get_contact_tasks(contact_id, location_id)

    async def get_contact_task(
        self, contact_id: str, task_id: str, location_id: str
    ) -> Task:
        """Get a specific task for a contact"""
        return await self._contacts.get_contact_task(contact_id, task_id, location_id)

    async def create_contact_task(
        self, contact_id: str, task: TaskCreate, location_id: str
    ) -> Task:
        """Create a new task for a contact"""
        return await self._contacts.create_contact_task(contact_id, task, location_id)

    async def update_contact_task(
        self, contact_id: str, task_id: str, updates: TaskUpdate, location_id: str
    ) -> Task:
        """Update an existing task for a contact"""
        return await self._contacts.update_contact_task(
            contact_id, task_id, updates, location_id
        )

    async def delete_contact_task(
        self, contact_id: str, task_id: str, location_id: str
    ) -> bool:
        """Delete a task for a contact"""
        return await self._contacts.delete_contact_task(contact_id, task_id, location_id)

    async def complete_contact_task(
        self, contact_id: str, task_id: str, completed: bool, location_id: str
    ) -> Task:
        """Mark a contact task as completed or incomplete"""
        return await self._contacts.complete_contact_task(
            contact_id, task_id, completed, location_id
        )

    # Contact Notes Methods - Delegate to ContactsClient

    async def get_contact_notes(self, contact_id: str, location_id: str) -> NoteList:
        """Get all notes for a contact"""
        return await self._contacts.get_contact_notes(contact_id, location_id)

    async def get_contact_note(
        self, contact_id: str, note_id: str, location_id: str
    ) -> Note:
        """Get a specific note for a contact"""
        return await self._contacts.get_contact_note(contact_id, note_id, location_id)

    async def create_contact_note(
        self, contact_id: str, note: NoteCreate, location_id: str
    ) -> Note:
        """Create a new note for a contact"""
        return await self._contacts.create_contact_note(contact_id, note, location_id)

    async def update_contact_note(
        self, contact_id: str, note_id: str, updates: NoteUpdate, location_id: str
    ) -> Note:
        """Update an existing note for a contact"""
        return await self._contacts.update_contact_note(
            contact_id, note_id, updates, location_id
        )

    async def delete_contact_note(
        self, contact_id: str, note_id: str, location_id: str
    ) -> bool:
        """Delete a note for a contact"""
        return await self._contacts.delete_contact_note(contact_id, note_id, location_id)

    # Contact Campaign/Workflow Assignment Methods - Delegate to ContactsClient

    async def add_contact_to_campaign(
        self, contact_id: str, campaign_id: str, location_id: str
    ) -> bool:
        """Add a contact to a campaign"""
        return await self._contacts.add_contact_to_campaign(contact_id, campaign_id, location_id)

    async def remove_contact_from_campaign(
        self, contact_id: str, campaign_id: str, location_id: str
    ) -> bool:
        """Remove a contact from a specific campaign"""
        return await self._contacts.remove_contact_from_campaign(contact_id, campaign_id, location_id)

    async def remove_contact_from_all_campaigns(
        self, contact_id: str, location_id: str
    ) -> bool:
        """Remove a contact from all campaigns"""
        return await self._contacts.remove_contact_from_all_campaigns(contact_id, location_id)

    async def add_contact_to_workflow(
        self, contact_id: str, workflow_id: str, location_id: str
    ) -> bool:
        """Add a contact to a workflow"""
        return await self._contacts.add_contact_to_workflow(contact_id, workflow_id, location_id)

    async def remove_contact_from_workflow(
        self, contact_id: str, workflow_id: str, location_id: str
    ) -> bool:
        """Remove a contact from a workflow"""
        return await self._contacts.remove_contact_from_workflow(contact_id, workflow_id, location_id)

    # Conversation Methods - Delegate to ConversationsClient

    async def get_conversations(
        self,
        location_id: str,
        limit: int = 100,
        skip: int = 0,
        contact_id: Optional[str] = None,
        starred: Optional[bool] = None,
        unread_only: Optional[bool] = None,
    ) -> ConversationList:
        """Get conversations for a location"""
        return await self._conversations.get_conversations(
            location_id=location_id,
            limit=limit,
            skip=skip,
            contact_id=contact_id,
            starred=starred,
            unread_only=unread_only,
        )

    async def get_conversation(
        self, conversation_id: str, location_id: str
    ) -> Conversation:
        """Get a specific conversation"""
        return await self._conversations.get_conversation(conversation_id, location_id)

    async def create_conversation(
        self, conversation: ConversationCreate
    ) -> Conversation:
        """Create a new conversation"""
        return await self._conversations.create_conversation(conversation)

    async def get_messages(
        self, conversation_id: str, location_id: str, limit: int = 100, skip: int = 0
    ) -> MessageList:
        """Get messages for a conversation"""
        return await self._conversations.get_messages(
            conversation_id, location_id, limit, skip
        )

    async def send_message(
        self, conversation_id: str, message: MessageCreate, location_id: str
    ) -> Message:
        """Send a message in a conversation"""
        return await self._conversations.send_message(
            conversation_id, message, location_id
        )

    async def update_message_status(
        self, message_id: str, status: str, location_id: str
    ) -> Message:
        """Update the status of a message"""
        return await self._conversations.update_message_status(
            message_id, status, location_id
        )

    # Opportunity Methods - Delegate to OpportunitiesClient

    async def get_opportunities(
        self,
        location_id: str,
        limit: int = 100,
        skip: int = 0,
        filters: Optional[OpportunitySearchFilters] = None,
    ) -> OpportunitySearchResult:
        """Get opportunities for a location"""
        return await self._opportunities.get_opportunities(
            location_id=location_id, limit=limit, skip=skip, filters=filters
        )

    async def get_opportunity(
        self, opportunity_id: str, location_id: str
    ) -> Opportunity:
        """Get a specific opportunity"""
        return await self._opportunities.get_opportunity(opportunity_id, location_id)

    async def create_opportunity(self, opportunity: OpportunityCreate) -> Opportunity:
        """Create a new opportunity"""
        return await self._opportunities.create_opportunity(opportunity)

    async def update_opportunity(
        self, opportunity_id: str, updates: OpportunityUpdate, location_id: str
    ) -> Opportunity:
        """Update an existing opportunity"""
        return await self._opportunities.update_opportunity(
            opportunity_id, updates, location_id
        )

    async def delete_opportunity(self, opportunity_id: str, location_id: str) -> bool:
        """Delete an opportunity"""
        return await self._opportunities.delete_opportunity(opportunity_id, location_id)

    async def update_opportunity_status(
        self, opportunity_id: str, status: str, location_id: str
    ) -> Opportunity:
        """Update opportunity status"""
        return await self._opportunities.update_opportunity_status(
            opportunity_id, status, location_id
        )

    async def get_pipelines(self, location_id: str) -> List[Pipeline]:
        """Get all pipelines for a location

        NOTE: This is the only pipeline endpoint that exists in the API.
        Individual pipeline and stage endpoints do not exist.
        """
        return await self._opportunities.get_pipelines(location_id)

    # Calendar Methods - Delegate to CalendarsClient

    async def get_appointments(
        self,
        contact_id: str,
        location_id: str,
    ) -> AppointmentList:
        """Get appointments for a contact"""
        return await self._calendars.get_appointments(
            contact_id=contact_id,
            location_id=location_id,
        )

    async def get_appointment(
        self, appointment_id: str, location_id: str
    ) -> Appointment:
        """Get a specific appointment"""
        return await self._calendars.get_appointment(appointment_id, location_id)

    async def create_appointment(self, appointment: AppointmentCreate) -> Appointment:
        """Create a new appointment"""
        return await self._calendars.create_appointment(appointment)

    async def update_appointment(
        self, appointment_id: str, updates: AppointmentUpdate, location_id: str
    ) -> Appointment:
        """Update an existing appointment"""
        return await self._calendars.update_appointment(
            appointment_id, updates, location_id
        )

    async def delete_appointment(self, appointment_id: str, location_id: str) -> bool:
        """Delete an appointment"""
        return await self._calendars.delete_appointment(appointment_id, location_id)

    async def get_calendars(self, location_id: str) -> CalendarList:
        """Get all calendars for a location"""
        return await self._calendars.get_calendars(location_id)

    async def get_calendar(self, calendar_id: str, location_id: str) -> Calendar:
        """Get a specific calendar"""
        return await self._calendars.get_calendar(calendar_id, location_id)

    async def get_free_slots(
        self,
        calendar_id: str,
        location_id: str,
        start_date: date,
        end_date: Optional[date] = None,
        timezone: Optional[str] = None,
    ) -> FreeSlotsResult:
        """Get available time slots for a calendar"""
        return await self._calendars.get_free_slots(
            calendar_id, location_id, start_date, end_date, timezone
        )

    # Form Methods - Delegate to FormsClient

    async def get_forms(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> FormList:
        """Get all forms for a location"""
        return await self._forms.get_forms(location_id, limit, skip)

    async def get_all_submissions(
        self,
        location_id: str,
        form_id: Optional[str] = None,
        contact_id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        limit: int = 100,
        skip: int = 0,
    ) -> FormSubmissionList:
        """Get all form submissions for a location"""
        return await self._forms.get_all_submissions(
            location_id, form_id, contact_id, start_date, end_date, limit, skip
        )

    async def upload_form_file(
        self, file_upload: FormFileUploadRequest
    ) -> Dict[str, Any]:
        """Upload a file to a form's custom field"""
        return await self._forms.upload_form_file(file_upload)

    # Business Methods - Delegate to BusinessesClient

    async def get_businesses(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> BusinessList:
        """Get all businesses for a location"""
        return await self._businesses.get_businesses(location_id, limit, skip)

    async def get_business(self, business_id: str, location_id: str) -> Business:
        """Get a specific business"""
        return await self._businesses.get_business(business_id, location_id)

    async def create_business(self, business: BusinessCreate) -> Business:
        """Create a new business"""
        return await self._businesses.create_business(business)

    async def update_business(
        self, business_id: str, updates: BusinessUpdate, location_id: str
    ) -> Business:
        """Update an existing business"""
        return await self._businesses.update_business(business_id, updates, location_id)

    async def delete_business(self, business_id: str, location_id: str) -> bool:
        """Delete a business"""
        return await self._businesses.delete_business(business_id, location_id)

    # User Methods - Delegate to UsersClient

    async def get_users(
        self, location_id: Optional[str] = None, limit: int = 100, skip: int = 0
    ) -> UserList:
        """Get all users"""
        return await self._users.get_users(location_id, limit, skip)

    async def get_user(self, user_id: str) -> User:
        """Get a specific user"""
        return await self._users.get_user(user_id)

    async def create_user(self, user: UserCreate) -> User:
        """Create a new user"""
        return await self._users.create_user(user)

    async def update_user(self, user_id: str, updates: UserUpdate) -> User:
        """Update an existing user"""
        return await self._users.update_user(user_id, updates)

    async def delete_user(self, user_id: str) -> bool:
        """Delete a user"""
        return await self._users.delete_user(user_id)

    # Campaign Methods - Delegate to CampaignsClient

    async def get_campaigns(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> CampaignList:
        """Get all campaigns for a location"""
        return await self._campaigns.get_campaigns(location_id, limit, skip)

    # Workflow Methods - Delegate to WorkflowsClient

    async def get_workflows(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> WorkflowList:
        """Get all workflows for a location"""
        return await self._workflows.get_workflows(location_id, limit, skip)

    # Location Methods - Delegate to LocationsClient

    async def get_location(self, location_id: str) -> Location:
        """Get a specific location"""
        return await self._locations.get_location(location_id)

    async def search_locations(
        self,
        company_id: Optional[str] = None,
        limit: int = 100,
        skip: int = 0,
        search_query: Optional[str] = None
    ) -> LocationList:
        """Search locations with filters"""
        return await self._locations.search_locations(company_id, limit, skip, search_query)

    async def create_location(self, location: LocationCreate) -> Location:
        """Create a new location"""
        return await self._locations.create_location(location)

    async def update_location(self, location_id: str, updates: LocationUpdate) -> Location:
        """Update an existing location"""
        return await self._locations.update_location(location_id, updates)

    async def delete_location(self, location_id: str) -> bool:
        """Delete a location"""
        return await self._locations.delete_location(location_id)

    # Calendar Administration Methods - Delegate to CalendarAdminClient

    async def create_calendar(self, calendar: CalendarCreate) -> Calendar:
        """Create a new calendar"""
        return await self._calendar_admin.create_calendar(calendar)

    async def update_calendar(self, calendar_id: str, updates: CalendarUpdate) -> Calendar:
        """Update an existing calendar"""
        return await self._calendar_admin.update_calendar(calendar_id, updates)

    async def delete_calendar(self, calendar_id: str) -> bool:
        """Delete a calendar"""
        return await self._calendar_admin.delete_calendar(calendar_id)

    async def get_calendar_groups(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> CalendarGroupList:
        """Get calendar groups for a location"""
        return await self._calendar_admin.get_calendar_groups(location_id, limit, skip)

    # Calendar Events Management Methods - Delegate to CalendarAdminClient

    async def delete_calendar_event(self, event_id: str, location_id: str) -> bool:
        """Delete a calendar event"""
        return await self._calendar_admin.delete_calendar_event(event_id, location_id)

    async def create_block_slot(self, block_slot_data: dict, location_id: str) -> dict:
        """Create a calendar block slot"""
        return await self._calendar_admin.create_block_slot(block_slot_data, location_id)

    async def update_block_slot(self, event_id: str, block_slot_data: dict, location_id: str) -> dict:
        """Update a calendar block slot"""
        return await self._calendar_admin.update_block_slot(event_id, block_slot_data, location_id)

    # Product Methods - Delegate to ProductsClient

    async def get_products(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> ProductList:
        """Get all products for a location"""
        return await self._products.get_products(location_id, limit, skip)

    async def get_product(self, product_id: str, location_id: str) -> Product:
        """Get a specific product"""
        return await self._products.get_product(product_id, location_id)

    async def create_product(self, product: ProductCreate) -> Product:
        """Create a new product"""
        return await self._products.create_product(product)

    async def update_product(
        self, product_id: str, updates: ProductUpdate, location_id: str
    ) -> Product:
        """Update an existing product"""
        return await self._products.update_product(product_id, updates, location_id)

    async def delete_product(self, product_id: str, location_id: str) -> bool:
        """Delete a product"""
        return await self._products.delete_product(product_id, location_id)

    # Product Price Methods - Delegate to ProductsClient

    async def get_product_prices(
        self, product_id: str, location_id: str, limit: int = 100, skip: int = 0
    ) -> ProductPriceList:
        """Get all prices for a product"""
        return await self._products.get_product_prices(product_id, location_id, limit, skip)

    async def get_product_price(
        self, product_id: str, price_id: str, location_id: str
    ) -> ProductPrice:
        """Get a specific product price"""
        return await self._products.get_product_price(product_id, price_id, location_id)

    async def create_product_price(
        self, product_id: str, price: ProductPriceCreate, location_id: str
    ) -> ProductPrice:
        """Create a new product price"""
        return await self._products.create_product_price(product_id, price, location_id)

    async def update_product_price(
        self, product_id: str, price_id: str, updates: ProductPriceUpdate, location_id: str
    ) -> ProductPrice:
        """Update an existing product price"""
        return await self._products.update_product_price(product_id, price_id, updates, location_id)

    async def delete_product_price(
        self, product_id: str, price_id: str, location_id: str
    ) -> bool:
        """Delete a product price"""
        return await self._products.delete_product_price(product_id, price_id, location_id)

    # Payment Methods - Delegate to PaymentsClient

    async def get_payment_orders(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> PaymentOrderList:
        """Get all payment orders for a location"""
        return await self._payments.get_payment_orders(location_id, limit, skip)

    async def get_payment_order(self, order_id: str, location_id: str) -> PaymentOrder:
        """Get a specific payment order"""
        return await self._payments.get_payment_order(order_id, location_id)

    async def get_order_fulfillments(
        self, order_id: str, location_id: str, limit: int = 100, skip: int = 0
    ) -> PaymentOrderFulfillmentList:
        """Get all fulfillments for a payment order"""
        return await self._payments.get_order_fulfillments(order_id, location_id, limit, skip)

    async def create_order_fulfillment(
        self, order_id: str, fulfillment: PaymentOrderFulfillmentCreate, location_id: str
    ) -> PaymentOrderFulfillment:
        """Create a new fulfillment for a payment order"""
        return await self._payments.create_order_fulfillment(order_id, fulfillment, location_id)

    async def get_payment_subscriptions(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> PaymentSubscriptionList:
        """Get all payment subscriptions for a location"""
        return await self._payments.get_payment_subscriptions(location_id, limit, skip)

    async def get_payment_subscription(self, subscription_id: str, location_id: str) -> PaymentSubscription:
        """Get a specific payment subscription"""
        return await self._payments.get_payment_subscription(subscription_id, location_id)

    async def get_payment_transactions(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> PaymentTransactionList:
        """Get all payment transactions for a location"""
        return await self._payments.get_payment_transactions(location_id, limit, skip)

    async def get_payment_transaction(self, transaction_id: str, location_id: str) -> PaymentTransaction:
        """Get a specific payment transaction"""
        return await self._payments.get_payment_transaction(transaction_id, location_id)

    async def get_payment_integration(self, location_id: str) -> PaymentIntegration:
        """Get the whitelabel payment integration for a location"""
        return await self._payments.get_payment_integration(location_id)

    async def create_payment_integration(
        self, integration: PaymentIntegrationCreate, location_id: str
    ) -> PaymentIntegration:
        """Create or configure a whitelabel payment integration"""
        return await self._payments.create_payment_integration(integration, location_id)

    # Location Tags Methods - Delegate to LocationsExtendedClient

    async def get_location_tags(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> LocationTagList:
        """Get all tags for a location"""
        return await self._locations_extended.get_location_tags(location_id, limit, skip)

    async def get_location_tag(self, location_id: str, tag_id: str) -> LocationTag:
        """Get a specific location tag"""
        return await self._locations_extended.get_location_tag(location_id, tag_id)

    async def create_location_tag(self, location_id: str, tag: LocationTagCreate) -> LocationTag:
        """Create a new location tag"""
        return await self._locations_extended.create_location_tag(location_id, tag)

    async def update_location_tag(self, location_id: str, tag_id: str, tag: LocationTagUpdate) -> LocationTag:
        """Update a location tag"""
        return await self._locations_extended.update_location_tag(location_id, tag_id, tag)

    async def delete_location_tag(self, location_id: str, tag_id: str) -> Dict[str, Any]:
        """Delete a location tag"""
        return await self._locations_extended.delete_location_tag(location_id, tag_id)

    # Location Custom Values Methods - Delegate to LocationsExtendedClient

    async def get_location_custom_values(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> LocationCustomValueList:
        """Get all custom values for a location"""
        return await self._locations_extended.get_location_custom_values(location_id, limit, skip)

    async def get_location_custom_value(self, location_id: str, custom_value_id: str) -> LocationCustomValue:
        """Get a specific location custom value"""
        return await self._locations_extended.get_location_custom_value(location_id, custom_value_id)

    async def create_location_custom_value(self, location_id: str, custom_value: LocationCustomValueCreate) -> LocationCustomValue:
        """Create a new location custom value"""
        return await self._locations_extended.create_location_custom_value(location_id, custom_value)

    async def update_location_custom_value(self, location_id: str, custom_value_id: str, custom_value: LocationCustomValueUpdate) -> LocationCustomValue:
        """Update a location custom value"""
        return await self._locations_extended.update_location_custom_value(location_id, custom_value_id, custom_value)

    async def delete_location_custom_value(self, location_id: str, custom_value_id: str) -> Dict[str, Any]:
        """Delete a location custom value"""
        return await self._locations_extended.delete_location_custom_value(location_id, custom_value_id)

    # Location Custom Fields Methods - Delegate to LocationsExtendedClient

    async def get_location_custom_fields(
        self, location_id: str, limit: int = 100, skip: int = 0
    ) -> LocationCustomFieldList:
        """Get all custom fields for a location"""
        return await self._locations_extended.get_location_custom_fields(location_id, limit, skip)

    async def get_location_custom_field(self, location_id: str, custom_field_id: str) -> LocationCustomField:
        """Get a specific location custom field"""
        return await self._locations_extended.get_location_custom_field(location_id, custom_field_id)

    async def create_location_custom_field(self, location_id: str, custom_field: LocationCustomFieldCreate) -> LocationCustomField:
        """Create a new location custom field"""
        return await self._locations_extended.create_location_custom_field(location_id, custom_field)

    async def update_location_custom_field(self, location_id: str, custom_field_id: str, custom_field: LocationCustomFieldUpdate) -> LocationCustomField:
        """Update a location custom field"""
        return await self._locations_extended.update_location_custom_field(location_id, custom_field_id, custom_field)

    async def delete_location_custom_field(self, location_id: str, custom_field_id: str) -> Dict[str, Any]:
        """Delete a location custom field"""
        return await self._locations_extended.delete_location_custom_field(location_id, custom_field_id)

    # Links Methods - Delegate to LinksClient

    async def get_links(self, location_id: str, limit: int = 100, skip: int = 0) -> LinkList:
        """Get all links for a location"""
        return await self._links.get_links(location_id, limit, skip)

    async def get_link(self, link_id: str, location_id: str) -> Link:
        """Get a specific link"""
        return await self._links.get_link(link_id, location_id)

    async def create_link(self, link: LinkCreate, location_id: str) -> Link:
        """Create a new link"""
        return await self._links.create_link(link, location_id)

    async def update_link(self, link_id: str, link: LinkUpdate, location_id: str) -> Link:
        """Update a link"""
        return await self._links.update_link(link_id, link, location_id)

    async def delete_link(self, link_id: str, location_id: str) -> Dict[str, Any]:
        """Delete a link"""
        return await self._links.delete_link(link_id, location_id)

    # Surveys Methods - Delegate to SurveysClient

    async def get_surveys(self, location_id: str, limit: int = 100, skip: int = 0) -> SurveyList:
        """Get all surveys for a location"""
        return await self._surveys.get_surveys(location_id, limit, skip)

    async def get_survey(self, survey_id: str, location_id: str) -> Survey:
        """Get a specific survey"""
        return await self._surveys.get_survey(survey_id, location_id)

    async def get_survey_submissions(
        self, location_id: str, survey_id: Optional[str] = None, limit: int = 100, skip: int = 0
    ) -> SurveySubmissionList:
        """Get survey submissions for a location"""
        return await self._surveys.get_survey_submissions(location_id, survey_id, limit, skip)

    # OAuth Management Methods - Delegate to OAuthManagementClient

    async def get_installed_locations(self, limit: int = 100, skip: int = 0) -> InstalledLocationList:
        """Get all locations where the OAuth application is installed"""
        return await self._oauth_management.get_installed_locations(limit, skip)

    async def generate_location_token(self, request: LocationTokenRequest) -> LocationToken:
        """Generate an OAuth token for a specific location"""
        return await self._oauth_management.generate_location_token(request)

    async def update_saas_subscription(self, location_id: str, subscription: SaasSubscriptionUpdate) -> SaasSubscription:
        """Update the SaaS subscription details for a specific location"""
        return await self._oauth_management.update_saas_subscription(location_id, subscription)

    # Location Templates Methods - Delegate to LocationsExtendedClient

    async def get_location_templates(self, location_id: str, limit: int = 100, skip: int = 0) -> LocationTemplateList:
        """Get all templates for a location"""
        return await self._locations_extended.get_location_templates(location_id, limit, skip)

    # Location Tasks Methods - Delegate to LocationsExtendedClient

    async def search_location_tasks(
        self, location_id: str, filters: Optional[LocationTaskSearchFilters] = None, limit: int = 100, skip: int = 0
    ) -> LocationTaskList:
        """Search tasks for a location"""
        return await self._locations_extended.search_location_tasks(location_id, filters, limit, skip)
