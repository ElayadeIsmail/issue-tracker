from fastapi import APIRouter
from . import auth,projects,issues


api_router = APIRouter()

api_router.include_router(auth.router,tags=["auth"])
api_router.include_router(projects.router,prefix="/projects",tags=["projects"])
api_router.include_router(issues.router,prefix="/projects",tags=["Issues"])