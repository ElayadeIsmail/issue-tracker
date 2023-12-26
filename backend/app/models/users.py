from sqlmodel import SQLModel,Field
from typing import Optional
    
# Database model, database table inferred from class name
class User(SQLModel, table=True):
    __tablename__="users"
    
    id:Optional[int] = Field(primary_key=True,default=None)
    email:str =  Field(unique=True, index=True);
    full_name:str
    is_active: bool = True
    is_superuser: bool = False
    hashed_password: str
    
    