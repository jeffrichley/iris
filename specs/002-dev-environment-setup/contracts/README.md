# API Contracts

This directory contains API contract specifications for the Iris cloud-first backend.

## Files

- **api-spec.yaml**: OpenAPI 3.1 specification for FastAPI routes
  - Authentication: Google OAuth2 + JWT Bearer
  - Endpoints: CRUD for projects, tasks, ideas, reminders, notes
  - All protected endpoints require valid Supabase JWT

## Viewing the Spec

### Option 1: Swagger UI (Automatic)

FastAPI generates interactive docs automatically:

```bash
# Start server
just dev

# Open browser
http://localhost:8000/docs        # Swagger UI
http://localhost:8000/redoc       # ReDoc
```

### Option 2: External Tools

```bash
# Swagger Editor (online)
https://editor.swagger.io/

# Paste contents of api-spec.yaml
```

## Authentication Flow

```
1. Frontend initiates Google OAuth → Supabase Auth
2. User consents via Google
3. Supabase returns JWT token
4. All API requests include: Authorization: Bearer <JWT>
5. FastAPI validates JWT and extracts user_id
6. RLS policies filter data by user_id automatically
```

## Testing Contracts

```bash
# Unit tests validate request/response schemas
pytest tests/contract/

# Integration tests verify actual API behavior
pytest tests/integration/test_api_crud.py
```

## Contract Versioning

- **Current Version**: v1 (`/api/v1/`)
- Breaking changes require new version (v2, v3, etc.)
- Deprecation notices 90 days before removal

