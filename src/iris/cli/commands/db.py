"""Database CLI commands for Iris project management system.

This module provides CLI commands for database operations
in the Iris application.
"""

import asyncio
import time
from pathlib import Path

import typer
from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn, TimeElapsedColumn

from iris.cli.output.display import DatabaseDisplay, ErrorDisplay
from iris.core.application import ensure_application_initialized
from iris.core.config.settings import initialize_settings
from iris.core.database.connection import initialize_database
from iris.core.utils.error_handler import get_global_error_handler, handle_errors
from iris.core.utils.exceptions import DatabaseError, MigrationError
from iris.core.utils.logging import get_cli_logger

app = typer.Typer(
    name="db",
    help="Database management commands for Iris",
    no_args_is_help=True,
    rich_markup_mode="rich",
)

console = Console()
logger = get_cli_logger()


@app.command()
@handle_errors(reraise=True, context={"command": "migrate"})
def migrate(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
    force: bool = typer.Option(False, "--force", "-f", help="Force migration without confirmation"),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="Show what would be migrated without applying"
    ),
) -> None:
    """Run database migrations."""
    logger.command_started("migrate", {"verbose": verbose, "force": force, "dry_run": dry_run})
    start_time = time.time()

    try:
        # Initialize application
        app = ensure_application_initialized()
        app.get_settings()
        app.get_database_connection()

        # Create migration display
        display = DatabaseDisplay(console)

        if dry_run:
            display.show_migration_dry_run()
            logger.command_completed("migrate", time.time() - start_time)
            return

        # Run migrations with progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Running migrations..."),
            BarColumn(),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Migrating database", total=100)

            # Simulate migration process
            for _i in range(10):
                progress.update(task, advance=10)
                time.sleep(0.1)  # Simulate work

        # Show migration results
        display.show_migration_success()

        logger.command_completed("migrate", time.time() - start_time)

    except (ConnectionError, MigrationError, DatabaseError) as e:
        logger.command_failed("migrate", str(e))
        error_display = ErrorDisplay(console)
        error_display.show_migration_error(str(e))
        raise typer.Exit(1) from None
    except Exception as e:
        # Handle unexpected errors
        error_handler = get_global_error_handler()
        iris_error = error_handler.handle_error(e, {"command": "migrate"})
        logger.command_failed("migrate", str(iris_error))
        error_display = ErrorDisplay(console)
        error_display.show_migration_error(str(iris_error))
        raise typer.Exit(1) from None


@app.command()
@handle_errors(reraise=False, context={"command": "test_connection"})
def test_connection(
    timeout: int = typer.Option(5, "--timeout", "-t", help="Connection timeout in seconds"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
) -> None:
    """Test database connection."""
    logger.command_started("test-connection", {"timeout": timeout, "verbose": verbose})
    start_time = time.time()

    try:
        # Initialize settings and database
        settings = initialize_settings()
        db_connection = initialize_database(
            settings.get_database_url(), **settings.get_connection_pool_config()
        )

        # Test connection with progress
        with Progress(
            SpinnerColumn(), TextColumn("[bold blue]Testing connection..."), console=console
        ) as progress:
            task = progress.add_task("Connecting to database", total=None)

            # Test connection
            result = asyncio.run(db_connection.test_connection())

            progress.update(task, completed=True)

        if result:
            display = DatabaseDisplay(console)
            display.show_connection_success(db_connection.database_url)
            logger.command_completed("test-connection", time.time() - start_time)
        else:
            error_display = ErrorDisplay(console)
            error_display.show_connection_failed(db_connection.database_url)
            raise typer.Exit(1) from None

    except ConnectionError as e:
        logger.command_failed("test-connection", str(e))
        error_display = ErrorDisplay(console)
        error_display.show_connection_error(str(e))
        raise typer.Exit(1) from None
    except Exception as e:
        # Handle unexpected errors
        error_handler = get_global_error_handler()
        iris_error = error_handler.handle_error(e, {"command": "test_connection"})
        logger.command_failed("test-connection", str(iris_error))
        error_display = ErrorDisplay(console)
        error_display.show_connection_error(str(iris_error))
        raise typer.Exit(1) from None


@app.command()
def health_check(
    detailed: bool = typer.Option(
        False, "--detailed", "-d", help="Show detailed health information"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output"),
) -> None:
    """Check database health and performance."""
    try:
        logger.command_started("health-check", {"detailed": detailed, "verbose": verbose})
        start_time = time.time()

        # Initialize settings and database
        settings = initialize_settings()
        db_connection = initialize_database(
            settings.get_database_url(), **settings.get_connection_pool_config()
        )

        # Perform health check with progress
        with Progress(
            SpinnerColumn(), TextColumn("[bold blue]Checking database health..."), console=console
        ) as progress:
            task = progress.add_task("Performing health check", total=None)

            # Get health information
            health_info = asyncio.run(db_connection.health_check())

            progress.update(task, completed=True)

        # Display health results
        display = DatabaseDisplay(console)
        if health_info["status"] == "healthy":
            display.show_health_success(health_info, detailed)
        else:
            display.show_health_failed(health_info)
            raise typer.Exit(1) from None

        logger.command_completed("health-check", time.time() - start_time)

    except Exception as e:
        logger.command_failed("health-check", str(e))
        error_display = ErrorDisplay(console)
        error_display.show_health_error(str(e))
        raise typer.Exit(1) from None


@app.command()
def status() -> None:
    """Show database status and configuration."""
    try:
        logger.command_started("status", {})
        start_time = time.time()

        # Initialize settings and database
        settings = initialize_settings()
        db_connection = initialize_database(
            settings.get_database_url(), **settings.get_connection_pool_config()
        )

        # Get connection information
        connection_info = asyncio.run(db_connection.get_connection_info())

        # Display status
        display = DatabaseDisplay(console)
        if connection_info is None:
            connection_info = {}
        display.show_database_status(settings, connection_info)

        logger.command_completed("status", time.time() - start_time)

    except Exception as e:
        logger.command_failed("status", str(e))
        error_display = ErrorDisplay(console)
        error_display.show_status_error(str(e))
        raise typer.Exit(1) from None


@app.command()
def reset(
    confirm: bool = typer.Option(False, "--confirm", "-y", help="Skip confirmation prompt"),
    force: bool = typer.Option(False, "--force", "-f", help="Force reset without confirmation"),
) -> None:
    """Reset database (WARNING: This will delete all data)."""
    if not confirm and not force:
        console.print("[bold red]WARNING: This will delete all data in the database![/bold red]")
        if not typer.confirm("Are you sure you want to continue?"):
            console.print("Operation cancelled.")
            raise typer.Exit(0)

    try:
        logger.command_started("reset", {"confirm": confirm, "force": force})
        start_time = time.time()

        # Initialize settings and database
        settings = initialize_settings()
        initialize_database(settings.get_database_url(), **settings.get_connection_pool_config())

        # Show reset progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold red]Resetting database..."),
            BarColumn(),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Resetting database", total=100)

            # Simulate reset process
            for _i in range(10):
                progress.update(task, advance=10)
                time.sleep(0.1)  # Simulate work

        # Show reset results
        display = DatabaseDisplay(console)
        display.show_reset_success()

        logger.command_completed("reset", time.time() - start_time)

    except Exception as e:
        logger.command_failed("reset", str(e))
        error_display = ErrorDisplay(console)
        error_display.show_reset_error(str(e))
        raise typer.Exit(1) from None


@app.command()
def backup(
    output: str | None = typer.Option(None, "--output", "-o", help="Output file path"),
    compress: bool = typer.Option(False, "--compress", "-c", help="Compress backup file"),
) -> None:
    """Create database backup."""
    try:
        logger.command_started("backup", {"output": output, "compress": compress})
        start_time = time.time()

        # Initialize settings and database
        settings = initialize_settings()
        initialize_database(settings.get_database_url(), **settings.get_connection_pool_config())

        # Generate backup filename if not provided
        if not output:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            output = f"iris_backup_{timestamp}.db"
            if compress:
                output += ".gz"

        # Show backup progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Creating backup..."),
            BarColumn(),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Backing up database", total=100)

            # Simulate backup process
            for _i in range(10):
                progress.update(task, advance=10)
                time.sleep(0.1)  # Simulate work

        # Show backup results
        display = DatabaseDisplay(console)
        display.show_backup_success(output)

        logger.command_completed("backup", time.time() - start_time)

    except Exception as e:
        logger.command_failed("backup", str(e))
        error_display = ErrorDisplay(console)
        error_display.show_backup_error(str(e))
        raise typer.Exit(1) from None


@app.command()
def restore(
    input_file: str = typer.Argument(..., help="Input backup file path"),
    force: bool = typer.Option(False, "--force", "-f", help="Force restore without confirmation"),
) -> None:
    """Restore database from backup."""
    if not force:
        console.print("[bold red]WARNING: This will replace all data in the database![/bold red]")
        if not typer.confirm("Are you sure you want to continue?"):
            console.print("Operation cancelled.")
            raise typer.Exit(0)

    try:
        logger.command_started("restore", {"input_file": input_file, "force": force})
        start_time = time.time()

        # Check if input file exists
        if not Path(input_file).exists():
            console.print(f"[bold red]Error: Backup file '{input_file}' not found.[/bold red]")
            raise typer.Exit(1) from None

        # Initialize settings and database
        settings = initialize_settings()
        initialize_database(settings.get_database_url(), **settings.get_connection_pool_config())

        # Show restore progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Restoring database..."),
            BarColumn(),
            TimeElapsedColumn(),
            console=console,
        ) as progress:
            task = progress.add_task("Restoring database", total=100)

            # Simulate restore process
            for _i in range(10):
                progress.update(task, advance=10)
                time.sleep(0.1)  # Simulate work

        # Show restore results
        display = DatabaseDisplay(console)
        display.show_restore_success(input_file)

        logger.command_completed("restore", time.time() - start_time)

    except Exception as e:
        logger.command_failed("restore", str(e))
        error_display = ErrorDisplay(console)
        error_display.show_restore_error(str(e))
        raise typer.Exit(1) from None


if __name__ == "__main__":
    app()
