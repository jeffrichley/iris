"""Main entry point using dependency injection.

This module shows how the main application would work with
dependency injection instead of global state.
"""

import typer
from dependency_injector.wiring import Provide, inject
from rich.console import Console

from iris.cli.commands.db_with_di import app as db_app
from iris.core.container import Container, configure_container

console = Console()


@inject
def main(
    environment: str = typer.Option("development", "--env", help="Application environment"),
    container: Container = Provide[Container],
) -> None:
    """Main entry point with dependency injection."""

    # Configure container for environment
    configure_container(environment)

    # Wire the container to inject dependencies
    container.wire(
        modules=[
            "iris.cli.commands.db_with_di",
            "iris.main_with_di",
        ]
    )

    try:
        # Create main CLI app
        cli_app = typer.Typer(name="iris", help="Iris Project Management System")

        # Add database commands
        cli_app.add_typer(db_app)

        # Run CLI
        cli_app()

    finally:
        # Cleanup (container handles this automatically)
        pass


if __name__ == "__main__":
    main()
