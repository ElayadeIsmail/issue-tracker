from sqlmodel import Relationship, SQLModel,Field
from typing import Optional,List

from app.models.projects_to_users import ProjectUserLink
    
# Database model, database table inferred from class name
class User(SQLModel, table=True):
    __tablename__="users"
    
    id:Optional[int] = Field(primary_key=True,default=None)
    username:str =  Field(unique=True, index=True);
    email:str =  Field(unique=True, index=True);
    full_name:str
    is_active: bool = True
    is_superuser: bool = False
    hashed_password: str
    
    created_projects: List["Project"] = Relationship(back_populates="admin")
    collaborator_projects: List["Project"] = Relationship(back_populates="collaborators",link_model=ProjectUserLink)
    

    
    