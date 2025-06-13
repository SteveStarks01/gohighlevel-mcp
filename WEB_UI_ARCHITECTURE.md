# GoHighLevel MCP Web UI Architecture

## 🎯 Project Overview

This document outlines the technical architecture for a comprehensive web-based user interface that transforms the existing GoHighLevel MCP integration into a marketplace app with an AI-powered conversational interface.

## 🏗️ Technical Architecture

### **Core Components**

#### 1. **Backend Layer (Enhanced MCP Server)**
- **Existing MCP Foundation**: Preserve all 115 existing MCP tools
- **Web API Layer**: FastAPI/Express.js REST API wrapper around MCP tools
- **OpenRouter Integration**: Replace Claude API with OpenRouter for AI functionality
- **Authentication Service**: Enhanced OAuth 2.0 for marketplace app installation
- **WebSocket Service**: Real-time communication for chat interface

#### 2. **Frontend Layer (React/Vue.js Dashboard)**
- **Dashboard Component**: Real-time metrics and KPI visualization
- **Chat Interface Component**: Conversational AI assistant
- **Authentication Component**: OAuth flow handling
- **Data Visualization**: Charts and graphs for GoHighLevel data

#### 3. **AI Processing Layer**
- **OpenRouter API Client**: Natural language processing
- **Intent Recognition**: Parse user requests and map to MCP tools
- **Context Management**: Maintain conversation history and user context
- **Response Generation**: Convert MCP tool results to natural language

### **Technology Stack**

#### **Backend Technologies**
```
- Python 3.12+ (existing MCP server)
- FastAPI (web API layer)
- WebSockets (real-time communication)
- OpenRouter API (AI processing)
- PostgreSQL/SQLite (conversation history)
- Redis (session management)
```

#### **Frontend Technologies**
```
- React.js 18+ with TypeScript
- Tailwind CSS (styling)
- Chart.js/Recharts (data visualization)
- Socket.io-client (WebSocket client)
- Axios (HTTP client)
- React Query (state management)
```

#### **Infrastructure**
```
- Docker (containerization)
- Nginx (reverse proxy)
- SSL/TLS certificates
- Environment-based configuration
```

## 🔐 Authentication & Security

### **OAuth 2.0 Marketplace Integration**
```
1. App Installation Flow:
   - User installs app from GoHighLevel marketplace
   - Redirect to billing URL with installation parameters
   - OAuth consent flow for required scopes
   - Store installation details and tokens

2. User Session Management:
   - Decrypt user session data using shared secret
   - Maintain user context (agency/location)
   - Handle token refresh automatically
```

### **Required OAuth Scopes**
```
- contacts.readonly, contacts.write
- conversations.readonly, conversations.write
- opportunities.readonly, opportunities.write
- calendars.readonly, calendars.write
- businesses.readonly, businesses.write
- users.readonly, users.write
- campaigns.readonly
- workflows.readonly
- locations.readonly, locations.write
- products.readonly, products.write
- payments/orders.readonly
- oauth.readonly, oauth.write
```

## 🎨 User Interface Design

### **Dashboard Layout**
```
┌─────────────────────────────────────────────────┐
│ Header: Logo, User Info, Settings              │
├─────────────────────────────────────────────────┤
│ KPI Cards Row:                                  │
│ [Contacts] [Opportunities] [Appointments] [$$] │
├─────────────────────────────────────────────────┤
│ Charts Section:                                 │
│ [Pipeline Chart] [Activity Timeline]           │
├─────────────────────────────────────────────────┤
│ AI Chat Interface:                              │
│ ┌─────────────────────────────────────────────┐ │
│ │ Chat History                                │ │
│ │ ┌─────────────────────────────────────────┐ │ │
│ │ │ User: Show me today's appointments      │ │ │
│ │ │ AI: Here are your 3 appointments...    │ │ │
│ │ └─────────────────────────────────────────┘ │ │
│ │ [Type your message here...] [Send]      │ │ │
│ └─────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────┘
```

### **Chat Interface Features**
- **Natural Language Input**: "Show me contacts created this week"
- **Contextual Responses**: AI understands user's current location/agency
- **Action Execution**: "Create a new contact for John Doe with email john@example.com"
- **Data Visualization**: Inline charts and tables in chat responses
- **Quick Actions**: Suggested actions based on current data

## 🤖 AI Assistant Capabilities

### **Intent Recognition & Tool Mapping**
```python
# Example intent mapping
INTENT_MAPPINGS = {
    "show_contacts": ["get_contacts", "search_contacts"],
    "create_contact": ["create_contact"],
    "schedule_appointment": ["create_appointment", "get_free_slots"],
    "view_opportunities": ["get_opportunities"],
    "send_message": ["send_message", "get_conversations"],
    "view_analytics": ["get_contacts", "get_opportunities", "get_appointments"]
}
```

### **Conversation Flow Examples**
```
User: "Show me today's appointments"
AI: Executes get_appointments → Formats response
Response: "You have 3 appointments today: [list with details]"

User: "Create a contact for Sarah Johnson"
AI: Executes create_contact → Confirms creation
Response: "I've created a new contact for Sarah Johnson. Would you like to add more details?"

User: "What's my pipeline looking like?"
AI: Executes get_opportunities + get_pipelines → Analyzes data
Response: "Your pipeline has $45,000 in opportunities across 3 stages: [breakdown]"
```

## 📁 Project Structure

```
web-ui/
├── backend/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── dashboard.py
│   │   │   ├── chat.py
│   │   │   └── webhooks.py
│   │   ├── services/
│   │   │   ├── openrouter_client.py
│   │   │   ├── mcp_bridge.py
│   │   │   ├── intent_processor.py
│   │   │   └── context_manager.py
│   │   └── models/
│   │       ├── chat.py
│   │       ├── user.py
│   │       └── installation.py
│   ├── websockets/
│   │   └── chat_handler.py
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard/
│   │   │   ├── Chat/
│   │   │   ├── Auth/
│   │   │   └── Common/
│   │   ├── services/
│   │   │   ├── api.ts
│   │   │   ├── websocket.ts
│   │   │   └── auth.ts
│   │   ├── hooks/
│   │   ├── utils/
│   │   └── types/
│   ├── public/
│   └── package.json
├── docker/
│   ├── Dockerfile.backend
│   ├── Dockerfile.frontend
│   └── docker-compose.yml
└── docs/
    ├── API.md
    ├── DEPLOYMENT.md
    └── USER_GUIDE.md
```

## 🚀 Implementation Phases

### **Phase 1: Foundation (Week 1-2)**
- [ ] Set up project structure
- [ ] Create FastAPI web layer around existing MCP tools
- [ ] Implement basic OAuth 2.0 marketplace integration
- [ ] Set up OpenRouter API client

### **Phase 2: Dashboard (Week 3-4)**
- [ ] Build React dashboard with KPI cards
- [ ] Implement data visualization components
- [ ] Create real-time data fetching from MCP tools
- [ ] Add responsive design

### **Phase 3: AI Chat Interface (Week 5-6)**
- [ ] Implement WebSocket chat infrastructure
- [ ] Build intent recognition system
- [ ] Create MCP tool mapping and execution
- [ ] Add conversation context management

### **Phase 4: Integration & Testing (Week 7-8)**
- [ ] End-to-end testing
- [ ] Performance optimization
- [ ] Security audit
- [ ] Documentation completion

## 🔧 Development Setup

### **Environment Variables**
```env
# GoHighLevel
GHL_CLIENT_ID=your_client_id
GHL_CLIENT_SECRET=your_client_secret
GHL_SHARED_SECRET=your_shared_secret
GHL_REDIRECT_URI=https://yourapp.com/oauth/callback

# OpenRouter
OPENROUTER_API_KEY=your_openrouter_key
OPENROUTER_MODEL=anthropic/claude-3-sonnet

# Database
DATABASE_URL=postgresql://user:pass@localhost/ghl_mcp
REDIS_URL=redis://localhost:6379

# Security
JWT_SECRET=your_jwt_secret
ENCRYPTION_KEY=your_encryption_key
```

### **Installation Commands**
```bash
# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Frontend setup
cd frontend
npm install
npm run dev

# Docker setup
docker-compose up -d
```

This architecture provides a solid foundation for building a comprehensive web-based AI assistant that leverages all existing MCP functionality while providing an intuitive user interface for GoHighLevel users.

## 🎉 **Implementation Status**

### ✅ **Completed Components**

#### **Backend Infrastructure**
- [x] FastAPI web server with MCP integration
- [x] OpenRouter API client for AI functionality
- [x] MCP bridge service for tool execution
- [x] Intent processor for natural language understanding
- [x] WebSocket handler for real-time chat
- [x] Authentication routes with OAuth 2.0 support
- [x] Dashboard API endpoints with comprehensive data
- [x] Chat API with conversation management
- [x] Webhook handlers for GoHighLevel events
- [x] Data models for users, chat, and sessions

#### **Frontend Application**
- [x] React 18+ with TypeScript setup
- [x] Tailwind CSS for modern styling
- [x] Responsive dashboard with KPI cards
- [x] Real-time chat interface with AI assistant
- [x] Chart.js integration for data visualization
- [x] WebSocket client for real-time communication
- [x] Authentication flow with OAuth callback
- [x] Component library with reusable UI elements
- [x] Suggested prompts and typing indicators
- [x] Message formatting with Markdown support

#### **Infrastructure & DevOps**
- [x] Docker containerization for both services
- [x] Docker Compose for local development
- [x] PostgreSQL and Redis integration
- [x] Environment configuration management
- [x] Health checks and monitoring setup
- [x] Production deployment configurations
- [x] Nginx reverse proxy configuration
- [x] Comprehensive documentation

### 🚀 **Quick Start Guide**

1. **Navigate to the web UI directory:**
   ```bash
   cd web-ui
   ```

2. **Copy and configure environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your GoHighLevel and OpenRouter credentials
   ```

3. **Start the application:**
   ```bash
   # Using the setup script (Linux/Mac)
   ./setup.sh start

   # Or using Docker Compose directly
   docker-compose up -d
   ```

4. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### 📋 **Features Implemented**

#### **Dashboard Features**
- Real-time KPI cards (contacts, opportunities, pipeline value, appointments)
- Interactive charts for pipeline visualization
- Recent activity feed with live updates
- Responsive design for all screen sizes
- Auto-refreshing data every 30 seconds

#### **AI Assistant Features**
- Natural language processing with OpenRouter
- Intent recognition for 15+ different actions
- Real-time WebSocket communication
- Conversation history and context retention
- Suggested prompts for common tasks
- Data visualization in chat responses
- Typing indicators and message status
- Support for all 115 MCP tools in the background

#### **Integration Features**
- Complete OAuth 2.0 flow for GoHighLevel marketplace
- Webhook handling for real-time data updates
- Session management with encrypted user data
- Cross-origin support for iframe embedding
- Automatic token refresh and error handling

### 🔧 **Technical Highlights**

- **100% TypeScript** frontend with strict type checking
- **Async/await patterns** throughout the backend
- **Real-time bidirectional communication** via WebSockets
- **Responsive design** with mobile-first approach
- **Production-ready** Docker containers
- **Comprehensive error handling** and logging
- **Security-first** approach with encryption and validation
- **Scalable architecture** ready for horizontal scaling

This implementation provides a complete, production-ready web-based AI assistant that transforms the existing MCP integration into an intuitive, conversational interface for GoHighLevel users.
