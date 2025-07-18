# DevOps CI/CD Service

A modern, secure user management platform with comprehensive authentication, authorization, and CI/CD pipeline.

---

## 🚀 Features

### **User Management**

- ✅ User registration with email and password
- ✅ JWT-based authentication
- ✅ Secure login and logout
- ✅ User profile information

### **Security**

- ✅ Secure password hashing with bcrypt
- ✅ JWT token authentication
- ✅ CORS protection
- ✅ Input validation with Pydantic
- ✅ SQL injection protection

### **Infrastructure**

- ✅ FastAPI backend with async support
- ✅ PostgreSQL database with async ORM
- ✅ Alembic database migrations
- ✅ Kubernetes deployment
- ✅ GitHub Actions CI/CD pipeline
- ✅ Docker containerization

---

## 📚 API Documentation

### **Interactive Documentation**

- **Swagger UI**: `/docs` - Interactive API explorer
- **Redoc**: `/redoc` - Beautiful API documentation
- **Scalar**: `/scalar` - Modern API client

### **API Endpoints**

```
POST /api/v1/users/register    # User registration
POST /api/v1/users/login       # User authentication
GET  /api/v1/users/me          # Get current user profile
GET  /health                   # Health check
```

---

## 🏗️ Architecture

### **Tech Stack**

- **Backend**: FastAPI (Python 3.11)
- **Database**: PostgreSQL with asyncpg
- **ORM**: SQLAlchemy 2.0 with async support
- **Authentication**: JWT tokens
- **Validation**: Pydantic models
- **Migrations**: Alembic
- **Container**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions

### **Project Structure**

```
devops-cicd-boiler/
├── app/
│   ├── api/v1/           # API routes
│   ├── core/             # Core functionality (auth, deps)
│   ├── crud/             # Database operations
│   ├── db/               # Database configuration
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   └── config.py         # Application settings
├── alembic/              # Database migrations
├── k8s_deploy/           # Kubernetes manifests
├── deploy/               # Deployment configurations
└── main.py               # FastAPI application
```

---

## 🛠️ Development Setup

### **Prerequisites**

- Python 3.11+
- PostgreSQL
- Docker (optional)
- kubectl (for deployment)

### **Local Development**

```bash
# Clone repository
git clone <repository-url>
cd devops-cicd-boiler

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your database and email settings

# Run database migrations
alembic upgrade head

# Start development server
uvicorn main:app --reload --port 8000
```

### **Environment Variables**

```bash
# Database
DATABASE_URL=postgresql+asyncpg://user:pass@localhost/dbname

# JWT
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=120
```

---

## 🚀 Deployment

### **Docker**

```bash
# Build image
docker build -t devops-service .

# Run container
docker run -p 8000:8000 devops-service
```

### **Kubernetes**

```bash
# Deploy to cluster
kubectl apply -k k8s_deploy/overlays/prod/

# Check deployment
kubectl get pods -n tiaspaces
```

### **CI/CD Pipeline**

- **Trigger**: Push to `main` branch
- **Build**: Docker image with GitHub Actions
- **Test**: Automated testing
- **Deploy**: Kubernetes deployment to EKS cluster

---

## 📊 Database Schema

### **Users Table**

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    phone_number VARCHAR NOT NULL,
    date_of_birth TIMESTAMP,
    address JSONB,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    hashed_password VARCHAR NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🔧 Configuration

### **Development vs Production**

- **Development**: SQLite database, local settings
- **Production**: PostgreSQL, environment-based configuration

### **Security Features**

- Password hashing with bcrypt
- JWT token expiration
- CORS protection
- Input sanitization
- SQL injection prevention

---

## 📝 API Examples

### **Register User**

```bash
curl -X POST "http://localhost:8000/api/v1/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword",
    "confirm_password": "securepassword",
    "first_name": "John",
    "last_name": "Doe",
    "phone_number": "+1234567890"
  }'
```

### **Login**

```bash
curl -X POST "http://localhost:8000/api/v1/users/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword"
```

### **Get Profile**

```bash
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact & Support

### **Developer**

- **GitHub**: [@sharhanalhassan](https://github.com/sharhan-alhassan)
- **LinkedIn**: [Sharhan Alhassan](https://www.linkedin.com/in/sharhan-alhassan1/)

### **Support**

- **Email**: sharhanalhassan@gmail.com
- **Issues**: [GitHub Issues](https://github.com/sharhanalhassan/devops-cicd-boiler/issues)

---

> Built with ❤️ using FastAPI, PostgreSQL, and Kubernetes
