import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import File, HTTPException, UploadFile

ROOT_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = ROOT_DIR / ".tmp"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def generate_target_name(original: str) -> str:
    return f"{uuid4().hex}{Path(original).suffix}"


def save_file_local(file: UploadFile = File(...)) -> dict:
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")
    target_name = generate_target_name(file.filename)
    target_path = UPLOAD_DIR / target_name
    with target_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": target_name, "url": f"/.tmp/{target_name}"}


def save_file_s3_placeholder(file: UploadFile, target_name: str) -> dict:
    # Placeholder for S3
    raise HTTPException(status_code=501, detail="S3 storage not configured")
