from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel,Field

from app.models.issues import IssuePriority, IssueStatus
from app.schemas.users import UserOut


class CreateIssue(SQLModel):
    name:str=Field(min_length=3)
    description:Optional[str]=Field(default=None)
    status:Optional[IssueStatus] = Field(default=IssueStatus.not_started)
    priority:Optional[IssuePriority] =Field(default=None)
    due_date: Optional[datetime] = Field(default=None)
    assignee_id: Optional[int] = Field(default=None)
    
    
class IssueOut(SQLModel):
    id:int
    name:str
    description:Optional[str]
    status:Optional[IssueStatus]
    priority:Optional[IssuePriority]
    due_date: Optional[datetime]
    assignee_id: Optional[int]
    assignee:Optional[UserOut]
    