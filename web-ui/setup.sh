#!/bin/bash

# GoHighLevel MCP Web UI Setup Script
# This script sets up the development environment for the web UI

set -e

echo "🚀 Setting up GoHighLevel MCP Web UI..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if required tools are installed
check_requirements() {
    print_status "Checking requirements..."
    
    # Check Docker
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi
    
    # Check Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi
    
    # Check Node.js (optional for local development)
    if command -v node &> /dev/null; then
        NODE_VERSION=$(node --version)
        print_success "Node.js found: $NODE_VERSION"
    else
        print_warning "Node.js not found. Required for local development."
    fi
    
    # Check Python (optional for local development)
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_success "Python found: $PYTHON_VERSION"
    else
        print_warning "Python3 not found. Required for local development."
    fi
    
    print_success "Requirements check completed"
}

# Setup environment file
setup_environment() {
    print_status "Setting up environment configuration..."
    
    if [ ! -f .env ]; then
        cp .env.example .env
        print_success "Created .env file from template"
        print_warning "Please edit .env file with your actual configuration values"
        print_warning "Required: GHL_CLIENT_ID, GHL_CLIENT_SECRET, GHL_SHARED_SECRET, OPENROUTER_API_KEY"
    else
        print_warning ".env file already exists. Skipping creation."
    fi
}

# Setup backend
setup_backend() {
    print_status "Setting up backend..."
    
    cd backend
    
    # Create virtual environment if Python is available
    if command -v python3 &> /dev/null; then
        if [ ! -d "venv" ]; then
            python3 -m venv venv
            print_success "Created Python virtual environment"
        fi
        
        # Activate virtual environment and install dependencies
        source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null || true
        
        if [ -f "requirements.txt" ]; then
            pip install -r requirements.txt
            print_success "Installed Python dependencies"
        fi
    else
        print_warning "Python3 not available. Skipping local backend setup."
    fi
    
    cd ..
}

# Setup frontend
setup_frontend() {
    print_status "Setting up frontend..."
    
    cd frontend
    
    # Install Node.js dependencies if Node is available
    if command -v npm &> /dev/null; then
        if [ -f "package.json" ]; then
            npm install
            print_success "Installed Node.js dependencies"
        fi
    else
        print_warning "npm not available. Skipping local frontend setup."
    fi
    
    cd ..
}

# Setup Docker environment
setup_docker() {
    print_status "Setting up Docker environment..."
    
    # Create necessary directories
    mkdir -p data/postgres
    mkdir -p data/redis
    mkdir -p logs
    
    # Build Docker images
    print_status "Building Docker images..."
    docker-compose build
    
    print_success "Docker environment setup completed"
}

# Start services
start_services() {
    print_status "Starting services with Docker Compose..."
    
    # Start services in detached mode
    docker-compose up -d
    
    # Wait a moment for services to start
    sleep 5
    
    # Check service status
    print_status "Checking service status..."
    docker-compose ps
    
    print_success "Services started successfully!"
    print_status "Frontend: http://localhost:3000"
    print_status "Backend API: http://localhost:8000"
    print_status "API Documentation: http://localhost:8000/docs"
}

# Show logs
show_logs() {
    print_status "Showing service logs (Ctrl+C to exit)..."
    docker-compose logs -f
}

# Main setup function
main() {
    echo "🎯 GoHighLevel MCP Web UI Setup"
    echo "================================"
    
    # Parse command line arguments
    case "${1:-setup}" in
        "setup")
            check_requirements
            setup_environment
            setup_backend
            setup_frontend
            setup_docker
            print_success "Setup completed successfully!"
            echo ""
            echo "Next steps:"
            echo "1. Edit .env file with your configuration"
            echo "2. Run './setup.sh start' to start services"
            echo "3. Visit http://localhost:3000 to access the application"
            ;;
        "start")
            start_services
            ;;
        "stop")
            print_status "Stopping services..."
            docker-compose down
            print_success "Services stopped"
            ;;
        "restart")
            print_status "Restarting services..."
            docker-compose restart
            print_success "Services restarted"
            ;;
        "logs")
            show_logs
            ;;
        "clean")
            print_status "Cleaning up Docker resources..."
            docker-compose down -v
            docker system prune -f
            print_success "Cleanup completed"
            ;;
        "help"|"-h"|"--help")
            echo "Usage: $0 [command]"
            echo ""
            echo "Commands:"
            echo "  setup     - Initial setup (default)"
            echo "  start     - Start services"
            echo "  stop      - Stop services"
            echo "  restart   - Restart services"
            echo "  logs      - Show service logs"
            echo "  clean     - Clean up Docker resources"
            echo "  help      - Show this help message"
            ;;
        *)
            print_error "Unknown command: $1"
            echo "Run '$0 help' for usage information"
            exit 1
            ;;
    esac
}

# Run main function with all arguments
main "$@"
