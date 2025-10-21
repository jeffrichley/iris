# Research: Cloud-First Development Environment

**Feature**: Cloud-First Development Environment Setup  
**Phase**: 0 (Research & Unknowns Resolution)  
**Date**: October 20, 2025

## Purpose

This document resolves all "NEEDS CLARIFICATION" items from the implementation plan, providing technical decisions, rationale, and code examples for Sprint 0 implementation.

---

## RES-001: Supabase Python Client Integration

**Decision**: Use `supabase-py` (official client) with singleton pattern for connection management

**Rationale**:
- Official Supabase Python client with active maintenance
- Built-in connection pooling via httpx
- Supports all Supabase features (Auth, Database, Storage, Realtime)
- Type hints included for IDE support

**Implementation Pattern**:

```python
# src/iris/database/supabase.py
from supabase import create_client, Client
from iris.config.settings import get_settings

_supabase_client: Client | None = None

def get_supabase() -> Client:
    """Get Supabase client singleton with connection pooling."""
    global _supabase_client
    
    if _supabase_client is None:
        settings = get_settings()
        _supabase_client = create_client(
            supabase_url=settings.SUPABASE_URL,
            supabase_key=settings.SUPABASE_ANON_KEY
        )
    
    return _supabase_client

# FastAPI dependency injection
async def get_db() -> Client:
    """FastAPI dependency for database access."""
    return get_supabase()
```

**Best Practices**:
- Use `SUPABASE_ANON_KEY` for client-side operations (RLS enforced)
- Use `SUPABASE_SERVICE_KEY` only for admin operations (bypasses RLS)
- Connection pooling handled automatically by httpx backend
- No explicit connection close needed (httpx manages lifecycle)

**Alternatives Considered**:
- Direct PostgreSQL connection (psycopg2): Bypasses Supabase Auth/RLS integration
- SQLAlchemy + Supabase: Adds unnecessary ORM complexity for cloud-first model

---

## RES-002: Google OAuth2 Provider Configuration

**Decision**: Use Supabase hosted authentication with Google Cloud Console OAuth2 client

**Configuration Steps**:

### Step 1: Google Cloud Console Setup
```
1. Navigate to: https://console.cloud.google.com
2. Create new project (or use existing): "Iris Development"
3. Enable Google+ API (required for profile access)
4. Navigate to: APIs & Services → Credentials
5. Create OAuth 2.0 Client ID
   - Application type: Web application
   - Name: "Iris Supabase Auth"
   - Authorized redirect URIs: https://<project-ref>.supabase.co/auth/v1/callback
6. Save Client ID and Client Secret
```

### Step 2: Supabase Dashboard Configuration
```
1. Navigate to: Supabase Dashboard → Authentication → Providers
2. Enable Google provider
3. Enter Client ID from Google Cloud Console
4. Enter Client Secret from Google Cloud Console
5. Scopes: email, profile (default, sufficient for MVP)
6. Save configuration
```

**Callback URL Pattern**:
```
https://<project-ref>.supabase.co/auth/v1/callback
```

Example: `https://abcdefghijklmnopqrst.supabase.co/auth/v1/callback`

**OAuth2 Scopes**:
- `email`: User's email address (required for user_id mapping)
- `profile`: User's name and profile picture (optional, for UX)

**Frontend Integration** (Deferred to Sprint 2):
```typescript
// Future: Initiate OAuth2 flow
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'google',
  options: {
    redirectTo: 'http://localhost:8000/auth/callback'
  }
})
```

**Backend Receives**:
- JWT token in Authorization header: `Bearer <token>`
- Token contains claims: `sub` (user_id), `email`, `provider: "google"`

**Alternatives Considered**:
- Firebase Auth: Requires Firebase project, vendor lock-in without PostgreSQL
- Auth0: Adds cost, unnecessary for single OAuth provider

---

## RES-003: JWT Validation with Supabase

**Decision**: Use `python-jose[cryptography]` with Supabase JWT_SECRET for validation

**JWT Structure** (Supabase-issued):
```json
{
  "sub": "550e8400-e29b-41d4-a716-446655440000",  // user_id (UUID)
  "email": "user@example.com",                    // from Google
  "app_metadata": {
    "provider": "google",
    "providers": ["google"]
  },
  "user_metadata": {
    "email": "user@example.com",
    "full_name": "John Doe",
    "avatar_url": "https://..."
  },
  "role": "authenticated",
  "aal": "aal1",
  "iss": "https://<project-ref>.supabase.co/auth/v1",
  "aud": "authenticated",
  "iat": 1697840000,
  "exp": 1697843600  // 1 hour expiration
}
```

**Validation Implementation**:

```python
# src/iris/auth/jwt.py
from jose import jwt, JWTError
from fastapi import HTTPException, Header
from iris.config.settings import get_settings

def validate_jwt(authorization: str = Header(...)) -> str:
    """
    Validate JWT token and extract user_id.
    
    Args:
        authorization: Authorization header value (Bearer <token>)
        
    Returns:
        user_id (UUID string)
        
    Raises:
        HTTPException: 401 if token invalid/expired/missing
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header format. Expected 'Bearer <token>'"
        )
    
    token = authorization.replace("Bearer ", "")
    settings = get_settings()
    
    try:
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=["HS256"],  # Supabase uses HS256
            audience="authenticated"  # Validate audience claim
        )
        
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(401, detail="Token missing 'sub' claim")
        
        # Optional: Validate provider is Google
        provider = payload.get("app_metadata", {}).get("provider")
        if provider != "google":
            raise HTTPException(401, detail=f"Invalid provider: {provider}")
        
        return user_id
        
    except JWTError as e:
        raise HTTPException(
            status_code=401,
            detail=f"Invalid token: {str(e)}"
        )

# FastAPI dependency
async def get_current_user(authorization: str = Header(...)) -> str:
    """FastAPI dependency to inject authenticated user_id."""
    return validate_jwt(authorization)
```

**Usage in Routes**:
```python
from fastapi import APIRouter, Depends
from iris.auth.jwt import get_current_user

router = APIRouter()

@router.get("/projects")
async def list_projects(user_id: str = Depends(get_current_user)):
    """List user's projects (RLS enforced by user_id)."""
    # user_id automatically injected from validated JWT
    return {"user_id": user_id, "projects": []}
```

**Security Considerations**:
- Algorithm restricted to HS256 only (prevent algorithm confusion attacks)
- Audience validation ensures token intended for this app
- Provider validation ensures only Google OAuth tokens accepted
- No grace period for expired tokens (enforce strict expiration)

**Alternatives Considered**:
- Supabase Python client's built-in auth: Designed for client-side, not API middleware
- PyJWT: Similar to python-jose, chosen jose for better FastAPI integration

---

## RES-004: Row Level Security (RLS) Policies

**Decision**: User-scoped RLS policies using `auth.uid()` function

**Policy Pattern for All Tables**:

```sql
-- Enable RLS on table
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

-- Policy: Users can only see their own data
CREATE POLICY "users_read_own_projects"
ON projects FOR SELECT
USING (auth.uid() = user_id);

-- Policy: Users can only insert their own data
CREATE POLICY "users_insert_own_projects"
ON projects FOR INSERT
WITH CHECK (auth.uid() = user_id);

-- Policy: Users can only update their own data
CREATE POLICY "users_update_own_projects"
ON projects FOR UPDATE
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

-- Policy: Users can only delete their own data
CREATE POLICY "users_delete_own_projects"
ON projects FOR DELETE
USING (auth.uid() = user_id);
```

**Development Mode** (Permissive RLS for testing):

```sql
-- Temporary policy for development (disable in production)
CREATE POLICY "dev_allow_all"
ON projects FOR ALL
USING (true)
WITH CHECK (true);

-- Disable with:
DROP POLICY "dev_allow_all" ON projects;
```

**RLS + FastAPI Integration**:

```python
# FastAPI passes user_id to Supabase, RLS auto-enforces
from iris.database.supabase import get_db

async def list_projects(user_id: str = Depends(get_current_user)):
    """RLS automatically filters by user_id."""
    db = get_db()
    
    # Supabase uses JWT from auth header, RLS applies automatically
    response = db.from_("projects").select("*").execute()
    
    # Only returns projects where auth.uid() = user_id
    return response.data
```

**Testing RLS**:
```python
@pytest.mark.integration
def test_rls_prevents_cross_user_access():
    """Users cannot access other users' projects."""
    # Create project as user1
    user1_jwt = authenticate_user("user1@example.com")
    create_project(user1_jwt, {"name": "User 1 Project"})
    
    # Attempt to read as user2
    user2_jwt = authenticate_user("user2@example.com")
    projects = list_projects(user2_jwt)
    
    # RLS should prevent seeing user1's projects
    assert len(projects) == 0
```

**Alternatives Considered**:
- Application-level filtering: Error-prone, RLS is defense-in-depth
- Service role bypass: Dangerous, defeats purpose of user isolation

---

## RES-005: SQLModel + PostgreSQL Best Practices

**Decision**: Use SQLModel with PostgreSQL-specific types (UUID, TIMESTAMPTZ)

**Base Model Pattern**:

```python
# src/iris/models/base.py
from sqlmodel import SQLModel, Field
from datetime import datetime
from uuid import UUID, uuid4

class BaseModel(SQLModel):
    """Base model with common fields for all entities."""
    
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
    
    user_id: UUID = Field(
        foreign_key="auth.users.id",
        nullable=False,
        index=True  # Index for RLS performance
    )
    
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": "NOW()"}
    )
    
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={
            "server_default": "NOW()",
            "onupdate": "NOW()"
        }
    )
```

**Example Entity Model**:

```python
# src/iris/models/project.py
from sqlmodel import Field
from enum import Enum
from iris.models.base import BaseModel

class ProjectStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    COMPLETED = "completed"

class Project(BaseModel, table=True):
    """Project entity with user isolation."""
    
    __tablename__ = "projects"
    
    name: str = Field(max_length=255, nullable=False)
    description: str | None = Field(default=None)
    status: ProjectStatus = Field(default=ProjectStatus.ACTIVE)
    
    # Relationships (defined in data-model.md)
    # tasks: list["Task"] = Relationship(back_populates="project")
```

**Type Mappings**:
- Python `UUID` → PostgreSQL `UUID`
- Python `datetime` → PostgreSQL `TIMESTAMPTZ`
- Python `str` → PostgreSQL `TEXT`
- Python `Enum` → PostgreSQL `TEXT` with CHECK constraint

**Migration SQL Generation**:
```python
# Generate SQL from SQLModel
from sqlmodel import create_engine, SQLModel

engine = create_engine("postgresql://...")
SQLModel.metadata.create_all(engine)  # Generates CREATE TABLE statements
```

**Alternatives Considered**:
- Pure SQLAlchemy: More verbose, SQLModel provides Pydantic integration
- Alembic migrations: Adds complexity, raw SQL sufficient for MVP

---

## RES-006: Docker Compose + FastAPI Hot-Reload

**Decision**: Volume mount source code with uvicorn --reload

**docker-compose.yml**:

```yaml
version: '3.8'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: iris-api
    ports:
      - "${API_PORT:-8000}:8000"
    volumes:
      # Mount source code for hot-reload
      - ./src:/app/src:delegated
      # Mount .env for configuration
      - ./.env:/app/.env:ro
    environment:
      - ENVIRONMENT=development
    command: >
      uvicorn src.iris.api.main:app
        --host 0.0.0.0
        --port 8000
        --reload
        --reload-dir /app/src
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 5s
```

**Dockerfile** (with hot-reload support):

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install uv for dependency management
RUN pip install --no-cache-dir uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --no-dev

# Copy source code (overridden by volume in development)
COPY src/ ./src/

# Expose FastAPI port
EXPOSE 8000

# Command overridden in docker-compose.yml for dev hot-reload
CMD ["uvicorn", "src.iris.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Hot-Reload Performance**:
- Uvicorn watches `/app/src` directory for changes
- Reloads typically complete in < 3 seconds (SC-006)
- Volume mount with `:delegated` for better macOS performance

**Alternatives Considered**:
- watchfiles: uvicorn --reload uses this internally
- No hot-reload: Slow development iteration (restart container manually)

---

## RES-007: Database Migration Strategy

**Decision**: SQL migration files with version numbering, applied via Supabase SQL Editor

**Migration File Structure**:

```
src/iris/database/migrations/
├── 001_initial_schema.sql      # Core tables + RLS policies
├── 002_add_indexes.sql         # Performance indexes
└── 003_add_audit_triggers.sql  # Future: audit logging
```

**Migration Template** (`001_initial_schema.sql`):

```sql
-- Migration: 001_initial_schema
-- Description: Create core tables with RLS policies
-- Date: 2025-10-20

BEGIN;

-- Create projects table
CREATE TABLE IF NOT EXISTS projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    status TEXT CHECK (status IN ('active', 'archived', 'completed')) DEFAULT 'active',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Create index on user_id for RLS performance
CREATE INDEX idx_projects_user_id ON projects(user_id);

-- Enable RLS
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

-- Create RLS policies
CREATE POLICY "users_read_own_projects"
ON projects FOR SELECT
USING (auth.uid() = user_id);

-- ... (repeat for tasks, ideas, reminders, notes)

COMMIT;
```

**Application Workflow**:

```bash
# Developer runs migration
just db-init

# Justfile command:
# db-init:
#     @echo "Applying migrations to Supabase..."
#     psql $SUPABASE_DATABASE_URL -f src/iris/database/migrations/001_initial_schema.sql
#     @echo "Migrations complete"
```

**Migration Tracking** (Future):

```sql
-- Create migration history table
CREATE TABLE IF NOT EXISTS schema_migrations (
    version INT PRIMARY KEY,
    applied_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    description TEXT
);

-- Record migration
INSERT INTO schema_migrations (version, description)
VALUES (1, '001_initial_schema');
```

**Alternatives Considered**:
- Alembic: Complex setup, autogeneration not needed for simple schema
- Supabase Migration API: Still beta, SQL files more explicit
- SQLModel.metadata.create_all(): Doesn't handle RLS policies or custom SQL

---

## RES-008: FastAPI Dependency Injection for user_id

**Decision**: Use FastAPI `Depends()` with JWT middleware for automatic user_id extraction

**Pattern**:

```python
# src/iris/auth/dependencies.py
from fastapi import Depends, Header, HTTPException
from iris.auth.jwt import validate_jwt

async def get_current_user_id(authorization: str = Header(...)) -> str:
    """
    Extract and validate user_id from JWT in Authorization header.
    
    Automatically called by FastAPI for any route with this dependency.
    """
    return validate_jwt(authorization)

# Usage in routes
from fastapi import APIRouter, Depends
from iris.auth.dependencies import get_current_user_id

router = APIRouter(prefix="/api/v1")

@router.get("/projects")
async def list_projects(
    user_id: str = Depends(get_current_user_id),
    db: Client = Depends(get_db)
):
    """
    List user's projects.
    
    user_id automatically injected from JWT validation.
    No manual token parsing in route code.
    """
    response = db.from_("projects") \
        .select("*") \
        .eq("user_id", user_id) \
        .execute()
    
    return response.data

@router.post("/projects")
async def create_project(
    project_data: dict,
    user_id: str = Depends(get_current_user_id),
    db: Client = Depends(get_db)
):
    """
    Create new project with automatic user_id assignment.
    """
    project_data["user_id"] = user_id  # Inject authenticated user
    response = db.from_("projects").insert(project_data).execute()
    return response.data[0]
```

**Public Endpoints** (No dependency):

```python
@router.get("/health")
async def health_check():
    """Public endpoint, no authentication required."""
    return {"status": "healthy"}
```

**Error Handling**:
- Missing Authorization header → 401 Unauthorized
- Invalid JWT format → 401 with specific error
- Expired JWT → 401 with expiration message
- All handled by `validate_jwt()`, route code stays clean

**Alternatives Considered**:
- Manual token extraction in each route: Repetitive, error-prone
- Middleware for all routes: Can't have public endpoints (like `/health`)
- Custom route decorator: Less idiomatic than FastAPI Depends()

---

## Summary of Decisions

| Research Task | Decision | Rationale |
|---------------|----------|-----------|
| RES-001 | supabase-py with singleton | Official client, connection pooling, type hints |
| RES-002 | Google OAuth2 via Supabase | Managed auth flow, callback handling |
| RES-003 | python-jose + JWT_SECRET | Standard JWT validation, FastAPI-friendly |
| RES-004 | RLS policies with auth.uid() | Defense-in-depth, automatic enforcement |
| RES-005 | SQLModel + PostgreSQL types | Pydantic integration, type safety |
| RES-006 | Docker volume mount + uvicorn --reload | Fast iteration, < 3sec reload |
| RES-007 | SQL migration files | Explicit, version-controlled, handles RLS |
| RES-008 | FastAPI Depends(get_current_user_id) | Clean dependency injection, automatic validation |

**All "NEEDS CLARIFICATION" items resolved. Ready for Phase 1 design.**

---

## References

- [Supabase Python Client Docs](https://supabase.com/docs/reference/python/introduction)
- [FastAPI Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [python-jose JWT](https://python-jose.readthedocs.io/)
- [Supabase Row Level Security](https://supabase.com/docs/guides/auth/row-level-security)
- [SQLModel Documentation](https://sqlmodel.tiangolo.com/)
- [uvicorn Deployment](https://www.uvicorn.org/deployment/)

