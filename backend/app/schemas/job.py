"""Job request/response schemas."""

from datetime import datetime
from pydantic import BaseModel, Field


class JobBase(BaseModel):
    """Base job schema."""
    title: str = Field(..., min_length=1, max_length=255)
    company: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    location: str | None = None
    salary_min: float | None = None
    salary_max: float | None = None
    url: str | None = None
    requirements: str | None = None


class JobCreate(JobBase):
    """Job creation schema."""
    linkedin_id: str = Field(..., min_length=1, max_length=255)


class JobUpdate(BaseModel):
    """Job update schema."""
    title: str | None = None
    company: str | None = None
    description: str | None = None
    location: str | None = None
    salary_min: float | None = None
    salary_max: float | None = None
    url: str | None = None
    requirements: str | None = None
    is_saved: bool | None = None


class JobResponse(JobBase):
    """Job response schema."""
    id: int
    linkedin_id: str
    user_id: int
    is_saved: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
