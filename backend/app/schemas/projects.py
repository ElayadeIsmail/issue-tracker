from typing import Optional,List
from sqlmodel import Field, SQLModel
from .users import UserOut


class CreateProject(SQLModel):
    name:str = Field(min_length=3,max_length=250)
    description:Optional[str]  =  Field(default=None);
    
    
class ProjectOut(SQLModel):
    id:Optional[int]
    name:str;
    description:Optional[str] 
    collaborators: List["UserOut"]
    admin_id: Optional[int] 
    admin:Optional["UserOut"]