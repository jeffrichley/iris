"""Application settings using Pydantic Settings.

Compliant with Constitution Principle 2: Explicit Over Implicit
All configuration centralized in dedicated config package.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables.
    
    All values loaded from .env file or environment variables.
    Validated on application startup per FR-055, FR-069.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # Ignore extra env vars
    )

    # Supabase Configuration (FR-027)
    SUPABASE_URL: str = Field(
        ...,
        description="Supabase project URL from dashboard"
    )
    SUPABASE_ANON_KEY: str = Field(
        ...,
        description="Supabase anon/public key (RLS enforced)"
    )
    SUPABASE_SERVICE_KEY: str = Field(
        default="",
        description="Supabase service role key (bypasses RLS, admin only)"
    )
    SUPABASE_JWT_SECRET: str = Field(
        ...,
        description="Supabase JWT secret for token validation"
    )

    # FastAPI Configuration
    API_HOST: str = Field(default="0.0.0.0")
    API_PORT: int = Field(default=8000, ge=1024, le=65535)
    ENVIRONMENT: Literal["development", "staging", "production"] = Field(
        default="development"
    )

    # Logging Configuration
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="DEBUG"
    )

    @field_validator("SUPABASE_URL")
    @classmethod
    def validate_supabase_url(cls, v: str) -> str:
        """Validate Supabase URL format (FR-055)."""
        if not v.startswith("https://"):
            raise ValueError("SUPABASE_URL must start with https://")
        if ".supabase.co" not in v:
            raise ValueError("SUPABASE_URL must be a valid Supabase project URL")
        return v

    @field_validator("SUPABASE_ANON_KEY", "SUPABASE_JWT_SECRET")
    @classmethod
    def validate_base64_jwt(cls, v: str) -> str:
        """Validate that keys appear to be base64-encoded JWTs (FR-055)."""
        if not v:
            raise ValueError("Supabase keys cannot be empty")
        # Basic JWT format check (should have 3 parts separated by dots)
        parts = v.split(".")
        if len(parts) != 3:
            raise ValueError("Invalid JWT format - expected 3 parts separated by dots")
        return v

    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.ENVIRONMENT == "development"

    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.ENVIRONMENT == "production"


@lru_cache
def get_settings() -> Settings:
    """Get cached settings singleton.
    
    Settings loaded once and cached for application lifetime.
    Validates configuration on first access per FR-055, FR-069.
    
    Returns:
        Settings: Validated application settings
        
    Raises:
        ValidationError: If .env configuration is invalid or missing required fields
    """
    return Settings()

