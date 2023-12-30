

from typing import Annotated
from fastapi import APIRouter, Depends
from app.auth.auth import get_current_user
from app.repositories.issues import get_project_issues as db_get_project_issues

from app.models.users import User


router = APIRouter()

@router.get("/{project_id}/issues")
async def get_project_issues(project_id:int,current_user: Annotated[User, Depends(get_current_user)]):
    result = await db_get_project_issues(project_id,current_user)
    return result