"""Application service."""

from typing import List
from sqlalchemy.orm import Session
from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.schemas.application import ApplicationCreate, ApplicationUpdate, ApplicationResponse
from app.models.application import ApplicationStatus
from app.core.exceptions import NotFoundException, ConflictException


class ApplicationService:
    """Service for job application operations."""

    def __init__(self, db: Session):
        self.db = db
        self.app_repo = ApplicationRepository(db)
        self.job_repo = JobRepository(db)

    def create_application(self, user_id: int, app_data: ApplicationCreate) -> ApplicationResponse:
        """Create a new job application."""
        # Check if job exists
        job = self.job_repo.get(app_data.job_id)
        if not job:
            raise NotFoundException("Job not found")

        # Check if already applied
        if self.app_repo.user_already_applied(user_id, app_data.job_id):
            raise ConflictException("You have already applied to this job")

        application = self.app_repo.create({
            "user_id": user_id,
            "job_id": app_data.job_id,
            "status": ApplicationStatus.PENDING,
            "cover_letter": app_data.cover_letter,
        })
        return ApplicationResponse.model_validate(application)

    def get_application(self, app_id: int) -> ApplicationResponse:
        """Get application by ID."""
        app = self.app_repo.get(app_id)
        if not app:
            raise NotFoundException("Application not found")
        return ApplicationResponse.model_validate(app)

    def get_user_applications(
        self, user_id: int, skip: int = 0, limit: int = 100
    ) -> List[ApplicationResponse]:
        """Get all applications for a user."""
        apps = self.app_repo.get_by_user(user_id, skip, limit)
        return [ApplicationResponse.model_validate(app) for app in apps]

    def get_applications_by_status(
        self, user_id: int, status: ApplicationStatus, skip: int = 0, limit: int = 100
    ) -> List[ApplicationResponse]:
        """Get applications by status."""
        apps = self.app_repo.get_by_status(user_id, status, skip, limit)
        return [ApplicationResponse.model_validate(app) for app in apps]

    def update_application(
        self, app_id: int, app_data: ApplicationUpdate
    ) -> ApplicationResponse:
        """Update application."""
        app = self.app_repo.get(app_id)
        if not app:
            raise NotFoundException("Application not found")

        update_dict = {}
        if app_data.status:
            update_dict["status"] = app_data.status
        if app_data.cover_letter is not None:
            update_dict["cover_letter"] = app_data.cover_letter
        if app_data.notes is not None:
            update_dict["notes"] = app_data.notes

        updated_app = self.app_repo.update(app_id, update_dict)
        return ApplicationResponse.model_validate(updated_app)

    def delete_application(self, app_id: int) -> bool:
        """Delete application."""
        return self.app_repo.delete(app_id)
