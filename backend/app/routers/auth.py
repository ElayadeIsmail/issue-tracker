from fastapi import APIRouter


router = APIRouter()

@router.post("/login")
async def login():
    return {"message":"Login Endpoint"}


@router.post("/register")
async def register():
    return {"message":"Login Endpoint"}