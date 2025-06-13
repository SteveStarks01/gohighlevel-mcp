"""
GoHighLevel MCP Web UI Backend
FastAPI server that provides web interface for the MCP integration
"""

import os
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

# Import existing MCP components
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from src.services.oauth_service import OAuthService
from src.api.client import GoHighLevelClient

# Import new web API components
from api.routes import auth, dashboard, chat, webhooks
from api.services.openrouter_client import OpenRouterClient
from api.services.mcp_bridge import MCPBridge
from websockets.chat_handler import ChatWebSocketHandler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global services
oauth_service: OAuthService = None
ghl_client: GoHighLevelClient = None
openrouter_client: OpenRouterClient = None
mcp_bridge: MCPBridge = None
chat_handler: ChatWebSocketHandler = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager"""
    global oauth_service, ghl_client, openrouter_client, mcp_bridge, chat_handler
    
    logger.info("🚀 Starting GoHighLevel MCP Web UI Backend...")
    
    # Initialize services
    oauth_service = OAuthService()
    ghl_client = GoHighLevelClient(oauth_service)
    openrouter_client = OpenRouterClient()
    mcp_bridge = MCPBridge(ghl_client)
    chat_handler = ChatWebSocketHandler(mcp_bridge, openrouter_client)
    
    logger.info("✅ All services initialized successfully")
    
    yield
    
    logger.info("🛑 Shutting down GoHighLevel MCP Web UI Backend...")


# Create FastAPI app
app = FastAPI(
    title="GoHighLevel MCP Web UI",
    description="Web-based AI assistant interface for GoHighLevel MCP integration",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get services
async def get_oauth_service() -> OAuthService:
    return oauth_service

async def get_ghl_client() -> GoHighLevelClient:
    return ghl_client

async def get_openrouter_client() -> OpenRouterClient:
    return openrouter_client

async def get_mcp_bridge() -> MCPBridge:
    return mcp_bridge

async def get_chat_handler() -> ChatWebSocketHandler:
    return chat_handler

# Include API routes
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])
app.include_router(webhooks.router, prefix="/api/webhooks", tags=["Webhooks"])

# WebSocket endpoint for chat
@app.websocket("/ws/chat")
async def websocket_chat_endpoint(
    websocket,
    chat_handler: ChatWebSocketHandler = Depends(get_chat_handler)
):
    """WebSocket endpoint for real-time chat"""
    await chat_handler.handle_connection(websocket)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "GoHighLevel MCP Web UI",
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint - serves the React app"""
    return {"message": "GoHighLevel MCP Web UI Backend", "status": "running"}

# Serve static files (React build)
if os.path.exists("../frontend/build"):
    app.mount("/static", StaticFiles(directory="../frontend/build/static"), name="static")
    
    @app.get("/{full_path:path}")
    async def serve_react_app(full_path: str):
        """Serve React app for all non-API routes"""
        if full_path.startswith("api/") or full_path.startswith("ws/"):
            raise HTTPException(status_code=404, detail="Not found")
        
        # Serve index.html for all other routes (React Router)
        with open("../frontend/build/index.html", "r") as f:
            return HTMLResponse(content=f.read())

if __name__ == "__main__":
    # Development server
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
