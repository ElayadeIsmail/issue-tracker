from typing import Optional
from fastapi import HTTPException,status

def not_found_error(message:Optional[str]="Resource Not Found"):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=message)