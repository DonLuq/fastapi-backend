from fastapi import APIRouter, Depends, UploadFile

from src.api.dependencies.api_key import verify_api_key
from src.services.file_service import FileService

router = APIRouter(prefix="/files", tags=["files"])


@router.post("/upload", status_code=201)
def upload_file(file: UploadFile, _: bool = Depends(verify_api_key)):
    """Upload a file to storage"""
    return FileService.upload_file(file)


@router.get("/list")
def list_files(_: bool = Depends(verify_api_key)):
    """List all uploaded files"""
    return FileService.list_files()
