"""FastMCP server for Iris.

Provides MCP tools that share business logic with REST API.
Both MCP tools and REST endpoints call the same service layer.

Run with:
    python src/iris/mcp/server.py

Or via stdio for MCP clients:
    python src/iris/mcp/server.py --transport stdio
"""

from typing import Any

from mcp import ServerSession
from mcp.server import Server
from mcp.types import Tool

from iris.database.supabase import get_supabase
from iris.models.project import ProjectStatus
from iris.services.project_service import ProjectService
from iris.utils.exceptions import AuthorizationError, DatabaseError, ValidationError
from iris.utils.logging import log_error, log_info

# Initialize MCP server
mcp = Server("iris-mcp")


# Helper: Get service instances


def get_services() -> dict[str, Any]:
    """Get all service instances.
    
    Returns dict of services for easy access in tools.
    """
    db = get_supabase()
    return {
        "projects": ProjectService(db=db),
        # Add more services as they're created:
        # "tasks": TaskService(db=db),
        # "ideas": IdeaService(db=db),
        # etc.
    }


# MCP Tools - Thin wrappers around services


@mcp.tool()
async def list_projects(
    user_id: str,
    status: str | None = None
) -> list[dict[str, Any]]:
    """List user's projects.
    
    Args:
        user_id: Authenticated user UUID
        status: Optional filter (active/archived/completed)
        
    Returns:
        List of user's projects
        
    Note: This tool calls the SAME ProjectService.list_projects()
    method that the REST API uses!
    """
    try:
        log_info(f"MCP tool: list_projects called for user {user_id}")
        
        services = get_services()
        status_filter = ProjectStatus(status) if status else None
        
        # Call same service method as REST API!
        projects = services["projects"].list_projects(
            user_id=user_id,
            status_filter=status_filter
        )
        
        log_info(f"Returned {len(projects)} projects")
        return projects
        
    except Exception as e:
        log_error(f"MCP tool error: {str(e)}", exception=e)
        raise


@mcp.tool()
async def create_project(
    user_id: str,
    name: str,
    description: str | None = None,
    status: str = "active"
) -> dict[str, Any]:
    """Create new project.
    
    Args:
        user_id: Authenticated user UUID
        name: Project name (1-255 chars)
        description: Optional project description
        status: Project status (active/archived/completed)
        
    Returns:
        Created project
        
    Note: Calls SAME ProjectService.create_project() as REST API!
    """
    try:
        log_info(f"MCP tool: create_project for user {user_id}, name={name}")
        
        services = get_services()
        project_status = ProjectStatus(status)
        
        # Call same service method as REST API!
        project = services["projects"].create_project(
            user_id=user_id,
            name=name,
            description=description,
            status=project_status
        )
        
        log_info(f"Created project: {project['id']}")
        return project
        
    except (ValidationError, DatabaseError, AuthorizationError) as e:
        log_error(f"MCP tool error: {str(e)}", exception=e)
        raise


@mcp.tool()
async def get_project(
    user_id: str,
    project_id: str
) -> dict[str, Any]:
    """Get project by ID.
    
    Args:
        user_id: Authenticated user UUID
        project_id: Project UUID
        
    Returns:
        Project details
    """
    try:
        from uuid import UUID
        
        services = get_services()
        return services["projects"].get_project(
            user_id=user_id,
            project_id=UUID(project_id)
        )
    except AuthorizationError as e:
        log_error(f"Project not found or unauthorized: {project_id}")
        raise


@mcp.tool()
async def update_project(
    user_id: str,
    project_id: str,
    name: str | None = None,
    description: str | None = None,
    status: str | None = None
) -> dict[str, Any]:
    """Update project.
    
    Args:
        user_id: Authenticated user UUID
        project_id: Project UUID
        name: Optional new name
        description: Optional new description
        status: Optional new status
        
    Returns:
        Updated project
    """
    try:
        from uuid import UUID
        
        services = get_services()
        status_enum = ProjectStatus(status) if status else None
        
        return services["projects"].update_project(
            user_id=user_id,
            project_id=UUID(project_id),
            name=name,
            description=description,
            status=status_enum
        )
    except (ValidationError, AuthorizationError, DatabaseError) as e:
        log_error(f"MCP tool error: {str(e)}", exception=e)
        raise


@mcp.tool()
async def delete_project(
    user_id: str,
    project_id: str
) -> dict[str, str]:
    """Delete project.
    
    Args:
        user_id: Authenticated user UUID
        project_id: Project UUID to delete
        
    Returns:
        Confirmation message
    """
    try:
        from uuid import UUID
        
        services = get_services()
        services["projects"].delete_project(
            user_id=user_id,
            project_id=UUID(project_id)
        )
        
        return {"status": "deleted", "project_id": project_id}
        
    except (AuthorizationError, DatabaseError) as e:
        log_error(f"MCP tool error: {str(e)}", exception=e)
        raise


# Main entry point


if __name__ == "__main__":
    import asyncio
    
    from mcp.server.stdio import stdio_server
    
    log_info("Starting Iris MCP Server", title="MCP Server")
    log_info("Available tools: list_projects, create_project, get_project, update_project, delete_project")
    
    # Run MCP server via stdio
    asyncio.run(stdio_server(mcp))

