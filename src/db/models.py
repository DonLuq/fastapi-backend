from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Modern SQLAlchemy 2.0 declarative base"""

    pass


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # files = relationship("File", back_populates="owner")


class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    original_name = Column(String, nullable=False)
    file_size = Column(Integer)
    content_type = Column(String)
    file_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.now)

    # Foreign key to user
    # user_id = Column(Integer, ForeignKey("users.id"))
    # owner = relationship("User", back_populates="files")


class StockData(Base):
    __tablename__ = "stock_data"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True, nullable=False)
    price = Column(String)
    change = Column(String)
    timestamp = Column(DateTime, default=datetime.now)
    # user_id = Column(Integer, ForeignKey("users.id"))
