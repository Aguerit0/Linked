"""Dependency injection for API routes."""

from typing import Optional, Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.auth_service import AuthService
from app.core.exceptions import AuthenticationException

security = HTTPBearer()


async def get_current_user(
    credentials: Annotated[HTTPAuthCredentials, Depends(security)],
    db: Session = Depends(get_db),
) -> dict:
    """Get current user from JWT token."""
    token = credentials.credentials
    auth_service = AuthService(db)
    
    payload = auth_service.verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    
    return {"user_id": int(user_id), "email": payload.get("email")}


CurrentUser = Annotated[dict, Depends(get_current_user)]
