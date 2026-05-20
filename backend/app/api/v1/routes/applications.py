"""Application routes."""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.application_service import ApplicationService
from app.schemas.application import ApplicationCreate, ApplicationUpdate, ApplicationResponse, ApplicationStatus
from app.core.exceptions import AppException
from app.api.v1.dependencies import CurrentUser
from typing import List

router = APIRouter(prefix="/applications", tags=["applications"])


@router.post("", response_model=ApplicationResponse)
async def create_application(
    app_data: ApplicationCreate, current_user: CurrentUser, db: Session = Depends(get_db)
):
    """Create a new application."""
    try:
        app_service = ApplicationService(db)
        return app_service.create_application(current_user["user_id"], app_data)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/{app_id}", response_model=ApplicationResponse)
async def get_application(app_id: int, db: Session = Depends(get_db)):
    """Get application by ID."""
    try:
        app_service = ApplicationService(db)
        return app_service.get_application(app_id)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("", response_model=List[ApplicationResponse])
async def list_applications(
    current_user: CurrentUser,
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
):
    """List all applications for current user."""
    try:
        app_service = ApplicationService(db)
        return app_service.get_user_applications(current_user["user_id"], skip, limit)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.get("/status/{status}", response_model=List[ApplicationResponse])
async def list_applications_by_status(
    status: ApplicationStatus,
    current_user: CurrentUser,
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
):
    """List applications by status."""
    try:
        app_service = ApplicationService(db)
        return app_service.get_applications_by_status(
            current_user["user_id"], status, skip, limit
        )
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.put("/{app_id}", response_model=ApplicationResponse)
async def update_application(
    app_id: int, app_data: ApplicationUpdate, db: Session = Depends(get_db)
):
    """Update an application."""
    try:
        app_service = ApplicationService(db)
        return app_service.update_application(app_id, app_data)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.delete("/{app_id}")
async def delete_application(app_id: int, db: Session = Depends(get_db)):
    """Delete an application."""
    try:
        app_service = ApplicationService(db)
        app_service.delete_application(app_id)
        return {"message": "Application deleted"}
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
