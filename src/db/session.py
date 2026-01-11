from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import settings


# Construct database URL
def get_database_url() -> str:
    if settings.storage_database_url:
        if settings.storage_database_user and settings.storage_database_password:
            return f"postgresql://{settings.storage_database_user}:{settings.storage_database_password}@{settings.storage_database_url}"
        return settings.storage_database_url
    return "sqlite:///./app.db"  # Fallback to SQLite


DATABASE_URL = get_database_url()

# Create engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)

# Session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency for getting database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
