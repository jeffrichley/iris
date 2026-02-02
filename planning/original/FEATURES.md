# 🌸 Iris Feature Backlog

## 1. Purpose

This document defines the **feature iteration list** for the Iris project. Each feature represents one full Spec‑Kit cycle (`/speckit.specify → /clarify → /checklist → /plan → /tasks → /analyze → /implement`).

Each item is intentionally small, atomic, and testable — allowing incremental progress without over‑planning.

---

## 2. Legend

| Symbol | Meaning                                            |
| :----: | :------------------------------------------------- |
|   🟥   | Phase 1A — Foundation (core CRUD and auth)         |
|   🟧   | Phase 1B — Productivity layer (daily‑use features) |
|   🟨   | Phase 1C — Polish & integration                    |
|   🟩   | Phase 2+ — Agent & autonomy extensions             |
|   ☐    | Not started                                        |
|   🚧   | In progress                                        |
|   ✅   | Complete                                           |

---

## 3. Feature Iteration Table

| #   | Feature                            | Description                                                          | Priority | Dependencies | Status |
| --- | ---------------------------------- | -------------------------------------------------------------------- | -------- | ------------ | ------ |
| 1   | **Add basic user login**           | Implement email + password authentication and session handling.      | 🟥       | None         | ☐      |
| 2   | **Create project entity**          | Define project model, CRUD API, and UI for project management.       | 🟥       | 1            | ☐      |
| 3   | **Add task management**            | Create task model and UI under each project (priority, due date).    | 🟥       | 2            | ☐      |
| 4   | **Idea inbox (Good Idea Fairy)**   | Capture spontaneous ideas and promote them to projects.              | 🟧       | 2            | ☐      |
| 5   | **Dashboard overview**             | Display unified view of projects, tasks, and deadlines.              | 🟧       | 2 – 3        | ☐      |
| 6   | **Daily briefing & reminders**     | Generate daily digest + notifications for upcoming tasks.            | 🟧       | 3 – 5        | ☐      |
| 7   | **Notes & attachments**            | Add notes per project/task and upload relevant files.                | 🟨       | 2            | ☐      |
| 8   | **Sync engine (Supabase)**         | Two‑way data sync and conflict resolution between SQLite ↔ Supabase. | 🟨       | 1 – 7        | ☐      |
| 9   | **Self‑dogfooding (Project Iris)** | Use Iris to manage its own development within the app.               | 🟨       | 1 – 8        | ☐      |
| 10  | **Agent integration prep**         | Add MCP hooks and LangGraph supervisor for automation.               | 🟩       | 1 – 9        | ☐      |

---

## 4. Phase Breakdown

### 🟥 Phase 1A — Foundations

1️⃣ Add basic user login
2️⃣ Create project entity
3️⃣ Add task management
**Goal:** Establish local‑first CRUD core and authentication.

### 🟧 Phase 1B — Productivity Layer

4️⃣ Idea inbox
5️⃣ Dashboard overview
6️⃣ Daily briefing & reminders
**Goal:** Make Iris useful day‑to‑day for managing research and work.

### 🟨 Phase 1C — Polish & Integration

7️⃣ Notes & attachments
8️⃣ Sync engine (Supabase)
9️⃣ Self‑dogfooding
**Goal:** Improve usability and validate stability through internal use.

### 🟩 Phase 2+ — Agent & Autonomy

🔟 Agent integration prep (LangGraph + MCP tools)
**Goal:** Extend Iris from structured manager → intelligent assistant.

---

## 5. Iteration Flow Example

For each feature, run:

```bash
/speckit.specify "<feature name>"
/speckit.clarify
/speckit.checklist
/speckit.plan
/speckit.tasks
/speckit.analyze
/speckit.implement   # Begin with User Story 1 only
```

Each feature lives under `specs/<###-feature-name>/` with its own artifacts.

---

## 6. Progress Tracking

- Use this table as the **single source of truth** for feature state.
- Update Status column manually (☐ → 🚧 → ✅).
- Optional: link each completed feature to its merged PR or release tag.

---

## 7. Notes

- Features are atomic but composable — any can be reprioritized without breaking dependencies.
- Optional UX improvements (themes, animations, keyboard shortcuts) will be logged separately under the _Enhancements_ label once Phase 1C stabilizes.

---

**Maintained by:** Jeff Richley & Iris
**Last Updated:** October 2025
