# 🔄 Cloud-First Architectural Pivot Summary

**Date**: October 20, 2025  
**Spec**: 002-dev-environment-setup  
**Decision**: Hard pivot from local-first to cloud-first architecture

---

## 📊 What Changed

### ❌ **Removed from Sprint 0**

| Component | Reason |
|-----------|--------|
| SQLite local database | Replaced by Supabase cloud PostgreSQL |
| Sync engine (local ↔ cloud) | No longer needed with single source of truth |
| Offline-first functionality | Deferred to Phase 2 or later |
| `iris` CLI tools | Polish deferred to later sprint |
| Local Supabase Docker | Cloud Supabase only |

### ✅ **Added to Sprint 0**

| Component | Purpose |
|-----------|---------|
| Supabase Auth (GoTrue) | User registration, login, JWT tokens |
| JWT verification in FastAPI | Protect API routes with token validation |
| User isolation (user_id in all tables) | Enable Row Level Security |
| RLS policies | User-scoped data access |
| Cloud-required environment setup | Supabase credentials configuration |

---

## 📋 New Sprint 0 Scope

### User Stories (Prioritized)

**P1 - Foundation**:
1. ✅ Development Environment Initialization (`just dev-setup`)
2. ✅ Supabase Database Schema (5 tables with user_id)

**P2 - Authentication & API**:
3. ✅ Supabase Auth Integration (register, login, JWT)
4. ✅ FastAPI JWT Verification (protected routes)

**P3 - Infrastructure**:
5. ✅ Docker Compose Stack (FastAPI only)

### Just Targets

| Command | Purpose |
|---------|---------|
| `just dev-setup` | Install dependencies, create `.env`, validate prerequisites |
| `just dev` | Start FastAPI server (Docker or direct uvicorn) |
| `just dev-stop` | Stop all running services |
| `just dev-logs` | Display service logs |
| `just db-init` | Create Supabase schema (5 tables + RLS) |
| `just db-reset` | Drop and recreate schema (dev only) |

### Database Schema (Supabase Cloud)

All tables include `user_id` column:

```sql
-- All records belong to authenticated user
CREATE TABLE projects (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES auth.users NOT NULL,
  name TEXT NOT NULL,
  description TEXT,
  status TEXT CHECK (status IN ('active', 'archived', 'completed')),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Similar structure for: tasks, ideas, reminders, notes
```

Row Level Security:
```sql
ALTER TABLE projects ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Users see only their own projects"
  ON projects FOR ALL
  USING (auth.uid() = user_id);
```

---

## 🚨 **ACTION REQUIRED**

### 1. Update Constitution (`planning/CONSTITUTION.md`)

**Current**:
```markdown
### 1. **Local-First Forever**
- User data MUST reside locally first (SQLite)
- Cloud sync is enhancement, not requirement
- Offline functionality is non-negotiable
```

**Change to**:
```markdown
### 1. **Cloud-First, Offline Later**
- User data resides in Supabase cloud (primary source of truth)
- Internet connectivity required for MVP
- Offline functionality deferred to Phase 2+
- Local-first model revisited after cloud version stabilizes
```

**Rationale**: Faster MVP delivery, reduced complexity, proven architecture

### 2. Update Architecture (`planning/original/ARCHITECTURE.md`)

**Remove**:
- SQLite database layer
- Sync engine diagrams
- Local-first flow diagrams

**Add**:
- Supabase as primary data store
- Authentication flow: Supabase Auth → JWT → FastAPI verification
- RLS policies for user data isolation
- Cloud-only data flow

**New Architecture**:
```
User (Browser/Desktop App)
    ↓
Supabase Auth (GoTrue)
    ↓ (JWT token)
FastAPI Backend
    ↓ (validates JWT, extracts user_id)
Supabase PostgreSQL (cloud)
    ↓ (RLS policies filter by user_id)
User-specific data only
```

### 3. Update Roadmap/Sprints

**Sprint 0 deliverable update**:
- ✅ Running FastAPI backend with JWT auth
- ✅ Supabase cloud database with 5 tables
- ✅ User registration and login working
- ✅ Protected API endpoints
- ❌ ~~Local SQLite database~~ (removed)
- ❌ ~~Sync engine skeleton~~ (removed)

**Sprint 1 implications**:
- CRUD operations work directly with Supabase (no local layer)
- All API routes use authenticated `user_id` for filtering
- RLS policies automatically enforce user isolation
- No sync logic needed

---

## 📐 Technical Details

### Environment Variables (`.env`)

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
```

### FastAPI JWT Middleware

```python
from fastapi import Depends, HTTPException, Header
from jose import jwt, JWTError

async def get_current_user(authorization: str = Header(...)):
    """Extract and validate JWT token from Authorization header."""
    if not authorization.startswith("Bearer "):
        raise HTTPException(401, "Invalid authorization header")
    
    token = authorization.replace("Bearer ", "")
    
    try:
        payload = jwt.decode(
            token,
            settings.SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            audience="authenticated"
        )
        return payload["sub"]  # user_id
    except JWTError:
        raise HTTPException(401, "Invalid or expired token")
```

### Docker Compose (FastAPI only)

```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./src:/app/src  # Hot reload
    env_file:
      - .env
    command: uvicorn src.iris.main:app --host 0.0.0.0 --reload
```

---

## 🎯 Success Metrics

| Metric | Target | Validates |
|--------|--------|-----------|
| Setup time | < 2 min | Environment initialization |
| Schema creation | < 10 sec | Database setup |
| User registration | < 2 sec | Auth integration |
| JWT validation | < 50ms (p95) | API security |
| Hot-reload | < 3 sec | Developer experience |
| Zero auth bypasses | 100% | Security enforcement |

---

## 📝 Next Steps

1. ✅ Spec completed and validated
2. **Next**: Run `/speckit.plan` to create implementation plan
3. Update Constitution (Principle 1)
4. Update Architecture document
5. Begin implementation (Sprint 0)

---

## ❓ Questions Answered

**Q: Setup vs servers?**  
A: `just dev-setup` = environment initialization, `just dev` = start servers

**Q: Iris CLI?**  
A: Deferred to later sprint (polish)

**Q: Local vs cloud Supabase?**  
A: Cloud Supabase only - no local Docker Supabase

**Q: Database fields?**  
A: Best guess from Architecture.md - 5 entities with user_id added to all

**Q: Docker Compose servers?**  
A: FastAPI only (frontend in Sprint 2, no local Supabase)

**Q: Push to where?**  
A: No push/sync needed - Supabase cloud is the single source of truth

---

*This pivot enables faster MVP delivery while maintaining path to offline functionality in future phases.*

