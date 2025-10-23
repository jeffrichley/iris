# Implementation Plan: Database Setup

**Branch**: `002-database-setup` | **Date**: 2024-12-19 | **Spec**: [Database Setup Specification](./spec.md)
**Input**: Feature specification from `/specs/002-database-setup/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement database infrastructure for Iris project management system including database connections, schema management, data models, and CLI tools. The system will support local SQLite with optional PostgreSQL, featuring connection pooling, migration capabilities, and a development CLI tool with rich logging.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: SQLAlchemy, Alembic, Rich, Typer, Pydantic, python-dotenv
**Storage**: SQLite (primary), PostgreSQL (optional), .env configuration
**Testing**: pytest, SQLAlchemy test fixtures
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: Single project with modular components (core, api, cli, tui)
**Performance Goals**: 5-second connection establishment, 100ms CRUD operations, 5-minute connection pool timeout
**Constraints**: Single-user TUI system, local-first architecture, offline-capable
**Scale/Scope**: 5 database tables, 3 CLI commands, connection pool of 5 connections

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Constitution Compliance Verified** - All principles from `planning/CONSTITUTION.md` are satisfied:

### Core Tenets Compliance:
- ✅ **Local-First Forever**: SQLite primary database, offline-capable architecture
- ✅ **Zero Data Loss**: Durable state changes, transaction management, connection pooling
- ✅ **Privacy by Design**: Local data storage, no telemetry, secure configuration
- ✅ **Performance is Feature**: 5-second connection, 100ms CRUD operations, performance monitoring

### Code Quality Standards Compliance:
- ✅ **Type Safety First**: All Python code will use type hints, Pydantic for validation
- ✅ **Explicit Over Implicit**: Clear function signatures, dependency injection, centralized config
- ✅ **Modular Architecture**: Clear layer separation (UI/API/Data), dependency inversion
- ✅ **Error Handling**: Rich library for colored logging, specific error messages
- ✅ **Documentation Standards**: Public APIs will have docstrings, architecture decisions documented

### Testing Standards Compliance:
- ✅ **Test Pyramid**: pytest with unit (70%), integration (20%), E2E (10%) distribution
- ✅ **Test Quality**: Deterministic, isolated, fast tests with descriptive names
- ✅ **Coverage Requirements**: 85% minimum coverage for core business logic

### Performance Requirements Compliance:
- ✅ **Response Time Targets**: Database operations < 100ms, connection establishment < 5s
- ✅ **Resource Management**: Connection pooling (5 connections), efficient query patterns
- ✅ **Optimization Strategy**: Correctness first, then perceived performance, then actual performance

## Project Structure

### Documentation (this feature)

```
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)

```
src/iris/
├── core/                    # Core database infrastructure
│   ├── database/           # DB connections, models, schema
│   │   ├── __init__.py
│   │   ├── connection.py   # Database connection management
│   │   ├── models.py       # SQLAlchemy models
│   │   └── migrations/     # Alembic migration files
│   ├── config/             # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py     # Environment configuration
│   └── utils/              # Shared utilities
│       ├── __init__.py
│       └── logging.py      # Logging configuration
├── api/                     # FastAPI + FastMCP services
│   ├── routes/             # API endpoints
│   │   ├── __init__.py
│   │   └── database.py     # Database health endpoints
│   ├── middleware/         # API middleware
│   │   ├── __init__.py
│   │   └── database.py     # Database connection middleware
│   └── services/           # Business logic services
│       ├── __init__.py
│       └── database.py     # Database service layer
├── cli/                     # CLI tool (iris-dev)
│   ├── commands/           # Command implementations
│   │   ├── __init__.py
│   │   └── db.py           # Database CLI commands
│   ├── output/             # Rich logging, progress bars
│   │   ├── __init__.py
│   │   └── display.py      # Rich output formatting
│   └── utils/              # CLI-specific utilities
│       ├── __init__.py
│       └── config.py       # CLI configuration
└── tui/                     # Textual TUI interface
    ├── screens/            # TUI screens/views
    │   ├── __init__.py
    │   └── database.py     # Database management screens
    ├── widgets/            # Custom widgets
    │   ├── __init__.py
    │   └── status.py       # Database status widgets
    └── utils/              # TUI-specific utilities
        ├── __init__.py
        └── database.py     # TUI database utilities

tests/
├── unit/                   # Unit tests
│   ├── test_database_connection.py
│   ├── test_models.py
│   └── test_cli_commands.py
├── integration/            # Integration tests
│   ├── test_database_integration.py
│   └── test_cli_integration.py
└── fixtures/              # Test fixtures
    ├── __init__.py
    └── database.py        # Database test fixtures
```

**Structure Decision**: Modular architecture with clear separation between core database infrastructure, API services, CLI tool, and TUI interface. Each component is independently testable and can be developed in parallel.

## Complexity Tracking

*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
