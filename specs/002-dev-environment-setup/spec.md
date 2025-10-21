# Feature Specification: Cloud-First Development Environment Setup

**Feature Branch**: `002-dev-environment-setup`  
**Created**: October 20, 2025  
**Updated**: October 20, 2025 (Cloud-First Pivot)  
**Status**: Draft  
**Architecture**: Cloud-First (Local/Offline deferred to future sprint)

## 🚨 Architectural Pivot Note

**Original Direction**: Local-first with SQLite + Supabase sync  
**New Direction**: Cloud-first with Supabase as primary data store  
**Rationale**: Simplified MVP delivery, faster time to working product, offline mode deferred

**Deprecated from Sprint 0**:
- Local SQLite database
- Sync engine (local ↔ cloud)
- Offline-first functionality
- `iris` CLI tools (polish for later)

**New Requirements**:
- Supabase as primary database
- Supabase Auth (GoTrue) for authentication
- JWT-based session management
- FastAPI JWT verification

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Development Environment Initialization (Priority: P1)

As a developer, I can set up the complete Iris development environment with a single command, installing dependencies and validating prerequisites, so I can begin development work immediately.

**Why this priority**: Without a properly configured environment, no development can proceed. This is the foundation that enables all other work.

**Independent Test**: Run `just dev-setup` on a fresh repository clone and verify that all dependencies are installed (Python packages via uv, Node packages, Docker verified), configuration templates are created, and the developer receives clear next-step instructions.

**Acceptance Scenarios**:

1. **Given** a fresh repository clone, **When** developer runs `just dev-setup`, **Then** uv installs all Python dependencies and Node.js packages are installed
2. **Given** the setup command runs, **When** dependencies are installed, **Then** `.env.example` is copied to `.env` with placeholder Supabase credentials and developer is prompted to configure
3. **Given** environment setup, **When** setup validates prerequisites, **Then** Python version (3.12/3.13), Docker availability, and Node.js version are verified with clear error messages for missing items
4. **Given** setup completion, **When** all validations pass, **Then** developer receives summary showing what was configured and instructions for next steps (configure Supabase credentials, run `just dev`)
5. **Given** partial setup failure, **When** a prerequisite check fails, **Then** setup stops gracefully with actionable error message explaining what's missing and how to install it

---

### User Story 2 - Supabase Database Schema (Priority: P1)

As a developer, I can initialize the Supabase database schema with the five core MVP tables (projects, tasks, ideas, reminders, notes), enabling me to develop and test API routes with real data persistence.

**Why this priority**: The database schema is the foundation for all data operations. Without tables in Supabase, API development cannot proceed. This must work before authentication can be tested with real users.

**Independent Test**: Run `just db-init` command, verify that all five tables are created in cloud Supabase with proper columns, indexes, foreign keys, and Row Level Security (RLS) policies. Insert test data via Supabase Studio to verify schema correctness.

**Acceptance Scenarios**:

1. **Given** Supabase credentials in `.env`, **When** developer runs `just db-init`, **Then** connection to cloud Supabase is established and five core tables are created (projects, tasks, ideas, reminders, notes)
2. **Given** tables are created, **When** developer views schema in Supabase Studio, **Then** all columns match specification (proper types, nullable/required, timestamps, UUIDs for IDs)
3. **Given** tables exist, **When** developer inserts a project record, **Then** foreign key relationships are enforced for linked tasks, notes, and reminders
4. **Given** the schema, **When** developer runs `just db-reset`, **Then** all tables are dropped and recreated with clean schema (development only, requires confirmation)
5. **Given** RLS policies, **When** developer attempts data access, **Then** Row Level Security policies are created (initially permissive for development, to be tightened with auth)
6. **Given** schema initialization, **When** tables already exist, **Then** command detects existing schema and offers to skip or reset

---

### User Story 3 - Supabase Authentication Integration (Priority: P2)

As a developer, I can integrate Supabase Auth (GoTrue) with Google OAuth2 for user authentication, enabling the application to manage user sessions with JWT tokens without storing any credentials locally.

**Why this priority**: Authentication is required for the cloud-first model. Google OAuth2 provides secure, passwordless authentication managed entirely by Supabase. This enables user-specific data access and sets the foundation for Row Level Security. Comes after database schema so we can test with real user accounts.

**Independent Test**: Initiate Google OAuth2 flow via Supabase Auth, complete Google sign-in, receive JWT token from Supabase, use token to access protected FastAPI endpoint, verify JWT validation works correctly and user identity (Google email, user_id) is extracted.

**Acceptance Scenarios**:

1. **Given** Supabase Auth is configured with Google OAuth2 provider, **When** developer initiates Google sign-in flow, **Then** Supabase redirects to Google OAuth consent screen with correct client_id and scopes
2. **Given** Google OAuth consent is granted, **When** Google redirects back to Supabase callback URL, **Then** Supabase creates or updates user account and returns access token (JWT) and refresh token
3. **Given** an OAuth error (user denies consent, invalid state), **When** callback is received, **Then** authentication fails with clear error message and no token is issued
4. **Given** a valid JWT token from Google OAuth flow, **When** developer decodes token, **Then** token contains user ID (Supabase UUID), email (from Google), provider ("google"), and role claims with Supabase signature
5. **Given** token expiration, **When** access token expires, **Then** refresh token can be used to obtain new access token without re-authenticating with Google
6. **Given** Supabase Auth UI, **When** developer accesses Supabase Studio, **Then** authenticated users appear in Auth dashboard with provider metadata (Google profile info, OAuth subject ID)

---

### User Story 4 - FastAPI Backend with JWT Verification (Priority: P2)

As a developer, I can run the FastAPI backend server that verifies Supabase JWT tokens on protected routes, ensuring only authenticated users can access data.

**Why this priority**: The API layer connects authentication (User Story 3) with database operations (User Story 2). This enables secure, user-specific data access and validates the full stack integration.

**Independent Test**: Start FastAPI server with `just dev`, call health endpoint (unprotected) successfully, call protected endpoint without token (receives 401), call protected endpoint with valid JWT (receives 200 and data), verify JWT validation uses Supabase public key.

**Acceptance Scenarios**:

1. **Given** FastAPI server is started, **When** developer accesses http://localhost:8000/health, **Then** unprotected health endpoint responds with 200 status and service information
2. **Given** a protected API endpoint, **When** developer calls endpoint without Authorization header, **Then** FastAPI returns 401 Unauthorized with clear error message
3. **Given** a valid Supabase JWT, **When** developer calls protected endpoint with `Bearer {token}` in Authorization header, **Then** FastAPI validates JWT signature using Supabase public key and returns 200 with data
4. **Given** an invalid or expired JWT, **When** developer attempts to access protected endpoint, **Then** FastAPI returns 401 with specific error (invalid signature, expired, malformed)
5. **Given** authenticated request, **When** JWT is validated, **Then** FastAPI extracts user ID from token claims and makes it available to route handlers for data filtering
6. **Given** FastAPI startup, **When** Supabase credentials are missing or invalid, **Then** server logs clear warning but starts successfully (allows health checks to work)
7. **Given** code changes to FastAPI, **When** developer saves file, **Then** server hot-reloads within 3 seconds without manual restart

---

### User Story 5 - Docker Compose Development Stack (Priority: P3)

As a developer, I can run the complete development stack (FastAPI + future frontend) using Docker Compose, providing consistent environment across all development machines.

**Why this priority**: Docker ensures consistency but isn't blocking for backend development (can run FastAPI directly). This enables standardized deployment and easier onboarding but comes after core functionality is proven.

**Independent Test**: Run `just dev` to start Docker Compose, verify FastAPI container starts and is accessible, check logs show successful Supabase connection, verify hot-reload works for mounted volumes.

**Acceptance Scenarios**:

1. **Given** Docker is running, **When** developer runs `just dev`, **Then** Docker Compose starts FastAPI container and service is accessible at http://localhost:8000
2. **Given** containers are running, **When** developer runs `just dev-logs`, **Then** FastAPI logs are displayed in real-time with colored output
3. **Given** the development stack, **When** developer runs `just dev-stop`, **Then** all containers stop gracefully and are removed
4. **Given** FastAPI container, **When** developer modifies Python code, **Then** changes hot-reload automatically via mounted volume without container restart
5. **Given** Docker Compose, **When** environment variables are updated in `.env`, **Then** restart picks up new configuration without rebuilding images
6. **Given** multiple developers, **When** each runs `just dev`, **Then** consistent environment behavior across Windows, macOS, and Linux

---

### Edge Cases

- **Supabase credentials missing**: When developer runs commands requiring Supabase without configured `.env`, display clear error with instructions on where to get credentials (Supabase dashboard → Project Settings → API)
- **Google OAuth not configured**: When Supabase Auth Google provider is not enabled in Supabase dashboard, return clear error directing developer to Authentication → Providers → Google in Supabase Studio
- **OAuth callback URL mismatch**: When Google OAuth redirect URI doesn't match Supabase configuration, authentication fails with clear error about URL mismatch and configuration instructions
- **Supabase connection failure**: When Supabase cloud is unreachable (network issue, wrong URL), log detailed connection error including endpoint attempted and suggest checking credentials and network
- **Port conflicts**: When port 8000 (FastAPI) is already in use, detect conflict and suggest either stopping conflicting service or updating port in `.env`
- **Invalid JWT format**: When API receives malformed Authorization header (missing "Bearer", invalid base64, wrong structure), return 401 with specific format error
- **JWT signature mismatch**: When JWT was signed with different key (wrong Supabase project, tampered token), fail validation and log security warning
- **Expired JWT in development**: When testing with expired token, return clear expiration error and suggest using refresh token flow
- **OAuth state parameter mismatch**: When OAuth callback state doesn't match expected value (CSRF protection), reject authentication with security warning
- **Database schema conflicts**: When `just db-init` finds existing tables with different schema, offer three options: skip, reset (dangerous), or abort
- **Docker not running**: When `just dev` is attempted without Docker, detect and provide instructions to start Docker Desktop with `docker ps` verification
- **Python version mismatch**: When Python < 3.12 or > 3.13, fail setup with clear message about required versions and link to installation
- **Supabase RLS blocking development**: When Row Level Security policies are too restrictive, provide debug mode to temporarily disable RLS for testing (document security implications)

## Requirements *(mandatory)*

### Functional Requirements

**Environment Setup**:
- **FR-001**: System MUST provide `just dev-setup` command that installs Python dependencies via uv, Node.js dependencies via npm, and validates prerequisites
- **FR-002**: Setup MUST verify Python 3.12/3.13, Docker availability, and Node.js 20.x, failing with actionable errors if missing
- **FR-003**: Setup MUST create `.env` from `.env.example` with placeholder Supabase credentials and instructions for configuration
- **FR-004**: Setup MUST validate `.env` configuration format (required fields present, URL format correct) before allowing `just dev` to run

**Database Schema**:
- **FR-005**: System MUST create `projects` table with columns: id (UUID primary key), user_id (UUID foreign key to auth.users), name (text required), description (text nullable), status (enum: active/archived/completed), created_at (timestamptz), updated_at (timestamptz)
- **FR-006**: System MUST create `tasks` table with columns: id (UUID), user_id (UUID), project_id (UUID foreign key to projects), title (text required), priority (enum: high/medium/low), due_date (timestamptz nullable), completed (boolean default false), notes (text nullable), created_at (timestamptz), updated_at (timestamptz)
- **FR-007**: System MUST create `ideas` table with columns: id (UUID), user_id (UUID), title (text required), description (text nullable), promoted_to_project_id (UUID nullable foreign key to projects), created_at (timestamptz)
- **FR-008**: System MUST create `reminders` table with columns: id (UUID), user_id (UUID), task_id (UUID nullable foreign key to tasks), message (text required), due_time (timestamptz required), created_at (timestamptz)
- **FR-009**: System MUST create `notes` table with columns: id (UUID), user_id (UUID), project_id (UUID foreign key to projects), content (text required), created_at (timestamptz), updated_at (timestamptz)
- **FR-010**: All tables MUST include user_id column with foreign key to auth.users to enable Row Level Security
- **FR-011**: Database schema MUST enforce referential integrity with foreign keys and ON DELETE CASCADE where appropriate
- **FR-012**: System MUST create indexes on foreign keys (project_id, task_id, user_id) and created_at columns for query performance
- **FR-013**: System MUST create Row Level Security (RLS) policies on all tables: initially permissive for development, user-scoped for production

**Authentication**:
- **FR-014**: System MUST support user authentication via Supabase Auth using Google OAuth2 as the primary provider (no local password storage)
- **FR-015**: System MUST initiate Google OAuth2 flow via Supabase Auth, returning access token (JWT) and refresh token upon successful authentication
- **FR-016**: Access tokens MUST expire after 1 hour, refresh tokens after 7 days (Supabase default configuration managed by Supabase)
- **FR-017**: System MUST support token refresh flow using refresh token to obtain new access token without re-authenticating with Google
- **FR-018**: JWT tokens MUST contain claims: sub (user ID), email (from Google), provider ("google"), role, iat (issued at), exp (expiration)
- **FR-019**: System MUST validate JWT signature using Supabase project's public key (JWT_SECRET from Supabase settings), with no local credential validation

**FastAPI Backend**:
- **FR-020**: FastAPI MUST provide unprotected `/health` endpoint returning service status and Supabase connection health
- **FR-021**: FastAPI MUST provide JWT verification middleware that extracts and validates Authorization Bearer tokens
- **FR-022**: JWT middleware MUST return 401 Unauthorized for missing, invalid, expired, or tampered tokens with specific error messages
- **FR-023**: JWT middleware MUST extract user_id from validated token and make available to route handlers via dependency injection
- **FR-024**: FastAPI MUST provide protected endpoints for CRUD operations on projects, tasks, ideas, reminders, and notes (implementation details in future sprints)
- **FR-025**: All protected endpoints MUST filter data by authenticated user_id to enforce user data isolation
- **FR-026**: FastAPI MUST use python-jose for JWT validation and supabase-py for Supabase client interactions
- **FR-027**: FastAPI MUST load configuration from environment variables using Pydantic Settings (compliant with Constitution Principle 2)
- **FR-028**: FastAPI MUST use rich library for colored logging output (compliant with Constitution Principle 4)
- **FR-029**: FastAPI MUST support hot-reload in development mode for rapid iteration

**Development Tools**:
- **FR-030**: System MUST provide `just dev` command that starts FastAPI server (via Docker or direct uvicorn) with hot-reload enabled
- **FR-031**: System MUST provide `just dev-stop` command that gracefully stops all running services
- **FR-032**: System MUST provide `just dev-logs` command that displays service logs with colored output
- **FR-033**: System MUST provide `just db-init` command that creates Supabase schema from migration files
- **FR-034**: System MUST provide `just db-reset` command that drops and recreates schema with confirmation prompt (development only)
- **FR-035**: Docker Compose MUST mount source code as volumes to enable hot-reload without rebuilding images
- **FR-036**: Docker Compose MUST use `.env` file for configuration with clear variable names and documentation

**OAuth2 Security**:
- **FR-037**: System MUST validate OAuth2 callback URLs match Supabase project configuration to prevent authorization code interception attacks
- **FR-038**: OAuth2 flow MUST use state parameter for CSRF protection, validating state on callback to prevent cross-site request forgery
- **FR-039**: System MUST handle OAuth2 error responses (user denies consent, invalid state, invalid redirect_uri) with clear user-facing error messages
- **FR-040**: System MUST document Google OAuth2 provider configuration requirement in dependencies and setup documentation

**JWT Security Enhancements**:
- **FR-041**: JWT validation MUST verify signature using Supabase JWT_SECRET and reject JWTs with tampered signatures with security warning logged
- **FR-042**: JWT validation MUST restrict algorithms to HS256 only, rejecting tokens with other algorithms (prevents algorithm confusion attacks)
- **FR-043**: JWT validation MUST verify required claims: audience ("authenticated"), issuer (Supabase project URL), provider ("google"), sub (user_id), exp (expiration)
- **FR-044**: JWT validation MUST reject tokens with future iat (issued-at) timestamps to prevent clock skew attacks
- **FR-045**: JWT validation MUST check provider claim equals "google" to prevent tokens from other OAuth providers being accepted
- **FR-046**: System MUST log security events when invalid JWTs are detected (tampered signature, wrong algorithm, invalid claims, expired tokens) with rich library formatted output

**Row Level Security (RLS) Policies**:
- **FR-047**: System MUST create RLS policies on ALL five tables (projects, tasks, ideas, reminders, notes) with four policy types per table: SELECT, INSERT, UPDATE, DELETE
- **FR-048**: RLS policies MUST use auth.uid() = user_id pattern for all operations to prevent cross-user data access
- **FR-049**: RLS policies MUST enforce user_id matching on INSERT operations via WITH CHECK clause to prevent user_id manipulation in API requests
- **FR-050**: System MUST document RLS transition plan: development mode uses permissive policies (controlled via environment variable), production mode uses strict user-scoped policies
- **FR-051**: System MUST provide mechanism to temporarily disable RLS for development debugging (via service_role key) with clear security implications documented

**Credential Security**:
- **FR-052**: System MUST store SUPABASE_JWT_SECRET in .env file with 0600 file permissions (read/write for owner only) on Unix systems
- **FR-053**: .env file MUST be included in .gitignore to prevent credential exposure in version control
- **FR-054**: .env.example MUST contain placeholder values (not actual secrets) with clear instructions for obtaining credentials
- **FR-055**: System MUST validate Supabase credentials format before startup (.env fields present, URL format correct, keys are base64-encoded JWTs)
- **FR-056**: System MUST use SUPABASE_ANON_KEY for client operations (RLS enforced) and document that SUPABASE_SERVICE_KEY bypasses RLS (admin use only)
- **FR-057**: System MUST sanitize log output to prevent credential exposure (redact JWT_SECRET, service keys, tokens from logs and error messages)

**Security Event Logging**:
- **FR-058**: System MUST log security events for: failed OAuth attempts, invalid JWTs (tampered, expired, wrong algorithm), RLS policy violations, credential validation failures
- **FR-059**: Security event logs MUST include: timestamp, event type, user identifier (if available), error details, request metadata (IP, user-agent from headers)
- **FR-060**: Error responses for authentication failures MUST avoid information leakage (don't reveal if email exists, use generic "authentication failed" messages)
- **FR-061**: 401 error responses MUST include minimal information: error type (invalid_token, expired_token, missing_token) without exposing internal details or stack traces

**Authorization & Data Isolation**:
- **FR-062**: System MUST clearly separate authentication (verifying who the user is) from authorization (verifying what user can access) in implementation
- **FR-063**: System MUST document that RBAC (role-based access control) is deferred to later sprint, current model uses user_id-based isolation only
- **FR-064**: Protected endpoints MUST extract user_id from validated JWT and use ONLY this value for data filtering (never accept user_id from request body or query params)
- **FR-065**: System MUST return 404 Not Found (not 403 Forbidden) when RLS filters out resources to avoid revealing resource existence to unauthorized users

**Session Management & Additional Security**:
- **FR-066**: System MUST support session invalidation on logout by relying on Supabase Auth sign-out functionality (client-side token deletion, server validates exp claim)
- **FR-067**: System MUST document that JWT token revocation is handled by token expiration (1 hour for access tokens), with compromised tokens requiring Supabase project JWT secret rotation
- **FR-068**: System MUST handle concurrent user sessions (multiple browser tabs, devices) by treating each session independently via JWT tokens, with no server-side session limit
- **FR-069**: System MUST validate .env file format on startup, rejecting malformed or malicious values with clear error messages and refusing to start
- **FR-070**: Docker volume mounts MUST be configured as read-only for sensitive configuration (/.env mounted as :ro) with source code as read-write for hot-reload
- **FR-071**: System MUST document that JWT replay attack protection is handled by short token expiration (1 hour) and HTTPS-only communication (enforced by Supabase)

### Key Entities

**User** (managed by Supabase Auth):
- Represents an authenticated user with email, password (hashed), email_confirmed status, and metadata
- Managed entirely by Supabase Auth (GoTrue), referenced by UUID in application tables

**Project**:
- Represents a user's project with name, description, status (active/archived/completed), and timestamps
- Belongs to one user (user_id foreign key)
- Has many tasks, notes, and reminders

**Task**:
- Represents a work item with title, priority (high/medium/low), optional due date, completion status, and notes
- Belongs to one user and one project
- May have reminders linked to it

**Idea**:
- Represents a captured idea with title and description
- Belongs to one user
- May be promoted to a project (promoted_to_project_id)

**Reminder**:
- Represents a time-based notification with message and due time
- Belongs to one user
- Optionally links to a task

**Note**:
- Represents free-form text content attached to a project
- Belongs to one user and one project
- Includes timestamps for creation and updates

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Developer can complete `just dev-setup` from fresh clone in under 2 minutes (excluding package downloads)
- **SC-002**: Database initialization (`just db-init`) creates all five tables in under 10 seconds with zero errors
- **SC-003**: Google OAuth2 authentication flow completes in under 3 seconds (excluding Google consent screen interaction) and returns valid JWT token
- **SC-004**: JWT validation on protected endpoints completes in under 50ms per request (measured at p95)
- **SC-005**: FastAPI server achieves "ready" state within 5 seconds of startup
- **SC-006**: Code changes reflect in running FastAPI server within 3 seconds (hot-reload verification)
- **SC-007**: Health endpoint responds in under 100ms including Supabase connection check
- **SC-008**: Zero authentication bypasses possible (all protected endpoints require valid JWT from Supabase)
- **SC-009**: Docker Compose startup completes and services are healthy within 30 seconds
- **SC-010**: Developer can complete full auth test flow (Google OAuth sign-in, receive token, access protected endpoint) in under 45 seconds

## Assumptions

- Supabase cloud service provides 99.9% uptime for development purposes (free tier acceptable)
- Developers have internet connectivity during development (cloud-first model requirement)
- Developers can create Supabase project and obtain credentials (free tier, no credit card required)
- Developers can configure Google OAuth2 provider in Supabase dashboard (requires Google Cloud Console OAuth client setup)
- Google OAuth2 callback URLs can be configured to point to Supabase hosted auth endpoints
- Row Level Security policies initially permissive for development, will be tightened in production
- Single-user development (multi-tenant RLS policies refined in later sprint)
- JWT secret rotation not required for Sprint 0 (Supabase handles key management automatically)
- Supabase manages all authentication flows (no local credential storage or validation)
- Supabase handles rate limiting, session management, and token rotation per their default policies
- Additional OAuth providers (GitHub, Microsoft) deferred to later sprint
- Frontend Supabase integration deferred to Sprint 2 (backend API provides auth layer for now)

## Dependencies

- Supabase cloud account and project (free tier)
- Google Cloud Console project with OAuth2 client configured (free tier)
- Google OAuth2 provider enabled in Supabase Authentication settings
- Docker Compose 2.x for container orchestration
- FastAPI with dependencies: python-jose[cryptography], supabase-py, python-multipart
- Pydantic Settings for configuration management
- Rich library for colored logging (Constitution compliance)
- Existing justfile and CI infrastructure (Spec 001)
- Environment variables: SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_JWT_SECRET
- Constitution Principle 2 (Explicit Over Implicit) for config management
- Constitution Principle 4 (Error Handling with rich library)

## Out of Scope

- Local SQLite database (deferred indefinitely, may revisit for offline mode)
- Sync engine between local and cloud (no longer applicable)
- Offline functionality (deferred to Phase 2 or later)
- `iris` CLI tools (polish for later sprint)
- Frontend implementation (Sprint 2)
- Email/password authentication (using Google OAuth2 only)
- Local credential storage or validation (all auth handled by Supabase)
- Additional OAuth providers beyond Google (GitHub, Microsoft, Apple deferred to later sprint)
- Password reset flows (not applicable with OAuth2)
- Email verification flows (handled by Google account verification)
- Multi-factor authentication (MFA) - relies on Google account MFA settings
- Custom rate limiting (Supabase default rate limiting applied)
- Custom token rotation (Supabase handles automatically)
- User profile management UI
- Admin user management
- API rate limiting beyond Supabase defaults
- API documentation beyond Swagger/OpenAPI auto-generation
- Production deployment configuration (Docker, Kubernetes, etc.)
- Performance optimization and caching strategies
- Database backups and disaster recovery
- Monitoring and observability tooling
- Load testing and scalability validation

## Future Considerations

**Constitution Update Required**: 
- Principle 1: "Local-First Forever" → "Cloud-First, Offline Later"
- Document rationale: Faster MVP delivery, reduced complexity, deferred offline mode

**Architecture Update Required**:
- Remove SQLite references
- Update data flow diagrams to show cloud-only path
- Document authentication flow (Supabase Auth → JWT → FastAPI verification)

**Sprint 1 Implications**:
- CRUD operations now work directly with Supabase (no local database layer)
- API routes use authenticated user_id for data filtering
- Row Level Security policies will be tightened for production
