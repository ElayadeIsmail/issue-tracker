from sqlmodel import SQLModel,Field
from pydantic import EmailStr
from typing import Optional

class CreateUser(SQLModel):
    email:EmailStr;
    username:str = Field(min_length=3,max_length=100);
    full_name:str = Field(min_length=3,max_length=250)
    password: str = Field(min_length=8,max_length=100)
    
class UserOut(SQLModel):
    id:int;
    username:str;
    email:str
    full_name:str
    
class FindUser(SQLModel):
    id: int | None = None;
    username: str | None = None;
    email:EmailStr|None = None 
    