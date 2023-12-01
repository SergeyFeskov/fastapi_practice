from fastapi import APIRouter

from api.handlers import user_router

main_api_router = APIRouter()

main_api_router.include_router(user_router, prefix="/users", tags=["user"])
