from fastapi import HTTPException,status
from app.database.database import engine
from app.schemas.users import CreateUser,FindUser
from sqlmodel import select,Session
from app.models.users import User
from app.core.security import get_password_hash

async def create_user(user_args:CreateUser):
    with Session(engine) as session:
        find_with_email_statement = select(User).where(User.email == user_args.email)
        user_with_email = session.exec(find_with_email_statement).first()
        if user_with_email is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email Already Exists")
        hashed_password = get_password_hash(user_args.password)
        user = User(email=user_args.email,full_name=user_args.full_name,hashed_password=hashed_password,is_active=True,is_superuser=False)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
            
            
async def find_user(args:FindUser):
    with Session(engine) as session: 
        if args.id:
            statement = select(User).where(User.id == args.id) 
        else:
            statement = select(User).where(User.email == args.email) 
        user = session.exec(statement).first()
        return user

