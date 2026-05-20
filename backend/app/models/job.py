"""Job model."""

from sqlalchemy import Column, Integer, String, Text, Float, Boolean, Index, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import BaseModel


class Job(BaseModel):
    """Job posting entity."""

    __tablename__ = "jobs"
    __table_args__ = (
        Index("idx_jobs_linkedin_id", "linkedin_id", unique=True),
        Index("idx_jobs_user_id", "user_id"),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    linkedin_id = Column(String(255), unique=True, nullable=False)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String(255), nullable=True)
    salary_min = Column(Float, nullable=True)
    salary_max = Column(Float, nullable=True)
    url = Column(String(1000), nullable=True)
    requirements = Column(Text, nullable=True)
    is_saved = Column(Boolean, default=False, nullable=False)

    # Relationships
    user = relationship("User", foreign_keys=[user_id])

    def __repr__(self) -> str:
        return f"<Job(id={self.id}, title={self.title}, company={self.company})>"
