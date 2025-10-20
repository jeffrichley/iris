# 🌸 Iris — Personal Project Management Assistant
### Complete Tech Stack (2025 Architecture, with MCP Integration)

---

## 🧱 1. Core System Architecture

| Layer | Technology | Purpose |
|--------|-------------|----------|
| **Frontend App** | **Tauri** (Rust + React + TypeScript) | Cross-platform desktop and mobile app shell with OS integration, notifications, and tray support. |
| **Backend Engine** | **FastAPI (Python)** | Local sidecar service handling REST + WebSocket endpoints, LangChain reasoning, sync, and voice pipeline. |
| **Database (Local)** | **SQLite** | Primary data store for offline tasks, reminders, and ideas. Shared between FastAPI and Tauri. |
| **Database (Cloud)** | **Supabase (PostgreSQL + pgvector)** | Cloud sync, auth, and long-term semantic memory. |
| **Sync Layer** | Custom timestamp-based differential sync | Manages bidirectional synchronization between SQLite and Supabase. |
| **Voice Subsystem** | **faster-whisper (ASR)** + **Coqui-TTS (TTS)** | Local speech-to-text and natural voice synthesis for full offline functionality. |
| **Reasoning Engine** | **LangChain** | AI reasoning, planning, and action execution using modular tool/agent structure. |
| **Vector Store** | **Supabase pgvector → optional local FAISS cache** | Semantic search and long-term memory persistence. |
| **MCP Server** | Custom Python-based JSON-RPC/stdio server | Allows agents to interact with Iris subsystems securely. |

---

## 🧠 2. AI Pipeline Flow

**Voice / Text Input → ASR (Whisper) → LangChain Reasoning → DB Actions → Response Generation → TTS Output**

| Stage | Technology | Description |
|--------|-------------|--------------|
| **Input Capture** | WebRTC + WebAudio + Tauri mic APIs | Records voice input or accepts typed text. |
| **ASR (Speech-to-Text)** | faster-whisper | Converts speech to text locally. |
| **Reasoning & Planning** | LangChain agents | Iris Core agent orchestrates sub-agents (Tasks, Reminders, Research). |
| **Action Layer** | LangChain tool calls → FastAPI routes | Executes CRUD or research actions, creates tasks, reminders, etc. |
| **Memory System** | LangChain buffer memory (short-term) + Supabase pgvector (long-term) | Hybrid memory for continuity and semantic recall. |
| **Response Generation** | LangChain output parser + Coqui-TTS | Generates verbal + text responses. |
| **Output Presentation** | Chat interface + voice playback | Returns answers through animated chat UI and voice. |

---

## 🖥️ 3. Frontend Stack (UI / UX Layer)

| Category | Technology | Role |
|-----------|-------------|------|
| **Framework** | React + TypeScript | Primary UI framework inside Tauri webview. |
| **Styling** | Tailwind CSS | Utility-first responsive styling. |
| **UI Components** | shadcn/ui | Clean, professional component kit. |
| **Icons** | Lucide Icons | Lightweight vector icons. |
| **State Management** | Zustand | Simple, fast global state store. |
| **Data Fetching** | TanStack Query | Smart caching and synchronization with backend APIs. |
| **Animation** | Framer Motion | Smooth transitions and voice-response animations. |
| **Realtime Events** | Supabase Realtime + FastAPI WebSocket | Live updates for DB sync + agent streaming. |
| **Notifications** | Tauri native API + in-app system | OS notifications and in-app alerts. |

### Visual Direction
- **Interaction Model:** Hybrid assistant (chat + collapsible dashboard).
- **Theme:** Dark mode first, “Iris Blue” (#6C63FF) accents, minimal gradients, glassy overlays.
- **Typography:** Inter / DM Sans for body, Fira Code for logs.
- **Layout:**
  - Floating Chat Panel with voice indicator + action chips.
  - Collapsible Dashboard tabs: Tasks | Projects | Ideas | Research | Reminders.
  - System tray quick-action menu.
  - Markdown rendering for summaries and notes.

---

## ⚙️ 4. Backend Stack (App & Infrastructure Layer)

| Component | Technology | Role |
|------------|-------------|------|
| **Framework** | FastAPI | REST + WebSocket backend for all agent and UI communication. |
| **Task Queue / Events** | Asyncio background tasks | Lightweight event scheduling and handling. |
| **Database ORM** | SQLModel / SQLAlchemy | Typed ORM for SQLite + Supabase schema alignment. |
| **Sync Engine** | Custom Python module | Timestamp + hash-based diff sync between SQLite and Supabase. |
| **LangChain Integration** | Tool + Agent graph | Modular reasoning system with tool-calling only (no regex). |
| **MCP Server** | Custom JSON-RPC server | Handles agent tool calls via stdio or local socket. |
| **Logging / Telemetry** | Loguru + Sentry | Structured logs + optional error reporting. |
| **Config Management** | .env via python-dotenv | Centralized environment configuration. |

---

## 🧰 5. Developer Experience (DX)

| Tool | Purpose |
|------|----------|
| **uv** | Fast Python dependency manager and task runner. |
| **just** | Cross-platform task runner (replaces Make). |
| **Typer CLI (iris)** | Developer CLI for managing builds, sync, voice tests, MCP tools, etc. |
| **Docker Compose** | Spins up FastAPI + Supabase local containers. |
| **Ruff + Black** | Linting and formatting. |
| **Pytest + Vitest** | Backend and frontend testing. |
| **GitHub Actions** | CI/CD for building Tauri apps and Docker images. |
| **Sentry (optional)** | Error tracking for production. |
| **Pre-commit hooks** | Auto-linting and test enforcement before commits. |

---

## 🧩 6. MCP & Agent Ecosystem

| Component | Location | Purpose |
|------------|-----------|----------|
| **MCP Server** | `/backend/mcp/` | Hosts callable system tools and APIs via JSON-RPC. |
| **Tool Registry** | `/backend/mcp/registry.yaml` | Defines all registered MCP tools and schemas. |
| **Agent Branch / Module** | `/agents/` or separate branch | Houses LangChain agents and LangGraph supervisors. |
| **MCP Tools (Examples)** | get_tasks, add_task, say_text, query_embeddings | Enables agents to interact with Iris subsystems dynamically. |

### Operation Modes
| Mode | Description |
|-------|--------------|
| **App Mode** | Tauri + FastAPI + MCP server embedded. |
| **Headless Mode** | MCP + LangChain only (no GUI) for testing and research. |
| **Research Mode** | Used by `agents` branch for experimental agent logic. |

---

## 🐳 7. Packaging & Distribution

| Layer | Decision | Notes |
|--------|-----------|-------|
| **Primary Distribution** | Tauri bundles (.dmg, .exe, .AppImage) | Cross-platform signed installers. |
| **Auto-update** | Tauri updater + GitHub Releases | Seamless updates for end-users. |
| **Dev Environment** | Docker Compose + local Tauri runner | One-command setup for contributors (`just dev`). |
| **CI/CD** | GitHub Actions | Automated build, test, and release pipelines. |

---

## 🧠 8. Logging, Monitoring & Analytics

| Layer | Tool | Purpose |
|--------|------|----------|
| **App Logging** | Loguru | Structured and colorized logs for local debugging. |
| **Error Reporting** | Sentry | Optional production error tracking. |
| **Event Analytics** | Supabase Functions (optional) | Track agent usage or task creation events. |

---

## 🧭 9. Overall System Flow

```
User (Voice/Text)
   ↓
ASR (faster-whisper)
   ↓
LangChain Agent Graph (Core, Task, Reminder, Summary)
   ↓
FastAPI Actions → SQLite
   ↓
Sync Engine → Supabase
   ↓
Realtime Events → Tauri Frontend (Zustand + TanStack Query)
   ↓
UI Render + Coqui-TTS Voice Output
   ↓
MCP Server ↔ Agents (Tool Calls, Context Access)
```

---

## 🧠 10. Developer Workflow Summary

| Action | Command |
|--------|----------|
| Run local dev stack | `just dev` or `iris dev` |
| Build desktop release | `iris build desktop --release` |
| Sync local ↔ Supabase | `iris sync --push` / `--pull` |
| Voice test | `iris voice test` |
| Run AI command | `iris ai run "summarize today’s tasks"` |
| Register MCP tool | `iris mcp add-tool "summarize_notes"` |
| Reset environment | `iris reset all` |
| Diagnostics | `iris doctor` |

---

## 🌟 Summary
- **Local-first intelligence** with full offline operation.  
- **MCP-integrated agent architecture** for modular AI expansion.  
- **Supabase cloud sync** with vector memory and real-time updates.  
- **Voice-native assistant** blending ASR + TTS for natural interaction.  
- **LangChain reasoning layer** controlling structured tools and memory.  
- **Modern UX stack** (Tauri + React + shadcn/ui + Framer Motion).  
- **World-class developer experience** powered by `uv`, `just`, and Typer CLI.
