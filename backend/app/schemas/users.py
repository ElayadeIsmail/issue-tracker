from sqlmodel import SQLModel,Field
from pydantic import EmailStr

class CreateUser(SQLModel):
    email:EmailStr;
    full_name:str = Field(min_length=3,max_length=250)
    password: str = Field(min_length=8,max_length=100)
    
class UserOut(SQLModel):
    id:int;
    email:str
    full_name:str
    
class FindUser(SQLModel):
    id:int | None;
    email:EmailStr|None 