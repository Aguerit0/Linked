"""Authentication routes."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth_service import AuthService
from app.schemas.user import UserCreate, TokenResponse
from app.core.exceptions import AppException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    """Login request model."""
    email: str
    password: str


class RefreshTokenRequest(BaseModel):
    """Refresh token request model."""
    refresh_token: str


@router.post("/register", response_model=dict)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user."""
    try:
        auth_service = AuthService(db)
        user = auth_service.register(user_data)
        return {
            "id": user.id,
            "email": user.email,
            "username": user.username,
            "message": "User registered successfully",
        }
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/login", response_model=TokenResponse)
async def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    """Login user and return tokens."""
    try:
        auth_service = AuthService(db)
        return auth_service.login(credentials.email, credentials.password)
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/refresh")
async def refresh_token(req: RefreshTokenRequest, db: Session = Depends(get_db)):
    """Refresh access token."""
    try:
        auth_service = AuthService(db)
        access_token = auth_service.refresh_access_token(req.refresh_token)
        return {"access_token": access_token, "token_type": "bearer"}
    except AppException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
