import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.api.routers import router as api_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ROOT_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = ROOT_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")

app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/pics")
def read_pic():
    files = []
    for p in UPLOAD_DIR.iterdir():
        if p.is_file():
            files.append({"filename": p.name, "url": f"/uploads/{p.name}"})
    return {"files": files}


@app.post("/uploadfile/", status_code=201)
async def create_upload_file(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No filename provided")
    suffix = Path(file.filename).suffix
    target_name = f"{uuid4().hex}{suffix}"
    target_path = UPLOAD_DIR / target_name

    try:
        with target_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    finally:
        await file.close()

    return {"filename": target_name, "url": f"/uploads/{target_name}"}
