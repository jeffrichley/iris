"""Project business logic service.

Framework-agnostic business logic that can be used by:
- FastAPI REST endpoints
- FastMCP MCP server tools
- CLI commands
- Background jobs

All methods are pure Python functions with no FastAPI/HTTP dependencies.
"""

from uuid import UUID

from supabase import Client

from iris.models.project import ProjectStatus
from iris.utils.exceptions import AuthorizationError, DatabaseError, ValidationError
from iris.utils.logging import log_error


class ProjectService:
    """Service for project business logic.
    
    All methods are framework-agnostic and can be called from:
    - FastAPI routes (REST API)
    - FastMCP tools (MCP server)
    - CLI commands
    - Background tasks
    
    Methods use pure Python types and return domain objects.
    """
    
    def __init__(self, db: Client):
        """Initialize service with database client.
        
        Args:
            db: Supabase client (injected, testable)
        """
        self.db = db
    
    def list_projects(
        self,
        user_id: str,
        status_filter: ProjectStatus | None = None
    ) -> list[dict[str, str]]:
        """List user's projects with optional status filter.
        
        Args:
            user_id: Authenticated user UUID
            status_filter: Optional filter by project status
            
        Returns:
            List of user's projects
            
        Raises:
            DatabaseError: If database query fails
            
        RLS: Automatically filters by user_id via auth.uid()
        """
        try:
            query = self.db.from_("projects").select("*")
            
            if status_filter:
                query = query.eq("status", status_filter.value)
            
            response = query.execute()
            return response.data
            
        except Exception as e:
            log_error(f"Failed to list projects: {str(e)}", exception=e)
            raise DatabaseError(message="Failed to retrieve projects") from e
    
    def get_project(self, user_id: str, project_id: UUID) -> dict[str, str]:
        """Get specific project by ID.
        
        Args:
            user_id: Authenticated user UUID (for logging/validation)
            project_id: Project UUID to retrieve
            
        Returns:
            Project data
            
        Raises:
            AuthorizationError: If project not found or not owned by user
            DatabaseError: If database query fails
            
        RLS: Returns 404 if project doesn't belong to user
        """
        try:
            response = self.db.from_("projects") \
                .select("*") \
                .eq("id", str(project_id)) \
                .execute()
            
            if not response.data:
                # RLS filtered it out or doesn't exist
                raise AuthorizationError(
                    message="Project not found",
                    details=f"project_id={project_id}, user_id={user_id}"
                )
            
            return response.data[0]
            
        except AuthorizationError:
            raise
        except Exception as e:
            log_error(f"Failed to get project: {str(e)}", exception=e)
            raise DatabaseError(message="Failed to retrieve project") from e
    
    def create_project(
        self,
        user_id: str,
        name: str,
        description: str | None = None,
        status: ProjectStatus = ProjectStatus.ACTIVE
    ) -> dict[str, str]:
        """Create new project for user.
        
        Args:
            user_id: Authenticated user UUID
            name: Project name (1-255 chars)
            description: Optional project description
            status: Project status (default: active)
            
        Returns:
            Created project with all fields
            
        Raises:
            ValidationError: If input validation fails
            DatabaseError: If database insert fails
        """
        # Validate input
        if not name or len(name) > 255:
            raise ValidationError(message="Project name must be 1-255 characters")
        
        try:
            data = {
                "user_id": user_id,
                "name": name,
                "description": description,
                "status": status.value
            }
            
            response = self.db.from_("projects").insert(data).execute()
            
            if not response.data:
                raise DatabaseError(message="Failed to create project")
            
            return response.data[0]
            
        except (ValidationError, DatabaseError):
            raise
        except Exception as e:
            log_error(f"Failed to create project: {str(e)}", exception=e)
            raise DatabaseError(message="Failed to create project") from e
    
    def update_project(
        self,
        user_id: str,
        project_id: UUID,
        name: str | None = None,
        description: str | None = None,
        status: ProjectStatus | None = None
    ) -> dict[str, str]:
        """Update project fields.
        
        Args:
            user_id: Authenticated user UUID
            project_id: Project UUID to update
            name: Optional new name
            description: Optional new description
            status: Optional new status
            
        Returns:
            Updated project
            
        Raises:
            ValidationError: If no fields to update or invalid values
            AuthorizationError: If project not found or not owned
            DatabaseError: If update fails
        """
        # Build update data (only include provided fields)
        update_data: dict[str, str] = {}
        
        if name is not None:
            if not name or len(name) > 255:
                raise ValidationError(message="Project name must be 1-255 characters")
            update_data["name"] = name
        
        if description is not None:
            update_data["description"] = description
        
        if status is not None:
            update_data["status"] = status.value
        
        if not update_data:
            raise ValidationError(message="No fields to update")
        
        try:
            response = self.db.from_("projects") \
                .update(update_data) \
                .eq("id", str(project_id)) \
                .execute()
            
            if not response.data:
                raise AuthorizationError(
                    message="Project not found",
                    details=f"project_id={project_id}, user_id={user_id}"
                )
            
            return response.data[0]
            
        except (ValidationError, AuthorizationError):
            raise
        except Exception as e:
            log_error(f"Failed to update project: {str(e)}", exception=e)
            raise DatabaseError(message="Failed to update project") from e
    
    def delete_project(self, user_id: str, project_id: UUID) -> None:
        """Delete project (cascades to tasks/notes).
        
        Args:
            user_id: Authenticated user UUID
            project_id: Project UUID to delete
            
        Raises:
            AuthorizationError: If project not found or not owned
            DatabaseError: If deletion fails
            
        Side Effects:
            - Cascades delete to tasks (FK: project_id)
            - Cascades delete to notes (FK: project_id)
        """
        try:
            response = self.db.from_("projects") \
                .delete() \
                .eq("id", str(project_id)) \
                .execute()
            
            if not response.data:
                raise AuthorizationError(
                    message="Project not found",
                    details=f"project_id={project_id}, user_id={user_id}"
                )
            
        except AuthorizationError:
            raise
        except Exception as e:
            log_error(f"Failed to delete project: {str(e)}", exception=e)
            raise DatabaseError(message="Failed to delete project") from e

