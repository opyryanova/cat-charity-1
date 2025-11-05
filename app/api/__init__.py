from fastapi import APIRouter

from app.api.endpoints.charity_project import router as project_router
from app.api.endpoints.donation import router as donation_router


api_router = APIRouter()
api_router.include_router(project_router)
api_router.include_router(donation_router)
