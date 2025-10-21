# Implementation Plan: Cloud-First Development Environment Setup

**Branch**: `002-dev-environment-setup` | **Date**: October 20, 2025 | **Spec**: [spec.md](spec.md)  
**Input**: Feature specification from `/specs/002-dev-environment-setup/spec.md`

## Summary

Implement cloud-first development environment for Iris using Supabase as primary data store with Google OAuth2 authentication. This foundational infrastructure enables Sprint 0 completion by establishing Docker Compose development stack, Supabase database schema (5 core tables with RLS), Google OAuth2 via Supabase GoTrue, FastAPI backend with JWT verification, and developer workflow automation via `just` commands. Key architectural decision: Pivot from local-first (SQLite + sync) to cloud-first (Supabase primary) for faster MVP delivery, with offline mode deferred to Phase 2+.

## Technical Context

**Language/Version**: Python 3.12/3.13 (per existing CI setup)  
**Primary Dependencies**: FastAPI, Supabase Python client (supabase-py), python-jose[cryptography], Pydantic Settings, Rich (logging)  
**Storage**: Supabase PostgreSQL (cloud) with Row Level Security, pgvector for future semantic features  
**Testing**: pytest with explicit decorators (@pytest.mark.unit/integration), just test command  
**Target Platform**: Cross-platform development (Windows, macOS, Linux) via Docker Compose + uv  
**Project Type**: Web application (FastAPI backend, Tauri frontend deferred to Sprint 2)  
**Performance Goals**: 
- Environment setup < 2 min (excluding downloads)
- Database init < 10 sec
- OAuth flow < 3 sec (excluding Google consent)
- JWT validation < 50ms p95
- API CRUD < 200ms per Constitution Principle 13

**Constraints**: 
- Cloud connectivity required (cloud-first model, no offline in Sprint 0)
- Supabase free tier limits (500MB database, 50K monthly active users sufficient for MVP)
- No local credential storage (all auth via Supabase/Google)
- Zero data loss (Constitution Principle 2)
- Performance budgets enforced (Constitution Principle 13)

**Scale/Scope**: 
- 5 database tables (projects, tasks, ideas, reminders, notes)
- Single developer environment initially
- 1,000 projects, 10,000 tasks per project (Constitution Principle 16)

## Constitution Check

**CRITICAL VIOLATION - Requires Justification**:

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| **Principle 1: "Local-First Forever"** → Cloud-First | Faster MVP delivery, reduced complexity, proven Supabase architecture | Local SQLite + sync engine adds 2-3 weeks development time, introduces sync conflict complexity, requires offline testing infrastructure not yet in place. Cloud-first validates product-market fit faster, leverages Supabase's battle-tested auth/RLS, defers offline mode until product validation complete. |
| Internet connectivity required (violates "offline functionality is non-negotiable") | Cloud-first model requires Supabase connection for all operations | Offline mode requires: local SQLite, bidirectional sync, conflict resolution, queue management. Deferred to Phase 2+ per PIVOT-NOTES.md after cloud version stabilizes. |

**Constitution Updates Required**:
- [ ] Update Principle 1 from "Local-First Forever" to "Cloud-First, Offline Later" 
- [ ] Document rationale in constitution: "Pivot to cloud-first for Sprint 0 enables faster validation. Offline mode planned for Phase 2 after cloud architecture proven."
- [ ] Add assumption: "Development requires internet connectivity until offline mode implemented"

**Compliant Principles**:
- ✅ Principle 2 (Zero Data Loss): Supabase handles durability, RLS prevents data corruption
- ✅ Principle 3 (Privacy by Design): User data scoped by RLS, no telemetry by default, Google OAuth explicit consent
- ✅ Principle 4 (Performance is Feature): Performance targets defined (SC-003 through SC-010)
- ✅ Code Quality Principle 1 (Type Safety): Pydantic for config, type hints required
- ✅ Code Quality Principle 4 (Error Handling): Rich library for logging (FR-028)
- ✅ Testing Principle 6 (Test Pyramid): pytest with explicit decorators (just test command)
- ✅ Tooling Principle 19: uv for deps, just for commands, no .venv references

**Re-evaluation After Phase 1 Design**: Will verify JWT security, RLS policies, OAuth2 flow comply with security principles.

## Project Structure

### Documentation (this feature)

```
specs/002-dev-environment-setup/
├── spec.md              # Feature specification (complete)
├── PIVOT-NOTES.md       # Cloud-first pivot rationale (complete)
├── checklists/
│   ├── requirements.md  # General requirements quality (complete)
│   └── security-auth.md # Security & OAuth2 requirements quality (complete)
├── plan.md              # This file (in progress)
├── research.md          # Phase 0 output (to be generated)
├── data-model.md        # Phase 1 output (to be generated)
├── quickstart.md        # Phase 1 output (to be generated)
├── contracts/           # Phase 1 output (to be generated)
│   └── api-spec.yaml    # OpenAPI spec for FastAPI routes
└── tasks.md             # Phase 2 output (via /speckit.tasks)
```

### Source Code (repository root)

**Structure Decision**: Web application pattern (FastAPI backend now, Tauri frontend Sprint 2)

```
# Backend (Sprint 0 focus)
src/iris/
├── __init__.py
├── config/
│   └── settings.py       # Pydantic Settings (FR-027, Constitution Principle 2)
├── models/
│   ├── __init__.py
│   ├── project.py        # SQLModel for projects table
│   ├── task.py           # SQLModel for tasks table
│   ├── idea.py           # SQLModel for ideas table
│   ├── reminder.py       # SQLModel for reminders table
│   └── note.py           # SQLModel for notes table
├── database/
│   ├── __init__.py
│   ├── supabase.py       # Supabase client initialization
│   └── migrations/       # SQL migration files for schema
│       └── 001_initial_schema.sql
├── auth/
│   ├── __init__.py
│   ├── jwt.py            # JWT validation middleware (FR-021, FR-022)
│   └── dependencies.py   # FastAPI dependency injection for auth
├── api/
│   ├── __init__.py
│   ├── main.py           # FastAPI app initialization
│   ├── health.py         # Health endpoint (FR-020)
│   └── routes/
│       ├── __init__.py
│       ├── projects.py   # Project CRUD (protected endpoints)
│       ├── tasks.py      # Task CRUD (protected endpoints)
│       ├── ideas.py      # Idea CRUD (protected endpoints)
│       ├── reminders.py  # Reminder CRUD (protected endpoints)
│       └── notes.py      # Note CRUD (protected endpoints)
└── utils/
    ├── __init__.py
    └── logging.py        # Rich logging configuration (FR-028)

tests/
├── __init__.py
├── conftest.py           # Pytest fixtures (Supabase mock, test DB)
├── unit/
│   ├── __init__.py
│   ├── test_jwt.py       # JWT validation unit tests
│   ├── test_models.py    # SQLModel validation tests
│   └── test_config.py    # Settings validation tests
└── integration/
    ├── __init__.py
    ├── test_auth_flow.py # OAuth2 + JWT integration test
    ├── test_api_crud.py  # Protected endpoint tests
    └── test_rls.py       # Row Level Security tests

# Development Environment
.env.example              # Template with Supabase placeholders (FR-003)
docker-compose.yml        # FastAPI container only (FR-001, US5)
Dockerfile                # FastAPI with hot-reload support (FR-002)
justfile                  # Extended with new commands (FR-030 through FR-034)

# Frontend (Sprint 2 - not in this spec)
frontend/                 # Deferred to Sprint 2 per spec Out of Scope
```

**Key Structure Decisions**:
1. **Modular API routes**: Separate file per entity for maintainability
2. **Auth as middleware**: JWT validation via dependency injection (FR-023)
3. **Config centralization**: Single settings.py using Pydantic (Constitution Principle 2)
4. **Migration-based schema**: SQL files in migrations/ for reproducibility
5. **Test isolation**: Unit vs integration split, explicit pytest markers

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Cloud-First (violates Principle 1) | Faster MVP delivery (2-3 weeks saved), proven Supabase patterns, leverages managed auth/RLS | Local SQLite + sync: Complex conflict resolution, queue management, offline test infrastructure. Delays validation. Cloud-first proves product viability faster. |
| Google OAuth2 only (no email/password) | Eliminates password storage, complexity, security risks. Google handles MFA, account recovery | Email/password requires: password hashing, reset flows, email verification, rate limiting, account lockout. OAuth2 delegates security to Google's battle-tested implementation. |
| Supabase vendor lock-in | Managed PostgreSQL + Auth + RLS + Realtime in one service. Free tier sufficient for MVP | Self-hosted PostgreSQL + Auth service + RLS policies + WebSocket server: 4 separate systems to configure/maintain. Supabase consolidates with migration path (standard PostgreSQL). |

**Justification Summary**: All complexity choices prioritize speed-to-market for MVP validation. Cloud-first architecture is simpler than local-first for initial release. Offline mode deferred until product validation complete. Supabase reduces operational complexity while maintaining PostgreSQL portability.

---

## Phase 0: Research & Unknowns

**Status**: To be completed - see [research.md](research.md)

**Unknowns Identified from Technical Context**:
1. Supabase Python client (supabase-py) best practices for FastAPI integration
2. Google OAuth2 provider configuration in Supabase dashboard (callback URLs, scopes)
3. JWT validation using Supabase JWT_SECRET (algorithm, claims validation)
4. Row Level Security (RLS) policy patterns for user_id enforcement
5. SQLModel with PostgreSQL (vs SQLite) - type mappings, UUIDs, timestamps
6. Docker Compose with FastAPI hot-reload (volume mounting, uvicorn watch)
7. Migration strategy for Supabase PostgreSQL (SQL files vs ORM migrations)
8. FastAPI dependency injection for authenticated user_id extraction

**Research Tasks**:
- [RES-001] Research Supabase Python client initialization and connection pooling
- [RES-002] Document Google OAuth2 setup in Supabase (credentials, callback URLs)
- [RES-003] Analyze JWT validation patterns with python-jose + Supabase
- [RES-004] Evaluate RLS policy templates for multi-tenant user isolation
- [RES-005] Determine SQLModel + PostgreSQL best practices (UUID primary keys, timestamptz)
- [RES-006] Investigate FastAPI + Docker hot-reload configurations
- [RES-007] Define migration workflow (Supabase Migration API vs raw SQL)
- [RES-008] Document FastAPI Depends() pattern for user_id injection

**Output**: [research.md](research.md) will contain decisions, rationale, and code examples for each research task.

---

## Phase 1: Design & Contracts

**Status**: To be completed after Phase 0

**Outputs**:
1. **[data-model.md](data-model.md)**: 5 core entities (projects, tasks, ideas, reminders, notes) with:
   - Table schemas (columns, types, constraints)
   - Foreign key relationships
   - RLS policy definitions
   - Indexes for performance

2. **[contracts/api-spec.yaml](contracts/api-spec.yaml)**: OpenAPI 3.1 specification with:
   - Authentication scheme (OAuth2 + JWT Bearer)
   - Protected endpoints (CRUD for 5 entities)
   - Request/response schemas
   - Error responses (401, 403, 404, 500)

3. **[quickstart.md](quickstart.md)**: Developer onboarding guide with:
   - Prerequisites (Docker, uv, Google Cloud Console OAuth2 setup)
   - Supabase project creation + Google provider configuration
   - `.env` configuration template
   - `just dev-setup` walkthrough
   - First OAuth2 login flow test
   - Protected API endpoint test with JWT

4. **Agent Context Update**: Updated `.cursorrules` or `.agents/cursor-rules.md` with:
   - Supabase Python client patterns
   - FastAPI + JWT middleware boilerplate
   - SQLModel + PostgreSQL conventions
   - Constitution compliance reminders

---

## Implementation Notes

### Critical Path
1. Phase 0 (Research) → Resolve all NEEDS CLARIFICATION
2. Constitution update (Principle 1 cloud-first pivot)
3. Phase 1 (Design) → Database schema + API contracts
4. Phase 2 (Tasks via /speckit.tasks) → Granular implementation steps

### Risk Mitigation
- **Supabase free tier limits**: Monitor usage, plan upgrade path
- **Google OAuth2 changes**: Use Supabase abstraction layer for provider portability
- **JWT expiration in development**: Document refresh token testing procedures
- **RLS policy errors**: Create debug mode flag to bypass RLS during development

### Dependencies on External Services
- Supabase cloud availability (99.9% uptime assumed)
- Google OAuth2 API (Google account required for developers)
- Docker Hub for base images (FastAPI, Python 3.12)

### Future Phases
- **Sprint 1**: CRUD implementation, FastAPI routes, SQLModel integration
- **Sprint 2**: Tauri frontend, Supabase client-side integration
- **Phase 2** (later): Offline mode implementation (local SQLite + sync engine)

---

**Next Steps**: Execute Phase 0 research to generate [research.md](research.md).
