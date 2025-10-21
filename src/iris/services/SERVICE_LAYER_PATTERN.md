# Service Layer Pattern: Sharing Logic Between REST and MCP

**Purpose**: Extract business logic into reusable services that work with both FastAPI and FastMCP

---

## 🎯 **Architecture Overview**

```
┌──────────────────────┐  ┌──────────────────────┐
│   FastAPI REST API   │  │   FastMCP MCP Server │
│   (HTTP endpoints)   │  │   (stdio/SSE tools)  │
└──────────┬───────────┘  └───────────┬──────────┘
           │                          │
           │   ┌──────────────────┐   │
           └──→│  Service Layer   │←──┘
               │ (Business Logic) │
               └────────┬─────────┘
                        │
               ┌────────▼─────────┐
               │   Data Layer     │
               │   (Supabase)     │
               └──────────────────┘
```

**Key Benefits**:
- ✅ Business logic in one place
- ✅ Reusable across protocols (REST, MCP, CLI, jobs)
- ✅ Easy to test (framework-agnostic)
- ✅ Single source of truth
- ✅ DRY principle (Don't Repeat Yourself)

---

## 📝 **Service Layer Rules**

### DO:
- ✅ Accept pure Python types (str, UUID, enums, dataclasses)
- ✅ Return domain objects (dicts, models, primitives)
- ✅ Raise domain exceptions (ValidationError, AuthorizationError, etc.)
- ✅ Inject dependencies (database client, settings)
- ✅ Include business validation
- ✅ Log business events

### DON'T:
- ❌ Import FastAPI (HTTPException, Request, Response, Depends)
- ❌ Import MCP types (Tool, types, etc.)
- ❌ Return HTTP responses (JSONResponse, status codes)
- ❌ Use framework-specific decorators
- ❌ Access request/context directly

---

## 🏗️ **Pattern Implementation**

### Step 1: Service Layer (Framework-Agnostic)

```python
# src/iris/services/project_service.py

class ProjectService:
    """Pure business logic - no framework dependencies."""
    
    def __init__(self, db: Client):
        """Inject dependencies (testable, swappable)."""
        self.db = db
    
    def list_projects(
        self,
        user_id: str,
        status_filter: ProjectStatus | None = None
    ) -> list[dict[str, str]]:
        """Business logic for listing projects.
        
        Pure Python in/out - works with any framework!
        """
        query = self.db.from_("projects").select("*")
        if status_filter:
            query = query.eq("status", status_filter.value)
        return query.execute().data
    
    def create_project(
        self,
        user_id: str,
        name: str,
        description: str | None = None
    ) -> dict[str, str]:
        """Business logic for creating project."""
        # Validation
        if not name or len(name) > 255:
            raise ValidationError("Name must be 1-255 chars")
        
        # Create
        data = {"user_id": user_id, "name": name, "description": description}
        response = self.db.from_("projects").insert(data).execute()
        return response.data[0]
```

### Step 2: FastAPI Route (Thin Controller)

```python
# src/iris/api/routes/projects.py

from fastapi import APIRouter, Depends
from iris.services.project_service import ProjectService

router = APIRouter(prefix="/api/v1/projects")

def get_project_service() -> ProjectService:
    """FastAPI dependency for service injection."""
    return ProjectService(db=get_supabase())

@router.get("")
async def list_projects(
    user_id: str = Depends(get_current_user_id),
    status_filter: ProjectStatus | None = None,
    service: ProjectService = Depends(get_project_service),
) -> list[dict]:
    """Thin controller - delegates to service."""
    return service.list_projects(user_id, status_filter)

@router.post("")
async def create_project(
    data: ProjectCreate,
    user_id: str = Depends(get_current_user_id),
    service: ProjectService = Depends(get_project_service),
) -> dict:
    """Thin controller - delegates to service."""
    try:
        return service.create_project(user_id, data.name, data.description)
    except ValidationError as e:
        raise HTTPException(400, detail=e.message)
```

### Step 3: FastMCP Tools (Thin Wrapper)

```python
# src/iris/mcp/server.py

from mcp.server import Server
from mcp.types import Tool
from iris.services.project_service import ProjectService
from iris.database.supabase import get_supabase

mcp = Server("iris-mcp")

@mcp.tool()
async def list_projects(
    user_id: str,
    status: str | None = None
) -> list[dict]:
    """MCP tool - delegates to same service!"""
    service = ProjectService(db=get_supabase())
    
    status_filter = ProjectStatus(status) if status else None
    return service.list_projects(user_id, status_filter)

@mcp.tool()
async def create_project(
    user_id: str,
    name: str,
    description: str | None = None
) -> dict:
    """MCP tool - delegates to same service!"""
    service = ProjectService(db=get_supabase())
    return service.create_project(user_id, name, description)
```

---

## 🔗 **Running Both Together**

### Option A: Separate Processes (Recommended)

```bash
# Terminal 1: FastAPI REST Server
just dev-server

# Terminal 2: FastMCP Server
python src/iris/mcp/server.py
```

### Option B: Embedded MCP in FastAPI (Advanced)

```python
# src/iris/api/main.py

from fastapi import FastAPI
from mcp.server.fastapi import MCPServerFastAPI

app = FastAPI()

# Add MCP endpoint
mcp_server = MCPServerFastAPI("iris-mcp")
app.mount("/mcp", mcp_server.get_asgi_app())

# Now accessible at:
# - REST API: http://localhost:8000/api/v1/projects
# - MCP: http://localhost:8000/mcp (SSE endpoint)
```

---

## ✅ **Benefits of This Pattern**

**For REST API**:
- Thin controllers (5-10 lines per endpoint)
- Easy to add new endpoints
- Clear separation of concerns

**For MCP Server**:
- Thin tool wrappers
- Same business logic as REST
- Consistent behavior

**For Testing**:
- Test service layer directly (no FastAPI/MCP needed)
- Mock database easily
- Fast unit tests

**For Future**:
- CLI commands use same services
- Background jobs use same services
- GraphQL endpoints use same services
- Any new protocol uses same services!

---

## 📦 **Directory Structure**

```
src/iris/
├── services/           # ← Business Logic (Framework-Agnostic)
│   ├── project_service.py
│   ├── task_service.py
│   └── ...
├── api/               # ← FastAPI (Thin Controllers)
│   ├── main.py
│   └── routes/
│       ├── projects.py  # Calls ProjectService
│       └── ...
├── mcp/               # ← FastMCP (Thin Tool Wrappers)
│   ├── server.py        # MCP server with tools
│   └── tools/
│       ├── projects.py  # Calls ProjectService
│       └── ...
├── models/            # ← Data Models (Shared)
├── database/          # ← Data Access (Shared)
└── auth/              # ← Authentication (Shared)
```

---

## 🚀 **Implementation Plan**

For Iris, I recommend:

1. **Keep what's built**: Current API routes work
2. **Add service layer**: Extract business logic (I've started with ProjectService)
3. **Refactor routes**: Make them thin (call services)
4. **Add MCP server**: Create `src/iris/mcp/server.py` with tools
5. **Share everything**: Services, models, database, auth all shared

**Next Steps**:
1. Refactor all 5 API routes to use services
2. Create MCP server with matching tools
3. Test both protocols access same data

---

Would you like me to:
1. ✅ Refactor all API routes to use service layer pattern?
2. ✅ Create the FastMCP server with tools?
3. ✅ Show example of running both together?

This will give you clean separation and maximum reusability! 🎯
