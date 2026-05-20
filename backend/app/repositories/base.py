"""Base repository with common CRUD operations."""

from typing import Generic, TypeVar, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """Base repository for CRUD operations."""

    def __init__(self, db: Session, model: type[T]):
        self.db = db
        self.model = model

    def create(self, obj_in: dict) -> T:
        """Create a new object."""
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def get(self, id: int) -> Optional[T]:
        """Get object by ID."""
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[T]:
        """Get all objects with pagination."""
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def update(self, id: int, obj_in: dict) -> Optional[T]:
        """Update an object."""
        db_obj = self.get(id)
        if db_obj:
            for key, value in obj_in.items():
                if value is not None:
                    setattr(db_obj, key, value)
            self.db.commit()
            self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> bool:
        """Delete an object."""
        db_obj = self.get(id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        return False
