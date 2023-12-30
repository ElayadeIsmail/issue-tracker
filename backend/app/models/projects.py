from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,List,TYPE_CHECKING
from app.models.projects_to_users import ProjectUserLink

# to avoid circular imports
if TYPE_CHECKING:
    from .users import User
    from .issues import Issue 
    
# Database model, database table inferred from class name
class Project(SQLModel, table=True):
    __tablename__="projects"
    
    id:Optional[int] = Field(primary_key=True,default=None)
    name:str;
    description:Optional[str]  =  Field(default=None);
    
    collaborators: List["User"] = Relationship(back_populates="collaborator_projects", link_model=ProjectUserLink)
    
    issues: List["Issue"] = Relationship(back_populates="project")
    
    admin_id: Optional[int] = Field(default=None, foreign_key="users.id")
    admin:Optional["User"] = Relationship(back_populates="created_projects")
    

 
    

    
    