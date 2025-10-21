"""Logging utilities using Rich library.

Compliant with Constitution Principle 4: Error Handling
MUST use rich library for colored logging output (FR-028).
"""

from datetime import datetime
from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from iris.config.settings import get_settings

# Global console instance
_console: Console | None = None


def get_console() -> Console:
    """Get Rich console singleton for colored output."""
    global _console
    
    if _console is None:
        settings = get_settings()
        _console = Console(
            color_system="auto",
            force_terminal=True if settings.ENVIRONMENT == "development" else None,
        )
    
    return _console


def log_info(message: str, title: str | None = None) -> None:
    """Log informational message with rich formatting."""
    console = get_console()
    
    if title:
        console.print(Panel(message, title=f"ℹ️  {title}", border_style="blue"))
    else:
        console.print(f"[blue]ℹ️  {message}[/blue]")


def log_warning(message: str, title: str | None = None) -> None:
    """Log warning message with rich formatting."""
    console = get_console()
    
    if title:
        console.print(Panel(message, title=f"⚠️  {title}", border_style="yellow"))
    else:
        console.print(f"[yellow]⚠️  {message}[/yellow]")


def log_error(message: str, title: str | None = None, exception: Exception | None = None) -> None:
    """Log error message with rich formatting.
    
    Compliant with FR-057: Sanitize output to prevent credential exposure.
    """
    console = get_console()
    
    # Sanitize message to redact potential secrets
    sanitized = _sanitize_message(message)
    
    if title:
        if exception:
            sanitized += f"\n\nError type: {type(exception).__name__}"
            # Don't include exception details to avoid credential leakage
        console.print(Panel(sanitized, title=f"❌ {title}", border_style="red"))
    else:
        console.print(f"[red]❌ {sanitized}[/red]")


def log_security_event(
    event_type: str,
    user_id: str | None = None,
    details: str | None = None,
    metadata: dict[str, Any] | None = None,
) -> None:
    """Log security event per FR-058, FR-059.
    
    Security events include:
    - Failed OAuth attempts
    - Invalid JWTs (tampered, expired, wrong algorithm)
    - RLS policy violations
    - Credential validation failures
    
    Args:
        event_type: Type of security event (e.g., "jwt_tampered", "oauth_failed")
        user_id: User identifier if available
        details: Additional event details
        metadata: Request metadata (IP, user-agent, etc.)
    """
    console = get_console()
    
    # Create security event table
    table = Table(title=f"🚨 Security Event: {event_type}", border_style="red")
    table.add_column("Field", style="bold")
    table.add_column("Value")
    
    table.add_row("Timestamp", datetime.utcnow().isoformat())
    table.add_row("Event Type", event_type)
    
    if user_id:
        table.add_row("User ID", user_id)
    
    if details:
        # Sanitize details to remove potential credentials
        sanitized_details = _sanitize_message(details)
        table.add_row("Details", sanitized_details)
    
    if metadata:
        for key, value in metadata.items():
            # Sanitize metadata values
            sanitized_value = _sanitize_message(str(value))
            table.add_row(key.title(), sanitized_value)
    
    console.print(table)


def _sanitize_message(message: str) -> str:
    """Sanitize log message to prevent credential exposure (FR-057).
    
    Redacts:
    - JWT tokens (Bearer xxx)
    - Supabase keys (eyJ...)
    - Passwords or secrets
    
    Args:
        message: Original message
        
    Returns:
        Sanitized message with credentials redacted
    """
    import re
    
    # Redact Bearer tokens
    message = re.sub(r"Bearer\s+[\w\-\.]+", "Bearer [REDACTED]", message)
    
    # Redact JWT-like strings (eyJ...)
    message = re.sub(r"eyJ[\w\-\.]+", "[REDACTED_JWT]", message)
    
    # Redact anything that looks like a secret key
    message = re.sub(
        r"(jwt_secret|api_key|secret_key|password|token)[\s:=]+[\w\-\.]+",
        r"\1=[REDACTED]",
        message,
        flags=re.IGNORECASE
    )
    
    return message

