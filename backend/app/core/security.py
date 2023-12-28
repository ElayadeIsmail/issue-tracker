from passlib.context import CryptContext
from datetime import timedelta,datetime
from jose import JWTError, jwt

from app.core import settings
from app.models.token import TokenData

ALGORITHM = "HS256"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password:str, hashed_password:str)->bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def create_access_token(data:dict,expires_delta:timedelta | None= None):
    to_encode = data.copy();
    if expires_delta:
        expire = datetime.utcnow()+expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire}) 
    encoded_jwt = jwt.encode(to_encode,key=settings.SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token:str)->TokenData | None:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise None
        token_data = TokenData(email==email)
    except JWTError:
        return None
    return token_data