"""FastAPI application initialization with middleware and exception handlers.

Compliant with Constitution Principle 4: Error Handling
Errors MUST be specific, never generic. User-facing errors MUST be actionable.

Per FR-012, FR-022: Exception handlers for custom error types.
Per FR-028: Rich library for colored logging.
"""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from iris.api import health
from iris.api.routes import ideas, notes, projects, reminders, tasks
from iris.utils.exceptions import (
    AuthenticationError,
    AuthorizationError,
    ConfigurationError,
    DatabaseError,
    ValidationError,
)
from iris.utils.logging import log_error, log_security_event


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application lifespan events (startup and shutdown).
    
    Replaces deprecated @app.on_event("startup") and @app.on_event("shutdown").
    Validates configuration on startup per FR-055, FR-069.
    """
    # Startup
    from iris.config.settings import get_settings
    from iris.utils.logging import get_console
    
    # Load and validate settings (will raise if .env invalid)
    settings = get_settings()
    
    console = get_console()
    console.print("\n")
    console.print("[bold blue]🌸 Iris API Starting...[/bold blue]")
    console.print(f"Environment: {settings.ENVIRONMENT}")
    console.print(f"API Host: {settings.API_HOST}:{settings.API_PORT}")
    console.print(f"Supabase URL: {settings.SUPABASE_URL}")
    console.print("\n")
    
    yield  # Application runs here
    
    # Shutdown
    console.print("\n[bold blue]🌸 Iris API Shutting down...[/bold blue]\n")


# Initialize FastAPI app with lifespan
app = FastAPI(
    title="Iris API",
    description="Cloud-first project management API with Google OAuth2 authentication",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS middleware (configure allowed origins based on environment)
# Settings loaded in startup event to avoid loading .env at import time
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Will be restricted in production via startup config
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception Handlers (T013)


@app.exception_handler(AuthenticationError)
async def authentication_error_handler(
    request: Request, exc: AuthenticationError
) -> JSONResponse:
    """Handle authentication errors (FR-022, FR-060, FR-061).
    
    Returns 401 Unauthorized with minimal information to avoid leakage.
    Logs security event per FR-046, FR-058.
    """
    # Log security event
    log_security_event(
        event_type="authentication_failed",
        details=exc.message,
        metadata={
            "path": str(request.url.path),
            "method": request.method,
        }
    )
    
    # Return generic error message (FR-060: avoid information leakage)
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content={"detail": "Authentication failed"},  # Generic message
    )


@app.exception_handler(AuthorizationError)
async def authorization_error_handler(
    request: Request, exc: AuthorizationError
) -> JSONResponse:
    """Handle authorization errors (FR-065).
    
    Returns 404 Not Found (not 403) to avoid revealing resource existence.
    """
    log_security_event(
        event_type="authorization_failed",
        details=exc.message,
        metadata={
            "path": str(request.url.path),
            "method": request.method,
        }
    )
    
    # Return 404 to hide resource existence (FR-065)
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "Resource not found"},
    )


@app.exception_handler(DatabaseError)
async def database_error_handler(request: Request, exc: DatabaseError) -> JSONResponse:
    """Handle database errors.
    
    Returns 500 Internal Server Error with generic message.
    Detailed error logged but not exposed to client.
    """
    log_error(
        f"Database error on {request.method} {request.url.path}: {exc.message}",
        title="Database Error",
        exception=exc
    )
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},  # Don't expose DB details
    )


@app.exception_handler(ValidationError)
async def validation_error_handler(request: Request, exc: ValidationError) -> JSONResponse:
    """Handle custom validation errors.
    
    Returns 400 Bad Request with actionable error message.
    """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.message},
    )


@app.exception_handler(ConfigurationError)
async def configuration_error_handler(
    request: Request, exc: ConfigurationError
) -> JSONResponse:
    """Handle configuration errors.
    
    Returns 500 with generic message (don't expose config details).
    """
    log_error(
        f"Configuration error: {exc.message}",
        title="Configuration Error",
        exception=exc
    )
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Server configuration error"},
    )


@app.exception_handler(RequestValidationError)
async def request_validation_error_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """Handle Pydantic request validation errors.
    
    Returns 400 with field-specific error details.
    """
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "detail": "Invalid request",
            "errors": exc.errors(),
        },
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle unexpected exceptions.
    
    Catch-all handler for unhandled exceptions.
    Logs full details but returns generic message to client.
    """
    log_error(
        f"Unhandled exception on {request.method} {request.url.path}",
        title="Unexpected Error",
        exception=exc
    )
    
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal server error"},
    )


# Register routers (T064)
# Routers imported at top of file

# Health endpoint (unprotected)
app.include_router(health.router)

# Protected API routes (all require JWT authentication)
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(ideas.router)
app.include_router(reminders.router)
app.include_router(notes.router)

