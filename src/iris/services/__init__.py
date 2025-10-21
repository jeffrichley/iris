"""Business logic services for Iris.

Service layer provides reusable business logic for both:
- FastAPI REST endpoints
- FastMCP MCP server tools

All services are framework-agnostic - they work with pure Python types
and return domain objects, not HTTP responses.
"""

from iris.services.project_service import ProjectService

__all__ = ["ProjectService"]

