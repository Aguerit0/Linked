"""User routes."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.user_service import UserService
from app.schemas.user import UserUpdate, UserResponse
from app.core.exceptions import AppException
from app.api.v1.dependencies import CurrentUser

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
async def get_profile(current_user: CurrentUser, db: Session = Depends(get_db)):
    """Get current user profile."""
    try:
        user_service = UserService(db)
        return user_service.get_user(current_user["user_id"])
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.put("/me", response_model=UserResponse)
async def update_profile(
    user_data: UserUpdate, current_user: CurrentUser, db: Session = Depends(get_db)
):
    """Update current user profile."""
    try:
        user_service = UserService(db)
        return user_service.update_user(current_user["user_id"], user_data)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.delete("/me")
async def delete_profile(current_user: CurrentUser, db: Session = Depends(get_db)):
    """Delete current user account."""
    try:
        user_service = UserService(db)
        user_service.delete_user(current_user["user_id"])
        return {"message": "User account deleted"}
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
