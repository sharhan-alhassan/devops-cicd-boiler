from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.v1.users import user_router

from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

description = """
DevOps CI/CD Service is a modern, secure user management platform with comprehensive authentication and authorization.

### Key Features

- **User Management**
  - Register, verify, and authenticate users
  - Role-based access (Customer, Admin)
  - Profile management and password reset via email OTP
  - JWT-based authentication with secure token handling

---

**Typical Workflow:**
1. User registers with email and password
2. User receives verification email with OTP
3. User verifies account and can login
4. User can view profile and manage account settings
5. Admins can monitor and manage all users

---

For more details, see the documentation below or contact support.
"""


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    yield
    # Shutdown


app = FastAPI(
    title="Backend Service",
    description=description,
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(
    user_router.router,
    prefix=f"{settings.API_V1_STR}/users",
    tags=["users"],
)


@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "healthy"}


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def landing_page():
    return """
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>DevOps Service Landing Page</title>
        <style>
            body {
                background: #181c20;
                color: #f3f3f3;
                font-family: 'Segoe UI', Arial, sans-serif;
                margin: 0;
                padding: 0;
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
            }
            .container {
                background: #23272b;
                border-radius: 16px;
                box-shadow: 0 4px 24px rgba(0,0,0,0.3);
                padding: 2.5rem 2rem 2rem 2rem;
                max-width: 420px;
                width: 90vw;
                margin: 2rem auto;
                text-align: center;
            }
            h1 {
                margin-bottom: 0.5rem;
                font-size: 2.2rem;
                color: #4a90e2;
            }
            p {
                color: #b0b8c1;
                margin-bottom: 2rem;
            }
            .links {
                display: flex;
                flex-direction: column;
                gap: 1rem;
            }
            a {
                background: #4a90e2;
                color: #ffffff;
                text-decoration: none;
                padding: 0.75rem 1.5rem;
                border-radius: 8px;
                font-weight: 600;
                font-size: 1.1rem;
                transition: background 0.2s, color 0.2s, box-shadow 0.2s;
                box-shadow: 0 2px 8px rgba(74,144,226,0.08);
            }
            a:hover {
                background: #5ba0f2;
                color: #ffffff;
                box-shadow: 0 4px 16px rgba(74,144,226,0.18);
            }
            .footer {
                margin-top: 2rem;
                color: #6c757d;
                font-size: 0.95rem;
            }
        </style>
    </head>
    <body>
        <div class=\"container\">
            <h1>DevOps Service</h1>
            <p>Welcome to the DevOps Service. Choose a documentation below:</p>
            <div class=\"links\">
                <a href=\"/docs\">Swagger UI</a>
                <a href=\"/redoc\">Redoc</a>
                <a href=\"/scalar\">Scalar Docs</a>
            </div>
            <div class=\"footer\">&copy; 2025 TiaSpaces. All rights reserved.</div>
        </div>
    </body>
    </html>
    """
