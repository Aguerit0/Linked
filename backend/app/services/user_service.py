"""User service."""

from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserUpdate, UserResponse
from app.core.security import hash_password
from app.core.exceptions import NotFoundException, ConflictException


class UserService:
    """Service for user operations."""

    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)

    def get_user(self, user_id: int) -> UserResponse:
        """Get user by ID."""
        user = self.user_repo.get(user_id)
        if not user:
            raise NotFoundException("User not found")
        return UserResponse.model_validate(user)

    def update_user(self, user_id: int, user_data: UserUpdate) -> UserResponse:
        """Update user information."""
        user = self.user_repo.get(user_id)
        if not user:
            raise NotFoundException("User not found")

        # Check for conflicts
        if user_data.email and user_data.email != user.email:
            if self.user_repo.email_exists(user_data.email):
                raise ConflictException("Email already in use")

        if user_data.username and user_data.username != user.username:
            if self.user_repo.username_exists(user_data.username):
                raise ConflictException("Username already taken")

        # Prepare update dict
        update_dict = {}
        if user_data.email:
            update_dict["email"] = user_data.email
        if user_data.username:
            update_dict["username"] = user_data.username
        if user_data.full_name:
            update_dict["full_name"] = user_data.full_name
        if user_data.password:
            update_dict["hashed_password"] = hash_password(user_data.password)

        updated_user = self.user_repo.update(user_id, update_dict)
        return UserResponse.model_validate(updated_user)

    def delete_user(self, user_id: int) -> bool:
        """Delete user (soft delete by deactivating)."""
        user = self.user_repo.get(user_id)
        if not user:
            raise NotFoundException("User not found")
        
        return self.user_repo.update(user_id, {"is_active": False}) is not None
