from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from app.core.settings import settings
from app.schemas.users import UserOut,CreateUser
from app.models.token import Token
from app.repositories.users import create_user
from app.core.security import create_access_token
from app.auth.auth import authenticate_user


router = APIRouter()

@router.post("/login/access_token",response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = await authenticate_user(form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid Credentials",headers={"WWW-Authenticate": "Bearer"},)
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username,"id":user.id}, expires_delta=access_token_expires
    )
    return {"access_token":access_token,"token_type":"bearer"}


@router.post("/register",status_code=201)
async def register(user_input:CreateUser):
    user = await create_user(user_input)
    userResponse = UserOut(email=user.email,username=user.username,id=user.id,full_name=user.full_name)
    return {"user":userResponse}