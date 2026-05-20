"""Job repository."""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.job import Job
from app.repositories.base import BaseRepository


class JobRepository(BaseRepository[Job]):
    """Job repository for database operations."""

    def __init__(self, db: Session):
        super().__init__(db, Job)

    def get_by_linkedin_id(self, linkedin_id: str) -> Optional[Job]:
        """Get job by LinkedIn ID."""
        return self.db.query(Job).filter(Job.linkedin_id == linkedin_id).first()

    def get_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Job]:
        """Get jobs for a specific user."""
        return (
            self.db.query(Job)
            .filter(Job.user_id == user_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_saved_by_user(self, user_id: int, skip: int = 0, limit: int = 100) -> List[Job]:
        """Get saved jobs for a specific user."""
        return (
            self.db.query(Job)
            .filter(Job.user_id == user_id, Job.is_saved == True)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def linkedin_id_exists(self, linkedin_id: str) -> bool:
        """Check if LinkedIn ID already exists."""
        return (
            self.db.query(Job).filter(Job.linkedin_id == linkedin_id).first()
            is not None
        )
