"""Application request/response schemas."""

from datetime import datetime
from pydantic import BaseModel, Field
from enum import Enum


class ApplicationStatus(str, Enum):
    """Application status enum."""
    PENDING = "pending"
    APPLIED = "applied"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    WITHDRAWN = "withdrawn"


class ApplicationBase(BaseModel):
    """Base application schema."""
    status: ApplicationStatus = ApplicationStatus.PENDING
    cover_letter: str | None = None
    notes: str | None = None


class ApplicationCreate(BaseModel):
    """Application creation schema."""
    job_id: int
    cover_letter: str | None = None


class ApplicationUpdate(BaseModel):
    """Application update schema."""
    status: ApplicationStatus | None = None
    cover_letter: str | None = None
    notes: str | None = None


class ApplicationResponse(ApplicationBase):
    """Application response schema."""
    id: int
    user_id: int
    job_id: int
    matched_score: int | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
