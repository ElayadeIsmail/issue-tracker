from typing import Optional
from fastapi import HTTPException,status

def not_found_error(message:Optional[str]="Resource Not Found"):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=message)

def bad_request_error(message:str):
    return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=message)

def unauthorized_request_error(message:Optional[str]="UNAUTHORIZED"):
    return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=message)