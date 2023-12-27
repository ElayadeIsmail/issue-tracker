from fastapi import APIRouter
from app.schemas.users import UserOut,CreateUser
from app.repositories.users import create_user


router = APIRouter()

@router.post("/login")
async def login():
    return {"message":"Login Endpoint"}


@router.post("/register",status_code=201)
async def register(user_input:CreateUser):
    user = await create_user(user_input)
    print(user)
    userResponse = UserOut(email=user.email,id=user.id,full_name=user.full_name)
    return {"user":userResponse}