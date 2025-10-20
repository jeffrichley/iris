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

- Initialize GitHub repo and create base folders (backend, frontend, docs, configs, tests).
- Add `pyproject.toml`, `package.json`, and `justfile`.
- Configure Docker Compose for FastAPI + Supabase.
- Set up Supabase instance and test basic sync.
- Implement basic SQLite schema and initial migration.
- Validate `uv` and `Typer` CLI commands.

**Deliverable:**

- Running local stack: Tauri shell + FastAPI backend + Supabase sync verified.

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

### 🟧 **Sprint 2 — Frontend Foundations (Week 3)**

**Goal:** Establish Tauri + React frontend framework.

**Tasks:**

- Initialize Tauri + React app with Tailwind, shadcn/ui, and Zustand.
- Implement navigation tabs (Projects, Tasks, Ideas, Dashboard).
- Connect to backend via FastAPI endpoints.
- Test data flow using TanStack Query.
- Implement dark mode and Iris brand theme.

**Deliverable:**

- Functional Tauri shell with working UI skeleton.

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
- Integrate Tauri native notifications.
- Add reminder management (add/edit/delete reminders).

**Deliverable:**

- Daily briefing notifications active.
- Idea-to-project promotion functional.

---

### 🟥 **Sprint 5 — Polishing & Dogfooding (Week 6)**

**Goal:** Stabilize, test, and begin using Iris to manage herself.

**Tasks:**

- UI/UX refinements: animations, icons, and shortcuts.
- Write onboarding flow (intro page + example project).
- Implement internal meta-project (Project: Iris) for self-management.
- Full end-to-end tests.
- Update PRD, Architecture, and Roadmap docs.

**Deliverable:**

- Iris managing her own tasks and roadmap.
- MVP ready for internal use and validation.

---

## 4. Milestone Summary

| Sprint | Goal                | Key Deliverable                  |
| ------ | ------------------- | -------------------------------- |
| 0      | Setup               | Repo + stack initialized         |
| 1      | Backend foundation  | CRUD + sync engine skeleton      |
| 2      | Frontend foundation | Tauri + React UI shell           |
| 3      | Core features       | Projects + tasks fully working   |
| 4      | Advanced features   | Ideas, reminders, daily briefing |
| 5      | Polishing           | Internal usage + validation      |

---

## 5. Acceptance Criteria for Phase 1

- All CRUD operations stable and persisted locally + via Supabase.
- Offline-first mode verified.
- Reminders and daily briefings operational.
- UI meets brand standards (Iris theme, minimal aesthetic).
- Iris’s own project managed within the app for ≥2 weeks.

---

## 6. Dependencies

- Supabase and Docker Compose for cloud and local sync.
- FastAPI + SQLModel for backend.
- Tauri + React for frontend.
- GitHub Actions for CI/CD.

---

## 7. Next Steps After Phase 1

- Begin Phase 2 planning (Agent Integration).
- Define new PRD sections for MCP tools and LangGraph supervisor.
- Conduct usability testing and user feedback analysis.

---

## 8. Summary

The six-sprint plan delivers a structured, testable Iris MVP that’s ready for dogfooding and iterative enhancement. By the end of Phase 1, Iris becomes a self-managed, local-first project assistant prepared for Phase 2 agent expansion.
