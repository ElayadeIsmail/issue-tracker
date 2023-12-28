from fastapi import HTTPException,status
from app.database.database import engine
from app.schemas.users import CreateUser,FindUser
from sqlmodel import select,Session,or_
from app.models.users import User
from app.core.security import get_password_hash

async def create_user(user_args:CreateUser):
    with Session(engine) as session:
        existing_user_statement = select(User).where(or_(User.email == user_args.email,User.username == user_args.username))
        existing_user = session.exec(existing_user_statement).first()
        if existing_user:
            if existing_user.username == user_args.username:
                field = "username"
            else:
                field = "email"
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail= f"{field} already exists")
        hashed_password = get_password_hash(user_args.password)
        user = User(email=user_args.email,username=user_args.username,full_name=user_args.full_name,hashed_password=hashed_password,is_active=True,is_superuser=False)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
            
            
async def find_user(args:FindUser):
    with Session(engine) as session: 
        if args.id:
            statement = select(User).where(User.id == args.id) 
        elif args.email:
            statement = select(User).where(User.email == args.email) 
        else :
            statement = select(User).where(User.username == args.username)
        user = session.exec(statement).first()
        return user

