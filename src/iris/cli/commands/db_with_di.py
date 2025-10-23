"""Database CLI commands using dependency injection.

This module shows how CLI commands would work with dependency injection
instead of global state.
"""

import asyncio
import time

import typer
from dependency_injector.wiring import Provide, inject
from rich.console import Console

from iris.cli.output.display import DatabaseDisplay
from iris.core.config.settings import Settings
from iris.core.container import Container
from iris.core.database.connection import DatabaseConnection
from iris.core.utils.error_handler import ErrorHandler
from iris.core.utils.logging import get_module_logger

logger = get_module_logger("cli.db")
console = Console()


@inject
def migrate(
    ctx: typer.Context,
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be migrated without executing"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed migration output"),
    settings: Settings = Provide[Container.settings],
    db_connection: DatabaseConnection = Provide[Container.database_connection],
    error_handler: ErrorHandler = Provide[Container.error_handler],
) -> None:
    """Run database migrations."""
    start_time = time.time()

    try:
        logger.info(f"Starting migration (dry_run={dry_run}, verbose={verbose})")

        # Migration logic here
        # All dependencies are explicit and testable!

        logger.info(f"Migration completed in {time.time() - start_time:.2f}s")
        console.print("[green]✓ Database migration completed successfully[/green]")

    except Exception as e:
        logger.error(f"Migration failed: {e}")
        error_handler.handle_error(e, context={"operation": "migrate"})
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e


@inject
def test_connection(
    ctx: typer.Context,
    timeout: int = typer.Option(30, "--timeout", help="Connection timeout in seconds"),
    db_connection: DatabaseConnection = Provide[Container.database_connection],
    error_handler: ErrorHandler = Provide[Container.error_handler],
) -> None:
    """Test database connection."""
    start_time = time.time()

    try:
        logger.info(f"Testing database connection (timeout={timeout}s)")

        # Test connection
        result = asyncio.run(db_connection.test_connection())

        if result:
            console.print("[green]✓ Database connection successful[/green]")
        else:
            console.print("[red]✗ Database connection failed[/red]")
            raise typer.Exit(1)

        logger.info(f"Connection test completed in {time.time() - start_time:.2f}s")

    except Exception as e:
        logger.error(f"Connection test failed: {e}")
        error_handler.handle_error(e, context={"operation": "test_connection"})
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e


@inject
def status(
    ctx: typer.Context,
    detailed: bool = typer.Option(False, "--detailed", help="Show detailed status information"),
    settings: Settings = Provide[Container.settings],
    db_connection: DatabaseConnection = Provide[Container.database_connection],
    error_handler: ErrorHandler = Provide[Container.error_handler],
) -> None:
    """Show database status."""
    start_time = time.time()

    try:
        logger.info(f"Getting database status (detailed={detailed})")

        # Get connection information
        connection_info = asyncio.run(db_connection.get_connection_info())
        if connection_info is None:
            connection_info = {}

        # Display status
        display = DatabaseDisplay(console)
        display.show_database_status(settings, connection_info)

        logger.info(f"Status check completed in {time.time() - start_time:.2f}s")

    except Exception as e:
        logger.error(f"Status check failed: {e}")
        error_handler.handle_error(e, context={"operation": "status"})
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1) from e


# Create the CLI app
app = typer.Typer(
    name="db",
    help="Database management commands for Iris",
    no_args_is_help=True,
)

app.command()(migrate)
app.command()(test_connection)
app.command()(status)
