# Tasks: Cloud-First Development Environment Setup

**Input**: Design documents from `/specs/002-dev-environment-setup/`  
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/api-spec.yaml, quickstart.md

**Tests**: Included per spec requirements (unit and integration tests for each user story)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each workflow.

## Format: `[ID] [P?] [Story] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4, US5)
- Include exact file paths in descriptions

## Path Conventions
- Backend source: `src/iris/`
- Backend tests: `tests/`
- Configuration files at repository root
- Documentation in `docs/development/`

---

## Phase 1: Setup (Project Infrastructure)

**Purpose**: Initialize basic project structure and configuration files

- [x] T001 Create directory structure per plan.md (src/iris/config, src/iris/models, src/iris/database, src/iris/auth, src/iris/api/routes, src/iris/utils)
- [x] T002 [P] Create .env.example with Supabase configuration placeholders (SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_JWT_SECRET, API_PORT, ENVIRONMENT)
- [x] T003 [P] Add .env to .gitignore if not already present
- [x] T004 [P] Update pyproject.toml with new dependencies (supabase-py, python-jose[cryptography], python-multipart, pydantic-settings)
- [x] T005 Run uv sync to install new dependencies

**Checkpoint**: ✅ Basic structure and dependencies in place

---

## Phase 2: Foundational (Core Infrastructure)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Create Pydantic Settings class in src/iris/config/settings.py with all environment variables (SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_JWT_SECRET, API_HOST, API_PORT, ENVIRONMENT)
- [x] T007 Create singleton function get_settings() in src/iris/config/settings.py
- [x] T008 [P] Configure rich Console in src/iris/utils/logging.py with colored output support
- [x] T009 [P] Create custom exception classes in src/iris/utils/exceptions.py (DatabaseError, AuthenticationError, ValidationError)
- [x] T010 Create base SQLModel class in src/iris/models/base.py with common fields (id, user_id, created_at, updated_at)
- [x] T011 Create Supabase client singleton in src/iris/database/supabase.py with get_supabase() function per research.md RES-001
- [x] T012 Create FastAPI app instance in src/iris/api/main.py with CORS, exception handlers, and middleware
- [x] T013 Add global exception handlers to main.py (DatabaseError, AuthenticationError, ValidationError, generic Exception)

**Checkpoint**: ✅ Foundation ready - all shared infrastructure exists, user story implementation can begin

---

## Phase 3: User Story 1 - Development Environment Initialization (Priority: P1) 🎯

**Goal**: Developers can run `just dev-setup` to install dependencies and validate prerequisites

**Independent Test**: Run `just dev-setup` on fresh clone, verify dependencies installed, `.env` created, prerequisite checks pass, developer receives next-step instructions

### Tests for User Story 1

**NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T014 [P] [US1] Unit test for prerequisite validation in tests/unit/test_setup.py (verify Python version check, Docker check, Node check)
- [ ] T015 [P] [US1] Integration test for dev-setup command in tests/integration/test_dev_setup.py (run just dev-setup in clean environment)

### Implementation for User Story 1

- [ ] T016 [P] [US1] Create prerequisite check script in scripts/check-prerequisites.sh (or .ps1 for Windows) that validates Python, Docker, Node versions
- [ ] T017 [US1] Update justfile with dev-setup target that runs: uv sync, npm install (if package.json exists), cp .env.example .env, prerequisite checks
- [ ] T018 [US1] Add prerequisite validation output with rich library (colored success/error messages, summary table)
- [ ] T019 [US1] Add next-steps instructions to dev-setup output (configure .env, run just dev)
- [ ] T020 [US1] Test dev-setup command on fresh clone per acceptance scenarios

**Checkpoint**: ✅ `just dev-setup` working, developer can configure environment

---

## Phase 4: User Story 2 - Supabase Database Schema (Priority: P1) 🎯

**Goal**: Developers can run `just db-init` to create 5 core tables in Supabase with RLS policies

**Independent Test**: Run `just db-init`, verify all five tables created in Supabase Studio with correct columns, indexes, foreign keys, and RLS policies. Insert test data to verify constraints.

### Tests for User Story 2

- [ ] T021 [P] [US2] Unit test for database utility functions in tests/unit/test_database.py (update_updated_at, set_completed_timestamp triggers)
- [ ] T022 [P] [US2] Integration test for schema initialization in tests/integration/test_schema_init.py (creates all tables, foreign keys enforced)
- [ ] T023 [P] [US2] Integration test for RLS policies in tests/integration/test_rls.py (verify users can only access their own data)

### Implementation for User Story 2

- [x] T024 [US2] Create SQL migration file src/iris/database/migrations/001_initial_schema.sql with utility functions per data-model.md
- [x] T025 [US2] Add projects table creation to 001_initial_schema.sql (columns per data-model.md: id, user_id, name, description, status, created_at, updated_at)
- [x] T026 [US2] Add tasks table creation to 001_initial_schema.sql (columns: id, user_id, project_id, title, priority, due_date, completed, completed_at, notes, created_at, updated_at)
- [x] T027 [US2] Add ideas table creation to 001_initial_schema.sql (columns: id, user_id, title, description, promoted_to_project_id, created_at)
- [x] T028 [US2] Add reminders table creation to 001_initial_schema.sql (columns: id, user_id, task_id, message, due_time, created_at)
- [x] T029 [US2] Add notes table creation to 001_initial_schema.sql (columns: id, user_id, project_id, content, created_at, updated_at)
- [x] T030 [US2] Add indexes to all tables in 001_initial_schema.sql (user_id, foreign keys, created_at per data-model.md)
- [x] T031 [US2] Add RLS enable and policies to all tables in 001_initial_schema.sql (users_read_own, users_insert_own, users_update_own, users_delete_own per data-model.md)
- [x] T032 [US2] Create db-init script in scripts/db-init.sh (or .ps1) that applies migration SQL to Supabase using psql or Supabase Python client
- [x] T033 [US2] Create db-reset script in scripts/db-reset.sh (or .ps1) that drops all tables with confirmation prompt
- [x] T034 [US2] Update justfile with db-init and db-reset targets
- [ ] T035 [US2] Test db-init command against cloud Supabase per acceptance scenarios

**Checkpoint**: ✅ Database schema exists in Supabase, RLS policies active, independently testable

---

## Phase 5: User Story 3 - Supabase Authentication Integration (Priority: P2)

**Goal**: Google OAuth2 authentication via Supabase GoTrue works, returns JWT tokens

**Independent Test**: Initiate OAuth flow, complete Google sign-in, receive JWT, decode token to verify claims (user_id, email, provider="google")

### Tests for User Story 3

- [ ] T036 [P] [US3] Unit test for OAuth2 configuration validation in tests/unit/test_oauth_config.py
- [ ] T037 [P] [US3] Integration test for Google OAuth flow in tests/integration/test_oauth_flow.py (mock Supabase Auth response, verify JWT structure)

### Implementation for User Story 3

- [ ] T038 [P] [US3] Add Google OAuth2 configuration instructions to docs/development/oauth-setup.md (Google Cloud Console steps, Supabase provider config per quickstart.md)
- [ ] T039 [P] [US3] Create OAuth helper functions in src/iris/auth/oauth.py (initiate_google_oauth, handle_callback if needed for backend-initiated flows)
- [ ] T040 [US3] Add GOOGLE_OAUTH_CLIENT_ID and GOOGLE_OAUTH_CLIENT_SECRET to settings.py (optional for backend verification)
- [ ] T041 [US3] Document OAuth testing procedure in quickstart.md verification section (manual Google sign-in via Supabase Studio)
- [ ] T042 [US3] Test OAuth flow manually: configure Google provider in Supabase, sign in with Google, verify JWT token received per acceptance scenarios

**Checkpoint**: ✅ OAuth2 flow working, JWT tokens issued by Supabase with correct claims

---

## Phase 6: User Story 4 - FastAPI Backend with JWT Verification (Priority: P2) 🎯

**Goal**: FastAPI validates Supabase JWT tokens on protected routes, extracts user_id for authorization

**Independent Test**: Start FastAPI server, call `/health` (200 OK), call protected endpoint without token (401), with valid token (200), with invalid token (401)

### Tests for User Story 4

- [ ] T043 [P] [US4] Unit test for JWT validation function in tests/unit/test_jwt.py (valid token, expired token, tampered token, missing claims)
- [ ] T044 [P] [US4] Unit test for get_current_user_id dependency in tests/unit/test_auth_dependencies.py
- [ ] T045 [P] [US4] Integration test for protected endpoints in tests/integration/test_protected_routes.py (with/without JWT, RLS enforcement)

### Implementation for User Story 4

- [x] T046 [P] [US4] Create Project SQLModel in src/iris/models/project.py extending BaseModel (fields per data-model.md)
- [x] T047 [P] [US4] Create Task SQLModel in src/iris/models/task.py extending BaseModel
- [x] T048 [P] [US4] Create Idea SQLModel in src/iris/models/idea.py extending BaseModel
- [x] T049 [P] [US4] Create Reminder SQLModel in src/iris/models/reminder.py extending BaseModel
- [x] T050 [P] [US4] Create Note SQLModel in src/iris/models/note.py extending BaseModel
- [x] T051 [US4] Implement JWT validation function in src/iris/auth/jwt.py per research.md RES-003 (validate_jwt with python-jose, algorithm HS256, audience check, provider check)
- [x] T052 [US4] Create FastAPI dependency get_current_user_id in src/iris/auth/dependencies.py that calls validate_jwt per research.md RES-008
- [x] T053 [US4] Implement health endpoint in src/iris/api/health.py (unprotected, returns status and Supabase connection check)
- [x] T054 [US4] Create router for projects in src/iris/api/routes/projects.py with protected GET /projects endpoint (returns empty list for now)
- [x] T055 [US4] Add user_id dependency to projects router (user_id: str = Depends(get_current_user_id))
- [x] T056 [US4] Implement POST /projects endpoint in projects.py per contracts/api-spec.yaml (creates project with user_id from JWT)
- [x] T057 [US4] Implement GET /projects/{project_id} endpoint in projects.py
- [x] T058 [US4] Implement PATCH /projects/{project_id} endpoint in projects.py
- [x] T059 [US4] Implement DELETE /projects/{project_id} endpoint in projects.py
- [x] T060 [P] [US4] Create router for tasks in src/iris/api/routes/tasks.py with all CRUD endpoints per contracts/api-spec.yaml
- [x] T061 [P] [US4] Create router for ideas in src/iris/api/routes/ideas.py with all CRUD endpoints per contracts/api-spec.yaml
- [x] T062 [P] [US4] Create router for reminders in src/iris/api/routes/reminders.py with all CRUD endpoints per contracts/api-spec.yaml
- [x] T063 [P] [US4] Create router for notes in src/iris/api/routes/notes.py with all CRUD endpoints per contracts/api-spec.yaml
- [x] T064 [US4] Register all routers in src/iris/api/main.py with /api/v1 prefix
- [x] T065 [US4] Add error handling for 401 Unauthorized responses with specific error messages (missing token, invalid format, expired, tampered) per FR-022
- [x] T066 [US4] Add error handling for 404 Not Found when RLS filters out results (user doesn't own resource)
- [ ] T067 [US4] Test protected endpoints per acceptance scenarios (no token → 401, invalid token → 401, valid token → 200)
- [ ] T068 [US4] Verify RLS enforcement: user A cannot access user B's data via API

**Checkpoint**: ✅ FastAPI backend with JWT auth working, all CRUD endpoints protected, RLS enforcing user isolation

---

## Phase 7: User Story 5 - Docker Compose Development Stack (Priority: P3)

**Goal**: Developers can run `just dev` to start FastAPI in Docker with hot-reload

**Independent Test**: Run `just dev`, verify container starts, access `/health` endpoint, modify code, verify hot-reload works in < 3 seconds

### Tests for User Story 5

- [ ] T069 [P] [US5] Integration test for Docker Compose startup in tests/integration/test_docker.py (verify services healthy, ports accessible)

### Implementation for User Story 5

- [ ] T070 [P] [US5] Create Dockerfile at repository root with Python 3.12 base, uv installation, dependency copying per research.md RES-006
- [ ] T071 [US5] Create docker-compose.yml at repository root with api service (port 8000, volume mount src/, env_file .env, uvicorn --reload command) per research.md RES-006
- [ ] T072 [US5] Create .dockerignore file (exclude .venv, __pycache__, .git, .env)
- [ ] T073 [US5] Update justfile with dev target (docker-compose up -d --build)
- [ ] T074 [US5] Update justfile with dev-stop target (docker-compose down)
- [ ] T075 [US5] Update justfile with dev-logs target (docker-compose logs -f api)
- [ ] T076 [US5] Add healthcheck to docker-compose.yml (curl http://localhost:8000/health every 10s)
- [ ] T077 [US5] Test Docker Compose startup per acceptance scenarios (just dev, access API, modify code, verify hot-reload)

**Checkpoint**: ✅ Docker development environment working with hot-reload, consistent across platforms

---

## Phase 8: Polish & Documentation

**Purpose**: Final touches, documentation updates, and comprehensive validation

- [ ] T078 [P] Update README.md with cloud-first architecture note and OAuth2 authentication requirement
- [ ] T079 [P] Update docs/development/ with new guide: supabase-setup.md (Supabase project creation, Google OAuth configuration, schema initialization)
- [ ] T080 [P] Add API documentation link to README (Swagger UI at /docs)
- [ ] T081 Create example .env file with detailed comments for each variable
- [ ] T082 Add troubleshooting section to quickstart.md (common errors: Docker not running, port conflicts, Supabase connection issues)
- [ ] T083 [P] Update planning/CONSTITUTION.md Principle 1 from "Local-First Forever" to "Cloud-First, Offline Later" with pivot rationale
- [ ] T084 [P] Update planning/original/ARCHITECTURE.md to remove SQLite references and add cloud-first data flow diagram
- [ ] T085 Validate quickstart.md by following all steps on fresh environment
- [ ] T086 Run full test suite (just test) and verify all tests pass with ≥85% coverage
- [ ] T087 Run just ci to verify all quality checks pass (lint, type-check, test)

**Checkpoint**: ✅ Documentation complete, environment validated, ready for Sprint 1 CRUD implementation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup (Phase 1) - BLOCKS all user stories
- **User Story 1 (Phase 3 - P1)**: Depends on Foundational (Phase 2) - Independent of other stories
- **User Story 2 (Phase 4 - P1)**: Depends on Foundational (Phase 2) - Independent of other stories  
- **User Story 3 (Phase 5 - P2)**: Depends on Foundational (Phase 2) - Independent of other stories
- **User Story 4 (Phase 6 - P2)**: Depends on Foundational (Phase 2) + User Story 2 (Phase 4) complete (needs database schema) + User Story 3 (Phase 5) complete (needs OAuth for JWT tokens)
- **User Story 5 (Phase 7 - P3)**: Depends on User Story 4 complete (needs working API to Dockerize)
- **Polish (Phase 8)**: Depends on all user stories complete

### User Story Dependencies

**Critical Path**:
```
Phase 1: Setup
  ↓
Phase 2: Foundational (BLOCKS EVERYTHING)
  ↓
Phase 3: US1 (Environment Init) - Can run in parallel with US2, US3
Phase 4: US2 (Database Schema) - Can run in parallel with US1, US3
Phase 5: US3 (OAuth2 Auth) - Can run in parallel with US1, US2
  ↓
Phase 6: US4 (FastAPI JWT) - DEPENDS on US2 + US3 (needs schema + auth)
  ↓
Phase 7: US5 (Docker) - DEPENDS on US4 (needs working API)
  ↓
Phase 8: Polish
```

**Parallel Opportunities**:
- US1, US2, US3 can all run in parallel after Foundational phase
- US4 must wait for US2 + US3
- US5 must wait for US4

**Recommended Order** (solo developer):
1. Setup → Foundational (required)
2. US2 (Database) - Most foundational
3. US3 (OAuth2) - Needed for JWT tokens
4. US1 (Environment) - Can be done anytime, low dependency
5. US4 (FastAPI JWT) - Integrates US2 + US3
6. US5 (Docker) - Packages everything
7. Polish

### Within Each User Story

- Tests FIRST (write tests, verify they FAIL)
- Models in parallel (marked [P])
- Services after models
- Endpoints after services
- Integration tests verify story complete

### Parallel Opportunities

**Foundational Phase**:
```bash
# These can all run in parallel:
T008: Configure rich logging
T009: Create exception classes
T010: Create base SQLModel
T011: Create Supabase client
```

**User Story 2 (Database)**:
```bash
# All table definitions can run in parallel:
T025: projects table
T026: tasks table
T027: ideas table
T028: reminders table
T029: notes table
T030: indexes (after tables exist)
T031: RLS policies (after tables exist)
```

**User Story 4 (API Routes)**:
```bash
# After JWT validation exists, all routers can run in parallel:
T054-T059: projects router (all CRUD)
T060: tasks router
T061: ideas router
T062: reminders router
T063: notes router
```

**Documentation (Phase 8)**:
```bash
# All documentation updates can run in parallel:
T078: README update
T079: Supabase setup guide
T080: API docs link
T083: Constitution update
T084: Architecture update
```

---

## Implementation Strategy

### MVP First (Minimum Viable Product)

**Goal**: Get working environment and database with minimal features

**Phases to Complete**:
1. Phase 1: Setup (T001-T005) - ~30 minutes
2. Phase 2: Foundational (T006-T013) - ~2 hours
3. Phase 4: User Story 2 - Database Schema (T021-T035) - ~3 hours
   - **STOP and VALIDATE**: Run `just db-init`, verify tables in Supabase Studio, test RLS
4. Phase 5: User Story 3 - OAuth2 (T036-T042) - ~2 hours
   - **STOP and VALIDATE**: Complete Google sign-in, receive JWT token
5. Phase 6: User Story 4 - FastAPI JWT (T043-T068) - ~4 hours
   - **STOP and VALIDATE**: Test protected endpoints with JWT, verify RLS

**At this point you have**:
- ✅ Working database schema with RLS
- ✅ OAuth2 authentication
- ✅ Protected API endpoints
- ✅ Full CRUD for all 5 entities
- ✅ Security enforced

**This is a functional MVP!** Can deploy and use for development.

**Optional additions**:
- Phase 3: User Story 1 - Environment setup polish (T014-T020) - ~1 hour
- Phase 7: User Story 5 - Docker (T069-T077) - ~1.5 hours
- Phase 8: Polish (T078-T087) - ~2 hours

**Total MVP Time**: ~11-12 hours
**Total with Polish**: ~14-15 hours

### Incremental Delivery Checkpoints

**Checkpoint 1** (After Phase 4 - US2): Database schema exists
- Tables created in Supabase
- RLS policies active
- Can manually insert data via Supabase Studio
- Validates data model

**Checkpoint 2** (After Phase 5 - US3): Authentication working
- Google OAuth2 configured
- JWT tokens issued
- Can test auth flow manually
- Validates OAuth integration

**Checkpoint 3** (After Phase 6 - US4): Full API functional
- Protected endpoints working
- JWT validation enforced
- CRUD operations for all 5 entities
- RLS automatically filtering by user
- **READY FOR SPRINT 1 FEATURE DEVELOPMENT**

**Checkpoint 4** (After Phase 7 - US5): Dockerized
- Consistent development environment
- Hot-reload for fast iteration
- Multi-platform support
- Ready for team collaboration

**Checkpoint 5** (After Phase 8 - Polish): Production-ready
- Complete documentation
- Constitution/architecture updated
- Full test coverage
- Quality checks passing

---

## Validation Criteria

### User Story 1 (Environment Init)
- [ ] `just dev-setup` completes successfully on fresh clone
- [ ] Dependencies installed (Python packages, Node if needed)
- [ ] `.env` created from `.env.example`
- [ ] Prerequisite checks validate Python, Docker, Node versions
- [ ] Developer receives clear next-step instructions

### User Story 2 (Database Schema)
- [ ] `just db-init` creates all 5 tables in Supabase (projects, tasks, ideas, reminders, notes)
- [ ] All columns match data-model.md specifications (types, constraints, defaults)
- [ ] Foreign keys enforce referential integrity
- [ ] Indexes created on user_id, foreign keys, created_at
- [ ] RLS policies enabled on all tables
- [ ] Users can only access their own data (verified via Supabase Studio)

### User Story 3 (OAuth2 Auth)
- [ ] Google OAuth provider configured in Supabase dashboard
- [ ] OAuth flow redirects to Google consent screen
- [ ] Successful auth returns JWT and refresh tokens
- [ ] JWT contains required claims (sub, email, provider="google", role, exp)
- [ ] Refresh token can obtain new access token
- [ ] Failed auth (user denies) returns clear error

### User Story 4 (FastAPI JWT)
- [ ] `/health` endpoint accessible without authentication (200 OK)
- [ ] Protected endpoints return 401 without Authorization header
- [ ] Protected endpoints return 401 with invalid/expired JWT
- [ ] Protected endpoints return 200 with valid JWT
- [ ] user_id extracted from JWT and available to route handlers
- [ ] All 5 entity CRUD endpoints working (projects, tasks, ideas, reminders, notes)
- [ ] RLS enforcement: User A cannot access User B's data via API
- [ ] Code changes hot-reload in < 3 seconds

### User Story 5 (Docker Compose)
- [ ] `just dev` starts Docker Compose successfully
- [ ] FastAPI container achieves healthy status in < 30 seconds
- [ ] API accessible at http://localhost:8000
- [ ] `/docs` shows Swagger UI with all endpoints
- [ ] `just dev-logs` displays container logs
- [ ] `just dev-stop` stops containers gracefully
- [ ] Hot-reload works with volume-mounted code
- [ ] Environment variables from `.env` loaded correctly

### Overall System
- [ ] All tests pass (just test) with ≥85% coverage
- [ ] Linting passes (just lint)
- [ ] Type checking passes (just type-check)
- [ ] CI pipeline passes (just ci)
- [ ] Quickstart.md instructions work on fresh environment
- [ ] All API contracts match contracts/api-spec.yaml

---

## Notes

- **[P] tasks** = Different files, can run in parallel
- **[Story] labels** = Map tasks to user stories for traceability
- **Tests FIRST** = TDD approach, write tests before implementation
- **Independent testing** = Each user story validates independently
- **Commit frequently** = Commit after each logical group of tasks
- **Stop at checkpoints** = Validate each user story works before moving to next

---

## Task Statistics

- **Total Tasks**: 87
- **Setup Phase**: 5 tasks
- **Foundational Phase**: 8 tasks (CRITICAL PATH - blocks all stories)
- **User Story 1 (P1)**: 7 tasks (Environment initialization)
- **User Story 2 (P1)**: 15 tasks (Database schema)
- **User Story 3 (P2)**: 7 tasks (OAuth2 authentication)
- **User Story 4 (P2)**: 26 tasks (FastAPI JWT + CRUD)
- **User Story 5 (P3)**: 9 tasks (Docker Compose)
- **Polish Phase**: 10 tasks

**Parallelizable Tasks**: 29 tasks marked with [P] (33% of total)

**MVP Scope** (Phases 1, 2, 4, 5, 6): 62 tasks (~71% of total, ~11-12 hours)

**Full Feature Scope**: 87 tasks (~14-15 hours)

**Critical Path**: Phase 2 (Foundational) must complete before user stories → US2 + US3 before US4 → US4 before US5

---

**Ready to implement!** Start with Phase 1 and work through systematically. Each checkpoint provides a working, independently testable increment. 🚀

