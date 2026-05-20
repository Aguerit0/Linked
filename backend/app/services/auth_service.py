"""Authentication service."""

from typing import Optional, Tuple
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password, create_access_token, create_refresh_token, decode_token
from app.core.exceptions import AuthenticationException, ConflictException
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, TokenResponse
from app.models.user import User


class AuthService:
    """Service for authentication operations."""

    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def register(self, user_data: UserCreate) -> User:
        """Register a new user."""
        if self.user_repo.email_exists(user_data.email):
            raise ConflictException("Email already registered")
        
        if self.user_repo.username_exists(user_data.username):
            raise ConflictException("Username already taken")

        hashed_password = hash_password(user_data.password)
        
        user = self.user_repo.create({
            "email": user_data.email,
            "username": user_data.username,
            "full_name": user_data.full_name,
            "hashed_password": hashed_password,
        })
        
        return user

    def login(self, email: str, password: str) -> TokenResponse:
        """Login user and return tokens."""
        user = self.user_repo.get_by_email(email)
        
        if not user or not verify_password(password, user.hashed_password):
            raise AuthenticationException("Invalid email or password")
        
        if not user.is_active:
            raise AuthenticationException("User account is disabled")

        access_token = create_access_token({"sub": str(user.id), "email": user.email})
        refresh_token = create_refresh_token({"sub": str(user.id)})
        
        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    def refresh_access_token(self, refresh_token: str) -> str:
        """Generate new access token from refresh token."""
        payload = decode_token(refresh_token)
        
        if not payload or payload.get("type") != "refresh":
            raise AuthenticationException("Invalid refresh token")
        
        user_id = payload.get("sub")
        user = self.user_repo.get(int(user_id))
        
        if not user or not user.is_active:
            raise AuthenticationException("User not found or disabled")
        
        return create_access_token({"sub": str(user.id), "email": user.email})

    def verify_token(self, token: str) -> Optional[dict]:
        """Verify token and return payload."""
        payload = decode_token(token)
        
        if not payload or payload.get("type") != "access":
            return None
        
        return payload
