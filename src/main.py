from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from src.api.routers import router as api_router
from src.core.config import settings
from src.utils.storage import save_file_local

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug_mode,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


@app.post("/uploadfile/", status_code=201)
def save_file(file: UploadFile) -> dict:
    # if STORAGE_BACKEND == "s3":
    # return save_file_s3_placeholder(file, target_name)
    return save_file_local(file)


@app.get("/content")
def read_pic():
    from src.utils.storage import UPLOAD_DIR

    files = [
        {"filename": p.name, "url": f"{UPLOAD_DIR}/{p.name}"}
        for p in UPLOAD_DIR.iterdir()
        if p.is_file()
    ]
    return {"files": files}
