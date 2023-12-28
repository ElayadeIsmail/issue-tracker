from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,List
from app.models.projects_to_users import ProjectUserLink

from app.models.users import User

    
    
# Database model, database table inferred from class name
class Project(SQLModel, table=True):
    __tablename__="projects"
    
    id:Optional[int] = Field(primary_key=True,default=None)
    name:str;
    description:Optional[str]  =  Field(default=None);
    
    collaborators: List["User"] = Relationship(back_populates="collaborator_projects", link_model=ProjectUserLink)
    
    admin_id: Optional[int] = Field(default=None, foreign_key="users.id")
    admin:Optional[User] = Relationship(back_populates="created_projects")
    

 
    

    
    