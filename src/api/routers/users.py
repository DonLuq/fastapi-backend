from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.api.dependencies.api_key import verify_api_key
from src.db.session import get_db
from src.schemas.user import Token, UserCreate, UserLogin, UserResponse
from src.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/register", response_model=UserResponse)
def register_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    _: bool = Depends(verify_api_key),
):
    """Register a new user"""
    return UserService.create_user(db, user_data)


@router.post("/login", response_model=Token)
def login_user(login_data: UserLogin, db: Session = Depends(get_db)):
    """Login user and get JWT token"""
    user = UserService.authenticate_user(db, login_data.email, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    # Generate JWT token here
    return {"access_token": "jwt_token_here", "token_type": "bearer"}


# @router.get("/whoami", response_model=UserResponse)
# def get_current_user_info(
#     return current_user: User = Depends(get_current_user)
# placeholder for current user endpoint
