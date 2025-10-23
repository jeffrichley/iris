"""CLI output display for Iris project management system.

This module provides rich output formatting and display capabilities
for the Iris CLI tool.
"""

from typing import Any

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table


class DatabaseDisplay:
    """Display class for database operations."""

    def __init__(self, console: Console):
        """Initialize database display.

        Args:
            console: Rich console instance
        """
        self.console = console

    def show_migration_success(self) -> None:
        """Show migration success message."""
        self.console.print()
        self.console.print(
            Panel(
                "[bold green][SUCCESS] Database migrations completed successfully![/bold green]",
                title="Migration Complete",
                border_style="green",
            )
        )
        self.console.print()

    def show_migration_dry_run(self) -> None:
        """Show migration dry run results."""
        table = Table(title="Migration Dry Run", box=box.ROUNDED)
        table.add_column("Migration", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Description")

        table.add_row("001_initial_schema", "[SUCCESS] Applied", "Create initial database schema")
        table.add_row("002_add_user_preferences", "[SUCCESS] Applied", "Add user preferences table")
        table.add_row("003_add_project_tags", "[PENDING] Pending", "Add project tags functionality")

        self.console.print()
        self.console.print(table)
        self.console.print()

    def show_connection_success(self, database_url: str) -> None:
        """Show connection success message."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold green][SUCCESS] Database connection successful![/bold green]\n"
                f"[dim]URL: {database_url}[/dim]",
                title="Connection Test",
                border_style="green",
            )
        )
        self.console.print()

    def show_health_success(self, health_info: dict[str, Any], detailed: bool = False) -> None:
        """Show health check success."""
        if detailed:
            self._show_detailed_health(health_info)
        else:
            self._show_basic_health(health_info)

    def _show_basic_health(self, health_info: dict[str, Any]) -> None:
        """Show basic health information."""
        table = Table(title="Database Health Check", box=box.ROUNDED)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        table.add_column("Status")

        table.add_row("Status", "Healthy", "[SUCCESS]")
        table.add_row("Response Time", f"{health_info.get('response_time', 0):.3f}s", "[SUCCESS]")
        table.add_row("Query Time", f"{health_info.get('query_time', 0):.3f}s", "[SUCCESS]")
        table.add_row("Project Count", str(health_info.get("project_count", 0)), "[SUCCESS]")

        self.console.print()
        self.console.print(table)
        self.console.print()

    def _show_detailed_health(self, health_info: dict[str, Any]) -> None:
        """Show detailed health information."""
        # Main health table
        main_table = Table(title="Database Health Check", box=box.ROUNDED)
        main_table.add_column("Metric", style="cyan")
        main_table.add_column("Value", style="green")
        main_table.add_column("Status")

        main_table.add_row("Status", "Healthy", "[SUCCESS]")
        main_table.add_row(
            "Response Time", f"{health_info.get('response_time', 0):.3f}s", "[SUCCESS]"
        )
        main_table.add_row("Query Time", f"{health_info.get('query_time', 0):.3f}s", "[SUCCESS]")
        main_table.add_row("Project Count", str(health_info.get("project_count", 0)), "[SUCCESS]")
        main_table.add_row("Timestamp", health_info.get("timestamp", "N/A"), "[SUCCESS]")

        # Connection pool table
        pool_info = health_info.get("pool_info", {})
        pool_table = Table(title="Connection Pool", box=box.ROUNDED)
        pool_table.add_column("Metric", style="cyan")
        pool_table.add_column("Value", style="blue")

        pool_table.add_row("Pool Size", str(pool_info.get("pool_size", 0)))
        pool_table.add_row("Checked In", str(pool_info.get("checked_in", 0)))
        pool_table.add_row("Checked Out", str(pool_info.get("checked_out", 0)))
        pool_table.add_row("Overflow", str(pool_info.get("overflow", 0)))
        pool_table.add_row("Invalid", str(pool_info.get("invalid", 0)))

        self.console.print()
        self.console.print(main_table)
        self.console.print()
        self.console.print(pool_table)
        self.console.print()

    def show_health_failed(self, health_info: dict[str, Any]) -> None:
        """Show health check failure."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Database health check failed![/bold red]\n"
                f"[dim]Error: {health_info.get('error', 'Unknown error')}[/dim]",
                title="Health Check Failed",
                border_style="red",
            )
        )
        self.console.print()

    def show_database_status(self, settings: Any, connection_info: dict[str, Any]) -> None:
        """Show database status and configuration."""
        # Configuration table
        config_table = Table(title="Database Configuration", box=box.ROUNDED)
        config_table.add_column("Setting", style="cyan")
        config_table.add_column("Value", style="blue")

        config_table.add_row("Database URL", settings.get_database_url())
        config_table.add_row("Environment", settings.application.environment)
        config_table.add_row("Pool Size", str(settings.database.db_pool_size))
        config_table.add_row("Pool Timeout", f"{settings.database.db_pool_timeout}s")
        config_table.add_row("Pool Recycle", f"{settings.database.db_pool_recycle}s")
        config_table.add_row("Echo", str(settings.database.db_echo))

        # Connection info table
        conn_table = Table(title="Connection Information", box=box.ROUNDED)
        conn_table.add_column("Metric", style="cyan")
        conn_table.add_column("Value", style="green")

        conn_table.add_row("Pool Size", str(connection_info.get("pool_size", 0)))
        conn_table.add_row("Checked In", str(connection_info.get("checked_in", 0)))
        conn_table.add_row("Checked Out", str(connection_info.get("checked_out", 0)))
        conn_table.add_row("Overflow", str(connection_info.get("overflow", 0)))
        conn_table.add_row("Invalid", str(connection_info.get("invalid", 0)))

        self.console.print()
        self.console.print(config_table)
        self.console.print()
        self.console.print(conn_table)
        self.console.print()

    def show_reset_success(self) -> None:
        """Show database reset success."""
        self.console.print()
        self.console.print(
            Panel(
                "[bold green][SUCCESS] Database reset completed successfully![/bold green]\n"
                "[dim]All data has been removed from the database.[/dim]",
                title="Reset Complete",
                border_style="green",
            )
        )
        self.console.print()

    def show_backup_success(self, output_file: str) -> None:
        """Show backup success."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold green][SUCCESS] Database backup created successfully![/bold green]\n"
                f"[dim]Output file: {output_file}[/dim]",
                title="Backup Complete",
                border_style="green",
            )
        )
        self.console.print()

    def show_restore_success(self, input_file: str) -> None:
        """Show restore success."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold green][SUCCESS] Database restored successfully![/bold green]\n"
                f"[dim]Input file: {input_file}[/dim]",
                title="Restore Complete",
                border_style="green",
            )
        )
        self.console.print()


class ProgressDisplay:
    """Display class for progress operations."""

    def __init__(self, console: Console):
        """Initialize progress display.

        Args:
            console: Rich console instance
        """
        self.console = console

    def show_migration_progress(self, migrations: list[dict[str, Any]]) -> None:
        """Show migration progress."""
        table = Table(title="Migration Progress", box=box.ROUNDED)
        table.add_column("Migration", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Time")

        for migration in migrations:
            status = "[SUCCESS] Applied" if migration.get("applied", False) else "[PENDING] Running"
            time_str = (
                f"{migration.get('duration', 0):.2f}s" if migration.get("duration") else "N/A"
            )
            table.add_row(migration["name"], status, time_str)

        self.console.print()
        self.console.print(table)
        self.console.print()

    def show_connection_progress(self, steps: list[str]) -> None:
        """Show connection progress."""
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Connecting to database..."),
            console=self.console,
        ) as progress:
            task = progress.add_task("Connection", total=len(steps))

            for i, step in enumerate(steps):
                progress.update(task, description=f"Step {i + 1}: {step}")
                progress.advance(task)
                # Simulate work
                import time

                time.sleep(0.5)

    def show_health_progress(self) -> None:
        """Show health check progress."""
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]Performing health check..."),
            console=self.console,
        ) as progress:
            progress.add_task("Health Check", total=None)
            # Simulate work
            import time

            time.sleep(1)


class ErrorDisplay:
    """Display class for error messages."""

    def __init__(self, console: Console):
        """Initialize error display.

        Args:
            console: Rich console instance
        """
        self.console = console

    def show_migration_error(self, error: str) -> None:
        """Show migration error."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Migration failed![/bold red]\n"
                f"[dim]Error: {error}[/dim]\n\n"
                f"[yellow]Suggested fixes:[/yellow]\n"
                f"• Check database connection\n"
                f"• Verify migration files\n"
                f"• Check database permissions",
                title="Migration Error",
                border_style="red",
            )
        )
        self.console.print()

    def show_connection_failed(self, database_url: str) -> None:
        """Show connection failure."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Database connection failed![/bold red]\n"
                f"[dim]URL: {database_url}[/dim]\n\n"
                f"[yellow]Suggested fixes:[/yellow]\n"
                f"• Check database server is running\n"
                f"• Verify connection parameters\n"
                f"• Check network connectivity",
                title="Connection Failed",
                border_style="red",
            )
        )
        self.console.print()

    def show_connection_error(self, error: str) -> None:
        """Show connection error."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Connection error![/bold red]\n"
                f"[dim]Error: {error}[/dim]\n\n"
                f"[yellow]Suggested fixes:[/yellow]\n"
                f"• Check database credentials\n"
                f"• Verify database URL format\n"
                f"• Check firewall settings",
                title="Connection Error",
                border_style="red",
            )
        )
        self.console.print()

    def show_health_error(self, error: str) -> None:
        """Show health check error."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Health check failed![/bold red]\n"
                f"[dim]Error: {error}[/dim]\n\n"
                f"[yellow]Suggested fixes:[/yellow]\n"
                f"• Check database connectivity\n"
                f"• Verify database schema\n"
                f"• Check database permissions",
                title="Health Check Error",
                border_style="red",
            )
        )
        self.console.print()

    def show_status_error(self, error: str) -> None:
        """Show status error."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Status check failed![/bold red]\n"
                f"[dim]Error: {error}[/dim]\n\n"
                f"[yellow]Suggested fixes:[/yellow]\n"
                f"• Check database connection\n"
                f"• Verify configuration\n"
                f"• Check database permissions",
                title="Status Error",
                border_style="red",
            )
        )
        self.console.print()

    def show_reset_error(self, error: str) -> None:
        """Show reset error."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Database reset failed![/bold red]\n"
                f"[dim]Error: {error}[/dim]\n\n"
                f"[yellow]Suggested fixes:[/yellow]\n"
                f"• Check database permissions\n"
                f"• Verify database connection\n"
                f"• Check for active connections",
                title="Reset Error",
                border_style="red",
            )
        )
        self.console.print()

    def show_backup_error(self, error: str) -> None:
        """Show backup error."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Database backup failed![/bold red]\n"
                f"[dim]Error: {error}[/dim]\n\n"
                f"[yellow]Suggested fixes:[/yellow]\n"
                f"• Check write permissions\n"
                f"• Verify disk space\n"
                f"• Check database connection",
                title="Backup Error",
                border_style="red",
            )
        )
        self.console.print()

    def show_restore_error(self, error: str) -> None:
        """Show restore error."""
        self.console.print()
        self.console.print(
            Panel(
                f"[bold red]❌ Database restore failed![/bold red]\n"
                f"[dim]Error: {error}[/dim]\n\n"
                f"[yellow]Suggested fixes:[/yellow]\n"
                f"• Check backup file exists\n"
                f"• Verify backup file format\n"
                f"• Check database permissions",
                title="Restore Error",
                border_style="red",
            )
        )
        self.console.print()
