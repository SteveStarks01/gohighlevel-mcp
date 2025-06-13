[![Automated Tests](https://github.com/basicmachines-co/open-ghl-mcp/actions/workflows/test.yml/badge.svg)](https://github.com/basicmachines-co/open-ghl-mcp/actions/workflows/test.yml)
# GoHighLevel MCP Server

A comprehensive Model Context Protocol (MCP) server that provides **complete integration** with the GoHighLevel API v2. This server enables AI assistants to interact with **all GoHighLevel functionality** through **115 production-ready tools** covering 100% of available API endpoints - from contact management and messaging to sales pipelines, calendar administration, product management, and payment processing.

## Features

- 🔐 **OAuth 2.0 Authentication**: Full OAuth flow with automatic token management by default
- 🏢 **Multi-location Support**: Works with agency accounts to manage multiple sub-accounts
- 🎯 **Complete API Coverage**: 115 tools covering 100% of GoHighLevel API v2 endpoints
- 👥 **Contact Management**: Complete CRUD operations for contacts, tasks, notes, and assignments
- 💬 **Conversations & Messaging**: Full messaging capabilities (SMS, Email, WhatsApp, etc.)
- 🎯 **Opportunities & Pipelines**: Complete sales pipeline management
- 📅 **Calendar & Appointments**: Full calendar administration and appointment management
- 📝 **Forms & Submissions**: Form management and file uploads
- 🏢 **Business & User Management**: Complete business and user administration
- 📢 **Campaign & Workflow Management**: Campaign and workflow operations
- 📍 **Location Management**: Full location administration with extended features
- 🛍️ **Product & Payment Management**: Complete e-commerce and payment processing
- 🔗 **Link & Survey Management**: Link and survey operations
- 🔐 **OAuth & SaaS Management**: OAuth and SaaS subscription management
- 🔄 **Automatic Token Refresh**: Handles token expiration seamlessly
- 🛠️ **MCP Tools & Resources**: Both tools and resources for flexible integration

## Prerequisites

- Python 3.12+
- `uv` package manager (or pip)
- One of the following:
  - **Standard Mode Configuration**: Access via our hosted GoHighLevel app (coming soon)
  - **Custom Mode Configuration**: Your own GoHighLevel Marketplace App credentials

## Getting Started - Installation

1. Clone the repository:
```bash
git clone https://github.com/basicmachines-co/open-ghl-mcp.git
cd open-ghl-mcp
```
2. Install dependencies:
```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

3. Start the server:
```bash
python -m src.main
```

## 1. Configuration

Use your own GoHighLevel Marketplace App:

1. Create your own GoHighLevel Marketplace App
2. Set the redirect URL to: `http://localhost:8080/oauth/callback`
3. Set the permissions you want for the tools and resources below


## 2. Usage

### Running the MCP Server

1. Start the server:
```bash
python -m src.main
```

2. Complete the setup wizard.

3. Configure your LLM to use the MCP server

### First-time Authentication

#### Custom Mode Setup
1. The server will ask you for your GHL Marketplace App Client ID and Secret
2. Install your App to generate an OAuth Token

## API Reference

This MCP server provides **complete access to GoHighLevel API v2** through both **Tools** (for actions) and **Resources** (for data browsing). With **115 comprehensive tools**, this integration covers **100% of available GoHighLevel API v2 endpoints**. All tools are fully tested, validated, and production-ready.

### 📊 **Complete Coverage Statistics**
- **115 Total Tools** covering all GoHighLevel API v2 endpoints
- **Contact Management**: 22 tools (contacts, tasks, notes, assignments)
- **Conversations & Messaging**: 6 tools (full messaging capabilities)
- **Opportunities & Sales**: 7 tools (complete pipeline management)
- **Calendar & Appointments**: 15 tools (full calendar administration)
- **Forms & Submissions**: 3 tools (form management and uploads)
- **Business & User Management**: 10 tools (complete administration)
- **Campaign & Workflow Management**: 2 tools (automation management)
- **Location Management**: 22 tools (full location administration)
- **Product & Payment Management**: 19 tools (complete e-commerce)
- **Link & Survey Management**: 6 tools (content management)
- **OAuth & SaaS Management**: 3 tools (authentication and subscriptions)

### 🛠️ MCP Tools (Actions)

This MCP server provides **115 comprehensive tools** covering 100% of GoHighLevel API v2 endpoints. All tools are fully tested and production-ready.

#### 👥 Contact Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `create_contact` | `POST /contacts` | Create a new contact |
| `update_contact` | `PUT /contacts/{id}` | Update existing contact |
| `delete_contact` | `DELETE /contacts/{id}` | Delete a contact |
| `get_contact` | `GET /contacts/{id}` | Get a single contact |
| `search_contacts` | `GET /contacts` | Search contacts with filters |
| `add_contact_tags` | `POST /contacts/{id}/tags` | Add tags to a contact |
| `remove_contact_tags` | `DELETE /contacts/{id}/tags` | Remove tags from a contact |

#### 📋 Contact Tasks Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_contact_tasks` | `GET /contacts/{contactId}/tasks` | Get all tasks for a contact |
| `get_contact_task` | `GET /contacts/{contactId}/tasks/{taskId}` | Get a specific contact task |
| `create_contact_task` | `POST /contacts/{contactId}/tasks` | Create new task for contact |
| `update_contact_task` | `PUT /contacts/{contactId}/tasks/{taskId}` | Update existing contact task |
| `delete_contact_task` | `DELETE /contacts/{contactId}/tasks/{taskId}` | Delete a contact task |
| `complete_contact_task` | `PUT /contacts/{contactId}/tasks/{taskId}/completed` | Mark task as completed/incomplete |

#### 📝 Contact Notes Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_contact_notes` | `GET /contacts/{contactId}/notes` | Get all notes for a contact |
| `get_contact_note` | `GET /contacts/{contactId}/notes/{id}` | Get a specific contact note |
| `create_contact_note` | `POST /contacts/{contactId}/notes` | Create new note for contact |
| `update_contact_note` | `PUT /contacts/{contactId}/notes/{id}` | Update existing contact note |
| `delete_contact_note` | `DELETE /contacts/{contactId}/notes/{id}` | Delete a contact note |

#### 🔄 Contact Assignment Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `add_contact_to_campaign` | `POST /contacts/{contactId}/campaigns/{campaignId}` | Add contact to campaign |
| `remove_contact_from_campaign` | `DELETE /contacts/{contactId}/campaigns/{campaignId}` | Remove contact from campaign |
| `remove_contact_from_all_campaigns` | `DELETE /contacts/{contactId}/campaigns/removeAll` | Remove contact from all campaigns |
| `add_contact_to_workflow` | `POST /contacts/{contactId}/workflow/{workflowId}` | Add contact to workflow |
| `remove_contact_from_workflow` | `DELETE /contacts/{contactId}/workflow/{workflowId}` | Remove contact from workflow |

#### 💬 Conversations & Messaging
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_conversations` | `GET /conversations/search` | Search and list conversations |
| `get_conversation` | `GET /conversations/{id}` | Get a single conversation |
| `create_conversation` | `POST /conversations` | Create new conversation |
| `get_messages` | `GET /conversations/{id}/messages` | Get messages from a conversation |
| `send_message` | `POST /conversations/{id}/messages` | Send messages (SMS ✅, Email ✅, WhatsApp, IG, FB, Custom, Live_Chat) |
| `update_message_status` | `PUT /conversations/messages/{messageId}/status` | Update message delivery status |

#### 🎯 Opportunities & Sales Pipeline
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_opportunities` | `GET /opportunities/search` | Search opportunities with filters |
| `get_opportunity` | `GET /opportunities/{id}` | Get a single opportunity |
| `create_opportunity` | `POST /opportunities` | Create new opportunity |
| `update_opportunity` | `PUT /opportunities/{id}` | Update existing opportunity |
| `delete_opportunity` | `DELETE /opportunities/{id}` | Delete opportunity |
| `update_opportunity_status` | `PUT /opportunities/{id}/status` | Update opportunity status |
| `get_pipelines` | `GET /opportunities/pipelines` | List all pipelines with stages |

#### 📅 Calendar & Appointments
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_calendars` | `GET /calendars` | List all calendars for location |
| `get_calendar` | `GET /calendars/{id}` | Get calendar details (54+ fields) |
| `get_appointments` | `GET /contacts/{contactId}/appointments` | Get appointments for contact |
| `get_appointment` | `GET /calendars/events/appointments/{eventId}` | Get single appointment details |
| `create_appointment` | `POST /calendars/events/appointments` | Create new appointment |
| `update_appointment` | `PUT /calendars/events/appointments/{eventId}` | Update existing appointment |
| `delete_appointment` | `DELETE /calendars/events/{eventId}` | Delete appointment |
| `get_free_slots` | `GET /calendars/{id}/free-slots` | Get available time slots |

#### 🔧 Calendar Administration
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `create_calendar` | `POST /calendars` | Create new calendar |
| `update_calendar` | `PUT /calendars/{calendarId}` | Update existing calendar |
| `delete_calendar` | `DELETE /calendars/{calendarId}` | Delete calendar |
| `get_calendar_groups` | `GET /calendars/groups` | Get calendar groups |
| `delete_calendar_event` | `DELETE /calendars/events/{eventId}` | Delete calendar event |
| `create_block_slot` | `POST /calendars/events/block-slots` | Create calendar block slot |
| `update_block_slot` | `PUT /calendars/events/block-slots/{eventId}` | Update calendar block slot |

#### 📝 Forms & Submissions
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_forms` | `GET /forms` | List all forms (basic info: id, name, locationId) |
| `get_all_form_submissions` | `GET /forms/submissions` | Get all submissions with filtering |
| `upload_form_file` | `POST /forms/upload-custom-files` | Upload file to custom field |

> **Note**: Limited API support for forms. The following are NOT available:
> - `GET /forms/{id}` (401 "Route not supported")
> - `GET /forms/{id}/submissions` (404 Not Found)
> - `POST /forms/submit` (401 Unauthorized)

#### 🏢 Business Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_businesses` | `GET /businesses` | List all businesses in location |
| `get_business` | `GET /businesses/{businessId}` | Get details of specific business |
| `create_business` | `POST /businesses` | Create new business entity |
| `update_business` | `PUT /businesses/{businessId}` | Update existing business |
| `delete_business` | `DELETE /businesses/{businessId}` | Delete business entity |

#### 👤 User Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_users` | `GET /users` | List all users in location |
| `get_user` | `GET /users/{userId}` | Get details of specific user |
| `create_user` | `POST /users` | Create new user account |
| `update_user` | `PUT /users/{userId}` | Update existing user |
| `delete_user` | `DELETE /users/{userId}` | Delete user account |

#### 📢 Campaign Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_campaigns` | `GET /campaigns` | List all campaigns in location |

#### ⚡ Workflow Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_workflows` | `GET /workflows` | List all workflows in location |

#### 📍 Location Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_location` | `GET /locations/{locationId}` | Get details of specific location |
| `search_locations` | `GET /locations/search` | Search locations with filters |
| `create_location` | `POST /locations` | Create new location |
| `update_location` | `PUT /locations/{locationId}` | Update existing location |
| `delete_location` | `DELETE /locations/{locationId}` | Delete location |

#### 🏷️ Location Tags Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_location_tags` | `GET /locations/{locationId}/tags` | List all tags for location |
| `get_location_tag` | `GET /locations/{locationId}/tags/{tagId}` | Get specific location tag |
| `create_location_tag` | `POST /locations/{locationId}/tags` | Create new location tag |
| `update_location_tag` | `PUT /locations/{locationId}/tags/{tagId}` | Update location tag |
| `delete_location_tag` | `DELETE /locations/{locationId}/tags/{tagId}` | Delete location tag |

#### 🔧 Location Custom Values
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_location_custom_values` | `GET /locations/{locationId}/customValues` | List location custom values |
| `get_location_custom_value` | `GET /locations/{locationId}/customValues/{id}` | Get specific custom value |
| `create_location_custom_value` | `POST /locations/{locationId}/customValues` | Create new custom value |
| `update_location_custom_value` | `PUT /locations/{locationId}/customValues/{id}` | Update custom value |
| `delete_location_custom_value` | `DELETE /locations/{locationId}/customValues/{id}` | Delete custom value |

#### 📊 Location Custom Fields
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_location_custom_fields` | `GET /locations/{locationId}/customFields` | List location custom fields |
| `get_location_custom_field` | `GET /locations/{locationId}/customFields/{id}` | Get specific custom field |
| `create_location_custom_field` | `POST /locations/{locationId}/customFields` | Create new custom field |
| `update_location_custom_field` | `PUT /locations/{locationId}/customFields/{id}` | Update custom field |
| `delete_location_custom_field` | `DELETE /locations/{locationId}/customFields/{id}` | Delete custom field |

#### 📄 Location Templates
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_location_templates` | `GET /locations/{locationId}/templates` | Get all templates for location |

#### ✅ Location Tasks
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `search_location_tasks` | `POST /locations/{locationId}/tasks/search` | Search tasks for location with filters |

#### 🔗 Link Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_links` | `GET /links` | List all links for location |
| `create_link` | `POST /links` | Create new link |
| `update_link` | `PUT /links/{linkId}` | Update existing link |
| `delete_link` | `DELETE /links/{linkId}` | Delete link |

#### 📊 Survey Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_surveys` | `GET /surveys` | List all surveys for location |
| `get_survey_submissions` | `GET /surveys/submissions` | Get survey submissions with filtering |

#### 🛍️ Product Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_products` | `GET /products` | List all products for location |
| `get_product` | `GET /products/{productId}` | Get details of specific product |
| `create_product` | `POST /products` | Create new product |
| `update_product` | `PUT /products/{productId}` | Update existing product |
| `delete_product` | `DELETE /products/{productId}` | Delete product |

#### 💰 Product Pricing
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_product_prices` | `GET /products/{productId}/price` | List prices for specific product |
| `get_product_price` | `GET /products/{productId}/price/{priceId}` | Get specific product price |
| `create_product_price` | `POST /products/{productId}/price` | Create new product price |
| `update_product_price` | `PUT /products/{productId}/price/{priceId}` | Update product price |
| `delete_product_price` | `DELETE /products/{productId}/price/{priceId}` | Delete product price |

#### 💳 Payment Orders
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_payment_orders` | `GET /payments/orders` | List all payment orders |
| `get_payment_order` | `GET /payments/orders/{orderId}` | Get specific payment order |
| `get_order_fulfillments` | `GET /payments/orders/{orderId}/fulfillments` | Get order fulfillments |
| `create_order_fulfillment` | `POST /payments/orders/{orderId}/fulfillments` | Create order fulfillment |

#### 🔄 Payment Subscriptions
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_payment_subscriptions` | `GET /payments/subscriptions` | List all payment subscriptions |
| `get_payment_subscription` | `GET /payments/subscriptions/{subscriptionId}` | Get specific subscription |

#### 💸 Payment Transactions
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_payment_transactions` | `GET /payments/transactions` | List all payment transactions |
| `get_payment_transaction` | `GET /payments/transactions/{transactionId}` | Get specific transaction |

#### 🔌 Payment Integration
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_payment_integration` | `GET /payments/integrations/provider/whitelabel` | Get whitelabel payment integration |
| `create_payment_integration` | `POST /payments/integrations/provider/whitelabel` | Create whitelabel payment integration |

#### 🔐 OAuth & SaaS Management
| Tool | GoHighLevel Endpoint | Description |
|------|---------------------|-------------|
| `get_installed_locations` | `GET /oauth/installedLocations` | Get OAuth installed locations |
| `generate_location_token` | `POST /oauth/locationToken` | Generate location token |
| `update_saas_subscription` | `PUT /update-saas-subscription/{locationId}` | Update SaaS subscription |

### 📖 MCP Resources (Data Browsing)

Resources provide read-only access to browse and explore GoHighLevel data through URI-based navigation.

#### 👥 Contact Resources
| Resource URI | GoHighLevel Endpoint | Description |
|-------------|---------------------|-------------|
| `contacts://{location_id}` | `GET /contacts` | Browse all contacts for location |
| `contact://{location_id}/{contact_id}` | `GET /contacts/{id}` | View single contact details |

#### 💬 Conversation Resources
| Resource URI | GoHighLevel Endpoint | Description |
|-------------|---------------------|-------------|
| `conversations://{location_id}` | `GET /conversations/search` | Browse all conversations for location |
| `conversation://{location_id}/{conversation_id}` | `GET /conversations/{id}` | View conversation with messages |

#### 🎯 Opportunity Resources
| Resource URI | GoHighLevel Endpoint | Description |
|-------------|---------------------|-------------|
| `opportunities://{location_id}` | `GET /opportunities/search` | Browse all opportunities for location |
| `opportunity://{location_id}/{opportunity_id}` | `GET /opportunities/{id}` | View single opportunity details |
| `pipelines://{location_id}` | `GET /opportunities/pipelines` | Browse all pipelines with stages |

#### 📅 Calendar Resources
| Resource URI | GoHighLevel Endpoint | Description |
|-------------|---------------------|-------------|
| `calendars://{location_id}` | `GET /calendars` | Browse all calendars for location |
| `calendar://{location_id}/{calendar_id}` | `GET /calendars/{id}` | View calendar details |
| `appointments://{location_id}/{contact_id}` | `GET /contacts/{id}/appointments` | Browse appointments for contact |

#### 🏢 Business Resources
| Resource URI | GoHighLevel Endpoint | Description |
|-------------|---------------------|-------------|
| `businesses://{location_id}` | `GET /businesses` | Browse all businesses for location |
| `business://{location_id}/{business_id}` | `GET /businesses/{id}` | View single business details |

#### 👤 User Resources
| Resource URI | GoHighLevel Endpoint | Description |
|-------------|---------------------|-------------|
| `users://{location_id}` | `GET /users` | Browse all users for location |
| `user://{location_id}/{user_id}` | `GET /users/{id}` | View single user details |

#### 🛍️ Product Resources
| Resource URI | GoHighLevel Endpoint | Description |
|-------------|---------------------|-------------|
| `products://{location_id}` | `GET /products` | Browse all products for location |
| `product://{location_id}/{product_id}` | `GET /products/{id}` | View single product details |

### 🔐 Authentication Requirements

All endpoints require proper authentication:

- **Company Token**: Used for location token exchange
- **Location Token**: Required for all location-specific operations (expires every 24 hours)
- **Automatic Refresh**: The MCP server handles token refresh automatically

### 📋 Example Usage

#### Resource Browsing Examples
```bash
# Contact Management
contacts://YOUR_LOCATION_ID                    # Browse all contacts
contact://YOUR_LOCATION_ID/CONTACT_ID          # View contact details

# Conversations & Messaging
conversations://YOUR_LOCATION_ID               # Browse conversations
conversation://YOUR_LOCATION_ID/CONVERSATION_ID # View conversation

# Opportunities & Sales
opportunities://YOUR_LOCATION_ID               # Browse opportunities
opportunity://YOUR_LOCATION_ID/OPPORTUNITY_ID  # View opportunity
pipelines://YOUR_LOCATION_ID                   # Browse pipelines

# Calendar & Appointments
calendars://YOUR_LOCATION_ID                   # Browse calendars
calendar://YOUR_LOCATION_ID/CALENDAR_ID        # View calendar
appointments://YOUR_LOCATION_ID/CONTACT_ID     # Browse appointments

# Business & User Management
businesses://YOUR_LOCATION_ID                  # Browse businesses
business://YOUR_LOCATION_ID/BUSINESS_ID        # View business
users://YOUR_LOCATION_ID                       # Browse users
user://YOUR_LOCATION_ID/USER_ID                # View user

# Product Management
products://YOUR_LOCATION_ID                    # Browse products
product://YOUR_LOCATION_ID/PRODUCT_ID          # View product
```

#### Tool Usage Examples
```bash
# Contact Operations
create_contact                                  # Create new contact
update_contact                                  # Update contact
add_contact_tags                               # Add tags to contact
create_contact_task                            # Create task for contact
create_contact_note                            # Create note for contact

# Messaging Operations
send_message                                   # Send SMS/Email/WhatsApp
get_conversations                              # Search conversations
update_message_status                          # Update message status

# Sales Operations
create_opportunity                             # Create new opportunity
update_opportunity_status                      # Update opportunity status
get_pipelines                                  # Get sales pipelines

# Calendar Operations
create_appointment                             # Create appointment
get_free_slots                                 # Get available slots
create_calendar                                # Create new calendar

# Business Operations
create_business                                # Create business
create_user                                    # Create user account
get_campaigns                                  # List campaigns
get_workflows                                  # List workflows

# Product & Payment Operations
create_product                                 # Create product
create_product_price                           # Create product price
get_payment_orders                             # List payment orders
get_payment_transactions                       # List transactions
```

## Development

### Testing

For local testing with real GoHighLevel accounts, you'll need:
- A GoHighLevel account with API access
- At least one sub-account (location) for testing
- Test contacts and data in your GoHighLevel instance

Create your own testing guidelines and keep sensitive data like location IDs and contact IDs in local files that are not committed to the repository.

### Running Tests

```bash
# Run all tests
uv run pytest

# Run tests with coverage report
uv run pytest --cov=src --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_api_client.py -v
```

### Code Quality

This project uses automated code quality tools. Before committing changes:

```bash
# Format code with Black
uv run black src/ tests/

# Check linting with flake8
uv run flake8 src/ tests/

# Run type checking with mypy
uv run mypy src/ --ignore-missing-imports

# Run all checks at once
uv run black src/ tests/ && uv run flake8 src/ tests/ && uv run mypy src/ --ignore-missing-imports
```

### Pre-commit Hook (optional)

To automatically format code before commits:

```bash
# Create a git pre-commit hook
echo '#!/bin/sh
uv run black src/ tests/
uv run flake8 src/ tests/
' > .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### Continuous Integration

The project uses GitHub Actions for CI/CD:
- Tests run automatically on all pushes and pull requests
- Tested with Python 3.12 and 3.13
- Includes linting, type checking, and test coverage
- Coverage reports are uploaded to Codecov (if configured)

## Architecture

The server follows a modular architecture:

- **OAuth Service**: Handles authentication and token management
- **API Client**: Manages communication with GoHighLevel API
- **MCP Server**: FastMCP-based server exposing tools and resources
- **Data Models**: Pydantic models for data validation

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and feature requests, please use the GitHub issues tracker.
