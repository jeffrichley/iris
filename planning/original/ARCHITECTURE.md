# 🧱 Iris System Architecture — Phase 1 MVP

## 1. Purpose

This document defines the architectural layout for the **Iris Phase 1 MVP** — a structured project, task, and idea manager designed to help Jeff organize and prioritize work across multiple domains. The MVP excludes chat and autonomous agents, focusing on a reliable, local-first application with cloud synchronization.

---

## 2. System Overview

The MVP architecture is designed for **local-first operation** with seamless **cloud sync** and clear separation between the **frontend (UI)**, **backend (API)**, and **database** layers.

```
+-------------------------------------------------------------+
|                      Iris (Tauri App)                      |
|  React + TypeScript + Tailwind + Zustand + TanStack Query  |
|-------------------------------------------------------------|
|           FastAPI Backend  (REST + WebSocket API)          |
|    - CRUD for projects, tasks, ideas, notes, reminders     |
|    - Local SQLite database                                 |
|    - Sync engine with Supabase cloud backend               |
|-------------------------------------------------------------|
|          Supabase Cloud Backend (PostgreSQL + pgvector)    |
|    - Remote data sync + backup                             |
|    - Realtime events + authentication                      |
+-------------------------------------------------------------+
```

---

## 3. Core Principles

| Principle               | Description                                                                                               |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| **Local-first**         | All data lives locally first (SQLite). Cloud sync enhances reliability but is not required for daily use. |
| **Offline resilience**  | The system operates without internet; sync occurs when reconnected.                                       |
| **Cross-platform**      | Built with Tauri for macOS, Windows, and Linux.                                                           |
| **Scalable foundation** | Designed for easy introduction of agents, chat, and automation in later phases.                           |
| **Transparency**        | Iris stores data in user-accessible SQLite and Supabase instances.                                        |

---

## 4. Component Breakdown

### 4.1 Frontend (Tauri + React)

| Component                | Description                                                                   |
| ------------------------ | ----------------------------------------------------------------------------- |
| **Tauri Shell**          | Provides desktop wrapper, file access, notifications, and auto-update system. |
| **React UI**             | Main interface with modular tabs: Projects, Tasks, Ideas, Reminders, Notes.   |
| **Zustand Store**        | Manages global application state (active project, filters, view modes).       |
| **TanStack Query**       | Handles async data fetching, mutation, and sync with FastAPI.                 |
| **Tailwind + shadcn/ui** | Provides modern responsive design and polished component library.             |
| **Framer Motion**        | Animations for dashboard transitions and modal pop-ups.                       |
| **Tauri Notifications**  | Native OS notifications for reminders and daily briefings.                    |

### 4.2 Backend (FastAPI)

| Module                   | Description                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| **Core API**             | REST endpoints for CRUD operations on Projects, Tasks, Ideas, Notes, Reminders. |
| **Sync Engine**          | Handles differential sync between SQLite and Supabase.                          |
| **Scheduler**            | Triggers background tasks for reminders and daily summaries.                    |
| **ORM Layer (SQLModel)** | Provides a typed schema for SQLite and Supabase compatibility.                  |
| **Realtime Channel**     | Optional WebSocket feed for live updates between UI and backend.                |
| **Logging**              | Loguru for structured logging and debugging.                                    |

### 4.3 Database Layer

| Layer             | Technology                       | Role                                                                          |
| ----------------- | -------------------------------- | ----------------------------------------------------------------------------- |
| **Local**         | SQLite                           | Primary data store. Holds all user data and metadata.                         |
| **Cloud**         | Supabase (PostgreSQL + pgvector) | Provides cloud sync, realtime events, and optional long-term semantic memory. |
| **Sync Strategy** | Timestamp + hash diff algorithm  | Ensures efficient bidirectional sync.                                         |

---

## 5. Data Model (MVP Schema)

### Entities

| Table         | Key Fields                                                  | Description                                 |
| ------------- | ----------------------------------------------------------- | ------------------------------------------- |
| **projects**  | id, name, description, status, created_at, updated_at       | Represents an individual project.           |
| **tasks**     | id, project_id, title, priority, due_date, completed, notes | Work items belonging to projects.           |
| **ideas**     | id, title, description, promoted_to_project, created_at     | Captures spontaneous ideas.                 |
| **reminders** | id, task_id (optional), message, due_time                   | Triggers notifications and daily summaries. |
| **notes**     | id, project_id, content, created_at                         | Free-form notes tied to projects.           |

### Relationships

- One project → many tasks, notes, and reminders.
- Ideas may be converted to projects.
- Tasks optionally link to reminders.

---

## 6. Sync Flow

```
[Local SQLite] ←→ [FastAPI Sync Module] ←→ [Supabase PostgreSQL]
```

**Flow Description:**

1. User creates or updates local data.
2. FastAPI logs timestamp + hash.
3. Sync module detects new/changed entries.
4. Pushes to Supabase if newer; pulls updates if local copy outdated.
5. Supabase emits realtime event → frontend updates via TanStack Query.

---

## 7. Reminders & Daily Briefing Engine

- Runs as a background task in FastAPI.
- Scans tasks/reminders due in next 24 hours.
- Sends desktop notifications and/or generates a summary view.
- Future phases may connect this to voice or email output.

---

## 8. Developer Experience

| Tool                   | Purpose                                                    |
| ---------------------- | ---------------------------------------------------------- |
| **uv**                 | Python dependency and environment manager.                 |
| **just**               | Task runner (builds, sync, test commands).                 |
| **Typer CLI (`iris`)** | Development CLI for managing builds, DB sync, and testing. |
| **Docker Compose**     | For running FastAPI + Supabase locally.                    |
| **Pytest / Vitest**    | Testing for backend and frontend respectively.             |
| **GitHub Actions**     | CI/CD pipeline for builds and tests.                       |
| **Pre-commit Hooks**   | Enforce code quality with Ruff + Black.                    |

---

## 9. Extensibility & Future Readiness

| Future Feature               | Design Consideration                                                     |
| ---------------------------- | ------------------------------------------------------------------------ |
| **Agents (Phase 2)**         | FastAPI exposes internal API hooks compatible with LangGraph supervisor. |
| **Chat Interface (Phase 3)** | WebSocket + MCP interface already stubbed in backend.                    |
| **Voice I/O (Phase 4)**      | Tauri shell prepared for microphone and audio output permissions.        |
| **Integrations (Phase 5)**   | Supabase tables and FastAPI routes modularized for extension.            |

---

## 10. Security & Privacy

- Local data stored in SQLite within user profile directory.
- Supabase communication secured with SSL.
- Authentication optional for personal use; OAuth planned for public releases.
- Sensitive logs excluded from Sentry reporting.

---

## 11. Deployment

| Environment     | Method                                                           |
| --------------- | ---------------------------------------------------------------- |
| **Development** | `just dev` launches Tauri + FastAPI + Supabase local stack.      |
| **Testing**     | GitHub Actions workflow triggers CI builds and coverage reports. |
| **Production**  | Tauri build → GitHub Releases with auto-update enabled.          |

---

## 12. Summary

The Phase 1 architecture delivers a solid foundation for structured project management while remaining flexible for future intelligent features. It prioritizes **data reliability**, **offline usability**, and **developer efficiency**, ensuring Iris can evolve into a fully autonomous personal assistant in later phases.

Project Layout
