"""Application model."""

from sqlalchemy import Column, Integer, String, Text, Boolean, Index, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum
from app.models.base import BaseModel


class ApplicationStatus(str, PyEnum):
    """Application status enum."""
    PENDING = "pending"
    APPLIED = "applied"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    WITHDRAWN = "withdrawn"


class Application(BaseModel):
    """Job application entity."""

    __tablename__ = "applications"
    __table_args__ = (
        Index("idx_applications_user_job", "user_id", "job_id"),
        Index("idx_applications_user_id", "user_id"),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False, index=True)
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.PENDING, nullable=False)
    cover_letter = Column(Text, nullable=True)
    matched_score = Column(Integer, nullable=True)  # 0-100
    notes = Column(Text, nullable=True)

    # Relationships
    user = relationship("User", foreign_keys=[user_id])
    job = relationship("Job", foreign_keys=[job_id])

    def __repr__(self) -> str:
        return f"<Application(id={self.id}, user_id={self.user_id}, job_id={self.job_id}, status={self.status})>"
