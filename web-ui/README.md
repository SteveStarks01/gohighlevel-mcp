# GoHighLevel MCP Web UI

A comprehensive web-based AI assistant interface for the GoHighLevel MCP integration. This application transforms the existing 115 MCP tools into an intuitive, conversational interface that can be installed as a GoHighLevel marketplace app.

## 🎯 **Overview**

This web UI provides:
- **Real-time Dashboard** with KPIs and data visualization
- **AI-Powered Chat Interface** using OpenRouter API
- **Natural Language Processing** for all 115 MCP tools
- **GoHighLevel Marketplace Integration** with OAuth 2.0
- **Responsive Design** for desktop and mobile
- **Production-Ready Architecture** with Docker support

## ✨ **Features**

### 📊 **Dashboard**
- Real-time KPI cards (contacts, opportunities, pipeline value, appointments)
- Interactive charts for pipeline and opportunity visualization
- Recent activity feed with live updates
- Auto-refreshing data every 30 seconds
- Responsive design for all screen sizes

### 🤖 **AI Assistant**
- Natural language chat interface powered by OpenRouter
- Intent recognition for 15+ different actions
- Real-time WebSocket communication
- Conversation history and context retention
- Suggested prompts for common tasks
- Data visualization in chat responses
- Support for all 115 MCP tools in the background

### 🔗 **GoHighLevel Integration**
- Complete OAuth 2.0 flow for marketplace installation
- Webhook handling for real-time data updates
- Session management with encrypted user data
- Cross-origin support for iframe embedding
- Automatic token refresh and error handling

## 🚀 **Quick Start**

### Prerequisites
- Docker and Docker Compose
- GoHighLevel Developer Account
- OpenRouter API Key

### Installation

1. **Navigate to the web UI directory:**
   ```bash
   cd web-ui
   ```

2. **Copy and configure environment:**
   ```bash
   cp .env.example .env
   ```

3. **Edit `.env` with your credentials:**
   ```env
   GHL_CLIENT_ID=your_ghl_client_id
   GHL_CLIENT_SECRET=your_ghl_client_secret
   GHL_SHARED_SECRET=your_ghl_shared_secret
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

4. **Start the application:**
   ```bash
   # Using Docker Compose
   docker-compose up -d
   
   # Check status
   docker-compose ps
   ```

5. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🏗️ **Architecture**

### **Backend (Python/FastAPI)**
- FastAPI web server with async/await patterns
- OpenRouter API client for AI functionality
- MCP bridge service connecting to existing 115 tools
- Intent processor for natural language understanding
- WebSocket handler for real-time chat
- OAuth 2.0 authentication with GoHighLevel
- PostgreSQL database with Redis caching

### **Frontend (React/TypeScript)**
- React 18+ with TypeScript and strict type checking
- Tailwind CSS for modern, responsive styling
- Chart.js for interactive data visualization
- WebSocket client for real-time communication
- React Query for efficient data fetching
- Component-based architecture with reusable UI elements

### **Infrastructure**
- Docker containerization for both services
- Docker Compose for local development
- Nginx reverse proxy for production
- Health checks and monitoring
- Environment-based configuration

## 💬 **AI Assistant Capabilities**

The AI assistant can understand and execute natural language requests such as:

- **"Show me today's appointments"** → Executes `get_appointments` with date filter
- **"Create a new contact for John Doe"** → Executes `create_contact` with extracted parameters
- **"What's my pipeline looking like?"** → Executes `get_opportunities` and `get_pipelines`
- **"Send a follow-up message to recent leads"** → Executes `get_contacts` and `send_message`
- **"Schedule a demo for tomorrow"** → Executes `create_appointment` with date parsing

### **Supported Intents**
- Contact management (create, update, search, tasks, notes)
- Conversations and messaging (SMS, email, WhatsApp)
- Opportunities and sales pipeline management
- Calendar and appointment scheduling
- Business and user management
- Analytics and reporting
- Campaign and workflow operations

## 📁 **Project Structure**

```
web-ui/
├── backend/                 # FastAPI backend
│   ├── api/
│   │   ├── routes/         # API route handlers
│   │   ├── services/       # Business logic services
│   │   └── models/         # Data models
│   ├── websockets/         # WebSocket handlers
│   └── main.py            # Application entry point
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── services/       # API clients
│   │   ├── hooks/          # Custom React hooks
│   │   └── types/          # TypeScript definitions
│   └── public/            # Static assets
├── docker/                # Docker configuration
├── docs/                  # Documentation
└── docker-compose.yml     # Service orchestration
```

## 🔧 **Development**

### **Local Development Setup**

1. **Backend development:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```

2. **Frontend development:**
   ```bash
   cd frontend
   npm install
   npm start
   ```

### **Available Scripts**

```bash
# Setup and start services
./setup.sh start

# Stop services
./setup.sh stop

# View logs
./setup.sh logs

# Clean up
./setup.sh clean
```

## 🚀 **Deployment**

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for comprehensive deployment instructions including:

- Docker Compose deployment
- AWS ECS/Lambda deployment
- Google Cloud Run deployment
- Azure Container Instances
- SSL/TLS configuration
- Monitoring and logging setup

## 🔒 **Security**

- OAuth 2.0 authentication with GoHighLevel
- Encrypted user session data
- CORS configuration for iframe embedding
- Rate limiting and input validation
- Secure environment variable management
- HTTPS enforcement in production

## 📊 **Monitoring**

- Health check endpoints for both services
- Structured logging with correlation IDs
- Error tracking and alerting
- Performance monitoring
- Real-time metrics dashboard

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 **License**

This project is part of the GoHighLevel MCP integration and follows the same licensing terms as the main project.

## 🆘 **Support**

For support and questions:
- Check the [documentation](docs/)
- Review [deployment guide](docs/DEPLOYMENT.md)
- Open an issue in the repository

---

**Built with ❤️ for the GoHighLevel community**
