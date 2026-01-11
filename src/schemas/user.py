from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, EmailStr


# Base schema
class UserBase(BaseModel):
    email: EmailStr


# Schema for creating user
class UserCreate(UserBase):
    password: str


# Schema for user response
class UserResponse(UserBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# Schema for user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for JWT token
class Token(BaseModel):
    access_token: str
    token_type: str


# File schema
class FileResponse(BaseModel):
    id: int
    filename: str
    original_name: str
    file_size: int
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)


# User with files
class UserWithFiles(UserResponse):
    files: List[FileResponse] = []
