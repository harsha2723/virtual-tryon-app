from fastapi import APIRouter, HTTPException
from models import User, UserCreate

router = APIRouter()

@router.post("/register")
async def register_user(user: UserCreate):
    existing_user = await User.find_one(User.email == user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    new_user = User(**user.dict())
    await new_user.insert()
    return {"msg": "User registered successfully"}

@router.get("/profile/{email}")
async def get_profile(email: str):
    user = await User.find_one(User.email == email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
