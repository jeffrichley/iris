# FastAPI + FastMCP Integration Guide

**Goal**: Share business logic between REST API and MCP server

---

## 🏗️ **Architecture**

```
┌─────────────────────────────────────────────────────────┐
│                    Client Layer                          │
├──────────────────┬──────────────────────────────────────┤
│  HTTP Clients    │  MCP Clients (Claude, Cursor, etc.)  │
│  (curl, browser) │  (stdio, SSE)                        │
└────────┬─────────┴────────────┬─────────────────────────┘
         │                      │
         │                      │
    ┌────▼──────┐         ┌─────▼──────┐
    │  FastAPI  │         │  FastMCP   │
    │  Routes   │         │   Tools    │
    │ (HTTP/REST)│         │  (MCP)     │
    └────┬──────┘         └─────┬──────┘
         │                      │
         │  ┌────────────────┐  │
         └─→│ Service Layer  │←─┘
            │ (Pure Python)  │
            └───────┬────────┘
                    │
            ┌───────▼────────┐
            │  Data Layer    │
            │  (Supabase)    │
            └────────────────┘
```

**Key Insight**: Both protocols call the SAME service methods!

---

## 📁 **File Structure**

```
src/iris/
├── services/              # ← BUSINESS LOGIC (Framework-Agnostic)
│   ├── __init__.py
│   ├── project_service.py # Pure Python, no FastAPI/MCP imports
│   ├── task_service.py
│   └── ...
│
├── api/                   # ← REST API (FastAPI)
│   ├── main.py            # FastAPI app
│   └── routes/
│       ├── projects.py    # Thin - calls ProjectService
│       └── ...
│
├── mcp/                   # ← MCP SERVER (FastMCP)
│   ├── server.py          # FastMCP app + tools
│   └── tools/             # (optional: organize tools)
│       └── projects.py
│
├── models/                # ← SHARED
├── database/              # ← SHARED
└── auth/                  # ← SHARED
```

---

## 💡 **Code Comparison**

### ❌ **BEFORE**: Logic in API Route (Not Reusable)

```python
# projects.py (BEFORE)

@router.post("")
async def create_project(data: ProjectCreate, user_id: str = Depends(...)):
    # Business logic mixed with HTTP handling - CAN'T REUSE!
    db = get_supabase()
    
    # Validation
    if not data.name or len(data.name) > 255:
        raise HTTPException(400, "Invalid name")
    
    # Database operation
    result = db.from_("projects").insert({
        "user_id": user_id,
        "name": data.name,
        ...
    }).execute()
    
    return result.data[0]
```

**Problem**: MCP tools would duplicate all this logic!

---

### ✅ **AFTER**: Service Layer (Reusable Everywhere)

**Service** (Pure Python):
```python
# services/project_service.py

class ProjectService:
    def create_project(self, user_id: str, name: str, ...) -> dict:
        # Business logic - framework agnostic
        if not name or len(name) > 255:
            raise ValidationError("Invalid name")
        
        result = self.db.from_("projects").insert({...}).execute()
        return result.data[0]
```

**FastAPI Route** (Thin):
```python
# api/routes/projects.py

@router.post("")
async def create_project(
    data: ProjectCreate,
    user_id: str = Depends(get_current_user_id),
    service: ProjectService = Depends(get_project_service),
):
    try:
        return service.create_project(user_id, data.name, ...)  # Delegate!
    except ValidationError as e:
        raise HTTPException(400, e.message)  # Convert to HTTP
```

**FastMCP Tool** (Thin):
```python
# mcp/server.py

@mcp.tool()
async def create_project(user_id: str, name: str, ...):
    service = ProjectService(db=get_supabase())
    return service.create_project(user_id, name, ...)  # Same method!
```

**Result**: Business logic in ONE place, used by BOTH protocols! ✨

---

## 🚀 **Running Both Servers**

### Option 1: Separate Processes (Recommended for Development)

```bash
# Terminal 1: FastAPI REST server
just dev-server
# → http://localhost:8000

# Terminal 2: FastMCP server
python src/iris/mcp/server.py
# → stdio for MCP clients
```

### Option 2: Combined Server (Production)

```python
# src/iris/combined_server.py

from fastapi import FastAPI
import uvicorn

# FastAPI app
app = FastAPI()

# Import and mount routes
from iris.api.routes import projects, tasks
app.include_router(projects.router)
app.include_router(tasks.router)

# FastMCP endpoint (SSE transport)
from iris.mcp.server import mcp
from mcp.server.sse import SseServerTransport

@app.get("/mcp/sse")
async def mcp_sse_endpoint(request: Request):
    """MCP Server-Sent Events endpoint."""
    async with SseServerTransport("/message") as transport:
        await mcp.run(transport)

# Run both on same port
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Now accessible at:
- REST: `http://localhost:8000/api/v1/projects`
- MCP: `http://localhost:8000/mcp/sse`

---

## 🎯 **Service Layer Best Practices**

### 1. Pure Python Types

```python
# ✅ GOOD - Framework-agnostic
def create_project(self, user_id: str, name: str) -> dict:
    pass

# ❌ BAD - FastAPI-specific
async def create_project(self, request: Request) -> JSONResponse:
    pass
```

### 2. Raise Domain Exceptions

```python
# ✅ GOOD - Framework converts them
if not name:
    raise ValidationError("Name required")

# ❌ BAD - HTTP-specific
if not name:
    raise HTTPException(400, "Name required")
```

### 3. Inject Dependencies

```python
# ✅ GOOD - Testable, swappable
class ProjectService:
    def __init__(self, db: Client):
        self.db = db

# ❌ BAD - Global state, hard to test
class ProjectService:
    def method(self):
        db = get_supabase()  # Hidden dependency
```

### 4. Return Domain Objects

```python
# ✅ GOOD - Framework formats response
def get_project(self, project_id: UUID) -> dict:
    return {"id": ..., "name": ...}

# ❌ BAD - HTTP-specific
def get_project(self, project_id: UUID) -> JSONResponse:
    return JSONResponse(content={...}, status_code=200)
```

---

## 🧪 **Testing Benefits**

**Service Layer Testing** (No framework needed):
```python
# tests/unit/test_project_service.py

def test_create_project_validates_name():
    mock_db = MockSupabaseClient()
    service = ProjectService(db=mock_db)
    
    # Test business logic directly!
    with pytest.raises(ValidationError):
        service.create_project(user_id="123", name="")
```

**vs Framework Testing** (Slower, more complex):
```python
# tests/integration/test_api.py

async def test_create_project_endpoint():
    client = TestClient(app)  # Start whole FastAPI app
    response = client.post("/api/v1/projects", ...)  # HTTP request
    assert response.status_code == 400
```

Service layer tests are:
- ⚡ **Faster** (no HTTP overhead)
- 🎯 **Focused** (test business logic only)
- 🔧 **Easier to mock** (simple dependency injection)

---

## 📋 **Implementation Checklist for Iris**

### Already Done:
- [x] ProjectService created (`src/iris/services/project_service.py`)
- [x] Example MCP server (`src/iris/mcp/server.py`)
- [x] Example refactored route (`src/iris/api/routes/projects_refactored_example.py`)

### To Complete Service Layer Pattern:

**Services to Create** (one per entity):
- [ ] TaskService (`src/iris/services/task_service.py`)
- [ ] IdeaService (`src/iris/services/idea_service.py`)
- [ ] ReminderService (`src/iris/services/reminder_service.py`)
- [ ] NoteService (`src/iris/services/note_service.py`)

**Refactor API Routes** (make thin):
- [ ] Refactor `api/routes/tasks.py` to use TaskService
- [ ] Refactor `api/routes/ideas.py` to use IdeaService
- [ ] Refactor `api/routes/reminders.py` to use ReminderService
- [ ] Refactor `api/routes/notes.py` to use NoteService
- [ ] Refactor `api/routes/projects.py` (use example as template)

**Add MCP Tools**:
- [ ] Add task tools to `mcp/server.py`
- [ ] Add idea tools to `mcp/server.py`
- [ ] Add reminder tools to `mcp/server.py`
- [ ] Add note tools to `mcp/server.py`

**Testing**:
- [ ] Unit tests for each service
- [ ] Integration tests verify REST + MCP return same results

---

## 🎯 **Benefits for Iris**

1. **Code Reuse**: Write business logic once, use in:
   - REST API (for frontend)
   - MCP server (for AI agents)
   - CLI commands (future)
   - Background jobs (reminders, sync)

2. **Easy Testing**: Test services without starting FastAPI or MCP

3. **Clear Separation**:
   - Routes: HTTP concerns (status codes, headers, parsing)
   - Tools: MCP concerns (tool schemas, descriptions)
   - Services: Business logic (validation, data operations)

4. **Future-Proof**: Add GraphQL, gRPC, WebSockets - all use same services!

---

## 🚀 **Next Steps**

1. Review `projects_refactored_example.py` to see the pattern
2. Review `project_service.py` for framework-agnostic logic
3. Review `mcp/server.py` for tool implementation
4. Refactor remaining API routes to use services
5. Add remaining MCP tools

**Want me to refactor all the routes and complete the MCP server?** 🤔

