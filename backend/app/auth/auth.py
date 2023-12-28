from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verify_password,decode_access_token
from app.schemas.users import FindUser
from app.repositories.users import find_user
from fastapi import Depends, HTTPException,status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def authenticate_user(email:str,password:str):
    user = await find_user(FindUser(email=email))
    if user is None:
        return False;
    if not verify_password(user.hashed_password,password):
        return False
    return user

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    token_data = decode_access_token(token=token)
    if token_data is None:
        raise credentials_exception
    user = await find_user(FindUser(email=token_data.email))
    if user is None:
        raise credentials_exception
    return user