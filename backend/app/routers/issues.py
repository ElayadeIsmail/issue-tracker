

from typing import Annotated,List
from fastapi import APIRouter, Depends,status
from app.auth.auth import get_current_user
from app.repositories.issues import get_project_issues as db_get_project_issues,create_issue as db_create_issue,update_issue as db_update_issue ,delete_issue as db_delete_issue

from app.models.users import User
from app.schemas.issues import IssueIn, IssueOut


router = APIRouter()

@router.get("/{project_id}/issues",response_model=List[IssueOut])
async def get_project_issues(project_id:int,current_user: Annotated[User, Depends(get_current_user)]):
    result = await db_get_project_issues(project_id,current_user)
    return result

@router.post("/{project_id}/issues",response_model=IssueOut,status_code=status.HTTP_201_CREATED)
async def create_project_issue(project_id:int,issue_args:IssueIn,current_user: Annotated[User, Depends(get_current_user)]):
    issue = await db_create_issue(project_id,issue_args,current_user)
    return issue

@router.put("/{project_id}/issues/{issue_id}",response_model=IssueOut)
async def update_project_issue(project_id:int,issue_id:int,issue_args:IssueIn,current_user: Annotated[User, Depends(get_current_user)]):
    issue = await db_update_issue(project_id,issue_id,issue_args,current_user)
    return issue

@router.delete("/{project_id}/issues/{issue_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_project_issue(project_id:int,issue_id:int,current_user: Annotated[User, Depends(get_current_user)]):
    await db_delete_issue(project_id,issue_id,current_user)
    return 