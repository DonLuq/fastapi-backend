from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from . import files, health, stocks, users

aggregate_router = APIRouter(prefix="/api/v1")

aggregate_router.include_router(health.router)
aggregate_router.include_router(files.router)
aggregate_router.include_router(stocks.router)
aggregate_router.include_router(users.router)


@aggregate_router.get("/", include_in_schema=False)
def redirect_to_docs():
    return RedirectResponse(url="/docs")
