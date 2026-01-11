from fastapi import APIRouter

from src.core.config import settings

router = APIRouter(prefix="/system", tags=["system"])


@router.get("/health")
def health_check():
    """System health check"""
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "debug_mode": settings.debug_mode,
    }


@router.get("/info")
def app_info():
    """Application information"""
    return {
        "name": settings.app_name,
        "version": "1.0.0",
        "storage_backend": settings.storage_backend,
    }
