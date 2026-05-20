"""Job service."""

from typing import List
from sqlalchemy.orm import Session
from app.repositories.job_repository import JobRepository
from app.schemas.job import JobCreate, JobUpdate, JobResponse
from app.core.exceptions import NotFoundException, ConflictException


class JobService:
    """Service for job operations."""

    def __init__(self, db: Session):
        self.db = db
        self.job_repo = JobRepository(db)

    def create_job(self, user_id: int, job_data: JobCreate) -> JobResponse:
        """Create a new job."""
        if self.job_repo.linkedin_id_exists(job_data.linkedin_id):
            raise ConflictException("This job already exists")

        job = self.job_repo.create({
            "user_id": user_id,
            "linkedin_id": job_data.linkedin_id,
            "title": job_data.title,
            "company": job_data.company,
            "description": job_data.description,
            "location": job_data.location,
            "salary_min": job_data.salary_min,
            "salary_max": job_data.salary_max,
            "url": job_data.url,
            "requirements": job_data.requirements,
        })
        return JobResponse.model_validate(job)

    def get_job(self, job_id: int) -> JobResponse:
        """Get job by ID."""
        job = self.job_repo.get(job_id)
        if not job:
            raise NotFoundException("Job not found")
        return JobResponse.model_validate(job)

    def get_user_jobs(self, user_id: int, skip: int = 0, limit: int = 100) -> List[JobResponse]:
        """Get all jobs for a user."""
        jobs = self.job_repo.get_by_user(user_id, skip, limit)
        return [JobResponse.model_validate(job) for job in jobs]

    def get_saved_jobs(self, user_id: int, skip: int = 0, limit: int = 100) -> List[JobResponse]:
        """Get saved jobs for a user."""
        jobs = self.job_repo.get_saved_by_user(user_id, skip, limit)
        return [JobResponse.model_validate(job) for job in jobs]

    def update_job(self, job_id: int, job_data: JobUpdate) -> JobResponse:
        """Update job information."""
        job = self.job_repo.get(job_id)
        if not job:
            raise NotFoundException("Job not found")

        update_dict = {}
        if job_data.title:
            update_dict["title"] = job_data.title
        if job_data.company:
            update_dict["company"] = job_data.company
        if job_data.description is not None:
            update_dict["description"] = job_data.description
        if job_data.location is not None:
            update_dict["location"] = job_data.location
        if job_data.salary_min is not None:
            update_dict["salary_min"] = job_data.salary_min
        if job_data.salary_max is not None:
            update_dict["salary_max"] = job_data.salary_max
        if job_data.url is not None:
            update_dict["url"] = job_data.url
        if job_data.requirements is not None:
            update_dict["requirements"] = job_data.requirements
        if job_data.is_saved is not None:
            update_dict["is_saved"] = job_data.is_saved

        updated_job = self.job_repo.update(job_id, update_dict)
        return JobResponse.model_validate(updated_job)

    def delete_job(self, job_id: int) -> bool:
        """Delete a job."""
        return self.job_repo.delete(job_id)
