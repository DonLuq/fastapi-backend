import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import File, HTTPException, UploadFile

from src.core.config import settings

ROOT_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = ROOT_DIR / settings.upload_dir
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class FileService:
    @staticmethod
    def upload_file(file: UploadFile) -> dict:
        """Upload file with business logic"""
        # Validation
        if file.size and file.size > 10_000_000:  # 10MB
            raise ValueError("File too large")

        return FileService.save_file_local(file)

    @staticmethod
    def list_files() -> dict:
        """List uploaded files"""
        files = [
            {"filename": p.name, "size": p.stat().st_size}
            for p in UPLOAD_DIR.iterdir()
            if p.is_file()
        ]
        return {"files": files}

    @staticmethod
    def generate_target_name(original: str) -> str:
        return f"{uuid4().hex}{Path(original).suffix}"

    @staticmethod
    def save_file_local(file: UploadFile = File(...)) -> dict:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No filename provided")
        target_name = FileService.generate_target_name(file.filename)
        target_path = UPLOAD_DIR / target_name
        with target_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"filename": target_name, "url": f"{target_path}"}
