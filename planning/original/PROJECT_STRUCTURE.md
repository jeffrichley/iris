# 🗂️ Project Structure — Iris

## 1. Purpose

This document defines the directory and file layout for **Project Iris**. The structure is designed for clarity, modularity, and scalability across multiple phases — from the Phase 1 MVP through full agentic autonomy.

The goal is to make the repository easy to navigate for both developers and Iris’s own agent subsystems as they evolve.

---

## 2. Design Principles

| Principle                  | Description                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------- |
| **Separation of concerns** | Frontend, backend, agents, and documentation live in clear boundaries.                      |
| **Extensibility**          | Future phases (agents, integrations, voice) can be added without reorganization.            |
| **Local-first**            | Backend and frontend share a local SQLite store for offline operation.                      |
| **Dogfooding**             | Iris manages her own tasks and documentation inside this structure.                         |
| **Consistency**            | Follows a common structure across all future Iris-related projects (Chrona, Petunia, etc.). |

---

## 3. Root Directory Layout

```
iris/
├── backend/                # FastAPI application and backend services
├── frontend/               # Tauri + React desktop frontend
├── agents/                 # LangGraph agent modules (future phases)
├── configs/                # Environment and build configuration files
├── docs/                   # Product, architecture, and roadmap documentation
├── scripts/                # Development and automation scripts
├── tests/                  # Integration and end-to-end tests
├── justfile                # Task automation commands
├── pyproject.toml          # Python dependencies (backend)
├── package.json            # Node dependencies (frontend)
└── README.md               # Project overview and setup instructions
```

---

## 4. Backend Structure

```
backend/
├── main.py                 # FastAPI entrypoint
├── api/                    # API endpoints (projects, tasks, ideas, reminders)
│   ├── __init__.py
│   ├── projects.py
│   ├── tasks.py
│   ├── ideas.py
│   └── reminders.py
├── models/                 # SQLModel schema definitions
│   ├── project.py
│   ├── task.py
│   ├── idea.py
│   ├── reminder.py
│   └── base.py
├── services/               # Core backend logic
│   ├── sync.py             # Sync engine (SQLite ↔ Supabase)
│   ├── scheduler.py        # Reminders and daily briefing engine
│   ├── notifications.py    # Tauri + OS notification hooks
│   └── logging.py          # Loguru configuration
├── db/                     # Database configuration
│   ├── session.py
│   ├── init_db.py
│   └── migrations/
├── mcp/                    # Future agent interface (Phase 2+)
│   ├── server.py
│   ├── registry.yaml
│   └── tools/
│       ├── get_tasks.py
│       └── summarize_notes.py
└── tests/                  # Pytest-based backend tests
```

---

## 5. Frontend Structure

```
frontend/
├── src/
│   ├── components/          # Reusable React components
│   ├── pages/               # Page-level UI (Dashboard, Projects, Ideas, Tasks)
│   ├── store/               # Zustand global state management
│   ├── hooks/               # Data fetching and helper hooks
│   ├── utils/               # Shared UI utilities
│   ├── styles/              # Tailwind + shadcn/ui configuration
│   ├── assets/              # Icons, images, fonts
│   └── types/               # TypeScript interfaces
├── public/                  # Static assets and index.html
├── tests/                   # Vitest frontend tests
├── tauri.conf.json          # Tauri build configuration
└── vite.config.ts           # Build tool configuration
```

---

## 6. Agents Structure (Planned for Phase 2+)

```
agents/
├── core/                   # Iris Core supervisor agent (LangGraph)
├── task_agent/             # Handles task creation and prioritization
├── reminder_agent/         # Manages reminders and summaries
├── summary_agent/          # Generates daily briefings
└── tests/                  # Unit and simulation tests for agents
```

---

## 7. Configurations

```
configs/
├── supabase/               # Supabase connection details and SQL migrations
├── .env.example            # Template for environment variables
├── tauri.conf.json         # Frontend build and app configuration
└── logging.conf.yaml       # Logging and telemetry setup
```

---

## 8. Documentation

```
docs/
├── PRD.md                  # Product Requirements Document
├── ARCHITECTURE.md         # System architecture and data model
├── ROADMAP.md              # Multi-phase development plan
├── SPRINTS.md              # Weekly sprint plan (Phase 1)
├── OKRS.md                 # Objectives and Key Results (future)
├── MCP_TOOLS.md            # Tool registry for agent layer (future)
└── PROJECT_STRUCTURE.md    # This document
```

---

## 9. Scripts

```
scripts/
├── dev.sh                  # Starts full development stack
├── build.sh                # Builds Tauri app for release
├── sync_db.py              # Manual sync between local and Supabase
└── test_all.sh             # Runs backend + frontend test suites
```

---

## 10. Tests

```
tests/
├── e2e/                    # Full workflow tests across UI + backend
├── backend/                # API and DB integration tests
├── frontend/               # UI tests (Cypress/Vitest)
└── data/                   # Fixtures and test data
```

---

## 11. Developer Utilities

| Tool                   | Command                                               | Description                                            |
| ---------------------- | ----------------------------------------------------- | ------------------------------------------------------ |
| **uv**                 | `uv run`                                              | Python dependency management and virtual environments. |
| **just**               | `just dev`                                            | Starts dev environment.                                |
| **Typer CLI (`iris`)** | `iris sync`, `iris build`, `iris doctor`              | Custom dev CLI for managing tasks and builds.          |
| **Docker Compose**     | `docker compose up`                                   | Launch Supabase + FastAPI locally.                     |
| **GitHub Actions**     | CI/CD for building and testing Iris across platforms. |                                                        |

---

## 12. Growth Plan

This structure is stable through the MVP and ready for:

* Phase 2 agent integrations (LangGraph + MCP).
* Phase 3 chat interface (WebSocket + MCP layer).
* Phase 4+ external integrations and analytics.

Future expansions (like plugins or voice subsystems) will live under `extensions/` or `voice/` directories.

---

## 13. Summary

The Iris repository layout is intentionally **clean, modular, and scalable**. Each part serves a defined role:

* **Backend** → Local-first logic and data.
* **Frontend** → Tauri-based structured UI.
* **Agents** → Reasoning and automation layer (future).
* **Docs** → Living artifacts guiding every phase.

This layout ensures Iris can grow organically without sacrificing clarity or maintainability.
