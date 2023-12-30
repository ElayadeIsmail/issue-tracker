from typing import Annotated
from fastapi import APIRouter, Depends,status
from app.auth.auth import get_current_user
from app.models.users import User
from app.repositories.projects import create_project as db_create_project,get_current_user_projects as db_get_current_user_projects

from app.schemas.projects import CreateProject

router = APIRouter()

@router.post("/",name="Create New Project",status_code=status.HTTP_201_CREATED)
async def create_project(create_project_args:CreateProject,current_user: Annotated[User, Depends(get_current_user)]):
    project = await db_create_project(project_args=create_project_args,admin=current_user)
    return project

@router.get("/",name="Get Current User Projects")
async def get_current_user_projects(current_user: Annotated[User, Depends(get_current_user)]):
    projects = await db_get_current_user_projects(current_user)
    return projects