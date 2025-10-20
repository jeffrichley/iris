# 🌸 Iris Phase 1 MVP — Product Requirements Document (PRD)

## 1. Overview

**Product:** Iris — Personal Project Management Assistant
**Version:** Phase 1 MVP (Structured Interface)
**Owner:** Jeff Richley
**Date:** October 2025

### Vision

Iris is designed to help you manage your complex ecosystem of projects, research efforts, and ideas without mental overload. The MVP focuses on creating a single, structured workspace to track projects, tasks, ideas, and deadlines — before adding agents, automation, or chat.

---

## 2. Problem Statement

You are juggling multiple simultaneous projects (research, PhD, robotics, AI frameworks, content networks). Traditional tools (Trello, Notion, Todoist) require manual organization and lack cross-project awareness.

Iris should solve:

- Cognitive overload from remembering dozens of tasks and deadlines.
- Lost or scattered ideas from spontaneous inspiration.
- Difficulty balancing priorities and workload across projects.
- Lack of an integrated system that both stores and synthesizes project data.

---

## 3. Goals & Success Metrics

### Goals

- Provide a **single, intuitive interface** for managing all ongoing and future projects.
- Enable structured **creation, tracking, and completion** of tasks.
- Offer a **Good Idea Fairy inbox** for idea capture and conversion to projects.
- Deliver **clear overviews** of progress, deadlines, and priorities.
- Support **daily briefings and reminders** to keep the user on track.

### Success Metrics

| Metric                                  | Target                                             |
| --------------------------------------- | -------------------------------------------------- |
| Tasks and projects managed through Iris | ≥ 80% of all active work by week 4                 |
| Missed deadlines                        | Reduced by 90% compared to baseline                |
| Task creation-to-completion rate        | ≥ 75% within target window                         |
| User satisfaction                       | Qualitative: “I trust Iris to manage my workload.” |

---

## 4. MVP Scope (Phase 1)

### In-Scope Functionality

| Category                       | Features                                                                           |
| ------------------------------ | ---------------------------------------------------------------------------------- |
| **Projects**                   | Create, edit, archive projects. View status, notes, deadlines.                     |
| **Tasks**                      | Add, edit, complete tasks. Associate with projects. Include priority and due date. |
| **Ideas (Good Idea Fairy)**    | Quick capture for ideas. Convert ideas into projects.                              |
| **Dashboard**                  | Unified view of all projects, tasks, and upcoming deadlines.                       |
| **Reminders / Daily Briefing** | Summary of due and upcoming tasks each day.                                        |
| **Notes / Attachments**        | Add notes per project or task, and upload relevant files.                          |
| **Meta Project**               | Use Iris to manage its own development (“Project: Iris”).                          |

### Out of Scope (for Later Phases)

- Conversational chat interface.
- Agentic autonomy or task parsing.
- Calendar and email integrations.
- Analytics and time tracking.
- Voice or multimodal input.

---

## 5. User Stories

1. **Project Management**
   As a user, I can create and organize projects so that each has its own space for tasks, notes, and due dates.
2. **Task Tracking**
   As a user, I can add tasks with priorities and deadlines to ensure I stay on schedule.
3. **Idea Capture**
   As a user, I can quickly record spontaneous ideas and later turn them into projects.
4. **Dashboard Awareness**
   As a user, I can view all active projects, upcoming deadlines, and overdue tasks in one dashboard.
5. **Reminders & Summaries**
   As a user, I can receive a morning briefing summarizing what’s due or important that day.
6. **Self-Dogfooding**
   As a user, I can manage Iris’s own roadmap and tasks inside Iris to ensure the system validates itself.

---

## 6. Non-Functional Requirements

| Category          | Requirement                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| **Performance**   | Dashboard and CRUD operations must execute in < 150 ms average latency.  |
| **Persistence**   | Local-first SQLite data with Supabase sync for cloud backup.             |
| **Reliability**   | No data loss on offline mode or app crash.                               |
| **Usability**     | Clean, minimal UI with dark theme and keyboard shortcuts.                |
| **Extensibility** | Architecture must support agent integration later with minimal refactor. |
| **Portability**   | Runs identically on macOS, Windows, and Linux (Tauri build targets).     |

---

## 7. Future Expansion (Beyond MVP)

| Phase       | Focus                                                             |
| ----------- | ----------------------------------------------------------------- |
| **Phase 2** | Introduce lightweight LangGraph agent layer for basic automation. |
| **Phase 3** | Add conversational chat interface powered by the agent system.    |
| **Phase 4** | Integrate calendar, email, and cross-platform synchronization.    |
| **Phase 5** | Proactive Iris (contextual suggestions, forecasting, and voice).  |

---

## 8. Acceptance Criteria

- All MVP functionality implemented and accessible through the structured UI.
- Projects, tasks, and ideas persist across sessions and sync with Supabase.
- Daily briefing feature operational.
- “Project: Iris” successfully managed through Iris interface.
- All core workflows validated through internal usage.

---

## 9. Dependencies

- Tech Stack as defined in `iris_tech_stack_mcp.md`.
- Supabase instance for sync and auth.
- Tauri build environment.
- FastAPI backend and SQLite schema alignment.

---

## 10. Deliverables

- `ARCHITECTURE.md` — finalized after PRD approval.
- `ROADMAP.md` — milestone plan for Phases 0–2.
- MVP UI and backend implementation.
- Internal validation by using Iris to manage her own development.

---

## 11. Sign-Off

**Prepared by:** Iris (AI Secretary) & Jeff Richley
**Approved by:** ☐ (to be signed after review)
