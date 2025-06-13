# Deployment Guide

This guide covers deploying the GoHighLevel MCP Web UI application to various environments.

## 🚀 Quick Start

### Prerequisites

- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.12+ (for local development)
- GoHighLevel Developer Account
- OpenRouter API Key

### Environment Setup

1. **Clone and navigate to the web-ui directory:**
   ```bash
   cd web-ui
   ```

2. **Copy environment file:**
   ```bash
   cp .env.example .env
   ```

3. **Configure environment variables:**
   ```bash
   # Edit .env file with your actual values
   nano .env
   ```

### Docker Deployment (Recommended)

1. **Start all services:**
   ```bash
   docker-compose up -d
   ```

2. **Check service status:**
   ```bash
   docker-compose ps
   ```

3. **View logs:**
   ```bash
   docker-compose logs -f
   ```

4. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## 🏗️ Production Deployment

### Using Docker Compose (Production)

1. **Create production environment file:**
   ```bash
   cp .env.example .env.production
   # Edit with production values
   ```

2. **Build and start production services:**
   ```bash
   docker-compose -f docker-compose.yml --profile production up -d
   ```

### Manual Deployment

#### Backend Deployment

1. **Install dependencies:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   ```bash
   export GHL_CLIENT_ID=your_client_id
   export GHL_CLIENT_SECRET=your_client_secret
   # ... other variables
   ```

3. **Run database migrations:**
   ```bash
   alembic upgrade head
   ```

4. **Start the backend:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

#### Frontend Deployment

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Build for production:**
   ```bash
   npm run build
   ```

3. **Serve with a web server:**
   ```bash
   # Using serve
   npx serve -s build -l 3000
   
   # Or using nginx
   sudo cp -r build/* /var/www/html/
   ```

## ☁️ Cloud Deployment

### AWS Deployment

#### Using AWS ECS with Fargate

1. **Build and push Docker images:**
   ```bash
   # Build images
   docker build -f docker/Dockerfile.backend -t ghl-mcp-backend .
   docker build -f docker/Dockerfile.frontend -t ghl-mcp-frontend .
   
   # Tag for ECR
   docker tag ghl-mcp-backend:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/ghl-mcp-backend:latest
   docker tag ghl-mcp-frontend:latest 123456789012.dkr.ecr.us-east-1.amazonaws.com/ghl-mcp-frontend:latest
   
   # Push to ECR
   docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/ghl-mcp-backend:latest
   docker push 123456789012.dkr.ecr.us-east-1.amazonaws.com/ghl-mcp-frontend:latest
   ```

2. **Create ECS task definition and service**
3. **Set up Application Load Balancer**
4. **Configure RDS for PostgreSQL**
5. **Configure ElastiCache for Redis**

#### Using AWS Lambda (Serverless)

1. **Install Serverless Framework:**
   ```bash
   npm install -g serverless
   ```

2. **Deploy backend as Lambda:**
   ```bash
   cd backend
   serverless deploy
   ```

### Google Cloud Platform

#### Using Google Cloud Run

1. **Build and push to Container Registry:**
   ```bash
   gcloud builds submit --tag gcr.io/PROJECT_ID/ghl-mcp-backend
   gcloud builds submit --tag gcr.io/PROJECT_ID/ghl-mcp-frontend
   ```

2. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy ghl-mcp-backend --image gcr.io/PROJECT_ID/ghl-mcp-backend --platform managed
   gcloud run deploy ghl-mcp-frontend --image gcr.io/PROJECT_ID/ghl-mcp-frontend --platform managed
   ```

### Microsoft Azure

#### Using Azure Container Instances

1. **Create resource group:**
   ```bash
   az group create --name ghl-mcp-rg --location eastus
   ```

2. **Deploy containers:**
   ```bash
   az container create --resource-group ghl-mcp-rg --name ghl-mcp-backend --image ghl-mcp-backend:latest
   az container create --resource-group ghl-mcp-rg --name ghl-mcp-frontend --image ghl-mcp-frontend:latest
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GHL_CLIENT_ID` | GoHighLevel OAuth Client ID | Yes | - |
| `GHL_CLIENT_SECRET` | GoHighLevel OAuth Client Secret | Yes | - |
| `GHL_SHARED_SECRET` | GoHighLevel Shared Secret | Yes | - |
| `GHL_REDIRECT_URI` | OAuth Redirect URI | Yes | - |
| `OPENROUTER_API_KEY` | OpenRouter API Key | Yes | - |
| `OPENROUTER_MODEL` | AI Model to use | No | `anthropic/claude-3-sonnet` |
| `DATABASE_URL` | Database connection string | Yes | - |
| `REDIS_URL` | Redis connection string | Yes | - |
| `JWT_SECRET` | JWT signing secret | Yes | - |
| `ENCRYPTION_KEY` | Data encryption key | Yes | - |

### SSL/TLS Configuration

For production deployments, ensure SSL/TLS is properly configured:

1. **Using Let's Encrypt with Nginx:**
   ```bash
   certbot --nginx -d yourdomain.com
   ```

2. **Using AWS Certificate Manager:**
   - Create certificate in ACM
   - Attach to Application Load Balancer

3. **Using Cloudflare:**
   - Configure DNS to point to your server
   - Enable SSL/TLS in Cloudflare dashboard

## 📊 Monitoring and Logging

### Health Checks

The application includes health check endpoints:

- Backend: `GET /health`
- Frontend: Available at root path

### Logging

Configure structured logging:

```python
# backend/main.py
import structlog

logger = structlog.get_logger()
```

### Monitoring

Recommended monitoring tools:

- **Application Performance:** New Relic, DataDog
- **Infrastructure:** Prometheus + Grafana
- **Error Tracking:** Sentry
- **Uptime Monitoring:** Pingdom, UptimeRobot

## 🔒 Security Considerations

### Production Security Checklist

- [ ] Use HTTPS everywhere
- [ ] Set secure environment variables
- [ ] Configure CORS properly
- [ ] Enable rate limiting
- [ ] Set up Web Application Firewall (WAF)
- [ ] Regular security updates
- [ ] Database encryption at rest
- [ ] Secure secret management
- [ ] Network security groups/firewalls
- [ ] Regular backups

### GoHighLevel Marketplace Requirements

- [ ] Valid SSL certificate
- [ ] Webhook endpoint security
- [ ] OAuth flow implementation
- [ ] Data encryption compliance
- [ ] Privacy policy and terms of service
- [ ] GDPR compliance (if applicable)

## 🚨 Troubleshooting

### Common Issues

1. **Database Connection Errors:**
   ```bash
   # Check database connectivity
   docker-compose exec postgres psql -U ghl_user -d ghl_mcp -c "SELECT 1;"
   ```

2. **Redis Connection Errors:**
   ```bash
   # Check Redis connectivity
   docker-compose exec redis redis-cli ping
   ```

3. **OAuth Errors:**
   - Verify redirect URI matches exactly
   - Check client ID and secret
   - Ensure proper scopes are requested

4. **WebSocket Connection Issues:**
   - Check firewall settings
   - Verify WebSocket support in load balancer
   - Check CORS configuration

### Log Analysis

```bash
# View application logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Filter for errors
docker-compose logs backend | grep ERROR
```

## 📈 Scaling

### Horizontal Scaling

1. **Load Balancer Configuration:**
   - Use sticky sessions for WebSocket connections
   - Health check configuration
   - SSL termination

2. **Database Scaling:**
   - Read replicas for PostgreSQL
   - Connection pooling
   - Query optimization

3. **Caching Strategy:**
   - Redis cluster for high availability
   - Application-level caching
   - CDN for static assets

### Performance Optimization

1. **Backend Optimization:**
   - Async/await patterns
   - Database query optimization
   - Response caching
   - Connection pooling

2. **Frontend Optimization:**
   - Code splitting
   - Lazy loading
   - Image optimization
   - Bundle analysis

This deployment guide provides comprehensive instructions for deploying the GoHighLevel MCP Web UI in various environments. Choose the deployment method that best fits your infrastructure and requirements.
