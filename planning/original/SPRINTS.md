# 🏃‍♀️ Iris Phase 1 — Sprint Plan

## 1. Purpose

This document defines the **week-by-week sprint plan** for the **Iris Phase 1 MVP**, focusing on the structured interface for project, task, and idea management. Each sprint lasts one week, and milestones align with the Roadmap.

---

## 2. Sprint Cadence

| Parameter                   | Value                                            |
| --------------------------- | ------------------------------------------------ |
| **Sprint Length**           | 1 week                                           |
| **Total Sprints (Phase 1)** | 6 (approximately 6 weeks)                        |
| **Phase Duration**          | November–December 2025                           |
| **Sprint Review**           | End of each week (Friday)                        |
| **Sprint Retrospective**    | Monday morning before next sprint                |
| **Tracking Tool**           | GitHub Projects board (linked to Iris dashboard) |

---

## 3. Sprint Breakdown

### 🟩 **Sprint 0 — Setup & Foundation (Week 1)**

**Goal:** Establish repository, development environment, and infrastructure.

**Tasks:**

- Initialize GitHub repo and create base folders (backend, tui, docs, configs, tests).
- Add `pyproject.toml` and `justfile`.
- Configure Docker Compose for FastAPI + Supabase.
- Set up Supabase instance and test basic sync.
- Implement basic SQLite schema and initial migration.
- Validate `uv` and `Typer` CLI commands.
- Set up Rich and Textual for TUI framework.

**Deliverable:**

- Running local stack: TUI + FastAPI backend + Supabase sync verified.

---

### 🟨 **Sprint 1 — Backend Foundations (Week 2)**

**Goal:** Build API and database layer for projects, tasks, and ideas.

**Tasks:**

- Implement SQLModel schemas: `projects`, `tasks`, `ideas`, `reminders`, `notes`.
- Build CRUD endpoints in FastAPI for each entity.
- Add logging (Loguru) and error handling.
- Integrate unit tests for API routes.
- Add sync engine skeleton (SQLite ↔ Supabase).

**Deliverable:**

- Tested and documented API routes.
- Local persistence confirmed.

---

### 🟧 **Sprint 2 — TUI Foundations (Week 3)**

**Goal:** Establish Rich + Textual TUI framework.

**Tasks:**

- Initialize Rich console interface with colored output and progress bars.
- Implement Textual TUI with navigation tabs (Projects, Tasks, Ideas, Dashboard).
- Connect to backend via direct SQLModel database access.
- Test data flow using Rich tables and panels.
- Implement Iris brand colors and terminal theme.

**Deliverable:**

- Functional TUI with working interface skeleton.

---

### 🟦 **Sprint 3 — Core Features: Projects & Tasks (Week 4)**

**Goal:** Enable project and task management with full CRUD and linking.

**Tasks:**

- Implement Project detail pages with linked Tasks.
- Add new project and task creation forms.
- Enable task completion, prioritization, and due dates.
- Add filtering and sorting on Dashboard.
- Test Supabase sync reliability.

**Deliverable:**

- Fully working project + task manager.
- Data persistence verified offline and online.

---

### 🟪 **Sprint 4 — Ideas, Notes, and Reminders (Week 5)**

**Goal:** Build the Good Idea Fairy inbox and reminder systems.

**Tasks:**

- Implement Ideas inbox (quick add + promote to project).
- Add project-level Notes section.
- Implement daily briefing background job (FastAPI scheduler).
- Integrate terminal notifications and alerts.
- Add reminder management (add/edit/delete reminders).

**Deliverable:**

- Daily briefing notifications active.
- Idea-to-project promotion functional.

---

### 🟥 **Sprint 5 — Polishing & Dogfooding (Week 6)**

**Goal:** Stabilize, test, and begin using Iris to manage herself.

**Tasks:**

- TUI/UX refinements: colors, layouts, and keyboard shortcuts.
- Write onboarding flow (intro page + example project).
- Implement internal meta-project (Project: Iris) for self-management.
- Full end-to-end tests.
- Update PRD, Architecture, and Roadmap docs.

**Deliverable:**

- Iris managing her own tasks and roadmap.
- MVP ready for internal use and validation.

---

## 4. Milestone Summary

| Sprint | Goal               | Key Deliverable                  |
| ------ | ------------------ | -------------------------------- |
| 0      | Setup              | Repo + stack initialized         |
| 1      | Backend foundation | CRUD + sync engine skeleton      |
| 2      | TUI foundation     | Rich + Textual TUI shell         |
| 3      | Core features      | Projects + tasks fully working   |
| 4      | Advanced features  | Ideas, reminders, daily briefing |
| 5      | Polishing          | Internal usage + validation      |

---

## 5. Acceptance Criteria for Phase 1

- All CRUD operations stable and persisted locally + via Supabase.
- Offline-first mode verified.
- Reminders and daily briefings operational.
- TUI meets brand standards (Iris colors, clean terminal aesthetic).
- Iris’s own project managed within the app for ≥2 weeks.

---

## 6. Dependencies

- Supabase and Docker Compose for cloud and local sync.
- FastAPI + SQLModel for backend.
- Rich + Textual for TUI frontend.
- GitHub Actions for CI/CD.

---

## 7. Next Steps After Phase 1

- Begin Phase 2 planning (Agent Integration).
- Define new PRD sections for MCP tools and LangGraph supervisor.
- Conduct usability testing and user feedback analysis.

---

## 8. Summary

The six-sprint plan delivers a structured, testable Iris MVP that’s ready for dogfooding and iterative enhancement. By the end of Phase 1, Iris becomes a self-managed, local-first project assistant prepared for Phase 2 agent expansion.
