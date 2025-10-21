# Quickstart: Cloud-First Development Environment

**Feature**: Cloud-First Development Environment Setup  
**Phase**: 1 (Design & Contracts)  
**Audience**: New developers setting up Iris development environment

## Overview

This guide walks you through setting up the complete Iris development environment from scratch, including:
- ✅ Installing prerequisites (Docker, uv, justfile)
- ✅ Creating Supabase project and configuring Google OAuth2
- ✅ Initializing database schema with RLS policies
- ✅ Running FastAPI backend with hot-reload
- ✅ Testing OAuth2 login flow and protected API endpoints

**Time Estimate**: 30-45 minutes (first-time setup)

---

## Prerequisites

### Required Software

| Tool | Version | Purpose | Installation |
|------|---------|---------|--------------|
| **Python** | 3.12 or 3.13 | Backend language | [python.org](https://python.org) |
| **uv** | Latest | Fast Python package manager | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **just** | Latest | Task runner | [just.systems/install](https://just.systems/install) |
| **Docker** | Latest | Container runtime | [docker.com/get-started](https://docker.com/get-started) |
| **Git** | Latest | Version control | [git-scm.com](https://git-scm.com) |

### Optional Tools

- **PostgreSQL client** (psql): For direct database access
- **Postman/Thunder Client**: For API testing

### Required Accounts (Free Tier)

1. **Google Cloud Console**: For OAuth2 client setup
2. **Supabase**: For database and authentication

---

## Step 1: Clone Repository

```bash
# Clone Iris repository
git clone https://github.com/jeffrichley/iris.git
cd iris

# Checkout Sprint 0 branch (if implementing this spec)
git checkout 002-dev-environment-setup

# Verify structure
ls -la
# Should see: src/, tests/, pyproject.toml, justfile, etc.
```

---

## Step 2: Install Dependencies

```bash
# Install Python dependencies via uv
uv sync --dev

# Verify installation
uv run python --version
# Should show: Python 3.12.x or 3.13.x

# Install just (if not already installed)
# macOS/Linux:
brew install just

# Windows:
scoop install just

# Verify just
just --version
```

---

## Step 3: Create Supabase Project

### 3.1 Sign Up for Supabase

1. Navigate to [supabase.com](https://supabase.com)
2. Click "Start your project"
3. Sign in with GitHub
4. Create new organization (e.g., "iris-dev")

### 3.2 Create Project

1. Click "New Project"
2. Project settings:
   - **Name**: `iris-development`
   - **Database Password**: [Generate strong password - SAVE THIS]
   - **Region**: Choose nearest region (e.g., US West, EU Central)
   - **Pricing Plan**: Free
3. Click "Create new project"
4. Wait ~2 minutes for project provisioning

### 3.3 Get Supabase Credentials

Once project is ready:

1. Navigate to **Project Settings** → **API**
2. Copy and save these values:
   - **Project URL**: `https://xxxxx.supabase.co`
   - **anon/public key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (long string)
   - **service_role key**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` (different long string)

3. Navigate to **Project Settings** → **API** → **JWT Settings**
4. Copy **JWT Secret**: Used for token validation

---

## Step 4: Configure Google OAuth2

### 4.1 Create Google Cloud Project

1. Navigate to [console.cloud.google.com](https://console.cloud.google.com)
2. Click "Select a project" → "New Project"
3. Project name: `iris-oauth`
4. Click "Create"

### 4.2 Enable Google+ API

1. Navigate to **APIs & Services** → **Library**
2. Search for "Google+ API"
3. Click "Enable"

### 4.3 Create OAuth2 Credentials

1. Navigate to **APIs & Services** → **Credentials**
2. Click "Create Credentials" → "OAuth 2.0 Client ID"
3. Configure consent screen (first time):
   - User Type: **External**
   - App name: `Iris Development`
   - User support email: [your email]
   - Developer contact: [your email]
   - Scopes: Add `email` and `profile`
   - Test users: Add your Google account
   - Click "Save and Continue"

4. Create OAuth Client ID:
   - Application type: **Web application**
   - Name: `Iris Supabase Auth`
   - Authorized redirect URIs: `https://[your-project-ref].supabase.co/auth/v1/callback`
     - Example: `https://abcdefghijklmnopqrst.supabase.co/auth/v1/callback`
     - Get project-ref from Supabase Project URL
   - Click "Create"

5. **SAVE** Client ID and Client Secret

### 4.4 Configure Supabase Auth Provider

1. In Supabase dashboard: **Authentication** → **Providers**
2. Find "Google" provider
3. Enable toggle
4. Enter:
   - **Client ID**: From Google Cloud Console
   - **Client Secret**: From Google Cloud Console
5. **Authorized Client IDs**: Leave empty (or add for mobile later)
6. Click "Save"

---

## Step 5: Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env file
nano .env  # or use your preferred editor
```

**Fill in `.env` with your Supabase credentials:**

```bash
# Supabase Configuration
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_JWT_SECRET=your-jwt-secret-from-supabase-settings

# FastAPI Configuration
API_HOST=0.0.0.0
API_PORT=8000
ENVIRONMENT=development

# Logging
LOG_LEVEL=DEBUG
```

**Security Check**:
```bash
# Verify .env is gitignored
cat .gitignore | grep .env
# Should see: .env

# NEVER commit .env to version control!
```

---

## Step 6: Initialize Database Schema

```bash
# Run database initialization
just db-init

# Expected output:
# ✓ Connecting to Supabase...
# ✓ Creating tables: projects, tasks, ideas, reminders, notes
# ✓ Creating indexes...
# ✓ Enabling Row Level Security...
# ✓ Creating RLS policies...
# ✓ Creating utility functions...
# ✓ Schema initialization complete!
```

**Verify in Supabase Studio**:
1. Navigate to **Table Editor**
2. Should see 5 tables: projects, tasks, ideas, reminders, notes
3. Click on each table to verify columns match data-model.md

---

## Step 7: Start Development Environment

```bash
# Start FastAPI backend (Docker Compose)
just dev

# Expected output:
# Building API container...
# Starting iris-api...
# ✓ API running at http://localhost:8000
# ✓ Swagger docs at http://localhost:8000/docs
# ✓ Hot-reload enabled
```

**Test Health Endpoint**:
```bash
# In new terminal:
curl http://localhost:8000/health

# Expected response:
# {
#   "status": "healthy",
#   "supabase_connected": true,
#   "timestamp": "2025-10-20T14:30:00Z"
# }
```

---

## Step 8: Test OAuth2 Authentication Flow

### 8.1 Initiate OAuth Flow (Manual Test)

Since frontend is deferred to Sprint 2, we'll use Supabase Studio for OAuth testing:

1. Open Supabase Dashboard → **Authentication** → **Users**
2. Click "Add user" → "Sign in with Google"
3. Complete Google OAuth consent
4. Copy the JWT token from the response

**Alternative: Use Supabase CLI** (if installed):
```bash
supabase auth users create --email your@email.com --password temp-pass
# Then use Supabase client to get JWT
```

### 8.2 Test Protected Endpoint with JWT

```bash
# Set JWT token from OAuth flow
export JWT_TOKEN="eyJhbGciOiJIUzI1NiIs..."

# Test protected endpoint (list projects)
curl -H "Authorization: Bearer $JWT_TOKEN" \
  http://localhost:8000/api/v1/projects

# Expected response (empty array first time):
# []

# Create a project
curl -X POST \
  -H "Authorization: Bearer $JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "My First Project", "description": "Testing API"}' \
  http://localhost:8000/api/v1/projects

# Expected response:
# {
#   "id": "550e8400-e29b-41d4-a716-446655440000",
#   "user_id": "660e8400-e29b-41d4-a716-446655440111",
#   "name": "My First Project",
#   "description": "Testing API",
#   "status": "active",
#   "created_at": "2025-10-20T14:35:00Z",
#   "updated_at": "2025-10-20T14:35:00Z"
# }

# List projects again (should see your project)
curl -H "Authorization: Bearer $JWT_TOKEN" \
  http://localhost:8000/api/v1/projects
```

### 8.3 Test Row Level Security

```bash
# Try accessing without JWT (should fail)
curl http://localhost:8000/api/v1/projects

# Expected response:
# {
#   "detail": "Invalid authorization header format. Expected 'Bearer <token>'"
# }

# Try with invalid JWT (should fail)
curl -H "Authorization: Bearer invalid-token" \
  http://localhost:8000/api/v1/projects

# Expected response:
# {
#   "detail": "Invalid token: ..."
# }
```

---

## Step 9: Explore Swagger UI

1. Open browser: http://localhost:8000/docs
2. Click "Authorize" button (top right)
3. Enter: `Bearer <your-jwt-token>`
4. Click "Authorize"
5. Now you can test all endpoints interactively!

**Try these operations**:
- GET `/api/v1/projects` - List projects
- POST `/api/v1/projects` - Create project
- POST `/api/v1/tasks` - Create task
- GET `/api/v1/tasks?project_id=<uuid>` - List project tasks

---

## Step 10: Run Tests

```bash
# Run all tests
just test

# Expected output:
# ✓ Unit tests: 25 passed
# ✓ Integration tests: 12 passed
# ✓ Coverage: 87%

# Run specific test types
just test -m unit        # Unit tests only
just test -m integration # Integration tests only
```

---

## Development Workflow

### Daily Development

```bash
# Start servers
just dev

# Make code changes in src/
# Server auto-reloads (< 3 seconds)

# Run tests
just test

# Check linting
just lint

# Format code
just format

# Stop servers
just dev-stop
```

### Database Operations

```bash
# Reset database (WARNING: Deletes all data!)
just db-reset

# Apply new migration
just db-migrate

# View database logs
just db-logs
```

### Viewing Logs

```bash
# FastAPI logs
just dev-logs

# Follow logs in real-time
just dev-logs -f
```

---

## Troubleshooting

### Issue: Docker not running

**Error**: `Cannot connect to Docker daemon`

**Solution**:
```bash
# Start Docker Desktop (GUI application)
# Or on Linux:
sudo systemctl start docker

# Verify:
docker ps
```

### Issue: Port 8000 already in use

**Error**: `Address already in use: 0.0.0.0:8000`

**Solution**:
```bash
# Find process using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill process or change port in .env:
API_PORT=8001
```

### Issue: Supabase connection failed

**Error**: `Supabase connection failed`

**Solution**:
1. Verify `SUPABASE_URL` is correct in `.env`
2. Verify `SUPABASE_ANON_KEY` is correct
3. Check Supabase project is running (green status in dashboard)
4. Test connection manually:
```bash
curl https://xxxxx.supabase.co/rest/v1/
```

### Issue: JWT validation fails

**Error**: `Invalid token`

**Solution**:
1. Verify `SUPABASE_JWT_SECRET` matches Supabase dashboard setting
2. Check JWT hasn't expired (1 hour default)
3. Ensure JWT was issued by correct Supabase project
4. Verify token format: `Bearer <token>` (note the space)

### Issue: RLS blocks legitimate queries

**Error**: `No rows returned` (but data exists)

**Solution**:
1. Verify `user_id` in JWT matches `user_id` in database records
2. Check RLS policies are correctly configured:
```sql
-- In Supabase SQL Editor:
SELECT * FROM projects WHERE user_id = auth.uid();
```
3. Temporarily bypass RLS for debugging (development only):
```sql
-- Use service_role key instead of anon key
```

---

## Next Steps

✅ **Environment Setup Complete!**

**Recommended Next Actions**:

1. **Implement CRUD Routes** (Sprint 1):
   - Create FastAPI routes per `contracts/api-spec.yaml`
   - Add SQLModel models per `data-model.md`
   - Write unit tests for each endpoint

2. **Add Frontend** (Sprint 2):
   - Set up Tauri + React
   - Integrate Supabase client for OAuth
   - Build UI components per design system

3. **Enhance Security**:
   - Review security checklist (`checklists/security-auth.md`)
   - Implement security event logging
   - Add rate limiting

4. **Performance Optimization**:
   - Add caching layer
   - Optimize database indexes
   - Implement connection pooling

---

## Resources

- **Project Documentation**: `specs/002-dev-environment-setup/`
- **API Contracts**: `contracts/api-spec.yaml`
- **Data Model**: `data-model.md`
- **Research Decisions**: `research.md`
- **Supabase Docs**: [supabase.com/docs](https://supabase.com/docs)
- **FastAPI Docs**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)

---

## Support

**Issues?** Check:
1. This quickstart guide (troubleshooting section)
2. Project README.md
3. Spec `checklists/requirements.md` and `checklists/security-auth.md`
4. Open issue on GitHub

**Happy coding!** 🚀

