from __future__ import annotations

from pydantic import BaseModel, Field, AnyUrl, validator

class YCStartup(BaseModel):
    """Pydantic model representing a Y Combinator startup.

    Attributes:
        company_name: The official company name. Must be non‑empty.
        description: Short tagline or description (optional).
        website: Official website URL (optional, must be a valid URL if present).
        batch: YC batch identifier, e.g. "Winter 2012" (optional).
        industry: Primary industry classification (optional).
        location: Human‑readable location string (optional).
    """

    company_name: str = Field(..., description="The official name of the startup.")
    description: str | None = Field(None, description="Short description or tagline.")
    website: AnyUrl | None = Field(None, description="Official website URL.")
    batch: str | None = Field(None, description="YC batch, e.g., 'Winter 2012'.")
    industry: str | None = Field(None, description="Primary industry of the startup.")
    location: str | None = Field(None, description="Location(s) of the startup.")

    @validator("company_name")
    def name_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("company_name cannot be empty")
        return v
