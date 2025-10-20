# 🗺️ Iris Development Roadmap

## 1. Purpose

This roadmap outlines the phased development plan for **Project Iris**, starting with the Phase 1 MVP (structured interface) and progressing toward intelligent, autonomous functionality. Each phase adds capabilities while maintaining stability and usability.

---

## 2. Guiding Principles

* **User-first:** Prioritize clear value for Jeff as the primary user before generalization.
* **Local-first:** Maintain offline functionality with seamless cloud synchronization.
* **Incremental intelligence:** Introduce AI and agents only after stable manual workflows.
* **Dogfooding:** Use Iris to manage Iris’s own development cycle.
* **Transparency:** Track every phase with living documentation (PRD, Architecture, Sprints, OKRs).

---

## 3. Phase Overview

| Phase | Title                      | Focus                                                                       | Outcome                                             |
| ----- | -------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------- |
| **0** | Vision & Architecture      | Define vision, architecture, and documentation artifacts.                   | Clear product scope and technical foundation.       |
| **1** | MVP — Structured Interface | Build UI and backend for managing projects, tasks, ideas, and reminders.    | Functional local-first project manager.             |
| **2** | Agent Integration          | Add LangGraph-based supervisor and simple agents (Task, Reminder, Summary). | Iris begins to assist and automate.                 |
| **3** | Conversational Iris        | Introduce chat interface powered by agent reasoning.                        | Natural interaction through text and voice.         |
| **4** | Cross-Integration Layer    | Connect with external tools (calendar, GitHub, Drive).                      | Iris operates across Jeff’s full digital ecosystem. |
| **5** | Autonomous Iris            | Proactive suggestions, scheduling, and self-improvement.                    | Self-managing, adaptive assistant.                  |

---

## 4. Phase 0 — Vision & Architecture ✅ (In Progress)

**Timeline:** October 2025
**Objective:** Establish Iris’s purpose, architecture, and development artifacts.

**Deliverables:**

* ✅ `PRD.md` — Problem, goals, and success metrics.
* ✅ `ARCHITECTURE.md` — Full system layout and data model.
* ✅ `ROADMAP.md` — This document.
* 🧱 Repo scaffolding with folders for backend, frontend, and configs.

**Success Criteria:**

* Approved architecture and scope.
* Clear definition of what MVP delivers.

---

## 5. Phase 1 — MVP: Structured Interface

**Timeline:** November–December 2025
**Objective:** Deliver a usable, local-first interface for managing projects, tasks, ideas, notes, and reminders.

**Key Features:**

* Project and task CRUD operations.
* Good Idea Fairy (idea inbox → convert to project).
* Dashboard overview with filters and due dates.
* Daily briefing and notification system.
* Supabase sync + local SQLite persistence.
* Use Iris to track her own development (meta-project).

**Deliverables:**

* MVP UI (Tauri + React + Tailwind).
* FastAPI backend + SQLite schema.
* Supabase cloud sync.
* `SPRINTS.md` file with weekly breakdowns.

**Success Criteria:**

* All tasks/projects managed inside Iris for ≥2 weeks.
* Zero data loss across offline/online transitions.
* Internal dogfooding complete.

---

## 6. Phase 2 — Agent Integration

**Timeline:** Q1 2026
**Objective:** Introduce LangGraph supervisor and simple agents to automate repetitive tasks.

**Key Features:**

* LangGraph-based Task, Reminder, and Summary agents.
* MCP tool registry (get_tasks, add_task, summarize_notes).
* Agent can generate daily reports or summaries.
* `MCP_TOOLS.md` created and maintained.

**Deliverables:**

* MCP server and registry YAML.
* Updated `ARCHITECTURE.md` and `PRD.md`.
* Basic agent evaluation tests.

**Success Criteria:**

* Iris autonomously generates daily summaries.
* Agents execute CRUD operations via MCP tools.
* Iris can manage her own sprint updates.

---

## 7. Phase 3 — Conversational Iris

**Timeline:** Mid 2026
**Objective:** Add chat interface to interact with Iris through natural language.

**Key Features:**

* Text chat UI.
* LangGraph conversation orchestration.
* Optional voice input/output (Whisper + Coqui).
* Chat actions mapped to existing MCP tools.

**Success Criteria:**

* Natural chat flow controlling all Iris functions.
* Voice optional but supported.
* Stable real-time event handling between UI ↔ backend.

---

## 8. Phase 4 — Cross-Integration Layer

**Timeline:** Late 2026
**Objective:** Integrate Iris with external ecosystems.

**Key Integrations:**

* Google Calendar (events & reminders).
* GitHub (project + issue sync).
* Drive/Docs (research materials).

**Deliverables:**

* OAuth layer + integration UI.
* Updated OKRs for cross-project management.

**Success Criteria:**

* Iris syncs and displays data from multiple services.
* Cross-tool context awareness operational.

---

## 9. Phase 5 — Autonomous Iris

**Timeline:** 2027 and beyond
**Objective:** Evolve Iris into a proactive partner that predicts needs, schedules tasks, and manages routines autonomously.

**Key Features:**

* Predictive task generation and scheduling.
* Contextual insights (“You’re overloaded this week — suggest re-prioritization?”).
* Adaptive voice and behavior tuning.

**Success Criteria:**

* Iris manages herself and other projects without manual prompting.
* Continuous learning feedback loop from user behavior.

---

## 10. Dependencies & Risks

| Dependency               | Mitigation                                            |
| ------------------------ | ----------------------------------------------------- |
| Supabase stability       | Local-first ensures no data loss.                     |
| Tauri build environments | Use GitHub Actions matrix builds for platform parity. |
| LangGraph maturity       | Keep agent APIs modular for easy version upgrades.    |
| Jeff’s time allocation   | Use Iris itself to track and balance workload.        |

---

## 11. Milestone Summary

| Phase | Title                     | Target Date | Key Output                 |
| ----- | ------------------------- | ----------- | -------------------------- |
| 0     | Vision & Architecture     | Oct 2025    | PRD, Architecture, Roadmap |
| 1     | MVP: Structured Interface | Dec 2025    | Working desktop app        |
| 2     | Agent Integration         | Q1 2026     | LangGraph + MCP tools      |
| 3     | Conversational Iris       | Mid 2026    | Chat + voice interface     |
| 4     | Cross-Integration         | Late 2026   | External connections       |
| 5     | Autonomous Iris           | 2027+       | Full adaptive assistant    |

---

## 12. Review Cycle

* **Review Frequency:** Monthly internal reviews.
* **Artifact Updates:** PRD, Architecture, and Roadmap updated at each phase.
* **Source of Truth:** Iris project repo (docs/ folder) with version-controlled artifacts.

---

## 13. Summary

This roadmap provides a controlled path from a structured, reliable project manager to a self-improving digital assistant. Each phase builds upon the prior one, ensuring Iris evolves gracefully without breaking core usability.
