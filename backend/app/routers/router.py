from fastapi import APIRouter
from . import auth,projects


api_router = APIRouter()

api_router.include_router(auth.router,tags=["auth"])
api_router.include_router(projects.router,prefix="/projects",tags=["projects"])