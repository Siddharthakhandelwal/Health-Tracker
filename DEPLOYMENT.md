# 🚀 Health Tracker Deployment Guide

Complete deployment guide for the Health Tracker API across different environments and platforms.

## 📋 Table of Contents

1. [Deployment Overview](#-deployment-overview)
2. [Prerequisites](#-prerequisites)
3. [Local Development Deployment](#-local-development-deployment)
4. [Production Deployment](#-production-deployment)
5. [Cloud Platform Deployments](#-cloud-platform-deployments)
6. [Docker Deployment](#-docker-deployment)
7. [Environment Configuration](#-environment-configuration)
8. [Security Considerations](#-security-considerations)
9. [Monitoring and Maintenance](#-monitoring-and-maintenance)
10. [Troubleshooting](#-troubleshooting)

## 🌐 Deployment Overview

The Health Tracker API is designed to be deployed across various environments:

- **Development**: Local machine for testing and development
- **Staging**: Pre-production environment for testing
- **Production**: Live environment serving real users

### Architecture Summary
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Load Balancer │    │  Health Tracker │    │  Google Gemini  │
│   (Optional)    │◄──►│      API        │◄──►│      AI API     │
│                 │    │                 │    │                 │
│ • Nginx         │    │ • FastAPI       │    │ • AI Models     │
│ • HAProxy       │    │ • Uvicorn       │    │ • Cloud Service │
│ • Cloud LB      │    │ • Python 3.9+   │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📋 Prerequisites

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **CPU** | 1 core | 2+ cores |
| **RAM** | 512MB | 2GB+ |
| **Storage** | 1GB | 5GB+ |
| **Network** | 1Mbps | 10Mbps+ |
| **OS** | Any Linux/Windows/macOS | Ubuntu 20.04+ |

### Software Dependencies

- **Python 3.9+** (Required)
- **pip** (Package manager)
- **Git** (Version control)
- **Docker** (Optional, for containerized deployment)
- **Nginx** (Optional, for reverse proxy)

### External Services

- **Google Gemini API Key** (Required)
- **Domain name** (Production only)
- **SSL Certificate** (Production only)

## 🏠 Local Development Deployment

### Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/Health-Tracker.git
cd Health-Tracker

# Create virtual environment
python -m venv health-tracker-env
source health-tracker-env/bin/activate  # Windows: health-tracker-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env.example .env
# Edit .env with your API key

# Run the application
python main.py
```

### Development Server Configuration

```python
# main.py - Development configuration
if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="127.0.0.1",  # Local access only
        port=8000, 
        reload=True,       # Auto-reload on code changes
        log_level="debug"  # Verbose logging
    )
```

### Testing the Deployment

```bash
# Test endpoints
python test_api.py

# Manual testing
curl http://localhost:8000/docs
```

## 🏭 Production Deployment

### Production Server Setup

#### 1. Server Preparation

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install python3 python3-pip python3-venv nginx supervisor -y

# Create application user
sudo useradd -m -s /bin/bash healthtracker
sudo su - healthtracker
```

#### 2. Application Setup

```bash
# Clone repository
git clone https://github.com/your-username/Health-Tracker.git
cd Health-Tracker

# Create production virtual environment
python3 -m venv venv
source venv/bin/activate

# Install production dependencies
pip install -r requirements.txt
pip install gunicorn  # Production WSGI server
```

#### 3. Production Configuration

Create production configuration file:

```python
# config/production.py
import os

class ProductionConfig:
    HOST = "0.0.0.0"
    PORT = 8000
    WORKERS = 4
    WORKER_CLASS = "uvicorn.workers.UvicornWorker"
    BIND = f"{HOST}:{PORT}"
    TIMEOUT = 120
    KEEPALIVE = 5
    MAX_REQUESTS = 1000
    MAX_REQUESTS_JITTER = 100
    LOG_LEVEL = "info"
    ACCESS_LOG = "/var/log/healthtracker/access.log"
    ERROR_LOG = "/var/log/healthtracker/error.log"
```

#### 4. Gunicorn Configuration

```bash
# Create gunicorn configuration
cat > gunicorn.conf.py << EOF
import multiprocessing

bind = "127.0.0.1:8000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 120
keepalive = 5
max_requests = 1000
max_requests_jitter = 100
preload_app = True
accesslog = "/var/log/healthtracker/access.log"
errorlog = "/var/log/healthtracker/error.log"
loglevel = "info"
EOF
```

#### 5. Systemd Service

```bash
# Create systemd service file
sudo tee /etc/systemd/system/healthtracker.service << EOF
[Unit]
Description=Health Tracker API
After=network.target

[Service]
User=healthtracker
Group=healthtracker
WorkingDirectory=/home/healthtracker/Health-Tracker
Environment=PATH=/home/healthtracker/Health-Tracker/venv/bin
EnvironmentFile=/home/healthtracker/Health-Tracker/.env
ExecStart=/home/healthtracker/Health-Tracker/venv/bin/gunicorn -c gunicorn.conf.py main:app
ExecReload=/bin/kill -s HUP \$MAINPID
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable healthtracker
sudo systemctl start healthtracker
```

#### 6. Nginx Reverse Proxy

```bash
# Create Nginx configuration
sudo tee /etc/nginx/sites-available/healthtracker << EOF
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://\$server_name\$request_uri;
}

server {
    listen 443 ssl http2;
    server_name your-domain.com www.your-domain.com;
    
    # SSL Configuration
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    
    # Security Headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
    
    # Proxy Configuration
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }
    
    # Health Check Endpoint
    location /health {
        proxy_pass http://127.0.0.1:8000/health;
        access_log off;
    }
    
    # Static files (if any)
    location /static/ {
        alias /home/healthtracker/Health-Tracker/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
EOF

# Enable site
sudo ln -s /etc/nginx/sites-available/healthtracker /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

## ☁️ Cloud Platform Deployments

### AWS Deployment

#### Option 1: EC2 Instance

```bash
# Launch EC2 instance (Ubuntu 20.04 LTS)
# Security Group: Allow HTTP (80), HTTPS (443), SSH (22)

# Connect to instance
ssh -i your-key.pem ubuntu@your-ec2-ip

# Follow production deployment steps above
```

#### Option 2: AWS Lambda + API Gateway

```python
# Install serverless dependencies
pip install mangum

# Create lambda_handler.py
from mangum import Mangum
from main import app

handler = Mangum(app)
```

```yaml
# serverless.yml
service: health-tracker

provider:
  name: aws
  runtime: python3.9
  region: us-east-1
  environment:
    GEMINI_API_KEY: ${env:GEMINI_API_KEY}

functions:
  api:
    handler: lambda_handler.handler
    events:
      - http:
          path: /{proxy+}
          method: ANY
          cors: true
      - http:
          path: /
          method: ANY
          cors: true

plugins:
  - serverless-python-requirements
```

#### Option 3: AWS ECS (Fargate)

```yaml
# docker-compose.yml for ECS
version: '3.8'
services:
  health-tracker:
    image: your-account.dkr.ecr.region.amazonaws.com/health-tracker:latest
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    logging:
      driver: awslogs
      options:
        awslogs-group: /ecs/health-tracker
        awslogs-region: us-east-1
        awslogs-stream-prefix: ecs
```

### Google Cloud Platform

#### Option 1: Google Cloud Run

```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/health-tracker', '.']
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/health-tracker']
  - name: 'gcr.io/cloud-builders/gcloud'
    args:
      - 'run'
      - 'deploy'
      - 'health-tracker'
      - '--image'
      - 'gcr.io/$PROJECT_ID/health-tracker'
      - '--region'
      - 'us-central1'
      - '--platform'
      - 'managed'
      - '--allow-unauthenticated'
```

```bash
# Deploy to Cloud Run
gcloud builds submit --config cloudbuild.yaml
```

#### Option 2: Google Compute Engine

```bash
# Create VM instance
gcloud compute instances create health-tracker-vm \
    --image-family=ubuntu-2004-lts \
    --image-project=ubuntu-os-cloud \
    --machine-type=e2-medium \
    --zone=us-central1-a

# Follow production deployment steps
```

### Heroku Deployment

```bash
# Install Heroku CLI
# Create Procfile
echo "web: uvicorn main:app --host=0.0.0.0 --port=\$PORT" > Procfile

# Create runtime.txt
echo "python-3.9.16" > runtime.txt

# Deploy to Heroku
heroku create your-health-tracker-app
heroku config:set GEMINI_API_KEY=your_api_key_here
git push heroku main
```

### DigitalOcean App Platform

```yaml
# .do/app.yaml
name: health-tracker
services:
- name: api
  source_dir: /
  github:
    repo: your-username/Health-Tracker
    branch: main
  run_command: uvicorn main:app --host=0.0.0.0 --port=8080
  environment_slug: python
  instance_count: 1
  instance_size_slug: basic-xxs
  envs:
  - key: GEMINI_API_KEY
    value: your_api_key_here
    type: SECRET
  http_port: 8080
```

## 🐳 Docker Deployment

### Dockerfile

```dockerfile
# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  health-tracker:
    build: .
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - health-tracker
    restart: unless-stopped

volumes:
  logs:
```

### Production Docker Deployment

```bash
# Build and run with Docker Compose
docker-compose up -d

# Scale the application
docker-compose up -d --scale health-tracker=3

# View logs
docker-compose logs -f health-tracker

# Update deployment
docker-compose pull
docker-compose up -d
```

## ⚙️ Environment Configuration

### Environment Variables

```bash
# .env file structure
# API Configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Application Settings
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=info

# Server Configuration
HOST=0.0.0.0
PORT=8000
WORKERS=4

# Security Settings
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=your-domain.com,www.your-domain.com

# External Services
SENTRY_DSN=your_sentry_dsn_here
REDIS_URL=redis://localhost:6379/0

# Database (future use)
DATABASE_URL=postgresql://user:password@localhost/healthtracker
```

### Environment-Specific Configurations

#### Development
```bash
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=debug
HOST=127.0.0.1
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### Staging
```bash
ENVIRONMENT=staging
DEBUG=false
LOG_LEVEL=info
HOST=0.0.0.0
ALLOWED_HOSTS=staging.your-domain.com
```

#### Production
```bash
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=warning
HOST=0.0.0.0
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

## 🔒 Security Considerations

### SSL/TLS Configuration

```bash
# Install Certbot for Let's Encrypt
sudo apt install certbot python3-certbot-nginx

# Obtain SSL certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

### Firewall Configuration

```bash
# Configure UFW firewall
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

### Security Headers

```nginx
# Additional security headers in Nginx
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';";
add_header Referrer-Policy "strict-origin-when-cross-origin";
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()";
```

### API Key Security

```python
# Secure API key handling
import os
from cryptography.fernet import Fernet

def get_encrypted_api_key():
    key = os.environ.get('ENCRYPTION_KEY')
    encrypted_key = os.environ.get('ENCRYPTED_GEMINI_KEY')
    
    f = Fernet(key)
    return f.decrypt(encrypted_key.encode()).decode()
```

## 📊 Monitoring and Maintenance

### Health Check Endpoint

```python
# Add to main.py
from datetime import datetime
import psutil

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
        "uptime": psutil.boot_time(),
        "memory_usage": psutil.virtual_memory().percent,
        "cpu_usage": psutil.cpu_percent(),
        "ai_service": "available"  # Check Gemini API connectivity
    }
```

### Logging Configuration

```python
# logging_config.py
import logging
import sys
from logging.handlers import RotatingFileHandler

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            RotatingFileHandler(
                'logs/app.log',
                maxBytes=10485760,  # 10MB
                backupCount=5
            ),
            logging.StreamHandler(sys.stdout)
        ]
    )
```

### Monitoring with Prometheus

```python
# metrics.py
from prometheus_client import Counter, Histogram, generate_latest

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'HTTP request duration')

@app.middleware("http")
async def add_prometheus_metrics(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    
    REQUEST_COUNT.labels(method=request.method, endpoint=request.url.path).inc()
    REQUEST_DURATION.observe(duration)
    
    return response

@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type="text/plain")
```

### Backup and Recovery

```bash
# Backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backups/healthtracker"

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup application files
tar -czf $BACKUP_DIR/app_$DATE.tar.gz /home/healthtracker/Health-Tracker

# Backup logs
tar -czf $BACKUP_DIR/logs_$DATE.tar.gz /var/log/healthtracker

# Clean old backups (keep last 7 days)
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete
```

## 🔧 Troubleshooting

### Common Issues

#### 1. Application Won't Start

```bash
# Check service status
sudo systemctl status healthtracker

# Check logs
sudo journalctl -u healthtracker -f

# Check port availability
sudo netstat -tlnp | grep :8000
```

#### 2. High Memory Usage

```bash
# Monitor memory usage
htop

# Check for memory leaks
python -m memory_profiler main.py

# Restart service
sudo systemctl restart healthtracker
```

#### 3. Slow Response Times

```bash
# Check AI API connectivity
curl -X POST "http://localhost:8000/water" \
     -H "Content-Type: application/json" \
     -d '{"amount_liters": 2.0}' \
     -w "Time: %{time_total}s\n"

# Monitor system resources
iostat -x 1
```

#### 4. SSL Certificate Issues

```bash
# Check certificate status
sudo certbot certificates

# Renew certificate
sudo certbot renew --dry-run

# Test SSL configuration
openssl s_client -connect your-domain.com:443
```

### Performance Optimization

#### 1. Application Tuning

```python
# Optimize Uvicorn settings
uvicorn main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --access-log \
    --loop uvloop \
    --http httptools
```

#### 2. Database Optimization (Future)

```python
# Connection pooling
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=30,
    pool_pre_ping=True
)
```

#### 3. Caching Strategy

```python
# Redis caching
import redis
from functools import wraps

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_response(expiration=300):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
            cached = redis_client.get(cache_key)
            
            if cached:
                return json.loads(cached)
            
            result = await func(*args, **kwargs)
            redis_client.setex(cache_key, expiration, json.dumps(result))
            return result
        return wrapper
    return decorator
```

### Maintenance Tasks

#### Daily Tasks
- Monitor application logs
- Check system resource usage
- Verify SSL certificate status
- Review error rates and response times

#### Weekly Tasks
- Update system packages
- Rotate log files
- Review security logs
- Test backup and recovery procedures

#### Monthly Tasks
- Update application dependencies
- Review and update security configurations
- Performance optimization review
- Capacity planning assessment

---

## 📞 Support and Resources

### Documentation Links
- [Setup Guide](SETUP_GUIDE.md)
- [API Documentation](API_GUIDE.md)
- [Architecture Overview](ARCHITECTURE.md)
- [Contributing Guide](CONTRIBUTING.md)

### External Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Docker Documentation](https://docs.docker.com/)

### Getting Help
- **Issues**: Report deployment issues on GitHub
- **Community**: Join discussions for deployment help
- **Professional Support**: Contact for enterprise deployment assistance

---

**🚀 Happy Deploying!**

*This deployment guide covers various deployment scenarios. Choose the option that best fits your requirements and infrastructure. For additional help, please refer to our community resources or create an issue on GitHub.*