

from typing import Annotated,List
from fastapi import APIRouter, Depends
from app.auth.auth import get_current_user
from app.repositories.issues import get_project_issues as db_get_project_issues,create_issue as db_create_issue

from app.models.users import User
from app.schemas.issues import CreateIssue, IssueOut


router = APIRouter()

@router.get("/{project_id}/issues",response_model=List[IssueOut])
async def get_project_issues(project_id:int,current_user: Annotated[User, Depends(get_current_user)]):
    result = await db_get_project_issues(project_id,current_user)
    return result

@router.post("/{project_id}/issues",response_model=IssueOut)
async def get_project_issues(project_id:int,issue_args:CreateIssue,current_user: Annotated[User, Depends(get_current_user)]):
    issue = await db_create_issue(project_id,issue_args,current_user)
    return issue