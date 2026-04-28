from fastapi import APIRouter
from app.api.v1 import users, tasks

api_v1_router = APIRouter(prefix="/api/v1")
api_v1_router.include_router(users.router)
api_v1_router.include_router(tasks.router)
