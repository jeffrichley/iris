# Architecture Decision: Service Layer for REST + MCP

**Date**: October 20, 2025  
**Decision**: Use Service Layer pattern to share business logic between FastAPI REST and FastMCP  
**Status**: ✅ Approved, Implementation Started

---

## 📊 **Decision Summary**

**Problem**: Need to provide both REST API (for frontend) and MCP server (for AI agents) without duplicating business logic.

**Solution**: Extract all business logic into framework-agnostic Service classes that both FastAPI routes and FastMCP tools call.

---

## 🏗️ **Pattern**

```
FastAPI Route          FastMCP Tool
     │                      │
     └──────┬───────────────┘
            │
     ProjectService.create_project()  ← Single implementation
            │
        Supabase DB
```

**Code Sharing**:
- ✅ Service layer: 100% shared
- ✅ Models: 100% shared
- ✅ Database: 100% shared
- ✅ Auth: 100% shared
- ✅ Utils: 100% shared

**Protocol-Specific**:
- FastAPI: Request/Response schemas, HTTP status codes, exception conversion
- FastMCP: Tool schemas, MCP types, stdio transport

---

## 📝 **Implementation Example**

See these files for the pattern:

1. **Service Layer** (Pure Python):
   - `src/iris/services/project_service.py` - Business logic
   - Methods: `list_projects()`, `create_project()`, `get_project()`, etc.

2. **FastAPI Route** (Thin Controller):
   - `src/iris/api/routes/projects_refactored_example.py` - HTTP wrapper
   - Delegates to ProjectService
   - Converts exceptions to HTTP responses

3. **FastMCP Server** (Thin Tools):
   - `src/iris/mcp/server.py` - MCP tools
   - Delegates to ProjectService
   - Same business logic as REST!

4. **Integration Guide**:
   - `src/iris/mcp/FASTAPI_FASTMCP_INTEGRATION.md` - Complete guide

5. **Pattern Documentation**:
   - `src/iris/services/SERVICE_LAYER_PATTERN.md` - Pattern explanation

---

## ✅ **Benefits**

| Benefit | Description |
|---------|-------------|
| **Code Reuse** | Write business logic once, use everywhere |
| **Testability** | Test services without starting servers |
| **Maintainability** | Change logic in one place |
| **Flexibility** | Easy to add new protocols (GraphQL, gRPC, CLI) |
| **Separation** | Clear boundaries: protocol vs business logic |

---

## 🎯 **Current Status**

**Implemented**:
- [x] Service layer pattern defined
- [x] ProjectService created (example)
- [x] Example refactored API route
- [x] Example MCP server with tools
- [x] Integration documentation

**To Do**:
- [ ] Create services for other entities (Task, Idea, Reminder, Note)
- [ ] Refactor all API routes to use services
- [ ] Add all MCP tools
- [ ] Add unit tests for services
- [ ] Add integration tests (verify REST + MCP consistency)

---

## 📚 **Reference Files**

| File | Purpose |
|------|---------|
| `services/SERVICE_LAYER_PATTERN.md` | Pattern explanation + rules |
| `mcp/FASTAPI_FASTMCP_INTEGRATION.md` | Integration guide |
| `services/project_service.py` | Example service implementation |
| `api/routes/projects_refactored_example.py` | Example thin controller |
| `mcp/server.py` | Example MCP server |

---

## 🚀 **Next Steps**

1. **Review the pattern**:
   - Read `services/SERVICE_LAYER_PATTERN.md`
   - Read `mcp/FASTAPI_FASTMCP_INTEGRATION.md`
   - Study `project_service.py` as template

2. **Refactor existing code**:
   - Create TaskService, IdeaService, ReminderService, NoteService
   - Refactor all API routes to use services
   - Add all MCP tools using same services

3. **Test**:
   - Write unit tests for services
   - Test REST API endpoints
   - Test MCP tools
   - Verify both return same data

---

**This pattern provides maximum code reuse and maintainability for Iris!** 🎯

