"""Application repository."""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.application import Application, ApplicationStatus
from app.repositories.base import BaseRepository


class ApplicationRepository(BaseRepository[Application]):
    """Application repository for database operations."""

    def __init__(self, db: Session):
        super().__init__(db, Application)

    def get_by_user_and_job(self, user_id: int, job_id: int) -> Optional[Application]:
        """Get application by user and job."""
        return (
            self.db.query(Application)
            .filter(Application.user_id == user_id, Application.job_id == job_id)
            .first()
        )

    def get_by_user(
        self, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[Application]:
        """Get applications for a specific user."""
        return (
            self.db.query(Application)
            .filter(Application.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_status(
        self, user_id: int, status: ApplicationStatus, skip: int = 0, limit: int = 100
    ) -> List[Application]:
        """Get applications by status for a specific user."""
        return (
            self.db.query(Application)
            .filter(Application.user_id == user_id, Application.status == status)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def user_already_applied(self, user_id: int, job_id: int) -> bool:
        """Check if user already applied to this job."""
        return (
            self.db.query(Application)
            .filter(Application.user_id == user_id, Application.job_id == job_id)
            .first()
            is not None
        )
