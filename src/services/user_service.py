from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.db.models import User
from src.schemas.user import UserCreate, UserResponse
from src.utils.password import hash_password, verify_password


class UserService:
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> UserResponse:
        # Check if user exists
        if db.query(User).filter(User.email == user_data.email).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )

        # Hash password
        hashed_password = hash_password(user_data.password)

        # Create user
        db_user = User(email=user_data.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return UserResponse.model_validate(db_user)

    @staticmethod
    def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
        user: Optional[User] = db.query(User).filter(User.email == email).first()
        if not user or not verify_password(password, str(user.hashed_password)):
            return None
        return user
