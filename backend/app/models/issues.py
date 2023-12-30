from datetime import datetime
from typing import Optional,TYPE_CHECKING
from sqlmodel import Field,Relationship
from .base import BaseModel
from enum import Enum

# to avoid circular imports
if TYPE_CHECKING:
    from .users import User
    from .projects import Project

class Priority(Enum):
    Hight = 3
    Medium = 2
    Low = 1

class Status(str,Enum):
    done = "done"
    in_progress = "in_progress"
    not_started = "not_started"


class Issue(BaseModel,table=True):
    __tablename__="issues"
    
    id:Optional[int] = Field(default=None,primary_key=True)
    name:str=Field(min_length=3)
    description:Optional[str]=Field(default=None)
    status:Optional[Status] = Field(default=Status.not_started)
    priority:Optional[Priority] =Field(default=None)
    due_date: Optional[datetime] = Field(default=None)
    project_id: Optional[int] = Field(default=None, foreign_key="projects.id")
    project:Optional["Project"] = Relationship(back_populates="issues")
    
    assignee_id: Optional[int] = Field(default=None, foreign_key="users.id")
    assignee:Optional["User"] = Relationship(back_populates="assigned_issues")