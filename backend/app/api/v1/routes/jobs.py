"""Job routes."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.job_service import JobService
from app.schemas.job import JobCreate, JobUpdate, JobResponse
from app.core.exceptions import AppException
from app.api.v1.dependencies import CurrentUser
from typing import List

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.post("", response_model=JobResponse)
async def create_job(
    job_data: JobCreate, current_user: CurrentUser, db: Session = Depends(get_db)
):
    """Create a new job."""
    try:
        job_service = JobService(db)
        return job_service.create_job(current_user["user_id"], job_data)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/{job_id}", response_model=JobResponse)
async def get_job(job_id: int, db: Session = Depends(get_db)):
    """Get job by ID."""
    try:
        job_service = JobService(db)
        return job_service.get_job(job_id)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("", response_model=List[JobResponse])
async def list_jobs(
    current_user: CurrentUser,
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
):
    """List all jobs for current user."""
    try:
        job_service = JobService(db)
        return job_service.get_user_jobs(current_user["user_id"], skip, limit)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/saved", response_model=List[JobResponse])
async def list_saved_jobs(
    current_user: CurrentUser,
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
):
    """List saved jobs for current user."""
    try:
        job_service = JobService(db)
        return job_service.get_saved_jobs(current_user["user_id"], skip, limit)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.put("/{job_id}", response_model=JobResponse)
async def update_job(
    job_id: int, job_data: JobUpdate, db: Session = Depends(get_db)
):
    """Update a job."""
    try:
        job_service = JobService(db)
        return job_service.update_job(job_id, job_data)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.delete("/{job_id}")
async def delete_job(job_id: int, db: Session = Depends(get_db)):
    """Delete a job."""
    try:
        job_service = JobService(db)
        job_service.delete_job(job_id)
        return {"message": "Job deleted"}
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
